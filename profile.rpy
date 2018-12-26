label profile:
    call screen profile
    screen profile():
        add "wallpaper"
        grid 2 3:
            transpose True
            xfill True
            xpos 280
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
                action Jump("caroline")
            imagebutton: ## Camille
                focus_mask True
                idle "characters/camille.png"
                hover "characters/camille_hover.png"
                action Jump("camille")
            imagebutton: ## Vincent
                focus_mask True
                idle "characters/vincent.png"
                hover "characters/vincent_h.png"
                action Jump("vincent")
        imagebutton: ## back
            focus_mask True
            idle "back.png"
            hover "back_hover.png"
            action Jump("computer")
