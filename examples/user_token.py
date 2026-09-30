"""Guide: act on behalf of a user (authorization_code + PKCE). The consent screen IS the
installation on the user — there is nothing to call on /installations for this case.
Split across your redirect handler (step 1) and your callback handler (steps 2–3)."""

from __future__ import annotations

import os
import secrets
from collections.abc import Callable
from typing import Any

from wefunder import TokenSet, Wefunder, create_authorization_url, exchange_code, generate_pkce


def begin_authorization(save_attempt: Callable[[str, str], None]) -> Any:
    # region guides/user-token
    # 1. Send the investor to consent. Keep state + the PKCE verifier in their session.
    pkce = generate_pkce()
    state = secrets.token_urlsafe(32)
    save_attempt(state, pkce.code_verifier)
    authorization_url = create_authorization_url(
        client_id=os.environ["WEFUNDER_CLIENT_ID"],
        redirect_uri=os.environ["WEFUNDER_REDIRECT_URI"],
        scopes=["read:investments"],
        state=state,
        pkce=pkce,
    )
    # redirect(authorization_url)

    # 2. On the callback, exchange the code (after checking `state` matches the session).
    tokens = exchange_code(
        client_id=os.environ["WEFUNDER_CLIENT_ID"],
        client_secret=os.environ.get("WEFUNDER_CLIENT_SECRET"),  # omit for public clients
        code="AUTHORIZATION_CODE",
        redirect_uri=os.environ["WEFUNDER_REDIRECT_URI"],
        code_verifier=pkce.code_verifier,
    )

    # 3. Read their holdings. The access token lasts two hours; the SDK rotates the refresh
    #    token for you and hands every new set to `store.save` — persist the whole thing.
    wf = Wefunder(
        tokens=tokens,
        client_id=os.environ["WEFUNDER_CLIENT_ID"],
        client_secret=os.environ.get("WEFUNDER_CLIENT_SECRET"),
        store=TokenStore(),
    )
    portfolio = wf.portfolio.get()
    print(portfolio.attributes.total_current_value_cents)
    # endregion
    return authorization_url


class TokenStore:  # harness stand-in for your DB
    def save(self, tokens: TokenSet) -> None:
        del tokens
