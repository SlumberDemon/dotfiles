import fabric
from fabric.utils import get_relative_path, monitor_file, set_stylesheet_from_file
from widgets.bar.main import statusBar
from widgets.screencorners.main import leftCorners, rightCorners
from widgets.sideleft.main import sideLeft


def check_css(*args):
    return set_stylesheet_from_file("css/main.css")


monitor = monitor_file(
    get_relative_path("css/color.css"), "none"
)  # change to main.css when developing
monitor.connect("changed", check_css)

if __name__ == "__main__":
    bar = statusBar()
    corners = leftCorners(), rightCorners()
    sideLeft = sideLeft()

    sideLeft.hide()

    set_stylesheet_from_file("css/main.css")

    fabric.start()
