import datetime

import psutil

from imports import *

batteryInfo = Fabricate(
    poll_from=lambda _: {
        "battery": int(
            psutil.sensors_battery().percent
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
        # led.set_tooltip_text(f"{value['battery']}% ~ {datetime.timedelta(seconds=value['secsleft'])}{(' ~ Charging' if value['charging'] is True else '')}"),
        led.set_style(
            f"background-color: {led_color(value['battery'], value['charging'])};"
        ),
    ),
)
# tooltip_text="0"
led = Button(name="led", style="background-color: #808080;")


def led_color(battery: int, charging: bool) -> str:
    if not charging:
        if 80 <= battery <= 100:
            return "#10C463"
        elif 50 <= battery <= 80:
            return "#FFA07A"
        elif 20 <= battery <= 50:
            return "#EEBB03"
        elif 1 <= battery <= 20:
            return "#E63946"
    else:
        return "#9370DB"
