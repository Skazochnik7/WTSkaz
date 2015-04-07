label summon_snape:
    if snape_busy:
        ">Профессор Снейп недоступен."
        if daytime:
            jump day_main_menu
        else: 
            jump night_main_menu
    
    
    $ renpy.play('sounds/door.mp3') #Sound of a door opening.
    #$ snapes_speed = 02.0 #The speed of moving the walking animation across the screen.
    #$ walk_xpos=470 #Animation of walking chibi. (From)
    #$ walk_xpos2=360 #Coordinates of it's movement. (To)
    #show screen snape_walk_01 
    #with d3
    #pause 1.5
    $ menu_x = 0.2 #Menu is moved to the left side. (Default menu_x = 0.5)
    $ tt_xpos=350 #Defines position of the Snape's full length sprite.
    $ tt_ypos=0
    $ s_sprite = "03_hp/10_snape_main/snape_01.png"
    show screen snape_02 #Snape stands still.
    show screen bld1
    show screen snape_main
    with Dissolve(.3)

  
    sna "Да, что такое?"
    label snape_ready:
        pass
    menu:
        "- Поговорить -" if sfmax and not chitchated_with_snape and not daytime: # sfmax - friendship with Snape maxed out.
            $ chitchated_with_snape = True #Prevents you from chitchating more then once a day. Turns back to False every night and every day.
            $ menu_x = 0.5 #Menu is moved to the left side. (Default menu_x = 0.5)
            #$ snape_busy = True
            jump snape_chitchat
        "- Поговорить -" if daytime and not chitchated_with_snape: # sfmax - friendship with Snape maxed out.
            $ chitchated_with_snape = True #Prevents you from chitchating more then once a day. Turns back to False every night and every day.
            $ menu_x = 0.5 #Menu is moved to the left side. (Default menu_x = 0.5)
            #$ snape_busy = True
            jump snape_chitchat

        "Купить зелье на букву \"Б\"" if teacher_jinn_quest == 2 and gold >= 7000:
            jump snape_tutor_2
        "\"Отвиснуть.\"" if not daytime and not sfmax: # Turns TRUE when friendship with Snape been maxed out.
        
            if teacher_jinn_quest == 1:
                jump snape_tutor_1
                
            elif one_of_ten == 10:
                call not_today #Snape says: "I am busy tonight."
#            elif snape_friendship >= 39 and whoring <= 5: # Whoring level <= 2. Makes sure you don't proceed after Date #6 until reached Whoring lvl 3.
#                call not_today #Snape says: "I am busy tonight."
            elif snape_friendship >= 88 and hermi.whoring <= 14: # hermi.whoring level <= 5. Makes sure you don't proceed after Date #12 until reached Whoring lvl 6.
                call not_today #Snape says: "I am busy tonight."
            else:
                pass
                $ menu_x = 0.5 #Menu is moved to the left side. (Default menu_x = 0.5)
                jump snape_dates
        "Ничего.":
            label snape_nothing:
            stop music fadeout 1.0
            $ menu_x = 0.5 #Menu is moved to the left side. (Default menu_x = 0.5)
            if daytime:
                sna "Ну что ж, тогда я вернусь к работе..."
                play music "music/Brittle Rille.mp3" fadein 1 fadeout 1
            else: 
                sna "Эмм... тогда доброй ночи."
                play music "music/Music for Manatees.mp3" fadein 1 fadeout 1
            $ snape_busy = True
            hide screen snape_02 #Snape stands still.
            hide screen bld1
            hide screen snape_main
            with d3
            $ renpy.play('sounds/door.mp3') #Sound of a door opening.
            if daytime:
                jump day_main_menu
            else: 
                jump night_main_menu
    

