label bartalk:
    if carolinelvl == 2 and carolinebarlvl == 1:
        play music "sounds/dreams.mp3" fadeout 1
        scene black
        scene cb-5 with fade
        p "So, how's it going Caroline?"
        scene cb-6
        c "It's going good, [p]."
        p "Busy night tonight?"
        c "Same old, same old."
        p "Reckon you could get me into the premium lounge?"
        scene cb-8
        c "I'm afraid not."
        p "Please, I'll make it up to you."
        scene cb-9
        c "I'm just following the rules, [p]!"
        $ carolinebarlvl += 1
        play music "sounds/popstars.mp3" fadeout 1
        scene cb-1
        jump barask
    if carolinelvl == 5 and carolinebarlvl == 2:
        play music "sounds/dreams.mp3" fadeout 1
        scene black
        scene cb-5 with fade
        p "Caroline!"
        scene cb-6 with dissolve
        c "Hello again, [p]. Couldn't get enough of me?"
        p "What do you mean? I just happen to be swinging by the bar!"
        scene cb-8 with dissolve
        c "Remember what I said, [p]. I act professional when I'm on the job."
        c "It's important to me."
        scene cb-5 with dissolve
        p "I respect that. Just here for a drink, haha."
        "Damn, Caroline's not as easy as the rest, is she?"
        "I probably shouldn't push it anymore than I have to. I'll just go say hi tomorrow."
        $ carolinebarlvl += 1
        jump barask
    if carolinelvl == 6 and carolinebarlvl == 3:
        p "Hey there!"
        p "How was your study this afternoon?"
        c "Oh it was alright."
        c "Did you get up to much?"
        p "Yeah! Just wandering around, you know."
        c "I'd love for us to just go on, but you know, this is my work and all..."
        p "I won't get in your way, don't worry!"
        c "Hey, uh, will you wait for me after work?"
        c "(I'm always tired after work and I just want to sleep, but...)"
        c "I usually end work quite late, but I think if you wanna hang around, we could catch up after?"
        p "Let's do that, Caroline."
        # Transition to bathroom
        p "It looks like she's warming up a little more to you, [p]."
        p "Hopefully I'll be able to get closer to her tonight."
        p "Alright. Don't screw this one up [p]. She's different from the rest."
        ## few moments later
        c "Oh, that was a tough shift!"
        p "Oh no! I hope it wasn't {i}too{/i} tiring."
        c "I'll be fine."
        p "How about a few drinks? Everyone's gone."
        c "Great idea."
        c "Dante's original?"
        p "You know me!"
        p "It's so different. Usually it's loud, the music is blaring and now all of a sudden it's so quiet."
        c "That's an interesting observation."
        p "So is it always you that works here?"
        c "Yes, but there used to be another girl here."
        c "She's working at another bar that the manager here owns."
        p "What's the trickiest part of the job?"
        c "It's not too bad actually. Turning up everyday is probably the hardest part."
        c "It's just so tiring sometimes!"
        p "Yeah, I can understand that."
        p "Thanks for the drink. I'll make it up to you, for sure."
        c "Don't worry about it, [p]."
        c "If you're ready we can go."
        p "You need any help packing up?"
        c "Yes please! We'll both get to leave sooner - and continue this at my place."
        ## all done
        p "All done!"
        c "Nice work, [p]! Final check.... and time to go."
        ## to house
        p "You know, you're surprisingly energetic. If I worked the whole night I'd be crashing in bed."
        c "Don't say that, [p], you're making me feel sleepy..."
        p "Just have a lie down then, take a rest."
        c "If I do that, I'll fall asleep."
        p "Come on, just lie down on the couch here. You know you want to."
        c "..."
        c "Alright."
        p "Haha, you don't need to torture yourself, you know?"
        p "We can always chill another time."
        c "We don't... have too much time..."
        p "What are you talking about, Caroline? Of course we do."
        p "..."
        p "Caroline?"
        "Damn. Out just like that that."
        p "I'll carry you to bed alright Caroline?"
        p "..."
        p "Alright, I'm going to carry you now."
        ## to bedroom
        p "You're quite light, Caroline!"
        p "Though, I suppose, I never really expected you to be heavy in the first place."
        p "I'll call you tomorrow, okay? Good night."
        c "...[p]."
        p "Hmmm?"
        c "Don't go... stay..."
        p "You want me to stay here, with you?"
        c "Mmmm..."
        p "Oh, okay."
        p "Just... right there then."
        c "Mmm~"
        ## sleep
        "A sleepful night passes..."
        p "Uh... where am I?"
        p "This isn't my room..."
        p "Caroline?!"
        p "..."
        "She's gone."
        p "I guess I was pretty tired that night too. I passed out pretty quick."
        p "She probably woke up before me, and if I'm lucky, I'll get some coffee already made for me."
        ## Transition
        c "Good morning, [p]."
        c "Did you sleep well last night?"
        p "Surprisingly well, I'd say. How about you?"
        c "I slept very well too, I must have been pretty tired."
        p "Haha, you were!"
        p "Must have been the mix of alcohol and long day."
        c "Well, I feel a lot better now, so that's good."
        c "I don't remember much about last night though. Tell me..."
        c "Did we... do anything?"
        p "Do... anything?"
        c "Well, you know..."
        p "I... don't thnk so."
        c "Oh, in that case, did I say anything?"
        p "The last thing you said was that we didn't have much time or something, then you passed out."
        p "What did you mean by that, anyway?"
        c "Ah."
        c "I'm going on a trip soon, an academic trip. We won't be able to meet for much longer before then, that's all."
        p "But you'll be back, right?"
        c "In a few weeks."
        p "A few weeks too long, I'd wager."
        c "That was my thought. I remember wanting to hit home base with you last night, so I was just curious if I went ahead with it."
        p "Whoa, hang on, what?!"
        p "You should've let me know!"
        c "Take the hints, [p]!"
        p "Y-you were sleeping, what- I can't move on that!"
        c "Maybe. So what's the next best thing?"
        p "The next best thing? Wha- oh."
        p "Um, err... like, now?"
        c "..."
        p "Oh, okay, got it."
        p "So, do you want to, like, you know, like, fuck or something?"
        p "Wait, that came out wrong, let me-"
        c "Oh my {i}god{/i}, hahaha!"
        c "Just let me do the work, [p], and stop talking just a bit."
        p "I love to hear your voice, but just this once..."
        ## sexy times
        "She embraced me and attacked my lips with such voracity that I could never have imagined from her!"
        p "Oh my, wow! Still waters run deep, Caroline."
        c "Med students are so busy, we have to be efficient even when we're having fun."
        p "I'm not complaining girl."
        c "Good. Sit down right there."
        p "Come on, show me what you got."
        ## sex over
        c "That was great sex, wasn't it [p]?"
        p "Never expected it, you're so good."
        c "You too!"
        p "No but, really, you've got a great pussy."
        c "And your penis was the perfect size. Really filled me out, I think."
        c "I might have gone a {i}little{/i} too hard... ouch."
        p "Man, Caroline, I'm still surprised you go this in you."
        c "Didn't you say it already? Still waters run deep."
        p "Clean on the streets."
        c "Freak under the sheets."
        p "Good for you!"
        p "So, when again is your trip?"
        c "I don't exactly know when, I don't like to check. I hope that it'll go away if I don't check."
        p "What is it, in a few days?"
        c "Something like that. Week, maybe? I don't know."
        p "Maybe I'll go on a trip too."
        c "Yours would be a fun trip. Mine would be one of those boring ones."
        p "I'm sure you'll get to have some fun too."
        c "I'm not counting on it."
        c "That's why I'm planning to have all the fun before I go."
        p "Amen to that."
        c "Coffee, [p]?"
        p "It would be a pleasure."
        call daykeep
        $ carolinebarlvl +=1
        jump map
    if carolinelvl == 6 and carolinelvl == 4:
        p "How's it going Caroline!"
        c "Hi, [p]. After the other day, sorry, but I'm just going to concentrate on my work for a bit."
        p "Aww."
        p "That's alright. I'll see you around."
        c "Thanks for understanding."
        "Hmm, I thought she would be warming up to me overtime, surely."
        "Maybe she just needs some distance?"
        "Yes, that's probably the type of girl she is."
        "I'll go have a coffee with her again tomorrow, and see what's up."
        $ carolinebarlvl += 1
        jump barask
    ## Generic
    scene cb-5
    p "Good to see you Caroline!"
    scene cb-8
    c "Good to see you too, remember to take care of yourself!"
    scene cb-1
    jump barask
