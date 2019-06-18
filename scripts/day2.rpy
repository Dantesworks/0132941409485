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
        $ depravity -= 1
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
        $ depravity += 1
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
    n "I'll keep an eye out for an outfit that you can wear as well [p]."
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
    n "Something for {i}every{/i} occasion."
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
            p "Surprise me with the next one girls!"

            jump outfitdone
        label swimsuitNicole:
            scene 4-65
            n "I'm sorry Kaira, but I have the hotter body."
            scene 4-67
            s "At least my body is natural~"
            scene 4-64
            if (askflag1 and askflag2 and askflag3):
                jump special
            p "Surprise me with the next one girls!"
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
    n "Now imagine Kaira stroking your cock.. her luscious tits bouncing in front of your face.. her groin grinding against yours.."
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
    play music "sounds/beach.mp3" fadeout 1
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
    scene black
    with fade
    stop music fadeout 1

## Chapter 6

    "..."
    "Guess I have a few moments to kill before they get ready."
    scene 6-1
    with fade
    play music "sounds/cinematic.mp3"
    "This place is big, but I barely know any faces here."
    "If I couldn’t go back to [mr] and Kaira, I would have no business being back at this place."
    "If I hadn’t met that guy who spoke to me back then, I wouldn’t be here either."
    scene 6-2
    "It’s a pity I never got his name. If I met him again I would definitely-"
    stop music fadeout 1
    scene 6-3
    "!!"
    scene 6-4
    play music "sounds/wistful.mp3"
    p "WTF"
    scene 6-5
    "???"
    scene 6-6
    p "HEY!!"
    scene 6-7
    p "Stop!"
    scene 6-8
    p "Why are you running from me?"
    scene 6-9
    with fade
    x "Pant pant..."
    p "Got you!"
    scene 6-10
    p "It’s me, [p], remember? You were that one that consoled me what I was upset!"
    scene 6-11
    x "..."
    scene 6-12
    x "Oh, [p]! I remember you!"
    x "Listen man, I wasn’t running from you, I was running from the chick behind you."
    p "Huh?"
    scene 6-11
    x "Dude, she has to be coming around now, you have to throw her off."
    p "Hang on, explain-"
    x "Go man go!"
    p "...Alright, I’ll do it. Think of it as returning the favour."
    scene 6-17
    with dissolve
    play music "sounds/armoir.mp3" fadeout 1
    "Ah, there she is."
    scene 6-18
    p "Hey there, are you looking for something?"
    scene 6-19
    x  "Oh... hey."
    scene 6-20
    x "Sorry... have you seen... Vincent?"
    p "What does he look like?"
    scene 6-21
    x "...someone with...he has black hair and-"
    p "Oh yeah, I saw a man with black hair run off in that direction. If you keep going that way, you should catch up with him!"
    scene 6-17
    x "S-sorry, I mean, thankyou..."
    scene 6-22
    "..."
    p "Seemed like a nice girl. I wonder why he was running away."
    scene 6-12
    with dissolve
    p "So, it’s Vincent right?"
    v "That’s me."
    p "She’s gone."
    scene 6-14
    play music "sounds/wistful.mp3" fadeout 1
    v "Ahh, thank you so much."
    p "What was that about? I thought you were the virtuous type. Didn’t think you would be going around breaking girl’s hearts."
    scene 6-15
    v "Ah well, you know..."
    p "She was cute too, pity."
    v "It’s a complicated thing."
    scene 6-13
    v "Anyway, it’s good to see you again, how are you holding up?"
    p "I’m good Vincent, thanks again for talking to me that day."
    scene 6-14
    v "No worries!"
    p "But what are {i}you{/i} doing here?"
    scene 6-13
    v "For work. I’m a photographer, I move around a bit."
    p "How long are you staying for?"
    scene 6-14
    v "Quite a while this time, they set up a new studio here."
    scene 6-16
    v "Means I should probably get to know the people in this town."
    v "Do you know many people here?"
    p "Not really, it’s been too long since I last left."
    scene 6-14
    v "God, [p], has put us together."
    v "Let’s go for a drink! Catch up or something."
    v "Bar... stripbar... your choice!"
    scene 6-16
    p "You are definitely not as virtuous as I thought you were."
    scene 6-13
    v "Hey, we’re all a little depraved in our own little ways."
    scene 6-15
    p "I’d love to, but I’ve got another appointment later tonight."
    scene 6-14
    v "No dramas. Here’s my business card."
    v "It’s my photography business number, but I answer it all the time. Give me a call sometime."
    p "Sure thing."
    scene 6-16
    v "Alright man, have fun with whatever you gotta do. See you later!"
    p "Laters!"
    scene black
    with fade
    stop music fadeout 1
    "..."
    "The girls should almost be done. It’s probably time to head to the bar."
    "({i}A few minutes later...{/i})"
