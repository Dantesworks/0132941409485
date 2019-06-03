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
            null
            null
            null
            null
            null
            null
            null
        imagebutton: ## back
            focus_mask True
            idle "back.png"
            hover "back_hover.png"
            action Jump("computer")
