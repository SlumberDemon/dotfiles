from imports import *

from .globe import globe
from .logo import logo
from .pwcontainer import pwcontainer
from .tlcontainer import tlcontainer
from .workspaces import workspaces
from .workspacescroll import workspacescroll


class center(Box):
    def __init__(self):
        super().__init__(
            name="center",
            children=[pwcontainer, globe, tlcontainer, logo, workspacescroll],
        )

        for connector in [globe, logo]:
            bulk_connect(
                connector,
                {
                    "enter-notify-event": lambda *args: self.change_cursor("pointer"),
                    "leave-notify-event": lambda *args: self.change_cursor("default"),
                    "button-press-event": self.on_button_press,
                },
            )

    def on_button_press(
        self, button: Button, event
    ):  # https://docs.gtk.org/gdk3/enum.EventType.html
        if event.button == 1 and event.type == 4:  # Single Click
            if button.get_name() == "globe":
                exec_shell_command("sofa full -r")
            elif button.get_name() == "logo":
                exec_shell_command("rofi -show drun")

        """
        # Doesn't allow for multiple events

        elif event.button == 1 and event.type == 5:  # Double Click
            if button.get_name() == "globe":
                exec_shell_command("sofa color -m light")
        elif event.button == 1 and event.type == 6:  # Triple Click
            if button.get_name() == "globe":
                exec_shell_command("sofa color -m dark")
            elif button.get_name() == "logo":
                exec_shell_command("systemctl suspend")
        """
