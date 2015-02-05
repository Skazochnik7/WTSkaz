label giving_skirt:
    $ dress_code = True # Turns TRUE when you gift the miniskirt. Unlocks the "dress code" button.
    $ gifted = True #Prevents you from giving Hermione a several gifts in a row. Turns back to False every night and every morning.
    $ have_miniskirt = False # Turns TRUE when you have the skirt in your possession.
    $ gave_miniskirt = True #Turns True when Hermione has the miniskirt.
    $ days_without_an_event = 0
    $herView.hideQ( d5 )
    
    
    $ mad = 0
    m "Вот... Это тебе..."
    $ the_gift = "03_hp/18_store/07.png" # Miniskirt.
    show screen gift
    with d3
    $ renpy.play('sounds/win2.mp3')
    ">Вы дали школьную мини-юбку Гермионе..."
    hide screen gift
    with d3
    $herView.hideQQ()
    $ pos = POS_140
    $herView.showQQ( "body_01.png", pos )
    her "Хм...? Что это?"
    $herView.hideshowQQ( "body_11.png", pos )
    her "Юбка?"
    $herView.hideshowQQ( "body_06.png", pos )
    her "Спасибо, профессор."
    m "Не стоит благодарности."
    $herView.hideQQ()
    $ renpy.play('sounds/win_04.mp3')   #Not loud.
    show screen notes
    #">\"Dresscode\" option unlocked. From now on you can affect Hermione's attire choices."
    $ pos = POS_370
    $herView.showQ( "body_01.png", pos )
    jump day_time_requests
    
    
    
### DRESS CODE ###
label mini_on:
    $pos = POS_370
    if whoring >= 0 and whoring <= 5: # Lv 1-2.
        $herView.hideshowQQ( "body_04.png", pos )
        her "Вы же не всерьез, сэр?!"
        her "Это мини юбка?!"
        $herView.hideshowQQ( "body_79.png", pos )
        her "...Она едва прикрывает мои прелести."
        menu:
            m "..."
            "\"Ладно. Забудь.\"":
                $herView.hideshowQQ( "body_66.png", pos )
                her "С удовольствием..."
                $herView.hideQQ()
                #_#with d3            
                $herView.showQQ( None, pos )
                jump day_time_requests
            "\"Я дам тебе 15 очков.\"":
                $ gryffindor +=15
                her "........................"
                her "..............................."
                $herView.hideshowQQ( "body_66.png", pos )
                her "Ну, ладно..."
                $herView.hideQQ()
                $ mad += 10
                call upset
        
        

    if whoring >= 6 and whoring <= 11: # Lv 3-4.
        $herView.hideshowQQ( "body_15.png", pos )
        her "Хм...?"
        $herView.hideshowQQ( "body_17.png", pos )
        her "Но она очень короткая..."
        menu:
            m "..."
            "\"Просто надень её!\"":
                $herView.hideshowQQ( "body_07.png", pos )
                her "Сэр, врядли это соответствует форме учеников Хогвартса."
                $herView.hideshowQQ( "body_09.png", pos )
                her "Я отказываюсь!"
                $herView.hideQQ()
                $ mad += 5
                call upset                                                                                                                                                                                                                #HERMIONE
                $herView.showQQ( None, pos )
                jump day_time_requests
            "\"Я дам тебе 15 очков.\"":
                $ gryffindor +=15
                $herView.hideshowQQ( "body_07.png", pos )
                her "Хм..."
                $herView.hideshowQQ( "body_08.png", pos )
                her "Ну, в таком случае..."
                $herView.hideshowQQ( "body_29.png", pos )
                her "Пока это приносит пользу моему факультету..."
            "\"Ладно. Забудь.\"":
                $herView.hideshowQQ( "body_01.png", pos )
                her "Ладно..."
                $herView.hideshowQQ( None, pos )
                jump day_time_requests

    if whoring >= 12 and whoring <= 17: # Lv 5-6.
        $herView.hideshowQQ( "body_15.png", pos )
        her "Хм...?"
        $herView.hideshowQQ( "body_17.png", pos )
        her "Но она очень короткая..."
        menu:
            m "..."
            "\"Просто надень ее!\"":
                $herView.hideshowQQ( "body_69.png", pos )
                her "Ладно, ладно..."
            "\"Я дам тебе 15 очков.\"":
                $ gryffindor +=15
                $herView.hideshowQQ( "body_07.png", pos )
                her "Хм..."
                $herView.hideshowQQ( "body_68.png", pos )
                her "Ладно, я не против."
            "\"Ладно. Забудь\"":
                $herView.hideshowQQ( "body_13.png", pos )
                her "Ох..."
                $herView.hideshowQQ( None, pos )
                jump day_time_requests
        


    
    if whoring >= 18: # Lv 7+
        $herView.hideshowQQ( "body_118.png", pos )
        her "Слушаюсь, сэр..."
        $herView.hideQQ()
        $herView.addFaceName( "body_78.png", pos )
                                                                                                                                                                                                                          #HERMIONE
    
    
    $ herView.data().addSkirt( CharacterExItem( herView.mClothesFolder, "skirt_short.png", G_Z_SKIRT ) )
    
    show screen blkfade
    with d3
    $ renpy.play('sounds/door.mp3') #Sound of a door opening.
    pause 2
    $ renpy.play('sounds/door.mp3') #Sound of a door opening.
    pause.3
    hide screen blkfade
    with d3
                                                                                                                                                                                                                     #HERMIONE
    $herView.showQQ( None, pos )
    jump day_time_requests
    
    
label mini_off:
    $ pos = POS_370
    if whoring >= 0 and whoring <= 5: # Lv 1-2.
        $herView.hideshowQQ( "body_04.png", pos )
        her "Я рада, что вы попросили меня об этом. "
        $herView.hideQQ()
        $herView.addFaceName( "body_03.png")
        
    if whoring >= 6 and whoring <= 11: # Lv 3-4.
        $herView.hideshowQQ( "body_01.png", pos )
        her "С удовольствием, сэр."

    if whoring >= 12 and whoring <= 17: # Lv 5-6.
        $herView.hideshowQQ( "body_13.png", pos )
        her "Хорошо..."
    
    if whoring >= 18: # Lv 7+
        $herView.hideshowQQ( "body_28.png", pos )
        her "Опять эта скукотища?"
    
    
    $ herView.data().addSkirt( CharacterExItem( herView.mClothesFolder, "skirt_normal.png", G_Z_SKIRT ) )
    
    show screen blkfade
    with d3
    $ renpy.play('sounds/door.mp3') #Sound of a door opening.
    pause 2
    $ renpy.play('sounds/door.mp3') #Sound of a door opening.
    pause.3
    hide screen blkfade
    with d3
    jump day_time_requests
   
    
    
label badge_put:
    $herView.hideQQ()

    $ pos = POS_370
    $herView.showQQ( "body_01.png", pos )
    her "Конечно, сэр..."
    
    $ herView.data().addItem( G_N_BADGE, CharacterExItem( herView.mClothesFolder, "badge.png", G_Z_DRESS + 1, 'dress' ) )
    
    show screen blkfade
    with d3
    $ renpy.play('sounds/door.mp3') #Sound of a door opening.
    pause 2
    $ renpy.play('sounds/door.mp3') #Sound of a door opening.
    pause.3
    hide screen blkfade
    with d3
    jump day_time_requests
    
    
label badge_take:
    $herView.hideQQ()
    
    $ pos = POS_370
    $herView.showQQ( "body_01.png", pos )
    her "Как пожелаете, сэр..."

    $ herView.data().delItem( G_N_BADGE )
    
    show screen blkfade
    with d3
    $ renpy.play('sounds/door.mp3') #Sound of a door opening.
    pause 2
    $ renpy.play('sounds/door.mp3') #Sound of a door opening.
    pause.3
    hide screen blkfade
    with d3
    jump day_time_requests
    
    
