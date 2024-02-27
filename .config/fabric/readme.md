# Hyprland config

```
layerrule = blur, fabric
layerrule = ignorezero 0.4, fabric
```

# Install

The aur package for fabric is out of date please build from source
> https://github.com/Fabric-Development/fabric

# Sofa 

Some features require the sofa cli to work
> https://github.com/slumberdemon/sofa

# Css

If you don't have the code in `.config/fabric` you will need to update the import line in `css/main.css`

```css
@import url('{your-path-here}/css/colors.css');
```

# Known issues
- Bar colours updating only after opening an app, etc (issue with hyprland blur)