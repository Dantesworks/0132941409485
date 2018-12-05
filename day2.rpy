label day2:

## Nightmare Chapter 3

    scene black
    with fade
    "*Hours later...*"
    play music "sounds/cyberpunk.mp3" fadeout 1
    scene 3-1
    with fade
    "Urghh...."
    "Jesus it's still dark? Why did I wake up so early?"
    "..."
    "Hang on... did I just hear something?"
    scene 3-2
    "*click*"
    scene 3-3
    $ renpy.pause ()
    scene 3-4:
        pos (0.0, -2.43)
        linear 6 pos (0.0, 0.0)
    $ renpy.pause(6.0,hard=True)
    $ renpy.pause ()
    scene 3-5
    p "What the-"
    p "Kaira? What are you doing here?!"
    p "And why are you not wearing clothes?!"
    scene 3-6
    s "I told you, [p], my boobs are getting too big for my clothes."
    scene 3-7
    p "What do you- what?!"
    p "You *need* to put something on Kaira!"
    scene 3-8
    s "What I *need*, [p], is you."
    scene 3-9
    p "You can't do that! You're not my girlfriend, you're my-"
    scene 3-10
    s "[sr]? Why should we let that come between true love?"
    scene 3-11
    s "I *need* you, [p]. I've grown a lot since you left."
    s "Let me show it to you, [p], please."
    scene 3-12
    s "I need you."
## Dream over

    scene black
    with fade
    stop music fadeout 1
    scene 3-13
    with fade
    "Gasp...pant"
    scene 3-14
    p "Just... a dream..."
    p "What the hell was that about?"
    scene 3-15

    play music "sounds/heart.mp3"

    s "What the hell was what about [p]?"
    scene 3-16
    p "AHHHHHHHH"
    scene 3-17
    s "I've been yelling at you for 5 whole minutes for you to get up!"
    scene 3-18
    p "You were... yelling at me?"
    s "YES dummy! I was yelling that I *need* you to wake up!"
    scene 3-19
    s "..."
    scene 3-20
    s "Sorry, I understand that you must be jetlagged and all, but I really don't want to keep Nicole waiting."
    scene 3-21
    p "Oh fuck, we're going shopping! That's right."
    s "Yes, you promised last night."
    p "Alright, alright... I'll get ready. Where's [mr]?"
    scene 3-22
    s "We can chitchat later. You get ready first. Meet me in the kitchen."
    p "... alright, alright..."
    scene 3-23
    "Wow she can really take the lead when she wants to..."
    "I should probably get up, don't want to keep Nicole waiting."
    "After all, this might actually go somewhere!"
    "But of course, it's always good to keep expectations low.. hehehe."

# In Kitchen

    play music "sounds/automata.mp3" fadeout 1
    scene 3-24
    with dissolve
    p "Sup Kaira."
    scene 3-25
    s "Good morning, [p]. Did you sleep well last night?"
    p "... like a lamb, hahaha."
    scene 3-26
    s "It didn't sound like that."
    "Shit, don't tell me I was sleep talking..."
    p "Oh it was pretty good until you woke me up! Did I say anything in my sleep?"
    scene 3-27
    s "Yeah, you did, but I couldn't make it out."
    "Phew..."
    s "You started mumbling when I tried to wake you, like you were in a nightmare."
    scene 3-28
    s "I didn't give you a nightmare did I? I feel so bad. I'm so sorry!"
    p "Aww, listen, I don't even remember what happened!"
    scene 3-29
    p "Kaira, I'm super thankful you woke up me alright? I would hate to miss the shopping trip and not spend time with you."
    scene 3-30
    s "You don't know how happy hearing that makes me [p]."
    p "Hey, it's the truth."
    p "So, what's the agenda here?"
    s "Oh, I'm just packing some snacks."
    p "Good idea, I should probably do that too."
    scene 3-31
    s "I packed yours too, [p]. That's just the thoughtful kind of [sr] I am!"
    scene 3-32
    s "But you'll have to carry the bag, deal?"
    p "Hahaha deal."
    scene 3-33
    s "Okay I'm ready! Let's go or we'll be late."
    menu ask2:

        "After you!":
            jump hugdone

        "Hang on, there's something I want to do...":
            jump hug

    label hug:
        scene 3-34
        pause 0.5
        scene 3-35
        pause 0.5
        scene 3-36
        pause 0.5
        scene 3-37
        p "I really appreciate this, you know that? I'm going through a rough patch right now, and I wanna say I'm really grateful you're sharing your time with me."
        scene 3-38
        s "Oh! This- this kind of stuff goes both ways... Don't think anything of it [p]!"
        s "You know, spending time with you also makes me really happy."
        scene 3-39
        s "..."
        scene 3-40
        s "heheh, you smell nice."
        p "..haha... that's slightly creepy."
        jump hugdone

    label hugdone:

