label lobby:
    call resortEvents from _call_resortEvents
    show screen map_icon
    show screen daytime
    show screen phone_icon
    hide screen fastforward
    if renpy.music.get_playing() != "sounds/slopes.mp3":
        play music "sounds/slopes.mp3" fadeout 1
    call screen lobby
    screen lobby():
        add "lobby"
        imagebutton:
            focus_mask True
            idle "camillelobby.png"
            hover "camillelobby_hover.png"
            action Jump("Camille")
label publicbathouse:
    call screen publicbathouse
    screen publicbathouse():
        add "bathhouse"
        imagebutton: ## tifa
            focus_mask True
            idle "tifa_idle.png"
            hover "tifa_hover.png"
            action Jump("tifa_story")
        imagebutton: ## back
            focus_mask True
            idle "back.png"
            hover "back_hover.png"
            action Jump("lobby")

label sauna:
    call screen sauna
    screen sauna():
        add "sauna"
        imagebutton: ## back
            focus_mask True
            idle "back.png"
            hover "back_hover.png"
            action Jump("lobby")

label pool:
    call screen pool
    screen pool():
        add "pool"
        imagebutton: ## back
            focus_mask True
            idle "back.png"
            hover "back_hover.png"
            action Jump("lobby")
        if daytime == 3:
            imagebutton:
                focus_mask True
                idle "pool_belle_idle.png"
                hover "pool_belle_hover.png"
                action Jump("belle")