label snape_dates:  ### HANGING WITH SNAPE ###
    show screen with_snape_animated
    play bg_sounds "sounds/fire02.mp3" fadeout 1.0 fadein 1.0 #Quiet...
    show screen fireplace_fire
    hide screen genie
    hide screen chair
    hide screen desk
    show screen desk
    
    hide screen snape_02 #Snape stands still.
    hide screen bld1
    hide screen snape_main
    with d3

    
    with fade
    $ fire_in_fireplace = True
   
    if this.IsStep("SNAPE"):
        show screen with_snape #Makes sure the scene is not animated...
        $ this.RunStep("SNAPE")
    
    
    if hero.Items.Any("wine"):
        $hero.Items.AddItem("wine",-1)
        if not wine_not:
            $wine_not=True # Turns True after you use Dumbledore's wine in the "Snape dating" for the first time. Makes sure the cut-scene is shown only once.
            call wine_first # Using Dumbledor's wine for the first time.
        else:
            call wine_not_first # Using Dumbledor's wine not for the first time.
    
    
    
    
    
    if snape_friendship >= 5 and snape_events == 0:
        call date_with_snape_01
        
    elif snape_friendship >= 12 and snape_events == 1: #LEVEL 02
        call date_with_snape_02
        
    elif snape_friendship >= 19 and snape_events == 2: #LEVEL 03
        call date_with_snape_03
        
    elif snape_friendship >= 27 and snape_events == 3: #LEVEL 04
        call date_with_snape_04
        
    elif snape_friendship >= 34 and snape_events == 4: #LEVEL 05
        call date_with_snape_05
        
    elif snape_friendship >= 41 and snape_events == 5: #LEVEL 06. Can't proceed after this until whoring >= Lv 3.
        call date_with_snape_06
        
    elif snape_friendship >= 48 and snape_events == 6: #LEVEL 07
        call date_with_snape_07
         
    elif snape_friendship >= 55 and snape_events == 7: #LEVEL 08
        call date_with_snape_08
        
    elif snape_friendship >= 62 and snape_events == 8: #LEVEL 09
        call date_with_snape_09
        
    elif snape_friendship >= 69 and snape_events == 9: #EVENT 10
        call date_with_snape_10
        
    elif snape_friendship >= 76 and snape_events == 10: #EVENT 10
        call date_with_snape_11
        
    elif snape_friendship >= 83 and snape_events == 11: #EVENT 11
        call date_with_snape_12
         
    elif snape_friendship >= 88 and snape_events == 12: #EVENT 12. If whoring level > 5.
        call date_with_snape_13
        
    elif snape_friendship >= 93 and snape_events == 13: #EVENT 13
        call date_with_snape_14
        
    elif snape_friendship >= 98 and snape_events == 14: #EVENT 14
        call date_with_snape_15
        
    else:
            
        show screen bld1
        with d3
        $ renpy.play('sounds/win_04.mp3')   #Not loud.
        hide screen notes
        show screen notes
        ">Вы проводите вечер, болтая с профессором Снейпом.\n>Ваши отношения с ним улучшились."
        hide screen bld1
        with d3
        
        

 
    $ snape_friendship +=1
    jump day_start
    
   
