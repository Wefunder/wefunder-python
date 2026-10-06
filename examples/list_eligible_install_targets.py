"""operationId: listEligibleInstallTargets — companies or syndicates the token's user could install your app
on (read:installations). An investor's empty list is not a failure."""

from __future__ import annotations

from typing import Any

from wefunder import Wefunder


def example(wf: Wefunder) -> Any:
    # region listEligibleInstallTargets
    targets = wf.installations.eligible_targets("company")
    for target in targets:
        print(target.id, target.name, target.tier, target.installed)
    # endregion
    return targets
