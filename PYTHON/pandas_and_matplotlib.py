import requests
from datetime import datetime, timedelta
import pandas as pd
import matplotlib.pyplot as plt
import os

# Calculate dates
today = datetime.now()
week_ago = today - timedelta(days=7)
print(f"Today = {today}, a week ago = {week_ago}")

# Format dates for API (YYYY-MM-DD)
start_date = week_ago.strftime("%Y-%m-%d")
end_date = today.strftime("%Y-%m-%d")
print(f"Start date = {start_date} and end date = {end_date}")

# Get Paris weather for past week
url = f"https://api.open-meteo.com/v1/forecast?latitude=48.85&longitude=2.35&start_date={start_date}&end_date={end_date}&daily=temperature_2m_max,temperature_2m_min,precipitation_sum&timezone=Europe/Paris"

response = requests.get(url)
data = response.json()
print(data)
print("")
print("----------------------------------------------------------")
print("")
daily_data = data["daily"]

df = pd.DataFrame({
    'date': daily_data['time'],
    'min_temp': daily_data['temperature_2m_min'],
    'max_temp': daily_data['temperature_2m_max']
})

df['date'] = pd.to_datetime(df['date'])
print(df)
print("")
print("----------------------------------------------------------")
print("")

plt.figure(figsize=(10,6))
plt.plot(df['date'], df['min_temp'], marker='o')
plt.plot(df['date'], df['max_temp'], marker='o')

plt.xlabel('Date')
plt.ylabel('Temp (Celcius)')
plt.title('Weather - Past 7 days')
plt.legend()

plt.xticks(rotation=45)
plt.tight_layout()

plt.savefig('weather.png')
plt.show()


print("")
print("----------------------------------------------------------")
print("")


if not os.path.exists('data'):
    os.makedirs('data')

df.to_csv('data/weather.csv', index=False)
print(f"Data saved as weather.csv")