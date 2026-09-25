"""The retry/refresh httpx transport wrapped around the real one. Centralizes the three
contract-driven behaviours:

* **401** → recover the token (rotation or re-mint, via the TokenManager) and retry ONCE,
  any method — a 401 means the request was rejected before processing.
* **429** → honour ``X-RateLimit-Reset`` (NOT ``Retry-After``) and retry, bounded.
* **5xx / network error** → retry IDEMPOTENT requests only (GET/HEAD/OPTIONS) with
  exponential backoff + jitter. Writes are never auto-retried.

Every attempt re-sends the same body bytes (``httpx.Request`` bodies are materialised
before dispatch), which is what made the equivalent Node fix necessary.
"""

from __future__ import annotations

import random as _random
import time
from collections.abc import Awaitable, Callable
from dataclasses import dataclass
from typing import Any

import httpx

from .token_manager import AsyncTokenManager, TokenManager

IDEMPOTENT_METHODS = frozenset({"GET", "HEAD", "OPTIONS"})
RATE_LIMIT_RESET_HEADER = "x-ratelimit-reset"


@dataclass(frozen=True, slots=True)
class RetryOptions:
    max_retries: int = 2
    base_delay_ms: float = 250
    max_delay_ms: float = 60_000


def rate_limit_wait_ms(reset_header: str | None, now_ms: float, max_delay_ms: float) -> float:
    """How long to wait for a 429. ``X-RateLimit-Reset`` may be an absolute epoch-seconds
    timestamp or a delta in seconds — values above ~1e9 are treated as absolute. Bounded so
    a misbehaving header can't hang the caller; absent/non-numeric → 1s."""
    fallback = min(1000.0, max_delay_ms)
    if reset_header is None:
        return fallback
    try:
        n = float(reset_header)
    except ValueError:
        return fallback
    wait = n * 1000 - now_ms if n > 1_000_000_000 else n * 1000
    return max(0.0, min(wait, max_delay_ms))


def backoff_ms(attempt: int, opts: RetryOptions, random_value: float) -> float:
    """``min(base·2ⁿ + base·2ⁿ·0.5·random, max)`` for retry attempt ``n`` (1-based)."""
    exp = opts.base_delay_ms * 2**attempt
    return min(exp + exp * 0.5 * random_value, opts.max_delay_ms)


def _now_ms() -> float:
    return time.time() * 1000


class _Policy:
    """Shared decision logic for the sync and async transports."""

    def __init__(
        self, retry: RetryOptions | None, now_ms: Callable[[], float] | None, rand: Callable[[], float] | None
    ) -> None:
        self.retry = retry or RetryOptions()
        self.now_ms = now_ms or _now_ms
        self.random = rand or _random.random

    def should_refresh(self, response: httpx.Response | None, refreshed: bool, can_refresh: bool) -> bool:
        return response is not None and response.status_code == 401 and not refreshed and can_refresh

    def rate_limit_delay(self, response: httpx.Response | None, attempt: int) -> float | None:
        if response is not None and response.status_code == 429 and attempt < self.retry.max_retries:
            return rate_limit_wait_ms(
                response.headers.get(RATE_LIMIT_RESET_HEADER), self.now_ms(), self.retry.max_delay_ms
            )
        return None

    def transient_delay(
        self, response: httpx.Response | None, error: Exception | None, idempotent: bool, attempt: int
    ) -> float | None:
        transient = error is not None or (response is not None and response.status_code >= 500)
        if transient and idempotent and attempt < self.retry.max_retries:
            return backoff_ms(attempt + 1, self.retry, self.random())
        return None


def _bearer(request: httpx.Request, token: str) -> None:
    request.headers["Authorization"] = f"Bearer {token}"


class RetryTransport(httpx.BaseTransport):
    """Sync transport: attaches the managed bearer, then applies the retry policy."""

    def __init__(
        self,
        inner: httpx.BaseTransport,
        *,
        token_manager: TokenManager | None = None,
        retry: RetryOptions | None = None,
        sleep: Callable[[float], Any] | None = None,
        now_ms: Callable[[], float] | None = None,
        random: Callable[[], float] | None = None,
    ) -> None:
        self._inner = inner
        self._tm = token_manager
        self._policy = _Policy(retry, now_ms, random)
        self._sleep = sleep or (lambda ms: time.sleep(ms / 1000))

    def handle_request(self, request: httpx.Request) -> httpx.Response:
        request.read()  # materialise the body once so every attempt re-sends the same bytes
        idempotent = request.method.upper() in IDEMPOTENT_METHODS
        token = self._tm.get_access_token() if self._tm is not None else None
        refreshed = False
        attempt = 0
        while True:
            if token is not None:
                _bearer(request, token)
            response: httpx.Response | None = None
            error: Exception | None = None
            try:
                attempt_response = self._inner.handle_request(request)
                attempt_response.read()
                response = attempt_response
            except httpx.TransportError as exc:
                error = exc
            if self._tm is not None and self._policy.should_refresh(response, refreshed, self._tm.can_refresh):
                refreshed = True
                token = self._tm.refresh(stale_token=token).access_token
                continue
            delay = self._policy.rate_limit_delay(response, attempt)
            if delay is None:
                delay = self._policy.transient_delay(response, error, idempotent, attempt)
            if delay is not None:
                attempt += 1
                self._sleep(delay)
                continue
            if response is not None:
                return response
            assert error is not None
            raise error

    def close(self) -> None:
        self._inner.close()


class AsyncRetryTransport(httpx.AsyncBaseTransport):
    """Async transport: same policy as :class:`RetryTransport`."""

    def __init__(
        self,
        inner: httpx.AsyncBaseTransport,
        *,
        token_manager: AsyncTokenManager | None = None,
        retry: RetryOptions | None = None,
        sleep: Callable[[float], Awaitable[Any]] | None = None,
        now_ms: Callable[[], float] | None = None,
        random: Callable[[], float] | None = None,
    ) -> None:
        self._inner = inner
        self._tm = token_manager
        self._policy = _Policy(retry, now_ms, random)
        self._sleep = sleep or _async_sleep_ms

    async def handle_async_request(self, request: httpx.Request) -> httpx.Response:
        await request.aread()
        idempotent = request.method.upper() in IDEMPOTENT_METHODS
        token = await self._tm.get_access_token() if self._tm is not None else None
        refreshed = False
        attempt = 0
        while True:
            if token is not None:
                _bearer(request, token)
            response: httpx.Response | None = None
            error: Exception | None = None
            try:
                attempt_response = await self._inner.handle_async_request(request)
                await attempt_response.aread()
                response = attempt_response
            except httpx.TransportError as exc:
                error = exc
            if self._tm is not None and self._policy.should_refresh(response, refreshed, self._tm.can_refresh):
                refreshed = True
                token = (await self._tm.refresh(stale_token=token)).access_token
                continue
            delay = self._policy.rate_limit_delay(response, attempt)
            if delay is None:
                delay = self._policy.transient_delay(response, error, idempotent, attempt)
            if delay is not None:
                attempt += 1
                await self._sleep(delay)
                continue
            if response is not None:
                return response
            assert error is not None
            raise error

    async def aclose(self) -> None:
        await self._inner.aclose()


async def _async_sleep_ms(ms: float) -> None:
    import asyncio

    await asyncio.sleep(ms / 1000)
