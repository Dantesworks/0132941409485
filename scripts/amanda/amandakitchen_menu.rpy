label amandakitchen:
    call hidescreens from _call_hidescreens_5
    if amandalvl == 2 and amandakitchenlvl == 1:
        scene black
        scene ak-1 with fade
        play music "sounds/wisteria.mp3" fadeout 1
        p "Hi [mr]!"
        p "How was work today?"
        scene ak-2
        m "It was challenging."
        m "Modelling is more than just good looks, you know!"
        p "Challenging?"
        scene ak-3
        m "Well, it's actually quite difficult to get on top."
        scene ak-6 with dissolve
        m "There are so many girls, since modelling is so glamorous."
        scene ak-7 with dissolve
        p "I'm sure you can beat them all out [mr]!"
        p "I believe in you!"
        scene ak-8
        m "If only there was a way to get more popular..."
        scene ak-9
        m "The income isn't as good as it used to be."
        "No wonder I get such shitty pocket money..."
        scene ak-10
        m "Oh, and there I go, bothering you with my troubles again."
        p "It's not problem at all, [mr]."
        p "I'm always here to listen."
        scene ak-7
        m "I love you [p]."
        scene ak-11 with dissolve
        m "Muah!"
        scene ak-12
        "I'm so lucky to have such a lovely [mr]."
        $ amandakitchenlvl += 1
        jump kitchen
    if amandalvl == 3 and amandakitchenlvl == 2:
        scene black
        scene ak-1 with fade
        play music "sounds/wisteria.mp3" fadeout 1
        p "How was work today?"
        scene ak-2
        m "It was great!"
        scene ak-8 with dissolve
        m "Well, it doesn't pay very well, but I got to take home a few freebies..."
        p "Hey?"
        scene ak-7
        m "I got to keep some of the outfits that I wore today!"
        p "Awesome."
        p "That's... real cool."
        scene ak-10
        m "You boys would never understand."
        p "No, no, I get it sometimes [mr]."
        p "This one time Nicole picked out some clothes for me, and that was pretty cool."
        p "It was fun. What a fun day that was."
        "Indeed..."
        scene ak-6
        m "Did she really?"
        scene ak-7 with dissolve
        m "I remember! You went clothes shopping with your [sr] and Nicole."
        m "I'm sure you enjoyed yourself very much~"
        p "Yeah, I got to meet Nicole and everything."
        scene ak-12 with dissolve
        m "Did you get to know her {i}well{/i}?"
        p "Well, sort of?"
        "Where is she going with this?"
        m "And Kaira, how was she?"
        p "Like you said [mr], she's grown a lot, haha!"
        p "Can barely believe she's the same girl, christ."
        scene ak-6
        m "She's a woman now, [p]."
        p "It's hard to believe sometimes."
        p "She had me pick out outfits as well, it was some sort of competition between her and Nicole."
        p "I had to pick out who wore their outfits the best."
        p "Was crazy hard."
        scene ak-7
        m "Sounds like you've got some experience."
        m "Come, let me show you what I picked up at work today."
        m "Let me know what you think."
        p "I guess I can make a few comments."
        scene ak-12
        m "I hope you're as excited as I am to show you!"
        p "Oh I am! Lead the way."
        ## Transition to bedroom
        scene black with fade
        scene a-4 with fade
        m "Like I said, it's not a usual thing, to be able to take the outfit home."
        p "Why'd they let you keep it?"
        scene a-5
        m "I'm not sure, but I'm not going to say no."
        p "It must have been because you looked so good in it!"
        scene a-6
        m "I think so!"
        m "Lets see what you think."
        m "Turn around and close your eyes."
        m "I'm going to slip it on."
        p "Looking forward to it."
        ## Turn around
        scene ae-2 with fade
        "..."
        "I wonder what outfit [mr] is going to wear."
        m "Hmm~hmm~♫"
        "..."
        p "Are you done yet?"
        m "Just a moment, sweetie, good things take time!"
        p "Are you putting it on?"
        m "I'm just about to, hang on."
        menu:
            "Wait for [mr] to put on her outfit.":
                "I'll get to see soon enough."
                "..."
            "Sneak a peek.":
                $ depravity += 1
                "Hehe, what's the harm?"
                scene ae-1 with fade
                "Oh"
                "My"
                "God"
                "..."
                "I've never seen [mr] like this before."
                "She's got her top off, and her breasts are in full display."
                "No wonder Kaira is jealous..."
                "Definitely model material... how on earth is she still single?"
                "..."
                "I shouldn't stare too long..."
                scene ae-2 with fade
                "..."
        m "You can turn around now, [p]."
        play music "sounds/masked.mp3" fadeout 1
        scene amanda3 with fade:
            pos (0.0, -3.22)
            linear 6 pos (0.0, 0.0)
        $ renpy.pause(6.0,hard=True)
        $ renpy.pause ()
        scene ae-3
        m "You're... not saying anything."
        m "You don't like it?"
        p "This... is what you model in?"
        scene ae-4 with dissolve
        m "..."
        m "Yes. Is there... something wrong?"
        p "..."
        p "There's nothing wrong."
        p "You look amazing [mr]."
        p "It wasn't what I was expecting, but it makes sense."
        scene ae-5 with dissolve
        m "What makes sense?"
        p "It's a little awkward to say, since you're my [mr] at all."
        scene ae-6 with dissolve
        m "It's okay, what is it?"
        p "Well, of course.."
        p "You're incredibly good looking, [mr]. And of course people are going to appreciate that."
        p "That's why you're a model after all."
        p "Damn, [mr], just damn!"
        scene ae-7
        m "Not the kind of modelling you were expecting, huh?"
        p "You're one... sexy woman."
        m "Fufufu~"
        scene ae-8
        m "All that to tell me something I already know?"
        p "Well, kinda caught me off guard."
        scene ae-9
        m "Why don't you tell me what you think about this outfit?"
        p "Alright, let's see a few poses!"
        scene ae-10
        m "You sound like the photographer."
        scene ae-11 with dissolve
        $ renpy.pause()
        scene ae-12 with dissolve
        $ renpy.pause()
        scene ae-13 with dissolve
        $ renpy.pause()
        scene ae-14 with dissolve
        $ renpy.pause()
        scene ae-15
        m "Well?"
        p "I think it looks as good as the woman wearing it."
        scene ae-16
        m "Which is to say?"
        p "You already know the answer. It's great."
        p "I feel like you could earn a lot of money doing this."
        scene ae-17
        m "People seem to always think so, but there are a lot of pretty girls out there."
        m "Getting your name out there is hard."
        p "You just need your big breakout"
        scene ae-18 with dissolve
        m "..."
        scene ae-19 with dissolve
        m "Why don't you come sit down?"
        m "It's been a long time since you've had a long chat with your [mr]."
        scene ae-20 with fade
        m "How are things going with you?"
        p "It's going much better than it used to be."
        p "Time really makes things better."
        p "I felt like I was in a vortex before, being sucked into chaos."
        scene ae-21
        m "It's good that you don't feel that way anymore."
        p "Well, in a way, I still feel like the chaos is still there."
        p "But I feel like I can come to terms with it. At the end of it, I might come out stronger."
        scene ae-22
        m "That's a mature perspective."
        m "You've really grown too, haven't you?"
        m "No longer the boy that left home."
        scene ae-23 with dissolve
        m "You've come back as a man."
        p "..."
        p "And how about you, [mr]?"
        scene ae-25 with dissolve
        m "To be honest, the modelling business is hard."
        m "There's a lot of girls out there - a lot of competition."
        m "The agency is putting more attention into the other girls, and I'm not getting as many photos as I used to."
        p "That's their mistake."
        p "Don't let it get you down, [mr]."
        scene ae-24
        m "Thank you, [p]."
        m "Look at me, being all negative!"
        m "Thanks for being here."
        m "Someone for me to talk to."
        p "No worries, [mr]. I'm very happy to help in any way."
        scene ae-26 with dissolve
        "I've never seen [mr] like this, I really want to just hold her..."
        scene ae-27 with dissolve
        m "(He's such a kind man...is that why I'm getting these feelings again?)"
        scene ae-28 with dissolve
        m "..."
        p "..."
        m "It's been a while, [p]."
        p "It really has."
        scene ae-29 with fade
        $ renpy.pause()
        m "It's... getting late, isn't it?"
        p "...You're right, I should probably go."
        m "Goodnight, [p]."
        p "See you tomorrow, [mr]."
        $ amandakitchenlvl += 1
        call daykeep from _call_daykeep_7
        jump hallway
    if amandalvl == 4 and amandakitchenlvl == 3:
        scene black
        scene ak-4 with fade
        play music "sounds/wisteria.mp3" fadeout 1
        p "Good to see you, [mr]."
        p "How did work go today?"
        scene ak-3 with dissolve
        m "It was... alright."
        "She doesn't seem too cheerful."
        "I wonder what's gone wrong."
        p "You don't sound like your usual self."
        m "..."
        scene ak-4
        m "Oh [p], I just don't know what to do."
        p "You can tell me, [mr]."
        m "{i}Sigh{/i}"
        scene ak-6 with dissolve
        m "I don't think people want to see me anymore."
        m "My hours are getting cut; the photographer is spending less time with me; soon I might not even have a job!"
        m "What am I going to do?"
        scene ak-9 with dissolve
        m "Am I losing my touch?"
        m "For a while, I felt like I had things under control."
        m "Am I only worth how I look like?"
        p "Don't say that!"
        p "It's not true."
        p "You don't even know if you'll lose the job yet."
        scene ak-6 with dissolve
        m "Let's not kid ourselves, [p]. This has been happening for a while now."
        m "I'm getting old. People just don't like to see me anymore."
        m "It's the way the industry is."
        "God I just can't bear to see her like this."
        p "Hey, look."
        p "I think I've been through this before, and you were there for me [mr]."
        p "When I lost everything, I could count on you guys."
        p "I guess what I'm trying to say is..."
        p "No matter what happens, I'll be here."
        p "I'll help you out. I promise."
        scene ak-10
        m "I'm bothering you with my troubles again!"
        p "Please don't say that!"
        p "You're still beautiful [mr], don't let anyone tell you otherwise!"
        p "Like I said, you just need the breakout."
        p "Heck, we don't even need the photographers and everything!"
        p "Anyone can take photos!"
        scene ak-9 with dissolve
        m "Oh [p] I really appreciate it, but it's the agency. I don't have the contacts or the means."
        p "Fuck em'."
        p "We'll figure something out."
        p "It's the age of the internet. I'm sure we can market your modelling pictures somewhere."
        p "Leave it to me."
        scene ak-6
        m "..."
        m "Don't put this onto yourself, if you-"
        p "I'm not, [mr]. Come on!"
        p "You've got the looks already, this makes the rest easy!"
        scene ak-7
        m "Fufu~"
        m "You always know how to cheer me up."
        scene ak-12 with dissolve
        p "Haha, take care in the meantime."
        "If [mr] loses her job, I'll need a camera at the very least to continue taking shots."
        "It won't be cheap, but it's the least I can do."
        $ amandakitchenlvl += 1
        jump hallway
    if amandalvl == 5 and amandakitchenlvl == 4:
        scene black
        scene ak-3 with fade
        play music "sounds/wisteria.mp3" fadeout 1
        p "I ask this alot, but how'd work go?"
        m "It's the same pattern. Hours are getting shorter and shorter."
        m "I'm not sure how sustainable it will be in the future."
        scene ak-1 with dissolve
        m "I had a think about this plan of yours though."
        p "Really? What did you think?"
        scene ak-7 with dissolve
        m "Well, I spoke to one of my friends in the industry, and she told me a few things that we need."
        m "We need to have some sort of camera to start off with, and we need to advertise ourselves."
        p "Easy, right?"
        scene ak-6
        m "I'd like to think so, but those are two things that I don't have access to."
        m "I don't know how to work a camera, or even how to choose one. On top of that, how can I advertise myself?"
        m "That's what the agency is supposed to be for, and they don't even want me."
        p "Leave it all to me, I'll figure something out."
        p "I can source a camera, no worries. I did a little bit of photography in university."
        p "As for the marketing, posting it on websites and stuff will do, but I'll ask around. We can build it up slowly."
        p "I'm confident that once we get you out there, your pictures will do the rest."
        scene ak-10
        m "Are you sure, [p]?"
        p "I'm confident."
        p "Just keep working as you are. I'll let you know when I've got a camera, and we can start there."
        scene ak-7
        m "Thank you so much."
        p "No worries, [mr]. You did the same for me."
        $ amandakitchenlvl += 1
        jump hallway
    if amandalvl == 6 and amandakitchenlvl == 5:
        scene black
        scene ak-1 with fade
        play music "sounds/wisteria.mp3" fadeout 1
        p "Not too tired from work I hope?"
        scene ak-2
        m "Work is always tiring, but I've been waiting the whole day to get back home."
        m "You said you were going to take some pictures of me?"
        p "Haha, I'm a bit rusty, but yes."
        p "So, I'm not actually too knowledgeable about how photoshoots work."
        p "Do you just stand there, and then I take pictures?"
        scene ak-7 with dissolve
        m "Well usually, there's an outfit picked for me, and I do a few poses. The photographer might also instruct me to do something as well."
        p "What does the photographer tell you to do?"
        m "Specific poses, facial expressions, anything."
        p "Oh cool. What about the outfit part? I haven't really got an outfit for you, haha."
        scene ak-9
        m "Hmm, maybe I can dig through what I already own."
        m "Like I said before, its not usual that I get to take outfits home."
        p "Sounds like a plan."
        p "Let's go to your room."
        p "To be honest, I'm really new to this. I feel like you'll be giving {i}me{/i} the instructions!"
        scene ak-12
        m "Oh don't worry [p]. Look at it like we're having fun together."
        ## Transition
        scene a-9 with fade
        m "So, what do you want me to do?"
        p "Do you want to put on an outfit? Or maybe just wear the one you have now?"
        scene a-10
        m "Hmm..."
        m "What would you like me to wear?"
        p "Well..."
        p "You're wearing kind of professional looking clothes, I guess its a good place to start."
        scene a-11
        m "Oh come on, I'm not wearing what I usually wear to work."
        m "We can go with professional, but let's choose a different outfit."
        p "Okay, sure. Whatcha got?"
        scene a-6 with dissolve
        m "Turn around and close your eyes, I'll show you."
        ## Turn around
        scene ae-2 with fade
        "..."
        "So [mr]'s going with professional..."
        "I wonder if the outfit will be spicy enough to draw in an audience..."
        m "Let's see..."
        "..."
        p "Is everything okay?"
        m "Well, I'm thinking of something conservative."
        "Aww."
        menu:
            "Wait for [mr] to put on her outfit.":
                "Professional and conservative. I wonder how she'll pull it off."
                "..."
            "Sneak a peek.":
                $ depravity += 1
                "I might as well steal a look if I'm getting no treats later."
                scene ae-30 with fade
                "Mmmmmm....."
                "She is so hot, I can't believe the modelling agency doesn't want her."
                "Those lucious legs and those thighs."
                "If we can harness this potential, we could make something really big."
                "Alright [p], keep it together!"
                scene ae-2 with fade
                "..."
        m "Done!"
        play music "sounds/masked.mp3" fadeout 1
        scene amanda-1 with fade:
            pos (0.0, -3.037)
            linear 6 pos (0.0, 0.0)
        $ renpy.pause(6.0,hard=True)
        $ renpy.pause ()
        scene ae-32
        m "Classy and professional."
        m "I added the glasses for the extra touch."
        p "It looks amazing, {i}You{/i} look amazing."
        scene ae-33
        m "Do you think people would like this?"
        p "Definitely!"
        p "Tons of people dig the more reserved look with glasses."
        p "People love glasses."
        p "We could slowly build up the portfolio to have a wide range of outfits."
        p "From covered up, to you... well, you know."
        scene ae-34 with dissolve
        m "Too skimpy?"
        p "I didn't want to say it, but yeah, sex sells."
        scene ae-35
        m "Well! I don't have a wardrobe full of stripper clothes. Do you think that's appropriate for my portfolio?"
        p "Umm, I'm not talking about that level of clothing, but like, in general, I think we could go for a variety of looks."
        p "Just like at your work, right?"
        scene ae-36
        m "You can be the photographer - keep on the lookout for clothing that you'd like me to wear!"
        p "Sure thing, I'll look around."
        p "So, do you wanna get into a few poses and I'll snap a few shots?"
        scene ae-33
        m "Would you like to direct me?"
        p "You probably have more experience than me, ahha."
        p "I'll do some reading on how to take photos and direct models."
        p "In the meantime, can you go through a few standard poses?"
        scene ae-34
        m "Aww, its more fun and interesting when I get directions, but sure, I'll lead this session."
        ## Poses
        scene ae-37 with dissolve
        $ renpy.pause()
        scene ae-37 with flash
        $ renpy.pause()
        scene ae-38 with dissolve
        $ renpy.pause()
        scene ae-38 with flash
        $ renpy.pause()
        scene ae-39 with dissolve
        $ renpy.pause()
        scene ae-39 with flash
        $ renpy.pause()
        ## Poses finished
        scene ae-32 with dissolve
        p "Just absolutely stunning pictures."
        scene ae-33
        m "Looks like you got some great pictures."
        p "The pictures are only as good as the model."
        m "There you go again!"
        p "So, what can you say about this oufit?"
        scene ae-40
        m "I imagine this is what a smart casual doctor's outfit might look like."
        m "Like a sexy doctor."
        p "So you can cure things."
        p "Like this tension in my pants..."
        scene ae-35 with dissolve
        m "Sorry?"
        p "Nothing."
        scene ae-40
        m "Well, this has been a fun session, but I've got work again tomorrow."
        m "Let's get better together, and hopefully I won't have to work there anymore."
        p "I'll be your manager and your photographer."
        p "If we take off, I want some part of the cut, hehehe..."
        scene ae-34
        m "You'll have to get good at giving directions first!"
        p "Don't worry, I'll work on it."
        m "I'm counting on it."
        $ amandakitchenlvl += 1
        call daykeep from _call_daykeep_5
        jump hallway
    if amandalvl == 7 and amandakitchenlvl == 6 and (long_gown or security_dress or gym_clothes): ## Room photoshoot
        scene black
        scene ak-1 with fade
        play music "sounds/wisteria.mp3" fadeout 1
        p "Evening [mr]."
        p "Hope work was fun."
        scene ak-2
        m "It was alright! Have you spotted some nice looking clothes I should wear?"
        p "A woman like you doesn't need clothes to look nice!"
        scene ak-7 with dissolve
        m "Aww, thank you."
        "I meant that in multiple ways..."
        p "But really, I got the clothes, [mr]!"
        m "Wow, I can't wait to see what you have in mind!"
        m "Which one am I trying on today?"
        menu:
            "Long Gown" if long_gown == True and long_gown_done == False:
                $ long_gown_done = True
                call long_gown_scene from _call_long_gown_scene
            "Security Dress" if security_dress == True and security_dress_done == False:
                $ security_dress_done = True
                call security_dress_scene from _call_security_dress_scene
            "Gym Clothes" if gym_clothes == True and gym_clothes_done == False:
                $ gym_clothes_done = True
                call gym_clothes_scene from _call_gym_clothes_scene
            "Actually, I haven't bought the outfit I wanted yet.":
                jump kitchen
        $ amandakitchenlvl += 1
        call daykeep from _call_daykeep_8
        jump hallway
    if amandalvl == 8 and amandakitchenlvl == 7 and (long_gown or security_dress or gym_clothes): ## Room photoshoot 2
        scene black
        scene ak-1 with fade
        play music "sounds/wisteria.mp3" fadeout 1
        p "Hiya!"
        p "Excited for our next session?"
        scene ak-2
        m "Hello to you too, [p]."
        m "Work tires me out, but I always get energy when our sessions are about to start."
        scene ak-7 with dissolve
        m "I've been thinking all day about what you've picked for me."
        p "I hope I won't dissappoint..."
        menu:
            "Long Gown" if long_gown == True and long_gown_done == False:
                $ long_gown_done = True
                call long_gown_scene from _call_long_gown_scene_1
            "Security Dress" if security_dress == True and security_dress_done == False:
                $ security_dress_done = True
                call security_dress_scene from _call_security_dress_scene_1
            "Gym Clothes" if gym_clothes == True and gym_clothes_done == False:
                $ gym_clothes_done = True
                call gym_clothes_scene from _call_gym_clothes_scene_1
            "Actually, I haven't bought the outfit I wanted yet.":
                jump kitchen
        $ amandakitchenlvl += 1
        call daykeep from _call_daykeep_9
        jump hallway
    if amandalvl == 9 and amandakitchenlvl == 8 and (long_gown or security_dress or gym_clothes): ## Room photoshoot 3
        scene black
        scene ak-1 with fade
        play music "sounds/wisteria.mp3" fadeout 1
        p "Hello [mr]!"
        p "Today's photoshoot is gonna be important."
        scene ak-2
        p "Well, they all are, but it's our best chance to show Vincent what we've got."
        scene ak-6 with dissolve
        m "You're making me stressed out, and I do this for a living!"
        scene ak-7
        m "What's the outfit I'm going to be wearing this time?"
        menu:
            "Long Gown" if long_gown == True and long_gown_done == False:
                $ long_gown_done = True
                call long_gown_scene from _call_long_gown_scene_2
            "Security Dress" if security_dress == True and security_dress_done == False:
                $ security_dress_done = True
                call security_dress_scene from _call_security_dress_scene_2
            "Gym Clothes" if gym_clothes == True and gym_clothes_done == False:
                $ gym_clothes_done = True
                call gym_clothes_scene from _call_gym_clothes_scene_2
            "Actually, I haven't bought the outfit I wanted yet.":
                jump kitchen
        $ amandakitchenlvl += 1
        call daykeep from _call_daykeep_10
        jump hallway
    if amandalvl == 10 and amandakitchenlvl == 9:
        scene black
        scene ak-1 with fade
        play music "sounds/wisteria.mp3" fadeout 1
        p "I've got great news!"
        scene ak-2
        m "Tell me!"
        p "You know Vincent?"
        p "Well, he's actually a really influential person in the modelling world."
        p "He's said he was looking for an upcomer for the runway show at Dante Studios and-"
        scene ak-13 with vpunch
        m "No way!"
        p "It's true! And he says you can have that spot!"
        m "..!!"
        scene ak-14 with hpunch
        m "Do you know what this means!"
        m "We might actually have a shot!"
        p "I'm really happy for you [mr]. You've heard of Dante Studios?"
        m "Yes! Everybody has! They're the biggest company around, and all their models are super popular!"
        m "Are you sure I get to go on the runway?"
        p "Yeah, Vincent said you can go on at the end."
        p "What's so good about Dante Studios?"
        scene ak-6 with dissolve
        m "Everything about their productions are super high quality, from their models, to photography to everything."
        m "If I get to go on, that means they think I'm up to scratch!"
        p "They're right; you are definitely up to scratch."
        m "When is this going to be, and where?"
        p "At Dante Studios, in a few days. Can I come with you?"
        scene ak-7
        m "Of course you can, [p]! You're the reason why this is all happening."
        p "Are you going to quit your job?"
        scene ak-8 with dissolve
        m "I think it's finally time. Dante Studios' shows are in the afternoon, and I won't be able to make it to both."
        p "Wow, this is really happening, huh?"
        m "I've got to get myself ready..."
        scene ak-7
        m "Come chat to me in the morning the show is on, and we'll go there in the afternoon!"
        p "I can't wait."
        $ amandakitchenlvl += 1
        call daykeep from _call_daykeep_16
        jump kitchen
    if amandalvl == 16:
        scene black
        scene ak-1 with fade
        p "Hey [mr]."
        scene ak-2 with dissolve
        m "Hi sweetie!"
        p "Long day at work?"
        scene ak-7 with dissolve
        m "Oh it was great. I love working with the rest of the Dante Studio girls."
        p "That's nice to hear!"
        "Should I use the aphrodisiac... or not?"
        "I don't even know if it works... but if it does..."
        "Should I even try it?"
        label aphro_choice:
        menu:
            "Don't use it.":
                default wildbillvariant = False
                $ wildbillvariant = True
                "There must be another way to do this."
                m "Is something the matter, [p]?"
                p "No!"
                m "You seem a bit weird."
                p "Am I? Hahaha."
                "I think I've got a plan to do this another way."
                "I better give Nyx and Maya a visit tomorrow to tell them I've changed my mind."
                scene black with fade
                ## Wild Bill
                "The next day, at Dante studios..."
                p "Any news about work, Vincent?"
                scene a-19_1 with dissolve
                v "Work? I'll tell you what's a piece of work."
                scene a-19_2 with dissolve
                v "Those two models I swear are nagging me every 2 minutes about whether you're in or not."
                p "Nyx and Maya?"
                scene a-19_1 with dissolve
                v "Yup. How are you so popular with them anyway?"
                p "It's a good question. Though, what do they want?"
                v "Beats me, and as you can tell, they certainly keep it secret from me."
                p "Ah."
                scene a-232 with hpunch
                ny "[p]! How did it go? We have to talk!"
                v "Can I stay here this time? Or will you get me to leave again?"
                ma "You can stay Vincent, because we're going to one of the studios to talk instead."
                scene a-220 with dissolve
                v "Bah."
                ny "It won't be too long, [p], come!"
                # transition
                scene black with fade
                play music "sounds/witch.mp3" fadeout 1
                scene a-275 with fade
                ny "Well? Did it work on Amanda?"
                p "I didn't get a chance to, unfortunately."
                scene a-276 with dissolve
                ny "What?"
                p "I wanted to, but... I had a change of heart."
                scene a-277 with dissolve
                ma "I think that may be have been for the better - but not in the way you think."
                p "How so?"
                ma "Remember how horny we were when you left us? That effect is only 100 percent activated when a penis is around."
                ma "But even without a penis present, the sightly weaker effect can still supposedly last weeks to months - until a certain something happens, we learned."
                p "What has to happen for it to go away?"
                scene a-278 with dissolve
                ny "An orgasm."
                ny "Once Maya and I reached her blissful climaxes, our lust rapidly subsided."
                p "Good to know."
                scene a-279 with dissolve
                ma "We're telling you this because we thought it would be useful for you to know that once you made Amanda cum, she'll lose that lust."
                p "That's fine. I don't think I'll use it anyway."
                scene a-280 with dissolve
                ny "..."
                ma "..."
                p "..."
                scene a-281 with dissolve
                ny "I'm saying, you can reconsider. That was our last bottle of aphrodisiac, you know."
                ny "We really hope it gets put to good use."
                p "Thanks for that, but I have another way that I'm going to go about this."
                scene a-282 with dissolve
                ma "Another way? What do you mean?"
                p "I don't need no aphrodisiac. Just let me make a few calls. You'll get me later."
                scene a-283 with dissolve
                ma "Look at his confidence, Nyx. Maybe he might pull it off after all."
                scene a-284 with dissolve
                ny "My, my~ As long as Amanda becomes less sexualy frustrated, I think we'd all be happy."
                p "I got this."
                ny "We've got to get back to work, and I'm sure you've got something you want to do too, isn't that right~?"
                ma "Until next time, [p]."
                p "Seeya."
                scene black with fade
                "Whoa, that was some pretty confident talk from me, to some stunning super models."
                "But I think this might just work. I don't need no aphrodisiac!"
                ## Later tonight..
                "A few hours later, into the evening..."
                scene a334 with fade
                n "Couldn't get enough of me, could you?"
                p "Oh yeah."
                n "Do you remember when we did it in this very room?"
                n "It was the first day I met you."
                scene a335 with dissolve
                p "Oof, if you put it like that, it sounds pretty slutty."
                n "It's how I am~"
                scene a336 with dissolve
                p "I'm glad to hear that. I could use your services."
                n "I bet you could."
                n "So what would you like me to do for you, daddy?"
                scene a337 with dissolve
                p "{i}Gulp!{/i}"
                p "You see, Nicole. There's a tension, somewhere down there."
                n "Ooh! Let me play, heheh."
                scene a338 with dissolve
                n "Is it... here?"
                scene a339 with dissolve
                "She gestures at my abdomen."
                scene a340 with dissolve
                p "Not quite, I feel like it's... lower down."
                n "Ooh, I think I know what you mean, hehe~"
                n "How about... here?"
                scene a341 with dissolve
                $ renpy.pause()
                p "I'd say you're on the money."
                n "Well then, let's see..."
                scene a342 with fade
                "Her well practised hand whipped my cock out."
                n "You {i}do{/i} have a tension."
                scene a343 with dissolve
                n "Jokes aside, I could see a tent in your pants the moment I sat down here with you."
                scene a344 with dissolve
                n "You horny, horny, boy~!"
                p "Oh come on. This is your fault. It's your special ability."
                scene a345 with dissolve
                n "My ability? To give guys around me instant boners?"
                n "Hahaha!"
                n "What about you? What's your power?"
                scene a346 with dissolve
                p "My power is to be able to keep up with a sex kitten like you."
                p "Now... we better get started or she'll get-"
                scene a347 with dissolve
                p "I mean..."
                scene a348 with dissolve
                n "Or what? Are we in a rush?"
                p "You talk too much Nicole. I prefer you with your mouth full."
                scene a349 with dissolve
                n "As you wish~"
                # BJ
                image a13 = Movie(play="/animations/a13.webm")
                scene a13 with dissolve
                n "Mmm, mmm, mmm, mmm."
                "I can't get over how good she is at this. How is she even going out with me?"
                "Her mouth felt like a pussy, the walls warm and moist."
                "She sucked as she went up and down my shaft."
                "Meanwhile, her tongue swirled around the head of my cock, just gently."
                "She wasn't even trying hard. She was just teasing."
                "Ah fuck, but I can't afford to blow my load too quickly, not now!"
                p "Hang on Nicole-"
                scene a350 with dissolve
                p "Just slow down a tick!"
                n "Mm~!"
                scene a351 with dissolve
                $ renpy.pause()
                # Amanda walks in
                scene a352 with hpunch
                m "!!"
                m "(T-This has happened before!)"
                m "(I can't believe it...)"
                scene a353 with dissolve
                m "(I need to go... but why can't I stop watching?)"
                scene a354 with dissolve
                m "(Seeing Nicole have her way with my [p]...)"
                scene a355 with dissolve
                m "(Is this the way it's meant to be?)"
                m "(The one time I gave in to my desires, I have to hide from it and shun myself.)"
                scene a356 with dissolve
                m "(But with Nicole...)"
                m "(She gets to enjoy [p] over, over, and over again. Making me watch, just as she did before~!)"
                scene a357 with dissolve
                m "(Making me watch... [p]'s thick cock cleaned by her slutty little tongue...)"
                scene a359 with dissolve
                m "(His balls carressed... as he looks into her eyes... full of lust, love, acceptance...)"
                scene a358 with dissolve
                m "(Will someone ever look that way at me?)"
                m "..."
                scene a360 with dissolve
                m "(To look at me, as he mounts me...)"
                scene a361 with dissolve
                m "(As I grasp his rod, guiding it towards my folds...)"
                scene a362 with dissolve
                m "(I could use both my hands to hold his cock... and the tip would still be enough to sink my mouth into...)"
                scene a363 with dissolve
                m "(I'm getting hot...)"
                scene a364 with dissolve
                m "(Faster... [p]... faster~!)"
                p "I'm cumming!"
                scene a365 with hpunch
                m "!!"
                m "(I can't be found out!)"
                scene a366 with dissolve
                $ renpy.pause()
                # Amanda disappears
                scene a367 with dissolve
                $ renpy.pause()
                scene a368 with dissolve
                $ renpy.pause()
                scene a369 with dissolve
                p "Phew, that was good."
                n "I swallowed every last drop like a good little girl~!"
                scene a370 with dissolve
                p "Good one Nicole, god you're great."
                p "Hey just wondering, did you hear the door open at all?"
                scene a371 with dissolve
                n "The door there?"
                scene a372 with dissolve
                n "I was too busy sucking the juices from your penis, sir."
                scene a373 with dissolve
                n "Were you expecting someone? Come to think about it, your [mr] should be home about now."
                p "The timings a little suspicious, you think?"
                scene a374 with dissolve
                n "Maybe you're just an exhibitionist like me."
                p "Haha."
                p "Keep it tight."
                scene black with fade
                "The next day, at Dante's studios."
                scene a-16 with fade
                "The master plan is in motion."
                "I let [mr] see me fucking Nicole's mouth, just to see how she would react."
                "Nicole did perfectly, and put on a great show."
                "Time to check up on [mr]."
                scene a-17 with dissolve
                v "Yes, buddy?"
                v "Here to see your [mr]?"
                p "Hey, there's nothing wrong with that right?"
                scene a-19 with dissolve
                v "I don't know man, you seem a little bit deep in thought."
                p "Oh, nothing much. I'll see you soon, huh?"
                scene a-18 with dissolve
                v "Good to see you too."
                
                p "Hi [mr], how's it going?"
                p "Feels like ages since the last time we met... but it probably wasn't so long ago, was it?"
                m "T-The last time we met?"
                # flash back
                p "Yeah, the last time. You remember?"
                m "Ah...."
                p "Uh, [mr]?"
                m "Ah, sorry, I... got distracted by something."
                p "Really? What's on your mind?"
                m "What's... on my mind?"
                p "Yeah, what are you thinking?"
                m "I was thinking of... juicy... hotdogs."
                p "Haha, juicy hotdogs? What on earth made you think of that?"
                m "What? I, uh-"
                m "Hang on, why are you so curious, [p]?"
                m "Your [mr] needs to do some more photo shoots."
                p "Fair enough, [mr]. I'm just having some fun."
                m "I'll head off now, [p]."
                p "Take care, [mr]."
                # nyx and maya come in
                ny "Hey, [p]!"
                p "Nyx!"
                ny "What exactly was your plan? Amanda has been super sexually frustrated today."
                ny "When Maya gets that way, the only solution is to eat her out, right Maya?"
                ma "Nyx..."
                ny "You're so cute."
                ny "You think Amanda would let me eat her out?"
                ma "Maybe if we didn't give the last bit of aphrodisiac to [p], we could have used it on Amanda."
                ny "She is far too lusty. Poor girl is barely concentrating at work."
                ny "And her hands, Maya, did you see them stray towards her pussy?"
                ma "I try not to look."
                p "Ladies, ladies!"
                p "I'm sorry your aphrodisiac didn't get used, okay?"
                p "And also, that's my [mr] you're talking about!"
                ma "I'm sorry about Nyx, [p]. You know how forward she can be."
                ma "I suppose you don't have to tell us, but what did you do?"
                ny "You must have done something. Amanda is so hot she's going insane."
                p "You could say I did something similar to giving an aphrodisiac."
                ma "That would explain how lustful she seems to be."
                ny "You made her that way, but you didn't satisfy her lust?"
                p "All I did was have sex with my girlfriend in front of her. I think that might have stimulated her."
                ny "Haha, I get it now. You are a cruel man, [p]!"
                ma "I see. So [p]'s plan is to test Amanda and explore their boundaries. He's making her go to him."
                ny "The payoff will be slower, but it might be sweeter. But then again, all sex is very sweet already."
                ny "Isn't that right, Maya?"
                ma "Shouldn't I be asking you that? You're the one eating me out all the time..."
                ny "That's right - it's always me doing the work. Shouldn't you be having a taste of me too? See how sweet I am~"
                ma "I'll pass, Nyx. After all, I don't know what you've put up there. Or who, for that matter."
                ny "Hey~ hey~!"
                ny "How did we get side tracked? Let's talk more about [p]."
                ny "Anyway, [p], that's such a cruel idea, it's so freakin' cool."
                ny "And if you are as cool as that idea, maybe you'll be one of them that I'll 'put up there' as Maya would say~"
                ny "Maybe we could even make Amanda watch! How exciting!"
                ma "..."
                ma "I think it's time for us to go, [p]. Nyx needs to cool her imagination."
                ma "All the best, [p]."
                p "Thanks."
                "Phew. Everytime I talk to that pair, it's an adrenalin rush."
                "I hope I get to know them better one day. What an interesting couple."
                "But in the meantime, I need to prove to myself that I don't need the aphrodisiac."
                "I have to up the ante with [mr], somehow. Somehow..."
                scene black with fade
                n "You're acting so passionately recently, I love it."
                n "So, what is the reason that you've been so damn horny?"
                p "I'm just hungry for your pussy."
                n "I'm so glad to have met you."
                n "So how are we going to do it today? We have to change it up, you know."
                n "The same positions gets boring if we do it for too long~"
                p "Oh yeah? What kinky shit do you have in mind?"
                n "That stuff yesterday was quite kinky, wasn't it? Your [mr] could have walked in on us at any time."
                n "You knew that, didn't you?"
                p "It's true, she comes home in the evenings."
                n "And it's the evening now, isn't it?"
                p "Also true."
                n "Oh~  I wonder~"
                n "Does your [mr] ever get jealous of me?"
                p "Jealous?"
                n "Yeah, I mean, I get to fuck such a thick stud {i}whenever{i} I want, and all she can do is touch herself while she listens to my moans~"
                p "Whoa, that's my [mr] you're talking about, haha."
                n "Hey, I'm only joking. She's pretty hot, for her age especially."
                n "I'm sure she'd be able to find all kinds of guys to give her cock."
                n "With how she looks... even younger guys too."
                n "Guys around {i}your{/i} age. Your friends even."
                p "Nah, I don't have friends. Not likely."
                n "Oh, but you know what I mean. Your [mr] could be getting so much dick if she wanted to. Why doesn't she?"
                n "After all, cock is the best."
                p "Well, let me consult your expert opinion."
                n "Oh, finally someone cares about what's between my ears and not what's between my legs~!"
                p "You know I love you Nicole. Don't do this to me."
                n "Haha, ask away, [p], ask away."
                p "What do you think my [mr] needs to realise that she needs... you know, a guy?"
                n "You mean a cock? A hard, thick, spurting cock?"
                p "Yeah, that too."
                n "Well, she needs to know what she's missing out on."
                p "Ah, the penis yeah. But how?"
                n "Well, I've got a great idea. In fact, you probably know it too."
                p "Do tell."
                n "Haha, alright. Listen closely then. It's-"
                m "Oh, hello you two!"
                m "I just came back from work, and wow, what a day."
                p "Oh hey [mr]. Welcome home!"
                n "Miss Amanda!"
                m "I hope I didn't intrude or anything. Just pretend I'm not here, okay?"
                m "Make yourselves at home."
                n "Will do."
                m "I'm just going to pop off into the kitchen and do the standard routine."
                p "Cooking some more meat again?"
                m "Haha, not today."
                n "No meat today, Amanda? You don't know what you're missing out on!"
                m "Ah, hahaha. Alright, I'll get onto my work."
                p "Yo. Stop that."
                n "Why? She didn't think anything. I'm just having some fun."
                n "Anyway, about the idea I was talking to you about-"
                p "Uh, not now. She's literally a few feet away from us."
                n "Oh my dear [p]. That's the point~"
                p "You... I.... err...."
                n "Oh my gosh, boys can be so stupid."
                n "But then again, you {i}are{/i} more visual creatures. Let me just show you."
                "Wordlessly, she started stripping, revealing her two bolted on tits."
                # strip
                p "Psst!! Nicole!!"
                p "We don't even have the excuse of being stumbled on!"
                p "If we do it now, we're obviously spiting her!"
                p "..."
                p "Where are you going! Come back now!"
                # Nicole walks to the wall
                "Wordlessly, she gestured me over, and bent over, her butt cheeks spreading apart, inviting me into her pussy."
                m "You two are really quiet. Remember, just pretend I'm not here. I don't mind some noise."
                "Nicole smirked."
                n "Hey Amanda?"
                m "Yes Nicole?"
                n "I think something might need your attention back here..."
                p "Alright Nicole, alright!"
                "I fiercely whispered."
                n "Oh never mind. It's been sorted out~"
                m "Good!"
                n "See, [p]? You just need a little encouragement."
                n "Don't get stage fright on me now. That would be so embarassing."
                p "And what you're doing now isn't?!"
                p "Fuck me."
                n "Deal."
                p "I mean... shit."
                n "Hard yet? Enter me."
                p "Fucking hell..."
                # fuck against wall
                n "Eek~!"
                m "What was that?"
                p "Nothing, that was nothing!"
                m "Are you sure?"
                n "Just~ a little~ surprised~"
                n "Ah~"
                m "You sound a bit breathless, are you okay Nicole?"
                n "Oh, I feel great~!"
                m "W-Well, if you say so."
                n "It's a...  hard feeling to describe."
                p "Shh..!"
                n "But sometimes in the moment... it feels like everything is bliss."
                n "And everything... consequences... responsiblities... it's all secondary~"
                n "Do you... know what I mean?"
                m "Just... living in the moment..."
                m "It's the smell of..."
                m "(It's the smell of sex...)"
                n "It's in the air.. you can feel it."
                m "(Are they having sex again?)"
                m "(Do I dare look?)"
                m "(But who am I? An aging woman, to interrupt their fun?)"
                m "(But oh does it take me back to those days when I was young, when I took risks.)"
                m "(When I lived for the moment.)"
                m "(When I craved cocks, and had my fair share to choose from!)"
                m "(Could I not return to those days?)"
                m "(What a curse it is, to have [p], a well endowed male living with me, and not be able to take advantage of it.)"
                m "(What a curse it is, to have them doing it right next to me, taunting me.)"
                m "(Revealing to me, how far I am from what I was.)"
                m "(But... I could embrace how I used to be... couldn't I?)"
                m "(I-I could take risks again, be naughty! Be young...)"
                m "(My body is telling me too. I can feel my pussy getting wet, and images of [p]'s cock is just flooding my mind.)"
                m "(Flooding... cum... all into me...)"
                m "(How I've missed the feeling of warm semen in my womb, making me feel safe and secure.)"
                m "(I can't help myself any more...)"
                m "(After all... if they're doing it... why can't I?)"
                m "(Let's play this game... together~)"
                # amanda masturbate
                # both cum
                "No way. It all went to Nicole's plan. It was like she had done this before."
                p "What's next?"
                n "Haven't I done enough for you? [p]?"
                n "You'll be able to figure the rest out. Can't make it too easy for you, after all."
                n "Anyway, I'm sure you'll find the way. You always manage to."
                n "You know, you're better with women than you think."
                p "Huh, very nice of you."
                n "Goodnight, [p]."
                p "Goodnight, Nicole."
            "Use it.":
                "Wow, it's like she's completely forgotten what happened before."
        "Time to bring that back up. I can't wait to see [mr] crawling over my cock."
        p "Hey, there's something I want to show you."
        scene ak-8 with dissolve
        m "Show me? Ah..."
        scene ak-7 with dissolve
        m "I'm a bit tired today. Like you said, it has been a long day. After I finish up in the kitchen I'll be taking an early day off."
        p "It won't be too long."
        m "How about tomorrow, [p]?"
        p "Oh, alright then. That'll work."
        scene ak-12 with dissolve
        m "Thank you."
        scene black with fade
        "Did she know what I was trying to force do something funny?"
        "Was I too horny? Did I give it away?"
        "..."
        "No matter. I'll go straight to her work tomorrow."
        $ amandalvl += 1
        jump kitchen
    scene ak-1
    p "Hey, I love you [mr]!"
    scene ak-2
    m "I love you too sweetie!"
    jump kitchen

