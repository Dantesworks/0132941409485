default DSLR = False
default primes_50 = False
default primes_85 = False
default Zoom = False
default tripod = False
default guide = False

default long_gown = False
default security_dress = False
default gym_clothes = False

default bogged = False


label online_shop:
    scene wallpaper
    menu:
        "Camera Equipment":
            jump camera_equipment
        "Outfits":
            jump outfits
        "Favours from Bogdanoff":
            if bogged == True:
                "Bogdanoffs will only manipulate the market for you once per day."
                jump online_shop
            else:
                jump bog
        "Exit":
            jump computer

label camera_equipment:
    menu:
        "DSLR Camera Body + 18-55mm Kit Lens - $400" if DSLR == False:
            if cash < 400:
                "Transaction failed - insufficient funds."
            else:
                $ cash -= 400
                $ DSLR = True
                "Thankyou for your purchase."
            jump camera_equipment
        "50mm Prime Lens - $500" if primes_50 == False:
            if cash < 500:
                "Transaction failed - insufficient funds."
            else:
                $ cash -= 500
                $ primes_50 = True
                "Thankyou for your purchase."
            jump camera_equipment
        "85mm Prime Lens - $1000" if primes_85 == False:
            if cash < 1000:
                "Transaction failed - insufficient funds."
            else:
                $ cash -= 1000
                $ primes_85 = True
                "Thankyou for your purchase."
            jump camera_equipment
        "70-200mm HQ Zoom Lens - $1500" if Zoom == False:
            if cash < 1500:
                "Transaction failed - insufficient funds."
            else:
                $ cash -= 1500
                $ Zoom = True
                "Thankyou for your purchase."
            jump camera_equipment
        "Tripod - $100" if tripod == False:
            if cash < 100:
                "Transaction failed - insufficient funds."
            else:
                $ cash -= 100
                $ tripod = True
                "Thankyou for your purchase."
            jump camera_equipment
        "Guide to Photography in the Modelling Industry - $50" if guide == False:
            if cash < 50:
                "Transaction failed - insufficient funds."
            else:
                $ cash -= 50
                $ guide = True
                "Thankyou for your purchase."
                p "Hmm, I should be able to take better pictures and direct [mr] now."
        "Back":
            jump online_shop
    jump online_shop

label outfits:
    menu:
        "Long Gown - $50" if long_gown == False:
            if cash < 50:
                "Transaction failed - insufficient funds."
            else:
                $ cash -= 50
                $ long_gown = True
                "Thankyou for your purchase."
        "Security Dress - $50" if security_dress == False:
            if cash < 50:
                "Transaction failed - insufficient funds."
            else:
                $ cash -= 50
                $ security_dress = True
                "Thankyou for your purchase."
        "Gym Clothes - $50." if gym_clothes == False:
            if cash < 50:
                "Transaction failed - insufficient funds."
            else:
                $ cash -= 50
                $ gym_clothes = True
                "Thankyou for your purchase."
        "Back":
            jump online_shop
    jump online_shop

label bog:
    scene bog
    menu:
        "Reset BCC value to 10 - $200":
            "Are you sure?"
            menu:
                "Yes":
                    if cash < 200:
                        "Transaction failed - insufficient funds."
                    else:
                        $ exchangeRate = 10
                        $ cash -= 200
                        $ bogged = True
                        "We're all going to make it."
                "No":
                    jump bog
        "Pump it (Increases BCC value by 100) - $200":
            if cash < 200:
                "Transaction failed - insufficient funds."
            else:
                $ exchangeRate += 100
                $ cash -= 200
                $ bogged = True
                "We're all going to make it."
        "Dump it (Decreases BCC value by 20 percent) - $200":
            if cash < 200:
                "Transaction failed - insufficient funds."
            else:
                $ exchangeRate = exchangeRate*0.8
                $ cash-= 200
                $ bogged = True
                "We're all going to make it."
        "Back":
            jump online_shop
    jump online_shop
