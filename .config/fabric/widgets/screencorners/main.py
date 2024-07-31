from fabric.widgets import Box, CenterBox, WaylandWindow
from fabric.widgets.shapes import Corner


class leftCorners(WaylandWindow):
    def __init__(
        self,
    ):
        super().__init__(
            title="corners-left",
            layer="overlay",
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
            layer="overlay",
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
