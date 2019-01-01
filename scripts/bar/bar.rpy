label barentrance:
    if renpy.music.get_playing() != "sounds/popstars.mp3":
        play music "sounds/popstars.mp3" fadeout 1
    show screen map_icon
    show screen daytime
    call screen barentrance
    screen barentrance():
        add "barentrance"
        if daytimes in carolineshow:
            imagebutton: ## caroline
                    focus_mask True
                    idle "carolinebar.png"
                    hover "carolinebar_hover.png"
                    action Jump("Carolinebar")
        imagebutton: ## premium lounge
            focus_mask True
            idle "premiumlounge.png"
            hover "premiumlounge_hover.png"
            if loungestatus:
                action Jump("barside")
            else:
                action Jump("loungestatusfalse")
label barside:
    hide screen map_icon
    show screen daytime
    call screen barside
    screen barside():
        if daytime == 4:
            add "barside"
        imagebutton: ## back
            focus_mask True
            idle "back.png"
            hover "back_hover.png"
            action Jump("barentrance")

label loungestatusfalse:
    scene black
    "Area closed for now."
    jump barentrance
