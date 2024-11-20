import requests
from twilio.rest import Client

# Main variables
endpoint = "https://api.openweathermap.org/data/2.5/forecast"
account_sid = ""
auth_token = ""
parameters = {"lat": 0,
              "lon": 0,
              "cnt": 0,
              "appid": ""}

# Make the get request
response = requests.get(url=endpoint, params=parameters)
# Raise an Exception in case of error
response.raise_for_status()
# Get the actual data
data = response.json()["list"]
# Functionality
bring_umbrella = False
for i in range(0, len(data)):
    # Access to the weather id
    weather_id = data[i]["weather"][0]["id"]
    # Check id
    if weather_id < 700:
        bring_umbrella = True

# Give advice
if bring_umbrella:
    # Log in to the Client
    client = Client(account_sid, auth_token)
    # Send the message
    message = client.messages.create(
        body="Bring an Umbrella ☔",
        from_="+16623543555",
        to="+524423649848")
    print(message.status)
