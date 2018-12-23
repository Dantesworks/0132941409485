label kaira:
    call screen kaira
    screen kaira():
        add "wallpaper"
        add "characters/kaira.png" xalign 0.5 ypos 50
        if nicolelvl = 1:
            vbox xsize 1800 xalign 0.5 yalign 0.5:
                text "When [p] met Kaira again, he discovered that she was no longer \
the young girl she once was. She had grown in many ways, and she knew this too. She is learning to use guile and charm to manipulate \
others to satisfy her desires, and who better to practise on than [p], who is always close by? With the influence of Nicole, she will be a \
force to be reckoned with indeed. She put these skills to practise on the second day, wearing alluring outfits to catch the eye of \
[p]. The day would culminate in an intimate experience between all parties involved, yet Kaira will deny remembering any of it. \
Despite this, [p] wonders if this is true, as he cannot shake the feeling that this experience will haunt him in the future." justify True size 28
        imagebutton: ## back
            focus_mask True
            idle "back.png"
            hover "back_hover.png"
            action Jump("profile")
label nicole:
    call screen nicole
    screen nicole():
        add "wallpaper"
        add "characters/nicole.png" xalign 0.5 ypos 50
        if kairalvl = 1:
            vbox xsize 1800 xalign 0.5 yalign 0.5:
                text