### FISHNETS ###
label nets_put:
    $ pos = POS_370
    if whoring >= 0 and whoring <= 5: # Lv 1-2.
        $herView.hideshowQQ( "body_11.png", pos )
        her "Ажурные чулки...?"
        $herView.hideshowQQ( "body_31.png", pos )
        her "Вы, должно быть, не серьезно, сэр!"
        menu:
            m "..."
            "\"Ладно. Забудь.\"":
                $herView.hideshowQQ( "body_69.png", pos )
                her "С радостью..."
                $herView.hideshowQQ( None, pos )
                jump day_time_requests
            "\"Я дам тебе 15 очков.\"":
                $ gryffindor +=15
                her "........................"
                her "..............................."
                $herView.hideshowQQ( "body_66.png", pos )
                her "Ну, хорошо..."
                $herView.hideQQ()
                $ mad += 5
                call upset
        
    if whoring >= 6 and whoring <= 11: # Lv 3-4.
        $herView.hideshowQQ( "body_15.png", pos )
        her "Хм...?"
        $herView.hideshowQQ( "body_17.png", pos )
        her "Я не из таких девушек, сэр..."
        her "Попытайте удачу с одной из \"Слизеринских\" шлюх..."
        menu:
            m "..."
            "\"Просто надень это!\"":
                $herView.hideshowQQ( "body_07.png", pos )
                her "Сэр, это врядли соответствует форме студента Хогвартса."
                $herView.hideshowQQ( "body_09.png", pos )
                her "Я отказываюсь!"
                $herView.hideQQ()
                $ mad += 5
                call upset                                                                                                                                                                                                                #HERMIONE
                $herView.showQQ( None, pos )
                jump day_time_requests
            "\"Я дам тебе 15 очков.\"":
                $ gryffindor +=15
                $herView.hideshowQQ( "body_07.png", pos )
                her "Хм..."
                $herView.hideshowQQ( "body_08.png", pos )
                her "Ну, раз так..."
                $herView.hideshowQQ( "body_29.png", pos )
                her "Пока это приносит пользу моему факультету..."
            "\"Ладно. Забудь\"":
                $herView.hideshowQQ( "body_01.png", pos )
                her "Ладно..."
                $herView.hideshowQQ( None, pos )
                jump day_time_requests

    if whoring >= 12 and whoring <= 17: # Lv 5-6.
        $herView.hideshowQQ( "body_15.png", pos )
        her "Хм...?"
        $herView.hideshowQQ( "body_17.png", pos )
        her "Ажурные чулки?"
        $herView.hideshowQQ( "body_29.png", pos )
        her "Я не уверена насчет этого, сэр..."
        menu:
            m "..."
            "\"Просто надень их!\"":
                $herView.hideshowQQ( "body_69.png", pos )
                her "Ладно, Ладно..."
            "\"Я дам тебе 15 очков.\"":
                $ gryffindor +=15
                $herView.hideshowQQ( "body_07.png", pos )
                her "Хм..."
                $herView.hideshowQQ( "body_68.png", pos )
                her "Ладно, я не против."
            "\"Ладно. Забудь\"":
                $herView.hideshowQQ( "body_13.png", pos )
                her "Ох..."
                $herView.hideshowQQ( None, pos )
                jump day_time_requests
        

    
    if whoring >= 18: # Lv 7+
        $herView.hideshowQQ( "body_118.png", pos )
        her "Если вы настаиваете, сэр..."
        $herView.hideQQ()
        $herView.addFaceName( "body_78.png" )
                                                                                                                                                                                                                          #HERMIONE
    
     
    $ herView.data().addItem( G_N_NETS, CharacterExItem( herView.mClothesFolder, "nets.png", G_Z_LEGS + 1, 'legs' ) )
    
    #$ legs_02 = True
    
    show screen blkfade
    with d3
    $ renpy.play('sounds/door.mp3') #Sound of a door opening.
    pause 2
    $ renpy.play('sounds/door.mp3') #Sound of a door opening.
    pause.3
    hide screen blkfade
    with d3
    pause.1
    $herView.showQQ( None, pos )
    jump day_time_requests
    
    
label nets_take:
    $ pos = POS_370
    if whoring >= 0 and whoring <= 5: # Lv 1-2.
        $herView.hideshowQQ( "body_04.png", pos )
        her "Я рада, что вы приняли это решение, сэр."
        $herView.hideQQ()
        $herView.addFaceName( "body_03.png" )
        
    if whoring >= 6 and whoring <= 11: # Lv 3-4.
        $herView.hideshowQQ( "body_01.png", pos )
        her "С удовольствием, сэр."

    if whoring >= 12 and whoring <= 17: # Lv 5-6.
        $herView.hideshowQQ( "body_12.png", pos )
        her "Как пожелаете, сэр."
    
    if whoring >= 18: # Lv 7+
        $herView.hideshowQQ( "body_28.png", pos )
        her "Правда? Ой..."
    
    
    $ herView.data().delItem( G_N_NETS )
    #$ legs_02 = False
    
    show screen blkfade
    with d3
    $ renpy.play('sounds/door.mp3') #Sound of a door opening.
    pause 2
    $ renpy.play('sounds/door.mp3') #Sound of a door opening.
    pause.3
    hide screen blkfade
    with d3
    $herView.showQQ( None, pos )
    jump day_time_requests
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
       
label giving_lube: # JAR OF Анальный лубрикант.
    $herView.hideQ( d5 )                                                                                                                                                                                                           #HERMIONE
    $ pos = POS_140
    
    if whoring >= 0 and whoring <= 5: # Lv 1-2.
        $ mad += 6
        $herView.showQ( "body_02.png", pos, d5 )                                                                                                                                                                                         #HERMIONE
        her "Я не знаю, что это..."
        $herView.hideshowQQ( "body_05.png", pos )
        her "Но мне кажется, что эта банка полна чего-то мерзкого и противного..."
        her "Нет, спасибо, сэр."
        $herView.hideQQ()
        call upset #Message saying that Hermione became upset with you.
        $herView.addFaceName( "body_03.png" )
       
        
        
    if whoring >= 6 and whoring <= 11: # Lv 3-4.
        $ mad += 2
        $herView.showQ( "body_73.png", pos, d5 )                                                                                                                                                                                                                      #HERMIONE
        her "Хм..."
        $herView.hideshowQQ( "body_66.png", pos )
        her "Мне кажется, я знаю, что это такое..."
        her "Но почему вы даете что-то вроде этого одному из ваших учеников, сэр?"
        $herView.hideshowQQ( "body_69.png", pos )
        her "Нет, спасибо."
        $herView.hideQQ()
        call upset #Message saying that Hermione became upset with you.
   
        
    if whoring >= 12 and whoring <= 17: # Lv 5-6.
        $ anal_lube -= 1
        $herView.showQ( "body_118.png", pos, d5 )
        her "Анальный лубрикант?"
        $herView.hideshowQQ( "body_189.png", pos )
        her "Эм...ну...я знаю девочку..."
        her "То есть, не знаю, она подруга моей подруги..."
        her "Да, я передам это ей..."
        $herView.hideQQ()
        $ the_gift = "03_hp/18_store/09.png" # Анальный лубрикант
        show screen gift
        with d3
        ">Вы даете банку Гермионе..."
        hide screen gift
        with d3
        $herView.hideshowQQ( "body_186.png", pos )
        her "Тем не менее, я думаю, вы не должны дарить такие подарки вашим ученикам, сэр."
        $herView.hideQQ()
        call no_change #Message: Hermione's mood did not change.
        $herView.addFaceName( "body_79.png ");
        
    if whoring >= 18: # Lv 7+  
        $ anal_lube -= 1
        $ mad -=5
        $herView.showQ( "body_124.png", pos, d5 )
        her "Анальный лубрикант, сэр?"
        $herView.hideshowQQ( "body_186.png", pos )
        her "Я знаю пару девушек, которые могли бы сделать что-нибудь с этим."
        $herView.hideshowQQ( "body_128.png", pos )
        her "Спасибо, что присматриваете за нами, сэр."
        $herView.hideQQ()
        call happy #Message that says that Hermione's mood has improved.
 
    $ pos = POS_370
    $herView.showQQ( None, pos )    
    jump day_time_requests
        
        
        
        
label giving_condoms: # A PACK OF CONDOMS
    $herView.hideQ( d5 )
    $ pos = POS_140
    
    if whoring >= 0 and whoring <= 5: # Lv 1-2.
        $ mad += 6
        $herView.showQ( "body_18.png", pos, d5 )
        her "Презервативы?!"
        $herView.hideshowQQ( "body_30.png", pos )
        her "Сэр, я даже не знаю, что с этим делать..."
        $herView.hideQQ()
        call upset #Message saying that Hermione became upset with you.
        $herView.addFaceName( "body_03.png" )
        
        
    if whoring >= 6 and whoring <= 11: # Lv 3-4.
        $herView.showQ( "body_07.png", pos, d5 )
        her "...Презервативы?"
        $herView.hideshowQQ( "body_04.png", pos )
        her "Эм... Является ли это частью какой-то новой обучающей программы Хогвартса? Вроде сексуального развитие или вроде того?"
        $herView.hideshowQQ( "body_189.png", pos )
        her "Нет, сэр ... Мне кажется, что неправильно принимать этот подарок от вас..."
        $herView.hideQQ()
        call no_change 
   
        
    if whoring >= 12 and whoring <= 17: # Lv 5-6.
        $ condoms -= 1
        $ mad -= 3
        $herView.showQ( "body_03.png", pos, d5 )
        her "Пачка презервативов?"
        her "Сэр, как мне использовать их?"
        $herView.hideshowQQ( "body_04.png", pos )
        her "Ну, я приму их, только потому, что невежливо отказываться от подарка..."
        $herView.hideQQ()
        $ the_gift = "03_hp/18_store/10.png" # CONDOMS
        show screen gift
        with d3
        ">Вы даете Гермионе пачку презервативов..."
        hide screen gift
        with d3
        call happy #Message that says that Hermione's mood has improved.
        $herView.addFaceName( "body_29.png" )
        

        
    if whoring >= 18: # Lv 7+  
        $ anal_lube -= 1
        $ mad -=4
        $herView.showQ( "body_08.png", pos, d5 )
        her "Пачка презервативов?"
        $herView.hideshowQQ( "body_128.png", pos )
        her "Я ценю вашу заботу, сэр. Спасибо."
        $herView.hideQQ()
        $ the_gift = "03_hp/18_store/10.png" # CONDOMS
        show screen gift
        with d3
        ">Вы даете пачку презервативов Гермионе..."
        hide screen gift
        with d3
        call happy #Message that says that Hermione's mood has improved.
        $herView.addFaceName( "body_45.png" )
 
    $ pos = POS_370
    $herView.showQQ( None, pos )
    jump day_time_requests
        
        
     
     
     
