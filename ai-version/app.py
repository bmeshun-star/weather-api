from fastapi import FastAPI, HTTPException, Query
import requests

app = FastAPI(title="AI-Assisted Weather API")

GEOCODING_URL = "https://geocoding-api.open-meteo.com/v1/search"
FORECAST_URL = "https://api.open-meteo.com/v1/forecast"
REQUEST_TIMEOUT = 10


@app.get("/weather")
def get_weather(city: str = Query(..., min_length=1)):
    city = city.strip()
    if not city:
        raise HTTPException(status_code=400, detail="City cannot be empty")

    try:
        location_response = requests.get(
            GEOCODING_URL,
            params={"name": city, "count": 1, "language": "en", "format": "json"},
            timeout=REQUEST_TIMEOUT,
        )
        location_response.raise_for_status()
        location_data = location_response.json()
    except (requests.RequestException, ValueError) as error:
        raise HTTPException(
            status_code=502, detail="Unable to look up the city"
        ) from error

    locations = location_data.get("results", [])
    if not locations:
        raise HTTPException(status_code=404, detail=f"City not found: {city}")

    location = locations[0]
    try:
        weather_response = requests.get(
            FORECAST_URL,
            params={
                "latitude": location["latitude"],
                "longitude": location["longitude"],
                "current": "temperature_2m,wind_speed_10m",
            },
            timeout=REQUEST_TIMEOUT,
        )
        weather_response.raise_for_status()
        weather_data = weather_response.json()
    except (requests.RequestException, ValueError, KeyError) as error:
        raise HTTPException(
            status_code=502, detail="Unable to retrieve weather data"
        ) from error

    return {
        "city": location.get("name", city),
        "country": location.get("country"),
        "current": weather_data.get("current"),
    }
