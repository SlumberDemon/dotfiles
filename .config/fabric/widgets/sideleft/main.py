from fabric.widgets import CenterBox, Label, WaylandWindow

from ._player import player


class sideLeft(WaylandWindow):
    def __init__(
        self,
    ):
        super().__init__(
            title="side-left",
            layer="top",
            anchor="top bottom left",
            margin="4px 4px 4px 4px",
            exclusive=False,
            visible=False,
            name="side-left",
            v_expand=True,
            h_expand=False,
        )

        self.main = CenterBox(name="side-left-container", size=450)

        self.player = player()

        self.main.add(self.player)

        self.add(self.main)

    def toggle(self):
        self.set_visible(not self.is_visible())
