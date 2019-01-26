label Kaira:
    call hidescreens from _call_hidescreens_1
    scene k-1
    if amandalvl == 2 and kairalvl == 1:
        jump kairatalk
    menu:
        "Talk":
            jump kairatalk
