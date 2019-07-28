label gallery2:
    call screen gallery2
    screen gallery2:
        add "wallpaper"
        vbox xalign 0.5 ypos 1000:
            text "Page 2"
        imagebutton: ## previous
            focus_mask True
            idle "logo_previous.png"
            hover "logo_previous_hover.png"
            action Jump("gallery1")
        grid 3 3:
            align (0.5, 0.3)
            spacing 80
            if nicolelvl > 8:
                imagebutton:
                    focus_mask True
                    idle "gallery_buttons/10_i.png"
                    hover "gallery_buttons/10_h.png"
                    action Jump("nicole_bj2")
            else:
                null
            if nicolelvl > 10:
                imagebutton:
                    focus_mask True
                    idle "gallery_buttons/11_i.png"
                    hover "gallery_buttons/11_h.png"
                    action Jump("nicole_park")
            else:
                null
            if gym_intro:
                imagebutton:
                    focus_mask True
                    idle "gallery_buttons/12.png"
                    hover "gallery_buttons/12_h.png"
                    action Jump("ver_bj")
            else:
                null
            if gym_intro:
                imagebutton:
                    focus_mask True
                    idle "gallery_buttons/13.png"
                    hover "gallery_buttons/13_h.png"
                    action Jump("o_bj")
            else:
                null
            if carolinelvl >= 6 and carolinebarlvl > 3:
                imagebutton:
                    focus_mask True
                    idle "gallery_buttons/14.png"
                    hover "gallery_buttons/14_h.png"
                    action Jump("caroline1")
            else:
                null
            if amandalvl > 14:
                imagebutton:
                    focus_mask True
                    idle "gallery_buttons/15.png"
                    hover "gallery_buttons/15_h.png"
                    action Jump("amandabj1")
            else:
                null
            if amandalvl > 15:
                imagebutton:
                    focus_mask True
                    idle "gallery_buttons/17.png"
                    hover "gallery_buttons/17_h.png"
                    action Jump("amandabj2")
            else:
                null
            if amandalvl > 18:
                imagebutton:
                    focus_mask True
                    idle "gallery_buttons/16.png"
                    hover "gallery_buttons/16_h.png"
                    action Jump("nyma")
            else:
                null
            if veronicalvl > 2:
                imagebutton:
                    focus_mask True
                    idle "gallery_buttons/18.png"
                    hover "gallery_buttons/18h.png"
                    action Jump("verc")
            else:
                null
        imagebutton: ## back
            focus_mask True
            idle "back.png"
            hover "back_hover.png"
            action Jump("computer")
