screen phone_icon():
    zorder 6
    if nicolelvl >= 8:
        imagebutton:
            focus_mask True
            idle "phone/icon.png"
            hover "phone/iconhover.png"
            action Show("homescreen")
