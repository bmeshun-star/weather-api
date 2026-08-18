from fastapi import FastAPI
import requests

app = FastAPI()

@app.get("/weather")
def get_weather(city: str):

    geocoding_url = "https://geocoding-api.open-meteo.com/v1/search"

    location_response = requests.get(geocoding_url, params= {"name": city,"count": 1})

    location_data = location_response.json()
    location = location_data["results"][0]
    latitude = location["latitude"]
    longitude = location["longitude"]
    weather_url = "https://api.open-meteo.com/v1/forecast"

    params = {"latitude": latitude,"longitude": longitude,"current": "temperature_2m,wind_speed_10m"}

    response = requests.get(weather_url, params=params)

    data = response.json()
    return {"city": city, "current": data.get("current")}