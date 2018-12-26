label base:
    scene future with flash
    play music "sounds/cyberpunk.mp3" fadeout 1
    x "Hello [p]."
    x "I'm here because choices have consequences."
    x "What you do or say reveals who you are."
    x "It's now time to take a look at the choices you've made."
    x "Did you knock on Kaira's door, or did you just walk in?"
    menu dep1:
        "I knocked":
            $ depravity = 0
            x "How polite."
        "I didn't knock":
            $ depravity = 1
            x "Bold."

    x "Did you hug Kaira before you went shopping with her?"
    menu dep2:
        "I left for shopping straight away.":
            x "I see."

        "I said I had something to do first.":
            $ depravity -= 1
            x "Wholesome."
    x "And finally, did you tell Kaira you thought she was sexy, or cute?"
    menu dep3:
        "I said she was sexy.":
            x "Very honest."
            $ depravity += 1
        "I said she was cute.":
            x "Good job."

    p "Why are you asking me these questions?"
    x "What you choose to say or do is up to you."
    x "But the consequences always follow."
    x "Your destiny is in your hands."
    p "Wait! You haven't answered my question yet!"
    x "Fear not, human, for we will meet again."
    x "Until then, know that we will be watching with great interest."
    scene black with fade


    #Amanda wakes up player Chapter 11
    play music "sounds/heart.mp3" fadeout 1
    m "(I still can't believe I saw [p] having sex last night.)"
    m "(I could barely go to sleep after that...)"
    m "(I'm sure Nicole saw me, but she continued to ride him anyway!"
    m "(Was she just taunting me?)"
    m "(What should I say when I see him?)"
    m "(Should I pretend I never saw it or-)"
    p "Eurghh..."
    m "!!"
    m "(Oh my god! He's so big!)"
    p "Oh hey [mr]."
    p "..."
    p "!!"
    p "OH SHIT!"
    p "Aahah [mr]! What are you doing here?"
    m "I was going to the kitchen to get something to eat!"
    m "Why are you naked?"
    p "Uh, um... I know it looks weird but I was.."
    p "...Sleep walking!"
    m "Sleep walking?"
    m "(Hmm, should I keep pressing him?)"
    p "Yeah, took off all my clothes for some reason, and walked-"
    p "Anyway [mr], jesus give me a 2 minutes alright, I'll put something on!"
    m "It sounds like you've been having issues with your sleep, [p]."
    m "Need me to tuck you in to bed?"
    p "Can we continue this after I've covered myself up?!"
    m "Don't be shy, [p], it's nothing your [mr] hasn't seen before! fufufu...."
    m "(Oh my, what a shock!)"
    m "(It's normal to feel this way, isn't it? Especially since he has such a-)"
    m "(Oh no, snap yourself out of it Amanda!)"

    scene living_room_idle with fade
    "Ahh, finally done."
    "I should probably head to [mr]'s room and try explain myself a bit better."
    jump living_room
