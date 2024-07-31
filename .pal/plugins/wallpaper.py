import argparse
import os
import random
import subprocess
from pathlib import Path

from InquirerPy import inquirer


class Plugin:
    def __init__(self, commands: argparse._SubParsersAction) -> None:
        self.command = commands.add_parser(
            "wallpaper",
            help="Set current wallpaper",
            description="Set current wallpaper",
        )
        self.function = {
            "name": "wallpaper",
            "description": "Set current wallpaper",
            "parameters": {
                "type": "object",
                "properties": {
                    "file": {
                        "type": "string",
                        "description": "Filename of image to set as wallpaper",
                    }
                },
                "required": ["file"],
            },
        }

    def run(self, args: argparse.Namespace, parser: argparse.ArgumentParser) -> None:
        if args.random:
            files = os.listdir(Path("Pictures"))
            file = random.choice(files)
        else:
            file = args.file

        if not file:
            files = os.listdir(Path("Pictures"))
            file = inquirer.fuzzy(
                message="Select wallpaper:",
                choices=files,
                raise_keyboard_interrupt=False,
                mandatory=False,
                long_instruction="Current: "
                + self.function["parameters"]["properties"]["file"]["enum"][
                    0
                ],  # set current wall
            ).execute()

        if file:
            if args.preview:
                os.system(
                    f"swww img $HOME/Pictures/{file} --transition-step 100 --transition-fps 60 --transition-type grow --transition-angle 30 --transition-duration 1"
                )
                os.system(
                    "wal -i $(swww query | grep -oP '(?<=currently displaying: image: ).*' | uniq)"
                )
            else:
                os.system(f"kitten icat $HOME/Pictures/{file}")

    def setup(self):
        current = subprocess.check_output(
            "swww query | grep -oP '(?<=currently displaying: image: /home/sofa/Pictures/).*' | uniq",
            shell=True,
            text=True,
        )

        self.function["parameters"]["properties"]["file"]["enum"] = [
            f"{str(current).strip()}"
        ]

        self.command.add_argument(
            "-f", "--file", help="Filename of image to set as wallpaper", action="store"
        )
        self.command.add_argument(
            "-p",
            "--preview",
            help="Preview file without setting",
            action="store_false",
        )
        self.command.add_argument(
            "-r", "--random", help="Set random wallpaper", action="store_true"
        )
