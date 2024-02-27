import datetime

import psutil

from imports import *
from widgets.bar.profile import profile


class panelTray(Box):
    def __init__(self):
        super().__init__(name="paneltray")

        self.details = SystemTray(name="tray")

        self.add(self.details)


slideTray = Box(children=panelTray(), name="slidetray")


class slideAnimationLeft(Box):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        self.slideTray = slideTray

        self.profile = profile

        self.revealer = Revealer(transition_type="slide-left", transition_duration=1000)
        self.revealer.add(self.slideTray)

        bulk_connect(
            self.profile,
            {
                "enter-notify-event": lambda *args: self.profile.change_cursor(
                    "pointer"
                ),
                "leave-notify-event": lambda *args: self.profile.change_cursor(
                    "default"
                ),
                "button-press-event": lambda *args: self.revealer.set_reveal_child(
                    not self.revealer.get_reveal_child()
                ),
            },
        )

        self.add(self.profile)
        self.add(self.revealer)
