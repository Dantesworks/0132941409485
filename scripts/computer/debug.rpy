label hacks:
    scene main_menu1
    menu:
        "Renamer":
            call renamer from _call_renamer
            jump hacks
        "Back":
            jump computer


label renamer:
    $ player = renpy.input("What is your name?")
    $ player = player.strip()
    if player == "":
        $ player = "Anon"

    $ mr = renpy.input("The older woman you live at home with is your ???. (Default = landlord)")
    $ mr = mr.strip()
    $ mr = mr.lower()
    if mr == "":
        $ mr = "landlord"

    $ sr = renpy.input("The younger woman you live with at home is your ???. (Default = housemate")
    $ sr = sr.strip()
    $ sr = sr.lower()
    if sr == "":
        $ sr = "housemate"

    "[p], [mr], [sr]."
    return

label wip:
    scene black
    "Work in progress! Check back later!"
    return
