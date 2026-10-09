"""operationId: revokeInstallation — revoke an installation (write:installations). Its tokens stop working
at once and the company drops out of your webhook audiences."""

from __future__ import annotations

from typing import Any

from wefunder import Wefunder


def example(wf: Wefunder) -> Any:
    # region revokeInstallation
    revoked = wf.installations.revoke("inst_7hQExampleInstall01")
    print(revoked.attributes.status)  # "revoked"
    # endregion
    return revoked