## Bar scene Chapter 7

    scene 7-11
    with dissolve
    play music "sounds/wisteria.mp3"
    "Wow, this place isn't bad at all."
    "The lighting is set up perfectly!"
    scene 7-12
    "Wait a minute... is that?"
    "It's the chick that Vincent was running away from!"
    scene 7-11
    "Poor girl, all by herself. Maybe I should go and say hi. But that might be awkward."
    "Dammit, I really need a drink though. What should I do?"
    menu bar:
        "Get a drink for both of you and talk to her.":
            jump talk

        "Get a drink for yourself and ignore her.":
            jump notalk

    label talk:
        scene 7-1
        "The nametag says 'Caroline'..."
        p "Hey, Caroline? I'm looking for a drink."
        scene 7-3
        c "What's on your mind?"
        scene 7-4
        p "Something creative, innovative, and interesting."
        p "Something really good."
        scene 7-5
        c "I think I have just what you need."
        scene 7-6
        c "Here, a glass of Original Dante. It's the best in the house!"
        c "Enjoy."
        scene 7-7
        p "One more thing."
        c "Yes sir?"
        p "Please pour one for the lady as well."
        scene 7-4
        c "Certainly."
        scene 7-18
        x "Hey... thankyou, but you don't..."
        p "Think nothing of it. I can tell you've had a rough day."
        scene 7-16
        x "..."
        scene 7-17
        x "Thankyou."
        jump camillet

    label notalk:
        scene 7-1
        "The nametag says 'Caroline'..."
        p "Hey, Caroline? I'm looking for a drink."
        scene 7-3
        c "What's on your mind?"
        scene 7-4
        p "Something creative, innovative, and interesting."
        p "Something really good."
        scene 7-5
        c "I think I have just what you need."
        scene 7-6
        c "Here, a glass of Original Dante. It's the best in the house!"
        c "Enjoy."
        scene 7-7
        p "Thankyou."
        scene 7-4
        "{i}sip{/i}"
        p "You're right, this is some really good stuff."
        scene 7-5
        c "Told you!"
        scene 7-4
        p "I like this place."
        c "Yeah it's usually quite busy, but today it's a bit more quiet."
        p "It's a good thing right? Gives us more time to chat."
        scene 7-9
        c "Aha."
        c "So, are you by yourself? Or..."
        p "I'm meeting up with my [sr] and her friend. They should be arriving pretty soon."
        p "...but in the meantime, what about you?"
        scene 7-8
        c "What {i}about{/i} me?"
        p "What {i}about{/i} you?"
        scene 7-9
        c "Hmmm..."
        scene 7-14
        c "I keep customer relationships perfectly professional."
        scene 7-5
        c "You could talk to the girl with the red hair over there though, she might be receptive."

        menu talk2:
            "Talk to the red headed girl.":
                jump camillet

            "Wait for Kaira and Nicole instead.":
                jump talkdone

    label camillet:
        $ camille_flag = True
        scene 7-16
        p "Hey, what's your name?"
        scene 7-18
        x "My... my name is... Camille."
        scene 7-16
        p "That's a beautiful name."
        p "Did you manage to find the man you were looking for?"
        scene 7-17
        t "...no, I- I couldn't."
        p "I'm sorry to hear that. Was he important to you?"
        scene 7-16
        t "..."
        scene 7-17
        t "I thought he would be somebody who... who would accept me."
        scene 7-19
        t "...but in the end, I wasn't what he expected."
        scene 7-21
        with dissolve
        p "I'm not sure what to say, but I can tell you're hurt."
        "Fuck did I play a part in upsetting this girl?"
        p "Is there anything I can do to help?"
        scene 7-22
        t "Y-You're already helping a lot by talking to me, thankyou."
        "Deja vu, it's just like when Vincent comforted me when I was sad."
        p "I'm just passing the favour on. Doing my good deed of the day, that sort of thing."
        p "Hey listen, my [sr] and her friend are coming soon, would you like to join us?"
        scene 7-23
        t "Ah- I-I really appreciate it.. but I've got something on, I'm sorry!"
        scene 7-22
        t "..but, can we talk again? Sometime?"
        p "Of course, here's my number."
        scene 7-22
        t "Thankyou!"
        t "..."
        scene 7-23
        t "Sorry! I forgot to ask your name!"
        p "Haha, that's okay. My name is [p]."
        scene 7-21
        t "...[p]..."
        p "That's right!"
        scene 7-22
        t "Thankyou [p]..."
        scene 7-24
        t "[p]..."
        p "Yeah, you got it!"
        t "Take care."
        p "You too, Camille. Goodbye!"
        scene 7-25
        with dissolve
        "..."
        "She's such a nice girl, but was kind of strange."
        "There must be a reason Vincent didn't go for it. I guess I'll find out sooner or later."
        jump talkdone



