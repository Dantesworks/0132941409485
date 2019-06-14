screen camille_profile():
    zorder 7
    imagebutton: ## Close
        idle "phone/close.png"
        action Hide("camille_profile")
    imagebutton: ## Profile
        focus_mask True
        idle "phone/profile/camille_profile.png"
        action NullAction()
    imagebutton: ## Home
        focus_mask True
        idle "phone/home.png"
        action [Show("homescreen"), Hide("camille_profile")]
    viewport xalign 0.5 yanchor 0 ypos 480 xsize 350 ysize 420 draggable True mousewheel True arrowkeys True:
        vbox xsize 350:
            text "[p] first met Camille by accident and his first conduct with her was one of trickery, as he lied about the location \
of the man she was pursuing. This may be fitting however, as there is an aura of a certain mystery surrounding Camille, and [p] cannot \
put his finger on it. Something is not as it seems. Perhaps these impressions are in part due to her shy and demure nature, and of her few words. The one thing clear is \
that Camille shared some history with Vincent. Perhaps interrogating Vincent will yield some clues on this mysterious figure." justify True size 18
    viewport xalign 0.5 yanchor 0 ypos 410 xsize 350 ysize 40 draggable True mousewheel True arrowkeys True:
        vbox xsize 350: #tips
            if camillelvl == 1:
                text "Go to the resort." justify True size 18
            elif camillelvl == 2:
                text "Make sure you have Nicole's phone, then go to the resort." justify True size 18
            elif camillelvl == 3:
                text "Make sure you have silver membership, then talk to Camille." justify True size 18
            elif camillelvl == 4:
                text "Go to the resort." justify True size 18
            elif camillelvl == 5:
                text "Go talk to Amanda in her bedroom in the morning." justify True size 18

            else:
                text "Content complete for this version! Vote for this character on Patreon to see more." justify True size 18
