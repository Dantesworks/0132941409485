label kaira:
    call screen kaira
    screen kaira():
        add "wallpaper"
        add "textbox.png"
        add "characters/kaira.png" xalign 0.5 ypos 50
        vbox xsize 1800 xalign 0.5 yalign 0.4:
            text "When [p] met Kaira again, he discovered that she was no longer \
the young girl she had once been. She had grown in many ways, and she knew this too. She hints that she is still not fully content, however and [p] has noted that there have been a few times where she expressed \
envy when confronted by other woman with larger breasts than her. Nevertheless, she is learning to use guile and charm to manipulate \
others to satisfy her desires, and who better to practise on than [p]? With the influence of Nicole, she will be a \
force to be reckoned with indeed. She put these skills to practise on the second day, wearing alluring outfits to catch the eye of \
[p]. The day would culminate in an intimate experience between all parties involved, yet Kaira will deny remembering any of it. \
[p] wonders if this is true, as he cannot shake the feeling that this experience will haunt him in the future." justify True size 28
        if kairalvl > 1:
            vbox xsize 1800 xalign 0.5 yalign 0.6:
                text "A conversation with Kaira reveals that she had been having 'perverted' dreams. \
Are these dreams similar to what [p] is experiencing?" justify True size 28
        imagebutton: ## back
            focus_mask True
            idle "back.png"
            hover "back_hover.png"
            action Jump("profile")
label nicole:
    call screen nicole
    screen nicole():
        add "wallpaper"
        add "textbox.png"
        add "characters/nicole.png" xalign 0.5 ypos 50
        vbox xsize 1800 xalign 0.5 yalign 0.36:
            text "[p] first met Nicole through Kaira. To say she made an impression was an understatment. \
If her looks didn't betray her already, Nicole is a seductress. Her perfecly sculpted body, Kaira reveals, \
may not have been entirely scuplted by nature, but perhaps in part by a surgical blade. Recognising the depravity within [p], \
Nicole doesn't hesitate to goad him into actions he might not usually perform, including intimate experiences with his own [sr]. \
The only certainty about Nicole is her confidence in her own appearance, and the willingness to augment herself to further sex appeal. \
Other than that, her motivations regarding [p] and [sr] are an enigma, and is something that [p] has resolved himself to elucidate." justify True size 28
        imagebutton: ## back
            focus_mask True
            idle "back.png"
            hover "back_hover.png"
            action Jump("profile")
label amanda:
    call screen amanda
    screen amanda():
        add "wallpaper"
        add "textbox.png"
        add "characters/amanda.png" xalign 0.5 ypos 50
        vbox xsize 1800 xalign 0.5 yalign 0.365:
            text "Amanda was always a caring and kind woman. Her young appearance belies her middle years, such that she \
finds work in the modelling industry. Despite being widowed for many years, she has continued to be content with being single. The story may have ended there, \
until she saw [p] again. Having a man in the house stirred some long forgotten emotions within Amanda. One night, she witnessed [p] and Nicole \
engage in intimacy, and her own reaction surprised her. Despite it being depraved, Amanda found herself lusting after [p]'s phallus, but quickly \
regained control of the situation. Regardless, living with [p] is a recipe for an interesting story, and there is no telling if one time her \
urges will triumph." justify True size 28
        imagebutton: ## back
            focus_mask True
            idle "back.png"
            hover "back_hover.png"
            action Jump("profile")
label camille:
    call screen camille
    screen camille():
        add "wallpaper"
        add "textbox.png"
        add "characters/camille.png" xalign 0.5 ypos 50
        if camillelvl == 1:
            vbox xsize 1800 xalign 0.5 yalign 0.35:
                text "[p] first met Camille by accident and his first conduct with her was one of trickery, as he lied about the location \
of the man she was pursuing. This may be fitting however, as there is an aura of a certain mystery surrounding Camille, and [p] cannot \
put his finger on it. Something is not as it seems. Perhaps these impressions are in part due to her shy and demure nature, and of her few words. The one thing clear is \
that Camille shared some history with Vincent. Perhaps interrogating Vincent will yield some clues on this mysterious figure." justify True size 28
        imagebutton: ## back
            focus_mask True
            idle "back.png"
            hover "back_hover.png"
            action Jump("profile")

label caroline:
    call screen caroline
    screen caroline():
        add "wallpaper"
        add "textbox.png"
        add "characters/caroline.png" xalign 0.5 ypos 50
        vbox xsize 1800 xalign 0.5 yalign 0.37:
            text "Caroline is a medical student who is independent and capable. Despite her rigorous study, she works a part time job \
at the local bar. If approached flirtatiously during work, Caroline would reject advances, demonstrating professionalism and responsibility. \
She appears to be quite optimisic about the idea of love, and tells [p] that no matter how society may view a relationship, it should not matter if \
the two people are truly in love with one another. While polite and reserved, Caroline attracts a level of respect from most people, and [p] \
unwittingly gains more and more respect for her at every interaction." justify True size 28
        if carolinelvl > 1:
            vbox xsize 1800 xalign 0.5 yalign 0.52:
                text "[p] met Caroline at the cafe one day, and discovered that she is a regular there." justify True size 28
        imagebutton: ## back
            focus_mask True
            idle "back.png"
            hover "back_hover.png"
            action Jump("profile")

label vincent:
    call screen vincent
    screen vincent():
        add "wallpaper"
        add "textbox.png"
        add "characters/vincent.png" xalign 0.5 ypos 50
        vbox xsize 1800 xalign 0.5 yalign 0.345:
            text "Vincent was first inadvertently introduced to [p] by Camille, but [p] had met him prior to that. \
Vincent had spoken to [p] at the start of his story, when he saw that [p] was distraught. He was successful in \
calming [p] down, but left before [p] could learn his name then. Now, Vincent has moved to this town to work as a photographer. \
This is just as well, because [p] plans to ask Vincent about his prior history with Camille, and what the mystery is exactly." justify True size 28
        imagebutton: ## back
            focus_mask True
            idle "back.png"
            hover "back_hover.png"
            action Jump("profile")