label talkdone:
# Party Chapter 8
    "..."
    "Why is Kaira and Nicole taking so long?"
    scene 7-1
    p "So, Caroline."
    scene 7-3
    play music "sounds/dreams.mp3" fadeout 1
    c "Yes?"
    p "Let's say you really liked a person, but society frowns upon your relationship, what would you do?"
    scene 7-8
    c "Asking for a friend?"
    p "Of course."
    scene 7-13
    c "Hmm..."
    scene 7-4
    c "I would say nothing should come between true love."
    c "If you really like that person, and they like you back, that's your answer."
    scene 7-14
    c "...but what do I know? I'm just a lowly bar maid!"
    scene 7-4
    p "Don't say that. You're more than you think."
    scene 7-8
    c "And how would you know that?"
    p "I just do."
    p "You... work here a lot?"
    scene 7-4
    c "It's just a part time thing, it's to support my study."
    p "So you're smart {i}and{/i} sexy."
    scene 7-8
    c "How original!"
    p "Just like this glass of Original Dante."
    p "What do you study?"
    scene 7-9
    c "I want to be a doctor one day, so I'm studying medicine."
    p "Impressive, that must be hard."
    scene 7-14
    c "Everyone says that, but I think as long as you put in the work, it can be done!"
    p "Well, people say I walk funny, and I'm pretty confused with what's happening in my life right now."
    p "Diagnose me Caroline, what's wrong with me?"
    scene 7-8
    c "Well, your eyes are darting around a bit. I don't know if you're just shy to meet my eyes, or if you have nystagmus."
    c "Either way, these signs are in keeping with Wernicke's Encephalopathy."
    p "Hang on- how?"
    scene 7-13
    c "I'm saying don't drink too much! Or you'll progress to Korsakoff Psychosis, and that's serious."
    p "...!"
    scene 7-14
    c "I'm joking, you don't have thiamine deficiency!"
    c "You're fun to mess with."
    scene 7-4
    c "But really, don't drink too much. You wouldn't want to embarrass yourself in front of your friends that have just arrived, would you?"
    "!!"
