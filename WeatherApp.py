import requests

API_KEY = '473bcbce5b8e30df9b361f761ede68ba'
BASE_URL = 'http://api.openweathermap.org/data/2.5/weather'

city=input('Enter City Name: ')


params={"q" : city,
        "appid" : API_KEY,
         "units" : "metric" }


response = requests.get(BASE_URL, params=params)
print(response.url)

if response.status_code == 200:
    data = response.json()
    temp = data["main"]["temp"]
    rain = data["rain"]["1h"]
    humidity = data["main"]["humidity"]
    print(f"Temperature: {temp}°C")
    print(f"Rain: {rain}%")
    print(f"Humidity: {humidity}%")
else:
    print("City not found!")
