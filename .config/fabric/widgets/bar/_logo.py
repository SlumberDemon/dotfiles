from fabric.utils import get_relative_path
from fabric.widgets import Box, Button, Svg

box = Box(
    children=Svg(size=20, svg_file=get_relative_path("../../assets/deta-symbolic.svg"))
)

logo = Button(name="center-logo", child=box)
