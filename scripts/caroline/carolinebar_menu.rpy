label Carolinebar:
    hide screen map_icon
    scene cb-1
    p "Hey Caroline!"
    scene cb-2
    c "Good to see you [p]!"
    c "How can I help you today?"
    menu barask:
        "I just wanted to talk to you.":
            if drinks:
                jump bartalk
            else:
                jump nobardrink
        "Alright let's grab a drink!":
            jump drinksmenu
        "What is this 'premium lounge?'":
            scene cb-2
            c "Why, it's where our most esteemed customers hang out!"
            p "How come it's so special?"
            c "Interesting and important characters come and go there - you should definitely check it out sometime!"
            p "How do I join?"
            c "That's easy! Just spend $100 on drinks, and the membership is yours!"
            jump barask
        "Never mind.":
            jump barentrance
label drinksmenu:
    scene cb-2
    c "Lovely!"
    c "What would the gentleman like today?"
    menu:
        "Original Dante - $10":
            if cash - 10 < 0:
                scene cb-3
                c "You don't have enough money - are you sure you're not drunk already?"
            elif drinks:
                scene cb-4
                c "You should finish your drink before you order another one."
            else:
                "Very original!"
                $ cash -= 10
                $ premiumcount += 10
                $ dante = True
                call drinks from _call_drinks
        "The Pink Russian - $8":
            if cash - 8 < 0:
                scene cb-3
                c "You don't have enough money - are you sure you're not drunk already?"
            elif drinks:
                scene cb-4
                c "You should finish your drink before you order another one."
            else:
                c "Fantastic choice."
                $ cash -= 8
                $ premiumcount += 8
                $ russian = True
                call drinks from _call_drinks_1
        "Damn, too expensive.":
            c "Drinks aren't cheap here!"
    scene cb-1
    jump barask

label nobardrink:
    scene black
    "Are you fucking retarded?"
    "At least buy a drink before you talk to the lady."
    "Try again, fool!"
    scene cb-1
    jump barask
