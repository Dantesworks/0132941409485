label cafe:
    if renpy.music.get_playing() != "sounds/coffee.mp3":
        play music "sounds/coffee.mp3" fadeout 1
    show screen map_icon
    show screen daytime
    call screen cafe
    screen cafe():
        add "cafe"
        imagebutton: ## ellie
            focus_mask True
            idle "elliecafe.png"
            hover "elliecafe_hover.png"
            action Jump("ellie_menu")
        if daytimes in carolineshow:
            imagebutton: ## caroline
                focus_mask True
                idle "carolinecafe.png"
                hover "carolinecafe_hover.png"
                if "coffee" in items or "water" in items:
                    action Jump("Caroline")
                else:
                    action Jump("nodrink")
label ellie_menu:
    scene ellie_menu
    ellie "Good morning sir! What would you like to drink today?"
    menu:
        "Coffee - $2":
            if "coffee" in items:
                ellie "You've already bought a coffee already!"
            else:
                if cash - 2 < 0:
                    ellie "Oh sorry, you don't seem to have enough money. You can always come back next time!"
                else:
                    $ cash -= 2
                    $ items.append("coffee")
                    ellie "Excellent choice! The caffeine is a great start to a productive day!"
        "Water - $1":
            if "water" in items:
                ellie "You've already bought a water already!"
            else:
                if cash - 1 < 0:
                    ellie "Oh sorry, you don't seem to have enough money. You can always come back next time!"
                else:
                    $ cash -= 1
                    $ items.append("water")
                    ellie "Always a good idea to stay hydrated!"
        "Do you have any job openings?" if cafejobask:
            ellie "Actually, we do! We're looking for a part-timer who can wash the dishes."
            p "Sounds like something I can do."
            p "When do I start?"
            ellie "Just pop over in the mornings and you can start your shift."
            "Sweet, getting a job is so easy."
            $ cafejob = True
            $ cafejobask = False
        "I'm here to start my shift." if cafejob:
            jump cafeJob
        "Actually, nothing for me.":
            ellie "No worries, do come back if you change your mind!"
    jump cafe
label nodrink:
    hide screen daytime
    hide screen map_icon
    scene black
    "Don't tell me you're actually going to sit down with her without a drink in hand."
    "What are you, some kind of freeloader?"
    "What are you, fucking gay?"
    "Try again, fool."
    jump cafe
