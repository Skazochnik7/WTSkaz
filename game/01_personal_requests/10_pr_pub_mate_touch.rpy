
###################REQUEST_10 (Level 03) (25 pt.) (Let a classmate touch you). (Available during daytime only).
label new_request_10:
    
    #__#hide screen hermione_main 
    #__#with d3
    $herView.hideQQ()
    m "{size=-4}(Сказать ей, что бы её одноклассник облапал её?){/size}"
    $ menu_x = 0.5 #Default position of the menu (0.5). Version B is $ menu_x = 0.2
    menu:
        "\"(Да, сделать это!)\"":
            pass
        "\"(Не сейчас.)\"":
            jump new_personal_request
            
    $ pos = POS_140

    if request_10_points == 0: # <================================================================================ FIRST TIME
        m "Мисс Грейнджер?"
        #__#$ h_xpos=140 #Defines position of the Hermione's full length sprite. (Default 370). 140 - center.
        #__#$ h_body = "03_hp/13_hermione_main/body_01.png" #Flashing panties
        #__#show screen hermione_main
        #__#with d3
        $herView.showQQ( "body_01.png", pos )
        her "Сэр?"
        m "Тебе нравятся мальчики твоего возраста, не правда ли?"
        #__#hide screen hermione_main                                                                  # HERMIONE
        #__#with d3                                                                                                       # HERMIONE
        $herView.hideQQ()
        #__#$ h_body = "03_hp/13_hermione_main/body_03.png"                # HERMIONE
        #__#show screen hermione_main                                                               # HERMIONE
        #__#with d3                                                                                                      # HERMIONE
        $herView.showQQ( "body_03.png", pos )
        her "...?"
        m "Может быть, кто-то из одноклассников?"
        #__#hide screen hermione_main                                                                  # HERMIONE
        #__#with d3                                                                                                       # HERMIONE
        $herView.hideQQ()
        #__#$ h_body = "03_hp/13_hermione_main/body_10.png"                # HERMIONE
        #__#show screen hermione_main                                                               # HERMIONE
        #__#with d3                                                                                                      # HERMIONE
        $herView.showQQ( "body_10.png", pos )
        her "Ну..."
        her "Должна ли я обсуждать с вами такие вопросы... сэр?"
        #__#hide screen hermione_main                                                                  # HERMIONE
        #__#with d3                                                                                                       # HERMIONE
        $herView.hideQQ()
        #__#$ h_body = "03_hp/13_hermione_main/body_29.png"                # HERMIONE
        #__#show screen hermione_main                                                               # HERMIONE
        #__#with d3                                                                                                      # HERMIONE
        $herView.showQQ( "body_29.png", pos )
        her "Я немного стесняюсь..."
        m "Конечно, я понимаю. Мне не стоит знать детали..."
        m "Но вот что мне нужно, что бы вы сделали, мисс Грейнджер."
        m "Подойдите к какому нибудь мальчику. Тому мальчику, \"о ком мечтаешь\", который нравится..."
        #__#hide screen hermione_main                                                                  # HERMIONE
        #__#with d3                                                                                                       # HERMIONE
        $herView.hideQQ()
        #__#$ h_body = "03_hp/13_hermione_main/body_31.png"                # HERMIONE
        #__#show screen hermione_main                                                               # HERMIONE
        #__#with d3                                                                                                      # HERMIONE
        $herView.showQQ( "body_31.png", pos )
        her ".......?"
        m "И пусть он потрогает тебя..."
        if whoring <=5 or request_02_c_points <= 1: # Counts how many times Hermione been sent to flirt with teachers.
            jump too_much
        #__#hide screen hermione_main                                                                  # HERMIONE
        #__#with d3                                                                                                       # HERMIONE
        $herView.hideQQ()
        #__#$ h_body = "03_hp/13_hermione_main/body_31.png"                # HERMIONE
        #__#show screen hermione_main                                                               # HERMIONE
        #__#with d3                                                                                                      # HERMIONE
        $herView.showQQ( "body_31.png", pos )
        her "Дать ему потрогать меня... сэр?"
        m "Да, потрогать тебя. Как мальчики трогают девочек?"
        m "Сколько тебе лет? Ты выглядишь достаточно взрослой..."
        m "Неужели твои родители еще не \"говорили\" с тобой?"
        #__#hide screen hermione_main                                                                  # HERMIONE
        #__#with d3                                                                                                       # HERMIONE
        $herView.hideQQ()
        #__#$ h_body = "03_hp/13_hermione_main/body_34.png"                # HERMIONE
        #__#show screen hermione_main                                                               # HERMIONE
        #__#with d3                                                                                                      # HERMIONE
        $herView.showQQ( "body_34.png", pos )
        her "\"Говорили\", сэр?"
        m "Да-да, \"говорили\"! О том, чем мальчики отличаются от девочек...?"
        m "У мальчиков есть \"пиписька\" и девочкам нравится брать \"пипиську\" в рот?"
        #__#hide screen hermione_main                                                                  # HERMIONE
        #__#with d3                                                                                                       # HERMIONE
        $herView.hideQQ()
        #__#$ h_body = "03_hp/13_hermione_main/body_03.png"                # HERMIONE
        #__#show screen hermione_main                                                               # HERMIONE
        #__#with d3                                                                                                      # HERMIONE
        $herView.showQQ( "body_03.png", pos )
        her "!!!"
        #__#hide screen hermione_main                                                                  # HERMIONE
        #__#with d3                                                                                                       # HERMIONE
        $herView.hideQQ()
        #__#$ h_body = "03_hp/13_hermione_main/body_47.png"                # HERMIONE
        #__#show screen hermione_main                                                               # HERMIONE
        #__#with d3                                                                                                      # HERMIONE
        $herView.showQQ( "body_47.png", pos )
        her "Какие же родители будут такое говорить своим детям?"
        m "Думаю, Акабур будет."
        #__#hide screen hermione_main                                                                  # HERMIONE
        #__#with d3                                                                                                       # HERMIONE
        $herView.hideQQ()
        #__#$ h_body = "03_hp/13_hermione_main/body_17.png"                # HERMIONE
        #__#show screen hermione_main                                                               # HERMIONE
        #__#with d3                                                                                                      # HERMIONE
        $herView.showQQ( "body_17.png", pos )
        her "Извините, сэр?"
        m "*Кхем!* Я имею ввиду, отвественные и заботливые!"
        m "Ну, в любом случае. Вот ваше задание на сегодня, мисс Грейнджер."
        m "Найти себе мальчика и уговорить его поласкать себя..."
        #__#hide screen hermione_main                                                                  # HERMIONE
        #__#with d3                                                                                                       # HERMIONE
        $herView.hideQQ()
        #__#$ h_body = "03_hp/13_hermione_main/body_69.png"                # HERMIONE
        #__#show screen hermione_main                                                               # HERMIONE
        #__#with d3                                                                                                      # HERMIONE
        $herView.showQQ( "body_69.png", pos )
        her ".........."
        m "Ты симпатичная девочка и это будет не трудно для тебя."
        her "....................."
        #__#hide screen hermione_main                                                                  # HERMIONE
        #__#with d3                                                                                                       # HERMIONE
        $herView.hideQQ()
        #__#$ h_body = "03_hp/13_hermione_main/body_66.png"                # HERMIONE
        #__#show screen hermione_main                                                               # HERMIONE
        #__#with d3                                                                                                      # HERMIONE
        $herView.showQQ( "body_66.png", pos )
        her "Сколько очков я получу за выполнение этого задания, сэр?"
        m "Хм... Думаю, 25 очков хватит..."
        #__#hide screen hermione_main                                                                  # HERMIONE
        #__#with d3                                                                                                       # HERMIONE
        $herView.hideQQ()
        #__#$ h_body = "03_hp/13_hermione_main/body_69.png"                # HERMIONE
        #__#show screen hermione_main                                                               # HERMIONE
        #__#with d3                                                                                                      # HERMIONE
        $herView.showQQ( "body_69.png", pos )
        her "25 очков..."
        her "...."
        #__#hide screen hermione_main                                                                  # HERMIONE
        #__#with d3                                                                                                       # HERMIONE
        $herView.hideQQ()
        #__#$ h_body = "03_hp/13_hermione_main/body_66.png"                # HERMIONE
        #__#show screen hermione_main                                                               # HERMIONE
        #__#with d3                                                                                                      # HERMIONE
        $herView.showQQ( "body_66.png", pos )
        her "Ладно, договорились..."
        m "Отлично..."
        #__#hide screen hermione_main                                                                  # HERMIONE
        #__#with d3                                                                                                       # HERMIONE
        $herView.hideQQ()
        #__#$ h_body = "03_hp/13_hermione_main/body_05.png"                # HERMIONE
        #__#show screen hermione_main                                                               # HERMIONE
        #__#with d3                                                                                                      # HERMIONE
        $herView.showQQ( "body_05.png", pos )
        her "Я, наверно, пойду. Скоро начнутся уроки..."
        #__#hide screen hermione_main
        $herView.hideQ() #"WARNING_Z"
    else:
        if whoring >= 6 and whoring <= 8: # LEVEL 03 
            m "Мисс Грейнджер?"
            #__#$ h_xpos=140 #Defines position of the Hermione's full length sprite. (Default 370). 140 - center.
            #__#$ h_body = "03_hp/13_hermione_main/body_01.png" #Flashing panties
            #__#show screen hermione_main
            #__#with d3
            $herView.showQQ( "body_01.png", pos )
            her "Сэр."
            m "Как насчет того, что бы дать вашему однокласснику полапать вас?"
            #__#hide screen hermione_main                                                                  # HERMIONE
            #__#with d3                                                                                                       # HERMIONE
            $herView.hideQQ()
            #__#$ h_body = "03_hp/13_hermione_main/body_120.png"                # HERMIONE
            #__#show screen hermione_main                                                               # HERMIONE
            #__#with d3                                                                                                      # HERMIONE
            $herView.showQQ( "body_120.png", pos )
            her "........"
            m "25 очков, мисс Грейнджер."
            #__#hide screen hermione_main                                                                  # HERMIONE
            #__#with d3                                                                                                       # HERMIONE
            $herView.hideQQ()
            #__#$ h_body = "03_hp/13_hermione_main/body_69.png"                # HERMIONE
            #__#show screen hermione_main                                                               # HERMIONE
            #__#with d3                                                                                                      # HERMIONE
            $herView.showQQ( "body_69.png", pos )
            her "Сэр, это только..."
            #__#hide screen hermione_main                                                                  # HERMIONE
            #__#with d3                                                                                                       # HERMIONE
            $herView.hideQQ()
            #__#$ h_body = "03_hp/13_hermione_main/body_79.png"                # HERMIONE
            #__#show screen hermione_main                                                               # HERMIONE
            #__#with d3                                                                                                      # HERMIONE
            $herView.showQQ( "body_79.png", pos )
            her "Я не понимаю, зачем мне делать такие вещи..."
            m "Что бы помочь своему факультету?"
            #__#hide screen hermione_main                                                                  # HERMIONE
            #__#with d3                                                                                                       # HERMIONE
            $herView.hideQQ()
            #__#$ h_body = "03_hp/13_hermione_main/body_66.png"                # HERMIONE
            #__#show screen hermione_main                                                               # HERMIONE
            #__#with d3                                                                                                      # HERMIONE
            $herView.showQQ( "body_66.png", pos )
            her "Я не про это..."
            #__#hide screen hermione_main                                                                  # HERMIONE
            #__#with d3                                                                                                       # HERMIONE
            $herView.hideQQ()
            #__#$ h_body = "03_hp/13_hermione_main/body_69.png"                # HERMIONE
            #__#show screen hermione_main                                                               # HERMIONE
            #__#with d3                                                                                                      # HERMIONE
            $herView.showQQ( "body_69.png", pos )
            her "Ладно, не обращайте внимание..."
            her "Скоро будет звонок, я, наверное, пойду..."
            m "Ты сделаешь это?"
            #__#hide screen hermione_main                                                                  # HERMIONE
            #__#with d3                                                                                                       # HERMIONE
            $herView.hideQQ()
            #__#$ h_body = "03_hp/13_hermione_main/body_66.png"                # HERMIONE
            #__#show screen hermione_main                                                               # HERMIONE
            #__#with d3                                                                                                      # HERMIONE
            $herView.showQQ( "body_66.png", pos )
            her "Я не знаю... Наверное..."
            #__#hide screen hermione_main
            $herView.hideQ() #"WARNING_Z"
        elif whoring >= 9 and whoring <= 11: # LEVEL 04
            m "Мисс Грейнджер, нужно что бы вы подошли к своему однокласснику и предложили ему полапать вас."
            #__#$ h_xpos=140 #Defines position of the Hermione's full length sprite. (Default 370). 140 - center.
            #__#$ h_body = "03_hp/13_hermione_main/body_01.png" #Flashing panties
            #__#show screen hermione_main
            #__#with d3
            $herView.showQQ( "body_01.png", pos )
            her "Я поняла, сэр..."
            m "Тогда ступай."
            her "..........."
            #__#hide screen hermione_main
            $herView.hideQ() #"WARNING_Z"
        elif whoring >= 12: # LEVEL 05+
            m "Мисс Грейнджер, я хочу, что бы вы пошли..."
            m "И нашли привлекательного парня, который бы вас облапал!"
            $ h_xpos=140 #Defines position of the Hermione's full length sprite. (Default 370). 140 - center.
            #__#$ h_body = "03_hp/13_hermione_main/body_01.png" #Flashing panties
            #__#show screen hermione_main
            #__#with d3
            $herView.showQQ( "body_01.png", pos )
            her "В каком смысле...?"
            #__#hide screen hermione_main                                                                                                                                                                                   #HERMIONE
            #__#with d3                                                                                                                                                                                                                        #HERMIONE
            $herView.hideQQ()
            #__#$ h_body = "03_hp/13_hermione_main/body_122.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
            #__#show screen hermione_main                                                                                                                                                                                 #HERMIONE
            #__#with d3                                                                                                                                                                                                                        #HERMIONE
            $herView.showQQ( "body_122.png", pos )
            her "В сексуальном, сэр?"
            m "Что? Нет, я имею ввиду, что бы он потрогал вас под одеждой..."
            #__#hide screen hermione_main                                                                                                                                                                                   #HERMIONE
            #__#with d3                                                                                                                                                                                                                        #HERMIONE
            $herView.hideQQ()
            #__#$ h_body = "03_hp/13_hermione_main/body_24.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
            #__#show screen hermione_main                                                                                                                                                                                 #HERMIONE
            #__#with d3                                                                                                                                                                                                                        #HERMIONE
            $herView.showQQ( "body_24.png", pos )
            her "А, понятно..."
            #__#hide screen hermione_main                                                                                                                                                                                   #HERMIONE
            #__#with d3                                                                                                                                                                                                                        #HERMIONE
            $herView.hideQQ()
            #__#$ h_body = "03_hp/13_hermione_main/body_68.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
            #__#show screen hermione_main                                                                                                                                                                                 #HERMIONE
            #__#with d3                                                                                                                                                                                                                        #HERMIONE
            $herView.showQQ( "body_68.png", pos )
            her "Хотелось бы, что бы это был..."
            #__#hide screen hermione_main                                                                                                                                                                                   #HERMIONE
            #__#with d3                                                                                                                                                                                                                        #HERMIONE
            $herView.hideQQ()
            #__#$ h_body = "03_hp/13_hermione_main/body_117.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
            #__#show screen hermione_main                                                                                                                                                                                 #HERMIONE
            #__#with d3                                                                                                                                                                                                                        #HERMIONE
            $herView.showQQ( "body_117.png", pos )
            her "А ничего, если это будет не один парень, ведь так?"
            m "Ты ещё спрашиваешь! Конечно нет!"
            m "Если будет кто-нибудь еще - это считается." 
            #__#hide screen hermione_main                                                                                                                                                                                   #HERMIONE
            #__#with d3                                                                                                                                                                                                                        #HERMIONE
            $herView.hideQQ()
            #__#$ h_body = "03_hp/13_hermione_main/body_122.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
            #__#show screen hermione_main                                                                                                                                                                                 #HERMIONE
            #__#with d3                                                                                                                                                                                                                        #HERMIONE
            $herView.showQQ( "body_122.png", pos )
            her "Отлично. Я зайду к вам после учебы, сэр, как обычно."
            m "Хорошо. Удачи."
            #__#hide screen hermione_main
            $herView.hideQ() #"WARNING_Z"

   

    $ request_10 = True

    hide screen bld1
    #__#hide screen hermione_main
    $herView.hideQ() #"WARNING_Z"
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

        


