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
        c "Chessy line, [p]!"
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
        scene c-12 with dissolve
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
    scene cc-2
    p "Good morning Caroline!"
    scene cc-3
    c "Good morning, [p]."
    c "I'm trying to cram right now. Sorry about this, but could give me a moment?"
    jump cafe
