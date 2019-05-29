label Amanda:
    call hidescreens from _call_hidescreens_4
    hide screen skip_evening
    scene a-1
    if amandalvl == 1:
        jump amandatalk
    menu:
        "Talk":
            jump amandatalk
        "Hey [mr]. Can I have some money?" if amandakitchenlvl < 10:
            jump amanda_money
        "I wanted to ask a question about Camille..." if camillelvl == 5:
            scene a-2 with fade
            p "Hey [mr]."
            scene a-1 with dissolve
            m "Hello!"
            p "I've got a strange question. It's a little weird."
            scene a-5 with dissolve
            m "Don't worry, you can ask me anything."
            p "Alright. I guess I'll go in straight into it then."
            p "Sigh... I've been seeing a girl recently [mr]."
            scene a-4 with dissolve
            m "That's so exciting! I'm so glad to hear."
            p "You see, I found out recently that she's not as she seems."
            scene a-5 with dissolve
            m "Every woman has secrets."
            p "..."
            p "Well, 'she' is actually a 'he.'"
            scene a-3 with dissolve
            m "I don't-"
            p "She has a dick, [mr]. I guess she's transgendering."
            m "..."
            m "And what are {i}your{/i} thoughts?"
            p "I don't know, I'm confused."
            scene a-9 with dissolve
            m "What are you worried about?"
            p "I'm worried about there being a penis on a girl I'm seeing. I'm worried about what people are going to think of me."
            p "I'm worried about how it's ever, possibly going to work out."
            scene a-11 with dissolve
            m "That's what other people think. What do you think?"
            p "I'm worried about how she's feeling and how everyone must have hurt her. And I feel sorry for her."
            scene a-5 with dissolve
            m "It sounds like you care about this person, you're just a little thrown off."
            p "Of course I do, but I can't care for her in the same way now."
            m "Why not? What's the difference?"
            p "..."
            p "You're encouraging me."
            scene a-2 with dissolve
            m "I'm encouraging you to think about what you want, and not what other people think."
            m "Look at me, [p]. I'm modelling and doing all that at my age. You woulnd't epxect a conservative answer from me, would you?"
            p "..."
            scene a-1 with dissolve
            m "It's up to you. No matter which way you go, I'm sure it'll end up working alright."
            p "Thanks, [mr]. I'll be honest with her, and honest to myself"
            scene a-13 with dissolve
            m "Go got 'em!"
            scene black with fade
            "I need to talk to Camille as soon as I can."
            "But it's in the morning now, and she only works at the resort in the afternoon."
            ## flashback
            scene cam-257 with flash
            t "I love it so much, I come almost every morning."
            scene black with fade
            "That's right, the Ice Cream Parlour!"
            ## Transition
            "She's already here."
            p "Excuse me."
            t "Ah, [p]."
            p "I just wanted to talk to you."
            t "I see."
            p "Sorry for leaving like that last time. My head was full."
            p "But now... Now I have to honest."
            menu:
                "For":
                    $ trapnation = True
                    p "I'll... be honest Camille."
                    p "I think I like you very much."
                    p "Whatever you think holds you back, doesn't. You're a beautiful girl to me and I really want to get to know you better."
                    p "What I did at the apartment- I was a bit surprised. But it doesn't make a difference."
                    t "Oh, [p]! I'm so happy to hear that."
                    t "I was afraid that you wouldn't like me anymore."
                    p "Never."
                    p "Hey. Let's go back to your apartment."
                    t "Now?"
                    p "Yeah, before you get to work. We need some time."
                    t "Time for what?"
                    p "Time to pick up where we left off last time."
                    p "You ready?"
                    ## sexy times
                    "Back in her apartment."
                    p "Do you want to do this, Camille?"
                    t "I do."
                    t "And you [p]? Are you sure you want to do this?"
                    p "I do."
                    "We turned away from each other and started taking our clothes off."
                    "This time, we were both naked."
                    "We looked at each other's bodies and there was a sense of disbelief."
                    "As though we couldn't believe this was happening."
                    t "Y-you look excited, [p]."
                    "She gestures towards my erect member."
                    p "And it's all because of you."
                    "Her penis remained flaccid."
                    t "It takes a bit for mine to be excited."
                    "Our breathing grew heavier as we moved towards each other."
                    "We kissed in an embrace of passion."
                    "Her penis brushed gently across mine, yet remained soft and innocent."
                    "Mine grew harder as blood coarsed through its veins."
                    p "You need something more exciting it seems."
                    p "Looks like you need to be roughed up."
                    "I push her towards the ground as she protests meekly."
                    t "[p], what will you do to me?"
                    p "Taking you where you're most vulnerable."
                    t "Ah!"
                    "She gasped for air as I thrust in her ass."
                    t "It hurts, [p]."
                    p "I'm sorry Camille, should we slow down?"
                    t "...no. Go faster!"
                    "She moaned more as I thrust in and out, her limp penis pushed back and forth."
                    p "Is this enough to get you excited?"
                    t "Mmm!"
                    p "Your dick's still limp"
                    p "Looks like we need to go-"
                    t "Ahh!!"
                    "Her whole body shuddered."
                    "As she shook, her limp penis shot out semen, coating the floor with her fluid."
                    p "You came from anal, you dirty little girl."
                    p "And it looks like you've ejaculated without even having an errection."
                    p "You were hiding your hornyness the whole time Camille? How naughty?"
                    t "I... I won't be able to sit for days."
                    "She was dazed and in an absolute bliss."
                    p "Good thing you stand and not sit at the reception then?"
                    t "Ah! I've got work soon!"
                    t "I need to get changed."
                    p "I'll get changed too. Don't be late for work!"
                    t "Thank you for everything [p]. I really loved today."
                    p "Thank you too, Camille. This is the happiest I've ever seen you."
                    t "I- I love you [p]."
                    p "Love you too, girl."
                    ## remove later
                    d "This is the end of Camille's content for this version. Thank you for playing!"
                    scene black with fade
                    "..."
                    v "Food here's great. Standards haven't slipped once."
                    wai "Thank you! We do our best."
                    v "It's why I come almost every day."s
                    wai "How long {i}have{/i} you been a patron for?"
                    v "Not too long ago. It was when I first met Camille, remember?"
                    wai "Oh yes. Speaking of which..."
                    wai "She met up with your friend the other day-"
                    v "Yeah I already know. He called me."
                    wai "No, this one's new. They met up again, and I think they're on good terms now."
                    v "Well, what do you know? Different strokes for different folks huh?"
                    v "Oh and by the way, remind me never to tell you you anything about my personal life."
                    wai "Ahahahaha!"

                "Against":
                    $ trapnation = False
                    p "I appreciate you for who you are, but that's just not compatible with what I'm going for."
                    p "I'm sorry."
                    p "I'm also sorry for leading you on, I really hope we can still be friends though, but again, it's not for me."
                    t "Thank you for being honest with me, [p]."
                    t "You didn't do anything wrong... it was my fault."
                    t "I... had hope and... it didn't work out."
                    p "But hey, listen. I have no doubt you will find somebody one day. I don't think it's impossible not to."
                    t "Thanks."
                    p "I'll still be annopying you at the resort alright? We're still going to be good friends."
                    t "I'd like that."
                    d "Camille's romance path ends here."
                    d "You can still buy resort memberships and she will be present in relation to other characters but she will no longer be romanceable."
                    ## remove later
                    d "This is the end of Camille's content for this version. Thank you for playing!"
                    scene black with fade
                    "..."
                    v "Food here's great. Standards haven't slipped once."
                    wai "Thank you! We do our best."
                    v "It's why I come almost every day."s
                    wai "How long {i}have{/i} you been a patron for?"
                    v "Not too long ago. It was when I first met Camille, remember?"
                    wai "Oh yes. Speaking of which..."
                    wai "She met up with your friend the other day-"
                    v "Yeah I already know. He called me."
                    wai "No, this one's new. They met up again, and I think they've seperated now."
                    v "Well, I can understand."
                    v "Oh and by the way, remind me never to tell you you anything about my personal life."
                    wai "Ahahahaha!"
            scene black with fade
            $ camillelvl += 1
            call daykeep
            jump map

            jump amanda_room
        "Actually, never mind.":
            jump amanda_room
