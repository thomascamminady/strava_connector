# Strava Connector

Simple Strava client written in Python

## Workflow

Run the following steps.

### Step 1

You have to first execute the first step (Create your App/API Connection) presented in this [amazing tutorial by Benji Knights Johnson.](https://medium.com/swlh/using-python-to-connect-to-stravas-api-and-analyse-your-activities-dummies-guide-5f49727aac86)

As a result you need to know your `client_id` and your `client_secret`

### Step 2

We need to run an initial authentication. Run the following code interactively in a python shell and replace the fake `client_id` and `client_secret` with the ones obtained in the previous step.

```python
from strava_connector import initial_auth
client_id = "8xxxxxxxxxx1"
client_secret = "axxxxxxxxxxxxxxxxxxxxxxxxxc"
initial_auth(client_id, client_secret)
Click on the following authentication url.
You will be redirected and have to click 'Authorize'.
This redirects to a domain that does not resolve.

Click here.         # On MacOs, you can do option+left mouse on this link.

Paste the full url in here.
http://localhost/exchange_token?state=&code=2xxxxxxxxxxxxxxxxxxx3&scope=read,activity:read_all,profile:read_all
{'client_secret': 'axxxxxxxxxxxxxxxxxxxxxxxxxc', 'client_id': '8xxxxxxxxxx1'}
{
    'token_type': 'Bearer',
    'expires_at': 1714407867,
    'expires_in': 20187,
    'refresh_token': '7xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxb',
    'access_token': '6xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxa',
    'athlete': {
        // redacted
    }
}
```

This creates two files, `.tokens_client.json` and `.tokens_strava.json`.

## Credits

- [Benji Knights Johnson](https://medium.com/swlh/using-python-to-connect-to-stravas-api-and-analyse-your-activities-dummies-guide-5f49727aac86)
- This package was created with [`cookiecutter`](https://github.com/audreyr/cookiecutter) and [`thomascamminady/cookiecutter-pypackage`](https://github.com/thomascamminady/cookiecutter-pypackage), a fork of [`audreyr/cookiecutter-pypackage`](https://github.com/audreyr/cookiecutter-pypackage).
