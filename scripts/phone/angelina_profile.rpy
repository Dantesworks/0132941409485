screen angelina_profile():
    zorder 7
    imagebutton: ## Close
        idle "phone/close.png"
        action Hide("angelina_profile")
    imagebutton: ## Profile
        focus_mask True
        idle "phone/profile/angelina_profile.png"
        action NullAction()
    imagebutton: ## Home
        focus_mask True
        idle "phone/home.png"
        action [Show("homescreen"), Hide("angelina_profile")]
    viewport xalign 0.5 yanchor 0 ypos 480 xsize 350 ysize 420 draggable True mousewheel True arrowkeys True:
        vbox xsize 350:
            text "A mysterious encounter with a knight of the holy order!" justify True size 18
    viewport xalign 0.5 yanchor 0 ypos 410 xsize 350 ysize 40 draggable True mousewheel True arrowkeys True:
        vbox xsize 350: #tips
            if cowgirl:
                text "View her art in the museum of patrons." justify True size 18
            else:
                text "Content complete for this version - this is a patreon commissioned character." justify True size 18
