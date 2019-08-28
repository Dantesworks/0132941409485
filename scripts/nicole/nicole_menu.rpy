label Nicole:
    call hidescreens from _call_hidescreens_7
    scene n-1
    if nicolelvl == 1:
        jump nicoletalk
    menu:
        "Talk.":
            jump nicoletalk
        "You're looking lonely there." if nicolelvl > 1:
            jump nicolesit
        "Actually, never mind.":
            jump living_room
