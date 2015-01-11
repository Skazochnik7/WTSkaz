
###################REQUEST_05 (Level 02) (BUTT MOLESTER).
label new_request_05:
    #__#hide screen hermione_main 
    #__#with d3
    $herView.hideQQ()
    m "{size=-4}(Я просто хочу немного помять ее попку.){/size}"
    $ menu_x = 0.5 #Default position of the menu (0.5). Version B is $ menu_x = 0.2
    menu:
        "\"(Да, давай попробуем!)\"":
            pass
        "\"(Не сейчас.)\"":
            jump new_personal_request

    
    if whoring <=2:
        jump too_much
        
    if whoring >= 3 and whoring <= 5:
        $ level = "02"
        $ new_request_05_01 = True # HEARTS.
    elif whoring >= 6 and whoring <= 8:
        $ level = "03"
        $ new_request_05_02 = True # HEARTS.
    elif whoring >= 9:
        $ level = "04"
        $ new_request_05_03 = True # HEARTS.
        
        
    if whoring >= 3 and whoring <= 5: # LEVEL 02 # Hermione is hesitant. <=================================================================================== FIRST EVENT.
        
        hide bld1
        with d3
        m "Подойди ближе, дитя. Давайка разомнем твою сочную попку."
        if request_05_points == 0 and whoring <= 5: #First time
            stop music fadeout 5.0
            #__#her_07 "Профессор Дамблдор!?"
            $her_head_state = 7
            her_head_main "Профессор Дамблдор!?"
            m "Расслабься. Это будет самая простая услуга за эти 15 очков, я обещаю."
            #__#her_08 "Но...."
            $her_head_state = 8
            her_head_main "Но...."
            m "Все, что я хочу, это несколько раз сжать твою милую попку..."
            #__#her_04 "Это неуместно, профессор................"
            $her_head_state = 4
            her_head_main "Это неуместно, профессор................"
            m "Всем не обязательно знать, как ты получила эти очки..."
            #__#her_12 "(Эти 15 очков действительно вытолкнут нас вперед...)"
            $her_head_state = 12
            her_head_main "(Эти 15 очков действительно вытолкнут нас вперед...)"
            #__#her_19 "(Черт.....!)"
            $her_head_state = 19
            her_head_main "(Черт.....!)"
        else:
            #__#her_04 "Снова.....?"
            $her_head_state = 4
            her_head_main "Снова.....?"
        hide screen bld1
        with d3
        $ walk_xpos=400 #Animation of walking chibi. (From)
        $ walk_xpos2=280 #Coordinates of it's movement. (To)
        $ hermione_speed = 03.0 #The speed of moving the walking animation across the screen.
        show screen hermione_walk_01 
        pause 1
        show screen blkfade
        with Dissolve(1)
        pause.5
        #__#her_04 ".................."
        her_head_main ".................."
        #__#her_04 "Вы хотите, чтобы я развернулась, сэр?"
        her_head_main "Вы хотите, чтобы я развернулась, сэр?"
        play music "music/(Orchestral) Playful Tension by Shadow16nh.mp3" fadein 1 fadeout 1 # SEX THEME.
        menu:
            m "Хм..."
            "\"Да, развернитесь, пожалуйста, Мисс Грейнджер.\"":
                #__#her_04 "Как вы скажите, сэр..."
                her_head_main "Как вы скажите, сэр..."
                hide screen hermione_walk_01
                hide screen genie
                show screen ctc
                show screen no_groping_02
                with d1
                hide screen blkfade
                with d5
                pause
                #__#her_04 "............."
                her_head_main "............."
                #__#her_04 "..........................."
                her_head_main "..........................."
                #__#her_25 "Сэр, я бы хотела покончить с этим как можно раньше..."
                $her_head_state = 25
                her_head_main "Сэр, я бы хотела покончить с этим как можно раньше..."
                m "Не торопи меня, девочка... Дай мне насладиться моментом..."
                #__#her_04 "............................."
                $her_head_state = 4
                her_head_main "............................."
                menu:
                    m "Хм..."
                    "- Сжать ее булочки -":
                        pass
                    "- Шлепнуть по попке -":
                        $ renpy.play('sounds/slap_02.mp3') #SLAP!
                        show screen white
                        with hpunch
                        pause.08
                        hide screen white
                        show screen bld1
                        #__#her_22 "!!!!!!!!!!!!!"
                        $her_head_state = 22
                        her_head_main "!!!!!!!!!!!!!"
                        #__#her_22 "Профессор!!?"
                        her_head_main "Профессор!!?"
                        menu:
                            "\"Ладно, ладно... Я просто не смогу устоять....\"":
                                #__#her_25 "......................."
                                $her_head_state = 25
                                her_head_main "......................."
                                pass
                            "- Шлепнуть еще раз -":
                                $ renpy.play('sounds/slap_02.mp3') #SLAP!
                                show screen white
                                with hpunch
                                pause.08
                                hide screen white
                                show screen bld1
                                #__#her_21 "!!!!!!!!!!!!!"
                                $her_head_state = 21
                                her_head_main "!!!!!!!!!!!!!"
                                #__#her_15 "Профессор, что вы делаете!?"
                                $her_head_state = 15
                                her_head_main "Профессор, что вы делаете!?"
                                #__#her_15 "Вы сказали, что будете просто щупать!"
                                her_head_main "Вы сказали, что будете просто щупать!"
                                menu:
                                    "\"Ладно, ладно... Я просто не смог устоять....\"":
                                        #__#her_25 "......................."
                                        $her_head_state = 25
                                        her_head_main "......................."
                                        pass
                                    "- Шлепнуть еще раз -":
                                        $ renpy.play('sounds/slap_02.mp3') #SLAP!
                                        show screen white
                                        with hpunch
                                        pause.08
                                        hide screen white
                                        show screen bld1
                                        #__#her_15 "Ой! Это больно!"
                                        $her_head_state = 15
                                        her_head_main "Ой! Это больно!"
                                        #__#her_20 "Это так унизительно!"
                                        $her_head_state = 20
                                        her_head_main "И так унизительно!"
                                        #__#her_20 "Вы сказали, что будете просто щупать!..."
                                        her_head_main "Вы сказали, что будете просто щупать!..."
                                        $her_head_state = 20
                                        her_head_main "Почему вы это делаете, профессор?"
                                        #__#her_20 "Why are you doing this, профессор?"
                                        g4 "Просто стойте, Мисс Грейнджер!"
                                        #__#her_19 "Я так не думаю, сэр!"
                                        $her_head_state = 19
                                        her_head_main "Я так не думаю, сэр!"
                                        #__#her_24 "Никакие очки не стоят такого!"
                                        $her_head_state = 24
                                        her_head_main "Никакие очки не стоят такого!"
                                        #__#her_23 "Вы злоупотребляете свой властью, сэр!"
                                        $her_head_state = 23
                                        her_head_main "Вы злоупотребляете своей властью, сэр!"
                                        g4 "Что?"
                                        #__#her_19 "Я ухожу!"
                                        $her_head_state = 19
                                        her_head_main "Я ухожу!"
                                        menu:
                                            g4 "Арх..."
                                            "\"Мои... Я прошу прощения...\"":
                                                #__#her_25 "Просто больше не делаете этого, сэр..."
                                                $her_head_state = 25
                                                her_head_main "Просто больше не делаете этого, сэр..."
                                                pass
                                            "\"Ты не получишь очков за это!\"":
                                                $ mad += 30
                                                #__#her_20 "Ха! See if I care, сэр!"
                                                $her_head_state = 20
                                                her_head_main "Ха! See if I care, сэр!"
                                                ### Takes place aftre you refuse to pay her the очков.
                                                $ walk_xpos=300 #Animation of walking chibi. (From)
                                                $ walk_xpos2=610 #Coordinates of it's movement. (To)
                                                $ hermione_speed = 03.0 #The speed of moving the walking animation across the screen.
                                                hide screen no_groping_02
                                                hide screen bld1
                                                show screen genie
                                                show screen hermione_walk_01_f 
                                                with fade
                                                pause 2
                                                hide screen hermione_walk_01_f 
                                                $ renpy.play('sounds/door.mp3') #Sound of a door opening.
                                                with Dissolve(.3)
                                                pause.5
                                                g4 "Арх! (You little brat!)"
                                                $ request_05_points += 1
                                                if daytime:
                                                    $ hermione_takes_classes = True
                                                    jump day_main_menu
                                                else:
                                                    $ hermione_sleeping = True
                                                    jump night_main_menu
                                            "\"Я вычту очки за это!\"":
                                                $ mad += 20
                                                #__#her_22 "Вы серьезно!?"
                                                $her_head_state = 22
                                                her_head_main "Вы серьезно!?"
                                                $ gryffindor -=10
                                                g4 " \"Гриффиндор\", минус 10 очков!"
                                                g4 "Все! Именно так!"
                                                #__#her_24 "Грр..........."
                                                $her_head_state = 24
                                                her_head_main "Грр..........."
                                                #__#her_24 "........................"
                                                her_head_main "........................"
                                                #__#her_27 "Это не справедливо..."
                                                $her_head_state = 27
                                                her_head_main "Это не справедливо..."
                                                m "Что? Эй, подожди, не начинай плакаться мне..."
                                                #__#her_29 "Я ненавижу вас, проф! Я ненавижу вас!"
                                                $her_head_state = 29
                                                her_head_main "Я ненавижу вас, проф! Я ненавижу вас!"
                                                
                                                $ walk_xpos=300 #Animation of walking chibi. (From)
                                                $ walk_xpos2=610 #Coordinates of it's movement. (To)
                                                $ hermione_speed = 02.0 #The speed of moving the walking animation across the screen.
                                                hide screen no_groping_02
                                                hide screen bld1
                                                show screen genie
                                                show screen hermione_run
                                                with fade
                                                pause.9
                                                hide screen hermione_run
                                                with Dissolve(.3)
                                                $ renpy.play('sounds/door.mp3') #Sound of a door opening.
                                                m ".............."
                                                menu:
                                                    "\"Черт. Чувствую себя хреново...\"":
                                                        $ mad -= 5
                                                        m "Черт... Чувствую себя хреново..."
                                                        #m "But who could resist slapping that little behind of her's?"
                                                        m "Но кто бы смог устоять и не шлепнуть ее великолепную попку?"
                                                    #"\"She made me do this, that brat!\"":
                                                    "\"Этот ребенок, все из-за нее!\"":
                                                        $ mad += 9
                                                        #m "She made me do this, that brat!"
                                                        #m "Acting all wounded now..."
                                                        #m "I bet she actually enjoyed the slapping and just won't admit it..."
                                                        m "Она подтолкнула меня к этому!"
                                                        m "А теперь строит из себя оскробленную..."
                                                        m "Я уверен что ей понравились эти шлепка, она просто не хочет признать этого..."
                                                $ request_05_points += 1
                                                if daytime:
                                                    $ hermione_takes_classes = True
                                                    jump day_main_menu
                                                else:
                                                    $ hermione_sleeping = True
                                                    jump night_main_menu     
        
                pause
                show screen groping_02
                with d7
                #__#her_07 "!!!!!!?"
                $her_head_state = 7
                her_head_main "!!!!!!?"
                m "Что такое, Мисс Грейнджер?"
                #__#her_15 "ничего профессор ..."
                $her_head_state = 15
                her_head_main "Ничего, профессор..."
                #__#her_15 "Просто... "
                her_head_main "Просто... "
                #__#her_15 "Я просто не могу поверить что это случилось..."
                her_head_main "Я просто не могу поверить что это случилось..."
                #__#her_15 "Это... неправльно..."
                her_head_main "Это... неправильно..."
                #m "Расслабься, девочка. It's not like you are enjoying this..."
                m "Расслабься, девочка. Ты же не получаешь от этого удовольствие..."
                #__#her_19 "Что? Конечно нет! Это непристойно..."
                $her_head_state = 19
                her_head_main "Что? Конечно нет! Это непристойно..."
                #__#her_19 "Я сделаю эту жертву для чести моего факультета..."
                her_head_main "Я иду эту жертву ради чести моего факультета..."
                m "Да, сосредоточся на этом..."
                #__#her_20 "...................."
                $her_head_state = 20
                her_head_main "...................."
                show screen bld1
                with d3
                pause
                #__#her_17 "Но, профессор..."
                $her_head_state = 17
                her_head_main "Но, профессор..."
                #__#her_05 "Почему  {size=+7}вы{/size} делаете это?"
                $her_head_state = 5
                her_head_main "Почему {size=+7}вы{/size} делаете это?"
                menu: 
                    m "Хм..."
                    "\"У меня есть свои причины...\"":
                        #__#her_12 "Oх..."
                        $her_head_state = 12
                        her_head_main "Oх..."
                        #__#her_25 "Хм..."
                        $her_head_state = 25
                        her_head_main "Хм..."
                    "\"Это для науки, конечно!\"":
                        #__#her_03 "Правда?!"
                        $her_head_state = 3
                        her_head_main "Правда?!"
                        #__#her_03 "Это одно из исследований?"
                        her_head_main "Это одно из исследований?"
                        m "Да, точно, я исследую... эм... э..."
                        m "Ну, тебе не понять, это некоторые довольно продвинутые магические штуки..."
                        #__#her_03 "Понятно..."
                        her_head_main "Понятно..."
                        #__#her_02 "Ну, если это для науки, то я рада помочь..."
                        $her_head_state = 2
                        her_head_main "Ну, если это для науки, то я рада помочь..."
                    "- Сжать её ягодицы жестче -":
                        ">Вы мнете ягодицы Гермионы с удвоеной силой."
                        #__#her_05 "...................."
                        $her_head_state = 5
                        her_head_main "...................."
                        #__#her_12 "(Должна ли я промолчать.....?)"
                        $her_head_state = 12
                        her_head_main "(Должна ли я промолчать.....?)"
                show screen blktone8
                with d3
                ">Вы продолжаете играть с ягодицами Гермионы..."
                ">Вы проводите руками вниз..."
                #__#her_15 "................"
                $her_head_state = 15
                her_head_main "................"
                label connection_of_rapes:
                menu:
                    "- Залесть к ней в трусики -":
                        ">Вы медленно запускаете свою руку в  ее трусики..."
                        #__#her_07 "Профессор... Что вы...?"
                        $her_head_state = 7
                        her_head_main "Профессор... Что вы...?"
                        m "Это нормально, просто подумай о тех 15 баллах, которые ты можешь получить..."
                        #__#her_12 "............."
                        $her_head_state = 12
                        her_head_main "............."
                        menu:
                            "- Поласкать её киску пальцем -":
                                show screen blkfade
                                with d3
                                ">Вы проникаете пальцем вниз и засовываете его в ее маленькую щель..."
                                #__#her_07 "Про? Нет! Что вы...?"
                                $her_head_state = 7
                                her_head_main "Про...? Нет! Что вы...?"
                                ">Гермиона пытается вырваться..."
                                menu:
                                    "- Засунуть палец силой! -":
                                        ">Вы силой вставляете палец ей в киску..."
                                        ">Там очень тепло и узко..."
                                        ">Но там очень сухо... Не похоже, что бы Гермиона получила от этого удоволствие..."
                                        jump screams_of_rapings
                                    "- Остановиться... -":
                                        pass
                            "- Поласкать пальцем ее попку -":
                                show screen blkfade
                                with d3
                                ">Вы вставялете свой палец в её узенькую дырочку..."
                                #__#her_07 "Профессор? Нет! Что вы делаете!?"
                                her_head_main "Профессор? Нет! Что вы делаете!?"
                                ">Гермиона пытается вырваться..."
                                menu:
                                    "- Силой засунуть палец -":
                                        ">Вы силой вставляете палец в её дырочку..."
                                        with hpunch
                                        #__#her_30 "!!?"
                                        $her_head_state = 30
                                        her_head_main "!!?"
                                        ">Там очень узко и тепло..."
                                        jump screams_of_rapings
                                    "- Умерить пыл... -":
                                        pass
                            "- Перестать испытывать удачу. -":
                                pass
                    "- Нет, на сегодня хватит. Отпустить её -":
                        pass
            "\"Нет. Просто стойте, Мисс Грейнджер.\"":
                #__#her_04 "Как вы скажите, сэр..."
                $her_head_state = 4
                her_head_main "Как вы скажите, сэр..."
                hide screen hermione_walk_01
                hide screen genie
                show screen ctc
                show screen no_groping_01
                with d1
                hide screen blkfade
                with d5
                pause
                #__#her_01 "Сэр,пожалуйста поторопитесь, прежде чем кто-нибудь узнает..."
                $her_head_state = 1
                her_head_main "Сэр,пожалуйста поторопитесь, прежде чем кто-нибудь узнает..."
                m "В чем проблема, Мисс Грейнджер?"
                m "Вы ведь знаете, что делаете это для факультета."
                #__#her_04 "Я знаю."
                $her_head_state = 4
                her_head_main "Я то знаю."
                #__#her_04 "Но никто не знает каким образом..."
                her_head_main "Но никто другой этого не знает...."
                #__#her_04 "Так, что давайте сделаем это как можно быстрее..."
                her_head_main "Так что давайте сделаем это как можно быстрее..."
                #__#her_05 "Пожалуйста..."
                $her_head_state = 5
                her_head_main "Пожалуйста..."
                m "Ну, если ты не против..."
                show screen groping_01
                with d7
                #__#her_07 "!!!"
                $her_head_state = 7
                her_head_main "!!!"
                m "Что случилось?"
                #__#her_05 "Ничего, сэр. У вас руки холодные вот и все..."
                $her_head_state = 5
                her_head_main "Ничего, сэр. У вас руки холодные вот и все..."
                show screen bld1 
                with d3
                show screen blktone8
                with d3
                ">Вы растираете руки об ноги Гермионы..."
                #__#her_04 "........................."
                $her_head_state = 4
                her_head_main "........................."
                ">Вы хорошенько сжимаете её ягодицы..."
                #__#her_19 "................."
                $her_head_state = 19
                her_head_main "................."
                m "Не смотри по сторонам, девочка. Я хочу чтобы ты смотрела мне в глаза."
                #__#her_19 "Я бы предпочла не смотреть, сэр..."
                her_head_main "Я бы предпочла не смотреть, сэр..."
                menu:
                    m "..."
                    "\"Ладно. Тогда просто продолжай стоять.\"":
                        #__#her_15 "Спасибо сэр..."
                        $her_head_state = 15
                        her_head_main "Спасибо, сэр..."
                        ">Вы делаете легкий массаж её ягодицам..."
                        #__#her_15 "...................."
                        her_head_main "...................."
                        ">И вы наслаждаетесь их формами..."
                        #__#her_19 "....................."
                        $her_head_state = 19
                        her_head_main "....................."
                        ">Затем вы в последний раз сжиматете её попку."
                        #__#her_19 "....................."
                        her_head_main "....................."
                    "\"Открой глаза, или лишишься очков!\"":
                        $ mad += 7
                        #__#her_19 "Арх! {size=-5}(Ах ты старый--{/size}"
                        her_head_main "Арх! {size=-5}(Ах ты старый--{/size}"
                        m "Вы что-то сказали, Мисс Грейнджер?"
                        #__#her_08 "Ничего, сэр."
                        $her_head_state = 8
                        her_head_main "Ничего, сэр."
                        ">Вы делаете легкий массаж её ягодицам..."
                        ">Гермиона смотрит вам в глаза, как она и сказала..."
                        #__#her_08 "...................."
                        her_head_main "...................."
                        #__#her_04 "..............................."
                        $her_head_state = 4
                        her_head_main "..............................."
                        m "Что я тебе говорил об отводе глаз?"
                        #__#her_19 "Да, я помню..."
                        $her_head_state = 19
                        her_head_main "Да, я помню..."
                        #__#her_08 "................................."
                        $her_head_state = 8
                        her_head_main "................................."
                        #__#her_25 "..................................."
                        $her_head_state = 25
                        her_head_main "..................................."
                        #__#her_25 ".................................................."
                        her_head_main ".................................................."
                        ">Вы продолжаете наслаждаться её упругой попкой..."
                        #__#her_08 "....................."
                        $her_head_state = 8
                        her_head_main "....................."
                        jump connection_of_rapes
    
        
    elif whoring >= 6: # LEVEL 04 # Hermione is hesitant. <=================================================================================== SECOND EVENT.
        $ new_request_05_02 = True # HEARTS.
        hide screen bld1
        with d3
        m "Подойди ближе, девочка. Позволь потрогать твою попку."
        #__#her_17 "Как скажете..."
        $her_head_state = 17
        her_head_main "Как скажете..."
        hide screen bld1
        with d3
        $ walk_xpos=400 #Animation of walking chibi. (From)
        $ walk_xpos2=280 #Coordinates of it's movement. (To)
        $ hermione_speed = 03.0 #The speed of moving the walking animation across the screen.
        show screen hermione_walk_01 
        pause 1
        show screen blkfade
        with Dissolve(1)
        pause.5
        #__#her_18 "Вы хотите чтобы я повернулась, сэр?"
        $her_head_state = 18
        her_head_main "Вы хотите чтобы я повернулась, сэр?"
        play music "music/(Orchestral) Playful Tension by Shadow16nh.mp3" fadein 1 fadeout 1 # SEX THEME.
        menu:
            m "Хм..."
            "\"Да. Повернитесь, Мисс Грейнджер.\"":
                #__#her_18 "Как вы скажите, сэр..."
                her_head_main "Как скажете, сэр..."
                hide screen hermione_walk_01
                hide screen genie
                show screen ctc
                show screen no_groping_02
                with d1
                hide screen blkfade
                with d5
                pause
                #__#her_35 "............."
                $her_head_state = 35
                her_head_main "............."
                menu:
                    m "Хм..."
                    "- Сжать ее булочки -":
                        pass
                    "- Шлепнуть по попке -":
                        $ renpy.play('sounds/slap_02.mp3') #SLAP!
                        show screen white
                        with hpunch
                        pause.08
                        hide screen white
                        show screen bld1
                        #__#her_22 "!!!!!!!!!!!!!"
                        $her_head_state = 22
                        her_head_main "!!!!!!!!!!!!!"
                        #__#her_18 "Профессор....?"
                        $her_head_state = 18
                        her_head_main "Профессор....?"
                        menu:
                            "\"Ладно, ладно... Я просто не смог удержаться....\"":
                                #__#her_18 "Хорошо..."
                                her_head_main "Хорошо..."
                                pass
                            "- Шлепнуть еще раз -":
                                $ renpy.play('sounds/slap_02.mp3') #SLAP!
                                show screen white
                                with hpunch
                                pause.08
                                hide screen white
                                show screen bld1
                                #__#her_21 "!!!!!!!!!!!!!"
                                $her_head_state = 21
                                her_head_main "!!!!!!!!!!!!!"
                                #__#her_18 "Профессор, что вы делаете!?"
                                $her_head_state = 18
                                her_head_main "Профессор, что вы делаете!?"
                                #__#her_18 "Вы сказали,что только потрогаете!"
                                her_head_main "Вы сказали, что только потрогаете!"
                                menu:
                                    "\"Ладно,ладно... Я просто не смог удержаться....\"":
                                        #__#her_18 "Это ведь не так трудно..."
                                        her_head_main "Это ведь не так трудно..."
                                        pass
                                    "- Шлепнуть еще раз -":
                                        $ renpy.play('sounds/slap_02.mp3') #SLAP!
                                        show screen white
                                        with hpunch
                                        pause.08
                                        hide screen white
                                        show screen bld1
                                        #__#her_34 "Пр, не так громко, пожалуйста..."
                                        $her_head_state = 34
                                        her_head_main "Проф, не так громко, пожалуйста..."
                                        #__#her_34 "Нас ведь могут услышать?"
                                        her_head_main "Нас ведь могут услышать?"
                                        m "Хорошо, хорошо... продолжу щупать..."
                                        #__#her_18 "................"
                                        $her_head_state = 18
                                        her_head_main "................"

                pause
                show screen groping_02
                with d7
                #__#her_18 "..................."
                her_head_main "..................."
                m "Вы сегодня тихая, Мисс Грейнджер."
                #__#her_18 "Я...?"
                her_head_main "Я...?"
                #__#her_35 "Ну, вы знаете меня, сэр..."
                $her_head_state = 35
                her_head_main "Ну, вы знаете меня, сэр..."
                #__#her_35 "Я просто рада быть частью факультета \"Гриффиндора\"...."
                her_head_main "Я просто рада быть частью факультета \"Гриффиндора\"...."
                #__#her_35 "Не обращайте внимание и продолжайте..."
                her_head_main "Не обращайте внимание и продолжайте..."
                #__#her_18 "(...Щупать меня...)"
                $her_head_state = 18
                her_head_main "(...Щупать меня...)"
                show screen blktone8
                with d3
                ">Вы продолжаете играть с попкой Гермионы..."
                #">And continue sliding your hands up and down her inner tighs..."
                ">Ваша рука продолжает скользить по внутренней части ее бедра..."
                #__#her_18 "................"
                her_head_main "................"
                label connection_of_rapes_02:
                menu:
                    "- Залезть к ней в трусики -":
                        ">Вы медленно запускаете свою руку в девичьи трусики... "
                        #__#her_17"Профессор... Что вы...?"
                        $her_head_state = 17
                        her_head_main "Профессор... Что вы...?"
                        m "Это нормально, просто подумай о тех 15 баллах, которые ты сможешь получить..."
                        #__#her_17 "Как вы скажите..."
                        her_head_main "Как скажете..."
                        menu:
                            "- Поласкать её киску пальцем -":
                                show screen blkfade
                                with d3
                                ">Вы проникаете пальцами вниз и вставляете один в ее маленькую щель..."
                                #__#her_18 "Профессор?" 
                                $her_head_state = 18
                                her_head_main "Профессор?"
                                menu:
                                    "- Засунуть палец в её киску силой! -":
                                        ">-Вы силой вставляете свой палец в её маленькую щель-..."
                                        ">Там очень тепло и узко...."
                                        ">Там немного влажно, похоже она получает немного удовольствия от этого..."
                                        jump screams_of_pleasure
                                    "- Прекратить... -":
                                        pass
                            "- Поласкать ее попку своим пальцем -":
                                show screen blkfade
                                with d3
                                ">Вы вставляете свой палец в её узенькую дырочку..."
                                #__#her_18 "Профессор? Что вы пытаетесь сделать?"
                                her_head_main "Профессор? Что вы пытаетесь сделать?"
                                menu:
                                    "- Силой вставить палец в её узкую попку -":
                                        ">Вы вставялете свой палец в её узенькую дырочку..."
                                        with hpunch
                                        #__#her_36 "aх... ваш палец в моей ..."
                                        $her_head_state = 36
                                        her_head_main "Ах... ваш палец в моей ..."
                                        ">Там тепло и узко..."
                                        jump screams_of_pleasure
                                    "- Прекратить... -":
                                        pass
                            "- Перестать испытывать удачу и отпустить девочку -":
                                pass
                    "- Нет, на сегодня хватит. Отпустить девочку -":
                        pass
            "\"Нет. Просто стойте, Мисс Грейнджер.\"":
                #__#her_04 "Как вы скажите, сэр..."
                $her_head_state = 4
                her_head_main "Как скажете, сэр..."
                hide screen hermione_walk_01
                hide screen genie
                show screen ctc
                show screen no_groping_01
                with d1
                hide screen blkfade
                with d5
                pause
                #__#her_01 "сэр,поторопитесь,пока никто не узнал про это..."
                $her_head_state = 1
                her_head_main "Сэр, поторопитесь, пока никто не узнал про это..."
                m "В чем проблема, Мисс Грейнджер?"
                m "Вы ведь знаете, что делаете это для своего факультета."
                #__#her_04 "Знаю."
                $her_head_state = 4
                her_head_main "Знаю."
                #__#her_04 "Но никто не видет каким образом..."
                her_head_main "Но никто другой не знает этого..."
                #__#her_04 "Так ,что давайте покончим с этим как можно быстрее..."
                her_head_main "Так что давайте покончим с этим как можно быстрее..."
                #__#her_05 "Пожалуйста..."
                $her_head_state = 5
                her_head_main "Пожалуйста..."
                m "Ну, если ты настаиваешь..."
                show screen groping_01
                with d7
                #__#her_07 "!!!"
                $her_head_state = 7
                her_head_main "!!!"
                m "Что случилось?"
                #__#her_05 "Ничего, сэр. Ничего, сэр. У вас руки холодные вот и все..."
                $her_head_state = 5
                her_head_main "Ничего, сэр. У вас руки холодные, вот и все..."
                show screen bld1 
                with d3
                show screen blktone8
                with d3
                ">Вы растираете руки об ноги Гермионы..."
                #__#her_04 "........................."
                $her_head_state = 4
                her_head_main "........................."
                ">И хорошенько жмакаете ягодицы..."
                #__#her_19 "................."
                $her_head_state = 19
                her_head_main "................."
                m "Не смотри по сторонам, девочка. Я хочу чтобы ты смотрела мне в глаза."
                #__#her_19 "Я бы предпочла не смотреть,, сэр..."
                her_head_main "Я бы предпочла не смотреть, сэр..."
                menu:
                    m "..."
                    "\"Ладно. Тогда просто продолжай стоять...\"":
                        #__#her_15 "Спасибо сэр..."
                        $her_head_state = 15
                        her_head_main "Спасибо сэр..."
                        ">Вы делаете легкий массаж её ягодицам..."
                        #__#her_15 "...................."
                        her_head_main "...................."
                        ">Вы продолжаете наслаждаться её упругой попкой..."
                        #__#her_19 "....................."
                        $her_head_state = 19
                        her_head_main "....................."
                        ">Затем вы в последний раз сжимаете их."
                        #__#her_19 "....................."
                        her_head_main "....................."
                    "\"Открой свои глаза или не получишь очков!\"":
                        $ mad += 20
                        #__#her_19 "Арх! {size=-5}(Старый козел--{/size}"
                        her_head_main "Арх! {size=-5}(Старый козел--{/size}"
                        m "Вы что-то сказали, Мисс Грейнджер?"
                        #__#her_08 "Ничего, сэр."
                        $her_head_state = 8
                        her_head_main "Ничего, сэр."
                        ">Вы делаете легкий массаж её ягодицам...."
                        ">Гермиона смотрит вам в глаза, как она и сказала..."
                        #__#her_08 "...................."
                        her_head_main "...................."
                        #__#her_04 "..............................."
                        $her_head_state = 4
                        her_head_main "..............................."
                        m "Что я тебе говорил об отводе глаз?"
                        #__#her_19 "Да, я помню...."
                        $her_head_state = 19
                        her_head_main "Да, я помню...."
                        #__#her_08 "................................."
                        $her_head_state = 8
                        her_head_main "................................."
                        #__#her_25 "..................................."
                        $her_head_state = 25
                        her_head_main "..................................."
                        #__#her_25 ".................................................."
                        her_head_main ".................................................."
                        ">Вы продолжаете наслаждаться её упругой попкой..."
                        #__#her_08 "....................."
                        $her_head_state = 8
                        her_head_main "....................."
                        jump connection_of_rapes_02  
        
  
  
  
  
    
        
