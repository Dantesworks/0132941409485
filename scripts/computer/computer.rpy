label computer:
    hide screen player_room
    if renpy.music.get_playing() != "sounds/you.mp3":
        play music "sounds/you.mp3"
    call hidescreens from _call_hidescreens_6
    call screen computer
    default bgswap = True
    default from_computer = False
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
        action [SetVariable("bgswap", True), SetVariable("from_computer", True), Jump("museum")]
    imagebutton: ## Memories
        focus_mask True
        idle "logo_treasured.png"
        hover "logo_treasured_hover.png"
        action Jump("gallery1")
    imagebutton: ## Shop
        focus_mask True
        idle "logo_characters.png"
        hover "logo_characters_hover.png"
        action Jump("online_shop")
    imagebutton: ## Gallery
        focus_mask True
        idle "logo_gallery.png"
        hover "logo_gallery_hover.png"
        action Jump("cgGallery")
    imagebutton: ## Friends
        focus_mask True
        idle "logo_friends.png"
        hover "logo_friends_hover.png"
        action Jump("friends")
    imagebutton: ## back
        focus_mask True
        idle "powerback.png"
        hover "powerback_hover.png"
        action Jump("player_room")
    textbutton "Hacks" action Jump("hacks")
    # textbutton "App" action [Show("btc"), Play("voice", "sounds/boom.mp3"), PauseAudio("music", True)] xalign 0.5
