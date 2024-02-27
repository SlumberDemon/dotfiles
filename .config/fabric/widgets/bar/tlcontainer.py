from imports import *

from .batteryindicator import led
from .datetime import datetime

tlcontainer = Box(name="tlcontainer", children=[datetime, led])
