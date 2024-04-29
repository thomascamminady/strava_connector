# Strava Connector

This is a simple [Strava](https://www.strava.com) client written in Python. I found Strava's Python API to be difficult to use, so I wrote this wrapper that uses `requests` to expose all `GET` requests that are available in Strava's [API documentation](https://developers.strava.com/docs/reference/).

You have to manually follow the tutorial listed below to retrieve a `client_id` and a `client_secret`. This has to be done only once. Afterwards, `strava_connector` exposes convenient wrappers.

## Installation

```
pip install strava_connector
```

or

```
poetry add strava_connector
```

## How to use

For the following example to work, you need to follow the _Authentication workflow_ below.

Here's an example that shows how to retrieve a user's recent activities.
This is a wrapper around [`getLoggedInAthleteActivities`](https://developers.strava.com/docs/reference/#api-Activities-getLoggedInAthleteActivities).

```python
from strava_connector.connector import Connector
connector = Connector(".tokens_client.json",".tokens_strava.json")
res = connector.getLoggedInAthleteActivities(page=1, per_page=3)
```

## Authentication workflow

Run the following steps.

### Step 1

You have to first execute the first step (Create your App/API Connection) presented in this [amazing tutorial by Benji Knights Johnson.](https://medium.com/swlh/using-python-to-connect-to-stravas-api-and-analyse-your-activities-dummies-guide-5f49727aac86)

As a result, you will have received your `client_id` and your `client_secret`.

### Step 2

We need to run an initial authentication.
Run the following code interactively in a python shell and replace the fake `client_id` and `client_secret` with the ones obtained in the previous step.

```python
from strava_connector import initial_auth
client_id = "8xxxxxxxxxx1"
client_secret = "axxxxxxxxxxxxxxxxxxxxxxxxxc"
initial_auth(client_id, client_secret)
```

This will prompt you to click on a link and the dialogue will look something like this:

```txt

Click on the following authentication url.
You will be redirected and have to click 'Authorize'.
This redirects to a domain that does not resolve.

Click here.         # On MacOs, you can do option+left mouse on this link.

Paste the full url in here.
http://localhost/exchange_token?state=&code=2xxxxxxxxxxxxx // redacted
{'client_secret': 'axxxxxxxxxxxxxxxxxxxxxxxxxc', 'client_id': '8xxxxxxxxxx1'}
{
    'token_type': 'Bearer',
    'expires_at': 1714407867,
    'expires_in': 20187,
    'refresh_token': '7xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxb',
    'access_token': '6xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxa',
    'athlete': { // redacted }
}
```

This creates the two required files, `.tokens_client.json` and `.tokens_strava.json`.

## AI warning

I heavily used [Github's Copilot](https://github.com/features/copilot) as an advanced autocomplete
for the creation of the `get_...` methods and for writing the `test_get_...` methods.

## Credits

- Strava authentication tutorial by [Benji Knights Johnson](https://medium.com/swlh/using-python-to-connect-to-stravas-api-and-analyse-your-activities-dummies-guide-5f49727aac86)
- This package was created with [`cookiecutter`](https://github.com/audreyr/cookiecutter) and [`thomascamminady/cookiecutter-pypackage`](https://github.com/thomascamminady/cookiecutter-pypackage), a fork of [`audreyr/cookiecutter-pypackage`](https://github.com/audreyr/cookiecutter-pypackage).
- Documentation via [pdoc](https://github.com/mitmproxy/pdoc)
