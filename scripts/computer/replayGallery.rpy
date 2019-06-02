label gallery1:
    call screen gallery1
    screen gallery1:
        add "wallpaper"
        grid 3 3:
            align (0.5, 0.3)
            spacing 80
            imagebutton: ## Replay
                focus_mask True
                idle "gallery_buttons/1.png"
                hover "gallery_buttons/1_hover.png"
                action Jump("nicole_bj")
            imagebutton: ## Replay
                focus_mask True
                idle "gallery_buttons/2.png"
                hover "gallery_buttons/2_hover.png"
                action Jump("cumswap")
            imagebutton: ## Replay
                focus_mask True
                idle "gallery_buttons/3.png"
                hover "gallery_buttons/3_hover.png"
                action Jump("nicole_ride")
            if nicolelvl >= 5:
                imagebutton:
                    focus_mask True
                    idle "gallery_buttons/4.png"
                    hover "gallery_buttons/4_hover.png"
                    action Jump("nicole_event1")
            else:
                null
            if nicolelvl >= 6:
                imagebutton:
                    focus_mask True
                    idle "gallery_buttons/5.png"
                    hover "gallery_buttons/5_hover.png"
                    action Jump("nicole_event2")
            else:
                null
            if widowlvl > 1:
                imagebutton:
                    focus_mask True
                    idle "gallery_buttons/6.png"
                    hover "gallery_buttons/6_hover.png"
                    action Jump("widow_1")
            else:
                null
            if kairalvl > 5:
                imagebutton:
                    focus_mask True
                    idle "gallery_buttons/7.png"
                    hover "gallery_buttons/7_hover.png"
                    action Jump("k_1")
            else:
                null
            if camillelvl > 3:
                imagebutton:
                    focus_mask True
                    idle "gallery_buttons/8.png"
                    hover "gallery_buttons/8_hover.png"
                    action Jump("cam_bj")
            else:
                null
            if camillelvl > 5:
                imagebutton:
                    focus_mask True
                    idle "gallery_buttons/9.png"
                    hover "gallery_buttons/9_hover.png"
                    action Jump("cam_anal_doggy")
            else:
                null
        imagebutton: ## back
            focus_mask True
            idle "back.png"
            hover "back_hover.png"
            action Jump("computer")
