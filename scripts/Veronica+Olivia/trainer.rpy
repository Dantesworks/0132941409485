label trainer:
    menu toys:
        "Vaginal dildo" if dildo:
            p "Tell me Olivia, do you think you would enjoy my cock in your pussy?"
            scene o-42
            o "Never."
            p "Good. Because I've got the next best thing."
            scene o-47 with dissolve
            $ renpy.pause()
            scene o-46 with dissolve
            o "Hm?"
            p "How long will you be lecturing today for?"
            scene o-43 with dissolve
            o "A few hours, why?"
            p "I'm going to insert this dildo into your pussy, and you have to keep it in for the entire class."
            scene o-44 with dissolve
            o "Why?"
            p "Because it'll be fun, but above all, because I said so."
            scene o-45 with dissolve
            o "That's disgusting! To have an object like that in my vagina for hours?"
            p "Is it digusting because you'll make a mess?"
            o "Never!"
            scene o-41 with dissolve
            p "Good. Then you can deal with it."
            p "Now open wide and let me put it in."
            scene o-42 with dissolve
            o "No, pervert. Give it to me, I'll put it in myself!"
            menu:
                "Put it in for her." if plugged:
                    $ vdildo2 = True
                    if olivialvl == 3:
                        $ olivialvl = 4
                    scene o-41 with dissolve
                    p "The butt plug was special in that only another person can take it out, and this is similar."
                    p "Trust me, it's easier to for someone else to help you."
                    scene o-44 with dissolve
                    o "(It's awkward and painful when I put it in myself.)"
                    o "(It might be easier for me to just let him.)"
                    scene o-45 with dissolve
                    o "...I will try it, just this once okay?"
                    p "Spread your legs."
                    scene o-52 with dissolve
                    p "What a beautiful view. You should spend more time in this position, Slut."
                    o "What are you waiting for?"
                    p "Hurry up and put it inside me!"
                    scene o-53 with dissolve
                    o "Aah!"
                    p "See? Nice and quick. Look how much easier it is if we work together."
                "Let her put it in.":
                    p "Very well."
                    scene black with fade
                    scene o-48 with fade
                    p "Is it in?"
                    scene o-49 with dissolve
                    o "Yes."
                    p "Show me."
                    scene black with fade
                    scene o-50 with fade
                    o "..."
                    o "See? I'm not lying."
                    p "Good Slut. It's staying there just by itself?"
                    p "You must be very tight down there."
            p "Hahahaha!"
            p "Off you go to class then. I'll be watching on the side."
            ## Lecture
            scene black with fade
            play music "sounds/cinematic.mp3" fadeout 1
            scene o-67 with fade
            o "Page 36 of the textbook is a good place to look up how to solve the problem."
            scene o-68 with dissolve
            o "Go take a quick read for 5 minutes."
            scene o-69 with fade
            o "(I'm not used to having things in my vagina, it's so sensitive!)"
            o "(I can't stop my vagina secreting juices out to lubricate it.)"
            scene o-70 with dissolve
            o "(It's mixing in with my sweat and it's just a sticky, moist mess!"
            o "(How much longer do I have to teach until the class is over?)"
            o "(I can't wait!)"
            scene black with fade
            scene o-71 with fade
            o "(Thank god... the class is finally over.)"
            scene o-72
            p "You squirmed a few times, but other than that, you acted pretty normal."
            scene o-73 with hpunch
            p "This must be too easy for you."
            scene o-74 with dissolve
            o "The class is over, take your damn dildo back."
            scene o-75 with dissolve
            o "Here."
            o "(It's soaking in my juices and sweat...)"
            scene o-76 with dissolve
            p "Turns out you did make a bit of a mess."
            p "I don't like sluts that can't clean themselves."
            scene o-77 with dissolve
            p "So go on, clean it up."
            scene o-79 with dissolve
            o "I don't have a cloth or tissue with me."
            p "Use your mouth."
            if plugged2:
                o "I can't, its disgusting!"
                p "You haven't tasted yourself before?"
                scene o-78 with dissolve
                if olivialvl == 4:
                    o "It was different!"
                    p "You've tasted yourself before and had me fuck you while you were on the toilet."
                    p "You are as filthy as it gets."
                else:
                    o "Of course not!"
                    p "Always time for a first, just like how I came into the bathroom the other day and fucked you while you were shitting."
                    p "You can't be more filthy than that."
                    p "In fact, you said you'd rather taste yourself rather than have me fuck you while on the toilet."
                scene o-80 with dissolve
                o "..."
                p "I don't want to make you do this the hard way, Slut. Go on, have a taste."
                o "(I'll do a small lick, and hopefully that won't make him embarrass me more."
                scene o-82 with dissolve
                # Lick
                o "(Urgh, it's still warm from the depths of my vagina.)"
                o "(Why is it so smelly?)"
                scene o-83 with dissolve
                o "(It's so slimy and salty, is this what vagina and sweat mixed together tastes like?"
                o "(I can't believe this. Me, Olivia, a highly respected lecturer..."
                scene o-84 with dissolve
                " (...made to lick a dildo that was forced into my vagina!)"
                scene o-85
                o "This is disgusting! How can you make me do this!"
                p "Easily."
                p "Did you taste good?"
                scene o-86 with dissolve
                o "{i}Sob{/i}"
                p "Now clean it up with your mouth properly."
                p "Just like it's a lollipop."
                scene o-87 with dissolve
                o "{i}Gulp{/i}"
                scene o-88 with dissolve
                o "{i}Lick, lick, lick, lick{/i}"
                o "(I can't believe I'm licking my own juice off a dildo that's been in my pussy for hours.)"
                scene o-89 with dissolve
                o "(Just hang in there for now, Olivia. Keep [p] happy for now and think of a way out of this.)"
                scene o-90 with dissolve
                o "...I'm finished."
                p "Nice and clean. Good job, Slut."
                scene o-91 with dissolve
                o "{i}Sob{/i}"
                p "Don't cry Slut! I think you've learnt something new today."
                p "I can't wait to see what we'll learn next time."
            else:
                o "No way! That's unsanitary."
                o "I'm going now, please leave me alone."
                "I just gotta keep at it. She'll come around."
            $ vdildo = True
            $ daytime = 4
            $ daytimes = str(daytime)
            if plugged2 and olivialvl == 6:
                $ olivialvl = 7
            call map_alt from _call_map_alt_17
        "Butt plug" if plug and vdildo:
            $ plugged = True
            p "We've played with your tight pussy."
            p "Now it's time to see how your butt is."
            scene o-42
            o "That should be out of bounds!"
            p "That's not for you to say."
            scene o-55
            p "I have here a very special butt plug."
            p "It gets bigger once it's inside you."
            scene o-54 with dissolve
            o "Let me guess... I have to put it in me?"
            p "Well done, you're getting used to this, Slut."
            scene o-49 with dissolve
            o "I just want to get it over and done with so I don't need to see your stupid gloating face as much."
            menu:
                "I'm putting in in for you" if vdildo2:
                    p "While it's possible to put on the butt plug by yourself. It's easier to have someone else help you."
                    o "I'm not letting you near my butt if I can help it, thank you very much."
                    p "But you can't help it. Bend over, Slut. Don't make me angry."
                    scene o-54 with dissolve
                    o "...yes."
                    p "Yes who?"
                    o "Yes... master."
                    p "Bend over."
                    scene o-59 with dissolve
                    p "Now show me your asshole."
                    scene o-60 with dissolve
                    $ renpy.pause()
                    scene o-61 with dissolve
                    $ renpy.pause()
                    scene o-62 with dissolve
                    o "I'm ready."
                    scene o-63 with dissolve
                    p "You're still holding back."
                    p "Relax your asshole."
                    o "..."
                    scene o-64 with dissolve
                    p "What a cute little asshole."
                    o "Just put it in me already."
                    scene o-65 with dissolve
                    $ renpy.pause()
                    scene o-66 with dissolve
                    o "Ah, it's so big compared to my small butthole!"
                "Fine":
                    p "Fine."
                    o "And I can put this one in myself, perv."
                    scene black with fade
                    scene o-48 with dissolve
                    p "Is it in?"
                    scene o-49 with dissolve
                    o "Yes."
                    p "You should know that's not good enough. Show me."
                    scene o-56 with dissolve
                    o "Check quickly, I have to get to class."
                    scene o-57 with dissolve
                    p "All those hours in the gym have paid off. You have great ass."
                    o "..."
                    o "It's in see?"
                    scene o-58 with dissolve
                    p "Nice and tight. Good!"
                    # Show
                    p "This is a special butt plug because the wearer can't remove it themselves."
                    p "Someone else must help them remove it."
                    scene o-56 with dissolve
                    o "You're lying."
                    p "You think I'm trying to trick you?"
                    p "If you didn't interrupt me at the start, I would've told you. Now listen, Slut."
                    scene o-14 with dissolve
                    p "A butt plug is different to a vaginal dildo. You can still piss around a dildo."
                    p "But this butt plug? I'm afraid you'll be sealed tight until I let you out."
                    scene o-19 with dissolve
                    o "You filthy bastard."
                    p "It won't be me who's going to be filthy at the end of it, it's you."
                    p "Tell you what, if you give a good lecture, I might let you out at the end of the day."
                    scene o-54 with dissolve
                    o "Monster."
            p "Time for class, Slut."
            # lecture
            scene black with fade
            play music "sounds/cinematic.mp3" fadeout 1
            scene o-67 with fade
            $ renpy.pause()
            scene o-68 with dissolve
            o "You can figure out the pH of the solution by plugging in the concentration of hydrogen ions into the equation."
            scene o-92 with fade
            o "(Ugh, The butt plug is so big that it's starting to really hurt.)"
            scene o-93 with dissolve
            o "(It's so thick it's blocking my rectum and stimulating my internal anal sphincter to contract!)"
            o "(My body is trying to pass it out and I feel like I have to take a shit.)"
            scene o-95 with dissolve
            o "(But I don't know if there's real shit I have to pass out, or if it's just the butt plug!)"
            scene o-94 with dissolve
            o "(It's so uncomfortable, I can't wait for the class to be over.)"
            scene black with fade
            scene o-96 with fade
            p "Another lecture complete, Slut. Are you learning a lot?"
            o "We're done, take the plug out."
            p "Why? You don't like it?"
            scene o-98
            o "Of course I don't like it, are you stupid?"
            o "Take it out!"
            p "Ask me properly, and I will."
            o "..."
            scene o-97 with dissolve
            o "Please, take the butt plug out!"
            p "I said, ask me properly, Slut."
            scene o-99 with dissolve
            o "...bastard."
            scene o-100 with dissolve
            o "Please, master, take my butt plug out."
            p "Where do you want me to remove it from?"
            scene o-101 with dissolve
            o "Please.... take it out from my anus."
            p "Good Slut. If you ask nicely, you get what you want."
            p "Now bend over."
            scene o-102 with dissolve
            p "It's all plugged up, but I can smell the stink from here."
            p "You're plugged up full of shit, aren't you?"
            o "It-It's just the butt plug!"
            scene o-103 with dissolve
            o "Ah~!"
            scene o-104 with dissolve
            o "That really hurt, you bastard!"
            p "Feeling better? The more pain I put your through, the sweeter the release."
            p "Remember, I only do this to help you, because I love you."
            p "This is something that you will need to learn."
            o "Shut up, you twisted rapist!"
            scene o-105 with dissolve
            o "(The full feeling's still there... I need to go to the bathroom!)"
            scene o-106 with dissolve
            o "I'm going to the restroom, I'm done for today..."
            menu:
                "Follow her" if vdildo2 and olivialvl >= 6:
                    # toilet sex
                    "I'm following her to the bathroom."
                    scene black with fade
                    scene o-107 with fade
                    o "(You're a proud woman, Olivia. You can't let these dirty men manipulate you all the time.)"
                    o "(The monster made me wear a butt plug for a whole day - leading me to have to run shamefully to the bathroom.)"
                    scene o-108 with dissolve
                    o "(I couldn't even use the bathroom, having to store all this shit in my stomach!)"
                    o "(The butt plug was so big, it even pushed onto my urethra, blocking my urine.)"
                    o "(There's so much piss and shit stored up inside me.)"
                    scene o-109 with dissolve
                    o "(I'll just have to bear with this until I can destroy the evidence.)"
                    o "(Until then, I'll give [p] a little bit of what he wants, to make him feel like he's in charge.)"
                    p "Surprise motherfucker!"
                    scene o-110 with hpunch
                    o "What are you doing here?!"
                    o "Can't you see I'm using the toilet?!"
                    p "I know you're dirtying your asshole and pussy with all the shit and piss that you're full of."
                    o "What do you want!"
                    o "I already gave you what you wanted today!"
                    p "You are a slut, and you haven't given me everything I wanted yet."
                    p "And now, I want you to spread your legs."
                    scene o-111 with hpunch
                    o "I...!"
                    o "(Didn't you say, Olivia, that you would just give him what he wants?)"
                    o "(Yes, make him feel like he's in charge, then screw him over when he least expects it!)"
                    o "My pleasure!"
                    o "But it's my dirt getting all over your penis if you think of doing something funny!"
                    o "In fact, I'd like to see you try!"
                    p "What, is that a challenge?"
                    o "Come and get it! Now you're getting cold feet?"
                    p "You're asking for it now."
                    scene o-112 with flash
                    o "Whaa-! I'm dirty down there, you're not going to let me wipe first?!"
                    o "Are you for real?"
                    p "Woo it stinks here! Who knew a hot woman like you could make such dirty smells?"
                    o "You bastard!"
                    scene white
                    show o3 with dissolve
                    p "Get used to this, Slut."
                    o "Y-Your penis is picking up my filth and pushing it inside me!"
                    p "You're wet down there. Is that your piss or your pussy juice?"
                    p "This is what you asked for, wasn't it? Don't tell me you're the one changing your mind?"
                    hide o3
                    show o4 with dissolve
                    o "You think you're winning? Ah~!"
                    o "I baited you into rubbing your penis all over my filth! I hope you're proud of yourself now!"
                    o "But still, I'd rather use my tongue to lick it off myself than have you push it deeper inside me!"
                    p "Be careful what you wish for, Slut."
                    "Damn she has a juicy pussy."
                    p "Show me your tits, whore. Let's see those puppies bounce!"
                    hide o4
                    show o5 with dissolve
                    o "My nipples!"
                    p "You've got gorgeous tits, Slut. We should parade them around, show the whole world!"
                    p "Nice and pink... you're just like those prostitutes in a brothel."
                    p "Your nipples, are they...?"
                    hide o5
                    show o6 with dissolve
                    p "Look at how erect your lewd nipples are!"
                    p "Don't tell me you're getting aroused!"
                    o "I'm - letting - you - fuck - me - to - prove - a - point!"
                    o "Ah - ah - ah - I'm not-"
                    o "- ah - ah - enjoying this-"
                    o "- ah - ah - at all!"
                    p "That's a shame, because I have... Argh!!"
                    hide o6
                    scene o-114 with dissolve
                    $ renpy.pause()
                    scene o-115 with flash
                    $ renpy.pause()
                    scene o-116 with flash
                    $ renpy.pause()
                    scene o-118 with dissolve
                    o "You spread your dirty cum all over my belly! How dare you!"
                    o "I...I..."
                    scene o-117 with dissolve
                    o "I can't believe you actually fucked me... on the toilet..."
                    scene o-119 with dissolve
                    o "...and made my vagina and anus into a mess of my filth and your cum."
                    o "When I walk home tonight, everyone will be able to smell me."
                    o "I am a proud woman, I studied hard to get my doctorate in chemistry."
                    o "But now when people stare at me on the street..."
                    o "They'll see a dirty, brainless..."
                    scene o-120 with dissolve
                    o "Bimbo slut... {i}Sob{/i}."
                    p "You've learnt another lesson today."
                    p "Remember it well."
                    image o3 = Movie(play="/animations/o3.webm")
                    image o4 = Movie(play="/animations/o4.webm")
                    image o5 = Movie(play="/animations/o5.webm")
                    image o6 = Movie(play="/animations/o6.webm")
                    $ plugged2 = True
                    $ renpy.pause()
                "Leave":
                    "It's been a long day. I'll leave her alone and call it a day."
            $ daytime = 4
            $ daytimes = str(daytime)
            call map_alt from _call_map_alt_18
        "Slutty outfit exhibition" if olivialvl >= 6:
            jump olivia_outfit
        "Dance" if olivialvl > 9:
            scene o200 with fade
            p "I don't know about you, but I had restful sleep last night."
            p "And you, slut?"
            scene o201 with dissolve
            o "It was fine."
            p "Was it? In that case I hope you've learned your dance well."
            p "Go on now, aren't you eager to show me what you've learnt."
            o "I didn't learn this just for you."
            scene o203 with dissolve
            o "(One day, I will show this dance to the one I love. Until then...)"
            p "Whatever. But you will dance for me."
            p "Come on now, get changed. Don't stall."
            o "..."
            # changed
            play music "sounds/brite.mp3" fadeout 1
            scene o-135 with dissolve
            $ renpy.pause()
            scene o-136 with dissolve
            $ renpy.pause()
            scene o-137 with dissolve
            $ renpy.pause()
            scene o-138 with dissolve
            $ renpy.pause()
            scene o-139 with dissolve
            $ renpy.pause()
            scene o-140 with dissolve
            $ renpy.pause()
            scene o238 with dissolve
            $ renpy.pause()
            scene o-121 with dissolve
            p "Beautiful. Those tits and hips of yours are wasted with any clothing less salacious."
            p "You look the best dressed like a slut. You should dress like this more."
            scene o239 with dissolve
            p "But I suppose, you already do a lot, don't you? I bet you have a huge collection of slutty lingerie at home!"
            o "Weren't you the one who said not to stall?"
            p "Well off you go."
            # animation ??
            $ renpy.movie_cutscene("animations/o7.webm", loops=0, stop_music=False)
            scene o240
            p "Hey, looks like you've got some talent at this. You sure you don't want to do this for a living?"
            scene o241 with dissolve
            o "{i}Pant... pant...{/i}"
            p "All this dancing has really worked you up a sweat!"
            p "You need to cool down a bit."
            o "Okay."
            p "So take your clothes off."
            o "What?"
            p "You're so hot and bothered, take some clothes off and cool down!"
            scene o242 with dissolve
            o "I..."
            p "You're used to this by now, aren't you? Come on, we're already in the mood."
            o "The lingerie is good, it helps me soak up my sweat. I... don't really want to-"
            scene o243 with dissolve
            o "I'm... dirty right now."
            p "What, it's just a little bit of sweat!"
            scene o244 with dissolve
            o "P-Please, this is one thing I don't like, it's my phobia."
            p "And you liked everything else? Slut. Give me a break. Take off your clothes now."
            scene o245 with dissolve
            o "{i}Sob{/i}"
            # strip
            scene o246 with dissolve
            $ renpy.pause()
            scene o247 with dissolve
            p "Wow, I don't even need to oil you up. Look how sweaty and dirty you are."
            p "Hmm, I can even smell your stench."
            scene o248 with dissolve
            p "No wonder you're shy about it. You should be too, you fucking slut."
            scene o249 with dissolve
            o "I-I can't help it..."
            scene o250 with dissolve
            o "This is just who I am..."
            p "This is who you are."
            p "Aww, why do you look so sad? I like to see you happier."
            p "Go on, dance."
            scene o251 with dissolve
            o "Bastard..."
            o "I can't."
            p "You were doing so well just before?"
            p "You need some encouragement?"
            # snap
            scene o251 with flash
            scene o252 with hpunch
            o "Please! The flash light will make my sweat show up even more!"
            scene o253 with dissolve
            p "Alright, alright. Let me give you a choice."
            p "Either dance for me now, or suck me off."
            p "You've done both before. You can't tell me that dancing is worse than sucking me off?"
            scene o255 with dissolve
            o "I..."
            scene o256 with dissolve
            o "(Olivia! Why can't you just dance, why is it so difficult?)"
            p "Well?"
            scene o257 with hpunch
            o "Fuck you, [p] I can't believe I'm doing this for you."
            p "You're going give me a blow job?"
            scene o257 with dissolve
            o "I would rather.. service you, than show off... in my sweat..."
            scene o258 with dissolve
            p "I can barely believe it. Look how far we've come, slut."
            p "Down on your knees."
            ## BJ
            scene o259 with dissolve
            p "This is the perfect view, slut. With you on your knees looking up into my eyes."
            p "Do you like the view?"
            o "Just hurry along."
            p "Fine."
            scene o260 with dissolve
            o "(Oh my god, I forgot how big it was...)"
            p "That was a cute reaction, slut. Are you salivating yet?"
            p "Come on. Start sucking."
            image o8 = Movie(play="/animations/o8.webm")
            scene o8 with dissolve
            o "Mmmm. Mmm. Mmm. Mmm."
            p "You sure you're not enjoying this?"
            o "Mmm!"
            p "You're making such lewd noises, you're really making love to it!"
            p "You've done this before, haven't you!"
            o "Mm!!"
            p "You're really trying to finish me off quick. Are you thinking that you want to get this over and done with as quickly as possible?"
            p "Aww, that's really cute. But fuck, it might just work..."
            image o9 = Movie(play="/animations/o9.webm")
            scene o9 with dissolve
            p "Oooh you're one tight little whore."
            p "You should've let me know you had this skill since day 1!"
            p "Ah shit, I'm cumming! Receive me!"
            scene o261
            $ renpy.pause()
            scene o262 with flash
            $ renpy.pause()
            scene o263 with flash
            $ renpy.pause()
            scene o264 with flash
            $ renpy.pause()
            scene o265 with flash
            $ renpy.pause()
            scene o266 with dissolve
            p "Damn, you're good. Had a lot of practice?"
            scene o267 with dissolve
            o "No."
            scene o268 with dissolve
            o "(Blow jobs aren't too hard... if he's happy with these maybe this will be all I need to keep him at bay...)"
            p "I love you slut, do you love me too?"
            scene o269 with dissolve
            o "Cheh!"
            o "Look at this disgusting mess you made on me! Mixed in with all my sweat!"
            scene o266 with dissolve
            p "Haha! Clean up. I'll see you again tomorrow."
            o "How... long is this going to go for..."
            call daykeep from _call_daykeep_53
            call map_alt from _call_map_alt_19
        "Naked Dance" if olivialvl > 11:
            scene black
            play music "sounds/cinematic.mp3" fadeout 1
            scene o270 with fade
            o "(I wonder if he's going to come around again.)"
            scene o271 with dissolve
            o "(Doesn't he know I have class to teach? Does he even know how disruptive he is?)"
            scene o272 with dissolve
            o "(Who am I kidding, he doesn't even care.)"
            scene o273 with dissolve
            o "(Hang on, why am I worried about him disrupting my classes?)"
            scene o274 with dissolve
            o "(I should be furious about him having his way with me!)"
            o "..."
            scene o275 with dissolve
            o "(But... I'm not.)"
            scene o276 with dissolve
            o "(Am I getting used to this?)"
            o "(Am I being desensitised?)"
            scene o277 with hpunch
            o "(Am I... secretly liking the way he treats me?)"
            scene o278 with dissolve
            o "No! I am a strong woman, and I hate men!"
            o "(But why do I hate men again?)"
            scene o279 with dissolve
            o "(It's because... I'm jealous.)"
            scene o280 with dissolve
            o "(I'm jealous because-)"
            scene o281 with hpunch
            play music "sounds/path.mp3" fadeout 1
            thug "Found you, you whore!"
            scene o282 with hpunch
            o "What?! W-Why are you here! I thought we had something sorted out!"
            scene o283 with dissolve
            thug "Didn't you get our letter?! Where the fuck is the shipment?"
            scene o284 with dissolve
            thug "You're making deals with the other rival gangs, aren't you!"
            thug "I'll teach you what we do to traitors!"
            scene o285 with dissolve
            o "No! I've been working hard, I swear! There have just been... distractions."
            scene o286 with hpunch
            thug "What the fuck?"
            scene o287 with dissolve
            thug "Distractions?"
            scene o288 with dissolve
            play music "sounds/jojofight.mp3" fadeout 1
            p "She's talking about me, thug."
            o "[p]! Stay back! You're only going to make it worse!"
            scene o289 with dissolve
            $ renpy.pause()
            scene o290 with vpunch
            $ renpy.pause()
            scene o291 with dissolve
            thug "And who the fuck is this?"
            scene o292 with dissolve
            p "I own this woman, not you. You don't tell her what to do."
            thug "So you're from a rival gang, huh?"
            p "Who I am isn't important. Just beat it."
            scene o293 with dissolve
            thug "Well, if you're not important, maybe I'll just take you out here and now!"
            p "Come."
            scene o294 with hpunch
            thug "HAAA!"
            scene o295 with dissolve
            p "Stand!"
            scene o296 with hpunch
            $ renpy.pause()
            # knocks him out
            scene o297 with dissolve
            $ renpy.pause()
            scene o298 with dissolve
            p "Lights out."
            scene o299 with dissolve
            o "Y-You knocked him out!"
            p "You're my property, Slut. And I protect my property."
            scene o300 with dissolve
            o "..."
            scene o301 with dissolve
            p "Call the cops, and get him out of here. I'm going to split."
            p "I'll come back tomorrow."
            scene o302 with dissolve
            o "I-"
            scene o303 with dissolve
            o "...okay."
            call daykeep from _call_daykeep_54
            $ olivialvl += 1
            call map_alt from _call_map_alt_20
            scene black
            scene o304 with fade
            p "Good day, Slut."
            scene o305 with dissolve
            o "[p]... I want to thank you for what you did."
            p "I told you, I protect my property."
            scene o306 with dissolve
            o "All this time, I thought you were the worst, but you did something brave."
            o "And you protected me."
            p "You need to rely on me, it's just a bit of tough love."
            scene o307 with dissolve
            o "I'm starting to understand what you're trying to do with me."
            "Is she thinking that she needs to rely on me for protection?"
            scene o308 with dissolve
            o "I have to admit though, I have a thing against men."
            p "What happened, was it that whole boyfriend thing?"
            scene o309 with dissolve
            o "I've never had a boyfriend."
            p "And I'm not trying to be your boyfriend. I'm here to be your master."
            scene o310 with dissolve
            o "..."
            scene o311 with dissolve
            o "Heh, well. If you must call yourself a master, there's not much I can do about it."
            p "I think we can get along just fine, Slut."
            P "I'll even make you a promise. Since apparently you hate men, I'll lay off on violating you."
            p "But in return, you must play the role of a dutiful slut, slave to her master."
            scene o312 with dissolve
            o "How degrading. But this offers more stability in our relationship."
            scene o313 with dissolve
            o "I don't have much of a choice. do I?"
            p "Your choice is to behave yourself, or not."
            p "If you behave yourself, I won't have to punish you."
            scene o314 with dissolve
            o "(What are you afraid of, Olivia?)"
            scene o315 with dissolve
            o "(I am afraid that I will grow to enjoy this slave play.)"
            scene o316 with dissolve
            o "Very well, but you better hold up your end of the bargain!"
            p "I'm a man of my word."
            scene o317 with dissolve
            o "Then fine."
            p "Good, very good. One day, I'll make you enjoy me dominating you."
            scene o318 with dissolve
            o "You can try!"
            p "So why don't we continue from last time? Dance for me again."
            p "But this time, naked. And I want you to work up a sweat."
            scene o319 with dissolve
            o "So be it."
            # dance and photos
            # strip
            scene o-135 with dissolve
            $ renpy.pause()
            scene o-136 with dissolve
            $ renpy.pause()
            scene o-137 with dissolve
            $ renpy.pause()
            scene o-138 with dissolve
            $ renpy.pause()
            scene o-139 with dissolve
            $ renpy.pause()
            scene o-140 with dissolve
            $ renpy.pause()
            scene o320 with dissolve
            $ renpy.pause()
            $ renpy.movie_cutscene("animations/o10.webm", loops=0, stop_music=False)
            scene o321 with dissolve
            o "Puff... puff"
            o "There, was that good enough?"
            p "I love how you're all hot and sweaty now. Let's quickly capture a few shots."
            scene o322 with dissolve
            o "You're still not happy?"
            p "Weren't you going to act the part of the dutiful slave, you slut?"
            p "Get on the table and spread your legs."
            o "..."
            scene o323 with dissolve
            $ renpy.pause()
            scene o323 with flash
            $ renpy.pause()
            scene o324 with dissolve
            $ renpy.pause()
            scene o324 with flash
            $ renpy.pause()
            p "Fuck, you're hot. Too bad I can't nail that pussy."
            p "Well, I suppose that's up to you, isn't it?"
            p "I would love for you to disobey me."
            p "Now get your hands in the air."
            scene o325 with dissolve
            $ renpy.pause()
            scene o325 with flash
            $ renpy.pause()
            scene o326 with dissolve
            $ renpy.pause()
            scene o326 with flash
            $ renpy.pause()
            p "Beautiful. All the time in the gym - for my pleasure!"
            p "You are truly the perfect slut."
            p "Now let me quickly get a few shots of that pussy up close."
            scene o327 with dissolve
            $ renpy.pause()
            scene o327 with flash
            $ renpy.pause()
            scene o328 with dissolve
            $ renpy.pause()
            scene o328 with flash
            $ renpy.pause()
            p "What a perfect little pussy."
            p "This pose serves you well, Slut!"
            scene o329 with dissolve
            o "Are you quite finished yet?"
            o "(I wouldn't have dreamed of letting him do this to me before.)"
            o "(Why am I giving it to him so easily?)"
            p "Just because you don't know how to shut up, we're doing one more."
            p "Push your tits together slut."
            scene o330 with dissolve
            $ renpy.pause()
            scene o330 with flash
            $ renpy.pause()
            p "Very good. I'm going to enjoy these photos at home now."
            p "Take care, Slut."
            scene o331 with dissolve
            o "W-why am I like this?"
            o "Hold it together, Olivia!"
            call map_alt from _call_map_alt_21
        "Never mind.":
            call map_alt from _call_map_alt_22
default vdildo = False
default vdildo2 = False
default plugged = False
default plugged2 = False