label ending_of_screams_of_pleasure:
    if whoring <= 5:
        $ whoring +=1
    show screen blkfade 
    with d5
    
    stop music fadeout 1.0
    ">Вы отпускаете ее попку..."
    m "На этом закончим."
    
    hide screen blktone8
    hide screen ctc
    hide screen bld1
    hide screen groping_01
    hide screen groping_02
    show screen hermione_02
    show screen genie
    with d1
    
    hide screen blkfade
    with d3

    $ gryffindor +=15
    m " \"Гриффиндор\" получает 15 очков!"
    
    $ request_05_points += 1
   
   
    $ hermione_chibi_xpos = 400 #Near the desk.
    show screen hermione_02 #Hermione stands still.
    show screen bld1
    hide screen blkfade
    with Dissolve(1)
    
    #__#$ h_xpos=370 #Defines position of the Hermione's full length sprite.
    #__#$ h_ypos=0
    $ pos = POS_370
    #__#$ h_body = "03_hp/13_hermione_main/body_29.png" #Sprite of Hermione's upper body.
    #__#show screen hermione_main
    #__#with d3
    $herView.showQQ( "body_29.png", pos )
    her ".................."
    her "Спасибо сэр..."
    if daytime:
        her "Теперь, мне лучше идти. Занятия вот-вот начнутся."
    else:
        her "Я лучше пойду. Уже очень поздно..."
    

    hide screen bld1
    #__#hide screen hermione_main
    $herView.hideQ( Dissolve(.3) )
    $ walk_xpos=400 #Animation of walking chibi. (From)
    $ walk_xpos2=610 #Coordinates of it's movement. (To)
    $ hermione_speed = 02.0 #The speed of moving the walking animation across the screen.
    show screen hermione_walk_01_f 
    pause 2
    hide screen hermione_walk_01_f 
    $ hermione_chibi_xpos = 610 #Near the desk.
    show screen hermione_01_f #Hermione stands still.
    with Dissolve(.3)
    
    if whoring >= 3 and whoring <= 5: #First level. Not happy.
        #__#her_12 "..........................."
        $her_head_state = 12
        her_head_main "..........................."
        
        
    hide screen hermione_01_f #Hermione stands still.
    with Dissolve(.3)
    $ renpy.play('sounds/door.mp3') #Sound of a door opening.
    with Dissolve(.3)
    pause.5

    call music_block # Lunches apropriete BGM day/night.

    if daytime:
        $ hermione_takes_classes = True
        jump day_main_menu
    else:
        $ hermione_sleeping = True
        jump night_main_menu