## Photoshoot scenes
label long_gown_scene:
    scene a-10 with fade
    p "This one is really fancy."
    p "It's a bit more... revealing though."
    scene a-9
    m "I see what you mean."
    m "Is this what you want to see on me?"
    p "Well, it's probably what the audience wants to see."
    scene a-11
    m "Don't you think it might be pushing it a bit?"
    p "Aaha, [mr], it's good to have a good range in the portfolio!"
    scene a-5 with dissolve
    m "Alright, dear. Turn around for a minute and I'll get it on."
    ## Turn around
    scene ae-2 with fade
    "..."
    "I can't wait to see her wear the gown. I think it'll look real nice on her."
    "..."
    p "Is eveything okay?"
    m "Sorry, I'm not used to wearing something like this!"
    p "Shouldn't be too much to work out."
    "It's barely any clothing anyway, hehe."
    menu:
        "Wait for [mr] to put on the gown.":
            "It's better to play it safe..."
            "..."
        "Sneak a peek.":
            $ depravity += 1
            "For... research purposes."
            scene ae-41 with fade
            "Oh..."
            "Yeah..."
            m "I hope you've still got your eyes closed~"
            "Shit!"
            scene ae-2 with fade
            "..."
    m "You can turn around now, [p]."
    play music "sounds/masked.mp3" fadeout 1
    scene amanda-2 with fade:
        pos (0.0, -3.43)
        linear 6 pos (0.0, 0.0)
    $ renpy.pause(6.0,hard=True)
    $ renpy.pause ()
    scene ae-43
    "Damn..."
    m "[p]! Are you going to pick your jaw up for the floor?"
    p "Eh uh, had a ministroke there."
    m "You really know how to pick a nice looking outfit!"
    p "It's not the outfit, it's the woman."
    m "You make me one happy [mr]~"
    scene ae-44 with dissolve
    m "So, what shots will you take? Mr Photographer?"
    p "Let's see...."
    p "I'll focus on the shots for now, and you work the poses."
    menu photoshoot1:
        "Head" if photo1 == False:
            $ photo1 = True
            scene ae-45 with dissolve
            $ renpy.pause ()
            scene ae-45 with flash
            $ renpy.pause()
            jump photoshoot1
        "Front" if photo2 == False:
            $ photo2 = True
            scene ae-46 with dissolve
            $ renpy.pause ()
            scene ae-46 with flash
            $ renpy.pause()
            jump photoshoot1
        "Back" if photo3 == False:
            $ photo3 = True
            scene ae-47 with dissolve
            $ renpy.pause ()
            scene ae-47 with flash
            $ renpy.pause()
            jump photoshoot1
        "Done" if photo1 == True and photo2 == True and photo3 == True:
            $ photo1 = False
            $ photo2 = False
            $ photo3 = False
    scene ae-48 with dissolve
    p "You're a stunner, [mr]."
    m "Of course I am~"
    m "Aren't you proud of having such a beauitful [mr]?"
    p "I will be if this takes off!"
    scene ae-49
    m "Fufufu~"
    p "So what did you think of this outfit?"
    m "It's beautiful, but a little revealing."
    p "You don't like showing skin, [mr]?"
    scene ae-50 with dissolve
    m "I supposed I do it occasionally at work, but it's something that I just have to be more comfortable with."
    p "Be confident and just express yourself, I think."
    scene ae-51
    m "Did you take that line from the book?"
    p "...maybe."
    m "It sounded like something an actual photographer would say."
    p "I {i}am{/i} an actual photographer."
    scene ae-49 with dissolve
    m "That's cute."
    m "See you next time, [p]."
    p "See you."
    return
