"""Guide: act for a company or syndicate. `wf` holds a MANAGER's user token with
`read:installations write:installations` (listing needs the read scope; write does not imply
it). Install, then mint the installation's own token — it has no expiry and no refresh;
revoking the install revokes it."""

from __future__ import annotations

from typing import Any

from wefunder import Wefunder
from wefunder._generated.api.installations import (
    create_installation,
    create_installation_token,
    list_eligible_install_targets,
    list_installations,
)
from wefunder._generated.api.syndicate_deals import list_syndicate_deals
from wefunder._generated.models.create_installation_body import CreateInstallationBody


def example(wf: Wefunder, syndicate_id: str = "syn_abc123Example") -> Any:
    # region guides/install-target
    # 1. Which companies / syndicates may this user install on? (Only those — an investor's
    #    empty list is not a failure.)
    targets = wf.call(list_eligible_install_targets, target_type="syndicate")
    for target in targets.data:
        print(target.id, target.name, "(already installed)" if target.installed else "")

    # 2. Install on one of them. The response carries the install (`data`) AND its token.
    body = CreateInstallationBody.from_dict(
        {"target_type": "syndicate", "target_id": syndicate_id, "scopes": ["read:syndicates"]}
    )
    installed = wf.call(create_installation, body=body)
    installation_token = installed.token.access_token

    # 3. Already installed (or the token wasn't kept)? Find the ACTIVE install on this target —
    #    the list is newest-first and includes revoked rows and user installs, so match on
    #    target + status, never on position — and mint a fresh token.
    if not installation_token:
        installs = wf.call(list_installations)
        install = next(
            (i for i in installs.data if i.attributes.status == "active" and i.attributes.target.id == syndicate_id),
            None,
        )
        if install is None:
            raise RuntimeError(f"not installed on {syndicate_id} yet")
        minted = wf.call(create_installation_token, external_id=install.id)
        installation_token = minted.token.access_token  # shown once — store it

    # 4. First request AS the installation.
    as_syndicate = Wefunder(access_token=installation_token)
    deals = as_syndicate.call(list_syndicate_deals, syndicate_id=syndicate_id)
    print(len(deals.data), "deals")
    # endregion
    return deals
