from fabric.utils import truncate
from imports import *


class volume(Box):
    def __init__(self) -> None:
        super().__init__(name="left-volume", h_expand=True, orientation="h")

        self.label = Label(
            label="Sound", h_align="start", v_align="start", name="volume-label"
        )
        self.slider = Scale(orientation="v", name="volume-slider", v_expand=True)

        self.children = CenterBox(
            orientation="v",
            h_expand=True,
            start_children=self.label,
            center_children=self.slider,
        )
