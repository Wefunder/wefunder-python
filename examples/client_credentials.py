"""Server-to-server: exchange client credentials for a token and make a call.
Run: WEFUNDER_CLIENT_ID=... WEFUNDER_CLIENT_SECRET=... python examples/client_credentials.py
"""

from __future__ import annotations

import os

from wefunder import Wefunder


def main() -> None:
    # region guides/client-credentials
    wf = Wefunder.from_client_credentials(
        client_id=os.environ["WEFUNDER_CLIENT_ID"],
        client_secret=os.environ["WEFUNDER_CLIENT_SECRET"],
        scopes=["read:public"],
    )

    print("mode:", wf.mode)  # "live" or "test", from the token prefix

    # client_credentials holds only read:public — browse public offerings.
    # (wf.users.me() would raise 403 insufficient_scope: it needs read:profile.)
    for offering in wf.offerings.all():
        print(offering.id)
    # endregion


if __name__ == "__main__":
    main()