### CANDY ###
label giving_candy: # CANDY.
    $herView.hideQ( d5 )
    $ pos = POS_140
    
    if whoring >= 0 and whoring <= 5: # Lv 1-2.
        $ mad -= 5
        $ candy -= 1
        $herView.showQ( "body_01.png", pos, d5 )
        her "Конфета?"
        $herView.hideQQ()
        $ the_gift = "03_hp/18_store/11.png" # CANDY
        show screen gift
        with d3
        ">Вы даете конфету Гермионе..."
        hide screen gift
        with d3
        $herView.showQQ( "body_06.png", pos )
        her "Спасибо, сэр."
        call happy #Message that says that Hermione's mood has improved.

    if whoring >= 6 and whoring <= 11: # Lv 3-4.
        $ mad -= 5
        $ candy -= 1
        $herView.showQ( "body_03.png", pos, d5 )
        her "Конфета?"
        $herView.hideshowQQ( "body_02.png", pos )
        her "Конфеты для детей, сэр."
        $herView.hideQQ()
        $ the_gift = "03_hp/18_store/11.png" # CANDY
        show screen gift
        with d3
        ">Вы даете конфету Гермионе..."
        hide screen gift
        with d3
        $herView.showQQ( "body_29.png", pos )
        her "Спасибо вам..."
        call happy #Message that says that Hermione's mood has improved.
        $herView.addFaceName( "body_06.png" )
        

        
    if whoring >= 12 and whoring <= 17: # Lv 5-6.
        $ mad -= 5
        $ candy -= 1
        $herView.showQ( "body_03.png", pos, d5 )
        her "Конфета?"
        $herView.hideQQ()
        $ the_gift = "03_hp/18_store/11.png" # CANDY
        show screen gift
        with d3
        ">Вы даете конфету Гермионе..."
        hide screen gift
        with d3
        $herView.showQQ( "body_08.png", pos )
        her "Eм... Конечно, спасибо..."
        call happy #Message that says that Hermione's mood has improved.
        $herView.addFaceName( "body_06.png" )
        
    if whoring >= 18: # Lv 7+  
        $ candy -= 1
        $ mad -=5
        $herView.showQ( "body_06.png", pos, d5 )
        her "Конфета?"
        $herView.hideshowQQ( "body_46.png", pos )
        her "Умные девушки используют конфеты как \"игрушку\"."
        $herView.hideQQ()
        $ the_gift = "03_hp/18_store/11.png" # CANDY
        show screen gift
        with d3
        ">Вы даете конфету Гермионе..."
        hide screen gift
        with d3
        $herView.showQQ( "body_74.png", pos )
        her "Спасибо, сэр."
        call happy #Message that says that Hermione's mood has improved.
        $herView.addFaceName( "body_128.png" )
 
    $ pos = POS_370
    $herView.showQQ( None, pos )
    jump day_time_requests
    
        
        
        

### CHOCOLATE ###
label giving_chocolate: # CHOCOLATE.
    $herView.hideQ( d5 )
    $ pos = POS_140
    
    if whoring >= 0 and whoring <= 5: # Lv 1-2.
        $ mad -= 10
        $ chocolate -= 1
        $herView.showQ( "body_01.png", pos, d5 )
        her "Плитка шоколада?"
        $herView.hideQQ()
        $ the_gift = "03_hp/18_store/12.png" # CHOCOLATE
        show screen gift
        with d3
        ">Вы даете Гермионе плитку шоколада..."
        hide screen gift
        with d3
        $herView.showQQ( "body_06.png", pos )
        her "Спасибо, сэр."
        call happy #Message that says that Hermione's mood has improved.

    if whoring >= 6 and whoring <= 11: # Lv 3-4.
        $ mad -= 10
        $ chocolate -= 1
        $herView.showQ( "body_03.png", pos, d5 )
        her "Плитка шоколада?"
        $herView.hideshowQQ( "body_09.png", pos )
        her "Хм..."
        her "Тут что-то о феях..."
        $herView.hideshowQQ( "body_11.png", pos )
        her "Это шутка какая-то, не так ли?"
        $herView.hideQQ()
        $ the_gift = "03_hp/18_store/12.png" # CHOCOLATE
        show screen gift
        with d3
        ">Вы даете Гермионе плитку шоколада..."
        hide screen gift
        with d3
        $herView.showQQ( "body_15.png", pos )
        her "Спасибо вам..."
        call happy #Message that says that Hermione's mood has improved.
        

        
    if whoring >= 12 and whoring <= 17: # Lv 5-6.
        $ mad -= 10
        $ chocolate -= 1
        $herView.showQ( "body_03.png", pos, d5 )
        her "Плитка шоколада?"
        $herView.hideshowQQ( "body_24.png", pos )
        her "Мне просто нравится как она хрустит, сэр! Н-не вкус..."
        $herView.hideQQ()
        $ the_gift = "03_hp/18_store/12.png" # CHOCOLATE
        show screen gift
        with d3
        ">Вы даете Гермионе плитку шоколада..."
        hide screen gift
        with d3
        $herView.showQQ( "body_01.png", pos )
        her "Эм... Конечно, спасибо..."
        call happy #Message that says that Hermione's mood has improved.
       
 
        
    if whoring >= 18: # Lv 7+  
        $ chocolate -= 1
        $ mad -= 10
        $herView.showQ( "body_06.png", pos, d5 )
        her "Плитка шоколада?"
        $herView.hideshowQQ( "body_111.png", pos )
        her "Вы балуете меня, сэр."
        $herView.hideQQ()
        $ the_gift = "03_hp/18_store/12.png" # CHOCOLATE
        show screen gift
        with d3
        ">Вы даете Гермионе плитку шоколада..."
        hide screen gift
        with d3
        $herView.showQQ( "body_129.png", pos )
        her "Спасибо вам."
        call happy #Message that says that Hermione's mood has improved.
        
 
    $ pos = POS_370
    $herView.showQQ( None, pos )
    jump day_time_requests
        

    ### VIBRATOR ###
label giving_vibrator: # VIBRATOR.
    $herView.hideQ( d5 )
    $ pos = POS_140
    
    if whoring >= 0 and whoring <= 5: # Lv 1-2.
        $ mad+= 10
        $herView.showQ( "body_01.png", pos, d5 )
        her "Магическая палочка?"
        $herView.hideshowQQ( "body_15.png", pos )
        her "Нет, выглядит как--"
        her ".........?"
        $herView.hideshowQQ( "body_18.png", pos )
        her "!!!"
        $herView.hideshowQQ( "body_187.png", pos )
        her "Профессор Дамблдор!"
        $herView.hideshowQQ( "body_30.png", pos )
        her "Это неуместно!"
        call upset
        $herView.addFaceName( "body_120.png" )
    
    if whoring >= 6 and whoring <= 11: # Lv 3-4.
        $ mad += 10
        $herView.showQ( "body_118.png", pos, d5 )
        her "Это то, что я думаю?"
        $herView.hideshowQQ( "body_186.png", pos )
        her "Сэр, позвольте напомнить вам о том, что я принадлежу факультету \"Гриффиндор\"."
        $herView.hideshowQQ( "body_120.png", pos )
        her "Этот подарок подходит для \"Слизеринских\" шлюх, сэр."
        call upset

    if whoring >= 12 and whoring <= 17: # Lv 5-6.
        $ vibrator -= 1
        $herView.showQ( "body_118.png", pos, d5 )
        her "Это...вибратор?"
        her "Дизайн..."
        her "Он напоминает мне мою палочку..."
        $herView.hideshowQQ( "body_118.png", pos )
        her "Это сделано на заказ для меня?"
        $herView.hideshowQQ( "body_30.png", pos )
        her "Это неуместно."
        $herView.hideshowQQ( "body_29.png", pos )
        her "Но, тем не менее..."
        $herView.hideQQ()
        $ the_gift = "03_hp/18_store/13.png" # VIBRATOR
        show screen gift
        with d3
        ">Вы даете вибратор Гермионе..."
        hide screen gift
        with d3
        call no_change
        

    if whoring >= 18: # Lv 7+  
        $ vibrator -= 1
        $ mad -= 10
        $herView.showQ( "body_11.png", pos, d5 )
        her "Это вибратор..."
        $herView.hideshowQQ( "body_10.png", pos )
        her "Это... вызывает во мне..."
        $herView.hideshowQQ( "body_66.png", pos )
        her "Грязные мысли, сэр"
        $herView.hideQQ()
        $ the_gift = "03_hp/18_store/13.png" # VIBRATOR
        show screen gift
        with d3
        ">Вы даете вибратор Гермионе..."
        hide screen gift
        with d3
        $herView.showQQ( "body_124.png", pos )
        her "Спасибо, сэр."
        $herView.hideQQ()
        call happy #Message that says that Hermione's mood has improved.
        
 
    $ pos = POS_370
    $herView.showQQ( None, pos )
    jump day_time_requests
        
        
        
        
        
        
        
        
        
        
            
            
            
            
            
        ### STRAP-ON ###
