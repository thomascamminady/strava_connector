<!-- # Strava Connector

## Authenticate

You have to first execute the steps presented in this [amazing tutorial by Benji Knights Johnson.](https://medium.com/swlh/using-python-to-connect-to-stravas-api-and-analyse-your-activities-dummies-guide-5f49727aac86)

You need to have two files inside the `stra2ical` folder:

`.client.json`

```json
{
  "client_id": 12345,
  "client_secret": "abc123abc123abc123abc123abc123abc123abc123"
}
```

And there should be a second file `.strava_tokens.json`. This is generated if you run the `authenticate.ipynb` that lives inside `notebooks/`. This is the script from Benji Knits Johnson's tutorial. The content of `.strava_tokens.json` looks like this:

```json
{
  "token_type": "Bearer",
  "access_token": "56756756756asdasdasdas56756756756asdasdasdas",
  "expires_at": 1711382710,
  "expires_in": 21600,
  "refresh_token": "xyz789xyz789xyz789xyz789xyz789"
}
```

## Credits

- [Benji Knights Johnson](https://medium.com/swlh/using-python-to-connect-to-stravas-api-and-analyse-your-activities-dummies-guide-5f49727aac86)
- This package was created with [`cookiecutter`](https://github.com/audreyr/cookiecutter) and [`thomascamminady/cookiecutter-pypackage`](https://github.com/thomascamminady/cookiecutter-pypackage), a fork of [`audreyr/cookiecutter-pypackage`](https://github.com/audreyr/cookiecutter-pypackage). -->
