label Caroline:
    call hidescreens from _call_hidescreens
    if carolinelvl == 1 and carolinebarlvl == 1:
        scene black
        scene cc-1 with fade
        p "Hey there. Caroline right?"
        scene cc-2 with dissolve
        c "...?"
        scene cc-3
        c "Oh hey! You're the guy at the bar when I was working."
        p "That's me."
        p "Um, would you mind if I joined you?"
        c "Not at all!"
        scene cc-5 with dissolve
        c "So, it's [p], isn't it?"
        p "You remember my name! But of course, you must have a great memory."
        scene cc-6
        c "I also remember you guys getting quite wild, you even had to carry your [sr] away."
        p "Yeah, I didn't think we would actually get to that haha."
        p "So what are you doing here?"
        scene cc-9
        c "A cup of coffee is my favourite thing in the morning."
        c "I also bring some notes so that I can study while I enjoy my coffee."
        scene cc-5
        c "Just perfect, ah~"
        p "Looks like you've got a nice deal sorted for yourself here."
        scene cc-4
        c "And what about you?"
        if "water" in items and not "coffee" in items:
            scene cc-8
            c "You've come to a cafe to buy water."
            c "Hehehe, allergic to coffee?"
            p "Yeah, money's a little tight right now."
            scene cc-16
            c "Aww that's okay. It's hard to find a job in today's market."
        if "water" in items and "coffee" in items:
            scene cc-5
            c "You've got a coffee {i}and{/i} water."
            c "Is the coffee too strong by itself?"
            p "I just couldnt decide which one to buy, so I bought both."
        if "coffee" in items and not "water" in items:
            scene cc-5
            c "You bought a cup of coffee - I see you've got a similar taste to mine."
            p "I love coffee."
            p "It's like, I don't even have blood in my veins, it's all coffee pumping through."
            scene cc-9
            c "I've found a kindred spirit!"
        scene cc-12
        c "I take it you're not a regular?"
        p "Whoa, how would you know, are you my stalker?"
        scene cc-13
        c "Hmm..."
        c "I come here {i}everyday{/i}, [p]. I think I'd have seen you if you do come around a bit."
        p "Alright, I'll come clean. I've only come here recently."
        p "I used to live here actually, but I moved away to study. But now that's done, so I'm here."
        scene cc-5
        c "Oh so you've already graduated?"
        p "Oh no, um. Something went wrong and I had to leave early."
        scene cc-16
        c "Ah, sorry I brought it up."
        p "That's no problem at all."
        scene cc-4
        c "..."
        p "So how long have you been working at the bar for?"
        scene cc-5
        c "Oh, for a few months. I work every night, so come say hi if you can!"
        p "Oh I will."
        p "What are you studying now?"
        scene cc-6
        c "I am studying... well, reviewing the criteria for the diagnosis of mental disorders."
        p "Ah so that's like DSM-5 criteria?"
        scene cc-12
        c "The DSM-5 is more like... a guideline."
        scene cc-5
        c "I would say if anyone is suffering mentally, then it's up to the clinician to render treatment that's tailored to the individual."
        p "Wow, you sound like a really empathetic person."
        p "I'd want you to be my doctor if I'm ever sick in the head!"
        scene cc-9
        c "You joke about it now, but mental illness is more like a spectrum, and we're all on it!"
        c "Whether you cross the line or not depends on many things, like your environment, the choices you make, and the potential consequences."
        p "You're saying our choices do matter."
        scene cc-14
        c "We are what we do."
        p "Absolutely fascinating..."
        c "Hahahaha!"
        p "Erm, I hope I haven't been distracting you from your study."
        scene cc-4
        c "I enjoy the break from the monotony, it's nice to have someone to talk to."
        p "Well, I've got another question."
        scene cc-5
        c "Yes?"
        p "That girl who was sitting next to me at the bar - you know her?"
        scene cc-15
        c "Ah, her name's Camille."
        scene cc-5
        c "It's rare for her to come up to the bar. She usually hangs out at the premium lounge."
        p "Is she quite shy?"
        scene cc-6
        c "I.. suppose. Why, are you interested?"
        menu:
            "I'm interested in all women I meet.":
                $ depravity += 1
                scene cc-14
                c "How bold!"
            "No, just curious.":
                scene cc-13
                c "Really?"
        p "I'm sorry, would you rather me talk about you instead?"
        scene cc-9
        c "Bahaha!"
        scene cc-11 with fade
        c "Oh dear, I've had a lot of fun, but my coffee is almost finished."
        p "Time flies when you're having fun."
        scene cc-5
        c "I have to go now, I'll see you tomorrow if you come around again. Otherwise, ta~!"
        scene cc-4
        p "Laters."
        scene cc-17 with dissolve
        "Hmm, this town ain't so bad."
        "Maybe I should go and see her tonight at the bar?"
        $ carolinelvl += 1
        call daykeep from _call_daykeep_4
        jump map
    if carolinelvl == 2 and carolinebarlvl == 2:
        scene black
        scene cc-1 with fade
        p "Caroline!"
        scene cc-2 with dissolve
        c "[p]!"
        scene cc-3
        c "Please, take a seat!"
        p "Gladly."
        scene cc-5 with dissolve
        p "You really do like to come every morning."
        c "It's true - I can't survive without my coffee."
        p "How many do you have a day?"
        scene cc-4
        c "Hmmm..."
        scene cc-5
        c "Three?"
        p "Whoa, three!"
        p "Surely, doctor, that's not good for you?"
        scene cc-6
        c "I'm not a doctor yet."
        c "It's the coffee withdrawal that's the bad part."
        c "That's why I can't stop."
        p "A hostage to your vices, Caroline!"
        scene cc-14
        c "It's not such a bad thing, it helps me concentrate anyway."
        scene cc-6 with dissolve
        c "Maybe you'll think of dabbling more into coffee? It's a great pastime."
        p "Yeah, sure. Teach me about it."
        p "That is, if it won't get in the way of your study."
        scene cc-9
        c "No, no- I don't mind. It's always nice to take a break for company."
        c "What would you like to know?"
        p "What's the difference between instant coffee and the one they have here?"
        scene cc-5
        c "There's a huge difference."
        p "How?"
        scene cc-6 with dissolve
        c "Can't you taste the difference?"
        p "Umm..."
        scene cc-14
        c "Hahaha!"
        c "Let me explain..."
        scene coffee with dissolve
        c "The espresso here is made from freshly ground beans. The fresh part is important."
        c "This is because the oils in the beans haven't evaporated yet. It's the oils that give it that great taste."
        c "The espresso is basically super concentrated coffee. It's a bit too strong for most people though."
        c "That's why we might add milk or water to it."
        c "Instant coffee is... well, not like espresso."
        p "Huh! So coffee is espresso plus milk?"
        scene cc-4 with dissolve
        c "Anything with espresso is coffee. There are just different ways of having it."
        c "For example, a Latte is espresso with some milk added to it."
        p "Oooh! So that's what the names mean."
        p "What's a 'cup of chino' then?"
        scene cc-6 with dissolve
        c "Do you mean a Cappuccino?"
        p "Yeah, that."
        scene cc-5
        c "It's like a Latte, except the milk that is added is more frothy."
        p "Frothy?"
        c "Yup, they have a milk frother which heats up the milk and sort of makes it creamier."
        p "Creamy! Yum."
        p "Which kind of coffee do you like the most?"
        scene cc-12
        c "For me, it's a Latte everytime. I love milk, but a Cappuccino is just too airy for me."
        p "Fair enough."
        p "So for you it's not just about getting the caffeine to help you study."
        scene cc-9 with dissolve
        c "Coffee is an experience."
        c "From cupping it in your hands, feeling the warmth of the coffee, and the hustle bustle of life."
        p "What are you thinking of now?"
        scene cc-15 with dissolve
        c "..."
        scene cc-8 with dissolve
        c "I'm thinking I'm having a pleasant time."
        c "But! All good times {i}must{/i} come to an end."
        p "Hang on-you're leaving?"
        scene cc-6
        c "I'm meeting up with some friends to do some group study."
        p "Weren't you already studying?"
        scene cc-5
        c "Group study is useful sometimes for remembering things."
        c "We all study up on something and teach each other about it, and it helps us remember what we study more."
        scene cc-9
        p "Study with me! I'm an empty tea cup. I'll learn anything you have to teach."
        c "I'll tell you a few things next time, but I really have to go now."
        p "See you!"
        c "Take care, [p]."
        scene cc-17 with dissolve
        $ carolinelvl += 1
        call daykeep from _call_daykeep_18
        jump map
    if carolinelvl == 3:
        scene black
        scene cc-1 with fade
        p "Good morning, Caroline!"
        scene cc-2 with dissolve
        c "Ah, [p]."
        scene cc-3
        c "I was wondering when you'd get here."
        scene cc-5 with dissolve
        c "So, what have you been up to?"
        p "I'm up to some learning, that's what."
        scene cc-6
        c "Learning?"
        p "Where we left off last time, you said you'd teach me about what you're studying."
        scene cc-8
        c "You're an eager beaver, what's up?"
        p "Oh you got me."
        p "I really just want to hear your voice."
        scene cc-13 with dissolve
        c "Oh gee..."
        c "Cheesy line, [p]!"
        p "Yeah well, did you like it?"
        scene cc-6 with dissolve
        c "I can always appreciate an honest guy."
        c "Question is: Do you say this to all the girls?"
        menu:
            "Only the pretty ones.":
                $ depravity += 1
                scene cc-8
                c "Daring play, [p]."
                p "Is it working?"
                c "Let's find out."
            "Just you.":
                scene cc-12
                c "Are you hitting on me?"
                p "Am I?"
                c "That's up to you."
        scene cc-15 with dissolve
        c "..."
        c "It's a pity."
        scene cc-16
        c "A relationship isn't really what I'm looking for at the moment."
        c "My study takes up a lot of my time - medicine is as time consuming as they say."
        c "I'm sorry [p]."
        "...wasn't she leading me on?"
        p "Hey, that's okay."
        p "Worth a try right?"
        scene cc-10
        c "Don't get me wrong, [p]. I like you, and I like your company. I enjoy talking to you."
        c "I just don't have the time to commit to a relationship."
        p "That's all good."
        p "I like it just the way it is right now."
        p "I mean, what we've got going on right now... chatting over coffee."
        p "Making plans to meet again in the future..."
        p "We're virtually dating already!"
        scene cc-5 with dissolve
        c "Interesting point of view."
        p "I'll never come between you and your studies, and I don't want you to sacrifice that for me. Never."
        c "That's considerate of you."
        p "Guess what I'm trying to say is. I'm not asking for a lot of commitment."
        p "I... just wanted to let you know where I was coming from."
        scene cc-4
        c "Well, [p], I appreciate your frankness."
        c "I really do."
        scene cc-6
        c "If we're already virtually dating, why don't we keep it up then?"
        p "Lets!"
        p "Hey, you mentioned last time you'd teach me a few things about what you're learning?"
        scene cc-4
        c "Yeah, I love teaching. It helps me remember it better too."
        p "What is it that you're learning right now again?"
        scene cc-5
        c "Psychiatry."
        p "That's similar to psychology right?"
        c "Well, similar, yes, but different."
        p "What's the difference? Always seemed quite similar to a layperson like myself."
        scene cc-12 with dissolve
        c "How can I put it..."
        c "Psychiatry is about dealing with mental diseases - the more disabling ones."
        c "You would need to know how the human mind works for both, but practically psychiatrists would deal with mental illnesses like severe depression, and schizophrenia."
        p "Oh so you're more into mental illnesses then?"
        scene cc-9
        c "Well, it's what I'm studying right now."
        p "Something that I know of is called schizophrenia. What exactly is that?"
        scene cc-8
        c "Well, it's the one that people typically think of when you say someone's psychotic."
        p "Psychotic as in crazy?"
        c "It's a specific kind of crazy. Technically, people who are psychotic hear or see things that aren't there."
        p "Ah, that kind."
        scene cc-9
        c "Of course, psychosis is just a symptom. Many things can cause psychosis, just like how many things can cause chest pain."
        p "Such as?"
        scene cc-12 with dissolve
        c "For chest pain?"
        p "Sure."
        scene cc-5 with dissolve
        c "A lot of things can cause chest pain. A heart attack can. A pulmonary embolism, pneumonia, reflux, costochondritis are just some other examples that can all cause chest pain."
        c "Of course, pulling your pectoralis major muscle during your bench-pressing at the gym will also cause chest pain."
        p "Oh I see. What's the most common cause of, um, psychosis?"
        scene cc-6
        c "Well, schizophrenia probably jumps to people's minds the first, but the most common is probably drug-induced. Taking methamphetamine and other illicit drugs..."
        p "Cannabis is safe though, right?"
        c "Well, it's what a lot of people like to believe, but it's also a common cause for psychotic presentations."
        p "Hmm, that's not what reddit told me. Everything in moderation, huh?"
        scene cc-9
        c "Definitely."
        c "Phew, that was good revision."
        p "Man, Caroline, you know a lot."
        c "Thank you, I spent a long time studying it!"
        p "You've also got a ton of passion for this kind of stuff."
        p "Teach me more!"
        scene cc-12 with dissolve
        c "That's a large topic, [p], and... one that we might not have time for."
        p "Are you going already?"
        scene cc-11 with dissolve
        c "Yes, I'm sorry, but- yes."
        scene cc-4
        c "But listen, maybe next time we could do something else? After coffee? I'll free up some time."
        p "Um, of course! I'd love to, did you have something in mind?"
        scene cc-14
        c "I'll... leave that up to you! Gotta go! Take care, [p]!"
        scene cc-17 with dissolve
        "Huh, I'm glad she's come around and found some time for me in her busy schedule."
        "But now the pressure's on me to find a place after the morning coffee..."
        "I'll come up with something."
        $ carolinelvl += 1
        call daykeep from _call_daykeep_17
        jump map
    if carolinelvl == 4:
        scene black
        scene cc-2 with fade
        p "Good morning Caroline."
        scene cc-3 with dissolve
        c "Hello, [p]. Will you be following up with your promise today?"
        p "Promise?"
        c "You remember the promise?"
        c "I freed up my schedule for this, you know. Where are we going?"
        p "Ah you were talking about that."
        scene cc-4 with dissolve
        p "You're in such a rush! Let's have a drink first."
        "Oh shit, I haven't thought of a place to go yet!"
        scene cc-5 with dissolve
        c "Oh, we are definitely having a coffee first, but I'm curious about your grand plans!"
        p "Grand? Ahahahah..."
        p "Really, really, you're putting the pressure on me!"
        scene cc-6 with dissolve
        c "No pressure."
        p "It's a suprise, Caroline."
        scene cc-9 with dissolve
        c "Ooh, I don't know how I feel about surprises."
        p "Take a guess."
        scene cc-13 with dissolve
        c "Hmmm... how about a clue?"
        p "Uh, it's a cool place that you probably want to go to very much."
        c "A cool place, that I want to go to..."
        scene cc-12 with dissolve
        c "Are we going to the music theatre?!"
        scene cc-14 with dissolve
        p "Bingo! That's exactly where I'm taking you! Ahaha...ahahha..."
        "Well played, [p], well played. This trick always works."
        "But damn, what the hell am I going to do at the music theatre?"
        c "Are we watching a musical, listening to a concert?"
        p "Um..."
        "Ah, shit."
        p "It's uh, a surprise."
        scene cc-9 with dissolve
        c "I love music. It's nice to know that you also appreciate that sort of thing."
        c "How did you come across the music theatre?"
        p "I went once or twice back when I was in high school."
        p "Never really to watch any shows - I'd go to one of the side rooms and have fun with some of the instruments."
        scene cc-5 with dissolve
        c "Do you play anything?"
        p "Not anything well, haha. But yeah, I like to just make some noise sometimes."
        scene cc-6 with dissolve
        c "It's like a release, I know what you mean."
        p "Do you play anything?"
        scene cc-4 with dissolve
        c "I've been playing the piano since I was a child, so I suppose I can play that quite well."
        c "I've also tried playing the violin, but that wasn't as fun."
        p "That's amazing. You didn't like the violin?"
        scene cc-12 with dissolve
        c "Getting started with the violin is always hard. A lot about sounding good is about how you draw the bow across the strings."
        c "With piano, there's not much skill - you just hit the note."
        c "With the violin, I was sounding really horrible, so I just thought I'd maybe revisit it another day."
        scene cc-13 with dissolve
        c "And you know what? That day never came."
        p "I reckon being good at the piano is awesome enough."
        scene cc-8 with dissolve
        c "Thank you, [p]. So, what have you been up to recently?"
        p "Just finding my feet. Making friends. Talking to... cool people like you!"
        c "Aww, aren't you nice."
        scene cc-6 with dissolve
        c "You know, I've been thinking. We're chatting quite pleasantly right now, and I like your company."
        c "But, what inspired you to come over in the first place?"
        p "I met you at the bar, remember? I always like saying hi to a familiar face."
        c "Oh that's right."
        p "You didn't remember? You even told me that you like to keep things professional at work, haha."
        scene cc-13 with dissolve
        c "Oh, I tell a lot of people that, [p]. It's hard to keep track sometimes."
        p "Very good. A very popular lady."
        scene cc-14 with dissolve
        c "No, I'm not!"
        p "You get hit on at the bar, no?"
        scene cc-6 with dissolve
        c "By drunk guys. They'll hit on anybody."
        p "Ever get hit on by girls?"
        scene cc-8 with dissolve
        c "Of course, but they're drunk too!"
        p "You ever get to have any fun, you know, enjoy yourself?"
        scene cc-12 with dissolve
        c "I'm a professional, [p]! I wasn't interested."
        scene cc-4 with dissolve
        p "You know, {i}I{/i} wasn't drunk when I said hi to you."
        p "Just something to keep in mind, you know, just saying."
        scene cc-9 with dissolve
        c "Haha, what's your point?"
        p "I'm a sincere guy, a real professional too."
        p "Someone with uh, integrity."
        scene cc-8 with dissolve
        c "Good character traits to have."
        p "I'm happy you think so too!"
        ## Time passes
        scene black with fade
        scene cc-5 with dissolve
        c "Are you ready to head off?"
        p "Let's go."
        scene cc-17 with dissolve
        "Oh no, I haven't actually got anything prepared."
        "Damn, it looks like I'll just have to wing it."
        ## Time passes
        stop music fadeout 1
        scene black with fade
        "A few moments later..."
        c "This is interesting, [p], we've left the theatre."
        c "Are we not watching a show?"
        p "We're going to one of the side rooms - surprise! Hahaha..."
        play music "sounds/yu.mp3" fadeout 1
        scene cc-43 with fade
        c "What a twist!"
        scene cc-18 with dissolve
        p "I was thinking, why watch a show, listen to music, when we can make our own?"
        scene cc-44 with dissolve
        c "Wow, it's almost like a library in here!"
        p "Aha, of course you would love the books."
        scene cc-45 with dissolve
        p "But I think the main character here is the grand piano in the middle."
        c "It's hard to miss it, for sure."
        scene cc-19 with dissolve
        p "I came here a bit when I was in high school and this was always a calm place where I could get away from it all."
        c "You come here by yourself?"
        p "Those who don't enjoy solitude cannot enjoy freedom."
        scene cc-21 with dissolve
        c "Didn't know you were a poet too, [p]."
        scene cc-18 with dissolve
        p "It's not my quote. My old math teacher used to write a quote on the whiteboard everyday, and this one resonated with me."
        scene cc-20 with dissolve
        c "Well this time, you're not alone."
        c "Are you going to play something?"
        scene cc-26 with dissolve
        p "I was never any good, and besides, it's been a while anyway."
        p "Maybe you could grace this place with some music?"
        scene cc-22 with dissolve
        c "I haven't played in a long time either!"
        scene cc-23 with dissolve
        c "But, let's see if I can improvise something."
        scene cc-24 with dissolve
        p "Improv? That takes some skill, doesn't it?"
        scene cc-25 with dissolve
        p "I'm pretty much stuck on trying to read whatever's on the music sheet."
        c "Oh, anyone can improv! Improv that sounds nice is the challenge..."
        scene cc-26 with dissolve
        p "I guess, but for the sake of prosperity, maybe I'll stay away from the improv myself."
        scene cc-27 with dissolve
        c "Just letting you know, don't expect too much, okay!"
        scene cc-28 with dissolve
        "Caroline gracefully stretched across the piano seat with a sense of familiarity and ease."
        "I could tell at this point, that this was a woman of class, confidence and elegance."
        "Yet above all, she exuded beauty in spite of her conservative manner of dress."
        "I... guess I'm starstruck."
        scene cc-27 with dissolve
        p "I can't stand the anticipation."
        c "Oh, stop. Anyway!"
        c "Here goes."
        ## play music
        scene cc-29 with fade
        "Um, let's see..."
        play music "sounds/caroline.mp3" fadeout 1
        "♫"
        scene cc-29
        $ renpy.pause(24.0,hard=True)
        stop music
        "How honest, and vulnerable at the same time. Is this you, Caroline?"
        p "Wow, that was beautiful. Really suits the atmosphere in this place."
        p "That was comfy."
        scene cc-30 with dissolve
        c "Thanks. I ended the tune with a funny chord. I think it made it sound more wistful."
        p "Are you going to make that into a full song at any stage?"
        scene cc-31 with dissolve
        c "Ooh, I might. But that's one of the great things about sitting down at the piano and playing what comes to mind."
        c "You get these short pieces and ideas, some you won't remember but if it's good enough, you'll write it down."
        p "This one has potential."
        scene cc-32 with dissolve
        p "I can imagine sitting in another room, next to the fireplace in the middle of a rainy day."
        scene black with fade
        p "The music floating through the hallway..."
        play music "sounds/caroline.mp3"
        scene cc-33 with fade
        c "And with a mug of coffee in hand?"
        p "That's my idea of a good time."
        menu:
            "A good looking girl next to me wouldn't hurt.":
                $ depravity += 1
                scene cc-34 with dissolve
                c "That's great to know, [p]."
            "Having someone else to share it with wouldn't hurt.":
                scene cc-34 with dissolve
                c "And would that somebody be me?"
                p "It could be. I don't discriminate."
                scene cc-35 with dissolve
                c "Ha!"
        scene cc-37 with dissolve
        c "So how are you rating this date?"
        p "It's not bad. It's just the start."
        p "What do you reckon?"
        scene cc-36 with dissolve
        c "I think it's very original and creative."
        p "Like Dante's original."
        scene cc-39 with dissolve
        c "You do love that drink very much, don't you? I should get you a week's supply for your birthday!"
        scene cc-38 with dissolve
        c "But as I was saying, this was an original date, [p], and that's endearing."
        p "If this is endearing, you'll love part two."
        c "You've done this much already, let me handle our next destination."
        scene cc-32 with dissolve
        p "Taking charge!"
        scene cc-40 with dissolve
        c "I want to share my studio apartment with you - it's a slice of heaven."
        c "And a good place for me to teach you more about coffee!"
        p "Oh, what's so special about this apartment?"
        scene cc-41 with dissolve
        c "It's... ambient. I think you'll enjoy the aesthetic."
        p "You're setting high expectations."
        c "Oh, its not fancy, that's not what it's about. It's just a nice place, like this one you know?"
        c "You feel wholesome."
        p "Like nothing can go wrong."
        p "If those are the vibes, than give me more."
        scene cc-42 with dissolve
        c "That's what I'm saying! So come on, let's go!"
        stop music fadeout 1
        scene black with fade
        "Does she like me?"
        "I think I felt a skip in my heart beat."
        "Is this what its like? To feel strongly attracted to someone?"
        ## transition
        play music "sounds/something.mp3" fadeout 1
        scene cc-46 with fade
        c "Welcome to my abode."
        p "Wow, nice place!"
        scene cc-47 with dissolve
        c "Take a look around!"
        p "I would love to."
        scene cc-48 with dissolve
        $ renpy.pause()
        scene cc-49 with dissolve
        $ renpy.pause()
        scene cc-50 with dissolve
        $ renpy.pause()
        scene cc-51 with dissolve
        $ renpy.pause()
        scene cc-53 with dissolve
        $ renpy.pause()
        scene cc-52 with dissolve
        $ renpy.pause()
        "This is really spacious and there are industrial flavours, its very much modern."
        "Mhmm. Even the tubes on the ceiling. I wonder if this place was ever like a warehouse or something that was repurposed."
        "With a killer view to boot as well."
        "All in all, not too shabby!"
        scene cc-54 with dissolve
        p "When you said it was all wholesome and ambient, I was expecting something with darker colours."
        p "More... earthy?"
        scene cc-55 with dissolve
        c "Oh I get what you mean. Wood and all that right?"
        scene cc-56 with dissolve
        c "The fireplace crackling, and all that."
        c "But this is a different feeling. It's clean and contemporary."
        scene cc-60 with dissolve
        c "You wake up in the morning and you feel like you're going to be productive."
        scene cc-57 with dissolve
        p "You've really got your life in order, wow!"
        c "It's a feeling of potential."
        p "So what's the average day for you like?"
        scene cc-58 with dissolve
        c "I wake up in the morning, get changed, and then I-"
        scene cc-57
        p "Go to the cafe for coffee?"
        scene cc-61 with dissolve
        c "Ah, I'm that predictable, aren't I?"
        scene cc-60 with dissolve
        p "Well, I do see you there every morning."
        p "What after that?"
        scene cc-59 with dissolve
        c "Oh I might come back home, I might go to a lecture, or I might go to the library."
        scene cc-62 with dissolve
        p "By the way, nice TV!"
        scene cc-63 with dissolve
        p "What do you watch?"
        c "Umm, I don't really watch television, but I do play games occassionally."
        scene cc-64 with dissolve
        p "You're a gamer?"
        c "Sometimes, I don't get much time usually though."
        p "Neat."
        scene cc-65 with dissolve
        p "Hang on, is that a coffee maker over there?"
        p "Then how come you always go to the cafe?"
        scene cc-66 with dissolve
        p "Looks like a fairly robust machine too. I'm sure you could pump out some good joe with this."
        scene cc-67 with dissolve
        c "Oh I can, but like I said, cafe in the mornings is a ritual."
        c "It's the hustle and bustle of people. It's the way coffee is supposed to be had - with other people!"
        c "It's no fun having it by yourself."
        scene cc-56 with dissolve
        p "Well, I'm here now, right? What say we enjoy one together?"
        c "I'd love to show you more about coffee."
        scene cc-70 with dissolve
        c "How do you take it?"
        p "Um, what are the options again?"
        scene cc-68 with dissolve
        c "Well you could always just have a shot of espresso, but that's no fun by itself."
        scene cc-69 with dissolve
        c "So how about a latte?"
        p "I'll take you up on that offer."
        c "Great. You know, this is one of the reasons I bought a coffee machine."
        scene cc-67 with dissolve
        c "To share with other people."
        p "I think that's very generous of you."
        c "Just make yourself at home, [p], I'll only be a few minutes."
        p "Sure, I'll just chill out here."
        scene cc-71 with dissolve
        "Despite what Caroline says, this place is quite fancy."
        "There's a beautiful view and if I woke up to this everyday, I'd be motivated and productive."
        scene cc-72 with dissolve
        p "I'll just crash on the couch."
        scene cc-74 with fade
        p "Mmm... so comfortable!"
        scene cc-73 with dissolve
        c "Relaxing, [p]?"
        p "Oh definitely. In such a lovely place, anyone would be."
        scene cc-75 with dissolve
        p "Relaxing and, uh, checking something out on my phone."
        c "Whatcha looking at?"
        scene redbubble with dissolve
        p "Just some coffee mugs"
        scene cc-76 with dissolve
        c "Thinking of getting your own coffee setup already? Have I converted you into the life of coffee yet?"
        scene redbubble2 with dissolve
        p "Maybe. I'm just taking a look at some custom mugs."
        c "Do they look good?"
        p "Not bad. Price seems alright."
        p "How's the coffee coming along?"
        scene cc-77 with dissolve
        c "Err, just a moment. I've almost finished the second. The second one always tastes better than the first, so I'll give you that one."
        p "Oh, thanks!"
        scene cc-78 with dissolve
        c "But let me just say, I like how these ones are turning out!"
        scene cc-75 with dissolve
        p "I'm looking forward to it!"
        "I wonder how the coffee would look in these mugs..."
        c "Hey, [p]!"
        p "Yeah?"
        scene cc-79 with dissolve
        c "The coffee's ready, come on over!"
        p "Oh boy!"
        ## coffee done
        scene cc-80 with fade
        c "Here, one for me, and one for you."
        c "Extra milk for you!"
        scene cc-81 with dissolve
        p "Mmmm..."
        p "Smells good. So does the coffee."
        c "Wow, that was smooth!"
        scene cc-82 with dissolve
        c "Go on, have a taste."
        p "Alright, let's have a taste!"
        scene cc-83 with fade
        p "Mmm, mmm, mmmMM!"
        p "It tastes really creamy. Good job!"
        scene cc-84 with dissolve
        c "Nice!"
        c "That's the frothed milk. But what do you think about the beans?"
        scene cc-87 with dissolve
        p "The beans themselves? Ooh I'm not sure I'm that good at picking that out."
        c "I'm using some Kenyan beans, and they're more stronger than say, the one at the cafe, don't you think?"
        p "I guess, but it's subtle. I might not have picked it up if you didn't say so."
        scene cc-84 with dissolve
        c "The strength, or the bitterness, is a slap in the face to really help me wake up sometimes."
        c "That's why I sometimes go for it over fruitier flavours."
        p "You really {i}do{/i} know your stuff."
        scene cc-85 with dissolve
        c "Oh, I just experiment and see what works for me. That's all."
        c "I might be completely wrong! This is just the way I analyse it."
        scene cc-86 with dissolve
        c "How do {i}you{/i} see it?"
        p "Hmm, my analysis?"
        p "I'd say... this coffee is like... you!"
        p "You started off with the espresso, which is like the serious and bitter stuff, but you have mixed with it the milk, which is creamy and good."
        scene cc-89 with dissolve
        c "That's an interesting metaphor."
        p "Like, there's a seriousness to your character but you're smooth and cool at the same time. You know?"
        scene cc-90 with dissolve
        c "That's a nice compliment, I suppose. I haven't really thought of myself as a cup of coffee before."
        p "It {i}is{/i} something you're associated with though, isn't it?"
        p "Careful, Caroline. Drink too many and you might turn into actual coffee!"
        c "You think!"
        scene cc-91 with dissolve
        c "That wouldn't be such a bad thing. I think I'd make as a nice cup of coffee."
        p "Not too bitter, I hope!"
        c "I would be the sweetest cup of coffee."
        p "I'd drink that."
        scene cc-88 with dissolve
        c "I'd be offended otherwise, haha!"
        scene cc-92 with dissolve
        p "Haha, oh man. The cream's a little heavy. I'm feeling a bit drowsy."
        c "Aha - that's why I had less milk."
        p "I thought coffee was meant to make you feel more awake."
        scene cc-93 with dissolve
        c "Hmm, maybe it would be better for you to have just coffee without the milk next time~"
        c "You can have a rest if you want. I'm not going to be doing too much anyway."
        scene cc-94 with dissolve
        p "{i}Yawn...{/i} just a quick rest."
        scene cc-95 with dissolve
        p "What are you gonna do in the meantime?"
        scene cc-96 with dissolve
        c "More study...."
        scene cc-95 with dissolve
        c "So in the meantime, just take a rest on the couch, and let me know if you need anything."
        p "What are you gonna be doing for real?"
        c "I'll pop into my room to get changed then I'll just study on the table."
        p "Right on."
        scene cc-97 with dissolve
        "Fuck this couch is nice."
        "Caroline's really got it together."
        "Responsible, ambitious... could I ever be like that?"
        "Man, she's the opposite of Nicole. Of course, everything has its pros and cons, but I could really appreciate this feeling of peace with Caroline."
        "Zzz..."
        scene black with fade
        play music "sounds/yu.mp3" fadeout 1
        $ renpy.pause()
        ## Dreams scene
        p "Uh, Caroline?"
        c "Yes, [p]?"
        scene cd-1 with fade
        $ renpy.pause()
        scene cd-2
        pause (0.2)
        scene cd-3
        pause (0.2)
        scene cd-4
        pause (0.2)
        scene cd-5
        pause (0.2)
        scene cd-6
        pause (0.2)
        scene cd-7
        $ renpy.pause()
        scene cd-8 with dissolve
        "When I'm with you, I feel like I could rise above it all and be a better person."
        "You inspire to me to improve."
        "I only hope that I could do a fraction of that for you."
        stop music fadeout 1
        scene black with fade
        "Zzz..."
        $ renpy.pause ()
        ## end
        scene cc-98 with fade
        p "Urgh... how long was I out for?"
        play music "sounds/something.mp3" fadeout 1
        c "Welcome back, [p]."
        scene cc-99 with dissolve
        p "Oh hey! Good morning Caroline."
        p "Whoa, where are your clothes? Am I still dreaming?"
        scene cc-100 with dissolve
        c "This is no dream, [p]."
        c "Sorry if I'm embarassing you. I'm one of those girls that feel more comfortable in just her skin."
        c "Especially when I'm at home."
        scene cc-101 with dissolve
        "Oh my god. I never thought I'd be able to see Caroline like this."
        "She's really... oh wow."
        scene cc-103 with dissolve
        p "Oh on, I'm not embarassed. I just thought that {i}you{/i} might be?"
        c "In medical school we get very used to the idea of bodies, and we often practise phsyical exams on each other."
        scene cc-102 with dissolve
        c "I guess, I'm pretty used to the idea of people seeing my body."
        c "I probably would have been more insecure about it before medschool though!"
        scene cc-134 with dissolve
        c "Speaking of which... there's still so much work left to do."
        p "You've got nothing to be insecure about."
        scene cc-103 with dissolve
        c "Thank you, you're sweet."
        scene cc-104 with dissolve
        c "I've been sitting down the whole time! I can barely feel my legs."
        scene cc-105 with dissolve
        c "Aah~! That feels good!"
        scene cc-106 with dissolve
        c "So, did you have a sweet dream?"
        p "Err, dream?"
        scene cc-107 with dissolve
        c "You were mumbling stuff in your sleep. It was pretty funny!"
        p "Ah..ahahha..."
        p "Nothing too incriminating, I hope."
        p "It was an okay dream."
        p "..."
        p "Did I say anything?"
        scene cc-108 with dissolve
        c "It didn't make sense entirely, but I felt like you were dreaming about someone important to you."
        c "Wanna talk about it?"
        scene cc-109 with dissolve
        p "Haha, there's not much to talk about."
        p "It was good dream, though. It's rare for me to have that kind of dream."
        scene cc-110 with dissolve
        c "What do you usually dream about?"
        p "It's pretty messed up stuff haha."
        scene cc-111 with dissolve
        c "Well it sounds like you just got a break. Told you this place has good vibes."
        p "Maybe you're right. I should come here more often then."
        scene cc-112 with dissolve
        c "Taking advantage of my hospitality, [p]?"
        p "I'll make it worth your while, promise."
        scene cc-111 with dissolve
        c "I'll hold you to that."
        scene cc-113 with dissolve
        c "So, what do you think about the view?"
        p "The view?"
        scene cc-114 with dissolve
        p "Not bad I'd say. Not bad at all."
        scene cc-115 with dissolve
        p "Let me get a closer look."
        scene cc-116 with dissolve
        c "Look, you can even see the shops on the other side."
        p "Oh you were talking about that view?"
        scene cc-117 with dissolve
        c "Oh [p], you're incorrigible!"
        p "That's a big word."
        menu:
            "It's not the only big thing about me.":
                $ depravity += 1
                c "Be careful not to set expectations too high~"
            "Oh I'm not so bad.":
                c "I really don't mind, [p]. I think it's funny!"
        scene cc-118 with dissolve
        p "How was your study?"
        scene cc-117 with dissolve
        c "It was good. I felt productive."
        p "You're always working so hard. You'll really make it big one day. You're gonne be a champ, I know it."
        scene cc-119 with dissolve
        c "Oh stop I'm going to blush."
        p "But no really. You're so smart and beautiful at the same time. It's just not fair. Really."
        scene cc-120 with dissolve
        c "[p]!"
        c "Oh now I'm really going to blush."
        p "I'm talking from my heart."
        scene cc-121 with dissolve
        p "I just think you're really attractive. And as man, I like to put my best foot forward."
        p "Come here, Caroline."
        scene cc-122 with dissolve
        c "..."
        c "Oh what the hell..."
        scene cc-124 with dissolve
        c "You're so good at this, aren't you?"
        p "We're all just trying our best in this world, aren't we?"
        scene cc-125 with dissolve
        c "{i}Sigh{/i}... [p]..."
        scene cc-126 with dissolve
        c "Oh, alright."
        scene cc-127 with dissolve
        c "Mmm~"
        "Caroline... I think I'm in love."
        scene cc-128 with dissolve
        c "(Oh I've forgotten how this feels like...)"
        scene cc-129 with dissolve
        c "..."
        p "Well, well well."
        scene cc-130 with dissolve
        c "You're not half bad."
        p "Ah, but you were better."
        scene cc-131 with dissolve
        c "Ahem! I've got work soon! I've got to get changed."
        p "Right, at the bar. Is it that time already?"
        p "It's like they say, time flies."
        scene cc-132 with dissolve
        c "I'll... have to change into my uniform. Give me a moment alright?"
        scene cc-133 with dissolve
        c "I'll be right back."
        scene cc-135 with dissolve
        "My god, what was that moment?"
        "I just kissed a girl and I felt like I had to somewhat work for it."
        "Caroline, Caroline, Caroline."
        scene cc-136 with dissolve
        "It is truly a beautiful day today."
        "What a gorgeous view indeed."
        scene cc-137 with fade
        c "[p]!"
        p "Done?"
        ## After change
        c "Tada~!"
        play music "sounds/dreams.mp3" fadeout 1
        scene cc-155:
            pos (0.0, -2.33)
            linear 6 pos (0.0, 0.0)
        $ renpy.pause(6.0,hard=True)
        $ renpy.pause ()
        scene cc-138 with dissolve
        p "It's actually skimpier than I thought before, the uniform."
        scene cc-139 with dissolve
        $ renpy.pause()
        scene cc-140 with dissolve
        $ renpy.pause()
        scene cc-141 with dissolve
        $ renpy.pause()
        scene cc-142 with dissolve
        c "The back is quite revealing isn't it?"
        c "Shows off my..."
        scene cc-143 with dissolve
        c "Well defined and non-wasted back muscles."
        p "I must say I prefer your previous outfit though."
        scene cc-144 with dissolve
        c "Cheeky."
        p "But, I don't mind this one either."
        scene cc-145 with dissolve
        p "Especially this area here...."
        scene cc-146 with dissolve
        $ renpy.pause()
        c "Ooh, where are your hands going cowboy?"
        scene cc-147 with dissolve
        p "Mm, what's this?"
        scene cc-148 with dissolve
        c "[p]! You know I've got work soon!"
        p "Oh I know, I know."
        scene cc-149 with dissolve
        p "I'll just be on the way out."
        p "Alright, time to go. Enjoy work, Caroline."
        scene cc-150 with dissolve
        p "All good times must come to an end."
        c "..."
        scene cc-151 with dissolve
        c "Hey, [p]-"
        scene cc-152 with dissolve
        p "You know, I don't know if what we had was a date but it was fun."
        scene cc-154 with dissolve
        p "Let's do it again, Caroline."
        scene cc-153 with dissolve
        c "It was fun, [p]. I... really enjoyed it."
        c "I'll see you again tomorrow, okay?"
        p "Deal. See you tomorrow!"
        stop music fadeout 1
        scene black with fade
        "Once again, [p], well played! To think that I could score a second date with Caroline. Awesome!"
        scene cc-154 with fade
        c "(I think I might... like him, but-)"
        c "(...)"
        c "(We'll just have to see how this one goes.)"
        scene black with fade
        $ carolinelvl += 1
        call daykeep
        call daykeep
        call daykeep
        jump map
    label carolineVisit: ## carolinelvl == 5, carolinebarlvl == 3
        scene cc-160
        "I guess Caroline hasn't arrived yet. I'll grab a coffee and wait for her."
        scene ellie_menu with dissolve
        p "Hey, good morning."
        scene cc-156 with dissolve
        ellie "Oh, [p], I've got a message for you."
        p "A message?"
        ellie "It's from that girl you always meet, Caroline. She says she won't be coming in today."
        p "Oh..."
        scene cc-157 with dissolve
        ellie "Instead, she asked me to tell you to just go to her apartment."
        p "Ah! I see. Thanks for the message!"
        scene cc-158 with dissolve
        ellie "Sounds exciting [p], good luck!"
        p "Haha, I have no idea what you're talking about."
        scene cc-159 with dissolve
        "Caroline wants to invite me straight to her place!"
        "Wow, this must mean she trusts me more. Maybe even... to take it to the next level."
        "Don't get ahead of yourself [p]..."
        scene black with fade
        "A few moments later..."
        # transition
        p "{i}Knock knock{/i}"
        c "Who's there?"
        p "It's me, [p]!"
        c "I'll be there just in a moment!"
        "..."
        c "Welcome!"
        scene cc-167:
            pos (0.0, -2.4)
            linear 6 pos (0.0, 0.0)
        $ renpy.pause(6.0,hard=True)
        $ renpy.pause ()
        scene cc-161 with dissolve
        p "Good morning Caroline, you're dressed in something else today!"
        c "You like it? It's comfy and really, that's what matters right?"
        p "Anyway, I believe you summoned me."
        scene cc-162 with dissolve
        c "Hey! I wasn't sure if you'd go to the cafe this morning, so I left the cafe girl a message."
        p "Let's swap numbers. You can just call me next time instead."
        scene cc-163 with dissolve
        c "Good idea! In the meantime, Coffee?"
        p "Yes please."
        scene cc-164 with dissolve
        c "Okay, just hang tight. I'm curious to see if the one I make today will taste the same as the one before."
        c "Why don't you put a game on, or something?"
        scene cc-165 with dissolve
        c "I'll be done real quick."
        p "Sure!"
        scene cc-166 with fade
        "..."
        "Now, if only I could figure out how to work this..."
        stop music fadeout 1
        scene black with fade
        "A few moments later..."
        ## Scene change Attack on titan
        play music "sounds/effects/aot1.mp3"
        scene aot-1 with hpunch
        p "V-Vincent?"
        scene aot-2 with dissolve
        p "What are you-?"
        scene aot-3 with vpunch
        v "[p]!"
        v "Argh!"
        scene aot-4 with hpunch
        p "What's the matter, are you okay?!"
        scene aot-5 with dissolve
        v "I-I don't have too much time."
        v "[p], oh [p]..."
        p "Vincent!"
        scene aot-6 with dissolve
        v "I'm... sorry...."
        scene aot-4 with hpunch
        p "Don't say that Vincent, you're going to be alright, you hear me!"
        scene aot-6 with dissolve
        v "She's... so much... stronger than we could have thought..."
        v "Haha- {i}cough{/i}. How could we have known?"
        v "How, possibly, could we have figured it out?"
        scene aot-7 with dissolve
        p "No, no, no!"
        scene aot-8 with dissolve
        v "We... don't have much time."
        scene aot-9 with dissolve
        $ renpy.pause()
        scene aot-10 with hpunch
        v "She's upon us!!"
        ## Scene to future
        scene aot-11
        x "Hidden charge:"
        scene aot-12 with flash
        x "Static discord."
        scene aot-13 with hpunch
        p "Argh!!"
        scene aot-14 with dissolve
        v "[p], you don't have to worry about me anymore."
        v "Use the power... save yourself."
        p "But if I use it, you'll-!"
        scene aot-15 with dissolve
        v "It's... going to be alright."
        v "I'll find a way."
        p "But-!"
        scene aot-16 with vpunch
        v "[p]!!!"
        scene aot-17
        p "Are you sure about this?!"
        scene aot-4 with hpunch
        p "Am I using it here?! For real?!"
        scene aot-16 with hpunch
        v "You must! For the sake of humanity! For the sake of those who have fallen before us!"
        v "This may be mankind's only chance!"
        p "I-! I understand!"
        scene aot-18 with dissolve
        "For most of my life I've been unsure of my true calling. But now..."
        "Now, I finally believe in myself."
        scene aot-19 with dissolve
        p "Take care of yourself Vincent. At this point, I can't guarantee what happens after."
        scene aot-20 with dissolve
        v "Mm!"
        v "(You were always the best of us.)"
        v "(My friend... I have no regrets.)"
        p "ARGH!!!"
        play music "sounds/effects/aot2.mp3"
        scene aot-21 with hpunch
        $ renpy.pause(2.0,hard=True)
        scene aot-22 with dissolve
        $ renpy.pause(3.5,hard=True)
        scene aot-29 with dissolve
        $ renpy.pause(3,hard=True)
        scene aot-23 with dissolve
        $ renpy.pause(3,hard=True)
        scene aot-25 with dissolve
        $ renpy.pause(1.5,hard=True)
        scene aot-26 with vpunch
        $ renpy.pause()
        p "{i}ROOOAAAAARRRRR!!!!!!!!!!!{/i}"
        scene aot-30 with dissolve
        $ renpy.pause()
        scene aot-28 with dissolve
        $ renpy.pause()
        stop music fadeout 1
        c "So? What do you think?"
        play music "sounds/something.mp3" fadeout 1
        scene cc-168 with fade
        p "Wow, what a game. Let's see."
        p "I think it's pretty cool how you can customise the characters to your choosing - even the party members and villain."
        scene cc-169 with dissolve
        c "Oooh, she's not necessarily the villain but I won't spoil it for you."
        scene cc-170 with dissolve
        p "All in all it's a pretty good game."
        scene cc-171 with dissolve
        c "Why did you customise the characters that way, anyway? Do you know them in real life?"
        p "Yeah, Vincent's a good mate. The girl is just random I met once or twice."
        scene cc-172 with dissolve
        c "She seems to have left an impression on you."
        p "Oh her? Nah, she just has this creepy vibe that really sticks with you."
        scene cc-173 with dissolve
        c "Is it strange, playing yourself and your friends in a game?"
        p "Hmm, it is. I mean, in their perspective, to them it's like everything happening in the game is real."
        p "What if {i}we{/i} were actually in a game? How freaky would that be!"
        scene cc-174 with dissolve
        c "It's interesting to think about."
        scene cc-175 with dissolve
        p "Thanks for the coffee, by the way."
        c "My pleasure, [p]."
        c "Did you like it?"
        p "Yeah, the coffee was good. Great as always, I'm sure."
        scene cc-176 with dissolve
        c "Really? There was no difference?"
        p "Uh, was there supposed to be a difference?"
        scene cc-177 with dissolve
        c "..."
        scene cc-178 with hpunch
        p "Oh I remember now! It's even BETTER than it was."
        p "You must've used different beans! Or something..."
        scene cc-179 with dissolve
        c "You'll have to try again later, [p]."
        p "Ah..."
        p "I'm not good at this stuff, you know that."
        scene cc-180 with dissolve
        c "Practice makes perfect, right?"
        p "Right."
        scene cc-181 with dissolve
        p "By the way, can I just say, I love how serious you are at the bar."
        c "You mean my professionalism."
        p "Not many people can keep their composure around me you know?"
        c "Haha! Jeez."
        scene cc-182 with dissolve
        p "I guess that makes you special."
        c "Because I can resist your charms?"
        p "Only for the time being."
        scene cc-183 with dissolve
        p "Love, uh, always finds a way."
        c "That's from Jurassic Park!"
        scene cc-174 with dissolve
        p "Jeff Goldblum, I think it was. Great movie too."
        p "Except I think instead of love, he said life, so I made a little twist on it you see."
        c "Very original and creative."
        p "Just like Dante's."
        scene cc-184 with dissolve
        p "On that note, don't you have a lot of study to do?"
        c "Umm, a little."
        p "What are you learning about now?"
        scene cc-185 with dissolve
        c "I'm just doing some revision on cell cycles - basic microbiology."
        p "Ooft. Sounds complicated. I don't want to hold you up anymore. You need to study, right?"
        scene cc-186 with dissolve
        c "Oh, ah, I was planning do some study a little later."
        p "No, no, I really don't want to get in the way of that."
        scene cc-187 with dissolve
        c "I don't need to study straight away, why don't you-?"
        p "Ah, I just don't wanna intrude. Anyway, didn't you know?"
        scene cc-188 with dissolve
        p "Absence makes the heart grow fonder."
        c "Always a clever quote you've got ready, huh?"
        p "Always."
        scene cc-189 with dissolve
        c" Fine, have it your way. I'll see you around?"
        p "See you around!"
        scene black with fade
        "I'm a little petty sometimes, playing hard to get. Hmm..."
        "Absence {i}does{/i} make the heart grow fonder. Hah, I'm regretting leaving so soon already."
        "Maybe it'll make her warm up to me more tonight at the bar."
        call daykeep
        call daykeep
        $ carolinelvl += 1
        jump map
    if carolinelvl == 6 and carolinebarlvl == 5:
        scene black
        scene cc-2 with fade
        p "Hey, Caroline."
        p "What's going on?"
        p "How's my favourite person doing?"
        scene cc-3 with dissolve
        c "Good morning [p]. I'm glad to see you're so cheery."
        scene cc-10 with dissolve
        c "..."
        p "What's going on? You're being a bit weird."
        scene cc-11 with dissolve
        c "[p]... There's something I want to talk to you about."
        p "..."
        p "What's up?"
        play music "sounds/san.mp3" fadeout 1
        c "I've had a lot of fun with you, [p], but I've been thinking really hard."
        "Oh no."
        scene cc-15 with dissolve
        c "It's this relationship stuff - I just don't know if I can commit to... all of this."
        c "It's hard finding the time f-for everything like my studies, and-"
        p "Are you... is this serious?"
        scene cc-294 with dissolve
        c "I'm sorry, [p] but I don't want you to think that I had sex with you just to take advantage of you!"
        c "At the time... I really wanted to."
        p "You're breaking up with me."
        scene cc-295 with dissolve
        c "I just want to put things on a pause for it a bit. It's just... the timing of it all."
        p "Huh."
        scene cc-296 with dissolve
        c "I hope you're not taking it the wrong way..."
        menu:
            "You just love to keep stringing me along, don't you?":
                $ depravity += 1
                p "You love flirting so close to the line, then pulling away."
                p "What is the matter with you?"
                scene cc-298 with dissolve
                c "No! [p]! That's not what it's like!"
            "It can't be helped.":
                p "Is... this what you really want?"
        c "I really wanted it to work, and I gave it a good go. But right now, I think I need a break."
        p "I thought you liked me. I liked you."
        scene cc-297 with dissolve
        c "I like you too, [p]. I really liked the time we-"
        p "Then why are you doing this? It was working so well! It's just so sudden."
        p "This is just... so out of the blue. Why?!"
        scene cc-299 with dissolve
        c "[p], please! I... can't commit enough time to make it work out."
        c "I'm just at this stage in my life where a lot of things are on the line."
        c "I told you as soon as I could, I promise!"
        p "We can work through it, set expectations."
        scene cc-300 with dissolve
        c "It's nothing you did wrong, [p]. There is just a lot on my plate."
        p "A lot on your... plate."
        scene cc-301 with dissolve
        c "..."
        p "It wasn't so long ago that I also had a lot on my plate myself."
        p "At the time, I wanted a break from it all. To recollect yourself."
        p "After that, I met you, Caroline."
        scene cc-302 with dissolve
        c "I'm sorry. It's just all the trips and exams coming up, I'm losing myself. I can't devote the time."
        p "I was like that too, and someone listened to me, and heard me out."
        p "If that's how it is, what can I do?"
        c "I'm going on my trip soon. I'll be leaving. That's why it's the right time to tell you now anyway. I tried to do it as soon as I could."
        p "Mm. I guess I'll see you when you're back."
        scene cc-303 with dissolve
        c "Well, until then, I still want to be your good friend."
        p "A friend, huh?"
        scene cc-304 with dissolve
        c "You know what I mean, [p]."
        scene cc-305 with dissolve
        p "Oh we'll be good friends. Goodbye, Caroline."
        scene cc-306 with dissolve
        c "[p]..."
        ## Autumn Scene
        scene cd-9 with vpunch
        p "For all the fuckings things that could have happened, fuck!"
        scene cd-10 with flash
        p "Fuckity fuck fuck! Did I, [p], just get dumped?!"
        scene cd-11 with dissolve
        x "Tell me, [p]. What happened?"
        p "The worst outcome. Got dumped."
        x "What did you do wrong?"
        scene cd-12 with dissolve
        p "I don't think I did anything wrong, but everything went to shit anyway."
        p "Why do you care about my life anyway?"
        x "Why indeed."
        scene cd-13 with dissolve
        p "Eh, what's the point, I don't understand."
        x "You will come to learn more later, but I don't do this without reason."
        x "Watch."
        scene cd-14 with dissolve
        $ renpy.pause()
        scene cd-15 with hpunch
        p "Wh-What is this?"
        scene cd-16 with hpunch
        p "WHAT THE FUCK DID YOU JUST SAY TO ME?"
        scene cd-17 with dissolve
        p "YOU WANNA BREAK UP WITH ME? THINK YOU'VE HAD ENOUGH?!"
        scene cd-18 with hpunch
        c "No! [p]! I'm sorry! I said I'm sorry!"
        scene cd-19 with dissolve
        p "Wha- who-?. This isn't me, I didn't do this! This... isn't me!"
        scene cd-20 with hpunch
        p "Well, well, look who it is. YOU just think you're so much better than me, don't you?"
        scene cd-21 with dissolve
        p "Looking at me like, I'm some kind of FUCKED up, DEPRAVED-"
        scene cd-22 with dissolve
        $ renpy.pause()
        x "It's happened before, perhaps in the past, or in the future, or somewhere else entirely."
        scene cd-23 with dissolve
        x "But it's happened."
        p "..."
        scene cd-24 with dissolve
        x "All things considered, your outcome isn't the worst, is it?"
        x "Continue on, [p]. You have much yet to learn about depravity."
        scene splash_caroline with dissolve
        d "This is the end of Caroline's chapter so far - I hope you enjoyed it and stay tuned for next time!"
        $ carolinelvl += 1
        call daykeep
        jump map
    scene cc-2
    p "Good morning Caroline!"
    scene cc-3
    c "Good morning, [p]."
    c "I'm trying to cram right now. Sorry about this, but could you give me a moment?"
    jump cafe
