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
        scene a-1 with dissolve
        m "Good morning!"
        p "Getting ready for work?"
        scene a-4 with dissolve
        m "It's the same routine everyday."
        p "Where do you go to work anyway?"
        m "It's a small studio somewhere in town..."
        p "Can you take me one day?"
        scene a-5 with dissolve
        m "Umm, haha... it's really nothing at all."
        m "Don't worry about it."
        p "Come on, I wanna see where you work!"
        scene a-1 with dissolve
        m "It's really nothing special. It's not worth fussing about."
        p "Aww!"
        scene a-3 with dissolve
        m "Besides, I might not be working there for much longer anyway."
        p "What do you mean?"
        m "My photoshoots are getting cut shorter and shorter, and-"
        scene a-8 with dissolve
        m "..."
        m "I guess we'll see."
        p "I'm sorry I brought it up."
        scene a-2 with dissolve
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
        scene a-2 with dissolve
        m "Good to see you [p]."
        scene a-3 with dissolve
        m "I was... thinking about what you said the other day."
        p "About not relying on the agency?"
        m "Yes, but how is that going to work?"
        scene a-8 with dissolve
        m "The agency gives me work, how could I possibly find work without them?"
        p "Like I said, it's the age of the internet."
        p "It's easy to reach people these days."
        m "How are we going to do that?"
        p "We just need to get you out there. Get an audience."
        p "Afterward, set up a Patreon, or something like that."
        scene a-5 with dissolve
        m "People will pay money for my pictures?"
        p "People don't {i}have{/i} to pay on Patreon, but they will if they want to go to heaven."
        scene a-4 with dissolve
        m "Hmm..."
        m "That sounds a little exciting."
        m "But will people really pay money? For me?"
        p "You're a beautiful woman, [mr]. Of course they will."
        p "The stupid agency has gotten you doubting yourself."
        p "Leave it to me, I'll sort something out."
        scene a-6 with dissolve
        m "You're too sweet."
        m "I'll see you when I'm back from work."
        "Hmm, we might be able to make something really cool"
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
        scene a-6 with dissolve
        m "Is it one of those 'pro' ones?"
        p "It's a DSLR camera, all the pros use them."
        scene a-5 with dissolve
        m "So how is it going to work?"
        p "Just go to work as usual, and when you come back in the evening, we can start taking pictures."
        p "We can build it up slowly so that we have solid content to release to people."
        scene a-7 with dissolve
        m "You're having me work throughout the whole day!"
        p "Ahaha, sorry [mr]. Do you think it might be better if you quit your job first?"
        m "Well, this is all very exciting, but I think I'll keep my job for now, even if it's not going too well."
        m "If this thing takes off, maybe I could look at quitting then."
        p "I just don't want you to burn out from working too long."
        scene a-1 with dissolve
        m "Oh don't worry, [mr] was just teasing!"
        scene a-2
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
        scene a-2 with fade
        play music "sounds/wisteria.mp3" fadeout 1
        p "Good morning [mr]."
        m "Good morning to you too, [p]!"
        p "I did some reading on the whole modelling and photography thing."
        p "I think we could definitely try taking some pictures when you come back from work."
        scene a-4 with dissolve
        m "Can you give me directions?"
        p "I'm still working on that bit. I think I should work on camera angles first."
        scene a-6 with dissolve
        m "That's good to hear!"
        m "A good photographer always has an outfit picked out for their model - have you any for me?"
        p "I'll make sure to pick a nice outfit before we have our next shoot."
        scene a-5
        m "I'm looking fowrward to it!"
        $ amandalvl += 1
        $ amandatalk = day
        jump amanda_room
    if amandalvl == 7 and amandakitchenlvl == 7 and day > amandatalk:
        scene black
        scene a-2 with fade
        play music "sounds/wisteria.mp3" fadeout 1
        p "How was the photoshoot yesterday, [mr]?"
        scene a-1
        m "It was really fun."
        m "You were like a real pro!"
        m "If we keep at it for a few more sessions, I'm sure you can move on to giving directions!"
        p "I know, I'm a slow learner. I'm still figuring out the different types of shots."
        p "What's an example of a direction I could give?"
        scene a-2 with dissolve
        m "You could tell me to look at the camera, arch my back, bite my lip..."
        m "That sort of direction."
        p "Sounds exciting, but I'll master taking shots for the next two sessions, and then I'll try some of that."
        m "If you please!"
        $ amandalvl += 1
        $ amandatalk = day
        jump amanda_room
    if amandalvl == 8 and amandakitchenlvl == 8 and day > amandatalk and nicolelvl >= 8:
        scene black
        scene a-1 with fade
        play music "sounds/wisteria.mp3" fadeout 1
        p "Good morning, [mr]"
        m "Good morning, [p!]!"
        p "You know I've been thinking about how to market you and get break you into the scene."
        scene a-3
        m "That parts always the challenge, isn't it?"
        p "It is, but I think I can call on someone for help."
        p "It's a long story, but I've got a friend called Vincent. He works in the photo industry."
        p "I think I'll give him a call and see if he has any tips."
        p "Actually, I can just call him now."
        scene a-1
        m "You know some interesting people!"
        scene ae-74 with dissolve
        p "Give me a moment..."
        p "He gave me his number before..."
        scene ae-75 with dissolve
        play music "sounds/wistful.mp3"
        "{i}Buzz... buzz{/i}."
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
        p "I'm going to take more pictures tonight, so I can chat with you tomorrow."
        v "Cool. How does coffee tomorrow morning sound?"
        p "I'm good with that, I'll see you at the cafe tomorrow."
        v "See you tomorrow"
        "..."
        scene ae-74 with dissolve
        p "Looks like I've got some contacts in the business!"
        scene a-7
        m "What did he say?"
        p "He said that he's got a few ideas for us, but that he'd need to see your pictures first."
        p "You know, to kind of get an idea of what you're going for."
        scene a-4
        m "Sounds fair."
        p "We'll meet up tomorrow after we get the shoot done tonight."
        scene a-1 with dissolve
        m "More to look forward to!"
        $ amandalvl += 1
        $ amandatalk = day
        jump amanda_room
    if amandalvl == 9 and amandakitchenlvl == 9 and day > amandatalk:
        scene black
        scene a-1 with fade
        play music "sounds/wisteria.mp3" fadeout 1
        p "Hey [mr]."
        m "Hi [p]."
        p "It's the big moment. I'm about to go and meet Vincent, and show him the pictures we've gotten so far."
        p "Are you excited?"
        scene a-6 with dissolve
        m "It's not the first time my pictures have been sent around - I'm not new to this, you know!"
        p "Well this is all still new to me."
        scene a-5
        m "What are you going to talk about?"
        p "I'm not sure yet. He just said that had had a few ideas about how he could promote your pictures."
        p "Vincent travels around the place working for the photography industry. I'm sure he has some insights."
        scene a-4
        m "Let's hope so."
        p "I'll be heading off soon. Just let me check that I've got the pictures ready."
        scene a-9 with dissolve
        m "Do you have the ones with the long gown?"
        p "Check."
        m "Security dress?"
        p "Check."
        m "Gym wear?"
        p "Check."
        scene a-11
        m "They're good pictures, [p]. You were a great photographer."
        p "Thanks [mr]. But they only look as good as you are beautiful."
        p "I'm sure Vincent will love 'em."
        p "It's time for me to go now. I shouldn't keep him waiting."
        scene a-2 with dissolve
        m "Good luck, [p]."
        p "To us both."
        ## Transition to Cafe
        scene black with fade
        stop music fadeout 1
        "Alright, time to head off to the cafe with the pictures."
        "..."
        scene ae-76 with fade
        play music "sounds/coffee.mp3" fadeout 1
        $ renpy.pause ()
        "Oh, there he is."
        scene ae-77 with dissolve
        p "Good morning Vincent, good to see you again buddy!"
        scene ae-78 with dissolve
        v "My man [p]!"
        v "It took you a while to call me man, I thought I lost you!"
        p "Yeah sorry, I actually didn't have a phone until quite recently."
        v "You bought a new one?"
        p "I didn't really buy it, but it's pretty new. It's the iDante phone from last year."
        p "My girlfriend gave it to me since she didn't need it anymore. She's got her eyes on the new one."
        scene ae-79 with dissolve
        v "That's modernity for you. Everything has to be new, shiny and pretty."
        p "Speaking of that, I brought some photos that I took of my [mr]."
        p "She's already working as a model, but we're hoping to go freelance."
        scene ae-81 with dissolve
        v "Oh sure, I'll take a look later, but before that..."
        v "Coffee? On me."
        p "Well, I'm not going to say no. Thanks!"
        v "No problem."
        scene ae-82 with dissolve
        v "Hey. Two cups of Joe please."
        ellie "Sugar?"
        scene ae-83 with dissolve
        v "Sugar? [p]?"
        menu:
            "Sure.":
                scene ae-82 with dissolve
                v "Looks like my friend wants some sugar."
                v "Could you give it to him?"
                scene ae-84 with dissolve
                ellie "Ahahah."
                ellie "There's plenty to go around!"
            "I'll pass.":
                scene ae-82 with dissolve
                v "No sugar thanks; I think you're sweet enough for the both of us."
                scene ae-84 with dissolve
                ellie "Oh gosh hahah."
        scene coffee with fade
        ellie "Here's your coffee!"
        v "Cheers."
        v "Mmm..."
        v "Nothing like some joe in the morning."
        p "Absolutely."
        scene ae-80 with fade
        v "So, what is it that you wanted to talk about?"
        p "I know you're in the photography/modelling industry, and I'm wondering if you had some insights."
        p "My [mr] is looking to quit the agency she's with and go solo."
        p "I think she's got the chops to do it, we just need to have a breakout."
        scene ae-78
        v "Let's see the pictures you took."
        p "Alright sure, here you go."
        scene ae-46 with dissolve
        $ renpy.pause ()
        v "Jeez man this is your [mr]?"
        p "Yeah it is."
        v "That gown looks stunning on her."
        p "Thanks, I'll tell her that."
        scene ae-59 with dissolve
        $ renpy.pause ()
        v "This one's completely different."
        p "I tried to go for different looks."
        v "It's looking good so far."
        scene ae-69 with dissolve
        $ renpy.pause ()
        v "Just fearless."
        p "She's not always confident, but I think she looks good in front of the camera."
        scene ae-78 with dissolve
        v "Wow, these all look great."
        v "Tell me again. This is your [mr]?"
        p "Yeah."
        v "Damn. Congratulations?"
        p "What for?"
        scene ae-79
        v "Never mind."
        scene ae-78
        v "I wasn't sure what I was expecting, but she's really something man. I'm seeing opportunities already."
        p "Really? Tell me!"
        v "First of all, I started doing photography and slowly made my way up."
        v "I'm now a large shareholder of a company."
        v "We do photography services, set up fashion shows, runways and generally have our ties in a lot of different things like that."
        v "I wanted to get to see the pictures because I'm actually looking for some upcomers."
        p "Is this where [mr] comes in?"
        scene ae-80
        v "Maybe. What's her name by the way?"
        p "It's Amanda."
        v "Well, I've been looking for someone in that age range and that particular look to fill out my range."
        v "You know, the milfy kind of look."
        p "Hey, that's my [mr] you're talking about!"
        scene ae-79
        v "Come on bro, let's be objective here. We both know this."
        p "...I guess."
        scene ae-80
        v "It's a bit of a risk for me, but considering that Amanda already has modelling experience..."
        v "How about featuring her as an upcoming model at our runway show coming up?"
        p "Wow, like with other models?"
        v "Yeah sure. She doesn't have to be as professional, or as well practised as the rest of them."
        v "She can just come in at the end."
        p "Wow, this wasn't what I was expecting."
        p "This is fantastic, super!"
        p "Thanks so much Vincent. You've helped me again!"
        scene ae-81
        v "It's a win-win situation. People like Amanda are actually in high demand. There aren't many people at that age with looks as good as hers."
        v "Clothes need models to sell. You think 20 year olds have a lot of money to spend?"
        v "Mate, middle aged customers is where the business is at."
        v "I think Amanda can slot in there just fine."
        p "She will be so happy to hear that."
        p "For some reason, her modelling agency have been cutting her number of photoshoots."
        v "Yeah they don't know talent when they see it."
        p "She did mention they were just a small studio."
        p "When is this show?"
        v "It's in few days actually, so it's good that we caught up."
        p "Okay, where and when should we go?"
        scene ae-80
        v "Go and have a chat with your [mr], then come by Dante Studios. It's where I'm at."
        p "Anything instructions I should give her?"
        v "All she has to do is walk up at the end. I'll give her a briefing before it starts."
        v "The theme of the show is 'Witches', by the way."
        p "Awesome, I'll let her know."
        scene ae-78
        v "Anything else buddy?"
        p "It's a lot to process, but we'll do our best!"
        v "I'm just glad to help."
        v "I'm going back to work now, I'll see you a few days."
        p "Thanks again, Vincent."
        $ amandalvl += 1
        $ amandatalk = day
        call daykeep from _call_daykeep_6
        jump map
    if amandalvl == 10 and amandakitchenlvl == 10 and day > amandatalk:
        scene black
        scene a-2 with fade
        play music "sounds/masked.mp3" fadeout 1
        p "This is the big day, [mr]."
        p "You're going on the runway."
        scene a-1
        m "I know, [p], I know!"
        scene a-6 with dissolve
        m "And none of this would have happened without you."
        m "Oh you, I'm such a lucky woman."
        p "Anything for you, [mr]. You know that."
        scene a-8 with dissolve
        m "(It's been so long since I've been able to just put myself into someone else's care...)"
        m "(I've forgotten how it feels to have such a strong, attractive man by my side.)"
        m "(...and he's right here, just for me.)"
        p "Are you alright, [mr]?"
        scene a-13 with dissolve
        m "..."
        m "I want to thank you, for everything you've done. I want to thank you, in a different way."
        scene a-14 with dissolve
        $ renpy.pause ()
        scene a-15 with dissolve
        "She leant in to kiss me, and so I kissed her back."
        "But this time, she wanted more."
        scene a-12 with dissolve
        m "Mmmm~"
        p "I-"
        "I reciprocated."
        "It was a kiss that only lovers could share."
        scene a-15 with dissolve
        $ renpy.pause ()
        scene a-14 with dissolve
        m "..."
        p "...[mr], I-"
        scene a-13 with dissolve
        m "Shhh..."
        m "I think we both learnt a little more about each other."
        p "I..."
        m "We have to go now, [p]."
        m "Let's... continue this after the whole show~"
        scene black with fade
        "And so we left with our hearts still trembling in our chests."
        "Neither knew how to proceed."
        "And so we contined, suspending our impulses."
        "For the time being."
        scene future with flash
        play music "sounds/cyberpunk.mp3"
        x "But you will fall to depravity."
        "If this is what it means to fall, then let me fall."
        x "You've already fallen far."
        "You don't understand. How could you?"
        "My wings are unfurled and I'm flying."
        "Let me fly closer to the sun."
        x "You will fly higher only to fall farther."
        x "When you fall, are you able to get back up?"
        play music "sounds/masked.mp3"
        scene a-3 with hpunch
        m "[p]?"
        "Who am I?"
        scene a-2
        m "Daydreaming?"
        p "Sorry, [mr], I... spaced out for a moment."
        p "Did-did we... what were we doing just now?"
        scene a-1
        m "Doing what?"
        scene a-2 with dissolve
        m "As I was saying, none of this would have happened without you."
        p "...Anything for you, [mr]."
        m "It's time to go now, the show's waiting for us!"
        jump runway




    scene a-1
    p "Looking good [mr]!"
    scene a-6 with dissolve
    m "Like I said, I've still got it!"
    jump amanda_room