label giving_strapon: # STRAP-ON.
    $herView.hideQ( d5 )
    $ pos = POS_140
    if whoring >= 0 and whoring <= 5: # Lv 1-2.
        $ mad -= 20
        $ strapon -= 1
        $herView.showQ( "body_18.png", pos, d5 )
        her "Что это?"
        $herView.hideshowQQ( "body_14.png", pos )
        her "Какой-то артефакт?"
        $herView.hideshowQQ( "body_01.png", pos )
        her "Так хорошо продуман..."
        $herView.hideshowQQ( "body_06.png", pos )
        her "Вы уверены, что мне стоит обладать этим?"
        $herView.hideQQ()
        $ the_gift = "03_hp/18_store/14.png" # STRAP-ON
        show screen gift
        with d3
        ">Вы даете страпон Гермионе..."
        hide screen gift
        with d3
        $herView.showQQ( "body_16.png", pos )
        her "Огромное спасибо, сэр. Я обещаю хорошо обращаться с ним."
        $herView.hideQQ()
        call happy
        $herView.addFaceName( "body_15.png" )
    
    
    if whoring >= 6 and whoring <= 11: # Lv 3-4.
        $ mad += 15
        $herView.showQ( "body_18.png", pos, d5 )
        her "!!!"
        $herView.hideshowQQ( "body_118.png", pos )
        her "Это..."
        her "Оно не выглядит... по человечески..."
        $herView.hideshowQQ( "body_69.png", pos )
        her "То есть..."
        $herView.hideshowQQ( "body_86.png", pos )
        her "Сэр, вам не стыдно?!"
        her "Дарить что-то вроде этого ученику?!"
        $herView.hideshowQQ( "body_87.png", pos )
        her ".................."
        $herView.hideshowQQ( "body_47.png", pos )
        her "Пожалуйста, уберите это."
        $herView.hideQQ()
        call upset

    if whoring >= 12 and whoring <= 17: # Lv 5-6.
        $ strapon -= 1
        $ mad -= 10
        $herView.showQ( "body_118.png", pos, d5 )
        her "Эта штука..."
        $herView.hideshowQQ( "body_117.png", pos )
        her "Это нормальный размер...для \"этого\"?"
        $herView.hideshowQQ( "body_189.png", pos )
        her "Я имею в виду..."
        $herView.hideshowQQ( "body_118.png", pos )
        her "......................."
        $herView.hideshowQQ( "body_117.png", pos )
        her "Это реквизит для какого-то розыгрыша?"
        $herView.hideshowQQ( "body_118.png", pos )
        her "Оно неплохо сделано "
        $herView.hideshowQQ( "body_33.png", pos )
        her "Я возьму его..."
        $herView.hideQQ()
        $ the_gift = "03_hp/18_store/14.png" # STRAP-ON
        show screen gift
        with d3
        ">Вы даете страпон Гермионе..."
        hide screen gift
        with d3
        call happy


    if whoring >= 18: # Lv 7+  
        $ strapon -= 1
        $ mad -= 30
        $herView.showQ( "body_48.png", pos, d5 )
        her "Это... Это великолепно, сэр..."
        $herView.hideshowQQ( "body_189.png", pos )
        her "Он смоделирован по тому самому Фестралу?"
        $herView.hideshowQQ( "body_190.png", pos )
        her "Но эти существа невидимы..."
        $herView.hideshowQQ( "body_118.png", pos )
        her ".................."
        $herView.hideshowQQ( "body_123.png", pos )
        her "Захватывающе..."
        $herView.hideshowQQ( "body_120.png", pos )
        her "Все не так, как вы могли подумать, сэр..."
        $herView.hideshowQQ( "body_127.png", pos )
        her "Я просто любуюсь мастерством..."
        $herView.hideQQ()
        $ the_gift = "03_hp/18_store/14.png" # STRAP-ON
        show screen gift
        with d3
        ">Вы даете страпон Гермионе..."
        hide screen gift
        with d3
        $herView.showQQ( "body_129.png", pos )
        her "Спасибо вам за подарок, сэр."
        $herView.hideQQ()
        call happy

 
    $ pos = POS_370
    $herView.showQQ( None, pos )
    jump day_time_requests
        
        
        
        
        
   
        ### BALL GAG ###
label giving_ballgag: # BALL GAG.
    $herView.hideQ( d5 )
    $ pos = POS_140
        
    if whoring >= 0 and whoring <= 5: # Lv 1-2.
        $ mad += 10
        $herView.showQ( "body_118.png", pos, d5 )
        her "Что это?"
        $herView.hideshowQQ( "body_141.png", pos )
        her "Выглядит как одна из игрушек для взрослых?"
        $herView.hideshowQQ( "body_30.png", pos )
        her "Какая женщина в здравом уме будет подвергать себя такому унижению?"
        $herView.hideshowQQ( "body_186.png", pos )
        her "И что мне с этим сделать?"
        $herView.hideshowQQ( "body_187.png", pos )
        her "Это очень обидно, сэр..."                                                                                                                                                                                                              
        call upset

    if whoring >= 6 and whoring <= 11: # Lv 3-4.
        $ mad += 5
        $herView.showQ( "body_186.png", pos, d5 )
        her "Сэр, вы не понимаете, насколько неправильно было бы для меня принять от вас такой подарок?"
        $herView.hideshowQQ( "body_189.png", pos )
        her "И ведь я даже не представляю, что с этим делать..."
        $herView.hideshowQQ( "body_118.png", pos )
        her "То есть, эти пушистые наручники, это просто..."
        her "И этот круглый кляп... Эм..."
        $herView.hideshowQQ( "body_120.png", pos )
        her "Сэр, пожалуйста..."
        her "Просто уберите это."
        call upset


    if whoring >= 12 and whoring <= 17: # Lv 5-6.
        $ ballgag -= 1
        $ mad -= 9
        $herView.showQ( "body_120.png", pos, d5 )
        her "Месяц назад я бы чувствовала себя оскорбленной, если бы получила такой подарок..."
        $herView.hideshowQQ( "body_118.png", pos )
        her "Но теперь я знаю, что некоторые девушки получают удовольствие от такого..."
        $herView.hideshowQQ( "body_117.png", pos )
        $herView.hideshowQQ( "body_120.png", pos )
        her "Уверяю вас, я не одна из таких, сэр."
        $herView.hideshowQQ( "body_189.png", pos )
        her "Но я знаю девушку, которая знает девушку, которая в таких вещах, как ..."
        $herView.hideshowQQ( "body_188.png", pos )
        her "Да, я возьму это и отдам ей..."
        $herView.hideQQ()
        $ the_gift = "03_hp/18_store/15.png" # BALL GAG.
        show screen gift
        with d3
        ">Вы даете кляп и наручники Гермионе..."
        hide screen gift
        with d3
        call happy

    if whoring >= 18: # Lv 7+  
        $ ballgag -= 1
        $ mad -= 15
        $herView.showQ( "body_190.png", pos, d5 )
        her "Кляп и наручники?"
        $herView.hideshowQQ( "body_122.png", pos )
        her "Это совершенно неуместно, сэр." # :)
        $herView.hideshowQQ( "body_129.png", pos )
        her "Но, подарок это подарок, так?"
        $herView.hideQQ()
        $ the_gift = "03_hp/18_store/15.png" # BALL GAG.
        show screen gift
        with d3
        ">Вы даете кляп и наручники Гермионе..."
        hide screen gift
        with d3
        call happy
        

 
    $ pos = POS_370
    $herView.showQQ( None, pos )
    jump day_time_requests
        
        
        
        
        
        
        
        
        
        
        
        
        
  
      ### ANAL PLUGS ###
