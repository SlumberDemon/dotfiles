from fabric.utils import bulk_connect
from fabric.widgets import Box, Revealer, SystemTray

from ._profile import profile

details = SystemTray(name="left-tray-details", icon_size=20)
tray = Box(children=details, name="left-tray")


class trayPanel(Box):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        self.tray = tray
        self.profile = profile

        self.revealer = Revealer(transition_type="slide-left", transition_duration=1000)
        self.revealer.add(self.tray)

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

        self.add(self.revealer)
