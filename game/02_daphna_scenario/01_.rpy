################
### LEVEL 01 ###                
###################REQUEST_01 JUST STAND THERE.
label daphna_pre_01: #LV.1 (Whoring = 0 - 2)
    $daphne.chibi.State("door", speed=20.0).Trans("walk neardesk", "blink")
    $snape.viewMode=3
#    $snape("~snape_01", "Хелло!")
    $snape("~01", "Хелло!")


label test_daphna: #LV.1 (Whoring = 0 - 2)
    $daphne.chibi.State("door", speed=20.0).Trans("walk neardesk", "blink")

    $snape.viewMode=3
#    $snape("~snape_01", "Хелло!")
    $snape("~01", "Хелло!")

    $screens.Show(["blktone"], d3)
    $daphne.viewMode=2
    $daphne("~55 00 3 opT",  "Добрый день, профессор Дамблдор.")
    $hero  (m,              "#(О, девица вполне товарного вида. Сиськи, правда, маловаты. Интересно, есть ли заклинание, чтобы их подрастить?..)",
                            "#(Нет, джинни, остановись, ты уже подрастил сиськи принцессе... мда)",
                            "Добрый день э-э… #(Великие пески, почему он не сказал как ее зовут?).")
    $daphne("~55 00 3 opT", "Профессор Снейп сказал, ЧТО вы ХОТЕЛИ МЕНЯ видеть.")
    $hero  (                "Эм, да. Но, он же сказал зачем я хотел тебя видеть. ")
    $daphne("~55 00 3 opT", "Нет, сэр. Он не сказал.")

    menu:
        "Поговорить насчет учебы":
            $hero  (                "Что ж, мисс, я хотел поговорить насчет вашей учебы.")
            $daphne("55 00 3 opT",  "Учеба не то, что меня волнует, сэр.",
                                    "Меня гораздо больше волнует, почему в Хогвартсе обучается грязнокровое мугродье.",
                                    "Вы же чистокровный волшебник, сэр?")
            $hero  (                "Я? А, ну да. Вроде того.")
            $daphne("55 00 3 opT",  "Да, вы правильно смущаетесь.",
                                    "По древности рода с Гринграссами никто не сравнится, так что вы должны чувствовать себя неловко.",)
            $hero  (                "(Гринграссы? Что это еще за хрень?)")
            $daphne("55 00 3 opT",  "Но как бы то ни было, сэр. Вы должны проследить, чтобы  мугродье не чувствовало себя здесь вольготно.",
                                    "А вы вместо этого приглашаете новых. И чистокровные девочки должны испытывать сложности.")
            $hero  (                "Чистокровные девочки?")
            $daphne("55 00 3 opT",  "Да, сэр! Почему это грязнокровка считается лучшей на курсе?",
                                    "Как это мугродье вообще может дышать одним воздухом с истинными волшебниками?",
                    "55 00 3 opT",  "Я могу еще быть рядом со всякими Малфоями или …",
                                    "Семейки так себе, второй сорт. Но какие-никакие чистокровки, а эта девица!!")
        "Поговорить насчет факультета":
            $hero  (                "Что ж, мисс, я хотел поговорить об обстановке на факультете.")
            $daphne("55 00 3 opT",  "Обстановка на факультете, сэр? Она отвратительна!",
                                    "Грязнокровое мугродье заполонило Хогвартс.")
            $hero  (                "#(Что это за?..)")
            $daphne("55 00 3 opT",  "И вы делаете вид, что этого не знаете. Хотя ваш отец…",
                                    "Он не посрамил своей колдовской чести и прикончил троих маглов, за что его и упрятали в Азкабан.")
            $hero  (                "Неужели? #(Что за висельники в родстве с местным директором..)")
            $daphne("55 00 3 opT",  "Не притворяйтесь, что вы этого не знаете, сэр.",
                                    "А если бы не знали, это не делало бы вам чести!",
                                    "Гринграссы всегда стояли за чистоту крови и когда видишь волшебника, который предает наши идеалы…")

    $hero  (                "#(Хм, какая экспрессия! Интересно трахается она так же энергично?)",
                            "Постойте, мисс, это все очень увлекательно, но, может, уже завершим прелюдию и приступим?")
    $daphne("55 00 3 opT",  "Приступим к чему, сэр?")
    $hero  (                "Ну, к этому самому… чпоки-чпоки, тити-мити, а?")
    $daphne("55 00 3 opT",  "\"Чпоки-чпоки\", сэр?")
    $hero  (                "Ну я не знаю, как это у вас, девушек, называется.",
                            "В общем то, что вы постоянно делаете с профессором и зачем он вас сюда прислал.")
    $daphne("55 00 3 opT",  "Я не понимаю, сэр.")
    $hero  (                "О, великие пески пустыни!",
                            "#(Она небыстро шевелит мозгами. Надеюсь, что бедрами шевелит быстрее.)",
                            "Я говорю, заняться тем, чем обычно занимаются шлю… девчонки вроде вас.")
    $daphne("55 00 3 opT",  "На что это вы намекаете?!")
    $hero  (                "Я намекаю? Да я прямо говорю!...")
    $daphne("55 00 3 opT",  "Если вы смеете намекать на то, чем занимаются некоторые особы с преподавателями, то это омерзительно!")
    $hero  (                "#(Э-э, Снейп, это что, шутка?)")
    $daphne("55 00 3 opT",  "Я сегодня же пошлю сову родителям и сообщу о грязных предложениях, которые вы мне тут делаете.",
                            "А уж они донесут об этом в министерство, будьте уверены.")
    $hero  (g4,             "#(Не могу поверить... Чертов Снейп!!!)",
                            "Эм, постойте, мисс, вы неправильно поняли!")
    $daphne("55 00 3 opT",  "Я все правильно поняла! Вам недолго осталось сидеть в этом кресле!")

    $daphne.viewMode=0
    $daphne.chibi.Trans("walk door").Hide()
    $hero  (                "...")




 

  












    jump night_start
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

    $ current_payout = 5 #Used when haggling about price of th favor.

    
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
    if IsFirstRun() and hermi.whoring <=5: #First time this event taking place.
