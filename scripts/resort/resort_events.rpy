label resortEvents:
    call hidescreens
    hide screen fastforward
    scene black
    menu:
        "Nicole event" if nicolelvl == 4 and day > nicoleday and daytime == 2:
            jump nicoleBathhouse
    return
