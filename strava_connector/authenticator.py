import json
import time
from typing import TypedDict

import requests


class Payload(TypedDict):
    client_id: str
    client_secret: str
    grant_type: str


class AuthPayload(Payload):
    code: str


class RefreshPayload(Payload):
    refresh_token: str


class Authenticator:
    def __init__(
        self,
        client_token_path: str,
        strava_token_path: str,
        encoding: str = "UTF-8",
        oauth_url: str = "https://www.strava.com/oauth/token",
        timeout_sec: int = 60,
    ) -> None:
        self._client_token_path = client_token_path
        self._strava_token_path = strava_token_path
        self._encoding = encoding
        self._oauth_url = oauth_url
        self._timeout = timeout_sec

    def _tokens(self, file) -> dict[str, str]:
        with open(file=file, encoding=self._encoding) as json_file:
            return json.load(fp=json_file)

    @property
    def strava_tokens(self) -> dict[str, str]:
        """Get the Strava tokens as dict."""
        return self._tokens(file=self._strava_token_path)

    @property
    def client_tokens(self) -> dict[str, str]:
        """Get the client tokes as dict."""
        return self._tokens(file=self._client_token_path)

    def get_refresh_payload(self) -> RefreshPayload:
        """Returns the refresh payload."""
        return {
            "client_id": self.client_tokens["client_id"],
            "client_secret": self.client_tokens["client_secret"],
            "grant_type": "refresh_token",
            "refresh_token": self.strava_tokens["refresh_token"],
        }

    def get_auth_payload(
        self, client_id: str, client_secret: str, code: str
    ) -> AuthPayload:
        """Returns the authentication payload."""
        return {
            "client_id": client_id,
            "client_secret": client_secret,
            "code": code,
            "grant_type": "authorization_code",
        }

    def initial_auth(
        self, client_id: str, client_secret: str, code: str
    ) -> None:
        """Performs the initial authentication."""
        # Save client data.
        with open(file=self._client_token_path, mode="w") as _:
            json.dump(
                obj={"client_secret": client_secret, "client_id": client_id},
                fp=_,
                indent=4,
            )

        payload: AuthPayload = self.get_auth_payload(
            client_id=client_id, client_secret=client_secret, code=code
        )
        response = requests.post(
            url=self._oauth_url, data=payload, timeout=self._timeout
        )

        strava_tokens = response.json()
        with open(file=self._strava_token_path, mode="w") as _:
            json.dump(obj=strava_tokens, fp=_, indent=4)

    def update_token(self) -> None:
        """Update token using refresh token."""
        # If access_token has expired then
        # use the refresh_token to get the new access_token
        if int(self.strava_tokens["expires_at"]) < time.time():
            # Make Strava auth API call with current refresh token
            payload: RefreshPayload = self.get_refresh_payload()
            response = requests.post(
                url=self._oauth_url, data=payload, timeout=self._timeout
            )
            # Save response as json in new variable
            new_strava_tokens = response.json()
            # Save new tokens to file
            with open(
                file=self._strava_token_path,
                mode="w",
                encoding=self._encoding,
            ) as f:
                json.dump(obj=new_strava_tokens, fp=f, indent=4)
