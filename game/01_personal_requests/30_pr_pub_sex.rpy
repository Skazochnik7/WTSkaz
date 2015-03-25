

    

    
###################REQUEST_30 (Level 08) (75 pt.) (FUCK A CLASSMATE). (Available during daytime only).
label new_request_30: #LV.8 (Whoring = 21 - 23)

    $herView.hideQQ()
    m "{size=-4}(Приказать ей переспать с одноклассником?){/size}"
    $ menu_x = 0.5 #Default position of the menu (0.5). Version B is $ menu_x = 0.2
    menu:
        "\"(Да, давай сделаем это!)\"":
            pass
        "\"(Не cейчас.)\"":
            $event.NotFinished()
            jump new_personal_request
            
    
    $ pos = POS_140
    
    if request_30_points == 0: # <================================================================================ FIRST TIME
        m "Мисс Грейнджер..."
        m "Сегодня я хочу, чтобы вы занялись сексом с любым одноклассником на ваш выбор."
        if hermi.whoring <=20 or request_24_points <= 1: # Counts how many times you sent Hermione to give blowjob to a boy.
            jump too_much
        play music "music/Chipper Doodle v2.mp3" fadein 1 fadeout 1 # HERMIONE'S THEME.
        $herView.hideshowQQ( "body_47.png", pos )
        her ".............."
        $herView.hideshowQQ( "body_66.png", pos )
        her "У меня было предчувствие, что, рано или поздно, до этого дойдет..."
        $herView.hideshowQQ( "body_69.png", pos )
        her "Но..."
        her "..................."
        m "Если вы сделаете это, \"Гриффиндор\" сегодня вечером получит семьдесят пять очков."
        $herView.hideshowQQ( "body_79.png", pos )
        her "Ну что ж, тогда я сделаю это, сэр."
        m "Отлично. Тогда встретимся после уроков."
        $herView.hideshowQQ( "body_120.png", pos )
        her "............."

        
    else: # <================================================================================ NOT FIRST TIME
        m "Мисс Грейнджер..."
        m "Мне нужно, чтобы вы занялись сексом с еще одним из ваших одноклассников."
        $herView.hideshowQQ( "body_117.png", pos )
        her "Еще раз, сэр?"
        m "Да. И вы снова получите 75 очков."
        $herView.hideshowQQ( "body_79.png", pos )
        her "Ну ладно..."
        
    
    
    
    
    $ request_30 = True

    hide screen bld1
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
    $event.Finalize()    
    jump day_main_menu
    
    

 
label new_request_30_complete: # <=================================================================================================== EVENING
    
    $ pos = POS_370

    # LEVEL 08+                
    if one_out_of_three == 1: ### EVENT (A)
        if fucked_ron_and_har:
            jump returns_next_morning
        else:
            $ fucked_ron_and_har = True #In public events. Have sex with a classmate. Event # 1. "Returns next morning". Turns True after that.

        
        m "....."
        m ".........."
        m "Она должна была уже быть здесь..."
        m "Хм..."
        $ request_30_points += 1 
        $ request_30 = False 
        $ hermione_sleeping = True
        $ request_30_a = True #Turns True when hermione fails to show up after her "Fuck a classmate" favour. Runs an event next morning.
        return
        # NEXT MORNING
        
        
    elif one_out_of_three == 2: ### EVENT (B)
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
        m "Мисс Грейнджер, вы выполнили задание?"
        show screen blktone
        with d3
        $herView.hideshowQQ( "body_120.png", pos )
        play music "music/Chipper Doodle v2.mp3" fadein 1 fadeout 1 # HERMIONE'S THEME.
        her "Да, сэр, выполнила."
        $herView.hideshowQQ( "body_186.png", pos )
        her "И из всех мест я выбрала библиотеку..."
        her "Поначалу, я немного беспокоилась, что мы будем слишком сильно шуметь..."
        her "Но он не продержался и минуты, сэр."
        m "Не вини его."
        m "Ты достаточно привлекательная, возможно, он просто перевозбудился..."
        $herView.hideshowQQ( "body_120.png", pos )
        her "И все же..."
        her "Парочка осторожных толчков и он уже кончает?"
        her "Как девушка, я не могу не чувствовать разочарования..."
        m "Ясно..."
        m "Что ты сделала потом?"
        m "Натянула трусики и пошла по своим делам, как будто ничего и не было?"
        $herView.hideshowQQ( "body_87.png", pos )
        her "Трусики?"
        $herView.hideshowQQ( "body_69.png", pos )
        her "Я больше не ношу их, сэр."
        m "Ох, правда?"
        $herView.hideshowQQ( "body_79.png", pos )
        her "Да... Я считаю, что если не одевать нижнее белье, то это укрепляет твой дух."
        m "Рад за вас, мисс Грейнджер."
        
        
    elif one_out_of_three == 3: ### EVENT (C)
        label returns_next_morning:
            pass
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
            
        m "Мисс Грейнджер, вы выполнили задание?"
        $herView.hideshowQQ( "body_120.png", pos )
        play music "music/(Orchestral) Playful Tension by Shadow16nh.mp3" fadein 1 fadeout 1 # SEX THEME.
        her "Да, сэр."
        $herView.hideshowQQ( "body_124.png", pos )
        her "Я отвела одного из парней с \"Когтеврана\" в женскую уборную..."
        her "...и дала ему в одной из кабинок."
        m "Отлично, девочка."
        $herView.hideshowQQ( "body_69.png", pos )
        her "....................."
        m "Я сказал, что ты хорошо справилась. В чем дело?"
        $herView.hideshowQQ( "body_189.png", pos )
        her "Эм... ну..."
        her "Мне хорошо платят за выполнение таких заданий..."
        her "Так что я не имею права жаловаться, но..."
        m "Хм...?"
        $herView.hideshowQQ( "body_183.png", pos )
        her "Но моя репутация начинает страдать и это беспокоит меня, сэр..."
        m "Твоя репутация?"
        $herView.hideshowQQ( "body_189.png", pos )
        her "Ну, да... эм..."
        m ".............."

