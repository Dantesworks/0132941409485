label Nicole:
    hide screen map_icon
    hide screen daytime
    scene n-1
    if nicolelvl == 1:
        jump nicoletalk
    menu:
        "Talk":
            jump nicoletalk
        "May over Nicole, I'm coming in.":
            jump amanda_money
        "Actually, never mind.":
            jump living_room
