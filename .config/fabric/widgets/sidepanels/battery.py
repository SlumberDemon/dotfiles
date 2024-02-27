import datetime

import psutil

from imports import *
from widgets.bar.batteryindicator import led


class panelBattery(Box):
    def __init__(self):
        super().__init__(name="panelbattery")

        self.details = Label(label="0", name="battery")

        self.add(self.details)

        batteryInfo = Fabricate(
            poll_from=lambda _: {
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
                self.details.set_label(
                    f"{value['battery']}% ~ {('Charging' if value['charging'] is True else str(datetime.timedelta(seconds=value['secsleft'])))}"
                ),
            ),
        )


slideBattery = Box(children=panelBattery(), name="slidebattery")


class slideAnimationRight(Box):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        self.slideBattery = slideBattery

        self.led = led

        self.revealer = Revealer(
            transition_type="slide-right", transition_duration=1000
        )
        self.revealer.add(self.slideBattery)

        bulk_connect(
            self.led,
            {
                "enter-notify-event": lambda *args: self.led.change_cursor("pointer"),
                "leave-notify-event": lambda *args: self.led.change_cursor("default"),
                "button-press-event": lambda *args: self.revealer.set_reveal_child(
                    not self.revealer.get_reveal_child()
                ),
            },
        )

        self.add(self.led)
        self.add(self.revealer)
