default studio_intro = False
label studio_lobby: # Vincent
    if renpy.music.get_playing() != "sounds/want.mp3":
        play music "sounds/want.mp3"
    show screen map_icon
    show screen daytime
    show screen phone_icon
    hide screen fastforward
    call screen studio
    screen studio():
        add "studio"
        imagebutton:
                focus_mask True
                idle "vincent.png"
                hover "vincent_hover.png"
                action Jump("vincent_studio")
label studio_intro:
    scene a-16
    p "Yo, Vincent!"
    scene a-17 with dissolve
    v "Hey [p]! Amanda did really well. We already have a few people asking about her."
    v "This might actually do really well. Dante's really happy about the attention she's getting."
    p "That's amazing. I'll pass that on."
    p "Speaking of which, where is she?"
    scene a-18 with dissolve
    v "She's got her own room now. All models get one at Dante Studios."
    p "She's a model now? Officially?"
    scene a-19 with dissolve
    v "Soon to be. Just a few shoots, and she'll be immortalised as one of Dante's models."
    v "Here, let me show you."
    ## Transition
    scene black with fade
    scene a-20 with fade
    v "Hey Amanda, you got a visitor."
    scene a-21 with hpunch
    play music "sounds/wisteria.mp3" fadeout 1
    m "[p]!"
    scene a-22 with dissolve
    v "Okay, [p], I'm heading back out. Let me know if you need anything."
    scene a-23 with dissolve
    $ renpy.pause()
    scene a-24 with dissolve
    p "Hi [mr], that was an awesome photoshoot you had. And wow, look at your office!"
    scene a-25 with dissolve
    $ renpy.pause()
    scene a-26 with dissolve
    $ renpy.pause()
    scene a-27 with dissolve
    $ renpy.pause()
    p "It's like you're a fancy CEO or something. Christ, look at this view!"
    scene a-28 with dissolve
    m "Yes, Dante treats his models well it looks like."
    p "So what do you use all this space for?"
    scene a-29 with dissolve
    m "You know, to change, do some paperwork, whatever that is needed to be done, really."
    m "It's my own place, so I'm told."
    scene a-30 with dissolve
    p "What I am saying - that model show was so cool!"
    p "I can't believe it's really my own [mr] on the stage!"
    scene a-31 with hpunch
    p "Man this is weird."
    scene a-32 with dissolve
    m "Thank you, [p], but I'm just getting started. There's still a lot of legwork to do."
    p "You're going to be one of Dante's models. You're going to be huge."
    m "That's the hope. And it's all thanks to you, [p]."
    p "We're not stopping here, though, [mr]. We can take this even further."
    scene a-33 with dissolve
    m "Being a model here is a big deal already, what are you thinking of?"
    p "Becoming your own brand, we could use this to springboard into-"
    scene a-34 with hpunch
    x "Amanda, is it alright if we come in?"
    scene a-35 with dissolve
    m "Oh yes, please!"
    play music "sounds/witch.mp3"
    scene a-68:
        pos (0.0, -1.64)
        linear 6 pos (0.0, 0.0)
    $ renpy.pause(6.0,hard=True)
    $ renpy.pause ()
    scene a-36 with dissolve
    m "That's Nyx over there and Maya too. They were also at the show, but you probably know that already."
    scene a-37 with dissolve
    ny "Hello Amanda, I see you've got a fan visiting already."
    scene a-38 with dissolve
    p "Oh hey guys. I saw you guys at the show. Can't believe I'm in the same room as such... beautiful models."
    scene a-39 with dissolve
    p "... my name is [p], by the way. In case you wanted to know..."
    scene a-40 with dissolve
    ny "We're just paying Amanda a visit."
    scene a-41 with dissolve
    ma "Nyx and I are welcoming the new girl. Just saying hi and then we'll... leave you two alone."
    scene a-43 with dissolve
    ny "I'm so happy for you Amanda, to have a fan so quickly already. [p], wasn't it?"
    ny "You know, I appreciate true and dedicated fans like you, [p]. How would you feel about a one-on-one fan meet-up with yours truly?"
    ny "I'm sure Amanda won't mind sharing."
    scene a-42 with dissolve
    p "Ahehehehe..."
    ma "I can't believe you, Nyx, you only just met the guy."
    scene a-43 with dissolve
    ny "Do you know how many men want to spend just 10 minutes with me? [p]?"
    scene a-44 with dissolve
    "Aww man..."
    ny "How about a double date with me {i}and{/i} Maya. Does that sweeten the deal?"
    m "I don't really..."
    scene a-45 with dissolve
    ma "Nyx.."
    scene a-46 with dissolve
    ny "We'd have a lot of fun."
    scene a-47 with vpunch
    m "Hey! Stop hitting on him!"
    ny "Hmm?"
    m "He's my-! He's my..."
    scene a-48 with dissolve
    m "...boyfriend..."
    scene a-49 with dissolve
    "Oh shit."
    scene a-50 with dissolve
    m "(Ah! Why did you say that Amanda!)"
    scene a-51 with dissolve
    p "Oh yes, she is my girlfriend. Can't take you up on that offer, sorry Nyx."
    scene a-52 with hpunch
    m "He'll be too busy having fun with me instead!"
    m "Lots and lots of fun..."
    scene a-53 with dissolve
    m "...right [p]?"
    p "Yes... that's right."
    scene a-54 with hpunch
    m "With the experience that only a middle-aged woman can provide!"
    scene a-55 with dissolve
    ny "..."
    ny "Sorry about that Amanda. I didn't mean to hit on your boyfriend."
    scene a-56 with dissolve
    ma "We came in to say hi, and to congratulate you on the show."
    m "Oh... thank you."
    ma "Being a model here is great, I'm sure you'll enjoy it."
    scene a-57 with dissolve
    ny "Sorry about intruding on you two. We'll come around again later."
    ma "Take care."
    scene a-58 with dissolve
    play music "sounds/wisteria.mp3" fadeout 1
    m "Phew."
    scene a-59 with dissolve
    p "Christ, [mr], what was that?"
    scene a-60 with dissolve
    m "I don't know, I just didn't feel comfortable with her hitting on you. Maybe it's a protective instinct, or maybe something else..."
    p "We're gonna have to tell them that you said the wrong thing."
    scene a-61 with dissolve
    m "No!"
    scene a-62 with dissolve
    m "..."
    scene a-63 with dissolve
    m "Just... act like a couple around them, okay? I think the image of a married woman doesn't suit a model as much anyway. Please."
    scene a-64 with dissolve
    p "Alright, [mr]."
    m "Thank you, [p]. I can always trust you."
    scene a-65 with dissolve
    p "So what happens now?"
    scene a-67 with dissolve
    m "Paperwork and photoshoots. Standard day of work, to be honest!"
    p "And the occassional modelling show."
    m "That's right."
    p "In that case, I'll leave you to work."
    scene a-66 with dissolve
    m "It's for the best. I love you [p]."
    p "Love ya, [mr]."
    # Transition
    scene black
    scene a-17 with fade
    play music "sounds/wistful.mp3" fadeout 1
    v "Enjoy the tour, [p]?"
    p "Great place you got here."
    p "Not a bad place to work in. Is there anyway I can help?"
    scene a-19_1 with dissolve
    v "Help? Hmm..."
    scene a-19 with dissolve
    v "Well there's always photoshoots you can look at doing."
    v "You any good?"
    p "It's a skill I'm building up over time. I mean, you saw the shots of [mr] right?"
    scene a-18 with dissolve
    v "Oh, that's right. So there is some talent there, aye?"
    v "Get back to me in a bit, I'll see what I can do for you."
    $ studio_intro = True
    jump studio_lobby
