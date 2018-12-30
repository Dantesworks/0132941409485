label gallery1:
    call screen gallery1
    screen gallery1:
        add "wallpaper"
        grid 3 3:
            # xfill True
            # yfill True
            # xmaximum 1600
            # ymaximum 900
            anchor (0.5, 0.5)
            align (0.5, 0.5)
            spacing 100
            #xcenter
            # xpos 217
            # ypos 80
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
                action Jump ("nicole_ride")
            null
            null
            null
            null
            null
            null
        imagebutton: ## back
            focus_mask True
            idle "back.png"
            hover "back_hover.png"
            action Jump("computer")
