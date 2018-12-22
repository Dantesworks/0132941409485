screen displayTextScreen:
    key "hide_windows" action NullAction()
    zorder 100
    default displayText = ("")

    vbox:
        xalign 0.5
        ypos 50
        frame:
            text "{size=+6}[displayText]{/size}"

label hallway:
    show screen map_icon
    show screen daytime
    call screen hallway
    screen hallway():
        imagemap:
            if daytime == 1:
                idle "hallway_idle"
            if daytime == 2:
                idle "hallway_idle"
            if daytime == 3:
                idle "hallway_idle"
            hover "hallway_hover"

            hotspot(422,385,119,269) hovered Show("displayTextScreen", displayText = "Living Room") action [Hide("displayTextScreen"), Jump("living_room")] unhovered Hide("displayTextScreen")
            hotspot(1446, 6, 297, 1051) hovered Show("displayTextScreen", displayText = "Kaira's Bedroom") action [Hide("displayTextScreen"), Jump("kaira_room")] unhovered Hide("displayTextScreen")
            hotspot(869, 378, 34, 283) hovered Show("displayTextScreen", displayText = "Amanda's Bedroom") action [Hide("displayTextScreen"), Jump("amanda_room")] unhovered Hide("displayTextScreen")
            hotspot(987, 270, 77, 504) hovered Show("displayTextScreen", displayText = "My Bedroom") action [Hide("displayTextScreen"), Jump("player_room")] unhovered Hide("displayTextScreen")

label living_room:
    hide screen map_icon
    show screen daytime
    call screen living_room
    screen living_room():
        imagemap:
            if daytime == 1:
                idle "living_room_idle"
            if daytime == 2:
                idle "living_room_idle"
            if daytime == 3:
                idle "living_room_2"
            hover "living_room_hover"
            hotspot(3,14,214,691) action [Hide("displayTextScreen"), Jump("hallway")] hovered Show("displayTextScreen", displayText = "Hallway") unhovered Hide("displayTextScreen")
            hotspot(1259,29,206,435) action [Hide("displayTextScreen"), Jump("kitchen")] hovered Show("displayTextScreen", displayText = "Kitchen") unhovered Hide("displayTextScreen")
        if nicoleday <= day and daytime == 2 and nicoleshow:
            imagebutton:
                focus_mask True
                idle "nicole_couch_idle.png"
                hover "nicole_couch_hover.png"
                hovered Show("displayTextScreen", displayText = "Nicole") action [Hide("displayTextScreen"), Jump("hallway")] unhovered Hide("displayTextScreen")

label kitchen:
    hide screen map_icon
    show screen daytime
    call screen kitchen
    screen kitchen():
        if daytime == 1:
            add "kitchen"
        if daytime == 2:
            add "kitchen"
        if daytime == 3:
            add "kitchen"
        imagebutton:
            focus_mask True
            idle "back.png"
            hover "back_hover.png"
            action Jump("living_room")
label kaira_room:
    hide screen map_icon
    show screen daytime
    call screen kaira_room
    screen kaira_room():
        if daytime == 1:
            add "kaira_room_idle"
        if daytime == 2:
            add "kaira_room_idle"
        if daytime == 3:
            add "hallway_idle"
        if daytime == 2 and kairashow:
            imagebutton:
                focus_mask True
                idle "kaira_sitting_idle.png"
                hover "kaira_sitting_hover.png"
                hovered Show("displayTextScreen", displayText = "Kaira") action [Hide("displayTextScreen"), Jump("Kaira")] unhovered Hide("displayTextScreen")
        imagebutton:
            focus_mask True
            idle "back.png"
            hover "back_hover.png"
            action Jump("hallway")

label amanda_room:
    hide screen map_icon
    show screen daytime
    call screen amanda_room
    screen amanda_room():
        if daytime == 1:
            add "amanda_room_idle"
        if daytime == 2:
            add "amanda_room_idle"
        if daytime == 3:
            add "amanda_room_2"
        if daytime == 1 and amandashow:
            imagebutton:
                focus_mask True
                idle "amanda_standing_idle.png"
                hover "amanda_standing_hover.png"
                hovered Show("displayTextScreen", displayText = "Amanda") action [Hide("displayTextScreen"), Jump("amanda")] unhovered Hide("displayTextScreen")
        imagebutton:
            focus_mask True
            idle "back.png"
            hover "back_hover.png"
            action Jump("hallway")
label player_room:
    hide screen map_icon
    show screen daytime
    call screen player_room
    screen player_room():
        imagemap:
            if daytime == 1:
                idle "player_room"
            if daytime == 2:
                idle "player_room"
            if daytime == 3:
                idle "player_room"
            hover "player_room_hover"
            hotspot(614, 212, 180, 522) action [Hide("displayTextScreen"), Jump("hallway")] hovered Show("displayTextScreen", displayText = "Hallway") unhovered Hide("displayTextScreen") #hallway
            hotspot(1461, 695, 456, 242) action [Hide("displayTextScreen"), Jump("sleep")] hovered Show("displayTextScreen", displayText = "Bed") unhovered Hide("displayTextScreen") #bed


        imagebutton:
            focus_mask True
            idle "laptop.png"
            hover "laptop_hover.png"
            hovered Show("displayTextScreen", displayText = "Computer") action [Hide("displayTextScreen"), Jump("computer")] unhovered Hide("displayTextScreen") # computer
