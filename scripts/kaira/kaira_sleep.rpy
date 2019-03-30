label kaira_sleep:
    call hidescreens from _call_hidescreens_14
    hide screen phone_icon
    scene black
    scene ks-1 with fade
    "Kaira's sleeping in just her underwear."
    "She looks so cute when she's sleeping."
    "What should I do?"
    menu:
        "Let's get that bra off.":
            "I shouldn't be doing this to my [sr], but I can't resist."
            scene ks-2 with dissolve
            "Wow, look at those tits."
            "You've really developed, Kaira."
            "Those nipples are nice and perky..."
            "I wonder what you're dreaming of."
            menu:
                "Massage her breasts.":
                    scene ks-3 with dissolve
                    "I can't believe I'm doing this, but she'll never find out, right?"
                    scene ks-4 with dissolve
                    "They're so soft yet firm at the same time. So this is what large and natural breasts feel like."
                    scene
                    $ renpy.movie_cutscene("animations/ks1.mpg", loops=-1, stop_music=False)
                    scene ks-5
                    s "Uhh... zzzz"
                    "Oh shit, is she waking?"
                    "Alright, that's enough, I need to get out of here."
                    jump kaira_room
        "Take her underwear off.":
            "I've been curious what you look like under there, Kaira."
            scene ks-6 with flash
            "Oh my god, she has an innie."
            scene ks-7 with dissolve
            "It's the perfect pussy. I can't imagine how tight it is in there."
            "..."
            "Nah, it'll never happen."
            "Better get out of here while I still can."
            jump kaira_room
        "Leave.":
            jump kaira_room
    jump kaira_room
