label camilletalk:
    if camillelvl == 1:
        play music "sounds/armoir.mp3" fadeout 1
        if talkcamille:
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
    if camillelvl == 2:
        play music "sounds/armoir.mp3" fadeout 1
        p "Hello Camille!"
        t "H-hey [p]."
        t "Is there somwhere where you'd like to go? Something I can help you with?"
        p "Nothing right now, I was just wondering how you're doing."
        p "Remember when we first met? You seemed to have your mind full with something, and I haven't asked you about that since then."
        t "Oh, that wasn't anything, really!"
        p "You sure?"
        t "Umm..."
        p "Hey, how about this?"
        p "Let's go off somewhere, and we'll have a man to man- I mean, man to woman talk."
        t "I- I'm working right now, I couldn't just go off- I mean, I'd love to, but still!"
        p "I think people are gonna be alright here. If someone comes, they'll ring the bell, right?"
        t "I.. suppose."
        t "But where are we going?"
        p "You know this place better than I do, why don't you show me around the VIP or staff areas!"
        t "I can't get you into the VIP, or I'll get into trouble. But maybe... after work?"
        t "Why don't you relax in the sauna, and I'll just come find you later?"
        p "The sauna. Right. Do I need the membership?"
        t "I'd love to let you in for free... but it's hard... I hope you understand?"
        p "I won't put you through any drama Camille. Don't worry. I need the silver membership right?"
        t "That's right!"
        p "Hold up, let me check to see if I have it."
        "Hmm, let me see..."
        $ camillelvl += 1
        jump lobby
    if camillelvl == 3:
        if resortmembership > 1:
            p "Yup, I'm a member. May I go to the sauna?"
            t "Of course. Let me take you."
            t "Welcome to the sauna. Do enjoy your stay here for a bit."
            p "Do come and say hi after work and we'll have a quick catch-up."
            t "I'll make sure to do that, [p]. Thank you."
            "Time to get changed."
            "I admit, I am a little curious about Camille. She always seems so shy, I'm little surprised she's meeting me afterwards."
            "Is this going to be like a date or something?"
            "Ah, shouldn't think too much about it [p]. We'll see."
            "The sauna is actually so nice. I rarely come to these sort of things but it's a great place to relax."
            "The hot steam is making me feel sleepy..."
            "..."
            "zzzzz...."
            x "Are you fancying Camille, [p]?"
            p "You, always in my dreams."
            x "Camille was rejected by Vincent. Will you reject Camille too?"
            p "A little too soon to say, don't you think?"
            p "She seems a nice girl. I have nothing against her."
            x "One day, you find out why you made a choice."
            p "What choice?"
            x "Which choice is more depraved? I'll leave that for you to find out."
            p "Why don't you ever answer my damn questions."
            p "Being all mysterious and shit."
            x "It's time to wake up."
            p "Ah!"
            "{i}Pant... pant{/i}*"
            "I hear someone coming in. Is it Camille?"
            "God how long was I out for?"
            t "Um, [p]?"
            p "Here."
            t "I'm done with work now, you said you wanted to have a meet up and have a chat?"
            p "Yeah, I did say that. The sauna was so relaxing, I lost track of time."
            p "Hang on, just let me get changed. Should I meet you back at the reception?"
            t "Yes, I'll meet you back there."
            p "Shit, I casually suggested a chat and now it seems like something serious."
            p "I'm just a lucky guy."
            scene black with fade
            p "Ah, back in my Kishou Arima outfit."
            t "Hello [p]."
            p "Oh hey Camille. I was just thinking of catching up."
            p "I've been meaning to meet up with you like I promised. Sorry again for not calling you, haha."
            p "So this seems serious. We should do something to fit the occassion. Where do you want to go?"
            t "Are you... are you feeling hungry?"
            "Yeah, hungry for action."
            p "I'm not too hungry, but I'll be keen for food still."
            t "In that case, how about we go to the bar?"
            p "Hmm, it's like we're coming full circle."
            p "Should we go now?"
            t "Um, I've got a few things I've got to handle at home first. How about I meet you there?"
            p "Sure, I'll wait there for you."
            ## transition to bar
            "Hm, I wonder how long she will take."
            "Girls always take ages, wonder if Camille will be any different."
            p "Hey Caroline, how is it going?"
            c "Good, [p], good!"
            c "Coming to the bar for a few drinks?"
            p "Yes, and I brought a friend this time!"
            c "A {i}girl{/i}-friend?"
            p "Aha, don't be silly. It's Camille. She's come here before, I'm sure you know her."
            c "Ah. Camille! Yes, I've come to know her pretty well over a period."
            p "Just thought I'd catch up with her."
            c "How again do you know her?"
            p "Well, I saw her in the bar here with you, rememeber? When I first came?"
            p "I met her before though to be honest. Poor girl was chasing after a guy who wasn't too keen on her."
            c "I see."
            p "His loss, am I right?"
            c "I think she's a great person and she'll find someone someday."
            c "So how is it that you two are meeting today?"
            p "I just saw that she was feeling a bit down, so I wanted to catch up with her and make sure she's okay."
            p "Anyway, I'm keen to always make new friends."
            c "That's good to hear, [p]."
            c "It looks like you won't have to wait much longer, she's here."
            ## bar scene
            p "Camille!"
            "It looks like she went home to change her outfit and her look. It's very cute and it's nice seeing her out of her working attire."
            p "The last time we were here- how long ago was that?"
            p "You're looking great by the way."
            t "Ah-thank you, [p]!"
            # fade to seat
            t "Hello Caroline."
            t "I hope your work isn't keeping you too busy!"
            c "I never mind if it's customers like yourselves."
            c "Can I help you two to a few drinks?"
            p "Camille?"
            t "I'm always fond of Dante's original."
            p "Me too. Let's go for that Caroline."
            c "I knew you'd say that. Coming right up!"
            p "You come here a lot, Camille?"
            t "I... come here sometimes."
            t "I like to see Caroline and the drinks here are nice."
            p "Are you good at handling your alcohol?"
            t "I was never any good, ah-"
            p "Reminds me of my [sr]. You know, she was here that night we were here last. Did you see her?"
            t "Ah, I must have left before she came."
            p "Oh that's right, you had to leave for something early back then. I hope that ended up being alright."
            t "Ah yes, I- I managed to sort it out."
            p "So tell me something about yourself, Camille."
            t "Err, well I work at the resort, and I enjoy it."
            p "Do you get any perks?"
            t "I have access to all the areas for free I guess."
            p "Hey, that's pretty awesome."
            p "What do you like to do the most at the resort?"
            t "There's an area with a hot spring. I like going there late at night and wash myself with while looking at the stars."
            p "Are there many people there at night?"
            t "No, it's closed at that time so it's just me. It's the fact that I'm alone that I like so much."
            p "I can imagine that it would be relaxing."
            t "What about you? What do you like to do?"
            menu:
                "I like meeting girls.":
                    $ depravity += 1
                    t "Aha, I'm glad I can make you happy in that case."
                "I like going to the resort.":
                    t "Oh, ah- I'm glad to see you come to the resort too."
                    p "Oh, I mean I like to swim and stuff but of course I like to see you too at the resort."
                    t "Ah- I... sorry, forget I said that."
            p "You know, you don't have to talk about it if you don't want to, but what was going on the day I first met you?"
            p "You were looking for a guy called... Vincent?"
            t "..."
            t "We used to meet up a bit, and one day, he became more distant."
            ## drinks more
            t "Caroline, may I have one more drink?"
            c "Of course Camille!"
            "Hmm, she's started to drink more heavily after I bring up Vincent. I wonder what's going on there."
            p "Sorry to bring it up."
            t "Mm."
            t "It's okay, it's in the past."

        else:
            "I need to make sure I have the silver membership first."
            jump Camille

    ## generic
    scene cam-5
    p "Working hard Camille?"
    t "I always try my best."
    jump Camille
