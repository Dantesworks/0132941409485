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
