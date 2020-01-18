screen homescreen():
    zorder 7
    imagebutton: ## Close
        idle "phone/close.png"
        action Hide("homescreen")
    imagebutton:
        focus_mask True
        idle "phone/homescreen.png"
        action NullAction()
    imagebutton: ## Close
        focus_mask True
        idle "phone/home.png"
        action Hide("homescreen")
    grid 4 5:
        align (0.5, 0.5)
        xspacing 15
        yspacing 50
        imagebutton:
            focus_mask True
            idle "phone/icon/rb_icon.png"
            action OpenURL("https://www.redbubble.com/people/danteworks/works/40125245-caroline-prestige?asc=u")
        imagebutton:
            focus_mask True
            idle "phone/icon/amanda_icon.png"
            action [Hide("homescreen"), Show("amanda_profile")]
        imagebutton:
            focus_mask True
            idle "phone/icon/kaira_icon.png"
            action [Hide("homescreen"), Show("kaira_profile")]
        imagebutton:
            focus_mask True
            idle "phone/icon/nicole_icon.png"
            action [Hide("homescreen"), Show("nicole_profile")]
        imagebutton:
            focus_mask True
            idle "phone/icon/caroline_icon.png"
            action [Hide("homescreen"), Show("caroline_profile")]
        imagebutton:
            focus_mask True
            idle "phone/icon/camille_icon.png"
            action [Hide("homescreen"), Show("camille_profile")]
        imagebutton:
            focus_mask True
            idle "phone/icon/veronica_icon.png"
            action [Hide("homescreen"), Show("veronica_profile")]
        imagebutton:
            focus_mask True
            idle "phone/icon/olivia_icon.png"
            action [Hide("homescreen"), Show("olivia_profile")]
        imagebutton:
            focus_mask True
            idle "phone/icon/angelina_icon.png"
            action [Hide("homescreen"), Show("angelina_profile")]
        imagebutton:
            focus_mask True
            idle "phone/icon/BCC_icon.png"
            action [Hide("homescreen"), Show("btc"), Play("voice", "sounds/boom.mp3"), PauseAudio("music", True)]
        null
        null
        null
        null
        null
        null
        null
        null
        null
        null
