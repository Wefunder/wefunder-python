"""Lazy auto-pagination over an OPAQUE cursor.

Different endpoints back the cursor with an int id, an ISO timestamp, or an offset, so it
is never inspected or arithmetic'd — ``meta.next_cursor`` is fed back verbatim. Items are
streamed one page at a time (the whole result set is never buffered). Stop conditions:
``meta.has_more`` is false, ``next_cursor`` is null/absent, or a cursor repeats (a guard
against an endpoint that loops). The Investment Delta API always sends ``next_cursor``,
even on the last page, so ``has_more`` is the terminating signal there.
"""

from __future__ import annotations

from collections.abc import AsyncIterator, Awaitable, Callable, Iterator, Mapping
from typing import Any, TypeVar

Cursor = str | int
T = TypeVar("T")


def _attr_or_key(obj: Any, name: str) -> Any:
    if obj is None:
        return None
    if isinstance(obj, Mapping):
        return obj.get(name)
    value = getattr(obj, name, None)
    # openapi-python-client marks absent fields with an ``Unset`` sentinel.
    return None if type(value).__name__ == "Unset" else value


def page_parts(page: Any) -> tuple[list[Any], bool | None, Cursor | None]:
    """``(items, has_more, next_cursor)`` from a dict page or a generated ``*ListEnvelope``."""
    data = _attr_or_key(page, "data") or []
    meta = _attr_or_key(page, "meta")
    has_more = _attr_or_key(meta, "has_more")
    next_cursor = _attr_or_key(meta, "next_cursor")
    return list(data), (has_more if isinstance(has_more, bool) else None), next_cursor


def paginate(fetch_page: Callable[[Cursor | None], Any]) -> Iterator[Any]:
    """Yield every item across all pages, lazily. ``fetch_page(None)`` is the first page."""
    cursor: Cursor | None = None
    seen: set[Cursor] = set()
    while True:
        items, has_more, next_cursor = page_parts(fetch_page(cursor))
        yield from items
        if has_more is False or next_cursor is None or next_cursor in seen:
            return
        seen.add(next_cursor)
        cursor = next_cursor


def collect(fetch_page: Callable[[Cursor | None], Any]) -> list[Any]:
    """Every item, in one list. Convenience over :func:`paginate` for small result sets."""
    return list(paginate(fetch_page))


async def apaginate(fetch_page: Callable[[Cursor | None], Awaitable[Any]]) -> AsyncIterator[Any]:
    """Async :func:`paginate`."""
    cursor: Cursor | None = None
    seen: set[Cursor] = set()
    while True:
        items, has_more, next_cursor = page_parts(await fetch_page(cursor))
        for item in items:
            yield item
        if has_more is False or next_cursor is None or next_cursor in seen:
            return
        seen.add(next_cursor)
        cursor = next_cursor


async def acollect(fetch_page: Callable[[Cursor | None], Awaitable[Any]]) -> list[Any]:
    """Async :func:`collect`."""
    return [item async for item in apaginate(fetch_page)]
