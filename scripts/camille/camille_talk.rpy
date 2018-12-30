label camilletalk:
    if camillelvl == 1:
        play music "sounds/armoir.mp3" fadeout 1
        if talkcamille:
            scene black
            scene cam-2 with fade
            p "Hey Camille, we've met before!"
            scene cam-1
            t "...[p]?"
            t "I didn't think I'd see you again."
            p "The town's not too big, I was sure we'd bump into each other again."
            scene cam-3
            t "You... weren't answering my texts and I thought the worst..."
            p "Oh yeah! I gave you my number!"
            p "I'm so sorry Camille, I totally forgot. I actually sold my phone because I needed some money!"
            p "I'll have to get a new one sometime."
            scene cam-2
            t "Oh I see... sorry for assuming."
            p "No, no that's alright."
            p "Anyway, what's happening here?"
            scene cam-4 with dissolve
            t "Oh, sorry I got distracted from my job again!"
            scene cam-5 with dissolve
            t "This is the luxury resort! We have many different kinds of facilities here."
            $ camillelvl += 1
            $ camilletalk = day
            jump Camille
        scene black
        scene cam-2 with fade
        p "Hey."
        p "I think we've met before."
        scene cam-1
        x "Oh, we met at the shopping mall..."
        p "Did you have any luck finding Vincent?"
        scene cam-3
        x "Ah... I must have just missed him..."
        "(Yeah, thought so.)"
        p "So, what's your name?"
        scene cam-3
        t "It's Camille. And you?"
        p "The name's [p]."
        scene cam-5
        t "[p]. I like that name."
        p "Anyway, what's happening here?"
        scene cam-4 with dissolve
        t "Oh, sorry I got distracted from my job again!"
        scene cam-5 with dissolve
        t "This is the luxury resort! We have many different kinds of facilities here."
        $ camillelvl += 1
        $ camilletalk = day
        jump Camille
    ## generic
    scene cam-5
    p "Working hard Camille?"
    t "I always try my best."
    jump Camille
