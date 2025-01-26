from imports import *

from ._player import player
from ._sysinfo import sysinfo
from ._volume import volume
from ._weather import weather


class sideLeft(WaylandWindow):
    def __init__(
        self,
    ):
        super().__init__(
            title="side-left",
            layer="top",
            anchor="top bottom left",
            margin="4px 4px 4px 4px",
            exclusivity="none",
            visible=False,
            name="side-left",
            v_expand=True,
            h_expand=False,
        )

        self.main = CenterBox(name="side-left-container", size=450, orientation="v")

        self.player = player()
        self.sysinfo = sysinfo()
        self.weather = weather()
        self.volume = volume()

        self.main.add_start(self.player)
        self.main.add_start(self.sysinfo)
        self.main.add_start(self.weather)
        self.main.add_start(self.volume)

        self.add(self.main)

    def toggle(self):
        self.set_visible(not self.is_visible())
