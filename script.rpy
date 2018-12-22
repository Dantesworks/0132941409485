label base:

    d "I hope you're enjoying your sleep!"
    d "Just before you wake up, I've got a few questions for you..."
    d "Did you knock on Kaira's door, or did you just walk in?"
    menu dep1:
        "I knocked":
            $ depravity = 0
            d "How polite!"
        "I didn't knock":
            $ depravity = 1
            d "Bold!"

    d "Did you hug Kaira before you went shopping with her?"
    menu dep2:
        "I left for shopping straight away.":
            d "And here I thought you hated shopping."

        "I said I had something to do first.":
            $ depravity -= 1
            d "Wholesome."
    d "And finally, did you tell Kaira you thought she was sexy, or cute?"
    menu dep3:
        "I said she was sexy.":
            d "You've done well."
            $ depravity += 1
        "I said she was cute.":
            d "Good job."

    p "Why are you asking me these questions?"
    d "Choices always have consequences, but it's time for you to wake up now!"

    #Amanda wakes up player Chapter 11

    m "(I still can't believe I saw [p] having sex last night.)"
    m "(I could barely go to sleep after that...)"
    m "(I'm sure Nicole saw me, but she continued to ride him anyway!"
    m "(Did she know how much I've been missing out on it? Was she goading me on?"
    m "(What should I say when I see him?)"
    m "(Should I pretend I never saw it or-)"
    p "Eurghh..."
    m "!!"
    m "(It's so big!)"
    p "Oh hey [mr]."
    p "..."
    p "!!"
    p "OH SHIT!"
    p "Aahah [mr]! What are you doing here?"
    m "I was going to the kitchen to get something to eat!"
    m "Why are you naked?"
    p "Uh, um... I know it looks weeird but I was.."
    p "...Sleep walking!"
    m "Sleep walking?"
    m "(Hmm, should I keep pressing him?)"
    p "Yeah, took off all my clothes for some reason, and walked-"
    p "Anyway [mr], jesus give me a 2 minutes alright, I'll put something on!"
    m "It sounds like you've been having issues with your sleep, [p]."
    m "Need me to tuck you in to bed?"
    p "Can we continue this after I've covered myself up?!"
    m "Don't be shy, [p], it's nothing your [mr] hasn't seen before!"
    m "(My boy is all grown up!)"
    m "(Maybe I can finally move on now, and find a man for myself.)"

    scene living_room_idle with fade
    "Ahh, finally done."
    "I should probably head to [mr]'s room and try explain myself a bit better."

    play music "sounds/heart.mp3" fadeout 1
    jump living_room