## Shopping Chapter 4
    scene black
    with dissolve
    "*Half an hour later...*"
    scene 4-1
    with dissolve
    p "...dammit where are you taking me Kaira?"
    s "We're going shopping remember!"
    p "The shops are right here, you're running past them all!"
    s "No, no, no, we're not just going to any shop. We're going to me and Nicole's favourite."
    s "Come, come, hurry up! Hurry up!"
    p "There's no need to go so fast! Hey!"
    s "It's not nice to keep people waiting, [p]. Nicole is waiting for us there already."
    s "Anyway, don't you think you'll have better chances of hitting on her if you get there before and impress her?"
    "Damn, she's right..!"
    p "Hahah, you know how to say the right things!"
    "..."

    scene 4-2
    s "Ta da! We're here!"
    s "I love this place, they've got tons of clothes that fit a ton of moods."
    scene 4-3
    s "Hmm let's see... do I feel sexy today or am I more for cute?"
    scene 4-4
    "This place is pretty neat. I can't say I shop for clothing a lot, but this place looks a notch above the rest. You can tell by how the changing rooms are so large."
    scene 4-3
    s "Uh [p]?"
    p "Sorry?"
    s "I said, am I sexy, or am I cute?"
    scene 4-5
    menu sexy:
        "I think I'll go with cute.":
            jump cute
        "You're the sexiest girl I've ever met, Kaira.":
            jump sexy1

    label cute:
        scene 4-6
        s "Hmm, I'm not sure what to think."
        s "What makes you say cute?"
        p "Well, Kaira, you're my [sr]."
        scene 4-7
        s "Oh, but why should we let that come between true love?"
        scene 4-8
        with fade
        "..!"
        "This is some deja vu."
        p "Hang on, Kaira, have you ever said that before?"
        scene 4-9
        s "Say what before?"
        p "The part about coming between true love."
        scene 4-10
        s "Did I even say that? I don't remember..."
        p "..."
        ##Where's Nicole
        scene 4-5
        p "Anyway, didn't you say Nicole would meet us here?"
        scene 4-11
        s "That's what she said. Can you see her around?"
        p "Kaira baby, I don't even know what she looks like. Come on."
        scene 4-12
        s "Oh right, sorry, ahahaah!"
        scene 4-13
        s "Hmm, I don't think she's here yet. Do you mind if we just wait around a bit? I'm sure she'll be here any minute now."
        p "Not at all, the day's all yours."
        ##
        s "..."
        scene 4-14
        s "Hey [p]."
        jump sexydone


    label sexy1:
        scene 4-12
        s "Fufu.. I didn't think you'd actually say it! Really?"
        p "What do you know, I'm an honest guy. It's the truth."
        s "I'm glad you said that."
        scene 4-24
        s "I mean, I'm glad about the honest part, not the.. well.. I guess being sexy is also nice, right? Even though I'm your [sr]."
        p "Why should we let that come between true love?"
        scene 4-14
        s "Aahahhaha jeez [p]."
        ##Where's Nicole
        scene 4-5
        p "Anyway, didn't you say Nicole would meet us here?"
        scene 4-11
        s "That's what she said. Can you see her around?"
        p "Kaira baby, I don't even know what she looks like. Come on."
        scene 4-12
        s "Oh right, sorry, ahahaah!"
        scene 4-13
        s "Hmm, I don't think she's here yet. Do you mind if we just wait around a bit? I'm sure she'll be here any minute now."
        p "Not at all, the day's all yours."
        ##
        "..."
        scene 4-14
        s "Umm, [p]?"
        p "What's up?"
        scene 4-25
        s "Uhhh... when you said I was sexy, what did you mean by that?"
        scene 4-5
        p "...oh, don't take me too seriously aha, you know I was just going with it and-"
        scene 4-26
        s "So am I not sexy?"
        scene 4-27
        p "No wait, I mean, of course you are. You don't have to worry-"
        scene 4-28
        s "Which part of me do you find sexy?"
        scene 4-29
        "... Am I really doing this?"
        p "..."
        scene 4-8
        p "It's... like, a general thing, you're generally sexy.. as a whole, you know."
        scene 4-30
        s "Fufufu [p], I thought you said you were honest."
        scene 4-31
        p "Look, you're my [sr]."
        s "And didn't you come up with how it shouldn't come between true love?"
        p "I didn't come up with it, I got it from.. I got it from-"
        scene 4-29
        "From you? Or was it from me? Fuck, what is going on."
        jump sexydone

    label sexydone:
        scene 4-15
        s "Surely you can find *something* about me that's sexy."
        p "..."
        scene 4-16
        p "Fine."
        p "You've got sexy tits Kaira."
        scene 4-17
        s "There you go! My boobies are 100 percent real too!"
        scene 4-18
        s "But I've still got long way to go to catch up with [mr]."
        scene 4-13
        p "You know, that's not something you necessarily have to aim for."
        p "..."
        p "I reckon they're fine the way they are, hahaha."
        scene 4-19
        p "Hey Kaira. Going forward, I think-"
        scene 4-20
        s "Oh Nicole! I didn't see you!"
        scene 4-21
        s "How long have you been standing there?"
        scene 4-22
        pause 0.5

        play music "sounds/beach.mp3"
        scene 4-23:
            pos (0.0, -2.96)
            linear 6 pos (0.0, 0.0)
        $ renpy.pause(6.0,hard=True)
        $ renpy.pause ()
    scene 4-27
    "Shit! I hope she didn't hear our conversation!"
    scene 4-32
    n "Hello Kaira, and hello to you [p]. It's Nicole."
    n "Kaira has told me a lot about you."
    scene 4-5
    p "Uh.. hahah.. Good things I hope?"
    "Shit! She's hot! Fuck me if she knows I think my [sr]'s sexy!"
    scene 4-33
    n "Hmm... You have nothing to worry about, [p]."
    scene 4-34
    s "You sure took your time, Nicole!"
    n "Ah, I was in a bit of a mess."
    s "I can tell! You're hair's not done up and I don't even know what you're dressed in."
    s "Good thing for you we're in a clothing shop. By the end of it we'll have you in a new hair style and a new outfit!"
    scene 4-32
    n "What about you [p]? Why don't I try whip my fashion magic and help you get a little stylish?"
    scene 4-34
    s "I think you should save it for yourself Nicole, you need it."
    scene 4-33
    n "Oh come on, you work on me, and I'll work on him. Deal?"
    p "I'm due for a wardrobe change anyway, why not."
    n "Excellent."


## Bonus

    scene bonus_1
    d "And that's all for version 0.2!"
    d "Please leave feedback to let me know how you liked Depravity."
    d "In the meantime, I found something real cool I wanted to show you."
    d "Turns out that Nicole girl's a bit of a slut and her photoshoot got leaked!"
    d "I don't know about you, but I would be very eager to see what Nicole gets up to in this next version!"


    scene b1
    $ renpy.pause ()
    scene b2
    $ renpy.pause ()
    scene b3
    $ renpy.pause ()
    scene b4
    $ renpy.pause ()
    scene b5
    $ renpy.pause ()
    scene b6
    $ renpy.pause ()
    scene b7
    $ renpy.pause ()
    scene b8
    $ renpy.pause ()
    scene b9
    $ renpy.pause ()
    scene b10
    $ renpy.pause ()
    scene b11
    $ renpy.pause ()
    scene b12
    $ renpy.pause ()
    scene b13
    $ renpy.pause ()
    scene b14
    $ renpy.pause ()
    scene b15
    $ renpy.pause ()
    scene b16
    $ renpy.pause ()

return
