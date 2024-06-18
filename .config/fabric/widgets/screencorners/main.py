from fabric.widgets import WaylandWindow, CenterBox, Box
from fabric.widgets.shapes import Corner


class leftCorners(WaylandWindow):
    def __init__(
        self,
    ):
        super().__init__(
            title="corners-left",
            layer="overlay",  # overlay (needs fixing with hypr layerrules)
            exclusive=False,
            anchor="left top bottom",
            margin="0px 0px -51px 0px",
        )

        self.right = CenterBox(
            orientation="v",
            start_children=[
                Corner(
                    orientation="top-left",
                    size=10,
                    name="corner-top-left",
                )
            ],
            end_children=[
                Corner(
                    orientation="bottom-left",
                    size=10,
                    name="corner-bottom-left",
                )
            ],
        )

        self.add(Box(orientation="h", children=[self.right]))

        self.show()


class rightCorners(WaylandWindow):
    def __init__(
        self,
    ):
        super().__init__(
            title="corners-right",
            layer="overlay",  # overlay (needs fixing with hypr layerrules)
            exclusive=False,
            anchor="right top bottom",
            margin="0px 0px -51px 0px",
        )

        self.right = CenterBox(
            orientation="v",
            start_children=[
                Corner(
                    orientation="top-right",
                    size=10,
                    name="corner-top-right",
                )
            ],
            end_children=[
                Corner(
                    orientation="bottom-right",
                    size=10,
                    name="corner-bottom-right",
                )
            ],
        )

        self.add(Box(orientation="h", children=[self.right]))

        self.show()
