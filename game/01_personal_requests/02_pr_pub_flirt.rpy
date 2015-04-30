
###################REQUEST_02_b (LEVEL 01) ### FLIRT WITH CLASSMATES ###
label new_request_02_b:
    $herView.hideQQ()
    m "{size=-4}(Попросить ее флиртовать с парнями из \"Слизерина\"?){/size}"
    $ menu_x = 0.5 #Default menu position restored.
    menu:
        "\"(Да, давай попробуем!)\"":
            pass
        "\"(Не сейчас)\"":
            $event.NotFinished()
            jump new_personal_request
    
    m "Мисс Грейнджер?"
    $ pos = POS_140
    $herView.showQQ( "body_13.png", pos )
    her "Да?"
    
    if request_02_b_points == 0 and hermi.whoring <= 5: ### LEVEL 01 and LEVEL 02
        ### LEVEL 01 ### <===============================================================FIRST EVENT!
        play music "music/Chipper Doodle v2.mp3" fadein 1 fadeout 1 # HERMIONE'S THEME.
        m "Что вы думаете насчет мальчиков из \"Слизерина\"?"
        $herView.hideshowQQ( "body_05.png", pos )
        her "Я терпеть их не могу, сэр."
        m "Ну, очень плохо. Потому что я хочу, чтобы ты подружилась с несколькими из них."
        $herView.hideshowQQ( "body_13.png", pos )
        her "Если я должна..."
        her "Ну, думаю, я могу быть вежлива с парой из них."
        m "Да, и я сказал \"подружиться с ними...\""
        m "Вообще-то, я имел в виду - позаигрывать с ними..."
        $herView.hideshowQQ( "body_48.png", pos )
        her "Заигрывать?!"
        $herView.hideshowQQ( "body_47.png", pos )
        her "Профессор Дамблдор!"
        $herView.hideshowQQ( "body_17.png", pos )
        her "Я даже не буду спрашивать, почему вам это интересно..."
        $herView.hideshowQQ( "body_11.png", pos )
        her "Но почему \"Слизерин\"?"
        her "Если вам нужно, чтобы я кокетничала сегодня, то я могу..."
        her "Но, пожалуйста, может быть другой факультет?"
        $herView.hideshowQQ( "body_44.png", pos )
        her "Может \"Гриффиндор\"?"
        m "Я просто стараюсь защитить вашу репутацию, Мисс Грейнджер."
        $herView.hideshowQQ( "body_15.png", pos )
        her "Сэр?"
        m "Вам важно мнение \"Слизеринских\" учеников о себе?"
        $herView.hideshowQQ( "body_30.png", pos )
        her "Вообще, мне плевать на мнение этих дикарей."
        m "Что насчет студентов из \"Гриффиндора\"?"
        $herView.hideshowQQ( "body_29.png", pos )
        her "Их мнение очень важно для меня..."
        $herView.hideshowQQ( "body_06.png", pos )
        her "Ох, понятно..."
        m "Точно... Просто идеально для вас, Мисс Грейнджер."
        her "Эм... Спасибо, профессор..."
        call music_block
    
    else:
        if hermi.whoring <= 2: ### LEVEL 01
            m "Мне нужно, чтобы ты завела пару друзей в \"Слизерине\"."
            her "То есть, снова заигрывать со \"слизеринскими\" парнями?"
            m "Это именно то, что я хочу от вас сегодня, Мисс Грейнджер."
            $herView.hideshowQQ( "body_02.png", pos )
            her "Мне действительно это нужно делать?"
            m "Мы уже проходили через это, девочка."
            m "В твоих же интересах заводить себе друзей в \"Слизерине\"."
            $herView.hideshowQQ( "body_04.png", pos )
            her "Да, я знаю, сэр."
            her "Но почему именно я?"
            m "Никто вас не заставляет, Мисс Грейнджер..."
            $herView.hideshowQQ( "body_05.png", pos )
            her "Вам не нужно напоминать мне это, сэр..."
            $herView.hideshowQQ( "body_07.png", pos )
            her "Ладно, я поняла... Сэр..."


        else: #if whoring >= 3 and whoring >= 6: ### LEVEL 02 and higher ## <=========================================================== SECOND EVENT!
            m "Ты должна кокетничать с парнями из \"Слизерина\"."
            her "Я посмотрю, что можно сделать."
            m "Отлично. Буду ждать вас после занятий."

    
    her "Ну, мне стоит идти. Занятия вот-вот начнутся..."
