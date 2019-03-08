label Amanda:
    call hidescreens from _call_hidescreens_4
    hide screen skip_evening
    scene a-1
    if amandalvl == 1:
        jump amandatalk
    menu:
        "Talk":
            jump amandatalk
        "Hey [mr]. Can I have some money?" if amandakitchenlvl < 10:
            jump amanda_money
        "Actually, never mind.":
            jump amanda_room
