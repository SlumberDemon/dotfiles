from imports import *

box = Box(
    children=Svg(
        size=20,
        svg_file=get_relative_path("../../assets/deta-symbolic.svg"),
    )
)

logo = Button(name="logo", child=box)
