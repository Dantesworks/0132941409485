default nicoleboth = False
default kairaboth = False
default amandaboth = False

default kairaday = 2
default nicoleday = 2
default amandaday = 1

default amandalvl = 1
default kairalvl = 1
default nicolelvl = 1
default cash = 0
default daytime = 1
default day = 1
default nicoledelay = 0
## Day Cycle
if daytime > 3:
    $ daytime = 1
    $ day += 1
## Sleep
label sleep:
    scene black
    menu:
        "Take a nap." if daytime < 3:
            $ daytime += 1

        "Sleep until the next day.":
            $ daytime = 1
            $ day += 1
    jump player_room
## Daytime Screen
screen daytime():
    zorder 3
    if daytime == 1:
        text "Morning"
    if daytime == 2:
        text "Afternoon"
    if daytime == 3:
        text "Night"
