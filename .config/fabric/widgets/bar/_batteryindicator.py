import datetime

import psutil

from fabric.utils import bulk_connect
from fabric.utils.fabricator import Fabricator
from fabric.widgets import Box, Button, Label, Revealer

batteryInfo = Fabricator(
    poll_from=lambda: {
        "battery": int(
            psutil.sensors_battery().percent
            if psutil.sensors_battery() is not None
            else 0
        ),
        "secsleft": int(
            psutil.sensors_battery().secsleft
            if psutil.sensors_battery() is not None
            else 0
        ),
        "charging": bool(
            psutil.sensors_battery().power_plugged
            if psutil.sensors_battery() is not None
            else False
        ),
    },
    interval=1000,
)

batteryInfo.connect(
    "changed",
    lambda _, value: (
        details.set_label(
            f"{value['battery']}% ~ {('Charging' if value['charging'] is True else str(datetime.timedelta(seconds=value['secsleft'])))}"
        ),
        indicator.set_style(
            f"background-color: {indicator_color(value["battery"], value['charging'])}"
        ),
    ),
)

details = Label(label="0", name="right-battery-details")
battery = Box(children=details, name="right-battery")
indicator = Button(name="center-indicator", style="background-color: #808080;")


def indicator_color(battery: int, charging: bool) -> str:
    if not charging:
        if 80 <= battery <= 100:
            return "#0EC463"
        elif 50 <= battery <= 80:
            return "#FFA07A"
        elif 20 <= battery <= 50:
            return "#EEBB03"
        elif 1 <= battery <= 20:
            return "#E63946"
    return "#9370DB"


class batteryPanel(Box):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        self.battery = battery
        self.indicator = indicator

        self.revealer = Revealer(
            transition_type="slide-right", transition_duration=1000
        )
        self.revealer.add(self.battery)

        bulk_connect(
            self.indicator,
            {
                "enter-notify-event": lambda *args: self.indicator.change_cursor(
                    "pointer"
                ),
                "leave-notify-event": lambda *args: self.indicator.change_cursor(
                    "default"
                ),
                "button-press-event": lambda *args: self.revealer.set_reveal_child(
                    not self.revealer.get_reveal_child()
                ),
            },
        )

        self.add(self.revealer)
