import logging
import datetime
import pytz
import requests
from pathlib import Path
from typing import Dict


def get_weather_key() -> str:
    with Path("weatherkey.txt").open() as weather_key_file:
        weather_key = weather_key_file.readline()
    return weather_key


def get_weather_forecast() -> Dict:
    location = [48.882272, 2.274652]
    fields = [
      "precipitationIntensity",
      "precipitationType",
      "temperature",
    ]

    time_zone = "Europe/Paris"
    tz_info = pytz.timezone(time_zone)
    now = datetime.datetime.now()
    start_time = datetime.datetime(
        now.year, now.month, now.day, now.hour, now.minute,
        tzinfo=tz_info)
    end = start_time + datetime.timedelta(days=1)

    request = requests.get(
        url="https://api.tomorrow.io/v4/timelines",
        params={"apikey": get_weather_key(),
                "location": f"{location[0]}, {location[1]}",
                "units": "metric",
                "fields": ",".join(fields),
                "timesteps": "1h",
                "timezone": time_zone,
                "startTime": start_time.isoformat(),
                "endTime": end.isoformat(),
                })

    return request.json()

