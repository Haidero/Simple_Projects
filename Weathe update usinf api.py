
import requests
api_key = "https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={API key}"
city = input("Enter your city: ")

response = requests.get(f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}")
weather_data = response.json()

print(f"Weather in {city}: {weather_data['weather'][0]['description']}")