label hacks:
    scene main_menu1
    menu:
        "Renamer":
            call renamer from _call_renamer
            jump hacks
        "Debugging":
            "Amanda [amandalvl] [amandakitchenlvl]"
            "Caroline [carolinelvl] [carolinebarlvl]"
            "Kaira [kairalvl]"
            "Nicole [nicolelvl]"
            "Camille [camillelvl]"
            jump computer
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
#     $ ab3 = int(ab + 7)
#     $ ab2 = int(renpy.input("[ab]"))
#     $ ab4 = ab2 - ab3
#     if ab4 == 0:
#         $ persistent.abc = False
#         return
#     else:
#         return
