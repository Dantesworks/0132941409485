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
                    action Jump("ver3")
            else:
                null
            if veronicalvl > 5:
                imagebutton:
                    focus_mask True
                    idle "gallery_buttons/r21.png"
                    hover "gallery_buttons/r21h.png"
                    action Jump("verc4")
            else:
                null
            if veronicalvl > 5:
                imagebutton:
                    focus_mask True
                    idle "gallery_buttons/r22.png"
                    hover "gallery_buttons/r22h.png"
                    action Jump("verc5")
            else:
                null
            if veronicalvl > 5:
                imagebutton:
                    focus_mask True
                    idle "gallery_buttons/r23.png"
                    hover "gallery_buttons/r23h.png"
                    action Jump("verc6")
            else:
                null
            if olivialvl > 12:
                imagebutton:
                    focus_mask True
                    idle "gallery_buttons/r24.png"
                    hover "gallery_buttons/r24h.png"
                    action Jump("olivia24")
            else:
                null
            if wildbillvariant:
                imagebutton:
                    focus_mask True
                    idle "gallery_buttons/r25.png"
                    hover "gallery_buttons/r25h.png"
                    action Jump("amandabill1")
            else:
                null
            if wildbillvariant:
                imagebutton:
                    focus_mask True
                    idle "gallery_buttons/r26.png"
                    hover "gallery_buttons/r26h.png"
                    action Jump("amandabill2")
            else:
                null
            null
        imagebutton: ## back
            focus_mask True
            idle "back.png"
            hover "back_hover.png"
            action Jump("computer")
