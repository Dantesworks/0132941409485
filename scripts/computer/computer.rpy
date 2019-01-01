label computer:
    if renpy.music.get_playing() != "sounds/dreams.mp3":
        play music "sounds/dreams.mp3"
    hide screen map_icon
    hide screen daytime
    call screen computer
    default bgswap = True
screen computer():
    if bgswap:
        add "wallpaper.png"
    else:
        add "wallpaper2.png"
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
    imagebutton: ## The Grand Museum of Patrons
        focus_mask True
        idle "museum.png"
        hover "museum_hover.png"
        hovered [SetVariable("bgswap", False), With(dissolve)]
        unhovered [SetVariable("bgswap", True), With(dissolve)]
        action [SetVariable("bgswap", True), Jump("museum")]
    imagebutton: ## Memories
        focus_mask True
        idle "logo_treasured.png"
        hover "logo_treasured_hover.png"
        action Jump("gallery1")
    imagebutton: ## Characters
        focus_mask True
        idle "logo_characters.png"
        hover "logo_characters_hover.png"
        action Jump("profile")
    imagebutton: ## back
        focus_mask True
        idle "powerback.png"
        hover "powerback_hover.png"
        action Jump("player_room")
