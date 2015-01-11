
###################REQUEST_20 (Level 05) (45 pt.) (MAKE OUT WITH A GIRL). (Available during daytime only). #####################################################################################
label new_request_20: #LV.5 (Whoring = 12 - 14)
    
        
        
    $herView.hideQQ()
    m "{size=-4}(Предложить ей пойти развлечься с одной из одноклассниц?){/size}"
    $ menu_x = 0.5 #Default position of the menu (0.5). Version B is $ menu_x = 0.2
    menu:
        "\"(Да, давай сделаем это!)\"":
            pass
        "\"(Не сейчас.)\"":
            jump new_personal_request
            
    
    $ pos = POS_140
    
    if request_20_points == 0: # <================================================================================ FIRST TIME
        m "Вы когда-нибудь целовали другую девушку, мисс Грейнджер?"
        $herView.hideQQ()
        $herView.showQQ( "body_07.png", pos )
        her "?!"
        
        if whoring <=11 or request_15_points <= 1: # Counts how many times you sent Hermione to flash a classmate.
            jump too_much
        play music "music/Chipper Doodle v2.mp3" fadein 1 fadeout 1 # HERMIONE'S THEME.
        $herView.hideQQ()
        $herView.showQQ( "body_02.png", pos )
        her "Я не... лесбиянка, сэр."
        m "Глупая девочка... Тебе не надо быть лесбиянкой, чтобы целовать девушек."
        m "Например, я регулярно занимаюсь этим, но я ведь не лесбиянка."
        $herView.hideQQ()
        $herView.showQQ( "body_05.png", pos )
        her "..............."
        her "Сэр--"
        m "Никаких \"сэров\"! Это твое задание на сегодня!"
        m "Найди какую-нибудь милашку и чмокни ее!"
        $herView.hideQQ()
        $herView.showQQ( "body_11.png", pos )
        her "Сэр, но я--"
        m "Свободны, мисс Грейнджер."
        $herView.hideQQ()
        $herView.showQQ( "body_07.png", pos )
        her "Сэр!......"
        m "Свободны, я сказал."
        $herView.hideQQ()
        $herView.showQQ( "body_09.png", pos )
        her "*Хм!*..."

    else: # <================================================================================ NOT FIRST TIME
        m "45 очков так и ждут, когда их заберут!"
        m "Интересуетесь, мисс Грейнджер?"
        if whoring >= 12 and whoring <= 14: # LEVEL 05 FIRST EVENT.
            play music "music/Chipper Doodle v2.mp3" fadein 1 fadeout 1 # HERMIONE'S THEME.
            $herView.hideQQ()
            $herView.showQQ( "body_03.png", pos )
            her "Это зависит от того..."
            her "Прийдется ли мне опять делать что-то развратное?"
            m "\"Развратное\"??! Когда это я--?"
            $herView.hideQQ()
            $herView.showQQ( "body_04.png", pos )
            her "Серьезно, сэр?"
            m "Ладно, ладно... Но все? что я хочу сегодня, так это чтобы ты немного развлеклась с другой девушкой."
            $herView.hideQQ()
            $herView.showQQ( "body_05.png", pos )
            her "Ох, и все?" # :(
            m "Да, ничего необычного для тебя, ведь так?"
            m "А вечером ты, конено же, получишь свои сорок пять очков."
            $herView.hideQQ()
            $herView.showQQ( "body_07.png", pos )
            her "............."
            m "...Ты согласна?"
            $herView.hideQQ()
            $herView.showQQ( "body_69.png", pos )
            her "Я посмотрю, что я смогу сделать, сэр..."
            m "Отлично. Тогда увидимся после занятий."
            $herView.hideQQ()
            $herView.showQQ( "body_79.png", pos )
            her "................"

        elif whoring >= 15 and whoring <= 17: # LEVEL 06. Event level 02.
            $herView.hideQQ()
            $herView.showQQ( "body_70.png", pos )
            her "Наверное..."
            m "Отлично. Все что мне нужно, так это чтобы ты немного развлеклась с другой девушкой."
            $herView.hideQQ()
            $herView.showQQ( "body_71.png", pos )
            her "Ясно..."
            m "Готовы выполнить задание, мисс Грейнджер?"
            $herView.hideQQ()
            $herView.showQQ( "body_29.png", pos )
            her "Наверное..."
            m "Отлично. Тогда увидимся после уроков."

            
        elif whoring >= 18: # LEVEL 07+ Event level 03.
            play music "music/Chipper Doodle v2.mp3" fadein 1 fadeout 1 # HERMIONE'S THEME.
            $herView.hideQQ()
            $herView.showQQ( "body_06.png", pos )
            her "Конечно, почему нет?"
            m "Отлично."
            m "Сегодня я хочу, чтобы ты немного поразвлекалась с другой девушкой."
            $herView.hideQQ()
            $herView.showQQ( "body_45.png", pos )
            her "Хорошо."
            $herView.hideQQ()
            $herView.showQQ( "body_64.png", pos )
            her "Я знаю парочку девченок, которые жаждут внимания и не будут возвражать против небольшого представления."
            m "Отлично. Тогда, встретимся после занятий."

    

    
    $ request_20 = True

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
    
    call music_block 
    
    jump day_main_menu
    
    

        

