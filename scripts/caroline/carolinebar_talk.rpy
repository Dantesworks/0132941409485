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
        scene black
        play music "sounds/dreams.mp3" fadeout 1
        scene cc-190 with fade
        p "Hey there!"
        p "How was your study this afternoon?"
        scene cc-191 with dissolve
        c "Oh it was alright."
        c "Did you get up to much?"
        p "Yeah! Just wandering around, you know."
        scene cc-192 with dissolve
        c "I'd love for us to just keeping chatting, but this is my work and all..."
        scene cc-190 with dissolve
        p "I won't get in your way, don't worry!"
        scene cc-193 with dissolve
        c "But- hey, [p] look... will you wait for me after work?"
        scene cc-194 with dissolve
        c "(I'm always tired after work and I just want to sleep, but...)"
        scene cc-195 with dissolve
        c "I usually end work quite late, but I think if you wanna hang around, we could catch up after?"
        scene cc-196 with dissolve
        p "Let's do that, Caroline."
        # Transition to bathroom
        scene cc-207 with fade
        p "It looks like she's warming up a little more to you, [p]."
        p "Hopefully I'll be able to get closer to her tonight."
        scene cc-208 with dissolve
        p "Alright. Don't screw this one up [p]. She's different from the rest."
        scene cc-209
        $ renpy.pause()
        scene cc-210
        $ renpy.pause()
        scene black with fade
        "A few moments later..."
        ## few moments later
        stop music fadeout 1
        scene cc-197 with fade
        c "Oh, that was a tough shift!"
        p "Oh no! I hope it wasn't {i}too{/i} tiring."
        scene cc-198 with dissolve
        c "I'll be fine."
        scene cc-199 with dissolve
        p "How about a few drinks? Everyone's gone."
        scene cc-200 with dissolve
        c "Great idea."
        c "Dante's original?"
        p "You know me!"
        scene cc-205 with dissolve
        p "It's so different. Usually it's loud, the music is blaring and now all of a sudden it's so quiet."
        c "That's an interesting observation."
        p "So is it always you that works here?"
        scene cc-201 with dissolve
        c "Yes, but there used to be another girl here."
        scene cc-202 with dissolve
        c "She's working at another bar that the manager here owns."
        p "What's the trickiest part of the job?"
        c "It's not too bad actually. Turning up everyday is probably the hardest part."
        scene cc-203 with dissolve
        c "It's just so tiring sometimes!"
        p "Yeah, I can understand that."
        scene cc-205 with dissolve
        $ renpy.pause()
        scene cc-206 with fade
        p "Thanks for the drink. I'll make it up to you, for sure."
        c "Don't worry about it, [p]."
        scene cc-204 with dissolve
        c "If you're ready we can go - and continue this at my place."
        p "The fun just never ends, huh?"
        c "Not tonight."
        scene black with fade
        ## to house
        play music "sounds/caroline.mp3" fadeout 1
        scene cc-211 with fade
        p "You know, you're surprisingly energetic. If I worked the whole night I'd be crashing in bed."
        c "Don't say that, [p], you're making me feel sleepy..."
        scene cc-212 with dissolve
        p "Just have a lie down then, take a rest."
        scene cc-213 with dissolve
        c "If I do that, I'll fall asleep."
        p "Just close your eyes. You know you want to."
        scene cc-214 with dissolve
        c "..."
        scene cc-215 with dissolve
        c "Alright."
        scene cc-216 with dissolve
        $ renpy.pause()
        scene cc-217 with dissolve
        p "Haha, you don't need to torture yourself, you know?"
        p "We can always chill another time."
        c "We don't... have too much time..."
        scene cc-218 with dissolve
        p "What are you talking about, Caroline? Of course we do."
        p "..."
        p "Caroline?"
        scene cc-219 with dissolve
        "Damn. Out just like that that."
        scene cc-220 with dissolve
        p "I'll carry you to bed alright Caroline?"
        scene cc-221 with dissolve
        "..."
        scene cc-222 with dissolve
        p "{i}Sigh{/i}... come, come."
        ## to bedroom
        scene cc-223 with fade
        p "You're quite light, Caroline!"
        scene cc-224 with dissolve
        p "Though, I suppose, I never really expected you to be heavy in the first place, thanks to these guns."
        scene cc-225 with dissolve
        "That poor girl must be exhausted, but she looks so vulnerable and beautiful right now."
        scene cc-226 with dissolve
        "It wouldn't be right, but I really want to have a feel of Caroline, to touch her, to put my hands on her."
        c "...[p]."
        scene cc-227 with hpunch
        p "!! I wasn't thinking of anything I swear! I mean-"
        p "..."
        p "I was just on my way out, aha Caroline, I really need to give you some rest, I mean-!"
        c "Stoooop...."
        scene cc-228 with dissolve
        p "Huh?"
        scene cc-229 with dissolve
        play music "sounds/alchemy.mp3" fadeout 1
        c "Help me, [p]... It's so tight."
        p "What's so tight, sorry?"
        c "Mmm...! It's digging into my back..."
        p "Oh right, gotcha. Hang on."
        scene cc-230 with dissolve
        "My heart thudded as I my fingers got closer to Caroline's top. Is she really asking me to help take her top off?"
        "I fumble around, before finally undoing the clip, letting her breasts free."
        scene cc-231 with dissolve
        p "Alright, done. Anything else?"
        c "...my pants... I can barely move my legs, please get em' off..."
        p "You sure, Caroline?"
        c "Mmm..."
        scene cc-232 with dissolve
        p "Okay, let's see..."
        "So do I pull up or down? Man female clothing confuse me. Let's try this."
        scene cc-233 with dissolve
        "This doesn't seem right... but damn, does Caroline go commando normally? What the-!"
        "But god is that the perfect pussy, I just wanna-"
        c "Get it offff...."
        p "On it, on it. I just got a little distracted."
        c "{i}Unintelligle mumbling {/i}"
        scene cc-234 with dissolve
        $ renpy.pause()
        scene cc-235 with dissolve
        "My god. Caroline is stunning. Let me take another look..."
        "I probably shouldn't go further, or she'll take me for a creep and I don't want to fuck this up."
        p "Anything else, Caroline?"
        c "Don't go... stay..."
        p "You want me to stay here, with you?"
        c "Mmmm..."
        p "Oh, okay."
        scene cc-237 with dissolve
        p "Just... right there then."
        c "Mmm~"
        scene cc-236 with dissolve
        p "God I can barely help myself, I just want to grab her, kiss her neck and nibble away at her ear."
        p "Hang tight, [p]. It's good enough that she let you get this close already, but this might be a test for statuatory rape."
        p "I'll be patient for one more night."
        scene cc-238 with dissolve
        p "Get some sleep now, and try again tomorrow..."
        stop music fadeout 1
        scene black with fade
        ## sleep
        "A sleepful night passes..."
        scene cc-239 with fade
        $ renpy.pause()
        scene cc-240 with dissolve
        p "Uh... where am I?"
        p "This isn't my room..."
        scene cc-241 with hpunch
        p "Caroline?!"
        scene cc-242
        $ renpy.pause()
        scene cc-243 with dissolve
        p "..."
        "She's gone."
        scene cc-244 with dissolve
        p "I guess I was pretty tired that night too. I passed out pretty quick."
        p "She probably woke up before me, and if I'm lucky, I'll get some coffee already made for me."
        ## Transition
        scene cc-245 with fade
        p "Urgh, I feel the creak in them ol' bones!"
        c "Good morning, [p]."
        play music "sounds/new.mp3" fadeout 1
        scene cc-246 with dissolve
        c "Did you sleep well last night?"
        p "Oh hey Caroline! Surprisingly well, I'd say. How about you?"
        scene cc-247 with dissolve
        c "I slept very well too, I must have been pretty tired."
        p "Haha, you were!"
        p "Must have been the mix of alcohol and long day."
        scene cc-248 with dissolve
        c "Well, I feel a lot better now, so that's good."
        scene cc-249 with dissolve
        c "I don't remember much about last night though. Tell me..."
        c "Did we... do anything?"
        p "Do... anything?"
        scene cc-250 with dissolve
        c "Well, you know..."
        p "I... don't think so."
        scene cc-251 with dissolve
        c "Oh, in that case, did I say anything?"
        p "The last thing you said was that we didn't have much time or something, then you passed out."
        p "What did you mean by that, anyway?"
        scene cc-252 with dissolve
        c "Ah."
        c "I'm going on a trip soon, an academic trip. We won't be able to meet for much longer before then, that's all."
        p "But you'll be back, right?"
        scene cc-253 with dissolve
        c "In a few weeks."
        scene cc-254 with dissolve
        p "A few weeks too long, I'd wager."
        scene cc-255 with dissolve
        c "That was my thought. I remember wanting to hit home base with you last night, so I was just curious if I went ahead with it."
        scene cc-257 with hpunch
        p "Whoa, hang on, what?!"
        p "You should've let me know!"
        scene cc-256 with dissolve
        c "Take the hints, [p]!"
        scene cc-258 with dissolve
        p "Y-you were sleeping, what- I can't move on that!"
        scene cc-259 with dissolve
        c "Maybe. So what's the next best thing?"
        scene cc-260 with dissolve
        p "The next best thing? Wha- oh."
        p "Um, err... like, now?"
        scene cc-261 with dissolve
        c "..."
        p "Oh, okay, got it."
        p "..."
        p "So, do you want to, like, you know, like, fuck or something?"
        p "Wait, that came out wrong, let me-"
        scene cc-262 with hpunch
        c "Oh my {i}god{/i}, hahaha!"
        scene cc-263 with dissolve
        c "Just let me do the work, [p], and stop talking just a bit."
        scene cc-264 with dissolve
        c "I love to hear your voice, but just this once..."
        ## sexy times
        scene cc-266 with dissolve
        "She embraced me and attacked my lips with such voracity that I could never have imagined from her, and I responded in kind."
        c "Mmm..."
        "The raw passion overtook me, and suddenly, we were laid bare and I was in a world where there were only two of us."
        scene cc-267 with dissolve
        "Just us two, and our undying lust."
        scene cc-269 with dissolve
        "We broke apart for a brief respite."
        p "My, my. Still waters run deep, Caroline."
        scene cc-268 with dissolve
        c "What can I say? I like to work hard and play hard."
        "Her cheeks were flushed and she had a glazed expression in her eyes."
        scene cc-270 with dissolve
        c "I hope you're enjoying the foreplay, [p], but let's get back down to earth."
        c "I think it's time for the main event."
        scene cc-271 with dissolve
        "Perhaps it was me with the glazed expression on my face, as I came back to reality."
        scene cc-272 with dissolve
        p "You're just so devastatingly beautiful, I got lost in your eyes there. We got time, right girl?"
        p "Come closer for a bit."
        scene cc-273 with dissolve
        "I drew her closer and embraced her. Her soft breasts pushed against my chest and I could feel her nipples hardening."
        c "You're so strong, just pulling me like that~"
        scene cc-274 with dissolve
        c "What are you-"
        scene cc-275 with dissolve
        c "Ooh!"
        scene cc-276 with dissolve
        "I can't help myself, Caroline. You're too hot. I love your lips."
        "Your smooth skin... those soft cushions on your chest that make you so lovely to hold in my hands."
        "After a while, we reluctantly pull away again."
        scene cc-277 with dissolve
        c "Enough, enough~!"
        c "Your lips taste great but I'm more curious about how something else tastes~"
        scene cc-278 with dissolve
        c "And I think I'm just about ready down there."
        c "Lay over there, and let's see who you really are."
        scene cc-279 with dissolve
        p "Show me what you got."
        scene cc-280 with dissolve
        c "For a girl that is quite comfortable in her skin, I think it's a little funny how I'm feeling a bit shy now."
        p "There's no need to be, Caroline. You're gorgeous."
        scene cc-281 with dissolve
        c "Oh, [p]. I've been wanting to do this for a long time."
        scene cc-282 with dissolve
        c "It's a healthy sex drive of a young adult, right?"
        c "Men turn women on."
        p "There's no need to justify it, Caroline. Sex is great."
        scene cc-283 with dissolve
        c "Hey, you're right."
        scene cc-284 with dissolve
        "She nimbly mounted me and my heart rate leapt as I realised I that I was really, truly about to insert my cock in Caroline's pussy."
        c "I'm so horny right now, you won't believe it."
        scene white
        $ renpy.movie_cutscene("animations/c1.mp4", loops=0, stop_music=False)
        scene cc-285 with dissolve
        p "Oh my god Caroline, you are so tight."
        c "That's good, isn't it [p]?"
        c "Nice and tight for you so we can feel good together!"
        c "I'm going to start rocking now okay [p]?"
        image c2 = Movie(play="/animations/c2.mp4")
        scene c2 with dissolve
        "Oh my god. Her vagina was gripping my member so tight as my penis thrust in and out of her folds."
        c "D-does this feel good?"
        p "Oh Caroline you have no idea."
        c "I feel really hot right now~"
        c "Mmm... mmm..."
        "She pushed herself up off my penis and would let herself fall slowly, gyrating her hips at the very end."
        "She moaned and exhaled sharply in tandem with these bursts of pleasure."
        p "You're so slippery down there."
        c "Yeah? That's because of you, you know, and your wonderful cock."
        p "The language coming from your mouth!"
        c "I'm just being honest, [p]. Your cock feels amazing in my pussy."
        p "Can you go faster?"
        c "Faster? Say please."
        p "Please, Caroline you beautiful girl, go faster."
        c "With pleasure~"
        image c3 = Movie(play="/animations/c3.mp4")
        scene c3 with dissolve
        c "Aa~!"
        c "The... heat... it just feels so fucking good!"
        p "Whoa!"
        c "Fuck me, [p]. Fuck me hard!! Aaah~!!!"
        "Christ this girl just let pleasure get to her head."
        c "Harder harder harder harder!"
        image c4 = Movie(play="/animations/c4.mp4")
        scene c4 with dissolve
        "Her tits jiggled in front of my face as she sped up."
        "I couldn't believe that I was fucking such a naturally beautiful woman."
        c "Oh fuck me, [p]! I'm close, I'm close!"
        p "Cum for me, you cock loving slut!"
        scene cc-286 with flash
        c "Aah~!!"
        "Her body shook against mine as she orgasmed."
        "I was amazed at how such a small body could generate so much force."
        scene cc-288 with dissolve
        c "Phew, I just came over your penis, [p]..."
        c "You just made me climax, oh you..."
        c "By the way, did you say I was a cock loving slut?"
        p "Erm, it was a heat of the moment sort of thing, haha."
        c "I'm just passionate, hehehe~"
        ## sex over
        scene cc-289 with fade
        c "That was great sex, wasn't it [p]?"
        p "Never expected it from you, you can be such a minx."
        scene cc-290 with dissolve
        c "You too!"
        p "No but, really, you've got a great pussy."
        c "And your penis was the perfect size. Really filled me out, I think."
        c "I might have gone a {i}little{/i} too hard..."
        scene cc-291 with dissolve
        c "Ouch."
        p "Man, Caroline, I'm still surprised you go this in you."
        scene cc-289 with dissolve
        c "Didn't you say it already? Still waters run deep. There's more than all of us than meets the eye."
        p "Good for you, Caroline. I think I'm in love."
        p "So, when again is your trip?"
        scene cc-291 with dissolve
        c "I don't exactly know when, I don't like to check. I hope that it'll go away if I don't check."
        p "What is it, in a few days?"
        c "Something like that. Week, maybe? I don't know."
        p "Maybe it's time for me to go on a trip too - a break doesn't sound like a bad idea at all."
        c "Yours would be a fun trip. Mine would be one of those boring ones."
        p "I'm sure you'll get to have some fun too, in between all the academic stuff."
        c "I'm not counting on it."
        scene cc-289 with dissolve
        c "That's why I'm planning to have all the fun before I go."
        p "Amen to that."
        scene cc-292 with dissolve
        c "But enough about that. Coffee, [p]?"
        scene cc-293 with dissolve
        p "It would be a pleasure."
        scene black with fade
        $ carolinebarlvl +=1
        $ daytime = 1
        $ day += 1
        $ pocketmoney = True
        $ dante = False
        $ russian = False
        $ drinks = False
        call cryptoChange from _call_cryptoChange_1
        $ bogged = False
        $ daytimes = str(daytime)
        if "coffee" in items:
            $ items.remove("coffee")
        if "water" in items:
            $ items.remove("water")
        call daykeep from _call_daykeep_46
        jump map
    if carolinelvl == 6 and carolinebarlvl == 4:
        scene black
        play music "sounds/dreams.mp3" fadeout 1
        scene cc-190 with fade
        p "How's it going Caroline!"
        p "I hope you're not feeling too sore!"
        scene cc-193 with dissolve
        c "Hi, [p]. Sorry, but I'm just going to concentrate on my work for a bit."
        p "Aww."
        p "That's alright. I'll see you around."
        scene cc-194 with dissolve
        c "Thanks for understanding."
        "Hmm, I thought she would be warming up to me by now, surely."
        "I mean I dicked her just now."
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
