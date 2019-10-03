label kairatalk:
    if amandalvl >= 2 and kairalvl == 1:
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
            call daykeep from _call_daykeep_23
            play music "sounds/heart.mp3" fadeout 1
            jump kaira_room
    if kairalvl == 2:
        $ amandakitchen = True
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
                "Is she... flirting with me, or am I just imagining it?"
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
        p "Glad to hear it. I've been happy too since I've been back. It's so good to come back to you guys."
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
        s "We've here!"
        scene k-32 with fade
        play music "sounds/missingyou.ogg" fadeout 1
        s "Let's go grab a seat, go go go!"
        p "American diner, huh?"
        scene k-33 with dissolve
        s "Old school. I just looove the decor. I swear, a nice looking place makes the food taste ten times better."
        p "Well, let's hope the food here tastes as good as the place looks."
        scene k-34 with dissolve
        s "Oh it does. You will love it!"
        p "You feeling hungry yet?"
        s "A little. You?"
        scene k-35 with dissolve
        p "I'm medium hungry. What's on the menu?"
        s "Aha! Since you're my guest, let me take care of that for you~"
        p "Sure, sure. So what does little Kaira here suggest?"
        s "Little? Hmph..."
        scene k-36 with dissolve
        s "The pizzas here are great. What do you think about ordering one and sharing?"
        p "Sharing is caring."
        scene k-37 with dissolve
        s "I'll take that as a yes."
        s "Excuse me!"
        scene k-51 with fade
        wai "Yes miss, what would you like to order?"
        s "The pizza special please!"
        wai "We make our pizza fresh here, so it may take a while. Will that be alright?"
        scene k-52 with dissolve
        s "Of course. It'll be worth the wait [p]!"
        scene k-50 with dissolve
        wai "Thank you for your patience."
        scene k-38 with dissolve
        s "Haha! I should have let you know. The wait can take a while."
        p "Just means more time I get to spend with you - all the better."
        scene k-44
        s "Aww, I'm glad you think so."
        p "Kaira, Kaira, Kaira."
        scene k-45
        s "[p]?"
        scene k-40
        p "I can totally see you being a psychologist."
        s "Really now?"
        p "Yeah."
        scene k-49
        s "You're lying!"
        p "No, no, I'm serious."
        s "What makes you say that?"
        p "I just think you're easy to talk to. You obviously care about other people."
        p "You're empathetic and willing to listen."
        scene k-36 with dissolve
        s "You... really mean that?"
        p "You bet I do. I think a psychologist really needs to earn trust, so that the patient can share all their secrets."
        scene k-39 with dissolve
        p "With you, Kaira, I feel like I can."
        s "..."
        scene k-47
        s "Are you trying to say in a roundabout way that you... need mental help?"
        scene k-41 with hpunch
        p "No no no, jesus."
        scene k-38 with dissolve
        p "I'm saying that as if I were a patient in general."
        "But really, I'm tempted to tell her everything."
        scene k-48 with dissolve
        s "That means so much to me [p].  You have no idea."
        s "Growing up, I was always the small and cute girl. Nobody really took me seriously."
        s "To have your faith that I can do something like that... it's really touching."
        p "Kaira, why didn't they take you seriously?"
        scene k-46
        s "Maybe it's the way I look."
        p "The way you look?"
        scene k-47
        s "I've got a cute face. Cute girls aren't taken seriously."
        p "You've got everything in you to show the world you deserve to be taken seriously."
        p "Think about it Kaira. You've got the looks, and you've got your inner qualities as well."
        p "Not such a bad thing, is it!"
        scene k-45 with dissolve
        s "Well, if you put it like that, hehe."
        scene k-44
        s "I'm the best [sr] in the world, aren't I?"
        s "I bet your friends are all jealous of you."
        p "Jealous how?"
        scene k-49
        s "That you get to spend your time with your awesome [sr], of course!"
        scene k-40
        p "Knowing my friends, they'd be trying to get in your pants."
        s "Ooh, I just get allll the boys."
        scene k-39
        p "I realise I haven't asked you yet. You getting any attention from the boys?"
        scene k-49 with dissolve
        s "Hmm. What if I am, what if I'm not?"
        p "Well, I think if you say you aren't you're a liar."
        scene k-36
        s "I had some attention when my boobies started to develop, but they just want me for my body."
        s "That doesn't mean much for me."
        p "So it's true then, girls that get hit on don't really appreciate that they're getting hit on."
        s "I would if they wanted something deeper, but it's always awkward and shy boys that can't even look at me in the eyes."
        s "I swear I can't even have a decent conversation without there being an ulterior motive."
        s "It's not like talking to you."
        scene k-38 with dissolve
        s "Now, I'm relaxed and I feel safe."
        s "You know, I'm not like this in front of the other guys."
        p "Wow, guess I'm special then. Why do I get such special treatment?"
        s "Well, I've known you for a long time and I just don't think you'd take advantage of me, and you'll always consider my feelings."
        scene k-45 with dissolve
        s "... and of course, I'm your [sr], so there's that too."
        p "You can come to me for anything Kaira, I'm always here for you."
        s "Maybe that's why I feel like nothing can go wrong, since I know there's you watching out for me."
        s "..."
        scene k-58 with dissolve
        s "You know what, [p]?"
        p "Yeah Kaira?"
        scene k-36
        s "Sometimes I wonder what it would be like if I wasn't your [sr]."
        p "What are you talking about, Kaira?"
        scene k-41 with dissolve
        s "I- I'm not sure, I guess sometimes I just feel-"
        scene k-42 with hpunch
        wai "Sorry for the wait!"
        scene k-53
        wai "Here's our pizza special for the lovely couple~"
        scene k-55
        s "Hehehe."
        p "Oh no, we're not-!"
        s "(He's so funny when he's flustered.)"
        s "(I'm not surprised she thinks we're a couple though...)"
        s "(I wonder what we would be like if I wasn't his [sr].)"
        scene k-54 with dissolve
        s "Thank you so much! It smells delicious."
        "I'm not going to lie, the pizza looks amazing."
        p "I can't wait to tuck in."
        s "You first, give it a go."
        p "I will!"
        scene k-57 with fade
        p "..."
        "*Nonomnomom*"
        s "What do you think?"
        scene k-56
        p "You really weren't wrong Kaira. This pizza is really good."
        s "I told you!"
        s "Woo, my turn now!"
        p "Enjoy, hahahah."
        scene k-58 with dissolve
        s "(Hanging out with [p] is different from hanging out with Nicole somehow.)"
        s "(It's fun, in a different kind of way.)"
        scene k-57 with dissolve
        "I think one day when I look back, this will be one of those good days."
        "Right now, I can forget about everything and just enjoy some good company."
        "The atmosphere {i}does{/i} add to the whole exper-"
        scene k-59
        play music "sounds/wistful.mp3" fadeout 1
        s "I... I don't feel so good."
        p "Oh no, what's wrong?"
        s "The... pizza..."
        scene k-60 with vpunch
        p "...!"
        p "Did you really finish the rest of it by yourself?"
        p "Did you just really?!"
        scene k-61
        s "Don't judge me!"
        s "... it tasted really good..."
        p "C'mon Kaira, you gotta learn how to control yourself."
        scene k-62 with dissolve
        s "..."
        p "Oh man... you're not going to puke, are you?"
        scene k-63
        s "No... pwomises..."
        "We were having such a good time too!"
        p "Oh man. What are we going to do with you Kaira?"
        scene k-64
        s "I feel so full..."
        p "Do you need to puke? Go to the bathroom. You'll feel better."
        scene k-65 with dissolve
        s "Be... right back."
        scene k-66 with dissolve
        $ renpy.pause()
        scene k-67 with dissolve
        "Christ, that girl, I swear."
        "Just as I was praising her, she acts like a little kid again."
        "She'll always be my younger [sr]."
        x "Will she? [p]?"
        scene k-68 with hpunch
        play music "sounds/cyberpunk.mp3"
        p "???"
        scene k-69 with hpunch
        p "Who- what?"
        p "How did you?!"
        p "..."
        p "Who... are you?"
        scene k-70
        x "Do you really want to know?"
        p "Yes, tell me who you are."
        p "Why do you show up in my dreams?"
        x "The answers to those questions won't change anything."
        p "I need some answer now, this is too fucking strange."
        scene k-71 with dissolve
        x "Giving you answers have never helped before."
        x "They never have, and they never will."
        p "I have no idea what you're talking about."
        x "Compose yourself, [p]. She's about to return."
        p "What?"
        s "[p]?"
        scene k-72 with vpunch
        play music "sounds/automata.mp3" fadeout 1
        p "Ah!"
        scene k-73 with dissolve
        p "..."
        p "What just happened?"
        s "I don't know, were you sleeping?"
        p "I... guess I must have dozed off."
        p "Did- did you puke? How are you feeling now?"
        scene k-74
        s "I did... a little bit, but I'm still not feeling super good."
        s "(I still want to spend time with him, but I'm not feeling too well. God, he must think I'm horrible!)"
        s "I wanna go home. I'm sorry, [p]."
        scene k-75
        p "Don't even worry about that Kaira, no problem."
        p "Your welfare is the most important thing."
        p "Let me handle the bill."
        scene k-76 with fade
        p "..."
        p "Hey, thanks for the pizza. How much is that going to be?"
        scene k-77
        wai "Oh, don't worry. This one's on the house. We're sorry it made your partner sick!"
        p "Oh no, there was nothing wrong with the pizza-"
        wai "Please sir, we wouldn't be able to accept the money in good faith."
        p "..."
        p "Okay, I see then."
        scene k-78 with dissolve
        p "Oh and by the way-"
        wai "Yes?"
        p "Did- did you see a girl around by any chance?"
        p "White hair. Sort of, purple suit."
        p "Did you... did you see something like that?"
        scene k-79
        wai "There hasn't been anyone after you two I believe."
        wai "Were you expecting someone else to arrive?"
        p "You... didn't see anyone?"
        scene k-80 with dissolve
        wai "I'm sorry sir, I don't believe there was anyone else."
        p "..."
        scene k-81
        s "[p]! Can we go now?"
        p "..."
        scene k-82
        p "Thanks for the meal."
        p "Let's go Kaira."
        scene black with fade
        ## Transition to night scene
        scene k-83 with fade
        p "My little Kaira."
        p "Are you feeling better now?"
        scene k-84
        s "I think I walked a little bit of it off."
        s "Thanks for helping me home, [p]."
        p "I just want to keep you safe."
        p "Are you feeling tired?"
        scene k-83 with dissolve
        s "Mhm."
        p "You want to go to bed?"
        scene k-84
        s "I can talk for a bit longer."
        scene k-86 with dissolve
        s "(Please don't go yet. Just a little longer...)"
        p "We've had a lot of fun today already. You can go rest if you want."
        p "You don't need to stay up for me."
        s "..."
        p "I'll let you sleep now."
        scene k-87
        s "No..."
        p "Hmmm?"
        s "Just stay for a bit longer."
        scene k-88
        s "I'm not sleeping just yet, still got to get out of these clothes first..."
        scene k-86 with dissolve
        s "It'll be okay, you can just look away."
        scene k-90 with dissolve
        s "(I feel like if he leaves, I don't know when I'll get to see him again.)"
        p "Alright."
        scene black with fade
        menu:
            "Keep my eyes shut.":
                "I shouldn't risk it."
                "..."
            "Who am I kidding? Sneak a look.":
                $ depravity += 1
                scene k-108:
                    pos (0.0, -3)
                    linear 6 pos (0.0, 0.0)
                $ renpy.pause(6.0,hard=True)
                $ renpy.pause ()
                scene k-91
                "She's as gorgeous as I remember."
                "Her... curves are amazing; I would love to just... run my hands along her body."
                "Feel her skin beneath my touch..."
                "Kaira's such a precious girl. I know I shouldn't be having these thoughts but..."
                scene black with fade
                "I'm glad I have someone like her close to me."
        s "...I'm ready now."
        scene k-92 with fade
        p "You don't like sleeping with much clothes do you?"
        scene k-93
        s "It's more comfortable this way."
        p "If you say so."
        p "Anything else?"
        scene k-94 with dissolve
        play music "sounds/missingyou.ogg" fadeout 1
        s "Can you tuck me into bed?"
        p "Haha, how?"
        s "Just like how [mr] used to do it."
        p "Oh right, when we were small."
        p "Just for you, Kaira, sure thing."
        p "On the cheek right?"
        scene k-95
        s "Mhm."
        p "Okay..."
        scene k-96 with dissolve
        p "Mwah!"
        p "Happy?"
        scene k-97 with dissolve
        s "That's not all of it, the left one too."
        p "Did [mr] used to give two kisses? That was such a long time ago."
        p "Fine."
        scene k-98 with dissolve
        p "Mwah!"
        scene k-99 with dissolve
        p "That was two for the price of one, Kaira!"
        p "Aren't you a lucky girl."
        scene k-100
        s "There's one more, remember?"
        p "..."
        p "Ah, I remember."
        p "Quick one."
        s "Mhm."
        scene k-101 with dissolve
        s "..."
        p "..."
        scene k-102 with dissolve
        $ renpy.pause ()
        scene k-103 with dissolve
        s "...!"
        "Her breath rose sharply."
        scene k-104 with dissolve
        s "Mmmmm..."
        scene k-105 with dissolve
        s "(I... feel strange....)"
        scene k-106 with vpunch
        s "Ah...!"
        s "[p], I-"
        p "I- I just remembered! I've got something to get to!"
        scene k-107
        s "Oh, I- me too! I mean..."
        p "Goodnight Kaira!"
        s "G-goodnight [p]."
        scene black with fade
        "Shit, what was that?"
        "That... felt like it lasted forever."
        "[p], what are you doing...?"
        $ kairalvl += 1
        $ kairatalk = day
        call daykeep from _call_daykeep_19
        call daykeep from _call_daykeep_20
        jump hallway
    if kairalvl == 3:
        scene black
        scene k-2 with fade
        play music "sounds/automata.mp3" fadeout 1
        s "Hi [p]. How are you?"
        p "I'm good. How are you, Kaira?"
        scene k-3
        s "Not too bad. I really want to spend some more time with you."
        p "We could maybe watch a movie later today?"
        scene k-9
        s "I guess ... But I want to go out! Do something that's not at home."
        s "[p], do you remember when mom used to take us to the beach? We would spend a whole day there just swimming and playing."
        p "Yeah I remember that. It was a lot of fun. But there's not really any beaches close to here."
        scene k-12
        s "Yeah you don't have to tell me that ... I know. I miss the beach."
        p "Is that why you're feeling down?"
        p "You know what... Do you know that resort place? It might not be the beach, but they have a swimming area."
        s "Yeah I've heard about it. It's supposed to be really nice."
        scene k-11
        s "Doesn't really matter though. I could never afford the membership price for that place."
        scene k-7 with dissolve
        p "I don't like seeing Kaira like this. I bet I could make her feel better if I could get her into that resort."
        p "I'll need the gold membership."
        $ kairalvl += 1
        $ kairatalk = day
        jump kaira_room
    if kairalvl == 4:
        if resortmembership > 2: ## resort check gold
            scene black
            scene k-1 with fade
            play music "sounds/automata.mp3" fadeout 1
            p "Hi, Kaira"
            scene k-2
            s "Hey, [p]"
            p "Still feeling a bit down?"
            s "I'm not reaaally down, I was just a little bored. I'll be fine"
            p "You know what I think would really make things great?"
            scene k-6 with vpunch
            s "What?"
            p "It's a gold membership, Kaira. I've got one."
            scene ke-1 with hpunch
            s "Are you serious? You have a membership for the resort and you haven't told me until now?"
            p "I only recently got it."
            s "[p] you have to take me there!"
            p "Yeah we can figure out a day. Maybe next weekend? Or maybe-"
            s "Right now! We're going right now!"
            p "Hang on-"
            s "Yay! Get ready soon [p]!"
            scene ke-4 with dissolve
            s "I'm going to think about what to wear."
            s "What do you think [p]?"
            p "Just wear your regular stuff, plus a swimsuit of course."
            scene ke-3
            s "A swimsuit?"
            "Yeah, the one you modelled for me the other day? Hehehe..."
            p "Yeah, we're going swimming. It's the resort."
            s "Do people do anything there besides swimming?"
            p "I'm... sure there's plenty to do."
            scene ke-2
            p "With the higher tier memberships, of course."
            s "There's higher than gold?"
            p "I think there will be. Its a work in progress."
            p "Something something renovations and a new architect. Or something."
            scene ke-3 with dissolve
            "..."
            "The resort is pretty big, I'm sure theres tons to do there."
            s "Alright then! I've picked out a swimsuit."
            p "Wow, Kaira, that was quick. Quicker than your usual time."
            s "Hmph!"
            s "Enough chit-chat, [p], it's time to go!"
            ## Transition to resort
            scene black with fade
            scene ne-0 with fade
            play music "sounds/slopes.mp3" fadeout 1
            p "Well Kaira, this is it."
            s "Wow this place is so nice!"
            scene ke-5 with dissolve
            s "You've got a gold membership too."
            scene ke-6 with dissolve
            s "Look at you, [p], you're taking me out on a date!"
            p "Yeah haha. Don't get too excited."
            scene cam-6 with dissolve
            p "Hi, Camille. Good to see you again. My [sr] and I are going to spend some time in the private pool."
            scene cam-5
            t "Okay no problem, [p]. You can just head in whenever you're ready."
            scene ke-7 with dissolve
            s "I can't believe you can afford a membership for this place. This is awesome."
            p "Bitcoin bros."
            scene ke-8 with dissolve
            s "Sorry?"
            p "Nothing."
            scene black with fade
            ## Transition to inside bathhouse
            scene ke-9 with fade
            t "Here you go, you two. Please enjoy yourselves."
            t "The private pool is a great place to just relax and enjoy some privacy."
            scene ke-10 with dissolve
            t "If there's anything that you need, please let me know."
            scene ke-11 with dissolve
            s "I hope you're not scared of water, [p]!"
            p "Me? Get real, I come here all the time."
            p "If anyone's afraid, it's you little girl."
            s "I'm great at swimming!"
            p "I hope so Kaira, coz' I'm not giving CPR."
            scene ke-12 with dissolve
            t "(Those two seem very close, if I didn't know I would-)"
            scene ke-13 with vpunch
            t "(Ah- you're imagining things again, Camille!)"
            scene ke-14 with dissolve
            s "The water looks amazing, [p]. I'm going to get changed. You should too."
            p "Right after you."
            scene black with fade
            ## Changing
            play music "sounds/masked.mp3" fadeout 1
            scene ke-15 with fade
            "As always, the women take the longest."
            scene ke-16 with dissolve
            "Alright [p], you gotta ready yourself. Act normal around Kaira."
            "Remember there are barriers."
            scene ke-17
            "Oh here she comes!"
            s "Hey~!"
            s "How do you like swimsuit?"
            scene ke-18:
                pos (0.0, -2.6)
                linear 6 pos (0.0, 0.0)
            $ renpy.pause(6.0,hard=True)
            $ renpy.pause ()
            scene ke-19
            "Whoa."
            "But at the same time, how could I not be attracted over something like that?"
            "Something so close, and yet so innocent..."
            s "..."
            s "Is everything okay [p]?"
            p "-I."
            scene ke-20
            s "Quite a bombshell this swimsuit!"
            p "Sure."
            p "I just got a bit distracted."
            scene ke-21 with dissolve
            s "Distracted by what?"
            p "The uh- colour of your swimsuit- it's just so interesting."
            "It's showing nearly everything! The way it hugs her frame and just entices me to touch her. As if daring me to make a move…"
            s "The colour?"
            s "[p], its completely white..."
            p "That was what was so interesting about it, you know?"
            scene ke-22 with dissolve
            s "Whatever [p]."
            p "You ready to get in the water, Kaira?"
            s "I sure am."
            s "Actually I can't even wait!"
            scene ke-23 with fade
            p "How is it?"
            p "Hot? Cold?"
            s "I haven't even gone in yet, hold up."
            scene ke-24 with dissolve
            s "..."
            s "Hmm...."
            p "Well?"
            scene ke-25 with dissolve
            s "Why don't you come in and find out for yourself?"
            p "Cheeky girl."
            s "Why are you so afraid of a little bit of water, [p]?"
            p "As you know Kaira, I hate the cold."
            p "Cold makes my balls shrink."
            p "I don't care if it's my [sr], I can't have my balls shrink in front of a woman."
            scene ke-26 with dissolve
            s "Haha... what?"
            scene ke-27 with dissolve
            p "Alright let's do it."
            s "You know, I hate cold water too."
            scene ke-26 with dissolve
            s "My nipples become stiff sometimes, it's quite embarassing!"
            p "It's cool how we can just say those sorts of things so casually."
            s "Why not? It's just you and me in here."
            s "And besides, I've said worse things to you already hehehe."
            p "You've got a point, I guess it's nothing new."
            scene ke-27 with dissolve
            p "Alright Kaira. You wanted me to try the water for myself?"
            p "I'll show you how I try the water."
            scene ke-28
            s "What are you-"
            scene ke-29 with hpunch
            s "[p]!"
            scene ke-30
            p "It's the OLYMPIC SPLASHUOOOO!!!"
            scene ke-31
            $ renpy.pause()
            scene ke-32 with flash
            s "..."
            p "Hey! It's not so cold after all."
            scene ke-33 with dissolve
            s "Well, [p], nobody said it was..."
            p "I hope you enjoyed the shower anyhow."
            s "Hey [p], since you're the one that took me out on this date, what do you plan we do next?"
            scene ke-35
            p "You probably haven't been swimming in ages, just enjoy yourself and try some use of my gold membership."
            scene ke-37
            s "Oh I will, but I want you to enjoy it too."
            scene ke-38 with dissolve
            p "What, did you have something in mind?"
            s "Let's just get exhausted and give it everything we got."
            p "They might have a gym here as well, I'm sure we'll be able to-"
            scene ke-39
            s "Stop, I've got a better idea."
            s "Hey, try catch me in the water!"
            scene ke-40 with dissolve
            s "Hehehehe!"
            scene ke-41
            "..."
            "Guess I'll play along."
            scene ke-42 with hpunch
            p "I'm coming for you Kaira! You better run!"
            s "AHHHH~!!"
            "While we swam and splashed around in the pool I had forgotten about my desires for her for a while."
            "It was nice to see her having fun like we used to all those years ago."
            "We tackled, fought and yelled with fun."
            scene ke-43 with dissolve
            "I have to admit I even found myself acting a bit like a child as well, but this kind of fun felt nostalgic."
            "From the look on her face she seemed to really enjoy it as well."
            scene ke-44 with dissolve
            "In just a moment, both of us were exhausted."
            scene ke-45 with dissolve
            play music "sounds/missingyou.ogg" fadeout 1
            s "You're pretty fast in the water, [p]."
            p "Catching you was hard!"
            scene ke-46 with dissolve
            s "Oh I'm so tired, who knew it would be such a work out."
            p "You're breathing hard."
            p "Maybe you should go to the gym more."
            scene ke-47
            s "Hey!"
            scene ke-48 with dissolve
            s "Hehehe, I should go to the gym though. Nicole does."
            p "I need to go to the gym too. I'm actually so unfit these da-"
            scene ke-49 with vpunch
            "!!!"
            "Her top must have come off when we were splashing around!"
            "Shit, should I tell her?"
            "But at the same time, this sight is bringing out my carnal desires."
            "I can't deny them for much longer. How could I?"
            menu:
                "Ahem, Kaira?":
                    p "I think something's wrong with your swimsuit..."
                    scene ke-50 with dissolve
                    s "..."
                    scene ke-51
                    s "Eeek!"
                    scene ke-52
                    s "Oh, [p]!"
                    p "I'm so sorry, I didn't know, I let you knew as soon as I could."
                "Nah, I think I'll enjoy it for a bit longer...":
                    $ depravity += 1
                    s "What's wrong, [p]?"
                    s "You suddenly cut off?"
                    scene ke-50 with dissolve
                    s "Hang on..."
                    scene ke-51
                    s "Eeek!"
                    scene ke-52
                    s "Oh, [p]!"
                    p "I was just about to say, I just lost my words!"
            scene ke-53 with dissolve
            $ renpy.pause ()
            scene ke-54 with dissolve
            s "Ahh haha! That's alright."
            scene ke-54 with dissolve
            s "You've seen me without my top before."
            p "I... have?"
            scene ke-56
            s "When we were kids, silly!"
            s "A little nudity doesn't matter, right?"
            scene ke-57
            s "We've already seen each other at our most vulnerable..."
            scene ke-58 with dissolve
            s "... and it looks like you've got something to show as well..."
            "Oh fuck, don't tell me."
            scene ke-59 with dissolve
            s "Having a party in your pants, [p]?"
            scene ke-61 with dissolve
            s "How come I wasn't invited?"
            scene ke-60
            p "Oh..."
            p "Well..."
            p "Ummm..."
            s "That's called a 'boner', isn't it?"
            p "It's uh, well... what have you seen one before?"
            scene ke-62
            s "I've seen it before. On the internet."
            p "Purely physiological. Perfectly normal."
            p "Don't read too much into it okay? Hahahah..."
            scene ke-63 with dissolve
            s "Alright~ I won't bring it up again aha-"
            p "You know what Kaira?"
            ## event end
            scene ke-64
            p "I think it's getting late. I think we should change and head home."
            scene ke-65
            s "Aw, but we were having so much fun!"
            p "Nah! Time to go!"
            s "Just because I teased you!"
            scene ke-66 with dissolve
            s "Ok fine."
            s "I guess it {i}is{/i} getting late."
            scene ke-67 with dissolve
            s "I'll get changed first, see you outside?"
            p "Seeya."
            scene ke-68 with dissolve
            $ renpy.pause ()
            scene ke-69
            "Wow, what was that."
            "That was too close, [p]."
            "She's kinda pushing it herself too."
            "Does she know what she's doing?"
            "..."
            "In either case, I need to get changed."
            scene black with fade
            #They both get changed.
            scene ke-70 with fade
            p "Ready to head back home?"
            s "As long as you're there to escort me."
            p "{i}You're{/i} the escort."
            scene ke-71 with dissolve
            s "Phh! Do I look like an escort?"
            p "Stop wasting energy, come on let's go."
            scene black with fade
            #They walk back home.
            scene k-95 with fade
            s "Thank you so much for taking me to the resort. I had such an amazing time"
            p "No problem. I'm glad you enjoyed it."
            s "[p], I was wondering ... I really like having you back home. And I've been having so much fun."
            s "Thank you."
            p "I'm really glad I came home, Kaira. I think I've wasted a lot of time. I should have come home a lot earlier."
            p "But what are you wondering, Kaira?"
            scene k-94 with dissolve
            s "You're so sweet, [p]. I was just thinking..."
            s "Remember when we were younger? We used to sleep in the same bed."
            p "Yeah I do remember that. We didn't sleep much, though. I think we spent most of the time joking around until [mr] would come in and demand that we go to sleep"
            scene k-93 with dissolve
            s "Hehehe, yeah I guess you're right about that."
            s "I was just wondering if we could maybe try that again"
            p "Uhm ..."
            scene k-94 with dissolve
            s "Oh come on. It would be like having a sleepover."
            s "I just remember how nice it was to not sleep all alone."
            "I'm not sure about this. It would be nice to not sleep alone. But she's my [sr], and we're not kids anymore. But somehow that doesn't deter me."
            p "Kaira, we were a loooot younger back then."
            scene k-92 with dissolve
            s "And so what? There's nothing wrong with having a sleepover with your [sr]."
            s "It would be fun! And I think we would sleep a lot better."
            p "I guess we could try it..."
            scene k-97 with dissolve
            s "Yay!"
            s "When it's time to go to bed, I'll come into your room."
            p "Haha alright. I'll be waiting."
            p "Just like old times."
            $ kairalvl += 1
            $ kairatalk = day
            call daykeep from _call_daykeep_21
            call daykeep from _call_daykeep_22
            jump kaira_room
        "Hang on, I need that gold membership first."
        jump kaira_room
    if kairalvl == 6:
        scene black
        scene k-3 with fade
        play music "sounds/missingyou.ogg" fadeout 1
        s "Hey, [p]! I hope you haven't missed me too much!"
        p "Eh?"
        p "That's right, a minute without me in your life is a minute too long."
        s "Ack!"
        p "Haha. So what are you doing?"
        scene k-11 with dissolve
        s "Planning on how to sneak into your room to cuddle without you noticing at night!"
        p "You want a repeat of what happened last time?"
        scene k-12 with dissolve
        s "Oh I know, I know. You think it's weird and you don't want [mr] to know."
        p "It's not that I particularly mind. I just don't want to send off the wrong impressions."
        scene k-8 with dissolve
        s "You don't trust me!"
        p "It's more like I don't trust myself."
        scene k-6 with dissolve
        s "Umm, what do you mean you don't trust yourself?"
        p "..."
        p "It's fine. You're old enough."
        p "You remember when we were at the pool?"
        scene k-4 with dissolve
        s "Mmm, mmm!"
        p "Well, I had a little accident downstairs, remember?"
        s "Downstairs?"
        s "Oh! That!"
        p "Well, when all the blood goes downstairs, there's not enough for upstairs, you know what I mean?"
        scene k-7 with dissolve
        s "Nope."
        p "As in, I might not think clearly, and do something dumb. You get me?"
        s "I don't get it. But I've already seen your thing down there before. What's the big deal?"
        p "Yeah maybe, when we were kids. That's different."
        scene k-6 with dissolve
        s "What's the difference?"
        menu:
            "Well, the size for one.":
                $ depravity += 1
                scene k-10 with dissolve
                s "Oh really? Then I really have to see!"
                p "..."
            "The dynamic is different.":
                s "I don't really get it, but if that's what you think is appropriate."
        p "Did someone turn up the temperature? Let's change the topic for a bit, haha."
        p "So, really, what are you up to?"
        scene k-5 with dissolve
        s "I'm about to start this quiz for homework. Wanna help me?"
        p "Sure, it should be stuff I've already done before."
        scene k169 with dissolve
        p "How many questions?"
        scene k170 with dissolve
        s "Just five!"
        p "When we do homework, we do homework, alright? No distractions."
        scene k171 with dissolve
        p "We got to put our thinking caps on. You have a thinking cap?"
        s "Hmm, when I want to focus, there's nothing that I put on."
        p "That was a metaphor, dummy Kaira! There's no such thing as a thinking cap in real life."
        scene k172 with dissolve
        s "Hey! I'm not dumb! People at school think I'm dumb because of my boobies."
        s "But I'm not!"
        p "Oh man, I'm sorry Kaira, I was just teasing you. I take it back."
        scene k173 with dissolve
        s "You can say it because you're my [p], but nobody else can okay?"
        p "No one else will. I'll tell them off if they do. Now what were you going to say?"
        scene k174 with dissolve
        s "I was going to say, I don't put things on to focus...."
        scene k175 with dissolve
        s "Instead, I take things off!"
        p "You take... things off?"
        scene k176 with dissolve
        s "Yes, I feel less constrained and less tight. It helps the blood flow!"
        p "Well, don't take too much off."
        scene k177 with dissolve
        s "Nope, just my top!"
        # strip off top
        scene k178 with dissolve
        $ renpy.pause()
        scene k179 with dissolve
        $ renpy.pause()
        scene k180 with dissolve
        $ renpy.pause()
        scene k181 with dissolve
        $ renpy.pause()
        scene k182 with dissolve
        s "Much better~!"
        scene k183 with dissolve
        p "Wow. Didn't I say no distractions?"
        scene k184 with dissolve
        s "You're not too distracted by my boobies are you, [p]?"
        scene k185 with dissolve
        s "My floofy boobies?"
        p "No, of course not..."
        scene k186 with dissolve
        s "Good, you're not like the rest of the guys, so it's fine right?"
        scene k187 with dissolve
        s "Of course, I wouldn't do this at school."
        p "So uh, let's get on with it. What did you need help with?"
        scene k188 with dissolve
        s "Let's take a look at this page here..."
        s "What do you think?"
        scene k189 with dissolve
        s "A, B, C, or D?"
        scene k190 with dissolve
        "Fuck, her tits are so large I just want to sink my head into those puppies."
        "Surely she knows what this is doing to me."
        "I can't concentrate!"
        "They look so soft!"
        scene k191 with dissolve
        s "Um, [p]? Which one?"
        p "..."
        scene k192 with dissolve
        s "[p]! Are you stuck on the first question already?"
        scene k193 with dissolve
        p "Oh erm! I- uh, double D's."
        scene k194 with dissolve
        s "Both of them are D?"
        s "Oh, you've already moved onto the next question already - I was worried that you might have forgotten this part, ahaha!"
        s "Okay, what about this next question?"
        s "I think it's A, but I'm not sure..."
        s "..."
        s "[p]?"
        scene k195 with dissolve
        p "Fuck, I think I'm hallucinating. They're just so mesmerisng!"
        p "Double D's..."
        s "Again?"
        s "The teacher must be trying to prank us or something, good thing I've got you to help!"
        s "Okay, final question. Is this one going to be D as well?"
        s "I think if I were the teacher, I would change the final question's answer just to confuse people."
        s "What do you think, [p]?"
        p "..."
        p "...all the D's... all of 'em...."
        s "You sure? Okay!"
        scene k196 with hpunch
        p "Oh shit, what?"
        s "I must say, [p], you looked like you were in a trance!"
        scene k197 with dissolve
        s "So this must be what you're like when you're really focussed on something."
        p "Oh I was focussed on something alright..."
        scene k198 with dissolve
        s "Thanks for your help, [p]! I can't wait to get full marks tomorrrow."
        p "No worries, Kaira!"
        p "Just curious, by the way..."
        p "Is this quiz... important?"
        scene k199 with dissolve
        s "Important?"
        p "Like, will you fail if you don't pass?"
        scene k200 with dissolve
        s "Nope! But I just wanted to impress the teacher by getting full marks."
        p "Oh ok, fair enough."
        "Phew! I feel better about the answers now."
        p "So uh, let me know how it goes tomorrow okay?"
        scene k201 with dissolve
        s "Will do!"
        scene black with fade
        $ kairalvl += 1
        call daykeep
        jump hallway
    if kairalvl == 7:
        play music "sounds/automata.mp3" fadeout 1
        scene black
        scene k-1 with fade
        p "Hey, how'd the test go?"
        scene k202 with hpunch
        s "[p]! They were all the wrong answers!"
        s "Oh no, Kaira! What went wrong?"
        s "They were the answers you gave me!"
        scene k203 with dissolve
        s "I was so confident they were right, I trusted you..."
        s "Then everyone in the class laughed at me! {i}Sob{/i}."
        p "Oh, geez Kaira. I didn't mean to, I promise!"
        p "Guess I got a little distracted, I broke my own rule."
        scene k204 with dissolve
        s "How come all my answers were wrong?"
        p "Well..."
        scene k205 with dissolve
        s "I knew it, you weren't paying attention!"
        scene k206 with dissolve
        s "You were distracted by my bewbies!"
        p "Y-you can't prove that!"
        p "..."
        scene k207 with dissolve
        p "Alright, it's true. Sorry Kaira, you know what I said earlier about blood rushing downstairs?"
        s "Hmmm..."
        p "It leaves less blood in the brain, to think."
        scene k208 with dissolve
        s "Oh. Did... my boobs do that do you?"
        p "I know you're my [sr] and all, but I couldn't help it, I swear! It's purely physiological."
        scene k209 with dissolve
        s "I don't know how to feel, [p]..."
        s "On one hand, I got laughed at by the class. On the other hand, I'm kinda happy that this means I'm more sexy than cute."
        p "Huh?"
        scene k210 with dissolve
        s "Remember when we at the clothing store? I asked you if I was sexy or cute."
        scene k211 with dissolve
        s "I like being sexy, it beats being cute by a mile!"
        p "How come it's so important to you?"
        scene k212 with dissolve
        s "Well, for one, sexy is like Nicole, and that's like, more power, right?"
        p "Being cute is really powerful as well. You could get away with a lot."
        scene k213 with dissolve
        s "But {i}I{/i} think, I could get away with {i}much{/i} more being sexy."
        scene k214 with dissolve
        s "I'm not a little girl anymore, [p]!"
        p "You're... definitely coming of age, Kaira. Listen, I'm sorry about all this."
        p "It hurts me to hear you got made fun of at school. I'll make it up to you, I promise."
        scene k215 with dissolve
        s "You'll make it up to me?"
        p "Sure. Hmm, would twenty bucks do?"
        scene k216 with hpunch
        s "[p]!!"
        p "Of course, you're right. How about fifty? That's a shift at the cafe, by the way."
        scene k217 with dissolve
        s "...!"
        p "I'm kidding, I'm kidding!"
        scene k218 with dissolve
        p "I'll make it up to you with some quality time, hmm? Just the two of us."
        s "That... sounds nice? Where are we going?"
        p "We'll go wherever {i}you{/i} want to go. Wherever Kaira's little heart desires."
        scene k219 with dissolve
        s "I've got a big heart, [p]! I'm kind and I'm caring!"
        p "Haha, you're right, my bad. So, where do you wanna go?"
        scene k220 with dissolve
        s "Let me see..."
        s "What's a nice place for two people to go?"
        p "Are you hungry?"
        s "Mm, not really."
        p "What's a nice hippy place that couples go to?"
        p "Let me take you to the local gallery, Kaira. Wouldn't that be nice?"
        p "We could look at some pretty pictures."
        scene k221 with dissolve
        s "Is that what couples do?"
        p "I think it is. It should be a nice. Art is not just about something to look at, you know?"
        p "When you look at art, it's also a chance to look at yourself."
        s "To look at myself? I have the mirror for that!"
        p "You spend a lot of time looking at yourself, do you Kaira?"
        scene k222 with dissolve
        s "To compare how my body changes day by day, of course. I think I'm still a growing girl."
        p "And also to check yourself out, I'd bet."
        scene k223 with dissolve
        s "There's a bit of that too~"
        p "But I mean, when you look at yourself with art, you look within yourself. You get to do some soul searching."
        p "You know, to look at yourself introspectively."
        scene k224 with dissolve
        s "Hmmm..."
        p "Come on, let's go. I'll show you."
        scene k225 with dissolve
        s "Oh okay, let's go, whoopie!"
        # to museum
        stop music fadeout 1
        scene black with fade
        "A few moments later..."
        play music "sounds/missingyou.ogg" fadeout 1
        scene k225 with fade
        p "So Kaira, here's an interesting arrangement. What do you think?"
        scene k227 with dissolve
        s "Wow, there are a lot of pictures here."
        scene k228 with dissolve
        p "Is there a particular one you like?"
        scene k229 with dissolve
        s "I like this one, of the landscape! It makes me feel like there's a lot of potential, and I just feel like, freedom."
        p "I like that one too. It's a very optimistic feeling. It reminds me of when you we were on the way to the diner, and you told me to look at the sky."
        scene k230 with dissolve
        s "Yeah, it was so pretty."
        scene k231 with dissolve
        s "I guess I'm that kind of girl."
        p "You'll like this flower too then, right?"
        scene k232 with dissolve
        s "What about the flower?"
        p "You think it's pretty?"
        s "It's okay. I like the animals more. Look! The lion!"
        scene k233 with dissolve
        p "Does it speak to you?"
        scene k234 with disolve
        s "Speak to me?"
        p "Like, do you feel something inside when you look at it, do you see yourself?"
        scene k235 with dissolve
        s "Ermm... I don't really see myself as a lion."
        scene k236 with dissolve
        s "A lion is supposed to be brave right? The lion roars, and makes a huge sound."
        scene k237 with dissolve
        s "I wish I could be like that."
        scene k238 with dissolve
        p "You don't feel like you could be brave?"
        scene k239 with dissolve
        s "I'm actually kind of shy and quiet sometimes..."
        p "Oh, I think you're definitely forthcoming and honest, what do you mean?"
        scene k240 with dissolve
        s "I'm comfortable with you and Nicole, so I'm less shy with you guys. But at school or when I'm with my other friends, I wish I could speak out more."
        scene k241 with dissolve
        s "(But even then, [p]... sometimes... I wish I could be more honest with you...)"
        scene k242 with dissolve
        p "Well, look Kaira. The lion wasn't always brave."
        scene k243 with dissolve
        s "No?"
        p "Of course not. The lion was once a cub, just a kid. He wasn't alwasy strong. But overtime, he became stronger, louder, braver. It was something that took time."
        p "Maybe that's what the message should be."
        scene k244 with dissolve
        s "I hope, [p], one day I can be brave."
        s "(I hope, one day, I can be honest with you.)"
        p "Hah, you have my full support, Kaira."
        scene k245 with dissolve
        s "..."
        scene k246 with dissolve
        s "Oh yeah, what about... this one?"
        s "How does that make {i}you{/i} feel?"
        scene k247 with dissolve
        p "It's an interesting mask..."
        scene k248 with dissolve
        "It's a mask, right? It looks like it's in pain."
        "Why would someone wear a such a sad face?"
        "Don't people typically wear a happy face to cover up a sad interior?"
        "Why would someone purposefully show an expresson of pain?"
        "Is it... penitence?"
        "I wonder what they did."
        play music "sounds/cyberpunk.mp3" fadeout 1
        x "It is repentance."
        scene k249 with hpunch
        p "!!"
        x "It is a story of redemption."
        scene k250 with dissolve
        x "It is often at the point of anagnorisis that the heroes come to this conclusion."
        x "Tragically, it is only after the peripeteia that our hero can repent."
        x "The greeks knew this."
        p "I-who-"
        scene k251 with dissolve
        x "Focus, [p], what do you see?"
        p "I... see..."
        scene k252 with dissolve
        play music "sounds/automata.mp3" fadeout 1
        s "Umm, [p]?"
        s "You're really focussed on that picture. Are things okay?"
        scene k254 with dissolve
        p "I see regret. I see a man who desperately wants to undo what he had done."
        p "I see man who would give anything to take back what he lost."
        p "He wears the mask because he knows he was responsible."
        p "He wants the world to know as penance."
        scene k253 with dissolve
        s "Whoa, [p], that's really deep all of a sudden."
        menu:
            "I'm not him.":
                $ depravity += 1
                scene k255 with dissolve
                s "Well, it's like me and the lion picture, right?"
                s "We aren't anything like the pictures we had a look into."
            "I can relate to him.":
                scene k255 with dissolve
                s "Well, you also said that I was more like the lion than I thought."
                s "Maybe the pictures let us look more into ourselves after all."
                scene k256 with dissolve
                s "I think I can see."
        scene k228 with dissolve
        p "Fascinating stuff Kaira. I think that's enough thinking for the day, for the both of us."
        p "What do you reckon?"
        s "Let's go home~! I'm getting tired."
        scene k226 with dissolve
        p "It was interesting though, wasn't it? I hope I made up for getting you those wrong answers."
        scene k231 with dissolve
        s "Erm, I haven't forgiven you yet! You'll have to hang out with me even more times before I do, okay?"
        scene k233 with dissolve
        p "It would be my pleasure to, Kaira."
        s "Yippie!"
        scene black with fade
        $ kairalvl += 1
        call daykeep
        call daykeep
        jump map
    if kairalvl == 8 and nicolelvl >= 10:
        play music "sounds/automata.mp3" fadeout 1
        scene black
        scene k-2 with fade
        p "So, I was thinking, Kaira."
        scene k-3 with dissolve
        s "Hmm?"
        p "You were talking about that trip with Nicole, and you said you had bought the tickets already or something."
        scene k-4 with dissolve
        s "We've booked the hotels! I invited you before too! Are you coming?"
        p "I've been thinking about it, and I've love to. Tell me more. Where are you guys going?"
        scene k-5 with dissolve
        s "We're actually going to where you were studying. Is that going to be alright?"
        p "..."
        s "Ah, [p], maybe it isn't the best idea, I'm sorry."
        p "No at all, it's a great area. Plenty of tourism, lots of shops around and young people. It's a great holiday destination."
        scene k-9 with dissolve
        s "So you don't mind?"
        p "Haha, of course not, I'm totally over it anyway. What's your plan for the trip?"
        scene k-12 with dissolve
        s "Well... haha, we haven't reaaally planned it out too much. We only have the hotel so far, and it was because we thought it looked awesome."
        p "Oh yeah? So you haven't bought plane tickets yet?"
        scene k-11 with dissolve
        s "Nope."
        p "What about hotel rooms? How many have you booked?"
        s "Just one for me and Nicole."
        p "How am I gonna fit?"
        scene k-5 with dissolve
        s "It's a big bed, [p]. I'm sure you'll squeeze in."
        p "Hmm, Nicole could sleep in the middle. That could work."
        scene k-9 with dissolve
        s "Huh? No! {i}You{/i} can sleep in the middle! I'm sure Nicole wouldn't mind."
        p "She's my girlfriend."
        scene k-8 with dissolve
        s "And I'm your [sr]. We can share, ok?"
        p "Why don't we invite [mr] as well? Woman's been working for so long. Now that she's in Dante Studios, it seems like a nice time for her to take a break."
        scene k-9 with dissolve
        s "Hmm, but that's four people in one bed!"
        p "You don't want [mr] along?"
        scene k-5 with dissolve
        s "Of course I do, but it looks like we'll have to change our plans a bit, hmm..."
        p "Let me grab a seat and talk about this."
        scene k-15 with fade
        p "Let's change the topic to plane tickets for a bit."
        scene k-19 with dissolve
        s "There's not much to think about, right? Just economy there and back. We can buy them whenever."
        p "There's more than just economy class, you know?"
        scene k-17 with dissolve
        s "Like business class?"
        scene k-21 with dissolve
        s "[p]! I-I don't have too much savings, you know that right?"
        scene k-20 with dissolve
        s "I think it's better to spend money on other things instead, right?"
        s "Like, clothes... food... mmm...."
        p "You know, business isn't the only alternative to economy. There's first class too."
        scene k-19 with dissolve
        s "First class? That's like super expensive! I super-duper can't afford that."
        p "If [mr] comes along, we'll need more hotel rooms too."
        scene k-25 with dissolve
        s "That's going to be more money. I saved up reaaally hard for this, [p]."
        p "I know, little Kaira, I know. Let me make you a deal."
        scene k-22 with dissolve
        s "Huh?"
        p "I'll cover all the expenses. In return, you'll have to forgive me for giving you the wrong answers from before."
        p "Deal?"
        scene k-25 with dissolve
        s "You'll pay for... everything?"
        p "I'll plan it all out too. Just leave it all to me."
        s "Are you joking?"
        p "Nope. I'll make sure it's the best trip you've had."
        s "How are you going to get the money?"
        p "I'm a master investor. Buy low sell high."
        scene k-19 with dissolve
        s "What's an investor?"
        p "I'll teach you all about it one day. So what do you say?"
        scene k-17 with dissolve
        s "You promise to make the bestest trip ever?"
        p "I promise."
        scene k-24 with vpunch
        s "Yippie yippie!"
        s "I love you I love you I love you [p]!"
        scene ke-1 with vpunch
        s "I can't wait to go, when are we going? What should I pack? Do I even need to pack?"
        s "I have more money left now to buy clothes, maybe I'll just buy it there!"
        p "Haha, easy easy. I'll go chat to [mr] and Nicole about my plans, and I'll come back once I've got everything ready and set to go, alright?"
        s "Wow, [p], I never imagined this. This is so awesome!"
        s "We're going to have so much fun, aren't we? What a treat!"
        scene ke-4 with dissolve
        p "I'm doing this for you, Kaira, I just want to see you happy girl."
        s "I like to see you happy too, [p]."
        s "I'm happy if you're happy."
        p "Likewise."
        s "So let's be happy together!"
        p "Yes Kaira, let's."
        scene black with fade
        "I just need ask [mr] to come and Nicole let know."
        $ kairalvl += 1
        jump hallway
    if kairalvl == 9 and nicolelvl == 12 and amandalvl > 21:
        p "Good news, Kaira, good news!"
        s "Ooh, tell me!"
        p "I've finished the arrangements for the trip, and I've got the essentials planned."
        s "Um, okay... can you tell me about it?"
        p "What do you want to know?"
        s "Everything! You said it was going to be really cool and really awesome right?"
        s "Tell me tell me tell me!"
        p "Alright, alright, gather round! You won't believe what I managed to put together."
        p "First, we're getting there by jet."
        s "Weren't we already going to go by plane? I mean, but still, thank you so much for buying tickets!"
        p "You're welcome Kaira, but it's not just any plane. This is a private jet, just for us four."
        s "You managed to get a private jet? No way!"
        p "Oh, it's no big deal, you know..."
        s "You're lying right? You're not telling the truth, are you?"
        p "C'mon Kaira, you don't trust me?"
        s "..."
        s "But, how did you get the money? A private jet must've been super expensive, there's no way-!"
        p "It's the power of BCC, Kaira. I'll teach you. One day."
        p "You'll believe it when you see it."
        s "Hmm, fishy [p], but I'll go along with it for now! What about after the plane ride?"
        p "Well! I booked out the deluxe lurious double hotel room package. Those rooms are fantastic."
        p "Maybe a little excessive, since we won't be staying in the hotel rooms for much of the day, but still!"
        p "I wanted to give you a great experience, Kaira."
        s "Aww, [p], this had better be super duper real, okay?!"
        s "Mmm, I can't wait!"
        p "I'm not done yet, I also got the Relaxing RV to take us around the place when we're going to all the different holiday destinations."
        s "Omg, this is all we need, [p]! I need to tell Nicole and [mr]!"
        s "I-I... when are we going!"
        p "Hmph, I thought you'd never ask."
        p "Let the others know, and we can go as soon as the next day."
        s "Oh, goodie!"
        $ kairalvl += 1
    if kairalvl == 10:
        menu:
            "Let the others know, and go on the trip!":
                d "You will not be able to return until the trip is over."
                d "Make sure to do things you want to do before you embark."
                d "Are you sure you want to go now?"
                menu:
                    "Yes":
                        p "Let the others know, Kaira. Get them ready!"
                        s "NICOLE!!!"
                        p "Jesus."
                        "..."
                        n "You called for me, Kaira?"
                        s "Me and [p] were just talking about the trip, and it's all sorted now!"
                        s "[p] says he got us a private jet! Oh, and two huge five star hotel rooms and like, a massive truck to go places with!"
                        n "Did you really, [p]?"
                        p "All this doubt, guys! Come on!"
                        n "I don't know how the hell you did it, but I think I'm loving you more and more."
                        n "This is going to make an unforgettable trip. You know that, right?"
                        p "That's the plan. Because you girls are worth it."
                        n "You're such a nice boyfriend, [p]. I must say I've got a good taste."
                        s "Hmm! [p] is nice to me too, you know!"
                        p "I'm nice to everyone; I'm just a nice guy."
                        n "Bleh."
                        n "Us girls like exclusive treatment."
                        s "Nicole's right, [p]. I don't mind sharing with Nicole, but you have to like, treat us nicer than the rest, okay?"
                        s "To be fair, Nicole, [p] is already a lot cooler than the boys in our class, right?"
                        n "You mean the creeps?"
                        p "..."
                        s "Yeah! Thankfully [p] is not like the rest of them, and that makes me happy."
                        s "Coz' there's something special about us, right [p], that makes you so nice to us."
                        s "Mm that must be it, bahahaha!"
                        n "Kaira's awfully possessive, isn't she? You must mean a lot to her."
                        p "Well, Kaira means a lot to me too. How could someone not love this cuddly, dumb little [sr]?"
                        s "Eh- I'm not dumb! But I like cuddly~"
                        p "I say that in the most loving way."
                        s "Aww! [p] should mean a lot to you too Nicole."
                        n "Whatever gives you that idea? Don't give the man an ego~"
                        s "Well, I thought you liked him a lot based on all the stories you told me about-"
                        n "-Hey! Uh, let's keep that between just us two..."
                        p "Stories, Nicole?"
                        n "It's just girl gossip."
                        p "I hope it's PG."
                        n "No comment~"
                        p "Never change, Nicole, never change."
                        n "Kaira's a grown girl now though, isn't she? She'll be alright."
                        s "I {i}did{/i} say my bewbies have grown a lot, didn't I?"
                        s "The proof is in the pudding!"
                        n "Two squishy mounds of pudding~"
                        s "Hehehe..."
                        p "Enough, listen up guys, let me fill you in on the rest of details."
                        "A few moments later..."
                        p "Alright that's all of it. I'll leave you two girls alone to do girl things now."
                        p "Would you please let [mr] know about the plans?"
                        s "Oh I can't wait to tell [mr] about the trip when she comes back."
                        s "But whatcha gonna do in the meantime?"
                        p "Planning this trip was hard, Kaira. I'm gonna go for a sleep."
                        s "Oh okay, rest well, [p]!"
                        n "I guess I shouldn't stay too long either, I've got a lot of things to pack."
                        p "Remember, travel light."
                        s "Yes, yes, we can just buy the clothes with the money we saved when we go clothes shopping."
                        n "The money we saved thanks to [p]."
                        n "Thank you, [p]!"
                        p "You're welcome, you're welcome..."
                        s "Go to rest now, [p], sorry for holding you up for so long."
                        n "Seeya, [p]."
                        p "I'll see you guys real soon."
                        stop music fadeout 1
                        "Wow, it took a lot of money, but this is really happening."
                        "I haven't looked forward to something so much in a long time."
                        scene black wth fade
                        "On a bright early morning on an exciting day..."
                        $ kairalvl += 1
                        # play lala land
                        label lala:
                        play music "sounds/bean.mp3" fadeout 1
                        scene p1 with dissolve
                        $ renpy.pause()
                        scene p2 with dissolve
                        p "I feel light and happy. Today's finally the day!"
                        scene p3 with dissolve
                        "Ahhh! Time to get prepared!"
                        scene p4 with dissolve
                        "Hmmm..."
                        scene p5 with dissolve
                        "How about..."
                        scene p6 with dissolve
                        "The Kishou Arima!"
                        scene p7 with fade
                        "The others should be ready by now."
                        "The flight leaves early in the morning."
                        "I can't miss my own flight now!"
                        scene p8 with dissolve
                        $ renpy.pause()
                        scene p9 with dissolve
                        $ renpy.pause()
                        scene p10 with dissolve
                        $ renpy.pause()
                        scene p11 with dissolve
                        $ renpy.pause()
                        scene p12 with dissolve
                        $ renpy.pause()
                        p "Good morning guys!"
                        scene p13 with dissolve
                        n "Good to see that I didn't need to wake you up this time, [p]."
                        scene p14 with dissolve
                        n "It's just as well, right? After all, my method of waking you up might have caused us to miss the flight~"
                        p "Careful, there are other people here!"
                        scene p15 with dissolve
                        p "Like Kaira!"
                        scene p16 with dissolve
                        s "That's coz we're all going on this trip together!"
                        s "Not just me, but [mr] too!"
                        scene p17 with dissolve
                        m "That's right, [p]. Good morning to you too. So, since we're all together..."
                        scene p18 with dissolve
                        m "Remember to behave, alright?"
                        p "You got that, Nicole?"
                        n "I'll be on my best behaviour."
                        m "Fufufu~"
                        scene p19 with dissolve
                        p "Let's not dilly dally and let's start loading up the bags."
                        s "What? Not even a hug for your [sr]?"
                        n "We'll have plenty of time for that later, Kaira. And I call dibs."
                        scene p20 with dissolve
                        m "Let's move out now, and then you can do more shopping later, Kaira!"
                        s "Hehehe!"
                        p "By the time we're back, these bags will be full!"
                        scene black with fade
                        scene p21 with fade
                        $ renpy.pause()
                        "Things are moving forward now, and I can't wait to see what will happen."
                        "Nicole will be definitely be trying to jump into my pants, but what about Kaira?"
                        "To be honest, I'm still not sure where I stand with her. If she pushes things forward, if Nicole decides to have her fun..."
                        "How am I supposed to react? Should I just let it happen?"
                        "And then there's the issue with [mr]. I still don't know how to interpret what's happened so far."
                        "Was what we did... a one off thing? Is she open to it again? She makes me feel like maybe its not the aphrodisiac after all."
                        "..."
                        "These thoughts occupy my mind as we arrive at the airport. Ha..."
                        "We don't have to line up though. It's just us on this flight."
                        "I can't wait to see their reactions!"
                        jump hol_plane
                    "No":
                        jump kaira_room
            "No, not ready to go yet.":
                jump kaira_room

    scene k-1
    p "How's my beautiful [sr] doing?"
    scene k-3
    s "Oooh!"
    s "So that's what [mr] means she says you have a silver tongue! You must do great around the ladies."
    p "I'm doing alright around you aren't I?"
    s "Alright alright! We'll talk later okay? I have to do some work first!"
    jump kaira_room
