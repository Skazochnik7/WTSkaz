
#################################################################################################################################
### LEVEL 02 ####################################################################################################################    
###################REQUEST_02_c (LEVEL02) ### FLIRT WITH TEACHERS ###
label new_request_02_c:
    
    #__#hide screen hermione_main 
    #__#with d3
    $herView.hideQQ()
    m "{size=-4}(Заставить ее флиртовать с учителем?){/size}"
    $ menu_x = 0.5 #Default position of the menu (0.5). Version B is $ menu_x = 0.2
    menu:
        "\"(Да, давай попробуем!)\"":
            pass
        "\"(Не сейчас.)\"":
            jump new_personal_request

    m "Мисс Грейнджер, я хочу, чтобы вы флиртовали с учителем."
    if whoring <=2 or request_02_b_points <= 1: # request_02_b_points - counts how many times Hermione was sent to flirt with boys. 
        jump too_much
   
    $ pos = POS_140

    if request_02_c_points == 0 and whoring <= 8: ### up to LEVEL 03
    ### LEVEL 03 ### <===============================================================FIRST EVENT!
        #__#$ h_xpos=140 #Defines position of the Hermione's full length sprite. (Default 370). 140 - center.
        #__#$ pos = POS_140
        #__#$ h_body = "03_hp/13_hermione_main/body_01.png" #Flashing Трусики
        #__#show screen hermione_main
        #__#with d3
        $herView.showQQ( "body_01.png", pos )
        her "Я постараюсь, сэр!"
        #__#hide screen hermione_main
        #__#with d3
        $herView.hideQQ()
        #__#$ h_xpos=140 #Defines position of the Hermione's full length sprite. (Default 370). 140 - center.
        #__#$ h_body = "03_hp/13_hermione_main/body_02.png" #Flashing Трусики
        #__#show screen hermione_main
        #__#with d3
        $herView.showQQ( "body_02.png", pos )
        her "Я рада, что вы наконец предложили это мне!"
        m "Да?"
        #__#hide screen hermione_main
        #__#with d3
        $herView.hideQQ()
        #__#$ h_xpos=140 #Defines position of the Hermione's full length sprite. (Default 370). 140 - center.
        #__#$ h_body = "03_hp/13_hermione_main/body_07.png" #Flashing Трусики
        #__#show screen hermione_main
        #__#with d3
        $herView.showQQ( "body_07.png", pos )
        her "Вы наконец-то решили устроить проверку учителям, которые обменивают очки на услуги, не так ли?" 
        #__#hide screen hermione_main
        #__#with d3
        $herView.hideQQ()
        #__#$ h_xpos=140 #Defines position of the Hermione's full length sprite. (Default 370). 140 - center.
        #__#$ h_body = "03_hp/13_hermione_main/body_16.png" #Flashing Трусики
        #__#show screen hermione_main
        #__#with d3
        $herView.showQQ( "body_16.png", pos )
        her "Для меня большая честь выступить в качестве приманки."
        m "Эм... Да, именно этим мы и займемся."
        #__#hide screen hermione_main
        #__#with d3
        $herView.hideQQ()
        #__#$ h_xpos=140 #Defines position of the Hermione's full length sprite. (Default 370). 140 - center.
        #__#$ h_body = "03_hp/13_hermione_main/body_07.png" #Flashing Трусики
        #__#show screen hermione_main
        #__#with d3
        $herView.showQQ( "body_07.png", pos )
        her "Отлично! Вы можете расчитывать на меня!"
    else:
        #__#hide screen hermione_main
        #__#with d3
        $herView.hideQQ()
        #__#$ h_xpos=140 #Defines position of the Hermione's full length sprite. (Default 370). 140 - center.
        #__#$ pos = POS_140
        #__#$ h_body = "03_hp/13_hermione_main/body_07.png" #Flashing Трусики
        #__#show screen hermione_main
        #__#with d3
        $herView.showQQ( "body_07.png", pos )
        her "Я зайду к вам с подробностями вечером."
        m "Буду ждать..."
    

    her "Ну, мне следует идти. Занятия вот-вот начнутся..."
    $ request_02_c = True

    hide screen bld1
    #__#hide screen hermione_main
    $herView.hideQ()
    hide screen blktone 
    hide screen hermione_02
    hide screen ctc
    with d3

    $ walk_xpos=400 #Animation of walking chibi. (From)
    $ walk_xpos2=610 #Coordinates of it's movement. (To)
    $ hermione_speed = 02.0 #The speed of moving the walking animation across the screen.
    show screen hermione_walk_01_f 
    pause 2
    hide screen hermione_walk_01_f 
    $ renpy.play('sounds/door.mp3') #Sound of a door opening.
    with Dissolve(.3)


    $ hermione_takes_classes = True
    jump day_main_menu

    
    