### SPECIAL DATE ###
label special_date_with_snape: #TAKES PLACE AFTER FIRST VISIT FROM HERMIONE.
#    $ snape_against_hermione = False #Turns True after event_08. Activates special event (THIS EVENT) when hanging out with Snape next time.
    $sna_head_state = 2
    sna_head_main "..........................."
    m "...............................?"
    $sna_head_state = 3
    sna_head_main "Я ненавижу ее..."
    menu:
        "\"Да! Та еще сука!\"":
            $sna_head_state = 1
            sna_head_main "Приятно знать, что мы одного мнения..."
            $sna_head_state = 2
            sna_head_main "Эта девка..."
        "\"Кого ты ненавидишь?\"":
            $sna_head_state = 1
            sna_head_main "И ты еще спрашивешь?"
            sna_head_main "Эту девку Гермиону, конечно!"
        "\"Она настолько плоха?\"":
            sna_head_main "Хуже!"

    $sna_head_state = 2
    sna_head_main "Лучший студент..."
    $sna_head_state = 3
    sna_head_main "Ведет все виды внеклассных мероприятий и клубов..."
    sna_head_main "Президент школьного Студенческого совета..."
    sna_head_main "Скорее всего станет старостой в ближайшее время..."
    $sna_head_state = 2
    sna_head_main "................"
    $sna_head_state = 3
    sna_head_main "............"
    with hpunch
    $sna_head_state = 5
    sna_head_main "{size=+7}Я ненавижу эту гребаную ведьму!!!{/size}"
    g4 "{size=-4}(Что за...?){/size}"
    $sna_head_state = 2
    sna_head_main ".............."
    sna_head_main "Раньше она просто раздражала, но в эти дни..."
    $sna_head_state = 1
    sna_head_main "Она стала реальной угрозой..."
    sna_head_main "Теперь эта ведьма - официально мой самый нелюбимый ученик из всей школы..."
    m "Как насчет этого мальчишки Поттера?"
    $sna_head_state = 6
    sna_head_main "Поттер? Ха! Да кто он такой!?"
    $sna_head_state = 1
    sna_head_main "Нет, я серьезно..."
    sna_head_main "Более того, я скажу, что Поттер младший, взятый вместе со своим жалким отцом..." #I will go as far as to say that Potter jr. and his wretched father combined..."
    sna_head_main "Не вызывает у меня столько злости, сколько эта маленькая ведьма, особенно в последнее время..."
    m "Да, конечно, мы оба знаем, что это не так..."
    $sna_head_state = 2
    sna_head_main "Да... Ты прав..."
    $sna_head_state = 7
    sna_head_main "Этот ублюдок Джеймс Поттер действительно бесит меня-"
    $sna_head_state = 6
    sna_head_main "Подожди, как ты узнал это?"
    m "Ну... Я читал книги..."
    sna_head_main "Что? Какие книги?"
    m "А, не важно. Я Джинн, помнишь? Я знаю всякое..."
    $sna_head_state = 9
    sna_head_main "Хм... И все же ты хочешь, чтобы я обучил тебя..."
    m "Ну, я говорил тебе, моя магия не полностью действует в вашем мире..."
    sna_head_main "Конечно, конечно..."
    m "......"
    m "Она приходила ко мне..."
    $sna_head_state = 10
    sna_head_main "Кто?"
    m "Девочка, Гермиона..."
    $sna_head_state = 1
    sna_head_main "Что?!"
    $sna_head_state = 2
    sna_head_main "Я думал, мы договорились о правиле \"никаких контактов с людьми\"."
    $sna_head_state = 7
    sna_head_main "(Хотя в последнее время я задавался вопросом, является ли она вообще человеком...)"
    m "Я знаю ... Она была вынуждена так поступить..."
    $sna_head_state = 1
    sna_head_main "Я полагаю она была здесь..."
    sna_head_main "Что она хотела?"
    
    if jerk_off_session:
        m "Я не имею понятия..."
        $sna_head_state = 11
        sna_head_main "??"
        m "Я дрочил в течение всего времени, пока она говорила..."
        $sna_head_state = 2
        sna_head_main "Ты..."
        sna_head_main "... делал что?"
        m "Эй, не суди меня!"
        m "Ты не знаешь, какого это - быть запертым в этой башне, как заключенный!"
        sna_head_main "Ты... т-ты..."
        $sna_head_state = 12
        sna_head_main "......"
        $sna_head_state = 15
        sna_head_main "Ха.... ха-ха... ХА-ХА-ХА!!!"
        m "Чт...? Что я сказал?"
        $sna_head_state = 14
        sna_head_main "Ха-ха-ха! Ты бесподобен!"
        $sna_head_state = 9
        sna_head_main "Все Джинны - такие... удивительные нигилисты?"
        m "Да уж... Мы - бессмертные, и, как правило, нам плевать."
        sna_head_main "Понятно..."
        $sna_head_state = 10
        sna_head_main "К сожалению, мы, простые смертные, не можем позволить себе такую роскошь..."
        
    else:
        m "Не уверен, что запомнил... Она много говорила ..."
        m "Что-то насчет \"гриффиндорских\" очков... и..."
        m "Э-э ... я не обращал внимания, если честно ..."
        $sna_head_state = 1
        sna_head_main "Пф... Наверное был загружен другим оправданным дерьмом..."
        $sna_head_state = 7
        sna_head_main "Она знаменита этим..."
    

    sna_head_main "У меня занятия завтра рано, так что давай закругляться." #собираться ночью."
    m "Что насчет обучения магии и прочему?"
    $sna_head_state = 10
    sna_head_main "Да, конечно..."
    sna_head_main "В следующий раз..."
    m "Хорошо..."
    
    

    
