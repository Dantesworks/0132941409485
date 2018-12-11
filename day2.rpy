label day2:

## Nightmare Chapter 3

    scene black
    with fade
    "(A few hours later)"
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
    p "You {i}need{/i} to put something on Kaira!"
    scene 3-8
    s "What I {i}need{/i}, [p], is you."
    scene 3-9
    p "You can't do that! You're not my girlfriend, you're my-"
    scene 3-10
    s "[sr]? Why should we let that come between true love?"
    scene 3-11
    s "I {i}need{/i} you, [p]. I've grown a lot since you left."
    s "Let me show it to you, [p], please."
    scene 3-12
    s "I {i}need{/i} you."
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

    play music "sounds/heart.mp3" fadeout 1

    s "What the hell was what about [p]?"
    scene 3-16
    p "AHHHHHHHH"
    scene 3-17
    s "I've been yelling at you for 5 whole minutes for you to get up!"
    scene 3-18
    p "You were... yelling at me?"
    s "YES dummy! I was yelling that I {i}need{/i} you to wake up!"
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
    p "Haha, class act."
    "..."

    scene 4-2
    with dissolve
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
        s "There you go!"
        s "You should know, my boobies are 100 percent real too!"
        scene 4-18
        s "But I've still got long way to go to catch up with [mr]."
        scene 4-13
        p "You know, that's not something you necessarily have to aim for."
        p "..."
        p "I reckon they're fine the way they are, hahaha."
        scene 4-3
        s "You love them, don't you?"
        s "Say you love my tits."
        scene 4-11
        p "You've got big tits Kaira."
        s "For you."
        scene 4-19
        p "Hey Kaira. Going forward, I think-"
        scene 4-20
        s "Oh Nicole! I didn't see you!"

        s "How long have you been standing there?"

## Nicole entrance

        play music "sounds/beach.mp3" fadeout 1
        scene 4-21
        $ renpy.pause(0.5,hard=True)
        scene 4-22
        $ renpy.pause(0.5,hard=True)
        scene 4-23:
            pos (0.0, -2.96)
            linear 6 pos (0.0, 0.0)
        $ renpy.pause(6.0,hard=True)
        $ renpy.pause ()
    scene 4-27
    "Shit! I hope she didn't overhear our conversation!"
    scene 4-32
    n "Hello Kaira, and hello to you [p]. It's Nicole."
    n "Kaira has told me a lot about you."
    scene 4-5
    p "Uh.. hahah.. Good things I hope?"
    "Shit! She's hot! I'm so fucked if she heard what I said about Kaira!"
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
    s "I think you should focus on yourself Nicole, you need it."
    scene 4-33
    n "Oh come on, you work on me, and I'll work on him. Deal?"
    p "I'm due for a wardrobe change anyway, why not."
    n "Excellent."
## Clothes
    scene 4-35
    p "...so, who do {i}I{/i} get to work on?"
    scene 4-36
    s "Why not the both of us?"
    scene 4-37
    s "We'll try some clothes on, and you tell us which one of us wears it better."
    p "What kind of things are you going for?"
    scene 4-39
    s "Ooh all kinds- from normal to swimwear."
    scene 4-38
    n "From casual to sexy."
    p "...so pretty much everything then."
    scene 4-40
    p "Alright ladies. You do your thing. I'll just be around here."
    n "I'll keep an eye out for an oufit that you can wear as well [p]."
    p "Can't wait."

    scene black
    with dissolve
    "Now I remember why I don't go shopping much. It's so damn boring."
    "At least this time I'll get something out of it."
    "(What feels like a few hours later...)"

    scene 4-41
    with dissolve
    s "We're done! We've each picked out a few things we wanted to try."
    scene 4-42
    n "Something for {i}every{/i} occassion."
    p "What do you mean?"
    scene 4-41
    s "Well, first off, we've got the smart casual outfit, then the casual outfit, then finishing off with a swimsuit of course!"
    s "At least, those were the rules."
    scene 4-43
    s "Right, Nicole?"
    scene 4-44
    n "What about the fourth outfit?"
    scene 4-41
    s "Ah yes, we also picked an extra outfit, but they don't fit with the rules, so we can try that on after the game."
    scene 4-42
    s "So which outfit do you want to see first [p]?"
