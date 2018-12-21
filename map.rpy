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
    call screen hallway
    screen hallway():
        imagemap:
            idle "hallway_idle"
            hover "hallway_hover"

            hotspot(422,385,119,269) hovered Show("displayTextScreen", displayText = "Living Room") action [Hide("displayTextScreen"), Jump("living_room")] unhovered Hide("displayTextScreen")
            hotspot(1446, 6, 297, 1051) hovered Show("displayTextScreen", displayText = "Kaira's Bedroom") action [Hide("displayTextScreen"), Jump("kaira_room")] unhovered Hide("displayTextScreen")
            hotspot(869, 378, 34, 283) hovered Show("displayTextScreen", displayText = "Amanda's Bedroom") action [Hide("displayTextScreen"), Jump("amanda_room")] unhovered Hide("displayTextScreen")

label living_room:
    call screen living_room
    screen living_room():
        imagemap:
            idle "living_room_idle"
            hover "living_room_hover"
            hotspot(3,14,214,691) action [Hide("displayTextScreen"), Jump("hallway")] hovered Show("displayTextScreen", displayText = "Hallway") unhovered Hide("displayTextScreen")
            hotspot(1259,29,206,435) action [Hide("displayTextScreen"), Jump("kitchen")] hovered Show("displayTextScreen", displayText = "Kitchen") unhovered Hide("displayTextScreen")
        imagebutton:
            focus_mask True
            idle "nicole_couch_idle.png"
            hover "nicole_couch_hover.png"
            hovered Show("displayTextScreen", displayText = "Nicole") action [Hide("displayTextScreen"), Jump("hallway")] unhovered Hide("displayTextScreen")


label kitchen:
    call screen kitchen
    screen kitchen():
        imagemap:
            idle "kitchen_idle"
            hover "kitchen_hover"
            hotspot(1515,693,398,388) action [Hide("displayTextScreen"), Jump("living_room")] hovered Show("displayTextScreen", displayText = "Living Room") unhovered Hide("displayTextScreen")

label kaira_room:
    call screen kaira_room
    screen kaira_room():
        imagemap:
            idle "kaira_room_idle"
            hover "kaira_room_hover"
            hotspot(0, 693, 183, 386) action [Hide("displayTextScreen"), Jump("hallway")] hovered Show("displayTextScreen", displayText = "Hallway") unhovered Hide("displayTextScreen")

        imagebutton:
            focus_mask True
            idle "kaira_sitting_idle.png"
            hover "kaira_sitting_hover.png"
            hovered Show("displayTextScreen", displayText = "Kaira") action [Hide("displayTextScreen"), Jump("hallway")] unhovered Hide("displayTextScreen")

label amanda_room:
    call screen amanda_room
    screen amanda_room():
        imagemap:
            idle "amanda_room_idle"
            hover "amanda_room_hover"
            hotspot(0, 964, 1390, 108) action [Hide("displayTextScreen"), Jump("hallway")] hovered Show("displayTextScreen", displayText = "Hallway") unhovered Hide("displayTextScreen")

        imagebutton:
            focus_mask True
            idle "amanda_standing_idle.png"
            hover "amanda_standing_hover.png"
            hovered Show("displayTextScreen", displayText = "Amanda") action [Hide("displayTextScreen"), Jump("hallway")] unhovered Hide("displayTextScreen")
