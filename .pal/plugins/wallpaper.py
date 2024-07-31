import os
import subprocess
import argparse
from InquirerPy import inquirer
from pathlib import Path

class Plugin:
    def __init__(self, commands: argparse._SubParsersAction) -> None:
        self.command = commands.add_parser(
            "wallpaper", help="Set current wallpaper", description="Set current wallpaper"
        )
        self.function = {
            "name": "wallpaper",
            "description": "Set current wallpaper",
            "parameters": {
                "type": "object",
                "properties": {
                    "file": {
                        "type": "string",
                        "description": "Filename of image to set as wallpaper"
                    }
                },
                "required": ["file"]
            }
        }

    def run(self, args: argparse.Namespace, parser: argparse.ArgumentParser) -> None:
        file = args.file

        if not file:
            files = os.listdir(Path("Pictures"))
            file = inquirer.fuzzy(
                message="Select wallpaper:",
                choices=files,
                raise_keyboard_interrupt=False,
                mandatory=False,
                long_instruction="Current: " + self.function["parameters"]["properties"]["file"]["enum"][0], # set current wall
            ).execute()

        if file:
            os.system(f"swww img $HOME/Pictures/{file} --transition-step 100 --transition-fps 60 --transition-type grow --transition-angle 30 --transition-duration 1")
            os.system("wal -i $(swww query | grep -oP '(?<=currently displaying: image: ).*' | uniq)")
            

    def setup(self):
        current = subprocess.check_output("swww query | grep -oP '(?<=currently displaying: image: /home/sofa/Pictures/).*' | uniq", shell=True, text=True)
        
        self.function["parameters"]["properties"]["file"]["enum"] = [f"{str(current).strip()}"]
        
        self.command.add_argument(
            "-f", "--file", help="Filename of image to set as wallpaper", action="store"
        )
