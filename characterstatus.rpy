default kairashow = ["2"]
default nicoleshow = []
default amandashow = ["1","3"]
default camilleshow = ["1"]
default carolineshow = ["1", "4"]

default amandalvl = 1
default kairalvl = 1
default nicolelvl = 1
default camillelvl = 1
default carolinelvl = 1
default carolinebarlvl = 1

default cash = 0
default items = []
default daytime = 1
default daytimes = str(daytime)
default day = 1
default nicoledelay = 0
default pocketmoney = True
default premiumcount = 0

default dante = False #drinks
default russian = False #drinks
default drinks = False

label drinks:
    if dante == True or russian == True:
        $ drinks = True
    return
## Permissions

default loungestatus = False
default amandanight = False


## Day Cycle
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
    $ carolineshow = ["1","4"]
    $ pocketmoney = True
    $ dante = False
    $ russian = False
    $ drinks = False
    ## remove cafe drinks
    if "coffee" in items:
        $ items.remove("coffee")
    if "water" in items:
        $ items.remove("water")
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
    add "cash_ui.png"
    text "[cash]" xpos 210 ypos 75 size 24 text_align 1
## Misc.
define flash = Fade(0.1, 0.0, 0.5, color="#fff")
define lastplayed = ""
