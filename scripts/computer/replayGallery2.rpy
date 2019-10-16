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
        imagebutton: ## next
            focus_mask True
            idle "logo_next.png"
            hover "logo_next_hover.png"
            action Jump("gallery3")
        grid 3 3:
            align (0.5, 0.3)
            spacing 80
            if nicolelvl > 8:
                imagebutton:
                    focus_mask True
                    idle "gallery_buttons/r10.png"
                    hover "gallery_buttons/r10h.png"
                    action Jump("nicole_bj2")
            else:
                null
            if nicolelvl > 10:
                imagebutton:
                    focus_mask True
                    idle "gallery_buttons/r11.png"
                    hover "gallery_buttons/r11h.png"
                    action Jump("nicole_park")
            else:
                null
            if gym_intro:
                imagebutton:
                    focus_mask True
                    idle "gallery_buttons/r12.png"
                    hover "gallery_buttons/r12h.png"
                    action Jump("ver_bj")
            else:
                null
            if gym_intro:
                imagebutton:
                    focus_mask True
                    idle "gallery_buttons/r13.png"
                    hover "gallery_buttons/r13h.png"
                    action Jump("o_bj")
            else:
                null
            if carolinelvl >= 6 and carolinebarlvl > 3:
                imagebutton:
                    focus_mask True
                    idle "gallery_buttons/r14.png"
                    hover "gallery_buttons/r14h.png"
                    action Jump("caroline1")
            else:
                null
            if amandalvl > 14:
                imagebutton:
                    focus_mask True
                    idle "gallery_buttons/r15.png"
                    hover "gallery_buttons/r15h.png"
                    action Jump("amandabj1")
            else:
                null
            if amandalvl > 15:
                imagebutton:
                    focus_mask True
                    idle "gallery_buttons/r17.png"
                    hover "gallery_buttons/r17h.png"
                    action Jump("amandabj2")
            else:
                null
            if amandalvl > 18:
                imagebutton:
                    focus_mask True
                    idle "gallery_buttons/r16.png"
                    hover "gallery_buttons/r16h.png"
                    action Jump("nyma")
            else:
                null
            if veronicalvl > 2:
                imagebutton:
                    focus_mask True
                    idle "gallery_buttons/r18.png"
                    hover "gallery_buttons/r18h.png"
                    action Jump("verc")
            else:
                null
        imagebutton: ## back
            focus_mask True
            idle "back.png"
            hover "back_hover.png"
            action Jump("computer")