label security_dress_scene:
    scene a-9 with fade
    p "Hahahah!"
    p "This one really is something."
    m "I see..."
    scene a-11 with dissolve
    m "Feeling naughty, [p]?"
    m "Need some discipline?"
    p "Christ, you're already in character."
    p "Get in the outfit first!"
    scene a-4 with dissolve
    m "As you wish~"
    m "You know the drill."
    p "Alright."
    ## Turn around
    scene ae-2 with fade
    "..."
    "Spicy stuff, can't wait to see her put it on."
    menu:
        "Wait for [mr] to put on the dress.":
            "I better be a good boy, or she might discipline me...hehe"
            "..."
        "Sneak a peek.":
            $ depravity += 1
            "It would be fitting to play the criminal..."
            scene ae-53 with fade
            "What would she even do to me if she found me looking?"
            "Maybe I should get caught on purpose one of these days."
            "..."
            "God that ass. What a thigh gap."
            scene ae-2 with fade
            "..."
    m "I'm ready."
    play music "sounds/masked.mp3" fadeout 1
    scene amanda-3 with fade:
        pos (0.0, -3.28)
        linear 6 pos (0.0, 0.0)
    $ renpy.pause(6.0,hard=True)
    $ renpy.pause ()
    scene ae-55
    p "What can I say?"
    p "Amazing as always."
    scene ae-56
    m "Good choice from you too!"
    m "It's a fierce outfit - I feel strong."
    scene ae-57
    m "Sexy and strong."
    p "I'm glad you like as it as much as I do."
    p "I'm going to take a few shots now."
    menu photoshoot2:
        "Head" if photo1 == False:
            $ photo1 = True
            scene ae-58 with dissolve
            $ renpy.pause ()
            scene ae-58 with flash
            $ renpy.pause ()
            jump photoshoot2
        "Front" if photo2 == False:
            $ photo2 = True
            scene ae-59 with dissolve
            $ renpy.pause ()
            scene ae-59 with flash
            $ renpy.pause ()
            jump photoshoot2
        "Back" if photo3 == False:
            $ photo3 = True
            scene ae-60 with dissolve
            $ renpy.pause ()
            scene ae-60 with flash
            $ renpy.pause ()
            jump photoshoot2
        "Done" if photo1 == True and photo2 == True and photo3 == True:
            $ photo1 = False
            $ photo2 = False
            $ photo3 = False
    scene ae-61
    p "I think people will really like these shots."
    p "Good job [mr]."
    scene ae-62
    m "You're the one who set this all up, thank you."
    p "It's nothing at all, like I said. I'm happy to help."
    p "I think we just need to get a few more photos, then we can think about marketing it."
    scene ae-56 with dissolve
    m "I'll leave it in your capable hands."
    p "Sounds good. See you later [mr]."
    m "See you."
    return
