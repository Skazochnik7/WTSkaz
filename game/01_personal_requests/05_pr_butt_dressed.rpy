
###################REQUEST_05 (Level 02) (BUTT MOLESTER).
label new_request_05:
    $herView.hideQQ()
    m "{size=-4}(Я просто хочу немного помять ее попку.){/size}"
    $ menu_x = 0.5 #Default position of the menu (0.5). Version B is $ menu_x = 0.2
    menu:
        "\"(Да, давай попробуем!)\"":
            pass
        "\"(Не сейчас)\"":
            $event.NotFinished()
            jump new_personal_request

    
    if hermi.whoring <=2:
        jump too_much
        
#    if whoring >= 3 and whoring <= 5:
#        $ level = "02"
#        $ new_request_05_01 = True # HEARTS.
#    elif whoring >= 6 and whoring <= 8:
#        $ level = "03"
#        $ new_request_05_02 = True # HEARTS.
#    elif whoring >= 9:
#        $ level = "04"
#        $ new_request_05_03 = True # HEARTS.

    $SetHearts(GetStage(hermi.whoring, 3, 3, 3))

        
        
    if hermi.whoring >= 3 and hermi.whoring <= 5: # LEVEL 02 # Hermione is hesitant. <=================================================================================== FIRST EVENT.
        
        hide bld1
        with d3
        m "Подойди поближе, детка. Давай-ка разомнем твою сочную попку."
        if IsFirstRun() and hermi.whoring <= 5: #First time
#        if request_05_points == 0 and whoring <= 5: #First time
            stop music fadeout 5.0
            $her_head_state = 7
            her_head_main "Профессор Дамблдор!?"
            m "Расслабься. Это будет самая простая услуга за эти 15 очков, я обещаю."
            $her_head_state = 8
            her_head_main "Но...."
            m "Все, что я хочу, это несколько раз сжать твою милую попку..."
            $her_head_state = 4
            her_head_main "Это неуместно, профессор................"
            m "Никто не узнает, как ты получила эти очки..."
            $her_head_state = 12
            her_head_main "(Эти 15 очков действительно нас продвинут...)"
            $her_head_state = 19
            her_head_main "(Черт.....!)"
        else:
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
        her_head_main ".................."
        her_head_main "Мне повернуться, сэр?"
        play music "music/(Orchestral) Playful Tension by Shadow16nh.mp3" fadein 1 fadeout 1 # SEX THEME.
        menu:
            m "Хм..."
            "\"Да, повернитесь, пожалуйста, Мисс Грейнджер.\"":
                her_head_main "Как скажете, сэр..."
                hide screen hermione_walk_01
                hide screen genie
                show screen ctc
                show screen no_groping_02
                with d1
                hide screen blkfade
                with d5
                pause
                her_head_main "............."
                her_head_main "..........................."
                $her_head_state = 25
                her_head_main "Сэр, я бы хотела поскорее покончить с этим..."
                m "Не торопи меня, девочка... Дай насладиться моментом..."
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
                        $her_head_state = 22
                        her_head_main "!!!!!!!!!!!!!"
                        her_head_main "Профессор!!?"
                        menu:
                            "\"Ладно, ладно... Я просто не смог устоять....\"":
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
                                $her_head_state = 21
                                her_head_main "!!!!!!!!!!!!!"
                                $her_head_state = 15
                                her_head_main "Профессор, что вы делаете!?"
                                her_head_main "Вы сказали, что будете просто щупать!"
                                menu:
                                    "\"Ладно, ладно... Я просто не смог устоять....\"":
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
                                        $her_head_state = 15
                                        her_head_main "Ой! Это больно!"
                                        $her_head_state = 20
                                        her_head_main "И так унизительно!"
                                        her_head_main "Вы сказали, что будете просто щупать!..."
                                        $her_head_state = 20
                                        her_head_main "Зачем вы это делаете, профессор?"
                                        g4 "Просто стойте, Мисс Грейнджер!"
                                        $her_head_state = 19
                                        her_head_main "Я так не думаю, сэр!"
                                        $her_head_state = 24
                                        her_head_main "Никакие очки не стоят такого!"
                                        $her_head_state = 23
                                        her_head_main "Вы злоупотребляете своей властью, сэр!"
                                        g4 "Что?"
                                        $her_head_state = 19
                                        her_head_main "Я ухожу!"
                                        menu:
                                            g4 "Арх..."
                                            "\"Мои... Я прошу прощения...\"":
                                                $her_head_state = 25
                                                her_head_main "Просто больше не делайте этого, сэр..."
                                                pass
                                            "\"Ты не получишь очков за это!\"":
                                                $ hermi.liking -= 30
                                                $her_head_state = 20
                                                her_head_main "Ха! И плевать, сэр!"
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
                                                g4 "Арх! (Ты, маленькая дрянь!...)"
