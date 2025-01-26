import operator
from collections.abc import Iterator
from imports import *


class Launcher(WaylandWindow):
    def __init__(self):
        super().__init__(
            title="launcher",
            name="launcher",
            layer="top",
            anchor="center",
            exclusivity="none",
            keyboard_mode="on-demand",
            visible=False,
            all_visible=False,
        )
        self._arranger_handler: int = 0
        self._all_apps = get_desktop_applications()

        self.viewport = Box(orientation="v")

        self.search = Entry(
            placeholder="Search for apps...",
            h_expand=True,
            notify_text=lambda entry, *_: self.arrange_viewport(entry.get_text()),
            on_button_press_event=print,
            name="launcher-search",
        )
        self.apps = ScrolledWindow(
            min_content_size=(600, 320),  # 2nd number is height
            max_content_size=(280 * 2, 320),
            child=self.viewport,
            name="launcher-apps",
        )
        self.action_area = Box(name="launcher-area")
        # add center boxes for action stufs check _file.py for stuf like calculator etc
        # add sections like raycast? so apps, suggestions etc
        # also add the smart thingy for calculations etc
        # self.smart_feature_thing # a box that appears between apps and search (like raycast)
        self.details_label = Label(label="Fabricast", name="launcher-details-label")
        self.details_image = (
            Image(
                icon_name="edit-undo-symbolic",
                name="launcher-details-icon",
            )
            .build()
            .set_pixel_size(8)
            .unwrap()
        )  # Icon size fix
        self.details = CenterBox(
            name="launcher-details",
            start_children=[
                Svg(
                    size=16,
                    svg_file=get_relative_path("../../assets/fabric-symbolic.svg"),
                    style="fill: #3D9A6F;",
                )
            ],
            end_children=[
                Button(child=Box(children=[self.details_label, self.details_image]))
            ],
        )

        self.add(
            Box(
                orientation="v",
                children=[self.search, self.action_area, self.apps, self.details],
            )
        )
        self.show_all()

        self.search.connect("key-release-event", self.on_key)

    def on_key(self, entry, event_key):
        if event_key.get_keycode()[1] == 9:  # Esc to exit
            self.toggle()

    def arrange_viewport(self, query: str = ""):
        remove_handler(self._arranger_handler) if self._arranger_handler else None

        self.viewport.children = []
        # self.viewport.add(    Label(label="Applications", v_expand=True, v_align="start"))  # title thingy, fix and stlye corrctly and other stuff if i want to keep this

        filtered_apps_iter = iter(
            [
                app
                for app in self._all_apps
                if query.casefold()
                in (
                    (app.display_name or "")
                    + (" " + app.name + " ")
                    + (app.generic_name or "")
                ).casefold()
            ]
        )
        """
        print(
            len(
                [
                    app
                    for app in self._all_apps
                    if query.casefold()
                    in (
                        (app.display_name or "")
                        + (" " + app.name + " ")
                        + (app.generic_name or "")
                    ).casefold()
                ]
            )
            )
        """
        should_resize = operator.length_hint(filtered_apps_iter) == len(self._all_apps)

        self._arranger_handler = idle_add(
            lambda *args: self.add_next_application(*args)
            or (self.resize_viewport() if should_resize else False),
            filtered_apps_iter,
            pin=True,
        )

        return False

    def add_next_application(self, apps_iter: Iterator[DesktopApp]):
        if not (app := next(apps_iter, None)):
            return False

        self.viewport.add(self.bake_application_slot(app))
        return True

    def resize_viewport(self):
        self.apps.set_min_content_width(
            self.viewport.get_allocation().width  # type: ignore
        )
        return False

    def bake_application_slot(self, app: DesktopApp, **kwargs) -> Button:
        return Button(
            name="launcher-app",
            child=Box(
                orientation="h",
                children=[
                    Image(
                        pixbuf=app.get_icon_pixbuf(size=24),
                        h_align="start",
                        name="launcher-app-icon",
                    ),
                    Label(
                        label=app.display_name or "Unknown",
                        v_align="center",
                        h_align="center",
                    ),
                    Box(h_expand=True),
                    Label(
                        label="Application",
                        tooltip_text=app.description,
                        name="launcher-app-label",
                    ),
                ],
            ),
            on_focus_in_event=lambda *_: (
                self.details_label.set_label("Open Application")
            ),
            #            on_enter_notify_event=lambda *_: (
            #                self.details_label.set_label("Open Application"),
            #                self.set_cursor("pointer"),
            #            ), # fix so that and css hover work
            on_clicked=lambda *_: (
                self.launch_app(app),  # use while dev  # app.launch()
                self.hide(),
            ),
            **kwargs,
        )

    # Temp keep
    def launch_app(self, app: DesktopApp):
        command = (
            " ".join([arg for arg in app.command_line.split() if "%" not in arg])
            if app.command_line
            else None
        )
        (
            exec_shell_command_async(
                f"hyprctl dispatch exec -- {command}",
                lambda *_: print(f"Launched {app.name}"),
            )
            if command
            else None
        )

    def toggle(self):
        self._all_apps = get_desktop_applications()
        self.search.set_text("")
        self.search.grab_focus()
        self.set_visible(not self.is_visible())
