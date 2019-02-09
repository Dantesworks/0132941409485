screen nicole_profile():
    imagebutton: ## Close
        idle "phone/close.png"
        action Hide("nicole_profile")
    imagebutton: ## Profile
        focus_mask True
        idle "phone/profile/nicole_profile.png"
        action NullAction()
    imagebutton: ## Home
        focus_mask True
        idle "phone/home.png"
        action [Show("homescreen"), Hide("nicole_profile")]
    viewport xalign 0.5 yanchor 0 ypos 480 xsize 350 ysize 420 draggable True mousewheel True arrowkeys True:
        vbox xsize 350:
            text "[p] first met Nicole through Kaira. To say she made an impression was an understatment. \
If her looks didn't betray her already, Nicole is a seductress. Her perfectly sculpted body, Kaira reveals, \
may not have been entirely scuplted by nature, but perhaps in part by a surgical blade. Recognising the depravity within [p], \
Nicole doesn't hesitate to goad him into actions he might not usually perform, including intimate experiences with his own [sr]. \
The only certainty about Nicole is her confidence in her own appearance, and the willingness to augment herself to further sex appeal. \
Other than that, her motivations regarding [p] and [sr] are an enigma, and is something that [p] has resolved himself to elucidate." justify True size 18
    viewport xalign 0.5 yanchor 0 ypos 410 xsize 350 ysize 40 draggable True mousewheel True arrowkeys True:
        vbox xsize 350:
            if nicolelvl == 8:
                text "Content complete for this version! Vote for this character on Patreon to see more." justify True size 18
