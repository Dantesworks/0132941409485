default gym_intro = False
default veronicalvl = 1
default olivialvl = 1
label gym:
    scene future
    stop music fadeout 1
    "{i}The environment changes; there is something not right with this world...{/i}"
    if gym_intro == False:
        $ gym_intro = True
        play music "sounds/cinematic.mp3" fadeout 1
        "Man this gym is hard to find."
        "Trying to get there is a workout in and of itself!"
        "Hang on... I think this is it."
        scene splash6 with fade
        d "You are about to enjoy content with commissioned side characters with very depraved themes, including blackmail and corruption."
        d "This story occurs in an alternate timeline, so proceed at your own risk!"
        scene future with fade
        x "Your name is [p], and you are but one [p] of many timelines I am watching over."
        x "It is my hope that this story will yield something interesting."
        scene r-1 with fade
        "Huh. It's smaller than I expected."
        "It's empty right now, but it wouldn't be able to hold that many people."
        scene r-2
        "Maybe there's another gym somewhere? This can't be it."
        scene r-3 with dissolve
        "Whatever, let's start the workout before people swarm the equipment."
        scene r-4 with dissolve
        "Hmm, I hear people approaching. Fuck I knew I wasn't going to get that lucky."
        s1 "Urgh, I feel so tired already. I'll be barely able to exercise."
        s2 "Oh, come on Olivia, gym is a place for you to reclaim your energy!"
        s1 "Okay, quick routine, but I need to head off after, Veronica."
        s1 "Alright, what should we get started on today?"
        scene r-6 with dissolve
        stop music fadeout 1
        s2 "How about we get started with some cardio first? And then maybe-"
        scene r-5 with hpunch
        play music "sounds/path.mp3"
        s1 "Hold on, Veronica. I think we've got an uninvited guest here."
        scene r-7
        p "Uninvited? Sorry, what?"
        scene r-8 with hpunch
        s1 "What are you even doing here?"
        s1 "Don't you know your place?"
        scene r-9
        p "Whoa, hang on lady, what are you talking about?"
        p "I'm just trying to lift some weights."
        s1 "Who do you think you are, the boss of this gym?"
        scene r-10
        s2 "Hey, Olivia, wait. I don't think he understands."
        "Hang on, this woman looks familiar..."
        scene r-11 with dissolve
        play music "sounds/wistful.mp3" fadeout 1
        p "Miss... Veronica?"
        scene r-12 with hpunch
        s2 "..."
        scene r-13 with dissolve
        s2 "[p]?"
        scene r-14 with dissolve
        s1 "You know this guy?"
        scene r-15 with dissolve
        s2 "He used to be one of my students!"
        s2 "[p], it's been a while, how are you doing now!"
        scene r-16 with dissolve
        s2 "Oh, and it's {i}Mrs{/i} Veronica now."
        p "Whoa, congratulations- and yes, it has been a while."
        "Damn, I had such a huge crush on her back in school..."
        scene r-17 with dissolve
        ver "This is my friend, Olivia. She's a lecturer at the local university."
        scene r-18 with hpunch
        o "This is a woman's gym, didn't you know?"
        "Oooooooh. So that's why it's so small. It's not the main gym."
        p "I... did not know that. My bad."
        ver "Let him stay, Olivia. There are plenty of machines here to go around!"
        scene r-19 with dissolve
        o "Why are you here anyway, [p]? Are you not a man?"
        o "Are you dickless?"
        p "I already said I didn't know it was a woman's gym. I'm sorry!"
        "Christ! What a bitch!"
        scene r-20 with dissolve
        ver "Olivia!"
        scene r-21 with dissolve
        ver "Sorry, [p]."
        o "I've wasted enough time already. I'm starting my workout."
        scene r-22 with dissolve
        o "Feel free to keep your friend happy Veronica, I need to finish this workout quick and head off."
        ver "Alright, give me a call later."
        scene r-23 with dissolve
        p "Miss- I mean, Mrs Veronica. Are you still teaching?"
        ver "Just call me Veronica, [p]. And yes, I'm still teaching. I love the profession."
        ver "What have you been up to since high school?"
        ver "I heard you left town for another university - you must be very successful!"
        ver "Have you graduated? Is that why you're back?"
        scene r-24 with dissolve
        p "..."
        p "I guess I'm just taking a break from university. I missed the folks back home, so just thought I'd take a trip back home."
        ver "When will you be going back?"
        p "Haha... It's sort of a permanent break."
        scene r-25 with dissolve
        ver "I see."
        ver "Well, like I said, Olivia is a local teacher at the university here. She teaches chemistry. Maybe something to consider?"
        p "You were always the best teacher back in highschool, Mrs. Veronica. Thanks for looking out for me. But somehow, I don't think Olivia's too fond of me."
        scene r-26 with dissolve
        ver "Oh, don't mind her today. She just had a tough day."
        p "Yeah?"
        ver "Let me say sorry on her behalf. She's a very busy and very strict woman. I think she's dealing with a lot from the university side of things."
        ver "All of that has made her quite short."
        scene r-28 with dissolve
        p "Ah that's alright. I didn't take it too personally. It's my fault anyway; I shouldn't have gone into the wrong gym."
        ver "No, no, [p], don't worry about that at all. To be honest, nobody comes here anyway, and like I said, there's plenty of machines to go around."
        ver "Think of it more as a private gym for us, than a woman's gym per se."
        p "Awesome! I'll pop in from time to time then, haha."
        scene r-29 with dissolve
        p "Tell me something about yourself Mrs. Veronica."
        p "What's been going on?"
        scene r-27 with dissolve
        ver "Just call me Veronica, you're not my student anymore!"
        p "Haha alright."
        ver "I teach at the same highschool, and I met a wonderful man and got married!"
        p "How'd you meet this guy?"
        scene r-25 with dissolve
        ver "Oh, he's a travelling businessman, and we met each other at the bar."
        p "Romantic!"
        ver "It was very exciting!"
        p "Are you guys, you know, settling down? Starting a family?"
        scene r-30 with dissolve
        ver "Oh no, not yet. He's very busy, you see and away for a lot of the time."
        ver "He says that once his job is more stable, he can finally settle down and we can think more about the future."
        p "Well, that sounds like a plan."
        scene r-31 with dissolve
        ver "So, what are you working out today?"
        p "It's been a while since I've been back at the gym..."
        p "A little, then straight to bench press."
        p "And you?"
        ver "Cardio for me. A few minutes on the treadmill? I never felt too comfortable around the weights. Maybe in return for staying at the woman's gym you can teach us the bench press technique?"
        p "Sure thing, would be my pleasure."
        p "What were you guys doing before you came to the gym?"
        scene r-27 with dissolve
        ver "Olivia and I love coming to the resort."
        ver "Usually, we walk to the resort and do a few exercises at the gym. Afterwards, we go to the sauna for a steam bath. We shower and then grab some tea at the resort. I love the routine."
        p "That actually sounds great. I'd love to say hi if I see you guys around in the future."
        "Maybe just Veronica, not Olivia."
        scene r-32 with hpunch
        o "I don't know about that."
        scene r-33 with dissolve
        o "I'm done, Veronica. Sorry, I'll have to skip out on you now, I've got something I need to attend to."
        ver "Oh don't worry about it, I'll see you next time. Take care okay?"
        scene r-34 with dissolve
        "Olivia seems so brash and rude."
        "How is she such great friends with Veronica? Veronica is so nice."
        ver "She {i}is{/i} a bit short today."
        p "What's going on with her?"
        ver "I'm not too sure. She said something about having to meet the quota. It's something to do with chemistry and her work, no doubt."
        ver "I still think you should consider approaching her one day and see if she could help you out with university related things. Just... another day, not today."
        p "Haha, we'll have to see about that. Thanks."
        scene r-35 with dissolve
        ver "Well, I'm going to do some cardio, then head off."
        p "Going to the sauna later?"
        ver "Maybe not today since Olivia's not coming."
        p "Fair enough. Talk to you later."
        scene r-36
        "Damn, Veronica's still got it."
        "A lot of dudes from my class crushed on her, not just me."
        "Sad to see that she's found someone now and our fantasies will always be unfulfilled."
        "Or will they?"
        "Damn."
        "She must come to the gym a lot to stay in such great shape."
        scene r-37 with dissolve
        "Okay, time to lift some heavy weights."
        "They say a man's strength increases two folds when a woman is watching."
        "Let's put that to the test."
        p "HURRR!!!"
        scene r-37 with flash
        "Ah fuck! It's too heavy!"
        p "Hey, help! Help!"
        scene r-39 with fade
        ver "Oh my god! Are you alright?"
        scene r-38 with dissolve
        p "I am now. Guess I got a little bit carried away..."
        "How embarassing!"
        scene r-40
        ver "Are you sure? You should take a break. Are you hurt anywhere?"
        scene r-41 with dissolve
        p "I'm fine, thanks to you."
        scene r-42
        ver "Maybe I should stay with you for a while. Just to make sure."
        p "You don't have any thing else to do later?"
        scene r-43 with dissolve
        ver "I was going to spend some time with Olivia, but she's gone so I have a free schedule. Don't worry about it."
        ver "I've finished with my workout. Let me do a quick shower, then I'll meet you back at the reception resort, alright?"
        p "Thanks, I'll meet you there."
        scene r-44 with dissolve
        ver "Don't work too hard, [p]!"
        scene r-45 with dissolve
        "Did I just inadvertently score a date with my old teacher?"
        "Well done, [p]."
        "What a twist of fate, huh?"
        scene r-46 with dissolve
        "I better hurry up and not keep her waiting."
        "Hmm... looks like someone left something behind... a note?"
        ## Hey bitch....
        scene letter with flash
        play music "sounds/path.mp3" fadeout 1
        $ renpy.pause()
        "My god. Dantenol? Isn't that the new drug on the streets these days?"
        "And university lecturer... was this someone's note to Olivia?"
        scene r-47
        "What has she gotten herself into? This might be useful for me to know one day."
        "I'll have to think more about this later."
        scene black with fade
        play music "sounds/slopes.mp3" fadeout 1
        "..."
        "I hope I haven't taken too long..."
        ver "[p]!"
        scene r-48:
            pos (0.0, -3.29)
            linear 6 pos (0.0, 0.0)
        $ renpy.pause(6.0,hard=True)
        $ renpy.pause ()
        scene r-49
        p "Mrs Veronica, it's so good to see you."
        ver "Please, [p], I'm not your teacher anymore, just call me Veronica!"
        p "Alright, I'll try, but old habits die hard haha."
        p "So err, are you going somewhere for lunch?"
        ver "Ah... I've already had something to eat, and besides..."
        scene r-50 with dissolve
        ver "I {i}am{/i} trying to lose weight, after all..."
        p "You? Lose weight? You're in great shape!"
        scene r-53 with dissolve
        ver "Well, my husband tells me I'm a little thick around the edges."
        p "Oh come on."
        scene r-51 with dissolve
        ver "It's good to be fit anyway."
        p "In that case, how about a few drinks then?"
        p "They say red wine makes you more youthful and beautiful."
        scene r-52 with dissolve
        ver "At the bar? It's closed at this time of the day."
        p "Oh, where else can we get some drinks?"
        scene r-49 with dissolve
        ver "I know a place, it's lesser known but I like casual tone. It'll give us more privacy too."
        p "Alright then, show me!"
        scene black with fade
        play music "sounds/wisteria.mp3" fadeout 1
        scene r-54 with fade
        ver "It's an industrial look, [p]."
        ver "I love coming sometimes after a physical day to just sip wine in a classy and discrete place."
        scene r-55 with dissolve
        wai "Welcome to the Loft."
        scene r-56 with dissolve
        wai "Good to see you again, Veronica."
        scene r-57 with dissolve
        wai "I see you've finally brought a man like you said you-"
        ver "Hold on! ...ahahah..."
        scene r-58 with dissolve
        ver "This is [p], one of my former students."
        wai "So a student no longer?"
        scene r-59 with dissolve
        ver "Ahh, just two glasses of red please."
        scene r-60 with dissolve
        wai "I'm sorry Veronica. Good luck."
        scene r-61 with dissolve
        wai "Here, two reds."
        scene r-62
        "What a strange conversation."
        "I thought Veronica said she was married."
        wai "Please enjoy."
        scene r-63 with fade
        p "She knows you. You must come here very often!"
        ver "I'm quite a drinker."
        scene r-64 with dissolve
        ver "You can tell by how quickly I'm downing this alcohol."
        scene r-65 with dissolve
        ver "..."
        scene r-66 with dissolve
        ver "I love red."
        p "So uh, Olivia."
        p "What's up with her?"
        scene r-67 with dissolve
        ver "She's a good friend of mine, but she has her flaws."
        p "She didn't like me very much."
        scene r-68 with dissolve
        ver "She used to be treated poorly by a man she used to see."
        ver "Now she hates all men."
        p "Wow. What's that like?"
        scene r-69 with dissolve
        ver "He was a horrible, vile, disgusting man. He cheated on my best friend and that's why she's the way she is now."
        scene r-70 with dissolve
        ver "People like that are really the worst, and, and..."
        scene r-71 with dissolve
        ver "..."
        p "Is that similar to what you're going through right now?"
        p "Is your husband... like this too?"
        ver "..."
        scene r-72 with dissolve
        ver "My husband is perfect, I love him. The problem isn't him... it's me."
        scene r-73 with dissolve
        play music "sounds/alchemy.mp3" fadeout 1
        ver "I just... don't feel as attracted to him as I used to..."
        ver "It's like the sparks have died off."
        ver "It's horrible, and all that, but... my feelings for him are gone."
        ver "It's dull in the bedroom, I have to pretend I enjoy it, and I can't believe it but I'm..."
        scene r-74 with dissolve
        ver "I'm looking for other people."
        p "Have you found someone else yet?"
        ver "No, I can't bring myself to."
        p "Thanks for telling me all this, Veronica."
        p "I want to tell you something too."
        p "For the longest time in high school, I had a huge crush on you."
        scene r-75 with dissolve
        ver "Ha, [p]. I appreciate it, but you're my student and I'm your teacher. It wouldn't be right."
        p "I'm not your student any more, Veronica. I'm an adult now. Just like you."
        scene r-76 with dissolve
        ver "..."
        scene r-77 with dissolve
        p "But some things don't change. I still have a huge crush on you, and I think I came into your life again at the right time."
        p "This was meant to be."
        scene r-78 with dissolve
        ver "Are you suggesting...?"
        p "I'm suggesting that we shouldn't deny ourselves."
        scene r-79 with dissolve
        ver "But my husband, god! How can I look him the eye if I've been seeing someone behind his back?"
        p "He doesn't need to know, Veronica. You can have the best of both worlds."
        p "All you have to do, is try it out with me, and you'll feel better. I promise."
        p "We can start slow."
        scene r-80 with dissolve
        ver "... what do you want me to do?"
        p "I've got a lot of things in mind, but the waitress is in the way."
        scene r-81 with dissolve
        ver "Don't worry about her. She... understands my situation."
        scene r-82 with dissolve
        ver "Sorry, Cara, could you give me and [p] a moment please?"
        wai "..."
        scene r-83 with dissolve
        wai "If you like."
        scene r-84 with dissolve
        $ renpy.pause()
        scene r-85 with dissolve
        p "It's just us two now, Miss Veronica."
        scene r-86 with dissolve
        ver "You can call me Veronica."
        p "I know, but I like calling you Miss Veronica, not Mrs Veronica."
        scene r-87 with dissolve
        p "You're my teacher from all the way back then, and while we're together, you're my Miss Veronica."
        p "Forget about him."
        scene r-90 with dissolve
        p "You just need to give it a go. Just the tip. And you'll never look back."
        ver "[p], I..."
        scene r-89 with dissolve
        p "Just the tip. Have a taste, Miss V."
        # looks around, cara around corner
        scene r-91 with dissolve
        $ renpy.pause()
        scene r-92 with dissolve
        $ renpy.pause()
        scene r-94 with dissolve
        ver "O-Okay."
        scene r-93 with dissolve
        ver "This is just a one off thing, alright? Just to see what it's like."
        p "Of course."
        scene r-95 with fade
        p "Don't be nervous, Miss Veronica. You're very beautiful."
        ver "(His penis is so much bigger than my husband's!)"
        ver "(Is this what it's like to feel lust after such a long time?)"
        scene white
        image ver1 = Movie(play="/animations/ver1.webm")
        image ver2 = Movie(play="/animations/ver2.webm")
        show ver1 with dissolve
        "The timid and uncertain way she licked the tip of my cock was strangely hot."
        "Despite her only licking such a small area, I could tell there was a dark longing there."
        "I was enjoying myself."
        ver "Lick, lick, lick, lick..."
        p "How are you liking it?"
        ver "Sorry I'm a bit awkward."
        p "You'll ease into it. Why don't you go faster?"
        ver "I'll try that."
        hide ver1
        show ver2 with dissolve
        "She picked up her speed, flicking my cock up with every stroke of her tongue on the underside of my penis."
        "The area where she licked became hot and wet with as she moisturised it with her saliva."
        "It would become cool as the air rushed around it only to become warm again after her tongue swept in again."
        ver "(Am I... enjoying this?)"
        p "You're so good at this, I'm about to-!"
        scene r-96 with dissolve
        $ renpy.pause()
        scene r-97 with flash
        $ renpy.pause()
        scene r-98 with flash
        $ renpy.pause()
        scene r-99 with dissolve
        p "That was fun, wasn't it?"
        scene r-99 with dissolve
        ver "[p]."
        ver "I feel really guilty. How could I have done this..?"
        scene r-100 with dissolve
        ver "My loyal husband... waiting for me at home..."
        scene r-102 with dissolve
        ver "I won't be able to face him anymore!"
        "Ah shit."
        scene r-104 with dissolve
        ver "I was just trying this, this wasn't serious, right [p]?"
        ver "I'm a good wife, right [p]?"
        scene r-103 with dissolve
        ver "...right?!"
        p "..."
        scene r-105 with dissolve
        ver "I-I'm going to forget this. This isn't me."
        scene r-106 with dissolve
        p "I'll be here for you, Veronica."
        ver "I... need to go now."
        p "Very well."
        scene r-107 with dissolve
        "That was fucking hot. A bit rocky, sure."
        "She'll come around. After all..."
        scene r-108 with dissolve
        "...her depravity is plain for all to see."
        $ veronicalvl += 1
        $ daytime = 4
        $ daytimes = str(daytime)
        call map_alt from _call_map_alt_12
    if veronicalvl == 2:
        play music "sounds/cinematic.mp3" fadeout 1
        scene r-109 with fade
        "Looks like I managed to catch Veronica at the gym today."
        scene r-110 with dissolve
        "My god, look at how fat that ass is. That gym is definitely not going to waste."
        p "Hello, Miss Veronica. Good to see you."
        scene r-111 with dissolve
        ver "Is it... [p]?"
        scene r-112 with dissolve
        ver "Oh, hey [p]..."
        p "How are you doing?"
        scene r-113 with dissolve
        ver "Oh I'm going good."
        p "Did you think much about the other day?"
        scene r-114 with dissolve
        ver "..."
        scene r-115 with dissolve
        ver "[p]..."
        scene r-116 with dissolve
        p "I don't want it to be awkward between us, but I just wanna say, I enjoyed it."
        p "And I think really, you liked it too."
        scene r-117 with dissolve
        ver "I'm a married woman, [p], and I have a loving husband at home."
        p "You said yourself, he's barely at home, he's travelling all the time and you're by yourself."
        p "I'm not asking you to leave, but you should be allowed to have some fun."
        ver "I..."
        scene r-118 with dissolve
        ver "Sorry. but I have to go now."
        ver "I've got some study material to pick up at the school."
        scene r-119 with dissolve
        p "Going already?"
        scene r-120 with dissolve
        ver "I've finished my workout."
        scene r-121 with dissolve
        ver "..."
        scene r-122 with dissolve
        ver "Goodbye."
        scene r-123 with dissolve
        "So Miss Veronica's going back to school, huh?"
        scene black with fade
        "I haven't been back in a while but I should go there after my work out and catch her in the classroom."
        stop music fadeout 1
        # transition
        "After the gym session..."
        play music "sounds/alchemy.mp3" fadeout 1
        scene r-124 with fade
        "She's right there, just like I remember her when I was back in high school."
        "All that time I had a crush on her. Now that I have a chance to get close to her, and convince her to try it out with me, I'm not going to give it up."
        scene r-125 with dissolve
        "I remember those countless afternoons popping boners in the classroom. And they were all because of you, Miss Veronica."
        "I've gotten you to suck me off already. I want to take this much further."
        play music "sounds/time.mp3" fadeout 1
        scene r-126 with dissolve
        p "Hey!"
        scene r-127 with dissolve
        ver "W-what?"
        scene r-128 with hpunch
        ver "[p]?! What are you doing here?"
        p "I used to come to this school, you know?"
        ver "Yes, I know, I was your teacher."
        p "Yeah, you {i}were{/i}."
        scene r-129 with dissolve
        p "It wasn't so long ago that I would be standing right here, and you would walk past me, Miss Veronica."
        ver "You can just call me Veronica."
        p "I know, but you know why I don't."
        scene r-130 with dissolve
        p "You're that sexy teacher, and to me you'll always be Miss Veronica."
        scene r-131 with dissolve
        p "You've got something I want. I've got something you need."
        scene r-132 with vpunch
        ver "[p]! Stop!"
        scene r-133 with dissolve
        ver "What we did that day - I regret it. It's not your fault-"
        ver "I was selfish. I was only thinking about myself and my pleasures, and what I was missing out on."
        ver "I wasn't thinking about my husband."
        p "The boys loved you in high school, Miss Veronica. It wasn't just because of your looks."
        scene r-134 with dissolve
        p "You are a caring woman who really looked after her students, and saw to their needs."
        p "But it's time to think about your own needs, Miss."
        ver "..."
        p "At the very least, let me do for you what you did for me."
        scene r-135 with dissolve
        ver "[p], I..."
        scene r-136 with dissolve
        p "School's over, Miss. It's just us two now."
        p "Be selfish just a little longer. And at the same time, do it for me."
        p "It's the right thing to do."
        scene r-137 with dissolve
        ver "(What would be the harm of giving in just a little?)"
        ver "(It-it's not like my husband will ever find out...)"
        ver "..."
        scene r-138 with dissolve
        ver "What do you want me to do?"
        p "Nothing, Miss Veronica. I'll do the work this time."
        stop music fadeout 1
        p "Just lean back, and... close your eyes."
        p "Just... give in."
        scene r-139 with fade
        # transition
        ver "[p], I... [p]-"
        p "Shh, just close your eyes. Let me do the work."
        play music "sounds/alchemy.mp3" fadeout 1
        scene r-140 with dissolve
        "She closed her eyes, but winced ever so slightly as I begin to undress her."
        scene r-141 with dissolve
        ver "[p], you're-"
        p "Just a little bit, Miss Veronica. Just enough for me to see your folds."
        "She acquiesces, as I peel off layer after layer."
        "Beneath that exterior, she wanted this very much."
        scene r-142 with dissolve
        $ renpy.pause()
        scene r-143 with dissolve
        $ renpy.pause()
        scene r-144 with hpunch
        ver "[p]~!"
        p "Don't worry, I'm just getting a good look at your pleasure parts."
        scene r-145 with dissolve
        "I got down onto my knees, and put my face close enough to smell the musk of a moist pussy."
        "Miss Veronica did nothing but look at me with her mouth agape."
        p "I'm just returning the favour."
        scene r-146 with dissolve
        ver "O-okay, but do it slowly okay?"
        p "Of course."
        scene r-147 with dissolve
        "She winced as my tongue tasted her moist vagina."
        "Was she reacting to the sensation of my tongue? Or her shame of how wet she was?"
        image ver3 = Movie(play="/animations/ver3.webm")
        scene ver3 with dissolve
        $ renpy.pause()
        "She kept her eyes shut as I licked her pussy over and over again."
        "From the cool dryness of her external folds to the sweet nectar within."
        "She trembled everytime I pushed my tongue deeper, to see how far it could go."
        image ver4 = Movie(play="/animations/ver4.webm")
        scene ver4 with dissolve
        $ renpy.pause()
        ver "Ah~ ah~ ah~ ah~"
        "She panted heavily but it was as though she was in pain."
        "Fighting between sin and pleasure. Her mind at war."
        p "Relax, Miss Veronica, just enjoy the fun."
        p "You've got such a beautiful and smoking hot body."
        p "Let yourself be attacked and consumed by the pleasure."
        image ver5 = Movie(play="/animations/ver5.webm")
        scene ver5 with dissolve
        $ renpy.pause()
        "Her eyes finally opened."
        ver "I.. I'm not used to this feeling, [p]."
        ver "I feel... tingling... from down there, throughout my whole body."
        image ver6 = Movie(play="/animations/ver6.webm")
        scene ver6 with dissolve
        $ renpy.pause()
        "She locked her eyes with mine and gritted her teeth."
        ver "Ahh... ahhh... ahhh... ahhh..."
        "Her breath became heavier."
        ver "I'm... getting... hotter..."
        ver "Ah~!"
        ver "It's like waves of pleasure are about to hit me!"
        image ver7 = Movie(play="/animations/ver7.webm")
        scene ver7 with dissolve
        $ renpy.pause()
        ver "I... feel... good~"
        "She could not help a smile creeping over her face as I licked the juices that her pussy was squeezing out."
        image ver8 = Movie(play="/animations/ver8.webm")
        scene ver8 with dissolve
        $ renpy.pause()
        p "Feeling like you're about to cum?"
        ver "I'm getting closer, closer~"
        ver "Closer....!!!"
        scene r-148 with flash
        ver "AHHH!"
        "She erupted in a climax. I wonder how long it's been."
        scene r-149 with dissolve
        p "That wasn't so bad now, was it? You liked it, didn't you? It felt good."
        scene r-150 with dissolve
        ver "..."
        ver "(That feeling of pleasure is something I hadn't ever felt with my husband. Is this how it's supposed to feel like?)"
        scene r-151 with dissolve
        ver "It... felt good, I think."
        scene r-152 with dissolve
        ver "Listen, [p], I-"
        play music "sounds/automata.mp3" fadeout 1
        scene r-153 with hpunch
        p "Quick, get changed. I think I hear someone."
        ver "Huh?"
        p "Someone's coming, go!"
        scene r-154 with dissolve
        $ renpy.pause()
        scene r-155 with dissolve
        $ renpy.pause()
        scene r-156 with dissolve
        $ renpy.pause()
        "Who would be here at this time?"
        scene r-157 with dissolve
        x "Mrs. Veronica?"
        "Hang on, is that-?"
        # kaira
        scene r-158 with dissolve
        "Kaira?"
        scene r-159 with hpunch
        ver "O-oh, y-yes, Kaira, it's me. Is there anything you need?"
        scene r-160 with dissolve
        s "Yes, I just wanted to know more about the-"
        scene r-161 with dissolve
        s "[p]? [p]!"
        scene r-162 with dissolve
        s "What are you doing here?"
        p "Oh hey Kaira! I'm just catching up with Miss, I mean, Mrs Veronica here."
        p "She used to be my teacher."
        scene r-163 with dissolve
        s "Oh!"
        scene r-164 with dissolve
        ver "You two know each other?"
        scene r-165 with dissolve
        p "Kaira's my [sr]. We live together."
        ver "Oh, I see. Did you need anything, Kaira?"
        scene r-166 with dissolve
        s "Mmm! What was the homework again?"
        scene r-167 with dissolve
        ver "The homework...?"
        scene r-168 with dissolve
        ver "Oh yes, the homework. Sorry, I'm a little frazzled. That would be pages 24 to 26."
        s "Thanks Mrs Veronica!"
        scene r-169 with dissolve
        s "I'll let you two continue your conversation. I'll see you later okay, [p]?"
        p "See you then, Kaira."
        # transition
        scene r-170 with dissolve
        play music "sounds/alchemy.mp3" fadeout 1
        $ renpy.pause()
        scene r-171 with dissolve
        ver "Phew, that was close."
        scene r-172 with dissolve
        ver "What if my students saw me like this, [p]? This must be a sign."
        p "A sign to what?"
        ver "A sign to stop."
        p "I made you climax and you loved it. It's not a sin to feel pleasure, Miss Veronica."
        p "If it's a sign, it's a sign that it's perfectly fine as long as no one finds out."
        scene r-173 with dissolve
        ver "..."
        p "Think of how good you felt. Only I can do this for you. Not your husband."
        scene r-174 with dissolve
        ver "I wonder what my friend Olivia would do in this situation."
        p "Well, you can only guess."
        scene r-175 with dissolve
        ver "You want me to... to do it with you without my husband knowing."
        p "It's not what I want. It's what you want too."
        p "How many chances like this present themselves?"
        p "You have a business man husband who's always busy, providing for you."
        p "But there things he just can't provide for."
        p "But I'm here. Someone you know, someone you can trust. And I can provide your other needs."
        p "You can have both."
        scene r-176 with dissolve
        ver "This is too much for me."
        ver "Sorry, [p]."
        p "I'll let you finish your work ,Miss Veronica but, just think about it."
        ver "Alright...fine. I will."
        scene r-178 with dissolve
        p "Thank you Miss Veronica."
        ver "Good bye."
        scene black with fade
        "I gave Veronica a taste of the nectar and I just need to give her time."
        "The more deprived of sex she is, the more she will remember me, and may even be curious about finaly getting fucked."
        "Oh that would be good."
        "I just need to set up an opportunity. A movie night? A date with flowers? I could make this happen."
        $ veronicalvl += 1
        $ daytime = 4
        $ daytimes = str(daytime)
        call map_alt from _call_map_alt_13
    if veronicalvl == 3:
        scene r179 with fade
        play music "sounds/cinematic.mp3" fadeout 1
        "Ah, my beloved Veronica."
        "I think I've got something to win her over."
        p "Hello Miss V."
        scene r180 with dissolve
        ver "Oh, [p], hello."
        p "Before you say anymore, I got you something."
        scene r181 with dissolve
        ver "What did you get me?"
        p "It's a tab for the bar at the loft. All on me."
        scene r182 with dissolve
        ver "You're trying to take me out on a date?"
        scene r183 with dissolve
        ver "You know that I'm already taken."
        p "Should you really be saying that?"
        scene r184 with dissolve
        ver "..."
        scene r185 with dissolve
        p "It's just a meet up. I know how much you like your wine."
        p "In the meantime, what are you doing?"
        ver "I was about to do some sit ups."
        p "Well, I'll let you get onto it then."
        # sit ups
        scene r186 with fade
        p "Hmm."
        scene r187 with dissolve
        ver "Is there something wrong with my technique?"
        p "If we get that suit off, I'll be able to tell."
        scene r188 with hpunch
        ver "[p]!"
        ver "I know that we've done some things already, but do you have to be this forward?"
        scene r189 with dissolve
        p "Alright, I'm sorry."
        p "But I think there is something that you could fix up."
        p "Start doing sit ups again?"
        scene r190 with dissolve
        ver "How is this?"
        scene r191 with dissolve
        p "You sure you can't take your pants off?"
        scene r192 with dissolve
        ver "It's suit that covers my whole body. If i take it off, it all comes off."
        p "Too bad, because I think I see your problem."
        scene r193 with dissolve
        ver "What is it?"
        scene r194 with dissolve
        p "The problem is... hehehe..."
        # shift
        play music "sounds/alchemy.mp3" fadeout 1
        scene r195 with vpunch
        p "You are far too horny. In attempt to right it, you've squeezed your legs together far too much."
        scene r196 with hpunch
        ver "[p]! What are you-!"
        ver "No..."
        p "Please be honest, Miss Veronica."
        scene r197 with dissolve
        p "I can feel the squelching from here."
        ver "It-it's not true!"
        image ver9 = Movie(play="/animations/ver9.webm")
        scene ver9 with dissolve
        ver "Ah~"
        p "It's all swollen and engorged."
        ver "[p]! I- what are you doing!"
        ver "Y-You're rubbing my-!"
        image ver10 = Movie(play="/animations/ver10.webm")
        scene ver10 with dissolve
        p "And you still haven't told me to stop yet."
        p "I'll give you the luxury of keeping face. And I'll take your lack of resistance as consent."
        ver "Why, I... hngg..."
        ver "Your fingers~ why do they feel..."
        scene r198 with flash
        ver "Ahh!!!!"
        # rub
        scene r199 with dissolve
        p "You're finished."
        p "See, now you're so much more relaxed. And had a great work out too!"
        p "You're so beautiful, Miss Veronica. If I'm right, it should be super sensitive, right now."
        ver "W-What's sensitive?"
        scene r200 with vpunch
        ver "Ah!"
        image ver11 = Movie(play="/animations/ver11.webm")
        scene ver11 with dissolve
        p "Right here, Miss Veronica."
        ver "Stop, please!"
        p "Alright, if you say so."
        scene r201 with dissolve
        p "Hmm, let's see."
        p "Now try the sit ups again, but this time, take it off, all of it."
        scene r202 with dissolve
        ver "What, why?"
        p "Because then you open yourself up, and you'll have nothing to hide."
        p "You won't feel like you have to close your legs eventually. It's like a confidence exercise."
        scene r203 with dissolve
        ver "(I think I see what he's trying to do... but I just can't bring myself... not yet..."
        scene r204 with dissolve
        ver "I think I know what you're after... but I can't go there."
        scene r205 with dissolve
        ver "It would be very inappropriate."
        p "Oh I see."
        ver "Thank you [p]."
        scene r206 with dissolve
        p "But hang on, I made you feel good. Shouldn't you return the favour?"
        p "I mean, you've done it before."
        scene r207 with dissolve
        ver "(He has a point...)"
        scene r208 with dissolve
        ver "You're right, I have been just taking all this time."
        ver "But, I just don't know how to feel about taking in your- you know."
        scene r210 with dissolve
        p "You could just do a few naked sit ups."
        scene r207 with dissolve
        ver "But then you'd come in for more."
        p "Miss Veronica."
        ver "..."
        scene r209 with dissolve
        play music "sounds/brite.mp3" fadeout 1
        ver "Sigh, very well. It's nothing I haven't done already."
        # strip
        scene r211 with fade
        $ renpy.pause()
        scene r212 with dissolve
        p "Oh my, you're a beautiful woman. Your husband is missing out. It's his loss. What a loser."
        ver "(It feels nice to be appreciated.)"
        "Those well-defined abs complements that gorgeous skin tone, coated with a bit of sweat."
        scene r213 with dissolve
        "What a great set of breasts too. The boys in the class always wondered what Miss V's tits looked like."
        "I can't believe I might be the only one to be lucky enough to finally find out!"
        scene r214 with dissolve
        "And that sweet pussy... I just want to savour it one more time..."
        # shift
        scene r215 with dissolve
        ver "Um, [p]?"
        p "We both knew this was coming, now let's both enjoy this."
        scene r216 with dissolve
        ver "I'm just repaying the favour, right?"
        scene r217 with dissolve
        ver "Oh~"
        ver "It feels good~"
        image ver12 = Movie(play="/animations/ver12.webm")
        scene ver12 with dissolve
        ver "This doesn't count as sex, right? I'm still faithful, right?"
        p "Faithful to your depraved desires."
        image ver13 = Movie(play="/animations/ver13.webm")
        scene ver13 with dissolve
        ver "No, wait, I can't do this if I'm cheating."
        ver "I'm still figuring things out, I'm not just listening to my desires!"
        p "Do you want me to stop?"
        ver "..."
        p "I thought so."
        image ver14 = Movie(play="/animations/ver14.webm")
        scene ver14 with dissolve
        ver "You-!"
        ver "You're. So. Fast!"
        ver "(But why does it feel so good?!)"
        ver "(Why does it not feel like this with my husband?)"
        ver "(Is this what I'm missing out on?!)"
        ver "(My mind is clouding up with pleasure... I can't think!"
        ver "Oh, [p]!"
        scene r218 with flash
        $ renpy.pause()
        p "I'm getting better at making you cum. You're getting warmed up over time."
        p "Much less frigid than before, and mmm, tasty!"
        scene r219 with dissolve
        ver "[p], I'm still figuring things out, okay?"
        p "If you say so."
        ver "No, really."
        p "..."
        scene r222 with dissolve
        p "Just leave your husband already. He's not going to give you any dick."
        p "And I know you want it."
        scene r220 with dissolve
        ver "That's not what it's all about! Maybe one day, you'll understand."
        p "I'm sorry, I went too far."
        ver "I... you..."
        scene r221 with dissolve
        ver "We will talk again later."
        p "Goodbye, Miss V."
        $ renpy.pause()
        $ veronicalvl += 1
        $ daytime = 4
        $ daytimes = str(daytime)
        call map_alt from _call_map_alt_14
    if veronicalvl == 4:
        scene black
        scene r241 with fade
        p "Hmm, she's not here yet. I wonder where she is..."
        scene black with fade
        play music "sounds/pretty.mp3" fadeout 1
        scene r223 with fade
        ver "Time to go to the gym~"
        scene r224 with dissolve
        ver "I have to make sure I look good..."
        scene r225 with dissolve
        ver "My skin is looking good, my gym wear is nice and tight."
        ver "Mm, my body looks good. I'm ready."
        scene r226 with dissolve
        play music "sounds/path.mp3" fadeout 1
        ver "..."
        ver "Hang on, Veronica. Why am I even doing this?"
        scene r227 with dissolve
        ver "Make-up for the gym? Who am I trying to look good for?"
        scene r228 with dissolve
        ver "What does this mean?"
        scene r229 with dissolve
        ver "Am I subconsciously trying to seduce [p]?"
        scene r230 with dissolve
        ver "Oh dear! What if he's there, right now?"
        scene r231 with dissolve
        ver "If I'm doing this subconsciously... what does this say about me?"
        ver "Am I inherently unfaithful to my husband?"
        scene r232 with dissolve
        ver "I can't deny... I'm not getting much action in the bedroom, and [p] makes it abundantly clear that he will satisfy me in that regard."
        scene r233 with dissolve
        ver "He's baiting me, luring me. Closer and closer. He gave me a taste, so that I would beg for more."
        scene r234 with dissolve
        ver "..."
        ver "And it's working."
        scene r235 with dissolve
        ver "What if... I gave into it?"
        scene r236 with hpunch
        ver "M-my husband is probably doing it too with other women right? That's why he's always on those business trips."
        scene r237 with dissolve
        ver "He's doing it too! Who could blame me?!"
        scene r238 with dissolve
        ver "..."
        scene r239 with dissolve
        ver "Oh... [p]..."
        scene r240 with dissolve
        ver "Enough of this, I need to do some exercise to clear my mind."
        # back to gym
        scene r241 with fade
        play music "sounds/alchemy.mp3" fadeout 1
        p "..."
        p "Time to get on with my routine I guess."
        scene r242 with dissolve
        p "Hang on... I hear something."
        # Veronica appears
        scene r243 with dissolve
        $ renpy.pause()
        scene r244 with vpunch
        ver "!!"
        scene r245 with dissolve
        ver "(It's [p]! What should I say, what should I do?)"
        scene r247 with dissolve
        ver "(Maybe I just shouldn't say anything!)"
        "Hmm, why is she avoiding my gaze?"
        scene r246 with dissolve
        p "Um, Miss Veronica?"
        # Looks up
        scene r248 with dissolve
        ver "..."
        scene r249 with dissolve
        ver "Um, just coming here to do my gym routine!"
        p "Yeah, me too. It's good to see you though."
        scene r250 with dissolve
        ver "Um, good to see you too!"
        scene r251 with dissolve
        p "I wanted to ask you something."
        ver "Y-Yes?"
        p "I wanted to know if you have time after."
        p "I'm thinking of us two going to the loft, the same place we first went to."
        scene r252 with hpunch
        ver "!!"
        ver "What for?"
        scene r253 with dissolve
        p "I just wanted to spend some time with my favourite teacher. I have nothing to do this afternoon too."
        p "So what do you say?"
        scene r254 with dissolve
        ver "(If I say yes, who knows where it will go on to next?)"
        ver "(But what reason do I have for saying no?)"
        scene r255 with dissolve
        ver "(If I can control myself, it shouldn't matter right? What's the harm?)"
        scene r256 with dissolve
        ver "(I need to stop acting so wierd in front of [p]!)"
        scene r257 with dissolve
        ver "Of course! I have time, and I can always appreciate some wine."
        p "Good, good!"
        # transition
        stop music fadeout 1
        scene black with fade
        "Some time passes..."
        scene r258 with fade
        play music "sounds/wisteria.mp3" fadeout 1
        p "Man, this is like deja vu!"
        scene r259 with dissolve
        p "Remember the last time we were here?"
        scene r260 with dissolve
        ver "Hmm... nope."
        scene r261 with dissolve
        p "Oh, come on, you're being modest, Miss Veronica!"
        scene r262 with dissolve
        ver "Who knows? I think I had a drink. That affects the memory."
        scene r263 with dissolve
        p "Haha. Speaking of which, how about another drink?"
        ver "Erm..."
        p "I'll be a gentleman. Just wait here. I'll get one for you."
        scene r264 with dissolve
        ver "Ah..."
        p "Don't worry about it."
        scene r265 with fade
        wai "It's been a while, sir."
        wai "Is the occassion a date?"
        scene r266 with dissolve
        p "I suppose you could say so."
        scene r267 with dissolve
        wai "Just like last time?"
        p "..."
        p "I hope so. With any luck anyway, haha."
        scene r268 with dissolve
        wai "I wish you the best."
        p "Sure."
        p "Anyway, I'm looking for drinks."
        scene r269 with dissolve
        wai "Knowing the occassion, may I make a recommendation?"
        p "Go ahead, I'm curious."
        scene r270 with dissolve
        wai "Veronica comes here a lot. I know her tastes, and I know what she finds {i}stimulating{/i}."
        scene r271 with dissolve
        wai "Are you interested?"
        p "Will it make her more adventurous?"
        wai "I can almost guarantee it."
        p "Deal. What about for me?"
        scene r272 with dissolve
        wai "The same."
        p "Haha, sure."
        # Get drinks
        scene r273 with fade
        "So, this drink makes us more adventurous, huh?"
        ver "What is this, [p]?"
        scene r274 with dissolve
        p "I'm not sure, but I'm told it's good. I got the same for myself."
        scene r275 with dissolve
        ver "Hmm..."
        #sip
        scene r276 with dissolve
        $ renpy.pause()
        scene r277 with dissolve
        $ renpy.pause()
        scene r278 with dissolve
        ver "It lifts the mood."
        p "That's good to hear."
        scene r279 with dissolve
        ver "How are you finding it?"
        scene r280 with dissolve
        p "I love it."
        ver "That's good."
        scene r281 with dissolve
        p "So, Miss Veronica."
        ver "Yes?"
        scene r282 with dissolve
        p "What's the deal with you and your husband?"
        p "Surely you know this would be something that I would eventually bring up."
        scene r283 with dissolve
        ver "..."
        scene r284 with dissolve
        ver "I thought it might happen."
        p "Tell me, how long ago was it when you had sex with him?"
        scene r285 with dissolve
        ver "My, [p], that's direct."
        p "Well?"
        ver "A lady can't say."
        p "You can't say, or you don't remember?"
        scene r286 with dissolve
        ver "..."
        ver "(He's right, I don't even remember the last time I received cock from my husband.)"
        p "Where is your husband now?"
        scene r287 with dissolve
        ver "He's on a business trip."
        p "Is he always on a business trip?"
        scene r288 with dissolve
        ver "He's an ambitious, hard-working man. Any dutiful wife should understand his situation."
        scene r289 with dissolve
        p "I noticed that you didn't refer to yourself as dutiful, and you didn't say that you understand his situation."
        p "That's because you don't think it's fair, do you? That you're left home alone for so long."
        p "Without love. Without intimacy."
        p "You think you should understand it, but you don't."
        scene r290 with dissolve
        ver "I-I don't understand what you're implying."
        p "Hey, there's no need to be ashamed. I can understand. It's a shit situation."
        scene r291 with dissolve
        ver "Y-You understand?"
        p "Yeah."
        scene r292 with dissolve
        p "Come to think of it, you don't think he's having sex with tons of gorgeous women when he's away on those business trips?"
        p "I bet he doesn't want sex even when he's home! He's got so many other girls to look forward to!"
        scene r293 with vpunch
        ver "No! That can't be true!"
        scene r294 with dissolve
        ver "It... can't!"
        scene r295 with dissolve
        p "You're receiving the short end of the stick here, Miss Veronica."
        p "He's having all this fun. You're being disrespected."
        p "You're a powerful woman, aren't you?"
        scene r296 with dissolve
        ver "I am. That's why I've been fighting my desires."
        scene r297 with dissolve
        p "No, that makes you weak. You don't even have the power to pursue what you want."
        p "..."
        p "Be honest, Miss Veronica. You want hard cock inside of you, and you're so weak you can't even admit it to yourself."
        scene r298 with hpunch
        ver "!!!"
        scene r299 with dissolve
        ver "I'm... weak for not having sex?"
        ver "T-That can't be right."
        p "You should try it out Miss Veronica. I'll unlock your world. After all we've done, it's only a little bit more."
        scene r300 with dissolve
        ver "..."
        ver "(What if he's right? There's no harm in trying it out, right? I've already tried out so many things with him before.)"
        scene r301 with dissolve
        ver "If we do this, you have to promise me."
        p "Hmm?"
        scene r302 with dissolve
        ver "Promise me that this will just be for today. T-This is just for today."
        scene r303 with dissolve
        p "Oh?"
        scene r304 with dissolve
        ver "It must be the drink. It's making me act this way."
        p "You have no idea."
        scene black with fade
        "A few moments later..."
        # scene change
        play music "sounds/alchemy.mp3" fadeout 1
        p "Where are we going?"
        ver "I know this hotel."
        "A few moments later..."
        p "Why this hotel?"
        scene r305 with fade
        ver "It's far from where I live."
        scene r306 with dissolve
        "How convenient for her to {i}happen{/i} to know this place."
        scene r307 with dissolve
        p "Well, how do you want to do this?"
        scene r308 with dissolve
        ver "Well, I-"
        scene r309 with dissolve
        p "You know what? Just let me lead it, Miss Veronica, and just enjoy."
        scene r310 with dissolve
        ver "Yes..."
        p "Very good. Why don't you start undressing?"
        scene r311 with dissolve
        ver "I understand..."
        play music "sounds/brite.mp3" fadeout 1
        # change
        scene r312 with dissolve
        $ renpy.pause()
        scene r313 with dissolve
        $ renpy.pause()
        scene r314 with dissolve
        $ renpy.pause()
        scene r315 with dissolve
        $ renpy.pause()
        scene r316 with dissolve
        $ renpy.pause()
        scene r317 with dissolve
        $ renpy.pause()
        scene r318 with dissolve
        $ renpy.pause()
        scene r319 with dissolve
        $ renpy.pause()
        scene r320 with dissolve
        $ renpy.pause()
        ver "I'm a little shy... like this."
        ver "Are you staring at me?"
        p "Of course, Miss Veronica. After all, you're a beautiful woman."
        p "Your body would be wasted if nobody looked at it."
        p "Now, hop up on that desk, and close your eyes."
        scene r321 with dissolve
        ver "Yes."
        scene r322 with dissolve
        $ renpy.pause()
        scene r323 with dissolve
        $ renpy.pause()
        ver "L-Like this?"
        p "Just lie down."
        scene r324 with dissolve
        $ renpy.pause()
        "Her breath got heavier as she lay down on the desk, her beautiful pussy in full display."
        p "Close your eyes, darling."
        scene r325 with dissolve
        ver "Please, be gentle."
        # sex
        scene r326 with dissolve
        p "I like it rough, Miss Veronica. I hope you do too."
        ver "I-"
        image ver15 = Movie(play="/animations/ver15.webm")
        scene ver15 with dissolve
        ver "AHHH!"
        p "How long have you waited for this, Miss Veronica?"
        p "Does it feel good, huh?!"
        ver "Ah~!"
        image ver16 = Movie(play="/animations/ver16.webm")
        scene ver16 with dissolve
        ver "It.. feels... so... big!"
        p "You're just tight, Miss. How long has it been since you last had sex?"
        p "This is what you've been missing all this time!"
        p "Does it feel good?"
        ver "Ah~ ah~ ah~ yes.. [p].. it feels good~"
        ver "But... faster..."
        p "Faster?"
        image ver17 = Movie(play="/animations/ver17.webm")
        scene ver17 with dissolve
        p "You horny, horny teacher."
        "As I thrust in and out of her leaking pussy, her breasts bounced up and down."
        "They were clearly natural, but were large, supple and firm at the same time."
        p "Do you know how lewd your body is? Your large tits and well toned body?"
        p "I can't believe your husband hasn't given you cock."
        p "Poor Miss Veronica, spending so much effort to look good, but nobody to fuck her!"
        p "Let's see those breasts jiggle more."
        image ver18 = Movie(play="/animations/ver18.webm")
        scene ver18 with dissolve
        ver "Thank you... for fucking me~!"
        p "I'm fucking close to cumming, Miss, and it's all because of how sexy you are."
        ver "I think I'm cumming too!"
        scene r327 with flash
        $ renpy.pause()
        scene r328 with flash
        $ renpy.pause()
        scene r329 with flash
        $ renpy.pause()
        scene r330 with flash
        $ renpy.pause()
        scene r331 with dissolve
        p "Oh fuck, that was great."
        p "That was great, wasn't it?"
        scene r322 with dissolve
        "Damn, she must have cum so hard she fainted."
        "I guess we're spending the night here."
        scene black with fade
        stop music fadeout 1
        # sex done
        "The next day, on a bright, cheerful morning..."
        play music "sounds/cinematic.mp3" fadeout 1
        scene r333 with fade
        ver "Zzz..."
        scene r334 with dissolve
        ver "Oh, my dear husband, do you know how long I've waited to be able to wake up next to you?"
        scene r335 with dissolve
        ver "I've missed you oh so very much~"
        p "You talking to me?"
        scene r336 with hpunch
        play music "sounds/alchemy.mp3" fadeout 1
        ver "AH!"
        scene r337 with vpunch
        ver "You're not my husband!"
        p "No, sorry to disappoint."
        scene r338 with dissolve
        ver "Last night, we-!"
        # sobs
        scene r339 with dissolve
        ver "{i}Sob...{/i}"
        scene r340 with dissolve
        ver "How could I have done this to my husband?"
        p "It's okay, Miss Veronica. You came so hard you fainted!"
        p "You loved it."
        scene r341 with dissolve
        ver "What's come over me? T-This is not the role model that I want to set for my students!"
        ver "I need to think about my love to my husband."
        scene r342 with dissolve
        p "Oh come on, we already said that he's probably fucking some other chick in a brothel."
        scene r343 with hpunch
        ver "That's not true!"
        scene r344 with dissolve
        ver "..."
        ver "I need to go now."
        scene r345 with dissolve
        ver "Please, [p]... don't follow me."
        p "..."
        # she leaves
        $ veronicalvl += 1
        scene splash5 with fade
        $ renpy.pause()
        call map_alt from _call_map_alt_15
    else:
        scene gym
        "Veronica isn't here."
        call map_alt from _call_map_alt_16
