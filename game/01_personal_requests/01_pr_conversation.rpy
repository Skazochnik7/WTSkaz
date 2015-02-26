################
### LEVEL 01 ###                
###################REQUEST_01 JUST STAND THERE.
label new_request_01: #LV.1 (Whoring = 0 - 2)
    $herView.hideQQ()
    m "{size=-4}(Я просто поговорю с ней...){/size}"
    menu:
        "\"(Да, сделаем это.)\"":
            pass
        "\"(Не сейчас.)\"":
            $event.NotFinished()
            jump new_personal_request
    play music "music/Chipper Doodle v2.mp3" fadein 1 fadeout 1 
    m "Ладно..."
    m "Просто расскажи что нового у тебя."
    $herView.hideQQ()
    $ pos = POS_140
    $herView.showQQ( "body_08.png", pos )
    
    if IsFirstRun(): #First time this event taking place.
#    if request_01 == 0: #First time this event taking place.
        her "Эм... Ладно..."
        her "Мне просто стоять здесь и говорить...? Как сейчас?"
    else:
        her "Стоя перед вами, верно? Я помню..."
    $herView.hideQQ()
    $ menu_x = 0.5 #Menu is moved to the left side.
    
    show screen blktone 
    with d3
    show screen ctc
    $herView.showQ( "body_01.png", pos )
    with Dissolve(.3)
    pause
    
    $pos = POS_140
    m "Итак?"
    if IsFirstRun() and whoring <=5: #First time this event taking place.
#    if request_01 == 0 and whoring <=5: #First time this event taking place.
#        $  new_request_01_01 = True #Hearts on menu buttons.
        $SetHearts(1)
        $herView.hideshowQQ( "body_11.png", pos )
        her "Эм... Ну что ж..."
        ">Гермиона смущается и слегка краснеет..."
        $herView.hideshowQQ( "body_12.png", pos )
        her "..................."
    if whoring >= 0 and  whoring <= 5: #LEVEL 01 and LEVEL 02
        if whoring >= 3 and whoring <= 5:
#            $ level = "02"
#            $ new_request_01_02 = True #Hearts on menu buttons.
            $SetHearts(2)
        $herView.hideshowQQ( "body_12.png", pos )
        her "В последнее время все относительно спокойно, ничего такого..."
        her "Кроме того дня, когда я завалила тест..."
        her "Все еще не могу поверить в это..."
        menu: 
            "- Дрочить пока она говорит -":
                $ d_flag_01 = True #If TRUE genie jerks off under the desk.    
                $herView.hideQ()
                hide screen blktone
                with d3
                ">Вы опускаете руки под стол и обхватываете свой член..."
                hide screen blktone8
                with d3
                hide screen genie
                show screen genie_jerking_off
                with d3
                pause
                $herView.hideQQ()
                $ pos = POS_370
                $herView.showQQ( "body_14.png", pos )
                her "Профессор, что вы делаете?"
                m "А? О, ничего. Просто чешу свою ногу."
                m "Так о чем ты говорила?"
                $herView.hideshowQQ( "body_14.png", pos )
                her "Да... Ну, тот тест я провалила..."
            "- Слушать ее -":
                $ d_flag_01 = False #NOT JERKING OFF.
                m "Да, это такая трагедия..."
                her "Именно! я рада, что вы понимаете меня, профессор."
                pass
        her "Как только вспомню об этом... Мне не слишком нравится это обсуждать..."
        m "Хорошо, что еще произошло за последнее время?"
        her "Эм... Ну, у меня очень хорошо идут дела с биологией..."
        her "Я имею в виду, у меня всегда хорошие оценки, но я все равно учусь усерднее..."
        her "Иногда мне кажется, что я знаю намного больше чем профессор Стебль..."
        if d_flag_01:
            m "{size=-4}(Да... ах...){/size}"
        else:
            # translators "(Sprout - росток, отросток. В книгах/фильмах ее зовут Памона Спраут/Памона Стебль.  Еще одна игра слов.)"
            m "(Профессор Стебль... Хе-хе, забавное имя...)"
        
        $herView.hideshowQQ( "body_07.png", pos )
        her "Вы что-то сказали?"
        m "Ничего, продолжай..."
        $herView.hideshowQQ( "body_14.png", pos )
        her "Ну, некоторые студенты смеются над профессором Квирреллом..."
        her "Конечно же, я не одобряю такое поведение."
        if d_flag_01:
            m "{size=-4}(Давай же! Скажи что-нибудь грязное!){/size}"
        else:
            m ".................."
        her "О, мое \"Общество по защите мужских прав\" набирает популярность..."
        her "И я очень рада..."
        $herView.hideshowQQ( "body_16.png", pos )
        her "Дайте нам только время, и мы реально сможем что-нибудь изменить..."
        $herView.hideshowQQ( "body_06.png", pos )
        her "Это очень воодушевляет, когда ты знаешь, что делаешь правильные вещи!"
        her "Вы согласны, профессор?"
        if d_flag_01:
            m "{size=-4}(Черт. Теперь она полностью убила все желание...){/size}"
            show screen genie
            with d3
            $ d_flag_01 = False #NOT JERKING OFF ANY MORE.
            pass
        else:
            m "Хх-хр-р-р........"
            m "А?"
            
        $herView.hideshowQQ( "body_05.png", pos )
        her "Профессор?"
        m "Да, да, я внимательно слушаю..."
        m "Это все очень самооправданно, э-э..."
        m "То есть, очень вдохновляет и даже переполняет, да..."
        $herView.hideshowQQ( "body_07.png", pos )
        her ".........................."
  
    elif whoring >= 6 and whoring<=11: #LEVEL 03
