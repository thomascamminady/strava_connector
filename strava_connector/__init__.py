""".. include:: ../README.md."""

import json
from urllib.parse import parse_qs, urlparse

from strava_connector.authenticator import Authenticator


def initial_auth(
    client_id: str,
    client_secret: str,
    client_token_path: str = ".tokens_client.json",  # noqa: S107
    strava_token_path: str = ".tokens_strava.json",  # noqa: S107
    to_print: bool = True,
) -> None:
    authenticator = Authenticator(
        strava_token_path=strava_token_path,
        client_token_path=client_token_path,
    )

    auth_url = f"""http://www.strava.com/oauth/authorize?client_id={client_id}&response_type=code&redirect_uri=http://localhost/exchange_token&approval_prompt=force&scope=profile:read_all,activity:read_all"""

    print("Click on the following authentication url.")
    print("You will be redirected and have to click 'Authorize'.")
    print("This redirects to a domain that does not resolve.")
    print()
    print(f"""[link={auth_url}]Click here.[/link]""")
    print()
    print("Paste the full url in here.")
    redirect_url = input()

    parsed_url = urlparse(redirect_url)
    code = parse_qs(parsed_url.query)["code"][0]

    authenticator.initial_auth(
        client_secret=client_secret,
        client_id=client_id,
        code=code,
    )
    if to_print:
        with open(client_token_path) as _:
            print(json.load(_))

        with open(strava_token_path) as _:
            print(json.load(_))