#    $ request_02_b = True

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
   
        
        
label new_request_02_b_complete:
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
    $herView.showQ( "body_01.png", pos )
    show screen hermione_02
    with Dissolve(.3)
    her "Добрый вечер, сэр."
    m "Мисс Грейнджер..."
    m "Вы завершили задание?"
    her "Я сделала все, как вы просили..."
    menu:
        "\"Отлично, вот твои очки\"":
            pass
        "\"Расскажи поподробнее\"":
            $herView.hideQQ()
            m "Со сколькими мальчиками вы успели позаигрывать, Мисс Грейнджер?"
            m "Раскажите мне."
            show screen blktone
            with d3
            if hermi.whoring >= 0 and hermi.whoring <= 2: ### LEVEL 01
                if one_out_of_three == 1: ### EVENT (A)
                    
                    stop music fadeout 1.0
                    $herView.hideshowQQ( "body_10.png", pos )
                    her "Ну..."
                    her "Был этот первокурсник..."
                    her "........."
                    m "Я слушаю..."
                    her "Эм... Я подошла к нему и сказала: \"Эй, красавчик!\"."
                    m "И?"
                    play music "music/Chipper Doodle v2.mp3" fadein 1 fadeout 1 # HERMIONE'S THEME.
                    $herView.hideshowQQ( "body_07.png", pos )
                    her "Он показал мне язык и убежал, сэр."
                    m "Ты пробовала заманить его обратно конфеткой?"
                    $herView.hideshowQQ( "body_10.png", pos )
                    her "Нет, сэр..."
                    her "Это не приходило мне в голову--"
                    m "Я шучу, Мисс Грейнджер."
                    $herView.hideshowQQ( "body_07.png", pos )
                    her "Сэр?"
                    m "Я не посылал тебя приставать к маленьким детям!"
                    $herView.hideshowQQ( "body_09.png", pos )
                    her "............."
                    m "Я попросил тебя флиртовать с мальчиками {size=+5}твоего{/size} возраста!"
                    $herView.hideshowQQ( "body_07.png", pos )
                    her "Сначала я хотела, но..."
                    $herView.hideshowQQ( "body_12.png", pos )
                    her "Я просто испугалась..."
                    her "То есть я презираю \"Слизеринцев\" слишком сильно, чтобы флиртовать с ними, сэр!"
                    $herView.hideshowQQ( "body_05.png", pos )
                    her "Мне приходится бороться с рвотным рефлексом при их виде!"
                    menu:
                        "\"Ладно. Попробуй в следующий раз.\"":
                            $herView.hideshowQQ( "body_06.png", pos )
                            her "Спасибо, сэр."
                            her "Я попробую, обещаю!"
                        "\"Ты провалилась! Никаких очков ты не получишь!\"":
                            stop music fadeout 1.0
                            $herView.hideshowQQ( "body_07.png", pos )
                            her "Я понимаю..."
                            m "Убирайся с глаз моих..."
                            $herView.hideshowQQ( "body_09.png", pos )
                            her "Да, сэр... Простите, сэр..."
                            jump could_not_flirt
                    
                elif one_out_of_three == 2: ### EVENT (B)
                    play music "music/Chipper Doodle v2.mp3" fadein 1 fadeout 1 # HERMIONE'S THEME.
                    $herView.hideshowQQ( "body_10.png", pos )
                    her "Ну, я пыталась подкатить к старшекласснику..."
                    m "Он повелся?"
                    $herView.hideshowQQ( "body_76.png", pos )
                    her "Он назвал меня \"Гриффиндорской шлюхой\", сэр!"
                    m "Понятно..."
                    m "И что ты сделала?"
                    $herView.hideshowQQ( "body_04.png", pos )
                    her "Ну, это было неправильно для ученика \"Хогвартса\"..."
                    her "И я сказала ему, что настучу на него."
                    m "Действительно захватывающая история..."
                    m "Что-то еще?"
                    $herView.hideshowQQ( "body_09.png", pos )
                    her "Да, был еще мальчик в библиотеке..."
                    her "Он, очевидно, был чем-то занят..."
                    her "Ну, я и предложила свою помощь..."
                    m "И?"
                    $herView.hideshowQQ( "body_76.png", pos )
                    her "Он назвал меня \"Главной шлюхой Гриффиндора\"..."
                    m "И ты угрожала настучать на него за это?"
                    $herView.hideshowQQ( "body_04.png", pos )
                    her "Конечно, сэр."
                    m "*Вздох*"
                    m "Что-то еще?"
                    $herView.hideshowQQ( "body_09.png", pos )
                    her "Ну, был еще один момент, похожий на предыдущие..."
                    m "\"Гриффиндорская шлюха\"?"
                    $herView.hideshowQQ( "body_66.png", pos )
                    her ".........да, сэр."
                    m "Вы делаете все неправильно, Мисс Грейнджер."
                    $herView.hideshowQQ( "body_69.png", pos )
                    her "Простите, профессор. Я думала, что будет легко..."
                    menu:
                        "\"Ну, ты хотя бы попыталась.\"":
                            $herView.hideshowQQ( "body_34.png", pos )
                            her "Видимо, флирт не самая сильная моя сторона..."
                        "\"Задание провалено. Ты не получишь очки!\"":
                            stop music fadeout 1.0
                            $herView.hideshowQQ( "body_11.png", pos )
                            $ hermi.liking -=15
                            her "Вы не заплатите мне, сэр?"
                            $herView.hideshowQQ( "body_21.png", pos )
                            her "Но вы обещали!"
                            $herView.hideshowQQ( "body_20.png", pos )
                            her "................"
                            call music_block
                            jump could_not_flirt
                    
                elif one_out_of_three == 3: ### EVENT (C)
                    stop music fadeout 1.0
                    $herView.hideshowQQ( "body_10.png", pos )
                    her "Ну, команда \"Слизерина\" по квиддичу занималась сегодня на стадионе..."
                    her "Я подумала, что смогу проникнуть на трибуны и болеть за них..."
                    $herView.hideshowQQ( "body_12.png", pos )
                    her "Но..."
                    m "Да?"
                    play music "music/Chipper Doodle v2.mp3" fadein 1 fadeout 1 # HERMIONE'S THEME.
                    $herView.hideshowQQ( "body_77.png", pos )
                    her "Все эти \"Слизеринские\" шлюхи уже были там."
                    her "У них были кричалки и все такое..."
                    $herView.hideshowQQ( "body_47.png", pos )
                    her "И некоторые из них даже вели себя неподобающим образом, сэр..."
                    her "Не могу поверить, что их приняли в нашу школу..."
                    m "Итак... что же было в конце этого всего?"
                    $herView.hideshowQQ( "body_69.png", pos )
                    her "Я просто ушла, сэр..."
                    menu:
                        m "Хм..."
                        "\"Но все же, вот твои очки.\"":
                            $herView.hideshowQQ( "body_16.png", pos )
                            her "Спасибо, сэр..."               
                            
                        "\"Задание провалено! Ты не получишь очки!\"":
                            stop music fadeout 1.0
                            $herView.hideshowQQ( "body_12.png", pos )
                            her "Все равно я чувствую, что не заслужила их..."
                            call music_block
                            jump could_not_flirt
                    
                    
                    
                    
            elif hermi.whoring >= 3 and hermi.whoring <= 5: ### LEVEL 02
                if one_out_of_three == 1: ### EVENT (A)
                    stop music fadeout 1.0
                    $herView.hideQQ()
                    $ pos = POS_140
                    $herView.showQQ( "body_10.png", pos )
                    her "Ну, был один парень в библиотеке..."
                    her "Он был чем-то озадачен, и я предложила помощь..."
                    m "И?"
                    play music "music/Chipper Doodle v2.mp3" fadein 1 fadeout 1 # HERMIONE'S THEME.
                    $herView.hideshowQQ( "body_75.png", pos )
                    her "Ну, к моему удивлению, он принял помощь..."
                    her "Он позволил закончить для него задание..."
                    $herView.hideshowQQ( "body_34.png", pos )
                    her "Пока я работала, он сделал пару неуместных замечаний, но я просто улыбалась в ответ..."
                    m "Кажется, он сам флиртовал с тобой..."
                    $herView.hideshowQQ( "body_24.png", pos )
                    her "Ну... думаю, да."
                    $herView.hideshowQQ( "body_45.png", pos )
                    her "Но, несмотря на его недостойное поведение, я подыгрывала ему..."
                    m "Помалкивая?"
                    her "Да, сэр..."
                    her "Полагаю, это и помогло мне достигнуть цели, верно?"
                    m "О-ох-х... {size=-2}(*с кислым лицом*){/size}"
                    m "Что у тебя еще есть?"
                    $herView.hideshowQQ( "body_69.png", pos )
                    her "Ну..."
                    her "Потом в коридоре я встретила ребят, которые оценили мою внешность в весьма вульгарной манере..."
                    $herView.hideshowQQ( "body_34.png", pos )
                    her "Но я просто улыбнулась им..."
                    m "И снова ты почти ничего не сделала..."
                    m "Это не то, о чем я просил, Мисс Грейнджер."
                    $herView.hideshowQQ( "body_34.png", pos )
                    her "Я знаю, сэр!"
                    $herView.hideshowQQ( "body_69.png", pos )
                    her "Но я очень занята. У меня встречи \"ОЗМП\" и еще занятия..."
                    her "Мне едва хватает времени..."
                    m "Это все, что ты хотела мне сказать сегодня?"
                    $herView.hideshowQQ( "body_69.png", pos )
                    her "Нет, сэр."
                    her "Около часа назад я столкнулась с Драко Малфоем."
                    m "Не может быть!!! (Понятия не имею, кто это...)"
                    her "Я пыталась быть дружелюбной с ним..."
                    $herView.hideshowQQ( "body_74.png", pos )
                    her "В итоге мы закончили не очень приличной беседой." 
                    translators "Drako - Драко Малфой.\nDark-Ох - темный..."
                    m "Понятно... Этот \"Темный\" парень..."
                    m "Он вообще смотрел на твои ножки?"
                    $herView.hideshowQQ( "body_02.png", pos )
                    her "Что?"
                    m "Он пялился на твои ноги или нет??"
                    $herView.hideshowQQ( "body_44.png", pos )
                    her "Эм... возможно, так и было..."
                    m "Что насчет сисек?"
                    $herView.hideshowQQ( "body_47.png", pos )
                    her "Профессор!!!"
                    m "Ладно. Получай свои очки. Ты хорошо постаралась."
                    $herView.hideshowQQ( "body_29.png", pos )
 
                elif one_out_of_three == 2: ### EVENT (B)
                    stop music fadeout 1.0
                    $herView.hideshowQQ( "body_10.png", pos )
                    her "Ну..."
                    her "Сегодня утром я заигрывала с одним парнем..."
                    $herView.hideshowQQ( "body_13.png", pos )
                    her "Через секунду уже с другим..."
                    $herView.hideshowQQ( "body_28.png", pos )
                    her "А потом случилось что-то странное..."
                    play music "music/(Orchestral) Playful Tension by Shadow16nh.mp3" fadein 1 fadeout 1 # SEX THEME.
                    her "Этот злобно выгядящий парень из \"Слизерина\" подошел и пригласил меня на свидание..."
                    $herView.hideshowQQ( "body_13.png", pos )
                    her "Я ему отказала, но все таки он шел со мной вместе."
                    m "Вам это понравилось, Мисс Грейнджер?"
                    $herView.hideshowQQ( "body_31.png", pos )
                    her "Я думаю, да... К моему собственному удивлению..."
                    $herView.hideshowQQ( "body_45.png", pos )
                    her "Мне вроде и было безразлично, но..."
                    $herView.hideshowQQ( "body_74.png", pos )
                    her "Он был так уверен и спокоен..."
                    $herView.hideshowQQ( "body_34.png", pos )
                    her "Я, конечно же, до сих пор ненавижу \"Слизерин\"!"
                    $herView.hideshowQQ( "body_73.png", pos )
                    her "Но..."
                    her "Может, некоторые ученики там по ошибке?"
                    $herView.hideshowQQ( "body_10.png", pos )
                    her "Может, \"Шляпа\"... спутала?"
                    menu:
                        "\"Просто забирай свои очки и иди!\"":
                            $herView.hideshowQQ( "body_07.png", pos )
                            her "................"
                        "\"Она никогда не ошибается!\"":
                            $herView.hideshowQQ( "body_13.png", pos )
                            her "Да, конечно... Все это знают..."
                        "\"Ты действительно так думаешь?\"":
                            $herView.hideshowQQ( "body_13.png", pos )
                            her "Ох, не обращайте на меня внимания."
                            her "Все знают, что \"Шляпа\" никогда не ошибается."
                    
                    
                elif one_out_of_three == 3: ### EVENT (C)
                    play music "music/Chipper Doodle v2.mp3" fadein 1 fadeout 1 # HERMIONE'S THEME.
                    $herView.hideshowQQ( "body_75.png", pos )
                    her "Пять парней, сэр!"
                    m "Действительно?"
                    $herView.hideshowQQ( "body_74.png", pos )
                    her "Да!"
                    $herView.hideshowQQ( "body_74.png", pos )
                    her "Один сегодня утром."
                    her "Потом сразу же еще двое мальчиков."
                    her "И еще один в третий раз."
                    $herView.hideshowQQ( "body_68.png", pos )
                    her "И после этого у меня был довольно приятный разговор с одним мальчиком."
                    $herView.hideshowQQ( "body_74.png", pos )
                    her "Он оказался весьма умным и неплохо воспитанным."
                    her "............................"
                    her "................"
                    $herView.hideshowQQ( "body_34.png", pos )
                    her "Но это не поменяет моего мнения насчет \"Слизерина\", сэр."
                    m "Мне это и не нужно, Мисс Грейнджер."
                    her "Я занимаюсь этим ради своего факультета!"
                    $herView.hideshowQQ( "body_32.png", pos )
                    her "Для гордого \"Гриффиндора\"!"
                    m "Ладно, ладно, успокойся, девочка."
                    $herView.hideshowQQ( "body_74.png", pos )

            elif hermi.whoring >= 6: # LEVEL 03 and higher.
                if one_out_of_three == 1: ### EVENT (A)
                    play music "music/Chipper Doodle v2.mp3" fadein 1 fadeout 1 # HERMIONE'S THEME.
                    $herView.hideshowQQ( "body_75.png", pos )
                    her "Одиннадцать мальчиков, сэр!"
                    m "Одиннадцать? Правда? Ваш личный рекдорд, Мисс Грейнджер!"
                    $herView.hideshowQQ( "body_74.png", pos )
                    her "Да."
                    $herView.hideshowQQ( "body_68.png", pos )
                    her "Так, посмотрим..."
                    her "Сначала эти два красавчика..."
                    $herView.hideshowQQ( "body_64.png", pos )
                    her "Потом несколько неловких слов еще с одним парнем."
                    $herView.hideshowQQ( "body_68.png", pos )
                    her "После этого был еще один парень..."
                    $herView.hideshowQQ( "body_73.png", pos )
                    her "Потом еще три парня..."
                    $herView.hideshowQQ( "body_74.png", pos )
                    her "Потом еще один, по моему..."
                    $herView.hideshowQQ( "body_75.png", pos )
                    her "И последний мальчик проводил меня до вашей башни, сэр..."
                    m "Так, одиннадцать?"
                    m "Вы действительно начинаете нравиться этим \"Слизеринским\" парням, ага?"
                    $herView.hideshowQQ( "body_74.png", pos )
                    her "Похоже на то..."
                    $herView.hideshowQQ( "body_73.png", pos )
                    her "Ну, не все из них были обходительны со мной поначалу..."
                    $herView.hideshowQQ( "body_64.png", pos )
                    her "Но я пытаюсь немного \"приручить\" их."
                    m "Приручить?"
                    $herView.hideshowQQ( "body_74.png", pos )
                    her "Да... Каждый раз, когда кто-то из них произносит мое имя..."
                    her "Я просто пытаюсь проглотить свою гордость и улыбнуться в ответ."
                    m "Хм..."
                    m "Например, если кто-то назовет тебя \"шлюхой\", ты просто улыбнешься в ответ?"
                    $herView.hideshowQQ( "body_34.png", pos )
                    her "Ну, да..."
                    m "Отлично, уверен, что вы отлично справились."
                    m "Прекрасная работа, Мисс Грейнджер."
                    $herView.hideshowQQ( "body_68.png", pos )
                    
                elif one_out_of_three == 2: ### EVENT (B)
                    play music "music/Chipper Doodle v2.mp3" fadein 1 fadeout 1 # HERMIONE'S THEME.
                    $herView.hideshowQQ( "body_75.png", pos )
                    her "Два свидания, семь очень приятных разговоров..."
                    $herView.hideshowQQ( "body_68.png", pos )
                    her "И один даже поцеловал меня..."
                    m "Впечатляет, Мисс Грейнджер."
                    $herView.hideshowQQ( "body_74.png", pos )
                    her "Я тоже так думаю, сэр. Спасибо."
                    $herView.hideshowQQ( "body_75.png", pos )
                    her "Ох, еще этот первокурсник..."
                    her "Я пыталась заигрывать с ним, но все закончилось простым разговором..."
                    her "Он называл меня \"Мисс Гермиона\"..."
                    her "Это так очаровательно..."
                    m "Ну, я не посылал вас приставать к детям, Мисс Грейнджер."
                    $herView.hideshowQQ( "body_66.png", pos )
                    her "Я не пристав..."
                    $herView.hideshowQQ( "body_34.png", pos )
                    her "Сэр! Семь подкатов и два свидания - ведь неплохо, не так ли?"
                    m "Ох, конечно."
                    $herView.hideshowQQ( "body_30.png", pos )
                    her "Теперь я хотела бы получить свою плату..."
                    $herView.hideshowQQ( "body_33.png", pos )
                    
                elif one_out_of_three == 3: ### EVENT (C)
                    stop music fadeout 1.0
                    $herView.hideshowQQ( "body_33.png", pos )
                    her "Сэр, простите, но..."
                    play music "music/Chipper Doodle v2.mp3" fadein 1 fadeout 1 # HERMIONE'S THEME.
                    $herView.hideshowQQ( "body_47.png", pos )
                    her "Я ненавижу этих \"Слизеринских\" ублюдков, сэр!"
                    m "Расскажи, что произошло."
                    $herView.hideshowQQ( "body_69.png", pos )
                    her "я не хочу говорить об этом..."
                    m "Расскажи мне, что произошло, девочка!"
                    $herView.hideshowQQ( "body_76.png", pos )
                    her "Я не хочу говорить об этом, сэр."
                    $herView.hideshowQQ( "body_69.png", pos )
                    her "Пожалуйста, не заставляйте меня..."
                    menu:
                        "\"Ладно. На сегодня достаточно.\"":
                            $herView.hideshowQQ( "body_33.png", pos )
                            her "Спасибо, сэр."
                            m "Значит, сегодня ты провалила задание?"
                            $herView.hideshowQQ( "body_34.png", pos )
                            her "О, совсем напротив, сэр."
                            play music "music/(Orchestral) Playful Tension by Shadow16nh.mp3" fadein 1 fadeout 1 # SEX THEME.
                            her "Один из мальчиков \"Слизерина\" взял меня в общую комнату..."
                            $herView.hideshowQQ( "body_03.png", pos )
                            her "Там была как минимум дюжина парней..."
                            $herView.hideshowQQ( "body_04.png", pos )
                            her "Все они знали, кто я ..."
                            her "Я была в центре внимания..."
                            $herView.hideshowQQ( "body_78.png", pos )
                            her "И я чувствовала себя превосходно..."
                            play music "music/Chipper Doodle v2.mp3" fadein 1 fadeout 1 # HERMIONE'S THEME.
                            $herView.hideshowQQ( "body_66.png", pos )
                            her "А потом на меня накинулась кучка этих \"Слизеринских\" шлюх..."
                            m "И?"
                            $herView.hideshowQQ( "body_69.png", pos )
                            her "Ну, они делали и говорили всякое такое..."
                            her "Не важно, я все равно ушла..."
                            m "Понятно..."
                            m "Ну, думаю, вы заслужили свои очки, Мисс Грейнджер."
                            $herView.hideshowQQ( "body_74.png", pos )

                        "\"Рассказывай или потеряешь свои очки!\"":
                            $ hermi.liking -=10
                            $herView.hideshowQQ( "body_66.png", pos )
                            her "Сэр, пожалуйста, я не хочу об этом говорить."
                            m "Никто не заставляет вас, Мисс Грейнджер."
                            m "Ты можешь уйти."
                            $herView.hideshowQQ( "body_47.png", pos )
                            her "{size=-4}(Упрямый старик!){/size}"
                            jump could_not_flirt
                            
                            
    
    $ gryffindor +=5
    m "\"Гриффиндор\" получает 5 очков."
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




    $ request_02_b_points += 1
#    $ request_02_b = False 
    $ hermione_sleeping = True
    
    $ p_level_02_active = True #When turns TRUE public favors of level 02 become available. 

    $event.Finalize()    
    
    if hermi.whoring <= 2:
        $ hermi.whoring +=1
        
    call music_block
    return        

