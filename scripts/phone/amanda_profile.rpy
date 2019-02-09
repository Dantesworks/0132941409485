screen amanda_profile():
    imagebutton: ## Close
        idle "phone/close.png"
        action Hide("amanda_profile")
    imagebutton: ## Profile
        focus_mask True
        idle "phone/profile/amanda_profile.png"
        action NullAction()
    imagebutton: ## Home
        focus_mask True
        idle "phone/home.png"
        action [Show("homescreen"), Hide("amanda_profile")]
    viewport xalign 0.5 yanchor 0 ypos 480 xsize 350 ysize 420 draggable True mousewheel True arrowkeys True:
        vbox xsize 350:
            text "Amanda was always a caring and kind woman. Her young appearance belies her middle years, such that she \
finds work in the modelling industry. Despite being widowed for many years, she has continued to be content with being single. The story may have ended there, \
until she saw [p] again. Having a man in the house stirred some long forgotten emotions within Amanda. One night, she witnessed [p] and Nicole \
engage in intimacy, and her own reaction surprised her. Despite it being depraved, Amanda found herself lusting after [p]'s phallus, but quickly \
regained control of the situation. Regardless, living with [p] is a recipe for an interesting story, and there is no telling elif one time her \
urges will triumph." justify True size 18
    viewport xalign 0.5 yanchor 0 ypos 410 xsize 350 ysize 40 draggable True mousewheel True arrowkeys True:
        vbox xsize 350:
            if amandalvl == 1 and amandakitchenlvl == 1:
                text "Go talk to [mr] in her room in the morning." justify True size 18
            elif amandalvl == 2 and amandakitchenlvl == 1:
                text "Go talk to [mr] in the kitchen in the evening." justify True size 18
            elif amandalvl == 2 and amandakitchenlvl == 2:
                text "Go talk to [mr] in her room in the morning." justify True size 18
            elif amandalvl == 3 and amandakitchenlvl == 2:
                text "Go talk to [mr] in the kitchen in the evening." justify True size 18
            elif amandalvl == 3 and amandakitchenlvl == 3:
                text "Go talk to [mr] in her room in the morning." justify True size 18
            elif amandalvl == 4 and amandakitchenlvl == 3:
                text "Go talk to [mr] in the kitchen in the evening." justify True size 18
            elif amandalvl == 4 and amandakitchenlvl == 4:
                text "Go talk to [mr] in her room in the morning." justify True size 18
            elif amandalvl == 5 and amandakitchenlvl == 4:
                text "Go talk to [mr] in the kitchen in the evening." justify True size 18
            elif amandalvl == 5 and amandakitchenlvl == 5:
                text "Purchase a DSLR Camera Body and kit lens from the online shop on the computer, then talk to [mr] in her room in the morning." justify True size 18
            elif amandalvl == 6 and amandakitchenlvl == 5:
                text "Go talk to [mr] in the kitchen in the evening." justify True size 18
            elif amandalvl == 6 and amandakitchenlvl == 6:
                text "Purchase the photography guide then talk to [mr] in her room in the morning." justify True size 18
            elif amandalvl == 7 and amandakitchenlvl == 6:
                text "Purchase some outfits, then talk to [mr] in the kitchen in the evening." justify True size 18
            elif amandalvl == 7 and amandakitchenlvl == 7:
                text "Go talk to [mr] in her room in the morning." justify True size 18
            elif amandalvl == 8 and amandakitchenlvl == 7:
                text "Purchase some outfits, then talk to [mr] in the kitchen in the evening." justify True size 18
            elif amandalvl == 8 and amandakitchenlvl == 8:
                text "Get a phone from Nicole, then talk to [mr] in her room in the morning." justify True size 18
            elif amandalvl == 9 and amandakitchenlvl == 8:
                text "Purchase some outfits, then talk to [mr] in the kitchen in the evening." justify True size 18
            elif amandalvl == 9 and amandakitchenlvl == 9:
                text "Go talk to [mr] in her room in the morning." justify True size 18
            elif amandalvl == 10 and amandakitchenlvl == 9:
                text "Go talk to [mr] in the kitchen in the evening." justify True size 18
            elif amandalvl == 10 and amandakitchenlvl == 10:
                text "Go talk to [mr] in her room in the morning." justify True size 18
            elif amandalvl == 11 and amandakitchenlvl == 11:
                text "Go talk to [mr] in the kitchen in the evening." justify True size 18
            else:
                text "Content complete for this version! Vote for this character on Patreon to see more." justify True size 18
