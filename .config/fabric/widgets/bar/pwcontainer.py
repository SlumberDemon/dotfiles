from imports import *

from .profile import profile
from .workspace import workspace

pwcontainer = Box(name="pwcontainer", children=[profile, workspace])
