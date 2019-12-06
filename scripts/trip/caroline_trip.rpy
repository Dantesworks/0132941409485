label caroline_trip:
    scene v324 with fade
    p "Aww, oh man. Last night was a wreck."
    p "I must have slept like a baby."
    scene v325 with dissolve
    p "Hey [mr]. Some day yesterday, huh?"
    scene v326 with dissolve
    p "Um, [mr]?"
    scene v327 with dissolve
    "Where is she?!"
    "Hey, is this a note?"
    scene letter2 with fade
    # Letter
    $ renpy.pause()
    scene v328 with dissolve
    p "Oh wow, I got ditched!"
    scene v329 with dissolve
    "What am I going to do now? When are they coming back?"
    scene v330 with dissolve
    "..."
    "This place is a tourist destination, but it was also the place where I studied before I lost everything."
    "Should I revisit my past, and go back to my university?"
    scene v331 with dissolve
    "Maybe now with the girls gone, it'll be a good time to face my past."
    scene black with fade
    "A few minutes later..."
    scene v332 with fade
    play music "sounds/hamilton.mp3"
    "In a way, this is the place where it all began."
    "I guess it wasn't too long ago, was it?"
    "This is my university, and I had some good times here."
    "But also..."
    scene v333 with dissolve
    "My university, where I broke down, and where Vincent found me. What would have happened had he not found me?"
    "I was sitting on that bench, right there."
    scene v334 with dissolve
    "Right there...?"
    "Hang on, is that-?"
    scene v335 with hpunch
    play music "sounds/san.mp3" fadeout 1
    p "C-Caroline?"
    # Caroline turning around
    scene v337 with dissolve
    $ renpy.pause()
    scene v338 with dissolve
    $ renpy.pause()
    scene v339 with dissolve
    $ renpy.pause()
    scene v340 with dissolve
    c "[p]? Is that you?"
    p "It {i}is{/i} you, Caroline! What are you doing here?"
    c "I could ask you the same thing!"
    scene v341 with dissolve
    p "I, uh... you got a moment?"
    p "Y-You mind if I take a seat?"
    scene v342 with dissolve
    c "If you like."
    scene v343 with fade
    p "When you said you were going on a trip, I didn't think you were going to come here."
    c "Well... here I am."
    p "Crazy, huh?"
    c "It's strange."
    scene v344 with dissolve
    p "..."
    p "Oh yeah, I, well, I saw you there, and just thought I'd say hi."
    scene v345 with dissolve
    c "You caught me a little off guard!"
    c "But thank you, [p]. I appreciate it."
    p "So uh, what are you doing here?"
    scene v346 with dissolve
    c "Here?"
    p "Yeah, at this university. I didn't think you went to medschool here."
    scene v347 with dissolve
    c "Oh no, I don't attend school here."
    p "Yeah, I didn't think so. So how come you're here?"
    scene v348 with dissolve
    c "Oh right. Yes."
    scene v349 with dissolve
    c "The professor with whom I'm doing research with works here."
    p "Ah, you did mention something about an academic trip."
    scene v350 with dissolve
    c "Yes. This would be it."
    p "So... is the research working out well?"
    scene v351 with dissolve
    c "It's... coming along."
    c "It's a bit of work, I'm afraid! I'm just taking a bit of a break now."
    p "Have to get back to work again soon, huh? You're busy as always."
    scene v352 with dissolve
    c "Unfortunately, that seems to be the case a lot of the time."
    p "More work later in the afternoon?"
    c "I'm afraid so."
    scene v353 with vpunch
    p "Hey listen!!"
    p "You've got to give yourself a break."
    scene v354 with dissolve
    c "A-A break?"
    p "I've got a much really good idea."
    p "How about a cup of coffee?"
    # caroline smiles
    scene v355 with dissolve
    $ renpy.pause()
    scene v356 with dissolve
    $ renpy.pause()
    scene v357 with dissolve
    c "Coffee?"
    p "Yeah, a coffee. On me."
    scene v358 with dissolve
    c "..."
    scene v359 with dissolve
    c "I'd love to. You certainly know my weakness, [p]."
    c "It would be my pleasure."
    play music "sounds/yu.mp3" fadeout 1
    scene v360 with flash
    $ renpy.pause()
    scene v361 with dissolve
    p "It's been a while, Caroline."
    scene v362 with dissolve
    $ renpy.pause()
    scene v363 with dissolve
    c "Yes, [p], it has."
    scene black with fade
    # SAVE BEFORE THIS
    default teleport = False
    $ teleport = True
    label teleporter:
        scene splash_nicole with fade
        stop music fadeout 1
        d "Make your save before this point!"
        d "This is as far as we go for the trip update for 0.55 so far."
        d "Coming up are a some Nicole X Kaira fun, and a meeting with our dear Caroline, voted for by patrons before."
        d "Here are just some more events that may come up! Vote for them on patreon :)"
        scene v65 with fade
        $ renpy.pause()
        d "Heading to the shops with the girls!"
        scene v66 with fade
        $ renpy.pause()
        d "Hit the casino and look the part!"
        scene v67 with fade
        $ renpy.pause()
        d "XXX action with Nicole and Kaira!"
        scene v69 with fade
        $ renpy.pause()
        d "Have a ball!"
        scene p21 with fade
        d "To be continued next time..."
        d "Thank you for playing!"
        scene black with fade
        d "Oh yeah, quick heads up..."
        scene merch with fade
        d "Merch is available!"
        scene merch
        $ renpy.pause()
        scene merch2 with fade
        $ renpy.pause()
        scene merch3 with fade
        d "The Art of Depravity, a 54 page book with character descriptions and character art is also on special. Come check it out!"
        scene merch3
        $ renpy.pause()
        scene black with fade
        d "Now is a chance to hack your way back to the map if there are some side character content you would like to do."
        d "Make sure to not touch anything else and return via the hacks menu in computer!"
        menu:
            "Go to the map":
                jump map
            "End game":
                $ renpy.full_restart()
