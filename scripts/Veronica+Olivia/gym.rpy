default gym_intro = False
default veronicalvl = 1
default olivialvl = 1
label gym:
    if gym_intro == False:
        $ gym_intro = True
        play music "sounds/cinematic.mp3" fadeout 1
        "Man this gym is hard to find."
        "Trying to get there is a workout in and of itself!"
        "Hang on... I think this is it."
        scene splash6 with fade
        d "You are about to enjoy content with commissioned side characters with very depraved themes, including blackmail and corruption."
        d "Proceed at your own risk!"
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
        image ver1 = Movie(play="/animations/ver1.mp4")
        image ver2 = Movie(play="/animations/ver2.mp4")
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
        call daykeep from _call_daykeep_31
        jump map
    if veronicalvl == 2:
        "Looks like I managed to catch Veronica at the gym today."
        p "Hello, Miss Veronica. Good to see you."
        ver "Oh, hey [p]..."
        p "How are you doing?"
        ver "Oh I'm going fine..."
        p "Did you think much about the other day?"
        ver "..."
        p "I don't want it to be awkward between us, but I just wanna say, I enjoyed it."
        p "And I think really, you liked it too."
        ver "I'm a married woman, [p], and I have a loving husband at home."
        p "You said yourself, he's barely at home, he's travelling all the time and you're by yourself."
        p "I'm not asking you to leave, but you should be allowed to have some fun."
        ver "I..."
        ver "Sorry. but I have to go now."
        ver "I've got some study material to pick up at the school."
        p "Going already?"
        ver "I've finished my workout."
        ver "..."
        ver "Goodbye."
        "So Miss Veronica's going back to school, huh?"
        "I haven't been back in a while but I should go there after my work out and catch her in the classroom."
        # transition
        "She's right there, just like I remember her when I was back in high school."
        "All that time I had a crush on her. Now that I have a chance to get close to her, and convince her to try it out with me, I'm not going to give it up."
        "I remember those countless afternoons popping boners in the classroom. And they were all because of you, Miss Veronica."
        "I've gotten you to suck me off already. I want to take this much further."
        p "Hey!"
        ver "[p]?! What are you doing here?"
        p "I used to come to this school, you know?"
        ver "Yes, I know, I was your teacher."
        p "Yeah, you {i}were{/i}."
        p "It wasn't so long ago that I would be standing right here, and you would walk past me, Miss Veronica."
        ver "You can just call me Veronica."
        p "I know, but you know why I don't."
        p "You're that sexy teacher, and to me you'll always be Miss Veronica."
        p "You've got something I want. I've got something you need."
        ver "[p]! Stop!"
        ver "What we did that day - I regret it. It's not your fault-"
        ver "I was selfish. I was only thinking about myself and my pleasures, and what I was missing out on."
        ver "I wasn't thinking about my husband."
        p "The boys loved you in high school, Miss Veronica. It wasn't just because of your looks."
        p "You are a caring woman who really looked after her students, and saw to their needs."
        p "But it's time to think about your own needs, Miss."
        ver "..."
        p "At the very least, let me do for you what you did for me."
        ver "[p], I..."
        p "School's over, Miss. It's just us two now."
        p "Be selfish just a little longer. And at the same time, do it for me."
        p "It's the right thing to do."
        ver "(What would be the harm of giving in just a little?)"
        ver "(It-it's not like my husband will ever find out...)"
        ver "..."
        ver "What do you want me to do?"
        p "Nothing, Miss Veronica. I'll do the work this time."
        p "Just lean back, and... close your eyes."
        ## cunni
        p "That wasn't so bad now, was it? You liked it, didn't you? It felt good."
        ver "..."
        ver "(That feeling of pleasure is something I hadn't ever felt with my husband. Is this how it's supposed to feel like?)"
        ver "It... felt good, I think."
        ver "Listen, [p], I-"
        p "Quick, get changed. I think I hear someone."
        "Who would be here at this time?"
        x "Mrs. Veronica?"
        "Hang on, is that-?"
        # kaira
        "Kaira?"
        ver "O-oh, y-yes, Kaira, it's me. Is there anything you need?"
        k "Yes, I just wanted to know more about the-"
        k "[p]? [p]!"
        k "What are you doing here?"
        p "Oh hey Kaira! I'm just catching up with Miss, I mean, Mrs Veronica here."
        p "She used to be my teacher."
        k "Oh!"
        ver "You two know each other?"
        p "Kaira's my [sr]. We live together."
        ver "Oh, I see. Did you need anything, Kaira?"
        k "Mmm! What was the homework again?"
        ver "The homework? Oh yes, the homework. Sorry, I'm a little frazzled."
        ver "That would be pages 24 to 26."
        k "Thanks Mrs Veronica!"
        k "I'll let you two continue your conversation. I'll see you later okay, [p]?"
        p "See you then, Kaira."
        # transition
        ver "Phew, that was close."
        ver "What if my students saw me like this, [p]? This must be a sign."
        p "A sign to what?"
        ver "A sign to stop."
        p "I made you climax and you loved it. It's not a sin to feel pleasure, Miss Veronica."
        p "If it's a sign, it's a sign that it's perfectly fine as long as no one finds out."
        ver "..."
        p "Think of how good you felt. Only I can do this for you. Not your husband."
        ver "I wonder what my friend Olivia would do in this situation."
        p "Well, you can only guess."
        ver "You want me to... to do it with you without my husband knowing."
        p "It's not what I want. It's what you want too."
        p "How many chances like this present themselves?"
        p "You have a business man husband who's always busy, providing for you."
        p "But there things he just can't provide for."
        p "But I'm here. Someone you know, someone you can trust. And I can provide your other needs."
        p "You can have both."
        ver "I... need to think about it."
        ver "Sorry, [p]."
        p "No, don't be sorry."
        p "I'll let you finish your work."
        p "Good bye Miss Veronica."
        ver "Good bye."
        scene black with fade
        "I gave Veronica a taste of the nectar and I just need to give her time."
        "The more deprived of sex she is, the more she will remember me, and may even be curious about finaly getting fucked."
        "Oh that would be good."
        "I just need to set up an opportunity. A movie night? A date with flowers? I could make this happen."
    else:
        scene gym
        "Veronica isn't here."
        jump map
