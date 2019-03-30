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
            imagebutton: ## raze
                focus_mask True
                idle "/images/gallery_buttons/museum/raze_i.png"
                hover "/images/gallery_buttons/museum/raze_h.png"
                action Jump("raze")
            imagebutton: ## born2game
                focus_mask True
                idle "/images/gallery_buttons/museum/born2game_i.png"
                hover "/images/gallery_buttons/museum/born2game_h.png"
                action Jump("born2game")
            imagebutton: ## yakai
                focus_mask True
                idle "/images/gallery_buttons/museum/yakai_i.png"
                hover "/images/gallery_buttons/museum/yakai_h.png"
                action Jump("yakai")
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
label raze:
    scene raze
    $ renpy.pause()
    "Full of sweat | Commissioned by RAZE"
    jump museum

label born2game:
    scene born2game
    $ renpy.pause()
    "Relaxing after work | Commissioned by Born2Game"
    jump museum

label yakai:
    scene yakai
    $ renpy.pause()
    "The picture we've all been waiting for | Commissioned by Yakai"
    jump museum

label lyda:
    scene lyda
    $ renpy.pause()
    "Looking forward to taming Amanda | Commissioned by Lyda"
    jump museum

label lama:
    scene lama
    $ renpy.pause()
    "J'en ai marre | Commissioned by Lama"
    jump museum

label dante:
    scene dante
    $ renpy.pause()
    "Commission for Android+ patrons | Commissioned by Dante"
    jump museum
