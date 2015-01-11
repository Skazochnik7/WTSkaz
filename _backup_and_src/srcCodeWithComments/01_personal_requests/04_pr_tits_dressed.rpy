    
###################REQUEST_04 (Level 02) (Touch tits's through fabric.)###############################
label new_request_04:
    #__#hide screen hermione_main 
    #__#with d3
    $herView.hideQQ()
    m "{size=-4}(Я хочу немного потискать ее грудки. Даже не буду просить оголить их. Очень безобидно){/size}"
    $ menu_x = 0.5 #Default position of the menu (0.5). Version B is $ menu_x = 0.2
    menu:
        "\"(Да, давай попробуем!)\"":
            pass
        "\"(Не сейчас.)\"":
            jump new_personal_request
    
    
    
    if whoring <=2: # LEVEL 01 # Hermione refuses.
        jump too_much
        
    elif whoring >= 3 and whoring <= 5: # LEVEL 02 # Hermione is hesitant. 
        $ new_request_04_01 = True # Hearts.
        hide bld1
        with d3
        m "Подойди, девочка..."
        #__#her_02 "Эм... Ладно..."
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

        #__#her_02 "сэр.....?"
        her_head_main "сэр.....?"
        menu: 
            m "..."
            "\"Я хочу потискать твои грудки.\"":
                #__#her_03 "Что? Что вы имеете в виду, профессор--?"
                $her_head_state = 3
                her_head_main "Что? Что вы имеете в виду, профессор--?"
                ">Гермиона чуть отходит назад..."
                ">Вы притягиваете ее и хватаетесь за грудки..." #WARNING_Z What the fuck?
                "- Просто протягиваете руку и хватаетесь за них. -"
                ">Вы протягиваете вторую и руку и вот уже держите обе сиськи!"
        stop music fadeout 1.0
        with hpunch
        #__#her_07 "!!!?"
        $her_head_state = 7
        her_head_main "!!!?"
        #__#her_08 "Профессор Дамблдор?!"
        $her_head_state = 8
        her_head_main "Профессор Дамблдор?!"
        ">Гермиона пытается оттолкнуть вас, но вы крепко схватили ее за бюст..."
        play music "music/(Orchestral) Playful Tension by Shadow16nh.mp3" fadein 1 fadeout 1 # SEX THEME.
        #__#her_09 "Профессор, что вы--?"
        $her_head_state = 9
        her_head_main "Профессор, что вы--?"
        ">Она снова пытается оттолкнуть вас."
        ">Вы сжимаете ее сиськи как тисками."
        #__#her_10 "Профессор, вы делаете мне больно!"
        $her_head_state = 10
        her_head_main "Профессор, вы делаете мне больно!"
        g4 "Просто стой на месте, девочка!"
        #__#her_11 "Н-но..."
        $her_head_state = 11
        her_head_main "Н-но..."
        m "Я просто хочу немного потискать твою грудь, за что ты получишь очки!"
        #__#her_12 "Н-но... это..."
        $her_head_state = 12
        her_head_main "Н-но... это..."
        m "Просто стой..."
        m "Представь что ты в любимом месте или вроде того..."
        #__#her_11 "М-моем любимом месте...?"
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
        #__#her_13 "............................"
        $her_head_state = 13
        her_head_main "............................"
        menu:
            "- Сжать ее груди со всей силой -":
                show screen blktone
                with d5
                ">Вы собираетесь с силами..."
                #__#her_12 "Мои..........."
                $her_head_state = 12
                her_head_main "Мои..........."
                ">Вы сжимаете ее груди сильнее..."
                #__#her_13 "Профессор, вы делаете мне больно..."
                $her_head_state = 13
                her_head_main "Профессор, вы делаете мне больно..."
                m "Тише, девочка..."
                #__#her_12 "Ау.............."
                $her_head_state = 12
                her_head_main "Ау.............."
                ">Вы сжимаете ее большие груди еще сильнее."
                #__#her_10"Ах! Это больно!"
                $her_head_state = 10
                her_head_main "Ах! Это больно!"
                #__#her_10 "Они сейчас лопнут! Пожалуйста, прекратите!"
                her_head_main "Они сейчас лопнут! Пожалуйста, прекратите!"
                m "Они не могут лопнуть, глупышка..."
                ">Вы ослабляете напор..."
                #__#her_13 "Это больно..."
                $her_head_state = 13
                her_head_main "Это больно..."
                m "Ты будешь в порядке..."
                #__#her_04 "........."
                $her_head_state = 4
                her_head_main "........."

            "- Массировать грудь -":
                show screen blktone
                with d5
                ">Вы начинаете массировать грудь Гермионы..."
                #__#her_13 "Профессор...?"
                $her_head_state = 13
                her_head_main "Профессор...?"
                m "Очки, девочка... Тебе нужны очки. Сконцентрируйся на этом."
                #__#her_04 "Да..."
                $her_head_state = 4
                her_head_main "Да..."
                #__#her_15 "Да, честь \"Гриффиндора\"..."
                $her_head_state = 15
                her_head_main "Да, честь \"Гриффиндора\"..."
                "*Жим-жим!*"
                ">Вы продолжаете массировать сисечки..."
                ">Вы слегка щипаете одну из грудок..."
                #__#her_13 "Профессор... Вы ущепнули меня...?"
                $her_head_state = 13
                her_head_main "Профессор... Вы ущепнули меня...?"
                ">Ваши попытки оказались напрасны. Ткань униформы слишком толстая..."
                #__#her_15 "\"Гриффиндор\" ............"
                $her_head_state = 15
                her_head_main "\"Гриффиндор\" ............"

            "- Отпустить ее и дать очки -":
                show screen blktone
                with d5
                m "Ну, если ты собираешься так драматизировать, то можешь просто уйти..."
                show screen blkfade
                with d5
                ">Вы отпускаете ее грудь..."
                #__#her_14 "Правда?"
                $her_head_state = 14
                her_head_main "Правда?"
                m "Да, да... Я все равно дам тебе очки..."
                #__#her_14 "Э-э... Спасибо, профессор..."
                her_head_main "Э-э... Спасибо, профессор..."
                m "Но сегодня вы их не заработали..."
                #__#her_12 "Оу........."
                $her_head_state = 12
                her_head_main "Оу........."

    if whoring >= 6: # LEVEL 03 and higher # Hermione doesn't mind. <============================================================================EVENT LEVEL: 03
        $ new_request_04_02 = True # Hearts.
        if whoring > 8: # LEVEL 03.
            $ new_request_04_03 = True # Hearts.
        stop music fadeout 2.0
        m "Подойди ближе, девочка... Я хочу сделать тебе массаж груди..."
        #__#her_14 "Как скажете, профессор..."
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
        ">Гермиона начинает стягивать свою униформу..."
        m "Нет, не стоит. Я хочу делать это пока ты полностью одета..."
        #__#her_14 "Ох, хорошо..."
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
        #__#her_16 "................"
        $her_head_state = 16
        her_head_main "................"
        menu:
            "\"Тебе нравится это, девочка?\"":
                #__#her_14 "Что...?"
                $her_head_state = 14
                her_head_main "Что...?"
                #__#her_14 "Ох, Я не против этого..."
                her_head_main "Ох, Я не против этого..."
                "*Жмак-жмак-жмак*"
                ">Вы продолжаете мягко мять ее грудь..."
                #__#her_16 "То есть, это не такая большая плата за то, что я получу в конце..."
                $her_head_state = 16
                her_head_main "То есть, это не такая большая плата за то, что я получу в конце..."
                ">Вы продолжаете мять ее грудки через униформу..."
                #__#her_01 "Небольшая цена для чести моего факультета......{image=textheart.png}"
                $her_head_state = 1
                her_head_main "Небольшая цена для чести моего факультета......{image=textheart.png}"
            "- Резко потянуть их с силой -":
                show screen blktone8
                with d3
                ">Внезапно вы сильно оттягиваете ее сиськи..."
                with vpunch
                #__#her_09 "Ауч...."
                $her_head_state = 9
                her_head_main "Ауч...."
                ">ВЫ снова оттягиваете ее сиськи. На этот раз чуть сильнее."
                with vpunch
                #__#her_09 "Ой! Профессор, что вы пытаетесь сделать...?"
                her_head_main "Ой! Профессор, что вы пытаетесь сделать...?"
                ">Вы оттягиваете их вниз со всей силы..."
                with vpunch
                with vpunch
                ">Гермиона теряет равновесие..."
                #__#her_17 "*Задыхаясь* Что вы делаете, сэр...?"
                $her_head_state = 17
                her_head_main "*Задыхаясь* Что вы делаете, сэр...?"
                #__#her_18 "Вам не стоит быть таким грубым со мной....{image=textheart.png}"
                $her_head_state = 18
                her_head_main "Вам не стоит быть таким грубым со мной....{image=textheart.png}"
        



    if whoring <= 5:
        $ whoring +=1
        
    show screen blkfade 
    with d3
    hide screen bld1
    #__#hide screen hermione_main
    $herView.hideQ()
    hide screen blktone 
    hide screen hermione_02
    hide screen ctc
    hide screen bld1
    hide screen chair_02 #Genie's chair.
    hide screen groping_03
    hide screen blktone8
    show screen genie
    show screen hermione_01 #Hermione stands still.


    stop music fadeout 1.0
    ">Вы отпускаете грудь Гермионы..."
    m "На этом все."
    #__#her_04 "................"
    $her_head_state = 4
    her_head_main "................"
    
    hide screen blkfade 
    with d3
    
    $ gryffindor +=15
    m "\"Гриффиндор\" получает 15 очков!"
    
    $ request_04_points += 1
   
   
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
        her "Мне лучше пойти. Уже поздно..."
    
    hide screen bld1
    #__#hide screen hermione_main
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