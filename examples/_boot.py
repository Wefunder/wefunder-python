"""Hidden harness — NOT shown in docs (no region markers; leading `_` excludes it from the
manifest). Every example is an `example(wf)` function; the e2e run-gate calls them with
this real sandbox client."""

from __future__ import annotations

import os

from wefunder import Wefunder


def boot_client() -> Wefunder:
    return Wefunder.from_client_credentials(
        client_id=os.environ["WEFUNDER_CLIENT_ID"],
        client_secret=os.environ["WEFUNDER_CLIENT_SECRET"],
        scopes=["read:public"],
    )