#    $ hermione_is_waiting_01 = True #Triggers another visit from Hermione. (Event_09)
    $this.special_date_with_snape.Finalize()
    jump day_start
    
#######################################################################################################################    
label special_date_with_snape_02: #TAKES PLACE AFTER SECOND VISIT FROM HERMIONE. (Where she says that she sent letter to the ministry.)
    show screen bld1
    with d5
    #$ snape_against_hermione = False #Turns True after event_10. Activates special event (THIS EVENT) when hanging out with Snape next time.
    m "......................."
    m "Гермиона Грейнджер приходила снова..."
    $sna_head_state = 1
    sna_head_main "Не произноси имя этой ведьмы, когда я здесь."
    $sna_head_state = 2
    sna_head_main "..............."
    $sna_head_state = 3
    sna_head_main "Черт возьми! Я взрослый человек, Альбус!"
    m "Меня зовут не-"
    sna_head_main "Глубокоуважаемый чародей..."
    m "Ну, ладно, проехали..."
    $sna_head_state = 2
    sna_head_main "Почему одно крошечное.... влагалище, может вызвать во мне столько злости?!"
    $sna_head_state = 4
    sna_head_main "Я думал, что с тобой как с моим союзником у меня будет шанс-"
    m "Бесит?" 
    $sna_head_state = 2
    sna_head_main "Да, не то слово..."
    $sna_head_state = 16
    sna_head_main "Но все, что я делал, давало ей больше возможностей, чтобы бесить меня..."
    sna_head_main "Она даже настроила учителей против меня..."
    $sna_head_state = 3
    sna_head_main "................."
    $sna_head_state = 7
    sna_head_main "Ее следует убрать..."
    m "Что ты имеешь в виду?"
    with hpunch
    $sna_head_state = 5
    sna_head_main "{size=+6}Я хочу убить ее!{/size}"
    g4 "Убить в буквальном смысле?"
    $sna_head_state = 6
    sna_head_main "У тебя есть другое предложение?"
    m "Ты шутишь, верно?"
    sna_head_main "Я?!"
    $sna_head_state = 11
    sna_head_main "Можешь сделать это для меня?"
    m "Эм..."
    m "Как бы я ни наслаждался убийством девочки..."
    m "Джинны не могут убивать..."
    $sna_head_state = 7
    sna_head_main "Вздор!"
    m "И мы осуждаем убийц..."
    if jerk_off_session:
        $sna_head_state = 17
        sna_head_main "В самом деле? Я думал, тебе плевать..."
        m "До определенной степени..."
        $sna_head_state = 7
        sna_head_main "............."
    $sna_head_state = 2
    sna_head_main "Ну...значит, не обращай на меня внимания..."
    sna_head_main "Это все - разговоры..."
    sna_head_main "Я бы никогда на самом деле не навредил студенту..."
    $sna_head_state = 3
    sna_head_main "(...до поры, до времени.)"
    m "Слушай, если она настолько вредна, почему бы просто не найти менее радикальный способ борьбы с ней?"
    $sna_head_state = 7
    sna_head_main "Ха... Порка была объявлена вне закона год назад..."
    m "Это не то, что я имею в виду..."
    $sna_head_state = 1
    sna_head_main "А?"
    m "Она лучший студент, так?"
    $sna_head_state = 2
    sna_head_main "Да, черт ее возьми. Эта девчонка трудоголик. Я признаю это за ней."
    m "Также она имеет превосходную репутацию."
    $sna_head_state = 6
    sna_head_main "О, да!"
    m "И она думает, что она лучше, чем все остальные ..."
    $sna_head_state = 17
    sna_head_main "Что ты будешь делать с этим?"
    m "Ну, кажется ее влияние исходит из репутации..."
    $sna_head_state = 11
    sna_head_main "......................?"
    m "Что если мы отнимем это у нее?"
    $sna_head_state = 10
    sna_head_main "Это заткнет ее, я полагаю..."
    $sna_head_state = 2
    sna_head_main "Но как? Она практически святая."
    $sna_head_state = 7
    sna_head_main "Даже студенты, которые ненавидят ее, тайно восхищаются ею."
    $sna_head_state = 2
    sna_head_main "Она не провалила ни одного теста за все время здесь..."
    sna_head_main "Она всегда опережает расписание..."
    $sna_head_state = 3
    sna_head_main "Черт, как же я ненавижу, когда она исправляет меня во время моих занятий..."
    $sna_head_state = 6
    sna_head_main "И благодаря ей \"Гриффиндор\" далеко впереди всех остальных сейчас..."
    $sna_head_state = 7
    sna_head_main "Даже \"Слизерин\" не так догоняет в этом году..."
    $sna_head_state = 16
    sna_head_main "........................"
    $sna_head_state = 6
    sna_head_main "Черт... Мне нужно больше вина..."
    m "Вино может подождать. Выслушай меня для начала!"
    $sna_head_state = 1
    sna_head_main "Ну...?"
    $ d_flag_01 = False
    $ d_flag_02 = False
    $ d_flag_03 = False
    label fuck_off:
    m "Хм... Итак..."
    menu:
        m "..."
        "{size=-3}\"Убедим ее в том, что она больше не лучший ученик!\"{/size}" if not d_flag_01:
            $ d_flag_01 = True
            sna_head_main "Что? Ты предлагаешь оценивать ее несправедливо?"
            $sna_head_state = 2
            sna_head_main "Ха... Дамблдор никогда не позволит-"
            $sna_head_state = 9
            sna_head_main "Погоди-ка!"
            m "Вот именно!"
            $sna_head_state = 18
            sna_head_main "Ты прав! Я стану оценивать ее несправедливо! Я мог бы даже подговорить других учителей!"
            sna_head_main "Я мог бы сказать, что это ваш приказ..."
            $sna_head_state = 19
            sna_head_main "И когда настоящий Дамблдор вернется, я сделаю вид, что не знал, кто ты на самом деле. И я..."
            m "...работал на директора."
            $sna_head_state = 10
            sna_head_main "Э-э..."
            sna_head_main "Это все еще ты, Джинн?"
            m "Да, да, все еще я..."
            $sna_head_state = 18
            sna_head_main "Отлично."
            if d_flag_01 and d_flag_02 and d_flag_03:
                pass
            else:
                jump fuck_off
        "{size=-3}\"Конечно же \"Гриффиндор\" потеряет кубок в этом году!\"{/size}" if not d_flag_02:
            $ d_flag_02 = True
            $sna_head_state = 1
            sna_head_main "Просто начать вычитать очки у них без всякой причины?"
            $sna_head_state = 18
            sna_head_main "О, мне нравится это!"
            $sna_head_state = 20
            sna_head_main "Есть несколько \"Слизеринских\" девиц, готовых получить дополнительные очки для своего факультета."
            $sna_head_state = 19
            sna_head_main "Да, это великолепно сработает!"
            $sna_head_state = 18
            sna_head_main "Ты - Гений!"
            m "Да, я и джинн и гений. Это вообще-то одно и то же ..."
            translators "По-английски 'джинн' (genie), звучит сходно с 'гений' (genius)."
            if d_flag_01 and d_flag_02 and d_flag_03:
                pass
            else:
                jump fuck_off

        "{size=-3}\"Испортим ее репутацию!\"{/size}" if not d_flag_03:
            $ d_flag_03 = True
            $sna_head_state = 1
            sna_head_main "Запятнаем ее репутацию?"
            sna_head_main "Эта девушка неподкупна..."
            m "Нонсенс!"
            m "Все, что нужно - это убедить ее сделать какие-то жертвы для \"блага\""
            $sna_head_state = 9
            sna_head_main "О, ну конечно..."
            $sna_head_state = 21
            sna_head_main "Она с удовольствием \"замарает руки\", только чтобы сохранить честь своего драгоценного \"Гриффиндора\"!"
            $sna_head_state = 9
            sna_head_main "И когда она это сделает, у нас появятся рычаги для воздействия..."
            if d_flag_01 and d_flag_02 and d_flag_03:
                pass
            else:
                jump fuck_off

    sna_head_main "Это может сработать!"
    m "Я тоже так думаю."
    $sna_head_state = 19
    sna_head_main "О, я чувствую себя таким... живым сегодня!"
    $sna_head_state = 15
    sna_head_main "Налей мне еще кубок!"
    $sna_head_state = 19
    sna_head_main "Занятие по \"Защите от Темных Искусств \" начнется завтра позднее, чем обычно!"
    m "....."
    m "Не кажется ли тебе это немного жестоким?"
    m "Я думаю, она просто девочка..."
    $sna_head_state = 8
    sna_head_main "Просто девочка?"
    sna_head_main "Ох, нет, нет, нет..."
    $sna_head_state = 4
    sna_head_main "Она - воплощение чистого зла!"
    $sna_head_state = 2
    sna_head_main "Если мы не сделаем этого сейчас..."
    $sna_head_state = 3
    sna_head_main "Однажды я могу просто не выдержать и \"Авада Кедаврануть\" ее!"
    m "Ты можешь что?"
    $sna_head_state = 4
    sna_head_main "Убью ее по-настоящему!"
    m "Хорошо, хорошо... Понял...."
    m "Давай выберем наименьшее из двух зол."
    $sna_head_state = 7
    sna_head_main "Да..."
    $sna_head_state = 6
    sna_head_main "Теперь налей мне еще вина."

    ">Вы проводите остаток вечера в компании Снейпа, запивая ваши заботы."
    
