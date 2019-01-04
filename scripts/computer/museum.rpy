label museum:
    if renpy.music.get_playing() != "sounds/medicine.mp3":
        play music "sounds/medicine.mp3" fadeout 1
    call screen museum
    screen museum():
        add "wallpaper2.png"
        #add "gallery_buttons/museum/title.png"
        imagebutton: ## back
            focus_mask True
            idle "back.png"
            hover "back_hover.png"
            action Jump("computer")
        grid 3 3:
            xfill
            yfill
            align (0.5, 0.5)
            spacing 100
            imagebutton: ## lyda
                focus_mask True
                idle "/images/gallery_buttons/museum/lyda_i.png"
                hover "/images/gallery_buttons/museum/lyda_h.png"
                action Jump("lyda")
            imagebutton: ## dante
                focus_mask True
                idle "/images/gallery_buttons/museum/dante_i.png"
                hover "/images/gallery_buttons/museum/dante_h.png"
                action Jump("dante")
            null
            null
            null
            null
            null
            null
            null
label lyda:
    image lyda = "/images/gallery_buttons/museum/lyda.jpg"
    scene lyda
    $ renpy.pause()
    "\"Looking forward to taming Amanda\" | Commissioned by Lyda"
    jump museum

label dante:
    image dante = "/images/gallery_buttons/museum/dante.jpg"
    scene dante
    $ renpy.pause()
    "\"Commission for Android+ patrons\" | Commissioned by Dante"
    jump museum
