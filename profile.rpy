label profile:
    call screen profile
    screen profile():
        add "wallpaper"
        grid 2 3:
            transpose True
            xfill True
            xpos 217
            ypos 80
            imagebutton: ## Kaira
                focus_mask True
                idle "characters/kaira.png"
                hover "characters/kaira_h.png"
                action Jump("kaira")
            imagebutton: ## Amanda
                focus_mask True
                idle "characters/amanda.png"
                hover "characters/amanda_h.png"
                action Jump("amanda")
            imagebutton: ## Nicole
                focus_mask True
                idle "characters/nicole.png"
                hover "characters/nicole_h.png"
                action Jump("nicole")
            imagebutton: ## Caroline
                focus_mask True
                idle "characters/caroline.png"
                hover "characters/caroline_hover.png"
                action Jump("nicole_bj")
            imagebutton: ## Camille
                focus_mask True
                idle "characters/camille.png"
                hover "characters/camille_hover.png"
                action Jump("nicole_bj")
            null
        imagebutton: ## back
            focus_mask True
            idle "back.png"
            hover "back_hover.png"
            action Jump("computer")
