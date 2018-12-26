label Kaira:
    hide screen daytime
    hide screen map_icon
    if amandalvl == 2 and kairalvl == 1:
        scene k-1
        play music "sounds/automata.mp3" fadeout 1
        p "Hi Kaira."
        scene k-2
        $ renpy.pause()
        scene k-3
        s "Afternoon [p]!"
        p "You were pretty wasted last night."
        p "How are you holding up?"
        scene k-6
        s "Last night?"
        s "I don't remember anything about last night."
        p "Phew!"
        p "I mean-"
        scene k-4
        s "It's okay, Nicole already told me what happened last night."
        p "..."
        p "She did?"
        "Oh no!"
        scene k-9
        s "Don't worry about it! It wasn't your fault I fell over."
        p "...hang on, what did Nicole tell you exactly?"
        scene k-8
        s "Now I'm the one confused."
        scene k-5
        s "She said I had too much to drink, and then I passed out and fell onto a pool of booze."
        s "That's apparently why I felt so sticky in the morning."
        p "..."
        scene k-11
        s "There's a lot of sticky liquid on my chest especially!"
        scene k-10
        s "My tits must have absorbed the fall. I knew they'd also have a practical use!"
        p "Are you feeling alright now?"
        scene k-12
        s "Hmm, I'm coming around now, but I still have this strange taste in my mouth."
        "Oh shit..."
        s "It's like nothing I've ever tasted before, but I don't mind it."
        scene k-4
        s "Anyway, Nicole said you took care of me when I was drunk. Thanks for that!"
        p "No worries at all, I'll always be there for my [sr]. You know that right?"
        s "Mm!"
        p "Speaking of Nicole, did you meet her in the morning?"
        scene k-10
        s "She came by and we went to grab a cup of coffee. I needed it sooo badly. I was feeling so groggy!"
        p "Where is she now?"
        scene k-12
        s "Why do you want to know anyway? Do you like her?"
        p "...I don't know what to say. She's quite a handful isn't she?"
        scene k-11
        s "Yeah they're big, but like, they're not real ya know? Not like mine!"
        p "That's not what I meant by handful haha."
        p "She's a... strange character."
        scene k-12
        s "Ooh, intriguing!"
        s "Do you want to learn more?"
        p "Yeah, I guess. How exactly did you guys meet?"
        scene k-10
        s "Hmm... we met in school and just sort of got along."
        s "Maybe she saw something in me?"
        scene k-8
        s "I don't know, we met a long time ago, we kinda meshed together well."
        p "Yeah but what exactly drew you together?"
        scene k-5
        s "Oh it's many things [p]! A friendship is not just because of one thing."
        scene k-4
        s "That goes for any kind of relationship!"
        scene k-11
        p "Looks like your memory problems are long standing."
        s "Hey!"
        scene k-12
        s "What do {i}you{/i} think about Nicole?"
        scene k-10
        p "Well!"
        menu:
            "I like her, but it'd be better if she was more... upfront?":
                scene k-4
                s "She can be quite introverted sometimes, but I think if you get to know her, she'll really open up."
                p "You think so?"
                jump k1

            "She's stunning yet mysterious. It's what guys like me go for.":
                $ depravity += 1
                s "If you guys ever end up being a thing, you have to credit me!"
                jump k1
        label k1:
            s "So, are you going to go for her? For real?"
            p "Chill, we'll see how it goes."
            scene k-12
            s "Well! You should know that Nicole usually comes over in the afternoons."
            s"Though, she won't be coming in today since we already caught up this morning."
            p "You've done well, little Kaira. Let the big man handle the rest."
            scene k-9
            s "Remember [p]! Never forget me even if you marry Nicole and move far far away!"
            p "Of course not, life wouldn't be complete without my [sr]."
            scene k-4
            p "..."
            p "By the way, something came to mind."
            p "Have you been having weird dreams lately?"
            scene k-6
            s "Um ah ah-!"
            p "Kaira?"
            scene k-9
            s "I haven't been having perverted dreams at all! What are you talking about?!"
            scene k-5
            s "Ah..."
            "Well that wasn't hard at all."
            p "Kaira, what about these dreams? You can tell me."
            scene k-9
            s "Ooh, um... Sorry I got a lot of work to do ehh, can't talk anymore, bye!"
            p "Hey look, I'm sorry for prodding. Maybe we could talk about it some other time?"
            s "Ahaha sure sure sure! But I reaaally got to get back to work!"
            p "Alright, I'll go!"
            scene black with fade
            s "Hey [p]!"
            scene k-13 with dissolve
            s "Sorry for cutting this short, we'll talk more about it later, ok?"
            s "Please don't hate me!"
            p "Never, Kaira. You tell me when you're ready."
            p "Bye!"
            scene black with fade
            "Is she having dreams that I'm having?"
            "They're more than just perverted dreams."
            "What does it mean?"
            "I guess I'll have to cross that bridge when I get there."
            $ kairalvl += 1
            $ nicoledelay = day + 1
            $ nicoleshow = ["2"]
            play music "sounds/heart.mp3" fadeout 1
            jump kaira_room

    scene k-1
    p "How's my beautiful [sr] doing?"
    scene k-3
    s "Oooh!"
    s "So that's what [mr] means she says you have a silver tongue! You must do great around the ladies."
    p "I'm doing alright around you aren't I?"
    s "Alright alright! We'll talk later okay? I have to do some work first!"
    jump kaira_room
