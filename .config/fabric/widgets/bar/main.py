from fabric.widgets import CenterBox, WaylandWindow

from ._batteryindicator import batteryPanel
from ._tray import trayPanel
from .center import center


class statusBar(WaylandWindow):
    def __init__(self):
        super().__init__(
            title="bar",
            layer="top",
            anchor="bottom",
            margin="0px 0px 5px 0px",
            exclusive=True,
            visible=True,
        )

        self.main = CenterBox(name="bar")
        self.center = center()

        self.right = batteryPanel()
        self.left = trayPanel()

        self.main.add_start(self.left)
        self.main.add_center(self.center)
        self.main.add_end(self.right)
        self.add(self.main)

        self.show()
