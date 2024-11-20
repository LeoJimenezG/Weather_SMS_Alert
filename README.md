# Weather_SMS_Alert
Send alert text messages (SMS) according to weather data, using Twilio API.

-- How does it work --
- Its funcionality is very simple. It makes a request to a weather api and evaluates the results checking for an specific condition.
- If the condition is checked, a SMS will be sent from your Twilio's number to the number you specify.
- In order for it to run properly, you will need use two APIs:
  -  Twilio: https://www.twilio.com/
  -  OpenWeatherMap: https://openweathermap.org/api
- Once you get all the credentials needed from the APIs, you will need to change the following variables:
  - Twilio credentials: <img width="166" alt="Screenshot 2024-11-19 at 18 55 18" src="https://github.com/user-attachments/assets/01e26baa-ec11-4d09-9902-0e5b32c284db">
  - OpenWeatherMap: <img width="247" alt="Screenshot 2024-11-19 at 18 56 12" src="https://github.com/user-attachments/assets/ba0901a6-a0f8-4058-8d06-608837509bf9">
  - In the variable "parameters", in "lat" put your latitude, in "lon" put your longitude, in "cnt" is the amount of data from the api and in "appid" your key.