label giving_plug: 
    $herView.hideQ( d5 )
    $ pos = POS_140

    if whoring >= 0 and whoring <= 5: # Lv 1-2.
        $ mad -= 8
        $ plug -= 1
        $herView.showQ( "body_01.png", pos, d5 )
        her "Хм...?"
        $herView.hideshowQQ( "body_15.png", pos )
        her "Это что-то вроде затычек?"
        $herView.hideQQ()
        $ the_gift = "03_hp/18_store/16.png" # ANAL PLUG.
        show screen gift
        with d3
        ">Вы даете Гермионе анальную пробку..."
        hide screen gift
        with d3
        $herView.hideshowQQ( "body_185.png", pos )
        her "Спасибо, сэр."
        call happy


    if whoring >= 6 and whoring <= 11: # Lv 3-4.
        $ mad -= 15
        $herView.showQ( "body_186.png", pos, d5 )
        her "Сэр, это какие-то игрушки для взрослых?"
        $herView.hideshowQQ( "body_187.png", pos )
        her "Это что-то из штук для анального секса?"
        her "Сэр, я считаю, что это одно из оружий для угнетения и унижения женщин!"
        $herView.hideshowQQ( "body_120.png", pos )
        her "Козел!"
        call upset

        
    if whoring >= 12 and whoring <= 17: # Lv 5-6.
        $herView.showQ( "body_120.png", pos, d5 )
        her "Да, я знаю девочку, которая..."
        $herView.hideshowQQ( "body_186.png", pos )
        her "Пользуется чем-то подобным..."
        her "Но не я, сэр."
        $herView.hideshowQQ( "body_120.png", pos )
        her "Нет. Спасибо."
        call no_change

    if whoring >= 18: # Lv 7+  
        $ plug -= 1
        $ mad -= 10
        $herView.showQ( "body_118.png", pos, d5 )
        her "Анальная пробка?"
        $herView.hideshowQQ( "body_117.png", pos )
        her "Я не пользуюсь таким..."
        $herView.hideshowQQ( "body_122.png", pos )
        her "Хотя она очень красива..."
        $herView.hideshowQQ( "body_118.png", pos )
        her "....................."
        $herView.hideshowQQ( "body_121.png", pos )
        her "Ну, ладно. Я возьму ее, если вы настаиваете."
        $herView.hideQQ()
        $ the_gift = "03_hp/18_store/16.png" # ANAL PLUGS.
        show screen gift
        with d3
        ">Вы даете Гермионе анальную пробку..."
        hide screen gift
        with d3
        $herView.showQQ( "body_127.png", pos )
        her "Но, конечно же, никогда не воспользуюсь..."
        $herView.hideshowQQ( "body_124.png", pos )
        her "................"
        call happy
        

 
    $ pos = POS_370
    $herView.showQQ( None, pos )
    jump day_time_requests
        
        
        
        
        
        
        
          ### EDUCATIONAL MAGAZINES ###
label giving_mag1: 
    $herView.hideQ( d5 )
    $ pos = POS_140
    
    if whoring >= 0 and whoring <= 5: # Lv 1-2.
        $ mad -= 15
        $ mag1 -= 1
        $herView.showQ( "body_01.png", pos, d5 )
        her "\"Популярные магические\" журналы?"
        $herView.hideQQ()
        $ the_gift = "03_hp/18_store/17.png" # EDUCATIONAL MAGAZIES.
        show screen gift
        with d3
        ">Вы даете несколько обучающих журналов Гермионе..."
        hide screen gift
        with d3
        $herView.showQQ( "body_06.png", pos )
        her "Спасибо, сэр!"
        her "Я использую их для своих исследований!"
        call happy

    if whoring >= 6 and whoring <= 11: # Lv 3-4.
        $ mad -= 10
        $ mag1 -= 1
        $herView.showQ( "body_01.png", pos, d5 )
        her "Временами я ищу в журналах информацию, которую не могу найти в книгах..."
        $herView.hideQQ()
        $ the_gift = "03_hp/18_store/17.png" # EDUCATIONAL MAGAZIES.
        show screen gift
        with d3
        ">Вы даете несколько обучающих журналов Гермионе..."
        hide screen gift
        with d3
        $herView.showQQ( "body_06.png", pos )
        her "Спасибо, сэр!"
        her "Я использую их для своих исследований!"
        call happy

    if whoring >= 12 and whoring <= 17: # Lv 5-6.
        $ mad -= 3 
        $ mag1 -= 1
        $herView.showQ( "body_02.png", pos, d5 )
        her "Ох..."
        $herView.hideshowQQ( "body_06.png", pos )
        her "Да, я читаю как можно больше журналов..."
        $herView.hideshowQQ( "body_10.png", pos )
        her "Особенно много в последнее время..."
        $herView.hideQQ()
        $ the_gift = "03_hp/18_store/17.png" # EDUCATIONAL MAGAZIES.
        show screen gift
        with d3
        ">Вы даете несколько обучающих журналов Гермионе..."
        hide screen gift
        with d3
        $herView.showQQ( "body_06.png", pos )
        her "Спасибо, сэр!"
        call happy
     

    if whoring >= 18: # Lv 7+  
        $ mag1 -= 1
        $herView.showQ( "body_10.png", pos, d5 )
        her "Эм..."
        $herView.hideshowQQ( "body_08.png", pos )
        her "Если быть честной, журналы уже не особо привлекают меня..."
        $herView.hideshowQQ( "body_11.png", pos )
        her "Но я не против принять их от вас."
        $herView.hideQQ()
        $ the_gift = "03_hp/18_store/17.png" # EDUCATIONAL MAGAZIES.
        show screen gift
        with d3
        ">Вы даете несколько обучающих журналов Гермионе..."
        hide screen gift
        with d3
        $herView.showQQ( "body_13.png", pos )
        her "Спасибо вам."
        call no_change 

 
    $ pos = POS_370
    $herView.showQQ( d3 )
    jump day_time_requests    
        
        
        
        
        
              ### GIRLY MAGAZINES ###
label giving_mag2: 
    $herView.hideQ( d5 )
    $ pos = POS_140

    if whoring >= 0 and whoring <= 5: # Lv 1-2.
        $herView.showQ( "body_15.png", pos, d5 )
        her "Хм?"
        $herView.hideshowQQ( "body_17.png", pos )
        her "Это какие-то журналы для \"слизеринских\" девок, я полагаю."
        $herView.hideshowQQ( "body_16.png", pos )
        her "Я выше, этих глупых журналов, сэр."
        call no_change
        $herView.addFaceName( "body_01.png" )
        
        
      
    if whoring >= 6 and whoring <= 11: # Lv 3-4.
        $ mad -= 5
        $ mag2 -= 1
        $herView.showQ( "body_04.png", pos, d5 )
        her "Я не читаю журналы такого рода..."
        $herView.hideshowQQ( "body_13.png", pos )
        her "................"
        $herView.hideshowQQ( "body_04.png", pos )
        her "Но я могу попробовать, просто смеха ради..."
        $herView.hideQQ()
        $ the_gift = "03_hp/18_store/18.png" # GIRLY MAGAZIES.
        show screen gift
        with d3
        ">Вы даете женские журналы Гермионе..."
        hide screen gift
        with d3
        $herView.showQQ( "body_08.png", pos )
        her "Спасибо, сэр!"
        call happy
        $herView.addFaceName( "body_06.png" )

    if whoring >= 12 and whoring <= 17: # Lv 5-6.
        $ mad -= 15 
        $ mag2 -= 1
        $herView.showQ( "body_10.png", pos, d5 )
        her "Мне стыдно признаваться, но..."
        $herView.hideshowQQ( "body_24.png", pos )
        her "Последнее время мне действительно нравится читать подобное..."
        $herView.hideQQ()
        $ the_gift = "03_hp/18_store/18.png" # GIRLY MAGAZIES.
        show screen gift
        with d3
        ">Вы даете женские журналы Гермионе..."
        hide screen gift
        with d3
        $herView.showQQ( "body_08.png", pos )
        her "Спасибо, сэр."
        call happy
        $herView.addFaceName( "body_06.png" )
        

    if whoring >= 18: # Lv 7+  
        $ mag2 -= 1
        $ mad -= 15
        $herView.showQ( "body_18.png", pos, d5 )
        her "Последний выпуск \"Девченок\"?!"
        $herView.hideshowQQ( "body_24.png", pos )
        her "Нет ничего лучше этого журнала!"
        $herView.hideQQ()
        $ the_gift = "03_hp/18_store/18.png" # GIRLY MAGAZIES.
        show screen gift
        with d3
        ">Вы даете женские журналы Гермионе..."
        hide screen gift
        with d3
        $herView.showQQ( "body_08.png", pos )
        her "Спасибо, сэр."
        call happy
        $herView.addFaceName( "body_06.png" )

 
    $ pos = POS_370
    $herView.showQQ( None, pos )
    jump day_time_requests        
        
        
        
                  ### Журналы для взрослых ###
