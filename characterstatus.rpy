default kairashow = ["2"]
default nicoleshow = []
default amandashow = ["1"]
default camilleshow = ["1"]
default carolineshow = ["1"]

default amandalvl = 1
default kairalvl = 1
default nicolelvl = 1
default camillelvl = 1
default carolinelvl = 1

default cash = 0
default daytime = 1
default daytimes = str(daytime)
default day = 1
default nicoledelay = 0

## Permissions

default loungestatus = False
default amandanight = False
## Day Cycle
if daytime > 4:
    $ daytime = 1
    $ day += 1
label daykeep:
    $ daytime += 1
    $ daytimes = str(daytime)
    return

## Sleep
label sleep:
    scene black
    menu:
        "Take a nap." if daytime < 4:
            $ daytime += 1

        "Sleep until the next day.":
            $ daytime = 1
            $ day += 1
    $ daytimes = str(daytime)
    jump player_room
## Daytime Screen
screen daytime():
    zorder 3
    if daytime == 1:
        add "ui_morning.png"
    if daytime == 2:
        add "Ui_afternoon.png"
    if daytime == 3:
        add "ui_evening.png"
    if daytime == 4:
        add "ui_night.png"
