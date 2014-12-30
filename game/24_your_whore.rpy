label your_whore:
    show screen end_u_1
    $ end_u_1_pic =  "03_hp/17_ending/02.png"
    
    $ badges = False
    
    hide screen hermione_main
    hide screen room # MAIN BG (DAY).
    
    hide screen notes #A bunch of notes poping out with a "win" sound effect.
    hide screen phoenix_food
    hide screen done_reading
    hide screen done_reading_02
    hide screen candlefire_01 #CANDLE FIRE.
    hide screen candlefire_02 #CANDLE FIRE.
    hide screen lightening #Hide lighting so it woudn't get stuck during clear sky weather and such.
    hide screen cloud_night_01 #NIGHT CLOUDS.
    hide screen cloud_night_02 #NIGHT CLOUDS.
    hide screen cloud_night_03 #NIGHT CLOUDS.
    hide screen bld1 #You know what this is. Just making sure it doesn't get stuck.
     
    hide screen main_menu_01  

    with fade
    #hide screen end_u_1                                           #<---- SCREEN
    #hide screen end_u_2                                           #<---- SCREEN
    hide screen end_u_3                                           #<---- SCREEN
    #hide screen end_u_4                                           #<---- SCREEN
    pause.1
    hide screen blkfade
    with d5
    show screen ctc
    pause
    hide screen ctc
    show screen bld1
    with d7
        
        
        
    
    
    
    
    
  
    m "Я должен убедиться, что остался незамечен..."
    m "......................"
    m "Как же дофига народу..."
    m "На сколько же огромна эта школа?"
    m ".................."
    m ".................................."
    m "Девченки нигде не видно..."
    m ".............."
    m "......................"
    m "Так...она должна быть где-то здесь..."
    m "................"
    m "................................."
    # FADE
    show screen blktone
    with d7
    
    if public_whore_ending: #Students talking. Ending "Public whore".
        mal "Вы слышали что говорят о Гермионе Грейнджер"
        mal2 "Что она стала первоклассной сосалкой?"
        mal "Ась? Не, это не слухи, это факт."
        mal "Говорят, что она за это получала оплату очками факультета."
        mal2 "Хм...я в это не верю, я думаю что она просто потаскуха."
        fem "Кто потаскуха?"
        mal "Ох, это ты..."
        fem "Так кто тут потаскуха?"
        mal2 "Гермиона Грейнджер..."
        fem "Оу! Вы, ребята, опять говорите об этой проститутке?"
        fem "Эта баба дрочит пару членов, отсасывает нескольким парням...и вдруг она новая школьная звезда."
        fem "Жалкая грязнокровка..."
        mal "Ты не должна ревновать ее--"
        fem "Ревновать??? ЕЁ??? Вот ещё!"
        fem "Я не зарабатываю себе популярность тем, что позволяю кому-то засовывать член мне в рот!"
        mal "Ну...если ты вдруг передумаешь..."
        fem "Что?"
        mal "Не стесняйся использовать меня, как ступеньку, на пути к своей славе!"
        fem "Ты бы этого хотел!"
        mal2 "Эй, ребят, мне кажется, что это Гермиона там!"
        mal "Точно!"
        mal2 "Как думаете, если я приглашу её на танец, мне потом что-нибудь перепадет?"
        mal "Нет, если я приглашу её первый!"
        $ renpy.play('sounds/run_04.mp3')    #<--------------------Sound of running off.
        pause 2
        mal2 "Эй, стой! Это моя идея!"
        $ renpy.play('sounds/run_03.mp3')    #<--------------------Sound of running off.
        pause 2
        fem "Ребят...?"
        fem "........................."
        fem "Мда... Парни........"
        
        
        
        
        
        
        
        
        
    else: #Students talking. Ending "Your whore".
        mal "(Вы слышали о чем поговаривают?)"
        mal2 "(Да. Говорят, что Гермиона в одиночку набрала очки факультета.)"
        fem "(Стала шлюхой за очки, имеешь ввиду?!)"
        fem "(Какой позор!)"
        mal "(Это лишь слухи!)"
        fem "(Я думаю, что это больше чем просто...)"
        mal "(Да заткнись уже. Ты просто ревнуешь!)"
        mal2 "(Да! Ты просто хочешь быть на месте Гермионы!Yeah, you wish you had Hermione's courage!)"
        mal "(Верно! Она верна \"Гриффиндору\" как никто другой! Exactly!)"
        mal "(И даже если это правда, что с того?)"
        mal "(Благодаря ей, наш факультет получит кубок в этом году!)"
        mal2 "(Именно! А что сделала ты для нашего факультета?)"
        fem "(Я..... Но....)"
        mal "(Верно! Так что нефиг наговаривать на Гермиону!)"
        mal2 "(Верно сказал, чувак.)"
        fem "(*Дуется*)"
    
    
    
    
    
    
    
    hide screen blktone
    with d3
    hide screen bld1
    with d3
    show screen ctc
    pause
    hide screen ctc
    
    
    $ end_u_2_pic =  "03_hp/17_ending/01.png"
    show screen end_u_2
    with d7
    show screen ctc
    pause
    hide screen ctc
    show screen bld1
    with d5
    m "(Вот она!)"
    
    mal "Эй, Гермиона..."
    $ her_head_xpos=390 #Defines position of the Hermione's full length sprite. (Default 370). 140 - center. Bottom right: 390
    $ her_head_ypos=235 #Defines position of the Hermione's full length sprite. (Default 0). Right bottom corner: 340 - head only. 235 - tits.
    show screen h_head2                                                             # HERMIONE
    $ h_body = "03_hp/13_hermione_main/body_159.png" # HERMIONE
    $ no_upper = True #Skirt not displayed.
    her "О, привет!"
    hide screen h_head2     
    mal "Ты выглядишь...просто превосходно сегодня вечером, Гермиона. You look... so beautiful tonight, Hermione."
    show screen h_head2                                                             # HERMIONE
    $ h_body = "03_hp/13_hermione_main/body_160.png" # HERMIONE
    her "Спасибо, ты тоже мило выглядишь."
    hide screen h_head2 
    mal2 "Могу ли я пригласить тебя на следующий танец?"
    mal "Что? Отвали, я был первый!"
    mal2 "Ты идешь к черту!"
    mal "Отлично, дружок! Сделай это!"
    mal2 "Я не твой \"дружок\", приятель!"
    show screen h_head2                                                             # HERMIONE
    $ h_body = "03_hp/13_hermione_main/body_161.png" # HERMIONE
    her ".............."
    hide screen h_head2 
    
    show screen blktone8
    with d3
    stop music fadeout 3.0
    m "Вот он, мой шанс!"
    m "(Псс! Девушка!)"
    show screen h_head2                                                             # HERMIONE
    $ h_body = "03_hp/13_hermione_main/body_162.png" # HERMIONE
    her "???"
    hide screen h_head2     
    m "(Красотка, это я! Тут!)"
    show screen h_head2                                                             # HERMIONE
    $ h_body = "03_hp/13_hermione_main/body_163.png" # HERMIONE
    her "Профессор Дамблодор?"
    hide screen h_head2     
    m "(Ш-ш-ш! Тише, и иди за мной.)"
    show screen h_head2                                                             # HERMIONE
    $ h_body = "03_hp/13_hermione_main/body_163.png" # HERMIONE
    her "А?"
    hide screen h_head2     
    pause.1
    $ end_u_1_pic =  "03_hp/17_ending/02.png"
    hide screen blktone8
    hide screen blktone
    hide screen bld1
    show screen end_u_1 #<---- SCREEN
    with fade
    show screen ctc
    pause
    hide screen ctc
    show screen bld1
    with d3


    
    
    # ALCOVE 
    
    show screen h_head2                                                             # HERMIONE
    $ h_body = "03_hp/13_hermione_main/body_162.png" # HERMIONE
    her "Сэр, что происходит? Почему вы... прячитесь?"
    hide screen h_head2
    m "Просто помолчи и послушай секундочку! Ты можешь кое что сделать для меня?"
    show screen h_head2                                                             # HERMIONE
    $ h_body = "03_hp/13_hermione_main/body_162.png" # HERMIONE
    play music "music/(Orchestral) Playful Tension by Shadow16nh.mp3" fadein 1 fadeout 1 # SEX THEME.
    her "Да, сэр"
    hide screen h_head2
    m "Хорошо, вот одна штука...Well, here is the thing then..."
    m "Кое-что, что ты должна зна--"
    show screen h_head2                                                             # HERMIONE
    $ h_body = "03_hp/13_hermione_main/body_166.png" # HERMIONE
    her "Конечно, сэр!"
    hide screen h_head2
    m "Что?"
    show screen h_head2                                                             # HERMIONE
    $ h_body = "03_hp/13_hermione_main/body_165.png" # HERMIONE
    her "Позвольте толькко сделать это быстро, хорошо?"
    hide screen h_head2
    g4 "Позволить сделать что?"
    show screen h_head2                                                             # HERMIONE
    $ h_body = "03_hp/13_hermione_main/body_164.png" # HERMIONE
    her2 "Вы хотите, что бы я поблагодарила вас за платье, верно, сэр?"
    hide screen h_head2
    m "Платье? Нет, я здесь не по этому."
    show screen h_head2                                                             # HERMIONE
    $ h_body = "03_hp/13_hermione_main/body_165.png" # HERMIONE
    her "Все хорошо, сэр. Я не против."
    hide screen h_head2
    m "Слушай меня, девочка! Я не тот, кем ты меня считае--"
    show screen h_head2                                                             # HERMIONE
    $ h_body = "03_hp/13_hermione_main/body_167.png" # HERMIONE
    her "Пожалуйста, сэр, позвольте мне немного приласкать вашего петушка."
    hide screen h_head2
    g4 "Гх--!!!"
    show screen h_head2                                                             # HERMIONE
    $ h_body = "03_hp/13_hermione_main/body_167.png" # HERMIONE
    her "Совсем чуть-чуть. Пожалуйста, я умоля вас..."
    hide screen h_head2
    g4 "Черт, проклятая ведьма!"
    g4 "Прекрати! Мне действительно нужно поговорить с тобой!"
    show screen h_head2                                                             # HERMIONE
    $ h_body = "03_hp/13_hermione_main/body_164.png" # HERMIONE
    her "Конечно, сэр."
    show screen h_head2                                                             # HERMIONE
    $ h_body = "03_hp/13_hermione_main/body_167.png" # HERMIONE
    her "Засунье ваш член мне в рот и говорите со мной."
    her "Поговорите со мнйо о грязных делишках."
    hide screen h_head2
    g4 "*рычит!*"
    m "*Вздох....*"
    m "Хорошо, можешь взять его..."
    m "Но ты злоупотребляешь своей силой, девченка!"
    show screen h_head2                                                             # HERMIONE
    $ h_body = "03_hp/13_hermione_main/body_168.png" # HERMIONE
    her "*Хихикает!*"
    hide screen h_head2
    m "И после того, как мы закончим, мы должны поговорить об этом!"
    
    # SUCKING
    
    show screen blkfade
    with d7
    her "*Чавк!* *Чавк!* *Чавк!*"
    m "................."
    
    $ end_u_1_pic =  "03_hp/17_ending/03.png" #<---- SCREEN
    hide screen blkfade
    hide screen bld1
    with d7
    show screen ctc
    pause
    hide screen ctc
    her "*Чавк!* *Глоть!* *Чавк!*"
    her "*Чавк--"
    $ end_u_2_pic =  "03_hp/17_ending/04.png" #<---- SCREEN
    show screen end_u_2                                             #<---- SCREEN
    with d7                                                                        #<---- SCREEN
    # LOOKING BACK
    her "Ась?.........."
    her "...................."
    $ end_u_1_pic =  "03_hp/17_ending/03.png" #<---- SCREEN
    show screen end_u_1                                             #<---- SCREEN
    with d7
    her "*Чавк!* *Глоть!* *Чавк!*"
    m "Да...Вот так.... о... да..."
    her "*Глоть!* *Чавк!* *Чавк!*"
    her "*Глоть--"
    $ end_u_2_pic =  "03_hp/17_ending/04.png" #<---- SCREEN
    show screen end_u_2                                             #<---- SCREEN
    with d7                                                                        #<---- SCREEN
    her "...................." #LOOKING BACK
    m "Просто продолжай!"
    m "Я скажу тебе, если кто-то будет идти..."
    her "Ох... не в этом дело, сэр..."
    m "Хм?"
    her "Скоро должы сделать объявление..."
    $ end_u_1_pic =  "03_hp/17_ending/03.png" #<---- SCREEN
    show screen end_u_1                                             #<---- SCREEN
    with d7
    her "*Чавк!* *Глоть!* *Чавк!*"
    m "Объявление?"
    her "*Чавк!* *Чавк!* *Чавк!*"
    her "*Чавк--"
    $ end_u_2_pic =  "03_hp/17_ending/04.png" #<---- SCREEN
    show screen end_u_2                                             #<---- SCREEN
    with d7                                                                        #<---- SCREEN
    her "Да. О коронации..."
    $ end_u_1_pic =  "03_hp/17_ending/03.png" #<---- SCREEN
    show screen end_u_1                                             #<---- SCREEN
    with d7
    her "*Глоть!* *Чавк!* *Глоть!*"
    m "Что...?"
    her "*Чавк--"
    $ end_u_2_pic =  "03_hp/17_ending/04.png" #<---- SCREEN
    show screen end_u_2                                             #<---- SCREEN
    with d7                                                                        #<---- SCREEN
    her "Коронация Королевы осеннего бала Хогвартса, сэр."
    m "Ох... Вот оно что?"
    m "Есть шанс, что ею станешь ты?"
    her "Шанс?"
    her "Это уже решено, сэр."
    m "Что?"
    her "Ой, я имею ввиду - я надеюсь, что стану..."
    her "Поскольку я та, кто организовал всё это, было бы справедливо..."
    her "Разве вы не согласны, сэр?"
    m "Понятно... Звучит как жульничество--"
    $ end_u_1_pic =  "03_hp/17_ending/07.png" #<---- SCREEN
    show screen end_u_1                                             #<---- SCREEN
    with d7
    her "*Чавк!* *Чавк!* *Чавк!*"
    $ end_u_2_pic =  "03_hp/17_ending/04.png" #<---- SCREEN
    show screen end_u_2                                             #<---- SCREEN
    with d7                                                                        #<---- SCREEN
    her "Разве вы не согласны, сэр?"
    m "Ммм..."
    her "Разве вы не согласны, сэр?"
    $ end_u_1_pic =  "03_hp/17_ending/06.png" #<---- SCREEN
    show screen end_u_1                                             #<---- SCREEN
    with d7                                                                        #<---- SCREEN
    with hpunch
    her "{size=+7}*Глотает!*{/size}" #DEEPTHROATING
    g4 "{size=+7}О, ДА!!!{/size}"
    her "*Глотает!* *Глотает!* *Глотает!*"
    her "*Глотает---"
    $ end_u_2_pic =  "03_hp/17_ending/04.png" #<---- SCREEN
    show screen end_u_2                                             #<---- SCREEN
    with d7                                                                        #<---- SCREEN
    her "Отлично. Я знала что вы будете \"за\"."
    $ end_u_1_pic =  "03_hp/17_ending/07.png" #<---- SCREEN
    show screen end_u_1                                            #<---- SCREEN
    with d7                                                                       #<---- SCREEN
    her "*Чавк!* *Чавк!* *Глоть!*"
    m "Ох ... Это великолепно ..."
    her "*Чавк!* *Чавк!* *Глоть!*"
    
    show screen bld1
    with d5
    sna "*Кхм!*"
    sna "Внимание, лечинки!" 
    m "(Снейп?)"
    sna "Я сказал, успокоиться всем!"
    sna "Время объявить, кто в этом году будет королевой в ежегодном \"Осеннем бале Хогвартса\"."
    
    