## Chapter 8 Party
    stop music fadeout 1
    s "[p]!"
    play music "sounds/beach.mp3"
    scene 8-0:
        pos (0.0, -1.67)
        linear 6 pos (0.0, 0.0)
    $ renpy.pause(6.0,hard=True)
    $ renpy.pause ()
    scene 8-1
    p "Oh damn you guys are finally here!"
    p "And what is this?"
    scene 8-4
    s "Sexy outfits huh?"
    p "It's really skimpy."
    scene 8-5
    n "Don't worry, it covers the important bits."
    scene 8-3
    s "Well Nicole, why don't you tell [p] about your makeover?"
    scene 8-6
    n "Uhh..."
    scene 8-5
    n "Well it's a sexy bra, sexy panties, sexy heels and these sexy leg things that really accentuate the hips."
    scene 8-7
    n "I also got a hair styling. Makes me look classy!"
    s "Good choice right?"
    scene 8-2
    p "I love it."
    scene 8-12
    s "All me!"
    scene 8-4
    s "And what about my one?"
    scene 8-12
    s "I know you love my boobs, [p], so I picked something that leaves little for your imagination!"
    s "Do you like them even more now?"
    scene 8-9
    n "How scandalous!"
    scene 8-8
    n "[p] is nowhere near as perverted as you are Kaira."
    scene 8-10
    n "Isn't that right [p]?"
    scene 8-1
    p "Yeah, Kaira, keep it in your pants."
    scene 8-13
    s "Hmph!"
    scene 8-14
    s "Looks like I'll have to try harder!"
    scene 8-5
    n "So, [p], are you going to buy us drinks or not?"
    scene 8-1
    p "Of course ladies!"
    p "I recommend Original Dante, apparently it's really creative."
    scene 8-10
    n "Just what you need Kaira."
    n "You need to learn to be more {i}creative{/i}."
    scene 8-14
    s "I think you're {i}creative{/i} enough for the both of us hehe."
    scene 7-1
    p "Hey Caroline!"
    scene 7-3
    p "2 Original Dantes please!"
    scene 8-15
    c "Coming right up!"
    scene 8-16
    c "As requested, 2 Original Dantes."
    scene 8-18
    s "One for each of his girlfriends!"
    scene 7-8
    c "I thought you said one of them were your [sr]?"
    scene 8-19
    p "She is! I have no idea what she's on about."
    scene 7-9
    c "You have interesting relationships [p]."
    scene 8-20
    p "You have no idea."
    scene 8-17
    n "Stop talking and start drinking."
    scene 8-38
    s "{i}sip{/i}"
    scene 8-37
    s "..."
    scene 8-29
    s "Bleh!"
    scene 8-22
    p "So what do you think?"
    scene 8-30
    s "Alcohol!"
    scene 8-28
    n "Well of course it's alcohol dummy!"
    scene 8-26
    n "You don't really drink at all do you Kaira?"
    scene 8-32
    s "I can drink!"
    scene 8-38
    with dissolve
    s "{i}glug...glug...{/i}"
    scene 8-35
    with dissolve
    s "{i}Burp{/i}"
    scene 8-30
    s "Ooohhh..."
    s "..."
    scene 8-31
    s "I love it!"
    scene 8-20
    p "You sure Kaira?"
    scene 8-27
    n "This place is so dead."
    scene 8-34
    n "What's the point of dressing up all sexy if noone's gonna watch?"
    scene 8-18
    s "That's okay!"
    s "We've got [p] to watch us dance all slutty hahaha!"
    scene 8-25
    p "I think you're drunk Kaira."
    scene 8-32
    s "No I'm not!"
    s "Nicole, tell him!"
    scene 8-26
    n "..."
    scene 8-28
    n "I think Kaira could do with a few more drinks!"
    scene 8-34
    n "Grab two more for us, would you Caroline?"
    scene 8-19
    p "Hey what about {i}my{/i} drink?"
    scene 8-28
    n "No more for you [p]..."
    scene 8-33
    n "I need you to be able to get it up later fufufu..."
    "Wow. Jesus Christ."
    scene 8-16
    c "Here, two more Original Dantes."
    scene 8-35
    n "Come on Kaira, here's your medication!"
    scene 8-32
    s "A good girl always takes her medication!"
    scene 8-37
    with dissolve
    s "{i}Drinks in silence{/i}"
    play music "sounds/popstars.mp3" fadeout 1
    scene 8-30
    s "I can do this all day!"
    scene 8-31
    s "OOOOH It's my favourite song from KDA!"
    s "Did you know Nicole! Kaisa and Evelynn are going to come to have a signing event soon!"
    scene 8-28
    n "Oh yeah I've heard of them."
    scene 8-22
    p "KDA? What's that?"
    scene 8-26
    s "You haven't heard of them?"
    scene 8-25
    s "They're only the hottest girl group around. Like I said, two of them are coming over sometime soon."
    scene 8-40
    with dissolve
    n "I love Kaisa. She's got a sexy body with a huge ass."
    scene 8-41
    with dissolve
    s "Really? Evelynn's seductive as hell though."
    s "I wanna be more like her."
    scene 8-18
    s "But neither of them have tits my size!"
    scene 8-31
    s "Come on, let's dance!"
    scene 8-33
    n "You need to fuel up before that, come finish my drink!"
    scene 8-38
    with dissolve
    s "More more more!"
    scene 8-39
    s "Aahahaha!"
