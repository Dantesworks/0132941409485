## BTC Code
default balanceBTC = 0
default balanceCash = 0
default exchangeRate = 10
default withdrawal_amount = 50

label cryptoChange:
    $ crypto_int = renpy.random.randint(-20, 25)
    $ crypto_float = float(crypto_int)
    $ crypto_ratio = crypto_float/100
    $ delta = exchangeRate*crypto_ratio
    $ exchangeRate = exchangeRate + delta
    return

## Screens
screen btc():
    zorder 7
    imagebutton: ## Close
        idle "phone/close.png"
        action [Hide("btc"), PauseAudio("music", False), Stop("voice")]
    imagebutton: ## BTC
        focus_mask True
        idle "phone/btc.png"
        action NullAction()
    imagebutton: ## Home
        focus_mask True
        idle "phone/home.png"
        action [Hide("btc"), Show("homescreen"), PauseAudio("music", False), Stop("voice")]
    imagebutton: ## Question
        focus_mask True
        idle "phone/question.png"
        hover "phone/questionhover.png"
        action [Show("questionBTC"), Hide("btc")]
    imagebutton: ## buy
        focus_mask True
        idle "phone/buy.png"
        hover "phone/buyhover.png"
        action [Play("sound", "sounds/effects/hey.mp3"), SetVariable("balanceBTC", balanceBTC+balanceCash/exchangeRate), SetVariable("balanceCash", 0)]
    imagebutton: ## sell
        focus_mask True
        idle "phone/sell.png"
        hover "phone/sellhover.png"
        action [Play("sound", "sounds/effects/mmm.mp3"), SetVariable("balanceBTC", 0), SetVariable("balanceCash", balanceCash+balanceBTC*exchangeRate)]
    if balanceCash >= withdrawal_amount:
        imagebutton: ## withdraw
            focus_mask True
            idle "phone/withdraw.png"
            hover "phone/withdrawhover.png"
            action [Play("sound", "sounds/effects/wo.mp3"), SetVariable("balanceCash", balanceCash-withdrawal_amount), SetVariable("cash", cash+withdrawal_amount)]
    if balanceCash < withdrawal_amount:
        imagebutton: ## withdraw 2
            focus_mask True
            idle "phone/withdraw.png"
            hover "phone/withdrawhover.png"
            action Show("btc")
    if cash >= withdrawal_amount:
        imagebutton: ## deposit
            focus_mask True
            idle "phone/deposit.png"
            hover "phone/deposithover.png"
            action [Play("sound", "sounds/effects/wassa.mp3"), SetVariable("balanceCash", balanceCash+withdrawal_amount), SetVariable("cash", cash-withdrawal_amount)]
    if cash < withdrawal_amount:
        imagebutton: ## deposit2
            focus_mask True
            idle "phone/deposit.png"
            hover "phone/deposithover.png"
            action Show("btc")
    text "[exchangeRate: .2f]" pos(1010, 732)
    text "[balanceBTC: .4f]" xanchor 1.0 pos(978, 438) color "#000000"
    text "[balanceCash: .2f]" xanchor 1.0 pos(978, 502) color "#000000"

screen questionBTC():
    imagebutton: ## Close
        idle "phone/close.png"
        action [Hide("questionBTC"), PauseAudio("music", False), Stop("voice")]
    imagebutton: ## BTC
        focus_mask True
        idle "phone/questionbtc.png"
        action NullAction()
    imagebutton: ## Home
        focus_mask True
        idle "phone/home.png"
        action [Hide("questionBTC"), PauseAudio("music", False), Stop("voice")]
    imagebutton: ## Question
        focus_mask True
        idle "phone/question.png"
        hover "phone/questionhover.png"
        action [Show("btc"), Hide("questionBTC")]
    hbox xalign 0.5 yalign 0.5 spacing 10:
        frame:
            textbutton "$5" action SetVariable("withdrawal_amount", 5)
        frame:
            textbutton "$50" action SetVariable("withdrawal_amount", 50)
        frame:
            textbutton "$500" action SetVariable("withdrawal_amount", 500)
        frame:
            textbutton "$5000" action SetVariable("withdrawal_amount", 5000)
