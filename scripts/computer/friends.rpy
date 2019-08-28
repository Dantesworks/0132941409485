label friends:
    call screen friends
    screen friends():
        add "wallpaper.png"
        imagebutton: ## back
            focus_mask True
            idle "back.png"
            hover "back_hover.png"
            action Jump("computer")
        grid 3 3:
            align (0.5, 0.3)
            spacing 80
            imagebutton:
                focus_mask True
                idle "gallery_buttons/friends/glacerose.png"
                hover "gallery_buttons/friends/glacerose_hover.png"
                action OpenURL("https://www.patreon.com/glacerose")
            imagebutton:
                focus_mask True
                idle "gallery_buttons/friends/zanith.png"
                hover "gallery_buttons/friends/zanith_hover.png"
                action OpenURL("https://www.patreon.com/zanith")
            imagebutton:
                focus_mask True
                idle "gallery_buttons/friends/sir.png"
                hover "gallery_buttons/friends/sir_hover.png"
                action OpenURL("https://www.patreon.com/Eternity_Games")
            null
            null
            null
            null
            null
            null
