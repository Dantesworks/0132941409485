default studio_intro = False
label studio_lobby: # Vincent
    if studio_intro == False:
        p "Yo, Vincent!"
        v "Hey [p]! Amanda did really well. We already have a few people asking about her."
        v "This might actually do really well. Dante's really happy about the attention she's getting."
        p "That's amazing. I'll pass that on."
        p "Speaking of which, where is she?"
        v "She's got her own room now. All models get one at Dante Studios."
        p "She's a model now? Officially?"
        v "Soon to be. Just a few shoots, and she'll be immortalised as one of Dante's models."
        v "Here, let me show you."
        ## Transition
        v "Hey Amanda, you got a visitor."
        m "[p]!"
        v "Okay, [p], I'm heading back out. Let me know if you need anything."
        p "Hi [mr], that was an awesome photoshoot you had. And wow, look at your office!"
        p "It's like you're a fancy CEO or something."
        m "Yes, Dante treats his models well it looks like."
        p "So what do you use all this space for?"
        m "You know, to change, do some paperwork, whatever that is needed to be done, really."
        m "It's my own place, so I'm told."
        p "What I am saying - that model show was so cool!"
        p "I can't believe it's really my own [mr] on the stage!"
        p "Man this is weird."
        m "Thank you, [p], but I'm just getting started. There's still a lot of legwork to do."
        p "You're going to be one of Dante's models. You're going to be huge."
        m "That's the hope. And it's all thanks to you, [p]."
        p "We're not stopping here, though, [mr]. We can take this even further."
        m "Being a model here is a big deal already, what are you thinking of?"
        p "Becoming your own brand, we could use this to springboard into-"
        x "Amanda, is it alright if we come in?"
        m "Oh yes, please!"
        m "That's Nyx over there and Maya too. They were also at the show, but you probably know that already."
        ny "I see you've got a fan vising already."
        p "Oh hey guys. I saw you guys at the show. Can't believe I'm in the same room as such... beautiful models."
        p "... my name is [p], by the way. In case you wanted to know..."
        ny "We're just paying Amanda a visit."
        ma "Welcoming the new girl. We'll be out soon."
        ny "You know, I could use a fan like you, [p]. How would you feel like a one-on-one fan meet-up with yours truly?"
        ma "I can't believe you, Nyx, you only just met the guy."
        ny "Do you know how many men want to spend just 10 minutes with me? [p]?"
        p "Ermm..."
        ny "How about a double date with me {i}and{/i} Maya. Does that sweeten the deal?"
        m "I don't really..."
        ny "We'd have a lot of fun."
        m "Hey! Stop hitting on him!"
        ny "Hmm?"
        m "He's my-! He's my.... boyfriend!"
        "Oh shit."
        m "(Ah! Why did you say that Amanda!)"
        p "Oh yes, she is my girlfriend. Can't take you up on that offer, sorry Nyx."
        m "He'll be too busy having fun with me instead!"
        m "Lots and lots of fun, right [p]?"
        p "Yes... that's right."
        m "With the experience that only a middle-aged woman can provide."
        ny "..."
        ny "Sorry about that Amanda. I didn't mean to hit on your boyfriend."
        ma "We came in to say hi, and to congratulate you on the show."
        m "Oh, thank you."
        ma "Being a model here is great, I'm sure you'll enjoy it."
        ny "Sorry about intruding on you two. We'll come around again later."
        ma "Take care."
        m "Phew."
        p "Christ, [mr], what was that?"
        m "I don't know, I just didn't feel comfortable with her hitting on you. Maybe it's a protective instinct, or maybe something else..."
        p "We're gonna have to tell them that you said the wrong thing."
        m "No!"
        m "Just... act like a couple around them, okay? I think the image of a married woman doesn't suit a model as much anyway."
        p "Alright, [mr]."
        m "Thank you, [p]. I can always trust you."
        p "So what happens now?"
        m "Paperwork and photoshoots. Standard day of work, to be honest!"
        p "And the occassional modelling show."
        m "That's right."
        p "In that case, I'll leave you to work."
        m "It's for the best. I love you [p]."
        p "Love ya, [mr]."
    call screen studio
    screen studio():
        add "studio"
        imagebutton:
                focus_mask True
                idle "vincent.png"
                hover "vincent_hover.png"
                action Jump("map")
