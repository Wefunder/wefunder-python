"""operationId: createInstallationToken — mint a company-owned token for an install a founder made
(write:installations). An explicit empty `scopes` grants nothing; omit it for the install's ceiling."""

from __future__ import annotations

from typing import Any

from wefunder import Wefunder


def example(wf: Wefunder) -> Any:
    # region createInstallationToken
    minted = wf.installations.mint_token("inst_7hQExampleInstall01", ["read:investments"])
    print(minted.token.access_token)  # shown once — store it
    # endregion
    return minted
