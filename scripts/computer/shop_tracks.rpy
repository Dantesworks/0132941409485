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
        "Nyx's Theme" if nyx_theme == False:
            if balanceBTC < 5:
                "Transaction failed - insufficient funds."
            else:
                $ balanceBTC -= 5
                $ nyx_theme = True
                "Enjoy the track in the Museum of Patrons."
            jump tracks
        "Maya's Theme" if maya_theme == False:
            if balanceBTC < 5:
                "Transaction failed - insufficient funds."
            else:
                $ balanceBTC -= 5
                $ maya_theme = True
                "Enjoy the track in the Museum of Patrons."
            jump tracks
        "Belle's Theme" if belle_theme == False:
            if balanceBTC < 5:
                "Transaction failed - insufficient funds."
            else:
                $ balanceBTC -= 5
                $ belle_theme = True
                "Enjoy the track in the Museum of Patrons."
            jump tracks

        "Back":
            jump online_shop
