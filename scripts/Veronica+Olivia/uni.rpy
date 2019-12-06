label map_alt:
    scene future with fade
    "{i}The environment changes; things seem back to normal.{/i}"
    jump map
default uni_intro = False
label uni:
    stop music fadeout 1
    call hidescreens from _call_hidescreens_17
    hide screen fastforward
    scene future
    "{i}The environment changes; there is something not right with this world...{/i}"
    call hidescreens from _call_hidescreens_15
    hide screen fastforward
    if uni_intro == False:
        $ uni_intro = True
        scene black
        play music "sounds/cinematic.mp3" fadeout 1
        scene o-1 with fade
        "Veronica suggested that I could see Olivia and see if she could help me out with my studies."
        scene o-2 with dissolve
        "But now that I'm seeing her again, she's hot, but damn does she look scary."
        "Alright, let's do this."
        scene o-3 with dissolve
        p "Excuse me, Olivia."
        o "Class is over. Got any questions? Ask them next time."
        scene o-4 with dissolve
        p "It's me, [p]. We met at the gym earlier?"
        scene o-5 with vpunch
        o "Oh, it's you. The idiot that doesn't even what sex he is."
        p "Listen, I didn't mean to use the woman's gym and I'm sorry."
        scene o-7 with dissolve
        o "What are you even doing here anyway? Can't you tell I don't like you?"
        p "..."
        p "I just need some help, please."
        p "I want to go to university again and get an education."
        o "That's good for you, [p]. But why do you think I care?"
        p "You're an educator, and I want to strive to better myself and learn new things."
        scene o-6 with dissolve
        o "Stupid men like you can't learn. What a pointless exercise."
        "Wow, what a bitch."
        scene o-8 with dissolve
        p "Are you sure about this?"
        o "You may leave now."
        p "..."
        scene o-9 with dissolve
        p "You don't help me, and you don't even point me in the right direction."
        p "You don't even care about education. I know why you're really here."
        scene o-10 with hpunch
        play music "sounds/path.mp3" fadeout 1
        p "You dropped this letter in the gym."
        scene o-11 with vpunch
        o "!!"
        p "You're just using university equipment to make drugs!"
        scene o-12
        o "Y-You can't prove that!"
        p "If I reported this, what do you think will happen?"
        p "They'll go through the inventory and you'll go to prison."
        p "And the people you make the drugs for, I'm sure they've got friends in prison too."
        p "If you piss them off, you're done for."
        scene o-13 with dissolve
        o "You, you!!"
        o "Argh!"
        scene o-14 with dissolve
        o "What do you want from me?"
        p "I just want to get into the program here. I want to make my parents proud."
        scene o-16 with dissolve
        o "Who do you think I am, [p]?"
        o "I can't get you into the program, idiot!"
        p "Why not?"
        o "You can come to the lectures, but that's it. Now leave."
        scene o-17
        p "Going to the lectures isn't going to get me that piece of paper at the end!"
        o "Sorry! Can't help you then. Off you go."
        "Grrr..."
        "I {i}will{/i} get something in return, Olivia."
        scene o-18 with dissolve
        o "What do you want, a handjob?"
        p "..."
        scene o-19 with hpunch
        o "Hah! You're not getting anything from me, you perverted thing. If that's what you're after you may as well turn around."
        o "All men like you are the same."
        scene o-20 with dissolve
        p "You talk big, Olivia, but I'm going to walk up to you now."
        p "And you're going to get on your knees."
        o "And why would I do that? Get away from me, you vermin!"
        o "Any closer and I'll scream!"
        p "And when they come I'll show them the letter. You'll be finished."
        p "This is a small price to pay, no?"
        scene o-21 with dissolve
        o "..!!"
        o "I HATE you. And one day, you will regret everything."
        scene o-22 with dissolve
        p "But not today. Go on, pleasure me."
        scene o-23 with dissolve
        o "(If he really does go to the authorities, I'll be in a lot of trouble!)"
        scene o-24 with dissolve
        o "(I'll just let it happen, and maybe he'll leave me afterwards.)"
        scene o-25 with dissolve
        "Speechlessly, she got on her knees."
        scene o-26 with dissolve
        "Shamefully, she looked down, yet maintained her defiant expression."
        p "Come on, Olivia. Make love to my penis."
        o "..."
        p "No? You asked for this."
        "Without warning, I grab a large tuft of her hair and pull it upwards."
        scene o-27 with vpunch
        o "Ahh!"
        p "One way or another, you will play ball."
        p "Now choke on it!"
        o "Noo!!"
        scene white
        image o1 = Movie(play="/animations/o1.webm")
        image o2 = Movie(play="/animations/o2.webm")
        show o1 with dissolve
        p "You're so much prettier when you're not talking Olivia."
        p "Your lips were made to be around a cock."
        o "Mm!!!"
        p "Lets take it up a notch, shall we? You can handle it."
        hide o1
        show o2 with dissolve
        o "Mm, mm, mm, mm..."
        p "You sound so much nicer making those kind of sounds."
        p "Now get on the fucking ground. I'm about to bust my load over you."
        hide o2
        scene o-28 with dissolve
        $ renpy.pause()
        scene o-29 with flash
        $ renpy.pause()
        scene o-30 with flash
        $ renpy.pause()
        scene o-31 with dissolve
        ## forced fellatio
        p "That wasn't so bad, was it?"
        scene o-32
        o "Fuck you. I hope you die in a fire!"
        play music "sounds/alchemy.mp3" fadeout 1
        p "I don't doubt for one moment you want me dead."
        p "I imagine you want me dead very much indeed, but unfortunately for you?"
        p "I have no intention of going anywhere, anytime soon."
        p "I own you now, Olivia."
        scene o-33 with dissolve
        o "You, fucking monster!"
        o "How can you live with yourself, when you can blackmail a woman and feel nothing?!"
        p "You know what I hate about people like you, Olivia?"
        scene o-34 with dissolve
        p "People like you act all high and mighty. You act so arrogant, like you're above us all."
        p "The only reason you're in this situation is because you're manufacturing drugs."
        p "You're no better than the scum-of-the-earth drug dealer."
        p "You make such addictive drugs, have you ever thought of the children who because of you, are now addicted?"
        p "Their lives ruined, relationships shattered..."
        p "Tell me, how do {i}you{/i} live with yourself?"
        o "..."
        p "Don't pretend you're anything more than a common whore."
        scene o-34 with dissolve
        o "It's different..."
        p "Spare me, whore. Veronica told me that you were once damaged by a male."
        p "Make no mistake, what you faced then will be nothing compared to what I will do to you."
        p "From now on, you call me Master, and your name is no longer Olivia. Your name is now, Slut."
        p "Do you understand, Slut?"
        scene o-36 with dissolve
        o "Go to hell."
        p "Still defiant? Even when I'm such a generous master?"
        p "Remember, I came to you for help and you pushed me away. Despite this, I am now offering you help."
        scene o-37 with hpunch
        o "How the fuck is this helping me?!"
        p "I'm saving you from yourself. You're a broken doll, Slut. You need me."
        p "Without my good will, you'll be arrested, and raped and beat to death in prison, if you even make it there."
        scene o-38 with dissolve
        p "Do you undestand now? You are my property."
        scene o-39 with dissolve
        o "{i}Sob, sob...{/i}"
        scene o-40 with dissolve
        p "I'll give you a night to mull it over. Your atittude had better change by tomorrow."
        scene black with fade
        scene future with flash
        play music "sounds/cyberpunk.mp3" fadeout 1
        x "Hello [p]."
        x "What a strong performance. A little out of character, don't you think?"
        p "Out of character?"
        p "It's power. Domination."
        x "You cannot deny your nature, true, and this is one of the most depraved timelines."
        x "But you will see, even in depravity there is redemption."
        x "After all, how can you rise, if you have not yet fallen?"
        x "Enjoy your time with her, [p] of this timeline."
        scene black with fade
        $ daytime = 4
        $ daytimes = str(daytime)
        $ olivialvl += 1
        call map_alt from _call_map_alt
    if olivialvl == 2:
        scene black
        play music "sounds/alchemy.mp3" fadeout 1
        scene o-41 with fade
        p "Afternoon, Slut."
        o "..."
        p "I said, afternoon, Slut!"
        scene o-42
        o "I do not answer to that name."
        p "You will, one day."
        p "What are the plans for you today?"
        scene o-41 with dissolve
        o "..."
        p "I asked you a question."
        o "..."
        scene o-43 with dissolve
        o "I'm a lecturer. I give classes."
        scene o-41
        p "Don't be so curt with me, Slut."
        p "Do not forget, I'm impulsive. If you make me angry, I might just report you and end your life."
        scene o-43 with dissolve
        o "...I understand."
        p "Master."
        o "Yes."
        p "Say it."
        scene o-44 with dissolve
        o "...Master."
        p "Say the full phrase."
        o "..."
        o "I understand... master."
        p "Well done, Slut. That wasn't so hard, was it?"
        scene o-45 with hpunch
        o "Fuck you."
        p "What was that?"
        scene o-46
        o "..."
        p "You can try preserve your dignity, but I wonder how long it will last."
        p "Tell me Slut, what do you teach?"
        scene o-45 with dissolve
        o "Chemistry."
        p "In front of many students?"
        o "Yes."
        p "Of course many students would come to class and stare at your body."
        p "You love the attention your body brings. It's why you go to the gym."
        scene o-41 with dissolve
        "I've got a few ideas of how to have fun with Olivia."
        "But first, I'll need to make sure I have some supplies."
        "I should check out the sex shop in the online shop on the computer."
        "I need a dildo at least."
        $ olivialvl += 1
        call map_alt from _call_map_alt_1
    if olivialvl == 3:
        scene black
        play music "sounds/alchemy.mp3" fadeout 1
        scene o-41 with fade
        p "Slut."
        o "Hmph."
        p "We'll see how long you can keep that attitude up for."
        jump trainer
    if olivialvl == 4:
        scene black
        play music "sounds/alchemy.mp3" fadeout 1
        scene o-41 with fade
        p "Good day, Slut."
        p "How are you liking me?"
        scene o-42 with hpunch
        o "To hell with you."
        p "I'm hurt. After all I've done? After I've treated you so well?"
        scene o-46 with dissolve
        o "..."
        p "Tell me, Slut. How do I compare?"
        p "Compared to the guy who apparently mistreated you before. How am I doing?"
        scene o-45 with dissolve
        o "I have no idea what you are talking about."
        p "Wasn't it the case that you had a boyfriend or someone who traumatised you?"
        o "A boyfriend? Men are digusting. What a stupid idea."
        p "Hang on, then who fucked you up in the past?"
        scene o-19 with dissolve
        o "Nobody! How many times do I have to tell you?"
        scene o-8 with dissolve
        p "..."
        p "No, this isn't how it works you stupid whore. You don't hide shit from me."
        scene o-10 with dissolve
        p "No matter, I'll ask again once your tongue is loosened up a bit more."
        scene o-12 with dissolve
        o "W-What are you going to do?"
        p "Relax. I'm a good master. I'll show you I'm better."
        p "In fact, I'm going to get you something nice as a reward, if you will."
        scene o-11 with dissolve
        o "A reward?"
        p "That got your curiosity, didn't it? You're getting used to how it's going to work."
        p "Good job, Slut."
        scene o-13 with dissolve
        o "..."
        p "That's right, a gift. Let me show you."
        "I need to make sure I buy the slutty outfit from the shop."
        $ olivialvl += 1
        call map_alt from _call_map_alt_2
    if olivialvl == 5:
        if so:
            label olivia_outfit:
                scene black
                play music "sounds/alchemy.mp3" fadeout 1
                scene o-121 with fade
                p "I'm back with your gift."
                p "It's what every slut loves. A slutty outfit."
                scene o-122 with dissolve
                o "What do you want from me?"
                p "Whoa. Show some appreciation, won't you?"
                p "This cost me a pretty penny. I invested money into this for you."
                p "I care about you."
                scene o-123 with dissolve
                o "Your gaslighting won't get to me."
                p "Think what you will, Slut, but one thing's for certain."
                p "You're going to wear my present to you. And you will love it."
                scene o-124 with dissolve
                o "This?"
                o "This barely covers anything. Do I like like a punk to you? Those years are behind me."
                o "What a gross outfit!"
                scene o-125 with hpunch
                p "Hey hey hey-"
                p "Is this the attitude you're going to have? Be a doll, won't you? Put this on."
                scene o-126 with dissolve
                o "The way you talk to me is creepy and disgusting. You make my skin crawl."
                p "Listen up, Slut."
                p "Either you put this on or I stretch your tight little anus with the dildos."
                p "It's your choice. I'm running out of patience."
                scene o-127 with dissolve
                o "..."
                o "I only have to wear this?"
                p "Of course. Have I ever lied to you?"
                scene o-128 with dissolve
                o "F-Fine!"
                o "Turn around!"
                scene o-129 with dissolve
                p "That's not how it works. You don't get to hide your body from me."
                scene o-130 with dissolve
                p "Strip. Now."
                scene o-131 with dissolve
                o "{i}Sob...{/i}"
                o "(I can't believe I'm getting humiliated again!)"
                o "(I'm so powerless against him!)"
                p "Understand?"
                scene o-132 with dissolve
                o "..yes."
                p "Call me master."
                scene o-133 with vpunch
                o "Cheh! I'm getting changed for you already, isn't that enough?!"
                p "Then talk less and strip more."
                scene o-134 with dissolve
                o "Hmph!"
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
                "Wow, what a strong and fit body."
                p "Hey, Slut."
                scene o-141 with dissolve
                p "Look at me with your pretty face."
                scene o-142 with dissolve
                o "..."
                p "Look me in the eyes."
                scene o-143 with dissolve
                p "You're so pretty with your mouth shut."
                p "Nice and vulnerable. This is where you belong."
                p "Now let me take those off."
                scene o-144 with dissolve
                o "..."
                scene o-145 with dissolve
                $ renpy.pause()
                scene o-146 with dissolve
                $ renpy.pause()
                scene o-147 with dissolve
                $ renpy.pause()
                "Jesus, what a well-maintained body."
                "That {i}will{/i} be mine one day, and I look forward to destroying it."
                scene o-148 with dissolve
                p "You've got a nice body, Slut."
                p "I'm going to bend you over one day and fill that ass with cock."
                scene o-149 with dissolve
                o "You're just a dirty rapist."
                p "Rapist? Oh I'm not going to rape you. Believe me, you're going to bend over willingly."
                p "Now shut up and put this on."
                scene o-150 with dissolve
                $ renpy.pause()
                scene o-151 with dissolve
                $ renpy.pause()
                scene o-152 with dissolve
                $ renpy.pause()
                scene o-153 with dissolve
                $ renpy.pause()
                scene o-154 with dissolve
                $ renpy.pause()
                # done
                o "Happy?"
                p "Very. You look great in that outfit, Slut. It suits you well."
                scene o-155 with dissolve
                $ renpy.pause()
                p "It doesn't cover too much, and shows off that body you worked so hard for."
                p "Tell me. Why do you work so hard at the gym if you didn't want people to stare at you?"
                o "..."
                scene o-156 with dissolve
                o "I don't do it for you, creep! It's not for your eyes."
                p "Oh hoho!"
                p "So you're working to impress someone else, are you?"
                p "Who are you trying to impress?"
                scene o-157 with hpunch
                o "I-"
                p "And here I thought you hated all men."
                scene o-158 with vpunch
                o "I do! I fucking hate you all. I will {i}never{/i} love or be friends with a male."
                p "What about the guy that mistreated you? He wasn't your boyfriend?"
                p "Or was it a random guy who just raped you?"
                scene o-159 with dissolve
                o "No such thing ever happened, how disgusting of you to repeat it."
                scene o-160 with dissolve
                p "Hmm, so if you're not trying to impress a man, are you possibly trying to impress..."
                p "...a woman?"
                scene o-161 with dissolve
                o "You bastard..."
                scene o-162 with dissolve
                p "Oh, thats fascinating. I didn't know you liked chicks, Slut!"
                p "I still have to wonder why you hate men so much, though. But, it's not something we have to worry about."
                p "I'm sure you'll come to love me over our time together!"
                o "Are you quite finished with your stupid monologue?"
                p "It's not wrong though, is it?"
                scene o-163 with dissolve
                o "I'm tired of playing dress up. Can I- I mean, I'm going now!"
                scene o-160 with dissolve
                p "Not so soon. Usually I'd have a dildo up your ass by now. We can't just end here."
                o "B-But you promised that it was either dress up or that!"
                p "Relax, your holes are safe for today. I just want to take a walk with you, talk about life."
                scene o-163 with dissolve
                o "A walk? With me dressed like this?"
                p "You already know it."
                o "What if people see me? That- that'll be-"
                p "Embarassing?"
                p "Whether you feel embarassed is up to you."
                p "How does this compare against losing your job, your reputation and possibly your life?"
                p "This is nothing. So don't make me ask twice. From now on you listen to my orders, understand?"
                scene o-164 with dissolve
                "She exhales deeply and there is a quiver at the end."
                scene o-165 with dissolve
                o "I... understand."
                p "Hahaha, gooood."
                scene black with fade
                "A few moments later."
                # outside
                play music "sounds/path.mp3" fadeout 1
                scene o-166 with fade
                o "Why did you take me here?"
                scene o-167 with dissolve
                p "I just wanted somewhere with people. A body like yours should be enjoyed and flaunted."
                scene o-168 with dissolve
                o "This is... embarassing."
                p "It's embarassing for me too, having a slut like you walking next to me."
                scene o-169 with dissolve
                p "You perverted looking thing. You look just like a cheap hooker on the street."
                scene o-170 with dissolve
                o "This is your fault!"
                p "Look where we are."
                scene o-171 with dissolve
                p "We're in the middle of the streets. You're in this situation now."
                p "I don't even want to be seen around you. Walk ahead of me."
                p "I don't want people to associate me with you."
                scene o-172 with dissolve
                o "I-I'm not that cheap looking, am I?"
                p "Shut up. Walk forward."
                scene o-173 with dissolve
                o "..."
                scene o-174 with dissolve
                "God, she looks the perfect amount of slutty."
                "She must be so uncomfortable right now."
                p "Just stand there for a bit."
                scene o-175 with dissolve
                o "H-Here?"
                p "Right there. And try it fit in."
                scene o-176 with dissolve
                o "How can I with this prostitute outfit!"
                scene o-177 with dissolve
                o "(Alright, Olivia, you have to calm down.)"
                o "(Try not to be self-conscious.)"
                scene o-178 with fade
                o "..."
                s3 "Honey, what do you think of that woman on the street there?"
                scene o-179 with hpunch
                s1 "That cheap looking slut? I hope you're not fancying her."
                s3 "People these days! Morals are like a thing of the past."
                scene o-180 with dissolve
                s1 "Don't give her attention, she's just begging for it."
                s1 "You might get STDs just from being too close."
                s3 "Don't worry! I won't be leaving you for such a skank."
                scene o-181 with hpunch
                o "I- I'm not a prostitute! It's just this outfit, I didn't choose to-"
                scene o-182 with hpunch
                s4 "Wow, ma'am, what a nice pair of tits you have!"
                s4 "How much for a blow job?"
                scene o-183 with dissolve
                o "I already said I'm not a whore!"
                s4 "Stuck up bitch playing hard to get. You're not as hot as you think, bitch."
                scene o-184 with dissolve
                s4 "Keep up this shit and someone will be bound to rape your sorry ass."
                scene o-185 with dissolve
                o "I-I...!"
                scene o-186 with hpunch
                s2 "Your behaviour here is very inappropriate!"
                scene o-187 with dissolve
                o "I-I know, this isn't what I-"
                s2 "Didn't you know? The feminist movement these days are about empowering women, and your whorish attire demeans and objectifies women."
                s2 "I just want you to know that not all of us are like you. You're alone."
                scene o-188 with fade
                o "(Why are people... so cruel to me?)"
                scene o-190 with dissolve
                o "(Is this who I am...? Do I... deserve this?)"
                scene o-191 with dissolve
                p "What an eye-opening experience."
                p "I think that took you down a few notches, Slut."
                p "Do you see now? You have no right to act so haughty."
                scene o-192 with dissolve
                o "No, it's all your fault!"
                scene o-193 with dissolve
                o "You made me into this!"
                p "Give me a break, haha!"
                scene o-194 with dissolve
                p "You know, I think you liked it. I think you're a sick exhibitionist."
                p "Was it an arousing experience for you?"
                scene o-195 with dissolve
                o "My body is for one person, and one person only. Not you, not them."
                o "You might be able to blackmail me now, [p], but I swear, I hate every bit of it."
                p "Well, let's see if we can change that."
                p "You're probably thinking to yourself: how can I get out of this situation?"
                p "Give it up, Slut. You're just a pair of tits in the end. You're not that smart."
                scene o-196 with dissolve
                o "We'll see."
                p "Oh we will. But I guarantee you. You'll learn to accept it and love me, or lose your job, your posessions, and maybe even your life."
                p "You're not that smart, but this should be a no-brainer."
                scene o-197 with dissolve
                o "..."
                p "Staying quiet? Good. A slut is prettiest with their mouth shut."
                scene o-198 with dissolve
                p "You've done well today and you may go home now."
                $ olivialvl += 1
                scene black with fade
                $ daytime = 4
                $ daytimes = str(daytime)
                call map_alt from _call_map_alt_3
        else:
            scene black
            scene o-41 with fade
            "I need to buy the slutty outfit from the shop first."
            call map_alt from _call_map_alt_4
    if olivialvl == 6:
        play music "sounds/cinematic.mp3" fadeout 1
        scene o-41 with fade
        p "Sup Slut."
        o "Hmph."
        p "How's my favourite exhibitionist doing?"
        scene o-41 with dissolve
        o "You will never have my dignity."
        p "I'd argue otherwise. But good news today, bitch."
        p "No public stuff. Today you're putting on a private show just for me."
        p "Do you know how to dance?"
        scene o-45 with dissolve
        o "..."
        p "No? No worries. All you have to do is follow my direction."
        p "I hope you know how to follow instructions."
        scene o-44 with dissolve
        o "I've done well so far, haven't I? What do you plan to do?"
        p "That's for you to find out. But first, I need to make sure I have a camera, ahahah!"
        scene o-42 with dissolve
        o "You..."
        scene black with fade
        "I need to make sure I have a camera with some kits lens."
        $ olivialvl += 1
        call map_alt from _call_map_alt_5
    if olivialvl == 7:
        if DSLR:
            play music "sounds/cinematic.mp3" fadeout 1
            scene o199 with fade
            p "I'm back slut. Now listen up."
            p "Stand up straight and put your hands behind your head."
            scene o200 with dissolve
            o "What are you going to do with that camera?!"
            p "What do you think? I'm going to blackmail you with the pictures later."
            scene o201 with dissolve
            o "You promised that if I did as you said, you wouldn't expose me!"
            p "That's right. If you're going to do as I say, you don't need to be afraid right?"
            p "Unless you want me to go and-"
            scene o202 with hpunch
            o "Fine!"
            scene o203 with dissolve
            o "Sigh."
            p "Good. This is how it works around here."
            play music "sounds/brite.mp3" fadeout 1
            scene o204 with fade
            p "Beautiful. You're so beautiful when you look so defiant, you know?"
            scene o204 with flash
            $ renpy.pause()
            scene o205 with dissolve
            $ renpy.pause()
            scene o205 with flash
            $ renpy.pause()
            p "Now spread your legs a bit. And pull up your dress."
            scene o206 with dissolve
            o "..."
            scene o207 with dissolve
            $ renpy.pause()
            scene o207 with flash
            $ renpy.pause()
            scene o208 with dissolve
            $ renpy.pause()
            scene o208 with flash
            $ renpy.pause()
            p "Wow, such lewd shots. You're following these instructions so well. Have you made adult videos before?"
            scene o209 with dissolve
            o "No. Of course not."
            p "Well you seem to know exactly what to do."
            o "I don't know about the women you typically associate myself with, but I'm competent."
            scene o210 with dissolve
            p "Good. Now take off your top."
            scene o211 with dissolve
            $ renpy.pause()
            scene o212 with dissolve
            $ renpy.pause()
            scene o212 with flash
            $ renpy.pause()
            p "And now that skirt."
            scene o213 with dissolve
            $ renpy.pause()
            scene o214 with dissolve
            $ renpy.pause()
            scene o214 with flash
            $ renpy.pause()
            p "Make a sexy pose for me."
            scene o215 with dissolve
            o "What do you want."
            p "You should know by now. Something sexy."
            scene o216 with dissolve
            o "..."
            scene o216 with flash
            $ renpy.pause()
            scene o216 with flash
            $ renpy.pause()
            p "Come on now, snap snap."
            p "I have to wonder. Has anyone else seen you like this before?"
            p "Am I... the first? Ahahaha!"
            scene o215 with dissolve
            o "You're just making me strip off more and more and give you a strip tease. Let's just get this over with."
            o "Let's stop this play."
            p "Whoa, aren't you eager."
            p "Alright, turn around. Let's get a look."
            o "Hmph."
            scene o217 with dissolve
            $ renpy.pause()
            p "Now get dressed."
            scene o218 with hpunch
            o "What? You're not going to get me to strip?"
            p "You think you're that pretty? You think men can't resist you? Don't get cocky now."
            scene o219 with dissolve
            o "No, I-!"
            p "Don't forget your place, slut. You're just a piece of meat."
            scene o220 with dissolve
            o "I... what is your goal?"
            p "I don't know. I'm just not feeling it. You'll need to learn to present yourself better."
            p "Tell you what. Pick out a piece of lingerie tomorrow and bring it here. Until then."
            scene o221 with dissolve
            o "What if I don't have it?"
            p "A slut like you has lingerie for sure, don't lie to me."
            o "..."
            scene o222 with dissolve
            p "Look at you, I bet you look at yourself in the mirror in your lingerie, thinking you're hot."
            p "Let's put that to the test, shall we?"
            p "I'll see you tomorrow."
            $ daytime = 4
            $ daytimes = str(daytime)
            $ olivialvl += 1
            call map_alt from _call_map_alt_6
        else:
            scene black with fade
            "I need to buy a camera first!"
            call map_alt from _call_map_alt_7
    if olivialvl == 8:
        play music "sounds/cinematic.mp3" fadeout 1
        scene o200 with fade
        p "Well, slut? Did you bring it?"
        o "Yes. I brought the lingerie."
        p "Well what are you waiting for? Put it on!"
        scene o203 with dissolve
        o "T-turn around."
        p "I don't think so."
        scene o-132 with dissolve
        o "Sigh."
        # strip
        play music "sounds/alchemy.mp3" fadeout 1
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
        scene o-121 with dissolve
        p "Well, well, well."
        scene o223 with dissolve
        p "Is red your favourite colour?"
        scene o224 with dissolve
        p "Truly the colour of a prostitute."
        o "No one has seen me like this before."
        scene o225 with dissolve
        o "Are you happy?"
        p "Thanks for your concern, slut, but I'm not satisfied just yet."
        p "Dance for me."
        scene o226 with dissolve
        o "I. Don't. Know How."
        p "Really? Looks like you've got some homework to do."
        p "Just move sexy. Go."
        scene o227 with dissolve
        o "But I..."
        scene o228 with dissolve
        o "Alright."
        # move
        scene o229 with dissolve
        $ renpy.pause()
        scene o230 with dissolve
        $ renpy.pause()
        scene o-125 with hpunch
        p "What the fuck are you doing?"
        p "I'm not even going to take pictures of that."
        p "Do you know how disgusting that dance was?"
        scene o231 with vpunch
        o "I'm sorry, I said I didn't know how!"
        p "Enough."
        scene o232 with dissolve
        p "I'll come back tomorrow."
        p "By then, you better have a sexy dance for me."
        p "Tell me, how are you going to prepare?"
        scene o233 with dissolve
        o "I... suppose I'll practise at home."
        p "Tell me your learning plan."
        p "I don't want you fucking up tomorrow as much as you have done today."
        scene o234 with dissolve
        o "..."
        o "I'll watch some videos... and practise in front of the mirror."
        p "Videos? What videos?"
        scene o235 with dissolve
        o "Videos of... strippers."
        p "You're going to look up videos of strippers and pretend to be one yourself?"
        scene o236 with dissolve
        o "Well, to see how they do it. How else am I supposed to learn how to dance like a whore?"
        scene o237 with dissolve
        p "Good. I want you dancing like a whore tomorrow."
        p "Don't disappoint me..."
        $ olivialvl += 1
        $ daytime = 4
        $ daytimes = str(daytime)
        call map_alt from _call_map_alt_8
    if olivialvl == 9:
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
        call daykeep from _call_daykeep_31
        $ olivialvl += 1
        call map_alt from _call_map_alt_9
    if olivialvl == 10:
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
        $ daytime = 4
        $ daytimes = str(daytime)
        $ olivialvl += 1
        call map_alt from _call_map_alt_10
    if olivialvl == 11:
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
        p "I'll even make you a promise. Since apparently you hate men, I'll lay off on violating you."
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
        scene splash7 with fade
        $ renpy.pause()
        $ daytime = 4
        $ daytimes = str(daytime)
        $ olivialvl += 1
        call map_alt from _call_map_alt_11
    if olivialvl == 12:
        jump trainer
