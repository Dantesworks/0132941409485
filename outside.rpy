label cafe:
    show screen map_icon
    show screen daytime
    call screen cafe
    screen cafe():
        if daytime == 1:
            add "cafe"

label barentrance:
    show screen map_icon
    show screen daytime
    call screen barentrance
    screen barentrance():
        if daytime == 4:
            add "barentrance"
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
    show barentrance
    "Area closed for now."
    jump barentrance
