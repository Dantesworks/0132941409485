screen displayTextScreen:
    zorder 100
    default displayText = ("")

    vbox:
        xalign 0.5
        ypos 50
        frame:
            text "{size=+6}[displayText]{/size}"

label hallway:
    if daytime != 4:
        if renpy.music.get_playing() != "sounds/heart.mp3":
            play music "sounds/heart.mp3" fadeout 1
    if daytime == 4:
        if renpy.music.get_playing() != "sounds/alchemy.mp3":
            play music "sounds/alchemy.mp3" fadeout 1
    show screen map_icon
    show screen daytime
    call screen hallway
    screen hallway():
        imagemap:
            idle "hallway_idle"
            hover "hallway_hover"
            if daytime == 4:
                idle "hallway2"
                hover "hallway2_hover"

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
            idle "living_room_idle"
            hover "living_room_hover"
            if daytime == 4:
                idle "living_room2"
                hover "living_room2_hover"
            hotspot(3,14,214,691) action [Hide("displayTextScreen"), Jump("hallway")] hovered Show("displayTextScreen", displayText = "Hallway") unhovered Hide("displayTextScreen")
            hotspot(1259,29,206,435) action [Hide("displayTextScreen"), Jump("kitchen")] hovered Show("displayTextScreen", displayText = "Kitchen") unhovered Hide("displayTextScreen")
        if nicoledelay <= day and (daytimes in nicoleshow):
            imagebutton:
                focus_mask True
                idle "nicole_couch_idle.png"
                hover "nicole_couch_hover.png"
                hovered Show("displayTextScreen", displayText = "Nicole") action [Hide("displayTextScreen"), Jump("Nicole")] unhovered Hide("displayTextScreen")

label kitchen:
    hide screen map_icon
    show screen daytime
    call screen kitchen
    screen kitchen():
        add "kitchen"
        if daytime == 4:
            add "kitchen2"
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
        add "kaira_room_idle"
        if daytime == 4:
            add "kaira_room2"
            imagebutton:
                focus_mask True
                idle "kaira_sleep.png"
                hover "kaira_sleep_hover.png"
                hovered Show("displayTextScreen", displayText = "Kaira") action [Hide("displayTextScreen"), Jump("kaira_sleep")] unhovered Hide("displayTextScreen")
        if daytimes in kairashow:
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
    if amandanight or daytime != 4:
        call screen amanda_room
        screen amanda_room():
            add "amanda_room_idle"
            if daytime == 4:
                add "amanda_room2"
                imagebutton:
                    focus_mask True
                    idle "amanda_sleep.png"
                    hover "amanda_sleep_hover.png"
                    hovered Show("displayTextScreen", displayText = "Amanda") action [Hide("displayTextScreen"), Jump("amanda_sleep")] unhovered Hide("displayTextScreen")
            if daytimes in amandashow:
                imagebutton:
                    focus_mask True
                    idle "amanda_standing_idle.png"
                    hover "amanda_standing_hover.png"
                    hovered Show("displayTextScreen", displayText = "Amanda") action [Hide("displayTextScreen"), Jump("Amanda")] unhovered Hide("displayTextScreen")
            imagebutton:
                focus_mask True
                idle "back.png"
                hover "back_hover.png"
                action Jump("hallway")
    jump amandalocked
label player_room:
    if daytime != 4:
        if renpy.music.get_playing() != "sounds/heart.mp3":
            play music "sounds/heart.mp3" fadeout 1
    if daytime == 4:
        if renpy.music.get_playing() != "sounds/alchemy.mp3":
            play music "sounds/alchemy.mp3" fadeout 1
    hide screen map_icon
    show screen daytime
    call screen player_room
    screen player_room():
        imagemap:
            idle "player_room"
            hover "player_room_hover"
            if daytime == 4:
                idle "player_room2"
                hover "player_room2_hover"
            hotspot(614, 212, 180, 522) action [Hide("displayTextScreen"), Jump("hallway")] hovered Show("displayTextScreen", displayText = "Hallway") unhovered Hide("displayTextScreen") #hallway
            hotspot(1461, 695, 456, 242) action [Hide("displayTextScreen"), Jump("sleep")] hovered Show("displayTextScreen", displayText = "Bed") unhovered Hide("displayTextScreen") #bed

        imagebutton:
            if daytime != 4:
                focus_mask True
                idle "laptop.png"
                hover "laptop_hover.png"
                hovered Show("displayTextScreen", displayText = "Computer") action [Hide("displayTextScreen"), Jump("computer")] unhovered Hide("displayTextScreen") # computer
            else:
                focus_mask True
                idle "laptop2.png"
                hover "laptop2_hover.png"
                hovered Show("displayTextScreen", displayText = "Computer") action [Hide("displayTextScreen"), Jump("computer")] unhovered Hide("displayTextScreen") # computer

## Room Permission Labels

label amandalocked:
    scene hallway2
    "The door is locked."
    jump hallway
