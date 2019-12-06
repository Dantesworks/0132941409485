label gallery3:
    call screen gallery3
    screen gallery3:
        add "wallpaper"
        vbox xalign 0.5 ypos 1000:
            text "Page 3"
        imagebutton: ## previous
            focus_mask True
            idle "logo_previous.png"
            hover "logo_previous_hover.png"
            action Jump("gallery2")
        grid 3 3:
            align (0.5, 0.3)
            spacing 80
            if veronicalvl > 3:
                imagebutton:
                    focus_mask True
                    idle "gallery_buttons/r19.png"
                    hover "gallery_buttons/r19h.png"
                    action Jump("verc2")
            else:
                null
            if veronicalvl > 4:
                imagebutton:
                    focus_mask True
                    idle "gallery_buttons/r20.png"
                    hover "gallery_buttons/r20h.png"
                    action Jump("verc3")
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