## dance floor
    scene 8-42
    with fade
    s "Wooo!"
    scene 8-43
    n "Come on [p], dance with us."
    n "Don't hold back!"
    scene 8-21
    p "I'm trying I swear."
    scene 8-23
    p "I'm just shit at dancing."
    scene 8-45
    s "Heheheh, you just have to let go!"
    scene 8-44
    n "Come, [p]. Slut drop with me when the beat drops."
    n "..."
    n "Now!"
    scene 8-47
    with dissolve
    $ renpy.pause ()
    p "Damn that's hot."
    scene 8-46
    s "What about this one, [p]?"
    scene 8-48
    with dissolve
    s "I call it the grind."
    scene 8-49
    with dissolve
    n "Oh Kaira you are so hot when you let loose."
    scene 8-50
    s "Am I turning you on Nicole?"
    n "Not as much as you're turning [p] on hehe."
    scene 8-51
    s "Show us your moves [p]!"
    menu dancemove:
        "The T Pose":
            jump T
        "Mr Sexy Smexy":
            jump smexy
        "The Seizureman":
            jump seizure
    label T:
        scene 8-52
        with fade
        p "I call this one, the T!"
        n "That's so dumb! I think I'm going to be sick!"
        jump dancemovedone
    label smexy:
        scene 8-53
        with fade
        p "I call this one, Mr Sexy Smexy!"
        n "Hey! Not bad!"
        jump dancemovedone
    label seizure:
        scene 8-54
        with fade
        p "I call this one, the Seizureman!"
        n "...impressive."
        jump dancemovedone

label dancemovedone:
    scene 8-55
    s "Uhh..."
    s "I don't feel so well..."
    scene 8-19
    p "I know I suck but I didn't know I was that bad-"
    scene 8-56
    n "..!"
    n "Take her to the bathroom!"

