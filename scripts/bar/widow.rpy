label widow:
    call hidescreens from _call_hidescreens_11
    scene black
    scene w-5 with fade
    p "Widowmaker?!"
    p "God damn, Caroline wasn't lying when she said VIPs come here."
    scene w-2 with dissolve
    w "A gentleman would introduce himself."
    p "My bad Miss Widowmaker, my name's [p]."
    w "What a foolish name."
    p "Hey!"
    scene w-6 with dissolve
    p "Look, I get it- I'm sorry to disturb you, but I'm a huge fan."
    p "I play Overwatch all the time. I didn't know you were a real thing!"
    scene w-3 with dissolve
    w "{i}Thing?{/i} I am no thing, I am Widowmaker."
    w "Go be a fly somewhere else, oui? Unless you want this spider to eat you."
    scene black with fade
    "Jesus christ she is one cold bitch."
    "I should probably buy her a drink, and maybe she'll warm up to me."
    scene cb-1 with fade
    p "Hey Caroline, I'm looking for a drink."
    scene cb-8 with dissolve
    c "What are you thinking of?"
    p "Anything special?"
    scene cb-5 with dissolve
    c "Hmmm..."
    scene cb-6 with dissolve
    c "How about the Original Dante, that's always special!"
    p "Is it popular?"
    c "Extremely!"
    p "Lovely, I'll take one."
    c "Just a moment~"
    "..."
    scene cb-9 with dissolve
    c "Enjoy the drink!"
    scene cb-1 with dissolve
    p "I hope she will."
    scene cb-3
    c "Sorry?"
    p "Ahem, nothing..."
    scene black with fade
    scene w-1 with fade
    p "Miss Widowmaker, I think we got off on the wrong foot."
    p "Why don't we start again over a drink? This one is called the Original Dante. They say it's really good."
    scene w-2
    w "Une dame se doit d'accepter un verre."
    p "..."
    p "Again?"
    scene w-4
    w "It means, little fly, that I will have your drink."
    p "Thank you."
    p "I mean, you're welcome."
    scene w-5 with fade
    w "You know I am Widowmaker."
    p "Of course, I'm a big fan. I've also like to find out more about you."
    p "You're a very interesting person."
    scene w-3
    w "Oooh?"
    w "You wish to know more about moi?"
    w "I'll give you three questions."
    "Shit."
    p "Okay, let me see..."
    scene w-6 with dissolve
    menu widowask:
        "So, Pharah or Mercy?":
            $ widowask1 = True
            scene w-5
            w "I do not understand your question."
            p "Like, if you had to pick one, which one would it be?"
            w "To kill?"
            p "Not exactly. You know what? Never mind."
        "Are you blue coz' your suit is too tight?":
            scene w-5
            w "I have no problem breathing, but you may if you continue this sort of questioning."
            p "..."
            p "So, guess suit's not too tight after all."
            $ widowask2 = True
    if widowask1 and widowask2:
        jump widowaskdone
    else:
        scene w-6
        jump widowask
