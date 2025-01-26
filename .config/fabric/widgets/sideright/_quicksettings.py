from icons import icons
from imports import *


class quicksettings(Box):
    def __init__(self) -> None:
        super().__init__(name="right-quicksettings", h_expand=True, orientation="h")

        self.wifi_icon = Label(name="settings-icon", markup=icons.wifi_on)
        self.bluetooth_icon = Label(name="settings-icon", markup=icons.bluetooth_on)
        self.mode_icon = Label(name="settings-icon", markup=icons.moon)
        self.dnd_icon = Label(name="settings-icon", markup=icons.dnd_on)

        self.wifi = Button(name="wifi-button", child=self.wifi_icon)
        self.bluetooth = Button(name="bluetooth-button", child=self.bluetooth_icon)
        self.mode = Button(name="mode-button", child=self.mode_icon)
        self.dnd = Button(name="dnd-button", child=self.dnd_icon)

        self.children = CenterBox(
            name="quicksettings-container",
            h_expand=True,
            orientation="h",
            center_children=[self.wifi, self.bluetooth, self.mode, self.dnd],
        )

        for connector in [self.wifi, self.bluetooth, self.mode, self.dnd]:
            bulk_connect(
                connector,
                {
                    "enter-notify-event": lambda *args: self.set_cursor("pointer"),
                    "leave-notify-event": lambda *args: self.set_cursor("default"),
                    "button-press-event": self.on_button_press,
                },
            )
        self.set_states()

    def on_button_press(self, button: Button, event):
        if event.button == 1 and event.type == 4:
            if button == self.wifi:

                self.set_states()

    def set_states(self):
        if "Powered: yes" in exec_shell_command("bluetoothctl show"):  # pyright: ignore
            self.bluetooth_icon.set_markup(icons.bluetooth_on)
            self.bluetooth.add_style_class("active")
        else:
            self.bluetooth_icon.set_markup(icons.bluetooth_off)
            self.bluetooth.remove_style_class("active")

        if "enabled" in exec_shell_command("nmcli radio wifi"):  # pyright:ignore
            self.wifi_icon.set_markup(icons.wifi_on)
            self.wifi.add_style_class("active")
        else:
            self.wifi_icon.set_markup(icons.wifi_off)
            self.wifi.remove_style_class("active")

        if "dark" in exec_shell_command(
            "gsettings get org.gnome.desktop.interface color-scheme"
        ):  # pyright: ignore
            self.mode_icon.set_markup(icons.moon)
            self.mode.add_style_class("active")
        else:
            self.mode_icon.set_markup(icons.sun)
            self.mode.add_style_class("active")
