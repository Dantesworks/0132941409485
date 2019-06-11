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
            if plugged2 and olivialvl == 3:
                $ olivialvl = 4
                ## Thankyou for playing
                scene black with fade
                scene splash7 with fade
                d "Thank you for playing Depravity. I hope you enjoyed playing with Olivia, brought to you by esteemed patron Raze."
            jump map
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
                "Follow her" if vdildo2:
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
                    scene o-111 with hpunch
                    o "Get out!"
                    o "I already gave you what you wanted today!"
                    p "You are a Slut and you will give be whatever I want, whenever I want."
                    p "And now, I want you to spread your legs."
                    scene o-112 with flash
                    o "No, please! I'm dirty down there, at least let me wipe first!"
                    p "It stinks here too! Who knew a hot woman like you could make such dirty smells?"
                    o "Stooop!"
                    scene white
                    show o3 with dissolve
                    p "Get used to this, Slut."
                    o "Y-Your penis is picking up my filth and pushing it inside me!"
                    p "You're wet down there. Is that your piss or your pussy juice?"
                    hide o3
                    show o4 with dissolve
                    o "I'd rather use my tongue to lick it off myself than have you push it deeper inside me!"
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
                    o "I can't believe you raped me... on the toilet..."
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
                    image o3 = Movie(play="/animations/o3.mp4")
                    image o4 = Movie(play="/animations/o4.mp4")
                    image o5 = Movie(play="/animations/o5.mp4")
                    image o6 = Movie(play="/animations/o6.mp4")
                    $ plugged2 = True

                "Leave":
                    "It's been a long day. I'll leave her alone and call it a day."
            $ daytime = 4
            $ daytimes = str(daytime)
            jump map
        "Never mind.":
            jump map
default vdildo = False
default vdildo2 = False
default plugged = False
default plugged2 = False
