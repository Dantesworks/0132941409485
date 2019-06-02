label Amanda:
    call hidescreens from _call_hidescreens_4
    hide screen skip_evening
    scene a-1
    if amandalvl == 1:
        jump amandatalk
    menu:
        "Talk.":
            jump amandatalk
        "Hey [mr]. Can I have some money?" if amandakitchenlvl < 10:
            jump amanda_money
        "I wanted to ask a question about Camille..." if camillelvl == 5:
            play music "sounds/masked.mp3" fadeout 1
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
            m "Look at me, [p]. I'm modelling and doing all that at my age. You woulnd't expect a conservative answer from me, would you?"
            p "..."
            scene a-1 with dissolve
            m "It's up to you. No matter which way you go, I'm sure it'll end up working alright."
            p "Thanks, [mr]. I'll be honest with her, and honest to myself."
            scene a-13 with dissolve
            m "Go got 'em!"
            scene black with fade
            "I need to talk to Camille as soon as I can."
            "But it's in the morning now, and she only works at the resort in the afternoon."
            "Where is she right now?!"
            ## flashback
            scene cam-257 with flash
            t "I love it so much, I come almost every morning."
            scene black with fade
            "That's right, the Ice Cream Parlour!"
            ## Transition
            scene cam-258 with fade
            "She's already here."
            scene cam-259 with dissolve
            p "Excuse me."
            scene cam-260 with dissolve
            t "Ah, [p]."
            scene cam-261 with dissolve
            p "I just wanted to talk to you."
            t "I see."
            p "Sorry for leaving like that last time. My head was full."
            p "But now... Now I have to honest."
            menu:
                "For":
                    $ trapnation = True
                    scene cam-262 with dissolve
                    p "I'll... be honest Camille."
                    p "I think I like you very much."
                    p "Whatever you think holds you back, doesn't. You're a beautiful girl to me and I really want to get to know you better."
                    p "What I did at the apartment- I was a bit surprised. But it doesn't make a difference."
                    scene cam-263 with dissolve
                    t "Oh, [p]! I'm so happy to hear that."
                    scene cam-264 with dissolve
                    t "I was afraid that you wouldn't like me anymore."
                    p "Never."
                    scene cam-265 with dissolve
                    p "Hey. Let's go back to your apartment."
                    t "Now?"
                    p "Yeah, before you get to work. We don't have much time."
                    t "Time for what?"
                    scene cam-266 with dissolve
                    p "Time to pick up where we left off last time."
                    p "You ready?"
                    t "Mmm!"
                    ## sexy times
                    play music "sounds/kiss.mp3" fadeout 1
                    scene black with fade
                    scene cam-278 with fade
                    "Back in her apartment."
                    scene cam-279 with dissolve
                    p "Do you want to do this, Camille?"
                    scene cam-280 with dissolve
                    t "I do."
                    scene cam-281 with dissolve
                    t "And you [p]? Are you sure you want to do this?"
                    p "I do."
                    scene cam-282 with dissolve
                    "We turned away from each other and started taking our clothes off."
                    "This time, when we turned back around, we were both naked."
                    scene cam-283 with dissolve
                    "We looked at each other's bodies and there was a sense of disbelief."
                    "As though we couldn't believe this was happening."
                    scene cam-284 with dissolve
                    t "Y-you look excited, [p]."
                    scene cam-285 with dissolve
                    "She gestures towards my erect member."
                    p "And it's all because of you."
                    scene cam-286 with dissolve
                    "Her penis remained flaccid."
                    t "It takes a bit for mine to be excited."
                    scene cam-287 with dissolve
                    "Our breathing grew heavier as we moved towards each other."
                    scene cam-288 with dissolve
                    t "I can't believe this is happening, [p]."
                    t "I feel like I'm dreaming."
                    p "Don't pinch yourself."
                    scene cam-289 with dissolve
                    "We kissed in an embrace of passion."
                    "Her penis brushed gently across mine, yet remained soft and tender."
                    "Mine grew harder as blood coarsed through its veins."
                    scene cam-290 with dissolve
                    p "You need something more exciting it seems."
                    p "Looks like you need to be roughed up."
                    scene cam-291 with vpunch
                    "I push her towards the ground as she protested meekly."
                    t "[p], what will you do to me?"
                    scene cam-292
                    p "Taking you where you're most vulnerable."
                    t "Ah!"
                    scene
                    $ renpy.movie_cutscene("animations/cam4.mp4", loops=0, stop_music=False)
                    scene cam-293
                    "She gasped for air as I thrust my penis into the depths of her asshole."
                    scene white
                    image cam5 = Movie(play="/animations/cam5.mp4")
                    show cam5 with dissolve
                    t "It hurts, [p]."
                    p "I know Camille, we're not lubed up."
                    p "Should we slow down?"
                    t "...no. I can take it. Go faster!"
                    hide cam5
                    image cam6 = Movie(play="/animations/cam6.mp4")
                    show cam6 with dissolve
                    p "You asked for this girl."
                    "She moaned more as I thrust in and out, her limp penis pushed back and forth."
                    p "Is this enough to get you excited?"
                    t "Mmm!"
                    p "Your dick's still limp though."
                    p "Looks like we still need to go harder!"
                    "I could feel skin tearing against skin as I thrust into her anus and hear her whimpers as she was undoubtedly feeling it too."
                    hide cam6
                    image cam7 = Movie(play="/animations/cam7.mp4")
                    show cam7 with dissolve
                    "This feeling heightened ten times."
                    p "I'm getting close!"
                    t "Ahh!!"
                    hide cam7
                    $ renpy.movie_cutscene("animations/cam8.mp4", loops=0, stop_music=False)
                    scene cam-294 with dissolve
                    "Her whole body shuddered."
                    "As she shook, her limp penis shot out semen, coating the floor with her fluid."
                    scene cam-296 with dissolve
                    p "You came from anal, you dirty little girl."
                    scene cam-295 with dissolve
                    p "And it looks like you've ejaculated without even having an errection."
                    p "You were hiding your hornyness the whole time Camille? How naughty!"
                    t "I... I won't be able to sit for days."
                    scene cam-297 with dissolve
                    "She was dazed and in an absolute bliss."
                    p "Good thing you stand and not sit at the reception then huh?"
                    t "Re...ception?"
                    scene cam-298 with hpunch
                    t "Ah! That's right! I've got work now!"
                    t "I need to get changed."
                    p "I'll get changed too. Don't be late for work!"
                    scene cam-299 with dissolve
                    t "Thank you for everything [p]. I really loved today."
                    p "Thank you too, Camille. This is the happiest I've ever seen you."
                    scene cam-300 with dissolve
                    t "I- I love you [p]."
                    p "Love you too, girl."
                    ## remove later
                    d "This is the end of Camille's content for this version. Thank you for playing!"
                    play music "sounds/special.mp3" fadeout 1
                    scene black with fade
                    "..."
                    scene cam-268 with fade
                    v "Food here's great. Standards haven't slipped once."
                    scene cam-269 with dissolve
                    wai "Thank you! We do our best."
                    scene cam-270 with dissolve
                    v "It's why I come almost every day."
                    scene cam-271 with dissolve
                    wai "How long {i}have{/i} you been a patron for?"
                    v "I started coming not too long ago. It was when I first met Camille, remember?"
                    scene cam-272 with dissolve
                    wai "Oh yes. Speaking of which..."
                    scene cam-273 with dissolve
                    wai "She met up with your friend the other day-"
                    v "Yeah I already know. He called me."
                    scene cam-274 with dissolve
                    wai "No, this one's new. They met up again, and I think they're together now."
                    scene cam-275 with dissolve
                    v "What do you know? Different folks for different strokes, huh?"
                    scene cam-276 with dissolve
                    v "Oh and by the way, remind me never to tell you you anything about my personal life."
                    scene cam-277 with dissolve
                    wai "Ahahahaha!"

                "Against":
                    $ trapnation = False
                    scene cam-262 with dissolve
                    p "I appreciate you for who you are, but that's just not compatible with what I'm going for."
                    p "I'm sorry."
                    scene cam-267 with dissolve
                    p "I'm also sorry for leading you on, I really hope we can still be friends though, but again, it's not for me."
                    t "It's always like this. Nobody ever likes me."
                    p "I'm... sorry."
                    scene cam-121 with dissolve
                    "I stare into the distance. I don't want to meet her eyes."
                    p "I'm sorry for hurting you."
                    t "Thank you for being honest with me, [p]."
                    scene cam-263 with dissolve
                    t "You didn't do anything wrong... it was my fault."
                    scene cam-264 with dissolve
                    t "I... had hope and... it didn't work out."
                    p "It's not your fault."
                    scene cam-265 with dissolve
                    p "I have no doubt you will find somebody one day. I think it's impossible not to."
                    t "Thank you."
                    scene cam-266 with dissolve
                    p "I'll still be annoying you at the resort alright? We're still going to be good friends."
                    t "I'd like that."
                    d "Camille's romance path ends here."
                    d "You can still buy resort memberships and she will be present in relation to other characters but she will no longer be romanceable."
                    ## remove later
                    d "This is the end of Camille's content for this version. Thank you for playing!"
                    play music "sounds/special.mp3" fadeout 1
                    scene black with fade
                    "..."
                    scene cam-268 with fade
                    v "Food here's great. Standards haven't slipped once."
                    scene cam-269 with dissolve
                    wai "Thank you! We do our best."
                    scene cam-270 with dissolve
                    v "It's why I come almost every day."
                    scene cam-271 with dissolve
                    wai "How long {i}have{/i} you been a patron for?"
                    v "I started coming not too long ago. It was when I first met Camille, remember?"
                    scene cam-272 with dissolve
                    wai "Oh yes. Speaking of which..."
                    scene cam-273 with dissolve
                    wai "She met up with your friend the other day-"
                    v "Yeah I already know. He called me."
                    scene cam-274 with dissolve
                    wai "No, this one's new. They met up again, and I think they've seperated now."
                    scene cam-275 with dissolve
                    v "Well, I can understand."
                    scene cam-276 with dissolve
                    v "Oh and by the way, remind me never to tell you you anything about my personal life."
                    scene cam-277 with dissolve
                    wai "Ahahahaha!"
            scene black with fade
            ## Remove
            d "Tune in next time for more!"
            $ camillelvl += 1
            call daykeep from _call_daykeep_24
            jump map

            jump amanda_room
        "Actually, never mind.":
            jump amanda_room
