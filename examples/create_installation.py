"""operationId: createInstallation — install your app on a company or syndicate the user can edit
(write:installations) and receive the company-owned token the install stands for."""

from __future__ import annotations

from typing import Any

from wefunder import Wefunder


def example(wf: Wefunder) -> Any:
    # region createInstallation
    install = wf.installations.create(
        {"target_type": "company", "target_id": "co_abc123Example", "scopes": ["read:offerings", "read:investments"]}
    )
    print(install.data.id, install.token.access_token)  # the token is shown once — store it
    # endregion
    return install
