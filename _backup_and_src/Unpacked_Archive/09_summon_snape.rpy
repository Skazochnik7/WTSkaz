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
        "\"Отвиснуть.\"" if not daytime and not sfmax: # Turns TRUE when friendship with Snape been maxed out.
            if one_of_ten == 10:
                call not_today #Snape says: "I am busy tonight."
#            elif snape_friendship >= 39 and whoring <= 5: # Whoring level <= 2. Makes sure you don't proceed after Date #6 until reached Whoring lvl 3.
#                call not_today #Snape says: "I am busy tonight."
            elif snape_friendship >= 88 and whoring <= 14: # Whoring level <= 5. Makes sure you don't proceed after Date #12 until reached Whoring lvl 6.
                call not_today #Snape says: "I am busy tonight."
            else:
                pass
                $ menu_x = 0.5 #Menu is moved to the left side. (Default menu_x = 0.5)
                jump snape_dates
        "Ничего.":
            stop music fadeout 1.0
            $ menu_x = 0.5 #Menu is moved to the left side. (Default menu_x = 0.5)
            if daytime:
                sna "Хорошо, вернусь тогда к работе..."
                play music "music/Brittle Rille.mp3" fadein 1 fadeout 1
            else: 
                sna "В таком случае, доброй ночи."
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
   
    if snape_against_hermione: #Turns True after event_08 (Hermione shows up for the first time).
                               #Activates special event when hanging out with Snape next time.
        show screen with_snape #Makes sure the scene is not animated...
        jump special_date_with_snape
    
    if snape_against_hermione_02: #Activates after second visit from Hermione (event_09).
        show screen with_snape #Makes sure the scene is not animated...
        jump special_date_with_snape_02
    
    
    if wine >= 1 and not wine_not: # Using Dumbledor's wine for the first time.
        $ wine_not = True # Turns True after you use Dumbledore's wine in the "Snape dating" for the first time. Makes sure the cut-scene is shown only once.
        call wine_first
    elif wine >= 1 and wine_not: # Using Dumbledor's wine not for the first time.
        call wine_not_first
    else:
        pass
    
    
    
    
    
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
    $ snape_against_hermione = False #Turns True after event_08. Activates special event (THIS EVENT) when hanging out with Snape next time.
    sna_02 "..........................."
    m "...............................?"
    sna_03 "Я ненавижу ее..."
    menu:
        "\"Да! Та еще сука!\"":
            sna_01 "Приятно знать, что мы одного мнения..."
            sna_02 "Эта девка..."
        "\"Кого ты ненавидишь?\"":
            sna_01 "Почему ты спрашивешь?"
            sna_01 "Эта девка - Гермиона, конечно!"
        "\"Она настолько плоха?\"":
            sna_01 "Хуже!"

    sna_02 "Лучший студент..."
    sna_03 "Ведет все виды внеклассных мероприятий и клубов..."
    sna_03 "Президент школьного Студенческого совета..."
    sna_03 "Скорее всего станет старостой в ближайшее время..."
    sna_02 "................"
    sna_03 "............"
    with hpunch
    sna_05 "{size=+7}Я ненавижу эту гребаную ведьму!!!{/size}"
    g4 "{size=-4}(Что за...?){/size}"
    sna_02 ".............."
    sna_02 "Раньше она просто раздражала, но в эти дни..."
    sna_01 "Она стала реальной угрозой..."
    sna_01 "Теперь эта ведьма официально мой нелюбимый ученик из всей школы..."
    m "Как насчет этого мальчишки Поттера?"
    sna_06 "Поттер? Ха! Да кто он такой!?"
    sna_01 "Нет, я серьезно..."
    sna_01 "Я зайду дальше и скажу, что Поттер младший и смесь его жалкого отца" #I will go as far as to say that Potter jr. and his wretched father combined..."
    sna_01 "Не вызывает у меня столько злости, как эта маленькая ведьма, которая делает это все последнее время..."
    m "Да, конечно, мы оба знаем, что это не так..."
    sna_02 "Да ... Ты прав..."
    sna_07 "Этот ублюдок Джеймс Поттер действительно бесит меня--"
    sna_06 "Подожди, как ты узнал это?"
    m "Ну... Я читал книги..."
    sna_06 "Что? Какие книги?"
    m "А, не важно. Я джиннн, помнишь? Я знаю всякое..."
    sna_09 "Хм... И все же ты хочешь, чтобы я обучил тебя..."
    m "Ну, я говорил тебе, моя магия не полностью действует в вашем мире..."
    sna_09 "Конечно, конечно..."
    m "......"
    m "Она приходила ко мне..."
    sna_10 "Кто?"
    m "Девочка, Гермиона..."
    sna_01 "Что?!"
    sna_02 "Я думал, мы договорились о правиле \"никаких контактов с людьми\"."
    sna_07 "(Хотя в последнее время я задавался вопросом является ли она вообще человеком...)"
    m "Я знаю ... Она была вынуждена так поступить..."
    sna_01 "Я полагаю она была здесь..."
    sna_01 "Что она хотела?"
    
    if jerk_off_session:
        m "Я не уверен..."
        sna_11 "??"
        m "Я дрочил в течение всего времени, пока она говорила..."
        sna_02 "Ты..."
        sna_02 "... делал что?"
        m "Эй, не суди меня!"
        m "Ты не знаешь, какого это быть запертым в этой башне, как заключенный!"
        sna_02 "Ты... т-ты...."
        sna_12 "......"
        sna_15 "Ха.... ха-ха... ХА-ХА-ХА!!!"
        m "Чт..? Что я сказал?"
        sna_14 "Ха-ха-ха! Ты бесподобен!"
        sna_09 "Все джинны такие...удивительные негилисты?"
        m "Да уж... Мы бессмертные, и как правило нам плевать."
        sna_09 "Понятно..."
        sna_10 "К сожалению, мы, простые смертные, не можем позволить себе такую роскошь..."
        
    else:
        m "Не уверен ... Она много говорила ..."
        m "Что-то насчет \"гриффиндорских\" очков...и..."
        m "Э-э ... я не обращал внимания, если честно ..."
        sna_01 "Пф... Наверное был загружен другим оправданным дерьмом..."
        sna_07 "Она знаменита этим..."
    

    sna_07 "У меня есть занятие завтра рано, так что давай закругляться." #собираться ночью."
    m "Что насчет обучения магии и прочему?"
    sna_10 "Да, конечно..."
    sna_10 "В следующий раз..."
    m "Хорошо..."
    
    

    
    $ hermione_is_waiting_01 = True #Triggers another visit from Hermione. (Event_09)
    jump day_start
    
