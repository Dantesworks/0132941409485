default nicoleshow = True
default kairashow = True
default amandashow = True
default amandalvl = 1
default kairalvl = 1
default nicolelvl = 1
default cash = 0
default daytime = 1
default day = 1
default nicoleday = 0
## Day Cycle
if daytime > 3:
    $ daytime = 1
    $ day += 1
## Sleep
label sleep:
    scene black
    if daytime < 3:
        menu sleep1:
            "Take a nap.":
                $ daytime += 1

            "Sleep until the next day.":
                $ daytime = 1
                $ day += 1
        jump player_room
    menu sleep2:
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
