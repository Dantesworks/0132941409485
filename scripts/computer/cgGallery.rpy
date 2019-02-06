label cgGallery:
    call screen cgGallery
    screen cgGallery:
        add "wallpaper"
        vbox xalign 0.5 ypos 1000:
            text "Page 1"
        imagebutton: ## back
            focus_mask True
            idle "back.png"
            hover "back_hover.png"
            action Jump("computer")
        imagebutton: ## next
            focus_mask True
            idle "logo_next.png"
            hover "logo_next_hover.png"
            action Jump("cgGallery2")
        grid 3 3:
            align (0.5, 0.3)
            spacing 80
            imagebutton:
                focus_mask True
                idle "gallery_buttons/cGGallery/1-i.png"
                hover "gallery_buttons/cGGallery/1-h.png"
                action Jump("g1")
            imagebutton:
                focus_mask True
                idle "gallery_buttons/cGGallery/2-i.png"
                hover "gallery_buttons/cGGallery/2-h.png"
                action Jump("g2")
            imagebutton:
                focus_mask True
                idle "gallery_buttons/cGGallery/3-i.png"
                hover "gallery_buttons/cGGallery/3-h.png"
                action Jump("g3")
            imagebutton:
                focus_mask True
                idle "gallery_buttons/cGGallery/4-i.png"
                hover "gallery_buttons/cGGallery/4-h.png"
                action Jump("g4")
            imagebutton:
                focus_mask True
                idle "gallery_buttons/cGGallery/5-i.png"
                hover "gallery_buttons/cGGallery/5-h.png"
                action Jump("g5")
            imagebutton:
                focus_mask True
                idle "gallery_buttons/cGGallery/7-i.png"
                hover "gallery_buttons/cGGallery/7-h.png"
                action Jump("g7")
            imagebutton:
                focus_mask True
                idle "gallery_buttons/cGGallery/8-i.png"
                hover "gallery_buttons/cGGallery/8-h.png"
                action Jump("g8")
            imagebutton:
                focus_mask True
                idle "gallery_buttons/cGGallery/9-i.png"
                hover "gallery_buttons/cGGallery/9-h.png"
                action Jump("g9")
            imagebutton:
                focus_mask True
                idle "gallery_buttons/cGGallery/10-i.png"
                hover "gallery_buttons/cGGallery/10-h.png"
                action Jump("g10")
label g1:
    image 1 = "/images/gallery_buttons/cgGallery/1.jpg"
    scene 1
    $ renpy.pause()
    jump cgGallery
label g2:
    image 2 = "/images/gallery_buttons/cgGallery/2.jpg"
    scene 2
    $ renpy.pause()
    jump cgGallery
label g3:
    image 3 = "/images/gallery_buttons/cgGallery/3.jpg"
    scene 3
    $ renpy.pause()
    jump cgGallery
label g4:
    image 4 = "/images/gallery_buttons/cgGallery/4.jpg"
    scene 4
    $ renpy.pause()
    jump cgGallery
label g5:
    image 5 = "/images/gallery_buttons/cgGallery/5.jpg"
    scene 5
    $ renpy.pause()
    jump cgGallery
label g7:
    image 7 = "/images/gallery_buttons/cgGallery/7.jpg"
    scene 7
    $ renpy.pause()
    jump cgGallery
label g8:
    image 8 = "/images/gallery_buttons/cgGallery/8.jpg"
    scene 8
    $ renpy.pause()
    jump cgGallery
label g9:
    image 9 = "/images/gallery_buttons/cgGallery/9.jpg"
    scene 9
    $ renpy.pause()
    jump cgGallery
label g10:
    image 10 = "/images/gallery_buttons/cgGallery/10.jpg"
    scene 10
    $ renpy.pause()
    jump cgGallery
