import requests
import os
from twilio.rest import Client
from twilio.http.http_client import TwilioHttpClient

api_key = "REDACTED"
MY_LAT = 1.290270
MY_LONG = 103.851959
account_sid = "REDACTED"
auth_token = "REDACTED"

OWM_Endpoint = "https://api.openweathermap.org/data/2.5/onecall"
weather_params = {
    "lat": MY_LAT,
    "lon": MY_LONG,
    "exclude": "current,minutely,daily",
    "appid": api_key,
}

response = requests.get(OWM_Endpoint, params=weather_params)
response.raise_for_status()
weather_data = response.json()
weather_slice = weather_data["hourly"][:12]

will_rain = False
for hour_data in weather_slice:
    condition_code = hour_data["weather"][0]["id"]
    if condition_code < 700:
        will_rain = True

if will_rain:
    proxy_client = TwilioHttpClient()
    proxy_client.session.proxies = {'https': os.environ['https_proxy']}
    client = Client(account_sid, auth_token, http_client=proxy_client)
    message = client.messages \
        .create(
        body="It's going to rain today. Remember to bring an umbrella ☂.",
        from_='+REDACTED',
        to='+REDACTED',
    )
    print(message.status)
