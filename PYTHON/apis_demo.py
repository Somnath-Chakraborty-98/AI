import requests

url = "https://api.open-meteo.com/v1/forecast"
params = {
    "latitude": 18.5204,     # Pune, India
    "longitude": 73.8567,
    "current": "temperature_2m,wind_speed_10m"
}

response = requests.get(url, params=params)
data = response.json()

print("Current weather:", data["current"])
print(data.keys())