#    if request_01 == 0 and hermi.whoring <=5: #First time this event taking place.
#        $  new_request_01_01 = True #Hearts on menu buttons.
        $SetHearts(1)
        $herView.hideshowQQ( "body_11.png", pos )
        her "Эм... Ну что ж..."
        ">Гермиона смущается и слегка краснеет..."
        $herView.hideshowQQ( "body_12.png", pos )
        her "..................."
    if hermi.whoring >= 0 and  hermi.whoring <= 5: #LEVEL 01 and LEVEL 02
        if hermi.whoring >= 3 and hermi.whoring <= 5:
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
  
    elif hermi.whoring >= 6 and hermi.whoring<=11: #LEVEL 03
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
        m "Да?"
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
            
            $ hermi.liking -= 7
            
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

    elif hermi.whoring >= 12: 
        her "Сэр, вы действительно позвали меня сюда из-за этих несчастных 5 очков?"
        her "Мне жалко тратить время на болтовню, которая почти ничего не принесет."
        $herView.hideshowQQ( "body_10.png", pos )
        her "Может, мы займемся чем-нибудь ....м-м... поинтереснее?"
        her "В смысле, дающим больше очков?"
        menu: 
            "\"И чем же вы хотите заняться?\"":
                m "И чем же вы хотите заняться, мисс Грейнджер?"
                $herView.hideshowQQ( "body_68.png", pos )
                her "Ну, не знаю, сэр. Есть разные варианты!"
                jump new_personal_request
            "\"C каких это пор вы стали выбирать себе задания, мисс Грейнджер?":
                $ SetHearts(4)
                m "C каких это пор вы стали выбирать себе задания, мисс Грейнджер?\""
                m "Кажется, это я здесь решаю какая услуга оплачивается."
                m "Так вот, сегодня оплачивается ваш рассказ."
                $herView.hideshowQQ( "body_202.png", pos )
                her "Простите, сэр! Конечно."
                m "Итак?"
                $herView.hideshowQQ( "body_93.png", pos )
                her "Ну, у меня все, как всегда. Я много учусь, сижу допоздна в библиотеке, скоро экзамены..."
                her "Потом заседания \"ОЗМП\"... "
                her "Кстати, мы решили распространить нашу деятельность дальше!" 
                her "Мы станем не только защищать права мужчин, сэр."
                m "Неужели?"
                her" Мы будем последовательно выступать против несправедливости и неправды!"
                if not this.flag_SCUKO_presented:
                    $this.flag_SCUKO_presented=True
                    her "Мы хотим теперь назвать наше общество С.Ц.У.К.О."
                    g4 "Что?! \"СУКИ\"?!"
                    $herView.hideshowQQ( "body_05.png", pos )
                    her "Не \"суки\", сэр!  С.Ц.У.К.О.!"
                    her "\"Союз Целенаправленно и Упорно Кривду Осуждающих!\""
                    $herView.hideshowQQ( "body_12.png", pos )
                    her "Правда, с названием пока не решено..." #Цель
                    g9 "О, это просто замечательное название!"
                    $herView.hideshowQQ( "body_208.png", pos )
                    her "Вы думаете?"
                    g9 "Даже не сомневайся, девочка."
                else:
                    g9 "Да-да, я вспомнил, вы переименовываетесь в общество су..."
                    $herView.hideshowQQ( "body_30.png", pos )
                    her "Не в общество су-, сэр! А в С.Ц.У.К.О.!"
                    her "Союз Целенаправленно и Упорно Кривду Осуждающих!"
                    $herView.hideshowQQ( "body_12.png", pos )
                    her "Правда, с названием все еще не решено..."
                    her "............................."
                $herView.hideshowQQ( "body_16.png", pos )
                her "Ну, вот, наверное и все."
                m "Все?"
                if not end.IsEnding(const_ENDING_STRONG_GIRL):
                    her "Да, сэр. Прошу заплатить мне и я пойду - у меня дела."
                    m "Хм... сегодня вы не в ударе, мисс Грейнджер."
                    $herView.hideshowQQ( "body_14.png", pos )
                    her "Ну, профессор, вы просили рассказать, я рассказала. Если бы вы попросили другую услугу..."
                    m "Хорошо, хорошо..."
                else:
                    $herView.hideshowQQ( "body_14.png", pos )
                    her "Ну, на пять очков, я уверена, что достаточно."
                    m "Вы опять за свое, юная леди?"
                    $herView.hideshowQQ( "body_102.png", pos )
                    her "Сэр, войдите и в мое положение. Я готова рассказать вам кое-что о развратных девицах..."
                    $herView.hideshowQQ( "body_189.png", pos )
                    her "И чтобы вы себя трогали..." 
                    $herView.hideshowQQ( "body_101.png", pos )
                    her "И могу даже говорить до тех пор, пока вы бурно не кончите."
                    m "Но?..."
                    $herView.hideshowQQ( "body_58.png", pos )
                    her "Но все это должно достойно оплачиваться!"
                    m "А вы становитесь корыстны, мисс Грейнджер."
                    her "Ничуть, сэр. Я просто знаю себе цену. И дополнительные 15 очков за рассказ о развратных девках - вполне справедливая плата."
                    menu: 
                        "\"Нет!\"":
                            m "Вы свободны, мисс Грейнджер!"
                            her "Как скажете, сэр. В таком случае, я хотела бы получить свою оплату."
                        "\"Хорошо, еще 15 очков. Рассказывай!":
                            $current_payout+=15
                            m "Ладно, я заплачу тебе. Рассказывай!"
                            $herView.hideshowQQ( "body_102.png", pos )
                            her "Да, сэр. И вы можете приступать к дрочке."
                            m "Черт бы тебя подрал, девчонка! Я сам решу когда и что мне делать."
                            $herView.hideshowQQ( "body_13.png", pos )
                            her "Простите, профессор."
                            her "Ну, я слышала, как две девочки разговаривали в спальне, как они берут в рот у парней."
                            $herView.hideshowQQ( "body_50.png", pos )
                            her "Конечно же, они не из Гриффиндора, сэр!"
                            m "Разумеется. Гриффиндорские девчонки ничего не берут в рот."
                            $herView.hideshowQQ( "body_120.png", pos )
                            her "Все так и есть, сэр. Мы слишком горды для этого и..."
                            m "Мисс Грейнджер!"
                            $herView.hideshowQQ( "body_55.png", pos )
                            her "Сэр?"
                            m "Это так вы зарабатываете 15 очков?"
                            her "Простите, сэр!.. Ну вот, одна из них, блондинка, рассказывала, что ее парень кончает так много, что у нее даже льется из носа."
                            $herView.hideshowQQ( "body_55.png", pos )
                            her "Ну, если по правде, сэр, она просто бахвалилась перед брюнеткой."
                            her "Там не так уж много спермы, просто она специально напрягалась, чтобы сперма попала в нос."
                            m "Откуда вы это знаете, мисс Грейнджер?"
                            m "Вы тоже принимали в этом участие?"
                            $herView.hideshowQQ( "body_103.png", pos )
                            her "Нет, сэр, я не занимаюсь таким! Просто я знаю... У меня свои источники."
                            m "Источники спермы? Хе-хе."
                            $herView.hideshowQQ( "body_30.png", pos )
                            her "Аргх! Если вы еще что-нибудь такое скажете, сэр, я просто уйду."
                            m "Мисс Грейнджер! Вы обещали мне рассказать нечто особенное, но пока я ничего такого не слышал."
                            m "Еще немного, я окончательно разочаруюсь в вас, и вы вообще не получите очков."
                            $herView.hideshowQQ( "body_28.png", pos )
                            her "Просто не сбивайте меня, сэр. Хорошо?"
                            $herView.hideshowQQ( "body_56.png", pos )
                            her "Ну вот... Одна девочка призналась мне, что ей нравится ходить без белья."
                            her "Когда она идет по лестнице и парни смотрят снизу ей под юбку, она чувствует... она возбуждается, сэр."
                            m "{size=-4}(О-о, это уже лучше...){/size}"

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

                            $herView.hideshowQQ( "body_122.png", pos )
                            her "Есть еще одна девчонка..."
                            her "Когда она была в Хогсмеде, она делала кое-что с карликом..."
                            m "{size=-4}(Ну и шлюха... ах... Да...){/size}"
                            her "И еще две девушки..."
                            $herView.hideshowQQ( "body_187.png", pos )
                            her "Они мастурбировали друг дружку на перемене. И парни на это смотрели. Это просто отвратительно, профессор!"
                            m "{size=-4}(О, д-да-а... Наверняка это было зрелище!){/size}"
                            $herView.hideshowQQ( "body_118.png", pos )
                            her "И потом та девчонка. Говорят, она ходит, засунув морковку в свою за... Ну, вы понимаете, меня."
                            her "Вроде как, она так разрабатывает... чтобы в нее было легче входить..."
                            m "{size=-4}(Да... вот ведь шлюха... прилежная шлюха... Продолжай!){/size}"
                            $herView.hideshowQQ( "body_68.png", pos )
                            her "И другая девочка, она дрочила сразу двоим..."
                            m "{size=-4}(Да! Да!){/size}"
                            $herView.hideshowQQ( "body_56.png", pos )
                            her "А потом опустилась на колени и взяла в рот у третьего..."
                            m "{size=-4}(Ох, шлюх-ха, я сейчас... уже...){/size}"
                            $herView.hideshowQQ( "body_122.png", pos )
                            her "На этом все, профессор."
                            g4 "Что?!"
                            $herView.hideshowQQ( "body_111.png", pos )
                            her "Вы мне платите 15 баллов за рассказ. Но кончить стоит еще столько же."
                            g4 "Мелкая дрянь!"
                            menu: 
                                "\"Ничего не получишь!\"":
                                    with d3
                                    hide screen genie_jerking_off
                                    show screen genie
                                    with d3
                                    m "Ничего не получишь!"
                                    m "Ни одного балла!"
                                    $herView.hideshowQQ( "body_05.png", pos )
                                    her "Очень хорошо, профессор! В таком случае не ждите, что я и дальше буду удовлетворять ваши прихоти!"
                                    $hermi.liking -= 30
                                    jump request_01_done
                                "\"Ладно. На этом все...\"":
                                    m "Аргх! Ну что ж, все... Хватит."
                                    with d3
                                    hide screen genie_jerking_off
                                    show screen genie
                                    with d3
                                    $herView.hideshowQQ( "body_04.png", pos )
                                    her "Как скажете, сэр. Я готова получить свои [current_payout] очков."
                                "\"Продолжай, будут тебе очки!\"":
                                    $current_payout+=15
                                    m "Не останавливайся, я дам тебе очки! Продолжай!"
                                    $herView.hideshowQQ( "body_127.png", pos )
                                    her "Да, сэр. Эти шлюхи, сэр, они каждый день сосут у пары парней и просят кончать им на лицо."
                                    her "И ходят с лицом, измазанным спермой. Они говорят, что это хорошо влияет на кожу."
                                    m "{size=-4}(Да, давай,... продолжай!){/size}"
                                    her "И слизеринские девки пообещали парням из квиддишной команды, что будут неделю будить их минетом, если они выиграют."
                                    her "И еще, сэр, рассказывали как одна девушка дрочила одному преподавателю..." 
                                    her "А потом тут же пошла дрочить другому..."
                                    m "{size=-4}(О, да-а-а,... эти шлюхи!){/size}"
                                    $herView.hideshowQQ( "body_78.png", pos )
                                    her "И потом, я слышала, появилась новая игра. Она называется \"Угадай дырку\"."
                                    m "{size=-4}(Угадай... ах-х... да....){/size}"
                                    $herView.hideshowQQ( "body_58.png", pos )
                                    her "В деревянной перегородке делают дырки ниже пояса, где несколько девчонок выставляют свои..."
                                    her "Прелести, сэр. И если парень угадал кто это..."
                                    m "{size=-4}(О, да... да... я уже... УЖЕ!){/size}{size=+2}*АРГХ!*{/size}"
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
                                    
                                    $MusicStart("Supergirl")                                   
                                    show screen bld1
                                    with d3
                                    $herView.showQQ( "body_64.png", pos )
                                    her "О-о, вы так мощно кончаете, профессор! Вам понравилось?"
                                    show screen genie_jerking_sperm_02
                                    with d3
                                    g4 "Ах, дерьмо, это так... Это невероятно охренительно!..."
                                    show screen genie
                                    #show screen genie_jerking_off
                                    with d3
                                    $herView.hideshowQQ( "body_111.png", pos )
                                    her "Я рада профессор, что вы кончаете. И все же, могу я получить свои очки? Всего [current_payout] очков."
                                    m "Ох-х... Уффф... Да, можешь... но"
                                    m "...что там с игрой \"Угадай дырку\"? Ты так и не дорассказала."
                                    $herView.hideshowQQ( "body_46.png", pos )
                                    her "Вы же и так кончили, сэр. Но если вы хотите узнать..."
                                    m "Что?! Ты опять вымогаешь очки?"
                                    her "Всего 15 очков, сэр."
                                    m "Ты зарываешься, девчонка!"
                                    $herView.hideshowQQ( "body_58.png", pos )
                                    her "Простите, сэр, тогда я просто получу свои [current_payout] очков и пойду."
                                    menu: 
                                        "\"Иди прочь!\"":
                                            m "Иди прочь. И помни, со мной шантаж не пройдет!"
                                            $herView.hideshowQQ( "body_58.png", pos )
                                            her "Да, сэр..."
                                        "\"Ладно. +15 очков, рассказывай. Но это в последний раз!\"":
                                            $current_payout+=15
                                            m "Хорошо, но помни, это в последний раз!"
                                            $herView.hideshowQQ( "body_64.png", pos )
                                            her "Конечно, я все понимаю."
                                            $herView.hideshowQQ( "body_56.png", pos )
                                            her "В общем, если парень угадывает чья это..."
                                            her "Гхм... в общем, угадывает чье это, то девчонка должна дать ему так, как он захочет."
                                            her "А если не угадывает, то он становится общим на целую ночь."
                                            m "Общим?"
                                            her "Да, сэр. Девчонки забирают его в свою спальню и он должен делать для них все."
                                            m "?!..."
                                            $herView.hideshowQQ( "body_122.png", pos )
                                            her "{size=+4}АБСОЛЮТНО{/size} все, что каждая из них скажет, сэр!"
                                            m "Вот дерьмо!"
                                            her "Профессор, по-моему у вас опять встает. Если вы хотите, продолжить, то всего 15 оч..."
                                            m "Нет!!! На сегодня достаточно!"
                                            $herView.hideshowQQ( "body_58.png", pos )
                                            her "Конечно, профессор."
                                    her "...................."
                                    hide screen genie_jerking_sperm_02
                                    with d3
                                    $MusicStop()




    stop music fadeout 2.0
    
