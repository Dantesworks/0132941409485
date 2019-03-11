label kairatalk:
    if amandalvl == 2 and kairalvl == 1:
        scene black
        scene k-1 with fade
        play music "sounds/automata.mp3" fadeout 1
        p "Hi Kaira."
        scene k-2 with dissolve
        $ renpy.pause()
        scene k-3 with dissolve
        s "Afternoon [p]!"
        p "You were pretty wasted last night."
        p "How are you holding up?"
        scene k-6
        s "Last night?"
        s "I don't remember anything about last night."
        p "Phew!"
        p "I mean-"
        scene k-4
        s "It's okay, Nicole already told me what happened last night."
        p "..."
        p "She did?"
        "Oh no!"
        scene k-9
        s "Don't worry about it! It wasn't your fault I fell over."
        p "...hang on, what did Nicole tell you exactly?"
        scene k-8
        s "Now I'm the one confused."
        scene k-5
        s "She said I had too much to drink, and then I passed out and fell onto a pool of booze."
        s "That's apparently why I felt so sticky in the morning."
        p "..."
        scene k-11
        s "There's a lot of sticky liquid on my chest especially!"
        scene k-10
        s "My tits must have absorbed the fall. I knew they'd also have a practical use!"
        p "Are you feeling alright now?"
        scene k-12
        s "Hmm, I'm coming around now, but I still have this strange taste in my mouth."
        "Oh shit..."
        s "It's like nothing I've ever tasted before, but I don't mind it."
        scene k-4
        s "Anyway, Nicole said you took care of me when I was drunk. Thanks for that!"
        p "No worries at all, I'll always be there for my [sr]. You know that right?"
        s "Mm!"
        p "Speaking of Nicole, did you meet her in the morning?"
        scene k-10
        s "She came by and we went to grab a cup of coffee. I needed it sooo badly. I was feeling so groggy!"
        p "Where is she now?"
        scene k-12
        s "Why do you want to know anyway? Do you like her?"
        p "...I don't know what to say. She's quite a handful isn't she?"
        scene k-11
        s "Yeah they're big, but like, they're not real ya know? Not like mine!"
        p "That's not what I meant by handful haha."
        p "She's a... strange character."
        scene k-12
        s "Ooh, intriguing!"
        s "Do you want to learn more?"
        p "Yeah, I guess. How exactly did you guys meet?"
        scene k-10
        s "Hmm... we met in school and just sort of got along."
        s "Maybe she saw something in me?"
        scene k-8
        s "I don't know, we met a long time ago, we kinda meshed together well."
        p "Yeah but what exactly drew you together?"
        scene k-5
        s "Oh it's many things [p]! A friendship is not just because of one thing."
        scene k-4
        s "That goes for any kind of relationship!"
        scene k-11
        p "Looks like your memory problems are long standing."
        s "Hey!"
        scene k-12
        s "What do {i}you{/i} think about Nicole?"
        scene k-10
        p "Well!"
        menu:
            "I like her, but it'd be better if she was more... upfront?":
                scene k-4
                s "She can be quite introverted sometimes, but I think if you get to know her, she'll really open up."
                p "You think so?"
                jump k1

            "She's stunning yet mysterious. It's what guys like me go for.":
                $ depravity += 1
                s "If you guys ever end up being a thing, you have to credit me!"
                jump k1
        label k1:
            s "So, are you going to go for her? For real?"
            p "Chill, we'll see how it goes."
            scene k-12
            s "Well! You should know that Nicole usually comes over in the afternoons."
            s"Though, she won't be coming in today since we already caught up this morning."
            p "You've done well, little Kaira. Let the big man handle the rest."
            scene k-9
            s "Remember [p]! Never forget me even if you marry Nicole and move far far away!"
            p "Of course not, life wouldn't be complete without my [sr]."
            scene k-4
            p "..."
            p "By the way, something came to mind."
            p "Have you been having weird dreams lately?"
            scene k-6
            s "Um ah ah-!"
            p "Kaira?"
            scene k-9
            s "I haven't been having perverted dreams at all! What are you talking about?!"
            scene k-5
            s "Ah..."
            "Well that wasn't hard at all."
            p "Kaira, what about these dreams? You can tell me."
            scene k-9
            s "Ooh, um... Sorry I got a lot of work to do ehh, can't talk anymore, bye!"
            p "Hey look, I'm sorry for prodding. Maybe we could talk about it some other time?"
            s "Ahaha sure sure sure! But I reaaally got to get back to work!"
            p "Alright, I'll go!"
            scene black with fade
            s "Hey [p]!"
            scene k-13 with dissolve
            s "Sorry for cutting this short, we'll talk more about it later, ok?"
            s "Please don't hate me!"
            p "Never, Kaira. You tell me when you're ready."
            p "Bye!"
            scene black with fade
            "Is she having dreams that I'm having?"
            "They're more than just perverted dreams."
            "What does it mean?"
            "I guess I'll have to cross that bridge when I get there."
            $ kairalvl += 1
            $ kairatalk = day
            $ nicoledelay = day + 1
            $ nicoleshow = ["2"]
            play music "sounds/heart.mp3" fadeout 1
            jump kaira_room
    if kairalvl == 2:
        scene black
        scene k-1 with fade
        play music "sounds/automata.mp3" fadeout 1
        p "Hi Kaira."
        scene k-3 with dissolve
        s "Hey [p], sorry I brushed you off last time. What's up?"
        p "Nothing much, just thought I'd say hi."
        s "That's nice of you."
        s "How are you finding your stay back so far?"
        p "I'm loving it. I mean, I'm meeting all these new people. It's also good to spend time with you, of course."
        scene k-4 with dissolve
        s "Mm!"
        s "There's still so much for us to do and talk about! Have you thought about what you want to do?"
        p "It's been a ton of fun already. I really liked getting to meet Nicole and seeing you get wasted haha."
        scene k-7
        s "Fun for you maybe..."
        scene k-10 with dissolve
        s "Did you like the shopping trip? Maybe we should do it again!"
        p "I know you love shopping, Kaira, but think about me!"
        scene k-12 with dissolve
        s "I think you got {i}plenty{/i} from that trip as well."
        p "That's... probably true as well, but how about we switched things up a bit?"
        s "Alright, what do you want to do?"
        p "Hm, I dunno. Let's see..."
        menu:
            "Maybe we could talk over some coffee?":
                scene k-10
                s "Coffee?"
                s "We could head to that local cafe."
                p "No wait, my bad, it's closed in the afternoon!"
            "Maybe we could check out the strip bar? Man has his needs, you know?":
                $ depravity += 1
                scene k-10
                s "Bahah!"
                s "Eww.. talk to Nicole if you want that sort of stuff!"
                scene k-11
                s "Besides, you've got me! You don't need them!"
                p "It's a different kind of need, Kaira. You'll learn about it one day."
                scene k-12
                s "Will you teach me?"
                p "..."
                p "Some things ya gotta learn on your own."
        scene k-6 with dissolve
        s "So what are we going to do? There's a resort that maybe we could go to?"
        s "Ah, my membership might be expired though..."
        p "Stuff that, why don't we just chill here?"
        s "Here?"
        scene k-7
        s "Eheheh, my room's sorta boring..."
        scene k-6
        s "We could really go anywhere and it'd be better-"
        p "Let's just have a good old deep and meaningful conversation."
        p "We've hung out already, but we haven't really had a chance to just talk."
        scene k-5
        s "Umm, what do you want to talk about?"
        p "Well, we'll see!"
        p "I mean, am I losing the plot or something? Don't girls love to chat?"
        scene k-10 with dissolve
        s "Ahah, okay!"
        p "C'mon let's sit down here. Let's get comfortable."
        ## Transition
        scene black with fade
        scene k-31 with fade
        p "So. How's life?"
        s "What kind of question is that..."
        p "Are you happy, sad? How are you feeling?"
        scene k-15 with dissolve
        s "Well..."
        scene k-16 with dissolve
        s "I feel happy? I am, most of the time."
        scene k-17
        s "I've been feeling it more since you've been back. How's that!"
        p "Glad to hear it. I'm been happy too since I've been back. It's so good to come back to you guys."
        scene k-18
        s "My turn!"
        s "Have I changed since the last time we met? Be honest."
        p "Yeah of course you've changed. It's called growing up. Happens to everyone."
        s "Yeah, but {i}how{/i} have I changed?"
        p "You really want the specifics.. jeez, how come?"
        scene k-21
        s "Answer my question first."
        p "Alright, alright."
        p "Let's see...."
        menu:
            "I think you've grown into a kind and considerate young woman.":
                p "What do you think?"
                scene k-24
                s "Aww, you're so nice!"
                p "I mean it, you've been really accommodating of me. I know it might have been a bit disruptive, but you made time for me."
                s "I'd do it anytime, [p]."
            "Your boob size probably went up a few cups.":
                $ depravity += 1
                scene k-24
                s "Woo!"
                p "Enjoying the validation?"
                scene k-17
                s "How scandalous, for you to say such a thing~"
                p "You were fishing for it."
        scene k-28 with dissolve
        p "What's your overall goal in life, Kaira?"
        p "What drives you? What makes you want to keep on living?"
        scene k-26 with dissolve
        s "What is with these philosophical questions, [p]?"
        p "It's not called a deep and meaningful conversation for no reason, Kaira."
        scene k-27
        s "Fine, fine..."
        s "My goal in life...?"
        scene k-22
        s "I guess it's... to be happy."
        s "I always had in mind that I would finish school, go to university to study something I found interesting."
        p "Would that make you happy?"
        scene k-19
        s "That'd be part of it. I really want to study and do something I find interesting."
        p "Any idea what that might be?"
        scene k-26
        s "Hmm, I like to think I'm a caring person, so maybe something health related where I can help people."
        s "I was always interested in how people think, so maybe I could do psychology or something like that."
        s "I guess I'm not sure."
        p "What after that?"
        scene k-24 with dissolve
        s "Well.... hahah!"
        s "I want to you know, find someone I like and fall in love with him. Maybe have a few kids. I think that'd be a good life."
        p "You've got it all sorted."
        scene k-16
        s "I'm not sure, life changes all the time though doesn't it? I've learnt that much."
        s "I mean, I've always thought I'd meet the love of my life after I've started working, but that doesn't have to be the case, does it?"
        s "Sometimes, things happen out of order in the most beautiful way. Maybe they won't happen at all and something else comes entirely!"
        p "I think the same. My own life has taken its own turn in ways I couldn't predict."
        p "Yet somehow, I feel like this was the way it was supposed to turn out."
        s "I think I know what you mean."
        scene k-27 with dissolve
        s "..."
        s "I've been having this dreams that tell me the strangest things."
        play music "sounds/alchemy.mp3" fadeout 1
        p "Dreams?"
        scene k-25
        s "I don't remember too much about them, but I've been having them since you've come back."
        p "What do you remember?"
        scene k-26
        s "I... I'm not sure. I think I see you in it sometimes. That makes sense though right? Since you've come back recently."
        p "Yeah, it would make sense that I come up, since I'm new."
        p "Let's play psychologist and see if we can figure out any meaning from these dreams."
        p "Do you remember what I do in your dreams?"
        scene k-19
        s "I'm not a psychologist yet! I don't know how to make sense of them."
        p "You don't have to- I'm just asking, do you remember what I get up to in your dreams?"
        s "Oh, I don't know. Why does it matter what I'm dreaming about? It's just a dream."
        p "Kaira?"
        scene k-25
        s "...I don't remember."
        "I wonder if she's hiding something."
        scene k-22
        s "There is someone else though."
        p "Someone else?"
        s "I've also had the strangest dreams when a woman, or a girl... I don't know."
        scene k-30 with dissolve
        p "What does she look like?"
        s "I don't remember, it's so hazy, but she had white hair. I wonder if that means anything."
        p "Does she say anything to you?"
        scene k-25
        s "She probably does speak to me, but I don't remember exactly."
        s "I just remember the gist of what she said."
        p "And what is that?"
        s "..."
        scene k-22
        s "Something about how it was all going to be okay. And to do what my heart says."
        s "She told me not to worry."
        scene k-29 with dissolve
        "If this is the same dream we're having, then why is Kaira's dream of that girl telling her different things than my dream is telling me?"
        s "None of it really makes sense to me. Do they make any to you?"
        p "I can't say for sure. They are strange indeed!"
        p "Not too put off by those nightmares are you?"
        scene k-21
        play music "sounds/automata.mp3" fadeout 1
        s "Nightmares? They're not nightmares, I love those dreams! Whenever I wake up I always feel warm and fuzzy!"
        p "Huh? You're not scared by that strange girl telling you how to live your life?"
        scene k-16
        s "She doesn't tell me what to do, she only tells me it's okay for me to be me."
        s "Maybe it's my inner self communicating to me. I don't know what it is, but I like her!"
        p "That's interesting."
        scene k-28
        p "Maybe you {i}should{/i} study psychology and make sense of all of these dreams."
        s "Definitely something to think about~"
        scene k-31 with dissolve
        s "It's been good having this conversation with you, [p], but I've got to grab some food now."
        p "Where are you going?"
        s "I was planning to eat out, maybe you'd come with me?"
        p "Sure, I've got nothing better to do. Where are we going?"
        s "I usually grab takeaway - but we can find somewhere else where we can sit."
        scene k-14 with dissolve
        s "There's this really cool place - it's nice and cosy and its themed like those old american diners."
        p "I don't really mind where we go."
        p "I'll trust you on this one."
        s "Hehe!"
        scene k-24 with dissolve
        s "Adventure time!"
        scene black with fade
        "..."
        p "How much longer do we need to walk?"
        s "Not much longer, I promise."
        p "..."
        p "Where are we going again?"
        s "You're always asking that, you did the same for our shopping trip!"
        s "Geez, just be patient [p]!"
        p "Alright, alright."
        s "Let's just enjoy the journey. There, look at the sky."
        ## show sky
        scene sky with fade
        p "..."
        s "Look at the colours!"
        p "What a grey gloomy day."
        s "[p]!"
        s "Don't you see the orange light?"
        p "You mean the light being blocked by the clouds?"
        s "Don't you just love how the colours blend together?"
        s "Look at how pretty it is!"
        "Kaira has a point. The clouds are fluffy and the sky is a beautiful shade."
        "The orange is seeping through the gaps in the clouds."
        p "Hey, you're right."
        p "It's really pretty."
        s "Stop for a bit, [p]. Breathe in the air..."
        s "..."
        s "Life is good. Don't you feel it? Everything is going to work out."
        "Kaira has an oddly comforting manner. But she's right."
        "For the moment, I feel like everything is just going to work itself out."
        s "You okay, [p]? You've gone a little quiet."
        p "Huh?"
        p "I- I just got distracted for a bit. Sorry, what's up?"
        s "..."
        s "Never mind, [p]~"
        s "We've arrived."
        s "Let's go grab a seat, go go go!"
        p "American diner, huh?"
        s "Old school. I just looove the decor. I swear, a nice looking place makes the food taste ten times better."
        p "Well, let's hope the food here tastes as good as the place looks."
        s "Oh it does. You will love it!"
        p "You feeling hungry yet?"
        s "A little. You?"
        p "I'm medium hungry. What's on the menu?"
        s "Aha! Since you're my guest, let me take care of that for you~"
        p "Sure, sure. So what does little Kaira here suggest?"
        s "Little? Hmph..."
        s "The pizzas here are great. What do you think about ordering one and sharing?"
        p "Sharing is caring."
        s "I'll take that as a yes."
        s "Excuse me!"
        wai "Yes miss, what would you like to order?"
        s "The pizza special please!"
        wai "We make our pizza fresh here, so it may take a while. Will that be alright?"
        s "Of course. It'll be worth the wait [p]!"
        wai "Thank you for your patience."
        s "Haha! I should have let you know. The wait can take a while."
        p "Just means more time I get to spend with you - all the better."
        s "Aww, I'm glad you think so."
        p "Kaira, Kaira, Kaira."
        s "[p]?"
        p "I can totally see you being a psychologist."
        s "Really now?"
        p "Yeah."
        s "You're lying!"
        p "No, no, I'm serious."
        s "What makes you say that?"
        p "I just think you're easy to talk to. You obviously care about other people."
        p "You're empathetic and willing to listen."
        s "You... really mean that?"
        p "You bet I do. I think a psychologist really needs to earn trust, so that the patient can share all their secrets."
        p "With you, Kaira, I feel like I can."
        s "..."
        s "Are you trying to say in a roundabout way that you... need mental help?"
        p "No no no, jesus."
        p "I'm saying that as if I were a patient in general."
        "But really, I'm tempted to tell her everything."
        s "That means so much to me [p].  You have no idea."
        s "Growing up, I was always the small and cute girl. Nobody really took me seriously."
        s "To have your faith that I can do something like that... it's really touching."
        p "Kaira, why didn't they take you seriously?"
        s "Maybe it's the way I look."
        p "The way you look?"
        s "I've got a cute face. Cute girls aren't taken seriously."
        p "You've got everything in you to show the world you deserve to be taken seriously."
        p "Think about it Kaira. You've got the looks, and you've got your inner qualities as well."
        p "Not such a bad thing, is it!"
        s "Well, if you put it like that, hehe."
        s "I'm the best [sr] in the world, aren't I?"
        s "I bet your friends are all jealous of you."
        p "Jealous how?"
        s "That you get to spend your time with your awesome [sr], of course!"
        p "Knowing my friends, they'd be trying to get in your pants."
        s "Ooh, I just get allll the boys."
        p "I realise I haven't asked you yet. You getting any attention from the boys?"
        s "Hmm. What if I am, what if I'm not?"
        p "Well, I think if you say you aren't you're a liar."
        s "I had some attention when my boobies started to develop, but they just want me for my body."
        s "That doesn't mean much for me."
        p "So it's true then, girls that get hit on don't really appreciate that they're getting hit on."
        s "I would if they wanted something deeper, but it's always awkward and shy boys that can't even look at me in the eyes."
        s "I swear I can't even have a decent conversation without there being an ulterior motive."
        s "It's not like talking to you."
        s "Now, I'm relaxed and I feel safe."
        s "You know, I'm not like this in front of the other guys."
        p "Wow, guess I'm special then. Why do I get such special treatment?"
        s "Well, I've known you for a long time and I just don't think you'd take advantage of me, and you'll always consider my feelings."
        s "... and of course, I'm your [sr], so there's that too."
        p "You can come to me for anything Kaira, I'm always here for you."
        s "Maybe that's why I feel like nothing can go wrong, since I know there's you watching out for me."
        s "..."
        s "You know what, [p]?"
        p "Yeah Kaira?"
        s "Sometimes I wonder what it would be like if I wasn’t your [sr]."
        p "What are you talking about, Kaira?"
        s "I- I'm not sure, I guess sometimes I just feel-"
        wai "Sorry for the wait!"
        wai "Here’s our pizza special for the lovely couple~"
        s "Hehehe."
        p "Oh no, we’re not-"
        s "Thank you so much! It smells delicious."
        "I'm not going to lie, the pizza looks amazing."
        p "I can't wait to tuck in."
        s "You first, give it a go."
        p "I will!"
        p "..."
        "*Nonomnomom*"
        s "What do you think?"
        p "You really weren't wrong Kaira. This pizza is really good."
        s "I told you!"
        s "Woo, my turn now."
        p "Enjoy, hahahah."
        "I think one day when I look back, this will be one of those good days."
        "Right now, I can forget about everything and just enjoy some good company."
        "The atmosphere {i}does{/i} add to the whole exper-"
        s "I... I don't feel so good."
        p "Oh no, what's wrong?"
        s "The... pizza..."
        p "...!"
        p "Did you really finish the rest of it by yourself?"
        P "Did you just really?!"
        s "Don't judge me!"
        s "... it tasted really good..."
        p "C'mon Kaira, you gotta learn how to control yourself."
        s "..."
        p "Oh man... you're not going to puke, are you?"
        s "No... pwomises..."
        p "Oh man. What are we going to do with you Kaira?"
        s "I feel so full!"
        p "Do you need to puke? Go to the bathroom. You'll feel better."
        s "Be... right back."
        "Christ, that girl, I swear."
        "Just as I was praising her, she acts like a little kid again."
        "She'll always be my younger [sr]."
        x "Will she? [p]?"
        p "Who- what?"
        p "How did you?!"
        p "..."
        p "Who... are you?"
        x "Do you really want to know?"
        p "Yes, tell me who you are."
        p "Why do you show up in my dreams?"
        x "The answers to those questions won't change anything."
        p "I need some answer now, this is too fucking strange."
        x "Giving you answers have never helped before."
        x "They never have, and they never will."
        p "I have no idea what you're talking about."
        x "Compose yourself, [p]. She's about to return."
        p "What?"
        s "[p]?"
        p "Ah!"
        p "..."
        p "What just happened?"
        s "I don't know, were you sleeping?"
        p "I... guess I must have dozed off."
        p "Did- did you puke? How are you feeling now?"
        s "I did... a little bit, but I'm still not feeling super good."
        s "I wanna go home."
        p "Sure thing, no problem."
        p "Let me handle the bill."
        p "..."
        p "Hey, thanks for the pizza. How much is that going to be?"
        wai "Oh, don't worry. This one's on the house. We're sorry it made your partner sick!"
        p "Oh no, there was nothing wrong with the pizza-"
        wai "Please sir, we wouldn't be able to accept the money in good faith."
        p "..."
        p "Okay, I see then."
        p "Oh and by the way-"
        wai "Yes?"
        p "Did- did you see a girl around by any chance?"
        p "White hair. Sort of, purple suit."
        p "Did you... did you see something like that?"
        wai "There hasn't been anyone after you two I believe."
        wai "Were you expecting someone else to arrive?"
        p "You... didn't see anyone?"
        wai "I'm sorry sir, I don't believe there was anyone else."
        p "..."
        s "[p]! Can we go now?"
        p "..."
        p "Thanks for the meal."
        p "Let's go Kaira."
        ## Transition to night scene
        p "My little Kaira."
        p "Are you feeling better now?"
        s "I think I walked a little bit of it off."
        s "Thanks for helping me home, [p]."
        p "I just want to keep you safe."
        p "Are you feeling tired?"
        s "Mhm."
        s "You want to go to bed?"
        s "I can talk for a bit longer."
        p "We've had a lot of fun today already. You can go rest if you want."
        p "You don't need to stay up for me."
        s "..."
        p "I'll let you sleep now."
        s "No..."
        p "Hmmm?"
        s "Just stay for a bit longer."
        s "I'm not sleeping just yet, still not to get out of these clothes first..."
        s "It'll be okay, you can just look away."
        p "Alright."
        scene black with fade
        menu:
            "Keep my eyes shut.":
                "I shouldn't risk it."
            "Who am I kidding? Sneak a look.":
                $ depravity += 1
                "She's as gorgeous as I remember."
                "Kaira's such a precious girl."
                "I'm glad I have someone like her close to me."
        s "...I'm ready now."
        p "You don't like sleeping with much clothes do you?"
        s "It's more comfortable this way."
        p "If you say so."
        p "Anything else?"
        s "Can you tuck me into bed?"
        p "Haha, how?"
        s "Just like how [mr] used to do it."
        p "Just for you, Kaira. On the cheek right?"
        s "Mhm."
        p "Happy?"
        s "The left one too."
        p "Did [mr] used to give two kisses? That was such a long time ago."
        s "There's one more."
        p "..."
        p "Ah, I remember."
        s "Mmmm."
        ## hand clench
        s "Ah..."
        s "[p], I-"
        p "I- I just remembered! I've got something to get to!"
        p "Goodnight Kaira."
        s "G-goodnight [p]."
        "Shit, what was that?"
        "That... felt like it lasted forever."
        "[p], what are you doing...?"
        $ kairalvl += 1
        $ kairatalk = day
        daytime = 4
        jump hallway



    scene k-1
    p "How's my beautiful [sr] doing?"
    scene k-3
    s "Oooh!"
    s "So that's what [mr] means she says you have a silver tongue! You must do great around the ladies."
    p "I'm doing alright around you aren't I?"
    s "Alright alright! We'll talk later okay? I have to do some work first!"
    jump kaira_room
