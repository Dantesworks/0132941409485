label lobby:
    show screen map_icon
    show screen daytime
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
    scene bathhouse with fade
    call screen publicbathouse
    screen publicbathouse():
        add "bathhouse"
        imagebutton: ## back
            focus_mask True
            idle "back.png"
            hover "back_hover.png"
            action Jump("lobby")

label sauna:
    scene sauna with fade
    call screen sauna
    screen sauna():
        add "sauna"
        imagebutton: ## back
            focus_mask True
            idle "back.png"
            hover "back_hover.png"
            action Jump("lobby")

label pool:
    scene pool with fade
    call screen pool
    screen pool():
        add "pool"
        imagebutton: ## back
            focus_mask True
            idle "back.png"
            hover "back_hover.png"
            action Jump("lobby")