#    ann "Quiet down everyone, quiet down..."
#    ann "It is time to choose this year's queen of the annual \"Hogwarts autumn ball\"."
    hide screen bld1
    with d5
    
    
    her "Чавк--"
    $ end_u_2_pic =  "03_hp/17_ending/04.png" #<---- SCREEN
    show screen end_u_2                                           #<---- SCREEN
    with d7                                                                       #<---- SCREEN
    her "О нет! Они уже начинают!"
    her "Но я не могу оставить вас в таком..."
    her "...состояние, сэр."
    
    
    her "Что же мне делать?"
    m "Просто иди, девочка. Мы закончим чуть позже."
    her "Но... Но вы подарили мне это платье, сэр. И..."
    her ".........."
    her "Нет, я просто не могу оставить вас сейчас, сэр."
    m "Отлично! Тогда закончи начитое."
    m "Если ты немного постараешься, мы закончим очень быстро."
    m "Я верю в тебя."
    her "Хм..."
    her "Тогда вы должны пообещать мне кое-что, сэр."
    m "И что же?"
    her "Пожалуйста, не сдерживайтесь."
    g9 "Хех... Я редко сдерживаюсь."
    show screen bld1
    with d5
    sna "В этом году королевой \"Осеннего бала\"..."
    sna "Сейчас посмотрим... Этот чертов конверт не открывается..."
    hide screen bld1
    with d5
    her "отлично. у нас есть немного времени."
    m "Да! Вот это воодушевление!"
    
    if public_whore_ending: #Students talking. Ending "Public whore".
        $ end_u_1_pic =  "03_hp/17_ending/03.png" #<---- SCREEN
        show screen end_u_1                                           #<---- SCREEN
        with d7                                                                       #<---- SCREEN
        her "*Чавк!* *Глоть!* *Чавк!*"
        m "Да..."
        $ end_u_2_pic =  "03_hp/17_ending/08.png" #<---- SCREEN
        show screen end_u_2                                           #<---- SCREEN
        with d7                                                                       #<---- SCREEN
        her "*Глоть!* *Чавк!* *Глоть!*"
        her "*Чавк--"
        $ end_u_1_pic =  "03_hp/17_ending/91.png" #<---- SCREEN
        show screen end_u_1                                           #<---- SCREEN
        with d7                                                                       #<---- SCREEN
        her "Сэр, вы думаете это правильно, угощать ЭТИМ свою студентку? Sir, is this really the proper way to treat one of your students?"
        m "Huh?"
        $ end_u_2_pic =  "03_hp/17_ending/08.png" #<---- SCREEN
        show screen end_u_2                                           #<---- SCREEN
        with d7                                                                       #<---- SCREEN
        her "*Чавк!* *Глоть!* *Глоть!*"
        her "*Чавк--"
        $ end_u_1_pic =  "03_hp/17_ending/92.png" #<---- SCREEN
        show screen end_u_1                                           #<---- SCREEN
        with d7                                                                       #<---- SCREEN
        her "Я такая хрупкая и чувствительная..."
        her "Мои родители доверили вам заботу обо мне..."
        $ end_u_2_pic =  "03_hp/17_ending/93.png" #<---- SCREEN
        show screen end_u_2                                           #<---- SCREEN
        with d7                                                                       #<---- SCREEN
        her "Вы должны были обращаться со мной \"хорошо\", сэр..."
        her "И что же вы сейчас делаете?"
        m "*Кхм!* Позволь мне повториться:..."
        m "{size=+7}\"Хах?\"{/size}"
        $ end_u_1_pic =  "03_hp/17_ending/94.png" #<---- SCREEN
        show screen end_u_1                                           #<---- SCREEN
        with d7                                                                       #<---- SCREEN
        her "Вы положили свой пенис в мой невинный ротик, сэр!"
        $ end_u_2_pic =  "03_hp/17_ending/95.png" #<---- SCREEN
        show screen end_u_2                                           #<---- SCREEN
        with d7                                                                       #<---- SCREEN
        her "*Чавк!* *Чавк!* *Чавк!*"
        g9 "О, я вижу! Да, я люблю невинных девочек!"
        her "*Чавк--"
        $ end_u_1_pic =  "03_hp/17_ending/91.png" #<---- SCREEN
        show screen end_u_1                                           #<---- SCREEN
        with d7                                                                       #<---- SCREEN
        her "Вы делали вид, будто добры ко мне..."
        her "Вы подарили мне это платье..."
        $ end_u_2_pic =  "03_hp/17_ending/92.png" #<---- SCREEN
        show screen end_u_2                                           #<---- SCREEN
        with d7                                                                       #<---- SCREEN
        her "А затем....................."
        $ end_u_1_pic =  "03_hp/17_ending/07.png" #<---- SCREEN
        show screen end_u_1                                           #<---- SCREEN
        with d7                                                                       #<---- SCREEN
        her "*Чавк!* *Глоть!* *Глоть!*"
        her "*Чавк--"
        $ end_u_2_pic =  "03_hp/17_ending/92.png" #<---- SCREEN
        show screen end_u_2                                           #<---- SCREEN
        with d7                                                                       #<---- SCREEN
        her "Вы воспользовались мной, профессор!"
        her "Обманом заставили сосать ваш большой член!"
        g4 "О...Да! Отлично! Oh... Yes! You're good!"
        $ end_u_1_pic =  "03_hp/17_ending/96.png" #<---- SCREEN
        show screen end_u_1                                           #<---- SCREEN
        with d7                                                                       #<---- SCREEN
        her "Я должна веселиться со своими одноклассниками на балу сейчас..."
        $ end_u_2_pic =  "03_hp/17_ending/93.png" #<---- SCREEN
        show screen end_u_2                                           #<---- SCREEN
        with d7                                                                       #<---- SCREEN
        her "Но чем я занимась?"
        $ end_u_1_pic =  "03_hp/17_ending/07.png" #<---- SCREEN
        show screen end_u_1                                           #<---- SCREEN
        with d7                                                                       #<---- SCREEN
        her "*Чавк!* *Чавк!* *Чавк!*"
        m "Ох..."
        $ end_u_2_pic =  "03_hp/17_ending/97.png" #<---- SCREEN
        show screen end_u_2                                           #<---- SCREEN
        with d7                                                                       #<---- SCREEN
        her "*Чавк!* *Глоть!* *Чавк!* *Чавк!* *Чавк!*"
        her "*Чавк--"
        $ end_u_1_pic =  "03_hp/17_ending/98.png" #<---- SCREEN
        show screen end_u_1                                           #<---- SCREEN
        with d7                                                                       #<---- SCREEN
        her "Я стою на коленях и отсасываю совему директору!"
        $ end_u_2_pic =  "03_hp/17_ending/97.png" #<---- SCREEN
        show screen end_u_2                                           #<---- SCREEN
        with d7                                                                       #<---- SCREEN
        her "*Чавк!* *Чавк!* *Глоть!*"
        m "О, да! Ты маленькая сучка!"
        her "*Чавк!* *Чавк!* *Чавк!*"
        her "*Чавк!* *Чавк!* *Глоть!*"
        g4 "Ты и правда умеешь говрить похотливые вещи...You are really good at this dirty talk stuff..."
        g9 "Ты должна попробовать писать детские книжки, или что-то типа..."
        $ end_u_1_pic =  "03_hp/17_ending/07.png" #<---- SCREEN
        show screen end_u_1                                           #<---- SCREEN
        with d7                                                                       #<---- SCREEN
        her "*Чавк--"
        $ end_u_2_pic =  "03_hp/17_ending/91.png" #<---- SCREEN
        show screen end_u_2                                           #<---- SCREEN
        with d7                                                                       #<---- SCREEN
        her "ОХ, но я не знаю как, сэр..."
        $ end_u_1_pic =  "03_hp/17_ending/92.png" #<---- SCREEN
        show screen end_u_1                                           #<---- SCREEN
        with d7                                                                       #<---- SCREEN
        her "Ведь я и сама ребенок..."
        g4 "Ты противная маленькая дрянь..."
        $ end_u_2_pic =  "03_hp/17_ending/97.png" #<---- SCREEN
        show screen end_u_2                                           #<---- SCREEN
        with d7                                                                       #<---- SCREEN
        her "*Чавк!* *Чавк!* *Глоть!* *Чавк!* *Чавк!*"
        
        show screen bld1
        with d5
        sna "Мисс Грейнджер?"
        sna "{size=-4}(Where is that girl?){/size}"
        ">A murmur is running though the crowd of students..."
        hide screen bld1
        with d5
        
        her "*Чавк!* *Чавк!* *Глоть!*"
        her "*Глоть--"
        $ end_u_1_pic =  "03_hp/17_ending/91.png" #<---- SCREEN
        show screen end_u_1                                           #<---- SCREEN
        with d7                                                                       #<---- SCREEN
        her "Сэр, я была послушной маленькой шлюшкой?"
        g4 "Да, сучка! Да!"
        $ end_u_2_pic =  "03_hp/17_ending/93.png" #<---- SCREEN
        show screen end_u_2                                           #<---- SCREEN
        with d7                                                                       #<---- SCREEN
        her "Вы бы сказали, что я хорошо научилась этому?"
        g9 "Я бы сказал, что ты великолепно научилась, девочка!"
        $ end_u_1_pic =  "03_hp/17_ending/92.png" #<---- SCREEN
        show screen end_u_1                                           #<---- SCREEN
        with d7                                                                       #<---- SCREEN
        her "Хорошо..."
        $ end_u_2_pic =  "03_hp/17_ending/99.png" #<---- SCREEN
        show screen end_u_2                                           #<---- SCREEN
        with d7                                                                       #<---- SCREEN
        her "Мои мамочка и папочка будут гордиться мной!"
        $ end_u_1_pic =  "03_hp/17_ending/95.png" #<---- SCREEN
        show screen end_u_1                                           #<---- SCREEN
        with d7                                                                       #<---- SCREEN
        her "*Чавк!* *Чавк!* *Глоть!*"
        g4 "Ох, ты убиваешь меня!"
        her "*Чавк-Чавк-Чавк-Чавк!!!*"
        g4 "О, да! Зашибись!"
        her "*Чавк--"
        $ end_u_2_pic =  "03_hp/17_ending/93.png" #<---- SCREEN
        show screen end_u_2                                           #<---- SCREEN
        with d7                                                                       #<---- SCREEN
        her "Заслужила ли я награду, сэр??"
        $ end_u_1_pic =  "03_hp/17_ending/100.png" #<---- SCREEN
        show screen end_u_1                                           #<---- SCREEN
        with d7                                                                       #<---- SCREEN
        her "Я бы хотела в качестве награды вашу сперму. Что бы вы спустили все до последней капли в мой ротик"
        g4 "Grh!"
        $ end_u_2_pic =  "03_hp/17_ending/97.png" #<---- SCREEN
        show screen end_u_2                                           #<---- SCREEN
        with d7                                                                       #<---- SCREEN
        her "*Чавк!* *Чавк!* *Чавк!*"
        g4 "Уже! Почти...!"
        her "{size=+5}*Чавк-Глоть-Чавк-Чавк!!!*{/size}"
        g4 "{size=+5}Вот оно--{/size}"
        $ end_u_1_pic =  "03_hp/17_ending/101.png" #<---- SCREEN
        show screen end_u_1                                           #<---- SCREEN
        with d7                                                                       #<---- SCREEN
        her "*Чавк--.........................."
        her "!!!"
        show screen ctc
        pause
        hide ctc
        show screen blkfade 
        with d7
        $ end_u_2_pic =  "03_hp/17_ending/102.png" #<---- SCREEN
        show screen end_u_2                                           #<---- SCREEN
        g4 "{size=+5}Когда...!? Почему ты не останавливаешся?!{/size}"
        g4 "{size=+5}Какого хрена ты делаешь--{/size}"
        hide screen blkfade 
        with d7
        show screen ctc
        pause
        hide screen ctc
        her "{size=+5}Cum for me. sir! Cum for me!{/size}"
        with hpunch
        g4 "{size=+5}What the hell is this?!{/size}"
        $ end_u_1_pic =  "03_hp/17_ending/103.png" #<---- SCREEN
        show screen end_u_1                                           #<---- SCREEN
        with d7                                                                       #<---- SCREEN
        her "{size=+5}Кончайте на меня, сэр! Я хочу вашу горячую сперму!{/size}"
        g4 "Аргх! Ты шлюха!"
        $ end_u_2_pic =  "03_hp/17_ending/104.png" #<---- SCREEN
        show screen end_u_2                                           #<---- SCREEN
        with d7                                                                       #<---- SCREEN
        her "{size=+5}Да!{/size}"
        her "{size=+5}Именно, я голодная до спермы шлюха, сэр!{/size}"
        with hpunch
        g4 "{size=+7}Аргх!!!{/size}"
        g4 "{size=+7}Возьми это, сейчас!!!{/size}"
        show screen white 
        pause .1
        hide screen white
        with hpunch
        g4 "{size=+7}АРГХ!{/size}"
        $ end_u_1_pic =  "03_hp/17_ending/105.png" #<---- SCREEN
        show screen end_u_1                                           #<---- SCREEN
        with d7                                                                       #<---- SCREEN
        her "{size=+5}Ах! Да, сэр! Да! Кончайте на меня!{/size}"
        show screen white 
        pause.1
        hide screen white
        pause.2
        show screen white 
        pause .1
        hide screen white
        with hpunch
        g4 "{size=+7}АРГХ!{/size}"
        g4 "{size=+7}Аргх!!! ДА!!!{/size}"
        $ end_u_2_pic =  "03_hp/17_ending/106.png" #<---- SCREEN
        show screen end_u_2                                           #<---- SCREEN
        with d7                                                                       #<---- SCREEN
        her "Ах... да... ах..."
        g4 "О... гх... *задыхается*"
        $ end_u_1_pic =  "03_hp/17_ending/105.png" #<---- SCREEN
        show screen end_u_1                                           #<---- SCREEN
        with d7                                                                       #<---- SCREEN
        her "Спасибо вам, сэр..."
        $ end_u_2_pic =  "03_hp/17_ending/107.png" #<---- SCREEN
        show screen end_u_2                                           #<---- SCREEN
        with d7                                                                       #<---- SCREEN
        her "..........................................."
        show screen ctc
        pause
        hide screen ctc
        show screen blkfade
        with d7
        
        # CUMMING
        pause.5
        m "Что на земле только что произошло, девочка?"
        $ her_head_xpos=390 #Defines position of the Hermione's full length sprite. (Default 370). 140 - center. Bottom right: 390
        $ her_head_ypos=235 #Defines position of the Hermione's full length sprite. (Default 0). Right bottom corner: 340 - head only. 235 - tits.
        show screen h_head2                                                             # HERMIONE
        $ h_body = "03_hp/13_hermione_main/body_165.png" # HERMIONE
        her "Что вы имеете ввиду, сэр?"
        hide screen h_head2  
        $ end_u_1_pic =  "03_hp/17_ending/02.png" #<---- SCREEN
        show screen end_u_1                                           #<---- SCREEN
        hide screen blkfade
        with d7
        m "Мне действительно нужно показывать на это?"
        g4 "{size=+5}Do I really?{/size}"
        show screen h_head2                                                             # HERMIONE
        $ h_body = "03_hp/13_hermione_main/body_165.png" # HERMIONE
        her "Oх... Вы имеете ввиду волосы?"
        hide screen h_head2
        m "Да...\"твои волосы\"..."
        show screen h_head2                                                             # HERMIONE
        $ h_body = "03_hp/13_hermione_main/body_168.png" # HERMIONE
        her "Ну...Что вы от меня хотите, сэр?"
        hide screen h_head2
        m "Что-нибудь..."
        g4 "...но {size=+7}THAT!{/size}"
        show screen h_head2                                                             # HERMIONE
        $ h_body = "03_hp/13_hermione_main/body_163.png" # HERMIONE
        her "Но...мне нужно выглядеть как можно лучше для коронации..."
        hide screen h_head2
        m "И прическа полная спермы это тебе обеспечит?"
        show screen h_head2                                                             # HERMIONE
        $ h_body = "03_hp/13_hermione_main/body_165.png" # HERMIONE
        her "Ну... да..."
        show screen h_head2                                                             # HERMIONE
        $ h_body = "03_hp/13_hermione_main/body_163.png" # HERMIONE
        her "Видите, сперма неплохо используется для укладки волос и--"
        hide screen h_head2
        
        show screen bld1
        with d5
        stop music fadeout 1.0
        sna "Мисс Грейнджер..................?"
        sna "Вы собираетесь пропустить свою коронацию, девченка?"
        sna "(Не то, чо бы для меня это было важно...)"
        hide screen bld1
        with d5
        
        show screen h_head2                                                             # HERMIONE
        $ h_body = "03_hp/13_hermione_main/body_161.png" # HERMIONE
        her "The coronation! I must go now!"
        hide screen h_head2
        $ renpy.play('sounds/run_03.mp3')    #<--------------------Sound of running off.
        pause 3
        
        m ".............................."
        m "................"
        m "..."
        with hpunch
        g4 "{size=+9}WHAT THE HELL...?!!{/size}"
        show screen ctc
        pause
        hide screen ctc
        show screen blkfade
        with d7
        

        ">..............{w}..................{w}...................."
        
        
        
        
    else:
        $ end_u_1_pic =  "03_hp/17_ending/06.png" #<---- SCREEN
        show screen end_u_1                                             #<---- SCREEN
        with d7                                                                        #<---- SCREEN
        with hpunch
        her "{size=+5}*Глотает!*{/size}"
        g4 "{size=+5}Даааааааа!{/size}"
        show screen bld1
        with d5
        sna "Так! Хм...?"
        sna "(Ну конечно... И почему я не удивлен?)"
        sna "Мисс Гермиона Грейнджер из \"Гриффиндора\"..."
        ">Бурные аплодисменты и приветствия."
        sna "Мисс Грейнджер, если вы будете так любезны, чтобы почтить нас своим присутствием ..."
        hide screen bld1
        with d5
        her "*Глотает--Глотает--Глотает!*"
        m "Да! Отлично, шлюха!"
        her "{size=+5}*Глотает--Глотает--Глотает!!!*{/size}"
        m "Да. Теперь поработай своим язычком."
        m "Полижи мои шарики. сучка. Ну!"
        $ end_u_2_pic =  "03_hp/17_ending/10.png" #<---- SCREEN
        show screen end_u_2                                             #<---- SCREEN
        with d7                                                                        #<---- SCREEN
        her "*Глотает!* *Лижет!* *Лижет!* *Глотает!*"
        m "Да...Супер!"
        m "Ты отличная шлюшка..."
        her "*Лижет!* *Лижет!* *Глотает!* *Лижет!*"
        m "Теперь смотри на меня, сосалка."
        $ end_u_1_pic =  "03_hp/17_ending/11.png" #<---- SCREEN
        show screen end_u_1                                             #<---- SCREEN
        with d7                                                                        #<---- SCREEN
        her "???................"
        $ renpy.play('sounds/spit.mp3') #Sound of spiting. 
        show screen white
        pause.3
        $ end_u_1_pic =  "03_hp/17_ending/12.png" #<---- SCREEN
        show screen end_u_1                                            #<---- SCREEN
        #with d3                                                                        #<---- SCREEN
        hide screen white
        with vpunch
        show screen ctc
        pause
        hide screen ctc
        her "*Глотает??!*"
        m "Не вздумай останавливаться!"
        $ end_u_2_pic =  "03_hp/17_ending/13.png" #<---- SCREEN
        show screen end_u_2                                             #<---- SCREEN
        with d7                                                                        #<---- SCREEN
        her "*Глотает--Глотает--Глотает!*"
        m "Да, сучка! Да!"
        show screen bld1
        with d5
        sna "Мисс Грейнджер?"
        sna "Если вы хотите..."
        sna "Мисс Грейнджер?"
        hide screen bld1
        with d5
        $ renpy.play('sounds/spit.mp3')    #<--------------------Sound of spiting. 
        show screen white
        pause.3
        $ end_u_2_pic =  "03_hp/17_ending/14.png" #<---- SCREEN
        show screen end_u_2                                            #<---- SCREEN
        hide screen white
        with vpunch
        show screen ctc
        pause
        hide screen ctc
        her "!!!!!!!!!!!"
        her "......................................?"
        m "Что-то случилось? Почему остановилась, сосуд для спермы?!"
        m "Продолжай сосать мои яйца!"
        $ end_u_1_pic =  "03_hp/17_ending/15.png" #<---- SCREEN
        show screen end_u_1                                             #<---- SCREEN
        with d7                                                                        #<---- SCREEN
        her "*Глотает--Глотает--Глотает!*"
        m "Да. Отличная шлюха."
        her "*Глотает--Глотает--Глотает!*"
        m "Заглоти его поглубже! Да, вот так!"
        her "*Глотает!* *Глотает!* *Глотает!*"
        m "Шарики! Не забывай работать язычком!"
        $ end_u_2_pic =  "03_hp/17_ending/16.png" #<---- SCREEN
        show screen end_u_2                                             #<---- SCREEN
        with d7                                                                        #<---- SCREEN
        her "*Глотает!* *Лижет!...* *Лижет!...*"
        m "Да! Держи темп и бы быстренько закончим!"
        m "Ох, чуть не забыл..."
        $ renpy.play('sounds/spit.mp3') #Sound of spiting. 
        pause.3
        $ end_u_2_pic =  "03_hp/17_ending/17.png" #<---- SCREEN
        show screen end_u_2                                            #<---- SCREEN
        with vpunch
        show screen ctc
        pause
        hide screen ctc
        her "..........................."
        her ".................."
        $ end_u_2_pic =  "03_hp/17_ending/18.png" #<---- SCREEN
        show screen end_u_2                                             #<---- SCREEN
        with d7                                                                        #<---- SCREEN
        her "*Глотает!* *Глотает!* *Лижет...* *Глотает!*"
        m "Ты выглядишь довольной с обконченным лицом."
        $ end_u_1_pic =  "03_hp/17_ending/19.png" #<---- SCREEN
        show screen end_u_1                                             #<---- SCREEN
        with d7                                                                        #<---- SCREEN
        her "*Глотает!* *Глотает!* *Лижет...* *Глотает!*"
        m "Хм..."
        her "*Глотает!* *Глотает!* *Лижет...* *Глотает!*"
        m "Может быть покажем это личико всем?"
        m "Должен ли я позвать нескольких твоих одноклассников?"
        $ end_u_2_pic =  "03_hp/17_ending/17.png" #<---- SCREEN
        show screen end_u_2                                            #<---- SCREEN
        with d7                                                                        #<---- SCREEN
        her "!!!!!!!!!!!!!!!"
        m "Расслабься..."
        m "Делай то, что делаешь..."
        $ end_u_1_pic =  "03_hp/17_ending/19.png" #<---- SCREEN
        show screen end_u_1                                            #<---- SCREEN
        with d7                                                                        #<---- SCREEN
        
        
        
        

        show screen bld1
        with d5
        sna "Мисс Грейнджер?"
        sna "{size=-4}(Where is that girl?){/size}"
        ">Среди студентов раздается ропот..."
        hide screen bld1
        with d5
        
        m "Отлично, слушай сюда, сучка."
        $ end_u_2_pic =  "03_hp/17_ending/20.png" #<---- SCREEN
        show screen end_u_2                                            #<---- SCREEN
        with d7                                                                        #<---- SCREEN
        her "*Глотает??*"
        m "Мне нужно, что бы ты оставалась здесь еще немного"
        her "???"
        $ end_u_1_pic =  "03_hp/17_ending/21.png" #<---- SCREEN
        show screen end_u_1                                           #<---- SCREEN
        with d7                                                                        #<---- SCREEN
        m "Да, именно так."
        her "................"
        
        $ end_u_2_pic =  "03_hp/17_ending/22.png" #<---- SCREEN
        show screen end_u_2                                           #<---- SCREEN
        with d7                                                                        #<---- SCREEN
        her "....................................."
        m "Я собираюсь задушить тебя своим членом..."
        m "Это будет весело...расслабься..."
        her "......................................"
        m "Твоя глотка великолепна, сучка."
        her "..........."
        $ end_u_1_pic =  "03_hp/17_ending/23.png" #<---- SCREEN
        show screen end_u_1                                           #<---- SCREEN
        with d7                                                                        #<---- SCREEN
        m "Така теплая и тугая..."
        her "............................................."
        her "...................."
        her "......."
        $ end_u_2_pic =  "03_hp/17_ending/24.png" #<---- SCREEN
        show screen end_u_2                                          #<---- SCREEN
        with d7                                                                        #<---- SCREEN
        with hpunch
        her "!!!"
        m "Знаю, знаю, ты не можешь дышать..."
        g9 "Но в этом и есть вся суть веселья!"
        
        with hpunch
        her "{size=+7}!!!!!!!!!!!!!!!!{/size}"
        m "Перестань сопротивляться, блядь! Ты никуда не пойдешь!"
        with hpunch
        her "{size=+9}!!!!!!!!!!!!!!!!{/size}"
        
        show screen bld1
        with d5
        sna "Мисс Грейнджер..................?"
        sna "Вы пропустите свою коронацию, дрянная девченка!"
        hide screen bld1
        with d5
        
        g9 "Хех..."
        g9 "Ты действительно королева сегодня..."
        g4 "И моя личная сосалка!"
        $ end_u_1_pic =  "03_hp/17_ending/26.png" #<---- SCREEN
        show screen end_u_1                                         #<---- SCREEN
        with d7                                                                        #<---- SCREEN
        her "{size=+7}!!!!!!!!!!!!!!!!{/size}"
        m "Оу, ты посинела, любимая."
        m "Ты в порядке?"
        $ end_u_1_pic =  "03_hp/17_ending/27.png" #<---- SCREEN
        show screen end_u_1                                         #<---- SCREEN
        with d7                                                                        #<---- SCREEN
        her "{size=+9}!!!!!!!!!!!!!!!!........................{/size}"
        m "Сотри, сука!"
        her "{size=+3}........................{/size}"
        g4 "Я сказал, смотри на меня!"
        $ end_u_2_pic =  "03_hp/17_ending/28.png" #<---- SCREEN
        show screen end_u_2                                        #<---- SCREEN
        with d7                                                                        #<---- SCREEN
        her "{size=+9}??!.....................{/size}"
        
        $ renpy.play('sounds/spit.mp3') #Sound of spiting. 
        pause.5
        
        $ end_u_1_pic =  "03_hp/17_ending/29.png" #<---- SCREEN
        show screen end_u_1                                        #<---- SCREEN
       # with d7                                                                        #<---- SCREEN
        with vpunch
        her "{size=+9}*!!!!!!!!!!!!!!!!!!*{/size}" # 4 (EYE)
        
        $ end_u_2_pic =  "03_hp/17_ending/30.png" #<---- SCREEN
        show screen end_u_2                                        #<---- SCREEN
        with d7                                                                        #<---- SCREEN
        her "...................................................................................."
        g4 "Вот это неплохо. Неплохой взгялд."
        $ end_u_1_pic =  "03_hp/17_ending/31.png" #<---- SCREEN
        show screen end_u_1                                        #<---- SCREEN
        with d7                                                                        #<---- SCREEN
        her "...........................................................*SOB!*"
        with hpunch
        g4 "Гхр!"
        g4 "Надвигается!"
        g4 "Я знаю, ты пытаешься взхдохнуть..."
        $ end_u_2_pic =  "03_hp/17_ending/32.png" #<---- SCREEN
        show screen end_u_2                                             #<---- SCREEN
        with d7                                                                        #<---- SCREEN
        g4 "Но, все что ты получишь от меня, это порция горячей спермы!"
        $ end_u_1_pic =  "03_hp/17_ending/33.png" #<---- SCREEN
        show screen end_u_1                                             #<---- SCREEN
        with d7                                                                        #<---- SCREEN
        with hpunch
        her "{size=+9}ГХР!!!!!!!!!!!!!!!!{/size}"
        with hpunch
        g4 "{size=+9}АРГХ!{/size}"
        with hpunch
        $ end_u_2_pic =  "03_hp/17_ending/34.png" #<---- SCREEN
        show screen end_u_2                                             #<---- SCREEN
        with d7                                                                        #<---- SCREEN
        her "{size=+9}*Глоть!-Глоть!-Глоть!-Глоть!-Глоть!*{/size}"
        g4 "{size=+5}Да, шлюшка! Пей мою сперму!{/size}"
        her "*Глоть!-Глоть!-Глоть!-Глоть......*"
        with hpunch
        g4 "Еще нет! Еще не все! Ох!"
        $ end_u_1_pic =  "03_hp/17_ending/35.png" #<---- SCREEN
        show screen end_u_1                                             #<---- SCREEN
        with d7                                                                        #<---- SCREEN
        her "{size=-4}*Глоть!* *Глоть!* *Глоть...*{/size}"
        m "Oh, yes..."
        $ end_u_2_pic =  "03_hp/17_ending/36.png" #<---- SCREEN
        show screen end_u_2                                             #<---- SCREEN
        with d7                                                                        #<---- SCREEN
        her "...................................................."
        m "Ну...я думаю, что это всё--"
        with hpunch
        g4 "{size=+5}Huh?!!{/size}"
        show screen blkfade
        with d3
        stop music fadeout 1.0
        g4 "Эй, как ты--"
        ">Гермиона резко встает и убегает, не сказав ни слова..."
        $ renpy.play('sounds/run_03.mp3')    #<--------------------Sound of running off.
        pause 3
        m "Хм...?"
        m "Оу, точно...коронация..."
        m "............."
        #m "Still need to talk to her though..."
        ">..............{w}..................{w}...................."
    
    pause 1
    
    
    if public_whore_ending: #Students talking. Ending "Public whore".
        $ s_head_xpos = 330 # x = 330,
        $ s_head_ypos = 340 #Right bottom corner: y = 340. y = 380 - no hand.
        $ s_sprite = "03_hp/10_snape_main/snape_03.png"
        show screen s_head2
        sna "Мисс Грейнджер...?"
        $ s_sprite = "03_hp/10_snape_main/snape_04.png"
        sna2 "Вы наконец-то решили показаться?"
        sna2 "Неприятный сюрприз..."
        show screen h_head2                                                             # HERMIONE
        $ h_body = "03_hp/13_hermione_main/body_162.png" # HERMIONE
        her "Профессор..."
        $ s_sprite = "03_hp/10_snape_main/snape_10.png"
        show screen s_head2
        sna "Что ж, выйдите вперед..."
        sna "Вот ваша корона..."
        sna "И ваш пьедестал..."
        $ tiara = True #Tiara is displayed.
        show screen h_head2                                                             # HERMIONE
        $ h_body = "03_hp/13_hermione_main/body_160.png" # HERMIONE
        her "Спасибо, профессор."
        hide screen h_head2        
        pause.7
        
        
        
        $ end_u_1_pic =  "03_hp/17_ending/108.png" #<---- SCREEN
        hide screen blkfade
        with d7
        $ renpy.play('sounds/applause01.ogg') # APPLAUSE
        show screen ctc
        pause
        hide screen ctc
        
        her "..............."
        her ".................................."
        $ end_u_2_pic =  "03_hp/17_ending/109.png" #<---- SCREEN
        show screen end_u_2                                             #<---- SCREEN
        with d7                                                                        #<---- SCREEN
        play music "music/11 Neville's Waltz.mp3" fadein 1 fadeout 1 # BALL THEME.
        her "Здравствуйте все!"
        her "Спасибо вам большое, что выбираете меня королевой второй год подряд!"
        
        show screen blktone
        show screen bld1
        with d3
        m "!!!"
        m "Её прическа выглядит просто идеально!"
        m "Думаю, что я был неправ--"
        g4 "А нет, вот оно!"
        g4 "Стекает за ухом!"
        hide screen blktone
        hide screen bld1
        with d3
        
        $ end_u_1_pic =  "03_hp/17_ending/110.png" #<---- SCREEN
        show screen end_u_1                                             #<---- SCREEN
        with d7                                                                        #<---- SCREEN
        her "Я хотел бы посвятить свое выступление каждой девушки в этой комнате ..."
        
        show screen blktone
        show screen bld1
        with d3
        g4 "Что она там задумала?"
        hide screen blktone
        hide screen bld1
        with d3
        
        $ end_u_2_pic =  "03_hp/17_ending/111.png" #<---- SCREEN
        show screen end_u_2                                             #<---- SCREEN
        with d7                                                                        #<---- SCREEN
        her "Я не собираюсь гвоорить громкие слова о том, что я не заслуживаю такой чести..."
        her "Потому что я думаю, что заслуживаю..."
        $ end_u_1_pic =  "03_hp/17_ending/112.png" #<---- SCREEN
        show screen end_u_1                                             #<---- SCREEN
        with d7                                                                        #<---- SCREEN
        her "Но я действительно благодарна вам за то, что стояю сейчас перед вами."
        
        show screen blktone
        show screen bld1
        with d3
        mal "(Хах?)"
        mal "(Что это у нее на лбу?)"
        mal2 "(Вспотела...?)"
        mal "(Хм... Возможно..)"
        hide screen blktone
        hide screen bld1
        with d3
        $ end_u_2_pic =  "03_hp/17_ending/113.png" #<---- SCREEN
        show screen end_u_2                                             #<---- SCREEN
        with d7                                                                        #<---- SCREEN
        her "В особенности я бы хотела поблагодарить наших учителей за их нелегкий труд."
        
        show screen blktone
        show screen bld1
        with d3
        g4 "Разве она не чувствует этого?"
        g4 "Лучше бы ей закрылиться побыстрее."
        hide screen blktone
        hide screen bld1
        with d3
        
        her "Хогвартс стала поистине вторым домом для всех нас..."
        $ end_u_1_pic =  "03_hp/17_ending/114.png" #<---- SCREEN
        show screen end_u_1                                             #<---- SCREEN
        with d7                                                                        #<---- SCREEN
        her "Я знаю, что я говорю о каждого студента в этом зале, когда я говорю так."
        
        show screen blktone
        show screen bld1
        with d3
        mal "(Это не похоже на пот, хотя...)"
        mal2 "(Даа...)"
        mal2 "(Какая-то странная фигня стекает с её волос...)"
        fem "(Парни, вы реально {size=+5}на столько{/size} слепы?)"
        mal "(Что?)"
        fem "(Это сперма...очивидно же.)"
        mal2 "(Что? Это бред!)"
        fem "(Я думаю, что знаю, как выглядит сперма, и это она!)"
        mal "(Уверен, что знаешь. *Хихикает*)"
        fem "(Не важно. Просто присмотритесь внимательнее.)"
        fem "(Должно быть какой-то парень засунул член в её прическу, и спустил всё туда.)"
        mal "(Хм... Трахать волосы? Это сейчас модно?)"
        mal2 "(Вы, девченки, делаете абсолютно сумасшедшие вещи!)"
        fem "(*Хмпф!* Не все мы шлюхи, вы должны знать.)"
        mal "(К сожалению, нет...)"
        fem "(\"К сожалению\"?!)"
        fem "(Пф! Вы, мужчины, абсолютно невежественны.)"
        fem "(Вы никогда не сможете построить прочных отношений со шлюхой!)"
        mal "(Что такое \"прочные отношения\"?)"
        fem "(Это когда ваша девушка - ваш лучший друг.)"
        mal "(Оу, я думаю, что не нуждаюсь в{size=+5}этом{/size}!)"
        mal "(У меня уже есть лучший друг, и этот уродливый мудак прямо здесь!)"
        mal2 "(Точно, чувак!)"
        mal "(Но я точно уверен, что смог бы найти шлюхе применение в своей жизни!)"
        mal2 "(Точно, чувак!)"
        fem "(...парни, вы такие...)"
        fem "Долбаные идиоты!!!"
        hide screen blktone
        hide screen bld1
        with d3
        $ end_u_2_pic =  "03_hp/17_ending/115.png" #<---- SCREEN
        show screen end_u_2                                             #<---- SCREEN
        with d7                                                                        #<---- SCREEN
        her "Я помню, когда я была еще совсем ребенком..."
        
        show screen blktone
        show screen bld1
        with d3
        m "Ась?"
        hide screen blktone
        hide screen bld1
        with d3
        
        her "Напуганная своей силой...ничего не понимающая"
        
        show screen blktone
        show screen bld1
        with d3
        m "Хм..."
        m "Это...похоже опять..."
        hide screen blktone
        hide screen bld1
        with d3
        
        her "Кто знает, что бы со мной случилось, если бы я не оказалась в Хогвартсе!"
        show screen blktone
        show screen bld1
        with d3
        m "И опять..."
        m "Хм, почему это она так странно подергивает плечем...?"
        hide screen blktone
        hide screen bld1
        with d3
        
        her "Я так рада, что учусь здесь..."
        show screen ctc
        pause
        stop music
        #$ renpy.play('sounds/scratch.wav')
        hide screen ctc
        $ end_u_1_pic =  "03_hp/17_ending/116.png" #<---- SCREEN
        show screen end_u_1                                             #<---- SCREEN
        with d7                                                                        #<---- SCREEN
        show screen ctc
        pause
        
        hide screen ctc
        # TIT BARES
        # MUSIC STOPS
        
        show screen blktone
        show screen bld1
        with hpunch
        g4 "!!!"
        #play music "music/(Orchestral) Playful Tension by Shadow16nh.mp3" fadein 1 fadeout 1 # SEX THEME.
        $ s_sprite = "03_hp/10_snape_main/snape_11.png"
        show screen s_head2
        sna "!!!"
        hide screen s_head2
        hide screen blktone
        hide screen bld1
        show screen ctc
        pause
        hide screen ctc
        play music "music/11 Neville's Waltz.mp3" fadein 1 fadeout 1 # BALL THEME.
        her "Спасибо большое вам всем..."
        $ end_u_2_pic =  "03_hp/17_ending/117.png" #<---- SCREEN
        show screen end_u_2                                             #<---- SCREEN
        with d7                                                                        #<---- SCREEN
        her "Позвольте мне повториться..."
        $ end_u_1_pic =  "03_hp/17_ending/118.png" #<---- SCREEN
        show screen end_u_1                                             #<---- SCREEN
        with d7                                                                        #<---- SCREEN
        her "Спасибо вам большое, что выбрали меня королевой бала в этом году..."
        show screen ctc
        pause
        hide screen ctc
        # SEX MUSIC STARTS TO PLAY
        
        show screen blktone
        with d7
        #play music "music/(Orchestral) Playful Tension by Shadow16nh.mp3" fadein 1 fadeout 1 # SEX THEME.
        mal "(Может у меня глюки?)"
        mal2 "(Похоже что нет...я тоже это вижу...)"
        mal "(Сиськи...Гермионы...Грейнджер...)"
        mal "(Похоже её платье порвалось, чувак!)"
        fem "(О нет! Мы должны сказать ей!)"
        mal "(Не смей лишать нас такого зрелища!)"
        fem "(Но...!!)"
        hide screen blktone
        with d7
        
        show screen ctc
        pause
        hide screen ctc
        her "И больше всего я благодарна моим родителям..."
        her "Они помогли мне..."
        her "Мама... Папа..."
        $ end_u_2_pic =  "03_hp/17_ending/119.png" #<---- SCREEN
        show screen end_u_2                                             #<---- SCREEN
        with d7                                                                        #<---- SCREEN
        her "Я бы хотела, что бы вы увидели, как сильно Хогвартс изменил меня..."
        her "Я бы хотела, что бы вы могли увидеть вашу девочку сейчас..."
        her "{size=-5}Ах...{/size}{image=textheart.png}"
        show screen ctc
        pause
        hide screen ctc
        
        show screen blktone
        with d7
        g4 "Эта шлюха покраснела! Похоже она отлично знает, что просиходит!"
        g4 "Настаящая шалава!"
        g4 "(Интересно, она спланировала всё это??!)"
        m "(Аарабская нооочь...Кхм...О чем это я!?)"
        hide screen blktone
        with d7
        
        $ end_u_1_pic =  "03_hp/17_ending/120.png" #<---- SCREEN
        show screen end_u_1                                             #<---- SCREEN
        with d7                                                                        #<---- SCREEN
        her "..............................."
        her ".................."
        show screen ctc
        pause
        hide screen ctc
        
        show screen blktone
        with d7
        mal "(Теперь она просто стоит...)"
        mal2 "(Мы успеем разглядеть получше...?)"
        mal "(Ты думаешь она не знает, что её дойки видны всем?)"
        fem "(Стыдно-то как...)"
        fem "(Похоже, что я чуть не пожалела настоящую шлюху...)"
        fem "........................"
        with hpunch
        fem "{size=+7}Прикрой сиськи, шлюха!!!{/size}"
        mal "(!!!)"
        mal2 "(Ты с ума сошла?!)"
        with hpunch
        fem "{size=+7}Гриффиндорская шлюха!!!{/size}"
        hide screen blktone
        with d7
        
        $ end_u_2_pic =  "03_hp/17_ending/121.png" #<---- SCREEN
        show screen end_u_2                                             #<---- SCREEN
        with d7                                                                        #<---- SCREEN
        her "{size=-3}Ah...{/size}{image=textheart.png}"
        her "...............................А-ха...{image=textheart.png}{image=textheart.png}{image=textheart.png}"
        show screen ctc
        pause
        hide screen ctc
        
        show screen bld1
        with d7
        cr1 "Покажи нам обе, Гермиона!"
        cr2 "Смотрите! Её лицо покрыто спермой!"
        cr1 "Тебе не стыдно?!"
        cr2 "Прикройся, шлюха!"
        hide screen bld1
        with d7
        
        $ end_u_1_pic =  "03_hp/17_ending/122.png" #<---- SCREEN
        show screen end_u_1                                             #<---- SCREEN
        with d7                                                                        #<---- SCREEN
        her "Ох...точно..."
        her "Чуть не забыла..."
        $ end_u_2_pic =  "03_hp/17_ending/123.png" #<---- SCREEN
        show screen end_u_2                                             #<---- SCREEN
        with d7                                                                        #<---- SCREEN
        her "{size=+5}Вперед, Гриффиндор{/size}"
        $ renpy.play('sounds/applause01.ogg') # APPLAUSE
        "*Дикие возгласы восхищения!*"
        $ end_u_1_pic =  "03_hp/17_ending/120.png" #<---- SCREEN
        show screen end_u_1                                             #<---- SCREEN
        with d7                                                                        #<---- SCREEN
        her "......................................"
        her ".........................................................."
        show screen ctc
        pause
        hide screen ctc
        
        show screen bld1
        with d7
        $ s_sprite = "03_hp/10_snape_main/snape_12.png"
        show screen s_head2
        sna "Замолчите сейчас же!"
        sna "Что касается вас, мисс Грейнджер..."
        sna "Я думаю, что это уж слишком."
        sna "Выметайтесь со сцены...Быстро..."
        hide screen s_head2
        pause.1
        hide screen bld1
        with d7
        
        $ end_u_2_pic =  "03_hp/17_ending/122.png" #<---- SCREEN
        show screen end_u_2                                             #<---- SCREEN
        with d7                                                                        #<---- SCREEN
        her "\"Выметаться\", сэр?"
        $ end_u_1_pic =  "03_hp/17_ending/119.png" #<---- SCREEN
        show screen end_u_1                                             #<---- SCREEN
        with d7                                                                        #<---- SCREEN
        her "Ох? Что это? Не может быть...одна из моих малышек выпала из платья..."
        $ end_u_2_pic =  "03_hp/17_ending/120.png" #<---- SCREEN
        show screen end_u_2                                             #<---- SCREEN
        with d7                                                                        #<---- SCREEN
        her "Как неловко..."
        $ end_u_1_pic =  "03_hp/17_ending/121.png" #<---- SCREEN
        show screen end_u_1                                             #<---- SCREEN
        with d7                                                                        #<---- SCREEN
        her "Ах...{image=textheart.png}{image=textheart.png}{image=textheart.png}"
        show screen ctc
        pause
        hide screen ctc
        
        show screen bld1
        with d7
        cr1 "Шлюха!"
        cr2 "Гриффиндорская сосалка!"
        cr1 "Я люблю ебя, Гермиона!"
        cr2 "Гриффиндор рулит!!!"
        
        $ s_sprite = "03_hp/10_snape_main/snape_18.png"
        show screen s_head2
        sna "Мисс Грейнджер, я сказал - достаточно!"
        hide screen s_head2
        pause.1
        hide screen bld1
        with d7
        her "Как скажете, профессор..."
        show screen bld1
        with d7
        $ s_sprite = "03_hp/10_snape_main/snape_12.png"
        show screen s_head2
        sna "И вытрите лицо. Выглядит отвратительно."
        hide screen s_head2
        pause.1
        hide screen bld1
        $ end_u_2_pic =  "03_hp/17_ending/122.png" #<---- SCREEN
        show screen end_u_2                                             #<---- SCREEN
        with d7                                                                        #<---- SCREEN
        her "Ой, правда? Это всего лишь мой--"
        show screen bld1
        with d7
        $ s_sprite = "03_hp/10_snape_main/snape_18.png"
        show screen s_head2
        sna "Мне это не интересно! Идите уже отсюда!"
        sna "Сейчас же!"
        hide screen s_head2
        pause.1
        hide screen bld1
        with d7
        $ end_u_1_pic =  "03_hp/17_ending/120.png" #<---- SCREEN
        show screen end_u_1                                             #<---- SCREEN
        with d7                                                                        #<---- SCREEN
        show screen ctc
        pause
        hide screen ctc
        show screen blkfade
        with d7
        $ renpy.play('sounds/applause01.ogg') # APPLAUSE
        ">Дикие вопли восхищений сопровождают Гермиону, пока она спускается по лестнице..."
        pause 1
        stop music fadeout 3.0
        ">.......................{w}....................{w}......................."
        
        # BACK AT THE ALCOVE (BLACK SCREEN STILL).
        $ end_u_2_pic =  "03_hp/17_ending/02.png" #<---- SCREEN
        show screen end_u_2                                             #<---- SCREEN
        with d7                                                                        #<---- SCREEN
        
        hide screen blkfade
        with d7
        show screen bld1
        with d5
        show screen ctc
        pause
        hide screen ctc
        
        $ her_head_xpos=390 #Defines position of the Hermione's full length sprite. (Default 370). 140 - center. Bottom right: 390
        $ her_head_ypos=235 #Defines position of the Hermione's full length sprite. (Default 0). Right bottom corner: 340 - head only. 235 - tits.
        show screen h_head2                                                             # HERMIONE
        $ h_body = "03_hp/13_hermione_main/body_165.png" # HERMIONE
        her "Профессор Дамблодор..."
        her2 "Вы хотели о чем-то поговорить со мной?"
        hide screen h_head2
        g4 "Поздно, сука!"
        show screen blkfade
        with d5
        show screen h_head2                                                             # HERMIONE
        $ h_body = "03_hp/13_hermione_main/body_164.png" # HERMIONE
        her "Сэр?!"
        hide screen h_head2
        g4 "Теперь я оттрахаю тебя как следует! Иди сюда!"
        play music "music/(Orchestral) Playful Tension by Shadow16nh.mp3" fadein 1 fadeout 1 # SEX THEME.
        show screen h_head2                                                             # HERMIONE
        $ h_body = "03_hp/13_hermione_main/body_181.png" # HERMIONE
        her "Конечно, сэр..."
        hide screen h_head2
        # INSERTION
        
        $ renpy.play('sounds/gltch.mp3')
        with hpunch
        with kissiris
        pause.5
        g4 "{size=+7}О ДААА!{/size}"
        
        
        $ end_u_1_pic =  "03_hp/17_ending/46.png" #<---- SCREEN
        show screen end_u_1                                             #<---- SCREEN
        with d2                                                                        #<---- SCREEN
        hide screen blkfade
        hide screen bld1
        with d7
        
        show screen ctc
        pause
        hide screen ctc
        
        
        her "Ааах!!!"
        g4 "Твоя речь обернулась полным позорм, девчонка!"
        $ end_u_2_pic =  "03_hp/17_ending/50.png" #<---- SCREEN
        show screen end_u_2                                             #<---- SCREEN
        with d7                                                                        #<---- SCREEN
        her "Мне кажется, все прошло довольно не плохо..."
        g4 "Имеешь ввиду твою грудь, которую мог увидеть каждый?!"
        $ end_u_1_pic =  "03_hp/17_ending/56.png" #<---- SCREEN
        show screen end_u_1                                             #<---- SCREEN
        with d2                                                                        #<---- SCREEN
        her "Не только это...ах..."
        g4 "Что?"
        her "Не только моя грудь..."
        g4 "Что случилось с той идеалисткой и невинной девочкой, которую я когда-то знал?!"
        $ end_u_2_pic =  "03_hp/17_ending/59.png" #<---- SCREEN
        show screen end_u_2                                             #<---- SCREEN
        with d7                                                                        #<---- SCREEN
        her "Вы выебали её из меня, сэр!"
        g4 "Ты чертовски права, детка!"
        $ end_u_1_pic =  "03_hp/17_ending/124.png" #<---- SCREEN
        show screen end_u_1                                             #<---- SCREEN
        with d2                                                                        #<---- SCREEN
        her "Выебали её из меня огромным членом, сэр!"
        g4 "Аргх! Шлюшка!"
        $ renpy.play('sounds/slap.mp3')
        show screen white 
        pause.1
        hide screen white
        with hpunch
        # SLAP!
        $ end_u_2_pic =  "03_hp/17_ending/58.png" #<---- SCREEN
        show screen end_u_2                                             #<---- SCREEN
        with d7                                                                        #<---- SCREEN
        her "Ах!!!"
        g4 "Заткнись, сучка! Тебя может кто-нибудь услышать!"
        $ renpy.play('sounds/slap.mp3')
        show screen white 
        pause.1
        hide screen white
        with hpunch
        # SLAP!
        
        her "Ах! Профссор!"
        g4 "Я скахал, тихо!"
        
        $ renpy.play('sounds/slap.mp3')
        show screen white 
        pause.1
        hide screen white
        with hpunch
        # SLAP!
        $ end_u_1_pic =  "03_hp/17_ending/55.png" #<---- SCREEN
        show screen end_u_1                                             #<---- SCREEN
        with d5                                                                       #<---- SCREEN
        her "Ах! Профессор!"
        $ end_u_2_pic =  "03_hp/17_ending/124.png" #<---- SCREEN
        show screen end_u_2                                               #<---- SCREEN
        with d5                                                                         #<---- SCREEN
        her "Да! Жесче, трахайте меня жесче!"
        m "Ты специально стонешь погромче, маленькая шлюшка?"
        g4 "Хочешь быть пойманной?"
        g4 "На профессорсокм члене?"
        $ end_u_1_pic =  "03_hp/17_ending/125.png" #<---- SCREEN
        show screen end_u_1                                             #<---- SCREEN
        with d5                                                                        #<---- SCREEN
        her "Ах! Может быть..."
        $ end_u_2_pic =  "03_hp/17_ending/124.png" #<---- SCREEN
        show screen end_u_2                                               #<---- SCREEN
        with d5                                                                         #<---- SCREEN
        her "Назовите меня \"грязнокровкой\", сэр!"
        m "Что?"
        $ end_u_1_pic =  "03_hp/17_ending/51.png" #<---- SCREEN
        show screen end_u_1                                             #<---- SCREEN
        with d5                                                                        #<---- SCREEN
        her "Назовите меня \"грязнокровкой\", пожалуйста!"
        m "\"Грязнокровкой\"?"
        $ end_u_2_pic =  "03_hp/17_ending/58.png" #<---- SCREEN
        show screen end_u_2                                             #<---- SCREEN
        with d5                                                                        #<---- SCREEN
        her "О! Да! Да! Я шлюхо-грязнокровка!"
        g4 "Эм...не важно!"
        
        #SLAP
        #SLAP
        #SLAP
        #SLAP
        
        
        $ renpy.play('sounds/slap.mp3')
        show screen white 
        pause.5
        hide screen white
        with hpunch
        
        $ renpy.play('sounds/slap.mp3')
        show screen white 
        pause.4
        hide screen white
        with hpunch
        
        $ renpy.play('sounds/slap.mp3')
        show screen white 
        pause.3
        hide screen white
        with hpunch
        
        $ renpy.play('sounds/slap.mp3')
        show screen white 
        pause.3
        hide screen white
        with hpunch
        
        $ renpy.play('sounds/slap.mp3')
        show screen white 
        pause.2
        hide screen white
        with hpunch
        
        $ renpy.play('sounds/slap.mp3')
        show screen white 
        pause.1
        hide screen white
        with hpunch

        
        $ end_u_1_pic =  "03_hp/17_ending/64.png" #<---- SCREEN
        show screen end_u_1                                             #<---- SCREEN
        with d5                                                                        #<---- SCREEN
        
        her "ААААААХ!ДААААА!"
        her "ДА!!! ДАААААА! АХ!"
        $ end_u_2_pic =  "03_hp/17_ending/63.png" #<---- SCREEN
        show screen end_u_2                                             #<---- SCREEN
        with d5                                                                        #<---- SCREEN
        her "Трахайте меня! Сильнее! Да!!!"
        g4 "Гхр! Сильнее, сучка?!"
        g4 "!!!"
        g4 "Дерьмо! Кто-то идет сюда!"
        $ end_u_1_pic =  "03_hp/17_ending/64.png" #<---- SCREEN
        show screen end_u_1                                             #<---- SCREEN
        with d5                                                                        #<---- SCREEN
        her "Нет, сэр, погодите! Отшлепайте меня!"
        g4 "Нет, идиотка! Какие-то придурки идут сюда!"
        $ end_u_2_pic =  "03_hp/17_ending/127.png" #<---- SCREEN
        show screen end_u_2                                             #<---- SCREEN
        with d5                                                                        #<---- SCREEN
        her "Что?!"
        
        # STUDENTS
        
        sly1 "Так, так, так...что это у нас тут?"
        $ end_u_1_pic =  "03_hp/17_ending/126.png" #<---- SCREEN
        show screen end_u_1                                             #<---- SCREEN
        with d7                                                                        #<---- SCREEN
        show screen ctc
        pause
        hide screen ctc
        her "!!!"
        sly1 "Я так и думал, что это \"гриффиндорская\"..."
        sly1 "Стонущая как шлюха..."
        sly1 "Которую трахает... Ой..."
        with hpunch
        sly1 "Профессор Дамблодор!?"
        m "Привет, парни..."
        her ".........................."
        sly1 "Упс... Эм... Мы не думали..."
        sly1 "Мы уже уходим..."
        m "Что? Не тупи, парень."
        m "Присоединяйтесь!"
        sly1 "Среьезно?"
        $ end_u_2_pic =  "03_hp/17_ending/128.png" #<---- SCREEN
        show screen end_u_2                                             #<---- SCREEN
        with d5                                                                        #<---- SCREEN
        her "ЧТО?!"
        m "Конечно."
        $ end_u_1_pic =  "03_hp/17_ending/129.png" #<---- SCREEN
        show screen end_u_1                                             #<---- SCREEN
        with d7                                                                        #<---- SCREEN
        her "Профессор!!!?"
        m "Она в полном вашем распоряжении!"
        $ end_u_2_pic =  "03_hp/17_ending/130.png" #<---- SCREEN
        show screen end_u_2                                             #<---- SCREEN
        with d5                                                                        #<---- SCREEN
        her "Профессор! Нет!"
        m "Что-то не так, сучка?"
        $ end_u_1_pic =  "03_hp/17_ending/129.png" #<---- SCREEN
        show screen end_u_1                                             #<---- SCREEN
        with d7                                                                        #<---- SCREEN
        her "Сэр, умоляю...не называйте так меня перед ними..."
        m "Что это с тобой стряслось? Вдруг стала такой застенчивой..."
        her "Разве вы не видете, что это \"Слизеринцы\"?!"
        m "И что?"
        her "Наши факультеты...это длинная история."
        m "Эм..."
        m "Что ж, ты станешь не плохим мостиком между \"Слизерином\" и \"Гриффиндором\"!"
        m "Гермиона Грейнджер, миротворец!"
        $ end_u_2_pic =  "03_hp/17_ending/130.png" #<---- SCREEN
        show screen end_u_2                                             #<---- SCREEN
        with d5                                                                        #<---- SCREEN
        her "Нет, сэр! Я стесняюсь!"
        her "И перестаньте долбить меня, пока мы говорим, сэр!"
        m "Парни, чего вы так долго возитесь?"
        m "Я же сказал, эта шлюха в вашем распоряжении!"
        her "Профессор Дамбл--"
        sly1 "Заткнись, тварь!"
        
        # FACE SPIT
        
        $ renpy.play('sounds/spit.mp3') #Sound of spiting. 
        show screen white
        $ end_u_2_pic =  "03_hp/17_ending/132.png" #<---- SCREEN
        show screen end_u_2                                             #<---- SCREEN
        pause.2
        hide screen white
        with hpunch
        

        
        show screen ctc
        pause
        hide screen ctc
        
        $ end_u_1_pic =  "03_hp/17_ending/133.png" #<---- SCREEN
        show screen end_u_1                                             #<---- SCREEN
        with d5                                                                        #<---- SCREEN
        her "!!!"
        m "Ну, начали!"
        
        sly2 "Ха-ха-ха! Неплохо! Взгляните на это тупое выражение лица!"
        $ end_u_2_pic =  "03_hp/17_ending/134.png" #<---- SCREEN
        show screen end_u_2                                             #<---- SCREEN
        with d5                                                                        #<---- SCREEN
        her "Вы... Вы...!"
        sly1 "Нам очень даже понравилось твое выступление, \"гриффиндорская сосалка\"."
        sly2 "Да... очень даже..."
        her "Это было не для вас, Слизеринских отморозков!"
        sly1 "Разве не для нас? Ты действительно такая дура?"
        sly1 "Ты показала свою грязнокровкину сиську на сцене! Перед всей школой!"
        sly1 "{size=+7}Конечно это было для всех, в том числе для нас, тупая ты пизда!{/size}"
        
        $ end_u_1_pic =  "03_hp/17_ending/135.png" #<---- SCREEN
        show screen end_u_1                                             #<---- SCREEN
        with d5                                                                        #<---- SCREEN

        her "Сэр! Прекратите трахать меня!"
        m "Ась? Разве тебе не нравится?"
        with hpunch
        pause.3
        her "Ах-аха! Нет, прекратите, профессор!"
        m "Остановиться? Мне казалось нужно трахать сильнее!"
        with hpunch
        pause.3
        with hpunch
        pause.3
        with hpunch
        pause.3
        $ end_u_2_pic =  "03_hp/17_ending/133.png" #<---- SCREEN
        show screen end_u_2                                             #<---- SCREEN
        with d5                                                                        #<---- SCREEN
        her "Аах-ха!!!"
        sly1 "Да... Теперь ты наша, шлюха!"
        
        show screen ctc
        pause
        hide screen ctc
        
        # DICKS OUT
        $ end_u_1_pic =  "03_hp/17_ending/136.png" #<---- SCREEN
        show screen end_u_1                                             #<---- SCREEN
        with d5                                                                        #<---- SCREEN
        her "Что?! Что вы делаете?!"
        $ end_u_2_pic =  "03_hp/17_ending/137.png" #<---- SCREEN
        show screen end_u_2                                             #<---- SCREEN
        with d5                                                                        #<---- SCREEN
        her "Уберите от меня ваши грязные члены, придурки!"
        with hpunch
        pause.3
        $ end_u_1_pic =  "03_hp/17_ending/138.png" #<---- SCREEN
        show screen end_u_1                                             #<---- SCREEN
        with d5                                                                        #<---- SCREEN
        her "Ах... Аха..."
        sly1 "Да... Я так давно ждал этого..."
        her "Профессор!"
        m "Ась? О, не думай обр мне, девочка."
        m "Представь, что меня тут нет..."
        
        # SPIT!
        
        $ renpy.play('sounds/spit.mp3') #Sound of spiting. 
        show screen white
        $ end_u_1_pic =  "03_hp/17_ending/139.png" #<---- SCREEN
        show screen end_u_1                                             #<---- SCREEN
        pause.2
        hide screen white
        with hpunch
        

        
        show screen ctc
        pause
        hide screen ctc
        
        $ end_u_2_pic =  "03_hp/17_ending/140.png" #<---- SCREEN
        show screen end_u_2                                             #<---- SCREEN
        with d5                                                                        #<---- SCREEN
        her "Прекратите! Хватит плевать мне в лицо, ублюдки!"
        sly1 "Что ты сделаешь, шлюха!"
        her "Я вас предупреждаю--"
        
        $ renpy.play('sounds/spit.mp3') #Sound of spiting. 
        show screen white
        $ end_u_2_pic =  "03_hp/17_ending/141.png" #<---- SCREEN
        show screen end_u_2                                            #<---- SCREEN
        pause.2
        hide screen white
        with hpunch
        

        
        show screen ctc
        pause
        hide screen ctc
        
        # SPIT!
        $ end_u_1_pic =  "03_hp/17_ending/142.png" #<---- SCREEN
        show screen end_u_1                                             #<---- SCREEN
        with d5                                                                        #<---- SCREEN
        her "{size=+5}*Глоть!*{/size}"
        sly2 "Аха-ха-ха! Прямо в рот! Отличное попадание, приятель!"
        sly1 "И она проглотила его тут же!"
        $ end_u_2_pic =  "03_hp/17_ending/140.png" #<---- SCREEN
        show screen end_u_2                                             #<---- SCREEN
        with d5                                                                        #<---- SCREEN
        her "Это было случайно!"
        sly1 "Правда? Давай посмотрим!"
        her "Ась?"
        
        # SPIT!
        
        $ renpy.play('sounds/spit.mp3') #Sound of spiting. 
        show screen white
        $ end_u_2_pic =  "03_hp/17_ending/141.png" #<---- SCREEN
        show screen end_u_2                                            #<---- SCREEN
        pause.2
        hide screen white
        with hpunch
        

        
        show screen ctc
        pause
        hide screen ctc

        
        # SPIT!
        $ end_u_1_pic =  "03_hp/17_ending/142.png" #<---- SCREEN
        show screen end_u_1                                             #<---- SCREEN
        with d5                                                                        #<---- SCREEN
        her "{size=+5}*Глоть!*{/size}"
        
        

        sly2 "Она снова проглотила!"
        $ end_u_2_pic =  "03_hp/17_ending/140.png" #<---- SCREEN
        show screen end_u_2                                             #<---- SCREEN
        with d5                                                                        #<---- SCREEN
        her "Это было неожиданно...просто рефлекс!"
        sly1 "Интересный рефлекс!"
        g4 "О... да..."
        with hpunch
        pause.3
        with hpunch
        pause.3
        her "Ах... Ах-аха..."
        her "Вы за это заплатите, тупые слизери--"
        sly1 "Заткнись, грязнокровка!"
        $ end_u_1_pic =  "03_hp/17_ending/143.png" #<---- SCREEN
        show screen end_u_1                                                #<---- SCREEN
        with hpunch                                                                        #<---- SCREEN
        
        # DICK IN MOUTH
        
        show screen ctc
        pause
        hide screen ctc
        
        her "!!!........................................................."
        sly2 "Отлично! Я следующий!"
        her "*Глоть!*"
        sly1 "Соси мой член, сука! Соси, я сказал!"
        m "Делай то, что тебе говорят мальчики."
        $ renpy.play('sounds/slap.mp3')
        show screen white 
        pause.3
        hide screen white
        with hpunch
        
        # SLAP!
        
        m "Ну же!"
        $ end_u_2_pic =  "03_hp/17_ending/144.png" #<---- SCREEN
        show screen end_u_2                                             #<---- SCREEN
        with d5                                                                        #<---- SCREEN
        her "*Чавк...*"
        sly1 "Она сделала это! Гермиона Грейнджер отсасывает у меня, парни!"
        sly2 "Здорово! Не могу дождаться своей очереди!"
        sly1 "О... воу... она хороша..."
        her "*Чавк!* *Чавк!* *Глоть!*"
        sly1 "О да... Да..."
        sly1 "Ох... Ты отлично сосешь, шлюха!"
        sly1 "Это... Я..."
        
        show screen white 
        pause.1
        hide screen white
        pause.2
        show screen white 
        pause .1
        hide screen white
        $ end_u_1_pic =  "03_hp/17_ending/145.png" #<---- SCREEN
        show screen end_u_1                                             #<---- SCREEN
        with hpunch
        her "{size=+7}*Глотает?!?*{/size}"
        sly1 "{size=+5}Да, да! Глотай всё!!!{/size}"
        

        $ end_u_2_pic =  "03_hp/17_ending/146.png" #<---- SCREEN
        show screen end_u_2                                             #<---- SCREEN
        with d5                                                                        #<---- SCREEN
        # CUMMING
        
        her "{size=+5}*Глоть-Глоть-Глоть-Глоть!*{/size}"
        her "*{size=+3}Глоть-Глоть-Глоть...*{/size}"
        her "*Глоть-Глоть-Глоть...*"
        her "{size=-3}*Глоть* *Глоть*{/size}"
        her "{size=-5}*Глоть*..................{/size}"
        her "........................................"
        $ end_u_1_pic =  "03_hp/17_ending/147.png" #<---- SCREEN
        show screen end_u_1                                             #<---- SCREEN
        with d5                                                                        #<---- SCREEN
        her "Г-ха..."
        her "Это все на что ты способен? Слабак!"
        sly2 "Ох... Заткнись сучка... Ты высосала меня досуха..."
        $ end_u_2_pic =  "03_hp/17_ending/137.png" #<---- SCREEN
        show screen end_u_2                                             #<---- SCREEN
        with d5                                                                        #<---- SCREEN
        her "Ну же! Кто следующий?!"
        sly2 "Я! Я следующий!"
        $ end_u_1_pic =  "03_hp/17_ending/148.png" #<---- SCREEN
        show screen end_u_1                                             #<---- SCREEN
        with hpunch                                                                       #<---- SCREEN
        
        show screen ctc
        pause
        hide screen ctc
        
        $ end_u_2_pic =  "03_hp/17_ending/149.png" #<---- SCREEN
        show screen end_u_2                                             #<---- SCREEN
        with d5                                                                        #<---- SCREEN
        her "*Чавк!* *Чавк!* *Чавк!*"
        g4 "О... Да... Да!"
        with hpunch
        pause.3
        with hpunch
        pause.3
        her "*Чавк!* *Чавк!* *Чавк!*"
        sly2 "Ох! Ее рот такой скользкий и теплый!"
        her "*Чавк!* *Чавк!* *Чавк!*"
        g4 "Да! Соси, сучка, соси мой член!"
        with hpunch
        pause.3
        with hpunch
        pause.3
        her "*Глоть!* Глоть!* *Чавк!*"
        sly2 "Я не знаю... гх... Как долго..."
        sly2 "...Я смогу сдерживаться."
        her "*Чавк--Чавк-Чавк-Чавк!*"
        her "*Чавк-Глоть-Чавк-Чавк-Глоть!!!*"
        sly2 "О, Боже... О, Боже..."
        her "*Чавк-Чавк-Чавк-Чавк-Чавк!!*"
        sly2 "Я... Я..."
        sly2 "..................."
        her "*Чавк-Чавк-Чавк-Чавк-Чавк!!*"
        with hpunch
        sly2 "{size=+7}I'm cummiiiiiiiiing!{/size}"
        
        show screen white 
        pause.1
        hide screen white
        pause.2
        show screen white 
        pause .1
        hide screen white
        $ end_u_2_pic =  "03_hp/17_ending/150.png" #<---- SCREEN
        show screen end_u_1                                             #<---- SCREEN
        with hpunch
        her "{size=+7}*Глотает?!?*{/size}"
        $ end_u_1_pic =  "03_hp/17_ending/149.png" #<---- SCREEN
        show screen end_u_1                                             #<---- SCREEN
        with d5                                                                        #<---- SCREEN
        her "{size=+5}*Глоть-Глоть-Глоть-Глоть!*{/size}"
        her "{size=+3}*Глоть-Глоть...*{/size}"
        her "*Глоть....."
        sly2 "Ах... мой член..."
        $ end_u_2_pic =  "03_hp/17_ending/152.png" #<---- SCREEN
        show screen end_u_2                                             #<---- SCREEN
        with d5                                                                        #<---- SCREEN
        her "Г-ха..."
        $ end_u_1_pic =  "03_hp/17_ending/151.png" #<---- SCREEN
        show screen end_u_1                                             #<---- SCREEN
        with d5                                                                        #<---- SCREEN
        her "Следующий! Давайте же! Это все, на что вы способны?"
        sly1 "Я следующий, грязнокровка!"
        $ end_u_2_pic =  "03_hp/17_ending/154.png" #<---- SCREEN
        show screen end_u_2                                             #<---- SCREEN
        with d5                                                                        #<---- SCREEN
        her "{size=-5}Ах... Не назыай меня так, урод...{/size}{image=textheart.png}"
        sly1 "Трахать твоё лицо действительно здорово, сучка!"
        sly1 "И после того, как я наполню твой рот спермой, ты скажешь мне спасибо!"
        sly1 "Поняла, шлюхо-грязнокровка?"
        $ end_u_1_pic =  "03_hp/17_ending/153.png" #<---- SCREEN
        show screen end_u_1                                             #<---- SCREEN
        with d5                                                                        #<---- SCREEN
        her "Иди на хер!"
        
        # Spit!
        
                
        $ renpy.play('sounds/spit.mp3') #Sound of spiting. 
        show screen white
        $ end_u_2_pic =  "03_hp/17_ending/141.png" #<---- SCREEN
        show screen end_u_2                                            #<---- SCREEN
        pause.2
        hide screen white
        with hpunch
        

        
        show screen ctc
        pause
        hide screen ctc

        
        # SPIT!
        $ end_u_1_pic =  "03_hp/17_ending/142.png" #<---- SCREEN
        show screen end_u_1                                             #<---- SCREEN
        with d5                                                                        #<---- SCREEN
        her "{size=+5}*Глоть!*{/size}"
        
        
        
        

        sly1 "Вот о чем я!"
        $ end_u_2_pic =  "03_hp/17_ending/154.png" #<---- SCREEN
        show screen end_u_2                                             #<---- SCREEN
        with d5                                                                        #<---- SCREEN
        her "Вы слабаки...\"slythe-"
        $ end_u_1_pic =  "03_hp/17_ending/155.png" #<---- SCREEN
        show screen end_u_1                                             #<---- SCREEN
        with d5                                                                   #<---- SCREEN
        her "!!?"
        $ end_u_2_pic =  "03_hp/17_ending/156.png" #<---- SCREEN
        show screen end_u_2                                             #<---- SCREEN
        with d5                                                                        #<---- SCREEN
        her "*Чавк!* *Чавк!* *Чавк!*"
        sly1 "Да! Да. ты чертова грязнокровка! Соси! Соси мой член!"
        m "Это довольно необычно..."
        sly1 "Сэр?"
        m "Просто..."
        m "Её пизда..."
        $ end_u_1_pic =  "03_hp/17_ending/155.png" #<---- SCREEN
        show screen end_u_1                                             #<---- SCREEN
        with d5                                                                   #<---- SCREEN
        her "*Чавк?*"
        m "Она сильно сжимается, когда ты называешь её \"грязнокровкой\"..."
        m "Попробуй снова назвать её так, парень."
        sly1 "Без проблем, сэр."
        $ end_u_2_pic =  "03_hp/17_ending/156.png" #<---- SCREEN
        show screen end_u_2                                             #<---- SCREEN
        with d5                                                                        #<---- SCREEN
        her "*Чавк!* *Чавк!* *Чавк!*"
        sly1 "Да, шлюха! Мне нравится трахать лицо грязнокровки!"
        sly1 "И тебе тоже нравится каждое мгновения, пока я делаю это, верно?"
        sly1 "Верно, грязнокровка?"
        her "*Чавк!* *Чавк!* *Глоть!*"
        m "Агась... Каждый раз когда ты называл её..."
        m "Ась?"
        m "Что это? Её ноги трясутся!"
        m "Ты уже кончила, сучка?"
        $ end_u_1_pic =  "03_hp/17_ending/157.png" #<---- SCREEN
        show screen end_u_1                                             #<---- SCREEN
        with d5                                                                   #<---- SCREEN
        her "..............................................."
        m "Я так и думал!"
        m "Парни, давайте немного ускоримся!"
        m "Давайте трахать её с двух сторон, пока она кончает как грязная шлюха!"
        sly1 "Конечно, сэр."
        sly1 "Возьмика это, \"грязнокровная\" шлюха!"
        with vpunch
        pause.3
        with vpunch
        pause.3
        with vpunch
        pause.3
        g4 "И это!!!"
        with hpunch
        pause.3
        with hpunch
        pause.3
        with hpunch
        pause.3
        her "{size=+7}!!!!!!!!{/size}"
        g4 "Да! Её киска переполнена соком!"
        sly1 "Агх! Её рот просто великолепен, сэр."
        sly1 "Я не знаю, как долго я... ох..."
        sly1 "Аргх!"
        sly1 "{size=+3}Да! Принимай порцию спермы, сучка!{/size}"
        
        
        
        show screen white 
        pause.1
        hide screen white
        pause.2
        show screen white 
        pause .1
        hide screen white
        $ end_u_1_pic =  "03_hp/17_ending/159.png" #<---- SCREEN
        show screen end_u_1                                             #<---- SCREEN
        with hpunch
        her "{size=+7}*Глотает?!?*{/size}"
        sly1 "{size=+5}Да, да! Глотай всё, до последней капли!!!{/size}"
        

        $ end_u_2_pic =  "03_hp/17_ending/160.png" #<---- SCREEN
        show screen end_u_2                                             #<---- SCREEN
        with d5                                                                        #<---- SCREEN
        # CUMMING
        
        her "{size=+5}*Глоть-Глоть-Глоть-Глоть!*{/size}"
        her "*{size=+3}Глоть-Глоть-Глоть...*{/size}"
        her "*Глоть-Глоть-Глоть...*"
        her "{size=-3}*Глоть* *Глоть*{/size}"
        her "{size=-5}*Глоть*..................{/size}"
        her "........................................"
        her "....................."
        $ end_u_1_pic =  "03_hp/17_ending/154.png" #<---- SCREEN
        show screen end_u_1                                             #<---- SCREEN
        with d7                                                                        #<---- SCREEN
        her "Г-ха..."
        sly2 "Вычисти мой яйца, девка..."
        m "Отлично, парни! Давайте как закончим эту вечернку эпическим концом."
        her "{size=+7}Я кончаю!{/size}"
        m "Да, кончай, шлюшка."
        m "Давайте парни, обкончайте её, залейте её целиком, хорошо?"
        sly1 "Конечно, сэр."
        sly2 "Да, сэр!"
        m "Да, покройте её лицо спермой!"
        $ end_u_2_pic =  "03_hp/17_ending/161.png" #<---- SCREEN
        show screen end_u_2                                             #<---- SCREEN
        with d5                                                                        #<---- SCREEN
        her "{size=+3}Нет! Я сейчас кончу... Стойте!{/size}"
        sly1 "Хех... Гермиона Грейнджер... Что за шлюха!"
        sly2 "Да! Просто грязная пизденка!"
        her "{size=+9}AAAAAХ!!!!!{/size}"
        her "{size=+3}Да! Я шлюха! Я шлюха!{/size}"
        sly1 "Наконец-то признала это!"
        sly2 "Я думал, что она дольше продержится!"
        sly1 "Я тоже!"
        sly2 "АРГХ!"
        
        show screen white 
        pause.1
        hide screen white
        pause.2
        show screen white 
        pause .1
        hide screen white
        $ end_u_1_pic =  "03_hp/17_ending/162.png" #<---- SCREEN
        show screen end_u_1                                             #<---- SCREEN
        with hpunch
        
        show screen ctc
        pause
        hide screen ctc

        
        her "{size=+8}AAAAAAAAAAAAХ!{/size}"
        her "{size=+3}Моё лицо!!{/size}"
        sly1 "Принимай угощенье, шлюха!"
        
        show screen white 
        pause.1
        hide screen white
        pause.2
        show screen white 
        pause .1
        hide screen white
        $ end_u_1_pic =  "03_hp/17_ending/163.png" #<---- SCREEN
        show screen end_u_1                                             #<---- SCREEN
        with hpunch
        
        show screen ctc
        pause
        hide screen ctc
        
        her "{size=+5}AAAAAAAAAAAAХ!{/size}"
        sly2 "АРГХ! УЖЕ! Моё тоже!"
        
        
        show screen white 
        pause.1
        hide screen white
        pause.2
        show screen white 
        pause .1
        hide screen white
        $ end_u_1_pic =  "03_hp/17_ending/164.png" #<---- SCREEN
        show screen end_u_1                                             #<---- SCREEN
        with hpunch
        
        show screen ctc
        pause
        hide screen ctc
        
        $ end_u_2_pic =  "03_hp/17_ending/165.png" #<---- SCREEN
        show screen end_u_2                                             #<---- SCREEN
        with d7                                                                        #<---- SCREEN
        
        show screen ctc
        pause
        hide screen ctc
        
        her "{size=+4}Я кончаю!{/size}"
        m "Ну что ж, не возражаешь, если я тоже?!"
        $ end_u_1_pic =  "03_hp/17_ending/166.png" #<---- SCREEN
        show screen end_u_1                                             #<---- SCREEN
        with d5                                                                        #<---- SCREEN
        her "{size=+3}Нет профессор, я............!{/size}"
        g4 "Аргх!"
        
        show screen white 
        pause.1
        hide screen white
        pause.2
        show screen white 
        pause .1
        hide screen white
        $ end_u_1_pic =  "03_hp/17_ending/167.png" #<---- SCREEN
        show screen end_u_1                                             #<---- SCREEN
        with hpunch
        
        show screen ctc
        pause
        hide screen ctc
        
        
        her "{size=+8}AAAAAAAAAAAAХ!{/size}"
        $ end_u_2_pic =  "03_hp/17_ending/168.png" #<---- SCREEN
        show screen end_u_2                                             #<---- SCREEN
        with d5                                                                        #<---- SCREEN
        her "{size=+5}Нет! Моё лицо! Моя киска! Ах! Я не могу перестать кончать!!!{/size}"
        sly1 "Что за прошмандовка!"
        sly2 "Шлюха!"
        sly1 "Грязнокровка!"
        her "{size=+8}AAAAAAAAAAAAХ!{/size}"
        
        $ renpy.play('sounds/spit.mp3') #Sound of spiting. 
        show screen white
        pause.3
        $ end_u_1_pic =  "03_hp/17_ending/169.png" #<---- SCREEN
        show screen end_u_1                                            #<---- SCREEN
        #with d3                                                                        #<---- SCREEN
        hide screen white
        with vpunch
        show screen ctc
        pause
        hide screen ctc
        $ end_u_2_pic =  "03_hp/17_ending/170.png" #<---- SCREEN
        show screen end_u_2                                             #<---- SCREEN
        with d5                                                                        #<---- SCREEN
        her "{size=+8}*Глоть!*{/size}"
        $ end_u_1_pic =  "03_hp/17_ending/168.png" #<---- SCREEN
        show screen end_u_1                                            #<---- SCREEN
        #with d3                                                                        #<---- SCREEN
        her "{size=+8}Я схожу с ума!{/size}"
        
        # SPIT!
        
        show screen ctc
        pause
        hide screen ctc
        
        show screen white
        with d9
        pause 1
        
        
        # WHITE FADE
        
        ">.............{w}......................{w}....................."
        
        # Character sprites.
        
        m "Что ж, спаисбо за ваше участие, парни."
        sly1 "Конечно, сэр, проффесор Дамблодор."
        sly2 "Рады были помоч, сэр."
        sly1 "Спасибо вам, профессор."
        sly2 "Ну что, вернемся на бал?"
        sly1 "Да, пошли!"
        sly2 "Пока, грязнокровная шлюшка!"
        sly1 "Да, спасибо за классный отсос, сучка!"
        show screen h_head2                                                             # HERMIONE
        $ h_body = "03_hp/13_hermione_main/body_176.png" # HERMIONE
        her ".........................."
        hide screen h_head2
        $ renpy.play('sounds/footsteps.mp3') #Walking away sound
        # Walking away sound...."
        
        $ end_u_1_pic =  "03_hp/17_ending/02.png" #<---- SCREEN
        
        pause 2
        
        hide screen white
        with d9
        
        sly1 "{size=-4}(Чувак, профессор Дамблодр реально крутой дедок.){/size}"
        sly2 "{size=-4}(Да... Кто бы мог подумать.){/size}"
        sly1 "{size=-4}(Ага. Я не могу не уважать его...){/size}"
        m "Ау... Какие хорошие парни..."
        sly2 "{size=-4}(Да... Я надеюсь что буду таким же как он, когда состарюсь.){/size}"
        g4 "Я не старик, это вы молодные олухи!"
        m "Я хотя, в каком-то смысле я все же стар..."
        
        show screen h_head2                                                             # HERMIONE
        $ h_body = "03_hp/13_hermione_main/body_176.png" # HERMIONE
        her ".........................."
        hide screen h_head2
        m "Эй, шлюха! Чего притихла?"
        show screen h_head2                                                             # HERMIONE
        $ h_body = "03_hp/13_hermione_main/body_177.png" # HERMIONE
        her "Я..."
        her "Я... не уверена..."
        show screen h_head2                                                             # HERMIONE
        $ h_body = "03_hp/13_hermione_main/body_176.png" # HERMIONE
        her "Что...? Что это......."
        hide screen h_head2
        m "Давай, девченка, возьми себя в руки!"
        show screen h_head2                                                             # HERMIONE
        $ h_body = "03_hp/13_hermione_main/body_178.png" # HERMIONE
        her "Я... Я... Что?"
        her "Я не понимаю... Я..."
        hide screen h_head2
        m "Хм..."
