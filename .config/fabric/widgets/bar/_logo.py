from fabric.utils import get_relative_path
from fabric.widgets import Button, Svg

logo = Button(
    name="center-logo",
    child=Svg(
        size=20,
        svg_file=get_relative_path("../../assets/deta-symbolic.svg"),
        # style="fill: #1793D1;",
    ),
)
