"""operationId: getCurrentUser — the connected user (read:profile; not for cc tokens)."""

from __future__ import annotations

from typing import Any

from wefunder import Wefunder


def example(wf: Wefunder) -> Any:
    # region getCurrentUser
    me = wf.users.me()
    print(me.id, me.attributes.name)
    # endregion
    return me
