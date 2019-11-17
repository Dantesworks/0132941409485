# default persistent.abc = True
# label abc:
#     if persistent.abc:
#         $ renpy.quit()
#     else:
#         return

# At home only
default kairashow = ["2"]
default nicoleshow = []
default amandashow = ["1"]
default camilleshow = []
default carolineshow = ["1", "4"]

## Character lvl
default amandalvl = 1
default amandakitchenlvl = 1
default kairalvl = 1
default nicolelvl = 1
default camillelvl = 1
default carolinelvl = 1
default carolinebarlvl = 1

## Character event delay
default amandaday = 1
default kairaday = 1
default nicoleday = 1
default camilleday = 1
default carolineday = 1
default carolinebarday = 1
## Outside home show commands
default amandakitchen = False

default cash = 0
default items = []
default daytime = 1
default daytimes = str(daytime)
default day = 1
default nicoledelay = 0
default pocketmoney = True
default premiumcount = 0

default cafejob = False
default cafejobask = True

default dante = False #drinks
default russian = False #drinks
default drinks = False

label drinks:
    if dante == True or russian == True:
        $ drinks = True
    return
## Permissions

default facilitiesIntro = False
default resortmembership = 0
label membershipcheck:
    if resortmembership == 0:
        $ membership = "no"
        $ nextmembership = "Bronze"
        $ membershipcost = 100
    elif resortmembership == 1:
        $ membership = "Bronze"
        $ nextmembership = "Silver"
        $ membershipcost = 200
    elif resortmembership == 2:
        $ membership = "Silver"
        $ nextmembership = "Gold"
        $ membershipcost = 500
    elif resortmembership == 3:
        $ membership = "Gold"
    return

default loungestatus = False
default amandanight = False
default talkcamille = False

## Day Cycle
label daykeep:
    $ daytime += 1
    $ daytimes = str(daytime)
    return

## Sleep
label fastforward:
    if daytime < 4:
        $ daytime += 1
        $ daytimes = str(daytime)
    jump map
label sleep:
    show screen player_room
    menu:
        "Take a nap." if daytime < 4:
            $ daytime += 1

        "Sleep until the next day.":
            #call abc
            $ daytime = 1
            $ day += 1
            call future from _call_future
            $ pocketmoney = True
            $ dante = False
            $ russian = False
            $ drinks = False
            call cryptoChange from _call_cryptoChange
            $ bogged = False
            $ renpy.free_memory()
    $ daytimes = str(daytime)
    if nicolelvl == 4:
        $ nicoleshow = []
    ## remove cafe drinks
    if "coffee" in items:
        $ items.remove("coffee")
    if "water" in items:
        $ items.remove("water")
    hide screen player_room
    jump player_room
## Daytime Screen
screen daytime():
    zorder 10
    if daytime == 1:
        add "ui_morning.png"
    if daytime == 2:
        add "Ui_afternoon.png"
    if daytime == 3:
        add "ui_evening.png"
    if daytime == 4:
        add "ui_night.png"
    add "cash_ui.png"
    text "[cash]" xanchor 1.0 xpos 270 ypos 73 size 24
screen skip_evening:
    zorder 3
    imagebutton:
        focus_mask True
        idle "ui_skip_evening.png"
        hover "ui_skip_evening_hover.png"
        action [Hide("skip_evening"), Jump("skip_evening")]
label skip_evening:
    call daykeep from _call_daykeep_11
    call daykeep from _call_daykeep_12
    jump amanda_room

## Misc.
define flash = Fade(0.1, 0.0, 0.5, color="#fff")
label hidescreens:
    hide screen daytime
    hide screen map_icon
    hide screen phone_icon
    return
