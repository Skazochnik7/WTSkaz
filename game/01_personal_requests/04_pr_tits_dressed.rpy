    
###################REQUEST_04 (Level 02) (Touch tits's through fabric.)###############################
label new_request_04:
    $herView.hideQQ()
    m "{size=-4}(Я хочу немного потискать ее грудки. Даже не буду просить оголить их. Очень безобидно){/size}"
    $ menu_x = 0.5 #Default position of the menu (0.5). Version B is $ menu_x = 0.2
    menu:
        "\"(Да, давай попробуем!)\"":
            pass
        "\"(Не сейчас.)\"":
            $event.NotFinished()
            jump new_personal_request
    
    
    
    $ current_payout = 15 #Used when haggling about price of th favor.
    if whoring <=2: # LEVEL 01 # Hermione refuses.
        jump too_much
        
    elif whoring >= 3 and whoring <= 5: # LEVEL 02 # Hermione is hesitant. 
#        $ new_request_04_01 = True # Hearts.

        hide bld1
        with d3
        m "Подойди, девочка..."
        $her_head_state = 2
        her_head_main "Эм... Ладно..."
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


        her_head_main "сэр.....?"
        menu: 
            m "..."
            "\"Я хочу потискать твои грудки.\"":
                $her_head_state = 3
                her_head_main "Что? Что вы имеете в виду, профессор--?"
                ">Гермиона чуть отходит назад..."
                ">Вы притягиваете ее и хватаетесь за грудки..." #WARNING_Z What the fuck?
                "- Просто протягиваете руку и хватаетесь за них. -"
                ">Вы протягиваете вторую и руку и вот уже держите обе сиськи!"
        stop music fadeout 1.0
        with hpunch
        $her_head_state = 7
        her_head_main "!!!?"
        $her_head_state = 8
        her_head_main "Профессор Дамблдор?!"
        ">Гермиона пытается оттолкнуть вас, но вы крепко схватили ее за бюст..."
        play music "music/(Orchestral) Playful Tension by Shadow16nh.mp3" fadein 1 fadeout 1 # SEX THEME.
        $her_head_state = 9
        her_head_main "Профессор, что вы--?"
        ">Она снова пытается оттолкнуть вас."
        ">Вы сжимаете ее сиськи как тисками."
        $her_head_state = 10
        her_head_main "Профессор, вы делаете мне больно!"
        g4 "Просто стой на месте, девочка!"
        $her_head_state = 11
        her_head_main "Н-но..."
        m "Я просто хочу немного потискать твою грудь, за что ты получишь очки!"
        $her_head_state = 12
        her_head_main "Н-но... это..."
        m "Просто стой..."
        m "Представь что ты в любимом месте или вроде того..."
        $her_head_state = 11
        her_head_main "М-моем любимом месте...?"
        ">Вы ощущаете насколько упруги грудки этой девчушки..."
        hide screen hermione_walk_01
        hide screen genie
        show screen ctc
        show screen bld1
        show screen chair_02 #Genie's chair.
        show screen groping_03
        with d1
        hide screen blkfade
        with d5
        pause
        $her_head_state = 13
        her_head_main "............................"
        menu:
            "- Сжать ее груди со всей силой -":
                show screen blktone
                with d5
                ">Вы собираетесь с силами..."
                $her_head_state = 12
                her_head_main "Мои..........."
                ">Вы сжимаете ее груди сильнее..."
                $her_head_state = 13
                her_head_main "Профессор, вы делаете мне больно..."
                m "Тише, девочка..."
                $her_head_state = 12
                her_head_main "Ау.............."
                ">Вы сжимаете ее большие груди еще сильнее."
                $her_head_state = 10
                her_head_main "Ах! Это больно!"
                her_head_main "Они сейчас лопнут! Пожалуйста, прекратите!"
                m "Они не могут лопнуть, глупышка..."
                ">Вы ослабляете напор..."
                $her_head_state = 13
                her_head_main "Это больно..."
                m "Ты будешь в порядке..."
                $her_head_state = 4
                her_head_main "........."

            "- Массировать грудь -":
                show screen blktone
                with d5
                ">Вы начинаете массировать грудь Гермионы..."
                $her_head_state = 13
                her_head_main "Профессор...?"
                m "Очки, девочка... Тебе нужны очки. Сконцентрируйся на этом."
                $her_head_state = 4
                her_head_main "Да..."
                $her_head_state = 15
                her_head_main "Да, честь \"Гриффиндора\"..."
                "*Жим-жим!*"
                ">Вы продолжаете массировать сисечки..."
                ">Вы слегка щипаете одну из грудок..."
                $her_head_state = 13
                her_head_main "Профессор... Вы ущепнули меня...?"
                ">Ваши попытки оказались напрасны. Ткань униформы слишком толстая..."
                $her_head_state = 15
                her_head_main "\"Гриффиндор\" ............"

            "- Отпустить ее и дать очки -":
                show screen blktone
                with d5
                m "Ну, если ты собираешься так драматизировать, то можешь просто уйти..."
                show screen blkfade
                with d5
                ">Вы отпускаете ее грудь..."
                $her_head_state = 14
                her_head_main "Правда?"
                m "Да, да... Я все равно дам тебе очки..."
                her_head_main "Э-э... Спасибо, профессор..."
                m "Но сегодня вы их не заработали..."
                $her_head_state = 12
                her_head_main "Оу........."

    if whoring >= 6: # LEVEL 03 and higher # Hermione doesn't mind. <============================================================================EVENT LEVEL: 03
