################### REQUEST_03 (Level 02) (Available during daytime only). "Give me your Трусики" ###############################
label new_request_03: #(Whoring = 3 - 5)
    if whoring <= 2:
        jump too_much
    #__#hide screen hermione_main
    #__#with d3
    $herView.hideQQ()
    
    $ pos = POS_370
    
    m "{size=-4}(Попросить ее отдать мне трусики и пойти на занятия?){/size}"
    $ menu_x = 0.5 #Default position of the menu. Version B is $ menu_x = 0.2
    menu:
        "\"(Да, давай попробуем!)\"":
            pass
        "\"(Не сейчас.)\"":
            jump new_personal_request
    $herView.showQQ( None, pos )
    #__# "Мисс Грейнджер?"
    #show screen hermione_main
    #__#with d3
    her "Я слушаю, сэр."
    m "Мне нужны ваши трусики..."   
    #__#hide screen hermione_main
    #__#with d3
    $herView.hideQQ()
    $ menu_x = 0.5 #Menu is moved to the left side.
    #__#$ h_xpos=120 #Defines position of the Hermione's full length sprite. Left: 370 Center: 120
    #__#$ h_ypos=0
    $ pos = POS_120
    #__#$ h_body = "03_hp/13_hermione_main/body_01.png" #Sprite of Hermione's upper body.
    #__#$herView.showQ( "body_01.png", pos, Dissolve(.3) )
    show screen blktone 
    show screen ctc
    #__#show screen hermione_main
    $herView.showQ( "body_01.png", pos )
    with Dissolve(.3)
    pause
    
    
    if request_03 == 0 and whoring <= 5: #First time this event taking place. and LEVEL 02.   <===================================== ONE TIME EVENT.
        stop music fadeout 10.0
        $ new_request_03_01 = True # HEARTS.
        $ request_03 += 1
        #__#hide screen hermione_main
        #__#with d3
        $herView.hideQQ()
        #__#$ h_xpos=120 #Defines position of the Hermione's full length sprite.
        #__#$ pos = POS_120
        #__#$ h_body = "03_hp/13_hermione_main/body_11.png" #Flashing Трусики
        #__#show screen hermione_main
        #__#with d3
        $herView.showQQ( "body_11.png", pos )
        her "Ч-что?"
        her "Мои... Трусики...?"
        her "Профессор Дамблдор, это..."
        m "Это моя сегодняшняя просьба, Мисс Грейнджер..."
        m "Если вам не интересно, можете уходить."
        her "Нет, мне интересно. Да... просто это..."
        her "Вам нужны мои...."
        play music "music/Chipper Doodle v2.mp3" fadein 1 fadeout 1 # HERMIONE'S THEME.
        #__#hide screen hermione_main
        #__#with d3
        $herView.hideQQ()
        #__#$ h_xpos=120 #Defines position of the Hermione's full length sprite.
        #__#$ h_body = "03_hp/13_hermione_main/body_47.png" #Flashing Трусики
        #__#show screen hermione_main
        #__#with d3
        $herView.showQQ( "body_47.png", pos )
        her "...Трусики, сэр?"
        m "Именно..."
        #__#hide screen hermione_main
        #__#with d3
        $herView.hideQQ()
        #__#$ h_xpos=120 #Defines position of the Hermione's full length sprite.
        #__#$ h_body = "03_hp/13_hermione_main/body_66.png" #Flashing Трусики
        #__#show screen hermione_main
        #__#with d3
        $herView.showQQ( "body_66.png", pos )
        her "Могу ли я узнать, что вы планируете с ними делать...?"
        m "Эм...Я провожу исследования..."
        her "Но это немного странно, не находите?"
        m "Но вам ведь не нравится, что девушки из \"Слизерина\"..."
        m "Оказывают услуги за очки для факультета, не так ли, Мисс Грейнджер?"
        #__#hide screen hermione_main
        #__#with d3
        $herView.hideQQ()
        #__#$ h_xpos=120 #Defines position of the Hermione's full length sprite.
        #__#$ h_body = "03_hp/13_hermione_main/body_47.png" #Flashing Трусики
        #__#show screen hermione_main
        #__#with d3
        $herView.showQQ( "body_47.png", pos )
        her "Верно!"
        #__#hide screen hermione_main
        #__#with d3
        $herView.hideQQ()
        #__#$ h_xpos=120 #Defines position of the Hermione's full length sprite.
        #__#$ h_body = "03_hp/13_hermione_main/body_12.png" #Flashing Трусики
        #__#show screen hermione_main
        #__#with d3
        $herView.showQQ( "body_12.png", pos )
        her "(Эти \"Слизеринские\" шлюхи потеряли все достоинство.)"
        #__#hide screen hermione_main
        #__#with d3
        $herView.hideQQ()
        m "Ну, тогда давайте!"
        #__#hide screen hermione_main
        #__#with d3
        $herView.hideQQ()
        #__#$ h_xpos=120 #Defines position of the Hermione's full length sprite.
        #__#$ h_body = "03_hp/13_hermione_main/body_66.png" #Flashing Трусики
        #__#show screen hermione_main
        #__#with d3
        $herView.showQQ( "body_66.png", pos )
        her "А?"
        m "Победите их в их же собственной игре!"
        #__#hide screen hermione_main
        #__#with d3
        $herView.hideQQ()
        #__#$ h_xpos=120 #Defines position of the Hermione's full length sprite.
        #__#$ h_body = "03_hp/13_hermione_main/body_14.png" #Flashing Трусики
        #__#show screen hermione_main
        #__#with d3
        $herView.showQQ( "body_14.png", pos )
        her "Что?"
        m "Да! Не дайте \"Слизерину\" вырваться в лидеры..."
        m "Но я не могу сделать этого прос так, даже, чтобы победить в игре!"
        #__#hide screen hermione_main
        #__#with d3
        $herView.hideQQ()
        #__#$ h_xpos=120 #Defines position of the Hermione's full length sprite.
        #__#$ h_body = "03_hp/13_hermione_main/body_11.png" #Flashing Трусики
        #__#show screen hermione_main
        #__#with d3
        $herView.showQQ( "body_11.png", pos )
        her "Профессор..."
        m "Директор не может иметь любимчиков, но вы знаете, что я думаю о \"Гриффиндоре\"..."
        m "Я могу просто дать вам очков, но это разрушит всю систему..."
        show screen blktone8
        #__#hide screen hermione_main
        #__#with d3
        $herView.hideQQ()
        ">Внезапно Гермиона протягивает вам руку..."
        ">Вы замечаете, что она сжимает какую-то ткань в кулаке..."
        ">Ее трусики? Вы не можете понять, когда же она успела их снять..."
        m "??!"
        ">Вы получили трусики Гермионы..."
        hide screen blktone8
        with d3
        #__#hide screen hermione_main
        #__#with d3
        $herView.hideQQ()
        #__#$ h_xpos=120 #Defines position of the Hermione's full length sprite.
        #__#$ h_body = "03_hp/13_hermione_main/body_67.png" #Flashing Трусики
        #__#show screen hermione_main
        #__#with d3
        $herView.showQQ( "body_67.png", pos )
        
        her "Просто возьмите их, сэр..."
        m "Что? Когда ты успела?"
        her "Ваша речь была такой трогательной..."
        her "Вы совершенно правы, сэр! Я должна победить их в этой игре."
        her "Мои занятия вот-вот начнутся. Мне лучше пойти..."
        #__#hide screen hermione_main
        #__#with d3
        $herView.hideQQ()

        #__#$ h_xpos=370 #Right: 370 Center: 120
        $ pos = POS_370
        #__#$ h_body = "03_hp/13_hermione_main/body_23.png" #Flashing Трусики
        #__#show screen hermione_main
        #__#with d3
        $herView.showQQ( "body_23.png", pos )
        her "..........."
        #__#hide screen hermione_main
        #__#with d3
        $herView.hideQQ()
        #__#$ h_xpos=370 #Right: 370 Center: 120
        #__#$ h_body = "03_hp/13_hermione_main/body_29.png" #Flashing Трусики
        #__#show screen hermione_main
        #__#with d3
        $herView.showQQ( "body_29.png", pos )
        her "...Я надеюсь, что никто не заметит, что у меня нет белья..."
        #__#hide screen hermione_main
        #__#with d3
        $herView.hideQQ()
        #__#$ h_xpos=370 #Right: 370 Center: 120
        #__#$ h_body = "03_hp/13_hermione_main/body_31.png" #Flashing Трусики
        #__#show screen hermione_main
        #__#with d3
        $herView.showQQ( "body_31.png", pos )
        her "Ох, я вернусь за ними вечером, сэр."
        m "Конечно. Твои трусики будут лежать на моем столе и ждать тебя..."
        #__#hide screen hermione_main
        #__#with d3
        $herView.hideQQ()
        #__#$ h_xpos=370 #Right: 370 Center: 120
        #__#$ h_body = "03_hp/13_hermione_main/body_34.png" #Flashing Трусики
        #__#show screen hermione_main
        #__#with d3
        $herView.showQQ( "body_34.png", pos )
        her "............."
        jump request_03_ends

    else: #<========================================================================================== FIRST EVENT!
        if request_03 >= 1:
            her "Снова, сэр?"
            m "Да, снова..."
        her "Вот..."
        if whoring >= 12: #LEVEL 05
            #__#hide screen hermione_main
            #__#with d3
            $herView.hideQQ()
            ">Гермиона достает свои трусики из кармана..."
            m "Что?"
            #__#hide screen hermione_main
            #__#with d3
            $herView.hideQQ()
            #__#$ h_xpos=120 #Defines position of the Hermione's full length sprite.
            #__#$ pos = POS_120
            #__#$ h_body = "03_hp/13_hermione_main/body_45.png" #Flashing Трусики
            #__#show screen hermione_main
            #__#with d3
            $herView.showQQ( "body_45.png", pos )
            her "Да, у меня было ощущение, что вы их попросите сегодня, сэр."
            m "Было ощущение?"
            #__#hide screen hermione_main
            #__#with d3
            $herView.hideQQ()
            #__#$ h_xpos=120 #Defines position of the Hermione's full length sprite.
            #__#$ h_body = "03_hp/13_hermione_main/body_68.png" #Flashing Трусики
            #__#show screen hermione_main
            #__#with d3
            $herView.showQQ( "body_68.png", pos )
            her "Ну, если быть честной, то я теперь не всегда их надеваю..."
        else:
            #__#hide screen hermione_main
            #__#with d3
            $herView.hideQQ()
            ">Гермиона снимает трусики и отдает их вам..."
        #__#hide screen hermione_main
        #__#with d3
        $herView.hideQQ()
        ">Получены трусики Гермионы."
        #__#$ h_body = "03_hp/13_hermione_main/body_15.png" #Flashing Трусики
        #__#show screen hermione_main
        #__#with d3
        $herView.showQQ( "body_15.png", pos )
        her "Ну, мне стоит идти на занятия. Они вот-вот начнутся..."

        
    label request_03_ends:
    $ request_03 = True #True when Hermione has no Трусики on.
    if whoring <= 5:
        $ whoring +=1
        
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


    ### MUSIC BLOCK ###
    if daytime:
        play music "music/Brittle Rille.mp3" fadein 1 fadeout 1 # DAY MUSIC
    else:
        play music "music/Music for Manatees.mp3" fadein 1 fadeout 1 # NIGHT MUSIC
    ### END OF BLOCK ###

    jump day_main_menu
    
    
        