#                                                $ request_05_points += 1
                                                if daytime:
                                                    $ hermione_takes_classes = True
                                                    jump day_main_menu
                                                else:
                                                    $ hermione_sleeping = True
                                                    jump night_main_menu
                                            "\"Я вычту очки за это!\"":
                                                $ hermi.liking -= 20
                                                $her_head_state = 22
                                                her_head_main "Вы серьезно!?"
                                                $ gryffindor -=10
                                                g4 " \"Гриффиндор\", минус 10 очков!"
                                                g4 "Да! Именно так!"
                                                $her_head_state = 24
                                                her_head_main "Грр..........."
                                                her_head_main "........................"
                                                $her_head_state = 27
                                                her_head_main "Это несправедливо..."
                                                m "Что? Эй, подожди, не начинай тут плакаться..."
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
                                                        $ hermi.liking += 5
                                                        m "Черт... Чувствую себя хреново..."
                                                        #m "But who could resist slapping that little behind of her's?"
                                                        m "Но кто бы смог устоять и не шлепнуть ее великолепную попку?"
                                                    #"\"She made me do this, that brat!\"":
                                                    "\"Эта девица, все из-за нее!\"":
                                                        $ hermi.liking -= 9
                                                        #m "She made me do this, that brat!"
                                                        #m "Acting all wounded now..."
                                                        #m "I bet she actually enjoyed the slapping and just won't admit it..."
                                                        m "Она подтолкнула меня к этому!"
                                                        m "А теперь строит из себя оскорбленную..."
                                                        m "Я уверен, ей понравились эти шлепки, она просто не хочет в этом признаваться..."
