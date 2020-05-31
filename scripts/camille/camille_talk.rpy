label camilletalk:
    default camille_flag = False
    if camillelvl == 1:
        play music "sounds/armoir.mp3" fadeout 1
        if camille_flag:
            scene black
            scene cam-2 with fade
            p "Hey Camille, we've met before!"
            scene cam-1
            t "...[p]?"
            t "I didn't think I'd see you again."
            p "The town's not too big, I was sure we'd bump into each other again."
            scene cam-3
            t "You... weren't answering my texts and I thought the worst..."
            p "Oh yeah! I gave you my number!"
            p "I'm so sorry Camille, I totally forgot. I actually sold my phone because I needed some money!"
            p "I'll have to get a new one sometime."
            scene cam-2
            t "Oh I see... sorry for assuming."
            p "No, no that's alright."
            p "Anyway, what's happening here?"
            scene cam-4 with dissolve
            t "Oh, sorry I got distracted from my job again!"
            scene cam-5 with dissolve
            t "This is the luxury resort! We have many different kinds of facilities here."
            $ camillelvl += 1
            $ camilletalk = day
            jump Camille
        scene black
        scene cam-2 with fade
        p "Hey."
        p "I think we've met before."
        scene cam-1
        x "Oh, we met at the shopping mall..."
        p "Did you have any luck finding Vincent?"
        scene cam-3
        x "Ah... I must have just missed him..."
        "(Yeah, thought so.)"
        p "So, what's your name?"
        scene cam-3
        t "It's Camille. And you?"
        p "The name's [p]."
        scene cam-5
        t "[p]. I like that name."
        p "Anyway, what's happening here?"
        scene cam-4 with dissolve
        t "Oh, sorry I got distracted from my job again!"
        scene cam-5 with dissolve
        t "This is the luxury resort! We have many different kinds of facilities here."
        $ camillelvl += 1
        $ camilletalk = day
        jump Camille
    if camillelvl == 2 and nicolelvl >= 8:
        scene black
        scene cam-8 with fade
        p "Hello Camille!"
        t "H-hey [p]."
        t "Is there somewhere you'd like to go? Something I can help you with?"
        p "Nothing right now, I was just wondering how you're doing."
        scene cam-11
        p "Remember when we first met? You seemed to have your mind full with something, and I haven't asked you about that since then."
        scene cam-12
        t "Oh, that wasn't anything, really!"
        p "You sure?"
        scene cam-13 with dissolve
        t "Umm..."
        p "Hey, how about this?"
        scene cam-9
        p "Let's go off somewhere, and we'll have a man to man- I mean, man to woman talk."
        t "I- I'm working right now, I couldn't just go off- I mean, I'd love to, but still!"
        scene cam-14 with dissolve
        p "I think people are gonna be alright here. If someone comes, they'll ring the bell, right?"
        scene cam-15 with dissolve
        t "I.. suppose."
        t "But where are we going?"
        p "You know this place better than I do, why don't you show me around the VIP or staff areas!"
        scene cam-12 with dissolve
        t "I can't get you into the VIP, or I'll get into trouble. But maybe... we can talk after work?"
        t "Why don't you relax in the sauna, and I'll just come find you later?"
        scene cam-11
        p "The sauna. Right. Do I need the membership?"
        t "I'd love to let you in for free... but it's hard... I hope you understand?"
        scene cam-10
        p "I won't put you through any drama Camille. Don't worry. I need the silver membership right?"
        t "That's right!"
        p "Hold up, let me check to see if I have it."
        "Hmm, let me see..."
        $ camillelvl += 1
        jump lobby
    if camillelvl == 3:
        if resortmembership > 1:
            scene black
            scene cam-9 with fade
            p "Yup, I'm a member. May I go to the sauna?"
            scene cam-16 with dissolve
            t "Of course. Let me take you."
            scene black with fade
            scene sauna with fade
            t "Welcome to the sauna. Do enjoy your stay here for a bit."
            p "Do come and say hi after work and we'll talk then."
            t "I'll make sure to do that, [p]. Thank you."
            "Time to get changed."
            scene black with fade
            scene cam-17 with fade
            "I admit, I am a little curious about Camille. She always seems so shy, I'm a little surprised she's meeting me afterwards."
            "Is this going to be like a date or something?"
            scene cam-18 with dissolve
            "Ah, shouldn't think too much about it [p]. We'll see."
            "The sauna is actually so nice. I rarely come to these sort of things but it's a great place to relax."
            scene cam-19 with dissolve
            "The hot steam is making me feel sleepy..."
            "..."
            scene black with fade
            "zzzzz...."
            play music "sounds/cyberpunk.mp3" fadeout 1
            scene cam-20 with vpunch
            x "Are you fancying Camille, [p]?"
            scene cam-21 with dissolve
            p "You, always in my dreams."
            x "Camille was rejected by Vincent. Will you reject Camille too?"
            scene cam-22 with dissolve
            p "A little too soon to say, don't you think?"
            p "She seems a nice girl. I have nothing against her."
            scene cam-23
            x "One day, you find out why you made a choice."
            p "What choice?"
            x "Which choice is more depraved? I'll leave that for you to find out."
            p "Why don't you ever answer my damn questions."
            p "Being all mysterious and shit."
            stop music fadeout 1
            scene cam-24 with dissolve
            x "It's time to wake up."
            scene cam-25 with hpunch
            p "Ah!"
            scene cam-26 with dissolve
            "{i}Pant... pant{/i}*"
            scene cam-27 with dissolve
            "I hear someone coming in. Is it Camille?"
            "God how long was I out for?"
            t "Um, [p]?"
            play music "sounds/slopes.mp3"
            scene cam-28 with dissolve
            p "Here."
            t "I'm done with work now, you said you wanted to have a meet up and have a chat?"
            scene cam-29
            p "Yeah, I did say that. The sauna was so relaxing, I lost track of time."
            scene cam-30 with dissolve
            p "Hang on, just let me get changed. Should I meet you back at the reception?"
            t "Yes, I'll meet you back there."
            scene cam-31 with dissolve
            "Shit, I casually suggested a chat and now it seems like something serious."
            "I'm just a lucky guy."
            scene black with fade
            scene cam-32 with fade
            "Ah, back in my Kishou Arima outfit."
            t "Hello [p]."
            scene cam-8 with hpunch
            p "Oh hey Camille. I was just thinking of catching up."
            p "I've been meaning to meet up with you like I promised. Sorry again for not calling you, haha."
            p "So this seems serious. We should do something to fit the occassion. Where do you want to go?"
            scene cam-15 with dissolve
            t "Are you... are you feeling hungry?"
            "Yeah, hungry for action."
            p "I'm not too hungry, but I'll be keen for food still."
            scene cam-16 with dissolve
            t "In that case, how about we go to the bar?"
            p "Hmm, it's like we're coming full circle."
            p "Should we go now?"
            t "Um, I've got a few things I've got to handle at home first. How about I meet you there?"
            scene cam-14 with dissolve
            p "Sure, I'll wait there for you."
            ## transition to bar
            scene black with fade
            play music "sounds/popstars.mp3" fadeout 1
            scene cam-33 with fade
            "Hm, I wonder how long she will take."
            "Girls always take ages, wonder if Camille will be any different."
            scene 7-1 with dissolve
            p "Hey Caroline, how is it going?"
            scene 7-3 with dissolve
            c "Good, [p], good!"
            c "Coming to the bar for a few drinks?"
            p "Yes, and I brought a friend this time!"
            scene 7-5 with dissolve
            c "A {i}girl{/i}-friend?"
            p "Aha, don't be silly. It's Camille. She's come here before, I'm sure you know her."
            scene 7-4 with dissolve
            c "Ah. Camille! Yes, I've come to know her pretty well over a period."
            p "Just thought I'd catch up with her."
            c "How again do you know her?"
            p "Well, I saw her in the bar here with you, rememeber? When I first came?"
            p "I met her before though to be honest. Poor girl was chasing after a guy who wasn't too keen on her."
            scene 7-13 with dissolve
            c "I see."
            p "His loss, am I right?"
            scene 7-9 with dissolve
            c "I think she's a great person and she'll find someone someday."
            c "So how is it that you two are meeting today?"
            p "I just saw that she was feeling a bit down, so I wanted to catch up with her and make sure she's okay."
            p "Anyway, I'm keen to always make new friends."
            c "That's good to hear, [p]."
            c "It looks like you won't have to wait much longer, she's here."
            ## bar scene
            play music "sounds/armoir.mp3" fadeout 1
            scene cam-34:
                pos (0.0, -1.87)
                linear 6 pos (0.0, -0.2)
            $ renpy.pause(6.0,hard=True)
            $ renpy.pause ()
            scene cam-35 with dissolve
            p "Camille!"
            "It looks like she went home to change her outfit and her make-up look. It's very cute and it's nice seeing her out of her working attire."
            p "The last time we were here- how long ago was that?"
            p "You're looking great by the way."
            scene cam-36 with dissolve
            t "Ah-thank you, [p]!"
            # fade to seat
            scene cam-37 with fade
            t "Hello Caroline."
            t "I hope your work isn't keeping you too busy!"
            c "I never mind if it's customers like yourselves."
            c "Can I help you two to a few drinks?"
            p "Camille?"
            scene cam-38 with dissolve
            t "I'm always fond of Dante's original."
            p "Me too. Let's go for that Caroline."
            scene 7-6 with dissolve
            c "I knew you'd say that. Coming right up!"
            scene cam-40 with dissolve
            p "You come here a lot, Camille?"
            scene cam-38 with dissolve
            t "I... come here sometimes."
            t "I like to see Caroline and the drinks here are nice."
            p "Are you good at handling your alcohol?"
            scene cam-39 with dissolve
            t "I was never any good, ah-"
            p "Reminds me of my [sr]. You know, she was here that night we were here last. Did you see her?"
            scene cam-41 with dissolve
            t "Ah, I must have left before she came."
            p "Oh that's right, you had to leave for something early back then. I hope that ended up being alright."
            scene cam-44 with dissolve
            t "Ah yes, I- I managed to sort it out."
            p "So tell me something about yourself, Camille."
            scene cam-43 with dissolve
            t "Err, well I work at the resort, and I enjoy it."
            p "Do you get any perks?"
            scene cam-45 with dissolve
            t "I have access to all the areas for free."
            scene cam-42 with dissolve
            p "Hey, that's pretty awesome."
            p "What do you like to do the most at the resort?"
            t "There's an area with a hot spring. I like going there late at night and bathe with while looking at the stars."
            p "That sounds quite romantic, actually."
            p "Are there many people there at night?"
            scene cam-43 with dissolve
            t "No, it's closed at that time so it's just me. It's the fact that I'm alone that I like so much."
            p "I can imagine that it would be relaxing."
            "My god, Camille really looks like something else with this new make-up."
            "She should rock this look more often."
            t "What about you? What do you like to do?"
            menu:
                "I like meeting girls.":
                    $ depravity += 1
                    scene cam-44 with dissolve
                    t "Aha..."
                "I like going to the resort.":
                    scene cam-45 with dissolve
                    t "Oh, ah- I'm glad to see you come to the resort too."
                    p "Oh, I mean I like to swim and stuff but of course I like to see you too at the resort."
                    scene cam-46 with dissolve
                    t "Ah- I... sorry, forget I said that."
            p "You know, you don't have to talk about it if you don't want to, but what was going on the day I first met you?"
            p "You were looking for a guy called... Vincent?"
            scene cam-47 with dissolve
            t "..."
            t "We used to meet up a bit, and one day, he became more distant."
            ## drinks more
            scene cam-49 with dissolve
            $ renpy.pause()
            scene cam-48 with dissolve
            t "Caroline, may I have one more drink?"
            c "Of course Camille!"
            "Hmm, she's started to drink more heavily after I brought up Vincent. I wonder what's going on there."
            scene cam-47
            p "Sorry to bring it up."
            t "Mm."
            t "It's okay, it's in the past."
            p "So, what else do you do in your free time?"
            scene cam-46 with dissolve
            t "Umm... I also like to draw."
            p "You're quite artistic then, aren't you?"
            p "What do you draw?"
            scene cam-43 with dissolve
            t "All sorts of things. There's an art class nearby."
            p "How's the art class?"
            t "I like it, it taught me the basic skills that I needed."
            t "More often though, I go in by myself to make drawings."
            p "What was the last thing you drew?"
            t "I drew a woman."
            p "You draw people often?"
            scene cam-42 with dissolve
            t "Well, I like just putting down on canvas the figures in my mind."
            t "So it could be anything really. Some days it can be nature, the other days people."
            p "You should show me around the class one day."
            t "I will! That should be fun."
            p "You know, we're in a club."
            scene cam-45 with dissolve
            t "Yes?"
            p "People usually dance in clubs."
            scene cam-44
            t "Oh! I-"
            p "Come on now, don't be shy!"
            p "Show us a few moves."
            scene cam-43 with dissolve
            t "Aha, [p], please-!"
            p "You've had a few drinks already, you should be all loosened up by now!"
            scene cam-46
            t "I really can't dance!"
            p "Oh, alright then. You get off this time."
            p "But next time- alright?"
            scene cam-44 with dissolve
            t "Next... time?"
            p "Yeah. Next time."
            p "For our next date."
            scene cam-43
            t "Ahh..."
            p "To get to know each other better."
            "I'm not stealing Vincent's girl, right? They weren't working out anyway."
            scene cam-45 with dissolve
            t "Okay!"
            scene cam-46 with dissolve
            t "..."
            t "Would you..."
            t "Would you like to come around, to... for me to show you around my house?"
            p "Is it a big house?"
            scene cam-43 with dissolve
            t "It's.. decently sized?"
            p "I'd love to Camille. I'm real curious where you live."
            t "It's one of the guest suites in the resort - I'm lucky enough to be able to live there."
            p "Sounds exciting."
            scene cam-45 with dissolve
            t "Okay, come with me."
            ## to house
            scene black with fade
            play music "sounds/slow.mp3" fadeout 1
            scene cam-50 with fade
            t "Welcome to my home, [p]."
            scene cam-51 with hpunch
            p "Wow, this is your place?"
            scene cam-52 with dissolve
            p "It's got a real modern aesthetic."
            scene cam-53 with dissolve
            p "What the hell, you're doing alright for yourself!"
            scene cam-54 with dissolve
            t "It's because I work at the resort- I can stay here for cheap."
            p "I could really get comfortable here."
            scene cam-55 with dissolve
            p "Wow, a pool too?"
            p "Jesus."
            scene cam-57 with dissolve
            t "I'm happy you like it. Are you hungry?"
            scene cam-56 with dissolve
            p "A little, we didn't actually grab anything to eat at the bar, and alcohol is never good on an empty stomach!"
            p "You got some snacks?"
            scene cam-58 with dissolve
            t "Hmm, I don't have a lot in stock, but I do have some noodles."
            p "Cup noodles?"
            scene cam-59 with dissolve
            t "Yes."
            p "Perfect."
            scene cam-60 with dissolve
            t "Just hang on a moment."
            t "Make yourself at home."
            p "Thank you, and will do!"
            scene cam-61 with dissolve
            "Wow, this place is so nice, and this is just the living room!"
            "If Camille didn't get to live here for cheap, this place would cost a ton."
            scene cam-62 with dissolve
            "I wonder if I could ever afford a place like this."
            "Maybe if I hit big on the crypto coins huh?"
            scene cam-64 with dissolve
            "Since Camille's invited me to her house, does this mean she's okay with the idea of going out with me?"
            scene cam-65
            "Fuck knows."
            scene cam-63 with dissolve
            "She's such a cute girl. I get that Vincent might not like her, but did he have to run away?"
            "I don't feel good asking her about it. I'll just have to chat with Vincent afterwards."
            scene cam-66 with dissolve
            t "(I hope he's looking at me.)"
            t "(Maybe he likes me.)"
            scene cam-67 with dissolve
            t "(Someone, finally, maybe.)"
            t "(Someone to love me for me.)"
            ## exchange glances and smiles
            scene cam-68 with dissolve
            $ renpy.pause ()
            scene cam-70 with dissolve
            $ renpy.pause ()
            scene cam-68 with dissolve
            $ renpy.pause ()
            scene cam-69 with dissolve
            t "(He is.)"
            scene cam-71
            t "Delicious cup noodles- on their way."
            scene cam-73 with fade
            p "It's everyone's favourite."
            p "Something so simple yet so good."
            scene cam-72 with dissolve
            t "Mmmm..."
            t "Late night food is the best."
            p "There's just one thing off. It'll be so much nicer staring at the view."
            scene cam-74 with dissolve
            t "View?"
            p "I'm gonna move over so I can stare at the skyline."
            scene cam-75 with dissolve
            t "Ahaha... okay."
            scene cam-76 with dissolve
            p "Much better."
            scene cam-77 with dissolve
            p "You know, your life must be so good."
            t "..."
            p "You get to work at the resort, where you get to access everything."
            p "After work you get to come back to this awesome house."
            p "If I could own something like this in the future, I'd have made it."
            t "Things aren't always what they look like though, on the surface."
            p "That's true. There's always more than meets the eye."
            scene cam-78 with dissolve
            p "So what's your secret?"
            scene cam-79 with dissolve
            t "Some things you can only learn by being close to somebody."
            t "I like this house, but it feels empty."
            scene cam-80 with dissolve
            t "There's something... missing."
            p "Not feeling too lonely are we?"
            scene cam-81 with dissolve
            t "Not as much as before."
            p "Well, I'm an extra body to keep you warm."
            t "..."
            scene cam-82 with dissolve
            p "Come here."
            t "...[p]?"
            ## kiss
            scene cam-83 with dissolve
            "First base."
            scene cam-84 with dissolve
            p "With a bit of alcohol, you really do come out of your shell don't you?"
            scene cam-85
            t "..."
            t "I-"
            p "It's alright."
            scene cam-86 with dissolve
            t "Thank you for that. I... liked it."
            t "Do you- do you want me to..."
            p "Hmmm?"
            scene cam-88 with dissolve
            t "Let me...let me do something for you."
            p "What are you thinking?"
            scene cam-87 with dissolve
            t "I can... I can return the favour."
            "She looks down suggestively."
            "Shit, this is uncharacteristically quick."
            menu:
                "I'm not going to say no.":
                    $ depravity += 1
                    # bj
                    scene cam-89 with dissolve
                    "Acting in a way that nobody could have imagined, she got down gingerly on her knees."
                    "Expert hands that did not belong to her pulled out my tightening penis."
                    p "Heh, seen one before, Camille?"
                    scene cam-90 with dissolve
                    t "Yes... yes I have."
                    "She took a look at it and I could tell there was a deep hunger behind those eyes, but also, something to prove."
                    "To become so intimate with someone like her so quickly, I could not ever imagine."
                    "There is something more to her, definitely, than meets the eye."
                    "And then she took me."
                    scene
                    $ renpy.movie_cutscene("animations/cam-1.webm", loops=-1, stop_music=False)
                    scene cam-91
                    t "Mmmm."
                    p "Argh."
                    p "You're so damn good, Camille."
                    p "How did you get so good?!"
                    "She sucked my cock with expert technique that she had no right in knowing."
                    "It seemed like she knew exactly where a penis is most sensitive."
                    scene
                    $ renpy.movie_cutscene("animations/cam-2.webm", loops=-1, stop_music=False)
                    scene cam-92
                    "She knew how a penis worked like it was the back of her hand."
                    "Her tongue carressed the underside of my shaft and I took her a lot more seriously."
                    scene
                    $ renpy.movie_cutscene("animations/cam-3.webm", loops=-1, stop_music=False)
                    scene cam-92
                    p "At this rate, Camille, I don't know how much longer I'll last!"
                    scene cam-93 with dissolve
                    p "Oh fuck!"
                    scene cam-94 with flash
                    $ renpy.pause ()
                    scene cam-95 with dissolve
                    p "Oh that was good. Are you alright Camille?"
                    p "...Camille?"
                    t "I..."
                    scene cam-96 with dissolve
                    t "Sorry I'm feeling a bit tired, I need to rest now."
                    p "Are you feeling okay?"
                    t "I'll see you again tomorrow okay? I just..."
                    scene cam-97 with dissolve
                    t "I'm not feeling too well and I need to rest."
                    scene cam-98
                    p "I'm sorry if it's anything I did."
                    t "Don't be! I just-"
                    scene cam-99 with dissolve
                    t "Please, I just need some time to myself."
                    t "I still want to see you again though. I'll see you tomorrow okay?"
                    scene cam-100 with dissolve
                    t "Nothing went wrong... Like I said, I just need some time."
                    scene cam-101 with dissolve
                    p "... Alright Camille, I respect that. I also want to see you again sometime."
                    p "We were moving a bit too quickly, I think."
                    scene cam-100 with dissolve
                    t "I'm sorry to end the night quick. I do like you, [p]."
                    t "There's just something I need to think about."
                    p "By all means."
                    p "I'll see you tomorrow again, okay?"
                    scene cam-102 with dissolve
                    t "Thank you [p]. Goodnight."
                    p "Take care."
                "You're drunk Camille, I don't think you should.":
                    scene cam-103 with dissolve
                    p "I think you're drunk, Camille!"
                    scene cam-104
                    t "Ah, of course, I-"
                    t "I... got carried away."
                    scene cam-105 with dissolve
                    p "It's not your fault, I just don't want to take advantage of you."
                    t "Thank you, [p]."
                    p "Um, you know what? It's probably best I head off now."
                    scene cam-106 with dissolve
                    p "I do want to see you again, though."
                    scene cam-107 with dissolve
                    t "I'm sorry about that, [p]."
                    p "Don't be, Camille. I appreciate it, but I don't want you to regret it tomorrow, haha."
                    p "I'll come chat you up again at the resort soon, alright?"
                    scene cam-108 with dissolve
                    t "Okay!"
                    p "Take care, Camille."
                    t "Goodnight, [p]!"
            stop music fadeout 1
            scene black with fade
            "That was a little strange."
            "Just a little."
            "I think it'd be a good idea to call Vincent and just see what's up."
            "{i}Ring ring...{/i}"
            play music "sounds/wistful.mp3"
            scene cam-109 with dissolve
            v "Hey there, Vincent here. Professional photography, modelling services and more. How can I help?"
            p "Hey Vince, it's me, [p]."
            scene cam-110
            v "Thought you'd never call. How's it going brother?"
            p "Listen, it's late and I'll cut to the chase. It's about that chick Camille."
            v "Huh?"
            p "She's the one you were trying to run away from."
            v "Oh I remember. Just a little unexpected that you want to chat about her."
            p "Are you on your phone right now?"
            v "Sort of, I'm hands-free."
            p "Anyway, are you free sometime?"
            play music "sounds/path.mp3" fadeout 1
            scene cam-111 with dissolve
            v "This sounds like an emergency, what's up?"
            p "It's a little important. How about we catch up and I'll tell you all about it?"
            v "..."
            v "Alright."
            scene cam-112 with dissolve
            v "Let's meet up tomorrow morning at the Ice Cream Parlour."
            p "...sure."
            v "I'll see you then."
            p "See you."
            scene black with fade
            ## The next day...
            "(THE NEXT DAY...)"
            play music "sounds/special.mp3" fadeout 1
            scene cam-113 with fade
            "..."
            scene cam-114
            v "I don't know, I don't know, everything on the menu just looks so good!"
            scene cam-115
            wai "Ahahaha..."
            scene cam-116 with dissolve
            v "I'm on a bit of a time budget though, I need to pick something quick, but I just can't choose."
            scene cam-117 with dissolve
            v "What's good here?"
            scene cam-119
            wai "Well, they're all good, and all the flavours are special-"
            scene cam-118
            v "Really? Ahahahahah!"
            scene cam-120 with dissolve
            "Looks like he's having fun."
            scene cam-121 with dissolve
            "This is an interesting place. I wonder if Vincent chose it for any reason."
            scene cam-123 with dissolve
            "I love the style of those chairs."
            scene cam-122 with dissolve
            "Guess he likes sucking on popsicles hahaha."
            scene cam-124
            v "Hey!"
            scene cam-125
            v "Nice to see you again buddy. Why didn't you say hi?"
            scene cam-126 with dissolve
            v "This guy's with me."
            scene cam-127 with dissolve
            wai "Okay, let me know when you two are ready to order."
            scene cam-128 with dissolve
            p "Thanks for meeting up with me on such short notice."
            scene cam-129
            v "No problem. How are you doing anyway?"
            p "I'm good man, I'm good. You?"
            scene cam-130 with dissolve
            v "Photography stuff here and there. All part of the job. But you on the phone last night-"
            scene cam-131 with dissolve
            v "You sounded like you had something urgent to talk about."
            v "Something about... Camille?"
            scene cam-133 with dissolve
            p "She works at the resort Vincent. I talk to her sometimes."
            v "Ah."
            p "She's a cute girl you know, just a little strange sometimes I feel."
            p "I wanted to ask you about your experiences and what's going on."
            scene cam-132 with dissolve
            v "Do you mean to say... you're hitting on Camille?"
            scene cam-133 with dissolve
            p "I was flirting a little bit... and it ended up that way."
            p "I guess I also want to check that you don't have anything going on with her anymore."
            scene cam-134
            v "No... not anymore."
            p "I didn't want to ask her, but I was curious what happened between you two. I feel like it's troubling her a little."
            scene cam-132 with dissolve
            v "Well..."
            p "Sorry to just spring this onto you."
            scene cam-135
            v "No, no. I had some sort of idea this would be where the conversation would go."
            v "There's not much to it. I mean, we started seeing each other and then I decided I didn't like her anymore."
            v "She found it hard to accept and so that's when I just had to make a break for it."
            p "A break?"
            scene cam-132 with dissolve
            v "Yeah, I broke it up with her the day I bumped into you at the mall."
            p "Damn man. That's tragic. I had no idea."
            scene cam-135 with dissolve
            v "How... is she doing anyway?"
            p "That's what I wanted to talk to you about."
            p "On the surface she's really shy, but there's something deeper there man, and I don't know what it is."
            scene cam-136 with dissolve
            v "Something deeper?"
            p "Yeah. Like, I feel like she's quite lonely and a bit too eager to jump into a relationship."
            p "Is that a red flag?"
            v "You care about red flags, [p]?"
            p "Touche."
            scene cam-137 with dissolve
            v "Well, did she come onto you?"
            p "A little, but she was drunk, I guess. So there's that."
            v "Sigh. Let me just say, she's different."
            scene cam-138 with dissolve
            p "Different how?"
            v "She's not your average girl."
            p "Does she have some sort of complex going on?"
            scene cam-139 with dissolve
            v "I don't know, maybe. Point is- look, I mean I don't feel like I should be telling you whether to go for her or not."
            p "Sure man, I get it, but I just want to figure out if she had some warning signs that made you break up with her."
            scene cam-140 with dissolve
            v "..."
            v "Well... she just wasn't for me man. I wouldn't do it myself if I were you, but of course, we already know that."
            p "Dammit man, what exactly turned you off? Tell me everything."
            scene cam-141
            v "Very well! Don't say I didn't warn you...!"
            scene cam-142 with dissolve
            v "..."
            scene cam-143 with dissolve
            v "I'd say Camille is a person who's had a tough past. Probably due to her experiences, she is less trusting then normal. That's why on the surface she seems quite shy and doesn't really engage."
            v "But under the right cirumstance, she can't supress the feelings she had previously been punished for showing."
            p "..."
            p "That sounds not bad to me. What's the problem?"
            scene cam-141
            v "The problem is! The problem is!"
            scene cam-142 with dissolve
            v "..."
            scene cam-144 with dissolve
            v "I shouldn't say anymore."
            p "C'mon man."
            scene cam-145
            v "Go say hi to her, [p]. The best way is probably for you to find out about her through talking to her yourself."
            p "Sounds fair."
            p "Thanks for coming again. Let me thank you with a milkshake or something from the menu."
            scene cam-146 with dissolve
            v "That's fine, [p]. Don't worry about it. I have to get back to work."
            p "So soon?"
            v "Yeah."
            p "By the way, why did you choose to meet in this place?"
            scene cam-147 with dissolve
            v "I thought it'd be funny."
            v "You see, Camille loves coming to this place."
            v "Just thought I'd show you it so you have a place in mind for a future date."
            p "You're just two steps ahead."
            scene cam-145 with dissolve
            v "But I'm behind on schedule!"
            p "Hang on, isn't it dangerous for us to meet up here then? I mean, if she likes coming around so much."
            scene cam-147 with dissolve
            v "No way she'll be here. She should be working at the resort around this time."
            scene cam-149
            p "The resort only opens in the afternoon- it's the morning right now."
            scene cam-148 with vpunch
            v "Oh shit."
            ## Glances around
            scene cam-150
            $ renpy.pause()
            scene cam-151
            $ renpy.pause()
            scene cam-150
            $ renpy.pause()
            scene cam-151
            $ renpy.pause()
            scene cam-150
            $ renpy.pause()
            scene cam-145 with dissolve
            v "Look."
            scene cam-152 with dissolve
            v "I wouldn't worry too much."
            ## Show Camille outside looking in.
            scene cam-153 with dissolve
            v "After all..."
            scene cam-154 with dissolve
            v "What are the chances?"
            scene cam-155
            t "(Oh, why is [p] talking to Vincent?)"
            t "(Could they be talking about me?)"
            scene cam-156 with dissolve
            t "(No Camille, you musn't, you always assume the worst! It's... probably nothing!)"
            scene cam-157 with dissolve
            $ renpy.pause()
            ## Show Camille leaving
            v "Alright, give me a call whenever you want to catch up again, huh?"
            p "Will do."
            $ daytime = 4
            $ daytimes = str(daytime)
            $ camillelvl += 1
            jump map

        else:
            "I need to make sure I have the silver membership first."
            jump Camille
    if camillelvl == 4:
        scene cam-8 with fade
        p "Hello Camille."
        t "Hello [p]."
        p "How are you feeling today?"
        t "I feel good, [p]..."
        scene cam-12
        t "Sorry about last night!"
        p "Don't say that Camille, we all got a little drunk that night thats all."
        p "So you free after work sometime? We should go out again."
        scene cam-13
        t "You want to go out with me?"
        p "Of course, who wouldn't?"
        scene cam-5 with dissolve
        t "Aha-"
        scene cam-6 with dissolve
        t "..."
        t "Mmm!"
        p "Where should we go this time?"
        scene cam-15 with dissolve
        t "There's this place that's quite good. It serves ice creams and other desserts."
        t "It's called the Ice Cream Parlour. Have you... heard of it?"
        scene cam-14 with dissolve
        p "I... think I know the place you're talking about."
        t "Shall go there after work then?"
        scene cam-9 with dissolve
        p "Sure. In the meantime, can I chill somewhere in the resort?"
        t "Of course, where do you want to go?"
        scene cam-11 with dissolve
        p "I think I'll go to the bath house this time."
        p "I think I already have the membership for that."
        scene cam-8 with dissolve
        t "You do!"
        p "Sweet. I'll see you later!"
        scene black with fade
        ## transition to bath house
        scene cam-158 with fade
        "Time to splash around, relax and kill some time."
        "What'll happen if I doze off again?"
        scene cam-159 with dissolve
        "That girl from my dreams..."
        "Last time I was able to talk to her. But many times I passively listen. And can't respond."
        "That's the thing with dreams though. Sometimes you feel like you just can't move."
        scene cam-160 with dissolve
        "The next time I see her, I'll charge at her. If it's just a dream, nothing will happen."
        "But this time I need answers."
        scene cam-161 with dissolve
        "..."
        "I just need to fall asleep. Shouldn't be too hard, after all-"
        scene cam-162 with dissolve
        "zzz....."
        scene black with fade
        stop music fadeout 1
        ## Wake up
        scene cam-163 with fade
        "Where... am I?"
        play music "sounds/time.mp3"
        "Am I dreaming?"
        scene cam-164
        p "Hello?"
        p "Who are you?!"
        scene cam-165 with dissolve
        "It's her."
        scene cam-166 with hpunch
        p "Hey!!"
        p "Do you hear me!"
        scene cam-167 with dissolve
        "No answer."
        p "Don't wanna talk? I'll make you talk."
        scene cam-166 with vpunch
        p "!!!"
        p "I can't move!"
        x "I appear in your subconcious to guide you, [p]."
        x "This is about the choices you make and how they affect the ending of your story."
        x "I can't give you help now though, not now. Some things you have to see to the end yourself."
        p "Help me?"
        p "Why did you summon me here?"
        scene cam-168 with dissolve
        x "..."
        x "I didn't. It was you who brought me here."
        p "What?"
        scene cam-169 with dissolve
        x "You have some talent."
        x "This might end up working out."
        p "What will work?!"
        scene cam-170
        x "This won't happen again."
        x "Well done, [p]."
        scene cam-171 with dissolve
        p "Wait, wai-!"
        scene cam-172 with dissolve
        $ renpy.pause()
        scene cam-173 with dissolve
        $ renpy.pause()
        scene cam-174 with dissolve
        $ renpy.pause()
        scene cam-175 with dissolve
        p "AHHHH!!!"
        scene black with fade
        $ renpy.pause()
        t "[p]?"
        play music "sounds/slopes.mp3" fadeout 1
        scene cam-176 with vpunch
        p "Ah!"
        p "I fell asleep again."
        scene cam-177 with dissolve
        p "So sorry Camille, haha. This is getting old for me."
        scene cam-178 with dissolve
        t "It's good right? It means you're relaxed."
        p "Why don't you come jump in the pool with me here?"
        p "We've got time right?"
        scene cam-179
        t "Erm. I didn't bring my swimming gear, sorry!"
        p "Oh, alright."
        p "In that case, let me get changed and let's go!"
        scene cam-180 with dissolve
        t "Mm!"
        scene black with fade
        play music "sounds/special.mp3" fadeout 1
        ## Transition
        scene cam-181 with fade
        t "I like this place a lot. It's got really good dessert, and I just love sweet things."
        p "I like this style of decor."
        t "When was the last time you came?"
        p "I've been here once before."
        scene cam-182 with dissolve
        t "How long ago was that?"
        scene cam-183 with dissolve
        p "This morning actually."
        scene cam-181 with dissolve
        t "What was the occassion?"
        p "Hahaha. Asking a lot of questions, Camille."
        t "I was just curious."
        p "..."
        scene cam-184 with dissolve
        p "I came myself out of boredom, but got chatting with some friendly guy along the way."
        p "How often do you come?"
        scene cam-185 with dissolve
        t "I love it so much, I come almost every morning."
        p "Dessert in the mornings?"
        scene cam-186 with dissolve
        t "Helps get me through my day!"
        scene cam-187 with dissolve
        t "Did you see something on the menu you liked?"
        p "I didn't actually get to have anything, so I'm looking forward to this one."
        scene cam-188 with dissolve
        p "What do you suggest?"
        t "The waffles here are really nice - I really like them."
        scene cam-189
        p "Waffles? They do that in Ice Cream places? I was going to ask for a soft serve or something."
        scene cam-190 with dissolve
        t "They have dessert here - so there's actually pancakes too!"
        t "What do you want to try?"
        scene cam-191 with dissolve
        p "Erm. I don't know!"
        scene cam-192
        wai "If I may, Camille is absolute right. We do pancakes and waffles here too!"
        wai "The waffles especially, are great."
        scene cam-193 with dissolve
        wai "In fact, I was going to recommend that to your friend earlier today."
        scene cam-194
        p "Wouldn't exactly call him my friend. More like... an acquiantance. Anyway Camille, I'll just have what you have."
        t "..."
        wai "What would you guys like to have?"
        scene cam-195 with dissolve
        t "Two orders of waffles please!"
        wai "Good choice, just a moment."
        scene cam-196
        p "Go find a seat Camille, I'll be over real quick."
        scene cam-197 with dissolve
        t "Don't take too long."
        scene cam-198 with dissolve
        $ renpy.pause()
        scene cam-199 with dissolve
        p "Ahem."
        scene cam-200 with dissolve
        wai "Yes?"
        p "I don't know how much you heard this morning, but I'd really appreciate it if you could just not reveal anything alright?"
        p "Just please don't talk about the guy from before, as well as everything we talked about."
        scene cam-201 with dissolve
        wai "If that's what you want. Sure."
        p "..."
        scene cam-202 with dissolve
        wai "I'll do you a favour this time. Next time it'll be my turn, alright?"
        p "Sure, whatever."
        scene cam-203
        "Jesus Christ. What does she want?"
        scene cam-204 with dissolve
        p "Sorry about that."
        scene cam-205 with dissolve
        t "No problem!"
        scene cam-206 with dissolve
        p "So, yeah."
        p "Busy day today?"
        scene cam-207 with dissolve
        t "The resort is becoming more popular and they're renovating things left and right."
        p "Well, that's cool I guess. There's actually quite a bit to do at the resort."
        p "You must be very skilled - you're holding down the fort by yourself!"
        scene cam-208 with dissolve
        t "I'm alright, haha."
        p "I'm playing."
        t "So [p], what's your story?"
        scene cam-209 with dissolve
        p "Me? I grew up here you know. I moved after I graduated from high school to study."
        scene cam-210 with dissolve
        p "Didn't work out too well though. Got caught up in the latest cryptocurrency craze and lost my money."
        p "And after all that I'm back here. Resting. A little insecure, but enjoying life and picking myself back up."
        scene cam-211 with dissolve
        p "Haha. Not very impressive, I know."
        scene cam-212
        t "Don't say that, [p]..."
        scene cam-213 with dissolve
        t "I- I know what that's like. Sort of, losing your way, and not feeling comfortable with where you are."
        p "There, there. A kindred spirit. So what's your story?"
        scene cam-214 with dissolve
        t "..."
        scene cam-215 with hpunch
        wai "Two waffles, as ordered."
        scene cam-216
        p "Wow, look at that!"
        scene cam-217 with dissolve
        p "It looks damn good!"
        t "Ah, [p], you have to tell me if you like this."
        p "All of a sudden, I'm really hungry."
        p "Shall we?"
        t "Let's!"
        scene black with fade
        ## A few moments later...
        scene cam-218 with fade
        p "I loved the bit of ice cream on the waffle. It's great. How did I not try this before?"
        t "Ah, there's always a first for everything."
        p "We were talking about something before the food arrived, but I don't remember what it was."
        p "What were we talking about again?"
        scene cam-219 with dissolve
        t "Mmm, I don't remember."
        p "..."
        scene cam-220 with dissolve
        "Vincent said he didn't like Camille because of something about how she suppresses her feelings."
        "She's not as trusting and is shy to start with. Something to do with her past experiences."
        "But isn't this how you want girls to be?"
        play music "sounds/armoir.mp3" fadeout 1
        p "You know, I want to come clean."
        scene cam-221 with dissolve
        t "..."
        p "The person I talked to this morning was Vincent."
        scene cam-222 with dissolve
        t "..!"
        p "I understand you knew each other before."
        p "He's told me everything."
        scene cam-223 with dissolve
        t "..."
        p "And you know what? I don't mind one bit. Everyone's got their own quirks and what not. I mean, it's who you are Camille."
        p "I think you're a very cute and beautiful girl through and through, and you can be honest with me."
        t "Y-you don't mind?"
        p "I don't. I probably can't imagine what happened in the past, but you don't have to hide it."
        p "I won't judge."
        scene cam-225 with dissolve
        t "I've been wanting to hear that for so long..."
        p "Haha, you alright there?"
        scene cam-224 with dissolve
        t "..."
        scene cam-226 with dissolve
        t "Ah, please come back to my place, there's a lot I want to show and tell you."
        p "I'll gladly come."
        scene black with fade
        "I wonder what happened to her in the past."
        "Looks like I'll learn a lot tonight."
        ## Transition
        play music "sounds/slow.mp3" fadeout 1
        scene cam-227 with fade
        t "Welcome again, [p]."
        p "Glad to be back."
        scene cam-228 with dissolve
        t "..."
        p "Is there something you wanted to let me know?"
        scene cam-229 with dissolve
        t "I really liked what you said to me back in the Ice Cream Parlour."
        scene cam-230 with dissolve
        t "It made me really happy."
        p "I was just being honest."
        t "I don't hear it a lot."
        scene cam-231 with dissolve
        t "Do you... like me?"
        p "I think I do, Camille."
        scene cam-232 with dissolve
        t "Thank you, [p]."
        scene cam-233 with dissolve
        t "I... want to show you something. Please close your eyes."
        p "Camille?"
        t "I'll let you know when you can open them."
        p "Very well."
        scene cam-234 with dissolve
        "..."
        scene black with fade
        "Oh my god what's this going to be?"
        "A kiss?"
        "A blow job like last time?"
        "Is she stripping?"
        "I wonder...."
        menu:
            "Sneak a peek.":
                $ depravity += 1
                scene cam-235:
                    pos (0.0, -2.32)
                    linear 6 pos (0.0, 0.0)
                $ renpy.pause(6.0,hard=True)
                $ renpy.pause ()
                "Wow, she {i}is{/i} stripping."
                "I've never seen Camille wear anything racy or provocative."
                "She's always been modestly dressed, This is the first time I'm seeing her... like this."
                "I don't think many people have seen her like this at all - her silky smooth skin... round bottom."
                "I'm a lucky guy."
                scene black with fade
            "Wait.":
                "She deserves this bit of respsect."
        t "[p]?"
        p "Camille."
        t "You can open your eyes now."
        stop music fadeout 3
        scene cam-236:
            pos (0.0, -1.24)
            linear 3 pos (0.0, 0.0)
        $ renpy.pause(3.0,hard=True)
        play music "sounds/jojo.mp3"
        scene cam-237 with hpunch
        play sound "sounds/effects/scratch.mp3"
        $ renpy.pause()
        ## Shock
        scene cam-238
        "{i}Record Scratch{/i}"
        "{i}Freeze Frame{/i}"
        "Yup. That's me, [p]."
        scene cam-239
        "And that's a penis."
        "You're probably wondering how I got myself into this situation."
        "Truth be told..."
        "I'm not too sure myself."
        ## Flashback to Vincent dialogue
        scene cam-254 with flash
        v "I'd say Camille is a person who's had a tough past. Probably due to her experiences, she is less trusting then normal. That's why on the surface she seems quite shy and doesn't really engage."
        v "But under the right cirumstance, she can't supress the feelings she had previously been punished for showing."
        scene cam-241 with fade
        "Dammit Vince. What kind of shit were you telling me before? Why didn't you tell me upfront?"
        "Was he afraid? Ashamed of being surprised too?"
        "Guilty that he rejected her?"
        scene cam-240 with dissolve
        "Does this mean Camille is actually a boy?"
        "But I was wholly convinced that she was a girl, and I was just getting it on with her!"
        "Vincent. What should I do?"
        scene cam-255 with flash
        v "Well... she just wasn't for me man. I wouldn't do it myself if I were you, but of course, we already know that."
        scene cam-256 with flash
        v "Go say hi to her, [p]. The best way is probably for you to find out about her through talking to her yourself."
        scene cam-242 with hpunch
        "Oh my god, what do I do now!"
        scene cam-243
        t "[p]?"
        p "Camille, I-"
        p "...this wasn't what I was expecting."
        scene cam-244 with dissolve
        t "I thought, but, I thought you knew everything!"
        p "Clearly there are a few gaps in my understanding."
        scene cam-245 with dissolve
        t "This always happens to me..."
        scene cam-246 with dissolve
        p "No, no, Camille, I'm just a bit surprised that's all."
        p "...need some time."
        p "I'll... be right back."
        scene cam-247
        "Holy fuck!"
        "I need to talk to somebody."
        scene black with fade
        "Let me call Vincent..."
        scene cam-248 with fade
        "{i}Ring ring ring{/i}"
        p "Pick up you fucker."
        scene cam-249 with dissolve
        v "Vincent here. Photography-"
        p "Listen man, it's me [p]."
        p "You didn't tell me Camille had a dick."
        v "..."
        scene cam-250
        v "Whoa, [p], you didn't ask!"
        p "Bullshit."
        p "You don't think it's important for me to know?!"
        scene cam-251 with dissolve
        v "Man, I tried to tell you but I just thought it was one of those things you have to figure out on your own."
        p "No man, she thought I already knew she had a penis and that's why she got comfortable with- fuck!"
        scene cam-252 with dissolve
        v "Join the club, [p]."
        p "I still care about how she feels man. She? He?"
        p "Man that experience must have destroyed her."
        scene cam-253 with dissolve
        v "I don't know how to help you buddy. I'm still working through it myself."
        p "Sigh. Thanks anyway."
        v "No problem. I'll be happy to meet up another time to debrief."
        p "Goodbye."
        v "Laters."
        scene black with fade
        "I need to talk to [mr]... ask her what I should do."
        $ camillelvl += 1
        $ daytime = 4
        $ daytimes = str(daytime)
        jump map
    ## Camillelvl 5 with Amanda question

    ## generic
    scene cam-5
    p "Working hard Camille?"
    t "I always try my best."
    jump Camille