label widowaskdone:
    scene w-2 with dissolve
    w "Pourquoi tu me demande une chose si stupide? Crétin!"
    w "Why must you ask such unsophisticated questions?"
    p "I was trying to be funny, I'm sorry!"
    p "I'll ask a serious question now, I promise."
    w "Go, before I change my mind."
    p "..."
    scene w-5 with dissolve
    p "So, did you know that it was Sombra that spoiled your plans to assassinate Volskaya?"
    p "I mean, I saw the whole thing, she-"
    scene w-7 with hpunch
    w "!!"
    w "How do you know that!"
    scene w-8 with vpunch
    w "That is top secret information known to Talon operatives only!"
    w "I should kill you for knowing that information."
    p "Whoa, hang on!"
    p "You can't kill me, there are witnesses everywhere! Besides, it's hardly a secret is it?"
    w "Nobody else must know, you must keep it a secret!"
    w "If Overwatch becomes aware of this it will get back to Talon and it will be the end of me."
    p "Huh."
    p "I won't tell anyone, but I need something in return."
    scene w-9
    w "I don't have money to give you, so forget it."
    p "It's not money I want."
    w "Then what is it?"
    p "It's something that I know you can give me."
    p "I... think you know what that is."
    scene w-10
    w "You dog you-"
    w "You despicable man!"
    p "What's wrong?"
    p "You make me happy, I make you happy. Sounds reasonable to me."
    scene w-11 with dissolve
    w "But, why?"
    p "I just want to be happy. Try your best to make me happy, and let's see if it's enough."
    scene w-12 with dissolve
    w "...only if you keep it a secret, and you must tell me how you know afterwards!"
    p "I'll do that if you do a good job."
    p "Now let's go to the bathroom and you can show me whether you're more than just a pretty face."
    scene w-10
    w "Va te faire enculer!"
    p "Haha, alright. We'll see if you can still talk when your mouth's full."
    ## transition
    scene w-13 with fade
    w "You should know, I'm only doing this for the sake of Talon."
    w "You will tell me afterwards how you found the information, yes?"
    scene w-14 with dissolve
    p "At the rate you're talking, you'll never find out."
    p "Come here, I've been dreaming of this moment for a long time."
    scene w-15
    w "You blackmailing dog... how many have you done this to?"
    p "Blackmail? Don't make me laugh. You want this, don't you?"
    scene w-16
    w "Let's just get this over with, I'm only doing this for intelligence."
    p "Whatever you say, but when this ends is up to you."
    scene w-17 with dissolve
    p "Don't try to hide it now. You're wondering what's inside these pants, aren't you?"
    p "Now come here and warm up my dick, you slut."
    scene w-18 with dissolve
    w "I... in my mouth?"
    p "Well it ain't gone suck itself."
    scene w-19 with dissolve
    w "..."
    scene w-20 with dissolve
    p "On your knees."
    scene w-21 with dissolve
    w "I hate you."
    p "You will love me by the end of our time together, Amelie."
    p "Now come on, I'm not doing your work for you."
    p "Now Lick the tip."
    scene
    $ renpy.movie_cutscene("animations/w1.mpg", loops=-1, stop_music=False)
    scene w-22
    p "Good girl."
    p "Now take me in."
    scene w-23 with dissolve
    w "..."
    w "(Just do it Amelie, think of it as my mission...)"
    scene
    $ renpy.movie_cutscene("animations/w2.mpg", loops=-1, stop_music=False)
    scene w-24
    "Shit, she's really good. I might not last too long at this rate!"
    p "Stop!"
    scene w-25 with dissolve
    w "Are you finished? Will you tell me how you have the intel now?"
    p "You think this is over? We haven't even started yet."
    scene w-26
    p "Has your frigid little ass forgotten how a man finishes?"
    scene w-28
    w "What else must I do!"
    scene w-27
    p "Stand up bitch."
    p "Now."
    w "..."
    scene w-29 with dissolve
    w "What will you do with me...?"
    p "Expose your breasts."
    w "..."
    scene w-30 with dissolve
    $ renpy.pause()
    "Look at those perky puppies."
    scene w-31
    w "Are you happy? Does this bring you joy?!"
    scene w-32
    p "Look at how stiff your nipples are."
    p "You're enjoying this more than you're showing."
    scene w-33 with dissolve
    p "I'll be happy once you work those fine hips of yours, Amelie. You know what to do."
    w "(I have no choice, he's forcing me!)"
    scene w-34 with dissolve
    p "Not as frigid as you make yourself seem, huh?"
    p "Straddle me and enjoy the ride."
    w "This will give me no pleasure!"
    scene
    $ renpy.movie_cutscene("animations/w3.mpg", loops=0, stop_music=False)
    scene w-36
    w "It's so big- you're filling me up~"
    p "I slid right into you, slut. Start bouncing you whore."
    scene
    $ renpy.movie_cutscene("animations/w4.mpg", loops=-1, stop_music=False)
    scene w-37
    p "You're coming around, good girl!"
    p "What a natural."
    w "This isn't...I feel... please. Let me stop."
    p "What's this Amelie? Are you close to the edge?"
    p "You've already come so far, keep rocking."
    scene
    $ renpy.movie_cutscene("animations/w4.mpg", loops=-1, stop_music=False)
    scene w-36
    w "...I can't...."
    w "Unghh!"
    scene
    $ renpy.movie_cutscene("animations/w5.mpg", loops=0, stop_music=False)
    scene w-38
    w "Ahhhh~~~~!"
    "Damn, she came."
    scene w-40 with dissolve
    p "Looks like you finished before me, slut."
    scene w-39 with dissolve
    p "You whole body is quivering, you're out for the count. Shame."
    scene w-41
    w "You... must keep it a secret. Tell me now, how did you find... the intel...?"
    p "I'm not telling you anything Amelie. You've cum like a brainless bimbo and left me dry."
    p "A selfish woman like you will have to make it up to me."
    p "I'll see you another time."
    scene w-42 with hpunch
    w "Wait, noo!"
    w "Please!"
    p "Stay beautiful bitch."
    $ widowlvl += 1
    jump barside


default widowlvl = 1
default widowask1 = False
default widowask2 = False
