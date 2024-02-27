import fabric
from imports import *
from widgets.bar.main import statusBar


def check_colors(*args):
    return set_stylesheet_from_file(get_relative_path("css/main.css"))


monitor = monitor_file(
    get_relative_path("./css/colors.css"), "none"
)  # when developing do main.css else colors.css
monitor.connect("changed", check_colors)

if __name__ == "__main__":
    bar = statusBar()

    set_stylesheet_from_file(get_relative_path("./css/main.css"))

    fabric.start()
