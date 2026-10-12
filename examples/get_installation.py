"""operationId: getInstallation — one installation by id (read:installations)."""

from __future__ import annotations

from typing import Any

from wefunder import Wefunder


def example(wf: Wefunder) -> Any:
    # region getInstallation
    install = wf.installations.get("inst_7hQExampleInstall01")
    print(install.attributes.status, install.attributes.scopes)
    # endregion
    return install
