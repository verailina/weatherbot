from pathlib import Path
import datetime
from typing import List

import plotly.graph_objects as go

from weatherbot.weather import WeatherPoint


def get_weather_image(points: List[WeatherPoint]) -> bytes:
    times = [point.date for point in points]
    tickvals = [point.date.strftime("%H:%M") for point in points]
    temperatures = [point.temperature for point in points]
    marks = [round(point.temperature) for point in points]


    # Create figure
    fig = go.Figure(
        layout=go.Layout(paper_bgcolor="rgba(0,0,0,0)",
                         plot_bgcolor="rgba(0,0,0,0)"))

    # Add trace
    fig.add_trace(
        go.Scatter(
            mode="markers+text",
            textposition="top center",
            x=times,
            y=temperatures,
            text=marks)
    )

    fig.add_trace(
        go.Scatter(
            x=times,
            y=temperatures,
            fill="tozeroy",
            line=dict(color="#ffe476"),
            fillcolor="#63a885"
            )
    )
    # Set templates
    fig.update_layout(width=1000,
                      height=500,
                      margin=dict(
                          l=10,
                          r=10,
                          b=20,
                          t=20,
                          pad=10
                      ),
                      font=dict(
                          family="Droid Serif, monospace",
                          size=20,
                          color="#ffe476"
                      ),
                      showlegend=False)
    fig.update_xaxes(showgrid=False)
    fig.update_yaxes(showgrid=False, tickvals=[])
    with Path("weather.jpg").open("wb") as out_image:
        out_image.write(fig.to_image("jpeg"))

    return fig.to_image("jpeg")


#get_weather_image([WeatherPoint(date=datetime.datetime(2022, 1, 13, 0, 0, tzinfo=datetime.timezone(datetime.timedelta(seconds=3600))), temperature=2.82), WeatherPoint(date=datetime.datetime(2022, 1, 13, 1, 0, tzinfo=datetime.timezone(datetime.timedelta(seconds=3600))), temperature=2.82), WeatherPoint(date=datetime.datetime(2022, 1, 13, 2, 0, tzinfo=datetime.timezone(datetime.timedelta(seconds=3600))), temperature=2.77), WeatherPoint(date=datetime.datetime(2022, 1, 13, 3, 0, tzinfo=datetime.timezone(datetime.timedelta(seconds=3600))), temperature=2.61), WeatherPoint(date=datetime.datetime(2022, 1, 13, 4, 0, tzinfo=datetime.timezone(datetime.timedelta(seconds=3600))), temperature=2.37), WeatherPoint(date=datetime.datetime(2022, 1, 13, 5, 0, tzinfo=datetime.timezone(datetime.timedelta(seconds=3600))), temperature=2.17), WeatherPoint(date=datetime.datetime(2022, 1, 13, 6, 0, tzinfo=datetime.timezone(datetime.timedelta(seconds=3600))), temperature=1.92), WeatherPoint(date=datetime.datetime(2022, 1, 13, 7, 0, tzinfo=datetime.timezone(datetime.timedelta(seconds=3600))), temperature=1.58), WeatherPoint(date=datetime.datetime(2022, 1, 13, 8, 0, tzinfo=datetime.timezone(datetime.timedelta(seconds=3600))), temperature=1.34), WeatherPoint(date=datetime.datetime(2022, 1, 13, 9, 0, tzinfo=datetime.timezone(datetime.timedelta(seconds=3600))), temperature=1.12), WeatherPoint(date=datetime.datetime(2022, 1, 13, 10, 0, tzinfo=datetime.timezone(datetime.timedelta(seconds=3600))), temperature=1.18), WeatherPoint(date=datetime.datetime(2022, 1, 13, 11, 0, tzinfo=datetime.timezone(datetime.timedelta(seconds=3600))), temperature=1.79), WeatherPoint(date=datetime.datetime(2022, 1, 13, 12, 0, tzinfo=datetime.timezone(datetime.timedelta(seconds=3600))), temperature=2.74), WeatherPoint(date=datetime.datetime(2022, 1, 13, 13, 0, tzinfo=datetime.timezone(datetime.timedelta(seconds=3600))), temperature=3.79), WeatherPoint(date=datetime.datetime(2022, 1, 13, 14, 0, tzinfo=datetime.timezone(datetime.timedelta(seconds=3600))), temperature=4.77), WeatherPoint(date=datetime.datetime(2022, 1, 13, 15, 0, tzinfo=datetime.timezone(datetime.timedelta(seconds=3600))), temperature=5.46), WeatherPoint(date=datetime.datetime(2022, 1, 13, 16, 0, tzinfo=datetime.timezone(datetime.timedelta(seconds=3600))), temperature=5.6), WeatherPoint(date=datetime.datetime(2022, 1, 13, 17, 0, tzinfo=datetime.timezone(datetime.timedelta(seconds=3600))), temperature=4.96), WeatherPoint(date=datetime.datetime(2022, 1, 13, 18, 0, tzinfo=datetime.timezone(datetime.timedelta(seconds=3600))), temperature=4.05), WeatherPoint(date=datetime.datetime(2022, 1, 13, 19, 0, tzinfo=datetime.timezone(datetime.timedelta(seconds=3600))), temperature=3.53), WeatherPoint(date=datetime.datetime(2022, 1, 13, 20, 0, tzinfo=datetime.timezone(datetime.timedelta(seconds=3600))), temperature=3.14), WeatherPoint(date=datetime.datetime(2022, 1, 13, 21, 0, tzinfo=datetime.timezone(datetime.timedelta(seconds=3600))), temperature=2.8), WeatherPoint(date=datetime.datetime(2022, 1, 13, 22, 0, tzinfo=datetime.timezone(datetime.timedelta(seconds=3600))), temperature=2.47), WeatherPoint(date=datetime.datetime(2022, 1, 13, 23, 0, tzinfo=datetime.timezone(datetime.timedelta(seconds=3600))), temperature=2.33), WeatherPoint(date=datetime.datetime(2022, 1, 14, 0, 0, tzinfo=datetime.timezone(datetime.timedelta(seconds=3600))), temperature=2.1)])