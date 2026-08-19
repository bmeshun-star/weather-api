from fastapi import FastAPI, HTTPException, Query
import requests

app = FastAPI(title="Weather Alert Service")

WEATHER_API_URL = "http://weather-service:8000/weather"
REQUEST_TIMEOUT = 10


@app.get("/alert")
def get_alert(city: str = Query(..., min_length=1)):
    city = city.strip()
    if not city:
        raise HTTPException(status_code=400, detail="City cannot be empty")

    try:
        response = requests.get(
            WEATHER_API_URL,
            params={"city": city},
            timeout=REQUEST_TIMEOUT,
        )
        response.raise_for_status()
        weather = response.json()
        current = weather["current"]
        temperature = current["temperature_2m"]
        wind_speed = current["wind_speed_10m"]
    except (requests.RequestException, ValueError, KeyError, TypeError) as error:
        raise HTTPException(
            status_code=502,
            detail="Unable to retrieve weather data",
        ) from error

    alert = temperature > 30 or wind_speed > 40
    message = "Weather alert: dangerous conditions" if alert else "Weather conditions are normal"

    return {
        "city": weather.get("city", city),
        "alert": alert,
        "message": message,
        "temperature_c": temperature,
        "wind_speed_kmh": wind_speed,
    }
