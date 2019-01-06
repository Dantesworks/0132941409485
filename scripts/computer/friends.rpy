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
                idle "gallery_buttons/friends/lykanz.png"
                hover "gallery_buttons/friends/lykanz_hover.png"
                action OpenURL("https://www.patreon.com/theinn")
            null
            null
            null
            null
            null
            null
            null
            null