#    $ snape_against_hermione_02 = False #Turns True after event_10. Activates special event (THIS EVENT) when hanging out with Snape next time.   
#    $ hermione_is_waiting_02 = True #Triggers another visit from Hermione. (Event_11)
   

    #$ hermione_is_waiting_01 = True #Triggers another visit from Hermione. (Event_09)
    hide screen bld1
    with d3
    $ days_without_an_event = 0 #Making sure next even will not start right away.
    $this.special_date_with_snape_02.Finalize()
    jump day_start
   
   
######################################################################################   

    
####Snape bonus###
#label snape_bonus:
#    if snape_events == 1:
#        if generating_snape_bonus == 1:
#            pass
#        elif generating_snape_bonus == 2:
#            $ slytherin +=3
#            "Slytherin got +3 points as a Snape-Bonus."
    
#    if snape_events == 2:#WEEK No.2
#        if generating_snape_bonus == 1:
#            pass
#        elif generating_snape_bonus == 2:
#            $ slytherin +=7
#            "Slytherin got +7 points as a Snape-Bonus."
    
#    if snape_events == 3:#WEEK No.3
#        if generating_snape_bonus == 1:
#            pass
#        elif generating_snape_bonus == 2:
#            $ slytherin +=10
#            "Slytherin got +10 points as a Snape-Bonus."
            
