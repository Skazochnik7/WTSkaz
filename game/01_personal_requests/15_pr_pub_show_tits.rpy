###################REQUEST_15 (Level 04) (35 pt.) (Flash your tits to a boy). (Available during daytime only).
label new_request_15: #LV.4 (Whoring = 9 - 11)
    
    
    
    $herView.hideQQ()
    m "{size=-4}(Сказать ей показать сиськи одному из одноклассников?){/size}"
    $ menu_x = 0.5 #Default position of the menu (0.5). Version B is $ menu_x = 0.2
    menu:
        "\"(Да, давай сделаем это!)\"":
            pass
        "\"(Не сейчас.)\"":
            $event.NotFinished()
            jump new_personal_request
            
    
    $ pos = POS_140
    
    if request_15_points == 0: # <================================================================================ FIRST TIME
        m "Мисс Грейнджер..."
        m "Сегодня мне бы хотелось подарить \"Гриффиндору\" 25 очков."
        $herView.hideshowQQ( "body_01.png", pos )
        her "Серьезно?"
        her "Спасибо, сэр!"
        m "Да, но сначала мне нужна твоя помощь..."
        her "Конечно, сэр! Все что угодно!"
        m "Мне нужно, чтобы ты вышла наружу и показала кому-нибудь свои сиськи..."
        stop music fadeout 1.0
        $herView.hideshowQQ( "body_02.png", pos )
        her "...?"
        m "Ну, знаешь, оголила грудь перед парнями..."
        $herView.hideshowQQ( "body_48.png", pos )
        her "?!!"
        if hermi.whoring <=8 or request_10_points <= 1: # request_10_points - counts how many times Hermione been sent to let boys touch her.
            jump too_much
        her "Профессор Дамблдор!"
        $herView.hideshowQQ( "body_47.png", pos )
        play music "music/Chipper Doodle v2.mp3" fadein 1 fadeout 1 # HERMIONE'S THEME.
        her "Это совершенно новый уровень неприемлимости! Даже для вас, сэр!"
        her "Как вы можете давать такие задания одной из своих учениц?"
        m "Так вот значит, как ты заговорила? Понятно..."
        m "Наверное, я подарю эти очки какому-нибудь другому факультету..."
        m "Может быть \"Слизерину\"?"
        $herView.hideshowQQ( "body_66.png", pos )
        her "................"
        m "Ты ведь знаешь, никакого давления..."
        $herView.hideshowQQ( "body_69.png", pos )
        her "Профессор..."
        her "Судьба моего факультета важна для меня, но..."
        m "Да ну?"
        m "Почему тогда я этого не замечаю?"
        m "Действительно, покажите мне, насколько она значима для вас, мисс Грейнджер."
        $herView.hideshowQQ( "body_47.png", pos )
        her "Но ведь это неприемлимо..."
        m "А в том ли мы положении, чтобы обсуждать что приемлимо, а что - нет?"
        $herView.hideshowQQ( "body_69.png", pos )
        her ".................."
        m "Я бы сказал, что поезд давно ушел..."
        $herView.hideshowQQ( "body_66.png", pos )
        her ".............."
        m "Все, что я прошу тебя сделать - это всего лишь дать какому-нибудь счастливцу взглянуть одним глазком..."
        $herView.hideshowQQ( "body_69.png", pos )
        her "Но почему? Почему я должна делать такие вещи?"
        m "Минута твоего времени за 35 очков..."
        m "Отличная сделка, ты не находишь?"
        her "Наверное..."
        her "Ладно, я посмотрю, что я могу сделать..."
        
    else: # <================================================================================ NOT FIRST TIME
        if hermi.whoring >= 9 and hermi.whoring <= 11: # LEVEL 04 FIRST EVENT.
            m "Я думаю, что тебе нужно показывать свои сиськи почаще, девочка."
            $herView.hideshowQQ( "body_44.png", pos )
            her "В смысле вам, сэр?"
            m "Нет, своим одноклассникам..."
            $herView.hideshowQQ( "body_117.png", pos )
            her "Ох..."
            m "Точно, иди и сделай это и приходи ко мне с отчетом..."
            $herView.hideshowQQ( "body_69.png", pos )
            her "Мне заплатят за это?"
            m "Конечно тебе заплатят за это, глупышка."
            m "Тридцать пять очков. Обычная ставка..."
            $herView.hideshowQQ( "body_69.png", pos )
            her "................."
            $herView.hideshowQQ( "body_66.png", pos )
            her "Что ж, ладно... Я посмотрю, что я смогу сделать, сэр..."
            
        elif hermi.whoring >= 12 and hermi.whoring <= 14: # LEVEL 05
            m "Мисс Грейнджер. У меня к вам вопрос."
            play music "music/Chipper Doodle v2.mp3" fadein 1 fadeout 1 # HERMIONE'S THEME.
            m "Как вы думаете, зачем женщине грудь?"
            $herView.hideshowQQ( "body_44.png", pos )
            her "...что вы имеете в виду, сэр?"
            m "Хорошо, давайте я перефразирую..."
            m "Назовите наиболее распространенную функцую женских молочных желез?"
            $herView.hideshowQQ( "body_15.png", pos )
            her "Ох..."
            $herView.hideshowQQ( "body_17.png", pos )
            her "Производство молока?"
            m "Хорошо. Как еще женщина может использовать свои сиськи?"
            $herView.hideshowQQ( "body_13.png", pos )
            her "Хм.."
            $herView.hideshowQQ( "body_17.png", pos )
            her "...привлекать мужчин?"
            m "Да. Давайте сосредоточимся на этом."
            m "Я хочу, чтобы вы вышли отсюда..."
            m "Нашли какого-нибудь удачливого ублюдка..."
            m "И показали ему сиськи..."
            $herView.hideshowQQ( "body_66.png", pos )
            her "{size=-3}(Я знала к чему идет этот разговор...){/size}"
            m "Что это было, мисс Грейнджер?"
            $herView.hideshowQQ( "body_69.png", pos )
            her "Я сказала, что тогда я лучше пойду, сэр."
            her "Мои занятия вот-вот начнутся..."
            m "Тридцать пять очков будут ждать вас по возвращению, сударыня."
            $herView.hideshowQQ( "body_79.png", pos )
            her ".............."
            
        elif hermi.whoring >= 15: # LEVEL 06+
            m "Девочка, мне нужно, чтобы ты вышла отсюда и показала сиськи какому-нибудь однокласснику."
            $herView.hideshowQQ( "body_127.png", pos )
            her "Я постараюсь, сэр."
            m "Серьезно? Так просто? Никаких возражений?"
            $herView.hideshowQQ( "body_128.png", pos )
            her "Мне ведь заплатят за это, ведь так?"
            m "Конечно."
            $herView.hideshowQQ( "body_127.png", pos )
            her "Тогда почему я должна отказываться от такого простого задания, как это?"
            her "Тридцать пять очков - честная цена за пару секунд удовольствия... эммм..."
            $herView.hideshowQQ( "body_74.png", pos )
            her "...в смысле, неудобства."
            m "{size=-3}(Она настолько изменилась?){/size}"
            g9 "{size=-3}(Я настолько хорош в тренировках, что это начинает пугать!){/size}"
            $herView.hideshowQQ( "body_45.png", pos )
            her "Занятия вот-вот начнутся... Я, пожалуй, пойду."
            her "До вечера, сэр."

    

    
    $ request_15 = True

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

    call music_block
    
    $ hermione_takes_classes = True
    
    $event.Finalize()    

    jump day_main_menu
    
    
    
    

        



