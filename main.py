import requests
import conditions
from twilio.rest import Client


param = {
    "key" : "dd30e8af174c4f6d89b173516231709",
    "q" : "San Jose",
    "days" : 1,
    "aqi" : "no",
    "alerts":"no"
}

# API Call
response = requests.get(url="http://api.weatherapi.com/v1/forecast.json",params=param)

# fetch hourly weather condition
hourly_weather = response.json()['forecast']['forecastday'][0]['hour']

# List to fetch all the weather data
weather_data = []

# bool variable to check if it is raining today
is_raining = False

# append all the data to weather_data
for weather in hourly_weather:

    weather_data.append(weather["condition"]['text'])

# check if it is raining any time in the next 24 hours
for weather in weather_data:

    if weather in conditions.conditions:

        is_raining = True

# twilio constants
account_sid = 'ACf83fa8ce30bef8fcc9757af90b05a18d'
auth_token = 'f00a1452fdab74d72148efa231d214cf'

# twilio client instance
client = Client(account_sid, auth_token)

# if it is raining shoot a text using twilio's API
if is_raining:

    message = client.messages.create(
        from_='+18445591173',
        to='+14085505024',
        body='It will be raining today! Please make sure to bring an umbrella'
    )

    print(message.sid)