#    $ gryffindor +=5
    $ gryffindor += current_payout
    
    $herView.hideQQ()
    $herView.showQ( None, pos, d3 )
    m "[current_payout] очков \"Гриффиндору\" мисс Грейнджер. Отличная работа." 
    
    #$herView.showQ( "body_07.png", pos, d3 )
    hide screen hermione_01_f #Hermione stands still.
    with d3
    her "Это все?"
    if hermi.whoring >= 0 and hermi.whoring <= 2: #LEVEL 01
        her "*Вздох облегчения*"
    m "Да, можете идти."
    if IsFirstRun():
#    if request_01 == 0:
        $herView.hideshowQQ( "body_01.png", pos )
        her "Еще [current_payout] очков... Ребята будут счастливы."
        her "Спасибо, профессор."

    label request_01_done___:
    if hermi.whoring <= 2:
            $ hermi.whoring +=1
 
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

    if current_payout>=35:
        m "................................."
        m "\"Угадай дырку\", надо же..." 
        m "Чего только не придумают эти шлюхи!"
        $posHead=gMakePos( 390, 235 )
    
    
    ### MUSIC BLOCK ###
    if daytime:
        play music "music/Brittle Rille.mp3" fadein 1 fadeout 1 # DAY MUSIC
    else:
        play music "music/Music for Manatees.mp3" fadein 1 fadeout 1 # NIGHT MUSIC
    ### END OF BLOCK ###

    $event.Finalize()    
    if daytime:
        $ hermione_takes_classes = True
        jump day_main_menu
    else:
        $ hermione_sleeping = True
        jump night_main_menu
        
