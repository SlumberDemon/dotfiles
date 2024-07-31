import json

from fabric.utils import bulk_connect, exec_shell_command, get_relative_path
from fabric.utils.fabricator import Fabricator
from fabric.widgets import Box, Button, CenterBox, Label, Svg  # WaylandWindow

"""
class floatingPlayer(WaylandWindow):
    def __init__(self):
        super().__init__(
            layer="overlay",
            exclusive=True,
            visible=False,
            name="floating-player",
            anchor="bottom left",
            v_expand=False,
            h_expand=False,
        )

        self.add(Label("test"))

    def toggle(self):
        self.set_visible(not self.is_visible())
"""


class player(Box):
    def __init__(self):
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
            name="left-player-backward",
            child=Svg(
                svg_file=get_relative_path("../../assets/skip-backward.svg"),
                size=30,
                style="fill: #ffffff;",
            ),
        )
        self.play = Button(
            name="left-player-play",
            child=Svg(
                svg_file=get_relative_path("../../assets/stop.svg"),
                size=30,
                style="fill: #ffffff;",
            ),
        )
        self.forward = Button(
            name="left-player-forward",
            child=Svg(
                svg_file=get_relative_path("../../assets/skip-forward.svg"),
                size=30,
                style="fill: #ffffff;",
            ),
        )

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
        )

        def extract_metadata(_, value):
            data = json.loads(value)

            self.art.set_style(f"background-image: url('{data['artUrl']}');")
            self.title.set_label(
                data["title"]
            )  # if bla bla then value else default (nothing)
            self.artist.set_label(data["artist"])

        self.playerInfo.connect("changed", extract_metadata)

        for connector in [self.backward, self.play, self.forward]:  # self.art
            bulk_connect(
                connector,
                {
                    "enter-notify-event": lambda *args: self.change_cursor("pointer"),
                    "leave-notify-event": lambda *args: self.change_cursor("default"),
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
        """
        elif event.button == 1 and event.type == 5:
            if button == self.art:
                floatingPlayer()
        """