label new_request_02_c_complete:  ### FLIRTING WITH TEACHERS COMPLETE ###
    $ walk_xpos=520 #Animation of walking chibi. (From)
    $ walk_xpos2=400 #Coordinates of it's movement. (To)
    $ hermione_speed = 02.0 #The speed of moving the walking animation across the screen.
    $ renpy.play('sounds/door.mp3') #Sound of a door opening.
    show screen hermione_walk_01 
    with d4
    pause 1.7 
    $ hermione_chibi_xpos = 400 #Near the desk.
    show screen hermione_02 #Hermione stands still.
    pause.5
    show screen bld1
    with Dissolve(.3)
    
    #__#$ h_xpos=370 #Defines position of the Hermione's full length sprite.
    #__#$ h_ypos=0
    $ pos = POS_370
    #__#$ h_body = "03_hp/13_hermione_main/body_01.png" #Sprite of Hermione's upper body.
    #__#show screen hermione_main
    $herView.showQ( "body_01.png", pos )
    show screen hermione_02
    with Dissolve(.3)
    her "Добрый вечер, сэр."
    m "Мисс Грейнджер..."
    m "Вы справились с заданием?"
    her "Я сделала, что вы просили, сэр..."
    menu:
        "\"Отлично. Вот твои очки.\"":
            pass
        "\"Теперь поподробнее.\"":
            #__#hide screen hermione_main
            #__#with d3
            $herView.hideQQ()
            m "Скажите, со сколькими учителями вы заигрывали, Мисс Грейнджер?"
            m "Мне нужны подробности."
            show screen blktone
            with d3
    
            if  whoring >= 3 and whoring <= 5: ### LEVEL 02 <===================================================================== EVENT LEVEL 01
                if one_out_of_three == 1: ### EVENT (A)
                    play music "music/Chipper Doodle v2.mp3" fadein 1 fadeout 1 # HERMIONE'S THEME.
                    #__#hide screen hermione_main
                    #__#with d3
                    $herView.hideQQ()
                    #__#$ h_xpos=370 #Defines position of the Hermione's full length sprite. (Default 370). 140 - center.
                    #__#$ pos = POS_370
                    #__#$ h_body = "03_hp/13_hermione_main/body_10.png" #Flashing Трусики
                    #__#show screen hermione_main
                    #__#with d3
                    $herView.showQQ( "body_10.png", pos )
                    her "Ну, я попыталась заигрывать с профессором Флитвиком..."
                    #__#hide screen hermione_main
                    #__#with d3
                    $herView.hideQQ()
                    #__#$ h_xpos=370 #Defines position of the Hermione's full length sprite. (Default 370). 140 - center.
                    #__#$ h_body = "03_hp/13_hermione_main/body_09.png" #Flashing Трусики
                    #__#show screen hermione_main
                    #__#with d3
                    $herView.showQQ( "body_09.png", pos )
                    her "Но это не сработало..."
                    #__#hide screen hermione_main
                    #__#with d3
                    $herView.hideQQ()
                    #__#$ h_xpos=370 #Defines position of the Hermione's full length sprite. (Default 370). 140 - center.
                    #__#$ h_body = "03_hp/13_hermione_main/body_12.png" #Flashing Трусики
                    #__#show screen hermione_main
                    #__#with d3
                    $herView.showQQ( "body_12.png", pos )
                    her ".............................."
                    m "Как замечательно..."
                    m "Это все, что вы сделали сегодня, Мисс Грейнджер?"
                    #__#hide screen hermione_main
                    #__#with d3
                    $herView.hideQQ()
                    #__#$ h_xpos=370 #Defines position of the Hermione's full length sprite. (Default 370). 140 - center.
                    #__#$ h_body = "03_hp/13_hermione_main/body_11.png" #Flashing Трусики
                    #__#show screen hermione_main
                    #__#with d3
                    $herView.showQQ( "body_11.png", pos )
                    her "Д-да..."
                    her "Но сэр, я знаю \"грязные\" факты о профессоре Флитвике!"
                    her "Всем известно, что из-за его роста..."
                    #__#hide screen hermione_main
                    #__#with d3
                    $herView.hideQQ()
                    #__#$ h_xpos=370 #Defines position of the Hermione's full length sprite. (Default 370). 140 - center.
                    #__#$ h_body = "03_hp/13_hermione_main/body_13.png" #Flashing Трусики
                    #__#show screen hermione_main
                    #__#with d3
                    $herView.showQQ( "body_13.png", pos )
                    her "Он иногда... Эм..."
                    #__#hide screen hermione_main
                    #__#with d3
                    $herView.hideQQ()
                    #__#$ h_xpos=370 #Defines position of the Hermione's full length sprite. (Default 370). 140 - center.
                    #__#$ h_body = "03_hp/13_hermione_main/body_29.png" #Flashing Трусики
                    #__#show screen hermione_main
                    #__#with d3
                    $herView.showQQ( "body_29.png", pos )
                    her "Он любит заглядывать под юбки учениц, сэр!"
                    m "Это еще не все?"
                    #__#hide screen hermione_main
                    #__#with d3
                    $herView.hideQQ()
                    #__#$ h_xpos=370 #Defines position of the Hermione's full length sprite. (Default 370). 140 - center.
                    #__#$ h_body = "03_hp/13_hermione_main/body_31.png" #Flashing Трусики
                    #__#show screen hermione_main
                    #__#with d3
                    $herView.showQQ( "body_31.png", pos )
                    her "Что?"
                    m "Я имею в виду, он нам всем нравится и мы возмущены таким поведением профессора Флик-флика."      #WARNING_Z text?
                    #__#hide screen hermione_main
                    #__#with d3
                    $herView.hideQQ()
                    #__#$ h_xpos=370 #Defines position of the Hermione's full length sprite. (Default 370). 140 - center.
                    #__#$ h_body = "03_hp/13_hermione_main/body_07.png" #Flashing Трусики
                    #__#show screen hermione_main
                    #__#with d3
                    $herView.showQQ( "body_07.png", pos )
                    her "Э-э... \"Профессор Флитвик\", сэр."
                    m "Верно. Внесем его в мой \"список непослушных мальчиков\" как я и говорил."
                    #__#hide screen hermione_main
                    #__#with d3
                    $herView.hideQQ()
                    #__#$ h_xpos=370 #Defines position of the Hermione's full length sprite. (Default 370). 140 - center.
                    #__#$ h_body = "03_hp/13_hermione_main/body_17.png" #Flashing Трусики
                    #__#show screen hermione_main
                    #__#with d3
                    $herView.showQQ( "body_17.png", pos )
                    her "......................"
                    m "Ну, не хочу это говорить, но вы очень плохо выполнили свою работу, Мисс Грейнджер."
                    #__#hide screen hermione_main
                    #__#with d3
                    $herView.hideQQ()
                    #__#$ h_xpos=370 #Defines position of the Hermione's full length sprite. (Default 370). 140 - center.
                    #__#$ h_body = "03_hp/13_hermione_main/body_12.png" #Flashing Трусики
                    #__#show screen hermione_main
                    #__#with d3
                    $herView.showQQ( "body_12.png", pos )
                    her "................................"
                    
                    $ pos = POS_140
                    
                    menu:
                        "\"Остаетесь без очков!\"":

                            #__#hide screen hermione_main
                            #__#with d3
                            $herView.hideQQ()
                            #__#$ h_xpos=140 #Defines position of the Hermione's full length sprite. (Default 370). 140 - center.
                            #__#$ pos = POS_140
                            #__#$ h_body = "03_hp/13_hermione_main/body_28.png" #Flashing Трусики
                            #__#show screen hermione_main
                            #__#with d3
                            $herView.showQQ( "body_28.png", pos )
                            her "но профессор, я сделала все что смогла!"
                            #__#hide screen hermione_main
                            #__#with d3
                            $herView.hideQQ()
                            #__#$ h_xpos=140 #Defines position of the Hermione's full length sprite. (Default 370). 140 - center.
                            #__#$ h_body = "03_hp/13_hermione_main/body_67.png" #Flashing Трусики
                            #__#show screen hermione_main
                            #__#with d3
                            $herView.showQQ( "body_67.png", pos )
                            her "Вы не можете отказаться от своего обещания!"
                            m "......................."
                            #__#hide screen hermione_main
                            #__#with d3
                            $herView.hideQQ()
                            #__#$ h_xpos=140 #Defines position of the Hermione's full length sprite. (Default 370). 140 - center.
                            #__#$ h_body = "03_hp/13_hermione_main/body_32.png" #Flashing Трусики
                            #__#show screen hermione_main
                            #__#with d3
                            $herView.showQQ( "body_32.png", pos )
                            stop music fadeout 1.0
                            her "Это не подобает директору школы!"
                            m "Вы провалились, Мисс Грейнджер."
                            #__#hide screen hermione_main
                            #__#with d3
                            $herView.hideQQ()
                            #__#$ h_xpos=140 #Defines position of the Hermione's full length sprite. (Default 370). 140 - center.
                            #__#$ h_body = "03_hp/13_hermione_main/body_76.png" #Flashing Трусики
                            #__#show screen hermione_main
                            #__#with d3
                            $herView.showQQ( "body_76.png", pos )
                            her "Арх!"
                            $ mad += 18
                            call music_block
                            jump could_not_flirt_02
                        "\"Хотя, вы заслужили эти очки.\"":
                            #__#hide screen hermione_main
                            #__#with d3
                            $herView.hideQQ()
                            #__#$ h_xpos=140 #Defines position of the Hermione's full length sprite. (Default 370). 140 - center.
                            $ pos = POS_140
                            #__#$ h_body = "03_hp/13_hermione_main/body_28.png" #Flashing Трусики
                            #__#show screen hermione_main
                            #__#with d3
                            $herView.showQQ( "body_28.png", pos )
                            her "Правда?"
                            #__#hide screen hermione_main
                            #__#with d3
                            $herView.hideQQ()
                            #__#$ h_xpos=140 #Defines position of the Hermione's full length sprite. (Default 370). 140 - center.
                            #__#$ h_body = "03_hp/13_hermione_main/body_75.png" #Flashing Трусики
                            #__#show screen hermione_main
                            #__#with d3
                            $herView.showQQ( "body_75.png", pos )
                            her "Огромное спасибо, профессор!"
                           
                elif one_out_of_three == 2: ### EVENT (B)
                    #__#hide screen hermione_main
                    #__#with d3
                    $herView.hideQQ()
                    #__#$ h_xpos=140 #Defines position of the Hermione's full length sprite. (Default 370). 140 - center.
                    $ pos = POS_140
                    #__#$ h_body = "03_hp/13_hermione_main/body_13.png" #Flashing Трусики
                    #__#show screen hermione_main
                    #__#with d3
                    $herView.showQQ( "body_13.png", pos )
                    her ".................."
                    her "............................"
                    m "Мисс Грейнджер?"
                    #__#hide screen hermione_main
                    #__#with d3
                    $herView.hideQQ()
                    #__#$ h_xpos=140 #Defines position of the Hermione's full length sprite. (Default 370). 140 - center.
                    #__#$ h_body = "03_hp/13_hermione_main/body_11.png" #Flashing Трусики
                    #__#show screen hermione_main
                    #__#with d3
                    $herView.showQQ( "body_11.png", pos )
                    her "Да, профессор... Мне жаль... Просто я..."
                    #__#hide screen hermione_main
                    #__#with d3
                    $herView.hideQQ()
                    #__#$ h_xpos=140 #Defines position of the Hermione's full length sprite. (Default 370). 140 - center.
                    #__#$ h_body = "03_hp/13_hermione_main/body_13.png" #Flashing Трусики
                    #__#show screen hermione_main
                    #__#with d3
                    $herView.showQQ( "body_13.png", pos )
                    her "............"
                    m "Ты сделала то, что я просил?"
                    #__#hide screen hermione_main
                    #__#with d3
                    $herView.hideQQ()
                    #__#$ h_xpos=140 #Defines position of the Hermione's full length sprite. (Default 370). 140 - center.
                    #__#$ h_body = "03_hp/13_hermione_main/body_14.png" #Flashing Трусики
                    #__#show screen hermione_main
                    #__#with d3
                    $herView.showQQ( "body_14.png", pos )
                    her "Я пыталась, сэр. Правда..."
                    m "С кем ты пыталась заигрывать?"
                    #__#hide screen hermione_main
                    #__#with d3
                    $herView.hideQQ()
                    #__#$ h_xpos=140 #Defines position of the Hermione's full length sprite. (Default 370). 140 - center.
                    #__#$ h_body = "03_hp/13_hermione_main/body_13.png" #Flashing Трусики
                    #__#show screen hermione_main
                    #__#with d3
                    $herView.showQQ( "body_13.png", pos )
                    her "........."
                    #__#hide screen hermione_main
                    #__#with d3
                    $herView.hideQQ()
                    #__#$ h_xpos=140 #Defines position of the Hermione's full length sprite. (Default 370). 140 - center.
                    #__#$ h_body = "03_hp/13_hermione_main/body_12.png" #Flashing Трусики
                    #__#show screen hermione_main
                    #__#with d3
                    $herView.showQQ( "body_12.png", pos )
                    her "Профессор Снейп, сэр."
                    play music "music/Chipper Doodle v2.mp3" fadein 1 fadeout 1 # HERMIONE'S THEME.
                    m "Северус? Интересно..."
                    m "И как все прошло?"
                    #__#hide screen hermione_main
                    #__#with d3
                    $herView.hideQQ()
                    #__#$ h_xpos=140 #Defines position of the Hermione's full length sprite. (Default 370). 140 - center.
                    #__#$ h_body = "03_hp/13_hermione_main/body_07.png" #Flashing Трусики
                    #__#show screen hermione_main
                    #__#with d3
                    $herView.showQQ( "body_07.png", pos )
                    her "Ужасно сэр..."
                    her "Простите, но я правда ненавижу Профессора Снейпа, сэр!"
                    m "И конечно же я уверен, что это взаимно..."
                    m "Расскажи, что произошло."
                    #__#hide screen hermione_main
                    #__#with d3
                    $herView.hideQQ()
                    #__#$ h_xpos=140 #Defines position of the Hermione's full length sprite. (Default 370). 140 - center.
                    #__#$ h_body = "03_hp/13_hermione_main/body_09.png" #Flashing Трусики
                    #__#show screen hermione_main
                    #__#with d3
                    $herView.showQQ( "body_09.png", pos )
                    her "Ничего не произошло, сэр. Он просто рассмеялся мне в лицо..."
                    #__#hide screen hermione_main
                    #__#with d3
                    $herView.hideQQ()
                    #__#$ h_xpos=140 #Defines position of the Hermione's full length sprite. (Default 370). 140 - center.
                    #__#$ h_body = "03_hp/13_hermione_main/body_29.png" #Flashing Трусики
                    #__#show screen hermione_main
                    #__#with d3
                    $herView.showQQ( "body_29.png", pos )
                    her "У меня не так уж много женского очарования, но я пыталась быть милой..."
                    #__#hide screen hermione_main
                    #__#with d3
                    $herView.hideQQ()
                    #__#$ h_xpos=140 #Defines position of the Hermione's full length sprite. (Default 370). 140 - center.
                    #__#$ h_body = "03_hp/13_hermione_main/body_30.png" #Flashing Трусики
                    #__#show screen hermione_main
                    #__#with d3
                    $herView.showQQ( "body_30.png", pos )
                    her "И он просто начал смеяться прямо мне в лицо!"
                    #__#hide screen hermione_main
                    #__#with d3
                    $herView.hideQQ()
                    #__#$ h_xpos=140 #Defines position of the Hermione's full length sprite. (Default 370). 140 - center.
                    #__#$ h_body = "03_hp/13_hermione_main/body_34.png" #Flashing Трусики
                    #__#show screen hermione_main
                    #__#with d3
                    $herView.showQQ( "body_34.png", pos )
                    her "...действительно страшно видеть, как Профессор Снейп смеется..."
                    her "........"
                    her "Я ужасно заигрываю, простите, сэр..."
                    #__#hide screen hermione_main
                    #__#with d3
                    $herView.hideQQ()
                    #__#$ h_xpos=140 #Defines position of the Hermione's full length sprite. (Default 370). 140 - center.
                    #__#$ h_body = "03_hp/13_hermione_main/body_47.png" #Flashing Трусики
                    #__#show screen hermione_main
                    #__#with d3
                    $herView.showQQ( "body_47.png", pos )
                    her "Но я знаю, что Профессор Снейп тоже проворачивает \"грязные\" делишки!"
                    her "Если бы вы отправили кого-то другого к нему, то все было бы иначе!"
                    m "Кого-то другого?"
                    #__#hide screen hermione_main
                    #__#with d3
                    $herView.hideQQ()
                    #__#$ h_xpos=140 #Defines position of the Hermione's full length sprite. (Default 370). 140 - center.
                    #__#$ h_body = "03_hp/13_hermione_main/body_44.png" #Flashing Трусики
                    #__#show screen hermione_main
                    #__#with d3
                    $herView.showQQ( "body_44.png", pos )
                    her "Да! Кого-то опытного..."
                    her "Кого-то..."
                    her "Кого-то, хм..."
                    m "Распущенного?"
                    #__#hide screen hermione_main
                    #__#with d3
                    $herView.hideQQ()
                    #__#$ h_xpos=140 #Defines position of the Hermione's full length sprite. (Default 370). 140 - center.
                    #__#$ h_body = "03_hp/13_hermione_main/body_66.png" #Flashing Трусики
                    #__#show screen hermione_main
                    #__#with d3
                    $herView.showQQ( "body_66.png", pos )
                    her "Да, я полагаю..."
                    m "Не сдавайтесь, Мисс Грейнджер. Мы сделаем из тебя шлюху э-э--"
                    m "То есть женщину!"
                    #__#hide screen hermione_main
                    #__#with d3
                    $herView.hideQQ()
                    #__#$ h_xpos=140 #Defines position of the Hermione's full length sprite. (Default 370). 140 - center.
                    #__#$ h_body = "03_hp/13_hermione_main/body_79.png" #Flashing Трусики
                    #__#show screen hermione_main
                    #__#with d3
                    $herView.showQQ( "body_79.png", pos )
                    her "..................."
                    menu:
                        "\"...Но ты не получишь очки в этот раз\"":
                            #__#hide screen hermione_main
                            #__#with d3
                            $herView.hideQQ()
                            #__#$ h_xpos=140 #Defines position of the Hermione's full length sprite. (Default 370). 140 - center.
                            #__#$ h_body = "03_hp/13_hermione_main/body_12.png" #Flashing Трусики
                            #__#show screen hermione_main
                            #__#with d3
                            $herView.showQQ( "body_12.png", pos )
                            her "Но я старалась..."
                            #__#hide screen hermione_main
                            #__#with d3
                            $herView.hideQQ()
                            #__#$ h_xpos=140 #Defines position of the Hermione's full length sprite. (Default 370). 140 - center.
                            #__#$ h_body = "03_hp/13_hermione_main/body_34.png" #Flashing Трусики
                            #__#show screen hermione_main
                            #__#with d3
                            $herView.showQQ( "body_34.png", pos )
                            her "И я чувствую себя очень униженной..."
                            #__#hide screen hermione_main
                            #__#with d3
                            $herView.hideQQ()
                            #__#$ h_xpos=140 #Defines position of the Hermione's full length sprite. (Default 370). 140 - center.
                            #__#$ h_body = "03_hp/13_hermione_main/body_33.png" #Flashing Трусики
                            #__#show screen hermione_main
                            #__#with d3
                            $herView.showQQ( "body_33.png", pos )
                            her "Но я понимаю и не буду с вами спорить..."
                            call music_block
                            jump could_not_flirt_02
                        "\"Ты заслужила очки, девочка.\"":
                            pass
                elif one_out_of_three == 3: ### EVENT (C)
                    stop music fadeout 1.0
                    #__#hide screen hermione_main
                    #__#with d3
                    $herView.hideQQ()
                    #__#$ h_xpos=370 #Defines position of the Hermione's full length sprite. (Default 370). 140 - center.
                    #__#$ pos = POS_370
                    #__#$ h_body = "03_hp/13_hermione_main/body_10.png" #Flashing Трусики
                    #__#show screen hermione_main
                    #__#with d3
                    $herView.showQQ( "body_10.png", pos )
                    her "Я пыталась флиртовать с профессором Филчем, сэр..."
                    m "Понятно. {size=-5}(Понятия не имею кто это.){/size}"
                    #__#hide screen hermione_main
                    #__#with d3
                    $herView.hideQQ()
                    #__#$ h_xpos=140 #Defines position of the Hermione's full length sprite. (Default 370). 140 - center.
                    $ pos = POS_140
                    #__#$ h_body = "03_hp/13_hermione_main/body_11.png" #Flashing Трусики
                    #__#show screen hermione_main
                    #__#with d3
                    $herView.showQQ( "body_11.png", pos )
                    play music "music/Chipper Doodle v2.mp3" fadein 1 fadeout 1 # HERMIONE'S THEME.
                    her "Да, знаю, технически он не учитель..."
                    m "А?"
                    #__#hide screen hermione_main
                    #__#with d3
                    $herView.hideQQ()
                    #__#$ h_xpos=140 #Defines position of the Hermione's full length sprite. (Default 370). 140 - center.
                    #__#$ h_body = "03_hp/13_hermione_main/body_01.png" #Flashing Трусики
                    #__#show screen hermione_main
                    #__#with d3
                    $herView.showQQ( "body_01.png", pos )
                    her "Но он является частью персонала школы..."
                    her "И мы нашли общий язык с ним!"
                    her "Он на удивление милый."
                    her "Но я не знаю ничего о его \"грязных\" делах, сэр."
                    translators "Filtch - мистер Филч. Filth - грязь."
                    m "Ага... Мистер Гряз{size=+7}ик{/size} исключен из списка."
                    #__#hide screen hermione_main
                    #__#with d3
                    $herView.hideQQ()
                    #__#$ h_xpos=140 #Defines position of the Hermione's full length sprite. (Default 370). 140 - center.
                    #__#$ h_body = "03_hp/13_hermione_main/body_07.png" #Flashing Трусики
                    #__#show screen hermione_main
                    #__#with d3
                    $herView.showQQ( "body_07.png", pos )
                    her "\"Мистер Филч\", сэр..."
                    m "А я что сказал?"
                    
                    
            elif whoring >= 6 and whoring <= 8: ### LEVEL 03 <=======================================================================================EVENT LEVEL 02
                if one_out_of_three == 1: ### EVENT (A)
                    stop music fadeout 1.0
                    #__#hide screen hermione_main
                    #__#with d3
                    $herView.hideQQ()
                    #__#$ h_xpos=140 #Defines position of the Hermione's full length sprite. (Default 370). 140 - center.
                    $ pos = POS_140
                    #__#$ h_body = "03_hp/13_hermione_main/body_10.png" #Flashing Трусики
                    #__#show screen hermione_main
                    #__#with d3
                    $herView.showQQ( "body_10.png", pos )
                    her "Ну, профессор Слагхорн пригласил меня к себе..."
                    her "Профессор просто пригласил меня на чашечку чая..."
                    #__#hide screen hermione_main
                    #__#with d3
                    $herView.hideQQ()
                    #__#$ h_xpos=140 #Defines position of the Hermione's full length sprite. (Default 370). 140 - center.
                    #__#$ h_body = "03_hp/13_hermione_main/body_16.png" #Flashing Трусики
                    #__#show screen hermione_main
                    #__#with d3
                    $herView.showQQ( "body_16.png", pos )
                    play music "music/Chipper Doodle v2.mp3" fadein 1 fadeout 1 # HERMIONE'S THEME.
                    her "Там было несколько девочек..."
                    her "Но все из них были намного младше меня..."
                    #__#hide screen hermione_main
                    #__#with d3
                    $herView.hideQQ()
                    #__#$ h_xpos=140 #Defines position of the Hermione's full length sprite. (Default 370). 140 - center.
                    #__#$ h_body = "03_hp/13_hermione_main/body_17.png" #Flashing Трусики
                    #__#show screen hermione_main
                    #__#with d3
                    $herView.showQQ( "body_17.png", pos )
                    her "Почти каждая из них была первокурсницей..."
                    #__#hide screen hermione_main
                    #__#with d3
                    $herView.hideQQ()
                    #__#$ h_xpos=140 #Defines position of the Hermione's full length sprite. (Default 370). 140 - center.
                    #__#$ h_body = "03_hp/13_hermione_main/body_16.png" #Flashing Трусики
                    #__#show screen hermione_main
                    #__#with d3
                    $herView.showQQ( "body_16.png", pos )
                    her "Пы пили чай и ели печеньки..."
                    her "Все было довольно безобидно..."
                    m "Ты флиртовала с кем-то или нет?"
                    her "Флиртовала..."
                    #__#hide screen hermione_main
                    #__#with d3
                    $herView.hideQQ()
                    #__#$ h_xpos=140 #Defines position of the Hermione's full length sprite. (Default 370). 140 - center.
                    #__#$ h_body = "03_hp/13_hermione_main/body_17.png" #Flashing Трусики
                    #__#show screen hermione_main
                    #__#with d3
                    $herView.showQQ( "body_17.png", pos )
                    her "Ну, то есть, я пыталась..."
                    her "Профессор Слагхорн, кажется, более заинтересован в молодых девочках..."
                    m "Вы будто ревнуете его, Мисс Грейнджер."
                    #__#hide screen hermione_main
                    #__#with d3
                    $herView.hideQQ()
                    #__#$ h_xpos=140 #Defines position of the Hermione's full length sprite. (Default 370). 140 - center.
                    #__#$ h_body = "03_hp/13_hermione_main/body_18.png" #Flashing Трусики
                    #__#show screen hermione_main
                    #__#with d3
                    $herView.showQQ( "body_18.png", pos )
                    her "Что?!"
                    #__#hide screen hermione_main
                    #__#with d3
                    $herView.hideQQ()
                    #__#$ h_xpos=140 #Defines position of the Hermione's full length sprite. (Default 370). 140 - center.
                    #__#$ h_body = "03_hp/13_hermione_main/body_69.png" #Flashing Трусики
                    #__#show screen hermione_main
                    #__#with d3
                    $herView.showQQ( "body_69.png", pos )
                    her "Это нелепо!"
                    m "Вот ваши очки..."
                    her "...................."
          
                elif one_out_of_three == 2: ### EVENT (B)
                    play music "music/Chipper Doodle v2.mp3" fadein 1 fadeout 1 # HERMIONE'S THEME.
                    #__#hide screen hermione_main
                    #__#with d3
                    $herView.hideQQ()
                    #__#$ h_xpos=140 #Defines position of the Hermione's full length sprite. (Default 370). 140 - center.
                    $ pos = POS_140
                    #__#$ h_body = "03_hp/13_hermione_main/body_80.png" #Flashing Трусики
                    #__#show screen hermione_main
                    #__#with d3
                    $herView.showQQ( "body_80.png", pos )
                    her "Это был удивительный день, сэр!"
                    m "Ну же, расскажите, Мисс Грейнджер..."
                    #__#hide screen hermione_main
                    #__#with d3
                    $herView.hideQQ()
                    #__#$ h_xpos=140 #Defines position of the Hermione's full length sprite. (Default 370). 140 - center.
                    #__#$ h_body = "03_hp/13_hermione_main/body_68.png" #Flashing Трусики
                    #__#show screen hermione_main
                    #__#with d3
                    $herView.showQQ( "body_68.png", pos )
                    her "У меня были занятия у профессора Локонса..."
                    her "сэр Локонс, он такой милый и умный..."
                    #__#hide screen hermione_main
                    #__#with d3
                    $herView.hideQQ()
                    #__#$ h_xpos=140 #Defines position of the Hermione's full length sprite. (Default 370). 140 - center.
                    #__#$ h_body = "03_hp/13_hermione_main/body_78.png" #Flashing Трусики
                    #__#show screen hermione_main
                    #__#with d3
                    $herView.showQQ( "body_78.png", pos )
                    her "И идеальный..."
                    m "Избавьте меня от вашей школьной влюбленности, Мисс Грейнджер."
                    #__#hide screen hermione_main
                    #__#with d3
                    $herView.hideQQ()
                    #__#$ h_xpos=140 #Defines position of the Hermione's full length sprite. (Default 370). 140 - center.
                    #__#$ h_body = "03_hp/13_hermione_main/body_80.png" #Flashing Трусики
                    #__#show screen hermione_main
                    #__#with d3
                    $herView.showQQ( "body_80.png", pos )
                    her "сэр Локонс был так любезен, что дал мне свой автограф..."
                    m "Как мило с его стороны."
                    #__#hide screen hermione_main
                    #__#with d3
                    $herView.hideQQ()
                    #__#$ h_xpos=140 #Defines position of the Hermione's full length sprite. (Default 370). 140 - center.
                    #__#$ h_body = "03_hp/13_hermione_main/body_68.png" #Flashing Трусики
                    #__#show screen hermione_main
                    #__#with d3
                    $herView.showQQ( "body_68.png", pos )
                    her "Да, не могу дождаться, когда покажу его девочкам!"
                    m "Хм.. Могу я увидеть его?"
                    #__#hide screen hermione_main
                    #__#with d3
                    $herView.hideQQ()
                    #__#$ h_xpos=140 #Defines position of the Hermione's full length sprite. (Default 370). 140 - center.
                    #__#$ h_body = "03_hp/13_hermione_main/body_45.png" #Flashing Трусики
                    #__#show screen hermione_main
                    #__#with d3
                    $herView.showQQ( "body_45.png", pos )
                    her "Сэр?"
                    m "Автограф, девочка. Могу я его увидеть?"
                    #__#hide screen hermione_main
                    #__#with d3
                    $herView.hideQQ()
                    #__#$ h_xpos=140 #Defines position of the Hermione's full length sprite. (Default 370). 140 - center.
                    #__#$ h_body = "03_hp/13_hermione_main/body_44.png" #Flashing Трусики
                    #__#show screen hermione_main
                    #__#with d3
                    $herView.showQQ( "body_44.png", pos )
                    her "Ну... Эм... Он в весьма тайной зоне, сэр."
                    m "Что? Ну, следовательно у профессора Локонса есть какие-то \"грязные\" делишки!"
                    #__#hide screen hermione_main
                    #__#with d3
                    $herView.hideQQ()
                    #__#$ h_xpos=140 #Defines position of the Hermione's full length sprite. (Default 370). 140 - center.
                    #__#$ h_body = "03_hp/13_hermione_main/body_69.png" #Flashing Трусики
                    #__#show screen hermione_main
                    #__#with d3
                    $herView.showQQ( "body_69.png", pos )
                    her "Это профессор Локонс, сэр..."
                    her "И... Эм..."
                    her "Ну, это не {size=+5}настолько{/size} укромное место..."
                    m "Покажи его мне!"
                    #__#hide screen hermione_main
                    #__#with d3
                    $herView.hideQQ()
                    #__#$ h_xpos=140 #Defines position of the Hermione's full length sprite. (Default 370). 140 - center.
                    #__#$ h_body = "03_hp/13_hermione_main/body_66.png" #Flashing Трусики
                    #__#show screen hermione_main
                    #__#with d3
                    $herView.showQQ( "body_66.png", pos )
                    her "Нет, сэр! Это было бы неуместно!"
                    menu: 
                        "{size=-3}\"Профессор Локонс вылетит из школы в ближайшее время!\"{/size}":
                            #__#hide screen hermione_main
                            #__#with d3
                            $herView.hideQQ()
                            #__#$ h_xpos=140 #Defines position of the Hermione's full length sprite. (Default 370). 140 - center.
                            #__#$ h_body = "03_hp/13_hermione_main/body_72.png" #Flashing Трусики
                            #__#show screen hermione_main
                            #__#with d3
                            $herView.showQQ( "body_72.png", pos )
                            her "Из-за меня?"
                            #__#hide screen hermione_main
                            #__#with d3
                            $herView.hideQQ()
                            #__#$ h_xpos=140 #Defines position of the Hermione's full length sprite. (Default 370). 140 - center.
                            #__#$ h_body = "03_hp/13_hermione_main/body_67.png" #Flashing Трусики
                            #__#show screen hermione_main
                            #__#with d3
                            $herView.showQQ( "body_67.png", pos )
                            her "Сэр, пожалуйста!"
                            m "Покажи мне!"
                            #__#hide screen hermione_main
                            #__#with d3
                            $herView.hideQQ()
                            #__#$ h_xpos=140 #Defines position of the Hermione's full length sprite. (Default 370). 140 - center.
                            #__#$ h_body = "03_hp/13_hermione_main/body_32.png" #Flashing Трусики
                            #__#show screen hermione_main
                            #__#with d3
                            $herView.showQQ( "body_32.png", pos )
                            her "Нет, мне стыдно!"
                            menu:
                                "\"Ладно. Вот твои очки.\"":
                                    #__#hide screen hermione_main
                                    #__#with d3
                                    $herView.hideQQ()
                                    #__#$ h_xpos=140 #Defines position of the Hermione's full length sprite. (Default 370). 140 - center.
                                    #__#$ h_body = "03_hp/13_hermione_main/body_74.png" #Flashing Трусики
                                    #__#show screen hermione_main
                                    #__#with d3
                                    $herView.showQQ( "body_74.png", pos )
                                    her "Спасибо за понимание, сэр."
                                "\"Покажи мне, или ты не получишь ничего!\"":
                                    #__#hide screen hermione_main
                                    #__#with d3
                                    $herView.hideQQ()
                                    #__#$ h_xpos=140 #Defines position of the Hermione's full length sprite. (Default 370). 140 - center.
                                    #__#$ h_body = "03_hp/13_hermione_main/body_72.png" #Flashing Трусики
                                    #__#show screen hermione_main
                                    #__#with d3
                                    $herView.showQQ( "body_72.png", pos )
                                    her "Что?!"
                                    #__#hide screen hermione_main
                                    #__#with d3
                                    $herView.hideQQ()
                                    #__#$ h_xpos=140 #Defines position of the Hermione's full length sprite. (Default 370). 140 - center.
                                    #__#$ h_body = "03_hp/13_hermione_main/body_73.png" #Flashing Трусики
                                    #__#show screen hermione_main
                                    #__#with d3
                                    $herView.showQQ( "body_73.png", pos )
                                    her "..............."
                                    #__#hide screen hermione_main
                                    #__#with d3
                                    $herView.hideQQ()
                                    #__#$ h_xpos=140 #Defines position of the Hermione's full length sprite. (Default 370). 140 - center.
                                    #__#$ h_body = "03_hp/13_hermione_main/body_29.png" #Flashing Трусики
                                    #__#show screen hermione_main
                                    #__#with d3
                                    $herView.showQQ( "body_29.png", pos )
                                    her ".................."
                                    #__#hide screen hermione_main
                                    #__#with d3
                                    $herView.hideQQ()
                                    #__#$ h_xpos=140 #Defines position of the Hermione's full length sprite. (Default 370). 140 - center.
                                    #__#$ h_body = "03_hp/13_hermione_main/body_47.png" #Flashing Трусики
                                    #__#show screen hermione_main
                                    #__#with d3
                                    $herView.showQQ( "body_47.png", pos )
                                    her "Ну, ладно, но только, чтобы очистить имя моего кумира..."
                                    #__#hide screen hermione_main
                                    #__#with d3
                                    $herView.hideQQ()
                                    show screen blktone8
                                    with d5
                                    #__#her_12 "Вот...."
                                    $her_head_state = 12
                                    her_head_main "Вот...."
                                    m "Хм..."
                                    hide screen blktone8 
                                    with d5
                                    #__#$ only_upper = True #Skirt lifted.          WARNING_Z
                                    #__#$ autograph = True #Autograph shown.
                                    #__#$ h_xpos=140 #Defines position of the Hermione's full length sprite. (Default 370). 140 - center.
                                    #__#$ h_body = "03_hp/13_hermione_main/body_51.png" #Flashing Трусики
                                    #__#show screen hermione_main
                                    
                                    $herView.data().saveState()
                                    # add pose with lifted skirt and authograph
                                    $herView.data().addPose( CharacterExItemSkirtLifted( herView.mPoseFolder, 'pose_skirt_up.png', G_Z_POSE ) )
                                    $herView.data().addItem( 'autograph', CharacterExItem( herView.mMiscFolder, 'autograph.png', G_Z_LEGS + 1 ) )
                                    
                                    $herView.showQ( "body_51.png", pos )
                                    hide screen ctc
                                    show screen ctc
                                    with d3
                                    pause
                                    #__#hide screen hermione_main
                                    #__#with d3
                                    $herView.hideQQ()
                                    #__#$ h_body = "03_hp/13_hermione_main/body_50.png" #Flashing Трусики
                                    #__#show screen hermione_main
                                    #__#with d3
                                    $herView.showQQ( "body_50.png", pos )
                                    her "Как вы понимаете, профессор Локонс очень смелый и воплощает в себе все чистое."
                                    pause
                                    m "Что мне теперь делать?"
                                    her "Можете не беспокоиться об этом, сэр."
                                    her "Он не один из \"пошлых\" учителей."
                                    m "Ах, да какое мне дело..."
                                    #__#hide screen hermione_main
                                    #__#with d3     
                                    $herView.hideQQ()
                                    #__#$ h_body = "03_hp/13_hermione_main/body_51.png" #Flashing Трусики
                                    #__#show screen hermione_main
                                    #__#with d3
                                    $herView.showQQ( "body_51.png", pos )
                                    her "............?"
                                    #__#hide screen hermione_main 
                                    #__#with d3
                                    $herView.hideQQ()
                                    
                                    # load before pose
                                    $herView.data().loadState()
                                    
                                    #__#$ only_upper = False #Skirt lifted.         WARNING_Z
                                    #__#$ autograph = False #Autograph shown.
                                    #__#$ h_xpos=140 #Defines position of the Hermione's full length sprite. (Default 370). 140 - center.
                                    #__#$ h_body = "03_hp/13_hermione_main/body_47.png" #Flashing Трусики
                                    #__#show screen hermione_main
                                    $herView.showQ( "body_47.png", pos, fade )
                                    pause
                                    hide screen ctc
                                    $ mad += 18
                        "\"Ладно... Вот твои очки.\"":
                            #__#hide screen hermione_main
                            #__#with d3
                            $herView.hideQQ()
                            #__#$ h_xpos=140 #Defines position of the Hermione's full length sprite. (Default 370). 140 - center.
                            #__#$ h_body = "03_hp/13_hermione_main/body_74.png" #Flashing Трусики
                            #__#show screen hermione_main
                            #__#with d3
                            $herView.showQQ( "body_74.png", pos )
                            her "Спасибо за понимание, профессор."
                            
                elif one_out_of_three == 3: ### EVENT (C)
                    play music "music/Chipper Doodle v2.mp3" fadein 1 fadeout 1 # HERMIONE'S THEME.
                    #__#hide screen hermione_main
                    #__#with d3
                    $herView.hideQQ()
                    #__#$ h_xpos=370 #Defines position of the Hermione's full length sprite. (Default 370). 140 - center.
                    $ pos = POS_370
                    #__#$ h_body = "03_hp/13_hermione_main/body_15.png" #Flashing Трусики
                    #__#show screen hermione_main
                    #__#with d3
                    $herView.showQQ( "body_15.png", pos )
                    her "Ну, сегодня я некоторое время заигрывала с мистером Филчем."
                    #__#hide screen hermione_main
                    #__#with d3
                    $herView.hideQQ()
                    #__#$ h_xpos=370 #Defines position of the Hermione's full length sprite. (Default 370). 140 - center.
                    #__#$ h_body = "03_hp/13_hermione_main/body_16.png" #Flashing Трусики
                    #__#show screen hermione_main
                    #__#with d3
                    $herView.showQQ( "body_16.png", pos )
                    her "Ну, мистел Филч очень начитанный и обладает манерами."
                    m "........"
                    #__#hide screen hermione_main
                    #__#with d3
                    $herView.hideQQ()
                    #__#$ h_xpos=370 #Defines position of the Hermione's full length sprite. (Default 370). 140 - center.
                    #__#$ h_body = "03_hp/13_hermione_main/body_13.png" #Flashing Трусики
                    #__#show screen hermione_main
                    #__#with d3
                    $herView.showQQ( "body_13.png", pos )
                    her "Не думаю, что кто-то знает его таким..."
                    her "Не думаю, что кто-то знает мистера Филча так, как я."
                    #__#hide screen hermione_main
                    #__#with d3
                    $herView.hideQQ()
                    #__#$ h_xpos=370 #Defines position of the Hermione's full length sprite. (Default 370). 140 - center.
                    #__#$ h_body = "03_hp/13_hermione_main/body_06.png" #Flashing Трусики
                    #__#show screen hermione_main
                    #__#with d3
                    $herView.showQQ( "body_06.png", pos )
                    her "Я чувствую, что со мной он очень открыт, сэр."
                    m "Ладно..."
                    m "Этот, мистер Фли{size=+7}нт{/size}--"
                    #__#hide screen hermione_main
                    #__#with d3
                    $herView.hideQQ()
                    $ h_xpos=370 #Defines position of the Hermione's full length sprite. (Default 370). 140 - center.
                    #__#$ h_body = "03_hp/13_hermione_main/body_04.png" #Flashing Трусики
                    #__#show screen hermione_main
                    #__#with d3
                    $herView.showQQ( "body_04.png", pos )
                    her "Мистер Филч, сэр."
                    m "Да, не важно... Он учитель?"
                    her "Мистер Филч? Учитель? Нет, сэр..."
                    #__#hide screen hermione_main
                    #__#with d3
                    $herView.hideQQ()
                    #__#$ h_xpos=370 #Defines position of the Hermione's full length sprite. (Default 370). 140 - center.
                    #__#$ h_body = "03_hp/13_hermione_main/body_06.png" #Flashing Трусики
                    #__#show screen hermione_main
                    #__#with d3
                    $herView.showQQ( "body_06.png", pos )
                    her "Он смотритель..."
                    m "Смотритель...?"
                    m "Ты имеешь в виду - дворник?"
                    #__#hide screen hermione_main
                    #__#with d3
                    $herView.hideQQ()
                    #__#$ h_xpos=370 #Defines position of the Hermione's full length sprite. (Default 370). 140 - center.
                    #__#$ h_body = "03_hp/13_hermione_main/body_10.png" #Flashing Трусики
                    #__#show screen hermione_main
                    #__#with d3
                    $herView.showQQ( "body_10.png", pos )
                    her "Ну..."
                    m "Мисс Грейнджер, я не посылал вас очаровывать дворников!"
                    #__#hide screen hermione_main
                    #__#with d3
                    $herView.hideQQ()
                    #__#$ h_xpos=370 #Defines position of the Hermione's full length sprite. (Default 370). 140 - center.
                    #__#$ h_body = "03_hp/13_hermione_main/body_14.png" #Flashing Трусики
                    #__#show screen hermione_main
                    #__#with d3
                    $herView.showQQ( "body_14.png", pos )
                    her "Но мистер Филч является частью школьного персонала, сэр!"
                    menu:
                        "\"Просто бери свои очки и уходи!\"":
                            #__#hide screen hermione_main
                            #__#with d3
                            $herView.hideQQ()
                            #__#$ h_xpos=370 #Defines position of the Hermione's full length sprite. (Default 370). 140 - center.
                            #__#$ h_body = "03_hp/13_hermione_main/body_03.png" #Flashing Трусики
                            #__#show screen hermione_main
                            #__#with d3
                            $herView.showQQ( "body_03.png", pos )
                            her "........................."
                        "\"Задание провалено! Ты не получишь очки!\"":
                            $ mad +=15
                            #__#hide screen hermione_main
                            #__#with d3
                            $herView.hideQQ()
                            #__#$ h_xpos=370 #Defines position of the Hermione's full length sprite. (Default 370). 140 - center.
                            #__#$ h_body = "03_hp/13_hermione_main/body_07.png" #Flashing Трусики
                            #__#show screen hermione_main
                            #__#with d3
                            $herView.showQQ( "body_07.png", pos )
                            her "Но профессор?"
                            m "Вы провалились, Мисс Грейнджер."
                            #__#hide screen hermione_main
                            #__#with d3
                            $herView.hideQQ()
                            #__#$ h_xpos=370 #Defines position of the Hermione's full length sprite. (Default 370). 140 - center.
                            #__#$ h_body = "03_hp/13_hermione_main/body_05.png" #Flashing Трусики
                            #__#show screen hermione_main
                            #__#with d3
                            $herView.showQQ( "body_05.png", pos )
                            her "........................................."
                            jump could_not_flirt_02


            elif whoring >= 9: # LEVEL 04 and higher.
                if one_out_of_three == 1: ### EVENT (A) LEVEL04 <============================================================================
                    stop music fadeout 1.0
                    #__#hide screen hermione_main
                    #__#with d3
                    $herView.hideQQ()
                    #__#$ h_xpos=370 #Defines position of the Hermione's full length sprite. (Default 370). 140 - center.
                    #__#$ pos = POS_370
                    #__#$ h_body = "03_hp/13_hermione_main/body_33.png" #Flashing Трусики
                    #__#show screen hermione_main
                    #__#with d3
                    $herView.showQQ( "body_33.png", pos )
                    her "............................."
                    her "....................................."
                    m "Мисс Грейнджер?"
                    #__#hide screen hermione_main
                    #__#with d3
                    $herView.hideQQ()
                    #__#$ h_xpos=370 #Defines position of the Hermione's full length sprite. (Default 370). 140 - center.
                    #__#$ h_body = "03_hp/13_hermione_main/body_34.png" #Flashing Трусики
                    #__#show screen hermione_main
                    #__#with d3
                    $herView.showQQ( "body_34.png", pos )
                    her "Профессор, Я....."
                    m "Что такое? Что произошло?"
                    #__#hide screen hermione_main
                    #__#with d3
                    $herView.hideQQ()
                    #__#$ h_xpos=370 #Defines position of the Hermione's full length sprite. (Default 370). 140 - center.
                    #__#$ h_body = "03_hp/13_hermione_main/body_29.png" #Flashing Трусики
                    #__#show screen hermione_main
                    #__#with d3
                    $herView.showQQ( "body_29.png", pos )
                    her "Ну..."
                    her "Мистер Филч, сэр..."
                    m "Дворник?"
                    #__#hide screen hermione_main
                    #__#with d3
                    $herView.hideQQ()
                    #__#$ h_xpos=370 #Defines position of the Hermione's full length sprite. (Default 370). 140 - center.
                    #__#$ h_body = "03_hp/13_hermione_main/body_31.png" #Flashing Трусики
                    #__#show screen hermione_main
                    #__#with d3
                    $herView.showQQ( "body_31.png", pos )
                    her "Я с ним немного флиртовала..."
                    her "И вначале все было отлично..."
                    #__#hide screen hermione_main
                    #__#with d3
                    $herView.hideQQ()
                    #__#$ h_xpos=370 #Defines position of the Hermione's full length sprite. (Default 370). 140 - center.
                    #__#$ h_body = "03_hp/13_hermione_main/body_29.png" #Flashing Трусики
                    #__#show screen hermione_main
                    #__#with d3
                    $herView.showQQ( "body_29.png", pos )
                    her "......................."
                    m "................?"
                    #__#hide screen hermione_main
                    #__#with d3
                    $herView.hideQQ()
                    #__#$ h_xpos=370 #Defines position of the Hermione's full length sprite. (Default 370). 140 - center.
                    #__#$ h_body = "03_hp/13_hermione_main/body_31.png" #Flashing Трусики
                    #__#show screen hermione_main
                    #__#with d3
                    $herView.showQQ( "body_31.png", pos )
                    her "А потом..."
                    #__#hide screen hermione_main
                    #__#with d3
                    $herView.hideQQ()
                    #__#$ h_xpos=370 #Defines position of the Hermione's full length sprite. (Default 370). 140 - center.
                    #__#$ h_body = "03_hp/13_hermione_main/body_29.png" #Flashing Трусики
                    #__#show screen hermione_main
                    #__#with d3
                    $herView.showQQ( "body_29.png", pos )
                    her "Не уверена, должна ли я..."
                    m "Мисс Грейнджер, если вы не хотите говорить, можете уйти."
                    #__#hide screen hermione_main
                    #__#with d3
                    $herView.hideQQ()
                    #__#$ h_xpos=370 #Defines position of the Hermione's full length sprite. (Default 370). 140 - center.
                    #__#$ h_body = "03_hp/13_hermione_main/body_32.png" #Flashing Трусики
                    #__#show screen hermione_main
                    #__#with d3
                    $herView.showQQ( "body_32.png", pos )
                    play music "music/Chipper Doodle v2.mp3" fadein 1 fadeout 1 # HERMIONE'S THEME.
                    her "Он показал мне свою \"штучку\", сэр!"
                    m "Его - что?"
                    #__#hide screen hermione_main
                    #__#with d3
                    $herView.hideQQ()
                    #__#$ h_xpos=370 #Defines position of the Hermione's full length sprite. (Default 370). 140 - center.
                    #__#$ h_body = "03_hp/13_hermione_main/body_34.png" #Flashing Трусики
                    #__#show screen hermione_main
                    #__#with d3
                    $herView.showQQ( "body_34.png", pos )
                    her "Его... мужское начало, сэр."
                    g9 "Так держать, парень-дворник!"
                    #__#hide screen hermione_main
                    #__#with d3
                    $herView.hideQQ()
                    #__#$ h_xpos=370 #Defines position of the Hermione's full length sprite. (Default 370). 140 - center.
                    #__#$ h_body = "03_hp/13_hermione_main/body_72.png" #Flashing Трусики
                    #__#show screen hermione_main
                    #__#with d3
                    $herView.showQQ( "body_72.png", pos )
                    her "Что?!"
                    m "*Кхм* То есть - это возмутимо!"
                    #__#hide screen hermione_main
                    #__#with d3
                    $herView.hideQQ()
                    #__#$ h_xpos=370 #Defines position of the Hermione's full length sprite. (Default 370). 140 - center.
                    #__#$ h_body = "03_hp/13_hermione_main/body_21.png" #Flashing Трусики
                    #__#show screen hermione_main
                    #__#with d3
                    $herView.showQQ( "body_21.png", pos )
                    her "Да... Мерзкий, кривой, весь в венах..."
                    m "Избавьте меня от ужасных подробностей, девушка."
                    #__#hide screen hermione_main
                    #__#with d3
                    $herView.hideQQ()
                    #__#$ h_xpos=370 #Defines position of the Hermione's full length sprite. (Default 370). 140 - center.
                    #__#$ h_body = "03_hp/13_hermione_main/body_20.png" #Flashing Трусики
                    #__#show screen hermione_main
                    #__#with d3
                    $herView.showQQ( "body_20.png", pos )
                    her "Зачем он вообще сделал это?"
                    her "Только что мы говорили, как вдруг..."
                    m "Ну, ваша благородная жертва не должна остаться незамеченной, Мисс Грейнджер!"
                    m "Пятнадцать очков \"Грифф--"
                    #__#hide screen hermione_main
                    #__#with d3
                    $herView.hideQQ()
                    #__#$ h_xpos=370 #Defines position of the Hermione's full length sprite. (Default 370). 140 - center.
                    #__#$ h_body = "03_hp/13_hermione_main/body_19.png" #Flashing Трусики
                    #__#show screen hermione_main
                    #__#with d3
                    $herView.showQQ( "body_19.png", pos )
                    her "Профессор Дамблдор, пожалуйста подождите."
                    m "А?"
                    #__#hide screen hermione_main
                    #__#with d3
                    $herView.hideQQ()
                    #__#$ h_xpos=370 #Defines position of the Hermione's full length sprite. (Default 370). 140 - center.
                    #__#$ h_body = "03_hp/13_hermione_main/body_31.png" #Flashing Трусики
                    #__#show screen hermione_main
                    #__#with d3
                    $herView.showQQ( "body_31.png", pos )
                    her "Ну, вы не собираетесь что-то с этим сделать?"
                    m "Ну..."
                    #__#hide screen hermione_main
                    #__#with d3
                    $herView.hideQQ()
                    #__#$ h_xpos=370 #Defines position of the Hermione's full length sprite. (Default 370). 140 - center.
                    #__#$ h_body = "03_hp/13_hermione_main/body_47.png" #Flashing Трусики
                    #__#show screen hermione_main
                    #__#with d3
                    $herView.showQQ( "body_47.png", pos )
                    her "Что если я не первая жертва..?"
                    her "Какой-нибудь первокур может получить травму на всю жизнь!"
                    m "Действительно может?"
                    #__#hide screen hermione_main
                    #__#with d3
                    $herView.hideQQ()
                    #__#$ h_xpos=370 #Defines position of the Hermione's full length sprite. (Default 370). 140 - center.
                    #__#$ h_body = "03_hp/13_hermione_main/body_31.png" #Flashing Трусики
                    #__#show screen hermione_main
                    #__#with d3
                    $herView.showQQ( "body_31.png", pos )
                    her "Это значит, что вы примете меры, сэр?"
                    m "Эм... Да, конечно..."
                    m "Занесу его в свой \"список\"..."
                    m "\"Позаботиться о дворнике и его жутко кривом члене.\"..."
                    m "Да, завтра же, в первую очередь."
                    #__#hide screen hermione_main
                    #__#with d3
                    $herView.hideQQ()
                    #__#$ h_xpos=370 #Defines position of the Hermione's full length sprite. (Default 370). 140 - center.
                    #__#$ h_body = "03_hp/13_hermione_main/body_16.png" #Flashing Трусики
                    #__#show screen hermione_main
                    #__#with d3
                    $herView.showQQ( "body_16.png", pos )
                    her "Спасибо сэр."
                    #__#hide screen hermione_main
                    #__#with d3
                    $herView.hideQQ()
                    #__#$ h_xpos=370 #Defines position of the Hermione's full length sprite. (Default 370). 140 - center.
                    #__#$ h_body = "03_hp/13_hermione_main/body_75.png" #Flashing Трусики
                    #__#show screen hermione_main
                    #__#with d3
                    $herView.showQQ( "body_75.png", pos )
                    her "Могу я получить свои очки?"
    
                elif one_out_of_three == 2: ### EVENT (B)
                    play music "music/Chipper Doodle v2.mp3" fadein 1 fadeout 1 # HERMIONE'S THEME.
                    #__#hide screen hermione_main
                    #__#with d3
                    $herView.hideQQ()
                    #__#$ h_xpos=370 #Defines position of the Hermione's full length sprite. (Default 370). 140 - center.
                    #__#$ pos = POS_370
                    #__#$ h_body = "03_hp/13_hermione_main/body_76.png" #Flashing Трусики
                    #__#show screen hermione_main
                    #__#with d3
                    $herView.showQQ( "body_76.png", pos )
                    her "Профессор Снейп!"
                    m "Эм... Ага, Я, вообще-то, Дамблдор, вроде как..."
                    #__#hide screen hermione_main
                    #__#with d3
                    $herView.hideQQ()
                    
                    g4 "{size=-5}(Стоп, может {size=+7}он{/size} сменил мою маскировку?){/size}"
                    g4 "{size=-5}(Значит, теперь я выгляжу как Профессор Снейп?){/size}"
                    g4 "{size=-5}(Во имя великих песков пустыни! Акабур, тебе следует сдерживать себя!){/size}"
                    a5 "{size=-5}(Нужно было сначала послушать девочку. Блин...){/size}"
                    #__#hide screen hermione_main
                    #__#with d3
                    $herView.hideQQ()
                    #__#$ h_xpos=370 #Defines position of the Hermione's full length sprite. (Default 370). 140 - center.
                    #__#$ h_body = "03_hp/13_hermione_main/body_02.png" #Flashing Трусики
                    #__#show screen hermione_main
                    #__#with d3
                    $herView.showQQ( "body_02.png", pos )
                    her "Профессор? С кем вы говорили?"
                    m "Эм... Я связался с духами из другого измерения..."
                    #__#hide screen hermione_main
                    #__#with d3
                    $herView.hideQQ()
                    #__#$ h_xpos=370 #Defines position of the Hermione's full length sprite. (Default 370). 140 - center.
                    #__#$ h_body = "03_hp/13_hermione_main/body_17.png" #Flashing Трусики
                    #__#show screen hermione_main
                    #__#with d3
                    $herView.showQQ( "body_17.png", pos )
                    her ".....??!"
                    #__#hide screen hermione_main
                    #__#with d3
                    $herView.hideQQ()
                    a6 "{size=-5}(Придерживайся сценария, придурок!){/size}"
                    g4 "Да, очень раздражительный дух ... Раздражительный и немой!"
                    a6 "{size=-5}(Ты......!){/size}"
                    #__#hide screen hermione_main
                    #__#with d3
                    $herView.hideQQ()
                    #__#$ h_xpos=370 #Defines position of the Hermione's full length sprite. (Default 370). 140 - center.
                    #__#$ h_body = "03_hp/13_hermione_main/body_02.png" #Flashing Трусики
                    #__#show screen hermione_main
                    #__#with d3
                    $herView.showQQ( "body_02.png", pos )
                    her "Профессор Дамблдор, пожалуйста, выслушайте меня!"
                    m "Да, да, девочка. Я слушаю."
                    #__#hide screen hermione_main
                    #__#with d3
                    $herView.hideQQ()
                    #__#$ h_xpos=370 #Defines position of the Hermione's full length sprite. (Default 370). 140 - center.
                    #__#$ h_body = "03_hp/13_hermione_main/body_04.png" #Flashing Трусики
                    #__#show screen hermione_main
                    #__#with d3
                    $herView.showQQ( "body_04.png", pos )
                    her "Я нашла подтверждение тому, что профессор Снейп коррумпирован и имеет \"грязные\" дела, сэр!"
                    m "Расскажи, что произошло."
                    #__#hide screen hermione_main
                    #__#with d3
                    $herView.hideQQ()
                    #__#$ h_xpos=370 #Defines position of the Hermione's full length sprite. (Default 370). 140 - center.
                    #__#$ h_body = "03_hp/13_hermione_main/body_02.png" #Flashing Трусики
                    #__#show screen hermione_main
                    #__#with d3
                    $herView.showQQ( "body_02.png", pos )
                    her "ну, сегодня во время занятий..."
                    her "Я делала все возможное, чтобы привлечь внимание профессора Снейпа..."
                    her "Я \"мечтательно\" пялилась на него..."
                    her "И следила за его членом..."
                    m "Ты..."
                    m "Смотрела в сторону его члена?"
                    #__#hide screen hermione_main
                    #__#with d3
                    $herView.hideQQ()
                    #__#$ h_xpos=370 #Defines position of the Hermione's full length sprite. (Default 370). 140 - center.
                    #__#$ h_body = "03_hp/13_hermione_main/body_04.png" #Flashing Трусики
                    #__#show screen hermione_main
                    #__#with d3
                    $herView.showQQ( "body_04.png", pos )
                    her "Да... Я имею в виду, когда вы смотрите туда и хотите кое-что от него..."
                    m "Откуда ты знаешь о таком?"
                    #__#hide screen hermione_main
                    #__#with d3
                    $herView.hideQQ()
                    #__#$ h_xpos=370 #Defines position of the Hermione's full length sprite. (Default 370). 140 - center.
                    #__#$ h_body = "03_hp/13_hermione_main/body_10.png" #Flashing Трусики
                    #__#show screen hermione_main
                    #__#with d3
                    $herView.showQQ( "body_10.png", pos )
                    her "Женские журналы..."
                    #__#hide screen hermione_main
                    #__#with d3
                    $herView.hideQQ()
                    #__#$ h_xpos=370 #Defines position of the Hermione's full length sprite. (Default 370). 140 - center.
                    #__#$ h_body = "03_hp/13_hermione_main/body_07.png" #Flashing Трусики
                    #__#show screen hermione_main
                    #__#with d3
                    $herView.showQQ( "body_07.png", pos )
                    her "Ну, не важно, это сработало, сэр."
                    #__#hide screen hermione_main
                    #__#with d3
                    $herView.hideQQ()
                    #__#$ h_xpos=370 #Defines position of the Hermione's full length sprite. (Default 370). 140 - center.
                    #__#$ h_body = "03_hp/13_hermione_main/body_47.png" #Flashing Трусики
                    #__#show screen hermione_main
                    #__#with d3
                    $herView.showQQ( "body_47.png", pos )
                    her "Когда занятия закончились, Профессор Снейп схватил меня за попку, сэр!"
                    m "Дьявол!"
                    m "Тебе понравилось, не так ли?"
                    #__#hide screen hermione_main
                    #__#with d3
                    $herView.hideQQ()
                    #__#$ h_xpos=370 #Defines position of the Hermione's full length sprite. (Default 370). 140 - center.
                    #__#$ h_body = "03_hp/13_hermione_main/body_30.png" #Flashing Трусики
                    #__#show screen hermione_main
                    #__#with d3
                    $herView.showQQ( "body_30.png", pos )
                    her "Сэр, я делаю это только для--"
                    m "Только \"во имя чести \"Гриффиндора\" и все такое. Да, помню."
                    m "Вот твои очки."
                    #__#hide screen hermione_main
                    #__#with d3
                    $herView.hideQQ()
                    #__#$ h_xpos=370 #Defines position of the Hermione's full length sprite. (Default 370). 140 - center.
                    #__#$ h_body = "03_hp/13_hermione_main/body_66.png" #Flashing Трусики
                    #__#show screen hermione_main
                    #__#with d3
                    $herView.showQQ( "body_66.png", pos )
  
                elif one_out_of_three == 3: ### EVENT (C)
                    stop music fadeout 1.0
                    #__#hide screen hermione_main
                    #__#with d3
                    $herView.hideQQ()
                    #__#$ h_xpos=370 #Defines position of the Hermione's full length sprite. (Default 370). 140 - center.
                    #__#$ pos = POS_370
                    #__#$ h_body = "03_hp/13_hermione_main/body_09.png" #Flashing Трусики
                    #__#show screen hermione_main
                    #__#with d3
                    $herView.showQQ( "body_09.png", pos )
                    her "Профессор Локонс!"
                    m "Ага! Добавим его в \"список непослушных\"!"
                    #__#hide screen hermione_main
                    #__#with d3
                    $herView.hideQQ()
                    #__#$ h_xpos=370 #Defines position of the Hermione's full length sprite. (Default 370). 140 - center.
                    #__#$ h_body = "03_hp/13_hermione_main/body_11.png" #Flashing Трусики
                    #__#show screen hermione_main
                    #__#with d3
                    $herView.showQQ( "body_11.png", pos )
                    her "Нет, сэр, это не то..."
                    #__#hide screen hermione_main
                    #__#with d3
                    $herView.hideQQ()
                    #__#$ h_xpos=370 #Defines position of the Hermione's full length sprite. (Default 370). 140 - center.
                    #__#$ h_body = "03_hp/13_hermione_main/body_12.png" #Flashing Трусики
                    #__#show screen hermione_main
                    #__#with d3
                    $herView.showQQ( "body_12.png", pos )
                    her "Или..."
                    her "Я не уверена..."
                    #__#hide screen hermione_main
                    #__#with d3
                    $herView.hideQQ()
                    #__#$ h_xpos=370 #Defines position of the Hermione's full length sprite. (Default 370). 140 - center.
                    #__#$ h_body = "03_hp/13_hermione_main/body_11.png" #Flashing Трусики
                    #__#show screen hermione_main
                    #__#with d3
                    $herView.showQQ( "body_11.png", pos )
                    her "Раньше я его обожала..."
                    #__#hide screen hermione_main
                    #__#with d3
                    $herView.hideQQ()
                    #__#$ h_xpos=370 #Defines position of the Hermione's full length sprite. (Default 370). 140 - center.
                    #__#$ h_body = "03_hp/13_hermione_main/body_13.png" #Flashing Трусики
                    #__#show screen hermione_main
                    #__#with d3
                    $herView.showQQ( "body_13.png", pos )
                    her "Но он..."
                    her "Он просто..."
                    #__#hide screen hermione_main
                    #__#with d3
                    $herView.hideQQ()
                    #__#$ h_xpos=370 #Defines position of the Hermione's full length sprite. (Default 370). 140 - center.
                    #__#$ h_body = "03_hp/13_hermione_main/body_20.png" #Flashing Трусики
                    #__#show screen hermione_main
                    #__#with d3
                    $herView.showQQ( "body_20.png", pos )
                    her "Как это возможно?"
                    her "Я не могу поверить в это..."
                    #__#hide screen hermione_main
                    #__#with d3
                    $herView.hideQQ()
                    play music "music/(Orchestral) Playful Tension by Shadow16nh.mp3" fadein 1 fadeout 1 # SEX THEME.
                    m "{size=-4}(Арх! Ожидание убивает меня!){/size}" 
                    m "{size=-4}(Может он заставил ее сосать?){/size}"
                    m "{size=-4}(Или, может, изнасиловал?){/size}"
                    g4 "Что такое, девочка? Говори!"
                    #__#hide screen hermione_main
                    #__#with d3
                    $herView.hideQQ()
                    #__#$ h_xpos=370 #Defines position of the Hermione's full length sprite. (Default 370). 140 - center.
                    #__#$ h_body = "03_hp/13_hermione_main/body_14.png" #Flashing Трусики
                    #__#show screen hermione_main
                    #__#with d3
                    $herView.showQQ( "body_14.png", pos )
                    her "А?"
                    m "Что профессор Локонс сделал с тобой?"
                    #__#hide screen hermione_main
                    #__#with d3
                    $herView.hideQQ()
                    #__#$ h_xpos=370 #Defines position of the Hermione's full length sprite. (Default 370). 140 - center.
                    #__#$ h_body = "03_hp/13_hermione_main/body_13.png" #Flashing Трусики
                    #__#show screen hermione_main
                    #__#with d3
                    $herView.showQQ( "body_13.png", pos )
                    her "Эм... Ничего, сэр..."
                    m "Ничего?!"
                    #__#hide screen hermione_main
                    #__#with d3
                    $herView.hideQQ()
                    #__#$ h_xpos=370 #Defines position of the Hermione's full length sprite. (Default 370). 140 - center.
                    #__#$ h_body = "03_hp/13_hermione_main/body_11.png" #Flashing Трусики
                    #__#show screen hermione_main
                    #__#with d3
                    $herView.showQQ( "body_11.png", pos )
                    her "Да. Я, конечно, загнала его в угол сегодня..."
                    #__#hide screen hermione_main
                    #__#with d3
                    $herView.hideQQ()
                    #__#$ h_xpos=370 #Defines position of the Hermione's full length sprite. (Default 370). 140 - center.
                    #__#$ h_body = "03_hp/13_hermione_main/body_31.png" #Flashing Трусики
                    #__#show screen hermione_main
                    #__#with d3
                    $herView.showQQ( "body_31.png", pos )
                    her "И еще могла выглядеть доступной для него..."
                    m "Серьезно?"
                    #__#hide screen hermione_main
                    #__#with d3
                    $herView.hideQQ()
                    #__#$ h_xpos=370 #Defines position of the Hermione's full length sprite. (Default 370). 140 - center.
                    #__#$ h_body = "03_hp/13_hermione_main/body_34.png" #Flashing Трусики
                    #__#show screen hermione_main
                    #__#with d3
                    $herView.showQQ( "body_34.png", pos )
                    her "Да... Не уверена, что он хотел от меня, сэр..."
                    m "Ну же, Мисс Грейнджер!"
                    #__#hide screen hermione_main
                    #__#with d3
                    $herView.hideQQ()
                    #__#$ h_xpos=370 #Defines position of the Hermione's full length sprite. (Default 370). 140 - center.
                    #__#$ h_body = "03_hp/13_hermione_main/body_32.png" #Flashing Трусики
                    #__#show screen hermione_main
                    #__#with d3
                    $herView.showQQ( "body_32.png", pos )
                    her "Выслушайте меня сначала, пожалуйста!"
                    m "Мои извинения. Продолжай."
                    #__#hide screen hermione_main
                    #__#with d3
                    $herView.hideQQ()
                    #__#$ h_xpos=370 #Defines position of the Hermione's full length sprite. (Default 370). 140 - center.
                    #__#$ h_body = "03_hp/13_hermione_main/body_14.png" #Flashing Трусики
                    #__#show screen hermione_main
                    #__#with d3
                    $herView.showQQ( "body_14.png", pos )
                    her "Ну, обычно профессор Локонс ведет себя как джентельмен..."
                    her "И... и я просто хотела очистить его имя от всех этих подозрений раз и навсегда..."
                    #__#hide screen hermione_main
                    #__#with d3
                    $herView.hideQQ()
                    #__#$ h_xpos=370 #Defines position of the Hermione's full length sprite. (Default 370). 140 - center.
                    #__#$ h_body = "03_hp/13_hermione_main/body_29.png" #Flashing Трусики
                    #__#show screen hermione_main
                    #__#with d3
                    $herView.showQQ( "body_29.png", pos )
                    her "..............."
                    her "Ну, профессор Локонс не отверг меня..."
                    m "Ты меня убиваешь, девочка!"
                    m "Он не отверг тебя, он не изнасиловал тебя..."
                    m "Тогда что произошло?"
                    #__#hide screen hermione_main
                    #__#with d3
                    $herView.hideQQ()
                    #__#$ h_xpos=370 #Defines position of the Hermione's full length sprite. (Default 370). 140 - center.
                    #__#$ h_body = "03_hp/13_hermione_main/body_33.png" #Flashing Трусики
                    #__#show screen hermione_main
                    #__#with d3
                    $herView.showQQ( "body_33.png", pos )
                    her "............."
                    #__#hide screen hermione_main
                    #__#with d3
                    $herView.hideQQ()
                    #__#$ h_xpos=370 #Defines position of the Hermione's full length sprite. (Default 370). 140 - center.
                    #__#$ h_body = "03_hp/13_hermione_main/body_34.png" #Flashing Трусики
                    #__#show screen hermione_main
                    #__#with d3
                    $herView.showQQ( "body_34.png", pos )
                    play music "music/Chipper Doodle v2.mp3" fadein 1 fadeout 1 # HERMIONE'S THEME.
                    her "Я заставила его плакать, сэр..."
                    m "..............стоп.......что?"
                    #__#hide screen hermione_main
                    #__#with d3
                    $herView.hideQQ()
                    #__#$ h_xpos=370 #Defines position of the Hermione's full length sprite. (Default 370). 140 - center.
                    #__#$ h_body = "03_hp/13_hermione_main/body_28.png" #Flashing Трусики
                    #__#show screen hermione_main
                    #__#with d3
                    $herView.showQQ( "body_28.png", pos )
                    her "Он озадаченно посмотрел и затем начал рыдать..."
                    her "Он смотрел на меня так, как будто боится, сэр."
                    #__#hide screen hermione_main
                    #__#with d3
                    $herView.hideQQ()
                    #__#$ h_xpos=370 #Defines position of the Hermione's full length sprite. (Default 370). 140 - center.
                    #__#$ h_body = "03_hp/13_hermione_main/body_29.png" #Flashing Трусики
                    #__#show screen hermione_main
                    #__#with d3
                    $herView.showQQ( "body_29.png", pos )
                    her "Я думаю..."
                    her "Я думаю, мистер Локонс боится женщин..."
                    m "Боится женщин?"
                    m "Что это может значить?"
                    #__#hide screen hermione_main
                    #__#with d3
                    $herView.hideQQ()
                    #__#$ h_xpos=370 #Defines position of the Hermione's full length sprite. (Default 370). 140 - center.
                    #__#$ h_body = "03_hp/13_hermione_main/body_34.png" #Flashing Трусики
                    #__#show screen hermione_main
                    #__#with d3
                    $herView.showQQ( "body_34.png", pos )
                    her "То, что ему нравятся мальчики, сэр?"
                    m "Ох..."
                    #__#hide screen hermione_main
                    #__#with d3
                    $herView.hideQQ()
                    #__#$ h_xpos=370 #Defines position of the Hermione's full length sprite. (Default 370). 140 - center.
                    #__#$ h_body = "03_hp/13_hermione_main/body_44.png" #Flashing Трусики
                    #__#show screen hermione_main
                    #__#with d3
                    $herView.showQQ( "body_44.png", pos )
                    her "............"
                    m "..........."
                    m "Ну, почти уверен, что этот опыт нанес вам травму, Мисс Грейнджер."
                    #__#hide screen hermione_main
                    #__#with d3
                    $herView.hideQQ()
                    #__#$ h_xpos=370 #Defines position of the Hermione's full length sprite. (Default 370). 140 - center.
                    #__#$ h_body = "03_hp/13_hermione_main/body_31.png" #Flashing Трусики
                    #__#show screen hermione_main
                    #__#with d3
                    $herView.showQQ( "body_31.png", pos )
                    her "Вроде, сэр..."
                    m "Ну, надеюсь эти очки поднимут тебе настроение.."
                    
                            
    
    $ gryffindor +=15
    m "\"Гриффиндор\" получает 15 очков!"
    her "Спасибо, сэр."
    
    hide screen bld1
    #__#hide screen hermione_main
    $herView.hideQ()
    hide screen blktone 
    hide screen hermione_02
    hide screen ctc
    with d3

    $ walk_xpos=400 #Animation of walking chibi. (From)
    $ walk_xpos2=610 #Coordinates of it's movement. (To)
    $ hermione_speed = 02.0 #The speed of moving the walking animation across the screen.
    show screen hermione_walk_01_f 
    pause 2
    hide screen hermione_walk_01_f 
    $ renpy.play('sounds/door.mp3') #Sound of a door opening.
    with Dissolve(.3)

    call music_block

    $ p_level_03_active = True #When turns TRUE public favors of level 03 become available. 

    
    if whoring <= 5:  # (if whoring >= 3 and whoring <= 5) - LEVEL 02
        $ whoring +=1

    $ request_02_c_points += 1 #Leveling up the event.
    $ request_02_c = False 
    $ hermione_sleeping = True

    return    
    
label could_not_flirt_02: #Sent here when chose "Задание провалено! Ты не получишь очки!"
    hide screen bld1
    #__#hide screen hermione_main
    $herView.hideQ()
    hide screen blktone 
    hide screen hermione_02
    hide screen ctc
    with d3

    $ walk_xpos=400 #Animation of walking chibi. (From)
    $ walk_xpos2=610 #Coordinates of it's movement. (To)
    $ hermione_speed = 02.0 #The speed of moving the walking animation across the screen.
    show screen hermione_walk_01_f 
    pause 2
    hide screen hermione_walk_01_f 
    $ renpy.play('sounds/door.mp3') #Sound of a door opening.
    with Dissolve(.3)
    
    $ request_02_b_points += 1
    $ request_02_b = False 
    $ hermione_sleeping = True
    
    return   
