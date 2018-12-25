screen map_icon():
    zorder 1
    imagebutton:
        focus_mask True
        idle "map_icon.png"
        hover "map_icon_hover.png"
        action Jump("map")


label map:
    hide screen map_icon
    show screen daytime
    call screen map
    screen map():
        add "map"
        imagebutton: #home
            focus_mask True
            idle "map_home.png"
            hover "map_home_hover.png"
            action Jump("hallway")
        imagebutton: #cafe
            focus_mask True
            idle "map_cafe.png"
            hover "map_cafe_hover.png"
            if daytime == 1:
                action Jump("cafe")
            else:
                action Jump("cafeclosed")
        imagebutton: #bar
            focus_mask True
            idle "map_bar.png"
            hover "map_bar_hover.png"
            if daytime == 4:
                action Jump("barentrance")
            else:
                action Jump("barclosed")

label cafeclosed:
    scene mapfill
    show screen daytime
    show cafeclosed
    $ renpy.pause()
    jump map

label barclosed:
    scene mapfill
    show screen daytime
    show barclosed
    $ renpy.pause()
    jump map
