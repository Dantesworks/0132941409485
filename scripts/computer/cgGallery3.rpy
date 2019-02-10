label cgGallery3:
    call screen cgGallery3
    screen cgGallery3:
        add "wallpaper"
        vbox xalign 0.5 ypos 1000:
            text "Page 3"
        imagebutton: ## back
            focus_mask True
            idle "back.png"
            hover "back_hover.png"
            action Jump("computer")
        imagebutton: ## previous
            focus_mask True
            idle "logo_previous.png"
            hover "logo_previous_hover.png"
            action Jump("cgGallery2")
        grid 3 3:
            align (0.5, 0.3)
            spacing 80
            if amandalvl > 10:
                imagebutton:
                    focus_mask True
                    idle "gallery_buttons/cGGallery/20-i.png"
                    hover "gallery_buttons/cGGallery/20-h.png"
                    action Jump("g20")
            else:
                null
            if amandalvl > 10:
                imagebutton:
                    focus_mask True
                    idle "gallery_buttons/cGGallery/21-i.png"
                    hover "gallery_buttons/cGGallery/21-h.png"
                    action Jump("g21")
            else:
                null
            if amandalvl > 10:
                imagebutton:
                    focus_mask True
                    idle "gallery_buttons/cGGallery/22-i.png"
                    hover "gallery_buttons/cGGallery/22-h.png"
                    action Jump("g22")
            else:
                null
            if amandalvl > 10:
                imagebutton:
                    focus_mask True
                    idle "gallery_buttons/cGGallery/23-i.png"
                    hover "gallery_buttons/cGGallery/23-h.png"
                    action Jump("g23")
            else:
                null
            if widowlvl > 1:
                imagebutton:
                    focus_mask True
                    idle "gallery_buttons/cGGallery/24-i.png"
                    hover "gallery_buttons/cGGallery/24-h.png"
                    action Jump("g24")
            else:
                null
            null
            null
            null
            null
label g20:
    scene 20
    $ renpy.pause()
    jump cgGallery3
label g21:
    scene 21
    $ renpy.pause()
    jump cgGallery3
label g22:
    scene 22
    $ renpy.pause()
    jump cgGallery3
label g23:
    scene 23
    $ renpy.pause()
    jump cgGallery3
label g24:
    scene 24
    $ renpy.pause()
    jump cgGallery3