##
    $ askflag1 = False
    $ askflag2 = False
    $ askflag3 = False
    menu askoutfit:
        "Casual.":
            jump casual

        "Smart Casual.":
            jump sc

        "Swimsuit.":
            jump swimsuit

## Casual
    label casual:
        $ askflag1 = True
        $ last = "1"
        s "One moment!"
        scene 4-68
        with dissolve
        "..."
        "They always take so long to change."
        n "Almost done!"
        s "When you're ready, Nic!"
        n "..."
        n "Ready."
        scene 4-48
        with fade
        $ renpy.pause ()
        scene 4-46
        $ renpy.pause ()
        scene 4-49
        $ renpy.pause ()
        scene 4-47
        $ renpy.pause ()
        scene 4-45
        $ renpy.pause ()
        scene 4-50
        s "Wow! Look at you Nicole."
        n "I see we both decided to go with knits."
        scene 4-51
        s "I suppose it's casual, but yours is racier than I expected!"
        scene 4-52
        n "I might have dressed like trash this morning, but I can turn it on when I want to."
        scene 4-45
        s "Well, [p], who's got the better outfit?"
        menu casualchoice:
            "Hmm, I'll have to give this one to Kaira.":
                jump casualKaira

            "Nicole wins this one for me.":
                jump casualNicole
        label casualKaira:
            scene 4-51
            s "Thanks [p]!"
            scene 4-50
            s "You're gorgeous Nicole, but maybe that outfit isn't the best for a casual setting."
            scene 4-45
            if (askflag1 and askflag2 and askflag3):
                jump special
            p "Let's see the next outfit."
            jump outfitdone
        label casualNicole:
            scene 4-52
            n "I'm glad [p] can appreciate good taste."
            scene 4-51
            s "That knit does look really good on you Nicole. Shows off your figure really well."
            scene 4-45
            if (askflag1 and askflag2 and askflag3):
                jump special
            p "Let's see the next outfit."
            jump outfitdone
## smart casual
    label sc:
        $ askflag2 = True
        s "I'm so excited!"
        scene 4-68
        with dissolve
        "..."
        "Any moment now."
        n "I'm done Kaira, are you close?"
        s "Finished too!"
        scene 4-54
        with fade
        $ renpy.pause ()
        scene 4-55
        $ renpy.pause ()
        scene 4-56
        $ renpy.pause ()
        scene 4-57
        $ renpy.pause ()
        scene 4-53
        $ renpy.pause ()
        scene 4-58
        n "Fufu... you're always very proud of your tits, Kaira."
        n "You never shy away from showing those puppies off!"
        scene 4-59
        s "Coming from you Nicole?"
        s "At least I now know you can also look formal."
        scene 4-53
        n "Which outfit do you like more [p]?"
        menu scchoice:
            "Hmm, I'll have to give this one to Kaira.":
                jump scKaira

            "Nicole wins this one for me.":
                jump scNicole
        label scKaira:
            scene 4-59
            s "You just can't resist me [p]!"
            scene 4-58
            n "Using sex appeal on him? You're a dirty girl."
            scene 4-53
            if (askflag1 and askflag2 and askflag3):
                jump special
            p "I'm looking forward to the next outfit."
            jump outfitdone
        label scNicole:
            scene 4-58
            n "[p] knows that the hottest girls also know how to look reserved. don't you [p]?"
            scene 4-59
            s "Interesting choice."
            scene 4-53
            if (askflag1 and askflag2 and askflag3):
                jump special
            p "What next?"
            jump outfitdone
