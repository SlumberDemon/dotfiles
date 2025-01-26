from imports import *

logo = Button(
    name="logo",
    child=Svg(
        size=20,
        svg_file=get_relative_path("../../assets/fabric-symbolic.svg"),
        style="fill: #3D9A6F;",
    ),
)