#    if snape_events == 4:#WEEK No.4
#        if generating_snape_bonus == 1:
#            pass
#        elif generating_snape_bonus == 2:
#            $ slytherin +=12
#            "Slytherin got +12 points as a Snape-Bonus."
            
#    if snape_events == 5:#WEEK No.5
#        if generating_snape_bonus == 1:
#            pass
#        elif generating_snape_bonus == 2:
#            $ slytherin +=16
#            "Slytherin got +16 points as a Snape-Bonus."
            
#    if snape_events == 6:#WEEK No.6
#        if generating_snape_bonus == 1:
#            pass
#        elif generating_snape_bonus == 2:
#            $ slytherin +=22
#            "Slytherin got +22 points as a Snape-Bonus."
            
#    if snape_events == 7:#WEEK No.7
#        if generating_snape_bonus == 1:
#            pass
#        elif generating_snape_bonus == 2:
#            $ slytherin +=26
#            "Slytherin got +26 points as a Snape-Bonus."
            
#    if snape_events == 8:#WEEK No.8
#        if generating_snape_bonus == 1:
#            pass
#        elif generating_snape_bonus == 2:
#            $ slytherin +=32
#            "Slytherin got +32 points as a Snape-Bonus."
            
#    if snape_events == 9:#WEEK No.9
#        if generating_snape_bonus == 1:
#            pass
#        elif generating_snape_bonus == 2:
#            $ slytherin +=36
#            "Slytherin got +36 points as a Snape-Bonus."
            
