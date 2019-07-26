# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define gui.dialogue_text_outlines = [ (1, "#000000", 1, 1) ]
define gui.name_text_outlines = [ (1, "#000000", 1, 1) ]
define c = Character("Caroline")
define p = Character("[player]", color="#55B7DC")
define m = Character("Amanda")
define s = Character("Kaira")
define n = Character("Nicole")
define t = Character("Camille")
define ellie = Character("Cafe girl")
define x = Character("???")
define v = Character("Vincent")
define d = Character("Dante")
define a = Character("Announcer")
define g1 = Character("Guest 1")
define g2 = Character("Guest 2")
define wai = Character("Waitress")
define s1 = Character("Woman #1")
define s2 = Character("Woman #2")
define o = Character("Olivia")
define ver = Character("Veronica")
define saf = Character("Saffron")
define ny = Character("Nyx")
define ma = Character("Maya")
define b = Character("Belle")

define w = Character("Widowmaker")
# The game starts here.

label splashscreen:
    $ jingle = renpy.random.randint(1, 3)
    scene black
    if jingle == 1:
        play sound "sounds/effects/1.mp3"
    elif jingle == 2:
        play sound "sounds/effects/2.mp3"
    elif jingle == 3:
        play sound "sounds/effects/3.mp3"
    scene splash3
    with Dissolve(4)

    $ renpy.pause(2.0,hard=False)
    $ renpy.pause()
    d "This is the beta version of the game, and is not intended for public release. Play at your own risk!"

    #call splashlogo

    scene black
    with Dissolve(1)

    scene splash4
    with Dissolve(1)

    $ renpy.pause(2.0,hard=False)
    $ renpy.pause()

    scene black
    with Dissolve(1)

    #scene splash6
    #with Dissolve(1)

    #$ renpy.pause(2.0,hard=False)
    #$ renpy.pause()

    scene splash2
    with Dissolve(1)

    $ renpy.pause(2.0,hard=True)
    $ renpy.pause()

    scene black
    with Dissolve(1)


    return

label start:
    default depravity = 0
    stop music fadeout 1
    "It's the feeling of deja vu. I feel - no, I know I've been here before."
    "All of this feels too... familiar."
    ## All endings are also beginnings. Where one chapter ends, another begins.
    scene quote with dissolve
    $ renpy.pause(2.0, hard = True)
    $ renpy.pause()
    play music "sounds/hamilton.mp3" fadeout 1

    scene 1_v_shocked
    with Dissolve(1)

#Player name

    x "What's going on here?"
    x "You look a bit down there, buddy. Are you alright?"
    x "What's your name, man?"
    $ player = renpy.input("My name?",default="Anon")
    $ player = player.strip()
    if player == "":
        $ player = "Anon"

    #Story start Chapter 1
    scene 1_v_serious with dissolve
    x "Hey [p], why do you look so upset? What's the matter?"
    p "I'm sorry, I really do like a mess, don't I?"
    p "Wave after wave of bad things are happening to me. I can barely deal with them."
    x "There, there."
    x "We all get that sometimes. It happens to all of us buddy, happens to all of us. What's going on, brother?"
    p "..."
    p "I gambled with my fortune. I gambled with many things. And I lost!"
    scene 1_v_shocked with dissolve
    x "What did you lose?" with dissolve
    scene 1_v_serious with dissolve
    p "Remember when bitcoin was booming? It just kept going up and I thought I could ride the wave."
    p "I put a lot of money in. A lot of money in at the top! I-I thought it'd keep going up..."
    p "And now, I've lost everything!"
    p "{i}Fucking{/i} bogs took everything from me!"
    scene 1_v_shocked with dissolve
    x "That's awful!"
    p "I can't pay rent, I can't pay my tuition fees, I've got nothing left!"
    p "I moved away from home just to study, I thought I could be independent, and now I can't even survive anymore!"
    p "Who am I? I'm nobody."
    x "You mentioned home, what about your family? I'm sure they can help?"
    p "F-family? Before I moved, I lived with two others."
    $ mr = renpy.input("The older woman you live at home with is your?",default="landlord")
    $ mr = mr.strip()
    $ mr = mr.lower()
    if mr == "":
        $ mr = "landlord"

    $ sr = renpy.input("The younger woman you live with at home is your?",default="housemate")
    $ sr = sr.strip()
    $ sr = sr.lower()
    if sr == "":
        $ sr = "housemate"

    x "Who are they?"
    p "I've got [mr] and [sr] back at home. Father figure bit the dust many years ago."
    scene 1_v_serious with dissolve
    x "I'm sorry about that."
    p "That's okay, I don't remember much about him anyway."
    x "What about your [mr] and [sr]?"
    p "I moved out years ago...haha. It's been a while."
    scene 1_v_determined with dissolve
    x "I don't know a lot about you buddy, but I know that it's important to have a strong support system to get you back onto your feet. When you lose everything, family is what you need."
    p "..."
    p "Maybe you're right. It might be time to swallow my pride and go back home."
    p "Thank you so much for coming by and sharing an ear."
    p "If you hadn't, I have no idea what I would've done. Who are you, by the way?"
    p "What's your name?"
    x "Oh don't worry about it buddy! I just like being helpful! Doing my good deed of the day, that sort of thing."
    scene 1_v_shit with hpunch
    x "Gosh! I have to get going now, or I'll be late! Goodbye and take care!"
    scene 1_v_gone with dissolve
    p "..."
    p "Bye!... oh he's already gone."
    "I guess he's right though... it might be a little strange going home without having finished my degree yet, but I need to know when I can't manage."
    "Heh... [mr], [sr]... I guess I'll be back sooner than expected."


