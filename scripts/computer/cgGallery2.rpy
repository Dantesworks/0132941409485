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
            null
            null
            null
            null
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
