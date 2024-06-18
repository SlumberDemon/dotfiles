from fabric.widgets import DateTime

datetime = DateTime(
    format_list=["%-I:%M %p %b %-d", "%-I:%M:%S %p %b %-d", "%a %-d %Y"],
    name="center-datetime",
)
