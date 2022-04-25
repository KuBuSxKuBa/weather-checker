import requests
import os
from twilio.rest import Client

parameters = {
    "lat":51.6636,
    "lon":16.0845,
    "appid":MY_API_KEY,
    "exclude":"current,minutely,daily"
}
connection = requests.get(url="https://api.openweathermap.org/data/2.5/onecall?", params=parameters)
connection.raise_for_status()
data = connection.json()
two_days = data["hourly"]
weather_ids = []
should_bring_umbrella = False
for hour in two_days[:12:1]:
    every_hour_weather = hour["weather"]
    dict = every_hour_weather[0]
    id = dict["id"]
    weather_ids.append(id)
for i in weather_ids:
    if int(i) < 700:
        should_bring_umbrella = True
    else:
        pass
if should_bring_umbrella:
    client = Client(account_sid, auth_token)
    message = client.messages \
        .create(
        body="Take umbrella with you!☔",
    )
    print(message.status)