label giving_mag3: 
    $herView.hideQ( d5 )
    $ pos = POS_140

    if whoring >= 0 and whoring <= 5: # Lv 1-2.
        $ mad += 7
        $herView.showQ( "body_02.png", pos, d5 )
        her "Это...?"
        $herView.hideshowQQ( "body_31.png", pos )
        her "Журналы для взрослых, сэр?"
        $herView.hideshowQQ( "body_69.png", pos )
        her "Учитывая ваш высокий статус?"
        $herView.hideshowQQ( "body_66.png", pos )
        her "Сэр, неужели вы не нашли более продуктивный способ провести свое время?"
        $herView.hideshowQQ( "body_47.png", pos )
        her "Я определенно не стану брать их..."
        call upset
        

    if whoring >= 6 and whoring <= 11: # Lv 3-4.
        $ mad += 3
        $herView.showQ( "body_05.png", pos, d5 )
        her "Журналы для взрослых?"
        $herView.hideshowQQ( "body_69.png", pos )
        her "Сэр, мне не интересно подобное."
        $herView.hideshowQQ( "body_47.png", pos )
        her "И это не очень уместный подарок для одного из ваших студентов."
        call upset
        $herView.addFaceName( "body_29.png" )


    if whoring >= 12 and whoring <= 17: # Lv 5-6.
        $ mad -= 8 
        $ mag3 -= 1
        $herView.showQ( "body_31.png", pos, d5 )
        her "Журналы для взрослых?"
        $herView.hideshowQQ( "body_34.png", pos )
        her "Сэр, мне кажется это не подходящий подарок для девушки моего возраста..."
        $herView.hideQQ()
        $ the_gift = "03_hp/18_store/19.png" # ADULT MAGAZIES.
        show screen gift
        with d3
        ">Вы даете Гермионе несколько журналов для взрослых..."
        hide screen gift
        with d3
        $herView.showQQ( "body_79.png", pos )
        her "Я уберу их подальше..."
        call happy
        $herView.addFaceName( "body_120.png" ) 


    if whoring >= 18: # Lv 7+  
        $ mag3 -= 1
        $ mad -= 15
        $herView.showQ( "body_75.png", pos, d5 )
        her "Новый выпуск \"Л.ю.б.в.и.\"!!!"
        $herView.hideshowQQ( "body_122.png", pos )
        her "Э-э...я имела в виду - \"Журналы для взрослых?\""
        her "Это слегка опрометчиво..."
        $herView.hideshowQQ( "body_74.png", pos )
        her "Но я возьму их..."
        $herView.hideQQ()
        $ the_gift = "03_hp/18_store/19.png" # ADULT MAGAZIES.
        show screen gift
        with d3
        ">Вы даете Гермионе несколько журналов для взрослых..."
        hide screen gift
        with d3
        $herView.showQQ( "body_74.png", pos )
        her "Спасибо, сэр."
        call happy
       

 
    $ pos = POS_370
    $herView.showQQ( None, pos )
    jump day_time_requests            
        
        
        
        
        
                      ### PORN MAGAZINES ###
label giving_mag4: 
    $herView.hideQ( d5 )
    $ pos = POS_140
    
    if whoring >= 0 and whoring <= 5: # Lv 1-2.
        $ mad += 15
        $herView.showQ( "body_01.png", pos, d5 )                                                                                                                                                                                       #HERMIONE
        her "Хм... Что это?"
        $herView.hideshowQQ( "body_130.png", pos )
        her "Сэр, это порно журналы!"
        $herView.hideshowQQ( "body_187.png", pos )
        her "Вам должно быть стыдно!"
        call upset
        


    if whoring >= 6 and whoring <= 11: # Lv 3-4.
        $ mad += 8
        $herView.showQ( "body_48.png", pos, d5 )
        her "Порно журналы?"
        $herView.hideshowQQ( "body_87.png", pos )
        her "Сэр, что мне с ними делать?"
        $herView.hideshowQQ( "body_79.png", pos )
        her "Исследовать их?"
        $herView.hideshowQQ( "body_86.png", pos )
        her "Козел!"
        call upset
        $herView.addFaceName( "body_120.png" )
        

    if whoring >= 12 and whoring <= 17: # Lv 5-6.
        $ mag4 -= 1
        $herView.showQ( "body_31.png", pos, d5 )
        her "Это жесткое порно."
        $herView.hideshowQQ( "body_34.png", pos )
        her "Не очень подходящий подарок для девушки моих лет!"
        $herView.hideshowQQ( "body_118.png", pos )
        her ".............."
        $herView.hideshowQQ( "body_117.png", pos )
        her "Но я возьму..."
        $herView.hideQQ()
        $ the_gift = "03_hp/18_store/20.png" # PORN MAGAZIES.
        show screen gift
        with d3
        ">Вы даете Гермионе несколько порно-журналов..."
        hide screen gift
        with d3
        $herView.showQQ( "body_79.png", pos )
        her "И я выброшу их в мусорное ведро, где они и должны быть... как и девушки, которые любят такие вещи..."
        call no_change
        $herView.addFaceName( "body_120.png" )

    if whoring >= 18: # Lv 7+  
        $ mag4 -= 1
        $ mad -= 15
        $herView.showQ( "body_48.png", pos, d5 )
        her "Порнография?"
        $herView.hideshowQQ( "body_118.png", pos )
        her "................"
        $herView.hideshowQQ( "body_117.png", pos )
        her "Как женщины вообще могут такое делать?"
        $herView.hideshowQQ( "body_118.png", pos )
        her "................."
        $herView.hideshowQQ( "body_120.png", pos )
        her "Ладно, я возьму их..."
        $herView.hideshowQQ( "body_189.png", pos )
        her "Исключительно для научных целей, конечно же..."
        $herView.hideQQ()
        $ the_gift = "03_hp/18_store/20.png" # PORN MAGAZIES.
        show screen gift
        with d3
        ">Вы даете Гермионе несколько порно-журналов..."
        hide screen gift
        with d3
        call happy
        $herView.addFaceName( "body_45.png" )

 
    $ pos = POS_370
    $herView.showQQ( None, pos )
    jump day_time_requests                
        
        
        
        
           
                      ### BUTTERBEER ###
label giving_beer: 
    $herView.hideQ( d5 )
    $ pos = POS_140
    
    if whoring >= 0 and whoring <= 5: # Lv 1-2.
        $ beer -= 1
        $ mad -= 3
        $herView.showQ( "body_01.png", pos, d5 )
        her "Сливочное пиво?"
        $herView.hideshowQQ( "body_08.png", pos )
        her "Вы уверены насчет этого?"
        $herView.hideshowQQ( "body_06.png", pos )
        her "Оно содержит алкоголь..."
        $herView.hideQQ()
        $ the_gift = "03_hp/18_store/21.png" # BUTTERBEER.
        show screen gift
        with d3
        ">Вы даете бутылку Гермионе..."
        hide screen gift
        with d3
        $herView.showQQ( "body_01.png", pos )
        her "Спасибо вам."
        call happy
        


    if whoring >= 6 and whoring <= 11: # Lv 3-4.
        $ mad -= 10
        $ beer -= 1
        $herView.showQ( "body_11.png", pos, d5 )
        her "Сливочное пиво, сэр?"
        $herView.hideQQ()
        
        $herView.showQQ( "body_14.png", pos )
        her "Это будет наш маленький секрет..."
        $herView.hideshowQQ( "body_06.png", pos )
        her "Я большая поклонница этого безвредного напитка."
        $herView.hideQQ()
        $ the_gift = "03_hp/18_store/21.png" # BUTTERBEER.
        show screen gift
        with d3
        ">Вы даете бутылку Гермионе..."
        hide screen gift
        with d3
        $herView.showQQ( "body_01.png", pos )
        her "Спасибо, сэр."
        call happy
        

        

    if whoring >= 12 and whoring <= 17: # Lv 5-6.
        $ mad -= 15
        $ beer -= 1
        $herView.showQ( "body_01.png", pos, d5 )
        her "Сливочное пиво?"
        $herView.hideshowQQ( "body_24.png", pos )
        her "Спасибо, сэр."
        $herView.hideQQ()
        $ the_gift = "03_hp/18_store/21.png" # BUTTERBEER.
        show screen gift
        with d3
        ">Вы даете бутылку Гермионе..."
        hide screen gift
        with d3
        $herView.showQQ( "body_06.png", pos )
        her "Я выпью ее с девочками несколько позднее."
        call happy
        

    if whoring >= 18: # Lv 7+  
        $ mad -= 20
        $ beer -= 1
        $herView.showQ( "body_06.png", pos, d5 )
        her "Сливочное пиво...?"
        $herView.hideshowQQ( "body_01.png", pos )
        her "Спасибо, сэр."
        $herView.hideQQ()
        $ the_gift = "03_hp/18_store/21.png" # BUTTERBEER.
        show screen gift
        with d3
        ">Вы даете бутылку Гермионе..."
        hide screen gift
        with d3
        $herView.showQQ( "body_06.png", pos )
        her "Я выпью ее с мальчишками несколько позднее."
        $herView.hideshowQQ( "body_189.png", pos )
        her "Э-э... Я хотела сказать с девочками, да."
        call happy
        $herView.addFaceName( "body_01.png" )

 
    $ pos = POS_370
    $herView.showQQ( None, pos )
    jump day_time_requests                
            
        
        
        
        
        
                   ### PLUSH OWL ###
