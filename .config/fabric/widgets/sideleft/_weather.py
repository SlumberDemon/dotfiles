import json
import os

from imports import *


class weather(Box):
    def __init__(self) -> None:
        super().__init__(name="left-weather", h_expand=True, orientation="h")

        self.weather_info = Fabricator(
            poll_from=f"curl -X GET 'http://api.weatherapi.com/v1/current.json?key={os.getenv('FABRIC_WEATHER_KEY')}&q={os.getenv('FABRIC_WEATHER_LOC')}&aqi=yes'",
            interval=1000 * 60 * 40,
        )

        self.temperature = Label(label="0", name="weather-temperature")
        self.condition_text = Label(
            label="None", name="weather-condition", h_align="start", v_align="start"
        )
        self.time = Label(label="Current · 00:00", name="weather-time")
        self.location = Label(label="None", name="weather-location")
        self.icon = Box(
            name="weather-icon",
        )

        self.details = Box(
            orientation="v",
            v_expand=True,
            v_align="center",
            children=[self.condition_text, Box(children=[self.location, self.time])],
        )

        def extract_metadata(_, value):
            data = json.loads(value)

            self.temperature.set_label(f"{round(int(data['current']['temp_c']))}°")
            self.condition_text.set_label(f"{data['current']['condition']['text']}")
            self.location.set_label(f"{data['location']['country']}")
            timestr = data["location"]["localtime"]
            self.time.set_label(f"Current · {timestr.split(' ', 1)[1]}")
            self.icon.set_style(
                f"background-image: url('http:{data['current']['condition']['icon']}');"
            )

        self.weather_info.connect("changed", extract_metadata)

        self.children = CenterBox(
            h_expand=True,
            center_children=[self.temperature, self.details, self.icon],
        )
