label cafeJob:
    call hidescreens from _call_hidescreens_12
    ellie "Just come on around the back."
    scene black with fade
    scene cafework with fade
    "Time to earn my keep..."
    scene black with fade
    "You have gained $50!"
    $ cash += 50
    call daykeep from _call_daykeep
    jump map
