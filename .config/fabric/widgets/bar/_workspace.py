import json

from imports import *

connection = Hyprland()

workspaceData = connection.send_command("j/activeworkspace").reply
activeWorkspace = json.loads(workspaceData.decode("utf-8"))["name"]
workspace = Label(label=f"Workspace {activeWorkspace}", name="center-workspace")


def on_workspace(obj, signal):
    global activeWorkspace
    activeWorkspace = json.loads(signal.data[0])
    workspace.set_label(f"Workspace {activeWorkspace}")


connection.connect("event::workspace", on_workspace)
