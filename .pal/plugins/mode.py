import os
import re
import argparse


class Plugin:
    def __init__(self, commands: argparse._SubParsersAction) -> None:
        self.command = commands.add_parser(
            "mode",
            help="Light/Dark mode switcher",
            description="Light/Dark mode switcher",
        )
        self.function = {
            "name": "mode",
            "description": "Switch between light/dark theme",
            "parameters": {
                "type": "object",
                "properties": {
                    "theme": {
                        "type": "string",
                        "description": "The theme that the current mode is set to",
                        "enum": ["light", "dark"],
                    }
                },
                "required": ["theme"],
            },
        }

    def run(self, args: argparse.Namespace, parser: argparse.ArgumentParser) -> None:
        if args.light or args.theme == "light":
            os.system("gsettings set org.gnome.desktop.interface gtk-theme 'adw-gtk3'")
            os.system(
                "gsettings set org.gnome.desktop.interface color-scheme 'prefer-light'"
            )
            os.system(
                "echo \"@import url('./light.css');\" > $HOME/.config/wofi/styles/color.css"
            )
            os.system(
                "echo \"@import url('./colors/light.css');\" > $HOME/.config/fabric/css/color.css"
            )
            os.system(
                "wal -i $(swww query | grep -oP '(?<=currently displaying: image: ).*' | uniq) -l"
            )
        elif args.dark or args.theme == "dark":
            os.system(
                "gsettings set org.gnome.desktop.interface gtk-theme 'adw-gtk3-dark'"
            )
            os.system(
                "gsettings set org.gnome.desktop.interface color-scheme 'prefer-dark'"
            )
            os.system(
                "echo \"@import url('./dark.css');\" > $HOME/.config/wofi/styles/color.css"
            )
            os.system(
                "echo \"@import url('./colors/dark.css');\" > $HOME/.config/fabric/css/color.css"
            )
            os.system(
                "wal -i $(swww query | grep -oP '(?<=currently displaying: image: ).*' | uniq)"
            )

    def setup(self) -> None:
        self.command.add_argument(
            "-l", "--light", help="Light mode", action="store_true"
        )
        self.command.add_argument("-d", "--dark", help="Dark mode", action="store_true")
        self.command.add_argument("-t", "--theme", help="Mode (AI)", action="store")