#        m "Doesn't look like you are in any condition for serious talks..."
#        show screen h_head2                                                             # HERMIONE
#        $ h_body = "03_hp/13_hermione_main/body_178.png" # HERMIONE
#        her "Serious talks?"
#        hide screen h_head2
#        m "Well, so be it, then."
#        m "I wrote you a letter."
#        show screen h_head2                                                             # HERMIONE
#        $ h_body = "03_hp/13_hermione_main/body_177.png" # HERMIONE
#        her "A letter...? What...? I...."
#        hide screen h_head2
#        m "Yes! Concentrate for a second, would you?"
#        m "I wrote you a letter. It should explain a couple of things."
        m "Я уже должен уходить."
        show screen h_head2                                                             # HERMIONE
        $ h_body = "03_hp/13_hermione_main/body_176.png" # HERMIONE
        her "Уходить...?"
        hide screen h_head2
        m "Да. Возможно ты тоже..."
        m "Иди приведи себя в порядок и отдохни."
        show screen h_head2                                                             # HERMIONE
        $ h_body = "03_hp/13_hermione_main/body_178.png" # HERMIONE
        her "Но я не могу уйти... Нет... Я должна..."
        her "Танцевать... Должна..."
        hide screen h_head2
        m "Танцевать? Ты не можешь танцевать в таком состоянии."
        show screen h_head2                                                             # HERMIONE
        $ h_body = "03_hp/13_hermione_main/body_176.png" # HERMIONE
        her "Нет! Я королева бала! Я должна...."
        hide screen h_head2
        m "О.К., как хочешь."
        m "Я ухожу..."
        show screen h_head2                                                             # HERMIONE
        $ h_body = "03_hp/13_hermione_main/body_176.png" # HERMIONE
        her "Досвиданья... сэр..."
        hide screen h_head2
        m "............."
        m "Прощай, девочка."
        
        show screen ctc
        pause
        hide screen ctc
        
        show screen blkfade 
        $ end_u_2_pic =  "03_hp/17_ending/90.png" #<---- SCREEN
        show screen end_u_2                                             #<---- SCREEN
        with d9                                                                        #<---- SCREEN
        pause.5
        hide screen blkfade
        with d5
        
        show screen ctc
        play music "music/07 Introducing Colin2.mp3" fadein 1 fadeout 1 # BALL THEME 02.
        pause
        hide screen ctc
        
        m "Хм..."
        m "Может мне остаться и посмотреть, как она будет танцевать после мультиоргазма?"
        m "Нет... Бал почти закончился. Это мой последний шанс свалить отсюда."
        
        show screen ctc
        pause
        hide screen ctc
        
        show screen blkfade 
        with d7
        pause.5

        
        
        
        
         
         
         
         
         
         
         
         
         
         
         
        
        
        
        
        
        
        
        
        
        
        
        
        
             
             
             
             
             
        
        
        
        
        
        
        
        
        
        
        

        
        
        
        
        
        
        
        
        

    else: # Ending "Your whore".
        $ s_head_xpos = 330 # x = 330,
        $ s_head_ypos = 340 #Right bottom corner: y = 340. y = 380 - no hand.
        $ s_sprite = "03_hp/10_snape_main/snape_03.png"
        show screen s_head2
        sna "Мисс Грейнджер...?"
        $ s_sprite = "03_hp/10_snape_main/snape_04.png"
        sna2 "Вы решили все таки показаться. Неприятный сюрприз..."
        show screen h_head2                                                             # HERMIONE
        $ h_body = "03_hp/13_hermione_main/body_169.png" # HERMIONE
        her "..............................."
        $ s_sprite = "03_hp/10_snape_main/snape_13.png"
        show screen s_head2
        sna "Что случилось с вашим лицом, девченка?"
        show screen h_head2                                                             # HERMIONE
        $ h_body = "03_hp/13_hermione_main/body_170.png" # HERMIONE
        her "......................................."
        $ s_sprite = "03_hp/10_snape_main/snape_13.png"
        show screen s_head2
        sna "Хм... Ну, выходите вперед..."
        sna "Вот ваша корона..."
        sna "И ваш пьедестал..."
        hide screen s_head2
        pause.7
        
        
        
        $ end_u_2_pic =  "03_hp/17_ending/37.png" #<---- SCREEN
        hide screen blkfade
        with d7
        
        $ renpy.play('sounds/applause01.ogg')
        show screen ctc
        pause
        hide screen ctc
        
        her "..............."
        her ".................................."
        her ".........................................................................."
        play music "music/11 Neville's Waltz.mp3" fadein 1 fadeout 1 # BALL THEME.
        $ end_u_1_pic =  "03_hp/17_ending/38.png" #<---- SCREEN
        show screen end_u_1                                            #<---- SCREEN
        with d3                                                                        #<---- SCREEN
        her "Ах-a.........................................."
        show screen bld1
        with d5
        m "Это...?"
        m "остатки моей спермы у её рта?"
        g4 "Какого черта она тварит?"
        hide screen bld1
        with d5
        
        $ end_u_2_pic =  "03_hp/17_ending/39.png" #<---- SCREEN
        show screen end_u_2                                            #<---- SCREEN
        with d3                                                                        #<---- SCREEN
        her "...................................."
        her "Здравствуйте все..." #Misspelled on purpose.
        $ end_u_1_pic =  "03_hp/17_ending/40.png" #<---- SCREEN
        show screen end_u_1                                            #<---- SCREEN
        with d3                                                                        #<---- SCREEN
        her "Спа*ибо, что соб*сь се*дня *десь..." #Misspelled on purpose.
        show screen bld1
        with d5
        m "Я едва могу разобрать, что она там бормочет..."
        hide screen bld1
        with d5
        her "Фпервых, я хотелабы поблаборить Ппофессора Даблбора..." #Misspelled on purpose.
        show screen bld1
        with d3
        m "Меня?"
        hide screen bld1
        with d3
        her "................"
        $ end_u_2_pic =  "03_hp/17_ending/37.png" #<---- SCREEN
        show screen end_u_2                                            #<---- SCREEN
        with d3                                                                        #<---- SCREEN
        stop music fadeout 1.0
        her ".................................................."
        show screen ctc
        pause
        hide screen ctc
        $ end_u_1_pic =  "03_hp/17_ending/41.png" #<---- SCREEN
        show screen end_u_1                                            #<---- SCREEN
        with d3                                                                        #<---- SCREEN
        $ renpy.play('sounds/Глоть.mp3') #Sound of Глотьing down a liqui
        her "{size=+5}*Глоть!!!*{/size}"
        $ end_u_2_pic =  "03_hp/17_ending/42.png" #<---- SCREEN
        show screen end_u_2                                            #<---- SCREEN
        with d3                                                                        #<---- SCREEN
        her "Гу-ха..."
        her "Спасибо вам, профессор."
        show screen bld1
        with d3
        with hpunch
        g4 "ТЫ ШЛЮХА!!!"
        g4 "Это просто отвратительно!"
        #m "Now I want to fuck you... Dammit."
        hide screen bld1
        with d3
        play music "music/11 Neville's Waltz.mp3" fadein 1 fadeout 1 # BALL THEME.
        $ end_u_1_pic =  "03_hp/17_ending/43.png" #<---- SCREEN
        show screen end_u_1                                            #<---- SCREEN
        with d3                                                                        #<---- SCREEN
        her "Я хотела бы так же поблагодарить своих родителей..."
        her "А так же моих одногруппников!"
        show screen bld1
        with d3
        $ renpy.play('sounds/applause01.ogg') # APPLAUSE
        ">Громкие крики и свист..."
        hide screen bld1
        with d3
        her "И конечно же учитилей..."
        $ end_u_2_pic =  "03_hp/17_ending/44.png" #<---- SCREEN
        show screen end_u_2                                            #<---- SCREEN
        with d3                                                                        #<---- SCREEN
        show screen bld1
        with d3
        ">Несколько слабых хлопков..."
        hide screen bld1
        with d3
        
        show screen ctc
        pause
        hide screen ctc
        show screen blktone
        with d5
        
        mal "(И так, в этом году снова Гермиона Грейнджер...)"
        fem "(Пф... И почему я не удивлена?)"
        mal2 "(Может потому, что она этого заслуживает?)"
        mal "(Да! Хватит гнать на Гермиону!)"
        fem "(Пф...Еще бы.)"
        mal "(Кстати, что это там у Гермионы...)"
        mal2 "(Точно, что-то во рту. Я тоже заметил.)"
        fem "(Я уверена, что это чья-то сперма!)"
        mal "(ЧТО!!?)"
        mal2 "(Что за отвратительные мысли!)"
        fem "(Почему нет?)"
        fem "(Ведь каждый знает, что она трахается с Профессором Дамблодором!)"
        mal "(Опять ты распускаешь грязные сплетни.)"
        mal2 "(Подожди, я хочу послушать об этом. Расскажи поподробнее.)"
        fem "(Что именно тебе рассказать?)"
        fem "(Гермиона Грейнджер шлюха и она любит сосать члены....)"
        fem "(Да, она очень любит сосать члены, но сперму она любит еще больше!)"
        mal "(....)"
        fem "(Она просто помешана на сперме! Она наверно выпивает по стакану спермы в день...)"
        fem "(Потому что если не делает этого, то становится сексуально-одержимой...)"
        mal2 "(.....)"
        fem "(И когда это происходит, она не может себя контролировать, и трахается с первым встречным мужиком.)"
        mal "(.............)"
        mal2 "(.....................)"
        fem "(Хм? Почему вы так смотрите на меня?)"
        mal "(Что? Нет, ничего такого.)"
        mal2 "(Да, продолжай рассказывать. У тебя неплохо получается!)"
        fem "(Хорошо получается?!)"
        fem "(Секундочку, вы, ребята, что вы имеете ввиду?)"
        mal "(Хех... Посмотри на ворона, вызывающего Черного Ворона!)"
        fem "(Что это значит?)"
        mal2 "(Ты сильно покраснела! И глаза словно затуманило!)"
        mal "(Да! Ты получаешь удовольствия от рассказа!)"
        fem "(!!!?)"
        fem "Вы идиоты!"
        $ renpy.play('sounds/run_03.mp3')    #<--------------------Sound of running off.
        pause 3
        mal "(Что? Что я такого сказал?)"
        mal2 "(Кто знает, чувак? Сучки иногда ведут себя как сумасшедшие...)"
        mal "(Они и есть сумасшедшие...)"


        
        hide screen blktone
        with d5
        $ end_u_1_pic =  "03_hp/17_ending/43.png" #<---- SCREEN
        show screen end_u_1                                            #<---- SCREEN
        with d3                                                                        #<---- SCREEN
        her "Спасибо большое всем вам, за помощь в организации этого мероприятия."
        her "И спасибо вам большое за то, что в этом году снова выбрали меня королевой бала..."
        $ end_u_1_pic =  "03_hp/17_ending/45.png" #<---- SCREEN
        show screen end_u_1                                            #<---- SCREEN
        with d3                                                                        #<---- SCREEN
        her "Это очень приятный и неожиданный сюрприз...!"
        her "И еще кое что..."
        $ end_u_2_pic =  "03_hp/17_ending/43.png" #<---- SCREEN
        show screen end_u_2                                            #<---- SCREEN
        with d3                                                                        #<---- SCREEN
        her "{size=+5}Go gryffindor!{/size}"
        show screen bld1
        with d5
        $ renpy.play('sounds/applause01.ogg') # APPLAUSE
        ">Толпа взрывается громки апплодисментами и свистом..."
        hide screen bld1
        with d5
        show screen ctc
        pause
        hide screen ctc
        show screen blkfade
        with d7
        pause.7
        stop music fadeout 1.0
        m "Отличная речь..."
        m "Очень возбуждающая...Кхс, я имел ввиду вдохновляющая."
        $ tiara = True #Tiara is displayed.
        show screen h_head2                                                             # HERMIONE
        $ h_body = "03_hp/13_hermione_main/body_165.png" # HERMIONE
        her "Спасибо, сэр."
        hide screen h_head2   
        m "Проглотила все что было перед всей школой?"
        g9 "Очень мило вышло."
        show screen h_head2                                                             # HERMIONE
        $ h_body = "03_hp/13_hermione_main/body_168.png" # HERMIONE
        her "........................................................"
        hide screen h_head2                     
        
        play music "music/(Orchestral) Playful Tension by Shadow16nh.mp3" fadein 1 fadeout 1 # SEX THEME.
        
        $ end_u_2_pic =  "03_hp/17_ending/02.png" #<---- SCREEN
        show screen end_u_2                                            #<---- SCREEN
        with d3                                                                        #<---- SCREEN
        hide screen blkfade 
        with d3
        show screen bld1 
        with d3
        m "Хорошо, девочка, давай поговорим теперь..." 
        show screen h_head2                                                             # HERMIONE
        $ h_body = "03_hp/13_hermione_main/body_162.png" # HERMIONE
        her "...................."
        hide screen h_head2
        m "Есть кое что, что я должен сказать тебе..."
        m "Не знаю с чего начать..."
        m "........................................"
        m "Ну, прежде всего я--"
        show screen h_head2                                                             # HERMIONE
        $ h_body = "03_hp/13_hermione_main/body_163.png" # HERMIONE
        her2 "Сэр, думаю я знаю, что вы имеете ввиду."
        hide screen h_head2
        m "Ты знаешь?"
        show screen h_head2                                                             # HERMIONE
        $ h_body = "03_hp/13_hermione_main/body_163.png" # HERMIONE
        her "Конечно."
        show screen h_head2                                                             # HERMIONE
        $ h_body = "03_hp/13_hermione_main/body_164.png" # HERMIONE
        her2 "Одного быстрого минет не достаточно, что бы отплатить вам за все, я права?"
        hide screen h_head2
        m "Что? Нет, я совсем не об этом--"
        hide screen h_head2
        show screen h_head2                                                             # HERMIONE
        $ h_body = "03_hp/13_hermione_main/body_164.png" # HERMIONE
        her "Все в порядке, сэр. Правда."
        show screen h_head2                                                             # HERMIONE
        $ h_body = "03_hp/13_hermione_main/body_165.png" # HERMIONE
        her "Просто позвольте мне немного спустить трусики..."
        hide screen h_head2
        g4 "Черт, девченка! Дай мне закончить!?"
        show screen h_head2                                                             # HERMIONE
        $ h_body = "03_hp/13_hermione_main/body_164.png" # HERMIONE
        her "Конечно, сэр..."
        hide screen h_head2
        m "Ась?"
        show screen h_head2                                                             # HERMIONE
        $ h_body = "03_hp/13_hermione_main/body_167.png" # HERMIONE
        her "Просто постарайтесь не запачкать мне платье, хорошо?"
        hide screen h_head2
        g4 "*Рычание!*"
        g4 "Иди сюда, шлюха!"
        g4 "Предположим, что я трахаю тебя последний раз!"
        show screen h_head2                                                             # HERMIONE
        $ h_body = "03_hp/13_hermione_main/body_162.png" # HERMIONE
        her "(Последний раз?)"
        hide screen h_head2
        show screen ctc
        pause
        hide screen ctc
        show screen blkfade 
        with d7
        
        # INSERTION
        
        $ renpy.play('sounds/gltch.mp3')
        with hpunch
        with kissiris
        
        $ her_head_xpos=390 #Defines position of the Hermione's full length sprite. (Default 370). 140 - center. Bottom right: 390
        $ her_head_ypos=340 #Defines position of the Hermione's full length sprite. (Default 0). Right bottom corner: 340 - head only. 235 - tits.
        show screen h_head2                                                             # HERMIONE
        $ h_body = "03_hp/13_hermione_main/body_172.png" # HERMIONE
        her2 "{size=+5}Ахх!!!{/size}"
        hide screen h_head2            
        g4 "О, да!"
        
        $ end_u_2_pic =  "03_hp/17_ending/46.png" #<---- SCREEN
        show screen end_u_2                                            #<---- SCREEN
        with d3                                                                        #<---- SCREEN
        hide screen blkfade 
        hide screen bld1
        with d7
        show screen ctc
        pause
        hide screen ctc
        her "Ах-ах..."
        m "Хм? твоя киска..."
        m "Она вся мокрая."
        $ end_u_1_pic =  "03_hp/17_ending/47.png" #<---- SCREEN
        show screen end_u_1                                            #<---- SCREEN
        with d5                                                                        #<---- SCREEN
        her "Ах...{image=textheart.png} Правда, сэр?"
        her "Это случилось чуть раньше..."
        m "Чуть раньше?"
        m "Имеешь ввиду, когда ты задыхалась от моего члена в своей глотке?"
        her "Ah...{image=textheart.png} Yes, sir..."
        m "Это может заставить тебя кончить?"
        $ end_u_2_pic =  "03_hp/17_ending/48.png" #<---- SCREEN
        show screen end_u_2                                            #<---- SCREEN
        with d5                                                                        #<---- SCREEN
        her "Немного..."
        m "Ну что ж, это похоже понравилось тебе, не так ли?"
        her "ах......"
        m "Не так ли, шлюха?!"
        her "Ах... Так и есть, сэр."
        m "Да, понравилось, ты, сучка!"
        $ end_u_1_pic =  "03_hp/17_ending/49.png" #<---- SCREEN
        show screen end_u_1                                            #<---- SCREEN
        with d5                                                                        #<---- SCREEN
        her "............."
        m "Сожми как следует мой член своей маленькой пизденкой!"
        her "......................"
        m "Хм...?"
        m "Почему это ты вдруг замолчала??"
        $ end_u_2_pic =  "03_hp/17_ending/51.png" #<---- SCREEN
        show screen end_u_2                                            #<---- SCREEN
        with d5                                                                        #<---- SCREEN
        her "Ох... Я босюь что кто-нибудь нас заметит--"
        m "Я думаю, ты просто хочешь чтоб тебя отшлепали!"
        her "Что!?"
        $ renpy.play('sounds/slap.mp3')
        show screen white 
        pause.1
        hide screen white
        with hpunch
        
        $ end_u_2_pic =  "03_hp/17_ending/52.png" #<---- SCREEN
        #show screen end_u_2                                            #<---- SCREEN
        #with d5                                                                        #<---- SCREEN
        her "Йееееес!"
        m "Заткнись, шлюха! Кто-нибудь услышит!"
        $ end_u_1_pic =  "03_hp/17_ending/53.png" #<---- SCREEN
        show screen end_u_1                                            #<---- SCREEN
        with d5                                                                        #<---- SCREEN
        her "Сэр, я--"
        
        $ renpy.play('sounds/slap.mp3')
        show screen white 
        pause.3
        hide screen white
        with hpunch
        $ end_u_1_pic =  "03_hp/17_ending/54.png" #<---- SCREEN
        #show screen end_u_1                                            #<---- SCREEN
        #with d5                                                                        #<---- SCREEN

        her "{size=+7}EEghh!!!{/size}"
        m "Тише, я сказал!"
        m "Или ты хочешь, что бы тебя поймали на члене вашего директора?"
        m "Хочешь, Мисс королева осеннего бала?"
        
        $ renpy.play('sounds/slap.mp3')
        show screen white 
        pause.3
        hide screen white
        with hpunch
        $ end_u_1_pic =  "03_hp/17_ending/55.png" #<---- SCREEN
        her "Ах..."
        m "Да, ты хочешь этого, не так ли?!"
        $ end_u_2_pic =  "03_hp/17_ending/56.png" #<---- SCREEN
        show screen end_u_2                                            #<---- SCREEN
        with d5                                                                        #<---- SCREEN
        her ".............."
        g4 "Отвечай мен, сучка!"
        $ renpy.play('sounds/slap.mp3')
        show screen white 
        pause.3
        hide screen white
        with hpunch
        $ end_u_2_pic =  "03_hp/17_ending/55.png" #<---- SCREEN
        her "Да,сэр! Я хочу этого!!!"
        $ end_u_1_pic =  "03_hp/17_ending/53.png" #<---- SCREEN
        show screen end_u_1                                            #<---- SCREEN
        with d5                                                                        #<---- SCREEN
        her "Шлепайте меня сильнее! Я это заслужила!"
        m "Это точно!"
        
        show screen ctc
        pause
        hide screen ctc
        
        $ renpy.play('sounds/slap.mp3')
        show screen white 
        pause.3
        hide screen white
        with hpunch
        $ end_u_1_pic =  "03_hp/17_ending/55.png" #<---- SCREEN
        
        show screen ctc
        pause
        hide screen ctc
        
        $ renpy.play('sounds/slap.mp3')
        show screen white 
        pause.3
        hide screen white
        with hpunch
        $ end_u_1_pic =  "03_hp/17_ending/55.png" #<---- SCREEN
        
        show screen ctc
        pause
        hide screen ctc
        
        $ renpy.play('sounds/slap.mp3')
        show screen white 
        pause.3
        hide screen white
        with hpunch
        $ end_u_1_pic =  "03_hp/17_ending/58.png" #<---- SCREEN
        
        show screen ctc
        pause
        hide screen ctc
        
        $ renpy.play('sounds/slap.mp3')
        show screen white 
        pause.3
        hide screen white
        with hpunch
        $ end_u_1_pic =  "03_hp/17_ending/58.png" #<---- SCREEN
        
        show screen ctc
        pause
        hide screen ctc
        
        $ renpy.play('sounds/slap.mp3')
        show screen white 
        pause.3
        hide screen white
        with hpunch
        $ end_u_1_pic =  "03_hp/17_ending/59.png" #<---- SCREEN
        
        
        show screen ctc
        pause
        hide screen ctc
        
        $ renpy.play('sounds/slap.mp3')
        show screen white 
        pause.3
        hide screen white
        with hpunch
        $ end_u_2_pic =  "03_hp/17_ending/59.png" #<---- SCREEN
        
        show screen ctc
        pause
        hide screen ctc
        
        her "{size=+7}Аааааах............................{/size}"


        show screen blktone
        with d3
        sna "Внимание, лечинки!"
        sna "Начинается вальст\"Осеннего Бала Хогвартса\"..."
        hide screen blktone 
        with d3
        
        $ end_u_2_pic =  "03_hp/17_ending/60.png" #<---- SCREEN
        show screen end_u_2                                          #<---- SCREEN
        with d5                                                                        #<---- SCREEN
        her "!!!"
        her "Танец! Я совсем забыла!!?"
        $ end_u_2_pic =  "03_hp/17_ending/61.png" #<---- SCREEN
        show screen end_u_2                                          #<---- SCREEN
        with d5                                                                        #<---- SCREEN
        her "Сэр, простите, но мне придется покинуть вас..."
        g4 "Ах... Твоя киска это нечто!"
        her "Сэр... Ах... Я серьезно."
        her "Все ожидают, что я, как королева, буду танцевать."
        g4 "Да... Это здорово, как никога... О, да."
        $ end_u_1_pic =  "03_hp/17_ending/62.png" #<---- SCREEN
        show screen end_u_1                                          #<---- SCREEN
        with d5                                                                        #<---- SCREEN
        her "Сэр, вы меня слушаете вообще?"
        m "О, все прекрасно слышу. И позволь мне кое что предложить."
        $ end_u_2_pic =  "03_hp/17_ending/61.png" #<---- SCREEN
        show screen end_u_2                                          #<---- SCREEN
        with d5                                                                        #<---- SCREEN
        her "Сэр?"
        m "Вместо того, что бы идти..."
        m "Я трахну тебя в задницу."
        m "Ась? Что-то не так?"
        her "Что? Н-но..."
        m "Я думаю, что это отличный план!"
        her "Сэр, нет! Я--"
        m "Секундочку, секундочку..."
        show screen blkfade
        with d7
        m "Позволь мне сначала вытащить член из твоей киски..."
        
        $ renpy.play('sounds/boing.mp3') #Sound of # POP!
        with hpunch
        pause.3
        show screen h_head2                                                             # HERMIONE
        $ h_body = "03_hp/13_hermione_main/body_172.png" # HERMIONE
        her "Ах..."
        show screen h_head2                                                             # HERMIONE
        $ h_body = "03_hp/13_hermione_main/body_167.png" # HERMIONE 
        her "Сэр, нет. Вы должны выслушать меня--"
        hide screen h_head2     
        $ renpy.play('sounds/gltch.mp3')
        with hpunch
        with kissiris
        
        # INSERTION
        show screen h_head2                                                             # HERMIONE
        $ h_body = "03_hp/13_hermione_main/body_173.png" # HERMIONE
        her "{size=+7}!!!!!!!!!!!!!!!!!{/size}"
        her "Моя...{w} Моя...{w} Моя..."
        hide screen h_head2     
        m "Заткнись, сучка! Слишком громко."
        with hpunch
        show screen h_head2                                                             # HERMIONE
        $ h_body = "03_hp/13_hermione_main/body_173.png" # HERMIONE
        her "{size=+7}МОЯ ЗАДНИЦА!!!!!!!!!!!!!{/size}"
        hide screen h_head2  
        g4 "Черт, девченка, я сказал тише."
        
        $ end_u_2_pic =  "03_hp/17_ending/63.png" #<---- SCREEN
        show screen end_u_2                                          #<---- SCREEN
        with d5                                                                        #<---- SCREEN
        
        hide screen blkfade 
        with d9
        her "{size=+7}Я не могу! Я не хочу! Так больно!!!{/size}"
        g4 "Может ты и не хочешь, зато я хочу, шлюшка!"
        $ end_u_1_pic =  "03_hp/17_ending/64.png" #<---- SCREEN
        show screen end_u_1                                          #<---- SCREEN
        with d5                                                                        #<---- SCREEN
        her "{size=+5}Ваш член просто огромен!{/size}"
        g4 "Нас поймают из-за тебя, тупаясучка!"
        m "Может быть это поможет тебе заткнуться..." 
        
        # Fishhooking.
        $ end_u_2_pic =  "03_hp/17_ending/65.png" #<---- SCREEN
        show screen end_u_2                                          #<---- SCREEN
        with d5                                                                        #<---- SCREEN
        her "!!!............"
        g4 "Все верно, шлюшка. Тише!"
        $ end_u_1_pic =  "03_hp/17_ending/66.png" #<---- SCREEN
        show screen end_u_1                                          #<---- SCREEN
        with d5                                                                        #<---- SCREEN
        her "Ах... Блах..."
        g4 "Твоя дырка... Чертовски узкая..."
        $ end_u_2_pic =  "03_hp/17_ending/67.png" #<---- SCREEN
        show screen end_u_2                                          #<---- SCREEN
        with d5                                                                        #<---- SCREEN
        her "Ах... блах... ah..."
        g4 "Твои слюни стекают по моей руке, грязная шлюшка!"
        her "Ах... Блах-блах... ах... бла-aх..."
        
        show screen blktone
        with d5
        stop music fadeout 1.0
        sna "Ну что ж, начнем..."
        sna "Сейчас вы получите пары..."
        sna "Нет! Парень -  девушка, вы два кретина. Где вы думаете, вы находитесь? В лаборатории?"

        hide screen blktone
        with d5
        $ end_u_1_pic =  "03_hp/17_ending/69.png" #<---- SCREEN
        show screen end_u_1                                            #<---- SCREEN
        with fade                                                                    #<---- SCREEN
        play music "music/07 Introducing Colin2.mp3" fadein 1 fadeout 1 # BALL THEME 02.
        m "Не волнуйся о том, что пропустишь танец, шлюха."
        m "Мы станцуем наш собственный танец..."
        her "Ах..."
        m "Да. В этом году королева исполняет сложное \"па\" с членом глубоко в попке!"
        $ end_u_2_pic =  "03_hp/17_ending/69.png" #<---- SCREEN
        show screen end_u_2                                            #<---- SCREEN
        with d5                                                                        #<---- SCREEN
        her "Ах... я ахх..."
        m "Вы что-то хотите сказать, ваше величество?"
        her "Ах... Я королева весеннего бала... ах..."
        m "Конечно же ты!"
        m "Но еще ты шлюха!"
        $ end_u_1_pic =  "03_hp/17_ending/68.png" #<---- SCREEN
        show screen end_u_1                                            #<---- SCREEN
        with d5                                                                        #<---- SCREEN
        her "Я шлюха..."
        $ end_u_2_pic =  "03_hp/17_ending/70.png" #<---- SCREEN
        show screen end_u_2                                           #<---- SCREEN
        with d5                                                                        #<---- SCREEN
        her "{size=+7}Я шлюха!!!{/size}"
        $ end_u_1_pic =  "03_hp/17_ending/71.png" #<---- SCREEN
        show screen end_u_1                                            #<---- SCREEN
        with d5                                                                        #<---- SCREEN
        her "{size=+10}Я шлюююююха!!!{/size}"
        g4 "Да! Ты маленькая, похотливая шлюшка!"
        $ renpy.play('sounds/slap.mp3')
        show screen white 
        pause.3
        hide screen white
        $ end_u_1_pic =  "03_hp/17_ending/72.png" #<---- SCREEN
        with hpunch
        her "{size=+5}Я шлюха!!!{/size}"
        g4 "Да, верно!"
        $ renpy.play('sounds/slap.mp3')
        show screen white 
        pause.3
        hide screen white
        with hpunch
        her "{size=+5}Я шлюха!!!{/size}"
        g4 "Да!"
        $ renpy.play('sounds/slap.mp3')
        show screen white 
        pause.3
        hide screen white
        with hpunch
        $ end_u_2_pic =  "03_hp/17_ending/73.png" #<---- SCREEN
        show screen end_u_2                                            #<---- SCREEN
        with d5                                                                        #<---- SCREEN
        her "{size=+5} Я кончаююю!!!{/size}"
        
        with hpunch
        g4 "Аргх! Мой член!"
        $ end_u_1_pic =  "03_hp/17_ending/74.png" #<---- SCREEN
        show screen end_u_1                                            #<---- SCREEN
        with d5                                                                        #<---- SCREEN
        her "{size=+10}Я КОНЧАААЮ! Я шлюха!{/size}"
        g4 "Я больше не могу его двигаться в тебе!"
        her "{size=+10}Я КОНЧАЮ!{/size}"
        

        
        g4 "Мой член застрял в твоей заднице, шлюха!"
        her "{size=+10}Я шлюююха!!!{/size}"
        g4 "Я говорю расслабься немного, сучка!"
        $ end_u_2_pic =  "03_hp/17_ending/73.png" #<---- SCREEN
        show screen end_u_2                                            #<---- SCREEN
        with d5                                                                        #<---- SCREEN
        her "{size=+7}Я не могу! Я кончаю!!!{/size}"
        g4 "Отлично! Продолжай! А потом я снова примусь за твою пизденку."
        $ end_u_1_pic =  "03_hp/17_ending/75.png" #<---- SCREEN
        show screen end_u_1                                            #<---- SCREEN
        with d5                                                                        #<---- SCREEN
        her "Ась?"
        # POP
        
        show screen blkfade
        with d7
        g4 "Не могу вытащить!"
        g4 "Расслабь чертову задницу, девченка!..."
        
        $ renpy.play('sounds/boing.mp3') #Sound of # POP!
        with hpunch
        pause.3
        show screen h_head2                                                             # HERMIONE
        $ h_body = "03_hp/13_hermione_main/body_175.png" # HERMIONE
        her "..........."
        hide screen h_head2                       
        m "Это..."
        
     
    #    $ renpy.play('sounds/gltch.mp3')
    #    with hpunch
    #    with kissiris
        
    #    # INSERTION
    #    show screen h_head2                                                             # HERMIONE
    #    $ h_body = "03_hp/13_hermione_main/body_175.png" # HERMIONE
    #    her "{size=+7}!!!!!!!!!!!!!!!!!{/size}"

        
        
        
        $ renpy.play('sounds/gltch.mp3')
        with hpunch
        with kissiris
        $ end_u_1_pic =  "03_hp/17_ending/77.png" #<---- SCREEN
        hide screen blkfade
        with d5
        # INSERTION
        her "{size=+10}ААААААААХ!!{/size}"
        her "Он снова в моей киске..."
        g4 "Верно, сучка!"
        $ end_u_2_pic =  "03_hp/17_ending/79.png" #<---- SCREEN
        show screen end_u_2                                            #<---- SCREEN
        with d5                                                                        #<---- SCREEN
        her "Но я все еще кончаю!"
        her "Что со мной происходит, сэр!?"

        m "Расслабься, я знаю что я делаю!"
        m "Это нормально для шлюшки."
        $ end_u_1_pic =  "03_hp/17_ending/78.png" #<---- SCREEN
        show screen end_u_1                                            #<---- SCREEN
        with d5                                                                        #<---- SCREEN
        her "{size=+5}Нет! Я сойду с ума!!!{/size}"
        g4 "Все в порядке. Просто ты в экстазе."
        g4 "Наслаждайся этим, пока я буду долбить твою киску!"
        her "{size=+5}Ах!!!{/size}"
        
        $ end_u_2_pic =  "03_hp/17_ending/81.png" #<---- SCREEN
        show screen end_u_2                                            #<---- SCREEN
        with d5                                                                        #<---- SCREEN
        her "{size=+5}Ох!!!{/size}"
        her "{size=+5}Я шлюха!!!{/size}"
        g4 "Верно!"
        her "{size=+5}Я тупая сучка!!!{/size}"
        g4 "Точно!"
        g4 "Ох... Я уже близко..."
        g4 "Аргх!"
        $ d_flag_01 = False #Came into pussy
        $ d_flag_02 = False #Came into asshole
        
        $ menu_x = 0.5 #Menu is moved to the left side.

                    
        menu:
            "-Кончить в киску Гермионы-":
                $ d_flag_01 = True #Came into pussy
                g4 "Как думаешь, твоя киска готова к этому, шлюшка!?"
                her "Сэр?!"
                g4 "Получай!"
                show screen white 
                pause.1
                hide screen white
                pause.2
                show screen white 
                pause .1
                hide screen white
                $ end_u_2_pic =  "03_hp/17_ending/86.png" #<---- SCREEN
                with hpunch
                her "{size=+5}Ах! ААааах!!{/size}"
                g4 "{size=+15}АРГХ!!!!!!!!!!!!!!!!{/size}"
                
               
                her "{size=+5}Ах! Я чувствую это! Так горячо внутри!{/size}"
                g4 "Аргх! Да!"
                $ end_u_1_pic =  "03_hp/17_ending/87.png" #<---- SCREEN
                show screen end_u_1                                         #<---- SCREEN
                with d5                                                                        #<---- SCREEN
                
                
                
                
                her "{size=+5}Оно внутри меня! Наполняет всю меня!!!{/size}"
                g4 "Да! Шлюха! Я накачал твою английскую пизденку своей спермой!"
                
              
                
                $ end_u_2_pic =  "03_hp/17_ending/88.png" #<---- SCREEN
                show screen end_u_2                                             #<---- SCREEN
                with d5                                                                        #<---- SCREEN
                her "Профессор! Мое платье!"
                g4 "Что?"
                her "Следите что бы не запачкать мое платье!"
                g4 "Заткнись про платье, шлюха! Ты портишь весь момент!"
                $ end_u_1_pic =  "03_hp/17_ending/87.png" #<---- SCREEN
                show screen end_u_1                                             #<---- SCREEN
                with d5                                                                        #<---- SCREEN
                her "{size=+5}Извините! Ваша шлюха просит прощенья!!!!{/size}"
                g4 "Да! Так-то лучше!"
                g4 "Ох......."
        
            "-Кончить в задницу Гермионы-":
                $ d_flag_02 = True #Came into asshole.
                g4 "Твоя задница должна быть уже готова к этом, шлюха!"
                her "Что?!"
                $ renpy.play('sounds/gltch.mp3')
                
                pause.5
                her "Ах..."
                
                #Pop
                
                #INSERTION
                $ renpy.play('sounds/boing.mp3') #Sound of # POP!
                with hpunch
                with kissiris
                $ end_u_1_pic =  "03_hp/17_ending/82.png" #<---- SCREEN
                show screen end_u_1                                          #<---- SCREEN
                with d5                                                                        #<---- SCREEN
                her "{size=+10}ААааааааах!!!{/size}"
                her "{size=+5}Снова в моей попке!{/size}"
                $ end_u_2_pic =  "03_hp/17_ending/81.png" #<---- SCREEN
                show screen end_u_2                                          #<---- SCREEN
                with d5                                                                        #<---- SCREEN
                her "{size=+5}Нет, сэр, пожалуйста! Не кончайте в мою попку!{/size}"
                her "{size=+5}Нет, Я же умру!!!{/size}"
                g4 "Ты не умрешь, грязная девченка."
                g4 "Ты будешь кончать как сумасшедшая какое-то время и только..."
                her "Нет, сэр, пожалуйста... Я боюсь..."
                g4 "Принимай подарочек, шлюшка!"
                show screen white 
                pause.1
                hide screen white
                pause.2
                show screen white 
                pause .1
                hide screen white
                with hpunch
                g4 "{size=+15}АРГХ!!!!!!!!!!!!!!!!{/size}"
                
                $ end_u_1_pic =  "03_hp/17_ending/82.png" #<---- SCREEN
                show screen end_u_1                                         #<---- SCREEN
                with d5                                                                        #<---- SCREEN
                her "{size=+5}Ах!Я чувствую это!!!{/size}"
                g4 "Аргх! Да!"
                $ end_u_2_pic =  "03_hp/17_ending/83.png" #<---- SCREEN
                show screen end_u_2                                             #<---- SCREEN
                with d5                                                                        #<---- SCREEN
                her "{size=+5}Оно внутри меня! Наполняет всю меня!!!{/size}"
                g4 "Да! ШЛЮХА! Я заполню тебя до краев спермой!"
                $ end_u_1_pic =  "03_hp/17_ending/84.png" #<---- SCREEN
                show screen end_u_1                                             #<---- SCREEN
                with d5                                                                        #<---- SCREEN
                her "Профессор! Платье!"
                g4 "Что?"
                her "Следите что бы не запачкать мое платье!"
                g4 "Заткнись про платье, шлюха! Ты портишь весь момент!!"
                $ end_u_2_pic =  "03_hp/17_ending/85.png" #<---- SCREEN
                show screen end_u_2                                             #<---- SCREEN
                with d5                                                                        #<---- SCREEN
                her "{size=+5}Извините! Ваша шлюха просит прощенья!!!!{/size}"
                g4 "Да! Так-то лучше!"
        
                
        $ her_head_xpos=390 #Defines position of the Hermione's full length sprite. (Default 370). 140 - center. Bottom right: 390
        $ her_head_ypos=235 #Defines position of the Hermione's full length sprite. (Default 0). Right bottom corner: 340 - head only. 235 - tits.
                
        show screen ctc
        pause
        hide screen ctc
        show screen blkfade
        with d9
        show screen h_head2                                                             # HERMIONE
        $ h_body = "03_hp/13_hermione_main/body_177.png" # HERMIONE
        stop music fadeout 1.0
        her "Ах..."
        her "Я...едва могу...стоять"
        hide screen h_head2     
        g4 "Я знаю, что это значит, девочка."
        g4 "Это был наш с тобой лучший трах!"
        show screen h_head2                                                             # HERMIONE
        $ h_body = "03_hp/13_hermione_main/body_177.png" # HERMIONE
        her "Да... Я никогда не забуду этого..."
        her "...сильнейшего оргазма..."
    #    her "But I must, go... The dance..."
    #    m "Go then..."
        show screen h_head2                                                             # HERMIONE
        $ h_body = "03_hp/13_hermione_main/body_176.png" # HERMIONE
        her "Сэр... Что вы хотели обсудить со мной..."
        hide screen h_head2     
        m "Да... Знаешь что? Я на самом деле написал тебе небольшое письмо по этому поводу..."
        show screen h_head2                                                             # HERMIONE
        $ h_body = "03_hp/13_hermione_main/body_178.png" # HERMIONE
        her "Письмо?"
        hide screen h_head2     
        m "Да... Оно должно прояснить некторые вещи..."
        show screen h_head2                                                             # HERMIONE
        $ h_body = "03_hp/13_hermione_main/body_177.png" # HERMIONE
        her "Оу... Хорошо..."
        hide screen h_head2     
        m "Только прочитай его завтра утром..."
        m "Или когда-нибудь..."
        m "Или не читай вообще, меня это не сообо волнует..."
        g4 "............."
        show screen h_head2                                                               # HERMIONE
        $ h_body = "03_hp/13_hermione_main/body_179.png" # HERMIONE
        her "Сэр...?"
        hide screen h_head2     
        m "Не делай такие глаза! Ты заставляешь чувствовать себя неловко..."
        m "Я написал тебе письмо, что-то не так?"
        show screen h_head2                                                               # HERMIONE
        $ h_body = "03_hp/13_hermione_main/body_179.png" # HERMIONE
        her "Я думаю...это очень мило............."
        hide screen h_head2 
        g4 "Иди девочка! Мне кажется ты опаздывала на какой-то танец!"
        show screen h_head2                                                               # HERMIONE
        $ h_body = "03_hp/13_hermione_main/body_180.png" # HERMIONE
        her "ТАНЦЕ!"
        her "Извините, я должна бежать!"
        her "Увидимся позже, сэр!"
        hide screen h_head2     
        
        $ renpy.play('sounds/run_03.mp3')    #<--------------------Sound of running off.
        pause 3
        m "......................"
        m "Не думаю......."
        m "Прощай... Гермиона..."
        pause.7
        ">..................................{w}.....................................{w}................................"
    
        play music "music/11 Neville's Waltz.mp3" fadein 1 fadeout 1 # BALL THEME.
        
        if d_flag_01: #Came into pussy
            show screen end_u_1                                             #<---- SCREEN
            $ end_u_1_pic =  "03_hp/17_ending/89.png" #<---- SCREEN
        else:
            show screen end_u_1                                             #<---- SCREEN
            $ end_u_1_pic =  "03_hp/17_ending/90.png" #<---- SCREEN
            
        ">Вы не надолго задержались, смотря ей вслед..."
        ">Наблюдая, как Гермиона танцует вальс..."
        hide screen blkfade
        with d7
        show screen ctc
        pause
        hide screen ctc
        ">Она устала и измотана, но очень хорошо это скрывает..."
        show screen bld1
        with d5
        m "(Хм... Эта девочка действительно сильная...)"
        m "(Во всём...)"
        hide screen bld1
        with d5
        if d_flag_01: #Came into pussy
            ">Вы заметили струйку прозрачной жидкости, стекающей по внутренней стороне ее бедра, никем не замеченной кроме вас..."
        elif d_flag_02: #Came into asshole.
            ">Так же вы заметили, что она сильно напрягает свои ягодицы."
            ">Видимо, делает все возможное, что бы сохранить те ощущения, которые вы подарили её задней дырочке..."
        show screen bld1
        with d5
        m "................................................."
        m "..............."
        m "(Я уже должен уходить...)"
        hide screen bld1
        with d5
        show screen ctc
        pause
        hide screen ctc
    
    
    #FINAL SCENE. GENIE IS LEAVING.
    
    
    
    show screen blkfade
    with d7
    pause 1
    stop music fadeout 1.0
    
    centered "{size=+7}{color=#cbcbcb}Окрестности Хогвартса{/color}{/size}"

    
    $ end_u_1_pic =  "03_hp/17_ending/171.png" #<---- SCREEN
    show screen end_u_1                                           #<---- SCREEN
    pause.3
    hide screen blkfade 
    with d7
    
    play music "sounds/night.mp3" fadein 1 fadeout 1 #NIGHT SOUNDS.
    
    show screen ctc
    pause
    hide screen ctc
    
    $ renpy.play('sounds/steps_grass.mp3') # SOUNDS OF STEPS IN THE GRESS.
    m "......."
    pause.5
    
    $ end_u_3_pic =  "03_hp/17_ending/172.png" #<---- SCREEN
    show screen end_u_3                                           #<---- SCREEN
    with d7                                                                       #<---- SCREEN
    
    
    
    m "Ну чтож, самое время, что бы уходить..."
    
    $ end_u_4_pic =  "03_hp/17_ending/173.png" #<---- SCREEN
    show screen end_u_4                                           #<---- SCREEN
    with d7                                                                       #<---- SCREEN
    pause.5
    
    
    m "Прощай, мир странной магии..."
    m "Прощай, моя шлю--......"
    m "Прощай, моя Гермиона..."
    m "............"
    m "......"
    
    $ renpy.play('sounds/magic4.ogg')
    with hpunch
    $ end_u_3_pic =  "03_hp/17_ending/174.png" #<---- SCREEN
    hide screen end_u_4                                           #<---- SCREEN
    show screen end_u_3                                           #<---- SCREEN
    with d7                                                                       #<---- SCREEN
    
    pause.2
    
    $ end_u_4_pic =  "03_hp/17_ending/175.png" #<---- SCREEN
    show screen end_u_4                                           #<---- SCREEN
    with d7                                                                       #<---- SCREEN
    
    pause.2
    
    hide screen end_u_3                                           #<---- SCREEN
    with d7                                                                       #<---- SCREEN
    
    pause.2
    
    hide screen end_u_4                                           #<---- SCREEN
    with d7                                                                       #<---- SCREEN
    

    show screen ctc
    pause
    hide screen ctc
    
    show screen blktone
    with d7
    
    show screen blktone8
    with d7
