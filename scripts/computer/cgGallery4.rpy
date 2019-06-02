label cgGallery4:
    call screen cgGallery4
    screen cgGallery4:
        add "wallpaper"
        vbox xalign 0.5 ypos 1000:
            text "Page 4"
        imagebutton: ## back
            focus_mask True
            idle "back.png"
            hover "back_hover.png"
            action Jump("computer")
        imagebutton: ## previous
            focus_mask True
            idle "logo_previous.png"
            hover "logo_previous_hover.png"
            action Jump("cgGallery3")
        grid 3 3:
            align (0.5, 0.3)
            spacing 80
            if camillelvl > 4:
                imagebutton:
                    focus_mask True
                    idle "gallery_buttons/cGGallery/29-i.png"
                    hover "gallery_buttons/cGGallery/29-h.png"
                    action Jump("g29")
            else:
                null
            if camillelvl > 5:
                imagebutton:
                    focus_mask True
                    idle "gallery_buttons/cGGallery/30-i.png"
                    hover "gallery_buttons/cGGallery/30-h.png"
                    action Jump("g30")
            else:
                null
            null
            null
            null
            null
            null
            null
            null


label g29:
    scene 29
    $ renpy.pause()
    jump cgGallery4
label g30:
    scene 30
    $ renpy.pause()
    jump cgGallery4
