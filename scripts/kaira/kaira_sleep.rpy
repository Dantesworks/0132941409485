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
                "Go further.":
                    call wip from _call_wip
                    "Alright, that's enough, I need to get out of here."
                    jump kaira_room

        "Leave.":
            jump kaira_room
    jump kaira_room
