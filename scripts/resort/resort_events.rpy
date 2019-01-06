label resortEvents:
    hide screen map_icon
    hide screen daytime
    scene black
    menu:
        "Nicole event" if nicolelvl == 4 and day > nicoleday and daytime == 2:
            jump nicoleBathhouse
    return
