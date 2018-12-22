label computer:
    hide screen map_icon
    call screen computer
    screen computer():
        add "wallpaper.png"
        imagebutton:
            focus_mask True
            idle "back.png"
            hover "back_hover.png"
            action Jump("player_room")
        imagebutton:
            focus_mask True
            idle "logo_patron.png"
            hover "logo_patron_hover.png"
            action OpenURL("https://www.patreon.com/danteworks")
        imagebutton:
            focus_mask True
            idle "logo_discord.png"
            hover "logo_discord_hover.png"
            action OpenURL("https://discord.gg/mVjjbDG")
        imagebutton: ## Replay
            focus_mask True
            idle "logo_treasured.png"
            hover "logo_treasured_hover.png"
            action Jump("nicole_bj")
