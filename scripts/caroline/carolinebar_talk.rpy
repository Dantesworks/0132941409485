label bartalk:
    if carolinebarlvl == 1:
        play music "sounds/dreams.mp3" fadeout 1
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
        play music "sounds/popstars.mp3" fadeout 1
        scene cb-1
        jump barask
    ## Generic
    scene cb-5
    p "Good to see you Caroline!"
    scene cb-8
    c "Good to see you too, remember to take care of yourself!"
    scene cb-1
    jump barask