label giving_owl: 
    $herView.hideQ( d5 )

    $ pos = POS_140

    if whoring >= 0 and whoring <= 5: # Lv 1-2.
        $ owl -= 1
        $ mad -= 7
        $herView.showQ( "body_01.png", pos, d5 )
        her "Плюшевая сова?"
        $herView.hideshowQQ( "body_06.png", pos )
        her "Так мило..."
        $herView.hideQQ()
        $ the_gift = "03_hp/18_store/22.png" # PLUSH OWL.
        show screen gift
        with d3
        ">Вы даете Гермионе плюшевую сову..."
        hide screen gift
        with d3
        $herView.showQQ( "body_01.png", pos )
        her "Спасибо, сэр."
        call happy
        
      

    if whoring >= 6 and whoring <= 11: # Lv 3-4.
        $ mad -= 10
        $ owl -= 1
        $herView.showQ( "body_11.png", pos, d5 )
        her "Плюшевая сова?"
        $herView.hideshowQQ( "body_06.png", pos )
        her "Мне нравится!"
        $herView.hideQQ()
        $ the_gift = "03_hp/18_store/22.png" # PLUSH OWL.
        show screen gift
        with d3
        ">Вы даете Гермионе плюшевую сову..."
        hide screen gift
        with d3
        $herView.showQQ( "body_01.png", pos )
        her "Спасибо, сэр."
        call happy

    if whoring >= 12 and whoring <= 17: # Lv 5-6.
        $ mad -= 15
        $ owl -= 1
        $herView.showQ( "body_01.png", pos, d5 )
        her "Игрушка?"
        $herView.hideshowQQ( "body_02.png", pos )
        her "Игрушки для детей, сэр."
        $herView.hideshowQQ( "body_29.png", pos )
        her "Но я возьму..."
        $herView.hideQQ()
        $ the_gift = "03_hp/18_store/22.png" # PLUSH OWL.
        show screen gift
        with d3
        ">Вы даете Гермионе плюшевую сову..."
        hide screen gift
        with d3
        $herView.showQQ( "body_01.png", pos )
        her "Спасибо, сэр."
        call happy
        
        
        
      
    if whoring >= 18: # Lv 7+  
        $ mad -= 4
        $ owl -= 1
        $herView.showQ( "body_66.png", pos, d5 )
        her "Это что-то из игрушек для взрослых?"
        $herView.hideshowQQ( "body_87.png", pos )
        her "Где-то есть переключатель или кнопка..."
        $herView.hideshowQQ( "body_124.png", pos )
        her "И ...оно вибрирует или как?"
        $herView.hideshowQQ( "body_190.png", pos )
        her "Ох...?"
        her "Так это действительно просто плюшевая сова?"
        $herView.hideshowQQ( "body_118.png", pos )
        her "Кошмар..."
        $herView.hideshowQQ( "body_34.png", pos )
        her "То есть, спасибо, сэр."
        $herView.hideQQ()
        $ the_gift = "03_hp/18_store/22.png" # PLUSH OWL.
        show screen gift
        with d3
        ">Вы даете Гермионе плюшевую сову..."
        hide screen gift
        with d3
        $herView.addFaceName( "body_01.png" )
        call happy

    $ pos = POS_370
    $herView.showQQ( None, pos )
    jump day_time_requests                
    
    
    
        
     ### SEX DOLL ###
label giving_sexdoll: 
    $herView.hideQ( d5 )
   
    $ pos = POS_140
    
    if whoring >= 0 and whoring <= 5: # Lv 1-2.
        $ mad += 20
        $herView.showQ( "body_48.png", pos, d5 )
        her "Это..."
        $herView.hideshowQQ( "body_34.png", pos )
        her "Секс-кукла?!"
        $herView.hideshowQQ( "body_32.png", pos )
        her "Профессор Дамблдор!!!"
        call upset
        $herView.addFaceName( "body_33.png" )

    if whoring >= 6 and whoring <= 11: # Lv 3-4.
        $ mad += 20
        $herView.showQ( "body_48.png", pos, d5 )
        her "Секс-кукла?"
        $herView.hideshowQQ( "body_120.png", pos )
        her "Это очень неприлично, для такого как вы..."
        call upset

    if whoring >= 12 and whoring <= 17: # Lv 5-6.
        $ mad -= 10
        $ sexdoll -= 1
        $herView.showQ( "body_118.png", pos, d5 )
        her "Секс-кукла..."
        $herView.hideshowQQ( "body_120.png", pos )
        her "Это немного неуместно..."
        $herView.hideshowQQ( "body_124.png", pos )
        her "Но может мы сможем использовать ее для розыгрышей или вроде того..."
        $herView.hideQQ()
        $ the_gift = "03_hp/18_store/23.png" # SEX DOLL.
        show screen gift
        with d3
        ">Вы даете Гермионе секс-куклу..."
        hide screen gift
        with d3
        $herView.showQQ( "body_124.png", pos )
        her "Спасибо, сэр."
        call happy
        
    if whoring >= 18: # Lv 7+  
        $ mad -= 30
        $ sexdoll -= 1
        $herView.showQ( "body_73.png", pos, d5 )
        her "Секс-кукла Джуанна?"
        $herView.hideshowQQ( "body_189.png", pos )
        her "Я не сказала бы, что одобряю подобное..."
        $herView.hideshowQQ( "body_124.png", pos )
        her "Но знаю, что Гарри хотел бы такую..."
        $herView.hideQQ()
        $ the_gift = "03_hp/18_store/23.png" # SEX DOLL.
        show screen gift
        with d3
        ">Вы даете Гермионе секс-куклу..."
        hide screen gift
        with d3
        $herView.showQQ( "body_188.png", pos )
        her "Спасибо, сэр."
        call happy
        

        
    $ pos = POS_370
    $herView.showQQ( None, pos )
    jump day_time_requests                
        
        
      ### SEXY LINGERIE ###
label giving_lingerie: 
    $herView.hideQ( d5 )

    $ pos = POS_140

    if whoring >= 0 and whoring <= 5: # Lv 1-2.
        $ mad += 10
        $herView.showQ( "body_118.png", pos, d5 )
        her "Нижнее белье?"
        $herView.hideshowQQ( "body_120.png", pos )
        her "Сэр, я не могу принять от вас такой подарок.."
        call upset
       
      

    if whoring >= 6 and whoring <= 11: # Lv 3-4.
        $herView.showQ( "body_118.png", pos, d5 )
        her "Сексуальное нижнее белье?"
        $herView.hideshowQQ( "body_117.png", pos )
        her "Вы ведь знаете, что я не могу принять этот подарок."
        $herView.hideshowQQ( "body_118.png", pos )
        her "(Хотя оно довольно милое)........."
        call no_change

    if whoring >= 12 and whoring <= 17: # Lv 5-6.
        $ mad -= 7
        $ lingerie -= 1
        $herView.showQ( "body_124.png", pos, d5 )
        her "Сексуальное нижнее белье?"
        $herView.hideshowQQ( "body_122.png", pos )
        her "Сэр, это несколько неуместно..."
        $herView.hideQQ()
        $ the_gift = "03_hp/18_store/24.png" # SEXY LINGERIE.
        show screen gift
        with d3
        ">Вы даете Гермионе сексуальное нижнее белье..."
        hide screen gift
        with d3
        $herView.showQQ( "body_188.png", pos )
        her "Спасибо, сэр."
        call happy

        
    if whoring >= 18: # Lv 7+  
        $ mad -= 15
        $ lingerie -= 1
        $herView.showQ( "body_124.png", pos, d5 )
        her "Сексуальное нижнее белье?"
        $herView.hideshowQQ( "body_123.png", pos )
        her "Как вам кажется, я могу стать похожей на одну из ведьм из тех журналов для взрослых?"
        $herView.hideshowQQ( "body_122.png", pos )
        her "Ох... То есть, спасибо, сэр."
        $herView.hideQQ()
        $ the_gift = "03_hp/18_store/24.png" # SEXY LINGERIE.
        show screen gift
        with d3
        ">Вы даете Гермионе сексуальное нижнее белье..."
        hide screen gift
        with d3
        call happy
        

    $ pos = POS_370
    $herView.showQQ( None, pos )
    jump day_time_requests                
        
    ### BROOM ###
