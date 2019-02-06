label cgGallery2:
    call screen cgGallery2
    screen cgGallery2:
        add "wallpaper"
        vbox xalign 0.5 ypos 1000:
            text "Page 2"
        imagebutton: ## back
            focus_mask True
            idle "back.png"
            hover "back_hover.png"
            action Jump("computer")
        imagebutton: ## next
            focus_mask True
            idle "logo_next.png"
            hover "logo_next_hover.png"
            action Jump("cgGallery3")
        imagebutton: ## previous
            focus_mask True
            idle "logo_previous.png"
            hover "logo_previous_hover.png"
            action Jump("cgGallery")
        grid 3 3:
            align (0.5, 0.3)
            spacing 80
            imagebutton:
                focus_mask True
                idle "gallery_buttons/cGGallery/11-i.png"
                hover "gallery_buttons/cGGallery/11-h.png"
                action Jump("g11")
            imagebutton:
                focus_mask True
                idle "gallery_buttons/cGGallery/12-i.png"
                hover "gallery_buttons/cGGallery/12-h.png"
                action Jump("g12")
            imagebutton:
                focus_mask True
                idle "gallery_buttons/cGGallery/13-i.png"
                hover "gallery_buttons/cGGallery/13-h.png"
                action Jump("g13")
            if nicolelvl >= 5:
                imagebutton:
                    focus_mask True
                    idle "gallery_buttons/cGGallery/14-i.png"
                    hover "gallery_buttons/cGGallery/14-h.png"
                    action Jump("g14")
            else:
                null
            if amandakitchenlvl > 2:
                imagebutton:
                    focus_mask True
                    idle "gallery_buttons/cGGallery/15-i.png"
                    hover "gallery_buttons/cGGallery/15-h.png"
                    action Jump("g15")
            else:
                null
            if amandakitchenlvl > 5:
                imagebutton:
                    focus_mask True
                    idle "gallery_buttons/cGGallery/16-i.png"
                    hover "gallery_buttons/cGGallery/16-h.png"
                    action Jump("g16")
            else:
                null
            if amandakitchenlvl > 8:
                imagebutton:
                    focus_mask True
                    idle "gallery_buttons/cGGallery/17-i.png"
                    hover "gallery_buttons/cGGallery/17-h.png"
                    action Jump("g17")
            else:
                null
            if amandakitchenlvl > 8:
                imagebutton:
                    focus_mask True
                    idle "gallery_buttons/cGGallery/18-i.png"
                    hover "gallery_buttons/cGGallery/18-h.png"
                    action Jump("g18")
            else:
                null
            if amandakitchenlvl > 8:
                imagebutton:
                    focus_mask True
                    idle "gallery_buttons/cGGallery/19-i.png"
                    hover "gallery_buttons/cGGallery/19-h.png"
                    action Jump("g19")
            else:
                null
label g11:
    image 11 = "/images/gallery_buttons/cgGallery/11.jpg"
    scene 11
    $ renpy.pause()
    jump cgGallery2
label g12:
    image 12 = "/images/gallery_buttons/cgGallery/12.jpg"
    scene 12
    $ renpy.pause()
    jump cgGallery2
label g13:
    image 13 = "/images/gallery_buttons/cgGallery/13.jpg"
    scene 13
    $ renpy.pause()
    jump cgGallery2
label g14:
    image 14 = "/images/gallery_buttons/cgGallery/14.jpg"
    scene 14
    $ renpy.pause()
    jump cgGallery2
label g15:
    scene 15
    $ renpy.pause()
    jump cgGallery2
label g16:
    scene 16
    $ renpy.pause()
    jump cgGallery2
label g17:
    scene 17
    $ renpy.pause()
    jump cgGallery2
label g18:
    scene 18
    $ renpy.pause()
    jump cgGallery2
label g19:
    scene 19
    $ renpy.pause()
    jump cgGallery2
