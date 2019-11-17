screen nicole_profile():
    zorder 7
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
may not have been entirely sculpted by nature, but perhaps in part by a surgical blade. Recognising the depravity within [p], \
Nicole doesn't hesitate to goad him into actions he might not usually perform, including intimate experiences with his own [sr]. \
The only certainty about Nicole is her confidence in her own appearance, and the willingness to augment herself to further sex appeal. \
Other than that, her motivations regarding [p] and [sr] are an enigma, and is something that [p] has resolved himself to elucidate." justify True size 18
    viewport xalign 0.5 yanchor 0 ypos 410 xsize 350 ysize 40 draggable True mousewheel True arrowkeys True:
        vbox xsize 350:
            if nicolelvl == 1:
                text "Talk to Amanda, Kaira, then talk to Nicole in the living room in the afternoon." justify True size 18
            elif nicolelvl == 2:
                text "Talk to Nicole in the afternoon after going to sleep." justify True size 18
            elif nicolelvl == 3:
                text "Make sure you have the bronze membership, then talk to Nicole." justify True size 18
            elif nicolelvl == 4:
                text "Go to the resort in the afternoon tomorrow." justify True size 18
            elif nicolelvl == 5:
                text "Talk to Nicole in the afternoon after going to sleep." justify True size 18
            elif nicolelvl == 6:
                text "Go to sleep." justify True size 18
            elif nicolelvl == 7:
                text "Talk to Nicole in the afternoon." justify True size 18
            elif nicolelvl == 8:
                text "Talk to Nicole in the afternoon." justify True size 18
            elif nicolelvl == 9:
                text "Talk to Nicole in the afternoon." justify True size 18
            elif nicolelvl == 10:
                text "Go to sleep." justify True size 18
            elif nicolelvl == 11 and (carolinelvl < 7 or kairalvl < 8 or amandalvl < 21):
                text "Play the other girl's routes." justify True size 18
            elif kairalvl == 8 and nicolelvl == 11:
                text "Talk to Kaira in her room in the afternoon." justify True size 18
            elif kairalvl == 9 and nicolelvl == 11:
                text "Talk to Nicole about the trip." justify True size 18
            elif kairalvl == 9 and nicolelvl == 12 and amandalvl == 21:
                text "Talk to [mr] about the trip in the morning." justify True size 18
            elif kairalvl == 9 and nicolelvl == 12 and amandalvl == 22 and (private_jet == False or luxurious_hotels == False or rv == False):
                text "Go to the shop on the computer to organise the trip." justify True size 18
            elif kairalvl == 9 and nicolelvl == 12 and amandalvl == 22 and private_jet and luxurious_hotels and rv:
                text "Talk to Kaira in her room in the afternoon." justify True size 18
            elif kairalvl == 10:
                text "Talk to Kaira again to start the trip!" justify True size 18
            else:
                text "Content complete for this version! Vote for this character on Patreon to see more." justify True size 18
