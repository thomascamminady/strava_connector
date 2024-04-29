import requests

from strava_connector.authenticator import Authenticator


class Connector:
    def __init__(self, client_token_path: str, strava_token_path: str) -> None:
        self.authenticator = Authenticator(
            client_token_path=client_token_path,
            strava_token_path=strava_token_path,
        )
        self.apiurl = """https://www.strava.com/api/v3"""

    @property
    def access_token(self) -> str:
        """Append the credentials to the request."""
        self.authenticator.update_token()
        return str(self.authenticator.strava_tokens["access_token"])

    def get_logged_in_athlete_activities(
        self, page: int, per_page: int = 200
    ) -> dict:
        """List Athlete Activities."""
        params = f"""per_page={per_page}&page={page}&access_token={self.access_token}"""
        url = f"{self.apiurl}/athlete/activities?{params}"
        result = requests.get(url, timeout=self.authenticator._timeout)
        return result.json()
