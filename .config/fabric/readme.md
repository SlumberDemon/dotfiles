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

- Change the logo by adding an SVG in `assets` and then updating `widgets/bar/_logo.py` line 5.

## Requirements

- [fabric](https://github.com/Fabric-Development/fabric)
- psutil 
- wofi

## Todo

- [ ] Dark mode
- [ ] Left side
- [ ] Right side
- [ ] Globe functionality
