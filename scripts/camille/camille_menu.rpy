label Camille:
    hide screen map_icon
    hide screen daytime
    if renpy.music.get_playing() != "sounds/slopes.mp3":
        play music "sounds/slopes.mp3" fadeout 1
    scene cam-6
    if camillelvl == 1:
        jump camilletalk
    menu:
        "Talk" if facilitiesIntro:
            jump camilletalk
        "I'd like access to the..." if resortmembership > 0:
            menu:
                "Public bathouse." if resortmembership > 0:
                    scene cam-5
                    t "Certainly, right this way!"
                    scene black with fade
                    jump publicbathouse
                "Sauna." if resortmembership > 1:
                    scene cam-5
                    t "Enjoy the steam!"
                    scene black with fade
                    jump sauna
                "Private pool." if resortmembership > 2:
                    scene cam-5
                    t "A pool just for you and your friends!"
                    scene black with fade
                    jump pool
                "Never mind":
                    jump lobby
        "Tell me more about the facilities here.":
            jump facilitiesIntro
        "Can I upgrade my membership?" if facilitiesIntro:
            call membershipcheck from _call_membershipcheck
            if resortmembership == 3:
                scene cam-7
                t "You already have the highest level of membership!"
                jump lobby
            scene cam-5
            t "You currently have [membership] membership."
            t "You may upgrade to [nextmembership] membership for $[membershipcost]."
            menu:
                "Let's do it!":
                    if cash - membershipcost > 0:
                        $ resortmembership += 1
                        $ cash -= membershipcost
                        scene cam-7
                        t "I think you'll really enjoy your stay here."
                        "([nextmembership] membership added!)"
                        jump Camille
                    scene cam-2
                    t "I'm sorry [p], maybe you left your wallet at home?"

                "I've got second thoughts...":
                    scene cam-5
                    t "You can always come back and change your mind."
                    t "The membership here is really worth it!"
            jump Camille
        "Actually, never mind.":
            jump lobby

label facilitiesIntro:
    scene cam-7
    t "We've got pools, saunas, restaurants and more!"
    p "Sounds like a great place to hang out."
    p "So, do I pay for this? How does that work?"
    scene cam-5
    t "We've got multiple levels of membership, starting at bronze."
    t "Unlocking higher tiers of membership gives you access to areas like private rooms and more luxurious areas."
    $ facilitiesIntro = True
    jump Camille
