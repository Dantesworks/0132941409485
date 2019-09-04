label amanda_studio:
        if amandalvl == 11:
            p "Just going to say hi to my [mr]."
            scene a-17 with dissolve
            v "All good man. You know the way."
            play music "sounds/wisteria.mp3" fadeout 1
            scene a-24 with dissolve
            p "Hey [mr]!"
            m "Back already?"
            p "What, you're not glad to see me?"
            scene a-28 with dissolve
            m "Yes, [p], but I've got work to do!"
            p "I think I'm going to help Vincent around with some photo work, so perhaps I've got some work to do too."
            m "Some of the other girls have photoshoots that need performed."
            scene a-30 with dissolve
            p "Yeah I know. I'll go look at that."
            jump studio_lobby
        if amandalvl == 12:
            scene black with fade
            play music "sounds/wisteria.mp3" fadeout 1
            scene a-114 with fade
            p "Hey, [mr]! How's work?"
            scene a-115 with dissolve
            m "There's a lot to get through! And how are you?"
            p "I've been so busy, [mr], but I've got a casual position at Dante Studios now, taking pictures."
            scene a-116 with dissolve
            m "That's awesome! I've heard! I'm so happy you're getting something out of this too."
            p "Thanks, [mr]. Have you been in many photoshoots yet?"
            scene a-117 with dissolve
            m "Yes, some basic stuff, nothing that I haven't done before. But there's exciting things coming up. Has Vincent told you?"
            p "No, he said he didn't know too much about it, and told me to ask you."
            scene a-118 with dissolve
            m "Oh, in that case, let me explain."
            scene a-119 with dissolve
            m "Nyx, Maya, and I are going to have a beach themed photoshoot for the main page of Dante's website!"
            m "It's going to be a link to show off the rest of the summer collection."
            p "That's fantastic, you're rising through the ranks quickly."
            scene a-120 with dissolve
            p "Does this job have something to do with me?"
            scene a-121 with hpunch
            m "Yes, I requested you to be our photographer. This is just like the old times, isn't it!"
            "Wow, hubba hubba!"
            p "Yeah, but now it'll be with two other super models."
            scene a-122 with dissolve
            m "Speaking of them, what is your opinion of Nyx?"
            p "Hmm. Nyx is quite confident in herself, I feel. And rightfully so, I mean she's kind of pretty."
            scene a-123 with dissolve
            m "Do you think so? Well I feel like she is too promiscuous, and I think women shouldn't be like that."
            scene a-124 with dissolve
            m "Remember to not go for girls like that, okay [p]? You should pick a classy woman."
            scene a-125 with dissolve
            m "Did you see her try to flirt with you in front of me? What a skank!"
            p "Well, to be fair, she didn't know I was supposed to be your boyfriend before you told her, I think she laid off quickly after that."
            scene a-126 with dissolve
            m "You think so? Anyway, remember what I always say - you need a woman who not only looks good but also knows how to care for you."
            scene a-127 with dissolve
            p "Yeah, got it [mr]. Jeez, tell me more about the photoshoot."
            scene a-128 with dissolve
            m "Yes! This one is going to be a bit more complicated than the previous photoshoots you've had, I think."
            m "Hmm, they told me to let you know to add the 85mm lens to your collection for some more versaility in your shots."
            m "I think just show up with your camera, your lens and yourself... and let us, the {i}super models{/i} do the rest of the work."
            p "Sounds easy enough! I'll make sure I get ready then."
            scene a-129 with dissolve
            m "Please! Come talk to me again when you're done and we can start the shoot!"
            scene black with fade
            $ amandalvl += 1
            jump studio_lobby
        if amandalvl == 13 and primes_85:
            scene black with fade
            play music "sounds/wisteria.mp3" fadeout 1
            scene a-114 with fade
            p "Hey, [mr]! I got the lens so I'm all set. How are you going?"
            scene a-115 with dissolve
            m "I'm going good, [p]. That's great you're ready, I wish we were as well."
            m "Could you give me and the girls some time to get ready? We just need to get changed into our swimsuits."
            p "Fair enough. Should I just wait here?"
            scene a-118 with dissolve
            m "If you'll turn around while I get changed."
            p "You're going to get changed here?"
            m "Yes, this room is for everything work related."
            p "Also fair enough. Okay [mr]. I promise I won't peek."
            "Heh heh heh..."
            scene a-116 with dissolve
            m "It's fine, [p]. Haven't we done this many times before? Don't forget, you've even seen me naked many times when you were young!"
            scene a-30 with dissolve
            p "Wow, [mr], you're really taking this boyfriend-girlfriend roleplay to the extreme here. If I weren't myself I'd say you're hitting on me!"
            m "Oooh? And so what if I am?"
            p "I would say, bring it lady. Show me what ya got. Don't tell me that being Dante's model is just for show!"
            scene a-115 with dissolve
            m "You're a cheeky boy, [p], but you really know how to make a woman feel special, I'll tell you that!"
            scene a-117 with dissolve
            m "It'll be good if you can keep this up around Nyx, that'll show her that I've still got what it takes..."
            scene a-119 with dissolve
            p "Hahaha. Go, get changed! We've got a shoot to do."
            m "Alright, alright."
            scene a-130 with dissolve
            m "Just close your eyes, and I'll be done in bit!"
            ## change
            scene a-131 with dissolve
            "Alright [p]. You know the drill."
            scene a-132 with dissolve
            menu:
                "Peek.":
                    $ depravity += 1
                    scene a-133 with fade
                    "Hnng!"
                    "She has such huge tits for a relatively slender waist."
                    "No wonder Kaira is jealous!"
                    scene black with fade
                "Wait.":
                    "I'm not perving on my [mr] today!"
            m "I'm ready, [p]."
            # transition
            play music "sounds/kiss.mp3" fadeout 1
            scene a-134:
                pos (0.0, -2.21)
                linear 6 pos (0.0, 0.0)
            $ renpy.pause(6.0,hard=True)
            $ renpy.pause ()
            scene a-135 with dissolve
            p "Wow, [mr]! That outfit looks great on you!"
            m "Aww, thanks [p]~"
            m "There's one more bit of assessory however..."
            scene a-136 with dissolve
            m "Now the look's complete."
            p "I could definitely see you on banners all around the country."
            m "Hopefully we'll see that after the model shoot."
            m "Now come on, [p], let's go!"
            scene black with fade
            scene a-137 with fade
            p "This place is actually massive. I was here the other day taking a few pictures for Maya."
            p "This screen here is new though. It must be for the beach theme."
            m "That's right, [p]."
            scene a-138 with dissolve
            p "Are you nervous?"
            m "No. Are you?"
            scene a-139 with dissolve
            p "..."
            p "I'm chill."
            p "So when are the other models getting here?"
            ny "Looks like we're right on cue."
            play music "sounds/pretty.mp3" fadeout 1
            scene a-147:
                pos (0.0, -1.94)
                linear 6 pos (0.0, 0.0)
            $ renpy.pause(6.0,hard=True)
            scene a-143 with dissolve
            "Holy... damn."
            scene a-141 with dissolve
            ma "You look great, Amanda!"
            "Yeah well you guys look great too."
            scene a-142 with dissolve
            m "Oh thanks girls! I see you guys have gone with a matching outfit!"
            scene a-143 with dissolve
            ny "Yes, we thought we'd look cute. I hope you'll agree."
            scene a-144 with dissolve
            p "For sure! I'm loving it. Both of you girls look excellent."
            scene a-145 with hpunch
            m "Ahem, [p]?"
            scene a-146 with hpunch
            p "I mean, erm. I've said too much."
            "Damn, [mr] is snippy today."
            scene a-148 with dissolve
            ny "Amanda really has you on a leash, hasn't she [p]?"
            p "It's not like that, really."
            scene a-149 with dissolve
            m "Let's be a litte professional here, girls. We're here to do a photoshoot."
            "It got serious real quick."
            scene a-150 with dissolve
            p "Okay okay ladies, one at a time, alright? And I'm talking about the photos."
            scene a-151 with dissolve
            p "We'll do some pictures of you guys individually, then as a group. How does that sound?"
            ma "You're the photographer, [p]."
            ny "Maya's right. Give us some directions, like I taught you to."
            scene a-152 with dissolve
            p "Okay. Which one you first?"
            scene a-153 with dissolve
            m "That's up to you, [p]!"
            p "Fine. How about you first then, [mr]- I mean, girlfriend? We were the first here, after all."
            "Shit that was close!"
            scene a-154 with dissolve
            m "Alright, let's go. This is so surreal, having you around while I'm working."
            p "I bet you didn't see us working together, did you, [mr]?"
            "Oh shit I did it again!"
            scene a-155 with hpunch
            m "Ahaha! My boyfriend meant to say mommy. He's into women with motherly instincts who can care for him."
            p "Uh, yes! That's why I call her [mr]. Not for any other reason, nope!"
            scene a-156 with hpunch
            ma "It is very curious indeed. What do you think, Nyx?"
            ny "I think I could be very motherly too if it came to it."
            p "Anyway! Let's get back to work! Amanda, why don't you start posing?"
            p "Let's get a few quick ones."
            scene a-157 with fade
            m "(I have a strange feeling as [p] is taking pictures of my body.)"
            m "(I feel like I'm the centre of attention, and everyone is looking at me. This is why I chose to be a model!)"
            scene a-158 with dissolve
            m "(Are you watching Nyx? Maya? This is a strange feeling, but I love it.)"
            scene a-159 with flash
            $ renpy.pause()
            scene a-160 with flash
            $ renpy.pause()
            scene a-161 with flash
            $ renpy.pause()
            p "You look beautiful, Amanda."
            ma "I agree, but let's move on a little, shall we? Or we will never get to the group shots."
            p "The exotic Maya has spoken. Sorry Amanda, we'll get right back to you soon."
            scene a-162 with dissolve
            m "I'm looking forward to it!"
            scene a-163 with fade
            ma "So [p], let's put your photography skills to the test."
            p "I hope you'll see I've improved."
            scene a-166 with flash
            $ renpy.pause()
            p "You look great in that swimsuit, Maya! Let's get one with you with your hands in front of your chest, looking demure."
            scene a-164 with flash
            $ renpy.pause()
            p "The boys will lap this up."
            scene a-165 with flash
            $ renpy.pause()
            p "This should be enough. Come on up Nyx, it's your turn."
            scene a-167 with fade
            ny "Let's show the other girls what we got."
            ny "Give me a few directions, [p], like I taught you."
            p "Alright. Look at the camera like you want to have sex with it."
            scene a-168 with dissolve
            ny "With pleasure."
            scene a-168 with flash
            $ renpy.pause()
            scene a-169 with flash
            $ renpy.pause()
            scene a-170 with flash
            $ renpy.pause()
            scene a-172 with hpunch
            m "(Oh my god, what is Nyx teaching [p] to say?)"
            p "Seductive! Now let's amp it up even more!"
            ny "Well, there's only one way to dial the temperature up~"
            scene a-173 with flash
            $ renpy.pause()
            p "What a scoop!"
            m "(I can't believe Nyx is playing with [p] right in front of me! How dare she? [p] is {i}my{/i} boyfriend!)"
            play music "sounds/path.mp3" fadeout 1
            scene a-171 with hpunch
            m "Hang on, stop this right now!"
            m "[p], there's something I need to do, and I need you to come with me. It's urgent."
            p "We won't be too long, we just need to do the group shot-"
            m "No ifs, ands, or buts young man!"
            m "We're going now!"
            scene a-174 with dissolve
            p "Alright, alright. Sorry girls, um... we'll finish this at a later time."
            # exit
            play music "sounds/pretty.mp3" fadeout 1
            scene a-175 with dissolve
            ny "Oh?"
            scene a-176 with dissolve
            ma "You should have shown some more sensitivity, Nyx."
            scene a-177 with dissolve
            ny "But this is how I work, Maya. Seduction sells. You're far too innocent to know. You should be more like me."
            ma "Whatever it is, you've upset Amanda now. We'll have to make it up to them."
            scene a-178 with dissolve
            ma "And besides, me being innocent is the reason you like me."
            ny "You're not wrong, Maya~"
            # back to mc
            scene black with fade
            play music "sounds/alchemy.mp3" fadeout 1
            scene a-179 with fade
            p "What's the big idea, [mr]? Is something up?"
            m "You know what you've done, young man."
            p "..."
            scene a-180 with dissolve
            m "I think that Nyx is setting a very bad example for you."
            scene a-181 with dissolve
            m "I'm supposed to be your girlfriend, but even then she was flirting with you! Right in front of me!"
            scene a-182 with dissolve
            p "She's a super model, [mr]. How often do I get to be in the same room as a super model? And to be with someone playful like Nyx-"
            scene a-183 with hpunch
            m "You know who else is a super model? Me, [p], me!"
            scene a-184 with dissolve
            m "She's not that much better than me, is she? I've still got it, haven't I? It's what you've always said."
            p "Oh, [mr]..."
            scene a-185 with dissolve
            p "Of course you're beautiful too, but its different."
            scene a-186 with dissolve
            m "Nyx is going to think that I'm a cuckqueen pushover who lets other women flirt with their own man."
            p "Nyx is sexy hot. It's true. You are hot too, but people don't just flirt with their own [mr] like that as naturally."
            p "I'm sorry for the shitty act. I'll make sure to pretend you're my girlfriend more."
            scene a-187 with dissolve
            m "...pretend?"
            m "Oh [p], I'm sorry. It's not just that..."
            scene a-188 with dissolve
            m "Sometimes, I can't help but feel like I'm... inferior, like my days are behind me already."
            p "That's not true, [mr]! You're a super model!"
            scene a-189 with dissolve
            m "Like the rest of the girls?"
            p "Of course."
            scene a-190 with dissolve
            m "I have the same sex appeal as the other girls?"
            p "That's why you're modelling with them."
            scene a-191 with dissolve
            m "Then why don't you flirt with me the same way you flirt with Nyx? If she turns you on, I should turn you on too, right?"
            p "Physically, for sure. I mean, if you weren't my [mr], then-"
            scene a-192 with dissolve
            m "I see that you're always smiling and jigged up physically around Nyx. Physcially, it should be the same for me too, right?"
            scene a-193 with dissolve
            m "Prove it to me, [p]."
            scene a-194 with vpunch
            p "Hang on, [mr], what do you mean?"
            scene a-195 with dissolve
            m "Drop your pants, young man."
            p "What are you saying?!"
            scene a-196 with dissolve
            m "It's nothing we haven't seen many times before. Don't make me say it twice, [p]!"
            scene a-197 with dissolve
            p "...fine. Alright."
            scene a-198 with dissolve
            $ renpy.pause()
            scene a-200 with dissolve
            m "(Oh my god...)"
            scene a-201 with dissolve
            m "(He has such a good size! It's just like when I saw him and Nicole having sex in the living room...)"
            scene a-202 with dissolve
            m "(...the strength and virility of a young man.)"
            m "(I want it... all to myself.)"
            p "I'm sorry you have to see this [mr], I'm a guy after all. Sometimes I can't help it."
            p "Err, [mr]?"
            scene a-203 with dissolve
            "Wordlessly, she dropped to her knees and approached my member gingerly."
            m "It... looks a bit tense, [p]. I'm sorry for doing this to you."
            p "N-not a problem... [mr]."
            scene a-204 with dissolve
            m "Won't you... let me help you with... that?"
            m "After all, it's just-"
            m "..."
            m "...been so long since I- since I...."
            scene a-205 with dissolve
            "For some reason, I did nothing as her hands delicately glided across my shaft."
            m "D-does this make it feel better?"
            p "Ahhh..."
            scene a-206 with dissolve
            m "I, I don't know what I'm doing, sorry. It's just been too long."
            p "No... [mr]?"
            scene a-207 with dissolve
            $ renpy.pause()
            # focus on amanda's face
            p "Please... go on."
            # Smile
            scene a-208 with dissolve
            $ renpy.pause()
            m "I'm glad, [p]. Let me help you unload that stress~"
            # sex scene
            image a1 = Movie(play="/animations/a1.mp4")
            scene a1 with dissolve
            p "Urgh, [mr], I-"
            m "Shh... [p]..."
            m "Just relax, and let [mr] do the work~"
            m "After all, this is what a girlfriend would do..."
            "She gripped my shaft and twisted as her hand travelled up and down."
            "It was as though she was making love to my cock with her hand."
            "Caressing it, milking it, savouring the feeling of a warm rod in her hands."
            m "Do you want [mr] to go faster, [p]? Will it help you feel better?"
            p "Ah-"
            m "Let's go faster, hmm?"
            image a2 = Movie(play="/animations/a2.mp4")
            scene a2 with dissolve
            "Her speed increased and her grip over my shaft tightened like a vice, forcing me closer to the edge."
            "In this moment, she was in control of me."
            m "Are you close, [p]? I hope I'm making you feel really good~"
            p "At this rate, [mr], I'm going to cum!"
            p "Stay back, I'll hit your clothes!"
            p "Ah!"
            scene a-209 with flash
            $ renpy.pause()
            scene a-210 with flash
            $ renpy.pause()
            scene a-211 with flash
            $ renpy.pause()
            m "I leaned back, but it still covered me..."
            m "This is what it feels like... I remember now..."
            p "Wow, [mr], wow. We just crossed a line into depravity."
            scene a-212 with dissolve
            m "Any regrets?"
            menu:
                "Yes":
                    p "I don't know. We will never be able to go back."
                    p "What will this mean for us?"
                "No":
                    $ depravity += 1
                    p "No. To tell you the truth, it's been something I wanted to do."
            scene a-213 with dissolve
            m "I don't know, this is new territory for me."
            p "Me too! What about you? Any regrets?"
            scene a-214 with dissolve
            m "..."
            scene a-215 with dissolve
            m "I felt like woman today, [p]. You made me feel like a true woman again."
            m "Like you said, it took crossing the line over into depravity to do that."
            p "I think there are still a few more lines left to cross."
            scene a-216 with dissolve
            m "You know, I don't know how I feel about that. What we did today was... special, but sometimes when we give in to our temptations, things don't work out."
            p "..."
            m "If we go any further, we'll never be able to go back. I don't think I'm ready for that."
            "Fuck, my [mr] was so eager to blow me and now she's having second thoughts?"
            "It feels bad, being rejected by my own [mr]."
            p "Yeah, I got something to do anyway, [mr]. It's getting late."
            scene a-213 with dissolve
            m "We'll talk again later."
            scene black with fade
            "Wow, what a day. What a day indeed."
            $ amandalvl += 1
            call daykeep from _call_daykeep_43
            call daykeep from _call_daykeep_44
            jump hallway
        if amandalvl == 14:
            scene black with fade
            play music "sounds/wisteria.mp3" fadeout 1
            scene a-114 with fade
            p "Hey, [mr]."
            scene a-124 with dissolve
            m "Oh, [p], it's you."
            "It's me?"
            p "So how has your day been?"
            scene a-126 with dissolve
            m "Well, it just started, so there's nothing really exciting going on."
            scene a-127 with dissolve
            "This is awkward. Who's going to address the elephant in the room?"
            p "..."
            m "..."
            p "Um, [mr]? I was thinking about what happened the other-"
            scene a-123 with dissolve
            m "Wait-let me just say something first."
            m "I was also thinking, [p], and I am sorry for what happened. Let's put this behind us and forget everything."
            p "What? But you were the one who-!"
            scene a-125 with dissolve
            m "It was my bad! I fell prey to my temptations but it won't happen again, I promise. I don't want to talk about it anymore."
            m "That day never existed."
            p "..."
            scene a-126 with dissolve
            m "I think I should go back to work now."
            p "...very well."
            scene black with fade
            "Fuck, this is so embarrassing!"
            $ amandalvl += 1
            jump studio_lobby
        if amandalvl == 18:
            "The aphrodisiac, I can't wait to try it on [mr]."
            play music "sounds/alchemy.mp3" fadeout 1
            scene a-17 with dissolve
            v "You look like you're in a bit of a rush, [p]!"
            p "I'm seeing Amanda, Vincent."
            v "Must be an emergency."
            p "Erm, not really. What's up?"
            scene a-19_1 with dissolve
            v "Huh? It just looks like you've got something to do. You're giving off those vibes, bro."
            p "Watcha goin' to do with your [mr]?"
            "Damn, is my depravity so plain to see?"
            p "I'm... in no more of a rush than I usually am."
            scene a-19 with dissolve
            v "Mate, I'm just shit talking. Don't let me hold you back, haha."
            p "Oh. Right."
            scene a-18 with dissolve
            v "You okay man? You're looking a bit anxious."
            p "Me?"
            "I have no idea what I'm about to do. Should I reconsider what I'm going to-"
            v "Yeah, [p], you. What's going on, brother?"
            "Oh my god, what am I thinking. Was I really about to try and use the aphrodisiac for [mr] to have sex with me?"
            "This can't be right... can it?"
            menu:
                "There's nothing wrong.":
                    $ depravity += 1
                    "It's going to be fine. She wants it anyway. She just doesn't know it yet."
                    p "There's nothing going on Vince."
                "There's something wrong.":
                    "There's something wrong with the picture here."
                    "Was I always like this?"
                    p "You're onto something Vincent."
                    p "There's something I'm apprehensive about."
                    "I think at the end of it, this is what [mr] really wants. That's why she wanted to see my penis in the first place."
                    "She wants us to be together, but she just can't get through those boundaries she puts around herself."
                    "It might seem wrong, but I think this is the right thing to do."
                    p "There's nothing you can do for me now."
            scene a-19_1 with dissolve
            v "If you say so man."
            v "Just let me know if you need someone to talk to, alright?"
            scene a-17 with dissolve
            v "Just like old times!"
            p "Thanks."
            scene black with fade
            "Sometimes when you do something you're not supposed to, you become extra self-concious."
            "I need to calm down, or this might not go smoothly at all."
            "Breathe in.... breathe out..."
            play music "sounds/cinematic.mp3" fadeout 1
            scene a-285 with fade
            p "Hello, [mr]."
            m "Good to see you, [p]."
            m "Are you here to do a job or something?"
            m "How is Dante Studios treating you?"
            scene a-286 with dissolve
            p "I'm not here for that, [mr]. I'm here for something else."
            p "There's something I want to show you."
            m "Something to show me? Oh, I'm excited to see!"
            scene a-287 with dissolve
            p "I'm glad you think so. But first, you need to uh, go over to that corner and turn around, and don't look until I say so."
            scene a-288 with dissolve
            m "Turn around? Don't be silly, [p]! You can just show me here!"
            p "Please, [mr], for this to work, you need to turn around."
            scene a-289 with dissolve
            m "You're acting strangely, [p], is this some sort of prank?"
            scene a-290 with hpunch
            "Oh what am I thinking? I don't even have confidence that this aphrodisiac will work!"
            "What if Nyx and Maya are just pretending?"
            scene a-291 with dissolve
            "Oh my god. Don't tell me they're playing me, and just putting tension between me and [mr]."
            "This might end up just a dumb prank - with me being the fool."
            scene a-292 with dissolve
            p "P-prank?"
            "No! It's too late, I've gone all in so far. Nothing ventured, nothing gained."
            p "Look [mr], you'll understand when you see."
            scene a-293 with dissolve
            m "This isn't about what we agreed to not talk about, is it?"
            p "..."
            scene a-294 with dissolve
            m "Well is it?"
            p "It's not, [mr]. This is not that. It's different okay?"
            m "...okay."
            scene a-295 with fade
            m "I'm facing the corner now and can't see you. You can do your magic trick now."
            "Oh but Amanda, if only you knew what kind of magic trick this was."
            # fap
            play music "sounds/alchemy.mp3" fadeout 1
            scene a-296 with dissolve
            "Just let me slowly pull my dick out..."
            "Apply the lotion, and..."
            scene a-297 with dissolve
            p "{i}Fap fap fap fap{/i}"
            scene a-298 with dissolve
            p "{i}Fap fap fap fap{/i}"
            m "Hey, what is that sound?"
            "Aww fuck I'm definitely all in now. This had better work!!"
            "But I need to get 100 percent hard first."
            scene a-299 with dissolve
            p "Almost ready, just hang on."
            scene a-300 with dissolve
            "Fuck think of something sexy! I'm picturing..."
            scene a-301 with dissolve
            "You, [mr], with your sexy curves and voluptuous tits."
            scene a-302 with dissolve
            $ renpy.pause()
            scene a-303 with dissolve
            $ renpy.pause()
            "That ass, oh with those wide, child-bearing hips."
            "Oh yes, oh yes."
            p "Ah, [mr]... you can... turn around now."
            # turn
            scene a-304 with dissolve
            m "What's the big-"
            play music "sounds/hamilton.mp3"
            scene a-305 with hpunch
            m "WHAT THE FUCK?!"
            scene a-306 with dissolve
            m "What are you doing young man?!"
            scene a-307 with vpunch
            p "It-it's not working?!"
            scene a-308 with hpunch
            m "What's not working? What exactly are you planning to do here, [p]!"
            "Oh fuck I fucked up hard."
            m "Why are you showing me your-"
            stop music fadeout 1
            scene a-309 with dissolve
            m "...dick?"
            play music "sounds/kiss.mp3" fadeout 1
            scene a-310 with dissolve
            m "That juicy, thick, manly dick..."
            p "Eh?"
            scene a-311 with dissolve
            m "What... is going on... I feel hot... thirsty..."
            scene a-312 with dissolve
            "Phew, the aphrodisiac is working. But remember what Nyx and Maya said..."
            "If [mr] cums, the aphrodisiac will stop working. But until then, the aphrodisiac effect will kick in whenever I whip out my cock."
            scene a-313 with dissolve
            p "What are you after, [mr]?"
            scene a-314 with dissolve
            m "I'm after your cock, [p], and I just-"
            scene a-315 with dissolve
            m "..."
            scene a-316 with dissolve
            m "I just want to have a small taste... just a small one..."
            scene a-317 with dissolve
            "She crept towards me with a glazed eyes that could only see one thing: cock."
            "Back when Nyx and Maya were affected by the aphrodisiac, they chose to make up with each other instead of me."
            "This means that they don't 100 percent lose control of themselves."
            "Based on [mr]'s worship of my cock, does this mean that she's got part of her that desperately wants to be fucked?"
            scene a-318 with dissolve
            m "Mmmm..."
            "I can't communicate with her anymore, she's completely infactuated."
            m "May, I? Just like last time, but this time, I'll make you feel good with my mouth..."
            scene a-319 with dissolve
            m "I... really want it in my mouth~"
            "Her tongue was already outside her mouth, as she was already acting out what was on her mind."
            scene a-320 with dissolve
            m "I can't wait anymore~"
            m "C-can I? Please?"
            p "Err..."
            m "I can't wait!"
            # BJ
            image a3 = Movie(play="/animations/a3.mp4")
            scene a3 with dissolve
            p "Oh fuck!"
            $ renpy.pause()
            "Without any warning, she thrust herself onto me, enveloping my cock in the velvety smooth textures of her mouth."
            "While her flesh covered every part of my cock, her tongue carressed me from underneath."
            m "Mmm...mmm...mmm...mmm..."
            image a4 = Movie(play="/animations/a4.mp4")
            scene a4 with dissolve
            $ renpy.pause()
            "Seeing [mr] on all fours sucking my dick was a sight to behold indeed."
            "To see her below me, to see her servicing me."
            "Wordless. Just here to satsify me and satiate her own desire for cock."
            "Nothing but the sound of her rhythmic moaning and lust and the perverted sounds coming from her mouth."
            image a5 = Movie(play="/animations/a5.mp4")
            scene a5 with dissolve
            $ renpy.pause()
            "With her eyes still closed, she sped up her rhythm, reaching further, deeper."
            p "You're going really deep [mr]. You're really well practised, despite not having a man for years."
            p "You must have practised on a dildo at home or something. Who were you imagining you were blowing?"
            m "Mm~"
            p "Was it me?"
            image a6 = Movie(play="/animations/a6.mp4")
            scene a6 with dissolve
            $ renpy.pause()
            "She did not reply, but continued her pace."
            "My [mr] is such a beautiful and sexy woman."
            "Her mouth feels like heaven, and look at those fat tits swinging back and forth!"
            image a7 = Movie(play="/animations/a7.mp4")
            scene a7 with dissolve
            $ renpy.pause()
            "Her eyes were still closed. She was completely entranced in the sensation of my cock in her mouth."
            "She explored every groove, ridge and bump."
            "Her tongue swept through every spot of my dick and then re-explored them again, as if she had forgotten."
            "Continuously familiarising herself with my cock."
            "I can see why she keeps her eyes closed - she was completely in love with the way my cock felt."
            image a8 = Movie(play="/animations/a8.mp4")
            scene a8 with dissolve
            $ renpy.pause()
            "Finally, she opens her eyes."
            m "Are you ready to cum now, [p]?"
            p "Yes, fuck, yes..."
            m "Then cum all over [mr]!"
            "She was ready to finish the job."
            p "Argh!!!"
            scene a-321 with flash
            $ renpy.pause()
            scene a-322 with flash
            $ renpy.pause()
            scene a-323 with flash
            $ renpy.pause()
            scene a-324 with flash
            $ renpy.pause()
            scene a-325 with flash
            $ renpy.pause()
            scene a-326 with dissolve
            m "Ah~ the sperm is all over my face, and for some reason I feel even hotter than before~!"
            "Oh shit, this was what Nyx had experienced too! But if I put my pants back on, maybe the effect will die down."
            m "Oh [p], I feel-"
            scene a-327 with dissolve
            m "Better?"
            p "Hello [mr]. You blew me, and you did a great job."
            scene a-328 with dissolve
            m "I-I couldn't control myself! I am truly a wicked, depraved woman!"
            p "No no no, what just happened was great. Don't you understand, [mr]?"
            p "We can do this, and still go back to being normal, whatever that means."
            p "We should be allowed to live and love."
            scene a-329 with dissolve
            m "These things are just... physical, [p]. And it was a physical temptation that overcame me."
            p "But we love each other too! We tell each other all time!"
            scene a-330 with dissolve
            m "This is in a different way."
            m "We have to pretend this never happened, yes."
            p "That's what you said last time."
            scene a-331 with dissolve
            m "I don't know how to deal with this."
            m "I just... want to go back to how things were."
            scene a-332 with dissolve
            m "..."
            scene a-333 with dissolve
            m "Thanks for visiting me, [p], but [mr] has got some work to do. I'll see you back at home, alright?"
            p "..."
            "Just like that, she surpresses it."
            p "Alright [mr], keep it tight."
            m "Thanks."
            scene black with fade
            "When she looks at me, how does she see me? I really think she sees me as something more."
            "She just needs some convincing... right?"
            "But I can't forget... if she orgasms, the aphrodisiac will wear off."
            "This means the aphrodisiac will only let me have sex with her once."
            "Once it wears off... will she go back to her boundaries, or will she stay open to me?"
            # end
            scene splash_amanda with fade
            d "Find out next time, on Depravity."
            scene black with fade
            $ amandalvl += 1
            call daykeep from _call_daykeep_45
            jump map
            if amandalvl == 20:
                p "Hey [mr]."
                m "[p]! I- um, I'm sorry-"
                m "I'm just a bit frazzled, I-I-I wasn't expecting you and uh-"
                p "It's alright, [mr], I'm a little bit like that too, but there's something important we have to do."
                p "We need to talk, [mr]!"
                m "...what do you wish to talk about?"
                p "About what happened the other day, about what how we... loved each other."
                m "Oh, but [p]... you know how I feel about it."
                p "So let's talk about it, please. It's because I understand it now."
                p "I just want to be honest."
                m "..."
                m "That day, I'm not sure what overcame me. I acted purely on my impulse, [p]."
                m "I felt a burning desire, and I acted on it. I felt... an attraction."
                m "The kind that a woman feels for a man. After all... it's been so long since my husband."
                m "Can you understand where I'm coming from?"
                p "It's a mutual thing, [mr]."
                m "I'm sorry to have done this to you."
                p "No, that- it's not your fault."
                p "It... it was mine."
                p "It might sound stupid, but I put an aphrodisiac on my penis. I was told it would work. To be honest, I wasn't sure."
                p "It's dumb, huh? It as all me."
                p "But, it was because I really believed there's something between us, I know it!"
                m "You would go that far, [p]?"
                p "..."
                m "You... like me back?"
                p "I..."
                p "You couldn't help yourself, [mr], but back then, I couldn't help myself either."
                p "I wanted it to happen real bad."
                m "(I think I might too...)"
                m "Oh, it's not your fault, [p], you couldn't help yourself. How could you, that means your [mr] has still got it, huh?"
                p "Ah, haha."
                m "But, how do we know if any of this is... natural? All this could be fake, just because of the aphrodisiac."
                p "I didn't use it the day when we had the photoshoot with Nyx and Maya. Back then, that was really you."
                p "And I was devastated afterwards, I really wanted it to continue, and I was selfish."
                p "Anyway, I said my bit."
                m "..."
                m "I feel happier already, [p]. Thank you for being honest with me."
                p "So, what now?"
                m "What now? We just go about it naturally."
                p "What does that mean?"
                m "It means we put this behind us, and whatever happens, happens."
                p "But the aphrodisiac, there's something about it which you should know, it's-"
                m "Come on, [p], did you really think there is such thing as a working aphrodisiac?"
                p "Huh?"
                p "Hang on, does this mean..."
                m "Thank you for visiting today, [p], you've helped me learn something."
                m "I've got to get back to work now!"
                p "Oh, okay, no problem. Seeya [mr]!"
                scene black with fade
                "Hmm..."
                $ amandalvl += 1
                call daykeep
                jump map

        else:
            v "Ooh, Amanda isn't available right now."
            v "Try again later!"
            jump studio_lobby