#        $ new_request_04_02 = True # Hearts.

#        if whoring > 8: # LEVEL 03.
#            $ new_request_04_03 = True # Hearts.

        stop music fadeout 2.0
        m "Подойди ближе, девочка... Я хочу сделать тебе массаж груди..."
        $her_head_state = 14
        her_head_main "Как скажете, профессор..."
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
        play music "music/(Orchestral) Playful Tension by Shadow16nh.mp3" fadein 1 fadeout 1 # SEX THEME.
        if this.new_request_12.IsFinished(): # Если уже играл с ее голыми сиськами
            ">Гермиона начинает стягивать свою униформу..."
            m "Нет, не стоит. Я хочу делать это пока ты полностью одета..."
            her_head_main "Ох, хорошо..."
        ">Гермиона стоит перед вами в ожидании..."
        ">Вы хватаете ее большие сиськи..."
        ">И усиленно начинаете их массировать..."

        hide screen hermione_walk_01
        hide screen genie
        show screen ctc
        show screen bld1
        show screen chair_02 #Genie's chair.
        show screen groping_03
        with d1
        hide screen blkfade
        with d5
        pause

        "*Жмак-жмак-жмак*"
        $her_head_state = 16
        her_head_main "................"
        menu:
            "\"Тебе нравится это, девочка?\"":
                $her_head_state = 14
                her_head_main "Что...?"
                her_head_main "Ох, Я не против этого..."
                "*Жмак-жмак-жмак*"
                ">Вы продолжаете мягко мять ее грудь..."
                $her_head_state = 16
                her_head_main "То есть, это не такая большая плата за то, что я получу в конце..."
                ">Вы продолжаете мять ее грудки через униформу..."
                $her_head_state = 1
                her_head_main "Небольшая цена для чести моего факультета......{image=textheart.png}"
            "- Резко потянуть их с силой -":
                show screen blktone8
                with d3
                ">Внезапно вы сильно оттягиваете ее сиськи..."
                with vpunch
                $her_head_state = 9
                her_head_main "Ауч...."
                ">ВЫ снова оттягиваете ее сиськи. На этот раз чуть сильнее."
                with vpunch
                her_head_main "Ой! Профессор, что вы пытаетесь сделать...?"
                ">Вы оттягиваете их вниз со всей силы..."
                with vpunch
                with vpunch
                ">Гермиона теряет равновесие..."
                $her_head_state = 17
                her_head_main "*Задыхаясь* Что вы делаете, сэр...?"
                $her_head_state = 18
                her_head_main "Не нужно быть таким грубым со мной....{image=textheart.png}"
                hide screen blktone8

        if whoring>=12: # Если уже играл с ее голыми сиськами
            her "Эмм... Профессор, может, вы будете делать это по-настоящему?"
            m "По-настоящему?"
            her "Да, я хочу, чтобы вы... То есть, чтобы я заработала больше очков. Может, я сниму форму?"
            menu:
                "Заголяйтесь, мисс!":
                    m "Хорошо. Заголяйтесь, мисс!"
                    show screen blkfade
                    with Dissolve(1)
                    pause.5

                    $ posHead = gMakePos( 390, 340 )

                    $herViewHead.showQ( "body_120.png", posHead )
                    her "Пфф! Сэр, вам обязательно \nбыть таким вульгарным?"
                    $herViewHead.hideQ()
                    m "Вы будете меня поучать, мисс Грейнджер, или, все-таки, зарабатывать очки?"
                    $herViewHead.showQ( "body_66.png", posHead )
                    her "......................."
                    $herViewHead.hideQ()
                    m "Итак?"


                    hide screen genie
                    show screen ctc
                    #show screen chair_02 #Genie's chair.
                    hide screen genie
                    show screen genie_and_tits_01
                    with d1
                    hide screen blkfade
                    with d5
                    "> Гермиона задирает блузку и рубашку."
                    $current_payout+=20
                    jump new_request_12_mainonly

                "На сегодня все.":
                    show screen blkfade
                    with Dissolve(1)
                    pause.5
                    $ hermione_chibi_xpos = 400 #Near the desk.
                    hide screen bld1
