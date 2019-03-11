label future:
    call hidescreens from _call_hidescreens_10
    hide screen player_room
    if nicolelvl == 6:
        scene black
        play music "sounds/cyberpunk.mp3"
        scene future with flash
        x "Sleeping well, [p]?"
        x "No doubt, after all, with your romantic escapades with Nicole, who wouldn't be sleeping easy?"
        x "She is without doubt a temptress."
        x "Is it blind hedonism that she chases after, or is there something more?"
        x "Is it possible to sink into depravity, and yet remain virtuous?"
        x "Learn more about her, so that you can learn more about yourself."
        scene black with fade
        "Am I still dreaming?"
        $ nicolelvl += 1
        return
    if kairalvl == 3:
        scene black
        play music "sounds/cyberpunk.mp3"
        scene future with flash
        p "Not again."
        x "Feeling conflicted? [p]?"
        x "Let's be honest [p]. You've always had feelings for your [sr], Kaira."
        p "It's not like that."
        p "It's... confusing."
        x "It's inevitable."
        x "It's already happened before."
        p "It's not right. I {i}know{/i} it's not right."
        p "Can I even fight the depravity?"
        x "It cannot be fought, but how you sink in, is up to you."
        p "Then what's the point?"
        p "Nothing I do will change how it ends anyway!"
        p "This dreams keep haunting me. I need to wake up now!"
        x "As you wish. The way out is this way."
        scene black with fade
        stop music
        "Then suddenly, darkness."
        "Is it over now?"
        "I see... is that?"
        p "...Kaira?"
        p "Kaira! Can you hear me?"
        "..."
        "She's not moving."
        "...I must be dreaming, but this seems so real."
        "..."
        "Right now, I can do anything to her, and I can just wake up afterwards."
        "Surely, here of all places, I can give in to my desires."
        "Do I dare?"
        menu nochoice:
            "Have your way with her.":
                $ depravity += 1
            "I can't.":
                "..."
                "But there appears no way out."
                "I have to give in."
        ## fondle boys
