label museum:
    call screen museum
    screen museum():
        add "wallpaper2.png"
        add "gallery_buttons/museum/title.png"
        imagebutton: ## back
            focus_mask True
            idle "back.png"
            hover "back_hover.png"
            action Jump("computer")
        imagebutton:
            focus_mask True
            idle "gallery_buttons/museum/frame1.png"
            hover "gallery_buttons/museum/frame1_hover.png"
            action Jump("mus1")
        add "gallery_buttons/museum/sig1.png"
        add "gallery_buttons/museum/sub1.png"

label mus1:
    image mus1 = "/images/gallery_buttons/museum/1.jpg"
    scene mus1
    $ renpy.pause()
    "Kaira - commissioned by Dante. Daemon tier and above patrons can commission their own with custom signature, subtitle, and message."
    jump museum
