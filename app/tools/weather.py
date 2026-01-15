import json
from pathlib import Path

file = Path("data/weather.json")

def load_data():
    with open(file, "r") as f:
        return json.load(f)

def get_data(city: str):
    weather_data = load_data()
    city = city.lower()
    return weather_data.get(city)