## Swimsuit
    label swimsuit:
        $ askflag3 = True
        n "Ah - my favourite."
        scene 4-68
        with dissolve
        "..."
        "This one shouldn't take too long."
        n "Done."
        s "Me too."
        scene 4-60
        with fade
        $ renpy.pause ()
        scene 4-61
        $ renpy.pause ()
        scene 4-62
        $ renpy.pause ()
        scene 4-63
        $ renpy.pause ()
        scene 4-64
        $ renpy.pause ()
        scene 4-65
        n "Kaira! You've gone skimpier than {i}me{/i}!"
        scene 4-67
        s "Feeling jealous?"
        scene 4-66
        s "I'm not the girl you first met!"
        menu swimsuitchoice:
            "Hmm, I'll have to give this one to Kaira.":
                jump swimsuitKaira

            "Nicole wins this one for me.":
                jump swimsuitNicole
        label swimsuitKaira:
            scene 4-66
            s "Was it my body, or was it the outfit?"
            s "Maybe it was both, hehehe!"
            scene 4-64
            if (askflag1 and askflag2 and askflag3):
                jump special
            p "Suprise me with the next one girls!"

            jump outfitdone
        label swimsuitNicole:
            scene 4-65
            n "I'm sorry Kaira, but I have the hotter body."
            scene 4-67
            s "At least my body is natural~"
            scene 4-64
            if (askflag1 and askflag2 and askflag3):
                jump special
            p "Suprise me with the next one girls!"
            jump outfitdone


    label outfitdone:

        if not(askflag1 and askflag2 and askflag3):
            jump askoutfit


label special:
    p "Amazing girls, that's all 3 outfits!"
    p "You guys both looked like super models."
    p "But you guys said something about a fourth outfit?"
    n "Oh yes."
    n "We also chose a another special outfit that we liked."
    s "There's no theme for it though, so it wasn't part of the game."
    n "Shall we?"
    s "Let's!"
    scene 4-68
    with dissolve
    "...so this time they're gonna get changed and I don't get to choose which one I like better?"
    n "Are you done yet Kaira?"
    s "Not yet, my one is quite a lot to put on."
    n "My one's dead simple."
    n "Alright, I think I'll head out first."
    scene 4-69
    with fade
    n "So, what do you think?"
    p "Like you said, it's simple, but very effective."
    n "Simple attire. Difficult to pull off."
    scene 4-70
    n "This is something I'm sure a man like yourself can appreciate."
    p "I can tell this is something you're quite used to."
    n "Used to what? Being sexy?"
    p "Very good."
    play music "sounds/alchemy.mp3" fadeout 1
    n "Fufufu... I can tell [p]."
    p "What can you tell?"
    scene 4-71
    n "On the surface, you're quite well composed, [p]. But that's just a front, whether you admit it or not."
    p "..."
    n "There's something stirring inside you."
    n "It's bursting through [p], and there's no way you're holding it back for long. Your eyes betray you."
    n "Not just by where they... land. But also behind them is an abyss that just keeps growing."
    n "I can see the hunger in your eyes when you look at our bodies."
    scene 4-72
    n "I don't mind you doing it to me, that's what I've made myself into. But you also lust after your [sr]."
    p "... hang on, that's not-"
    n "Even if you deny it, we both know the things you said to Kaira before I joined you two."
    "Oh fuck, she {i}did{/i} overhear us."
    scene 4-91
    p "What are you trying to say about me?"
    scene 4-73
    n "Kaira, are you done yet?"
    s "Yes, I'm finally done!"
    scene 4-74
    s "This outfit I chose is super interesting!"
    s "I think it's quite fancy and you can sort of choose how you want to wear it."
    scene 4-75
    n "I think you look hot as hell Kaira. That shows off your curves perfectly."
    s "Thanks Nicole!"
    scene 4-76
    s "Like I was saying, you can actually take off the leg pieces, like..."
    scene 4-77
    s "..this!"
    scene 4-75
    n "You've got a shapely ass Kaira, I'd love to bury my face into it."
    scene 4-79
    n "... and I'm sure [p] would as well."
    s "Ahahaha, you're so sweet all of a sudden!"
    scene 4-80
    s "What do you think [p]?"
    "Kaira is so hot, I can't believe I'm thinking this even though she's my [sr]. Is she doing this to me on purpose?"
    "Her juicy tits, that well formed ass..."
    "What is this feeling?!"
    "Why am I feeling this way?!!"
    s "[p]?"
    scene 4-82
    p "..."
    scene 4-84
    p "I... think it looks good Kaira..."
    scene 4-83
    s "Fufufu... speechless?"
    scene 4-85
    s "I like that suit Nicole, it's so you. Straight up oozing sex appeal."
    s "Are you trying impress [p]?"
    scene 4-86
    n "Hmmm.. I think you're onto something."
    scene 4-82
    s "You should go for him, he's a {i}great{/i} guy."
    "Christ, look at my [sr]'s ass."
    scene 4-87:
        pos (0.0, -3.34)
        linear 6 pos (0.0, 0.0)
    $ renpy.pause(6.0,hard=True)
    $ renpy.pause ()
    scene 4-88
    "These types of feelings are perfectly normal, aren't they?"
    "It's a physiological response."
    scene 4-85
    s "Anyway, Nicole, I {i}did{/i} say that we were going to give you a full makeover right?"
    scene 4-75
    n "I'm a lucky girl."
    scene 4-88
    s "So my plan is, let's get you all prettied up. I'll go find two more special outfits, one for me, and one for you."
    s "They're secret, and you have to wear it for when we go get drinks tonight."
    n "I love unplanned parties."
    scene 4-89
    s "[p], you coming?"
    p "Uh, sure."
    scene 4-79
    n "You won't regret it, we'll make {i}sure{/i} you have fun!"
    scene 4-90
    s "In the meantime, why don't you show [p] the clothes you picked out for him?"
    scene 4-75
    n "No worries."
    s "Lovely! I'll head off now!"
    scene 4-79
    n "Well cowboy, what are you waiting for?"

