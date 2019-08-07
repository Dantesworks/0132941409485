label gallery1:
    call screen gallery1
    screen gallery1:
        add "wallpaper"
        vbox xalign 0.5 ypos 1000:
            text "Page 1"
        imagebutton: ## next
            focus_mask True
            idle "logo_next.png"
            hover "logo_next_hover.png"
            action Jump("gallery2")
        grid 3 3:
            align (0.5, 0.3)
            spacing 80
            imagebutton: ## Replay
                focus_mask True
                idle "gallery_buttons/r1.png"
                hover "gallery_buttons/r1.png"
                action Jump("nicole_bj")
            imagebutton: ## Replay
                focus_mask True
                idle "gallery_buttons/r2.png"
                hover "gallery_buttons/r2h.png"
                action Jump("cumswap")
            imagebutton: ## Replay
                focus_mask True
                idle "gallery_buttons/r3.png"
                hover "gallery_buttons/r3.png"
                action Jump("nicole_ride")
            if nicolelvl >= 5:
                imagebutton:
                    focus_mask True
                    idle "gallery_buttons/r4.png"
                    hover "gallery_buttons/r4h.png"
                    action Jump("nicole_event1")
            else:
                null
            if nicolelvl >= 6:
                imagebutton:
                    focus_mask True
                    idle "gallery_buttons/r5.png"
                    hover "gallery_buttons/r5h.png"
                    action Jump("nicole_event2")
            else:
                null
            if widowlvl > 1:
                imagebutton:
                    focus_mask True
                    idle "gallery_buttons/r6.png"
                    hover "gallery_buttons/r6h.png"
                    action Jump("widow_1")
            else:
                null
            if kairalvl > 5:
                imagebutton:
                    focus_mask True
                    idle "gallery_buttons/r7.png"
                    hover "gallery_buttons/r7h.png"
                    action Jump("k_1")
            else:
                null
            if camillelvl > 3:
                imagebutton:
                    focus_mask True
                    idle "gallery_buttons/r8.png"
                    hover "gallery_buttons/r8h.png"
                    action Jump("cam_bj")
            else:
                null
            if camillelvl > 5:
                imagebutton:
                    focus_mask True
                    idle "gallery_buttons/r9.png"
                    hover "gallery_buttons/r9h.png"
                    action Jump("cam_anal_doggy")
            else:
                null
        imagebutton: ## back
            focus_mask True
            idle "back.png"
            hover "back_hover.png"
            action Jump("computer")
