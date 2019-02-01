label amandatalk:
    if amandalvl == 1:
        scene black
        scene a-1 with fade
        play music "sounds/wisteria.mp3" fadeout 1
        p "Hi [mr]."
        m "Good morning [p], and I see this time you've even got your clothes on!"
        p "Oooh, I'm so sorry about that."
        scene a-2
        p "I can't help it you know, my feet just take me to random places when I'm sleep walking!"
        scene a-1
        m "Did you have a wild night last night?"
        "I probably shouldn't tell her I fucked Nicole..."
        p "Uh, no uh, of course not, it was a pretty normal night. What do you mean wild?"
        scene a-3
        m "You didn't go out to party with Kaira and Nicole?"
        p "Ah of course! Yeah we went out, it was great. I thought you were talking about something else."
        scene a-4 with dissolve
        m "What did you think I was talking about?"
        "Fuck!"
        p "Uhh... I'm not sure anymore. Ah, I think the alcohol is still disabling my brain a bit!"
        p "Wernicke's encephalopathy, or something."
        scene a-5
        m "What's that?"
        p "Oh apparently it's something you get from too much alcohol. This medical student called Caroline I met at the bar told me about it."
        scene a-6 with dissolve
        m "Wow, look at you! Meeting girls at the bar!"
        m "Was she cute?"
        p "Oh no haha, I mean, she's beautiful, but she was the bar maid. Not really looking to meet anyone you know."
        scene a-1 with dissolve
        m "Well maybe you can meet her in a different context, and ask her out sometime."
        p "I'll have to meet her again first."
        p "Anyway, I should probably check up on Kaira."
        scene a-1
        m "She's gone out with Nicole to the cafe to get some coffee. They might be on their way back now. She should be back in the afternoon!"
        m "You can take a nap on your bed to pass time."
        p "And where will you be?"
        scene a-8
        m "Oh dearie, [mr] has to go and work."
        m "I ought to be back sometime in the evening."
        p "Have fun modelling [mr], don't give too many guys nosebleeds!"
        scene a-7 with dissolve
        m "Oh stop it!"
        play music "sounds/heart.mp3" fadeout 1
        $ amandalvl += 1
        $ amandatalk = day
        $ amandakitchen = True
        jump amanda_room
    if amandalvl == 2 and amandakitchenlvl == 2 and day > amandatalk:
        scene black
        scene a-2 with fade
        $ amandashow = ["1"]
        play music "sounds/wisteria.mp3" fadeout 1
        p "Good morning, [mr]!"
        p "Getting ready for another day of work?"
        scene a-1
        m "The work never stops."
        p "It's enjoyable work though, right?"
        scene a-8
        m "..."
        scene a-2 with dissolve
        m "Yes, it's quite fun."
        "She doesn't sound too convinced?"
        p "Tell me about it."
        p "What kind of work do you do?"
        scene a-3
        m "Well, I model. I go into the studio, get some shots done, and I get some payment."
        p "Is it stressful?"
        scene a-4 with dissolve
        m "Well..."
        scene a-5 with dissolve
        m "It's never an easy thing you know, to relax in front of the camera."
        m "It takes a lot of honesty, and you have to be very confident to do it well."
        p "You should be really confident, you're gorgeous [mr]!"
        p "I can't imagine you could take a bad picture."
        scene a-6 with dissolve
        m "Oh, [p], fufufu..."
        m "Thanks for the encouragement!"
        p "I'm only telling the truth, you know that."
        scene a-7
        m "And how are you going yourself?"
        p "Just hanging around town, getting to know different people I guess."
        p "Enjoy work, [mr]."
        scene a-5
        m "I will. I'll tell you all about it when I get back this evening~!"
        $ amandalvl += 1
        $ amandatalk = day
        jump amanda_room
    if amandalvl == 3 and amandakitchenlvl == 3 and day > amandatalk:
        scene black
        scene a-2 with fade
        play music "sounds/wisteria.mp3" fadeout 1
        p "Hello [mr]."
        m "Good morning!"
        p "Getting ready for work?"
        m "It's the same routine everyday."
        p "Where do you go to work anyway?"
        m "It's a small studio somewhere in town..."
        p "Can you take me one day?"
        m "Umm, haha... it's really nothing at all."
        m "Don't worry about it."
        p "Come on, I wanna see where you work!"
        m "It's really nothing special. It's not worth fussing about."
        p "Aww!"
        m "Besides, I might not be working there for much longer anyway."
        p "What do you mean?"
        m "My photoshoots are getting cut shorter and shorter, and-"
        m "..."
        m "I guess we'll see."
        p "I'm sorry I brought it up."
        m "Oh, that's okay. I'll see you in the evening, okay?"
        p "Take it easy, [mr]."
        $ amandalvl += 1
        $ amandatalk = day
        jump amanda_room
    if amandalvl == 4 and amandakitchenlvl == 4 and day > amandatalk:
        scene black
        scene a-1 with fade
        play music "sounds/wisteria.mp3" fadeout 1
        p "Hi [mr]."
        m "Good to see you [p]."
        m "I was... thinking about what you said the other day."
        p "About not relying on the agency?"
        m "Yes, but how is that going to work?"
        m "The agency gives me work, how could I possibly find work without them?"
        p "Like I said, it's the age of the internet."
        p "It's easy to reach people these days."
        m "How are we going to do that?"
        p "We just need to get you out there. Get an audience."
        p "Afterward, set up a Patreon, or something like that."
        m "People will pay money for my pictures?"
        p "People don't {i}have{/i} to pay on Patreon, but only cheap fucks freeload."
        m "Hmm..."
        m "That sounds a little exciting."
        m "But will people really pay money? For me?"
        p "You're a beautiful woman, [mr]. Of course they will."
        p "The stupid agency has gotten you doubting yourself."
        p "Leave it to me, I'll sort something out."
        m "You're too sweet."
        m "I'll see you when I'm back from work."
        "Hmm, we might be able to make something new."
        $ amandalvl += 1
        $ amandatalk = day
        jump amanda_room
    if amandalvl == 5 and amandakitchenlvl == 5 and day > amandatalk and DSLR == True:
        scene black
        scene a-1 with fade
        play music "sounds/wisteria.mp3" fadeout 1
        p "Exciting news, [mr]!"
        p "I got us a camera!"
        p "Cost me a pretty penny too."
        m "Is it one of those 'pro' ones?"
        p "It's a DSLR camera, all the pros use them."
        m "So how is it going to work?"
        p "Just go to work as usual, and when you come back in the evening, we can start taking pictures."
        p "We can build it up slowly so that we have solid content to release to people."
        m "You're having me work throughout the whole day!"
        p "Ahaha, sorry [mr]. Do you think it might be better if you quit your job first?"
        m "Well, this is all very exciting, but I think I'll keep my job for now, even if it's not going too well."
        m "If this thing takes off, maybe I could look at quitting then."
        p "I just don't want you to burn out from working too long."
        m "Oh don't worry, [mr] was just teasing!"
        m "I enjoyed our evening session last time, and that was kind of like modelling, no?"
        m "I'm sure it'll be a lot of fun."
        p "Awesome, we'll give it a go when you come back tonight."
        p "Take care, [mr]!"
        m "You too, sweetie!"
        $ amandalvl += 1
        $ amandatalk = day
        jump amanda_room
    if amandalvl == 6 and amandakitchenlvl == 6 and day > amandatalk and guide == True:
        scene black
        scene a-1 with fade
        play music "sounds/wisteria.mp3" fadeout 1
        p "Good morning [mr]."
        m "Good morning to you too, [p]!"
        p "I did some reading on the whole modelling and photography thing."
        p "I think we could definitely try taking some pictures when you come back from work."
        m "Can you give me directions?"
        p "I'm still working on that bit. I think I should work on camera angles first."
        m "That's good to hear!"
        m "A good photographer always has an outfit picked out for their model - have you any for me?"
        p "I'll make sure to pick a nice outfit before we have our next shoot."
        m "I'm looking fowrward to it!"
        $ amandalvl += 1
        $ amandatalk = day
        jump amanda_room
    if amandalvl == 7 and amandakitchenlvl == 7 and day > amandatalk:
        scene black
        scene a-1 with fade
        play music "sounds/wisteria.mp3" fadeout 1
        p "How was the photoshoot yesterday, [mr]?"
        m "It was really fun."
        m "You were like a real pro!"
        m "If we keep at it for a few more sessions, I'm sure you can move on to giving directions!"
        p "I know, I'm a slow learner. I'm still figuring out the different types of shots."
        p "What's an example of a direction I could give?"
        m "You could tell me to look at the camera, arch my back, bite my lip..."
        m "That sort of direction."
        p "Sounds exciting, but I'll master taking shots for the next two sessions, and then I'll try some of that."
        m "If you please!"
        $ amandalvl += 1
        $ amandatalk = day
        jump amanda_room
    if amandalvl == 8 and amandakitchenlvl == 8 and day > amandatalk and nicolelvl >= 6:
        scene black
        scene a-1 with fade
        play music "sounds/wisteria.mp3" fadeout 1
        p "Good morning, [mr.]"
        m "Good morning, [p!]!"
        p "You know I've been thinking about how to market you and get break you into the scene."
        m "That parts always the challenge, isn't it?"
        p "It is, but I think I can call on someone for help."
        p "It's a long story, but I've got a friend called Vincent. He works in the photo industry."
        p "I think I'll give him a call and see if he has any tips."
        p "Actually, I can just call him now."
        m "You know some interesting people!"
        p "Give me a moment..."
        p "He gave me his number before..."
        p "{i}Buzz... buzz{/i}."
        v "Hey there, Vincent here. Professional photography, modelling services and more. How can I help?"
        p "Um, hey Vincent. It's me, [p]."
        v "...[p]?"
        v "Jesus man, I thought you'd never call."
        v "How's it going?"
        p "I'm going good, Vincent. Hey listen."
        p "You said you worked at some photography business right?"
        v "I do a bit of this and a bit of that, what's up?"
        p "My [mr]'s a model, but she's considering going freelance."
        p "Do you have any insights about how she can have her breakthrough to reach a large audience?"
        v "Well, I have a few ideas, but we should talk about it over coffee or something."
        v "You should also show me a few pictures, that way I'd know where she could fit into the market."
        p "Oh that's no problem at all."
        p "I'm going to take more pictures tonight, so I chat with you tomorrow."
        v "Cool. How does coffee tomorrow morning sound?"
        p "I'm good with that, I'll see you at the cafe tomorrow."
        v "see you tomorow"
        "..."
        p "Looks like I've got some contacts in the business!"
        m "What did he say?"
        p "He said that he's got a few ideas for us, but that he'd need to see your pictures first."
        p "You know, to kind of get an idea of what you're going for."
        m "Sounds fair."
        p "We'll meet up tomorrow after we get the shoot done tonight."
        m "More to look forward to!"
        $ amandalvl += 1
        $ amandatalk = day
        jump amanda_room

    scene a-1
    p "Looking good [mr]!"
    scene a-6 with dissolve
    m "Like I said, I've still got it!"
    jump amanda_room
