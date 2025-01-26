from typing import cast
from gi.repository import GdkPixbuf

from imports import *

NOTIFICATION_WIDTH = 360
NOTIFICATION_IMAGE_SIZE = 64
NOTIFICATION_TIMEOUT = 10 * 1000  # 10 seconds


class notificationWidget(Box):
    def __init__(self, notification: Notification, **kwargs):
        super().__init__(
            size=(NOTIFICATION_WIDTH, -1),
            name="notification",
            spacing=8,
            orientation="v",
            **kwargs,
        )

        self._notification = notification

        body_container = Box(spacing=4, orientation="h")

        if image_pixbuf := self._notification.image_pixbuf:
            body_container.add(
                Image(
                    pixbuf=image_pixbuf.scale_simple(
                        NOTIFICATION_IMAGE_SIZE,
                        NOTIFICATION_IMAGE_SIZE,
                        GdkPixbuf.InterpType.BILINEAR,
                    )
                )
            )

        body_container.add(
            Box(
                # spacing=4,
                orientation="v",
                children=[
                    Box(
                        orientation="h",
                        children=[
                            Label(
                                label=self._notification.summary,
                                ellipsization="middle",
                            )
                            .build()
                            .add_style_class("summary")
                            .unwrap(),
                        ],
                        h_expand=True,
                        v_expand=True,
                    ).build(
                        lambda box, _: box.pack_end(
                            Button(
                                name="notification-close",
                                image=Image(
                                    icon_name="window-close",
                                    icon_size=16,
                                ),
                                v_align="center",
                                h_align="end",
                                on_clicked=lambda *_: self._notification.close(),
                                on_enter_notify_event=lambda *_: (
                                    self.set_cursor("pointer"),
                                ),
                            ),
                            False,
                            False,
                            0,
                        )
                    ),
                    Label(
                        label=self._notification.body,
                        line_wrap="word-char",
                        v_align="start",
                        h_align="start",
                        ellipsization="end",
                    )
                    .build()
                    .add_style_class("body")
                    .unwrap(),
                ],
                h_expand=True,
                v_expand=True,
            )
        )

        self.add(body_container)

        if actions := self._notification.actions:
            self.add(
                Box(
                    spacing=4,
                    orientation="h",
                    children=[
                        Button(
                            name="notification-button",
                            h_expand=True,
                            v_expand=True,
                            label=action.label,
                            on_clicked=lambda *_, action=action: action.invoke(),
                            on_enter_notify_event=lambda *_: (
                                self.set_cursor("pointer"),
                            ),
                        )
                        for action in actions
                    ],
                )
            )

        self._notification.connect(
            "closed",
            lambda *_: (
                parent.remove(self) if (parent := self.get_parent()) else None,  # type: ignore
                self.destroy(),
            ),
        )

        invoke_repeater(
            NOTIFICATION_TIMEOUT,
            lambda: self._notification.close("expired"),
            initial_call=False,
        )


class notifcationPopup(WaylandWindow):
    def __init__(self):
        super().__init__(
            title="notifications",
            margin="4px 4px 4px 4px",
            anchor="top right",
            child=Box(
                size=2,
                spacing=4,
                orientation="v",
            ).build(
                lambda viewport, _: Notifications(
                    on_notification_added=lambda notifs_service, nid: viewport.add(
                        notificationWidget(
                            cast(
                                Notification,
                                notifs_service.get_notification_from_id(nid),
                            )
                        )
                    )
                )
            ),
            visible=True,
            all_visible=True,
        )