#                                                $ request_05_points += 1
                                                if daytime:
                                                    $ hermione_takes_classes = True
                                                    jump day_main_menu
                                                else:
                                                    $ hermione_sleeping = True
                                                    jump night_main_menu     
        
                pause
                show screen groping_02
                with d7
                $her_head_state = 7
                her_head_main "!!!!!!?"
                m "Что такое, Мисс Грейнджер?"
                $her_head_state = 15
                her_head_main "Ничего, профессор..."
                her_head_main "Просто... "
                her_head_main "Я просто не могу поверить, что это случилось..."
                her_head_main "Это... неправильно..."
                #m "Расслабься, девочка. It's not like you are enjoying this..."
                m "Расслабься, девочка. Ты могла бы получать от этого удовольствие..."
                $her_head_state = 19
                her_head_main "Что? Конечно, нет! Это непристойно..."
                her_head_main "Я иду на эту жертву ради чести моего факультета..."
                m "Да, сосредоточься на этом..."
                $her_head_state = 20
                her_head_main "...................."
                show screen bld1
                with d3
                pause
                $her_head_state = 17
                her_head_main "Но, профессор..."
                $her_head_state = 5
                her_head_main "Почему {size=+7}вы{/size} делаете это?"
                menu: 
                    m "Хм..."
                    "\"У меня есть свои причины...\"":
                        $her_head_state = 12
                        her_head_main "Oх..."
                        $her_head_state = 25
                        her_head_main "Хм..."
                    "\"Это для науки, конечно!\"":
                        $her_head_state = 3
                        her_head_main "Правда?!"
                        her_head_main "Это одно из исследований?"
                        m "Да, точно, я исследую... эм... э..."
                        m "Ну, тебе не понять, это кое-какие продвинутые магические штуки..."
                        her_head_main "Понятно..."
                        $her_head_state = 2
                        her_head_main "Ну, если это для науки, то я рада помочь..."
                    "- Сжать её ягодицы жестче -":
                        ">Вы мнете ягодицы Гермионы с удвоеной силой."
                        $her_head_state = 5
                        her_head_main "...................."
                        $her_head_state = 12
                        her_head_main "(Должна ли я промолчать.....?)"
                show screen blktone8
                with d3
                ">Вы продолжаете играть с ягодицами Гермионы..."
                ">Вы проводите руками вниз..."
                $her_head_state = 15
                her_head_main "................"
                label connection_of_rapes:
                menu:
                    "- Залесть к ней в трусики -":
                        ">Вы медленно запускаете свою руку в  ее трусики..."
                        $her_head_state = 7
                        her_head_main "Профессор... Что вы...?"
                        m "Все нормально, просто подумай о тех 15 баллах, которые ты получишь..."
                        $her_head_state = 12
                        her_head_main "............."
                        menu:
                            "- Поласкать её киску пальцем -":
                                show screen blkfade
                                with d3
                                ">Ваша рука проникает вниз, и вы трогаете ее маленькую щель..."
                                $her_head_state = 7
                                her_head_main "Про?.. Нет! Что вы?.."
                                ">Гермиона пытается вырваться..."
                                menu:
                                    "- Засунуть палец силой! -":
                                        ">Вы силой вставляете палец ей в киску..."
                                        ">Там очень тепло и узко..."
                                        ">Но там очень сухо... Не похоже, что Гермиона получает удовольствие..."
                                        jump screams_of_rapings
                                    "- Остановиться... -":
                                        pass
                            "- Поласкать пальцем ее попку -":
                                show screen blkfade
                                with d3
                                ">Вы дотрагиваетесь до её узенькой дырочки..."
                                her_head_main "Профессор? Нет! Что вы делаете!?"
                                ">Гермиона пытается вырваться..."
                                menu:
                                    "- Силой засунуть палец -":
                                        ">Вы силой вставляете палец в её дырочку..."
                                        with hpunch
                                        $her_head_state = 30
                                        her_head_main "!!?"
                                        ">Там очень тесно и тепло..."
                                        jump screams_of_rapings
                                    "- Умерить пыл... -":
                                        pass
                            "- Перестать испытывать удачу. -":
                                pass
                    "- Нет, на сегодня хватит. Отпустить её -":
                        pass
            "\"Нет. Просто стойте, Мисс Грейнджер.\"":
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
                $her_head_state = 1
                her_head_main "Сэр, пожалуйста, поторопитесь, пока кто-нибудь не узнал..."
                m "В чем проблема, Мисс Грейнджер?"
                m "Вы ведь знаете, что все это ради факультета."
                $her_head_state = 4
                her_head_main "Я-то знаю."
                her_head_main "Но другие не знают..."
                her_head_main "Так что давайте сделаем это как можно быстрее..."
                $her_head_state = 5
                her_head_main "Пожалуйста..."
                m "Ну, если ты не против..."
                show screen groping_01
                with d7
                $her_head_state = 7
                her_head_main "!!!"
                m "Что случилось?"
                $her_head_state = 5
                her_head_main "Ничего, сэр. У вас руки холодные, вот и все..."
                show screen bld1 
                with d3
                show screen blktone8
                with d3
                ">Вы растираете руки об ноги Гермионы..."
                $her_head_state = 4
                her_head_main "........................."
                ">Вы хорошенько сжимаете её ягодицы..."
                $her_head_state = 19
                her_head_main "................."
                m "Не смотри по сторонам, девочка. Я хочу, чтобы ты смотрела мне в глаза."
                her_head_main "Я бы предпочла не смотреть, сэр..."
                menu:
                    m "..."
                    "\"Ладно. Тогда просто стой.\"":
                        $her_head_state = 15
                        her_head_main "Спасибо, сэр..."
                        ">Вы слегка массируете её ягодицы..."
                        her_head_main "...................."
                        ">И вы наслаждаетесь этими формами..."
                        $her_head_state = 19
                        her_head_main "....................."
                        ">Затем вы в последний раз сжимаете её попку."
                        her_head_main "....................."
                    "\"Открой глаза, или лишишься очков!\"":
                        $ hermi.liking -= 7
                        her_head_main "Арх! {size=-5}(Ах ты, старый...{/size}"
                        m "Вы что-то сказали, Мисс Грейнджер?"
                        $her_head_state = 8
                        her_head_main "Ничего, сэр."
                        ">Вы слегка массируете её ягодицы..."
                        ">Гермиона смотрит вам в глаза, как договаривались..."
                        her_head_main "...................."
                        $her_head_state = 4
                        her_head_main "..............................."
                        m "Что я тебе говорил насчет твоего взгляда?"
                        $her_head_state = 19
                        her_head_main "Да, я помню..."
                        $her_head_state = 8
                        her_head_main "................................."
                        $her_head_state = 25
                        her_head_main "..................................."
                        her_head_main ".................................................."
                        ">Вы продолжаете наслаждаться её упругой попкой..."
                        $her_head_state = 8
                        her_head_main "....................."
                        jump connection_of_rapes
    
        
    elif hermi.whoring >= 6: # LEVEL 04 # Hermione is hesitant. <=================================================================================== SECOND EVENT.
