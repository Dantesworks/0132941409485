label amandakitchen:
    hide screen daytime
    hide screen map_icon
    if amandakitchenlvl == 1:
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
    if amandalvl == 3:
        scene black
        scene ak-1 with fade
        play music "sounds/wisteria.mp3" fadeout 1
        p "How was work today?"
        m "It was great!"
        m "Well, it doesn't pay very well, but I got to take home a few freebies..."
        p "Hey?"
        m "I got to keep some of the outfits that I wore today!"
        P "Awesome."
        p "That's... real cool."
        m "You boys would never understand."
        p "No, no, I get it sometimes [mr]."
        p "This one time Nicole picked out some clothes for me, and that was pretty cool."
        p "It was fun. What a fun day that was."
        "Indeed..."
        m "Did she really?"
        m "I remember! You went clothes shopping with your [sr] and Nicole."
        m "I'm sure you enjoyed yourself very much~"
        p "Yeah, I got to meet Nicole and everything."
        m "Did you get to know her {i}well{/i}?"
        p "Well, sort of?"
        "Where is she going with this?"
        m "And Kaira, how was she?"
        p "Like you said [mr], she's grown a lot, haha!"
        p "Can barely believe she's the same girl, christ."
        m "She's a woman now, [p]."
        p "It's hard to believe sometimes."
        p "She had me pick out outfits as well, it was some sort of competition between her and Nicole."
        p "I had to pick out who wore their outfits the best."
        p "Was crazy hard."
        m "Sounds like you've got some experience."
        m "Come, let me show you what I picked up at work today."
        m "Let me know what you think."
        p "I guess I can make a few comments."
        m "I hope you're as excited as I am to show you!"
        p "Oh I am! Lead the way."
        ## Transition to bedroom
        m "Like I said, it's not a usual thing, to be able to take the outfit home."
        p "Why'd they let you keep it?"
        m "I'm not sure, but I'm not going to say no."
        p "It must have been because you looked so good in it!"
        m "I think so!"
        m "Lets see what you think."
        m "Turn around and close your eyes."
        m "I'm going to slip it on."
        p "Looking forward to it."
        ## Turn around
        "..."
        "I wonder what outfit [mr] is going to wear."
        m "Hmm~hmm~♫"
        "..."
        p "Are you done yet?"
        m "Just a moment, sweetie, good things take time!"
        p "Are you putting it on."
        m "I'm just about to, hang on."
        menu:
            "Wait for [mr] to put on her outfit.":
                "I'll get to see soon enough."
            "Sneak a peek.":
                $ depravity += 1
                "Hehe, what's the harm?"
                "Wow."
                "I've never seen [mr] like this before."
                "Her tits are massive. No wonder Kaira is jealous!"
                "Definitely model material... how is she still single?"
                "I shouldn't stare too long..."
                "..."
        m "You can turn around now, [p]."
        m "You're... not saying anything."
        m "You don't like it?"
        p "This... is what you model in?"
        m "..."
        m "Yes. Is there... something wrong?"
        p "..."
        p "There's nothing wrong."
        p "You look amazing [mr]."
        p "It wasn't what I was expecting, but it makes sense."
        m "What makes sense?"
        p "It's a little awkward to say, since you're my [mr] at all."
        m "It's okay, what is it?"
        p "Well, of course.."
        p "You're incredibly good looking, [mr]. And of course people are going to appreciate that."
        p "That's why you're a model after all."
        p "Damn, [mr], just damn!"
        m "Not the kind of modelling you were expecting, huh?"
        p "You're one... sexy lady."
        m "Fufufu~"
        m "All that to tell me something I already know?"
        p "Well, kinda caught me off guard."
        m "Why don't you tell me what you think about this outfit?"
        p "Alright, let's see a few poses!"
        m "You sound like the photographer."
        p "I think it looks as good as the woman wearing it."
        m "Which is to say?"
        p "You already know the answer. It's great."
        p "I feel like you could earn a lot of money doing this."
        m "People seem to always think so, but there are a lot of pretty girls out there."
        m "Getting your name out there is hard."
        p "You just need your big breakout"
        m "..."
        m "Why don't you come sit down?"
        m "It's been a long time since you've had a long chat with your [mr]."
        m "How are things going with you?"
        p "It's going much better than it used to be."
        p "Time really makes things better."
        p "I felt like I was in a vortex before, being sucked into chaos."
        m "It's good that ou don't feel that way anymore."
        p "Well, in a way, I still feel like the chaos is still there."
        p "But I feel like I can come to terms with it. At the end of it, I might come out stronger."
        m "That's a mature perspective."
        m "You've really grown too, haven't you?"
        m "No longer the boy that left home."
        m "You've come back as a man."
        p "..."
        p "And how about you, [mr]?"
        m "To be honest, the modelling business is hard."
        m "There's a lot of girls out there - a lot of competition."
        m "The agency is putting more attention into the other girls, and I'm not getting as many photos as I used to."
        p "That's their mistake."
        p "Don't let it get you down, [mr]."
        m "Thank you, [p]."
        m "Look at me, being all negative!"
        m "Thanks for being here."
        m "Someone for me to talk to."
        p "No worries, [mr]. I'm very happy to help in any way."
        "I've never seen [mr] like this, I really want to just hold her..."
        m "(He's such a kind man...why am I getting these feelings again?)"
        m "..."
        p "..."
        m "It's... getting late, isn't it?"
        p "...You're right, I should probably go."
        m "Goodnight, [p]."
        p "See you tomorrow, [mr]."
        $ amandakitchenlvl += 1
        jump hallway

    scene ak-1
    p "Hey, I love you [mr]!"
    scene ak-2
    m "I love you too sweetie!"
    jump kitchen
