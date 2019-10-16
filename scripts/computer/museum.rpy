default from_museum = 0
label museum:
    if from_computer:
        play music "sounds/special.mp3" fadeout 0.5
        $ from_computer = False
    call screen museum
    screen museum():
        add "wallpaper2.png"
        #add "gallery_buttons/museum/title.png"
        imagebutton: ## juke
            focus_mask True
            idle "juke_i.png"
            hover "juke_h.png"
            action [SetVariable("from_museum", 1), Jump("juke_box")]
        imagebutton: ## back
            focus_mask True
            idle "back.png"
            hover "back_hover.png"
            action Jump("computer")
        imagebutton: ## next
            focus_mask True
            idle "logo_next.png"
            hover "logo_next_hover.png"
            action Jump("museum2")
        grid 3 3:
            align (0.5, 0.3)
            spacing 80
            imagebutton: ## tnvl
                focus_mask True
                idle "/images/gallery_buttons/museum/tnvl_i.png"
                hover "/images/gallery_buttons/museum/tnvl_h.png"
                action Jump("tnvl")
            imagebutton: ## vlad
                focus_mask True
                idle "/images/gallery_buttons/museum/vlad_i.png"
                hover "/images/gallery_buttons/museum/vlad_h.png"
                action Jump("vlad")
            imagebutton: ## dis
                focus_mask True
                idle "/images/gallery_buttons/museum/dis_i.png"
                hover "/images/gallery_buttons/museum/dis_h.png"
                action Jump("dis")
            imagebutton: ## coil3
                focus_mask True
                idle "/images/gallery_buttons/museum/coil3_i.png"
                hover "/images/gallery_buttons/museum/coil3_h.png"
                action Jump("coil3")
            imagebutton: ## coil2
                focus_mask True
                idle "/images/gallery_buttons/museum/coil2_i.png"
                hover "/images/gallery_buttons/museum/coil2_h.png"
                action Jump("coil2")
            imagebutton: ## coil
                focus_mask True
                idle "/images/gallery_buttons/museum/coil_i.png"
                hover "/images/gallery_buttons/museum/coil_h.png"
                action Jump("coil")
            imagebutton: ## raze2
                focus_mask True
                idle "/images/gallery_buttons/museum/raze2_i.png"
                hover "/images/gallery_buttons/museum/raze2_h.png"
                action Jump("raze2")
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

label tnvl:
    scene tnvl
    $ renpy.pause()
    "A voice calls you into the painting."
    menu:
        "Listen to it.":
            "Enjoy this bonus content, brought to you by TNVL!"
            jump cowgirl
        "Resist it.":
            jump museum
label vlad:
    scene vlad
    $ renpy.pause()
    "Will you put some sunscreen on me? | Vladzer"
    jump museum
label dis:
    scene dis
    $ renpy.pause()
    "Make a picture of the female from the game that inspired you the most in making this one | Disimulated"
    #d "The inspiration of my game came from Manic Minxy's Perverted Hotel."
    #d "My favourite characters from that game are Hailey and Brooke, the twin sisters."
    jump museum
label coil2:
    scene coil2
    $ renpy.pause()
    "Greek Goddess Kaira! | Coil X Tesla"
    jump museum
label coil:
    scene coil
    $ renpy.pause()
    "Will you sleep with me tonight? | Coil X Tesla"
    jump museum


label raze2:
    scene raze2
    $ renpy.pause()
    "More sweat | Raze"
    jump museum

label raze:
    scene raze
    $ renpy.pause()
    "Spending time at the sauna | Raze"
    jump museum

label born2game:
    scene born2game
    $ renpy.pause()
    "Relaxing after work | Born2Game"
    jump museum

label yakai:
    scene yakai
    $ renpy.pause()
    "The picture we've all been waiting for | Yakai"
    jump museum2

label lyda:
    scene lyda
    $ renpy.pause()
    "Looking forward to taming Amanda | Lyda"
    jump museum2

label lama:
    scene lama
    $ renpy.pause()
    "J'en ai marre | Lama"
    jump museum2

label dante:
    scene dante
    $ renpy.pause()
    "Commission for Daemon+ patrons | Dante"
    jump museum2
