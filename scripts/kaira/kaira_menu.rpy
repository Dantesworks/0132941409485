label Kaira:
    call hidescreens
    scene k-1
    if amandalvl == 2 and kairalvl == 1:
        jump kairatalk
    menu:
        "Talk":
            jump kairatalk
