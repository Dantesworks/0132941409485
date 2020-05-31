default tifalvl = 1
label tifa_story:
    if tifalvl == 1:
        play music "sounds/those.mp3" fadeout 1
        scene black
        scene ti1 with fade
        tifa "Hello, I'm sorry to disturb you. But I need some help."
        p "Help?"
        scene ti2 with dissolve
        tifa "My name is Tifa, and I'm lost."
        scene ti3 with dissolve
        tifa "I was in the middle of a fight, and I was teleported here somehow."
        tifa "Perhaps it was the result of some kind of materia."
        scene ti4 with dissolve
        tifa "So please, tell me, where am I?"
        scene ti5 with dissolve
        p "This... is the resort."
        scene ti6 with dissolve
        tifa "The resort?"
        p "Yeah..."
        scene ti7 with dissolve
        tifa "Are we still on Gaia?"
        p "Gaia? What's Gaia?"
        scene ti8 with dissolve
        tifa "This must be some sort of interdimensional travel!"
        scene ti9 with dissolve
        tifa "And... why am I dressed like this?"
        p "You don't usually fight in that gear?"
        scene ti10 with dissolve
        tifa "No! Of course not - this must be also the effect of that spell!"
        scene ti11 with dissolve
        tifa "How embarassing."
        p "I never thought you were real, Tifa!"
        scene ti12 with dissolve
        tifa "Real? You have heard of me before?"
        p "Yeah, you're really popular!"
        scene ti13 with dissolve
        tifa "While it seems I'll be stuck in this world a little while, this world doesn't seem too bad!"
        scene ti14 with dissolve
        tifa "So, I'll be enlisting you for help!"
        scene ti15 with dissolve
        p "My help?"
        tifa "Hmmm..."
        tifa "It might take me some time to figure out how to get back. In the meantime, I'll need to get out of this outfit."
        tifa "Maybe there's someone else I could talk to for help?"
        tifa "Hey~!"
        scene ti16 with dissolve
        p "Um! I'm not sure, Tifa. But I could take you somewhere to get changed."
        scene ti17 with dissolve
        tifa "Good. Unfortunately, I don't have any gil on me, so I won't be able to pay for clothes."
        p "Gil? That must be the currency you use there. Don't worry, I might have some money on me."
        scene ti18 with dissolve
        tifa "You have my thanks."
        scene ti19 with dissolve
        p "But - hang on, how is this even happening? I'm confused. How did you even-"
        scene ti20 with dissolve
        tifa "You can ask the questions later, after I get out of these clothes!"
        p "Fair enough, Tifa, you're right. The questions can wait."
        p "Let me check if I've got enough cash."
        scene ti21 with dissolve
        tifa "I'll be right here."
        $ tifalvl += 1
        jump publicbathouse
    if tifalvl == 2:
        play music "sounds/those.mp3" fadeout 1
        scene black
        scene ti21 with fade
        "I'll need at least $100 to buy Tifa all her clothes. I should make sure I have that much."
        "Let's see..."
        if cash < 100:
            p "Drat, I'm a bit short on cash. I'll have to come back later."
            tifa "I'll be waiting here. Please remember, I still need your help!"
            jump publicbathouse