#######################################################################################################################    
label special_date_with_snape_02: #TAKES PLACE AFTER SECOND VISIT FROM HERMIONE. (Where she says that she sent letter to the ministry.)
    show screen bld1
    with d5
    #$ snape_against_hermione = False #Turns True after event_10. Activates special event (THIS EVENT) when hanging out with Snape next time.
    m "......................."
    m "Гермиона Грейнджер приходила снова..."
    sna_01 "Не произноси имя этой ведьмы, когда я здесь"
    sna_02 "..............."
    sna_03 "Черт возьми! Я взрослый человек, Альбус!"
    m "Меня зовут не--"
    sna_03 "Уважаемый мастер..."
    m "Ну, хорошо, пусть так..."
    sna_02 "Почему одно крошечное .... влагалище, может вызвать во мне столько злости?!"
    sna_04 "Я думал, что с тобой, как с моим союзником, у меня будет шанс--"
    m "Бесит?" 
    sna_02 "Да, не то слово..."
    sna_16 "Но все, что я делал, давало ей больше возможностей, чтобы бесить меня..."
    sna_16 "Она даже настроила учителей против меня..."
    sna_03 "................."
    sna_07 "Ее следует убрать..."
    m "Что ты имеешь в виду?"
    with hpunch
    sna_05 "{size=+6}Я хочу убить ее!{/size}"
    g4 "Убить в буквальном смысле?"
    sna_06 "У тебя есть другое предложение?"
    m "Ты шутишь, верно?"
    sna_06 "Я?!"
    sna_11 "Можешь сделать это для меня?"
    m "Эм..."
    m "Как бы я наслаждался убийство девочки..."
    m "Но джиннны не могу убивать..."
    sna_07 "Вздор!"
    m "И мы осуждаем убийц..."
    if jerk_off_session:
        sna_17 "В самом деле? Я думал тебе плевать..."
        m "До определенной степени..."
        sna_07 "............."
    sna_02 "Ну...значит не обращай на меня внимания..."
    sna_02 "Это все разговоры..."
    sna_02 "Я бы никогда на самом деле не навредил студенту..."
    sna_03 "(...до поры, до времени.)"
    m "Слушай, если она настолько вредна, почему бы просто не найти менее радикальный способ борьбы с ней?"
    sna_07 "Ха... Порка была объявлена вне закона год назад..."
    m "Это не то, что я имею в виду..."
    sna_01 "А?"
    m "Она лучший студент, так?"
    sna_02 "Да, черт ее возьми. Эта девочка труженица. Я даю ей это."
    m "Также она имеет превосходную репутацию."
    sna_06 "О, да!"
    m "И она думает, что она лучше, чем все остальные ..."
    sna_17 "Что ты будешь делать с этим?"
    m "Ну, кажется ее влияние исходит из репутации..."
    sna_11 "......................?"
    m "Что если мы отнимем это у нее"
    sna_10 "Это заткнет ее, я полагаю..."
    sna_02 "Но как? Она практически святая."
    sna_07 "Даже студенты, которые ненавидят ее, тайно восхищаются ею."
    sna_02 "Она не провалила ни одного теста за все время здесь..."
    sna_02 "Она всегда опережает расписание..."
    sna_03 "Черт, как же я ненавижу, когда она исправляет меня во время моих занятий..."
    sna_06 "И благодаря ей \"Гриффиндор\" далеко впереди всех остальных сейчас..."
    sna_07 "Даже \"Слизерин\" не так догоняет в этом году..."
    sna_16 "........................"
    sna_06 "Черт... Мне нужно больше вина..."
    m "Вино может подождать. Выслушай меня для начала!"
    sna_01 "Ну...?"
    $ d_flag_01 = False
    $ d_flag_02 = False
    $ d_flag_03 = False
    label fuck_off:
    m "Хм... Итак..."
    menu:
        m "..."
        "{size=-3}\"Убедим ее в том, что она больше не лучший ученик!\"{/size}" if not d_flag_01:
            $ d_flag_01 = True
            sna_01 "Что? Ты предлагаешь оценивать ее несправедливо?"
            sna_02 "Ха... Дамблдор никогда не позволит--"
            sna_09 "Погоди ка!"
            m "Точно!"
            sna_18 "Ты прав! Я буду оценивать ее несправедливо! Я бы мог даже подговорить других учителей!"
            sna_18 "Я бы мог сказать, что это ваш приказ..."
            sna_19 "И когда настоящий Дамблдор вернется, я сделаю вид, что не знал, кто ты на самом деле..."
            m "Работка для меня."
            sna_10 "Э-э..."
            sna_10 "Это все еще ты, джиннни?"
            m "Да, да, все еще я..."
            sna_18 "Отлично."  
            if d_flag_01 and d_flag_02 and d_flag_03:
                pass
            else:
                jump fuck_off
        "{size=-3}\"Конечно же \"Гриффиндор\" потеряет кубок в этом году!\"{/size}" if not d_flag_02:
            $ d_flag_02 = True
            sna_01 "Просто начать вычиать очки у них без как либо причины?"
            sna_18 "О, мне нравится это!"
            sna_20 "Есть несколько \"Слизеринских\" девушек, которые готовы получить допольнительные очки для своего дома."
            sna_19 "О, это великолепно сработает!"
            sna_18 "Ты Гений!"
            m "Да, я джинн-гений. Но каковы шансы ..."
            if d_flag_01 and d_flag_02 and d_flag_03:
                pass
            else:
                jump fuck_off

        "{size=-3}\"Испортим ее репутацию!\"{/size}" if not d_flag_03:
            $ d_flag_03 = True
            sna_01 "Запятнаем ее репутацию?"
            sna_01 "Эта девушка не подкупна..."
            m "Нонсенс!"
            m "Все что нужно, это убедить ее сделать какие-то жертвы для \"блага\""
            sna_09 "О, ну конечно..."
            sna_21 "Она бы с удовольствием \"Замарала свои руки\", чтобы сохранить честь своего драгоценного \"Гриффиндора\"!"
            sna_09 "И когда она это сделает, у нас появятся рычаги для давления..."
            if d_flag_01 and d_flag_02 and d_flag_03:
                pass
            else:
                jump fuck_off

    sna_09 "Это может сработать!"
    m "Я тоже так думаю"
    sna_19 "О, я чувствую себя таким живым сегодня!"
    sna_15 "Налей мне еще кубок!"
    sna_19 "Занятие по \"Защите от Темных Искусств \" начнется завтра позднее чем обычно!"
    m "....."
    m "Не кажется ли тебе это немного жестоким?"
    m "Я думаю, она просто девочка..."
    sna_08 "Просто девочка?"
    sna_08 "Ох, нет, нет, нет..."
    sna_04 "Она воплощение чистого зла!"
    sna_02 "Если мы не сделаем этого сейчас..."
    sna_03 "В один из дней я могу просто щелкнуть и \"Авада Кедаврануть\" ее!"
    m "Ты можешь что?"
    sna_04 "Убью ее по настоящему!"
    m "Хорошо, хорошо... Понял...."
    m "Давай выберем наименьшее из двух зол."
    sna_07 "Да..."
    sna_06 "Теперь налей мне еще вина."

    ">Вы проводите остаток вечера в компании Снейпа запивая ваши заботы."
    
    $ snape_against_hermione_02 = False #Turns True after event_10. Activates special event (THIS EVENT) when hanging out with Snape next time.   
    $ hermione_is_waiting_02 = True #Triggers another visit from Hermione. (Event_11)
   

    #$ hermione_is_waiting_01 = True #Triggers another visit from Hermione. (Event_09)
    hide screen bld1
    with d3
    $ days_without_an_event = 0 #Making sure next even will not start right away.
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
    m "Смотри что у меня есть!"
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
    $ wine -= 1
    
    $ s_sprite = "03_hp/10_snape_main/24.png"                                        # SNAPE
    show screen s_head2                                                                                                 # SNAPE
    sna2 "Это бутылка из тайнка Дамблдора!"
    $ s_sprite = "03_hp/10_snape_main/snape_06.png"                                        # SNAPE
    show screen s_head2                                                                                                 # SNAPE
    sna2 "Очень дорогая и очень раритетная вещица."
    hide screen s_head2 
    m "В таком случае можем ли мы позволить себе?"
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
    m "Смотри что у меня есть!"
    hide screen s_head2    
    pause.1
    $ the_gift = "03_hp/18_store/27.png" # WINE.
    show screen gift
    with d3
    ">Вы передаете Снейпу бутылку, которую нашли в шкафу..." 
    hide screen gift
    with d3
    $ wine -= 1
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
        sna2 "Вы нашли тайник Альбуса или это его личный винный погреб?"
    elif one_of_ten == 6:
        $ s_sprite = "03_hp/10_snape_main/snape_02.png"                                        # SNAPE
        show screen s_head2    
        sna2 "В последнее время мне с трудом дается выпивка, но это!"
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
    
    jump snape_ready