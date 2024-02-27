from imports import *
from widgets.sidepanels.main import *

from .center import center


class statusBar(Window):
    def __init__(
        self,
    ):
        super().__init__(
            layer="top",
            anchor="bottom",
            margin="0px 0px 5px 0px",
            exclusive=True,
            visible=True,
        )

        self.main = CenterBox(name="main")

        self.center = center()

        self.right = slideAnimationRight()
        self.left = slideAnimationLeft()

        self.main.add_center(self.left)
        self.main.add_center(self.center)
        self.main.add_center(self.right)

        self.add(self.main)

        self.show()
