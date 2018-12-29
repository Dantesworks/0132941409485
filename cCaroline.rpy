label Caroline:
    hide screen map_icon
    hide screen daytime
    if carolinelvl == 1:
        scene black
        scene cc-1 with fade
        p "Hey there. Caroline right?"
        scene cc-2 with dissolve
        c "...?"
        scene cc-3
        c "Oh hey! You're the guy at the bar when I was working."
        p "That's me."
        p "Um, would you mind if I joined you?"
        c "Not at all!"
        scene cc-5 with dissolve
        c "So, it's [p], isn't it?"
        p "You remember my name! But of course, you must have a great memory."
        scene cc-6
        c "I also remember you guys getting quite wild, you even had to carry your [sr] away."
        p "Yeah, I didn't think we would actually get to that haha."
        p "So what are you doing here?"
        scene cc-9
        c "A cup of coffee is my favourite thing in the morning."
        c "I also bring some notes so that I can study while I enjoy my coffee."
        scene cc-5
        c "Just perfect, ah~"
        p "Looks like you've got a nice deal sorted for yourself here."
        scene cc-4
        c "And what about you?"
        if "water" in items and not "coffee" in items:
            scene cc-8
            c "You've come to a cafe to buy water."
            c "Hehehe, allergic to coffee?"
            p "Yeah, money's a little tight right now."
            scene cc-16
            c "Aww that's okay. It's hard to find a job in today's market."
        if "water" in items and "coffee" in items:
            scene cc-5
            c "You've got a coffee {i}and{/i} water."
            c "Is the coffee too strong by itself?"
            p "I just couldnt decide which one to buy, so I bought both."
        if "coffee" in items and not "water" in items:
            scene cc-5
            c "You bought a cup of coffee - I see you've got a similar taste to mine."
            p "I love coffee."
            p "It's like, I don't even have blood in my veins, it's all coffee pumping through."
            scene cc-9
            c "I've found a kindred spirit!"
        scene cc-12
        c "I take it you're not a regular?"
        p "Whoa, how would you know, are you my stalker?"
        scene cc-13
        c "Hmm..."
        c "I come here {i}everyday{/i}, [p]. I think I'd have seen you if you do come around a bit."
        p "Alright, I'll come clean. I've only come here recently."
        p "I used to live here actually, but I moved away to study. But now that's done, so I'm here."
        scene cc-5
        c "Oh so you've already graduated?"
        p "Oh no, um. Something went wrong and I had to leave early."
        scene cc-16
        c "Ah, sorry I brought it up."
        p "That's no problem at all."
        scene cc-4
        c "..."
        p "So how long have you been working at the bar for?"
        scene cc-5
        c "Oh, for a few months. I work every night, so come say hi if you can!"
        p "Oh I will."
        p "What are you studying now?"
        scene cc-6
        c "I am studying... well, reviewing the criteria for the diagnosis of mental disorders."
        p "Ah so that's like DSM-5 criteria?"
        scene cc-12
        c "The DSM-5 is more like... a guideline."
        scene cc-5
        c "I would say if anyone is suffering mentally, then it's up to the clinician to render treatment that's tailored to the individual."
        p "Wow, you sound like a really empathetic person."
        p "I'd want you to be my doctor if I'm ever sick in the head!"
        scene cc-9
        c "You joke about it now, but mental illness is more like a spectrum, and we're all on it!"
        c "Whether you cross the line or not depends on many things, like your environment, the choices you make, and the potential consequences."
        p "You're saying our choices do matter."
        scene cc-14
        c "We are what we do."
        p "Absolutely fascinating..."
        c "Hahahaha!"
        p "Erm, I hope I haven't been distracting you from your study."
        scene cc-4
        c "I enjoy the break from the monotony, it's nice to have someone to talk to."
        p "Well, I've got another question."
        scene cc-5
        c "Yes?"
        p "That girl who was sitting next to me at the bar - you know her?"
        scene cc-15
        c "Ah, her name's Camille."
        scene cc-5
        c "It's rare for her to come up to the bar. She usually hangs out at the premium lounge."
        p "Is she quite shy?"
        scene cc-6
        c "I.. suppose. Why, are you interested?"
        menu:
            "I'm interested in all women I meet.":
                $ depravity += 1
                scene cc-14
                c "How bold!"
            "No, just curious.":
                scene cc-13
                c "Really?"
        p "I'm sorry, would you rather me talk about you instead?"
        scene cc-9
        c "Bahaha!"
        scene cc-11 with fade
        c "Oh dear, I've had a lot of fun, but my coffee is almost finished."
        p "Time flies when you're having fun."
        scene cc-5
        c "I have to go now, I'll see you tomorrow if you come around again. Otherwise, ta~!"
        scene cc-4
        p "Laters."
        scene cc-17 with dissolve
        "Hmm, this town ain't so bad."
        "Maybe I should go and see her tonight at the bar?"
        $ carolinelvl += 1
        $ daytime += 1
        $ daytimes = str(daytime)
        jump map
    scene cc-2
    p "Good morning Caroline!"
    scene cc-3
    c "Good morning, [p]."
    c "I'm trying to cram right now. Sorry about this, but could you talk to me later?"
    jump cafe

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

label bartalk:
    if carolinebarlvl == 1:
        scene black
        scene cb-5 with fade
        p "So, how's it going Caroline?"
        scene cb-6
        c "It's going good, [p]."
        p "Busy night tonight?"
        c "Same old, same old."
        p "Reckon you could get me into the premium lounge?"
        scene cb-8
        c "I'm afraid not."
        p "Please, I'll make it up to you."
        scene cb-9
        c "I'm just following the rules, [p]!"
        $ carolinebarlvl += 1
        scene cb-1
        jump barask
    ## Generic
    scene cb-5
    p "Good to see you Caroline!"
    scene cb-8
    c "Good to see you too, remember to take care of yourself!"
    scene cb-1
    jump barask
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