#    if snape_events == 10:#WEEK No.10
#        if generating_snape_bonus == 1:
#            pass
#        elif generating_snape_bonus == 2:
#            $ slytherin +=43
#            "Slytherin got +43 points as a Snape-Bonus."
            
#    if snape_events == 11:#WEEK No.11
#        if generating_snape_bonus == 1:
#            pass
#        elif generating_snape_bonus == 2:
#            $ slytherin +=46
#            "Slytherin got +46 points as a Snape-Bonus."
            
#    if snape_events == 12:#WEEK No.12
#        if generating_snape_bonus == 1:
#            pass
#        elif generating_snape_bonus == 2:
#            $ slytherin +=50
#            "Slytherin got +50 points as a Snape-Bonus."
            
#    if snape_events == 13:#WEEK No.13
#        if generating_snape_bonus == 1:
#            pass
#        elif generating_snape_bonus == 2:
#            $ slytherin +=56
#            "Slytherin got +56 points as a Snape-Bonus."
            
#    if snape_events == 14:#WEEK No.14
#        if generating_snape_bonus == 1:
#            pass
#        elif generating_snape_bonus == 2:
#            $ slytherin +=61
#            "Slytherin got +61 points as a Snape-Bonus."
            
#    if snape_events == 15:#WEEK No.15
#        if generating_snape_bonus == 1:
#            pass
#        elif generating_snape_bonus == 2:
#            $ slytherin +=66
#            "Slytherin got +66 points as a Snape-Bonus."

#return




####################################
label wine_first:
    m "Смотри, что у меня есть!"
    $ s_head_xpos = 330 # x = 330,                                                                              # SNAPE
    $ s_head_ypos = 380 #Right bottom corner: y = 340. y = 380 - no hand.       # SNAPE
    $ s_sprite = "03_hp/10_snape_main/snape_05.png"                                        # SNAPE
    show screen s_head2                                                                                                 # SNAPE
    sna "Хм..?"
    sna "Дай-ка взглянуть..."
    hide screen s_head2    
    pause.1
    $ the_gift = "03_hp/18_store/27.png" # WINE.
    show screen gift
    with d3
    ">Вы передаете Снейпу бутылку, которую нашли в шкафу..." 
    hide screen gift
    with d3
#    $ wine -= 1
    
    $ s_sprite = "03_hp/10_snape_main/24.png"                                        # SNAPE
    show screen s_head2                                                                                                 # SNAPE
    sna2 "Эта бутылка из тайника Дамблдора!"
    $ s_sprite = "03_hp/10_snape_main/snape_06.png"                                        # SNAPE
    show screen s_head2                                                                                                 # SNAPE
    sna2 "Очень дорогая и очень раритетная вещица."
    hide screen s_head2 
    m "В таком случае, можем ли мы позволить себе?"
    $ s_sprite = "03_hp/10_snape_main/snape_02.png"                                        # SNAPE
    show screen s_head2                                                                                                 # SNAPE
    sna "Мы, безусловно, можем!"
    hide screen s_head2 
    show screen bld1
    with d3
    $ renpy.play('sounds/win_04.mp3')   #Not loud.
    hide screen notes
    show screen notes
    ">Ваши отношения с профессором Снейпом улучшились."
    $ snape_friendship +=1
    hide screen bld1
    with d3
    return


