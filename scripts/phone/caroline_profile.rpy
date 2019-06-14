screen caroline_profile():
    zorder 7
    imagebutton: ## Close
        idle "phone/close.png"
        action Hide("caroline_profile")
    imagebutton: ## Profile
        focus_mask True
        idle "phone/profile/caroline_profile.png"
        action NullAction()
    imagebutton: ## Home
        focus_mask True
        idle "phone/home.png"
        action [Show("homescreen"), Hide("caroline_profile")]
    viewport xalign 0.5 yanchor 0 ypos 480 xsize 350 ysize 420 draggable True mousewheel True arrowkeys True:
        vbox xsize 350:
            text "Caroline is a medical student who is independent and capable. Despite her rigorous study, she works a part time job \
at the local bar. If approached flirtatiously during work, Caroline would reject advances, demonstrating professionalism and responsibility. \
She appears to be quite optimisic about the idea of love, and tells [p] that no matter how society may view a relationship, it should not matter if \
the two people are truly in love with one another. While polite and reserved, Caroline attracts a level of respect from most people, and [p] \
unwittingly gains more and more respect for her at every interaction." justify True size 18
    viewport xalign 0.5 yanchor 0 ypos 410 xsize 350 ysize 40 draggable True mousewheel True arrowkeys True:
        vbox xsize 350:
            if carolinelvl == 1 and carolinebarlvl == 1:
                text "Go to the Cafe." justify True size 18
            elif carolinelvl == 2 and carolinebarlvl == 1:
                text "Go to the Bar." justify True size 18
            elif carolinelvl == 2 and carolinebarlvl == 2:
                text "Go to the Cafe." justify True size 18
            elif carolinelvl == 3:
                text "Go to the Cafe." justify True size 18
            else:
                text "Content complete for this version! Vote for this character on Patreon to see more." justify True size 18
