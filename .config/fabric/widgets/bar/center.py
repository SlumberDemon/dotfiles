from imports import *

from ._batteryindicator import indicator
from ._datetime import datetime
from ._globe import globe
from ._logo import logo
from ._minimap import minimap
from ._profile import profile
from ._workspace import workspace


class center(Box):
    def __init__(self, **kwargs) -> None:
        super().__init__(
            name="center",
            children=[
                Box(name="pwcontainer", children=[profile, workspace]),
                globe,
                Box(name="tlcontainer", children=[datetime, indicator]),
                logo,
                minimap,
            ],
        )

        for connector in [logo]:  # globe
            bulk_connect(
                connector,
                {
                    "enter-notify-event": lambda *args: self.set_cursor("pointer"),
                    "leave-notify-event": lambda *args: self.set_cursor("default"),
                    "button-press-event": self.on_button_press,
                },
            )

    def on_button_press(
        self, button: Button, event
    ):  # https://docs.gtk.org/gdk3/enum.EventType.html
        if event.button == 1 and event.type == 4:  # Single Click
            if button.get_name() == "center-logo":
                exec_shell_command("wofi --show drun --fork")
                # switch it to fabricast