## Chapter 5

    scene 5-1
    n "Step on through."
    n "We're gonna get you sorted."
    scene 5-2
    "..."
    "What is she planning?"
    "Don't let your guard down [p]."
    scene 5-3
    scene 5-4
    with dissolve
    n "Now do you understand what I'm saying about you? You're burning up, [p]."
    scene 5-6
    p "You're insane. I have no idea what you're on about."
    p "Why are you trying to make stories up?"
    p "There's zero evidence to what you're saying!"
    scene 5-5
    n "You don't think anybody will notice that you're horny for your own [sr]?"
    p "What I'm doing is completely normal."
    scene 5-6
    n "Oh you depraved one! Do normal people throw away their morality so easily?"
    p "I've done nothing like that."
    scene 5-5
    n "Is that right? Then what's this here?"
    scene 5-8
    n "You're rock hard!"
    scene 5-7
    n "We both know it wasn't just me that turned you on!"
    "{i}PUSH{/i}"
    scene 5-9
    p "Uh! What are you-?"
    n "Relax, [p]. I'm doing you a favour."
    n "At this rate, you won't be able to control yourself around Kaira anymore."
    scene 5-12
    n "Don't fight it, let it happen."
    p "Get your hands away from -!"
    scene 5-13
    n "All it took was a tug for it to slide out [p]."
    n "Why lie to yourself?"
    n "You're a big guy."
    p "For you."
    scene 5-10
    "Fuck, her hands feel so good around my cock!"
    "I can't give her this power over me, but I need this so bad!"
    scene 5-11
    n "You're a good size [p], you shouldn't be so shy~"
    "Urgh...!"
    scene 5-13
    n "Do you feel my smooth hands slide around your cock?"
    n "Now imagine Kaira stroking your cock.. her lucious tits bouncing in front of your face.. her groin grinding against yours.."
    scene 3-12
    with fade
    p "FUCK!"
    scene 5-14
    p "I'm cumming!"
    n "Oh shit! It's going to go everywhere!"
    scene 5-15
    p "Arghhh!"
    n "*Gulp*"
    n "There's just so much~!"
    scene 5-16
    n "*Gulp*"
    p "That's right you fucking whore."
    n "*Gulp*"
    scene 5-17
    n "How much cum do you have?!"
    n "Were you trying to drown me?"
    scene 5-18
    s "[p]?"
    "!!"
    p "Yes?"
    scene 5-34
    s "I'm done with my two outfits!"
    s "How are you going with yours?"
    scene 5-18
    p "Yeah I'm trying it on right now, I'll just be a few more minutes!"
    scene 5-19
    n "A few minutes huh? You better get hard again quickly then."
    p "Don't you make a single noise you slut."
    n "Stop talking and get hard for me."
    scene 5-21
    n "That's a good boy~"
    scene 5-20
    p "Ergh!"
    "It's so sensitive!"
    p "Ha, you fucking slut."
    n "Mhm.. Mhmm..."
    s "Hey [p], do you know where Nicole went?"
    "Oh no!"
    scene 5-34
    s "I can't see her anywhere!"
    scene 5-16
    p "No idea babe I - argh!"
    n "Mhmm!!!"
    p "I'm not sure where she is!"
    n "*Glug*"
    p "Hey I'll talk to you when I'm done alright?"
    s "Alright!"
    "Phew...I came pretty hard again."
    scene 5-24
    p "Who's the depraved one now, you cock sucking whore?"
    scene 5-25
    n "Fufufu... I like you more when you're more carnal, when you drop your facade."
    scene 5-26
    n "I could get used to this side of you."
    p "You're responsible for this."
    n "As responsible as Kaira is for your lust towards her."
    p "It's her fault too."
    scene 5-28
    n "I never said she wasn't depraved herself."
    n "Though, not quite as sunken in to depravity as you are. Would you drag her in with you?"
    p "..."
    n "I'd love to do this again sometime, but there's something that needs attention before that..."
    scene 5-27
    n "Quick, get this outfit on, and slip out before me."
    scene black
    with dissolve
    "Quick quick quick!"
    scene 5-29
    with dissolve
    p "..."
    p "Coast is clear."
    play music "sounds/heart.mp3" fadeout 1
    scene 5-30
    n "So, Kaira, what do you think?"
    scene 5-32
    s "There you are Nicole! I was looking for you!"
    scene 5-31
    n "That's funny, I was just around here."
    s "My, my, look at you [p]!"
    s "What's this one called?"
    scene 5-29
    p "I call it, the 'Kishou Arima'."
    p "You dig it?"
    scene 5-33
    s "I like you with glasses, and that jacket look is so much better than your old, dirty shirt!"
    p "Hey!"
    s "Hahaha!"
    s "Well let's not stick around too long, we've got a party to go to!"
    n "I've got a feeling those outfits you picked are going to be outrageous."
    scene 5-35
    s "They are. Just the way you love it."