#                    $herView.hideQ()
                    hide screen blktone 
                    hide screen hermione_02
                    hide screen ctc
                    hide screen bld1
                    hide screen chair_02 #Genie's chair.
                    hide screen groping_03
                    show screen genie
                    show screen hermione_01 #Hermione stands still.
                    hide screen blkfade
                    with Dissolve(1)


                    $herView.showQQ( "body_55.png", pos )
                    m "На сегодня все, девочка."
                    m "Впрочем, если ты готова лечь и раздвинуть ножки..."
                    if whoring<18: # Если не готова к сексу
                        $herView.showQQ( "body_05.png", pos )
                        her "Аргх! Сэр... как вы можете!... Я!..."
                        m "Тише, дорогая, тише. Я просто пошутил."
                    else:
                        $herView.showQQ( "body_103.png", pos )
                        her "Я... я согласна, профессор."
                        g9 "Я и не сомневался, что ты будешь только ЗА."
                        $herView.showQQ( "body_120.png", pos )
                        her "Не просто так, профессор, это за очки для факультета, для гордого \"Гриффиндора\"!"
                        m "Да-да, старая песня."
                        $herView.showQQ( "body_51.png", pos )
                        her "Аргх! Сэр... как вы можете!... Я!..."
                        m "Ладно-ладно, мисс Грейнджер, я пошутил насчет раздвинутых ножек. Никто на вас не покушается."

                    if not end.IsEnding(const_ENDING_STRONG_GIRL):
                        $herView.showQQ( "body_120.png", pos )
                        her "Гррх!... Заплатите мне и я пойду!"
                        $mad=+30
                        jump new_request_04_finish
                    else:
                        $MusicStart("Supergirl",0.3)                                   
                        $herView.showQQ( "body_50.png", pos )
                        her "Эти ваши шутки, профессор..."
                        $herView.showQQ( "body_61.png", pos )
                        her "................................"
                        $herView.showQQ( "body_69.png", pos )
                        her "................................"
                        m "Что?"
                        $herView.showQQ( "body_29.png", pos )
                        her "Я тут подумала, что может быть..."
                        m "Да?"
                        $herView.showQQ( "body_56.png", pos )
                        her "Может быть и могла бы..."
                        m "Могла бы что?"
                    if whoring<18: # Если не готова к сексу
                        $herView.showQQ( "body_123.png", pos )
                        her "Ну как вы и сказали, раздвинуть... Если это будет как следует оплачиваться, конечно!"
                        g9 "Разумеется, будет. Конечно!" 
                    else:
                        $herView.showQQ( "body_123.png", pos )
                        her "Ну как вы и сказали, раздвинуть... бесплатно."
                        $herView.showQQ( "body_64.png", pos )
                        her "Не подумайте ничего такого, просто, вы это {size=+4}ТАК{/size} здорово делаете..."
                        g9 "Ну вот, наконец-то ты берешься за ум, девочка!"

                    g9 "Ну тогда иди сюда, снимай трусы..."
                    $herView.showQQ( "body_80.png", pos )
                    her "Тише, профессор, тише, не надо так возбуждаться!.. Я тоже {size=+4}ПОШУТИЛА{/size}!"
                    g4 "...................."
                    g4 "Ах ты, мелкая мерзавка!"
                    $herView.showQQ( "body_100.png", pos )
                    her "Мы квиты, сэр! А теперь я хочу получить свои очки."
                    menu:
                        "Вон!":
                            m "Вон отсюда! Очков не будет!"
                            $herView.showQQ( "body_05.png", pos )
                            her "Поскольку вы не держите свое слово, сэр, вероятно, я не смогу больше приходить к вам."
                            $mad+=50
                            jump new_request_04_nopoints
                        "Что ж, получай!":
                            m "Что ж, мисс Грейнджер, получайте свои очки."
                            m "Но в следующий раз за такие шутки очки у вас будут вычитаться, а не добавляться."
                            m "Я доступно излагаю?"
                            $herView.showQQ( "body_58.png", pos )
                            her "Вполне, сэр."
                            her "Но если так, профессор, то я мне придется молчать, как рыба об лед. Я буду бояться лишнее слово сказать."
                            m "Это только к лучшему, мисс Грейнджер."
                            $herView.showQQ( "body_129.png", pos )
                            her "Как же я буду отчитываться вам, профессор?.. Но, конечно, я сделаю как вы говорите."
                            "> Гермиона обрачивается уходить."
                            m "Ладно, мисс Грейнджер, на этот раз я вас прощаю. Но предупреждаю - попридержите свой язычок!"
                            $herView.showQQ( "body_84.png", pos )
                            her "Конечно, профессор!"



    label new_request_04_finish:
    $SetHearts(GetStage(whoring, 3, 3, 3))

    if whoring <= 5:
        $ whoring +=1
        
    show screen blkfade 
    with d3
    hide screen bld1
    $herView.hideQ()
    hide screen blktone 
    hide screen hermione_02
    hide screen ctc
    hide screen bld1
    hide screen chair_02 #Genie's chair.
    hide screen groping_03
    show screen genie
    show screen hermione_01 #Hermione stands still.


    stop music fadeout 1.0
    if whoring<12: # Если еще не играл с ее голыми сиськами
        ">Вы отпускаете грудь Гермионы..."
        m "На этом все."
        $her_head_state = 4
        her_head_main "................"
    else:
        $MusicStop()
    
    hide screen blkfade 
    with d3
    
    $ gryffindor +=current_payout
    m "\"Гриффиндор\" получает [current_payout] очков!"
    
