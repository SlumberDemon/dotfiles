from imports import *

from ._quicksettings import quicksettings


class sideRight(WaylandWindow):
    def __init__(
        self,
    ):
        super().__init__(
            title="side-right",
            layer="top",
            anchor="top bottom right",
            margin="4px 4px 4px 4px",
            exclusivity="none",
            visible=False,
            name="side-right",
            v_expand=True,
            h_expand=False,
        )

        self.main = CenterBox(name="side-right-container", size=450, orientation="v")

        self.quicksettings = quicksettings()

        self.main.add_start(self.quicksettings)

        self.add(self.main)

    def toggle(self):
        self.set_visible(not self.is_visible())
