default DSLR = False
default primes_50 = False
default primes_85 = False
default Zoom = False
default tripod = False
default guide = False

default long_gown = False
default security_dress = False
default gym_clothes = False

default dildo = False
default plug = False

default bogged = False
default juke = False

## Music
default amanda_theme = False
default camille_theme = False
default caroline_theme = False
default kaira_theme = False
default nicole_theme = False
default vincent_theme = False

label online_shop:
    scene wallpaper
    menu:
        "Camera Equipment":
            jump camera_equipment
        "Outfits":
            jump outfits
        "Sex shop" if olivialvl > 2:
            jump sex_shop
        "Favours from Bogdanoff":
            if bogged == True:
                "Bogdanoffs will only manipulate the market for you once per day."
                jump online_shop
            else:
                jump bog
        "Juke Box" if juke == False:
            jump juke
        "Music Tracks" if juke:
            "All tracks cost 5 BCC."
            jump tracks
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
                "Thank you for your purchase."
            jump camera_equipment
        "50mm Prime Lens - $500" if primes_50 == False:
            if cash < 500:
                "Transaction failed - insufficient funds."
            else:
                $ cash -= 500
                $ primes_50 = True
                "Thank you for your purchase."
            jump camera_equipment
        "85mm Prime Lens - $1000" if primes_85 == False:
            if cash < 1000:
                "Transaction failed - insufficient funds."
            else:
                $ cash -= 1000
                $ primes_85 = True
                "Thank you for your purchase."
            jump camera_equipment
        "70-200mm HQ Zoom Lens - $1500" if Zoom == False:
            if cash < 1500:
                "Transaction failed - insufficient funds."
            else:
                $ cash -= 1500
                $ Zoom = True
                "Thank you for your purchase."
            jump camera_equipment
        "Tripod - $100" if tripod == False:
            if cash < 100:
                "Transaction failed - insufficient funds."
            else:
                $ cash -= 100
                $ tripod = True
                "Thank you for your purchase."
            jump camera_equipment
        "Guide to Photography in the Modelling Industry - $50" if guide == False:
            if cash < 50:
                "Transaction failed - insufficient funds."
            else:
                $ cash -= 50
                $ guide = True
                "Thank you for your purchase."
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
                "Thank you for your purchase."
        "Security Dress - $50" if security_dress == False:
            if cash < 50:
                "Transaction failed - insufficient funds."
            else:
                $ cash -= 50
                $ security_dress = True
                "Thank you for your purchase."
        "Gym Clothes - $50." if gym_clothes == False:
            if cash < 50:
                "Transaction failed - insufficient funds."
            else:
                $ cash -= 50
                $ gym_clothes = True
                "Thank you for your purchase."
        "Back":
            jump online_shop
    jump online_shop
label sex_shop:
    menu:
        "Dildo - $50" if dildo == False:
            if cash < 50:
                "Transaction failed - insufficient funds."
            else:
                $ cash -= 50
                $ dildo = True
                "Thank you for your purchase."
            jump sex_shop
        "Butt Plug - $80" if plug == False:
            if cash < 50:
                "Transaction failed - insufficient funds."
            else:
                $ cash -= 50
                $ plug = True
                "Thank you for your purchase."
            jump sex_shop
        "Exit":
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

label juke:
    "Spend BCC to unlock the Juke Box in the Museum of Patrons to play tracks that you purchase."
    "Would you like to purchase the Juke Box for 10 BCC?"
    menu:
        "Yes":
            if balanceBTC < 10:
                "Transaction failed - insufficient funds."
            else:
                $ balanceBTC -= 10
                $ juke = True
                "Make sure to purchase tracks to play."
            jump online_shop
        "No":
            jump online_shop

label tracks:
    menu:
        "Amanda's Theme" if amanda_theme == False:
            if balanceBTC < 5:
                "Transaction failed - insufficient funds."
            else:
                $ balanceBTC -= 5
                $ amanda_theme = True
                "Enjoy the track in the Museum of Patrons."
            jump tracks
        "Camille's Theme" if camille_theme == False:
            if balanceBTC < 5:
                "Transaction failed - insufficient funds."
            else:
                $ balanceBTC -= 5
                $ camille_theme = True
                "Enjoy the track in the Museum of Patrons."
            jump tracks
        "Caroline's Theme" if caroline_theme == False:
            if balanceBTC < 5:
                "Transaction failed - insufficient funds."
            else:
                $ balanceBTC -= 5
                $ caroline_theme = True
                "Enjoy the track in the Museum of Patrons."
            jump tracks
        "Kaira's Theme" if kaira_theme == False:
            if balanceBTC < 5:
                "Transaction failed - insufficient funds."
            else:
                $ balanceBTC -= 5
                $ kaira_theme = True
                "Enjoy the track in the Museum of Patrons."
            jump tracks
        "Nicole's Theme" if nicole_theme == False:
            if balanceBTC < 5:
                "Transaction failed - insufficient funds."
            else:
                $ balanceBTC -= 5
                $ nicole_theme = True
                "Enjoy the track in the Museum of Patrons."
            jump tracks
        "Vincent's Theme" if vincent_theme == False:
            if balanceBTC < 5:
                "Transaction failed - insufficient funds."
            else:
                $ balanceBTC -= 5
                $ vincent_theme = True
                "Enjoy the track in the Museum of Patrons."
            jump tracks

        "Back":
            jump online_shop

## Juke Box
label juke_box:
    scene wallpaper2
    menu:
        "Amanda's Theme" if amanda_theme == True:
            play music "sounds/wisteria.mp3" fadeout 1
        "Camille's Theme" if camille_theme == True:
            play music "sounds/armoir.mp3" fadeout 1
        "Caroline's Theme" if caroline_theme == True:
            play music "sounds/dreams.mp3" fadeout 1
        "Kaira's Theme" if kaira_theme == True:
            play music "sounds/automata.mp3" fadeout 1
        "Nicole's Theme" if nicole_theme == True:
            play music "sounds/beach.mp3" fadeout 1
        "Vincent's Theme" if vincent_theme == True:
            play music "sounds/wistful.mp3" fadeout 1
        "Back":
            if from_museum == 1:
                jump museum
            elif from_museum == 2:
                jump museum2
    jump juke_box
