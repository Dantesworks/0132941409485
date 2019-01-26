screen map_icon():
    zorder 1
    imagebutton:
        focus_mask True
        idle "map_icon.png"
        hover "map_icon_hover.png"
        action Jump("map")
screen fastforward():
    zorder 5
    imagebutton:
        focus_mask True
        idle "ui_forward.png"
        hover "ui_forward_hover.png"
        action Jump("fastforward")

label map:
    if renpy.music.get_playing() != "sounds/wanderer.mp3":
        play music "sounds/wanderer.mp3"
    call hidescreens from _call_hidescreens_3
    show screen daytime
    show screen fastforward
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
