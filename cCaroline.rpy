label Caroline:
    if carolinelvl == 1:
        p "Hey there. Caroline right?"
        c "...?"
        c "Oh hey! You're the guy at the bar when I was working."
        p "That's me."
        p "Um, would you mind if I joined you?"
        c "Not at all!"
        c "So, it's [p], isn't it?"
        p "You remember my name! But of course, you must have a great memory."
        c "I also remember you guys getting quite wild, you even had to carry your [sr] away."
        p "Yeah, I didn't think we would actually get to that haha."
        p "So what are you doing here?"
        c "A cup of coffee is my favourite thing in the morning."
        c "I also bring some notes so that I can study while I enjoy my coffee."
        c "Just perfect, ah~"
        p "Looks like you've got a nice deal sorted for yourself here."
        c "And what about you?"
        if "water" in items and not "coffee" in items:
            c "You've come to a cafe to buy water."
            c "Hehehe, allergic to coffee?"
            p "Yeah, money's a little tight right now."
            c "Aww that's okay. It's hard to find a job in today's market."
        if "water" in items and "coffee" in items:
            c "You've got a coffee {i}and{/i} and water."
            c "Is the coffee too strong by itself?"
            p "I just couldnt decide which one to buy, so I bought both."
        if "coffee" in items and not "water" in items:
            c "I see you've got a similar taste to mine."
            p "I love coffee."
            p "It's like, I don't even have blood in my veins, it's all coffee pumping through."
            c "I've found a kindred spirit!"
        c "I take it you're not a regular?"
        p "Whoa, how would you know, are you my stalker?"
        c "Hmm..."
        c "I come here {i}everyday{/i}, [p]. I think I'd have seen you if you do come around a bit."
        p "Alright, I'll come clean. I've only come here recently."
        p "I used to live here actually, but I moved away to study. But now that's done, so I'm here."
        c "Oh so you've already graduated?"
        p "Oh no, um. Something went wrong and I had to leave early."
        c "Ah, sorry I brought it up."
        p "That's no problem at all."
        c "..."
        p "So how long have you been working at the bar for?"
        c "Oh, for a few months. I work every night, so come say hi if you can!"
        p "Oh I will."
        p "What are you studying now?"
        c "I am studying... well, reviewing the criteria for the diagnosis of mental disorders."
        p "Ah so that's like DSM-5 criteria?"
        c "The DSM-5 is more like... a guideline."
        c "I would say if anyone is suffering mentally, then it's up to the clinician to render treatment that's tailored to the individual."
        p "Wow, you sound like a really empathetic person."
        p "I'd want you to be my doctor if I'm ever sick in the head!"
        c "You joke about it now, but mental illness is more like a spectrum, and we're all on it!"
        c "Whether you cross the line or not depends on many things, like your environment, the choices you make, and the potential consequences."
        p "You're saying our choices do matter."
        c "We are what we do."
        p "Absolutely fascinating..."
        c "Hahahaha!"
        p "Erm, I hope I haven't been distracting you from your study."
        c "I enjoy the break from the monotony, it's nice to have someone to talk to."
        p "Well, I've got another question."
        c "Yes?"
        p "That girl who was sitting next to me at the bar - you know her?"
        c "Ah, her name's Camille."
        c "It's rare for her to come up to the bar. She usually hangs out at the premium lounge."
        p "Is she quite shy?"
        c "I.. suppose. Why, are you interested?"
        menu:
            "I'm interested in all women I meet.":
                $ depravity += 1
                c "How bold!"
            "No, just curious.":
                c "Really?"
        p "I'm sorry, would you rather us talk about you instead?"
        c "Bahaha!"
        c "Oh dear, I've had a lot of fun, but my coffee is almost finished."
        p "Time flies when you're having fun."
        c "I have to go now, I'll see you tomorrow if you come around again. Otherwise, ta~!"
        p "Laters."
        "Hmm, this town ain't so bad."
        "Maybe I should go and see her tonight at the bar?"
        $ carolinelvl += 1
        $ carolineshow = ["4"]
        jump cafe
    p "Good morning Caroline!"
    c "Good morning, [p]."
    c "I'm trying to cram right now. Sorry about this, but could you talk to me later?"
    jump cafe

label Carolinebar:
    p "Hey Caroline!"
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
            c "Why, it's where our most esteemed customers hang out!"
            p "How come it's so special?"
            c "Interesting and important characters come and go there - you should definitely check it out sometime!"
            p "How do I join?"
            c "That's easy! Just spend $100 on drinks, and the membership is yours!"
            jump barask
        "Never mind.":
            jump barentrance

label bartalk:
    if carolinebarlvl == 2:
        p "So, how's it going Caroline?"
        c "It's going good, [p]."
        p "Busy night tonight?"
        c "Same old, same old."
        p "Reckon you could get me into the premium lounge?"
        c "I'm afraid not."
        p "Please, I'll make it up to you."
        c "I'm just following the rules, [p]!"
        $ carolinebarlvl += 1
        jump barask
    ## Generic
    p "Good to see you Caroline!"
    c "Good to see you too, remember to take care of yourself!"
    jump barask
label drinksmenu:
    c "Lovely!"
    c "What would the gentleman like today?"
    menu:
        "Original Dante - $10":
            if cash - 10 < 0:
                c "You don't have enough money - are you sure you're not drunk already?"
            elif drinks:
                c "You should finish your drink before you order another one."
            else:
                "Very original!"
                $ cash -= 10
                $ premiumcount += 10
                $ dante = True
                call drinks
        "The Pink Russian - $8":
            if cash - 8 < 0:
                c "You don't have enough money - are you sure you're not drunk already?"
            elif drinks:
                c "You should finish your drink before you order another one."
            else:
                c "Fantastic choice."
                $ cash -= 8
                $ premiumcount += 8
                call drinks
        "Damn, too expensive.":
            c "Drinks aren't cheap here!"
    jump barask
label nobardrink:
    scene black
    "Are you fucking retarded? You've either finished your drink already, or haven't bought one yet."
    "At least buy a drink before you talk to the lady."
    "Try again, fool!"
    jump barask