## Chapter 6
    "This place is big, but I barely know any faces here."
    "If I couldn’t go back to [mr] and Kaira, I would have no business being back at this place."
    "If I hadn’t met that guy who spoke to me back then, I wouldn’t be here either."
    "It’s a pity I never got his name. If I met him again I would definitely-"
    "!!"
    p "WTF"
    p "HEY!!"
    p "Stop!"
    p "Why are you running from me?"
    p "Got you!"
    p "It’s me, [p], remember? You were that one that spoke to me back then."
    x "Oh, [p]! I remember you!"
    x "Listen man, I wasn’t running from you, I was running from the chick behind you."
    p "Huh?"
    x "Dude, she has to be coming around now, you have to throw her off."
    p "Hang on, explain-"
    x "Go man go!"
    p "...Alright, I’ll do it. Think of it as payback."
    "Ah, there she is."
    p "Hey there, are you looking for something?"
    x  "Oh... hey."
    x "Sorry... have you seen... Vincent?"
    p "What does he look like?"
    x "...someone with...he has black hair and-"
    p "Oh yeah, I saw a man with black hair run off in that direction. If you keep going that way, you should catch up with him!"
    x "S-sorry, I mean, thankyou..."
    "..."
    p "Seemed like a nice girl. I wonder why he was running away."
    p "So, it’s Vincent right?"
    v "That’s me."
    p "She’s gone."
    v "Ahh, thank you so much."
    p "What was that about? I thought you were the virtuous type. Didn’t think you would be going around breaking girl’s hearts."
    v "Ah well, you know..."
    p "She was cute too, pity."
    v "It’s a complicated thing."
    v "Anyway, it’s good to see you again, how are you holding up?"
    p "I’m good Vincent, thanks again for talking to me that day."
    v "No worries!"
    p "But what are {i}you{/i} doing here?"
    v "For work. I’m a photographer, I move around a bit."
    p "How long are you staying for?"
    v "Quite a while this time, they set up a new studio here."
    v "Means I should probably get to know the people in this town."
    v "Do you know many people here?"
    p "Not really, it’s been too long since I last left."
    v "God, [p], has put us together."
    v "Let’s go for a drink! Catch up or something."
    v "Bar... stripbar... your choice!"
    p "You are definitely not as virtuous as I thought you were."
    v "Hey, we’re all a little depraved in our own little ways."
    p "I’d love to, but I’ve got another appointment later tonight."
    v "No dramas. Here’s my business card."
    v "It’s my photography business number, but I answer it all the time. Give me a call sometime."
    p "Sure thing."
    v "Alright man, I got to go, see you later."
    p "Laters!"
    "..."
    "The girls should almost be done. It’s probably time to head to the bar."
    "..."
