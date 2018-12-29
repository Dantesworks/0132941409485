label Amanda:
    hide screen daytime
    hide screen map_icon
    scene a-1
    if amandalvl == 1:
        jump amandatalk
    menu:
        "Talk":
            jump amandatalk
        "Hey [mr]. Can I have some money?":
            jump amanda_money
        "Actually, never mind.":
            jump amanda_room
