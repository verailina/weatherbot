import logging
import datetime
import requests
from pathlib import Path


def get_weather_key() -> str:
    with Path("weatherkey.txt").open() as weather_key_file:
        weather_key = weather_key_file.readline()
    return weather_key


get_timeline_url = "https://api.tomorrow.io/v4/timelines"
weather_key = get_weather_key()
location = [48.882272, 2.274652]
fields = [
  "precipitationIntensity",
  "precipitationType",
  "temperature",
]
units = "metric"
timesteps = ["current", "1d"]
now = datetime.datetime.now()
startTime = datetime.datetime(now.year, now.month, now.day, now.hour, now.minute, tzinfo=datetime.timezone.fromutc())
end = now + datetime.timedelta(days=7)
time_zone = "Europe/Paris"
params = {"apikey": weather_key,
          "location": f"{location[0]}, {location[1]}",
          "units": units,
          "fields": ",".join(fields),
          "timesteps": ",".join(timesteps),
          "timezone": time_zone,
          "startTime": now.isoformat(),
          "endTime": end.isoformat(),
          }
print(now.isoformat())
request = requests.get(url=get_timeline_url, params=params)

print(request.json())
