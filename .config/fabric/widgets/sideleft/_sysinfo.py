import psutil

from icons import icons
from imports import *


class sysinfo(Box):
    def __init__(self) -> None:
        super().__init__(name="left-sysinfo", h_expand=True, orientation="h")

        self.systemInfo = Fabricator(
            poll_from=lambda f: {
                "cpu": psutil.cpu_percent(),
                "ram": psutil.virtual_memory().percent,
                "storage": psutil.disk_usage("/").percent,
                "temp": psutil.sensors_temperatures()["nvme"][0].current,
                # temp here
            },
            interval=1000,
        )

        self.systemInfo.connect(
            "changed",
            lambda _, value: (self.update(value)),
        )

        self.cpu_circular = CircularProgressBar(
            size=(64, 64), name="left-sysinfo-circular", max_value=100
        )
        self.cpu = Box(
            name="left-sysinfo-box",
            children=[
                Overlay(
                    child=self.cpu_circular,
                    overlays=[
                        Label(
                            markup=icons.cpu,
                            name="left-sysinfo-icon",
                            style="margin-left: 2px;",
                        ),
                    ],
                )
            ],
        )

        self.ram_circular = CircularProgressBar(
            size=(64, 64), name="left-sysinfo-circular", max_value=100
        )
        self.ram = Box(
            name="left-sysinfo-box",
            children=[
                Overlay(
                    child=self.ram_circular,
                    overlays=[
                        Label(
                            markup=icons.ram,
                            name="left-sysinfo-icon",
                            style="margin-left: 1px;",
                        ),
                    ],
                )
            ],
        )

        self.storage_circular = CircularProgressBar(
            size=(64, 64), name="left-sysinfo-circular", max_value=100
        )
        self.storage = Box(
            name="left-sysinfo-box",
            children=[
                Overlay(
                    child=self.storage_circular,
                    overlays=[
                        Label(
                            markup=icons.storage,
                            name="left-sysinfo-icon",
                        ),
                    ],
                )
            ],
        )

        self.temp_circular = CircularProgressBar(
            size=(64, 64), name="left-sysinfo-circular", max_value=100
        )
        self.temp = Box(
            name="left-sysinfo-box",
            children=[
                Overlay(
                    child=self.temp_circular,
                    overlays=[
                        Label(
                            markup=icons.temperature,
                            name="left-sysinfo-icon",
                        )
                    ],
                )
            ],
        )

        self.children = CenterBox(
            h_expand=True,
            orientation="h",
            center_children=[self.cpu, self.ram, self.storage, self.temp],
        )

        # cpu, ram, storage, temp, 5th thing?

    def update(self, value):
        self.cpu_circular.value = value["cpu"]
        self.ram_circular.value = value["ram"]
        self.storage_circular.value = value["storage"]
        self.temp_circular.value = value["temp"]
