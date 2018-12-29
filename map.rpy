screen map_icon():
    zorder 1
    imagebutton:
        focus_mask True
        idle "map_icon.png"
        hover "map_icon_hover.png"
        action Jump("map")


label map:
    $ lastplayed = "m"
    play music "sounds/wanderer.mp3"
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
                action Show("cafeclosed")
        imagebutton: #bar
            focus_mask True
            idle "map_bar.png"
            hover "map_bar_hover.png"
            if daytime == 4:
                action Jump("barentrance")
            else:
                action Show("barclosed")
        imagebutton: #resort
            focus_mask True
            idle "map_resort.png"
            hover "map_resort_hover.png"
            if daytime == 2 or daytime == 3:
                action Jump("lobby")
            else:
                action Show("resortclosed")

screen cafeclosed():
    add "cafeclosed.png"
    imagebutton:
        idle "close.png"
        action Hide("cafeclosed")


screen barclosed():
    add "barclosed.png"
    imagebutton:
        idle "close.png"
        action Hide("barclosed")

screen resortclosed():
    add "resortclosed.png"
    imagebutton:
        idle "close.png"
        action Hide("resortclosed")
