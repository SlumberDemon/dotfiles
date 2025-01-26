import operator
from collections.abc import Iterator

from fabric import Application
from fabric.utils import (
    DesktopApp,
    get_desktop_applications,
    get_relative_path,
    idle_add,
    remove_handler,
)
from fabric.widgets.box import Box
from fabric.widgets.button import Button
from fabric.widgets.entry import Entry
from fabric.widgets.image import Image
from fabric.widgets.label import Label
from fabric.widgets.scrolledwindow import ScrolledWindow
from fabric.widgets.wayland import WaylandWindow


class Launcher(WaylandWindow):
    def __init__(self, **kwargs):
        super().__init__(
            title="launcher",
            layer="top",
            anchor="center",
            keyboard_mode="on-demand",
            # visible=False,
            **kwargs,
        )
        self._desktop_apps = get_desktop_applications()

        self.viewport = Box(orientation="v")

        self.search = Entry(
            placeholder="Search for apps...",
            h_expand=True,
            name="search",
            notify_text=lambda entry, *_: self.arrange_viewport(entry.get_text()),
            on_button_press_event=print,
        )

        # self.smart_feature_thing # a box that appears between apps and search (like raycast)

        self.apps = ScrolledWindow(
            child=self.viewport,
        )

        self.add(self.search)
        self.add(self.apps)

    def arrange_viewport(self, query: str = ""):
        remove_handler(self._arranger_handler) if self._arranger_handler else None

        self.viewport.children = []

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
        self.scrolled_window.set_min_content_width(
            self.viewport.get_allocation().width  # type: ignore
        )
        return False

    def bake_application_slot(self, app: DesktopApp, **kwargs) -> Button:
        return Button(
            child=Box(
                orientation="h",
                children=[
                    Image(pixbuf=app.get_icon_pixbuf(), h_align="start"),
                    Label(
                        label=app.display_name or "Unknown",
                        v_align="center",
                        h_align="center",
                    ),
                ],
            ),
            tooltip_text=app.description,
            on_clicked=lambda *_: (app.launch(), self.application.quit()),
            **kwargs,
        )


if __name__ == "__main__":
    launcher = Launcher()
    app = Application("launcher", launcher)
    app.set_stylesheet_from_file(get_relative_path("_launcher.css"))
    app.run()