## Bar scene

    "Wow, this place isn't bad at all."
    "The lighting is set up perfectly!"
    "Wait a minute... is that?"
    "It's the chick that Vincent was running away from!"
    "Poor girl, all by herself. Maybe I should go and say hi. But that might be awkward."
    "Dammit, I really need a drink though. What should I do?"
    menu talk:
        "Get a drink for both of you and talk to her.":
            jump talk

        "Get a drink for yourself and ignore her.":
            jump notalk

    label talk:
        p "Hey, I'm looking for a drink."
        c "what's on your mind?"
        p "Something creative, innovative, and interesting."
        p "Something really good."
        c "I think I have just what you need."
        c "Here, a glass of Original Dante. It's the best in the house!"
        c "Enjoy."
        p "One more thing."
        c "Yes sir?"
        p "Please pour one for the lady as well."
        c "Certainly."
        x "Hey... thankyou, but you don't..."
        p "Think nothing of it. I can tell you've had a rough day."
        x "..."
        x "Thankyou."
        jump camille

    label notalk:
        p "Hey, I'm looking for a drink."
        c "what's on your mind?"
        p "Something creative, innovative, and interesting."
        p "Something really good."
        c "I think I have just what you need."
        c "Here, a glass of Original Dante. It's the best in the house!"
        c "Enjoy."
        p "Thankyou."
        "{i}sip{/i}"
        p "You're right, this is some really good stuff."
        c "Told you!"
        p "I like this place."
        c "Yeah it's usually quite busy, but today it's a bit more quiet."
        p "It's a good thing right? Gives us more time to chat."
        c "Aha."
        c "So, are you by yourself? Or..."
        p "I'm meeting up with a my [sr] and her friend. They should be arriving pretty soon."
        p "...but in the meantime, what about you?"
        c "What {i}about{/i} me?"
        p "What {i}about{/i} you?"
        c "Hmmm..."
        c "I keep customer relationships perfectly professional."
        c "You could talk to the girl with the red hair over there though, she might be receptive."

        menu talk2:
            "Talk to the red headed girl.":
            jump camille

            "Wait for Kaira and Nicole instead.":
            jump talkdone

    label camille
        p "Hey, what's your name?"
        x "My name is... Camille."
        p "That's a beautiful name."
        p "Did you manage to find the one man you were looking for."
        t "...no, I- I couldn't."
        p "I'm sorry to hear that. Was he important to you?"
        t "..."
         "I thought he would be somebody who... who would accept me."
        t "...but in the end, I wasn't what he expected."
        p "I'm not sure what to say, but I can tell you're hurt."
        "Fuck did I play a part in upsetting this girl?"
        p "Is there anything I can do to help?"
        t "Y-You're already helping a lot by talking to me, thankyou."
        "Deja vu, it's just like when Vincent comforted me when I was sad."
        p "I'm just passing the favour on. Doing my good deed of the day, that sort of thing."
        p "Hey listen, my [sr] and her friend are coming soon, would you like to join us?"
        t "Ah- I-I really appreciate it.. but I have to go, I'm sorry!"
        t "..but, can we talk again? Sometime?"
        p "Of course, here's my number."
        t "Thankyou!"
        t "..."
        t "Sorry! I forgot to ask your name!"
        p "Haha, that's okay. My name is [p]."
        t "...[p]..."
        p "That's right!"
        t "Thankyou [p]..."
        t "[p]..."
        p "Yeah, you got it!"
        t "Take care, [p]."
        p "You too, Camille. Goodbye!"
        "..."
        "She's such a nice girl, but was kind of strange."
        "There must be a reason Vincent didn't go for it. I guess I'll find out sooner or later."
        jump talkdone



    label talkdone:


    scene bonus_1
    d "And that's all for version 0.2!"
    d "In the next episode, look forward to partying with the girls in their new sexy outfits, as well as a chance encounter with the mysterious stranger again."
    d "And always, please leave feedback on the f95zone page to let me know how you liked Depravity. I've also added a patreon link."
    d "In the meantime, I found something real cool I wanted to show you. Turns out that Nicole girl's a bit of a slut and her photoshoot got leaked!"
    d "Come check it out!"

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
