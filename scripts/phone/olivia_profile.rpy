screen olivia_profile():
    zorder 7
    imagebutton: ## Close
        idle "phone/close.png"
        action Hide("olivia_profile")
    imagebutton: ## Profile
        focus_mask True
        idle "phone/profile/olivia_profile.png"
        action NullAction()
    imagebutton: ## Home
        focus_mask True
        idle "phone/home.png"
        action [Show("homescreen"), Hide("olivia_profile")]
    viewport xalign 0.5 yanchor 0 ypos 480 xsize 350 ysize 420 draggable True mousewheel True arrowkeys True:
        vbox xsize 350:
            text "Olivia is a stern and strict woman, a fitting character for someone employed as a lecturer. \
[p] disovers that she, however, is not as morally upright as the impression she is trying to exude, and it will be \
up to [p] to bring her back to earth." justify True size 18
    viewport xalign 0.5 yanchor 0 ypos 410 xsize 350 ysize 40 draggable True mousewheel True arrowkeys True:
        vbox xsize 350: # tips
            if gym_intro == False:
                text "Acquire bronze membership at the resort, then go to the gym." justify True size 18
            elif gym_intro and olivialvl < 3:
                text "Go the University location on the map." justify True size 18
            elif olivialvl == 3:
                if dildo == False:
                    text "Go purchase the dildo from the online shop, then go to the University." justify True size 18
                elif vdildo == True and plugged == False:
                    text "Buy and use the butt plug from the online shop, then go to the University." justify True size 18
                elif plugged == True:
                    text "Put the vaginal dildo in for her." justify True size 18
            elif olivialvl == 4:
                text "Go the University location on the map." justify True size 18
            elif olivialvl == 5:
                text "Buy the slutty outfit then go back to the university." justify True size 18
            elif olivialvl == 6:
                text "Go the University location on the map." justify True size 18
            elif olivialvl == 7:
                text "Acquire a camera with kit lens, then go the University location on the map." justify True size 18
            elif olivialvl == 8:
                text "Go the University location on the map." justify True size 18
            elif olivialvl == 9:
                text "Go the University location on the map." justify True size 18
            elif olivialvl == 10 and plugged2 == False:
                text "Put in the butt plug for her and follow her at the end." justify True size 18
            elif olivialvl == 11:
                text "Go the University location on the map." justify True size 18
            elif olivialvl == 12:
                text "Go the University location on the map." justify True size 18
            else:
                text "Content complete for now - this is a patreon commissioned character." justify True size 18