##Coming home
    play music "sounds/heart.mp3" fadeout 1
    scene 1_entrance1
    with Dissolve(2)
    "The plane ride was hell, and I'm so tired, but I think I'm finally here. Back home."
    "These familiar streets remind me of the old times when I didn't have anything to worry about."
    "I wonder if [mr] or Kaira have changed. Back in school the boys would always talk about how hot [mr] was!"
    "It's so wrong but I'd probably have to agree. It's a pity she hasn't been able to find somebody since dad passed away."
    "Kaira was just a kid when I left, but she's now in her final few years of school."
    "I guess she's would be almost grown up now, wouldn't she?"
    scene 1_entrance2
    "Alright, no more idling around. It's time to say hi."
    "{i}Knock knock{/i}"

## Meeting family Chapter 2

    scene 2_int
    with Dissolve(2)
    p "Hey! It's me, [p], I'm back!"
    p "..."
    p "Is anybody home?"

    play music "sounds/wisteria.mp3" fadeout 1
    m "...[p]?"
    scene 2_int1
    pause .5
    scene 2_int2
    $ renpy.pause(2.0,hard=True)
    m "Is that really you [p]?"
    p "Hey [mr]?"

    scene 2_int3 with dissolve
    m "Oh.. wow you-you've grown so much!"
    p "And you haven't changed at all [mr]."

    scene 2_int4 with dissolve
    m "You've got a silver tongue [p]!"
    p "It's true [mr], you're as beautiful as you've always been."

    scene 2_int5 with dissolve
    m "Oh stop it you!"
    m "So how was your stay away from home? Did my boy find a girlfriend?"
    p "I don't know about the girlfriend part, but I really enjoyed it all [mr], before everything went to shit that is."

    scene 2_int2 with dissolve
    m "[mr] is so sorry to hear that, let me give you a kiss."
    p "Haha, alright [mr]."

    scene 2_int6
    pause .5
    scene 2_int7
    pause 1

    scene 2_int8
    m "Remember, [p], we'll always be here for you."
    p "Haha, I know."
    m "You must be starving [p]! Let me go cook something for you!"
    m "Go say hi to your [sr] in the meantime. She's probably locked up in her room and didn't even hear you come in!"
    p "Sure thing, I'll be looking forward to that meal!"

    scene 2_int9
    "Now... where was my little [sr]'s room again?"

    scene 2_int10
    m "My boy has grown to be such a man."
    m "Oh well, no time to stand around, time to cook some meat!"

    scene 2_int11
    p "I think this is Kaira's room. Should I knock to see if she's there?"

    menu:

        "Knock on the door.":
            jump choice1_yes

        "Don't knock and just go in.":
            jump choice1_no

    label choice1_yes:

        "{i}Knock knock{/i}"
        "..."
        s "Please come in!"

        jump choice1_done

    label choice1_no:

        $ depravity += 1

        jump choice1_done

    label choice1_done:

    play music "sounds/automata.mp3" fadeout 1
    scene 2_int12
    with Dissolve(1)
    p "..."

    scene 2_int13
    s "..."

    scene 2_int14
    p "...hey Kaira I -"

    scene 2_int15
    s "OH MY GOD! WHO ARE YOU!"
    p "Whoa hang on!! It's me, [p], you're my [sr]! Remember me?!"

    scene 2_int16
    s "...[p]?"

    scene 2_int17
    s "..."
    s "You're back!"

    scene 2_int18
    pause 1

    scene 2_int19
    p "Whoa take it easy!"
    s "[p], [p], [p]! You're finally here! Oooh I'm so sorry for shouting at you, I thought you were [mr] coming in and then I saw you and then-"
    p "There, there, take it easy. It's all good!"
    p "I'm happy to see you too."
    s "Sorry I couldn't greet you when you arrived. I was busy with... stuff."
    p "That's alright. What were you doing anyway?"
    s "I was trying on clothes 'coz a lot of them don't fit anymore!"
    p "How come? I thought you had a ton of clothes."
    s "... My bewbies grew a lot bigger [p]. I was wondering when [mr]'s genes would kick in!"
    p "Uh - ah... I see..."
    "Her tits have definitely gotten bigger, and I can feel them push into me right now! Does she know what she's doing?!"

    scene 2_int20
    p "It's good that we can joke about this kind of stuff to each other Kaira."
    s "Oh it's no joke! This is very serious for me [p]."
    p "I think [mr]'s making us some dinner, we should probably check up on that. Wanna come?"
    s "I'll see you there in a bit, let me cover myself up first. Don't want to make [mr] jealous!"
    "Somehow, I think the jealousy goes the other way round..."
    p "Alright Kaira, I'll see you soon."

    scene black
    with fade
    p "Alright [p], you know where the living room is..."
    p "It should be... right here!"

    play music "sounds/heart.mp3" fadeout 1
    scene 2_int21
    with fade
    pause 1

    scene 2_int22
    m "You're here [p]! Come come! I've been waiting."
    m "You need to try this burger I've made!"
    scene 2_int23
    m "You won't find better even in the restaurants! I've used the juiciest meat - oh it's mouth watering, you have to try it!"
    scene 2_int24
    p "Haha, I'm sure it'll be great [mr]! It smells amazing from here."
    m "Sit! Sit! Sit!"
    p "Okay okay!"
    scene 2_int25
    "This burger looks amazing. I can tell [mr] put a lot of effort into this. I'm so lucky to have such a wonderful [mr]."
    p "The burger looks as good as it smells, honestly. I didn't know you had this in you! I don't remember you ever being this fancy!"
    m "You and your silver tongue!"
    m "Go ahead and take a bite! Tell me what you think!"
    p "Alright, here goes."
    scene 2_int26
    "*Omnomnomnom..."
    m "...well?"
    p "It's good [mr], jesus it's great! You really have gotten good. Let me take another bite..."
    scene 2_int27
    m "Fufufu... I'm so happy you think so!"
    m "I bet you regret ever leaving!"
    p "You're right [mr], I should never have left."
    scene 2_int29
    m "So, what's taking your [sr] so long? Wasn't she coming with you?"
    p "I don't know, she said she was trying on her clothes or something."
    p "Something about growing out of them."
    scene 2_int28
    m "Ah-"
    p "Hmm?"
    m "Your [sr] has 'grown' a lot, hasn't she?"
    p "I'm not sure I-"
    scene 2_int29
    m "It's ok [p] hahaha."
    scene 2_int26
    m "I get worried sometimes though. She hasn't experienced something like this before."
    m "When I had my spurt, I faced many struggles that I didn't expect."
    m "You'll be there to help her through it, won't you [p]?"
    "What is [mr] suggesting I do to help Kaira?"
    "I've got no clue..."
    p "I'm not sure exactly what-"
    s "Ahoy!"

    scene 2_int30
    m "Kaira! You've kept us waiting!"
    s "Sorry [mr], I got held up a little bit but the food smells sooooo good!"
    p "You took your time!"
    scene 2_int31 with dissolve
    s "Hey [p]! When the last time the three of us ate together?"
    p "I don't remember, Kaira, but I'm looking forward to it. Come grab a seat."
    scene 2_int32
    pause 1
    scene 2_int33
    s "So tell us [p], what have you been up to?"
    p "Oh you know, I was studying, working, fending for myself that sort of thing."
    scene 2_int34
    s "Was it fun? It must be so exciting living away from home."
    p "Hahaha, yeah it was pretty fun to start with I guess, but you get used to it eventually."
    s "I can't wait to move out -"
    scene 2_int35
    m "Ahem! What about your poor [mr]. I will be so lonely!"
    s "Ahaha, just kidding [mr]!"
    scene 2_int36
    p "But in the end, its a great experience. I'm glad to be back home though, to rest and get my bearings back. You know."
    scene 2_int33
    s "Stay strong [p], I'm on your side! We can take on the whole world together!"
    p "Haha, thanks Kaira. Love you."

    $ menu_flag1 = False
    $ menu_flag2 = False
    scene 2_int47
    menu ask:

        "Hey [mr], what do you get up to these days?":
            jump choice2_m

        "Kaira, how's school treating ya?":
            jump choice2_s

    label choice2_m:

        $ menu_flag1 = True
        scene 2_int39
        m "Hmm, let me think.."
        scene 2_int40
        m "When I'm not cooking for and looking after your [sr] here, I like to dance and watch movies I suppose."
        scene 2_int41
        m "I occasionally work too, but other than that, there's not too much on my plate, so it's good to have you around."
        p "That actually sounds like the perfect life. What kind of job are you working now?"
        scene 2_int42
        m "fufu... you might think I'm joking [p], but I'm actually doing a little bit of modelling!"
        p "Wow [mr], that's amazing! How did you land that gig?"
        scene 2_int41
        m "Oh please it's nothing big. I knew a friend who knew someone in the business. Who even knows how long it'll go for..."
        scene 2_int35
        s "Maybe I should try modelling too, do you think I'll do good?"
        m "Don't get too confident Kaira! Your [mr]'s still got it!"
        p "Yeah [mr] I'm so happy for you."
        scene 2_int38
        jump choice2_done

    label choice2_s:

        $ menu_flag2 = True
        scene 2_int43
        s "Eh, school's alright. I'm glad I'm almost out."
        scene 2_int44
        s "I'm no longer a girl anymore, and I want some more independence. That's why I'm so envious of you."
        scene 2_int35
        m "I can see that Kaira, but one day you might look back and miss your days at school."
        scene 2_int45
        s "Yeah I don't see how that's possible.."
        p "Did you make any good friends?"
        scene 2_int34
        s "I've got a really good friend, her name's Nicole."
        p "How about any good boy friends?"
        scene 2_int44
        s "..."
        scene 2_int42
        m "Oh Kaira, why don't you tell [p] what you told me the other day?"
        scene 2_int44
        s "[mr] I don't even know what you're talking about."
        scene 2_int41
        m "Just teasing you~"
        scene 2_int34
        s "What about you [p]? Did you find any cute girls?"
        scene 2_int46
        p "Aha...ahahah...."
        scene 2_int34
        s "In that case, you should meet Nicole sometime!"
        p "Oh, your school mate?"
        s "Yeah!"


        jump choice2_done

    label choice2_done:
        if not(menu_flag1 and menu_flag2):
            scene 2_int38
            jump ask

    scene 2_int47
    p "It's good to hear you guys are doing well. So what's the plan tomorrow?"
    scene 2_int33
    s "Me and Nicole are going shopping tomorrow morning! You should come join us!"
    scene 2_int42
    m "Shopping? What for?"
    scene 2_int43
    s "For clothes..."
    scene 2_int41
    m "Ah~"
    m "It would be a good idea for you to go [p], it'll be nice for you to spend some time with your [sr]."
    scene 2_int37
    s "Yes [p], come! I think I'm going to go and do a big haul this time, so I'll needing lots of second opinions."
    s "Nicole will be there too!"
    p "Yeah I got it, your friend. Jeez."
    scene 2_int43
    p "..."
    p "Alright I'll go-"
    scene 2_int34
    s "Yippie!"
    p "-but I'm really tired, so I'll have go to bed now if I want to wake up tomorrow."
    scene 2_int48
    m "That's fine, [p]. Goodnight, and sleep tight, and remember to have fun tomorrow!"
    p "Haha alright, goodnight [mr], goodnight Kaira, I'll see you guys tomorrow."

    stop music fadeout 1
    scene 2_int49
    with fade
    "Christ I'm so tired I can barely keep my eyes open."
    "I'm surprised I even made it to the-"
    scene 2_int50
    "zzzzzz..."

    jump day2
