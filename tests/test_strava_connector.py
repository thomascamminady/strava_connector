"""Tests for `strava_connector` package."""


# TODO:
# This is very basic testing only.
# As long as there is no "Authorization Error" in the response,
# the test passes.

from typing import Any

import pytest

from strava_connector.connector import Connector

ACTIVITY_IDS = [11285761263]
ATHLETE_IDS = []
CLUB_IDS = []
GEAR_IDS = []
ROUTE_IDS = []


def get_connection() -> Connector:
    return Connector(
        client_token_path=".tokens_client.json",
        strava_token_path=".tokens_strava.json",
    )


def check_response(response: Any) -> None:
    if isinstance(response, dict):
        if "message" in response.keys():
            if response["message"] == "Authorization Error":
                raise Exception("Authorization Error")


@pytest.mark.parametrize("id", ACTIVITY_IDS)
def test_getActivityById(id) -> None:
    connection = get_connection()
    response = connection.getActivityById(id=id)
    check_response(response)


@pytest.mark.parametrize("id", ACTIVITY_IDS)
def test_getCommentsByActivityId(id) -> None:
    connection = get_connection()
    response = connection.getCommentsByActivityId(id=id)
    check_response(response)


@pytest.mark.parametrize("id", ACTIVITY_IDS)
def test_getKudoersByActivityId(id) -> None:
    connection = get_connection()
    response = connection.getKudoersByActivityId(id=id)
    check_response(response)


@pytest.mark.parametrize("id", ACTIVITY_IDS)
def test_getLapsByActivityId(id) -> None:
    connection = get_connection()
    response = connection.getLapsByActivityId(id=id)
    check_response(response)


def test_getLoggedInAthleteActivities() -> None:
    connection = get_connection()
    response = connection.getLoggedInAthleteActivities(page=1)
    check_response(response)


@pytest.mark.parametrize("id", ACTIVITY_IDS)
def test_getZonesByActivityId(id) -> None:
    connection = get_connection()
    response = connection.getZonesByActivityId(id=id)
    check_response(response)


def test_getLoggedInAthlete() -> None:
    connection = get_connection()
    response = connection.getLoggedInAthlete()
    check_response(response)


def test_getLoggedInAthleteZones() -> None:
    connection = get_connection()
    response = connection.getLoggedInAthleteZones()
    check_response(response)


@pytest.mark.parametrize("athlete_id", ATHLETE_IDS)
def test_getStats(athlete_id) -> None:
    connection = get_connection()
    response = connection.getStats(athlete_id)
    check_response(response)


@pytest.mark.parametrize("club_id", CLUB_IDS)
def test_getClubActivitiesById(club_id) -> None:
    connection = get_connection()
    response = connection.getClubActivitiesById(club_id)
    check_response(response)


@pytest.mark.parametrize("club_id", CLUB_IDS)
def test_getClubAdminsById(club_id) -> None:
    connection = get_connection()
    response = connection.getClubAdminsById(club_id)
    check_response(response)


@pytest.mark.parametrize("club_id", CLUB_IDS)
def test_getClubById(club_id) -> None:
    connection = get_connection()
    response = connection.getClubById(club_id)
    check_response(response)


@pytest.mark.parametrize("club_id", CLUB_IDS)
def test_getClubMembersById(club_id) -> None:
    connection = get_connection()
    response = connection.getClubMembersById(club_id)
    check_response(response)


def test_getLoggedInAthleteClubs() -> None:
    connection = get_connection()
    response = connection.getLoggedInAthleteClubs(page=1)
    check_response(response)


@pytest.mark.parametrize("gear_id", GEAR_IDS)
def test_getGearById(gear_id) -> None:
    connection = get_connection()
    response = connection.getGearById(gear_id)
    check_response(response)


@pytest.mark.parametrize("route_id", ROUTE_IDS)
def test_getRouteAsGPXById(route_id) -> None:
    connection = get_connection()
    response = connection.getRouteAsGPX(route_id)
    check_response(response)


@pytest.mark.parametrize("route_id", ROUTE_IDS)
def test_getRouteAsTCXById(route_id) -> None:
    connection = get_connection()
    response = connection.getRouteAsTCX(route_id)
    check_response(response)


@pytest.mark.parametrize("route_id", ROUTE_IDS)
def test_getRouteById(route_id) -> None:
    connection = get_connection()
    response = connection.getRouteById(route_id)
    check_response(response)


@pytest.mark.parametrize("athlete_id", ATHLETE_IDS)
def test_getRoutesByAthleteId(athlete_id) -> None:
    connection = get_connection()
    response = connection.getRoutesByAthleteId(athlete_id)
    check_response(response)
