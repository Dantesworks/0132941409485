label base:
    scene future with flash
    play music "sounds/cyberpunk.mp3" fadeout 1
    x "Hello [p]."
    x "I'm here because choices have consequences."
    x "What you do or say reveals to me your inner depravity."
    x "I'll be watching the choices you make."
    x "Now tell me, did you knock on Kaira's door, or did you just walk in?"
    menu:
        "I knocked":
            $ depravity = 0
            x "How polite."
        "I didn't knock":
            $ depravity = 1
            x "Bold."

    x "Did you hug Kaira before you went shopping with her?"
    menu:
        "I left for shopping straight away.":
            x "I see."

        "I said I had something to do first.":
            $ depravity -= 1
            x "Wholesome."
    x "Did you tell Kaira you thought she was sexy, or cute?"
    menu:
        "I said she was sexy.":
            x "Very honest."
            $ depravity += 1
        "I said she was cute.":
            x "Good job."
    x "Finally, did you talk to the red headed girl at the bar, or not?"
    menu:
        "I went ahead and said hi.":
            $ talkcamille = True
        "It was awkward, so I kind of ignored her.":
            $ depravity += 1

    p "Why are you asking me these questions?"
    x "What you choose to say or do is up to you."
    x "But the consequences always follow."
    x "Your destiny is in your hands."
    p "Wait! You haven't answered my question yet!"
    p "If you're already watching, why do you have to ask me these questions?"
    x "Fear not, human, for we will meet again."
    x "Until then, know that we will be watching with great interest."
    scene black with fade


    #Amanda wakes up player Chapter 11
    play music "sounds/heart.mp3" fadeout 1
    scene 11-3 with fade
    m "I still can't believe I saw [p] having sex last night."
    m "I could barely go to sleep after that..."
    scene 11-1
    m "I'm sure Nicole saw me, but she continued to ride him anyway!"
    m "Was she just taunting me?"
    scene 11-2
    m "What should I say when I see him?"
    m "Should I pretend I never saw it or-"
    p "Eurghh..."
    scene 11-4 with dissolve
    m "!!"
    scene 11-5 with dissolve
    $ renpy.pause()
    scene 11-6
    m "(Oh my god! He's so big!)"
    scene 11-7
    p "Oh hey [mr]."
    scene 11-8
    p "..."
    scene 11-9
    p "!!"
    p "OH SHIT!"
    scene 11-10 with dissolve
    p "Aahah [mr]! What are you doing here?"
    scene 11-11
    m "I was going to the kitchen to get something to eat!"
    m "Why are you naked?"
    p "Uh, um... I know it looks weird but I was.."
    p "...Sleep walking!"
    scene 11-12
    m "Sleep walking?"
    m "(Hmm, should I keep pressing him?)"
    p "Yeah, took off all my clothes for some reason, and walked-"
    p "Anyway [mr], jesus give me a 2 minutes alright, I'll put something on!"
    scene 11-13
    m "It sounds like you've been having issues with your sleep, [p]."
    m "Need me to tuck you in to bed?"
    p "Can we continue this after I've covered myself up?!"
    scene 11-14
    m "Don't be shy, [p], it's nothing your [mr] hasn't seen before! fufufu...."
    m "I'll see you later sweetie!"
    scene 11-15 with dissolve
    m "(Oh my, what are these feelings?)"
    m "(I'm so hot down there!)"
    m "(It's like my pussy is just hungering for that large, thick cock.)"
    scene 11-17
    m "(Thrusting in and out, in and out, hngg~)"
    m "(It's normal to feel this way, isn't it? Especially since he has such a- )"
    scene 11-16
    m "(Oh no, snap yourself out of it Amanda!)"
    m "(I need go to to to my room and clear my thoughts...)"

    scene living_room_idle with fade
    "Ahh, finally done."
    "I should probably head to [mr]'s room and try explain myself a bit better."
    d "The free-roaming part of the game has started!"
    d "Access the map in the top right corner in the hallway."
    d "Advance time by sleeping, or by using the fast-forward button on the top left corner of the map."
    d "You will get an automatic quest guide once you get Nicole's phone, so do her quest first if you get stuck."
    d "Some routes are also LOCKED until you get the phone! So get the phone from Nicole first!!"
    d "To do this, talk to Amanda in the morning, Kaira in the afternoon, then you will find Nicole in the living room in the afternoon on the next day."
    d "Nicole's phone will also unlock money making through cryptocurrency investing - be sure to do this in combination with the Bogdanoff Favours in the online shop."
    d "Have fun!"
    "Hmm, how do I make a ton of money again?"
    menu:
        "Use the BCC app on Nicole's phone with Bogdanoff Favours in the online shop":
            d "Correct!"
        "Masturbate in a corner":
            d "Not quite!"
            d "The best way to get filthy rich is to use the BCC app on Nicole's phone with the Bogdanoff favours in the online shop."
    jump living_room