label new_request_20_complete: # <=================================================================================================== EVENING
    
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

    $ pos = POS_370

    $ request_20 = False 

    if whoring >= 12 and whoring <= 14: # LEVEL 05                    
        if one_out_of_three == 1: ### EVENT (A)
            stop music fadeout 1.0
            m "Мисс Грейнджер..."
            m "Вам удалось выполнить задание?"
            show screen blktone
            with d3
            $herView.hideQQ()
            $herView.showQQ( "body_11.png", pos )
            her "Я..."
            m "Я сказал тебе повеселиться с другой девушкой..."
            m "Ты сделала это?"
            $herView.hideQQ()
            $herView.showQQ( "body_10.png", pos )
            her "Я..."
            her "Я пыталась, сэр. Я правда пыталась."
            m "И?"
            $herView.hideQQ()
            $herView.showQQ( "body_29.png", pos )
            her "Ну..."
            play music "music/Chipper Doodle v2.mp3" fadein 1 fadeout 1 # HERMIONE'S THEME.
            her "Мне было стыдно и неловко..."
            m "Так ты это сделала, или нет?"
            $herView.hideQQ()
            $herView.showQQ( "body_69.png", pos )
            her "...нет, сэр..."
            her "Все, что я сделала - это выставила себя полной дурой..."
            $herView.hideQQ()
            $herView.showQQ( "body_47.png", pos )
            her "Перед всем классом..."
            m "Расскажи мне, что произошло, девочка."
            $herView.hideQQ()
            $herView.showQQ( "body_69.png", pos )
            her "Нет, не расскажу сэр."
            her "Ни за что на свете!"
            $herView.hideQQ()
            $herView.showQQ( "body_132.png", pos )
            her "Так или иначе, зачем мне надо было выполнять такое дурацкое задание?!"
            her "Какой во всем этом смысл?"
            $herView.hideQQ()
            $herView.showQQ( "body_30.png", pos )
            her "Я ненавижу его!"
            $herView.hideQQ()
            $herView.showQQ( "body_69.png", pos )
            her "..............."
            her "................."
            m ".............."
            m "Тебе не заплатят, ты знаешь об этом, так?"
            $herView.hideQQ()
            $herView.showQQ( "body_30.png", pos )
            her "Мне все равно..."
            $ mad +=25
            jump could_not_flirt #Sent here when choose "Favor failed! No points for you!" (Hermione is leaving without getting any points).
            
        elif one_out_of_three == 2: ### EVENT (B)
            play music "music/Chipper Doodle v2.mp3" fadein 1 fadeout 1 # HERMIONE'S THEME.
            m "Мисс Грейнджер, вы выполнили задание?"
            show screen blktone
            with d3
            $herView.hideQQ()
            $herView.showQQ( "body_16.png", pos )
            her "Выполнила, сэр..."
            m "Хорошо. Расскажи поподробнее."
            $herView.hideQQ()
            $herView.showQQ( "body_17.png", pos )
            her "Ну, я поцеловала девочку. Так, как вы мне и велели."
            m "Ты была смущена?"
            $herView.hideQQ()
            $herView.showQQ( "body_69.png", pos )
            her "Очень, сэр." # :( D: :D::D:D:D::D::D::D::DDD:DD
            m "Но тебе понравилось?"
            $herView.hideQQ()
            $herView.showQQ( "body_79.png", pos )
            her "*Хм!*..."
            m "Итак, вы поцеловали девушку и вам это понравилось?"
            $herView.hideQQ()
            $herView.showQQ( "body_66.png", pos )
            her "Да..."
            m "С языком?"
            $herView.hideQQ()
            $herView.showQQ( "body_66.png", pos )
            her "Да..."
            her "Это был настоящий поцелуй взасос, если вам интересно."
            her "Теперь я могу получить свою плату?"
            $herView.hideQQ()
            $herView.showQQ( "body_69.png", pos )
            her "Прошу, сэр..."
            m "Ладно, хорошо..."

        elif one_out_of_three == 3: ### EVENT (C)
            play music "music/Chipper Doodle v2.mp3" fadein 1 fadeout 1 # HERMIONE'S THEME.
            m "Мисс Грейнджер, вы выполнили задание?"
            show screen blktone
            with d3
            $herView.hideQQ()
            $herView.showQQ( "body_16.png", pos )
            her "Да, сэр, выполнила."
            m "Хорошо. Расскажи мне, как все прошло."
            $herView.hideQQ()
            $herView.showQQ( "body_16.png", pos )
            her "Все прошло хорошо, сэр."
            m "Превосходно. Расскажи мне детали."
            $herView.hideQQ()
            $herView.showQQ( "body_04.png", pos )
            her "Что бы вам хотелось узнать, сэр?"
            m "Расскажи мне все! Та девушка была симпатичной?"
            m "Она ответила на поцелуй?"
            $herView.hideQQ()
            $herView.showQQ( "body_08.png", pos )
            her "Она была относительно симпатичной, сэр."
            her "И она ответила на поцелуй..."
            $herView.hideQQ()
            $herView.showQQ( "body_184.png", pos )
            her "..........."
            $herView.hideQQ()
            $herView.showQQ( "body_08.png", pos )
            her "Что-то еще, сэр?"
            m "...."
            m "Почему с тобой так сложно?"
            $herView.hideQQ()
            $herView.showQQ( "body_04.png", pos )
            her "При всем уважении, сэр..."
            her "Вы сказали мне поцеловать другую девушку, и я поцеловала..."
            $herView.hideQQ()
            $herView.showQQ( "body_03.png", pos )
            her "Теперь, не могли бы вы быть так любезны заплатить мне?"
            m "......................"
            menu:
                "\"Мне не нравится ваш тон, леди.\"":
                    $herView.hideQQ()
                    $herView.showQQ( "body_04.png", pos )
                    her "Какая жалость, сэр."
                    m "Это точно..."
                    m "Потому что тебе никто ничего не заплатит, нахальная мелкая ведьма."
                    $herView.hideQQ()
                    $herView.showQQ( "body_03.png", pos )
                    stop music fadeout 1.0
                    her "Что?"
                    $herView.hideQQ()
                    $herView.showQQ( "body_11.png", pos )
                    her "Сэр, вы не можете так поступить!"
                    m "Свободны."
                    $herView.hideQQ()
                    $herView.showQQ( "body_10.png", pos )
                    her "Н-но--"
                    $herView.hideQQ()
                    $herView.showQQ( "body_11.png", pos )
                    her "Сэр, пожалуйста!"
                    her "Девушка была из \"Пуффендуя\", и--"
                    m "Поздно для этого, мисс Грейнджер."
                    m "Вы свободны."
                    $herView.hideQQ()
                    $herView.showQQ( "body_21.png", pos )
                    her "......"
                    $ mad +=25
                    jump could_not_flirt #Sent here when choose "Favor failed! No points for you!" (Hermione is leaving without getting any points).
                            
                "\"Ладно. Вот твоя плата.\"":
                    pass



    elif whoring >= 15 and whoring <= 17: # LEVEL 06. Event level 02.     
        if one_out_of_three == 1: ### EVENT (A)
            m "Мисс Грейнджер, вы выполнили задание?"
            show screen blktone
            with d3
            $herView.hideQQ()
            $herView.showQQ( "body_16.png", pos )
            her "Выполнила, сэр..."
            m "Тогда почему вы просто стоите и молчите? Рассказывайте."
            $herView.hideQQ()
            $herView.showQQ( "body_14.png", pos )
            her "Эм, ладно..."
            her "Та девочка была из\"Когтеврана\"..."
            $herView.hideQQ()
            $herView.showQQ( "body_13.png", pos )
            her "Я думаю, что она младшеклассница, но я не спрашивала..."
            her "Мы начали разговаривать о парнях..."
            $herView.hideQQ()
            $herView.showQQ( "body_16.png", pos )
            her "И она сказала мне, что ни разу не целовалась..."
            her "И что она боится, что у нее, наверное, будет плохо получаться..."
            $herView.hideQQ()
            $herView.showQQ( "body_06.png", pos )
            her "Ну я и предложила свою помощь..."
            play music "music/(Orchestral) Playful Tension by Shadow16nh.mp3" fadein 1 fadeout 1 # SEX THEME.
            her "Потом мы вместе провели время в одной из кабинок в туалете..."
            $herView.hideQQ()
            $herView.showQQ( "body_45.png", pos )
            her "Развлекаясь..."
            $herView.hideQQ()
            $herView.showQQ( "body_31.png", pos )
            her "Она довольно быстро приноровилась... Думаю, что после небольшой практики она будет по настоящему хороша в этом..."
            $herView.hideQQ()
            $herView.showQQ( "body_45.png", pos )
            her "А еще она была такой милашкой..."
            $herView.hideQQ()
            $herView.showQQ( "body_46.png", pos )
            her "Она называла меня \"Мисс Грейнджер\"..."
            m "Хм..."
            m "Я не помню, чтобы давал вам задание смущать маленьких детей, мисс Грейнджер."
            $herView.hideQQ()
            $herView.showQQ( "body_64.png", pos )
            her "\"Маленьких детей\"? Позвольте, сэр..."
            her "Вы бы видели эту девочку..."
            her "Миниатюрная? Может быть... Но определенно не \"ребенок\"."
            $herView.hideQQ()
            $herView.showQQ( "body_111.png", pos )
            her "И я уверяю вас, что она была какой угодно, но не смущенной."
            her "На самом деле, под конец нашего \"урока\" она стала даже немного несносной..."
            $herView.hideQQ()
            $herView.showQQ( "body_31.png", pos )
            her "У меня даже появилось чувство, что она просто воспользовалась мной..."
            m "Ох... Ну, в таком случае..."
            $herView.hideQQ()
            $herView.showQQ( "body_45.png", pos )

            
        elif one_out_of_three == 2: ### EVENT (B)
            m "Мисс Грейнджер. Вы выполнили задание?"
            show screen blktone
            with d3
            $herView.hideQQ()
            $herView.showQQ( "body_16.png", pos )
            play music "music/Chipper Doodle v2.mp3" fadein 1 fadeout 1 # HERMIONE'S THEME.
            her "Выполнила, сэр."
            m "Расскажи мне, как все прошло."
            $herView.hideQQ()
            $herView.showQQ( "body_31.png", pos )
            her "Ну... Эм..."
            her "Есть одна девушка, которая любит... девушек..."
            her "Я подумала, что она будет идеальным кандидатом для моего задания..."
            her "И я спросила, могу ли я ее поцеловать..."
            $herView.hideQQ()
            $herView.showQQ( "body_87.png", pos )
            her "Она сказала, что для этого мы должны пойти в женскую уборную..."
            her "Но я поцеловала ее прямо там, в коридоре..."
            $herView.hideQQ()
            $herView.showQQ( "body_31.png", pos )
            her "И она поцеловала меня в ответ, но..."
            $herView.hideQQ()
            $herView.showQQ( "body_118.png", pos )
            her "Вскоре это начало казаться мне странным..."
            her "То, как она целовала меня..."
            $herView.hideQQ()
            $herView.showQQ( "body_117.png", pos )
            her "Она делала это как парень, сэр..."
            $herView.hideQQ()
            $herView.showQQ( "body_118.png", pos )
            her "Агрессивно, но уверенно..."
            $herView.hideQQ()
            $herView.showQQ( "body_120.png", pos )
            her "Естественно, вскоре вокруг нас собралась небольшая группа наблюдателей..."
            $herView.hideQQ()
            $herView.showQQ( "body_183.png", pos )
            her "В основном парни, конечно..."
            $herView.hideQQ()
            $herView.showQQ( "body_182.png", pos )
            her "Некоторые из них даже подбадривали нас..."
            $herView.hideQQ()
            $herView.showQQ( "body_129.png", pos )
            her "....."
            her "Кстати, та девушка, что я поцеловала, сэр..."
            m "Хм...?"
            $herView.hideQQ()
            $herView.showQQ( "body_127.png", pos )
            her "Она одна из тех непопулярных ребят..."
            her "Я знаю, что остальные ученики могли издеваться над ней..."
            $herView.hideQQ()
            $herView.showQQ( "body_129.png", pos )
            her "Но сегодня все изменилось..."
            her "Я голыми руками вытащила ту девушку из социального болота..."
            $herView.hideQQ()
            $herView.showQQ( "body_111.png", pos )
            her "В \"лесбиянку, что развлекается с Гермионой Грейнджер\"!"
            m "Вау... Ты прямо герой..."
            $herView.hideQQ()
            $herView.showQQ( "body_128.png", pos )
            her "Думаю да, сэр..."
            her "Я изменила жизнь той бедной девушки..."
            m "Ты меня расстрогала..."

            
            
        elif one_out_of_three == 3: ### EVENT (C)
            show screen blktone
            with d3
            $herView.hideQQ()
            $herView.showQQ( "body_16.png", pos )
            play music "music/Chipper Doodle v2.mp3" fadein 1 fadeout 1 # HERMIONE'S THEME.
            her "Профессор Дамблдор?"
            m "Да, мисс Грейнджер?"
            $herView.hideQQ()
            $herView.showQQ( "body_31.png", pos )
            her "Могу я задать вопрос, сэр?"
            m "Конечно."
            $herView.hideQQ()
            $herView.showQQ( "body_69.png", pos )
            her "Эм..."
            $herView.hideQQ()
            $herView.showQQ( "body_66.png", pos )
            her "Почему парни так любят наблюдать за целующимися девушками, сэр?"
            menu:
                m "..."
                "\"Кто знает? Парни странные.\"":
                    $herView.hideQQ()
                    $herView.showQQ( "body_118.png", pos )
                    her "Да, это точно, так ведь...?"
                    m "Да, да..."
                    m "И вот почему такие молоденькие девушки как ты...."
                    m "Часто интересуются намного более взрослыми джентельменами..."
                    $herView.hideQQ()
                    $herView.showQQ( "body_117.png", pos )
                    her "??!"
                    $herView.hideQQ()
                    $herView.showQQ( "body_79.png", pos )
                    her "Это не то, что я имела в виду, сэр..."
                "\"Ты не поймешь.\"":
                    $herView.hideQQ()
                    $herView.showQQ( "body_120.png", pos )
                    her "Хм..."
                    $herView.hideQQ()
                    $herView.showQQ( "body_117.png", pos )
                    her "Как насчет вас, сэр?"
                    her "Вы были таким же, когда были юны?"
                    m "Нравилось ли мне наблюдать за двумя развлекающимися девушками?"
                    m "Ну конечно."
                    m "Как и сейчас..."
                    $herView.hideQQ()
                    $herView.showQQ( "body_120.png", pos )
                    her "Ох..."
                "\"Целующиеся девушки? Где?!!\"":
                    $herView.hideQQ()
                    $herView.showQQ( "body_76.png", pos )
                    her "Тск!......................" # :(
            
            
            $herView.hideQQ()
            $herView.showQQ( "body_87.png", pos )
            her "Ну, я спрашиваю вас только потому, сэр..."
            $herView.hideQQ()
            $herView.showQQ( "body_117.png", pos )
            her "...что в нашей школе это что-то вроде новой моды..."
            her "И этим пользуются некоторые девушки, чтобы привлечь внимание парней..."
            m "Вы одна из таких девушек, мисс Грейнджер?"
            $herView.hideQQ()
            $herView.showQQ( "body_118.png", pos )
            her "Наверное..."
            $herView.hideQQ()
            $herView.showQQ( "body_120.png", pos )
            her "В смысле, это только из-за услуг, что вы у меня покупаете, сэр..."
            m "Хорошо... Расскажи мне больше."
            $herView.hideQQ()
            $herView.showQQ( "body_80.png", pos )
            her "Ну, как вы знаете, я достаточно популярна..."
            $herView.hideQQ()
            $herView.showQQ( "body_74.png", pos )
            her "Так что все, что мне надо было сделать, так это просто намекнуть, что я не прочь заняться этим сегодня..."
            her "И тут же выстроилась очередь..."
            $herView.hideQQ()
            $herView.showQQ( "body_45.png", pos )
            her "Конечно, я выбрала девушку из \"Гриффиндора\"..."
            $herView.hideQQ()
            $herView.showQQ( "body_31.png", pos )
            her "И мы устроили небольшое шоу прямо посреди класса..."
            m "Хорошо... С языком и всем прочим?"
            $herView.hideQQ()
            $herView.showQQ( "body_29.png", pos )
            her "С языком и всем прочим, сэр."
            m "Отличная работа."
            $herView.hideQQ()
            $herView.showQQ( "body_45.png", pos )

    elif whoring >= 18: # LEVEL 07+                  
        if one_out_of_three == 1: ### EVENT (A) # Snowballing
            label snowballing:
                pass
            m "Мисс Грейнджер..."
            show screen blktone
            with d3
            $herView.hideQQ()
            $herView.showQQ( "body_16.png", pos )
            play music "music/Chipper Doodle v2.mp3" fadein 1 fadeout 1 # HERMIONE'S THEME.
            her "Добрый вечер, сэр."
            m "Вы выполнили свое задание?"
            $herView.hideQQ()
            $herView.showQQ( "body_15.png", pos )
            her "Да, сэр."
            m "Я весь внимание..."
            $herView.hideQQ()
            $herView.showQQ( "body_17.png", pos )
            her "Ну, я поцеловала ту неприятную блондинку из \"Слизерина\"..."
            m "Хм... \"неприятную\", да?"
            m "Потому что она из \"Слизерина\"?"
            $herView.hideQQ()
            $herView.showQQ( "body_16.png", pos )
            her "Именно, сэр."
            m "Хм..."
            m "Ты не думаешь, что это небольшой предрассудок с твоей стороны?"
            m "Или может ты становишься \"факультистом\"?"
            $herView.hideQQ()
            $herView.showQQ( "body_185.png", pos )
            her "...\"факультистом\", сэр?"
            m "Ну, знаешь... Как \"сексист\" или \"расист\"..."
            m "Просто поставь \"ист\" после какого-нибудь слова и это сразу же станет плохой штукой..."
            $herView.hideQQ()
            $herView.showQQ( "body_13.png", pos )
            her "Слова \"факультист\" не существует, сэр..."
            m "Нету? Тогда подожди..."
            $herView.hideQQ()
            $herView.showQQ( "body_185.png", pos )
            her ".............?"
            m "\"Факультофобия\"...?"
            m "Нет, стой, я понял!"
            m "\"Факультофоб\"!"
            $herView.hideQQ()
            $herView.showQQ( "body_07.png", pos )
            her "Прекратите, сэр. Я - никто из этих странных слов..."
            her "\"Слизеринцы\" злые и надоедливые. Никто их не любит и это факт!"
            m "Ладно, пофиг. Тогда вернемся к \"девчачьим поцелуйчикам\"."
            $herView.hideQQ()
            $herView.showQQ( "body_29.png", pos )
            her "..............."
            her "Как я и говорила..."
            $herView.hideQQ()
            $herView.showQQ( "body_31.png", pos )
            her "Я поцеловала ту девушку из \"Слизерина\"..."
            $herView.hideQQ()
            $herView.showQQ( "body_69.png", pos )
            her "Конечно, в обычной ситуации я бы никогда этого не сделала..."
            her "Уж точно ни с кем-то с того жалкого факультета..."
            $herView.hideQQ()
            $herView.showQQ( "body_79.png", pos )
            her "Но она подошла ко мне сама и практически умоляла меня сделать это с ней..."
            $herView.hideQQ()
            $herView.showQQ( "body_69.png", pos )
            her "Именно сегодня..."
            her "Если честно..."
            $herView.hideQQ()
            $herView.showQQ( "body_79.png", pos )
            her "Она была довольно-таки привлекательной..."
            $herView.hideQQ()
            $herView.showQQ( "body_120.png", pos )
            her "Для кого-то из \"Слизерина\"..."
            $herView.hideQQ()
            $herView.showQQ( "body_127.png", pos )
            her "Я не спросила, почему она так отчаянно в этом нуждалась..."
            her "Возможно, она просто пыталась за мой счет увеличить свою популярность..."
            her "Или кто-то из школьного персонала купил у нее эту услугу..."
            $herView.hideQQ()
            $herView.showQQ( "body_186.png", pos )
            her "Так же, как вы покупаете услуги от меня, сэр..."
            m "(Снейп?)"
            $herView.hideQQ()
            $herView.showQQ( "body_47.png", pos )
            her "Если это так, то я уверена, что это был профессор Снейп..."
            m "Что? Да он бы никогда..."
            $herView.hideQQ()
            $herView.showQQ( "body_69.png", pos )
            her "Вы в самом деле должны разобраться в делишках профессор Снейпа, сэр..."
            m "Конечно..."
            m "Пока мы говорим, я заношу его в мой \"список плохих мальчиков\"..."
            $herView.hideQQ()
            $herView.showQQ( "body_66.png", pos )
            her ".........."
            m "Что произошло дальше?"
            $herView.hideQQ()
            $herView.showQQ( "body_87.png", pos )
            her "Ох, точно..."
            her "Ну, мы немного поразвлекались..."
            her "Она была очень... страстной."
            $herView.hideQQ()
            $herView.showQQ( "body_122.png", pos )
            her "Мне кажется, что это было то еще зрелище..."
            her "Парни свистели и подбадривали..."
            $herView.hideQQ()
            $herView.showQQ( "body_124.png", pos )
            her "В общем, мы решили немного \"поиграть в снежки\"..."
            m "Простите, что вы решили?"
            $herView.hideQQ()
            $herView.showQQ( "body_122.png", pos )
            her "\"Поиграть в снежки\", сэр."
            $herView.hideQQ()
            $herView.showQQ( "body_128.png", pos )
            her "Это когда одна девушка плюет в рот другой девушке..."
            her "Мы называем это \"снежками\"..."
            her "Почему-то парни сходят с ума от такого..."
            m "Могу себе представить..."
            $herView.hideQQ()
            $herView.showQQ( "body_127.png", pos )
            her "В общем, она плюнула в мой рот..."
            her "А затем я плюнула в ее..."
            $herView.hideQQ()
            $herView.showQQ( "body_187.png", pos )
            her "Хотя намного больше мне хотелось плюнуть ей в лицо!"
            $herView.hideQQ()
            $herView.showQQ( "body_69.png", pos )
            her "Затем она вернула мой плевок..."
            $herView.hideQQ()
            $herView.showQQ( "body_187.png", pos )
            her "Я с трудом поборола желание врезать ей по наглой роже за это..."
            $herView.hideQQ()
            $herView.showQQ( "body_120.png", pos )
            her "Но я думаю, что парни бы не оценили этого..."
            m "Ох как вы ошибаетесь..."
            $herView.hideQQ()
            $herView.showQQ( "body_124.png", pos )
            her "В любом случае, после этого мы целовались еще некоторое время..."
            her "И перемена закончилась..."
            $herView.hideQQ()
            $herView.showQQ( "body_122.png", pos )
            her "И мне пришлось бежать в класс..."
            m "*Вздох...* Беззаботные и невинные школьные деньки..."
            m "Уроки... Домашние задания..."
            m "Школьницы \"играющие в снежки\" во дворе..."
            m "Отличная работа, мисс Грейнджер."
            $herView.hideQQ()
            $herView.showQQ( "body_68.png", pos )
            

        elif one_out_of_three == 2: ### EVENT (B)
            m "Мисс Грейнджер, вы выполнили задание?"
            show screen blktone
            with d3
            $herView.hideQQ()
            $herView.showQQ( "body_16.png", pos )
            her "Выполнила, сэр."
            $herView.hideQQ()
            $herView.showQQ( "body_68.png", pos )
            her "Только... эм..."
            m "Что такое?"
            $herView.hideQQ()
            $herView.showQQ( "body_45.png", pos )
            her "Ну... У меня есть подруга..."
            her "Ее зовут Джинни Уизли..."
            $herView.hideQQ()
            $herView.showQQ( "body_188.png", pos )
            her "И... эм..."
            her "Я не знаю, как это сказать..."
            m "Просто скажи это, девочка."
            $herView.hideQQ()
            $herView.showQQ( "body_31.png", pos )
            her "Ну, мы решили вместе прогулять урок зельеварения..."
            her "И вместо него подготовиться к тесту по травничеству..."
            her "Ну, мы с Джинни учились..."
            her "И болтали о парнях..."
            m "Естественно..."
            $herView.hideQQ()
            $herView.showQQ( "body_189.png", pos )
            play music "music/(Orchestral) Playful Tension by Shadow16nh.mp3" fadein 1 fadeout 1 # SEX THEME.
            her "И тогда я, вроде как, поцеловала ее..."
            $herView.hideQQ()
            $herView.showQQ( "body_128.png", pos )
            her "И Джинни вернула мой поцелуй с такой страстью..."
            her "Что у нас все кончилось больше, чем просто поцелуями..."
            g9 "После этого у вас была битва подушками в одном лишь нижнем белье?"
            $herView.hideQQ()
            $herView.showQQ( "body_190.png", pos )
            her "Эмм... Нет..."
            m "Тогда что вы сделали?"
            $herView.hideQQ()
            $herView.showQQ( "body_188.png", pos )
            her "Я не скажу вам, сэр." # :)
            her "Вы посылали меня поцеловать девушку..."
            her "И я именно это и сделала."
            $herView.hideQQ()
            $herView.showQQ( "body_122.png", pos )
            her "Остальные происшествия могут быть моими маленькими тайнами."
            m "Это жестоко, маленькая ты ведьма."
            $herView.hideQQ()
            $herView.showQQ( "body_64.png", pos )
            her "Мои очки, пожалуйста." # :)
            m "Ладно..."

            
        elif one_out_of_three == 3: ### EVENT (C) Only takes place once
            if lazy_aka_not_yet:
                pass
            else:
                jump snowballing
                
            $ lazy_aka_not_yet = False #Makes sure this event only takes place once.
            play music "music/Chipper Doodle v2.mp3" fadein 1 fadeout 1 # HERMIONE'S THEME.
            m "Мисс Грейнджер, вы завершили задание?"
            show screen blktone
            with d3
            $herView.hideQQ()
            $herView.showQQ( "body_45.png", pos )
            her "Да, сэр."
            m "Шикарно. Расскажите мне больше."
            show screen blktone
            with d3
            $herView.hideQQ()
            $herView.showQQ( "body_64.png", pos )
            her "Конечно."
            her "Я решила попробовать сегодня другой подход..."                                                                                                                                                                                                              
            $ pos.xpos = 500

            # use CharacterExItemPoseParade to hide all items
            $ herView.data().addPose( CharacterExItemPoseParade( herView.mPoseFolder, "hermione_bugged_branch.png", G_Z_FACE + 5 ) )
            $herView.showQ( "body_63.png", pos )
            stop music
            her "Я выяснила, что ессссссссссссссссссссссссссссссссссссссссссссссссссссссссссссссссссссссссссссссссссссссссссссссссссссс"
            m "Хах?"
            $herView.hideQ()
            $herView.data().delPose()
            her "Если я смоооооооооо"
            pause
            pause
            pause
            
            with hpunch
            g4 "{size=+5}ТВОЮ МАТЬ!!!{/size}"
            g4 "{size=+5}АКАБУР?!!!{/size}"
            a4 "Хм...? ЧТО?!! Что ты хочешь от меня?"
            a4 "Еще нет релизной даты! Хватит спрашивать меня!"
            g4 "Что ты несешь?"
            a5 "Нет, я не сплю..." 
            a7 "*Зевает*..."
            a5 "................"
            m "Так что, теперь Гермиона будет постоянно заикаться? Так и было задумано?"
            pause
            pause
            g4 "Ты еще здесь?"
            a1 "Я не сплю..."
            a5 "Просто мои глаза отдыхают..."
            g4 "Что за черт, чувак?"
            g4 "Просто иди и поспи, пока ты все не испортил."
            m "Иди вздремни и закончи этот ивент, как полагается."
            a1 "Я не могу..."
            a1 "Я хочу, чтобы эта игра вышла как можно быстрее..."
            a1 "Нет, перепиши это. Я хочу чтобы она вышла быстрее, чем это возможно..."
            a1 "Люди верят в меня... и..."
            a7 "*зевает*..."
            a1 "И...."
            pause
            pause
            
            m "Акабур?"
            m "Чувак?"
            
            pause
            pause
            
            m "*Вздох*...ладно, я думаю, что мы можем пропустить этот ивент."
           # m "Just this once though..."
            m "Хорошо, хоть уровень \"развратности\" Гермионы увеличился..."
            m "Не придется возиться с сохранениями..."
            
            aa "Zzzz....zzz....."
            aa "Zzz.... Лола? Нет... Я сказал, убери свои сиськи... Zzzz....."
            aa "Zzz.... И не зови меня так.... Zzz...."
            
            m "*Вздох...* Как-то немного грустно..."
            

            
    $ gryffindor +=45
    m "45 очков \"Гриффиндору\"!"
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


 
 
 
 
    
    $ request_20_points += 1 
    $ request_20 = False 
    $ hermione_sleeping = True

    call music_block
    
    return
    
    