label new_request_03_complete: # WHORING LEVEL 02 <=================
    
    $ walk_xpos=610 #Animation of walking chibi. (From)
    $ walk_xpos2=400 #Coordinates of it's movement. (To)
    $ hermione_speed = 03.0 #The speed of moving the walking animation across the screen.
    $ renpy.play('sounds/door.mp3') #Sound of a door opening.
    show screen hermione_walk_01 
    with d4
    pause 2.5
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

    $ pos = POS_120
    
    "Добрый вечер, сэр..."
    play music "music/Chipper Doodle v2.mp3" fadein 1 fadeout 1 # HERMIONE'S THEME.
    menu:
        "\"Вот твои трусики.\"":
            if have_cum_soaced_panties:
                jump panties_soaked_in_cum
            else:
                her "Спасибо, сэр."
                her "И моя оплата?"
                m "Конечно."
        "\"Как прошел ваш день, Мисс Грейнджер?\"":
            if  whoring <= 5: #LEVEL 02. EVENT LEVEL: 01
                $ new_request_03_01 = True # HEARTS.
                #__#hide screen hermione_main
                #__#with d3
                $herView.hideQQ()
                #__#$ h_xpos=120 #Defines position of the Hermione's full length sprite. center: 120. Right: 370.
                $ pos = POS_120
                #__#$ h_body = "03_hp/13_hermione_main/body_15.png" #Flashing Трусики
                #__#show screen hermione_main
                #__#with d3
                $herView.showQQ( "body_15.png", pos )
                her "Ох..."
                her "Довольно обычно..."
                #__#hide screen hermione_main
                #__#with d3
                $herView.hideQQ()
                #__#$ h_xpos=120 #Defines position of the Hermione's full length sprite.
                #__#$ h_body = "03_hp/13_hermione_main/body_13.png" #Flashing Трусики
                #__#show screen hermione_main
                #__#with d3
                $herView.showQQ( "body_13.png", pos )
                her "Хотя я не уверена, возможно кто-то мог заметить, что я..."
                #__#hide screen hermione_main
                #__#with d3
                $herView.hideQQ()
                #__#$ h_xpos=120 #Defines position of the Hermione's full length sprite. center: 120. Right: 370.
                #__#$ h_body = "03_hp/13_hermione_main/body_29.png" #Flashing Трусики
                #__#show screen hermione_main
                #__#with d3
                $herView.showQQ( "body_29.png", pos )
                her "....."
                #__#hide screen hermione_main
                #__#with d3
                $herView.hideQQ()
                #__#$ h_xpos=120 #Defines position of the Hermione's full length sprite. center: 120. Right: 370.
                #__#$ h_body = "03_hp/13_hermione_main/body_31.png" #Flashing Трусики
                #__#show screen hermione_main
                #__#with d3
                $herView.showQQ( "body_31.png", pos )
                her "Могу я получить свои трусики назад?"
                m "Конечно..."
                #__#hide screen hermione_main
                #__#with d3
                $herView.hideQQ()
                ">Вы отдаете Гермионее ее трусики..."
                if have_cum_soaced_panties:
                    jump panties_soaked_in_cum
                else:
                    #__#hide screen hermione_main
                    #__#with d3
                    $herView.hideQQ()
                    #__#$ h_xpos=120 #Defines position of the Hermione's full length sprite. center: 120. Right: 370.
                    #__#$ h_body = "03_hp/13_hermione_main/body_31.png" #Flashing Трусики
                    #__#show screen hermione_main
                    #__#with d3
                    $herView.showQQ( "body_31.png", pos )
                    her "И мои очки?"
                    m "Да, да..."
            elif whoring >= 6 and whoring <= 8: #LEVEL 03. EVENT LEVEL 02.
                $ new_request_03_02 = True # HEARTS.
                #__#hide screen hermione_main
                #__#with d3
                $herView.hideQQ()
                #__#$ h_xpos=120 #Defines position of the Hermione's full length sprite. center: 120. Right: 370.
                $ pos = POS_120
                #__#$ h_body = "03_hp/13_hermione_main/body_15.png" #Flashing Трусики
                #__#show screen hermione_main
                #__#with d3
                $herView.showQQ( "body_15.png", pos )
                her "Ох..."
                her "Все как всегда..."
                her "Я провела некоторое время с одноклассниками..."
                her "И у нас было недолго собрание \"ОЗМП\"..."
                translators "Напоминание.\nОЗМП - Общество по Защите Мужских Прав."
                #__#hide screen hermione_main
                #__#with d3
                $herView.hideQQ()
                #__#$ h_xpos=120 #Defines position of the Hermione's full length sprite. center: 120. Right: 370.
                #__#$ h_body = "03_hp/13_hermione_main/body_16.png" #Flashing Трусики
                #__#show screen hermione_main
                #__#with d3
                $herView.showQQ( "body_16.png", pos )
                her "Я произносила небольшую речь на тему \"Почему обменивать очки для факультета на сексуальные услуги это плохо\"..."
                #__#hide screen hermione_main
                #__#with d3
                $herView.hideQQ()
                #__#$ h_xpos=120 #Defines position of the Hermione's full length sprite. center: 120. Right: 370.
                #__#$ h_body = "03_hp/13_hermione_main/body_12.png" #Flashing Трусики
                #__#show screen hermione_main
                #__#with d3
                $herView.showQQ( "body_12.png", pos )
                her "Я чувствовала себя не очень, так как была без белья..."
                menu:
                    "\"Ах ты маленькая лицемерка!\"":
                        $ mad +=5
                        #__#hide screen hermione_main
                        #__#with d3
                        $herView.hideQQ()
                        #__#$ h_xpos=120 #Defines position of the Hermione's full length sprite. center: 120. Right: 370.
                        #__#$ h_body = "03_hp/13_hermione_main/body_14.png" #Flashing Трусики
                        #__#show screen hermione_main
                        #__#with d3
                        $herView.showQQ( "body_14.png", pos )
                        her "Профессор?"
                        m "Только этим утром ты обменяла свои труски..."
                        m "И несколькими часами позднее произносила речь, осуждая подобное..."
                        #m "What would you call this?"
                        #__#hide screen hermione_main
                        #__#with d3
                        $herView.hideQQ()
                        #__#$ h_xpos=120 #Defines position of the Hermione's full length sprite. center: 120. Right: 370.
                        #__#$ h_body = "03_hp/13_hermione_main/body_69.png" #Flashing Трусики
                        #__#show screen hermione_main
                        #__#with d3
                        $herView.showQQ( "body_69.png", pos )
                        #her "I know you are right, профессор..."
                        her "(Но нам нужны эти очки...)"
                        #__#hide screen hermione_main
                        #__#with d3
                        $herView.hideQQ()
                        #__#$ h_xpos=120 #Defines position of the Hermione's full length sprite. center: 120. Right: 370.
                        #__#$ h_body = "03_hp/13_hermione_main/body_66.png" #Flashing Трусики
                        #__#show screen hermione_main
                        #__#with d3
                        $herView.showQQ( "body_66.png", pos )
                        her "Могу я получить свои очки?"
                        m "Что насчет трусиков?"
                        #__#hide screen hermione_main
                        #__#with d3
                        $herView.hideQQ()
                        #__#$ h_xpos=120 #Defines position of the Hermione's full length sprite. center: 120. Right: 370.
                        #__#$ h_body = "03_hp/13_hermione_main/body_34.png" #Flashing Трусики
                        #__#show screen hermione_main
                        #__#with d3
                        $herView.showQQ( "body_34.png", pos )
                        her "Ох, их, конечно же, тоже..." 
                        if have_cum_soaced_panties:
                            jump panties_soaked_in_cum
                        else:
                            pass
                    "\"Это для блага...\"":
                        her "Именно!"
                        her "Нам очень нужны эти очки..."
                        her "Это не моя ошибка, это дыры в системе образования..."
                        #__#hide screen hermione_main
                        #__#with d3
                        $herView.hideQQ()
                        #__#$ h_xpos=120 #Defines position of the Hermione's full length sprite. center: 120. Right: 370.
                        #__#$ h_body = "03_hp/13_hermione_main/body_16.png" #Flashing Трусики
                        #__#show screen hermione_main
                        #__#with d3
                        $herView.showQQ( "body_16.png", pos )
                        her "Я не перестану быть символом праведности для моих сверстников!"
                        #__#hide screen hermione_main
                        #__#with d3
                        $herView.hideQQ()
                        #__#$ h_xpos=120 #Defines position of the Hermione's full length sprite. center: 120. Right: 370.
                        #__#$ h_body = "03_hp/13_hermione_main/body_31.png" #Flashing Трусики
                        #__#show screen hermione_main
                        #__#with d3
                        $herView.showQQ( "body_31.png", pos )
                        her "Могу я получить свои трусики обратно, пожалуйста?"
                        if have_cum_soaced_panties:
                            jump panties_soaked_in_cum
                        else:
                            her "И мои очки."
            elif whoring >= 9: #LEVEL 04. EVENT LEVEL 03.
                $ new_request_03_03 = True # HEARTS.
                #__#hide screen hermione_main
                #__#with d3
                $herView.hideQQ()
                #__#$ h_xpos=120 #Defines position of the Hermione's full length sprite. center: 120. Right: 370.
                $ pos = POS_120
                #__#$ h_body = "03_hp/13_hermione_main/body_16.png" #Flashing Трусики
                #__#show screen hermione_main
                #__#with d3
                $herView.showQQ( "body_16.png", pos )
                her "Еще один обычный день в Хогвартсе..."
                her "Ничего примечательного..."
                #__#hide screen hermione_main
                #__#with d3
                $herView.hideQQ()
                #__#$ h_xpos=120 #Defines position of the Hermione's full length sprite. center: 120. Right: 370.
                #__#$ h_body = "03_hp/13_hermione_main/body_29.png" #Flashing Трусики
                #__#show screen hermione_main
                #__#with d3
                $herView.showQQ( "body_29.png", pos )
                her "Хотя, должна признаться..."
                her "Я была по странному свободна без белья..."
                her "Хм..."
                #__#hide screen hermione_main
                #__#with d3
                $herView.hideQQ()
                #__#$ h_xpos=120 #Defines position of the Hermione's full length sprite. center: 120. Right: 370.
                #__#$ h_body = "03_hp/13_hermione_main/body_45.png" #Flashing Трусики
                #__#show screen hermione_main
                #__#with d3
                $herView.showQQ( "body_45.png", pos )
                her "Я могу получить свои трусики назад?"
                m "Конечно..."
                #__#hide screen hermione_main
                #__#with d3
                $herView.hideQQ()
                ">Вы отдаете Гермионее ее трусики..."
                if have_cum_soaced_panties:
                    jump panties_soaked_in_cum
                else:
                    #__#hide screen hermione_main
                    #__#with d3
                    $herView.hideQQ()
                    #__#$ h_xpos=120 #Defines position of the Hermione's full length sprite. center: 120. Right: 370.
                    #__#$ h_body = "03_hp/13_hermione_main/body_45.png" #Flashing Трусики
                    #__#show screen hermione_main
                    #__#with d3
                    $herView.showQQ( "body_45.png", pos )
                    her "И мои очки?"
                    m "Да, да..."
    label back_from_panties:
    $ gryffindor +=15
    m "Пятнадцать очков \"Гриффиндору\", мисс Грейнджер. Вы заслужили." 
    her "Спасибо, сэр..."
    m "Можешь идти."
    her "Доброй ночи, сэр."
    #m "Да, доброй ночи..."

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



    $ request_03_points += 1 #Leveling up the event.
    $ request_03 = False #When False - you gave her her Трусики back.
    $ hermione_sleeping = True

    play music "music/Music for Manatees.mp3" fadein 1 fadeout 1 # NIGHT MUSIC

    return 
    
    
    
