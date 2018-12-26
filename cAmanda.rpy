label Amanda:
    hide screen daytime
    hide screen map_icon
    scene a-1
    menu:
        "Talk":
            if amandalvl == 1:
                play music "sounds/wisteria.mp3" fadeout 1
                p "Hi [mr]."
                m "Good morning [p], and I see this time you've even got your clothes on!"
                p "Oooh, I'm so sorry about that."
                scene a-2
                p "I can't help it you know, my feet just take me to random places when I'm sleep walking!"
                scene a-9
                m "Did you have a wild night last night?"
                "I probably shouldn't tell her I fucked Nicole..."
                p "Uh, no uh, of course not, it was a pretty normal night. What do you mean wild?"
                scene a-3
                m "You didn't go out to party with Kaira and Nicole?"
                p "Ah of course! Yeah we went out, it was great. I thought you were talking about something else."
                scene a-4
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
                scene a-1
                m "Well maybe you can meet her in a different context, and ask her out sometime."
                p "I'll have to meet her again first."
                p "Anyway, I should probably check up on Kaira."
                scene a-9
                m "She's gone out with Nicole to the cafe to get some coffee. They might be on their way bakc now. She should be back in the afternoon!"
                p "And where will you be?"
                scene a-8
                m "Oh dearie, [mr] has to go and work."
                m "I ought to be back sometime in the evening."
                p "Have fun modelling [mr], don't give too many guys nosebleeds!"
                scene a-7
                m "Oh stop it!"
                play music "sounds/heart.mp3" fadeout 1
                $ amandalvl += 1
                jump Amanda
            scene a-1
            p "Looking good [mr]!"
            scene a-6 with dissolve
            m "Like I said, I've still got it!"
            jump Amanda
        "Hey [mr]. Can I have some money?":
            if pocketmoney:
                scene a-3
                m "I'm only working a part time job!"
                scene a-2
                m "I can't spare too much, but how about $5?"
                scene a-8
                m "Maybe if the job paid better..."
                scene a-1
                p "Thanks!"
                "I wonder if there's a way to help [mr] out."
                $ pocketmoney = False
                $ cash += 15
                jump Amanda
            scene a-4 with dissolve
            m "You've already asked for money today!"
            scene a-5
            m "I wish I had more to give. You should help out sometime and earn your keep!"
            p "Haha, I'll look for a way."
            jump Amanda
        "Actually, never mind.":
            jump amanda_room