#    $ end_u_4_pic =  "title2.jpg" #<---- SCREEN
#    show screen end_u_3                                           #<---- SCREEN
#    with fade                                                                     #<---- SCREEN
    
    
#    show screen blkfade 
#    with d9
    pause .5
    
    
    ## FINAL CREDITS ###
    stop music fadeout 1.0
    if public_whore_ending: # PUBLIC WHORE ENDING
        centered "{size=+7}{color=#cbcbcb}Поздравляем с прохождением игры!{/color}{/size}\n\n\
              {size=+5}{color=#cbcbcb}Это концовка \"02\" из \"02\".{/color}{/size}"
    else: # YOUR PERSONAL WHORE
        centered "{size=+7}{color=#cbcbcb}Поздравляем с прохождением игры!{/color}{/size}\n\n\
              {size=+5}{color=#cbcbcb}Это концовка \"01\" из \"02\".{/color}{/size}"
        
    hide screen blktone8
    with d7
    
    play music "music/02 - Shanghai Honey.mp3" fadein 1 fadeout 1 # ORANGE RANGE THEME.
    
    
    #play music "music/Real Talk by Brix.MP3" fadein 1 fadeout 1 
    #play music "music/03_2_Voicemail Freestyle Mike Wiebe.mp3" fadein 3 fadeout 1  
    #scene image "08_ending/e05.png" with Dissolve(2)
    # show akaani with d5
    #$ dermo = "genie_attack"
    #$ dermo = "snape_attack_guard"
    $ dermo = "ch_sna defend"
    
    show screen credits_chibi
    centered "{cps=20}{size=+5}{color=#ea91b0}-Тренер Ведьмы-{/color}{/size}\n\n\
    {color=#e5e297}-\{Written and directed by\}-{/color}\n{size=+5}{color=#cbcbcb}AKABUR{/color}{/size}\n\n\
    {color=#e5e297}-\{Head programmer\}-{/color}\n {size=+5}{color=#cbcbcb}AKABUR{/color}{/size}\n\n\
    {color=#e5e297}-\{Artwork by\}-{/color}\n   {size=+5}{color=#cbcbcb}AKABUR{/color}{/size}\n\n\
    {color=#e5e297}-\{Additional Artwork\}-{/color}\n   {size=+5}{color=#cbcbcb}DAHR{/color}{/size}\n\n\
    {color=#e5e297}-\{Texts proofread and edited by\}-{/color}\n   {size=+5}{color=#cbcbcb}LYK.D9{/color}{/size}\n\n\
    {color=#e5e297}-\{Technical advisor\}-{/color}\n   {size=+5}{color=#cbcbcb}XALJIO{/color}{/size}\n\n\
    {color=#e5e297}-\{Game testers\}-{/color}\n   {size=+5}{color=#cbcbcb}XALJIO\nLYK.D9\nDAHR\nAKABUR{/color}{/size}\n\n{/cps}"
    

    
    
    nvl clear


    #$ dermo = "ch_hem run_f"