label gym_clothes_scene:
    scene a-9 with fade
    p "I wonder what you'll think about this one."
    scene a-10
    m "Haha, seriously?"
    scene a-11 with dissolve
    m "I haven't worn something like this since I was a school girl."
    m "Are people into this?"
    p "Trust me, they are."
    p "Ooooh yes. They are."
    scene a-9
    m "Okay, let's see if this will fit me..."
    ## Turn around
    scene ae-2 with fade
    "..."
    "This is a more innocent look. We're really going to cover the whole range."
    menu:
        "Wait for [mr] to put on the outfit.":
            "..."
        "Sneak a peek.":
            $ depravity += 1
            "Let's play the school pervert."
            scene ae-63 with fade
            "I was never one to peek at girls in the changing room."
            "But then again, the average girl don't look like [mr]."
            "I have a beautiful [mr]."
            scene ae-2 with fade
            "..."
    m "This is kinda tight, but I'm done."
    play music "sounds/masked.mp3" fadeout 1
    scene amanda-4 with fade:
        pos (0.0, -3.038)
        linear 6 pos (0.0, 0.0)
    $ renpy.pause(6.0,hard=True)
    $ renpy.pause ()
    scene ae-66
    p "I feel like I've done something very right, or very wrong."
    scene ae-67 with dissolve
    m "What do you mean?"
    p "It's just, well..."
    p "You must've been very popular in high school [mr]."
    m "I had a few boys coming my way back then."
    p "If you weren't my [mr], I might just have been one of them."
    scene ae-65
    m "You are so flattering!"
    m "Work your magic, Mr Photographer!"
    menu photoshoot3:
        "Head" if photo1 == False:
            $ photo1 = True
            scene ae-68 with dissolve
            $ renpy.pause ()
            scene ae-68 with flash
            $ renpy.pause ()
            jump photoshoot3
        "Front" if photo2 == False:
            $ photo2 = True
            scene ae-69 with dissolve
            $ renpy.pause ()
            scene ae-69 with flash
            $ renpy.pause ()
            jump photoshoot3
        "Back" if photo3 == False:
            $ photo3 = True
            scene ae-70 with dissolve
            $ renpy.pause ()
            scene ae-70 with flash
            $ renpy.pause ()
            jump photoshoot3
        "Done" if photo1 == True and photo2 == True and photo3 == True:
            $ photo1 = False
            $ photo2 = False
            $ photo3 = False
    scene ae-71
    p "Did you use to wear something like this back in school?"
    m "Yes, but not frequently."
    m "I was never a fan of sports."
    m "Running around was always a chore."
    p "Oh, how come?"
    scene ae-72
    m "It's a problem men like you won't understand~"
    p "Ah, I see."
    p "Thanks for the good work today, [mr]."
    p "Jeez, I'm getting tired!"
    scene ae-71
    m "Me too, I'll see you tomorrow."
    p "Goodnight."
    return
## Tracking
default photo1 = False
default photo2 = False
default photo3 = False

default long_gown_done = False
default security_dress_done = False
default gym_clothes_done = False
