from fabric.widgets import WaylandWindow, CenterBox, Label


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
            visible=True,
            name="side-left",
            v_expand=True,
            h_expand=False,
        )

        self.main = CenterBox(name="side-left-container", size=450)

        self.main.add_center(Label("hi"))

        self.add(self.main)