label new_request_15_complete:
    
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

    if hermi.whoring >= 9 and hermi.whoring <= 11: # LEVEL 04 <=============================================================EVENT LEVEL 01                    
        if one_out_of_three == 1: ### EVENT (A)
                

                $herView.showQ( "body_31.png", pos )
                show screen hermione_02
                with Dissolve(.3)
                her "Добрый вечер, сэр..."
                m "Мисс Грейнджер..."
                m "Ну, как все прошло?"
                $herView.hideshowQQ( "body_34.png", pos )
                her "Эм... Если честно, не слишком хорошо..."
                her "................................"
                m "Просто расскажите мне, что произошло."
                $herView.hideshowQQ( "body_31.png", pos )
                her "В том то и дело, сэр..."
                her "Ничего не произошло..."
                $herView.hideshowQQ( "body_87.png", pos )
                her "Я просто не смогла заставить себя сделать это..."
                m "Понятно..."
                m "Ну, я не могу раздавать очки просто так, сударыня."
                $herView.hideshowQQ( "body_16.png", pos )
                her "Конечно, сэр... Я понимаю..."
                $herView.hideshowQQ( "body_29.png", pos )
                her "Я буду больше стараться в следующий раз... Я обещаю..."
                m "Тогда, пока я просто отложу эти тридцать пять очков для вас..."
                $herView.hideshowQQ( "body_29.png", pos )
                her "Спасибо, сэр..."
                her "..."
                her "Я, пожалуй, пойду."
                $ request_15 = False 
                $ hermione_sleeping = True
                $ request_15_points += 1 
                jump could_not_flirt #Sent here when choose "Favor failed! No points for you!" (Hermione is leaving without getting any points).

        elif one_out_of_three == 2: ### EVENT (B)
            m "Мисс Грейнджер, вы завершили свое задание?"
            play music "music/Chipper Doodle v2.mp3" fadein 1 fadeout 1 # HERMIONE'S THEME.
            $herView.hideshowQQ( "body_29.png", pos )
            her "Эм... Вроде того..."
            m "Вроде того?"
            $herView.hideshowQQ( "body_31.png", pos )
            her "Да... эм..."
            her "Ну, я решила поробовать показать их тому парню из \"Пуффендуя\"..."
            $herView.hideshowQQ( "body_87.png", pos )
            her "Я ждала подходящего момента..."
            her "Я волновалась, что что-нибудь пойдет не так..."
            $herView.hideshowQQ( "body_69.png", pos )
            her "И, конечно, все что могло произойти - произошло..."
            $herView.hideshowQQ( "body_31.png", pos )
            her "Когда я попыталась раздеться перед ним..."
            her "Сначала я подняла свою жилетку..."
            her "Затем, когда я попыталась поднять мою рубашку..."
            her "Одна из грудей застряла в ткани и поднялась вместе с рубашкой..."
            $herView.hideshowQQ( "body_32.png", pos )
            her "Так что только одна из моих грудей была обнажена. Я отчаянно пыталась освободить вторую, но..."
            her "Я начала привлекать внимание остальных учеников..."
            her "Так что мне пришлось быстро одернуть одежду..."
            her "И момент был упущен..."
            $herView.hideshowQQ( "body_33.png", pos )
            her "............"
            m "Хм..."
            m "Что насчет того парня? Он увидел твои сиськи?"
            $herView.hideshowQQ( "body_31.png", pos )
            her "Ну, я думаю, что он мог увидеть одну..."
            her "Но, судя по выражению его лица..."
            her "Я сомневаюсь, что он понял, что все это было для него."
            $herView.hideshowQQ( "body_29.png", pos )
            her "......................"
            $herView.hideshowQQ( "body_31.png", pos )
            her "Простите, сэр..."
            m "Все хорошо..."
            m "Я и не ожидал, что у тебя будет все получаться идеально в начале твоей тренировки..."
            $herView.hideshowQQ( "body_117.png", pos )
            her "(Моей тренировки?)"
            
        elif one_out_of_three == 3: ### EVENT (C)
            play music "music/Chipper Doodle v2.mp3" fadein 1 fadeout 1 # HERMIONE'S THEME.
            m "Мисс Грейнджер, вы выполнили свое задание?"
            show screen blktone
            with d3
            $herView.hideshowQQ( "body_29.png", pos )
            her "Выполнила, сэр."
            m "Хорошо. Расскажите мне больше."
            $herView.hideshowQQ( "body_31.png", pos )
            her "Эм... На самом деле, тут особо нечего рассказывать..."
            her "Первую половину дня я провела в библиотеке..."
            her "Обычно в такое время там почти никого нет..."
            her "Кроме меня там был только один ученик..."
            $herView.hideshowQQ( "body_120.png", pos )
            her "Какой-то парень из \"Когтеврана\"..."
            her "Я помахала ему, и когда он посмотрел на меня..."
            $herView.hideshowQQ( "body_117.png", pos )
            her "Я быстро подняла свою рубашку..."
            m "Хорошая работа."
            m "Как он отреагировал на ваши обнаженные сиськи?"
            $herView.hideshowQQ( "body_118.png", pos )
            her "Я не уверена..."
            $herView.hideshowQQ( "body_117.png", pos )
            her "Он был несколько шокирован, я полагаю..."
            $herView.hideshowQQ( "body_118.png", pos )
            her "После того, как я показала ему грудь, мне было слишком неудобно оставаться там..."
            $herView.hideshowQQ( "body_117.png", pos )
            her "Поэтому, я просто собрала все свои книги и ушла..."
            m "Ясно..."
            
    elif hermi.whoring >= 12 and hermi.whoring <= 14: # LEVEL 05 <=============================================================EVENT LEVEL 02
        if one_out_of_three == 1: ### EVENT (A)
            stop music fadeout 1.0
            show screen blktone
            with d3
            m "Мисс Грейнджер. Вы выполнили свое задание?"
            $herView.hideshowQQ( "body_44.png", pos )
            her "Да сэр, выполнила."
            $herView.hideshowQQ( "body_118.png", pos )
            her "............."
            m "Ну? Как все прошло?"
            $herView.hideshowQQ( "body_118.png", pos )
            her "................"
            $herView.hideshowQQ( "body_69.png", pos )
            play music "music/Chipper Doodle v2.mp3" fadein 1 fadeout 1 # HERMIONE'S THEME.
            her "Просто для справки, сэр..."
            m "Хм?"
            $herView.hideshowQQ( "body_30.png", pos )
            her "Я думаю, что заставлять своих учеников делать подобные вещи..."
            $herView.hideshowQQ( "body_120.png", pos )
            her "Это ниже такого уважаемого мага, как вы..."
            m "\"Заставлять\"? Никто не заставлял тебя ничего делать, моя девочка."
            m "Ты сама пришла ко мне, помнишь?"
            $herView.hideshowQQ( "body_31.png", pos )
            her ".........."
            m "Ты умоляла меня купить твои сексуальные услуги."
            $herView.hideshowQQ( "body_29.png", pos )
            her "...Я...."
            $herView.hideshowQQ( "body_31.png", pos )
            her "Я не говорила \"сексуальные\"..."
            m "Так или иначе, вы можете прекратить продавать мне эти услуги в любой момент, мисс Грейнджер."
            $herView.hideshowQQ( "body_69.png", pos )
            her "Наверное..."
            m "Но вы по-прежнему продолжаете приходить снова и снова..."
            $herView.hideshowQQ( "body_118.png", pos )
            her "............................"
            m "Быть может, на самом деле вы получаете от этого какую-то извращенную форму удовольствия?"
            $herView.hideshowQQ( "body_47.png", pos )
            her "Что?"
            m "Как вам не стыдно, мисс Грейнджер! Как вам не стыдно!"
            $herView.hideshowQQ( "body_47.png", pos )
            her "Сэр, я бы никогда...!"
            m "Хватит. Вы выполнили задание, или нет?"
            $herView.hideshowQQ( "body_120.png", pos )
            her "Да, выполнила..."
            m "И?"
            $herView.hideshowQQ( "body_87.png", pos )
            her "И это все что я могу сказать..."
            $herView.hideshowQQ( "body_120.png", pos )
            her "........"
            m ".........."
            her "........"
            m "Ай, плевать. Забирай свои очки и проваливай."
            $herView.hideshowQQ( "body_120.png", pos )
            her "Спасибо, сэр."

        elif one_out_of_three == 2: ### EVENT (B)
            play music "music/Chipper Doodle v2.mp3" fadein 1 fadeout 1 # HERMIONE'S THEME.
            m "Мисс Грейнджер..."
            $herView.hideshowQQ( "body_33.png", pos )
            her "Добрый вечер, сэр..."
            m "Вы выполнили задание?"
            $herView.hideshowQQ( "body_31.png", pos )
            her "Да, выполнила, сэр..."
            $herView.hideshowQQ( "body_33.png", pos )
            her ".........."
            m "................"
            her "..............."
            m "И??"
            $herView.hideshowQQ( "body_31.png", pos )
            her "Могу я получить плату, пожалуйста?"
            m "После того как расскажите, чем именно вы занимались сегодня."
            $herView.hideshowQQ( "body_33.png", pos )
            her "...................."
            $herView.hideshowQQ( "body_31.png", pos )
            her "Я правда обязана рассказывать об этом, сэр?"
            m "Когда ты вот так выворачиваешься..."
            m "Ты только будишь мое любопытство. Ты же знаешь об этом, ведь так?"
            $herView.hideshowQQ( "body_117.png", pos )
            her "Ууу..."
            $herView.hideshowQQ( "body_118.png", pos )
            her "Нуу... Эмм..."
            her "Хорошо, вот как все было..."
            $herView.hideshowQQ( "body_32.png", pos )
            her "Я показала сиськи тому \"Слизеринскому\" младшекласснику в коридоре..."
            her "Но я стояла слишком близко к нему..."
            $herView.hideshowQQ( "body_33.png", pos )
            her "...."
            her "...."
            $herView.hideshowQQ( "body_31.png", pos )
            her "Ну, он схватился за одну из моих грудей, сэр..."
            her "...он сжал ее и не отпускал..."
            $herView.hideshowQQ( "body_117.png", pos )
            her "Он заставил меня пообещать встретиться с ним после занятий..."
            her "И дать ему..."
            $herView.hideshowQQ( "body_131.png", pos )
            her "...еще немного \"поиграть с моими сиськами\"..."
            $herView.hideshowQQ( "body_118.png", pos )
            her "Вот видите, почему я ненавижу \"Слизеринских\" парней, сэр..."
            her "У них нет и тени чести.."
            her "..."
            m "Ты сдержала свое обещание?"
            $herView.hideshowQQ( "body_117.png", pos )
            her "Нет, еще нет..."
            her "Я собираюсь встретиться с этим отвратительным парнем после того, как мы закончим здесь, сэр."
            m "Понятно..."
            m "Ну, тогда мы не должны заставлять того парня долго ждать, ведь так?"
            
        elif one_out_of_three == 3: ### EVENT (C)
            m "Мисс Грейнджер, вы выполнили свое задание?"
            show screen blktone 
            with d3
            $herView.hideshowQQ( "body_14.png", pos )
            her "Выполнила, сэр..."
            m "Я слушаю..."
            $herView.hideshowQQ( "body_31.png", pos )
            her "Ну..."
            her "Мне пришлось провести большую часть дня в библиотеке..."
            her "Так что у меня не было времени выполнить ваше задание как полагается, сэр..."
            m "Хм...?"
            play music "music/(Orchestral) Playful Tension by Shadow16nh.mp3" fadein 1 fadeout 1 # SEX THEME.
            her "Вместо этого я просто подошла к окну в библиотеке, и..."
            $herView.hideshowQQ( "body_118.png", pos )
            her "...и просто подняла рубашку и прижалась обнаженной грудью к стеклу..."
            her "И простояла так несколько секунд..."
            her "Чтобы убедиться, что хоть кто-нибудь увидит меня снаружи..."
            $herView.hideshowQQ( "body_117.png", pos )
            her "Надеюсь, что это тоже считается..."
            m "Хм..."
            m "Как думаешь, сколько учеников увидели, что ты стоишь за тем окном?"
            $herView.hideshowQQ( "body_118.png", pos )
            her "Я не уверена, сэр... Наверное один или два...?"
            m "\"Наверное\"?"
            $herView.hideshowQQ( "body_182.png", pos )
            her "Я не знаю, сэр..."
            her "Если честно, я держала глаза закрытыми..."
            m "Тогда откуда ты знаешь, что хоть кто-то тебя увидел, а?"
            $herView.hideshowQQ( "body_141.png", pos )
            her "Я услышала, что кто-то крикнул: \"Глядите! Вон там, в окне!\"."
            her "Когда я услышала это, я поправила одежду и быстро ушла..."
            $herView.hideshowQQ( "body_117.png", pos )
            her "...."
            m "Хм..."
            m "Ну ладно... Думаю, что это считается..."

    elif hermi.whoring >= 15: # LEVEL 06+ <=============================================================EVENT LEVEL 03
        if one_out_of_three == 1: ### EVENT (A)
            m "Мисс Грейнджер, вы выполнили задание?"
            show screen blktone
            with d3
            $herView.hideshowQQ( "body_45.png", pos )
            her "Выполнила, сэр..."
            m "Я слушаю..."
            $herView.hideshowQQ( "body_44.png", pos )
            her "Ну... Мне пришлось провести большую часть дня в библиотеке......"
            her "Так что у меня не было времени выполнить ваше задание как полагается, сэр..."
            m "Хм...?"
            $herView.hideshowQQ( "body_117.png", pos )
            her "Вместо этого, я просто подошла к окну в библиотеке, и..."
            play music "music/(Orchestral) Playful Tension by Shadow16nh.mp3" fadein 1 fadeout 1 # SEX THEME.
            her "...подняла рубашку и прижалась обнаженной грудью к стеклу..."
            $herView.hideshowQQ( "body_31.png", pos )
            her "Я простояла так некоторое время..."
            $herView.hideshowQQ( "body_87.png", pos )
            her "Вскоре, со двора меня стали замечать..."
            her "Вряд ли они могли увидеть мое лицо..."
            $herView.hideshowQQ( "body_118.png", pos )
            her "По крайней мере, я надеюсь..."
            $herView.hideshowQQ( "body_117.png", pos )
            her "Но они определенно видели мою грудь, прижатую к холодному оконному стеклу, сэр..."
            $herView.hideshowQQ( "body_118.png", pos )
            her "Вскоре, собралась небольшая толпа..."
            $herView.hideshowQQ( "body_121.png", pos )
            her "Люди кричали и подбадривали меня, показывали на мою обнаженную грудь..."
            $herView.hideshowQQ( "body_87.png", pos )
            her "Затем я увидела, как несколько парней побежали ко входу в библиотеку..."
            $herView.hideshowQQ( "body_117.png", pos )
            her "Мне пришлось быстро уйти, чтобы меня не обнаружили..."
            m "Хм..."
            m "Как вы думаете, сколько людей сегодня увидели ваши сиськи, мисс Грейнджер?"
            $herView.hideshowQQ( "body_31.png", pos )
            her "Сложно сказать, сэр..."
            her "Думаю, что-то около пары десятков парней..."
            $herView.hideshowQQ( "body_29.png", pos )
            her "И несколько девушек..."
            her "Я думаю, что и школьный библиотекарь мог меня увидеть..."
            m "Хм... Ну что ж, прекрасная работа."
            
        elif one_out_of_three == 2: ### EVENT (B)
            stop music fadeout 1.0
            m "Мисс Грейнджер, вы выполнили ваше задание?"
            show screen blktone
            with d3
            $herView.hideshowQQ( "body_45.png", pos )
            her "Вполнила, сэр."
            m "Тогда расскажи мне."
            $herView.hideshowQQ( "body_31.png", pos )
            her "Эм... Ладно..."
            her "Я показала сиськи тому парню в гостинной \"Гриффиндора\"..."
            $herView.hideshowQQ( "body_14.png", pos )
            her "И тут рядом со мной я заметила Джинни..."
            m "Еще один парень?"
            $herView.hideshowQQ( "body_13.png", pos )
            her "Парень? Нет, Джинни - это женское имя, сэр."
            m "....."
            $herView.hideshowQQ( "body_14.png", pos )
            her "Джинни Уизли, сэр"
            m "Хорошо, ладно, продолжай..."
            $herView.hideshowQQ( "body_13.png", pos )
            her "эм..."
            her "......."
            $herView.hideshowQQ( "body_24.png", pos )
            play music "music/Chipper Doodle v2.mp3" fadein 1 fadeout 1 # HERMIONE'S THEME.
            her "*Хихикает*"
            m "Хм...?"
            $herView.hideshowQQ( "body_46.png", pos )
            her "Затем, Джинни схватила мои сиськи..."
            her "И стала сжимать их..."
            her "Дальше, она начала страстно целовать мою грудь..."
            m "............"
            $herView.hideshowQQ( "body_111.png", pos )
            her "Покрывать поцелуями и сосать мои соски..."
            $herView.hideshowQQ( "body_128.png", pos )
            her "И я не смогла сдержаться - я начала стонать..."
            m ".............."
            $herView.hideshowQQ( "body_129.png", pos )
            her "Видя это, тот парень достал свой пульсирующий член..."
            her "И облил нас с Джинни своей горячей спермой!"
            $herView.hideshowQQ( "body_111.png", pos )
            her "А после мы с Джинни слизали его горячее семя с наших молодых тел..."
            m ".............."
            m "Ты все это выдумала?"
            $herView.hideshowQQ( "body_24.png", pos )
            her "...может быть."
            $herView.hideshowQQ( "body_128.png", pos )
            her "Я просто подумала, что вы хотели бы услышать что-то подобное, сэр..."
            m "Я хотел бы услышать правду."
            $herView.hideshowQQ( "body_127.png", pos )
            her "Даже если она невероятно скучная, сэр?"
            m "Скучная или нет..."
            m "Я всего лишь хочу знать, что произошло на самом деле..."
            m "Держи свои фантазии при себе, девочка."
            $herView.hideshowQQ( "body_70.png", pos )
            her "Как пожелаете, сэр."
            her "Моя подруга Джинни проходила мимо, когда я показывала сиськи тому парню."
            her "Но она обещала, что никому не расскажет."
            $herView.hideshowQQ( "body_15.png", pos )
            her "И это все что произошло, сэр..."
            m "Понятно..."
            m "И все таки это мне нравится больше, чем какие-то выдуманные истории..."
            
        elif one_out_of_three == 3: ### EVENT (C)
           
            m "Мисс Грейнджер, вы выполнили задание?"
            show screen blktone
            with d3
            $herView.hideshowQQ( "body_45.png", pos )
            play music "music/Chipper Doodle v2.mp3" fadein 1 fadeout 1 # HERMIONE'S THEME.
            her "Выполнила, сэр."
            m "Хорошо, тогда расскажи мне, как все прошло."
            $herView.hideshowQQ( "body_29.png", pos )
            her "Так, дайте подумать..."
            her "Сначала я показала их одному парню из \"Когтеврана\"..."
            $herView.hideshowQQ( "body_31.png", pos )
            her "Затем тому старшекласснику из \"Пуффендуя\"..."
            $herView.hideshowQQ( "body_45.png", pos )
            her "Затем еще одному парню из \"Когтеврана\"."
            m "???"
            $herView.hideshowQQ( "body_34.png", pos )
            her "После этого я по ошибке показала грудь младшекласснику из \"Гриффиндора\"..."
            $herView.hideshowQQ( "body_29.png", pos )
            her "Нет, стойте...  парень из \"Гриффиндора\" был после другого парня..."
            m "Скольким парням вы показали сиськи сегодня, мисс Грейнджер?"
            $herView.hideshowQQ( "body_117.png", pos )
            her "Где-то около полудесятка?"
            $herView.hideshowQQ( "body_122.png", pos )
            her "У меня было окно в расписании..."
            her "И поэтому я решила отработать заранее несколько смен ваших поручений, сэр."
            m "Это не поручения, мисс Грецнджер..."
            m "И нет никаких смен..."
            $herView.hideshowQQ( "body_31.png", pos )
            her "Ох...?"
            m "Вы просто получите вашу обычную плату, вот и все."
            $herView.hideshowQQ( "body_29.png", pos )
            her "Ох... Понятно..."
            m "Но, мисс Грейнджер..."
            $herView.hideshowQQ( "body_31.png", pos )
            her "Да, сэр?"
            g9 "Работа была сделана на отлично."
            $herView.hideshowQQ( "body_128.png", pos )
            her "Спасибо, сэр."
        


    $ gryffindor +=35
    m "35 очков \"Гриффиндору\"!"
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
    
    $ posHead = gMakePos( 390, 340 )
    if one_out_of_three == 2 and hermi.whoring >= 12 and hermi.whoring <= 14: #Event level 02.
        $ hermione_chibi_xpos = 610 # Stands near the door.
        show screen hermione_01_f #Hermione stands still.
        pause.3
        $herViewHead.showQ( "body_120.png", posHead )
        her "\"Слизерин\"..."
        $herViewHead.hideQ()
        hide screen hermione_01_f #Hermione stands still.
    
    if one_out_of_three == 3 and hermi.whoring >= 12 and hermi.whoring <= 14: #Event level 02.
        $ hermione_chibi_xpos = 610 # Stands near the door.
        show screen hermione_01_f #Hermione stands still.
        pause.3
        $herViewHead.showQ( "body_120.png", posHead )
        her "(Я не могу поверить, что я делала это сегодня...)"
        her2 "(Что, если бы Гарри или Рон увидели меня такой?)"
        her "(Стоящей там...)"
        her "(Прижимающейся грудью к оконному стеклу...)"
        her2 "(Наверное, я бы просто умерла от стыда на том самом месте...)"
        her2 "(Нет. Защита чести \"Гриффиндора\" - мой приоритет номер один.)"
        her2 "(Мы должны получить кубок в этом году, неважно какой ценой...)"
        her "(........)"
        $herViewHead.hideQ()
        hide screen hermione_01_f #Hermione stands still.
    
    if hermi.whoring >= 15 and one_out_of_three == 1: # LEVEL 06+ <=============================================================EVENT LEVEL 03
        $ hermione_chibi_xpos = 610 # Stands near the door.
        show screen hermione_01_f #Hermione stands still.
        pause.3
        $herViewHead.showQ( "body_123.png", posHead )
        her "........................."
        $herViewHead.hideQ()
        hide screen hermione_01_f #Hermione stands still.

            
            
    $ renpy.play('sounds/door.mp3') #Sound of a door opening.
    with Dissolve(.3)


 
 
 
 
    
    $ request_15_points += 1 
    $ request_15 = False 
    $ hermione_sleeping = True

    call music_block

    $event.Finalize()    

    return
    
    
    
    
    
    
    

