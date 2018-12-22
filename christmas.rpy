label christmas:
    scene black
    with fade
    $ renpy.pause ()
    scene c-1
    with fade
    "Ah, it's that time of the year again."
    "But... I don't think I've been terribly good this year unfortunately."
    "It's a beautiful season, but I deserve none of it."
    n "Hey [p!]!"
    scene c-3
    with dissolve
    play music "sounds/beach.mp3"
    n "You look like you need some cheering up!"
    p "So you're Miss Santa Claus."
    scene c-4
    p "How ironic, you're the naughtiest girl I know."
    scene c-2
    n "I'm special."
    n "I give the goods to the naughty kids."
    scene c-5
    n "And you've been a very naughty boy this year [p]."
    p "Haha, what am I getting this year?"
    p "And don't tell me it's you, that's far too cheesy."
    scene c-6
    n "Hmm..."
    scene c-4
    n "Close [p], but not quite."
    scene c-3
    n "It's something you've wanted all along, take a guess!"
    menu christmasask:
        "Uhh, bitcoin back at $20,000?":
             jump christmasdone

        "The bogs in a jail cell?":
            jump christmasdone

        "High speed internet?":
            jump christmasdone

label christmasdone:
    scene c-7
    n "No silly!"
    scene c-3
    n "I've wrapped it up all ready for you, it's waiting in the sleigh!"
    scene c-9
    with dissolve
    play music "sounds/automata.mp3" fadeout 1
    $ renpy.pause ()
    p "...Kaira?"
    scene c-9
    s "It's me!"
    scene c-8
    s "I'm the one you wanted all along!"
    p "Haha, skimpy as always."
    scene c-10
    with dissolve
    s "Just for you hehehe."
    scene c-11
    with dissolve
    s "You don't look right, [p]! What's wrong?"
    p "The snow, Kaira."
    scene c-12
    s "What about it?"
    p "It doesn't feel cold."
    scene c-13
    s "Of course it doesn't, I've gone ahead and made you all hot!"
    scene c-14
    with dissolve
    play music "sounds/cyberpunk.mp3" fadeout 1
    p "No, that's not it."
    p "..."
    p "This isn't... real, is it?"
    p "Jesus, this is just another fucking dream."
    scene c-15
    s "Why do you keep pushing me away, [p]?"
    scene c-18
    s "I know I'm your [sr], but I really, really like you."
    scene c-19
    s "We shouldn't ever let anything come between true love."
    scene c-16
    p "You've said that before Kaira."
    p "..."
    scene c-17
    p "I've had this nightmare before!"
    scene c-20
    s "It doesn't have to be a nightmare [p]."
    p "..."
    p "Soon, I'll wake up, and this will all be over."
    scene c-21
    s "Will you just leave me?"
    s "What we have here is still important!"
    "I can't just walk away..."
    scene c-20
    p "I'm tired Kaira..."
    p "I don't know what to think. I came home to gain my bearings back after losing my way."
    p "But now, I have more questions than ever, and I'm less sure of myself."
    scene c-22
    s "Let me help, [p]."
    p "You should leave me Kaira. I'm sinking into this hole of... depravity."
    scene c-23
    play music "sounds/wistful.mp3" fadeout 1
    s "Then let me sink with you!"
    p "I-"
    "..."
    scene c-24
    s "It's going to be okay. I know it's hard, and I understand."
    scene c-25
    s "It's not easy, I know, but you're going to be okay, do you hear me!"
    scene c-26
    s "You're going a good job [p]."
    p "... Thanks Kaira, that... means something to me."
    scene c-29
    s "I just want you to accept yourself."
    scene c-27
    s "I'm really sorry I've caused you so much pain!"
    scene c-28
    s "I shouldn't have come to see you, I don't want you to feel like this."
    scene c-29
    p "Kaira, I-"
    scene c-30
    p "...Don't leave me."
    scene c-31
    s "I'm happy you said that [p], I don't want to leave you either."
    s "We can always see each other again, [p]."
    p "How?"
    scene c-32
    s "I'm your [sr], dummy! Just come talk to me in the morning!"
    scene black
    with fade
    "..."
    jump base
