import dotenv

from imports import *
from widgets.osd.notifications import notifcationPopup
from widgets.bar.main import statusBar
from widgets.launcher.main import Launcher
from widgets.screencorners.main import leftCorners, rightCorners
from widgets.sideleft.main import sideLeft
from widgets.sideright.main import sideRight

dotenv.load_dotenv()


def check_css(*args):
    return set_stylesheet_from_file("./css/main.css")


if __name__ == "__main__":
    monitor = monitor_file(get_relative_path("./css/color.css"), "none")
    monitor.connect("changed", check_css)

    notifications = notifcationPopup()

    bar = statusBar()
    corners = leftCorners(), rightCorners()
    launcher = Launcher()
    sideLeft = sideLeft()
    sideRight = sideRight()

    # Hide initially

    launcher.hide()
    sideLeft.hide()
    sideRight.hide()

    app = Application()

    app.set_stylesheet_from_file("css/main.css")
    app.run()
