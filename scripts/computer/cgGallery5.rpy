label cgGallery5:
    call screen cgGallery5
    screen cgGallery5:
        add "wallpaper"
        vbox xalign 0.5 ypos 1000:
            text "Page 5"
        imagebutton: ## back
            focus_mask True
            idle "back.png"
            hover "back_hover.png"
            action Jump("computer")
        imagebutton: ## previous
            focus_mask True
            idle "logo_previous.png"
            hover "logo_previous_hover.png"
            action Jump("cgGallery4")
        imagebutton: ## next
            focus_mask True
            idle "logo_next.png"
            hover "logo_next_hover.png"
            action Jump("cgGallery6")
        grid 3 3:
            align (0.5, 0.3)
            spacing 80
            if carolinelvl > 4:
                imagebutton:
                    focus_mask True
                    idle "gallery_buttons/cGGallery/38.png"
                    hover "gallery_buttons/cGGallery/38-h.png"
                    action Jump("g38")
            else:
                null
            if amandalvl > 13:
                imagebutton:
                    focus_mask True
                    idle "gallery_buttons/cGGallery/39.png"
                    hover "gallery_buttons/cGGallery/39-h.png"
                    action Jump("g39")
            else:
                null
            if amandalvl > 13:
                imagebutton:
                    focus_mask True
                    idle "gallery_buttons/cGGallery/40.png"
                    hover "gallery_buttons/cGGallery/40h.png"
                    action Jump("g40")
            else:
                null
            if amandalvl > 13:
                imagebutton:
                    focus_mask True
                    idle "gallery_buttons/cGGallery/41.png"
                    hover "gallery_buttons/cGGallery/41h.png"
                    action Jump("g41")
            else:
                null
            if amandalvl > 13:
                imagebutton:
                    focus_mask True
                    idle "gallery_buttons/cGGallery/42.png"
                    hover "gallery_buttons/cGGallery/42h.png"
                    action Jump("g42")
            else:
                null
            if bellelvl > 2:
                imagebutton:
                    focus_mask True
                    idle "gallery_buttons/cGGallery/43.png"
                    hover "gallery_buttons/cGGallery/43h.png"
                    action Jump("g43")
            else:
                null
            if veronicalvl > 2:
                imagebutton:
                    focus_mask True
                    idle "gallery_buttons/cGGallery/44.png"
                    hover "gallery_buttons/cGGallery/44h.png"
                    action Jump("g44")
            else:
                null
            if olivialvl > 5:
                imagebutton:
                    focus_mask True
                    idle "gallery_buttons/cGGallery/45.png"
                    hover "gallery_buttons/cGGallery/45h.png"
                    action Jump("g45")
            else:
                null
            if kairalvl > 6:
                imagebutton:
                    focus_mask True
                    idle "gallery_buttons/cGGallery/46i.png"
                    hover "gallery_buttons/cGGallery/46h.png"
                    action Jump("g46")
label g46:
    scene 46
    $ renpy.pause()
    jump cgGallery5
label g45:
    scene 45
    $ renpy.pause()
    jump cgGallery5
label g44:
    scene 44
    $ renpy.pause()
    jump cgGallery5
label g43:
    scene 43
    $ renpy.pause()
    jump cgGallery5
label g42:
    scene 42
    $ renpy.pause()
    jump cgGallery5
label g41:
    scene 41
    $ renpy.pause()
    jump cgGallery5
label g40:
    scene 40
    $ renpy.pause()
    jump cgGallery5
label g39:
    scene 39
    $ renpy.pause()
    jump cgGallery5
label g38:
    scene 38
    $ renpy.pause()
    jump cgGallery5