label new_request_10_complete: #<==========================================================================EVENING
    
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
    $herView.showQ( "body_01.png", pos ) #"WARNING_Z"
    show screen hermione_02
    with Dissolve(.3)
    
    her "Добрый вечер, сэр."
    m "Мисс Грейнджер..."
    m "Вы выполнили задание?"
    her "Я сделала так, как вы просили..."
    menu:
        "\"Отлично. Вот твои очки.\"":
            pass
        "\"Расскажи подробнее.\"":
            #__#hide screen hermione_main
            #__#with d3
            $herView.hideQQ()
            m "Расскажи подробнее."
            show screen blktone
            with d3
            
            if whoring >= 6 and whoring <= 8: # LEVEL 03 # EVENT LEVEL 01.
                stop music fadeout 3.0
                #__#hide screen hermione_main                                                                                                                                                                                   #HERMIONE
                #__#with d3                                                                                                                                                                                                                        #HERMIONE
                $herView.hideQQ()
                #__#$ h_xpos=370 #Defines position of the Hermione's full length sprite. (Default 370). (Center: 140)                                                       #HERMIONE
                #__#$ h_body = "03_hp/13_hermione_main/body_12.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
                #__#show screen hermione_main                                                                                                                                                                                 #HERMIONE
                #__#with d3                                                                                                                                                                                                                        #HERMIONE
                $herView.showQQ( "body_12.png", pos )
                her "......"
                #__#hide screen hermione_main                                                                                                                                                                                   #HERMIONE
                #__#with d3                                                                                                                                                                                                                        #HERMIONE
                $herView.hideQQ()
                #__#$ h_body = "03_hp/13_hermione_main/body_13.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
                #__#show screen hermione_main                                                                                                                                                                                 #HERMIONE
                #__#with d3                                                                                                                                                                                                                        #HERMIONE
                $herView.showQQ( "body_13.png", pos )
                her "Ну... Эм..."
                m "Говори, девочка."
                m "Ты дала себя потрогать какому-нибудь везунчику?"
                    
                if one_out_of_three == 1: ### EVENT (A)
                    her "Да, дала, сэр..."
                    m "Ну же? Расскажи."
                    her "Ну, вообще-то, мало чего рассказывать..."
                    #__#hide screen hermione_main                                                                                                                                                                                   #HERMIONE
                    #__#with d3                                                                                                                                                                                                                        #HERMIONE
                    $herView.hideQQ()
                    #__#$ h_body = "03_hp/13_hermione_main/body_31.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
                    #__#show screen hermione_main                                                                                                                                                                                 #HERMIONE
                    #__#with d3                                                                                                                                                                                                                        #HERMIONE
                    $herView.showQQ( "body_31.png", pos )
                    her "Я сказала одному парню, что он может немного меня потрогать, если захочет..."
                    #__#hide screen hermione_main                                                                                                                                                                                   #HERMIONE
                    #__#with d3                                                                                                                                                                                                                        #HERMIONE
                    $herView.hideQQ()
                    #__#$ h_body = "03_hp/13_hermione_main/body_29.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
                    #__#show screen hermione_main                                                                                                                                                                                 #HERMIONE
                    #__#with d3                                                                                                                                                                                                                        #HERMIONE
                    $herView.showQQ( "body_29.png", pos )
                    her "Сначала он подумал, что это шутка..."
                    #__#hide screen hermione_main                                                                                                                                                                                   #HERMIONE
                    #__#with d3                                                                                                                                                                                                                        #HERMIONE
                    $herView.hideQQ()
                    #__#$ h_body = "03_hp/13_hermione_main/body_33.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
                    #__#show screen hermione_main                                                                                                                                                                                 #HERMIONE
                    #__#with d3                                                                                                                                                                                                                        #HERMIONE
                    $herView.showQQ( "body_33.png", pos )
                    her "Так стыдно..."
                    m "Так он трогал тебя или нет?"
                    #__#hide screen hermione_main                                                                                                                                                                                   #HERMIONE
                    #__#with d3                                                                                                                                                                                                                        #HERMIONE
                    $herView.hideQQ()
                    #__#$ h_body = "03_hp/13_hermione_main/body_33.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
                    #__#show screen hermione_main                                                                                                                                                                                 #HERMIONE
                    #__#with d3                                                                                                                                                                                                                        #HERMIONE
                    $herView.showQQ( "body_33.png", pos )
                    play music "music/(Orchestral) Playful Tension by Shadow16nh.mp3" fadein 1 fadeout 1 # SEX THEME.
                    her "Да, трогал..."
                    m "Ну и где же он тебя трогал?"
                    #__#hide screen hermione_main                                                                                                                                                                                   #HERMIONE
                    #__#with d3                                                                                                                                                                                                                        #HERMIONE
                    $herView.hideQQ()
                    #__#$ h_body = "03_hp/13_hermione_main/body_29.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
                    #__#show screen hermione_main                                                                                                                                                                                 #HERMIONE
                    #__#with d3                                                                                                                                                                                                                        #HERMIONE
                    $herView.showQQ( "body_29.png", pos )
                    her "Эм... мои ноги..."
                    her "И мою грудь, немного..."
                    m "Это всё?"
                    #__#hide screen hermione_main                                                                                                                                                                                   #HERMIONE
                    #__#with d3                                                                                                                                                                                                                        #HERMIONE
                    $herView.hideQQ()
                    #__#$ h_body = "03_hp/13_hermione_main/body_31.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
                    #__#show screen hermione_main                                                                                                                                                                                 #HERMIONE
                    #__#with d3                                                                                                                                                                                                                        #HERMIONE
                    $herView.showQQ( "body_31.png", pos )
                    her "Да, сэр..."
                    #__#hide screen hermione_main                                                                                                                                                                                   #HERMIONE
                    #__#with d3                                                                                                                                                                                                                        #HERMIONE
                    $herView.hideQQ()
                    #__#$ h_body = "03_hp/13_hermione_main/body_33.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
                    #__#show screen hermione_main                                                                                                                                                                                 #HERMIONE
                    #__#with d3                                                                                                                                                                                                                        #HERMIONE
                    $herView.showQQ( "body_33.png", pos )
                    her "Уже поздно... я думаю мне пора..."
                    #__#hide screen hermione_main                                                                                                                                                                                   #HERMIONE
                    #__#with d3                                                                                                                                                                                                                        #HERMIONE
                    $herView.hideQQ()
                    #__#$ h_body = "03_hp/13_hermione_main/body_34.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
                    #__#show screen hermione_main                                                                                                                                                                                 #HERMIONE
                    #__#with d3                                                                                                                                                                                                                        #HERMIONE
                    $herView.showQQ( "body_34.png", pos )
                    her "Извините, сэр..."
                    m "Тебе не стоит извиняться, девочка."
                    m "Ты молодец. Этого достаточно... пока что..."
                    
                elif one_out_of_three == 2: ### EVENT (B)
                    stop music fadeout 3.0
                    #__#hide screen hermione_main                                                                                                                                                                                   #HERMIONE
                    #__#with d3                                                                                                                                                                                                                        #HERMIONE
                    $herView.hideQQ()
                    #__#$ h_body = "03_hp/13_hermione_main/body_69.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
                    #__#show screen hermione_main                                                                                                                                                                                 #HERMIONE
                    #__#with d3                                                                                                                                                                                                                        #HERMIONE
                    $herView.showQQ( "body_69.png", pos )
                    her "Я сделала это, сэр!"
                    her "Но это было так отвратительно и стыдно..."
                    m "Это всё, что ты хочешь сообщить мне?."
                    m "Лучше расскажи где он тебя трогал..."
                    play music "music/(Orchestral) Playful Tension by Shadow16nh.mp3" fadein 1 fadeout 1 # SEX THEME.
                    her "Эм..."
                    #__#hide screen hermione_main                                                                                                                                                                                   #HERMIONE
                    #__#with d3                                                                                                                                                                                                                        #HERMIONE
                    $herView.hideQQ()
                    #__#$ h_body = "03_hp/13_hermione_main/body_117.png" #Sprite of Hermione's upper body.                                                                 #HERMIONE
                    #__#show screen hermione_main                                                                                                                                                                                 #HERMIONE
                    #__#with d3                                                                                                                                                                                                                        #HERMIONE
                    $herView.showQQ( "body_117.png", pos )
                    her "Ну, он трогал меня под юбкой, немного..."
                    her "Я дала ему потрогать мою..."
                    #__#hide screen hermione_main                                                                                                                                                                                   #HERMIONE
                    #__#with d3                                                                                                                                                                                                                        #HERMIONE
                    $herView.hideQQ()
                    #__#$ h_body = "03_hp/13_hermione_main/body_118.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
                    #__#show screen hermione_main                                                                                                                                                                                 #HERMIONE
                    #__#with d3                                                                                                                                                                                                                        #HERMIONE
                    $herView.showQQ( "body_118.png", pos )
                    her "...киску, через юбку, сэр."
                    m "Хорошо. Что было потом?"
                    #__#hide screen hermione_main                                                                                                                                                                                   #HERMIONE
                    #__#with d3                                                                                                                                                                                                                        #HERMIONE
                    $herView.hideQQ()
                    #__#$ h_body = "03_hp/13_hermione_main/body_131.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
                    #__#show screen hermione_main                                                                                                                                                                                 #HERMIONE
                    #__#with d3                                                                                                                                                                                                                        #HERMIONE
                    $herView.showQQ( "body_131.png", pos )
                    her "Затем он начал трогать себя..."
                    her "И я решила уйти..."
                    m "Ясно..."
                    #__#hide screen hermione_main                                                                                                                                                                                   #HERMIONE
                    #__#with d3                                                                                                                                                                                                                        #HERMIONE
                    $herView.hideQQ()
                    #__#$ h_body = "03_hp/13_hermione_main/body_33.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
                    #__#show screen hermione_main                                                                                                                                                                                 #HERMIONE
                    #__#with d3                                                                                                                                                                                                                        #HERMIONE
                    $herView.showQQ( "body_33.png", pos )
                    her "............."
                    
                elif one_out_of_three == 3: ### EVENT (C)
                    her "Я сделала это, сэр..."
                    #__#hide screen hermione_main                                                                                                                                                                                   #HERMIONE
                    #__#with d3                                                                                                                                                                                                                        #HERMIONE
                    $herView.hideQQ()
                    #__#$ h_body = "03_hp/13_hermione_main/body_31.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
                    #__#show screen hermione_main                                                                                                                                                                                 #HERMIONE
                    #__#with d3                                                                                                                                                                                                                        #HERMIONE
                    $herView.showQQ( "body_31.png", pos )
                    play music "music/(Orchestral) Playful Tension by Shadow16nh.mp3" fadein 1 fadeout 1 # SEX THEME.
                    her "Я завела одного парня из \"Пуффендуя\" в пустую комнату и предложила ему потрогать себя, если он захочет."
                    her "И..."
                    #__#hide screen hermione_main                                                                                                                                                                                   #HERMIONE
                    #__#with d3                                                                                                                                                                                                                        #HERMIONE
                    $herView.hideQQ()
                    #__#$ h_body = "03_hp/13_hermione_main/body_29.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
                    #__#show screen hermione_main                                                                                                                                                                                 #HERMIONE
                    #__#with d3                                                                                                                                                                                                                        #HERMIONE
                    $herView.showQQ( "body_29.png", pos )
                    her "..........."
                    m "И?"
                    #__#hide screen hermione_main                                                                                                                                                                                   #HERMIONE
                    #__#with d3                                                                                                                                                                                                                        #HERMIONE
                    $herView.hideQQ()
                    #__#$ h_body = "03_hp/13_hermione_main/body_31.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
                    #__#show screen hermione_main                                                                                                                                                                                 #HERMIONE
                    #__#with d3                                                                                                                                                                                                                        #HERMIONE
                    $herView.showQQ( "body_31.png", pos )
                    her "Ну, он сначала трогал меня..."
                    #__#hide screen hermione_main                                                                                                                                                                                   #HERMIONE
                    #__#with d3                                                                                                                                                                                                                        #HERMIONE
                    $herView.hideQQ()
                    #__#$ h_body = "03_hp/13_hermione_main/body_33.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
                    #__#show screen hermione_main                                                                                                                                                                                 #HERMIONE
                    #__#with d3                                                                                                                                                                                                                        #HERMIONE
                    $herView.showQQ( "body_33.png", pos )
                    her "......"
                    m "Не заставляй меня вытаскивать из тебя каждое слово!"
                    m "Что произошло потом?"
                    #__#hide screen hermione_main                                                                                                                                                                                   #HERMIONE
                    #__#with d3                                                                                                                                                                                                                        #HERMIONE
                    $herView.hideQQ()
                    #__#$ h_body = "03_hp/13_hermione_main/body_87.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
                    #__#show screen hermione_main                                                                                                                                                                                 #HERMIONE
                    #__#with d3                                                                                                                                                                                                                        #HERMIONE
                    $herView.showQQ( "body_87.png", pos )
                    her "Ну..."
                    stop music fadeout 1.0
                    her "Я думала ему понравилось лапать {size=+5}меня{/size} {size=+5}собой{/size}..."
                    #__#hide screen hermione_main                                                                                                                                                                                   #HERMIONE
                    #__#with d3                                                                                                                                                                                                                        #HERMIONE
                    $herView.hideQQ()
                    #__#$ h_body = "03_hp/13_hermione_main/body_44.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
                    #__#show screen hermione_main                                                                                                                                                                                 #HERMIONE
                    #__#with d3                                                                                                                                                                                                                        #HERMIONE
                    $herView.showQQ( "body_44.png", pos )
                    her "Он просил меня называть его \"Сисястым мальчиком\"..."
                    play music "music/Despair_by_erenik.mp3" fadein 1 fadeout 1 # SAD THEME.
                    #__#hide screen hermione_main                                                                                                                                                                                   #HERMIONE
                    #__#with d3                                                                                                                                                                                                                        #HERMIONE
                    $herView.hideQQ()
                    #__#$ h_body = "03_hp/13_hermione_main/body_31.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
                    #__#show screen hermione_main                                                                                                                                                                                 #HERMIONE
                    #__#with d3                                                                                                                                                                                                                        #HERMIONE
                    $herView.showQQ( "body_31.png", pos )
                    her "И потом он рассказал мне, что у него очень маленький член..."
                    #__#hide screen hermione_main                                                                                                                                                                                   #HERMIONE
                    #__#with d3                                                                                                                                                                                                                        #HERMIONE
                    $herView.hideQQ()
                    #__#$ h_body = "03_hp/13_hermione_main/body_22.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
                    #__#show screen hermione_main                                                                                                                                                                                 #HERMIONE
                    #__#with d3                                                                                                                                                                                                                        #HERMIONE
                    $herView.showQQ( "body_22.png", pos )
                    her "Он просто повторял это *всхлип*..."
                    #__#hide screen hermione_main                                                                                                                                                                                   #HERMIONE
                    #__#with d3                                                                                                                                                                                                                        #HERMIONE
                    $herView.hideQQ()
                    #__#$ h_body = "03_hp/13_hermione_main/body_21.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
                    #__#show screen hermione_main                                                                                                                                                                                 #HERMIONE
                    #__#with d3                                                                                                                                                                                                                        #HERMIONE
                    $herView.showQQ( "body_21.png", pos )
                    her "Почему есть такие идиоты, как он?"
                    her "*Хнык!* Я больше не могла находиться рядом с ним и убежала...."
                    m "Извините, что рассказываю вам это..."
                    #__#hide screen hermione_main                                                                                                                                                                                   #HERMIONE
                    #__#with d3                                                                                                                                                                                                                        #HERMIONE
                    $herView.hideQQ()
                    #__#$ h_body = "03_hp/13_hermione_main/body_21.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
                    #__#show screen hermione_main                                                                                                                                                                                 #HERMIONE
                    #__#with d3                                                                                                                                                                                                                        #HERMIONE
                    $herView.showQQ( "body_21.png", pos )
                    her "Это было просто ужасно, сэр..."
                    m "Ладно тебе, ладно..."
                    #__#hide screen hermione_main                                                                                                                                                                                   #HERMIONE
                    #__#with d3                                                                                                                                                                                                                        #HERMIONE
                    $herView.hideQQ()
                    #__#$ h_body = "03_hp/13_hermione_main/body_23.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
                    #__#show screen hermione_main                                                                                                                                                                                 #HERMIONE
                    #__#with d3                                                                                                                                                                                                                        #HERMIONE
                    $herView.showQQ( "body_23.png", pos )
                    her "*Хнык!*"
                    m "Если я накину тебе 10 дополнительных очков, тебе будет легче?"
                    #__#hide screen hermione_main                                                                                                                                                                                   #HERMIONE
                    #__#with d3                                                                                                                                                                                                                        #HERMIONE
                    $herView.hideQQ()
                    #__#$ h_body = "03_hp/13_hermione_main/body_19.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
                    #__#show screen hermione_main                                                                                                                                                                                 #HERMIONE
                    #__#with d3                                                                                                                                                                                                                        #HERMIONE
                    $herView.showQQ( "body_19.png", pos )
                    her "М? Это было бы мило с вашей стороны."
                    $ gryffindor += 10
                    m "Конечно... 10 дополнительных очков \"Гриффиндору\"."
                    #__#hide screen hermione_main                                                                                                                                                                                   #HERMIONE
                    #__#with d3                                                                                                                                                                                                                        #HERMIONE
                    $herView.hideQQ()
                    #__#$ h_body = "03_hp/13_hermione_main/body_140.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
                    #__#show screen hermione_main                                                                                                                                                                                 #HERMIONE
                    #__#with d3                                                                                                                                                                                                                        #HERMIONE
                    $herView.showQQ( "body_140.png", pos )
                    her "Спасибо, сэр..."
                    m "А вот и остальные баллы..."
            
            elif whoring >= 9 and whoring <= 11: # LEVEL 04
                if one_out_of_three == 1: ### EVENT (A)
                    #__#hide screen hermione_main                                                                                                                                                                                   #HERMIONE
                    #__#with d3                                                                                                                                                                                                                        #HERMIONE
                    $herView.hideQQ()
                    #__#$ h_xpos=370 #Defines position of the Hermione's full length sprite. (Default 370). (Center: 140)                                                       #HERMIONE
                    #__#$ h_body = "03_hp/13_hermione_main/body_16.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
                    #__#show screen hermione_main                                                                                                                                                                                 #HERMIONE
                    #__#with d3                                                                                                                                                                                                                        #HERMIONE
                    $herView.showQQ( "body_16.png", pos )
                    her "Ну... Тут нечего рассказывать..."
                    her "Я нашла одного мальчика из \"Когтерван\"..."
                    her "Завела его в свободную аудиторию в восточном крыле..."
                    her "Он подумал, что я хочу посмотреть на его мускулы..."
                    her "Но я сказала, что хочу, что бы он потрогал меня..."
                    #__#hide screen hermione_main                                                                                                                                                                                   #HERMIONE
                    #__#with d3                                                                                                                                                                                                                        #HERMIONE
                    $herView.hideQQ()
                    #__#$ h_body = "03_hp/13_hermione_main/body_33.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
                    #__#show screen hermione_main                                                                                                                                                                                 #HERMIONE
                    #__#with d3                                                                                                                                                                                                                        #HERMIONE
                    $herView.showQQ( "body_33.png", pos )
                    her "...ну и он начал меня трогать."
                    m "Ясно..."
                    m "Хорошая работа, Мисс Грейнджер."
                    #__#hide screen hermione_main                                                                                                                                                                                   #HERMIONE
                    #__#with d3                                                                                                                                                                                                                        #HERMIONE
                    $herView.hideQQ()
                    #__#$ h_xpos=370 #Defines position of the Hermione's full length sprite. (Default 370). (Center: 140)                                                       #HERMIONE
                    #__#$ h_body = "03_hp/13_hermione_main/body_44.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
                    #__#show screen hermione_main                                                                                                                                                                                 #HERMIONE
                    #__#with d3                                                                                                                                                                                                                        #HERMIONE
                    $herView.showQQ( "body_44.png", pos )
                    her "Я получу свои очки, сэр?"
                    m "Одну минуту, мисс Грейнджер. Я хочу получить ответ на вопрос, который сейчас задам."
                    #__#hide screen hermione_main                                                                                                                                                                                   #HERMIONE
                    #__#with d3                                                                                                                                                                                                                        #HERMIONE
                    $herView.hideQQ()
                    #__#$ h_xpos=370 #Defines position of the Hermione's full length sprite. (Default 370). (Center: 140)                                                       #HERMIONE
                    #__#$ h_body = "03_hp/13_hermione_main/body_31.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
                    #__#show screen hermione_main                                                                                                                                                                                 #HERMIONE
                    #__#with d3                                                                                                                                                                                                                        #HERMIONE
                    $herView.showQQ( "body_31.png", pos )
                    her "???"
                    m "Вам понравилось?"
                    m "Вам понравилось то чувство, когда он трогал вас?"
                    #__#hide screen hermione_main                                                                                                                                                                                   #HERMIONE
                    #__#with d3                                                                                                                                                                                                                        #HERMIONE
                    $herView.hideQQ()
                    #__#$ h_xpos=370 #Defines position of the Hermione's full length sprite. (Default 370). (Center: 140)                                                       #HERMIONE
                    #__#$ h_body = "03_hp/13_hermione_main/body_127.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
                    #__#show screen hermione_main                                                                                                                                                                                 #HERMIONE
                    #__#with d3                                                                                                                                                                                                                        #HERMIONE
                    $herView.showQQ( "body_127.png", pos )
                    her "Хм..."
                    her "Ну, он был симпатичным..."
                    #__#hide screen hermione_main                                                                                                                                                                                   #HERMIONE
                    #__#with d3                                                                                                                                                                                                                        #HERMIONE
                    $herView.hideQQ()
                    #__#$ h_xpos=370 #Defines position of the Hermione's full length sprite. (Default 370). (Center: 140)                                                       #HERMIONE
                    #__#$ h_body = "03_hp/13_hermione_main/body_120.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
                    #__#show screen hermione_main                                                                                                                                                                                 #HERMIONE
                    #__#with d3                                                                                                                                                                                                                        #HERMIONE
                    $herView.showQQ( "body_120.png", pos )
                    her "Я не злилась на него за то, что он трогает меня, если вы это хотели услышать, сэр..."
                    m "Ясно..."
                    
                elif one_out_of_three == 2: ### EVENT (B)
                    #__#hide screen hermione_main                                                                                                                                                                                   #HERMIONE
                    #__#with d3                                                                                                                                                                                                                        #HERMIONE
                    $herView.hideQQ()
                    #__#$ h_xpos=370 #Defines position of the Hermione's full length sprite. (Default 370). (Center: 140)                                                       #HERMIONE
                    #__#$ h_body = "03_hp/13_hermione_main/body_16.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
                    #__#show screen hermione_main                                                                                                                                                                                 #HERMIONE
                    #__#with d3                                                                                                                                                                                                                        #HERMIONE
                    $herView.showQQ( "body_16.png", pos )
                    her "Ну..."
                    her "Я не уверена в том, что вы это хотите услышать, но..."
                    her "Во время того, как нас учили собирать траву..."
                    #__#hide screen hermione_main                                                                                                                                                                                   #HERMIONE
                    #__#with d3                                                                                                                                                                                                                        #HERMIONE
                    $herView.hideQQ()
                    #__#$ h_body = "03_hp/13_hermione_main/body_44.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
                    #__#show screen hermione_main                                                                                                                                                                                 #HERMIONE
                    #__#with d3                                                                                                                                                                                                                        #HERMIONE
                    $herView.showQQ( "body_44.png", pos )
                    her "Я дала одному парну дотронуться до себя под юбкой..."
                    her "И пока профессор Стебель обьясняла разницу между \"мандрейк\" и \"мандрагоры\"..."
                    #__#hide screen hermione_main                                                                                                                                                                                   #HERMIONE
                    #__#with d3                                                                                                                                                                                                                        #HERMIONE
                    $herView.hideQQ()
                    #__#$ h_body = "03_hp/13_hermione_main/body_08.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
                    #__#show screen hermione_main                                                                                                                                                                                 #HERMIONE
                    #__#with d3                                                                                                                                                                                                                        #HERMIONE
                    $herView.showQQ( "body_08.png", pos )
                    her "Конечно, кое что я уже знала..."
                    #__#hide screen hermione_main                                                                                                                                                                                   #HERMIONE
                    #__#with d3                                                                                                                                                                                                                        #HERMIONE
                    $herView.hideQQ()
                    #__#$ h_body = "03_hp/13_hermione_main/body_44.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
                    #__#show screen hermione_main                                                                                                                                                                                 #HERMIONE
                    #__#with d3                                                                                                                                                                                                                        #HERMIONE
                    $herView.showQQ( "body_44.png", pos )
                    her "Я дала потрогать своему партнеру по лабораторным мою попу..."
                    her "Ну, вот и всё..."
                    m "Хм..."
                    menu:
                        "\"Ты могла бы и постараться, что бы выполнить задание.\"":
                            #__#hide screen hermione_main                                                                                                                                                                                   #HERMIONE
                            #__#with d3                                                                                                                                                                                                                        #HERMIONE
                            $herView.hideQQ()
                            #__#$ h_body = "03_hp/13_hermione_main/body_31.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
                            #__#show screen hermione_main                                                                                                                                                                                 #HERMIONE
                            #__#with d3                                                                                                                                                                                                                        #HERMIONE
                            $herView.showQQ( "body_31.png", pos )
                            her "Да, я знаю, извините."
                            m "Просто в следующий раз приложи больше усилий."
                            her "Хорошо, я постараюсь, сэр."
                        "\"Хвалю, что сделала это во время занятий.\"":
                            #__#hide screen hermione_main                                                                                                                                                                                   #HERMIONE
                            #__#with d3                                                                                                                                                                                                                        #HERMIONE
                            $herView.hideQQ()
                            #__#$ h_body = "03_hp/13_hermione_main/body_74.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
                            #__#show screen hermione_main                                                                                                                                                                                 #HERMIONE
                            #__#with d3                                                                                                                                                                                                                        #HERMIONE
                            $herView.showQQ( "body_74.png", pos )
                            her "Спасибо, сэр."
                            m "Вижу, что ты заслужила награду."
                            
                elif one_out_of_three == 3: ### EVENT (C)
                    stop music fadeout 1.0
                    #__#hide screen hermione_main                                                                                                                                                                                   #HERMIONE
                    #__#with d3                                                                                                                                                                                                                        #HERMIONE
                    $herView.hideQQ()
                    #__#$ h_xpos=370 #Defines position of the Hermione's full length sprite. (Default 370). (Center: 140)                                                       #HERMIONE
                    #__#$ h_body = "03_hp/13_hermione_main/body_69.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
                    #__#show screen hermione_main                                                                                                                                                                                 #HERMIONE
                    #__#with d3                                                                                                                                                                                                                        #HERMIONE
                    $herView.showQQ( "body_69.png", pos )
                    her "................."
                    m "???"
                    #__#hide screen hermione_main                                                                                                                                                                                   #HERMIONE
                    #__#with d3                                                                                                                                                                                                                        #HERMIONE
                    $herView.hideQQ()
                    #__#$ h_body = "03_hp/13_hermione_main/body_69.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
                    #__#show screen hermione_main                                                                                                                                                                                 #HERMIONE
                    #__#with d3                                                                                                                                                                                                                        #HERMIONE
                    $herView.showQQ( "body_69.png", pos )
                    
                    play music "music/(Orchestral) Playful Tension by Shadow16nh.mp3" fadein 1 fadeout 1 # SEX THEME.
                    
                    her "Я не хочу говорить об этом, сэр..." 
                    m "Что случилось, малышка? Выговорись."
                    #__#hide screen hermione_main                                                                                                                                                                                   #HERMIONE
                    #__#with d3                                                                                                                                                                                                                        #HERMIONE
                    $herView.hideQQ()
                    #__#$ h_body = "03_hp/13_hermione_main/body_79.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
                    #__#show screen hermione_main                                                                                                                                                                                 #HERMIONE
                    #__#with d3                                                                                                                                                                                                                        #HERMIONE
                    $herView.showQQ( "body_79.png", pos )
                    her "................."
                    #__#hide screen hermione_main                                                                                                                                                                                   #HERMIONE
                    #__#with d3                                                                                                                                                                                                                        #HERMIONE
                    $herView.hideQQ()
                    #__#$ h_body = "03_hp/13_hermione_main/body_31.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
                    #__#show screen hermione_main                                                                                                                                                                                 #HERMIONE
                    #__#with d3                                                                                                                                                                                                                        #HERMIONE
                    $herView.showQQ( "body_31.png", pos )
                    her "Но... мне так стыдно..."
                    #__#hide screen hermione_main                                                                                                                                                                                   #HERMIONE
                    #__#with d3                                                                                                                                                                                                                        #HERMIONE
                    $herView.hideQQ()
                    #__#$ h_body = "03_hp/13_hermione_main/body_33.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
                    #__#show screen hermione_main                                                                                                                                                                                 #HERMIONE
                    #__#with d3                                                                                                                                                                                                                        #HERMIONE
                    $herView.showQQ( "body_33.png", pos )
                    her "Мне правда нужно рассказывать, сэр?"
                    m "Да, я люблю слушать такие вещи!"
                    #__#hide screen hermione_main                                                                                                                                                                                   #HERMIONE
                    #__#with d3                                                                                                                                                                                                                        #HERMIONE
                    $herView.hideQQ()
                    #__#$ h_body = "03_hp/13_hermione_main/body_69.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
                    #__#show screen hermione_main                                                                                                                                                                                 #HERMIONE
                    #__#with d3                                                                                                                                                                                                                        #HERMIONE
                    $herView.showQQ( "body_69.png", pos )
                    her "................."
                    her "Ладно..."
                    her "Я подошла к парню, которого всегда считала привлекательным..."
                    her "Нашла в себе силы и попросила его идти за мной..."
                    #__#hide screen hermione_main                                                                                                                                                                                   #HERMIONE
                    #__#with d3                                                                                                                                                                                                                        #HERMIONE
                    $herView.hideQQ()
                    #__#$ h_body = "03_hp/13_hermione_main/body_31.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
                    #__#show screen hermione_main                                                                                                                                                                                 #HERMIONE
                    #__#with d3                                                                                                                                                                                                                        #HERMIONE
                    $herView.showQQ( "body_31.png", pos )
                    her "Обычно, я бы даже не подошла к нему..."
                    her "Но тот факт, что я выполняю задание, каким-то образом заставил меня собрать свою волю в кулак..."
                    her "Это придало мне смелости..."
                    m "Рад помочь, Мисс Грейнджер."
                    #__#hide screen hermione_main                                                                                                                                                                                   #HERMIONE
                    #__#with d3                                                                                                                                                                                                                        #HERMIONE
                    $herView.hideQQ()
                    #__#$ h_body = "03_hp/13_hermione_main/body_87.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
                    #__#show screen hermione_main                                                                                                                                                                                 #HERMIONE
                    #__#with d3                                                                                                                                                                                                                        #HERMIONE
                    $herView.showQQ( "body_87.png", pos )
                    her "Я завела его в библиотеку..."
                    her "Мы нашли тихое место, между книжными шкафами..."
                    her "И я сказала ему, что он может трогать меня как пожелает..."                 
                    her "И...."
                    #__#hide screen hermione_main                                                                                                                                                                                   #HERMIONE
                    #__#with d3                                                                                                                                                                                                                        #HERMIONE
                    $herView.hideQQ()
                    #__#$ h_body = "03_hp/13_hermione_main/body_88.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
                    #__#show screen hermione_main                                                                                                                                                                                 #HERMIONE
                    #__#with d3                                                                                                                                                                                                                        #HERMIONE
                    $herView.showQQ( "body_88.png", pos )
                    her ".........."
                    m "Что?"
                    #__#hide screen hermione_main                                                                                                                                                                                   #HERMIONE
                    #__#with d3                                                                                                                                                                                                                        #HERMIONE
                    $herView.hideQQ()
                    #__#$ h_body = "03_hp/13_hermione_main/body_33.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
                    #__#show screen hermione_main                                                                                                                                                                                 #HERMIONE
                    #__#with d3                                                                                                                                                                                                                        #HERMIONE
                    $herView.showQQ( "body_33.png", pos )
                    her "....................."
                    #__#hide screen hermione_main                                                                                                                                                                                   #HERMIONE
                    #__#with d3                                                                                                                                                                                                                        #HERMIONE
                    $herView.hideQQ()
                    #__#$ h_body = "03_hp/13_hermione_main/body_32.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
                    #__#show screen hermione_main                                                                                                                                                                                 #HERMIONE
                    #__#with d3                                                                                                                                                                                                                        #HERMIONE
                    $herView.showQQ( "body_32.png", pos )
                    play music "music/Despair_by_erenik.mp3" fadein 1 fadeout 1 # SAD THEME.
                    her "Он начал трогать мои... ноги, сэр."
                    m "Эм?"
                    m "Ваши \"ноги\"? Это как тот малый с большими сиськами на днях?"
                    #__#hide screen hermione_main                                                                                                                                                                                   #HERMIONE
                    #__#with d3                                                                                                                                                                                                                        #HERMIONE
                    $herView.hideQQ()
                    #__#$ h_body = "03_hp/13_hermione_main/body_66.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
                    #__#show screen hermione_main                                                                                                                                                                                 #HERMIONE
                    #__#with d3                                                                                                                                                                                                                        #HERMIONE
                    $herView.showQQ( "body_66.png", pos )
                    her "Нет, сэр..."
                    her "Он попросил, чтобы я сняла свою обувь..."
                    her "Потом он..."
                    #__#hide screen hermione_main                                                                                                                                                                                   #HERMIONE
                    #__#with d3                                                                                                                                                                                                                        #HERMIONE
                    $herView.hideQQ()
                    #__#$ h_body = "03_hp/13_hermione_main/body_21.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
                    #__#show screen hermione_main                                                                                                                                                                                 #HERMIONE
                    #__#with d3                                                                                                                                                                                                                        #HERMIONE
                    $herView.showQQ( "body_21.png", pos )
                    her "Он стал нюхать мои лодыжки, сэр!"
                    #__#hide screen hermione_main                                                                                                                                                                                   #HERMIONE
                    #__#with d3                                                                                                                                                                                                                        #HERMIONE
                    $herView.hideQQ()
                    #__#$ h_body = "03_hp/13_hermione_main/body_22.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
                    #__#show screen hermione_main                                                                                                                                                                                 #HERMIONE
                    #__#with d3                                                                                                                                                                                                                        #HERMIONE
                    $herView.showQQ( "body_22.png", pos )
                    her "Я почувствовала себя такой... разбитой!"
                    m "И он даже не притронулся к твоей груди или попке?"
                    #__#hide screen hermione_main                                                                                                                                                                                   #HERMIONE
                    #__#with d3                                                                                                                                                                                                                        #HERMIONE
                    $herView.hideQQ()
                    #__#$ h_body = "03_hp/13_hermione_main/body_143.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
                    #__#show screen hermione_main                                                                                                                                                                                 #HERMIONE
                    #__#with d3                                                                                                                                                                                                                        #HERMIONE
                    $herView.showQQ( "body_143.png", pos )
                    her "Нет, сэр... *хнык!*"
                    m "Ладно, что случилось потом?"
                    #__#hide screen hermione_main                                                                                                                                                                                   #HERMIONE
                    #__#with d3                                                                                                                                                                                                                        #HERMIONE
                    $herView.hideQQ()
                    #__#$ h_body = "03_hp/13_hermione_main/body_142.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
                    #__#show screen hermione_main                                                                                                                                                                                 #HERMIONE
                    #__#with d3                                                                                                                                                                                                                        #HERMIONE
                    $herView.showQQ( "body_142.png", pos )
                    her "Ничего! Я не выдержала этого унижения и... убежала..."
                    her "Я даже забыла там свою обувь и спустя пару часов пришлось возвращаться за ней..."
                    #__#hide screen hermione_main                                                                                                                                                                                   #HERMIONE
                    #__#with d3                                                                                                                                                                                                                        #HERMIONE
                    $herView.hideQQ()
                    #__#$ h_body = "03_hp/13_hermione_main/body_145.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
                    #__#show screen hermione_main                                                                                                                                                                                 #HERMIONE
                    #__#with d3                                                                                                                                                                                                                        #HERMIONE
                    $herView.showQQ( "body_145.png", pos )
                    her "*Хнык!*............"
                    m "Хм..."
                    m "Получается он тебя облапал..."
                    m "Правда, немного в своеобразной манере..."
                    #__#hide screen hermione_main                                                                                                                                                                                   #HERMIONE
                    #__#with d3                                                                                                                                                                                                                        #HERMIONE
                    $herView.hideQQ()
                    #__#$ h_body = "03_hp/13_hermione_main/body_145.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
                    #__#show screen hermione_main                                                                                                                                                                                 #HERMIONE
                    #__#with d3                                                                                                                                                                                                                        #HERMIONE
                    $herView.showQQ( "body_145.png", pos )
                    her "*Хнык!* Как бы я хотела, что бы он просто потрогал мою грудь или попу, как обычный мальчик, сэр... *Хнык!*"
                    m "Успокойся, успокойся..."
                    m "Ты заработала свою награду сегодня..."
        
        
        
            elif whoring >= 12: # LEVEL 05+
                if one_out_of_three == 1: ### EVENT (A)
                    stop music fadeout 1.0
                    #__#hide screen hermione_main                                                                                                                                                                                   #HERMIONE
                    #__#with d3                                                                                                                                                                                                                        #HERMIONE
                    $herView.hideQQ()
                    #__#$ h_body = "03_hp/13_hermione_main/body_29.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
                    #__#show screen hermione_main                                                                                                                                                                                 #HERMIONE
                    #__#with d3                                                                                                                                                                                                                        #HERMIONE
                    $herView.showQQ( "body_29.png", pos )
                    her "......"
                    #__#hide screen hermione_main                                                                                                                                                                                   #HERMIONE
                    #__#with d3                                                                                                                                                                                                                        #HERMIONE
                    $herView.hideQQ()
                    #__#$ h_body = "03_hp/13_hermione_main/body_31.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
                    #__#show screen hermione_main                                                                                                                                                                                 #HERMIONE
                    #__#with d3       
                    $herView.showQQ( "body_31.png", pos )
                    her "Ну..."
                    her "Во время зельеварения, сегодня..."
                    her "Я написала записку на клочке бумаги..."
                    her "И передала её моему партнёру по лабораторным работам, и затем..."
                    #__#hide screen hermione_main                                                                                                                                                                                   #HERMIONE
                    #__#with d3                                                                                                                                                                                                                        #HERMIONE
                    $herView.hideQQ()
                    #__#$ h_body = "03_hp/13_hermione_main/body_69.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
                    #__#show screen hermione_main                                                                                                                                                                                 #HERMIONE
                    #__#with d3       
                    $herView.showQQ( "body_69.png", pos )
                    play music "music/Chipper Doodle v2.mp3" fadein 1 fadeout 1 # HERMIONE'S THEME.
                    her "Профессор Снейп вытащил её из моей руки..."
                    #__#hide screen hermione_main                                                                                                                                                                                   #HERMIONE
                    #__#with d3                                                                                                                                                                                                                        #HERMIONE
                    $herView.hideQQ()
                    #__#$ h_body = "03_hp/13_hermione_main/body_79.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
                    #__#show screen hermione_main                                                                                                                                                                                 #HERMIONE
                    #__#with d3       
                    $herView.showQQ( "body_79.png", pos )
                    her "Он прочитал её перед всем классом, который был полностью заполнен..."
                    m "О чем говорилось в записке?"
                    #__#hide screen hermione_main                                                                                                                                                                                   #HERMIONE
                    #__#with d3                                                                                                                                                                                                                        #HERMIONE
                    $herView.hideQQ()
                    #__#$ h_body = "03_hp/13_hermione_main/body_87.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
                    #__#show screen hermione_main                                                                                                                                                                                 #HERMIONE
                    #__#with d3       
                    $herView.showQQ( "body_87.png", pos )
                    her "Ну..."
                    her "Там было сказано: \"Ты можешь потрогать мою попку, если захочешь. Я думаю, Профессор Снейп не догадается.\""
                    #__#hide screen hermione_main                                                                                                                                                                                   #HERMIONE
                    #__#with d3                                                                                                                                                                                                                        #HERMIONE
                    $herView.hideQQ()
                    #__#$ h_body = "03_hp/13_hermione_main/body_118.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
                    #__#show screen hermione_main                                                                                                                                                                                 #HERMIONE
                    #__#with d3       
                    $herView.showQQ( "body_118.png", pos )
                    her "Все сильно смеялись..."
                    her "Было так стыдно, что я хотела провалиться на месте..."
                    #__#hide screen hermione_main                                                                                                                                                                                   #HERMIONE
                    #__#with d3                                                                                                                                                                                                                        #HERMIONE
                    $herView.hideQQ()
                    #__#$ h_body = "03_hp/13_hermione_main/body_47.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
                    #__#show screen hermione_main                                                                                                                                                                                 #HERMIONE
                    #__#with d3       
                    $herView.showQQ( "body_47.png", pos )
                    her "Я ненавижу профессора Снейпа, сэр..."
                    m "Что случилось потом?"
                    #__#hide screen hermione_main                                                                                                                                                                                   #HERMIONE
                    #__#with d3                                                                                                                                                                                                                        #HERMIONE
                    $herView.hideQQ()
                    #__#$ h_body = "03_hp/13_hermione_main/body_87.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
                    #__#show screen hermione_main                                                                                                                                                                                 #HERMIONE
                    #__#with d3       
                    $herView.showQQ( "body_87.png", pos )
                    her "Ничего..."
                    play music "music/(Orchestral) Playful Tension by Shadow16nh.mp3" fadein 1 fadeout 1 # SEX THEME.
                    her "Но, когда закончились занятия..."
                    her "Я заметила, как три парня из \"Слизерин\" жадно и пошло смотрят на меня..."
                    her "Вообще-то они для меня ничего не значат..."
                    her "Поэтому мы ждали, пока все выйдут из класса..."
                    #__#hide screen hermione_main                                                                                                                                                                                   #HERMIONE
                    #__#with d3                                                                                                                                                                                                                        #HERMIONE
                    $herView.hideQQ()
                    #__#$ h_body = "03_hp/13_hermione_main/body_117.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
                    #__#show screen hermione_main                                                                                                                                                                                 #HERMIONE
                    #__#with d3       
                    $herView.showQQ( "body_117.png", pos )
                    her "И потом я дала им потрогать себя..."
                    her "Они трогали меня везде, профессор..."
                    m "\"Везде\"?"
                    her "Да... Везде, сэр..."
                    #__#hide screen hermione_main                                                                                                                                                                                   #HERMIONE
                    #__#with d3                                                                                                                                                                                                                        #HERMIONE
                    $herView.hideQQ()
                    #__#$ h_body = "03_hp/13_hermione_main/body_128.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
                    #__#show screen hermione_main                                                                                                                                                                                 #HERMIONE
                    #__#with d3       
                    $herView.showQQ( "body_128.png", pos )
                    her "Их руки были под моей юбкой, под моей блузкой..."
                    her "И потом моё дыхание участилось..."
                    #__#hide screen hermione_main                                                                                                                                                                                   #HERMIONE
                    #__#with d3                                                                                                                                                                                                                        #HERMIONE
                    $herView.hideQQ()
                    #__#$ h_body = "03_hp/13_hermione_main/body_121.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
                    #__#show screen hermione_main                                                                                                                                                                                 #HERMIONE
                    #__#with d3       
                    $herView.showQQ( "body_121.png", pos )
                    her "И один из них засунул свои пальчики ко мне в рот..."
                    her "И их прикосновения были такими... ненасытными..." 
                    her "У меня аж закружилась голова..."
                    #__#hide screen hermione_main                                                                                                                                                                                   #HERMIONE
                    #__#with d3                                                                                                                                                                                                                        #HERMIONE
                    $herView.hideQQ()
                    #__#$ h_body = "03_hp/13_hermione_main/body_128.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
                    #__#show screen hermione_main                                                                                                                                                                                 #HERMIONE
                    #__#with d3       
                    $herView.showQQ( "body_128.png", pos )
                    her "Это было очень возбуждающе, сэр."
                    m "Очень хорошо, Мисс Грейнджер. Просто прекрасно."
                    
                    
                if one_out_of_three == 2: ### EVENT (B)
                    #__#hide screen hermione_main                                                                                                                                                                                   #HERMIONE
                    #__#with d3                                                                                                                                                                                                                        #HERMIONE
                    $herView.hideQQ()
                    #__#$ h_body = "03_hp/13_hermione_main/body_01.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
                    #__#show screen hermione_main                                                                                                                                                                                 #HERMIONE
                    #__#with d3                                                                                                                                                                                                                        #HERMIONE
                    $herView.showQQ( "body_01.png", pos )
                    her "Вообще-то, кое что необычное произошло сегодня со мной, сэр..."
                    her "После занятий по Защите от темных чар..."
                    her "Ко мне подошёл коренастый парень из \"Пуффендуя\"..."
                    #__#hide screen hermione_main                                                                                                                                                                                   #HERMIONE
                    #__#with d3                                                                                                                                                                                                                        #HERMIONE
                    $herView.hideQQ()
                    #__#$ h_body = "03_hp/13_hermione_main/body_122.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
                    #__#show screen hermione_main                                                                                                                                                                                 #HERMIONE
                    #__#with d3                                                                                                                                                                                                                        #HERMIONE
                    $herView.showQQ( "body_122.png", pos )
                    play music "music/(Orchestral) Playful Tension by Shadow16nh.mp3" fadein 1 fadeout 1 # SEX THEME.
                    her "Он рассказал, что до него дошли слухи, что я даю мальчикам трогать себя..."
                    #__#hide screen hermione_main                                                                                                                                                                                   #HERMIONE
                    #__#with d3                                                                                                                                                                                                                        #HERMIONE
                    $herView.hideQQ()
                    #__#$ h_body = "03_hp/13_hermione_main/body_128.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
                    #__#show screen hermione_main                                                                                                                                                                                 #HERMIONE
                    #__#with d3                                                                                                                                                                                                                        #HERMIONE
                    $herView.showQQ( "body_128.png", pos )
                    her "Обычно, я бы даже ничего не сделала..."
                    her "Но я решила не упускать возможность..."
                    #__#hide screen hermione_main                                                                                                                                                                                   #HERMIONE
                    #__#with d3                                                                                                                                                                                                                        #HERMIONE
                    $herView.hideQQ()
                    #__#$ h_body = "03_hp/13_hermione_main/body_78.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
                    #__#show screen hermione_main                                                                                                                                                                                 #HERMIONE
                    #__#with d3                                                                                                                                                                                                                        #HERMIONE
                    $herView.showQQ( "body_78.png", pos )
                    her "Я завела парня в тихое место и разрешила ему потрогать себя..."
                    her "Я позволила ему потрогать меня под одеждой..."
                    her "Потом попросила ему потрогать мою грудь..."
                    #__#hide screen hermione_main                                                                                                                                                                                   #HERMIONE
                    #__#with d3                                                                                                                                                                                                                        #HERMIONE
                    $herView.hideQQ()
                    #__#$ h_body = "03_hp/13_hermione_main/body_128.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
                    #__#show screen hermione_main                                                                                                                                                                                 #HERMIONE
                    #__#with d3                                                                                                                                                                                                                        #HERMIONE
                    $herView.showQQ( "body_128.png", pos )
                    her "Ну, в общем, как обычно..."
                    m "Отлично, мисс Грейнджер."
                    
                if one_out_of_three == 3: ### EVENT (C)
                    stop music fadeout 1.0
                    #__#hide screen hermione_main                                                                                                                                                                                   #HERMIONE
                    #__#with d3                                                                                                                                                                                                                        #HERMIONE
                    $herView.hideQQ()
                    #__#$ h_xpos=370 #Defines position of the Hermione's full length sprite. (Default 370). (Center: 140)                                                       #HERMIONE
                    #__#$ h_body = "03_hp/13_hermione_main/body_44.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
                    #__#show screen hermione_main                                                                                                                                                                                 #HERMIONE
                    #__#with d3                                                                                                                                                                                                                        #HERMIONE
                    $herView.showQQ( "body_44.png", pos )
                    her "Ну..."
                    her "Я сделала то, о чем вы меня просили, сэр..."
                    her "Но... в некотором роде... эм..."
                    #__#hide screen hermione_main                                                                                                                                                                                   #HERMIONE
                    #__#with d3                                                                                                                                                                                                                        #HERMIONE
                    $herView.hideQQ()
                    #__#$ h_body = "03_hp/13_hermione_main/body_78.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
                    #__#show screen hermione_main                                                                                                                                                                                 #HERMIONE
                    #__#with d3                                                                                                                                                                                                                        #HERMIONE
                    $herView.showQQ( "body_78.png", pos )
                    her "Но, в некотором роде, это задание перешло в кое что другое..."
                    play music "music/(Orchestral) Playful Tension by Shadow16nh.mp3" fadein 1 fadeout 1 # SEX THEME.
                    m "Хм?"
                    #__#hide screen hermione_main                                                                                                                                                                                   #HERMIONE
                    #__#with d3                                                                                                                                                                                                                        #HERMIONE
                    $herView.hideQQ()
                    #__#$ h_body = "03_hp/13_hermione_main/body_44.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
                    #__#show screen hermione_main                                                                                                                                                                                 #HERMIONE
                    #__#with d3                                                                                                                                                                                                                        #HERMIONE
                    $herView.showQQ( "body_44.png", pos )
                    her "Хм..."
                    her "Ну, в общем... я была поймана за тем, что давала трогать свою грудь одному мальчику..."
                    m "Ты была поймана? Учителем?"
                    #__#hide screen hermione_main                                                                                                                                                                                   #HERMIONE
                    #__#with d3                                                                                                                                                                                                                        #HERMIONE
                    $herView.hideQQ()
                    #__#$ h_body = "03_hp/13_hermione_main/body_45.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
                    #__#show screen hermione_main                                                                                                                                                                                 #HERMIONE
                    #__#with d3                                                                                                                                                                                                                        #HERMIONE
                    $herView.showQQ( "body_45.png", pos )
                    her "Нет, сэр..."
                    #__#hide screen hermione_main                                                                                                                                                                                   #HERMIONE
                    #__#with d3                                                                                                                                                                                                                        #HERMIONE
                    $herView.hideQQ()
                    #__#$ h_body = "03_hp/13_hermione_main/body_46.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
                    #__#show screen hermione_main                                                                                                                                                                                 #HERMIONE
                    #__#with d3                                                                                                                                                                                                                        #HERMIONE
                    $herView.showQQ( "body_46.png", pos )
                    her "Девушкой этого парня..."
                    m "Интересно..."
                    #__#hide screen hermione_main                                                                                                                                                                                   #HERMIONE
                    #__#with d3                                                                                                                                                                                                                        #HERMIONE
                    $herView.hideQQ()
                    #__#$ h_body = "03_hp/13_hermione_main/body_117.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
                    #__#show screen hermione_main                                                                                                                                                                                 #HERMIONE
                    #__#with d3                                                                                                                                                                                                                        #HERMIONE
                    $herView.showQQ( "body_117.png", pos )
                    her "Сначала, она была зла на него..."
                    #__#hide screen hermione_main                                                                                                                                                                                   #HERMIONE
                    #__#with d3                                                                                                                                                                                                                        #HERMIONE
                    $herView.hideQQ()
                    #__#$ h_body = "03_hp/13_hermione_main/body_122.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
                    #__#show screen hermione_main                                                                                                                                                                                 #HERMIONE
                    #__#with d3                                                                                                                                                                                                                        #HERMIONE
                    $herView.showQQ( "body_122.png", pos )
                    her "Но потом..."
                    #__#hide screen hermione_main                                                                                                                                                                                   #HERMIONE
                    #__#with d3                                                                                                                                                                                                                        #HERMIONE
                    $herView.hideQQ()
                    #__#$ h_body = "03_hp/13_hermione_main/body_124.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
                    #__#show screen hermione_main                                                                                                                                                                                 #HERMIONE
                    #__#with d3                                                                                                                                                                                                                        #HERMIONE
                    $herView.showQQ( "body_124.png", pos )
                    her "Эмм... Она начала трогать мою грудь..."
                    #__#hide screen hermione_main                                                                                                                                                                                   #HERMIONE
                    #__#with d3                                                                                                                                                                                                                        #HERMIONE
                    $herView.hideQQ()
                    #__#$ h_body = "03_hp/13_hermione_main/body_111.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
                    #__#show screen hermione_main                                                                                                                                                                                 #HERMIONE
                    #__#with d3                                                                                                                                                                                                                        #HERMIONE
                    $herView.showQQ( "body_111.png", pos )
                    her "Точно так же, как минуту назад меня трогал её парень..."
                    her "Затем она повернулась к нему и сказала..."
                    #__#hide screen hermione_main                                                                                                                                                                                   #HERMIONE
                    #__#with d3                                                                                                                                                                                                                        #HERMIONE
                    $herView.hideQQ()
                    #__#$ h_body = "03_hp/13_hermione_main/body_16.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
                    #__#show screen hermione_main                                                                                                                                                                                 #HERMIONE
                    #__#with d3                                                                                                                                                                                                                        #HERMIONE
                    $herView.showQQ( "body_16.png", pos )
                    her "\"Я люблю тебя, дорогой, И хочу разделить с тобой всё...\""
                    her "\"...включая твоих шлюх.\""
                    #__#hide screen hermione_main                                                                                                                                                                                   #HERMIONE
                    #__#with d3                                                                                                                                                                                                                        #HERMIONE
                    $herView.hideQQ()
                    #__#$ h_body = "03_hp/13_hermione_main/body_117.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
                    #__#show screen hermione_main                                                                                                                                                                                 #HERMIONE
                    #__#with d3                                                                                                                                                                                                                        #HERMIONE
                    $herView.showQQ( "body_117.png", pos )
                    her "Я была возмущена тем, что она назвала меня шлюхой..."
                    #__#hide screen hermione_main                                                                                                                                                                                   #HERMIONE
                    #__#with d3                                                                                                                                                                                                                        #HERMIONE
                    $herView.hideQQ()
                    #__#$ h_body = "03_hp/13_hermione_main/body_06.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
                    #__#show screen hermione_main                                                                                                                                                                                 #HERMIONE
                    #__#with d3                                                                                                                                                                                                                        #HERMIONE
                    $herView.showQQ( "body_06.png", pos )
                    her "Но это был такой милый и романтический жест..."
                    her "Вы согласны со мной, сэр?"
                    m "Абсолютно..."
                    m "Вот, что значит настоящая любовь - она {size=+5} должна {/size} проходить через всё."
                    m "И что же случилось потом?"
                    #__#hide screen hermione_main                                                                                                                                                                                   #HERMIONE
                    #__#with d3                                                                                                                                                                                                                        #HERMIONE
                    $herView.hideQQ()
                    #__#$ h_body = "03_hp/13_hermione_main/body_24.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
                    #__#show screen hermione_main                                                                                                                                                                                 #HERMIONE
                    #__#with d3                                                                                                                                                                                                                        #HERMIONE
                    $herView.showQQ( "body_24.png", pos )
                    her "Эм... Они поцеловались, конечно же..."
                    #__#hide screen hermione_main                                                                                                                                                                                   #HERMIONE
                    #__#with d3                                                                                                                                                                                                                        #HERMIONE
                    $herView.hideQQ()
                    #__#$ h_body = "03_hp/13_hermione_main/body_44.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
                    #__#show screen hermione_main                                                                                                                                                                                 #HERMIONE
                    #__#with d3                                                                                                                                                                                                                        #HERMIONE
                    $herView.showQQ( "body_44.png", pos )
                    her "И парень начал трогать меня снова..."
                    #__#hide screen hermione_main                                                                                                                                                                                   #HERMIONE
                    #__#with d3                                                                                                                                                                                                                        #HERMIONE
                    $herView.hideQQ()
                    #__#$ h_body = "03_hp/13_hermione_main/body_29.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
                    #__#show screen hermione_main                                                                                                                                                                                 #HERMIONE
                    #__#with d3                                                                                                                                                                                                                        #HERMIONE
                    $herView.showQQ( "body_29.png", pos )
                    her "И потом он трогал её и она трогала его..."
                    her "И они целовались..."
                    her "Я почувствовала себя третьей лишней и решила тихо удалиться......"
                    m "Ясно..."
                    

    $ gryffindor +=25
    m " \"Гриффиндор\" получает 25 очков!"
    her "Спасибо, сэр."
    
    hide screen bld1
    #__#hide screen hermione_main
    $herView.hideQ() #"WARNING_Z"
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



    $ touched_by_boy = True #Makes sure that Public favours do not get locked after reaching Whoring level 05.
    
    call music_block
    
    $ request_10_points += 1 
    $ request_10 = False 
    $ hermione_sleeping = True
    return