### Трусики SOAKED IN CUM ###
label panties_soaked_in_cum:
    $ have_cum_soaced_panties = False #TRUE when you have the Трусики in your possession (before you return them to Hermione).
    $ she_knows_about_cum = False
    $ pos = POS_120
    
    if whoring >= 3 and whoring <= 5: # LEVEL 02
        #__#hide screen hermione_main
        #__#with d3
        $herView.hideQQ()
        #__#$ h_xpos=120 #Defines position of the Hermione's full length sprite. center: 120. Right: 370.
        #__#$ pos = POS_120
        #__#$ h_body = "03_hp/13_hermione_main/body_71.png" #Flashing Трусики
        #__#show screen hermione_main
        #__#with d3
        $herView.showQQ( "body_71.png", pos )
        her "Хм....?"
        #__#hide screen hermione_main
        #__#with d3
        $herView.hideQQ()
        #__#$ h_xpos=120 #Defines position of the Hermione's full length sprite. center: 120. Right: 370.
        #__#$ h_body = "03_hp/13_hermione_main/body_05.png" #Flashing Трусики
        #__#show screen hermione_main
        #__#with d3
        $herView.showQQ( "body_05.png", pos )
        her "Сэр? Что это такое?"
        her "Что вы с ними сделали?"
        #__#hide screen hermione_main
        #__#with d3
        $herView.hideQQ()
        #__#$ h_xpos=120 #Defines position of the Hermione's full length sprite. center: 120. Right: 370.
        #__#$ h_body = "03_hp/13_hermione_main/body_07.png" #Flashing Трусики
        #__#show screen hermione_main
        #__#with d3
        $herView.showQQ( "body_07.png", pos )
        her "Они в чем-то скользком..."
        menu:
            "\"Эксперимент провалился.\"":
                #__#hide screen hermione_main
                #__#with d3
                $herView.hideQQ()
                #__#$ h_xpos=120 #Defines position of the Hermione's full length sprite. center: 120. Right: 370.
                #__#$ h_body = "03_hp/13_hermione_main/body_02.png" #Flashing Трусики
                #__#show screen hermione_main
                #__#with d3
                $herView.showQQ( "body_02.png", pos )
                her "Эсперимент провалился, сэр?"
                m "Да...Или, лучше сказать..."
                g9 "\"Эксперимент прошел очень хорошо\"? Хе-хе..."
                #__#hide screen hermione_main
                #__#with d3
                $herView.hideQQ()
                #__#$ h_xpos=120 #Defines position of the Hermione's full length sprite. center: 120. Right: 370.
                #__#$ h_body = "03_hp/13_hermione_main/body_07.png" #Flashing Трусики
                #__#show screen hermione_main
                #__#with d3
                $herView.showQQ( "body_07.png", pos )
                her ".....................?"
                her "Что это был за эксперимент?"
                m "Что? Ох..."
                m "Я провожу пару сверх-секретных исследований."
                m "Я не могу обсуждать их со студентами."
                #__#hide screen hermione_main
                #__#with d3
                $herView.hideQQ()
                #__#$ h_xpos=120 #Defines position of the Hermione's full length sprite. center: 120. Right: 370.
                #__#$ h_body = "03_hp/13_hermione_main/body_05.png" #Flashing Трусики
                #__#show screen hermione_main
                #__#with d3
                $herView.showQQ( "body_05.png", pos )
                her "................................"
            "\"Вы мне дали их такими!\"":
                her "Я уверена, что это не так, сэр!"
                her ".........................."
        #__#hide screen hermione_main
        #__#with d3
        $herView.hideQQ()
        #__#$ h_xpos=120 #Defines position of the Hermione's full length sprite. center: 120. Right: 370.
        #__#$ h_body = "03_hp/13_hermione_main/body_71.png" #Flashing Трусики
        #__#show screen hermione_main
        #__#with d3
        $herView.showQQ( "body_71.png", pos )
        her "Ну, мне потребуется сперва очистить их от всего этого..."
        m "Или ты можешь их надеть прямо сейчас."
        #__#hide screen hermione_main
        #__#with d3
        $herView.hideQQ()
        #__#$ h_xpos=120 #Defines position of the Hermione's full length sprite. center: 120. Right: 370.
        #__#$ h_body = "03_hp/13_hermione_main/body_14.png" #Flashing Трусики
        #__#show screen hermione_main
        #__#with d3
        $herView.showQQ( "body_14.png", pos )
        her "Что?"
        #__#hide screen hermione_main
        #__#with d3
        $herView.hideQQ()
        #__#$ h_xpos=120 #Defines position of the Hermione's full length sprite. center: 120. Right: 370.
        #__#$ h_body = "03_hp/13_hermione_main/body_13.png" #Flashing Трусики
        #__#show screen hermione_main
        #__#with d3
        $herView.showQQ( "body_13.png", pos )
        her "Мне бы этого правда не хотелось, сэр..."
        menu:
            "\"Надень их или потеряешь очки!\"":
                $ mad +=7
                #__#hide screen hermione_main
                #__#with d3
                $herView.hideQQ()
                #__#$ h_xpos=120 #Defines position of the Hermione's full length sprite. center: 120. Right: 370.
                #__#$ h_body = "03_hp/13_hermione_main/body_72.png" #Flashing Трусики
                #__#show screen hermione_main
                #__#with d3
                $herView.showQQ( "body_72.png", pos )
                her "Что?"
                her "Профессор, вы шутите, так?"
                m "Вообще-то нет..."
                #__#hide screen hermione_main
                #__#with d3
                $herView.hideQQ()
                #__#$ h_xpos=120 #Defines position of the Hermione's full length sprite. center: 120. Right: 370.
                #__#$ h_body = "03_hp/13_hermione_main/body_31.png" #Flashing Трусики
                #__#show screen hermione_main
                #__#with d3
                $herView.showQQ( "body_31.png", pos )
                her "Н-но..."
                #__#hide screen hermione_main
                #__#with d3
                $herView.hideQQ()
                #__#$ h_xpos=120 #Defines position of the Hermione's full length sprite. center: 120. Right: 370.
                #__#$ h_body = "03_hp/13_hermione_main/body_33.png" #Flashing Трусики
                #__#show screen hermione_main
                #__#with d3
                $herView.showQQ( "body_33.png", pos )
                her "........................................"
                #__#hide screen hermione_main
                #__#with d3
                $herView.hideQQ()
                #__#$ h_xpos=120 #Defines position of the Hermione's full length sprite. center: 120. Right: 370.
                #__#$ h_body = "03_hp/13_hermione_main/body_47.png" #Flashing Трусики
                #__#show screen hermione_main
                #__#with d3
                $herView.showQQ( "body_47.png", pos )
                her "(ВЫ всегда настаиваете на своем, сэр?)"
                m "Что такое, Мисс Грейнджер?"
                #__#hide screen hermione_main
                #__#with d3
                $herView.hideQQ()
                #__#$ h_xpos=120 #Defines position of the Hermione's full length sprite. center: 120. Right: 370.
                #__#$ h_body = "03_hp/13_hermione_main/body_30.png" #Flashing Трусики
                #__#show screen hermione_main
                #__#with d3
                $herView.showQQ( "body_30.png", pos )
                her "Ничего, сэр."
                her "Верните мне трусики!"
                #__#hide screen hermione_main
                #__#with d3
                $herView.hideQQ()
                show screen blktone8
                with d3
                ">Гермиона нерешительно надевает трусики..."
                ">Несколько капель спермы стекают по ее ноге..."
                ">Гермионе, видимо, очень неудобно..."
                hide screen blktone8
                with d3
                #__#hide screen hermione_main
                #__#with d3
                $herView.hideQQ()
                #__#$ h_xpos=120 #Defines position of the Hermione's full length sprite. center: 120. Right: 370.
                #__#$ h_body = "03_hp/13_hermione_main/body_34.png" #Flashing Трусики
                #__#show screen hermione_main
                #__#with d3
                $herView.showQQ( "body_34.png", pos )
                her "......................"
            "\"Ну, как хочешь...\"":
                pass
    if whoring >= 6 and whoring <= 8: # LEVEL 03 (SECOND EVENT)
        #__#hide screen hermione_main
        #__#with d3
        $herView.hideQQ()
        #__#$ h_xpos=120 #Defines position of the Hermione's full length sprite. center: 120. Right: 370.
        #__#$ pos = POS_120
        #__#$ h_body = "03_hp/13_hermione_main/body_71.png" #Flashing Трусики
        #__#show screen hermione_main
        #__#with d3
        $herView.showQQ( "body_71.png", pos )
        her "Мои трусики..."
        #__#hide screen hermione_main
        #__#with d3
        $herView.hideQQ()
        #__#$ h_xpos=120 #Defines position of the Hermione's full length sprite. center: 120. Right: 370.
        #__#$ h_body = "03_hp/13_hermione_main/body_73.png" #Flashing Трусики
        #__#show screen hermione_main
        #__#with d3
        $herView.showQQ( "body_73.png", pos )
        her "Что произошло с ними, сэр?"
        menu: 
            "\"Эксперимент не увенчался успехом.\"":
                her "Хм..."
                her "Понятно..."
            "\"Вы мне дали их такими!\"":
                her "Да? Ох, ясно..."
        #__#hide screen hermione_main
        #__#with d3
        $herView.hideQQ()
        ">Гермиона, усмехаясь, берет свои пропитаные спермой трусики..."
        #__#hide screen hermione_main
        #__#with d3
        $herView.hideQQ()
        #__#$ h_xpos=120 #Defines position of the Hermione's full length sprite. center: 120. Right: 370.
        #__#$ h_body = "03_hp/13_hermione_main/body_71.png" #Flashing Трусики
        #__#show screen hermione_main
        #__#with d3
        $herView.showQQ( "body_71.png", pos )
        her "Вероятно, их стоит очистить прежде чем надевать..."
        m "Почему бы не надеть их прямо сейчас?"
        #__#hide screen hermione_main
        #__#with d3
        $herView.hideQQ()
        #__#$ h_xpos=120 #Defines position of the Hermione's full length sprite. center: 120. Right: 370.
        #__#$ h_body = "03_hp/13_hermione_main/body_17.png" #Flashing Трусики
        #__#show screen hermione_main
        #__#with d3
        $herView.showQQ( "body_17.png", pos )
        her "Хм....?"
        #__#hide screen hermione_main
        #__#with d3
        $herView.hideQQ()
        #__#$ h_xpos=120 #Defines position of the Hermione's full length sprite. center: 120. Right: 370.
        #__#$ h_body = "03_hp/13_hermione_main/body_71.png" #Flashing Трусики
        #__#show screen hermione_main
        #__#with d3
        $herView.showQQ( "body_71.png", pos )
        her "Ну, думаю можно их надеть еще раз, прежде чем постирать..."
        #__#hide screen hermione_main
        #__#with d3
        $herView.hideQQ()
        show screen blktone8
        with d3
        ">Гермиона надевает свои трусики..."
        hide screen blktone8
        with d3
        #__#hide screen hermione_main
        #__#with d3
        $herView.hideQQ()
        #__#$ h_xpos=120 #Defines position of the Hermione's full length sprite. center: 120. Right: 370.
        #__#$ h_body = "03_hp/13_hermione_main/body_34.png" #Flashing Трусики
        #__#show screen hermione_main
        #__#with d3
        $herView.showQQ( "body_34.png", pos )
        her "(Выглядит забавно...)"
        #__#hide screen hermione_main
        #__#with d3
        $herView.hideQQ()
        #__#$ h_xpos=120 #Defines position of the Hermione's full length sprite. center: 120. Right: 370.
        #__#$ h_body = "03_hp/13_hermione_main/body_44.png" #Flashing Трусики
        #__#show screen hermione_main
        #__#with d3
        $herView.showQQ( "body_44.png", pos )
        her "Это все, сэр?"
    if whoring >= 9: #LEVEL 04+ (THIRD EVENT)
        #__#hide screen hermione_main
        #__#with d3
        $herView.hideQQ()
        #__#$ h_xpos=120 #Defines position of the Hermione's full length sprite. center: 120. Right: 370.
        #__#$ pos = POS_120
        #__#$ h_body = "03_hp/13_hermione_main/body_71.png" #Flashing Трусики
        #__#show screen hermione_main
        #__#with d3
        $herView.showQQ( "body_71.png", pos )
        her "Мои трусики..."
        if request_03 >= 1:
            her "Они снова в чем-то скользком..."
        else:
            her "Они покрыты чем-то скользким..."
        her "И забавно пахнут..."
        #__#hide screen hermione_main
        #__#with d3
        $herView.hideQQ()
        #__#$ h_xpos=120 #Defines position of the Hermione's full length sprite. center: 120. Right: 370.
        #__#$ h_body = "03_hp/13_hermione_main/body_29.png" #Flashing Трусики
        #__#show screen hermione_main
        #__#with d3
        $herView.showQQ( "body_29.png", pos )
        her "Хм... Этот запах..."
        her "Какой-то знакомый..."
        #__#hide screen hermione_main
        #__#with d3
        $herView.hideQQ()
        #__#$ h_xpos=120 #Defines position of the Hermione's full length sprite. center: 120. Right: 370.
        #__#$ h_body = "03_hp/13_hermione_main/body_45.png" #Flashing Трусики
        #__#show screen hermione_main
        #__#with d3
        $herView.showQQ( "body_45.png", pos )
        her "Что вы с ними делали, сэр?"
        menu:
            "\"Эксперимент не увенчался успехом\"":
                her "Эксперимент, да?"
                her "Какого рода?"
                #__#hide screen hermione_main
                #__#with d3
                $herView.hideQQ()
                #__#$ h_xpos=120 #Defines position of the Hermione's full length sprite. center: 120. Right: 370.
                #__#$ h_body = "03_hp/13_hermione_main/body_46.png" #Flashing Трусики
                #__#show screen hermione_main
                #__#with d3
                $herView.showQQ( "body_46.png", pos )
                her "Нет, не отвечайте...Мне кажется я знаю..."
            "\"Вы мне дали их такими!\"":
                her "Я так не думаю, сэр."
                her "Но ладно, если вы не хотите говорить, сэр..."
                her "Я уверена, что знаю, что с ними произошло..."
            "\"Я кончил на них!\"":
                $ she_knows_about_cum = True
                #__#hide screen hermione_main
                #__#with d3
                $herView.hideQQ()
                #__#$ h_xpos=120 #Defines position of the Hermione's full length sprite. center: 120. Right: 370.
                #__#$ h_body = "03_hp/13_hermione_main/body_64.png" #Flashing Трусики
                #__#show screen hermione_main
                #__#with d3
                $herView.showQQ( "body_64.png", pos )
                her "Я знала это..."
                her "Они пахнут спермой!"
        #__#hide screen hermione_main
        #__#with d3
        $herView.hideQQ()
        #__#$ h_xpos=120 #Defines position of the Hermione's full length sprite. center: 120. Right: 370.
        #__#$ h_body = "03_hp/13_hermione_main/body_68.png" #Flashing Трусики
        #__#show screen hermione_main
        #__#with d3
        $herView.showQQ( "body_68.png", pos )
        her "Хм..."
        her "Похоже, стоит их постирать, прежде чем надевать..."
        #__#hide screen hermione_main
        #__#with d3
        $herView.hideQQ()
        #__#$ h_xpos=120 #Defines position of the Hermione's full length sprite. center: 120. Right: 370.
        #__#$ h_body = "03_hp/13_hermione_main/body_64.png" #Flashing Трусики
        #__#show screen hermione_main
        #__#with d3
        $herView.showQQ( "body_64.png", pos )
        her "Или вы хотите, чтобы я надела их сейчас, сэр...?"
        menu: 
            "\"Да! Надень их сейчас, девочка!\"":
                her "Ну, если так надо..."
            "\"Мне плевать. Делай что хочешь.\"":
                her "Почему бы не надеть их еще раз?"
        
        #__#hide screen hermione_main
        #__#with d3
        $herView.hideQQ()
        #__#$ h_xpos=120 #Defines position of the Hermione's full length sprite. center: 120. Right: 370.
        #__#$ h_body = "03_hp/13_hermione_main/body_74.png" #Flashing Трусики
        #__#show screen hermione_main
        #__#with d3
        $herView.showQQ( "body_74.png", pos )
        her "Я делаю это только для того, чтобы выиграть кубок в этом году..."
        m "Верно..."
        
        #__#hide screen hermionу_main
        #__#with d3
        $herView.hideQQ()
        
        show screen blktone8
        with d3
        ">Гермиона быстро проскальзывает в свои влажные трусики..."
        hide screen blktone8
        with d3
        
        # NEW Branch :)
        $pos = POS_120
        if she_knows_about_cum == True and whoring >= 12:
            $herView.showQQ( "body_58.png", pos )
            her "...Сэр?"
            m "Да?"
            $herView.hideQQ()
            
            $herView.showQQ( "body_58.png", pos )
            her "Одна подруга говорила мне, что парням нравятся всякие извращения."
            $herView.hideQQ()
            $herView.showQQ( "body_129.png", pos )
            her "Это правда, сэр?"
            m "Кхм, ну, если ты спрашиваешь..."
            m "О чем конкретно ты говоришь?"
            $herView.hideQQ()
            $herView.showQQ( "body_84.png", pos )
            her "Ну, например..."
            $herView.hideQQ()
            
            $herView.data().saveState()
            $herView.data().addPose( CharacterExItemSkirtLifted( herView.mPoseFolder, 'pose_skirt_up.png', G_Z_POSE ) )
            $herView.data().addItem( 'panties_cum', CharacterExItem( herView.mMiscFolder, 'panties_soaked.png', G_Z_PANTIES + 1, 'panties' ) )
            
            $herView.showQQ( "185.png", pos )
            her "...если девушка будет в трусиках, пропитанной спермой?"
            pause
            menu:
                "\"Безусловно, парни в восторге от этого!\"":
                    $herView.hideQQ()
                    $herView.showQQ( "body_128.png", pos )
                    her "Я так и думала, профессор."
                    $herView.hideQQ()
                    $herView.data().loadState()
                    $herView.showQQ( "body_52.png", pos )
                    her "Тогда я пойду?"
                    m "Хм, да да, мисс Грейнджер..."
                    $herView.hideQQ()
                    $herView.showQQ( "body_64.png", pos )
                    her "Вы ничего не забыли, сэр?"
                    m "Ох..."
                    $herView.hideQQ()
                    $herView.showQQ( "body_45.png", pos )

                "\"Я думаю, это грязно!\"":
                    $mad += 15
                    $herView.hideQQ()
                    $herView.data().loadState()
                    $herView.showQQ( "body_51.png", pos )
                    her "Хм!"
                    $herView.hideQQ()
                    $herView.showQQ( "body_191.png", pos )
                    her "Мои очки, сэр!"
                    
                    

    jump back_from_panties