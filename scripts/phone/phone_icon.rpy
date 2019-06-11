screen phone_icon():
    zorder 6
    if nicolelvl >= 8:
        imagebutton:
            focus_mask True
            idle "phone/icon.png"
            hover "phone/iconhover.png"
            action Show("homescreen")
    else:
        imagebutton:
            focus_mask True
            idle "guide_i.png"
            hover "guide_h.png"
            action Show("guide")

screen guide(): ## How to get Nicole Phone
    viewport xalign 0.5 yanchor 0 ypos 410 xsize 350 draggable True mousewheel True arrowkeys True:
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
            else:
                text "Content complete for this version! Vote for this character on Patreon to see more." justify True size 18
    imagebutton: ## Close
        idle "phone/close.png"
        action Hide("guide")
