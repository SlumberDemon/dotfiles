# Notice

Due to being left stale the code may have lots of bugs and errors which will not be fixed by me. It is also not fully complete.
Feel free to copy, modify or use this config!

## Hyprland

Add these layer rules to your hyprland config.

```
layerrule = blur, bar
layerrule = ignorealpha 0.4, bar

layerrule = blur, side-left
layerrule = ignorealpha 0.4, side-left
layerrule = animation slide, side-left

layerrule = blur, side-right
layerrule = ignorealpha 0.4, side-right
layerrule = animation slide, side-right


layerrule = blur, launcher
layerrule = ignorealpha 0.4, launcher
#layerrule = animation popin, launcher

layerrule = blur, floating-player
layerrule = ignorealpha 0.4, floating-player

layerrule = blur, notifications
layerrule = ignorealpha 0.4, notifications
```

To setup shortcuts, you will need fabric-cli

```
bind = Super, Space, exec, fabric-cli execute default "launcher.toggle()"
bind = Super, B, exec, fabric-cli execute default "sideLeft.toggle()"
bind = Super, N, exec, fabric-cli execute default "sideRight.toggle()"
```

To start the bar, I recommend using a virtual environment for packages, I also suggest putting the fabric config into .config/fabric

```
exec-once = cd ~/.config/fabric && .venv/bin/python main.py
```

## Customize

- Add your own profile picture by changing the asset in `assets/profile.png`.

- Change the logo by adding an SVG in `assets` and then updating `widgets/bar/_logo.py` line 5. I recommend using icons from [simpleicons](https://simpleicons.org/).

## Mode

Change `css/color.css` to use light/dark, no need to restart fabric as the changes are applied automatically.

```
@import url("./colors/<mode>.css");
```

## Requirements

- [fabric](https://github.com/Fabric-Development/fabric)
- [fabric-cli](https://github.com/Fabric-Development/fabric-cli)
- psutil
- wofi
- playerctl

#### Optional

- watchfiles

## Environment

In an .env file configs for weather widget are needed, uses https://www.weatherapi.com/. Put into root dir

```
FABRIC_WEATHER_KEY=***********
FABRIC_WEATHER_LOC=london
```

To install python libraries I recommend using a .venv

```py
# with uv
uv venv
# then activate .venv
uv pip install -r requirements.txt
```

```py
# with pip
python3 -m venv .venv
# then activate .venv
pip install -r requirements.txt
```


## Run

```sh
python3 main.py
```

or

```sh
watchfiles "python3 main.py" .
```

## Features

- Bar
- Notifications
- Side panels
- Side menus
- App launcher
- Screen corners

## Todo

- [x] Dark mode
  - [x] Icons (maybe use icons from icon browser and then like in launcher)
- [ ] Left side
  - [x] Media player
  - [x] System info
  - [x] Weather
  - [ ] Volume
- [ ] Right side
  - [ ] Quick settings?
    - [ ] Wifi
    - [ ] Bluetooth
    - [ ] Mode (dark/light)
    - [ ] Dnd
  - [ ] Calender?
  - [ ] Brightness
  - [ ] Notifications center
- [ ] App launcher
  - [ ] Sections (Commands, Applications)
  - [ ] Commands
  - [ ] Action Area
  - [ ] Fuzzy search (thefuzz pypi)
  - [ ] Fix hover
- [x] Notifications
- [ ] Volume indicator
- [ ] Brightness indicator
- [ ] Dynamic notch?
- [x] Update to rewrite
  - [x] Fix issues
- [ ] Improve css naming conventions
- [ ] Keybinds cheat sheet?
- [ ] Bar
  - [ ] Globe functionality
  - [ ] Fix opening fabricast
- [ ] Logging with loguru?

#### Help

Are you really stuck? While I probably won't check everyday, if you are facing a problem open an issue, I might help you!