#    $ request_04_points += 1
   
   
    $ hermione_chibi_xpos = 400 #Near the desk.
    show screen hermione_02 #Hermione stands still.
    show screen bld1
    hide screen blkfade
    with Dissolve(1)
    
    $ pos = POS_370
    if current_payout==35:
        $herView.showQQ( "body_05.png", pos )
        her "Постойте, сэр!"
        her "Почему 35 очков? 15 и 35 в сумме дают 50!"
        m "Нет, мисс Грейнджер. 35 это и в сумме 35!"
        $herView.showQQ( "body_76.png", pos )
        her "Сэр, при всем уважении! Пощупать через форму всегда стоило 15 очков, а просто так - 35!"
        her "Не пытайтесь меня обсчитать!"
        m "Мисс Грейнджер, я пошел вам навстречу, разрешил демонстрировать сиськи..."
        m "...и дал 35 очков вместо обещанных 15-ти. И теперь выcлушиваю от вас претензии!"
        m "Не зря говорят, добрые дела не остаются безнаказанными..."
        her "Добрые дела, сэр?! Мы договаривались, что..."
        m "Договаривались? Мы что, договаривались что вы продаете мне две услуги за раз?"
        $herView.showQQ( "body_66.png", pos )
        her "Нет, но..."
        m "Если бы вы заранее обсудили это со мной..."
        her "Я хотела, но..."
        m "Что \"но\"? Вам так понравилось, что вы забыли обо всем на свете?" 
        $herView.showQQ( "body_88.png", pos )
        her "Нет! Совсем нет!"
        m "Как бы там ни было, мисс Грейнджер, решение окончательное. 35 очков и ни очком больше!" 
        $herView.showQQ( "body_86.png", pos )
        her "Это нечестно, сэр!"
        $mad+=15
    else:
        $herView.showQQ( "body_29.png", pos )
        her ".................."
        her "Спасибо, сэр..."
        if daytime:
            her "Теперь, мне лучше идти. Занятия вот-вот начнутся."
        else:
            her "Мне лучше пойти. Уже поздно..."
    
    label new_request_04_nopoints:
    hide screen bld1
    $herView.hideQ()
    with Dissolve(.3)
    $ walk_xpos=400 #Animation of walking chibi. (From)
    $ walk_xpos2=610 #Coordinates of it's movement. (To)
    $ hermione_speed = 02.0 #The speed of moving the walking animation across the screen.
    show screen hermione_walk_01_f 
    pause 2
    hide screen hermione_walk_01_f 
    $ renpy.play('sounds/door.mp3') #Sound of a door opening.
    with Dissolve(.3)
    pause.5

    ### MUSIC BLOCK ###
    if daytime:
        play music "music/Brittle Rille.mp3" fadein 1 fadeout 1 # DAY MUSIC
    else:
        play music "music/Music for Manatees.mp3" fadein 1 fadeout 1 # NIGHT MUSIC
    ### END OF BLOCK ###


    if daytime:
        $ hermione_takes_classes = True
        jump day_main_menu
    else:
        $ hermione_sleeping = True
        jump night_main_menu
