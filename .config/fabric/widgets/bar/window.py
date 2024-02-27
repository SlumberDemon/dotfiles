from imports import *

window = ActiveWindow(
    formatter=FormattedString(
        "{title(win_class)}",
        title=lambda x, max_length=20: (
            "Desktop"
            if len(x) == 0
            else x if len(x) <= max_length else x[: max_length - 3] + "..."
        ),
    ),
    name="window",
)
