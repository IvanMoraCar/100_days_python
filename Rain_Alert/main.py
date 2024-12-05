import requests
from twilio.rest import Client

WEATHER_KEY = "9caad723ec450bdbdcea4c7d9f0f7050"
LATITUDE = "32.514946"
LONGITUDE = "-117.038246"
TIMESTAMPS = "4"

# URL completa con el esquema HTTPS
OWM_Endpoint = "https://api.openweathermap.org/data/2.5/forecast"
account_sid = 'ACb13919c58c79d8b15ea87e85c58a44d3'
auth_token = '19d92c7755152e36b6ffc90e3043b64d'

weather_params = {
    "lat": LATITUDE,
    "lon": LONGITUDE,
    "appid": WEATHER_KEY,
    "cnt": TIMESTAMPS
}

response = requests.get(OWM_Endpoint, params=weather_params)
response.raise_for_status()
weather_data = response.json()


will_rain = False
for day in range(int(TIMESTAMPS)):
    weather_code = weather_data["list"][day]["weather"][0]["id"]
    if weather_code < 700:
        will_rain = True
if will_rain:
    client = Client(account_sid, auth_token)
    message = client.messages.create(
        from_='+17752626385',
        body="It's going to rain. Remember to bring an umbrella",
        to='+526632002998'
    )
    print(message.status)

# will_rain = False
# for hour_data in weather_data["list"]:
#     condition_code = hour_data["weather"][0]["id"]
#     if int(condition_code) < 700:
#         will_rain = True
#
# if will_rain:
#     print("Bring an umbrella")





