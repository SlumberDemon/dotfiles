## Hyprland

Add these layer rules to your hyprland config.

```
layerrule = blur, bar
layerrule = ignorealpha 0.4, bar

layerrule = blur, side-*
layerrule = ignorealpha 0.4, side-*
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
- psutil
- wofi
- playerctl

## Todo

- [x] Dark mode
- [ ] Left side
  - [ ] Player widget
- [ ] Right side
- [ ] Globe functionality
