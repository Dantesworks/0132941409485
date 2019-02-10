label barentrance:
    if renpy.music.get_playing() != "sounds/popstars.mp3":
        play music "sounds/popstars.mp3" fadeout 1
    show screen map_icon
    show screen daytime
    show screen phone_icon
    hide screen fastforward
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
            if premiumcount >= 100:
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
        if widowlvl == 1:
            imagebutton: ## widow
                focus_mask True
                idle "barside_widow_idle.png"
                hover "barside_widow_hover.png"
                action Jump("widow")
        imagebutton: ## back
            focus_mask True
            idle "back.png"
            hover "back_hover.png"
            action Jump("barentrance")

label loungestatusfalse:
    scene black
    "Non VIP members need not apply."
    jump barentrance