## Chapter 9 bar bathroom
    scene black
    with fade
    "..."
    scene 9-1
    with fade
    n "She is just out of it! Hahahah!"
    scene 9-3
    s "Nuu..! I'm fine!"
    p "Why did you have to get her so drunk?"
    p "You're her friend, shouldn't you know that she can't take any-"
    scene 9-2
    n "And she's your [sr]! I didn't see you stopping her from drinking!"
    scene 9-4
    s "Nico- You're always trying to ruin my fun and-"
    scene 9-5
    with dissolve
    s "..."
    scene 9-6
    s "[p]..."
    p "...?"
    scene 9-7
    s "Do you love me [p]?"
    p "Ah fuck."
    scene 9-8
    s "Am I sexy?"
    scene 9-9
    s "I can try harder I promise."
    s "You're always act like the big brother in my life. But I love you in a different way."
    scene 9-10
    s "If you won't fall in love with me, will you fall in love with my body?"
    scene 9-11
    "..."
    "Fuck it's happening again, and I don't know how to-"
    scene 9-12
    n "You're rock hard again, [p]."
    scene 9-13
    n "Let me free you up!"
    p "No!"
    scene 9-20
    with dissolve
    "..."
    scene 9-14
    p "What are you trying to do?!"
    scene 9-15
    n "Look, she's barely conscious. She's just functioning purely off impulses."
    scene 9-16
    n "Calm down, she won't remember a thing tomorrow."
    scene 9-17
    n "Meanwhile, you can do to her supple body whatever you like."
    scene 9-18
    n "Should I nibble her tits while you take her virginity?"
    scene 9-19
    n "She {i}is{/i} a virgin, you know."
    scene 9-21
    "The urges are so strong..."
    "But... I can't..."
    scene 9-22
    p "I won't do it. I can fight my depravity."
    p "I won't rape my own [sr]."
    p "I don't know why you want me to."
    scene 9-23
    n "I just want us all to have some fun, but if you're not ready for it, I don't mind."
    scene 9-24
    s "Please [p], let me show you..."
    p "..Kaira..."
    scene 9-25
    with dissolve
    s "Noone has ever seen them before."
    n "You're doing a good job Kaira! Squeeze them together for us."
    scene 9-26
    with dissolve
    s "Is this good, [p]?"
    scene 9-28
    n "Look at how hard [p]'s cock is! That's all because of you Kaira!"
    scene 9-27
    s "Fufufu..."
    s "I'm so glad I make you happy [p]..."
    scene 9-29
    "Am I just going to let this happen?"
    "I can't move!"
    scene 9-30
    s "Spread it all over me [p]~"
    scene 9-31
    "With Nicole rubbing me off and Kaira watching, I think I'm about to-!"
    scene white
    with fade
    "ARGH!"
    n "Good boy~"
    n "Did you like that Kaira?"
    n "If you make [p] cum, then that means you've been a good girl!"
    scene 9-32
    with fade
    s "..."
    scene 9-33
    with dissolve
    s "This...is... cum?"
    scene 9-34
    with dissolve
    s "It tastes..."
    scene 9-35
    with dissolve
    s "Mmm..."
    scene 9-36
    with dissolve
    s "..."
    scene 9-37
    n "Isn't she the cutest thing? Too bad she'll forget everything by tomorrow."
    scene 9-38
    n "I think you'll make a beautiful cumslut Kaira, but now it's my turn."
    scene 9-40
    p "Wait a moment!"
    scene 9-39
    n "I already know you can go at least twice in one go so shut up and feed me."
    scene 9-41
    n "You should be begging me for this."
    scene
    $ renpy.movie_cutscene("animations/nicole1.mp4", loops=-1, stop_music=False)
    scene 9-42
    n "Cum for me [p], you know how much I crave your juicy cum."
    n "Come on, don't be a shy boy."
    p "God you really know how to rile me up."
    p "Fuck I'm close!"
    s "..."
    scene 9-43
    s "I...want..more... cum...!"
    scene 9-44
    n "You already had some Kaira, let me have my turn."
    "I was so close!"
    scene 9-45
    s "But I want more! {i}sob{/i}"
    scene 9-46
    n "You've got it all over your face and tits. Why don't you just lick it off yourself?"
    scene 9-47
    s "Just because you're a hoe with fake tits doesn't mean you get to keep all the delicious cum to yourself!"
    scene 9-48
    n "(I'm never getting this bitch drunk again.)"
    scene 9-49
    n "Fine, I'll share some with you later. Now let me finish him off."
    scene
    $ renpy.movie_cutscene("animations/nicole2.mp4", loops=-1, stop_music=False)
    scene white
    "I'm spent..."
    scene 9-50
    with fade
    $ renpy.pause ()
    scene 9-51
    with dissolve
    $ renpy.pause ()
    scene 9-52
    with dissolve
    $ renpy.pause ()
    scene 9-53
    with dissolve
    n "Hmm!"
    scene 9-54
    with dissolve
    $ renpy.pause ()
    scene 9-55
    with dissolve
    $ renpy.pause ()
    scene 9-56
    with dissolve
    s "mmmm"
    scene 9-57
    with dissolve
    $ renpy.pause ()
    scene 9-58
    n "(You're so beautiful, Kaira.)"
    scene 9-59
    n "Jeez, look at this girl huh?"
    n "Her pussy's so horny, the floor is covered with her pussy grool."
    n "Too bad you're not up for it [p]. Kaira got you off and you won't even return the favour!"
    scene 9-60
    n "If it were up to me, I'd fuck you till you screamed you gorgeous girl~"
    scene 9-61
    p "Enough! We have to clean up and go. It's a miracle noone's walked in on us."
    scene 9-62
    p "Can you stand Kaira?"
    p "..."
    p "You're helping me take her home Nicole."
    scene 9-63
    n "Of course! Anything to spend more time with you and your cute little [sr]."
    scene black
    with fade
    stop music fadeout 1
    "(A few moments later...)"

