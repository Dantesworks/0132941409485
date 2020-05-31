label hacks:
    scene main_menu1
    menu:
        "Renamer":
            call renamer from _call_renamer
            jump hacks
        "Play Amanda alternative route" if amandalvl >= 21 and wildbillvariant == False:
            play music "sounds/alchemy.mp3" fadeout 1
            jump aphro_choice
        "Debugging":
            "Amanda [amandalvl] [amandakitchenlvl]"
            "Caroline [carolinelvl] [carolinebarlvl]"
            "Kaira [kairalvl]"
            "Nicole [nicolelvl]"
            "Camille [camillelvl]"
            jump computer
        "Gifts of the Bogdanoffs":
            $ cash += 1000
            jump computer
        "Amanda isn't showing up when she is supposed to!":
            "Don't click this if you don't have this problem!!"
            menu:
                "Oops I made a mistake":
                    jump computer
                "I meant to click this":
                    $ amandashow = ["1"]
                    $ amandakitchen = True
                    jump computer
        "No new Olivia content!":
            $ olivialvl = 11
            "Fixed!"
            jump computer
        "Go back to the trip" if teleport:
            jump teleporter
        "Back":
            jump computer


label renamer:
    $ player = renpy.input("What is your name?")
    $ player = player.strip()
    if player == "":
        $ player = "Anon"

    $ mr = renpy.input("The older woman you live at home with is your ???. (Default = landlady)")
    $ mr = mr.strip()
    $ mr = mr.lower()
    if mr == "":
        $ mr = "landlady"

    $ sr = renpy.input("The younger woman you live with at home is your ???. (Default = housemate")
    $ sr = sr.strip()
    $ sr = sr.lower()
    if sr == "":
        $ sr = "housemate"

    "[p], [mr], [sr]."
    return

label wip:
    scene black
    d "Work in progress! Check back later!"
    d "Vote Kaira and I promise you a scene next update."
    return

# label splashlogo:
#     $ persistent.abc = True
#     $ ab = renpy.random.randint(10, 20)
#     $ ab3 = int(ab + 4)
#     $ ab2_preint = renpy.input("[ab]")
#     if ab2_preint == "":
#         $ ab2_preint = 2000
#     else:
#         $ ab2_preint = int(ab2_preint)
#     $ ab2 = ab2_preint#int("[ab2_preint]")
#     $ ab4 = ab2 - ab3
#     if ab4 == 0:
#         $ persistent.abc = False
#         return
#     else:
#         return
