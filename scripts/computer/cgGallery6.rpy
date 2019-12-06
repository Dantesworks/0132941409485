label cgGallery6:
    call screen cgGallery6
    screen cgGallery6:
        add "wallpaper"
        vbox xalign 0.5 ypos 1000:
            text "Page 6"
        imagebutton: ## back
            focus_mask True
            idle "back.png"
            hover "back_hover.png"
            action Jump("computer")
        imagebutton: ## previous
            focus_mask True
            idle "logo_previous.png"
            hover "logo_previous_hover.png"
            action Jump("cgGallery5")
        grid 3 3:
            align (0.5, 0.3)
            spacing 80
            if veronicalvl > 3:
                imagebutton:
                    focus_mask True
                    idle "gallery_buttons/cGGallery/47i.png"
                    hover "gallery_buttons/cGGallery/47h.png"
                    action Jump("g47")
            else:
                null
            if veronicalvl > 4:
                imagebutton:
                    focus_mask True
                    idle "gallery_buttons/cGGallery/48i.png"
                    hover "gallery_buttons/cGGallery/48h.png"
                    action Jump("g48")
            else:
                null
            if olivialvl > 11:
                imagebutton:
                    focus_mask True
                    idle "gallery_buttons/cGGallery/49i.png"
                    hover "gallery_buttons/cGGallery/49h.png"
                    action Jump("g49")
            else:
                null
            if cowgirl == True:
                imagebutton:
                    focus_mask True
                    idle "gallery_buttons/cGGallery/50i.png"
                    hover "gallery_buttons/cGGallery/50h.png"
                    action Jump("g49")
            else:
                null
            null
            null
            null
            null
            null
label g50:
    scene 50
    $ renpy.pause()
    jump cgGallery6
label g49:
    scene 49
    $ renpy.pause()
    jump cgGallery6
label g48:
    scene 48
    $ renpy.pause()
    jump cgGallery6
label g47:
    scene 47
    $ renpy.pause()
    jump cgGallery6
