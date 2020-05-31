screen kaira_profile():
    zorder 7
    imagebutton: ## Close
        idle "phone/close.png"
        action Hide("kaira_profile")
    imagebutton: ## Profile
        focus_mask True
        idle "phone/profile/kaira_profile.png"
        action NullAction()
    imagebutton: ## Home
        focus_mask True
        idle "phone/home.png"
        action [Show("homescreen"), Hide("kaira_profile")]
    viewport xalign 0.5 yanchor 0 ypos 480 xsize 350 ysize 420 draggable True mousewheel True arrowkeys True:
        vbox xsize 350:
            text "When [p] met Kaira again, he discovered that she was no longer \
the young girl she had once been. She had grown in many ways, and she knew this too. She hints that she is still not fully content, however and [p] has noted that there have been a few times where she expressed \
envy when confronted by other woman with larger breasts than her. Nevertheless, she is learning to use guile and charm to manipulate \
others to satisfy her desires, and who better to practise on than [p]? With the influence of Nicole, she will be a \
force to be reckoned with indeed. She put these skills to practise on the second day, wearing alluring outfits to catch the eye of \
[p]. The day would culminate in an intimate experience between all parties involved, yet Kaira will deny remembering any of it." justify True size 18
    viewport xalign 0.5 yanchor 0 ypos 410 xsize 350 ysize 40 draggable True mousewheel True arrowkeys True:
        vbox xsize 350: # tips
            if kairalvl == 1:
                text "Talk to Kaira in her room in the afternoon." justify True size 18
            elif kairalvl == 2:
                text "Talk to Kaira in her room in the afternoon." justify True size 18
            elif kairalvl == 3:
                text "Talk to Kaira in her room in the afternoon." justify True size 18
            elif kairalvl == 4:
                text "Purchase the gold membership from the resort, then talk to Kaira in her room in the afternoon." justify True size 18
            elif kairalvl == 5:
                text "Go to bed." justify True size 18
            elif kairalvl == 6:
                text "Talk to Kaira in her room in the afternoon." justify True size 18
            elif kairalvl == 7:
                text "Talk to Kaira in her room in the afternoon." justify True size 18
            elif kairalvl == 8 and (nicolelvl < 11 or carolinelvl < 7 or amandalvl < 21):
                text "Play the other girl's routes." justify True size 18
            elif kairalvl == 8 and nicolelvl == 11:
                text "Talk to Kaira in her room in the afternoon." justify True size 18
            elif kairalvl == 9 and nicolelvl == 11:
                text "Talk to Nicole about the trip, or finish Amanda's content if not finished already." justify True size 18
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
