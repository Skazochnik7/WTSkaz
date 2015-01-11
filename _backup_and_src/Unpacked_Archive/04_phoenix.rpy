label phoenix:
    if bird_interact == 15: # Counts how many times you have interacted with the bird.
        stop music fadeout 3.0
        $ bird_interact += 1 # Counts how many times you have interacted with the bird.
        show screen blktone8
        with d7
        a1 "Хорошо, давайте проясним кое-что..."
        a1 "Взаимодействие с этой птицей не даст вам буквально ничего."
        a1 "Есть счетчик, который стартует это событие после того, как вы сделали что-то определенное количество раз и все."
        a1 "На первый взгляд у меня есть весьма амбициозные планы на этого ублюдка"
        a1 "Что-то вроде покупки еды для него, ласки и в конечном итоге получаения от всего этого какого-то вознаграждения..."
        a1 "Все это было вырезано как и другие \"штуки\"..."
        a1 "Вообще я хотел убрать эту птицу, но не смог заставить себя это сделать..."
        a1 "Но после того, как я провел столько времени анимируя это чертово падающее перо..."
        a1 "С этого момента вы сможете продолжать кормить и гладить птицу, но я просто хочу, чтобы вы знали, что это не даст вам ничего."
        a2 "Извините за то, что прервал вас. Наслаждайтесь игрой дальше."
        hide screen blktone8
        with d3
        call music_block
        jump day_main_menu
    
    menu:
        "- Исследовать -" if not bird_examined:
            $ bird_examined = True
            hide screen genie
            $ tt_xpos=270
            $ tt_ypos=90
            show screen genie_stands
            show screen chair_02 #Empty chair near the desk.
            show screen desk
            with Dissolve(0.5)
            m "Хм....."
            m "Даже эта странная птица излучает магию.."
            show screen genie
            hide screen genie_stands
            hide screen chair_02 #Empty chair near the desk.
            hide screen desk
            with Dissolve(0.5)
            jump day_main_menu
            
            
            
        "- Покормить птицу -" if not phoenix_is_feed and bird_examined:
            $ phoenix_is_feed = True
            jump feeding
            
        "- Погладить птицу -" if bird_examined:
            jump petting
        "- Ничего -":
            call screen main_menu_01    
            
            
### FEEDING ###
label feeding:
    $ bird_interact += 1 # Counts how many times you have interacted with the bird.
    hide screen genie
    show screen feeding 
    with Dissolve(0.3)
    pause 1
    show screen phoenix_food
    $ genie_speaks = renpy.random.randint(1, 3) #Determines what phrase if any Genie will use.
    if genie_speaks == 1:
        m "Держи..."
    else:
        pause.5
    show screen genie
    hide screen feeding 
    with Dissolve(0.3)
    call screen main_menu_01    
    

### PETTING ###
label petting:
    $ bird_interact += 1 # Counts how many times you have interacted with the bird.
    hide screen genie
    show screen petting
    with Dissolve(0.3)
    pause 3
    show screen sad_phoenix #SMILEY
    pause 1.5
    m "Птица плохо выглядит. Может быть она больна?" #The bird doesn't look good. Is it sick or something
    pause.5
    
    
    
    show screen genie
    hide screen sad_phoenix #SMILEY
    hide screen petting
    with Dissolve(0.3)
    call screen main_menu_01
    
    
    
    
   