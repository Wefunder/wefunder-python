"""operationId: listInstallations — where your app is installed (read:installations). An installation is
what makes a company/syndicate an AUDIENCE for your webhooks — no install, no deliveries."""

from __future__ import annotations

from typing import Any

from wefunder import Wefunder


def example(wf: Wefunder) -> Any:
    # region listInstallations
    installs = wf.installations.list()
    for install in installs.data:
        print(install.id, install.attributes.target.id, install.attributes.status)
    # endregion
    return installs
