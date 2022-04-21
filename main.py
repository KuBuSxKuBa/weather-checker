import requests
import os
from twilio.rest import Client

MY_API_KEY = "35741ecda8f40ac70194fbbb68dec766"
account_sid = 'ACd992902117ed811872a1c5f8765030fa'
auth_token = 'f0ef6f146067c12427045df365c0088c'

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
        body="Weź ze sobą parasolkę!\nW przeciągu 12 godzin będzie padał deszcz lub śnieg ☔",
        from_='+18596961072',
        to='+48883992636'
    )
    print(message.status)