#        label test:
        menu:
            "Разбирайся сама":
                m "Ну, ты взрослая девочка, или тебе нужны няньки, которые будут заботиться о твоей репутации?"
                $ end.SetEndingValue(const_ENDING_STRONG_GIRL,3)
            "Просто будь осторожнее":
                m "Просто будь осторожнее."
#        m ".............."
        $herView.hideshowQQ( "body_120.png", pos )
        her "Да, вы правы, сэр."
        her "Извините, забудьте о том, что я только что сказала, сэр."
        m "Хм..."
#        jump your_whore




    



    $ gryffindor += 75 #75
    m "75 очков \"Гриффиндору\"!"
    her "Спасибо, сэр."
    
    hide screen bld1
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


    
    $ request_30_points += 1 
    $ request_30 = False 
    $ hermione_sleeping = True
    
    call music_block
    
    $event.Finalize()    
    return

    
    
    
   
   
   
   ####
   
label new_request_30_complete_a: #Hermione does not show up. This is label where she shows up next morning.
    $ request_30_a = False #Turns True when hermione fails to show up after her "Fuck a classmate" favour. Runs an event next morning.
    
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
            
    play music "music/Chipper Doodle v2.mp3" fadein 1 fadeout 1 # HERMIONE'S THEME.
    m "Мисс Грейнджер, вчера вы прогуляли свой отчет."
    $herView.hideQQ()

    $ pos = POS_370

    $herView.showQQ( "body_16.png", pos )
    her "Да, извините, сэр, мне жаль... *зевает*..."
    m "Вы не желаете объясниться?"
    $herView.hideshowQQ( "body_190.png", pos )
    her "Конечно, сэр."
    $herView.hideshowQQ( "body_188.png", pos )
    her "Хотя мне немного неловко..."
    $herView.hideshowQQ( "body_190.png", pos )
    her "Я провела прошлую ночь со своими друзьями..."
    m "Девичник с подружками, хах?"
    $herView.hideshowQQ( "body_122.png", pos )
    her "Подружками?"
    $herView.hideshowQQ( "body_189.png", pos )
    her "Нет, сэр. Гарри и Рон - парни..."
    m "Хм..."
    $herView.hideshowQQ( "body_188.png", pos )
    her "Да, мы долгое время были лучшими друзьями..."
    $herView.hideshowQQ( "body_128.png", pos )
    play music "music/(Orchestral) Playful Tension by Shadow16nh.mp3" fadein 1 fadeout 1 # SEX THEME.
    her "Но прошлой ночью мальчики сделали меня своей маленькой игрушкой..."
    $herView.hideshowQQ( "body_123.png", pos )
    her "И я ничуть не возражала..."
    her "Они делали со мной все, что хотели..."
    her "И все, что я хотела, чтобы было сделано со мной, тоже исполнилось..."
    $herView.hideshowQQ( "body_121.png", pos )
    her "................."
    $herView.hideshowQQ( "body_122.png", pos )
    her "Мне за это заплатят, сэр?"
    
    $ gryffindor += 75 #75
    m "75 очков\"Гриффиндору\"!"
    her "Спасибо, сэр."
    
    hide screen bld1
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


    
    $ request_30_points += 1 
    $ request_30 = False 
    $ hermione_takes_classes = True
    
    call music_block 
    
    $event.Finalize()    
    return

  