## Chapter 10 back at home

    scene 10-1
    with fade
    play music "sounds/alchemy.mp3" fadeout 1
    p "Remember to be quiet. It's super late and my [mr]'s probably asleep."
    scene 10-2
    n "You're making the noise not me."
    scene 10-3
    p "I'll take her to bed, go wait for me in the living room."
    s "{i}Groan{/i}"
    scene 10-4
    n "Don't have too much fun without me~"
    scene 10-5
    n "Poor Kaira, she'll take a bit to break in."
    scene 10-6
    n "But we'll violate you soon enough~"
    scene 10-9
    with fade
    n "This is fun, What a nice living room."
    n "It's been a while since I've visited Kaira."
    scene 10-10
    n "Urgh, but I'm still so horny from before."
    n "Why can't anyone match my appetite?"
    scene 10-46
    with fade
    "Man this day has just been so long..."
    scene 10-48
    "Nicole really is a vixen."
    scene 10-14
    with fade
    "!!"
    scene 10-11
    p "Ni-Nicole?"
    scene 10-12
    n "What are you gawking at [p]?"
    scene 10-13
    n "I've gotten you off 4 times today, why don't you come and return the favour?"
    scene 10-15
    p "I'm so tired, I can barely stand."
    scene 10-18
    n "I know you're tired baby, so I'll do the work, like I always do."
    n "Don't worry. Once we get started, you'll wish we never stopped."
    scene 10-15
    n "You're a sex fiend, [p], you can just keep going on and on."
    p "Fake tits, fake ass.. you've fully embraced being a whore haven't you?"
    scene 10-17
    n "Ouch, I'll have you know the ass is real, but I'm always open to augmenting myself, [p]..."
    scene 10-18
    n "I can be your personal bimbo~"
    p "That's what I like to hear, especially after the shit you pulled at the bar today."
    scene 10-16
    n "Oh come on, I know you enjoyed it as much as I did."
    n "Now {i}get{/i} on the floor!"
    scene 10-7
    with fade
    m "Did... I just hear something?"
    scene 10-8
    m "It's from the living room!"
    scene 10-19
    with fade
    n "How does it feel to be straddled?"
    n "Let's edge together all night long~"
    scene
    $ renpy.movie_cutscene("animations/nicole3.mp4", loops=-1, stop_music=False)
    scene 10-20
    n "Are you coming along?"
    n "Do you want to put it in?"
    n "I want to put it in too~!"
    scene 10-21
    p "You little minx."
    p "One of these days you'll flip my switch."
    scene 10-36
    with fade
    m "!!"
    scene 10-37
    m "([p] and... Kaira's friend?)"
    m "(Wow, how bold of them to do it in the living room!)"
    scene 10-38
    n "!!"
    scene 10-39
    n "(Shit, that's [p]'s [mr]!)"
    scene 10-40
    n "(Let me show you what you're missing out on Amanda!)"
    scene 10-22
    with dissolve
    n "Say out loud what you'll do to my voluptuous body [p]."
    p "I will fuck you until your eyes-"
    scene
    $ renpy.movie_cutscene("animations/nicole4.mp4", loops=0, stop_music=False)
    scene 10-23
    n "Ahhh~!!"
    p "You depraved little bitch, it slid right in."
    n "Hang tight, [p]. I'm about to rock your world!"
    scene
    $ renpy.movie_cutscene("animations/nicole5.mp4", loops=-1, stop_music=False)
    scene 10-24
    p "I can't believe it. You really are just a horny little slut aren't you?"
    n "It... feels.... so... good~"
    scene 10-41
    m "(I can't believe [p] and Nicole are fucking in front of my eyes!)"
    scene 10-44
    m "(He's grown so much...)"
    m "(And his thick cock thrusting in and out of her pussy...)"
    scene
    $ renpy.movie_cutscene("animations/nicole6.mp4", loops=-1, stop_music=False)
    scene 10-25
    n "Faster~ faster~ faster~!"
    scene 10-45
    m "(It's been so long, and somehow... I wish it were me bouncing on that cock!"
    scene
    $ renpy.movie_cutscene("animations/nicole7.mp4", loops=-1, stop_music=False)
    scene 10-26
    n "Oooh I'm close I'm so fucking close~!"
    scene 10-43
    m "(Calm yourself down Amanda!)"
    scene 10-42
    m "(Let [p] have his personal space...)"
    scene 10-27
    n "AHHHH~!!!!!"
    scene
    $ renpy.movie_cutscene("animations/nicole8.mp4", loops=0, stop_music=False)
    scene 10-28
    n "{i}Pant...pant...{/i}"
    p "Just... like a cheap whore."
    scene 10-29
    n "It's been such a long time since I came this hard."
    n "Your cock is amazing."
    scene 10-30
    "I'm so tired... I can barely stay awake."
    p "Go on, just give me a few moments..."
    scene 10-31
    n "You did a great job [p]~"
    n "You made me cum like a fountain!"
    scene 10-32
    p "Don't just leave me here... help.."
    n "Oh no I think I've outstayed my hospitality."
    scene 10-33
    n "See you in the morning [p]."
    n "Well..."
    scene 10-34
    n "...I won't be, but your [sr] or [mr] will."
    n "Wouldn't it be fun for them to find you passed out like this?"
    n "Goodnight [p]~"
    scene 10-35
    p "You.... bitch....."
    p "zzzzzzzzz"

    jump christmas
