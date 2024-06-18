import json
import time

from fabric.hyprland.service import Hyprland
from fabric.widgets import Box, EventBox

connection = Hyprland()

workspaceData = connection.send_command("j/activeworkspace").reply
activeWorkspace = json.loads(workspaceData.decode("utf-8"))["name"]


# Scroll event credits to gummybearalbum in fabric discord


def on_scroll(widget, event):
    if event.delta_x != 0:
        on_scroll.scroll_value += event.delta_x
        if on_scroll.scroll_value >= 5 * on_scroll.multiple:
            on_scroll.multiple += 1
            connection.send_command(f"/dispatch workspace e+1")
        if on_scroll.scroll_value <= -5 * on_scroll.multiple:
            on_scroll.multiple += 1
            connection.send_command(f"/dispatch workspace e-1")
    else:
        on_scroll.multiple = 1
        on_scroll.scroll_value = 0


on_scroll.multiple = 1
on_scroll.scroll_value = 0


scrollBox = Box(name="center-minimap")
minimap = EventBox(events="smooth-scroll", children=scrollBox)

minimap.connect("scroll-event", on_scroll)
