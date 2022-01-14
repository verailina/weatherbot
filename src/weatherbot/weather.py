import logging
import os
import datetime
import pytz
import requests
from pathlib import Path
from typing import Dict, List, NamedTuple


def get_weather_key() -> str:
    weather_key = os.environ.get("WEATHER_KEY")
    if weather_key is None:
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

    result = request.json()
    if "data" not in result:
        result = get_weather_forecast_dummy()
    return result


def get_weather_forecast_dummy():
    return {'data': {'timelines': [
    {'timestep': '1h', 'startTime': '2022-01-12T22:00:00+01:00',
     'endTime': '2022-01-13T22:00:00+01:00', 'intervals': [
        {'startTime': '2022-01-12T22:00:00+01:00',
         'values': {'precipitationIntensity': 0, 'precipitationType': 0,
                    'temperature': 3.08}},
        {'startTime': '2022-01-12T23:00:00+01:00',
         'values': {'precipitationIntensity': 0, 'precipitationType': 0,
                    'temperature': 3}},
        {'startTime': '2022-01-13T00:00:00+01:00',
         'values': {'precipitationIntensity': 0, 'precipitationType': 0,
                    'temperature': 2.96}},
        {'startTime': '2022-01-13T01:00:00+01:00',
         'values': {'precipitationIntensity': 0, 'precipitationType': 0,
                    'temperature': 2.86}},
        {'startTime': '2022-01-13T02:00:00+01:00',
         'values': {'precipitationIntensity': 0, 'precipitationType': 0,
                    'temperature': 2.61}},
        {'startTime': '2022-01-13T03:00:00+01:00',
         'values': {'precipitationIntensity': 0, 'precipitationType': 0,
                    'temperature': 2.34}},
        {'startTime': '2022-01-13T04:00:00+01:00',
         'values': {'precipitationIntensity': 0, 'precipitationType': 0,
                    'temperature': 2.22}},
        {'startTime': '2022-01-13T05:00:00+01:00',
         'values': {'precipitationIntensity': 0, 'precipitationType': 0,
                    'temperature': 2.19}},
        {'startTime': '2022-01-13T06:00:00+01:00',
         'values': {'precipitationIntensity': 0, 'precipitationType': 0,
                    'temperature': 1.99}},
        {'startTime': '2022-01-13T07:00:00+01:00',
         'values': {'precipitationIntensity': 0, 'precipitationType': 0,
                    'temperature': 1.68}},
        {'startTime': '2022-01-13T08:00:00+01:00',
         'values': {'precipitationIntensity': 0, 'precipitationType': 0,
                    'temperature': 1.24}},
        {'startTime': '2022-01-13T09:00:00+01:00',
         'values': {'precipitationIntensity': 0, 'precipitationType': 0,
                    'temperature': 0.86}},
        {'startTime': '2022-01-13T10:00:00+01:00',
         'values': {'precipitationIntensity': 0, 'precipitationType': 0,
                    'temperature': 0.97}},
        {'startTime': '2022-01-13T11:00:00+01:00',
         'values': {'precipitationIntensity': 0, 'precipitationType': 0,
                    'temperature': 1.72}},
        {'startTime': '2022-01-13T12:00:00+01:00',
         'values': {'precipitationIntensity': 0, 'precipitationType': 0,
                    'temperature': 2.56}},
        {'startTime': '2022-01-13T13:00:00+01:00',
         'values': {'precipitationIntensity': 0, 'precipitationType': 0,
                    'temperature': 3.65}},
        {'startTime': '2022-01-13T14:00:00+01:00',
         'values': {'precipitationIntensity': 0, 'precipitationType': 0,
                    'temperature': 4.69}},
        {'startTime': '2022-01-13T15:00:00+01:00',
         'values': {'precipitationIntensity': 0, 'precipitationType': 0,
                    'temperature': 5.42}},
        {'startTime': '2022-01-13T16:00:00+01:00',
         'values': {'precipitationIntensity': 0, 'precipitationType': 0,
                    'temperature': 5.58}},
        {'startTime': '2022-01-13T17:00:00+01:00',
         'values': {'precipitationIntensity': 0, 'precipitationType': 0,
                    'temperature': 5.01}},
        {'startTime': '2022-01-13T18:00:00+01:00',
         'values': {'precipitationIntensity': 0, 'precipitationType': 0,
                    'temperature': 4.13}},
        {'startTime': '2022-01-13T19:00:00+01:00',
         'values': {'precipitationIntensity': 0, 'precipitationType': 0,
                    'temperature': 3.63}},
        {'startTime': '2022-01-13T20:00:00+01:00',
         'values': {'precipitationIntensity': 0, 'precipitationType': 0,
                    'temperature': 3.21}},
        {'startTime': '2022-01-13T21:00:00+01:00',
         'values': {'precipitationIntensity': 0, 'precipitationType': 0,
                    'temperature': 2.59}},
        {'startTime': '2022-01-13T22:00:00+01:00',
         'values': {'precipitationIntensity': 0, 'precipitationType': 0,
                    'temperature': 2.32}}]}]}}


class WeatherPoint(NamedTuple):
    date: datetime.datetime
    temperature: float

    @staticmethod
    def from_values(date: str, values: Dict) -> "WeatherPoint":
        date = datetime.datetime.fromisoformat(date)
        return WeatherPoint(
            date=date,
            temperature=values["temperature"])


def parse_weather_forecast(forecast: Dict) -> List[WeatherPoint]:
    timelines = forecast["data"]["timelines"]
    if len(timelines) == 0:
        return []
    intervals = timelines[0]["intervals"]
    return [WeatherPoint.from_values(interval["startTime"], interval["values"])
            for interval in intervals]


# forecast = get_weather_forecast()
# print(parse_weather_forecast(forecast))
