label Nicole:
    hide screen map_icon
    hide screen daytime
    scene n-1
    if nicolelvl == 1:
        jump nicoletalk
    menu:
        "Talk":
            jump nicoletalk
        # "Move over Nicole, I'm coming in." if nicolelvl == 10:
        #     jump amanda_money
        "Actually, never mind.":
            jump living_room
