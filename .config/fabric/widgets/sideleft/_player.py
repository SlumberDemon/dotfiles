import json
import time

from icons import icons
from imports import *


class floating(WaylandWindow):
    def __init__(self):
        super().__init__(
            title="floating-player",
            layer="overlay",
            visible=False,
            name="floating-player",
            anchor="bottom left",
            v_expand=False,
            h_expand=False,
            margin="0px 0px -47px 4px",
            exclusivity="none",
        )

        self.art = Button(
            name="floating-art",
        )

        self.backward = Button(
            child=Label(
                markup=icons.backward, name="left-player-icon", style="font-size: 20px;"
            )
        )
        self.forward = Button(
            child=Label(
                markup=icons.forward, name="left-player-icon", style="font-size: 20px;"
            )
        )
        self.status = Label(
            markup=icons.stop, name="left-player-icon", style="font-size: 28px;"
        )
        self.play = Button(child=self.status)

        self.children = Overlay(
            child=self.art,
            overlays=CenterBox(
                v_align="center",
                name="floating-controls",
                start_children=self.backward,
                center_children=self.play,
                end_children=self.forward,
            ),
        )

        self.playerInfo = Fabricator(
            poll_from='playerctl --follow metadata --format \'{"status": "{{status}}", "artUrl": "{{mpris:artUrl}}", "title": "{{ markup_escape(title) }}", "artist": "{{ markup_escape(artist) }}"}\'',
            stream=True,
            interval=1000,
        )

        def extract_metadata(_, value):
            if value:
                data = json.loads(value)

                self.art.set_style(f"background-image: url('{data['artUrl']}');")
                self.status.set_markup(
                    (
                        icons.stop
                        if data["status"] == "Stopped"
                        else (
                            icons.pause if data["status"] == "Playing" else icons.play
                        )
                    )
                )

            else:
                self.status.set_markup(icons.stop)

        self.playerInfo.connect("changed", extract_metadata)

        for connector in [self.backward, self.play, self.forward, self.art]:
            bulk_connect(
                connector,
                {
                    "enter-notify-event": lambda *args: self.set_cursor("pointer"),
                    "leave-notify-event": lambda *args: self.set_cursor("default"),
                    "button-press-event": self.on_button_press,
                },
            )

    def on_button_press(self, button: Button, event):
        if event.button == 1 and event.type == 4:
            if button == self.backward:
                exec_shell_command("playerctl previous")
            elif button == self.play:
                exec_shell_command("playerctl play-pause")
            elif button == self.forward:
                exec_shell_command("playerctl next")
        elif event.button == 1 and event.type == 5:
            if button == self.art:
                self.hide()

    def toggle(self):
        self.set_visible(not self.is_visible())


class player(Box):
    def __init__(self) -> None:
        super().__init__(
            name="left-player",
            h_expand=True,
            orientation="h",
        )

        self.art = Button(name="left-player-art")
        self.title = Label(
            label="Nothing playing",
            name="left-player-title",
            justification="center",
            ellipsization="end",
            character_max_width=24,
        )
        self.artist = Label(
            name="left-player-artist",
            justification="center",
            ellipsization="end",
            character_max_width=20,
        )

        self.backward = Button(
            child=Label(markup=icons.backward, name="left-player-icon")
        )
        self.forward = Button(
            child=Label(markup=icons.forward, name="left-player-icon")
        )
        self.status = Label(
            markup=icons.stop, name="left-player-icon", style="font-size: 36px;"
        )
        self.play = Button(child=self.status)

        self.controls = CenterBox(
            name="left-player-controls",
            start_children=[self.backward],
            center_children=[self.play],
            end_children=[self.forward],
            orientation="h",
            h_expand=True,
        )
        self.info = Box(
            name="left-player-info",
            children=[self.title, self.artist, self.controls],
            orientation="v",
            v_align="center",
            h_expand=True,
        )

        self.details = Box(children=[self.info], h_expand=True, v_expand=True)

        self.playerInfo = Fabricator(
            poll_from='playerctl --follow metadata --format \'{"status": "{{status}}", "artUrl": "{{mpris:artUrl}}", "title": "{{ markup_escape(title) }}", "artist": "{{ markup_escape(artist) }}"}\'',
            stream=True,
            interval=1000,
        )

        def extract_metadata(_, value):
            if value:
                data = json.loads(value)

                self.art.set_style(f"background-image: url('{data['artUrl']}');")
                self.title.set_label(data["title"])
                self.artist.set_label(data["artist"])
                self.status.set_markup(
                    (
                        icons.stop
                        if data["status"] == "Stopped"
                        else (
                            icons.pause if data["status"] == "Playing" else icons.play
                        )
                    )
                )

            else:
                self.title.set_label("Nothing playing")
                self.artist.set_label("")
                self.status.set_markup(icons.stop)

        self.playerInfo.connect("changed", extract_metadata)

        for connector in [self.backward, self.play, self.forward, self.art]:
            bulk_connect(
                connector,
                {
                    "enter-notify-event": lambda *args: self.set_cursor("pointer"),
                    "leave-notify-event": lambda *args: self.set_cursor("default"),
                    "button-press-event": self.on_button_press,
                },
            )

        self.add(self.art)
        self.add(self.details)

    def on_button_press(self, button: Button, event):
        if event.button == 1 and event.type == 4:
            if button == self.backward:
                exec_shell_command("playerctl previous")
            elif button == self.play:
                exec_shell_command("playerctl play-pause")
            elif button == self.forward:
                exec_shell_command("playerctl next")
        elif event.button == 1 and event.type == 5:
            if button == self.art:
                floating().toggle()  # fix not toggling # always shows, might even multiple?
