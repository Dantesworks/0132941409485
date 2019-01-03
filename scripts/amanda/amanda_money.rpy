label amanda_money:
    if pocketmoney:
        scene a-3
        m "I'm only working a part time job!"
        scene a-2
        m "I can't spare too much, but how about $15?"
        scene a-8
        m "Maybe if the job paid better..."
        scene a-1
        p "Thanks!"
        "I wonder if there's a way to help [mr] out."
        $ pocketmoney = False
        $ cash += 15
        jump amanda_room
    scene a-4 with dissolve
    m "You've already asked for money today!"
    scene a-5
    m "I wish I had more to give. You should help out sometime and earn your keep!"
    p "Haha, I'll look for a way."
    jump amanda_room