### ALL THE SCREAMS ABOUT RAPE ###
label screams_of_rapings:
    #__#her_10 "НЕТ! Что вы наделали!!?"
    $her_head_state = 10
    her_head_main "НЕТ! Что вы наделали!!?"
    ">Гермиона сильно толкает вас..."
    with hpunch
    #__#her_10 "Почему вы это делаете со мной, сэр...?"
    her_head_main "Почему вы это делаете со мной, сэр...?"
    #__#her_27 "Я не согласна делать это... для..."
    $her_head_state = 27
    her_head_main "Я не согласна делать это... для..."
    #__#her_27 "Для... вас..."
    her_head_main "Для... вас..."
    with hpunch
    #__#her_29 "{size=+7}ВЫ ИЗНАСИЛОВАЛИ МЕНЯ!{/size}"
    $her_head_state = 29
    her_head_main "{size=+7}ВЫ ИЗНАСИЛОВАЛИ МЕНЯ!{/size}"
    g4 "Что? Не смеши, девочка! Я не далал этого!"
    #__#her_29 "Да, изнасиловали! Изнасиловали!"
    her_head_main "Да, изнасиловали! Изнасиловали!"
    g4 "Я уверен, что это не так!"
    #__#her_29 "Нет,вы сделали это профессор!"
    her_head_main "Нет, вы сделали это профессор!"
    #__#her_31 "Теперь дайте мне 20 очков--"
    $her_head_state = 31
    her_head_main "Теперь дайте мне 20 очков--"
    #__#her_31 "Нет, 100 очков или я пожалуйюсь на вас в гильдию магии!!"
    her_head_main "Нет, 100 очков или я пожалуйюсь на вас в гильдию магии!!"
    menu:
        m "(Ах, черт...)"
        "\"Ладно, ладно... 100 очков...\"":
            $ gryffindor +=100
            m "100 очков \"Гриффиндору\" !"
            m "Все, сделано..."
            m "Теперь вы успокоились, Мисс Грейнджер?"
            #__#her_29 "Нет,еще нет!"
            $her_head_state = 29
            her_head_main "Нет, еще нет!"
            #__#her_29 "Я была изнасилована!"
            her_head_main "Я была изнасилована!"
            g4 "Ох, успокойся  девочка, я не насиловал тебя! Все что я сделал это--"
            with hpunch
            #__#her_29 "{size=+7}Вы изнасиловали меня!!!{/size}"
            her_head_main "{size=+7}Вы изнасиловали меня!!!{/size}"
            g4 "Великие пески пустыни, потише говори об изнасиловании!?"
            g4  "Кто-нибудь может услышать тебя!"
            #__#her_29 "Отлично! Я хочу чтобы они услышали!"
            her_head_main "Отлично! Я хочу чтобы они услышали!"
            m "Почему ты досих пор недовольна? Я уже заплатил тебе!"
            #__#her_32 "Oх... ладно..."
            $her_head_state = 32
            her_head_main "Oх... ладно..."
            #__#her_33 "Но я тебя ненавижу!Я ненавижу вас профессор!"
            $her_head_state = 33
            her_head_main "Но я вас ненавижу! Я ненавижу вас, профессор!"
            $ mad +=30

        "\"Ты блефуешь, девочка!\"":
            #__#her_29 "Нет!Я сделаю это"
            $her_head_state = 29
            her_head_main "Нет! Я сделаю это"
            g4 "Делай что хочешь"
            g4 "Никакого изнасилования не было!"
            #__#her_29 "Я ненавижу вас,профессор!"
            her_head_main "Я ненавижу вас,профессор!"
            $ mad +=50


    hide screen bld1
    hide screen ctc
    #__#hide screen hermione_main
    $herView.hideQ()
    show screen genie
    hide screen groping_01
    hide screen groping_02
    hide screen blkfade
    hide screen blktone8
    with Dissolve(.3)
    $ walk_xpos=400 #Animation of walking chibi. (From)
    $ walk_xpos2=610 #Coordinates of it's movement. (To)
    $ hermione_speed = 02.0 #The speed of moving the walking animation across the screen.
    show screen hermione_walk_01_f 
    pause 2
    hide screen hermione_walk_01_f 
    $ hermione_chibi_xpos = 610 #Near the desk.
    show screen hermione_01_f #Hermione stands still.
    with Dissolve(.3)

    if whoring >= 3 and whoring <= 5: #First level. Not happy.
        #__#her_12 "..........................."
        $her_head_state = 12
        her_head_main "..........................."
        
        
    hide screen hermione_01_f #Hermione stands still.
    with Dissolve(.3)
    $ renpy.play('sounds/door.mp3') #Sound of a door opening.
    with Dissolve(.3)
    pause.5

    if daytime:
        $ hermione_takes_classes = True
        jump day_main_menu
    else:
        $ hermione_sleeping = True
        jump night_main_menu        
    


########### SCREAM OF PLEASURES ###        
label screams_of_pleasure:
    #__#her_34 "Aх...."
    $her_head_state = 34
    her_head_main "Aх...."
    #__#her_34 "Он внутри меня..."
    her_head_main "Он внутри меня..."
    #__#her_18 "Нет, профессор, вы должны остановиться..."
    $her_head_state = 18
    her_head_main "Нет, профессор, вы должны остановиться..."
    m "Почему? Тебе не нравиться?"
    #__#her_18 "Не имеет значение нравиться мне или нет, сэр."
    her_head_main "Не имеет значения, нравиться мне это или нет, сэр."
    #__#her_18 "Вы знаете почему я делаю это..."
    her_head_main "Вы знаете почему я делаю это..."
    #__#her_18 "И это неправильно,что вы даете всего 15 очков..."
    her_head_main "И это неправильно, что вы даете всего 15 очков..."
    ">Гермиона отталкивает вас..."
    m "Хех... Я вижу..."
    m "Ну, в таком случае..."
    jump ending_of_screams_of_pleasure

    