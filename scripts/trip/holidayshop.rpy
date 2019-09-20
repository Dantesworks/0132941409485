default private_jet = False
default luxurious_hotels = False
default rv = False

label shop_holiday:
    scene wallpaper
    if renpy.music.get_playing() != "sounds/you.mp3":
        play music "sounds/you.mp3"
    menu:
        "Private Jet" if private_jet == False:
            play music "sounds/dreams.mp3" fadeout 1
            scene t1 with fade
            "Welcome to the e-tour of Dante's Jets, available to be hired for the discerning customer!"
            "Dante's Jets promise the privacy, luxury and convenience of the highest order."
            scene t2 with dissolve
            "Simply set the destination, and our world class artifical intelligence will take you to your destination."
            scene t3 with dissolve
            "Dante's Jets are preloaded with food and beverage for a mile-high experience that you will not forget."
            scene t4 with dissolve
            "Enjoy a spacious cabin that will accomodate dozens."
            scene t5 with dissolve
            "Amenities include a large bedroom for maximum luxury."
            scene t6 with dissolve
            "A premium walk-in bathroom has been designed to include all necessites conceivable for a complete package."
            scene t3 with dissolve
            "Hire a once-in-a-lifetime trip with Dante's Jets today!"
            "This experience could be yours for a mere $500,000 dollars!"
            menu:
                "Cough it up.":
                    if cash < 500000:
                        "Transaction failed - insufficient funds."
                    else:
                        $ cash -= 500000
                        $ private_jet = True
                        "Thank you for your purchase."
                    jump shop_holiday
                "Too rich for my blood.":
                    jump shop_holiday
        "Luxurious Hotels" if luxurious_hotels == False:
            play music "sounds/dreams.mp3" fadeout 1
            scene t8 with fade
            "Introducing the double room package of Luxurious Hotels!"
            "The first room enjoys a large bed with large floor-to-ceiling windows offering an excellent view of the city."
            scene t7 with dissolve
            "Luxurious couches await you when you return to your room while a vibrant fireplace keeps you warm."
            scene t9 with dissolve
            "A table and drawer is conveniently placed for business."
            scene t10 with dissolve
            "A large wardrobe is placed just outside the luxurious bathroom to accommodate efficiency and ease."
            "The bathroom is adorned with beautiful tiles and includes a bath and shower."
            scene t11 with dissolve
            "The second room features a large window featuring an exquisite view of the skyline."
            "The bed is large enough to easily accommodate your partner and yourself."
            scene t12 with dissolve
            "Transparent walls render a stylish bathroom that will surely lead to provactive and sensual moments."
            scene t13 with dissolve
            "A spacious room gives plenty of area to move around, and a television and desk provide entertainment and comfort whenever you are in the hotel."
            scene t11 with dissolve
            "This double room package may be had for a criminal price of $100,000! Do not miss out on this deal!"
            menu:
                "Cough it up.":
                    if cash < 100000:
                        "Transaction failed - insufficient funds."
                    else:
                        $ cash -= 100000
                        $ luxurious_hotels = True
                        "Thank you for your purchase."
                    jump shop_holiday
                "Too rich for my blood.":
                    jump shop_holiday
        "Relaxing RV" if rv == False:
            play music "sounds/dreams.mp3" fadeout 1
            scene t14 with fade
            "Introducing the renovated model of our renowned range of RVs!"
            scene t15 with dissolve
            "Enjoy a spacious cabin that can fit your family and friends comfortably."
            "The RV is fitted with with a table, seats, sofa and kitchen."
            scene t16 with dissolve
            "The dining area is next to large windows which let light spill through, illuminating the scene."
            scene t17 with dissolve
            "Further in are a bathroom, refrigerator, storage cupboards..."
            scene t18 with dissolve
            "...and a large bed for maximum comfort."
            scene t14 with dissolve
            "All this can be rented for a mere $5,000!"
            menu:
                "Cough it up.":
                    if cash < 5000:
                        "Transaction failed - insufficient funds."
                    else:
                        $ cash -= 5000
                        $ rv = True
                        "Thank you for your purchase."
                    jump shop_holiday
                "Too rich for my blood.":
                    jump shop_holiday
        "Back":
            if luxurious_hotels and private_jet and rv:
                $ shop_holiday = False
            jump online_shop
