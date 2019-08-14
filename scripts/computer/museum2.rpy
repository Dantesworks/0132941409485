label museum2:
    call screen museum2
    screen museum2():
        add "wallpaper2.png"
        #add "gallery_buttons/museum/title.png"
        imagebutton: ## juke
            focus_mask True
            idle "juke_i.png"
            hover "juke_h.png"
            action [SetVariable("from_museum", 2), Jump("juke_box")]
        imagebutton: ## back
            focus_mask True
            idle "back.png"
            hover "back_hover.png"
            action Jump("computer")
        imagebutton: ## previous
            focus_mask True
            idle "logo_previous.png"
            hover "logo_previous_hover.png"
            action Jump("museum")
        grid 3 3:
            align (0.5, 0.3)
            spacing 80
            imagebutton: ## lyda
                focus_mask True
                idle "/images/gallery_buttons/museum/lyda_i.png"
                hover "/images/gallery_buttons/museum/lyda_h.png"
                action Jump("lyda")
            imagebutton: ## lama
                focus_mask True
                idle "/images/gallery_buttons/museum/lama_i.png"
                hover "/images/gallery_buttons/museum/lama_h.png"
                action Jump("lama")
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

label coil3:
    scene coil3
    $ renpy.pause()
    "The temperature of the hot spring is just right, why don’t you... | Coil X Tesla"
    jump museum