#    $ dermo = "jerking_off_03_ani"
#    show screen credits_chibi
   
  
    $ xder = 160
    $ yder = 160
    $ dermo = "jerking_off_03_ani"
    show screen uni_cr
    hide screen credits_chibi
   
    
    
    
    centered "{cps=40}{size=+5}{color=#e5e297}-\{Sound Effects\}-{/color}{/size}\n    {color=#cbcbcb}http://www.freesound.org/{/color}\n\n\
    \
    {size=+5}{color=#e5e297}Перевод для вас пилили \n\
        {a=http://pornolab.net/forum/profile.php?mode=viewprofile&u=14141420}Ave_Fletch{/a} \n\
        {a=http://pornolab.net/forum/profile.php?mode=viewprofile&u=15155170}Discordnk90{/a} \n\
        {a=http://pornolab.net/forum/profile.php?mode=viewprofile&u=8041771}maniac4a{/a} \n\
        {a=http://pornolab.net/forum/profile.php?mode=viewprofile&u=4472572}Rio-Violente{/a} \n\
        {a=http://pornolab.net/forum/profile.php?mode=viewprofile&u=16957111}MrFrost1991{/a} \n\
        {a=http://pornolab.net/forum/profile.php?mode=viewprofile&u=18304384}babaylolxz{/a} \n\
        {a=http://pornolab.net/forum/profile.php?mode=viewprofile&u=16733487}Nyarkohotep{/a} \n\
        Если кого-то забыли -- простите ;) \
    \n\n\
    {size=+5}{color=#e5e297}-\{Music provided by\}-{/color}{/size}\n    {color=#cbcbcb}http://incompetech.com/{/color}\n\n\
    \
    \
    \
    \
    {size=+5}{color=#e5e297}-\{MUSIC\}-{/color}{/size}\n\
    \
    \
    \
    {color=#e5e297}\"(Orchestral) Playful Tension\" {/color}{color=#cbcbcb}by Shadow16nh.{/color}\n\
    {color=#e5e297}\"Prologue\" {/color}{color=#cbcbcb}Harry Potter OST.{/color}\n\
    {color=#e5e297}\"Shanghai Honey\"{/color} {color=#cbcbcb}by orange range.{/color}\n\
    {color=#e5e297}\"Introducing Colin\"{/color} {color=#cbcbcb}Harry Potter OST.{/color}\n\
    {color=#e5e297}\"Neville's Waltz\" {/color}{color=#cbcbcb}Harry Potter OST.{/color}\n\
    {color=#e5e297}\"The Quidditch Match\" {/color}{color=#cbcbcb}Harry Potter OST.{/color}\n\
    {color=#e5e297}\"Anguish\" {/color}{color=#cbcbcb}by  Kevin MacLeod.{/color}\n\
    {color=#e5e297}\"Awkward Meeting\" {/color}{color=#cbcbcb}by  Kevin MacLeod.{/color}\n\
    {color=#e5e297}\"Brittle Rille\" {/color}{color=#cbcbcb}by  Kevin MacLeod.{/color}\n\
    {color=#e5e297}\"Chipper Doodle v2\" {/color}{color=#cbcbcb}by  Kevin MacLeod.{/color}\n\
    {color=#e5e297}\"Dark Fog\" {/color}{color=#cbcbcb}by  Kevin MacLeod.{/color}\n\
    {color=#e5e297}\"Despair\" {/color}{color=#cbcbcb}by erenik.{/color}\n\
    {color=#e5e297}\"Game Over Theme\" {/color}{color=#cbcbcb}Final Fantasy VII OST.{/color}\n\
    {color=#e5e297}\"Boss Theme\" {/color}{color=#cbcbcb}Final Fantasy VII OST.{/color}\n\
    {color=#e5e297}\"Hitman\" {/color}{color=#cbcbcb}by  Kevin MacLeod.{/color}\n\
    {color=#e5e297}\"Music for Manatees\" {/color}{color=#cbcbcb}by  Kevin MacLeod.{/color}\n\
    {color=#e5e297}\"Plaint\" {/color}{color=#cbcbcb}by  Kevin MacLeod.{/color}\n\
    {color=#e5e297}\"Under-the-Radar\" {/color}{color=#cbcbcb}by  PhobyAk.{/color}{/cps}"
 
    
    $ xder = 670
    $ yder = 410
    $ dermo = "ch_hem run_f"
    #$ dermo = "no_shirt_dance_ani"
    nvl clear

    centered "{cps=40}{size=+2}{color=#e5e297}-\{CREATOR OF THIS GAME WOULD ALSO LIKE TO PERSONALLY THANK\}-{/color}{/size}\n\n{color=#cbcbcb} \
    {size=+5}Dahr{/size}{/color}\n{color=#e5e297}for still working for me pretty much free of charge, for inspiring me to keep on going and simply for being a good friend and colleague. {/color}\n\n\
    {color=#cbcbcb}{size=+5}Xaljio{/size}{/color}\n{color=#e5e297} for not only being my personal \"Ren'Py\" consultant but also an extremely thorough game-tester.\n\n\
    {color=#cbcbcb}{size=+5}Lyk.D9 (a.k.a. Silentchill){/size}{/color}\n {color=#e5e297}for toiling tirelessly over my texts full of typos and broken grammar. {/color}\n\n\
    {color=#cbcbcb}{size=+5}Bookfisher{/size}{/color}\n{color=#e5e297}For everything.\n\n\
    {color=#cbcbcb}{size=+5}The fate (universe or higher power){/size}{/color}\n{color=#e5e297}For giving me an opportunity to release another game while retaining complete creative freedom.\n\n\n\
    \
    {color=#cbcbcb}{size=-1}A whole bunch of other people who helped me with development of this game in one way or another,\n but whom I forgot to mention.{/color}\n\
    {color=#cbcbcb}And of course to everyone else who supports\nme and my work.\n\n\n\
    \
    {/color}{/size}{/cps}"

    hide screen uni_cr
    
    nvl clear

    centered "{cps=70}{color=#cbcbcb}This is not a commercial video game. The entire project was independently founded solely through\nhttp://www.patreon.com/ and\nby \"Hentai United\" subscribers.{/color}\n\n\n\
    \
    {size=-1}{color=#e5e297}-People who supported development of this game with extraordinary amount of money-{/size}\n\
    {color=#cbcbcb}Lawrence Dash, Wirefull, Dorago, Benoit Yan Larose, Talisca{/color}\n\n\
    \
    {size=-1}{color=#e5e297}-\"INVESTOR\" pledges-{/size}\n\
    {color=#cbcbcb}Ace, Linus Furtenbach (Bluue), Eduardo Pereira Carneiro, Vicente Sampedro Burgos, Morning Dawnstar, Wolo, John Layon, stefan mitrano, Gavin Spears, sergio.{/color}\n\n\
    \
    \
    {size=-1}{color=#e5e297}-\"AGENT\" pledges-{/size}\n\
    {color=#cbcbcb}Cameron MacDowell, Zarsher, Guynonymous, Nerzha, Silvanus2004, Xipomus, Carpy Rex, Adler, Deitan-Baruch St-Amand, Martin Neal, wetrx, mark howard, \
Kenneth Aguilar, alt, David McClellan, Leo H Wilkin, Thorn, TheDudeAbides, Alexandre Rouleau, thomas taylor, Alexander, Redmoonx22, Valdee, Alexander Lykke Landkildehus, Lucas Ferrari, Dom, derek zhang,Charlatan, Preston C T, waylan, Forrest, Loopy, JohnnyBB, Phantom Void, Kyaa, Stephen Richardson, mark herzog, will newton, Sascha Klug, Joshua McDonald, Undying S, John Cawley III, KitsuneEyes, Slingthatcat, Kieran James, Homod saleh al-shammri, randomuser89, Paul Keating, Antonio B, Marko, Tobias, Akhil Chokshi, Smiling_Jack, Clif Morgan, Derek Heynsbergen, Jack Cartwright, Damien Zaid, callmemusashi Mozambiqued, Nemesis Valentine Vanyar, Stalker, Jason, 4nubis, Curtis, Michael Simon, AB, The Wanderer (Mark Hawker), paul, JEB, Voe, Aselobar, Elgrangato82, froste, YllegaL, Bisongun, Skye Tomlinson, Parad0x, Eric Chen, Destiny, Podchamawa Petrovitch, Will, lc, Sathyan Mathai, Lisandro Gil, bill tedd, Tommy Turner, Marcel Kral, Oric13, Ren Ashjiro, anthony donihee, Honey Withers, Christopher, TofuCats, Drake King, Bookfisher Herring, Dustpan, dusty parrott, Bjorn, Robert Jolly, wilson yang, Tudor G, Arzaz, Etienne Ngo, xazathothx, Robert L Schliff, RO, DavidB, Daedilus, david green, Matt, Ketil, ALEXANDER KOVALEV, Oa, John, PG, largo_leet, David, Artemsgvozdem, heyPert.{/color}{/size}\n\n{/cps}"\
         
         
    nvl clear
    centered "{cps=70}{size=-1}{color=#e5e297}-\"REBEL\" pledges-{/size}\n\
    {size=-4}{color=#cbcbcb}1234ghumm, A. R., AJ Ferolie, Catalyst Greenhorn, Abraham Benitio, Actafool812, Adam, Casax5, Adam, FearTheDee, Akasection, Alejandro Luna, Aleksandr, Alex Odoul, Alex P., Alexander Randolph, Maidaniuk Yurii, Alexander, Alexei, Alkosh, Allan Pineda, Altagar, Andreas Janning, Andrei Kuz, Andrey Nikolaev, Anton Belyankin, Anton Tropicflames, Antonio Jos Mucoz Gonzalez, Antonio Rivera, Artur Kevorkov, Baran, BearPerson, BeepBep, Benjamin Drew, Bernard Winters, Bob Mannaro, Boyko, Brad, Brandon Gauthier, Brandon Mirr, Brent, Brett Williams, Bruce Gates, Byakuya36, Cirrus, Calmea, Carez, Carnosaur, Chad Dunkerley, Charles Able, Chemmy, Chris, Christopher Coulter, Christopher Woo, Christopher, Conner Owen, Conrad Boucher, Cruise Russo, Cyanide Sam, DMetal, Dakota Rude, Damian Boggs, Daniel Beard, Daniel Nathans, Daniel Smith, Daniel Szczuka, Daniel Torres, Danno, Danny Johansson, Danny Nguyen, Darkflame256, David Lestina, David Ruskin, David, Dean, Devin Barr, Dirk Delva, Donaj88, Donoth Aveano, DoornailsAreJealous, Demodraken, Double A, Drity, Edward le coyte, Eldar Scum, Eric Hsu, Evan waleske, Fabian, Faux, Fetsch Sebastian, Finrock, Fix, Formless, FoxPrince623, Frank Pietsch, Fraziel, Frederic Chen, Garrett Smith, Geoff Levario, Georgika, Gregc, Greg Hartley, Gregory G, Gunderson, Harm Harm, Harry Tizard, Hooverspleen, Ian W, Innes French, Jacob Thompson, Jacob, Jake Smith, Janis Feldbergs, Janus, Jared Whisenand, Jarred Leverton, Jason Buisman, Jason Chong, Jeff Abrams, Jeff, Jeremiah, John F, John S, John doe, John, Jonathan Backer, Jonathan, Joseph Balbuena, Joseph Oliveira, Josh Stegmaier, Juan Gomez, Jurdia, Justin Golden, Karl Stevenson, Karolis, Kenneth Guevarra, Kenneth Jackson, Kenny Huang, Kimo Linder-Fattah, Kolkina, Kristian Lund Jensen, Kryssler, Kurrel, Kyle Sarty, Kyuubi43, LIndy, Levone W., Jonathan Liu, Lockkaliber, Lord G, Lord Rayek, Lothvarthian Malik, Lukas Vystup, Luke Arrowsmith, Magmanox, Majushi, Mario Mueller, Mark Walrusburg, Martino Livio Martinello, Mason Davis, Matt Sullivan, Matthew Young, Michael Klepper, Michael McPherson, Michael O'Hara, Michael, Mike M., Mike Orlando, MinoCrossing, Miran, Mitchell Goodwin, Monky of Space, Morten Brunebjerg Hansen, Myers, N Metso, Naintoxe, Nairolf, Nathan S, Neo Savoric, Niels T, NugLord, Number37, Nym Nemo, Oliver Pirie, Oscar Lan, PS, Passionately Odd Syntax, Patrick Fochler, Patrick, Paul Allen, Peter Grnlykke, Professor Snape, PuddingPowder, Pel-Tore, Rabe, Raglan Strom, Randolph Carter, Random, Reaver78, Rekoar, Reny Frederiksen, Richard Buettner, RickRub, Rightmind, Rob, Robert Doughty, Robert Simmons, Rodrigo Das Flores, Rune Daugaard Lundsteen, Runkle, Russell, SJ M, SYukito, Sane 300, Sayting, Sinedd, Scorch289, Sean Carstensen, Sebastian Tauch, Sehad, Shane Fitzsimons, Shawn Aiken, Skellman, Skull616, SlaveToTheSound, Smaug, Some Guy, Steffen Nissen, Stephen Krieger, Steve Jones, Steven Cunningham, Syr, TGriz, Talon Grant, Teemu, Thae, The Masked Masturbator, This Isntmahname, Thomas Frobish, Thomas Grimes, Thomas Vazquez, Timmothy Firewood, Tom Arne Vestby2, Tony Taylor, Tony Veliz, Truvor, Tuki, Tyler, Venron, Vervalsen, Vi9, Visp, Wanderer, Weenie Beenie, Wesley Gamble, XDrakeX, Xev, YummyTiger, Yuu Yi, Zach Rzepiela, Zakmonster, Zeath, Zenzard, Zim outside, Zoggy, alvin suryaputra, am1tg3, andrew gardiner, artisticMink, barry r king, bloodangel99, butts, caleb4532, charles turnbull, cvonsuela28, dingo egret, dingo1489, eXotic, fernando frias, gliph13, ippherita, izys, jabix, jassem dashti, john smith, josiah richter, karkazin, kyle mock, lia sven, lucas2684, n1ghtfox, nobody, potatohead, progste, randellspec, retchedegg, robster, silvarius2000, srt20022003, strider19, tehcalipwnt, terribleplan, thegreatbambe, timmy turner, varoksa, xenus, ziric.{/color}{/size}\n\n{/cps}"
    
    nvl clear
    centered "{cps=70}{size=-1}{color=#e5e297}-\"ACTIVIST\" pledges-{/size}\n\
    {size=-4}{color=#cbcbcb}Adam, Alvin, AmateurArtist98, Anders Sandahl, Naqqash Chaudhry, Andre, Andrew E., Bayushi, Ben Belcastro, Brandon Louie, Brandon Robinet, Brian Wilson, Carmen Williams, Chad Bennett, Dan George, Darklogic, Darknezzz, Dave Shevlin, David Crosby, David Sparkes, Douglas Jones, Draconic Paragon, DragonTamer, Ervin, Francis Dixson, Fredinator, Gene Boglin, George Craig, Greg, Guillaume Mroz, Gustaf Johansson, Hirin, Ian Lindop, IanDasein, Inge, Izzy Sabur, JBTClown, JP, Jack, Jacob Kain, Jan Hanenkamp, Jan M., Jan, Johannes Uwer, John Turner, Joshua Baadsgaard, KiSwordsman, Krux2022, L, Legio 20th, Marconi Ribeiro, Mike, Marius L, Mathias Frandsen, Matthew Marqueta, Max, Michael Webb, Miha Antauer, Mikhail V. Platonov, Mitch, Mountainj6, MrDurper, Sean Hill, Sam, Muirewedd, Neogeta, Nick Foronda, Nick, Noah Gerhards, Oren Barzilai, Pashike, Peeves, Phil Fairbanks, Philip G Honore, Riu Bas, Robert, Reinis Aleksejevs, Rougespartan181, Robert Lesundak, SO, SYH, Sacs, Sapherin, Sayyid, Sean, Shawn MacInnis, Simanith, Soda Zero, Speculations, Stephen Evans, Stonedrake, TRONboy, Tamenund Jones, Tintron, Victor Jd, Vincent McCool, Vitaliy Kasianenko, Vorcai0, Wolfcub, X.p., X39, Yan Luong, Zaker, chippy, joesco726, kurorol2, lambroll, ljennia, matthew lampell, moonwalkin, nh, raaq, six2make4, zack, Andry Sidorov.{/color}{/size}\n\n\
    \
    {size=-1}{color=#e5e297}-\"SUPPORTER\" pledges-{/size}\n\
    {size=-4}{color=#cbcbcb}AS84, Aaron Gregory, Gianfranco Calzoni, Aarvil Kemph, Aestus, Alex Martin, Andrea, Andreas, Andrew, Antilles, Antonboeg, Aran, Armando Soto, Azuliar, Batman, Balint Sule, Ben Rog-Wilhelm, Benjamin Cathey, Beth, Brad Hingston, Brandon Grant, Brendan, Brian Borden, Bru, Canyon, Capperroff, Chaintan, Christian Wong, Colton Clayton, Corey S., D, Damian Paradis, Daniel Chai, Daniel Geach, Daniel, Danny Mullay, Darpy, Dave doedry, David Leitner, Dax, Doctor Worm, Dragonman, Edd Holmes, Erebe, Eric Speaker, Fattycakes, FearTheDee, FeyOne, Filip Jaromin, Florian Eberle, FooldiverDX, Fortifel, Frank Bull, G V, Gaetano, Gary Tinsley, Gerald, Gerald, Gerhalt, Gregoire Fauconnier, Gregory, Happy Days, Hellomellowyellow, Hurf durf, Ian Sayer, Ilya, Ivan Nadasaki, J Solomon, Jack Simons, Jack Trebles, James Brown, James Do, Jan-Kristoffer Brekke, Jayro Zipzapili, Jesse Doerksen, Jim, John Jon'zz, John Smith, Jonas Högman, Jose Gonzalez, Joshua West, Julian Silva, KC maps, Kabuto, Kasper Nohr, Kenny Bailey, Kevin McKie, Kuroguma, Lanthanio, Louie Castro, MaiconMM, Majinken, Malcom Reynolds, Marc Voigt, Marcel Muller, Marius Thomassen, MarkAurel, Martin Ax, Matri, Matt, Matthew Lam, Max Robitzsch, MeХмonkeys, MercuryTwins, Messor Marra, Michael Troseth, Michael, Michael, Michael, Mike Bow, Mike Jones, Mike Moperz, Mikhail, N0body, NalfeinDoUrden, Nate A, Nicholas Alan McGuire, Nikuss, Nils Harder, Nitrat, Nordicberserk, Notsutos, Oberon, Onyxdime, Oxion1988, Ozzy, Paradosi, Pasi Huttunen, Patrick Gill, Paul Coad, patrick welsh, Paul, Pshenitsyn, PeeM, Peter Nikolas, Peter Ryskin, Pitt85, Preator, Pulimanne, Randall Lively, Richard Dumont, Richard Heying, Richard Soderberg, Riley Heffernan, Robert Bodo, Robert Davis, Rodrigo Rosado, Ronald, Roy Zimmermann, Ryan Bossard, Ryan Calhoun, Salvadore Broadfoot, Scott Barrie, Sebastien Elie, Sebastien Jalbert, SgtAfro, Shadefalcon, Stefano Sottocorna, SilverAxe, Sixxiie, Sky Valverde, Sodajuice, Steffen Sloth, TK, TP Samblanet, Taylor Patton, Taylor, Tenebrys Hentai Flash Games, Matthew Pruter, John Stanko, craig chadwick, TheOriginalJ, Thomas, Timeyy, Tony Li, TonyNinja, Tracy Scops, Travis Haapala, TrikJoker, Tyler Jones, Tyson, Urza Viderico, VC, Vasder, Vay Jay, Victor Sarosi, Warren P Nelson, Wayne Chattillon, William Farris, William Golding, Wlodzimierz Donatowicz, Xaljio, Xisis, brett, bronzeRanger, clerk4470, ghosti1, gillen, ismael torres, jaron uecker, levi tibbals, oakland, otakuguy01, rip_cpu, severin, sirpoffalot, teh_cabbage, tenko, trajor white, wilhelm, winsloven, Arkadii Terentiev, xxx, DAHR.{/color}{/size}\n\n\
    \
    {color=#e5e297}{size=-4}-\{Thank you, Joseph Antoni, for organizing all these 750+ names for me.\}-{/size}{/color}{/cps}"
              
              
              
              
              
              
    pause 1
    
    show screen ctc
    pause 
    hide screen ctc
    show screen blkfade
    with d9
    stop music fadeout 3.0
    ">................................{w}...........................{w}................................."
    pause.5
    centered "{size=+7}{color=#cbcbcb}Следующим утром...{/color}{/size}"
    
    hide screen end_u_1                                           #<---- SCREEN
    hide screen end_u_2                                           #<---- SCREEN
    hide screen end_u_3                                           #<---- SCREEN
    hide screen end_u_4                                           #<---- SCREEN
    hide screen blktone
    hide screen blktone8
    stop bg_sounds #Stops playing the fire SFX.
    stop weather #Stops playing the rain SFX.
    hide screen notes #A bunch of notes poping out with a "win" sound effect.
    hide screen phoenix_food
    hide screen done_reading
    hide screen done_reading_02
    hide screen candlefire_01 #CANDLE FIRE.
    hide screen candlefire_02 #CANDLE FIRE.
    hide screen lightening #Hide lighting so it woudn't get stuck during clear sky weather and such.
    hide screen cloud_night_01 #NIGHT CLOUDS.
    hide screen cloud_night_02 #NIGHT CLOUDS.
    hide screen cloud_night_03 #NIGHT CLOUDS.
    hide screen bld1 #You know what this is. Just making sure it doesn't get stuck.
     
    show screen new_window # CLEAR WEATHER.
    
    hide screen room_night #Hiding NIGHT BG from last night.
    show screen room #Showing main room BG. 

    hide screen door   
    hide screen cupboard
    hide screen chair
    hide screen fireplace
    hide screen phoenix
    hide screen candle_01    
    hide screen candle_02
    hide screen genie
    hide screen owl
    hide screen owl_02
    hide screen with_snape #Genie hangs out with Snape in front of the fireplace.
    hide screen with_snape_animated #Genie hangs out with Snape in front of the fireplace.

        
    show screen door   
    show screen cupboard
    show screen chair
    show screen fireplace
    show screen phoenix
    show screen candle_01    
    show screen candle_02
    show screen dumbledore

    hide screen blkfade
    with d9
    
    show screen ctc
    pause
    hide screen ctc
    
    show screen bld1
    with d3
    dum "................................"
    hide screen bld1
    with d3
    
    
    if public_whore_ending: # PUBLIC WHORE ENDING
        $ renpy.play('sounds/door.mp3') #Sound of a door opening.
        $ snapes_speed = 02.0 #The speed of moving the walking animation across the screen.
        $ walk_xpos=470 #Animation of walking chibi. (From)
        $ walk_xpos2=360 #Coordinates of it's movement. (To)
        show screen snape_walk_01 
        with d3
        pause 1.5
        show screen snape_02 #Snape stands still.
        pause.1
        show screen bld1
        with Dissolve(.3)
        
        play music "music/Dark Fog.mp3" fadein 1 fadeout 1 # SNAPE'S THEME
        dum "Доброе утро, Северус."
        $ s_head_xpos = 330 # x = 330,                                                                              # SNAPE
        $ s_head_ypos = 340 #Right bottom corner: y = 340. y = 380 - no hand.       # SNAPE
        $ s_sprite = "03_hp/10_snape_main/snape_09.png"                                         # SNAPE
        show screen s_head2                                                                                                 # SNAPE
        sna "......................................."
        hide screen s_head2              
        dum "Я хочу поделиться с тобой весьма необычной историей, старый друг."
        $ s_sprite = "03_hp/10_snape_main/snape_09.png"                                         # SNAPE
        show screen s_head2                                                                                                 # SNAPE
        sna "......................................"
        hide screen s_head2     
        dum "Но сначала..."
        $ s_sprite = "03_hp/10_snape_main/snape_09.png"                                         # SNAPE
        show screen s_head2                                                                                                 # SNAPE
        sna "........................................"
        hide screen s_head2     
        dum2 "Эм... Северус?"
        $ s_sprite = "03_hp/10_snape_main/snape_09.png"                                         # SNAPE
        show screen s_head2                                                                                                 # SNAPE
        sna "........................................."
        $ s_sprite = "03_hp/10_snape_main/snape_06.png"                                         # SNAPE
        show screen s_head2                                                                                                 # SNAPE
        sna "Кто контролирует?"
        hide screen s_head2     
        dum2 "Извини?"
        $ s_sprite = "03_hp/10_snape_main/snape_26.png"                                         # SNAPE
        show screen s_head2                                                                                                 # SNAPE
        sna "Кто контролирует?" # T_T
        hide screen s_head2     
        dum2 "...кто контролирует что?"
        $ s_sprite = "03_hp/10_snape_main/snape_26.png"                                         # SNAPE
        show screen s_head2                                                                                                 # SNAPE
        sna "А...?"
        hide screen s_head2     
        dum2 "А?"
        $ s_sprite = "03_hp/10_snape_main/snape_27.png"                                         # SNAPE
        show screen s_head2                                                                                                 # SNAPE
        sna "Ака....?"
        hide screen s_head2     
        dum2 "Это бессмысленно, Северус."
        $ s_sprite = "03_hp/10_snape_main/snape_29.png"                                         # SNAPE
        show screen s_head2                                                                                                 # SNAPE
        sna "Ах, чертовщина..................."
        hide screen s_head2     
        pause.5
        show screen ctc
        pause
        hide screen ctc
        stop music fadeout 1.0
        
        show screen blkfade
        with d7
        pause 2
        
        
        
        
        

        
        
    
    else: # PERSONAL WHORE ENDING 

        $ renpy.play('sounds/door.mp3') #Sound of a door opening.
        
        $ walk_xpos=610 #Animation of walking chibi. (From)
        $ walk_xpos2=400 #Coordinates of it's movement. (To)
        $ hermione_speed = 03.0 #The speed of moving the walking animation across the screen.
        show screen hermione_walk_01 
        pause 3
        $ hermione_chibi_xpos = 400 #Near the desk.
        show screen hermione_02 #Hermione stands still.
        pause.5
        show screen bld1
        with Dissolve(.3)
        
        $ h_xpos=370 #Defines position of the Hermione's full length sprite.
        $ h_ypos=0
        show screen hermione_02
        
        show screen ctc
        pause
        hide screen ctc
        play music "music/Chipper Doodle v2.mp3" fadein 1 fadeout 1 # HERMIONE'S THEME.
        $ tiara = False #Turns off displaying of the tiara in h_head2 screen.
        $ her_head_xpos=390 #Defines position of the Hermione's full length sprite. (Default 370). 140 - center. Bottom right: 390
        $ her_head_ypos=235 #Defines position of the Hermione's full length sprite. (Default 0). Right bottom corner: 340 - head only. 235 - tits.  
        show screen h_head2                                                                                                  # HERMIONE
        $ h_body = "03_hp/13_hermione_main/body_120.png"                                     # HERMIONE
        
        her "Сэр, если речь пойдет о том, что было вчера..."
        #her "You wanted to see me, sir?"
        hide screen h_head2       
        dum "Доброе утро, мисс Грейнджер."
        show screen h_head2                                                                                                  # HERMIONE
        $ h_body = "03_hp/13_hermione_main/body_79.png"                                     # HERMIONE
        her2 "На самом деле мне не настолько понравилось, вы знаете..."
        hide screen h_head2  
        dum "Мисс Грейнджер, я нашел это на своем столе..."
        dum "Это адресовано вам..."
        show screen h_head2                                                                                                  # HERMIONE
        $ h_body = "03_hp/13_hermione_main/body_15.png"                                     # HERMIONE
        her "Письмо, сэр?"
        show screen h_head2                                                                                                  # HERMIONE
        $ h_body = "03_hp/13_hermione_main/body_24.png"                                     # HERMIONE
        her "Ох, конечно! Это вы мне его написали."
        hide screen h_head2  
        dum "Это письмо не от меня, мисс Грейнджер."
        show screen h_head2                                                                                                  # HERMIONE
        $ h_body = "03_hp/13_hermione_main/body_17.png"                                     # HERMIONE
        her "Разве?"
        show screen h_head2                                                                                                  # HERMIONE
        $ h_body = "03_hp/13_hermione_main/body_24.png"                                     # HERMIONE
        her "Ох, понятно..."
        her2 "Вы не должны этого стесняться, сэр. Все в порядке."
        hide screen h_head2  
        dum "*эм*... вот."
        show screen h_head2                                                                                                  # HERMIONE
        $ h_body = "03_hp/13_hermione_main/body_06.png"                                     # HERMIONE
        her2 "Спасибо, сэр."
        show screen h_head2                                                                                                  # HERMIONE
        $ h_body = "03_hp/13_hermione_main/body_73.png"                                     # HERMIONE
        her "Посмотрим...."
        stop music fadeout 7.0
        hide screen h_head2  
        pause.1
        
        
        $ letter_text = "{size=-7}Кому: Гермионе Грейнджер\n\n{/size}{size=-4}Дорогая [word_01]. \nЯ не тот, кто вы думаете... Даже не человек, если честно. В течении нескольких месяцев я выдавал себя за профессор Дамблдора. Но теперь мне нужно вернуться в [word_02]. К тому времени, как ты получишь письмо, я буду уже далеко. Мы больше никогда не встретимся, но я буду лелеять воспоминания об этом времени в вашем мире.\n\nПрощай, моя маленькая[word_03]. {size=-3}\n\n-[word_04]-{/size}"

        label last_letter:
        show screen letter
        show screen ctc
        show screen bld1
        with Dissolve(.3)
        pause
        menu:
            "-Закончить чтение-":
                pass    
            "-Продолжить чтение-":
                jump last_letter
        hide screen letter
        hide screen ctc
        hide screen bld1
        with Dissolve(.3)
        
        
     
        show screen bld1
        with d3
        show screen h_head2                                                                                                  # HERMIONE
        $ h_body = "03_hp/13_hermione_main/body_197.png"                                     # HERMIONE
        her "............................................................................................................................................................."
        hide screen h_head2  
        dum "Я полагаю, отправитель это некий Джинн?"
        dum "Тот, кто выдавал себя за меня, все это время?"
        show screen h_head2                                                                                                  # HERMIONE
        $ h_body = "03_hp/13_hermione_main/body_197.png"                                     # HERMIONE
        her "............................................................................................................................................................."
        hide screen h_head2  
        dum "Ну, теперь я вернулся..."
        dum "И я положу конец вашему \"бизнесу по обмену очков\", конечно же."
        hide screen hermione_main                                                                                                                                                                                   #HERMIONE
        with d3                                                                                                                                                                                                                        #HERMIONE
        $ h_xpos=370 #Defines position of the Hermione's full length sprite. (Default 370). (Center: 140)                                                       #HERMIONE
        $ h_body = "03_hp/13_hermione_main/body_86.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
        show screen hermione_main                                                                                                                                                                                 #HERMIONE
        with d3                                                                                                                                                                                                                        #HERMIONE
        pause.1
        with hpunch
        play music "music/Chipper Doodle v2.mp3" fadein 1 fadeout 1 # HERMIONE'S THEME.
        her "{size=+7}Что?!!{/size}"
        hide screen hermione_main                                                                                                                                                                                   #HERMIONE
        with d3                                                                                                                                                                                                                        #HERMIONE
        $ h_body = "03_hp/13_hermione_main/body_66.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
        show screen hermione_main                                                                                                                                                                                 #HERMIONE
        with d3                                                                                                                                                                                                                        #HERMIONE
        her "Как я буду получать дополнительные очки?"
        dum "Есть другие пути, мисс Грейнджер."
        hide screen hermione_main                                                                                                                                                                                   #HERMIONE
        with d3                                                                                                                                                                                                                        #HERMIONE
        $ h_body = "03_hp/13_hermione_main/body_186.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
        show screen hermione_main                                                                                                                                                                                 #HERMIONE
        with d3                                                                                                                                                                                                                        #HERMIONE
        her "А...?"
        dum "Усердный труд."
        hide screen hermione_main                                                                                                                                                                                   #HERMIONE
        with d3                                                                                                                                                                                                                        #HERMIONE
        $ h_body = "03_hp/13_hermione_main/body_187.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
        show screen hermione_main                                                                                                                                                                                 #HERMIONE
        with d3                                                                                                                                                                                                                        #HERMIONE
        her "Это так тупо!"
        dum2 "Мисс Грейнджер, вам следует следить за своим языком--"
        ### TITS ###
        #$ only_upper = True
        hide screen hermione_main                                                                                                                                                                                   #HERMIONE
        with d5                                                                                                                                                                                                                        #HERMIONE
        $ h_xpos=140 #Defines position of the Hermione's full length sprite. (Default 370). (Center: 140)                                                       #HERMIONE
        $ h_body = "03_hp/13_hermione_main/body_81.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
        show screen hermione_main                                                                                                                                                                                 #HERMIONE
        with d5                                                                                                                                                                                                                       #HERMIONE
        show screen ctc
        stop music
        pause
        hide screen ctc
        #her "..."
        
        dum3 "{size=+4}!!!{/size}"
        hide screen hermione_main                                                                                                                                                                                   #HERMIONE
        with d5                                                                                                                                                                                                                        #HERMIONE
        $ h_body = "03_hp/13_hermione_main/body_86.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
        show screen hermione_main                                                                                                                                                                                 #HERMIONE
        with d5                                                                                                                                                                                                                       #HERMIONE
        her "Или вы хотите увидеть мою киску, сэр?"
        hide screen hermione_main                                                                                                                                                                                   #HERMIONE
        with d3                                                                                                                                                                                                                        #HERMIONE
        $ only_upper = True
        $ h_body = "03_hp/13_hermione_main/body_61.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
        show screen hermione_main                                                                                                                                                                                 #HERMIONE
        with d3                                                                                                                                                                                                                        #HERMIONE
        show screen ctc
        pause
        hide screen ctc

        with hpunch
        dum5 "{size=+7}Арх!!!{/size}"
        
        
        her "Я готова на все ради очков, сэр!"
        hide screen hermione_main                                                                                                                                                                                   #HERMIONE
        with d5                                                                                                                                                                                                                        #HERMIONE
        $ only_upper = False
        $ h_body = "03_hp/13_hermione_main/body_86.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
        show screen hermione_main                                                                                                                                                                                 #HERMIONE
        with d5                                                                                                                                                                                                                       #HERMIONE
        with hpunch
        her "То есть {size=+9}АБСОЛЮТНО НА ВСЕ!!!{/size}"
 
        
        
        hide screen hermione_main                                                                                                                                                                                   #HERMIONE
        with d3                                                                                                                                                                                                                        #HERMIONE
        

        
        
        hide screen bld1
        with d3
        $ walk_xpos=400 #Animation of walking chibi. (From)
        $ walk_xpos2=280 #Coordinates of it's movement. (To)
        $ hermione_speed = 03.0 #The speed of moving the walking animation across the screen.
        show screen hermione_walk_01 
        pause 1
        show screen blkfade
        with Dissolve(0.3)
        $ renpy.play('sounds/08_hop_on_desk.mp3') #Sound of the desk squeaking. 
        pause.7
        
        dum4 "Ох, дорогая... {image=textheart.png} "
        pause 1
        
    $ renpy.play('sounds/win2.mp3')   #Not loud.
    centered "{size=+7}{color=#cbcbcb}-\{Спасибо за игру!\}-{/color}{/size}\n\n\
              {size=+1}{color=#cbcbcb}-АКАБУР 2014-{/color}{/size}"
    
    pause 2

    $ badges = True # Turns the badges layer in hermione_main back on.
        
    $ persistent.game_complete = True # Turns TRUE after you beat the game. Unlocks the gallery.
        
    if public_whore_ending:
        $ persistent.ending_02 = True # Unlocked ending 01.
    else:
        $ persistent.ending_01 = True # Unlocked ending 01.
        
    $ persistent.gold = 0
    $ persistent.gold = persistent.gold + gold
        
    ### THE SKIRT ###
    if gave_miniskirt: #Turns True when Hermione has the miniskirt.
        $ persistent.haveskirt = True # Makes sure you only need to buy the skirt once. Checked at the +new game screen.
   
    
    ### POSSESSIONS ###
    $ persistent.lolipop = 0
    $ persistent.lolipop = persistent.lolipop + candy # LOLIPOP.
    
    $ persistent.choco = 0
    $ persistent.choco = persistent.choco + chocolate # CHOCOLATE.
                    
    $ persistent.owl = 0
    $ persistent.owl = persistent.owl + owl # PLUSH OWL.
                
    $ persistent.beer = 0
    $ persistent.beer = persistent.beer + beer # BUTTERBEER
                
    $ persistent.mag1 = 0
    $ persistent.mag1 = persistent.mag1 + mag1 #MAGAZINE # 1
    
    $ persistent.mag2 = 0
    $ persistent.mag2 = persistent.mag2 + mag2 #MAGAZINE #  2
    
    $ persistent.mag3 = 0
    $ persistent.mag3 = persistent.mag3 + mag3 #MAGAZINE # 3
    
    $ persistent.mag4 = 0
    $ persistent.mag4 = persistent.mag4 + mag4 #MAGAZINE # 1

    $ persistent.krum = 0
    $ persistent.krum = persistent.krum + krum # KRUM POSTER.

    $ persistent.lin = 0
    $ persistent.lin = persistent.lin + lingerie # LENGERIE.

    $ persistent.con = 0 
    $ persistent.con = persistent.con + condoms # CONDOMS.
       
    $ persistent.vib = 0
    $ persistent.vib = persistent.vib + vibrator # VIBRATOR.
        
    $ persistent.lube = 0
    $ persistent.lube = persistent.lube + anal_lube # Anal lubricant.

    $ persistent.gag = 0
    $ persistent.gag = persistent.gag + ballgag # BALL GAG.
          
    $ persistent.plug = 0
    $ persistent.plug = persistent.plug + plug # ANAL PLUG.
          
    $ persistent.strap = 0
    $ persistent.strap = persistent.strap + strapon # STRAP-ON.
           
    $ persistent.broom = 0
    $ persistent.broom = persistent.broom + broom # BROOM.
              
    $ persistent.doll = 0
    $ persistent.doll = persistent.doll + sexdoll  # SEX DOLL.

    $ persistent.wine = 0
    $ persistent.wine = persistent.wine + wine # WINE.

            
           
    ### SACRED SCROLLS ###
    
    if sscroll_01:
        $ persistent.ss_01 = True # Sacred Scroll 01 will be unlocked in the gallery.
    if sscroll_02:
        $ persistent.ss_02 = True # Sacred Scroll 02 will be unlocked in the gallery.
    if sscroll_03:
        $ persistent.ss_03 = True # Sacred Scroll 03 will be unlocked in the gallery.
    if sscroll_04:
        $ persistent.ss_04 = True # Sacred Scroll 04 will be unlocked in the gallery.
    if sscroll_05:
        $ persistent.ss_05 = True # Sacred Scroll 05 will be unlocked in the gallery.
    if sscroll_06:
        $ persistent.ss_06 = True # Sacred Scroll 06 will be unlocked in the gallery.
    if sscroll_07:
        $ persistent.ss_07 = True # Sacred Scroll 07 will be unlocked in the gallery.
    if sscroll_08:
        $ persistent.ss_08 = True # Sacred Scroll 08 will be unlocked in the gallery.
    if sscroll_09:
        $ persistent.ss_09 = True # Sacred Scroll 09 will be unlocked in the gallery.
    if sscroll_10:
        $ persistent.ss_10 = True # Sacred Scroll 10 will be unlocked in the gallery.
        
    if sscroll_11:
        $ persistent.ss_11 = True # Sacred Scroll 11 will be unlocked in the gallery.
    if sscroll_12:
        $ persistent.ss_12 = True # Sacred Scroll 12 will be unlocked in the gallery.
    if sscroll_13:
        $ persistent.ss_13 = True # Sacred Scroll 13 will be unlocked in the gallery.
    if sscroll_14:
        $ persistent.ss_14 = True # Sacred Scroll 14 will be unlocked in the gallery.
    if sscroll_15:
        $ persistent.ss_15 = True # Sacred Scroll 15 will be unlocked in the gallery.
    if sscroll_16:
        $ persistent.ss_16 = True # Sacred Scroll 16 will be unlocked in the gallery.
    if sscroll_17:
        $ persistent.ss_17 = True # Sacred Scroll 17 will be unlocked in the gallery.
    if sscroll_18:
        $ persistent.ss_18 = True # Sacred Scroll 18 will be unlocked in the gallery.
    if sscroll_19:
        $ persistent.ss_19 = True # Sacred Scroll 19 will be unlocked in the gallery.
    if sscroll_20:
        $ persistent.ss_20 = True # Sacred Scroll 11 will be unlocked in the gallery.
            
             
    if sscroll_21:
        $ persistent.ss_21 = True # Sacred Scroll 21 will be unlocked in the gallery.
    if sscroll_22:
        $ persistent.ss_22 = True # Sacred Scroll 22 will be unlocked in the gallery.
    if sscroll_23:
        $ persistent.ss_23 = True # Sacred Scroll 23 will be unlocked in the gallery.
    if sscroll_24:
        $ persistent.ss_24 = True # Sacred Scroll 24 will be unlocked in the gallery.
    if sscroll_25:
        $ persistent.ss_25 = True # Sacred Scroll 25 will be unlocked in the gallery.
    if sscroll_26:
        $ persistent.ss_26 = True # Sacred Scroll 26 will be unlocked in the gallery.
    if sscroll_27:
        $ persistent.ss_27 = True # Sacred Scroll 27 will be unlocked in the gallery.
    if sscroll_28:
        $ persistent.ss_28 = True # Sacred Scroll 28 will be unlocked in the gallery.
    if sscroll_29:
        $ persistent.ss_29 = True # Sacred Scroll 29 will be unlocked in the gallery.
    if sscroll_30:
        $ persistent.ss_30 = True # Sacred Scroll 12 will be unlocked in the gallery.
        
        
        
        
        
        
        

        
        