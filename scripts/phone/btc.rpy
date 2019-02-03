## BTC Code
default balanceBTC = 0
default balanceCash = 0
default exchangeRate = 10

label cryptoChange:
    $ crypto_int = renpy.random.randint(-40, 67)
    $ crypto_float = float(crypto_int)
    $ crypto_ratio = crypto_float/100
    $ delta = exchangeRate*crypto_ratio
    $ exchangeRate = exchangeRate + delta
    return

## Screens
screen btc():
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
        action [Hide("btc"), PauseAudio("music", False), Stop("voice")]
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
    if balanceCash >= 50:
        imagebutton: ## withdraw
            focus_mask True
            idle "phone/withdraw.png"
            hover "phone/withdrawhover.png"
            action [Play("sound", "sounds/effects/wo.mp3"), SetVariable("balanceCash", balanceCash-50), SetVariable("cash", cash+50)]
    if balanceCash < 50:
        imagebutton: ## withdraw 2
            focus_mask True
            idle "phone/withdraw.png"
            hover "phone/withdrawhover.png"
            action Show("btc")
    if cash >= 50:
        imagebutton: ## deposit
            focus_mask True
            idle "phone/deposit.png"
            hover "phone/deposithover.png"
            action [Play("sound", "sounds/effects/wassa.mp3"), SetVariable("balanceCash", balanceCash+50), SetVariable("cash", cash-50)]
    if cash < 50:
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
