label fireplace:
    menu:
        "- Осмотреть камин -" if not fireplace_examined:
            $ fireplace_examined = True
            hide screen genie
            $ tt_xpos=350
            $ tt_ypos=90
            show screen genie_stands
            show screen chair_02 #Empty chair near the desk.
            show screen desk
            with Dissolve(0.5)
            m "Хм... Выглядит как обычный камин..."
            show screen genie
            hide screen genie_stands
            hide screen chair_02 #Empty chair near the desk.
            hide screen desk
            with Dissolve(0.5)
            jump day_main_menu
            
            
            
            
            
            
            
            
        "- Зажечь огонь -" if not fire_in_fireplace and not day == 1:
            #$ renpy.play('sounds/fire01.ogg')  
            #play bg_sounds "sounds/fire01.ogg" fadeout 1.0 fadein 1.0 #LOUD!
            #play bg_sounds "sounds/fire02.mp3" fadeout 1.0 fadein 1.0 #Quiet...
            $ fire_in_fireplace = True
            show screen fireplace_fire
            jump day_main_menu
        "- Потушить огонь -" if fire_in_fireplace:
            $ fire_in_fireplace = False
            stop bg_sounds #Stops playing the fire SFX.
            hide screen fireplace_fire
            jump day_main_menu
        "- Ничего -":
            jump day_main_menu