#        $ new_request_05_02 = True # HEARTS.
        hide screen bld1
        with d3
        m "Подойди ближе, девочка. Позволь потрогать твою попку."
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
        $her_head_state = 18
        her_head_main "Вы хотите, чтобы я повернулась, сэр?"
        play music "music/(Orchestral) Playful Tension by Shadow16nh.mp3" fadein 1 fadeout 1 # SEX THEME.
        menu:
            m "Хм..."
            "\"Да. Повернитесь, Мисс Грейнджер.\"":
                her_head_main "Как скажете, сэр..."
                hide screen hermione_walk_01
                hide screen genie
                show screen ctc
                show screen no_groping_02
                with d1
                hide screen blkfade
                with d5
                pause
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
                        $her_head_state = 22
                        her_head_main "!!!!!!!!!!!!!"
                        $her_head_state = 18
                        her_head_main "Профессор....?"
                        menu:
                            "\"Ладно, ладно... Я просто не смог удержаться....\"":
                                her_head_main "Хорошо..."
                                pass
                            "- Шлепнуть еще раз -":
                                $ renpy.play('sounds/slap_02.mp3') #SLAP!
                                show screen white
                                with hpunch
                                pause.08
                                hide screen white
                                show screen bld1
                                $her_head_state = 21
                                her_head_main "!!!!!!!!!!!!!"
                                $her_head_state = 18
                                her_head_main "Профессор, что вы делаете!?"
                                her_head_main "Вы сказали, что только потрогаете!"
                                menu:
                                    "\"Ладно,ладно... Я просто не смог удержаться....\"":
                                        her_head_main "Это ведь не так трудно..."
                                        pass
                                    "- Шлепнуть еще раз -":
                                        $ renpy.play('sounds/slap_02.mp3') #SLAP!
                                        show screen white
                                        with hpunch
                                        pause.08
                                        hide screen white
                                        show screen bld1
                                        $her_head_state = 34
                                        her_head_main "Проф, не так громко, пожалуйста..."
                                        her_head_main "Нас ведь могут услышать?"
                                        m "Хорошо, хорошо... продолжу щупать..."
                                        $her_head_state = 18
                                        her_head_main "................"

                pause
                show screen groping_02
                with d7
                her_head_main "..................."
                m "Вы сегодня тихая, Мисс Грейнджер."
                her_head_main "Я...?"
                $her_head_state = 35
                her_head_main "Ну, вы знаете меня, сэр..."
                her_head_main "Я просто рада быть частью \"Гриффиндора\"..."
                her_head_main "Не обращайте внимания, продолжайте..."
                $her_head_state = 18
                her_head_main "(...Щупать меня...)"
                show screen blktone8
                with d3
                ">Вы продолжаете играть с попкой Гермионы..."
                #">And continue sliding your hands up and down her inner tighs..."
                ">Ваша рука продолжает скользить по внутренней части ее бедра..."
                her_head_main "................"
                label connection_of_rapes_02:
                menu:
                    "- Залезть к ней в трусики -":
                        ">Вы медленно запускаете свою руку в девичьи трусики... "
                        $her_head_state = 17
                        her_head_main "Профессор... Что вы...?"
                        m "Все нормально, просто подумай о тех 15 баллах, которые ты получишь..."
                        her_head_main "Как скажете..."
                        menu:
                            "- Поласкать её киску пальцем -":
                                show screen blkfade
                                with d3
                                ">Ваша рука проникает вниз, и вы трогаете ее маленькую щель..."
                                $her_head_state = 18
                                her_head_main "Профессор?"
                                menu:
                                    "- Засунуть палец в её киску силой! -":
                                        ">-Вы силой вставляете свой палец в её маленькую щель-..."
                                        ">Там очень тесно и тепло..."
                                        ">Там немного влажно... Похоже, ей немного приятно..."
                                        jump screams_of_pleasure
                                    "- Прекратить... -":
                                        pass
                            "- Поласкать ее попку своим пальцем -":
                                show screen blkfade
                                with d3
                                ">Вы дотрагиваетесь до её узенькой дырочки..."
                                her_head_main "Профессор? Что вы пытаетесь сделать?"
                                menu:
                                    "- Силой вставить палец в её узкую попку -":
                                        ">Вы вставляете свой палец в её узенькую дырочку..."
                                        with hpunch
                                        $her_head_state = 36
                                        her_head_main "Ах... ваш палец в моей ..."
                                        ">Там очень тесно и тепло..."
                                        jump screams_of_pleasure
                                    "- Прекратить... -":
                                        pass
                            "- Перестать испытывать удачу и отпустить девочку -":
                                pass
                    "- Нет, на сегодня хватит. Отпустить девочку -":
                        pass
            "\"Нет. Просто стойте, Мисс Грейнджер.\"":
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
                $her_head_state = 1
                her_head_main "Сэр, поторопитесь, пока никто не узнал..."
                m "В чем проблема, Мисс Грейнджер?"
                m "Вы ведь знаете, что все это ради факультета."
                $her_head_state = 4
                her_head_main "Знаю."
                her_head_main "Но другие не знают..."
                her_head_main "Так что давайте покончим с этим как можно быстрее..."
                $her_head_state = 5
                her_head_main "Пожалуйста..."
                m "Ну, если ты настаиваешь..."
                show screen groping_01
                with d7
                $her_head_state = 7
                her_head_main "!!!"
                m "Что случилось?"
                $her_head_state = 5
                her_head_main "Ничего, сэр. У вас руки холодные, вот и все..."
                show screen bld1 
                with d3
                show screen blktone8
                with d3
                ">Вы растираете руки об ноги Гермионы..."
                $her_head_state = 4
                her_head_main "........................."
                ">И хорошенько жмакаете ягодицы..."
                $her_head_state = 19
                her_head_main "................."
                m "Не смотри по сторонам, девочка. Я хочу, чтобы ты смотрела мне в глаза."
                her_head_main "Я бы предпочла не смотреть, сэр..."
                menu:
                    m "..."
                    "\"Ладно. Тогда просто стой...\"":
                        $her_head_state = 15
                        her_head_main "Спасибо сэр..."
                        ">Вы слегка массируете её ягодицы..."
                        her_head_main "...................."
                        ">Вы продолжаете наслаждаться её упругой попкой..."
                        $her_head_state = 19
                        her_head_main "....................."
                        ">Затем вы в последний раз сжимаете их."
                        her_head_main "....................."
                    "\"Открой глаза, или не получишь очки!\"":
                        $ hermi.liking -= 20
                        her_head_main "Арх! {size=-5}(Старый козел...{/size}"
                        m "Вы что-то сказали, Мисс Грейнджер?"
                        $her_head_state = 8
                        her_head_main "Ничего, сэр."
                        ">Вы слегка массируете её ягодицы..."
                        ">Гермиона смотрит вам в глаза, как договаривались..."
                        her_head_main "...................."
                        $her_head_state = 4
                        her_head_main "..............................."
                        m "Что я тебе говорил о глазах?"
                        $her_head_state = 19
                        her_head_main "Да, я помню...."
                        $her_head_state = 8
                        her_head_main "................................."
                        $her_head_state = 25
                        her_head_main "..................................."
                        her_head_main ".................................................."
                        ">Вы продолжаете наслаждаться её упругой попкой..."
                        $her_head_state = 8
                        her_head_main "....................."
                        jump connection_of_rapes_02  
        
  
  
  
  
    
        
