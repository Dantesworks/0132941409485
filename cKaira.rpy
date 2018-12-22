label Kaira:

    if kairalvl == 1:
        scene black
        p "Hi Kaira"
        s "Afternoon [p]!"
        p "You were pretty wasted last night."
        p "How are you holding up?"
        s "Last night?"
        s "I don't remember anything about last night."
        p "Phew!"
        p "I mean-"
        s "It's okay, Nicole already told me what happened last night."
        p "..."
        p "I know what you're thinking, and we probably shouldn't have gone there, but-"
        s "Don't worry about it! It wasn't your fault I fell over."
        p "...hang on, what did Nicole tell you exactly?"
        s "Now I'm the one confused."
        s "She said I had too much to drink, and then I passed out and fell onto a pool of booze."
        s "That's apparently why I felt so sticky in the morning."
        p "..."
        s "There's a lot of sticky liquid on my chest especially!"
        s "My tits must have absorbed the fall. I knew they'd also have a practical use!"
        p "Are you feeling alright now?"
        s "Hmm, I'm coming around now, but I still have this strange taste in my mouth."
        "Oh shit..."
        s "It's like nothing I've ever tasted before, but I don't mind it."
        s "Anyway, Nicole said you took care of me what I was drunk. Thanks for that!"
        p "No worries at all, I'll always be there for my [sr]. You know that right?"
        s "Mm!"
        p "Speaking of Nicole, did you meet her in the morning?"
        s "She came by and we went to grab a cup of coffee at the cafe. I needed it sooo badly. I was feeling so groggy!"
        p "Where is she now?"
        s "Why do you want to know anyway? Do you like her?"
        p "...I don't know what to say. She's quite a handful isn't she?"
        s "Yeah they're big, but like, they're not real ya know? Not like mine!"
        p "That's not what I meant by handful haha."
        p "She's a... strange character."
        s "Ooh, intriguing!"
        s "Do you want to learn more?"
        p "Yeah, I guess. How exactly did you guys meet?"



        $ kairalvl += 1
        $ nicoleday = day + 1
        jump kaira_room
