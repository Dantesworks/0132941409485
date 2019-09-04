default vincent_work = 1
label vincent_studio:
    call hidescreens from _call_hidescreens_16
    scene a-16
    menu:
        "Visit Amanda":
            if studio_intro == False:
                jump studio_intro
            jump amanda_studio
        "Work" if studio_intro:
            if amandalvl == 11 and vincent_work == 1:
                scene a-17 with dissolve
                v "[p]!"
                scene a-16 with dissolve
                v "I was thinking about that work I got for ya."
                v "The pay rate will probably start off on the low side, considering you're a beginner."
                p "That's fine. Slow and steady."
                scene a-18 with dissolve
                v "I'm glad you understand."
                v "Nyx has a photoshoot coming up soon, and we're looking for some close up shots of her face."
                v "Standard close ups. Centre the face, then just click."
                p "Sounds easy enough. I have a camera and lens already."
                scene a-19_1 with dissolve
                v "We're looking for a more specific kind of shot."
                v "You'll need one of those low aperture lens. Hmm, something like 50mm primes."
                p "Yeah, I'll look into that."
                scene a-16 with dissolve
                v "Come talk to me again when you've got the goods."
                $ vincent_work += 1
                jump studio_lobby
            if amandalvl == 11 and vincent_work == 2:
                if primes_50:
                    p "Hey, I got those lens."
                    scene a-19_1 with dissolve
                    v "The 50mm prime lens - also known as the nifty fifty."
                    v "Did you know, [p]? They are reknowned for their versatilty."
                    scene a-18 with dissolve
                    v "Surely, a must-have for all kinds of photographers."
                    p "Cool. Can you tell me more about the next photoshoot?"
                    v "It's with the beautiful Nyx. We need some close shots of the head."
                    p "Just the head?"
                    scene a-16 with dissolve
                    v "Hmm, I'd say collar bones and up. You know?"
                    v "Nyx is experienced at this stuff anyway. She'll let you know what to do, I'm sure."
                    p "Okay, sounds good."
                    scene a-19 with dissolve
                    v "Don't be nervous alright? Haha. It's gonna be fine."
                    p "I can't believe it. I'm about to be the photographer of a famous model."
                    v "Photographer in a very controlled situation with a narrow scope."
                    scene a-18 with dissolve
                    v "Slow and steady, right?"
                    p "Right. I got it."
                    v "Ready? I'll show you the way."
                    stop music fadeout 1
                    scene black with fade
                    v "Just through here mate. The next voice you hear will be Nyx's."
                    p "Jesus Christ this is formal."
                    scene a-69 with fade
                    play music "sounds/witch.mp3" fadeout 1
                    ny "Vincent you're finally here. Let's get this shoot over with."
                    scene a-70 with dissolve
                    ny "..."
                    ny "You're not Vincent."
                    scene a-71 with dissolve
                    p "It's [p]. We've met earlier."
                    scene a-72 with dissolve
                    ny "You're Amanda's boyfriend."
                    p "..."
                    p "That's right. I'm a little new to the job, but I'm also your photographer for today."
                    p "Nice to meet you, hahaha..."
                    scene a-73 with dissolve
                    ny "Really? By the way, won't Amanda be jealous if her boyfriend is photographing other beautiful women?"
                    p "Haha, do you think so?"
                    scene a-74 with dissolve
                    ny "Well after all, she seemed {i}so{/i} protective of you."
                    p "Yeah I can see how it comes across that way. You could almost say like a... motherly instinct."
                    "Oh man, I regret that pun already."
                    ny "In any case, let's start shall we? Usually it's the photographer giving directions, but since you're new..."
                    scene a-75 with dissolve
                    ny "I don't mind having the tables turned a little."
                    p "Thank you for your generosity."
                    scene a-76 with dissolve
                    p "Now let's see..."
                    p "Just uh... look at the camera here..."
                    scene a-77 with flash
                    $ renpy.pause()
                    p "Great shot. Now, what else..."
                    scene a-78 with dissolve
                    ny "I think Vincent gave you an easy shoot by just focusing on the face, front on."
                    ny "But even then, there are variations."
                    ny "Usually you can vary it up a bit by asking the model to change their facial expression."
                    scene a-79 with dissolve
                    ny "How about asking me to put on a more fierce expression?"
                    p "Uhh... such as?"
                    scene a-80 with dissolve
                    ny "Hey Nyx, give me a fierce gaze sharper than glass and a pout that could seduce even women."
                    ny "...like that."
                    p "Okay, sure..."
                    p "Let's try a look so fierce I feel like I'm being stabbed by a thousand daggers."
                    scene a-82 with dissolve
                    ny "Interesting description... let's see."
                    scene a-83 with dissolve
                    $ renpy.pause()
                    scene a-84 with flash
                    $ renpy.pause()
                    p "Great. Now how about biting your lips at the same time?"
                    scene a-85 with dissolve
                    $ renpy.pause()
                    scene a-85 with flash
                    $ renpy.pause()
                    scene a-86 with dissolve
                    p "Great shots! Oh you look so good."
                    ny "A photographer's job is made easier by a good model. This is fun, isn't it?"
                    p "I woulnd't mind doing more."
                    scene a-87 with dissolve
                    ny "There are more chances down the line. Dante's models are not just known for attractiveness, but also sex appeal."
                    ny "If you're into that sort of thing, I'm sure Vincent can arrange it."
                    p "Oh I am!"
                    scene a-88 with dissolve
                    ny "Don't sound {i}too{/i} eager, [p]. Remember Amanda."
                    p "Right."
                    scene a-89 with dissolve
                    ny "Till next time."
                    scene black
                    scene a-17 with fade
                    play music "sounds/want.mp3" fadeout 1
                    v "How was the work?"
                    v "Feeling tired?"
                    p "Hardly man. This stuff is great. Here are the shots."
                    scene a-18 with dissolve
                    v "I'll take a look later, I'm sure they're good."
                    v "Here's the pay for this job. Not too bad, right?"
                    "You have gained $100!"
                    $ cash += 100
                    p "Sweet."
                    scene a-19 with dissolve
                    v "By the way, uh, Nyx. She's really something isn't she?"
                    p "Oh for sure!"
                    scene a-19_1 with dissolve
                    v "Did she, you know, say something about me?"
                    p "Erm. I don't know, was she meant to tell me something?"
                    scene a-19 with dissolve
                    v "Ah mate, never mind, don't worry! Hahaha..."
                    p "..."
                    p "You've got the hots for her haven't you?"
                    scene a-19_2 with hpunch
                    v "Shh! Don't say that around here man."
                    p "What's the matter, bro? There's nothing wrong with that, she's hot."
                    scene a-19_1 with dissolve
                    v "Yeah that may be, but I wouldn't be tangled in her affairs man."
                    v "Hey. You just haven't heard the stories."
                    p "Stories? What stories?"
                    v "A tale for another time."
                    scene a-16 with dissolve
                    v "Come back next time, [p]. See if I can find you more work."
                    scene black with fade
                    $ vincent_work += 1
                    call daykeep from _call_daykeep_33
                    jump map
                else:
                    v "Sorry, [p]. We need those 50mm primes."
                    jump studio_lobby
            if amandalvl == 11 and vincent_work == 3:
                v "Interesting stuff, [p]."
                v "We need a few shots of Maya to go on our website."
                scene a-18 with dissolve
                v "Portrait shots. Nothing too hard."
                p "Does she have to look formal and serious?"
                scene a-17 with dissolve
                v "Erm. Maybe one with a faint smile?"
                v "It's just a passport style picture."
                scene a-19 with dissolve
                v "You're the photographer, [p], use your judgement."
                p "Alright, can do."
                scene a-16 with dissolve
                v "It'll be against a white background. Let me take you to the studio."
                stop music fadeout 1
                scene black with fade
                v "Just here, mate. Good luck!"
                p "Thanks, Vince."
                play music "sounds/pretty.mp3" fadeout 1
                scene a-90 with fade
                p "Hey Maya!"
                scene a-91 with dissolve
                ma "Nyx told me about you, [p]."
                p "Good things?"
                scene a-92 with dissolve
                ma "Haha! Something about being an up and coming photographer for Dante studios?"
                ma "We have a great work culture here. The photographers treat the models well, and vice versa."
                p "Sounds awesome."
                scene a-93 with dissolve
                ma "We're actually looking for a portrait shot of me to go up on the website on the page where the models are listed."
                ma "It'll have a lot of other models up there too, so make sure I stand out!"
                p "I can't imagine that would be difficult for you."
                scene a-94 with dissolve
                ma "Hmm?"
                p "I mean, you have those ears, right? It's a very exotic look."
                p "Are those elf ears, by the way?"
                scene a-95 with dissolve
                ma "Elf ears? Is something the matter with my ears?"
                p "..."
                p "Yeah. Are those like, prosthetics or something?"
                ma "Prosthetics?"
                scene a-97 with dissolve
                p "I mean they're like... pointier than the average person's."
                ma "Oh, I suppose you're right. I've never really thought about it."
                p "So they're not prosthetics...?"
                scene a-95 with dissolve
                ma "I don't think so, I've had them for as long as I remember."
                p "Okay..."
                p "Anyway, that's what I meant when I said they help you stand out."
                ma "Ah, I suppose that makes sense."
                scene a-96 with hpunch
                "This conversation makes no sense."
                scene a-98 with dissolve
                p "I don't know why I brought it up, sorry. Let's continue on, haha."
                p "So, I think just a portrait shot, right?"
                scene a-99 with dissolve
                ma "Yes, but let's also get a little bit creative."
                scene a-100 with dissolve
                ma "Why don't you just start off with a basic shot of me standing still?"
                scene a-98 with flash
                $ renpy.pause()
                p "Alright, done."
                scene a-102 with dissolve
                ma "Did Nyx give you any pointers on how to shoot?"
                p "Yeah, a bit. Let me try out what I learned."
                p "Could you put your hands on your hips?"
                scene a-103 with dissolve
                ma "Like this?"
                scene a-104 with flash
                $ renpy.pause()
                p "Great."
                p "Now kneel down, with your hands above your head."
                scene a-105 with dissolve
                ma "Oh, you're getting creative."
                scene a-106 with dissolve
                $ renpy.pause()
                scene a-107 with flash
                $ renpy.pause()
                scene a-108 with flash
                $ renpy.pause()
                p "Awesome."
                p "Now stick your tongue out and look..."
                scene a-109 with dissolve
                ma "Sexy?"
                scene a-110 with dissolve
                p "Right on."
                scene a-110 with flash
                $ renpy.pause()
                scene a-111 with flash
                $ renpy.pause()
                scene a-112 with dissolve
                p "That's a nice collection. Good job, Maya!"
                ma "Nyx must have taught you quite a bit, I can tell!"
                ma "She usually likes the more suggestive poses and expressions."
                p "And what do you like?"
                scene a-113 with dissolve
                ma "Who knows? I'm an enigma."
                p "You are indeed. Anyway, let me get these shots back to Vincent. I think you'll stand out plenty on that website!"
                # transition
                scene black
                play music "sounds/want.mp3" fadeout 1
                scene a-17 with fade
                v "So, how'd it go?"
                p "It went great! I think Dante will be pleased with these shots. I got a few questions about Maya though."
                p "What is up with her ears?"
                scene a-19_1 with dissolve
                v "Who knows man. All the models are a little strange in their own ways."
                p "We're all a little strange, I feel."
                scene a-19 with dissolve
                v "Oh we all have quirks. Definitely. But we don't have ears twice the normal size now do we?"
                p "What's up with that?"
                scene a-18 with dissolve
                v "I wish I knew. Well, that's probably a lie. But see, it makes her unique and thats one of the things that Dante Studios likes."
                p "Makes sense to me."
                v "Good. Here's your pay."
                $ cash += 100
                "You have gained $100!"
                scene a-17 with dissolve
                v "I've got good news coming your way. At this rate, you might get a job that will pay more. Amanda and the other models are talking about it."
                v "Have a chat to your [mr] tomorrow and she might be able to update you."
                v "As for me? I feel like some ice cream..."
                scene black with fade
                $ vincent_work += 1
                $ amandalvl += 1
                call daykeep from _call_daykeep_34
                jump map
            if amandalvl == 15:
                scene black
                scene a-217 with fade
                v "[p]! I was going to say..."
                v "What the hell was that earlier? Apparently you just left in the middle of a shoot!"
                p "Oh, right. Something important came up, and I had to leave with Amanda."
                p "Sorry about that. Are Maya and Nyx really pissed off?"
                scene a-218 with dissolve
                v "No, not really. They seemed understanding."
                p "Oh really? That's good."
                scene a-219 with dissolve
                v "It might have been because I promised that you'd make it up to them."
                p "How am I gonna make it up to them?"
                v "I don't know. They wanted to talk to you and come to an arrangement. I'll let them handle it."
                scene a-220 with vpunch
                v "Girls!"
                scene a-221 with dissolve
                v "You girls wanted [p]?"
                scene a-222 with dissolve
                ny "That's right. Could you please leave us for a moment, Vincent?"
                scene a-223 with dissolve
                v "What? Getting rid of me already?"
                ny "..."
                v "Aww, okay."
                scene a-224 with dissolve
                $ renpy.pause()
                scene a-225 with dissolve
                p "I'm slightly freaked out. What did you want to chat about?"
                scene a-226 with dissolve
                ma "Nyx?"
                scene a-227 with dissolve
                ny "Fine. I'm sorry for what happened with Amanda earlier. I overstepped my boundaries."
                p "Oh? Haha, I see."
                p "To be honest, I don't mind really, so don't worry about it. Though, probably don't do it again around Amanda."
                p "Anyway, shouldn't you be apologising to Amanda, not me?"
                scene a-228 with dissolve
                ny "..."
                scene a-229 with dissolve
                ny "I've already done so, don't worry. Anyway, as an apology, I wanted to show you something."
                scene a-230 with dissolve
                ma "Oh Nyx, are you really?"
                ny "It'll be fine, Maya."
                p "..."
                play music "sounds/alchemy.mp3" fadeout 1
                scene a-231 with dissolve
                ny "I wanted to give you something to help you out with your relationship. That is, an aphrodisiac."
                p "An aphrodisiac?"
                scene a-232 with dissolve
                ny "Yes. It's a sexual potion. It's going to drive any woman crazy and lusting for cock."
                ny "It's the same thing I use to make Maya more lively."
                scene a-233 with dissolve
                ma "Nyx! You're {i}far{/i} too forward with these kinds of things."
                p "Why are you giving me this?"
                scene a-234 with dissolve
                ny "Why not? A sexually satisfied Amanda would be beneficial for us both. She's far too frustrated at work."
                p "Frustrated?"
                ny "Yeah. Sexually frustrated. She needs a good pounding, [p]. And you need to give it to her."
                scene a-232 with dissolve
                ny "Just ask Maya what a good orgasm can do for your mood."
                ma "..."
                p "..."
                ny "Well, Maya?"
                scene a-235 with dissolve
                ma "It's good for the soul."
                scene a-236 with dissolve
                ny "See [p]? It's something worth considering. Tell me, when was the last time you had sex with Amanda?"
                p "Excuse me?"
                ny "I bet it was ages ago, wasn't it?"
                p "We did it right after the photo shoot, if you really must know!"
                scene a-237 with dissolve
                ny "Really? Did she manage to cum?"
                p "Well to be fair, it was just a handjob, so it's not like I couldn't get her off or anything."
                "At this rate, a handjob might be the last thing I ever get..."
                ny "See? You need to get her off, [p]. Try it out, you'll have her over you in no time."
                "The last thing [mr] said was for me to forget everything that we did togther."
                "If this sex potion stuff does work, how is she going to deal with it?"
                scene a-238 with dissolve
                p "So to be sure, this aphrodisiac is going to make all girls who see my dick horny?"
                ny "Only those around you when you activate it."
                "Bah, this is probably all a scam anyway, and I'll look like an idiot in the end."
                "But still..."
                p "Well, if it's free, I might as try it out. So do you have it on you?"
                scene a-239 with dissolve
                ny "Yes, and I'll show you. But not here. We need to go somewhere private."
                p "..."
                scene a-240 with dissolve
                ma "Just follow us, [p], and indulge Nyx for a bit."
                p "Okay."
                scene black with fade
                # transition
                p "Well?"
                scene a-241 with fade
                ny "It might be a bit cliche, but this stuff comes in a bottle."
                p "The aphrodisiac?"
                ny "Yep."
                scene a-242 with dissolve
                ny "On it's own it is only mildy effective, but once it comes into contact with an erect penis, it activates completely."
                ny "The result? All females who come upon your penis will find themselves in heat."
                scene a-243 with dissolve
                ny "None of us has experienced the full effect yet."
                scene a-244 with dissolve
                ny "That's the theory, anyway."
                p "The theory? You haven't tried this out before? This is 100 percent a dud!"
                ny "No, no, trust me. I've seen it work, I think."
                scene a-245 with dissolve
                p "So this is why I'm your guinea pig, huh? You don't give a damn about my relationship with Amanda. You just need to try this out."
                ny "[p], we want the best for you and Amanda but we also want to try this out."
                scene a-246 with dissolve
                ma "I'm sorry about Nyx, [p], but there's nothing to lose."
                p "I guess that's true. So what are you going to do, slather this over my dick?"
                scene a-247 with dissolve
                ny "Two things. First, it has to be an erect dick. Second, you can slather it on yourself."
                p "What, you won't even do me the courtesy?"
                scene a-248 with dissolve
                ny "Uh, blame Maya - she'll hate me if I touch someone else. Right Maya?"
                scene a-249 with dissolve
                ma "I'll be fine with anything but touching."
                scene a-250 with dissolve
                ny "Oooh, that interesting. Hey [p], looks like I can't masturbate you, but I {i}can{/i} give you a show."
                ny "That's got to be better than nothing, right?"
                "What a fucking tease."
                p "Whatever. Let's do this."
                scene a-251 with dissolve
                ny "Deal. First, slather the lotion into your hand."
                scene a-252 with dissolve
                p "Done."
                scene a-253 with dissolve
                ny "Now, the fun part..."
                scene a-254 with dissolve
                $ renpy.pause()
                scene a-255 with dissolve
                $ renpy.pause()
                scene a-256 with dissolve
                ny "Why don't you start rubbing your cock to me?"
                ny "That's right... starting jerking it as I rub my soft tits.."
                scene a-257 with dissolve
                ny "Yes... just like that."
                p "Oh yeah baby."
                scene a-258 with dissolve
                ny "Jerking to my perfect breasts~"
                scene a-259 with dissolve
                $ renpy.pause()
                ny "Oooh, look at my perky nipples! You like them, don't you?"
                scene a-260 with dissolve
                $ renpy.pause()
                ny "Looks like I'm getting a bit excited too~"
                ny "Hehehee!"
                scene a-261 with dissolve
                ny "As I... glide my hands over my waist..."
                # Maya reaction
                p "{i}Rub rub rub{/i}"
                scene a-262 with dissolve
                ny "Keep going, [p], that's right~"
                ny "Are you hard yet-?"
                "I was hard ten minutes ago, lady!"
                ny "Are you-"
                # turned on
                scene a-263 with vpunch
                ny "Oh?"
                scene a-264 with dissolve
                ny "Maya... I'm feeling... hot~"
                ny "My breath- is- becoming-"
                scene a-265 with dissolve
                ma "M-mine too."
                p "Aww fuck! I'm cumming!"
                # jizz
                scene a-266 with dissolve
                $ renpy.pause()
                scene a-267 with flash
                $ renpy.pause()
                scene a-268 with flash
                $ renpy.pause()
                scene a-269 with dissolve
                ny "The sperm mixed with the aphrodisiac just landed on my skin!"
                scene a-270 with dissolve
                ny "It's making me ten times as horny as before~"
                scene a-271 with dissolve
                p "Well ladies, I've got a refractory period, but it isn't very long."
                p "If you just gimme a-"
                scene a-272 with dissolve
                ma "No, [p]~ There is one application of the aphrodisiac left, take it..."
                ma "Nyx is mine alone~"
                ny "Spread yourself, Maya~!"
                scene a-273 with fade
                p "..."
                ma "Quick, Nyx, put your fingers in me!"
                image m1 = Movie(play="/animations/m1.mp4")
                scene m1 with dissolve
                $ renpy.pause()
                ny "Oh, Maya, you're so cute but today I just want to make you squirm!"
                ma "What is happening to us Nyx, I feel so horny!"
                ny "I'm going to make you cum~!"
                "This is so hot, I can't miss out on this! I want a threesome with two super models!"
                p "So, uh-"
                scene a-274 with hpunch
                ma "Leave!!"
                "Wew!"
                p "Alright, alright! Have your own fun."
                scene black with fade
                "At least I didn't come out of this empty handed. With this lotion, I can seduce [mr]."
                "I should probably wait for [mr] to come home and then apply this to my cock."
                "Yes, that's a good idea."
                $ amandalvl += 1
                jump studio_lobby
            if amandalvl == 17:
                p "Any news about work, Vincent?"
                scene a-19_1 with dissolve
                v "Work? I'll tell you what's a piece of work."
                scene a-19_2 with dissolve
                v "Those two models I swear are nagging me every 2 minutes about whether you're in or not."
                p "Nyx and Maya?"
                scene a-19_1 with dissolve
                v "Yup. How are you so popular with them anyway?"
                p "It's a good question. Though, what do they want?"
                v "Beats me, and as you can tell, they certainly keep it secret from me."
                p "Ah."
                scene a-232 with hpunch
                ny "[p]! How did it go? We have to talk!"
                v "Can I stay here this time? Or will you get me to leave again?"
                ma "You can stay Vincent, because we're going to one of the studios to talk instead."
                scene a-220 with dissolve
                v "Bah."
                ny "It won't be too long, [p], come!"
                # transition
                scene black with fade
                play music "sounds/witch.mp3" fadeout 1
                scene a-275 with fade
                ny "Well? Did it work on Amanda?"
                p "I didn't get a chance to, unfortunately."
                scene a-276 with dissolve
                ny "What?"
                p "I wanted to, but I didn't get to. I'm planning to do it today."
                scene a-277 with dissolve
                ma "That might be for the better."
                p "How come?"
                ma "Remember how horny we were when you left us? That effect is only 100 percent activated when a penis is around."
                ma "But even without a penis present, the sightly weaker effect can still supposedly last weeks to months - until a certain something happens, we learned."
                p "What has to happen for it to go away?"
                scene a-278 with dissolve
                ny "An orgasm."
                ny "Once Maya and I reached her blissful climaxes, our lust rapidly subsided."
                p "Good to know."
                scene a-279 with dissolve
                ma "We're telling you this because we thought it be useful for you to know that once you made Amanda cum, she'll lose that lust."
                p "That's fine. I'll just use more aphrodisiac. You guys got more, right?"
                scene a-280 with dissolve
                ny "..."
                ma "..."
                p "..."
                scene a-281 with dissolve
                ny "That was our last bottle, and also one of the reasons why we wanted to try the full activation before we finally all ran out."
                p "Are you telling me, that if Amanda ever cums, I won't get laid again?"
                scene a-282 with dissolve
                ma "Not necessarily. Only the lustful part that made her seduce you will disappear."
                ma "If she truly has feelings for you, then she should still like you after the artifical lust is gone."
                p "I see."
                scene a-283 with dissolve
                ma "If she doesn't cum, however, then the aphrodisiac will continue to be activated whenever she sees your penis."
                scene a-284 with dissolve
                ny "So don't be in too much of a rush, [p], but do enjoy your treat."
                p "Thanks."
                ny "We've got to get back to work, and I'm sure you've got something you want to do to, isn't that right~?"
                ma "Until next time, [p]."
                p "Seeya."
                scene black with fade
                $ amandalvl += 1
                jump studio_lobby
            if amandallv == 19:
                p "Any work, Vince?"
                v "It's the dynamic duo, Nyx and Maya. They want you in the studio again."
                p "Is this to take a shot, or-?"
                v "Sigh. I don't know man. I wasn't told of any upcoming job. Maybe it's just another one of your secret chats."
                p "It's... not {i}too{/i} big a deal, really. I'll tell you about it one day."
                v "No, no, nope! I'm just working a job here man, any business with them is business I'd rather stay out of!"
                p "They seem like nice girls, why do you think that about them?"
                p "Did they do something to you?"
                v "Don't worry about it, [p]. They're waiting for you."
                p "You'll tell me one day, deal?"
                v "Maybe one day we can tell each other everything, hahaha!"
                scene black with fade
                p "So, you two were waiting here just for me?"
                ny "It's a nice room here, don't you think?"
                ny "Maya and I feel at home right here."
                p "I'm sure you two get up to a lot of kinky stuff here, no doubt."
                ma "Ahem."
                ma "We were... curious about, well... you know."
                menu:
                    "Play dumb":
                        p "About what?"
                        ma "The thing we showed you, you know, with Amanda?"
                        menu:
                            "Play dumber":
                                p "You're gonna have to spell it out."
                                ma "..."
                                ma "The aphrodisiac."
                            "The aphrodisiac?":
                                jump aphro
                    "The aphrodisiac?":
                        jump aphro
                label aphro:
                    p "Oh!!!"
                    p "Haha."
                    p "It worked great. It worked fine, it really turned her on, and, yeah."
                    p "I... felt like a cheat, in a way."
                    ny "No, need, [p], no need! Sometimes people just need a little encouragement."
                    ny "We knew it worked, to be honest. There was really no need for Maya to ask you."
                    p "How did you know?"
                    ny "Well, Amanda has a spring in her step now. She's definitely happier than before, more free."
                    p "You really think so?"
                    ma "Don't feel too bad, [p]. Every relationship needs a stimulus every now and again."
                    ny "We would know, wouldn't we, Maya?"
                    ma "..."
                    ma "I mean, have some faith in yourself, [p]. The aphrodisiac just lowered her inhibitions."
                    ma "She had sex with you because she wanted to."
                    ny "That's true. We didn't just fuck you when you slapped that sex paste on, did we?"
                    ny "We fucked each other."
                    ma "Nyx..!"
                    p "So you didn't fuck me because you didn't like me... but Amanda did?"
                    ma "There's something deeper beneath it all."
                    p "Thanks guys. But, I feel like there's a catch somewhere. Why are you guys so helpful?"
                    ny "Didn't we say already? A happy Amanda is a happy Nyx and Maya."
                    p "Is it just that?"
                    ma "You think too much of ulterior motivations, [p]. Just run with it!"
                    ny "Hear, hear! Believe in the good of this world, [p]."
                    p "You two must be two very good samaritans."
                    ny "You could say we live a sinful life, but when there's a chance to, you know, redeem things..."
                    ma "To do the good deed of the day, for example."
                    ny "That's where we're coming from."
                    p "Vincent's said something like that before, doing the good deed of the day."
                    p "So, what should I do next?"
                    ma "No doubt Amanda is confused about a lot of things, including those feelings that overwhelmed her."
                    ma "Maybe go talk to her, and smooth it all over."
                    ma "If the use of the aphrodisiac was depraved, then consider this the redemption."
                    p "Sounds... reasonable."
                    p "Thanks for that. What are you two up to in the meantime?"
                    ny "Trying out more sexy lingerie, maybe."
                    ny "When we're ready, we'll invite you over for more photoshoots, how about that?"
                    ma "You'll even get paid too, [p]. Give us some more time, aand hopefully we can get Vincent to arrange something more."
                    p "Cool beans."
                    ny "Seeya, [p]."
                    ma "Goodbye, and good luck."
                    scene black with fade
                    $ amandalvl += 1
                    jump studiolobby
            else:
                v "What's up [p]?"
                v "Sorry, no work for you just yet!"
                jump vincent_studio
        "Nevermind":
            jump studio_lobby