label giving_broom: 
    $herView.hideQ( d5 )
    
    $ pos = POS_140

    if whoring >= 0 and whoring <= 5: # Lv 1-2.
        $ mad -= 20
        $ broom -= 1
        $herView.showQ( "body_01.png", pos, d5 )
        her "Метла...?"
        $herView.hideshowQQ( "body_03.png", pos )
        her "Хм..."
        $herView.hideshowQQ( "body_07.png", pos )
        her "Что это за странные штуки на ней?"
        $herView.hideshowQQ( "body_08.png", pos )
        her "Выглядит как седло...?"
        $herView.hideQQ()
        $ the_gift = "03_hp/18_store/25.png" # BROOM
        show screen gift
        with d3
        ">Вы даете метлу Гермионе..."
        hide screen gift
        with d3
        $herView.showQQ( "body_11.png", pos )
        her "Спасибо вам за подарок, сэр."
        $herView.addFaceName( "body_06.png" )
        call happy
       
      

    if whoring >= 6 and whoring <= 11: # Lv 3-4.
        $ mad -= 20
        $ broom -= 1
        $herView.showQ( "body_01.png", pos, d5 )
        her "Метла...?"
        $herView.hideshowQQ( "body_07.png", pos )
        her "Хм..."
        $herView.hideshowQQ( "body_05.png", pos )
        her "Это какая-то секс-игрушка, не так ли?"
        $herView.hideshowQQ( "body_87.png", pos )
        her "Ну, неплохо сделано..."
        $herView.hideQQ()
        $ the_gift = "03_hp/18_store/25.png" # BROOM
        show screen gift
        with d3
        ">Вы даете метлу Гермионе..."
        hide screen gift
        with d3
        $herView.showQQ( "body_120.png", pos )
        her "Спасибо, сэр."
        call happy
        
        
    if whoring >= 12 and whoring <= 17: # Lv 5-6.
        $ mad -= 30
        $ broom -= 1
        $herView.showQ( "body_118.png", pos, d5 )
        her "Метла...?"
        her "Хм..."
        $herView.hideshowQQ( "body_66.png", pos )
        her "Что это за седло...?"
        $herView.hideshowQQ( "body_127.png", pos )
        her "Ну, не важно."
        her "Отказываться от дорогого подарка было бы глупо..."
        $herView.hideQQ()
        $ the_gift = "03_hp/18_store/25.png" # BROOM
        show screen gift
        with d3
        ">Вы даете метлу Гермионе..."
        hide screen gift
        with d3
        $herView.showQQ( "body_120.png", pos )
        her "Спасибо, сэр."
        call happy

    if whoring >= 18: # Lv 7+  
        $ mad -= 30
        $ broom -= 1
        $herView.showQ( "body_124.png", pos, d5 )
        her "Метла..."
        her "Хм..."
        $herView.hideshowQQ( "body_189.png", pos )
        her "Это седло, сэр..."
        $herView.hideshowQQ( "body_190.png", pos )
        her "Оно было разработано специально для меня, не так ли?"
        $herView.hideshowQQ( "body_185.png", pos )
        her "Я не уверена, неуместно это или разумно..."
        $herView.hideshowQQ( "body_129.png", pos )
        her "Но это идеальное инженерное решение..."
        $herView.hideQQ()
        $ the_gift = "03_hp/18_store/25.png" # BROOM
        show screen gift
        with d3
        ">Вы даете метлу Гермионе..."
        hide screen gift
        with d3
        $herView.showQQ( "body_128.png", pos )
        her "Спасибо, сэр."
        call happy


    $ pos = POS_370
    $herView.showQQ( None, pos )
    jump day_time_requests                
        
    ### KRUM POSTER ###
label giving_krum: 
    $herView.hideQ( d5 )
    $ pos = POS_140
    
    if whoring >= 0 and whoring <= 5: # Lv 1-2.
        $herView.showQ( "body_73.png", pos, d5 )
        her "Постер Квиддича?"
        $herView.hideshowQQ( "body_185.png", pos )
        her "Что мне с ним делать, сэр?"
        $herView.hideshowQQ( "body_184.png", pos )
        her "Нет, спасибо."
        call no_change
        $herView.addFaceName( "body_71.png" )


    if whoring >= 6 and whoring <= 11: # Lv 3-4.
        $ mad -= 1
        $ krum -= 1
        $herView.showQ( "body_73.png", pos, d5 )
        her "Постер по Квиддичу?"
        $herView.hideshowQQ( "body_185.png", pos )
        her "Хм..."
        $herView.hideshowQQ( "body_71.png", pos )
        her "Мне кажется, я видела этого игрока пару раз..."
        $herView.hideshowQQ( "body_06.png", pos )
        her "Это тот студент из Дурмштранга?"
        $herView.hideQQ()
        $ the_gift = "03_hp/18_store/26.png" # KRUM POSTER.
        show screen gift
        with d3
        ">Вы даете постер Гермионе..."
        hide screen gift
        with d3
        call happy
        

        
    if whoring >= 12 and whoring <= 17: # Lv 5-6.
        $ mad -= 15
        $ krum -= 1
        $herView.showQ( "body_73.png", pos, d5 )
        her "Постер Виктора Крама, сэр?"
        $herView.hideshowQQ( "body_08.png", pos )
        her "Ну, я немного интересуюсь квиддичем..."
        $herView.hideshowQQ( "body_87.png", pos )
        her "Не понять, что девушки находят в этих перекачанных парнях..."
        $herView.hideQQ()
        $ the_gift = "03_hp/18_store/26.png" # KRUM POSTER.
        show screen gift
        with d3
        ">Вы даете постер Гермионе..."
        hide screen gift
        with d3
        call happy
        
        
       
    if whoring >= 18: # Lv 7+  
        $ mad -= 25
        $ krum -= 1
        $herView.showQ( "body_72.png", pos, d5 )
        her "Постер Виктора Крама?!"
        $herView.hideshowQQ( "body_24.png", pos )
        her "Спасибо, сэр!"
        $herView.hideQQ()
        $ the_gift = "03_hp/18_store/26.png" # KRUM POSTER.
        show screen gift
        with d3
        ">Вы даете постер Гермионе..."
        hide screen gift
        with d3
        $herView.showQQ( "body_46.png", pos )
        her "Не могу дождаться, чтобы повесить его над своей кроватью!"
        $herView.hideshowQQ( "body_64.png", pos )
        her "Девченки обзавидуются..."
        call happy


    $ pos = POS_370
    jump day_time_requests                    
        
        
        
        
        
     ### S.P.E.W. BADGE ###
label giving_badge_01: 
    $herView.hideQ( d5 )

    $ pos = POS_140

    $ mad -= 30
    $ badge_01 = 7 # Means already gifted.
    $herView.showQ( "body_01.png", pos, d5 )
    her "Значок?"
    $herView.hideQQ()
    $ the_gift = "03_hp/18_store/29.png" # S.P.E.W. BADGE.
    show screen gift
    with d3
    ">Вы даете значок Гермионе...\n>Значок \"А.В.Н.Э.\" был добавлен в гардероб Гермионы."
    hide screen gift

    $ dress_code = True

    $herView.showQQ( "body_06.png", pos )
    her "Спасибо, сэр."
    call happy


    $ pos = POS_370
    $herView.showQQ( None, pos )
    jump day_time_requests                    
            
        
        
        
    ### Ажурные чулки ###
label giving_nets: 
    $herView.hideQ( d5 )

    $ pos = POS_140

    $ mad -= 30
    $ nets = 7 # Means already gifted.
    $herView.showQ( "body_03.png", pos, d5 )
    her "Пара чулков?"
    $herView.hideQQ()
    $ the_gift = "03_hp/18_store/30.png" # FISHNETS.
    show screen gift
    with d3
    ">Вы даете Гермионе пару чулков...\n>Ажурные чулки добавлены в ее гардероб."
    hide screen gift

    $ dress_code = True

    $herView.showQQ( "body_04.png", pos )
    her "Спасибо, сэр."
    call happy
    
    $herView.addFaceName( "body_03.png" )

    $ pos = POS_370
    $herView.showQQ( None, pos )
    jump day_time_requests                    
            
   
    
    
    
    
    
    
    
    
    
    
    
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
    label happy:
        $herView.hideQQ()
        if mad <= 0:
            $ mad = 0
        if mad == 0:
            ">Настроение Гермионы улучшено...\n>Гермиона {size=+5}не злится{/size} на вас..."
        else:
            ">Настроение Гермионы улучшено...\n>Гермиона {size=+5}огорчена вами{/size}..."
        return



    label no_change:
        $herView.hideQQ()
        ">Настроение Гермионы не изменилось..."
        return
        
    label upset:
        $herView.hideQQ()
        ">Настроение Гермионы ухудшилось...\n>Гермиона {size=+5}злится{/size} на вас..."
        return
        
        


