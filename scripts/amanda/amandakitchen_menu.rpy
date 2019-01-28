label amandakitchen:
    call hidescreens from _call_hidescreens_5
    if amandalvl == 2:
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
        call daykeep from _call_daykeep_5
        jump hallway
    if amandalvl == 4:
        scene black
        scene ak-1 with fade
        play music "sounds/wisteria.mp3" fadeout 1
        p "Good to see you, [mr]."
        p "How did work go today?"
        m "It was... alright."
        "She doesn't seem too cheerful."
        "I wonder what's gone wrong."
        p "You don't sound like your usual self."
        m "..."
        m "Oh [p], I just don't know what to do."
        p "You can tell me, [mr]."
        m "{i}Sigh{/i}"
        m "I don't think people want to see me anymore."
        m "My hours are getting cut; the photographer is spending less time with me; soon I might not even have a job!"
        m "What am I going to do?"
        m "Am I losing my touch?"
        m "For a while, I felt like I had things under control."
        m "Am I only worth how I look like?"
        p "Don't say that!"
        p "It's not true."
        p "You don't even know if you'll lose the job yet."
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
        m "I'm bothering you with my troubles again!"
        p "Please don't say that!"
        p "You're still beautiful [mr], don't let anyone tell you otherwise!"
        p "Like I said, you just need the breakout."
        p "Heck, we don't even need the photographers and everything!"
        p "Anyone can take photos!"
        m "Oh [p] I really appreciate it, but it's the agency.. I don't have the contacts or the means."
        p "Fuck em'."
        p "We'll figure something out."
        p "It's the age of the internet. I'm sure we can market your modelling pictures somewhere."
        p "Leave it to me."
        m "..."
        m "Don't put this onto yourself, if you-"
        p "I'm not, [mr]. Come on!"
        p "You've got the looks already, this makes the rest easy!"
        m "Fufu~"
        m "You always know how to cheer me up."
        p "Haha, take care in the meantime."
        "If [mr] loses her job, I'll need a camera at the very least to continue taking shots."
        "It won't be cheap, but it's the least I can do."
        $ amandakitchenlvl += 1
        jump hallway
    if amandalvl == 5:
        scene black
        scene ak-1 with fade
        play music "sounds/wisteria.mp3" fadeout 1
        p "I ask this alot, but how'd work go?"
        m "It's the same pattern. Hours are getting shorter and shorter."
        m "I'm not sure how sustainable it will be in the future."
        m "I had a think about this plan of yours."
        p "Really? What did you think?"
        m "Well, I spoke to one of my friends in the industry, and she told me a few things that we need."
        m "We need to have some sort of camera to start off with, and we need to advertise ourselves."
        p "Easy, right?"
        m "I'd like to think so, but those are two things that I don't have access to."
        m "I don't know how to work a camera, or even how to choose one. On top of that, how can I advertise myself?"
        m "That's what the agency is supposed to be for, and they don't even want me."
        p "Leave it all to me, I'll figure something out."
        p "I can source a camera, no worries. I did a little bit of photography in university."
        p "As for the marketing, posting it on websites and stuff will do, but I'll ask around. We can build it up slowly."
        p "I'm confident that once we get you out there, your pictures will do the rest."
        m "Are you sure, [p]?"
        p "I'm confident."
        p "Just keep working as you are. I'll let you know when I've got a camera, and we can start there."
        m "Thank you so much."
        p "No worries, [mr]. You did the same for me."
        $ amandakitchenlvl += 1
        jump hallway
    if amandalvl == 6:
        scene black
        scene ak-1 with fade
        play music "sounds/wisteria.mp3" fadeout 1
        p "Not too tired from work I hope?"
        m "Work is always tiring, but I've been waiting the whole day to get back home."
        m "You said you were going to take some pictures of me?"
        p "Haha, I'm a bit rusty, but yes."
        p "So, I'm not actually too knowledgeable about how photoshoots work."
        p "Do you just stand there, and then I take pictures?"
        m "Well usually, there's an outfit picked for me, and I do a few poses. The photographer might also instruct me to do something as well."
        p "What does the photographer tell you to do?"
        m "Specific poses, facial expressions, anything."
        p "Oh cool. What about the outfit part? I haven't really got an outfit for you, haha."
        m "Hmm, maybe I can dig through what I already own."
        m "Like I said before, its not usual that I get to take outfits home."
        p "Sounds like a plan."
        p "Let's go to your room."
        p "To be honest, I'm really new to this. I feel like you'll be giving {i}me{/i} the instructions!"
        m "Oh don't worry [p]. Look at it like we're having fun together."
        ## Transition
    scene ak-1
    p "Hey, I love you [mr]!"
    scene ak-2
    m "I love you too sweetie!"
    jump kitchen
