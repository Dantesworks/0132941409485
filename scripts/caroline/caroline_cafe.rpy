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
        c "The more severe ones, yes."
        p "I've heard of this thing called schizophrenia, what is that again?"
        scene cc-8
        c "Well, it's the one that people typically think of when you say someone's psychotic."
        p "Psychotic as in crazy?"
        c "It's a specific kind of crazy. People who are psychotic hear or see things that aren't there."
        p "Ah, that kind of crazy."
        scene cc-9
        c "Of course, psychosis is just a symptom. Many things can cause psychosis, just like how many things can cause chest pain."
        p "Such as?"
        scene cc-12 with dissolve
        c "For chest pain?"
        p "Sure, gimme a few examples."
        scene cc-5 with dissolve
        c "A lot of things can cause chest pain. A heart attack can. A pulmonary embolism, pneumonia, reflux, costochondritis are just some other examples that can all cause chest pain."
        c "Of course, pulling your pectoralis major muscle during your bench-pressing at the gym will also cause chest pain."
        p "Oh I get it, so many things can cause psychosis too? What's the most common?"
        scene cc-6
        c "Well, schizophrenia probably jumps to people's minds the first, but the most common is probably drug-induced. Taking methamphetamine and other illicit drugs can make you crazy."
        p "Cannabis is safe though, right?"
        c "Well, it's what a lot of people like to believe, but it's also a common cause for psychotic presentations."
        p "Wow, everything in moderation, huh?"
        scene cc-9
        c "Definitely!"
        c "Phew, that was good revision."
        p "Man, Caroline, you know a lot!"
        c "Thank you, I spent a long time studying it!"
        p "You've also got a ton of passion for this kind of stuff."
        p "Tell me about depression next, I know a lot of people have it. What's the deal with it?"
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
        p "Good morning Caroline."
        c "Hello, [p]. Will you be following up with your promise today?"
        p "Promise?"
        c "You remember the promise?"
        c "I freed up my schedule for this, you know. Where are we going?"
        p "Ah you were talking about that."
        p "You're in such a rush! Let's have some a drink first."
        "Oh shit, I haven't thought of a place to go yet!"
        c "Oh, we are definitely having a coffee first, but I'm curious about your grand plans!"
        p "Grand? Ahahahah..."
        p "Really, really, you're putting the pressure on me!"
        c "No pressure."
        p "It's a suprise, Caroline."
        c "Ooh, I don't know how I feel about surprises."
        p "Take a guess."
        c "Hmmm... how about a clue?"
        p "Uh, it's a cool place that you probably want to go to very much."
        c "A cool place, that I want to go to..."
        c "Are we going to the music theatre?!"
        p "Bingo! That's exactly where I'm taking you! Ahaha...ahahha..."
        "Well played, [p], well played. This trick always works."
        "But damn, what the hell am I going to do at the music theatre?"
        C "Are we watching a musical, listening to a concert?"
        p "Um..."
        "Ah, shit."
        p "It's uh, a surprise."
        c "I love music. It's nice to know that you also appreciate that sort of thing."
        c "How did you come across the music theatre?"
        p "I went once or twice back when I was in high school."
        p "Never really to watch any shows - I'd go to one of the side rooms and have fun with some of the instruments."
        c "Do you play anything?"
        p "Not anything well, haha. But yeah, I like to just make some noise sometimes."
        c "It's like a release, I know what you mean."
        p "Do you play anything?"
        c "I've been playing the piano since I was a child, so I suppose I can play that quite well."
        c "I've also tried playing the violin, but that wasn't as fun."
        p "That's amazing. You didn't like the violin?"
        c "Getting started with the violin is always hard. A lot about sounding good is about how you draw the bow across the strings."
        c "With piano, there's not much skill - you just hit the note."
        c "With the violin, I was sounding really horrible, so I just thought I'd maybe revisit it another day."
        c "And you know what? That day never came."
        p "I reckon being good at the piano is awesome enough."
        c "Thank you, [p]. So, what have you been up to recently?"
        p "Just finding my feet. Making friends. Talking to... cool people like you!"
        c "Aww, aren't you nice."
        c "You know, I've been thinking. We're chatting quite pleasantly right now, and I like your company."
        c "But, what inspired you to come over in the first place?"
        p "I met you at the bar, remember? I always like saying hi to a familiar face."
        c "Oh that's right."
        p "You didn't remember? You even told me that you like to keep things professional at work, haha."
        c "Oh, I tell a lot of people that, [p]. It's hard to keep track sometimes."
        p "Very good. A very popular lady."
        c "No, I'm not!"
        p "You get hit on at the bar, no?"
        c "By drunk guys. They'll hit on anybody."
        p "Ever get hit on by girls?"
        c "Of course, but they're drunk too!"
        p "You ever get to have any fun, you know, enjoy yourself?"
        c "I'm a professional, [p]! I wasn't interested."
        p "You know, {i}I{/i} wasn't drunk when I said hi to you."
        p "Just something to keep in mind, you know, just saying."
        c "Haha, what's your point?"
        p "I'm a sincere guy, a real professional too."
        p "Someone with uh, integrity."
        c "Good character traits to have."
        p "I'm happy you think so too!"
        ## Time passes
        c "Are you ready to head off?"
        p "Let's go."
        "Ah shit, I haven't actually got anything prepared."
        "I'll just have to wing it."
        ## Time passes
        c "This is interesting, [p], we've left the theatre."
        c "Are we not watching a show?"
        p "We're going to one of the side rooms - surprise! Hahaha..."
        c "What a twist!"
        p "I was thinking, why watch a show, listen to music, when we can make our own?"
        p "I came here a bit when I was in high school and this was always a calm place where I could get away from it all."
        c "You come here by yourself?"
        p "Those who don't enjoy solitude cannot enjoy freedom."
        c "A wordsmith too, [p]?"
        p "It's not my quote. My old math teacher used to write a quote on the whiteboard everyday, and this one resonated with me."
        c "Well this time, you're not alone."
        c "Are you going to play something?"
        p "I was never any good, and besides, it's been a while anyway."
        p "Maybe you could grace this place with some music?"
        c "I haven't played in a long time either!"
        c "But, let's see if I can improvise something."
        c "Just letting you know, I'm making this up on the spot okay!"
        p "I can't stand the anticipation."
        c "Oh, stop. Anyway!"
        c "Here goes."
        ## play music
        p "Wow, good job. Really suits the atmosphere in this place."
        c "Thanks. I ended the tune with a funny chord. I think it made it sound more wistful."
        p "Are you going to make that into a full song at any stage?"
        c "Ooh, I might. But that's one of the great things about sitting down at the piano and playing what comes to mind."
        c "You get these short pieces and ideas, some you won't remember but if it's good enough, you'll write it down."
        p "This one has potential."
        p "I can imagine sitting in another room, next to the fireplace in the middle of a rainy day."
        p "The music floating through the hallway..."
        c "And with a mug of coffee in hand?"
        p "That's my idea of a good time."
        menu:
            "A good looking girl next to me wouldn't hurt.":
                $ depravity += 1
                c "That's great to know, [p]."
            "Having someone else to share it with wouldn't hurt.":
                c "And would that somebody be me?"
                p "It could be. I don't discriminate."
                c "Ha!"
        c "So how are you rating this date?"
        p "It's not bad. It's just the start."
        p "What do you reckon?"
        c "I think it's very original and creative."
        p "Like Dante's original."
        c "You do love that drink very much, don't you? I should get you a week's supply for your birthday!"
        c "But as I was saying, this was an original date, [p], and that's endearing."
        p "If this is endearing, you'll love part two."
        c "You've done this much already, let me handle our next destination."
        p "Taking charge!"
        c "I want to share my studio apartment with you - it's a slice of heaven."
        c "And a good place for me to teach you more about coffee!"
        p "Oh, what's so special about this apartment?"
        c "It's... ambient. I think you'll enjoy the aesthetic."
        p "You're setting high expectations."
        c "Oh, its not fancy, that's not what it's about. It's just a nice place, like this one you know?"
        c "You feel wholesome."
        p "Like nothing can go wrong."
        p "If those are the vibes, than give me more."
        c "That's what I'm saying! So come on, let's go!"
        ## transition
        c "Welcome to my abode."
        p "Nice! There are industrial flavours, its very much modern."
        p "When you said it was all wholesome and ambient, I was expecting something with darker colours."
        p "More... earthy?"
        c "Oh I get what you mean. Wood and all that right?"
        c "The fireplace crackling, and all that."
        c "But this is a different feeling. It's clean and contemporary."
        c "You wake up in the morning and you feel like you're going to be productive."
        p "You've really got your life in order, wow!"
        c "It's a feeling of potential."
        p "So what's the average day for you like?"
        c "I wake up in the morning, get changed, and then I-"
        p "Go to the cafe for coffee?"
        c "Ah, I'm that predictable, aren't I?"
        p "Well, I do see you there every morning."
        P "What after that?"
        c "Oh I might come back home, I might go to a lecture, or I might go to the library."
        p "Hang on, is that a coffee maker over there?"
        p "Then how come you always go to the cafe?"
        p "Looks like a fairly robust machine too. I'm sure you could pump out some good joe with this."
        c "Oh I can, but like I said, cafe in the mornings is a ritual."
        c "It's the hustle and bustle of people. It's the way coffee is supposed to be had - with other people!"
        c "It's no fun having it by yourself."
        p "Well, I'm here now, right? What say we enjoy one together?"
        c "I'd love to show you more about coffee."
        c "How do you take it?"
        p "Um, what are the options again?"
        c "Well you could always just have a shot of espresso, but that's no fun by itself."
        c "How about a latte?"
        p "Sounds nice."
        c "Great. You know, this is one of the reasons I bought a coffee machine."
        c "To share with other people."
        p "So, are you going to make it, like right now?"
        c "Yeah, should only be a few minutes."
        p "Sure, I'll just chill out here."
        "Despite what Caroline says, this place is quite fancy."
        "There's a beautiful view and if I woke up to this everyday, I'd be motivated and productive."
        c "What are you up to, [p]?"
        p "Oh, just checking something out on my phone."
        c "Whatcha looking at?"
        p "Just some coffee mugs"
        c "Thinking of getting your own coffee setup already? Have I converted you into the life of coffee yet?"
        p "Maybe. I'm just taking a look at some custom mugs."
        c "Do they look good?"
        p "Not bad. Price seems alright."
        p "How's the coffee coming along?"
        c "Err, just a moment. I've almost finished the second. The second one always tastes better than the first, so I'll give you that one."
        p "Oh, thanks!"
        ## coffee done
        c "Ah, perfect. Here, try it out. What do you think?"
        p "Mmmm..."
        p "That's creamy!"
        c "That's the frothed milk. But what do you think about the beans?"
        p "The beans themselves? Ooh I'm not sure I'm that good at picking that out."
        c "I'm using some Kenyan beans, and they're more stronger than say, the one at the cafe, don't you think?"
        p "I guess, but it's subtle. I might not have picked it up if you didn't say so."
        c "The strength, or the bitterness, is a slap in the face to really help me wake up sometimes."
        c "That's why I sometimes go for it over fruitier flavours."
        p "You really {i}do{/i} know your stuff."
        c "Oh, I just experiment and see what works for me. That's all."
        c "I might be completely wrong! This is just the way I analyse it."
        c "How do {i}you{/i} see it?"
        p "Hmm, my analysis?"
        p "I'd say... this coffee is like... you!"
        p "You started off with the espresso, which is like the serious and bitter stuff, but you have mixed with it the milk, which is creamy and good."
        c "That's an interesting metaphor."
        p "Like, there's a seriousness to your character but you're smooth and cool at the same time. You know?"
        c "That's a nice compliment, I suppose. I haven't really thought of myself as a cup of coffee before."
        p "It {i}is{/i} something you're associated with though, isn't it?"
        p "Careful, Caroline. Drink too many and you might turn into actual coffee!"
        c "You think!"
        c "That wouldn't be such a bad thing. I think I'd make as a nice cup of coffee."
        p "Not too bitter, I hope!"
        c "I would be the sweetest cup of coffee."
        p "I'd drink that."
        c "I'd be offended otherwise, haha!"
        p "Haha, oh man. The cream's a little heavy. I'm feeling a bit drowsy."
        c "I'm used to it by now."
        p "I thought coffee was meant to make you feel more awake."
        c "Hmm, maybe it would be better for you to have just coffee without the milk next time."
        c "You can have a rest if you want. I'm not going to be doing too much anyway."
        p "{i}Yawn...{/i} just a quick rest."
        p "What are you gonna do in the meantime?"
        c "More study."
    scene cc-2
    p "Good morning Caroline!"
    scene cc-3
    c "Good morning, [p]."
    c "I'm trying to cram right now. Sorry about this, but could you give me a moment?"
    jump cafe