label ending_of_screams_of_pleasure:
    if hermi.whoring <= 5:
        $ hermi.whoring +=1
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
    
#    $ request_05_points += 1
   
   
    $ hermione_chibi_xpos = 400 #Near the desk.
    show screen hermione_02 #Hermione stands still.
    show screen bld1
    hide screen blkfade
    with Dissolve(1)
    
    $ pos = POS_370
    $herView.showQQ( "body_29.png", pos )
    her ".................."
    her "Спасибо, сэр..."
    if daytime:
        her "Мне лучше идти. Занятия вот-вот начнутся."
    else:
        her "Я лучше пойду. Уже очень поздно..."
    

    hide screen bld1
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
    
    if hermi.whoring >= 3 and hermi.whoring <= 5: #First level. Not happy.
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
    $her_head_state = 10
    her_head_main "НЕТ! Что вы наделали!!?"
    ">Гермиона сильно толкает вас..."
    with hpunch
    her_head_main "Почему вы это делаете со мной, сэр...?"
    $her_head_state = 27
    her_head_main "Я не согласна делать это... для..."
    her_head_main "Для... вас..."
    with hpunch
    $her_head_state = 29
    her_head_main "{size=+7}ВЫ ИЗНАСИЛОВАЛИ МЕНЯ!{/size}"
    g4 "Что? Не смеши, девочка! Я не делал этого!"
    her_head_main "Да, изнасиловали! Изнасиловали!"
    g4 "Я уверен, что это не так!"
    her_head_main "Нет, вы сделали это, профессор!"
    $her_head_state = 31
    her_head_main "Теперь дайте мне 20 очков..."
    her_head_main "Нет, 100 очков, или я пожалуюсь на вас в министерство!!"
    menu:
        m "(Ах, черт...)"
        "\"Ладно, ладно... 100 очков...\"":
            $ gryffindor +=100
            m "100 очков \"Гриффиндору\" !"
            m "Все, сделано..."
            m "Теперь вы успокоились, Мисс Грейнджер?"
            $her_head_state = 29
            her_head_main "Нет, еще нет!"
            her_head_main "Я была изнасилована!"
            g4 "Ох, успокойся  девочка, я не насиловал тебя! Все, что я сделал - это..."
            with hpunch
            her_head_main "{size=+7}Вы изнасиловали меня!!!{/size}"
            g4 "Великие пески пустыни, потише об изнасиловании!"
            g4  "Кто-нибудь может услышать тебя!"
            her_head_main "Отлично! Я хочу, чтобы они услышали!"
            m "Почему ты до сих пор недовольна? Я уже заплатил тебе!"
            $her_head_state = 32
            her_head_main "Oх... ладно..."
            $her_head_state = 33
            her_head_main "Но я все равно вас ненавижу! Я ненавижу вас, профессор!!"
            $ hermi.liking -=30

        "\"Ты блефуешь, девочка!\"":
            $her_head_state = 29
            her_head_main "Нет! Я сделаю это"
            g4 "Делай, что хочешь"
            g4 "Никакого изнасилования не было!"
            her_head_main "Я ненавижу вас, профессор!"
            $ hermi.liking -=50


    hide screen bld1
    hide screen ctc
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

    if hermi.whoring >= 3 and hermi.whoring <= 5: #First level. Not happy.
        $her_head_state = 12
        her_head_main "..........................."
        

        
    hide screen hermione_01_f #Hermione stands still.
    with Dissolve(.3)
    $ renpy.play('sounds/door.mp3') #Sound of a door opening.
    with Dissolve(.3)
    pause.5

    $event.Finalize()    
    if daytime:
        $ hermione_takes_classes = True
        jump day_main_menu
    else:
        $ hermione_sleeping = True
        jump night_main_menu        
    


########### SCREAM OF PLEASURES ###        
label screams_of_pleasure:
    $her_head_state = 34
    her_head_main "Aх...."
    her_head_main "Он внутри меня..."
    $her_head_state = 18
    her_head_main "Нет, профессор, вы должны остановиться..."
    m "Почему? Тебе не нравиться?"
    her_head_main "Не имеет значения, нравится мне это или нет, сэр."
    her_head_main "Вы знаете почему я делаю это..."
    her_head_main "И это неправильно, что вы даете всего 15 очков..."
    ">Гермиона отталкивает вас..."
    m "Хех... Я вижу..."
    m "Ну, в таком случае..."
    jump ending_of_screams_of_pleasure

    
