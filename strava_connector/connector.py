import requests

from strava_connector.authenticator import Authenticator


class Connector:
    def __init__(
        self,
        client_token_path: str,
        strava_token_path: str,
        api_url: str = """https://www.strava.com/api/v3""",
    ) -> None:
        self.api_url = api_url
        self.authenticator = Authenticator(
            client_token_path=client_token_path,
            strava_token_path=strava_token_path,
        )

    @property
    def access_token(self) -> str:
        """Append the credentials to the request."""
        self.authenticator.update_token()
        return str(self.authenticator.strava_tokens["access_token"])

    def get_request(
        self,
        route: str,
        print_query: bool,
        params: dict,
    ) -> dict:
        """GET request against strava's API."""
        params["access_token"] = self.access_token
        params_str = "&".join(
            [f"{k}={v}" for k, v in params.items() if v is not None]
        )
        url = f"{self.api_url}/{route}?{params_str}"
        if print_query:
            print(url)
        result = requests.get(url, timeout=self.authenticator._timeout)
        return result.json()

    def getActivityById(
        self,
        id: int,
        include_all_efforts: bool | None = None,
        print_query: bool = False,
    ) -> dict:
        """Get Activity.

        https://developers.strava.com/docs/reference/#api-Activities-getActivityById
        """
        return self.get_request(
            route=f"activities/{id}",
            print_query=print_query,
            params={
                "include_all_efforts": include_all_efforts,
            },
        )

    def getCommentsByActivityId(
        self,
        id: int,
        page: int | None = None,
        per_page: int | None = None,
        page_size: int | None = None,
        after_cursor: str | None = None,
        print_query: bool = False,
    ) -> dict:
        """List Activity Comments .

        https://developers.strava.com/docs/reference/#api-Activities-getCommentsByActivityId
        """
        return self.get_request(
            route=f"activities/{id}/comments",
            print_query=print_query,
            params={
                "page": page,
                "per_page": per_page,
                "page_size": page_size,
                "after_cursor": after_cursor,
            },
        )

    def getKudoersByActivityId(
        self,
        id: int,
        page: int | None = None,
        per_page: int | None = None,
        print_query: bool = False,
    ) -> dict:
        """List Activity Kudoers.

        https://developers.strava.com/docs/reference/#api-Activities-getKudoersByActivityId
        """
        return self.get_request(
            route=f"activities/{id}/kudos",
            print_query=print_query,
            params={
                "page": page,
                "per_page": per_page,
            },
        )

    def getLapsByActivityId(
        self,
        id: int,
        print_query: bool = False,
    ) -> dict:
        """Get Activity Laps.

        https://developers.strava.com/docs/reference/#api-Activities-getLapsByActivityId
        """
        return self.get_request(
            route=f"activities/{id}/laps",
            print_query=print_query,
            params={},
        )

    def getLoggedInAthleteActivities(
        self,
        page: int,
        per_page: int | None = None,
        print_query: bool = False,
    ) -> dict:
        """List Athlete Activities.

        https://developers.strava.com/docs/reference/#api-Activities-getLoggedInAthleteActivities
        """
        return self.get_request(
            route="athlete/activities",
            print_query=print_query,
            params={
                "page": page,
                "per_page": per_page,
            },
        )

    def getZonesByActivityId(
        self,
        id: int,
        print_query: bool = False,
    ) -> dict:
        """Get Activity Zones.

        https://developers.strava.com/docs/reference/#api-Activities-getZonesByActivityId
        """
        return self.get_request(
            route=f"activities/{id}/zones",
            print_query=print_query,
            params={},
        )

    def getLoggedInAthlete(
        self,
        print_query: bool = False,
    ) -> dict:
        """Get Athlete.

        https://developers.strava.com/docs/reference/#api-Athletes-getLoggedInAthlete
        """
        return self.get_request(
            route="athlete",
            print_query=print_query,
            params={},
        )

    def getLoggedInAthleteZones(
        self,
        print_query: bool = False,
    ) -> dict:
        """Get Zones.

        https://developers.strava.com/docs/reference/#api-Athletes-getLoggedInAthleteZones
        """
        return self.get_request(
            route="athlete/zones",
            print_query=print_query,
            params={},
        )

    def getStats(
        self,
        id: int,
        print_query: bool = False,
    ) -> dict:
        """Get Stats.

        https://developers.strava.com/docs/reference/#api-Athletes-getStats
        """
        return self.get_request(
            route=f"athletes/{id}/stats",
            print_query=print_query,
            params={},
        )

    def getClubActivitiesById(
        self,
        id: int,
        page: int | None = None,
        per_page: int | None = None,
        print_query: bool = False,
    ) -> dict:
        """List Club Activities.

        https://developers.strava.com/docs/reference/#api-Clubs-getClubActivitiesById
        """
        return self.get_request(
            route=f"clubs/{id}/activities",
            print_query=print_query,
            params={
                "page": page,
                "per_page": per_page,
            },
        )

    def getClubAdminsById(
        self,
        id: int,
        page: int | None = None,
        per_page: int | None = None,
        print_query: bool = False,
    ) -> dict:
        """List Club Administrators.

        https://developers.strava.com/docs/reference/#api-Clubs-getClubAdminsById
        """
        return self.get_request(
            route=f"clubs/{id}/admins",
            print_query=print_query,
            params={
                "page": page,
                "per_page": per_page,
            },
        )

    def getClubById(
        self,
        id: int,
        print_query: bool = False,
    ) -> dict:
        """Get Club.

        https://developers.strava.com/docs/reference/#api-Clubs-getClubById
        """
        return self.get_request(
            route=f"clubs/{id}",
            print_query=print_query,
            params={},
        )

    def getClubMembersById(
        self,
        id: int,
        page: int | None = None,
        per_page: int | None = None,
        print_query: bool = False,
    ) -> dict:
        """List Club Members.

        https://developers.strava.com/docs/reference/#api-Clubs-getClubMembersById
        """
        return self.get_request(
            route=f"clubs/{id}/members",
            print_query=print_query,
            params={
                "page": page,
                "per_page": per_page,
            },
        )

    def getLoggedInAthleteClubs(
        self,
        page: int,
        per_page: int | None = None,
        print_query: bool = False,
    ) -> dict:
        """List Athlete Clubs.

        https://developers.strava.com/docs/reference/#api-Athletes-getLoggedInAthleteClubs
        """
        return self.get_request(
            route="athlete/clubs",
            print_query=print_query,
            params={
                "page": page,
                "per_page": per_page,
            },
        )

    def getGearById(
        self,
        id: str,
        print_query: bool = False,
    ) -> dict:
        """Get Gear.

        https://developers.strava.com/docs/reference/#api-Gears-getGearById
        """
        return self.get_request(
            route=f"gear/{id}",
            print_query=print_query,
            params={},
        )

    def getRouteAsGPX(
        self,
        id: int,
        print_query: bool = False,
    ) -> dict:
        """Export Route GPX.

        https://developers.strava.com/docs/reference/#api-Routes-getRouteAsGPX
        """
        return self.get_request(
            route=f"routes/{id}/export_gpx",
            print_query=print_query,
            params={},
        )

    def getRouteAsTCX(
        self,
        id: int,
        print_query: bool = False,
    ) -> dict:
        """Export Route TCX.

        https://developers.strava.com/docs/reference/#api-Routes-getRouteAsTCX
        """
        return self.get_request(
            route=f"routes/{id}/export_tcx",
            print_query=print_query,
            params={},
        )

    def getRouteById(
        self,
        id: int,
        print_query: bool = False,
    ) -> dict:
        """Get Route.

        https://developers.strava.com/docs/reference/#api-Routes-getRouteById
        """
        return self.get_request(
            route=f"routes/{id}",
            print_query=print_query,
            params={},
        )

    def getRoutesByAthleteId(
        self,
        id: int,
        page: int | None = None,
        per_page: int | None = None,
        print_query: bool = False,
    ) -> dict:
        """List Athlete Routes.

        https://developers.strava.com/docs/reference/#api-Routes-getRoutesByAthleteId
        """
        return self.get_request(
            route=f"athletes/{id}/routes",
            print_query=print_query,
            params={
                "page": page,
                "per_page": per_page,
            },
        )

    def getEffortsBySegmentId(
        self,
        segment_id: int,
        start_date_local: str | None = None,
        end_date_local: str | None = None,
        per_page: int | None = None,
        print_query: bool = False,
    ) -> dict:
        """List Segment Efforts.

        https://developers.strava.com/docs/reference/#api-SegmentEfforts-getEffortsBySegmentId
        """
        return self.get_request(
            route=f"segments/{id}/all_efforts",
            print_query=print_query,
            params={
                "segment_id": segment_id,
                "start_date_local": start_date_local,
                "end_date_local": end_date_local,
                "per_page": per_page,
            },
        )

    def getSegmentEffortById(
        self,
        id: int,
        print_query: bool = False,
    ) -> dict:
        """Get Segment Effort.

        https://developers.strava.com/docs/reference/#api-SegmentEfforts-getSegmentEffortById
        """
        return self.get_request(
            route=f"segment_efforts/{id}",
            print_query=print_query,
            params={},
        )

    def exploreSegments(
        self,
        bounds: str,
        activity_type: str | None = None,
        min_cat: int | None = None,
        max_cat: int | None = None,
        print_query: bool = False,
    ) -> dict:
        """Explore segments.

        https://developers.strava.com/docs/reference/#api-Segments-exploreSegments
        """
        return self.get_request(
            route="segments/explore",
            print_query=print_query,
            params={
                "bounds": bounds,
                "activity_type": activity_type,
                "min_cat": min_cat,
                "max_cat": max_cat,
            },
        )

    def getRouteStreams(
        self,
        id: int,
        print_query: bool = False,
    ) -> dict:
        """Get Route Streams.

        https://developers.strava.com/docs/reference/#api-Streams-getRouteStreams
        """
        return self.get_request(
            route=f"routes/{id}/streams",
            print_query=print_query,
            params={},
        )

    def getSegmentEffortStreams(
        self,
        id: int,
        keys: list[str],
        key_by_type: bool = False,
        print_query: bool = False,
    ) -> dict:
        """Get Segment Effort Streams.

        https://developers.strava.com/docs/reference/#api-Streams-getSegmentEffortStreams
        """
        return self.get_request(
            route=f"segment_efforts/{id}/streams",
            print_query=print_query,
            params={
                "keys": keys,
                "key_by_type": key_by_type,
            },
        )

    def getSegmentStreams(
        self,
        id: int,
        keys: list[str],
        key_by_type: bool = False,
        print_query: bool = False,
    ) -> dict:
        """Get Segment Streams.

        https://developers.strava.com/docs/reference/#api-Streams-getSegmentStreams
        """
        return self.get_request(
            route=f"segments/{id}/streams",
            print_query=print_query,
            params={
                "keys": keys,
                "key_by_type": key_by_type,
            },
        )

    def getUploadById(
        self,
        uploadId: int,
        print_query: bool = False,
    ) -> dict:
        """Get Upload.

        https://developers.strava.com/docs/reference/#api-Uploads-getUploadById
        """
        return self.get_request(
            route=f"uploads/{id}",
            print_query=print_query,
            params={"uploadId": uploadId},
        )
