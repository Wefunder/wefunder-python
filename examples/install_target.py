"""Guide: act for a company or syndicate. `wf` holds a MANAGER's user token with
`read:installations write:installations` (listing needs the read scope; write does not imply
it). Install, then mint the installation's own token — it has no expiry and no refresh;
revoking the install revokes it."""

from __future__ import annotations

from typing import Any

from wefunder import Wefunder
from wefunder._generated.api.syndicate_deals import list_syndicate_deals


def example(wf: Wefunder, syndicate_id: str = "syn_aB3xQ9k2vF8mNp1zT5wY7Qc4") -> Any:
    # region guides/install-target
    # 1. Which companies / syndicates may this user install on? (Only those — an investor's
    #    empty list is not a failure.)
    for target in wf.installations.eligible_targets("syndicate"):
        print(target.id, target.name, "(already installed)" if target.installed else "")

    # 2. Install. The response carries the install (`data`) AND its token. If the app is
    #    already installed here the API answers 409 `already_installed`; install_or_mint_token
    #    mints a fresh token for that existing install instead, re-requesting the same scopes.
    #    Any other error (revoked install, missing scope) still raises.
    installed = wf.installations.install_or_mint_token(
        {"target_type": "syndicate", "target_id": syndicate_id, "scopes": ["read:syndicates"]}
    )
    installation_token = installed.token.access_token  # shown once — store it

    # 3. First request AS the installation.
    as_syndicate = Wefunder(access_token=installation_token)
    deals = as_syndicate.call(list_syndicate_deals, syndicate_id=syndicate_id)
    print(len(deals.data), "deals")
    # endregion
    return deals
