label cafeJob:
    hide screen map_icon
    hide screen daytime
    ellie "Just come on around the back."
    scene black with fade
    scene cafework with fade
    "Time to earn my keep..."
    scene black with fade
    "You have gained $30!"
    $ cash += 30
    call daykeep from _call_daykeep
    jump map
