screen phone_icon():
    zorder 6
    if nicolelvl >= 6:
        imagebutton:
            focus_mask True
            idle "phone/icon.png"
            hover "phone/iconhover.png"
            action [Show("btc"), Play("voice", "sounds/boom.mp3"), PauseAudio("music", True)] xalign 0.5