label wine_not_first:
    m "Смотри, что у меня есть!"
    hide screen s_head2    
    pause.1
    $ the_gift = "03_hp/18_store/27.png" # WINE.
    show screen gift
    with d3
    ">Вы передаете Снейпу бутылку, которую нашли в шкафу..." 
    hide screen gift
    with d3
#    $ wine -= 1
    $ s_head_xpos = 330 # x = 330,                                                                              # SNAPE
    $ s_head_ypos = 380 #Right bottom corner: y = 340. y = 380 - no hand.       # SNAPE
    $ s_sprite = "03_hp/10_snape_main/snape_05.png"                                        # SNAPE
    show screen s_head2                                                                                                 # SNAPE
    sna "Еще одна?"
    if one_of_ten == 1:
        $ s_sprite = "03_hp/10_snape_main/snape_02.png"                                        # SNAPE
        show screen s_head2    
        sna2 "Великолепно!"
    elif one_of_ten == 2:
        $ s_sprite = "03_hp/10_snape_main/snape_02.png"                                        # SNAPE
        show screen s_head2    
        sna2 "Превосходно!"
    elif one_of_ten == 3:
        $ s_sprite = "03_hp/10_snape_main/snape_02.png"                                        # SNAPE
        show screen s_head2    
        sna2 "Бесподобно!"
    elif one_of_ten == 4:
        $ s_sprite = "03_hp/10_snape_main/snape_02.png"                                        # SNAPE
        show screen s_head2    
        sna2 "Отлично, мой друг!"
    elif one_of_ten == 5:
        $ s_sprite = "03_hp/10_snape_main/snape_05.png"                                        # SNAPE
        show screen s_head2    
        sna2 "Ты нашел тайник Альбуса или это его личный винный погреб?"
    elif one_of_ten == 6:
        $ s_sprite = "03_hp/10_snape_main/snape_02.png"                                        # SNAPE
        show screen s_head2    
        sna2 "В последнее время мне с трудом дается выпивка, но не эта!"
    elif one_of_ten == 7:
        $ s_sprite = "03_hp/10_snape_main/snape_02.png"                                        # SNAPE
        show screen s_head2    
        sna2 "Отлично! Я уже чувствую себя менее напряженным!"
    elif one_of_ten == 8:
        $ s_sprite = "03_hp/10_snape_main/snape_02.png"                                        # SNAPE
        show screen s_head2    
        sna2 "Становится все лучше и лучше!"
    elif one_of_ten == 9:
        $ s_sprite = "03_hp/10_snape_main/snape_05.png"                                        # SNAPE
        show screen s_head2    
        sna2 "Серьезно, насколько велик этот тайник?"
    elif one_of_ten == 2:
        $ s_sprite = "03_hp/10_snape_main/snape_02.png"                                        # SNAPE
        show screen s_head2    
        sna2 "Уверен, нами быть хорошо! Давай откупорим этого ублюдка!"
    
    hide screen s_head2 
    show screen bld1
    with d3
    $ renpy.play('sounds/win_04.mp3')   #Not loud.
    hide screen notes
    show screen notes
    ">Ваши отношения с профессором Снейпом улучшились."
    $ snape_friendship +=1
    hide screen bld1
    with d3
    return
    
    
  ########
label not_today:
    if one_out_of_three == 1:
        sna "К сожалению, я не могу сегодня..."
    elif one_out_of_three == 2:
        sna "К сожалению, у меня есть другие дела сегодня ночью..."
    elif one_out_of_three == 3:
        sna "К сожалению, у меня другие планы. Может быть, в другой раз?"
    
    jump snape_nothing

