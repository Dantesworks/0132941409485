screen veronica_profile():
    zorder 7
    imagebutton: ## Close
        idle "phone/close.png"
        action Hide("veronica_profile")
    imagebutton: ## Profile
        focus_mask True
        idle "phone/profile/veronica_profile.png"
        action NullAction()
    imagebutton: ## Home
        focus_mask True
        idle "phone/home.png"
        action [Show("homescreen"), Hide("veronica_profile")]
    viewport xalign 0.5 yanchor 0 ypos 480 xsize 350 ysize 420 draggable True mousewheel True arrowkeys True:
        vbox xsize 350:
            text "Ah, Veronica, [p]'s teacher during his high school years. [p] had a crush on Veronica back then, but then again, who didn't? \
Kind, motherly, beautiful. These are just some words used to describe Veronica. A fortuitous meeting would lead to events, \
surely, to the prosperity of both parties. And the rest is history." justify True size 18
    viewport xalign 0.5 yanchor 0 ypos 410 xsize 350 ysize 40 draggable True mousewheel True arrowkeys True:
        vbox xsize 350: # tips
            if gym_intro == False:
                text "Acquire bronze membership at the resort, then go to the gym." justify True size 18
            elif veronicalvl == 2:
                text "Go to the gym." justify True size 18
            elif veronicalvl == 3:
                text "Go to the gym." justify True size 18
            elif veronicalvl == 4:
                text "Go to the gym." justify True size 18
            else:
                text "Content complete for now - this is a patreon commissioned character." justify True size 18
