label amandatalk:
    if amandalvl == 1:
        scene black
        scene a-1 with fade
        play music "sounds/wisteria.mp3" fadeout 1
        p "Hi [mr]."
        m "Good morning [p], and I see this time you've even got your clothes on!"
        p "Oooh, I'm so sorry about that."
        scene a-2
        p "I can't help it you know, my feet just take me to random places when I'm sleep walking!"
        scene a-1
        m "Did you have a wild night last night?"
        "I probably shouldn't tell her I fucked Nicole..."
        p "Uh, no uh, of course not, it was a pretty normal night. What do you mean wild?"
        scene a-3
        m "You didn't go out to party with Kaira and Nicole?"
        p "Ah of course! Yeah we went out, it was great. I thought you were talking about something else."
        scene a-4 with dissolve
        m "What did you think I was talking about?"
        "Fuck!"
        p "Uhh... I'm not sure anymore. Ah, I think the alcohol is still disabling my brain a bit!"
        p "Wernicke's encephalopathy, or something."
        scene a-5
        m "What's that?"
        p "Oh apparently it's something you get from too much alcohol. This medical student called Caroline I met at the bar told me about it."
        scene a-6 with dissolve
        m "Wow, look at you! Meeting girls at the bar!"
        m "Was she cute?"
        p "Oh no haha, I mean, she's beautiful, but she was the bar maid. Not really looking to meet anyone you know."
        scene a-1 with dissolve
        m "Well maybe you can meet her in a different context, and ask her out sometime."
        p "I'll have to meet her again first."
        p "Anyway, I should probably check up on Kaira."
        scene a-1
        m "She's gone out with Nicole to the cafe to get some coffee. They might be on their way back now. She should be back in the afternoon!"
        m "You can take a nap on your bed to pass time."
        p "And where will you be?"
        scene a-8
        m "Oh dearie, [mr] has to go and work."
        m "I ought to be back sometime in the evening."
        p "Have fun modelling [mr], don't give too many guys nosebleeds!"
        scene a-7 with dissolve
        m "Oh stop it!"
        play music "sounds/heart.mp3" fadeout 1
        $ amandalvl += 1
        $ amandatalk = day
        $ amandakitchen = True
        jump amanda_room
    if amandalvl == 2 and amandakitchenlvl == 2 and day > amandatalk:
        scene black
        scene a-2 with fade
        play music "sounds/wisteria.mp3" fadeout 1
        p "Good morning, [mr]!"
        p "Getting ready for another day of work?"
        scene a-1
        m "The work never stops."
        p "It's enjoyable work though, right?"
        scene a-8
        m "..."
        scene a-2 with dissolve
        m "Yes, it's quite fun."
        "She doesn't sound too convinced?"
        p "Tell me about it."
        p "What kind of work do you do?"
        scene a-3
        m "Well, I model. I go into the studio, get some shots done, and I get some payment."
        p "Is it stressful?"
        scene a-4 with dissolve
        m "Well..."
        scene a-5 with dissolve
        m "It's never an easy thing you know, to relax in front of the camera."
        m "It takes a lot of honesty, and you have to be very confident to do it well."
        p "You should be really confident, you're gorgeous [mr]!"
        p "I can't imagine you could take a bad picture."
        scene a-6 with dissolve
        m "Oh, [p], fufufu..."
        m "Thanks for the encouragement!"
        p "I'm only telling the truth, you know that."
        scene a-7
        m "And how are you going yourself?"
        p "Just hanging around town, getting to know different people I guess."
        p "Enjoy work, [mr]."
        scene a-5
        m "I will. I'll tell you all about it when I get back this evening~!"
        $ amandalvl += 1
        $ amandatalk = day
        jump amanda_room

    scene a-1
    p "Looking good [mr]!"
    scene a-6 with dissolve
    m "Like I said, I've still got it!"
    jump amanda_room