#        $  new_request_01_03 = True #Hearts on menu buttons.
        $ SetHearts(3)
        $herView.hideshowQQ( "body_12.png", pos )
        her "У меня в последнее время все вроде-как в порядке..."
        her "Хм..."
        her "Сейчас факультеты \"Слизерина\" и \"Гриффиндора\" очень сильно соперничают."
        her "И честно говоря, это совершенно неправильно..."
        her "\"Гриффиндор\" уверенно лидировал бы, если бы не \"Слизеринские\" шлюхи..."
        her "Я только и слышу, что они получают свои очки за \"услуги\"..."
        $herView.hideshowQQ( "body_04.png", pos )
        her "Очень подло!"
        m "И что же вы теперь будете делать, мисс Грейнджер?"
        $herView.hideshowQQ( "body_03.png", pos )
        her "Точно!"
        m "А?"
        $herView.hideshowQQ( "body_04.png", pos )
        her "Я должна трудится еще лучше, чтобы выровнять шансы, неравные из-за этих грязных девок..."
        $herView.hideshowQQ( "body_03.png", pos )
        her "Спасибо, что помогаете мне, профессор."
        menu: 
            "- Начать дрочить -":
                $ d_flag_01 = True #If TRUE genie jerks off under the desk.    
                $herView.hideQ()
                hide screen blktone
                with d3
                ">Вы опускаете руки под стол и обхватываете свой член..."
                hide screen blktone8
                with d3
                hide screen genie
                show screen genie_jerking_off
                with d3
                pause
                $herView.hideQQ()
                $ pos = POS_370
                $herView.showQQ( "body_14.png", pos )
                her "Профессор, что вы делаете?"
                her "Вы же не.....?"
                $herView.hideshowQQ( "body_29.png", pos )
                her "Вы...?"
                m "Ничего. Просто продолжай."
                $herView.hideshowQQ( "body_07.png", pos )
                her "Хм..."
                m "{size=-4}(Она что-то заподозрила? Да нет...){/size}"
            "- Внимательно выслушать ее -":
                $ d_flag_01 = False #NOT JERKING OFF.
                m "Не стоит благодарности."
                pass
        $herView.hideshowQQ( "body_16.png", pos )
        her "Ну, как я и сказала..."
        her "Я слышала, одна девчонка обменяла свои пикантные фотографии на десятку для факультета..."
        if d_flag_01:
            m "{size=-4}(Ну и шлюха... ах... Да...){/size}"
        else:
            m "Десять очков, да?"
        her "Да..."
        if d_flag_01:
            $herView.hideshowQQ( "body_29.png", pos )
            her "И эти две девушки..."
            her "Ходит слух, что они даже спят с профессором Снейпом..."
            m "{size=-4}(Да... Эти маленькие, грязные \"слизеринские\" шлюхи!){/size}"
            $herView.hideshowQQ( "body_45.png", pos )
            her "Еще был случай, я слышала, что ученица дрочила учителю прямо на занятии..."
            m "{size=-4}(Да... Это очень круто, продолжай!){/size}"
            $herView.hideshowQQ( "body_29.png", pos )
            her "И другая девочка, она сосала учителю!"
            m "{size=-4}(Да! Да!){/size}"
            $herView.hideshowQQ( "body_46.png", pos )
            her "А еще одна девочка позволила кончить себе в рот..."
            her "И ведь она все это проглотила и ей понравилось!"
            m "{size=-4}(Минуту... Она что, это выдумывает?){/size}"
            $herView.hideshowQQ( "body_64.png", pos )
            her "Я ведь тоже очень грязная девчонка..."
            g4 "Что?!"
            $herView.hideshowQQ( "body_65.png", pos )
            her "Я просто обожаю сосать члены..."
            her "Я хочу чтобы мужчина кончил мне на лицо, как в тех фильмах, которые я смотрю!"
            g4 "{size=-4}(Ах ты, маленькая шлюха! Ты сделала это!) *Аргх!*{/size}"
            $herView.hideQQ()
            show screen white 
            pause.1
            hide screen white
            pause.2
            show screen white 
            pause .1
            hide screen white
            with hpunch
            g4 "Аргх! ДА!"
            $herView.hideQQ()
            hide screen bld1
            with d3
            show screen genie_jerking_sperm
            with d3
            #pause 3
            pause
            
            $ mad = +7
            
            show screen bld1
            with d3
            $herView.showQQ( "body_47.png", pos )
            her "Я знала! Вы трогаете себя, профессор!"
            show screen genie_jerking_sperm_02
            with d3
            g4 "Что? Нет, я просто... ах, дерьмо, это просто охренительно..."
            show screen genie
            #show screen genie_jerking_off
            with d3
            $herView.hideshowQQ( "body_32.png", pos )
            her "Это отвратительно! Как вы могли!?"
            her "Сэр, вы ведь директор! Вы должны подавать хороший пример!"
            m "Эй, маленькая Мисси, ты так и будешь судить меня или тебе нужны очки?"
            $herView.hideshowQQ( "body_34.png", pos )
            her "Мои очки, пожалуйста. Я думаю, я заслужила их."
            m "Да, даже очень."
            $herView.hideshowQQ( "body_47.png", pos )
            her "Фу... Теперь я чувствую себя такой грязной..."
            hide screen genie_jerking_sperm_02
            with d3
        else:
            her "Мы должны прекратить это, профессор!"
            m "Да, конечно..."
            her "Так вы согласны со мной?"
            her "Я думаю, следует ввести систему штрафов, чтобы наказать девушек которые поступают таким нечестным образом..."
            m "(Все, что я слышу это - \"нужно наказать девочек\"...)"
            her "Так же это поможет мальчикам, так они не будут дискриминироваться!"
            m "Мальчики?"
            m "О, точно...Никому не нужны их услуги... Ублюдки."
            $herView.hideQQ()
            $herView.showQ( "body_03.png", pos, d3 )
            her "Я так рада, что вы понимаете меня, сэр."
            m "Да, да, конечно..."

    elif whoring >= 12: #LEVEL 03
        $ SetHearts(4)
        her "Сэр, вы действительно позвали меня сюда из-за этих несчастных 5 очков?"
        her "Мне жалко тратить время на болтовню, которая почти ничего не принесет."
        her "Может, мы займемся с вами чем-нибудь ....м-м... поинтереснее? В смысле, дающим больше очков?"
        menu: 
            "\"И чем же вы хотите заняться?\"":
                m "И чем же вы хотите заняться, мисс Грейнджер?"
                her "Ну, не знаю, сэр. Есть разные варианты!"
                jump new_personal_request
            "\"C каких это пор вы стали выбирать себе задания, мисс Грейнджер?":
                m "C каких это пор вы стали выбирать себе задания, мисс Грейнджер?"
                m "Кажется, это я здесь решаю какая услуга оплачивается."
                m "Так вот, сегодня оплачивается ваш рассказ."
                her "Простите, сэр! Конечно."
                m "Итак?"
                her "Ну, у меня все, как всегда. Я много учусь, сижу допоздна в библиотеке, скоро экзамены..."
                her "Потом заседания \"ОЗМП\"... Кстати, мы решили расширить нашу деятельность." 
                her "Мы будем не только защищать права мужчин, сэр."
                m "Неужели?"
                her" Мы будем последовательно выступать против несправедливости и неправды."
                if True:
                    her "Мы даже хотим теперь назвать наше общество С.Ц.У.К.О."
                    m "Что?! \"СУКИ\"?!"
                    her "Не \"суки\", сэр, а С.Ц.У.К.О. - Союз Целенаправленно и Упорно Кривду Осуждающих. Правда, с названием пока не решено..."
                    m "О, это просто замечательное название!"
                    her "Вы думаете?"
                    m "Даже не сомневайся, девочка."
                else:
                    m "Да-да, я вспомнил, вы переименовываетесь в общество су..."
                    her "Не в общество су-, сэр! А в С.Ц.У.К.О. - Союз Целенаправленно и Упорно Кривду Осуждающих. Правда, с названием все еще не решено..."
                    her "............................."
                her "Ну, вот, наверное и все."
                m "Все?"
                her "Ну, на пять очков, я уверена, что достаточно."
                m "Вы опять за свое, юная леди?"
                her "Сэр, войдите и в мое положение. Я могу рассказать вам кое-что о развратных девицах."
                her "Позволить вам трогать себя и говорить до тех пор, пока вы бурно не кончите."
                m "Но?..."
                her "Но все это должно достойно оплачиваться!"
                " и говорить о них пока вы себя"
                her "Сэр, войдите и в мое положение. Я провожу здесь полчаса своего времени и получаю пять очков. Это смешно."
                pass


        $herView.hideshowQQ( "body_12.png", pos )
        her "У меня в последнее время все вроде-как в порядке..."
        her "Хм..."
        her "Сейчас факультеты \"Слизерина\" и \"Гриффиндора\" очень сильно соперничают."
        her "И честно говоря, это совершенно неправильно..."
        her "\"Гриффиндор\" уверенно лидировал бы, если бы не \"Слизеринские\" шлюхи..."
        her "Я только и слышу, что они получают свои очки за \"услуги\"..."
        $herView.hideshowQQ( "body_04.png", pos )
        her "Очень подло!"
        m "И что же вы теперь будете делать, мисс Грейнджер?"
        $herView.hideshowQQ( "body_03.png", pos )
        her "Точно!"
        m "А?"
        $herView.hideshowQQ( "body_04.png", pos )
        her "Я должна трудится еще лучше, чтобы выровнять шансы, неравные из-за этих грязных девок..."
        $herView.hideshowQQ( "body_03.png", pos )
        her "Спасибо, что помогаете мне, профессор."
        menu: 
            "- Начать дрочить -":
                $ d_flag_01 = True #If TRUE genie jerks off under the desk.    
                $herView.hideQ()
                hide screen blktone
                with d3
                ">Вы опускаете руки под стол и обхватываете свой член..."
                hide screen blktone8
                with d3
                hide screen genie
                show screen genie_jerking_off
                with d3
                pause
                $herView.hideQQ()
                $ pos = POS_370
                $herView.showQQ( "body_14.png", pos )
                her "Профессор, что вы делаете?"
                her "Вы же не.....?"
                $herView.hideshowQQ( "body_29.png", pos )
                her "Вы...?"
                m "Ничего. Просто продолжай."
                $herView.hideshowQQ( "body_07.png", pos )
                her "Хм..."
                m "{size=-4}(Она что-то заподозрила? Да нет...){/size}"
            "- Внимательно выслушать ее -":
                $ d_flag_01 = False #NOT JERKING OFF.
                m "Не стоит благодарности."
                pass
        $herView.hideshowQQ( "body_16.png", pos )
        her "Ну, как я и сказала..."
        her "Я слышала, одна девчонка обменяла свои пикантные фотографии на десятку для факультета..."
        if d_flag_01:
            m "{size=-4}(Ну и шлюха... ах... Да...){/size}"
        else:
            m "Десять очков, да?"
        her "Да..."
        if d_flag_01:
            $herView.hideshowQQ( "body_29.png", pos )
            her "И эти две девушки..."
            her "Ходит слух, что они даже спят с профессором Снейпом..."
            m "{size=-4}(Да... Эти маленькие, грязные \"слизеринские\" шлюхи!){/size}"
            $herView.hideshowQQ( "body_45.png", pos )
            her "Еще был случай, я слышала, что ученица дрочила учителю прямо на занятии..."
            m "{size=-4}(Да... Это очень круто, продолжай!){/size}"
            $herView.hideshowQQ( "body_29.png", pos )
            her "И другая девочка, она сосала учителю!"
            m "{size=-4}(Да! Да!){/size}"
            $herView.hideshowQQ( "body_46.png", pos )
            her "А еще одна девочка позволила кончить себе в рот..."
            her "И ведь она все это проглотила и ей понравилось!"
            m "{size=-4}(Минуту... Она что, это выдумывает?){/size}"
            $herView.hideshowQQ( "body_64.png", pos )
            her "Я ведь тоже очень грязная девчонка..."
            g4 "Что?!"
            $herView.hideshowQQ( "body_65.png", pos )
            her "Я просто обожаю сосать члены..."
            her "Я хочу чтобы мужчина кончил мне на лицо, как в тех фильмах, которые я смотрю!"
            g4 "{size=-4}(Ах ты, маленькая шлюха! Ты сделала это!) *Аргх!*{/size}"
            $herView.hideQQ()
            show screen white 
            pause.1
            hide screen white
            pause.2
            show screen white 
            pause .1
            hide screen white
            with hpunch
            g4 "Аргх! ДА!"
            $herView.hideQQ()
            hide screen bld1
            with d3
            show screen genie_jerking_sperm
            with d3
            #pause 3
            pause
            
            $ mad = +7
            
            show screen bld1
            with d3
            $herView.showQQ( "body_47.png", pos )
            her "Я знала! Вы трогаете себя, профессор!"
            show screen genie_jerking_sperm_02
            with d3
            g4 "Что? Нет, я просто... ах, дерьмо, это просто охренительно..."
            show screen genie
            #show screen genie_jerking_off
            with d3
            $herView.hideshowQQ( "body_32.png", pos )
            her "Это отвратительно! Как вы могли!?"
            her "Сэр, вы ведь директор! Вы должны подавать хороший пример!"
            m "Эй, маленькая Мисси, ты так и будешь судить меня или тебе нужны очки?"
            $herView.hideshowQQ( "body_34.png", pos )
            her "Мои очки, пожалуйста. Я думаю, я заслужила их."
            m "Да, даже очень."
            $herView.hideshowQQ( "body_47.png", pos )
            her "Фу... Теперь я чувствую себя такой грязной..."
            hide screen genie_jerking_sperm_02
            with d3
        else:
            her "Мы должны прекратить это, профессор!"
            m "Да, конечно..."
            her "Так вы согласны со мной?"
            her "Я думаю, следует ввести систему штрафов, чтобы наказать девушек которые поступают таким нечестным образом..."
            m "(Все, что я слышу это - \"нужно наказать девочек\"...)"
            her "Так же это поможет мальчикам, так они не будут дискриминироваться!"
            m "Мальчики?"
            m "О, точно...Никому не нужны их услуги... Ублюдки."
            $herView.hideQQ()
            $herView.showQ( "body_03.png", pos, d3 )
            her "Я так рада, что вы понимаете меня, сэр."
            m "Да, да, конечно..."





    stop music fadeout 2.0
    
    $ gryffindor +=5
    
    $herView.hideQQ()
    $herView.showQ( None, pos, d3 )
    m "Пять очков \"Гриффиндору\" мисс Грейнджер. Отличная работа." 
    
    #$herView.showQ( "body_07.png", pos, d3 )
    hide screen hermione_01_f #Hermione stands still.
    with d3
    her "Это все?"
    if whoring >= 0 and whoring <= 2: #LEVEL 01
        her "*Вздох облегчения*"
    m "Да, можете идти."
    if IsFirstRun():
#    if request_01 == 0:
        $herView.hideshowQQ( "body_01.png", pos )
        her "Еще пять очков... Ребята будут счастливы."
        her "Спасибо, профессор."

    label request_01_done:
    if whoring <= 2:
            $ whoring +=1
 
#    $ request_01 += 1
    
    hide screen bld1
    $herView.hideQ()
    hide screen blktone 
    hide screen ctc
    with Dissolve(.3)
    
    $ walk_xpos=400 #Animation of walking chibi. (From)
    $ walk_xpos2=610 #Coordinates of it's movement. (To)
    $ hermione_speed = 02.0 #The speed of moving the walking animation across the screen.
    show screen hermione_walk_01_f 
    pause 2
    hide screen hermione_walk_01_f 
    $ renpy.play('sounds/door.mp3') #Sound of a door opening.
    with Dissolve(.3)
    
    
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
        
