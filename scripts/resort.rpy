label lobby:
    show screen map_icon
    show screen daytime
    call screen lobby
    screen lobby():
        add "lobby"
        imagebutton:
            focus_mask True
            idle "camillelobby.png"
            hover "camillelobby_hover.png"
            action Jump("map")
