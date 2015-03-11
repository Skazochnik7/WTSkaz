label your_whore:
    show screen end_u_1
    $ end_u_1_pic =  "03_hp/17_ending/02.png"
    
    
    $herView.hideQ()
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
        
        
        
    
    
    
    
    
  
    m "Нужно убедиться, что меня никто не заметил..."
    m "......................"
    m "Народу просто до черта..."
    m "Как же огромна эта школа!..."
    m ".................."
    m ".................................."
    m "Девчонки нигде не видно..."
    m ".............."
    m "......................"
    m "Так... она должна быть где-то здесь..."
    m "................"
    m "................................."
    # FADE
    show screen blktone
    with d7

    $herView.data().saveState()
    $herView.data().addItem( 'splatters', CharacterExItemSplatters( herView.mMiscFolder, "splatters.png", G_Z_POSE + 1 ) )
    
#    if queen_whore_ending: #Students talking. Ending "Queen whore".
    if end.IsEnding(const_ENDING_STRONG_GIRL): #Students talking. Ending "Prostitute".
        mal "Чувак, слышал новую сплетню? Гермиона теперь стала брать деньги."
        mal2 "Ну, после того, как она в одиночку заработала все очки факультета..."
        fem "...заработала все очки факультета?"
        mal "Ох, это ты... "
        fem "Вы, парни, опять об этой проститутке Гермионе? Неужели вокруг нет нормальных девушек?"
        fem "Эта баба дрочит члены, отсасывает всем желающим, а теперь устроила из этого бизнес, но вы только о ней и говорите! "
        mal2 "А знаешь, после того, как она в одиночку добилась победы факультета, она может позволить себе и не такой бизнес!" 
        mal2 "И кто ее в этом упрекнет? Только не я."
        mal "И не я, чувак!"
        fem "Да вы совсем сдурели! Поклоняетесь дешевой потаскухе!"
        mal "Не такой уж и дешевой."
        fem "Что?"
        mal "Не такой уж и дешевой, говорю."
        fem "Ой, прости, пожалуйста, я не узнавала за сколько она подставляет передок."
        mal "А что так? Боишься, что за тебя и половины не дадут?"
        fem "Да пошел ты! {size=-2}(*Дуется*){/size}"
        mal2 "И потом, чтоб ты знала, она не обязательно берет деньги."
        mal2 " Если приносишь очки Гриффиндору, то можешь..."
        fem "Надо же! Да она просто мать Тереза!"
        mal "А ты просто ревнуешь к ней!"
        fem "Головка бо-бо? Чтобы я ревновала к проститутке?"
        fem "За кого вы меня принимаете?!"
        mal2 "Точно ревнуешь!"
        mal2 " А когда узнаешь сколько она берет за ночь - вообще с ума сойдешь."
        fem "Очень надо..."
        mal2 "Ну, не надо, так не надо."
        fem "..."
        mal2 "..."
        mal "Я отойду, чувак, мне надо отлить. {size=-2}(*Уходит*){/size}"
        fem "{size=-2}(вслед) {/size}Спасибо, что сообщил!"
        mal2 "..."
        fem "..."
        mal2 "..."
        fem "...А, все-таки, сколько?"
        fem "Не то, чтобы мне было сильно интересно, просто..."
        fem "Забавно узнать... {size=-2}(ядовито){/size} почем нынче 'Мисс Популярность'."
        mal2 "Я слышал про 3 тысячи."
        fem "С ума сошел?! Мои предки вдвоем за месяц столько не зарабатывают!"
        mal2 "Ну, твои предки вдвоем за месяц, а она одна за ночь. И желающих хватает."
        fem "{size=-2}(*мотает головой*){/size} Все равно не верю!"
        fem "Я могу понять 500 монет, ну тысяча, если девушка очень, ну очень хороша..."
        mal2 "Так хороша, как ты?"
        fem "Что?"
        mal2 "У меня есть тысяча... И я считаю, что ты очень хороша."
        fem "{size=-2}(*краснеет*) {/size}Что ты несешь?!"
        mal2 "Я считаю, что ты так хороша, что готов отдать тебе деньги прямо сейчас и встретиться с тобой после бала."
        mal2 "А если ты мне откажешь, я с горя просто все промотаю."
        mal2 "Вот деньги..."
        fem "{size=-2}(*вздыхает*) {/size} Ну почему вы, парни, такие неотесанные?"
        fem "Может, я и так согласилась бы, обставь ты все романтично и красиво!"
        fem "А ты сразу пытаешься купить меня, как какую-нибудь Гермиону!"
        mal2 "Ну, тогда давай просто... {size=-2}(*собирается убрать купюры*){/size}"
        fem "Нет-нет {size=-2} (*выхватывает деньги*) {/size}... "
        fem "В смысле, я, конечно, и так пойду с тобой, просто потому что ты - классный парень."
        fem "А деньги... ну просто, куплю что-нибудь на них. Это же подарок мне, так?"
        mal2 "Конечно. {size=-2} (*довольно улыбается*) {/size}Тогда жду тебя у выхода после бала."
        "> Студент шлепает студентку по заднице и уходит."
        fem "Пф!......"
        fem "..........."
        fem "...3 тысячи за ночь, с ума сойти..." 
        fem "Ну и проститутка!..."
        fem "Ох, парни, почему вы в упор не замечаете нормальных девчонок?!"


#    if public_whore_ending: #Students talking. Ending "Public whore".
    if end.IsEnding(const_ENDING_PUBLIC_WHORE): #Students talking. Ending "Public whore".
        mal "Вы слышали что говорят о Гермионе Грейнджер?"
        mal2 "Что она стала первоклассной сосалкой?"
        mal "Хах? Не, это не слухи, это факт."
        mal "Говорят, что она за это получала оплату очками факультета."
        mal2 "Хм...я в это не верю, я думаю что она просто потаскуха."
        fem "Кто потаскуха?"
        mal "Ох, это ты..."
        fem "Так кто тут потаскуха?"
        mal2 "Гермиона Грейнджер..."
        fem "Оу! Вы, ребята, опять говорите об этой проститутке?"
        fem "Эта баба дрочит пару членов, отсасывает нескольким парням... и вдруг она новая школьная звезда."
        fem "Жалкая грязнокровка..."
        mal "Ты не должна ревновать ее--"
        fem "Ревновать??? ЕЁ??? Вот ещё!"
        fem "Я не зарабатываю себе популярность тем, что позволяю кому-то засовывать член мне в рот!"
        mal "Ну... если ты вдруг передумаешь..."
        fem "Что?"
        mal "Не стесняйся использовать меня, как ступеньку на пути к своей славе!"
        fem "Ты бы этого хотел!"
        mal2 "Эй, ребят, мне кажется, что это Гермиона там!"
        mal "Точно!"
        mal2 "Как думаете, если я приглашу её на танец, мне потом что-нибудь перепадет?"
        mal "Нет, если я приглашу её первым!"
        $ renpy.play('sounds/run_04.mp3')    #<--------------------Sound of running off.
        pause 2
        mal2 "Эй, стой! Это моя идея!"
        $ renpy.play('sounds/run_03.mp3')    #<--------------------Sound of running off.
        pause 2
        fem "Ребят...?"
        fem "........................."
        fem "Мда... Парни........"
        
        
#    else: #Students talking. Ending "Your whore".
    if end.IsEnding(const_ENDING_YOUR_WHORE): #Students talking. Ending "Your whore".
        mal "(Вы слышали о чем поговаривают?)"
        mal2 "(Да. Говорят, что Гермиона в одиночку набрала очки факультета.)"
        fem "(Стала шлюхой за очки, имеешь ввиду?!)"
        fem "(Какой позор!)"
        mal "(Это лишь слухи!)"
        fem "(Я думаю, что это больше, чем просто...)"
        mal "(Да заткнись уже. Ты просто ревнуешь!)"
        mal2 "(Да! Ты просто хочешь быть на месте Гермионы! Да, ты просто мечаешь стать такой же как она!)"
        mal "(Верно! Она верна \"Гриффиндору\" как никто другой! Точно!)"
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
    $ posHead = gMakePos( 390, 235 )
    $herViewHead.data().addPose( CharacterExItemPoseParade( herViewHead.mPoseFolder, "pose_parade.png", G_Z_POSE ) )

    $herViewHead.showQ( "body_159.png", posHead )
    her "О, привет!"
    $herViewHead.hideQ()
    mal "Ты выглядишь... просто великолепно, Гермиона! Ты... ты просто безупречна сегодня!"
    $herViewHead.showQ( "body_160.png", posHead )
    her "Спасибо, ты очень милый."
    $herViewHead.hideQ()
    mal2 "Можно тебя пригласить на следующий танец?"
    mal "Что? Отвали, я был первый!"
    mal2 "Ты идешь к черту!"
    mal "Отлично, дружок! Попробуй меня туда отправить!"
    mal2 "Я не твой \"дружок\", приятель!"
    $herViewHead.showQ( "body_161.png", posHead )
    her ".............."
    $herViewHead.hideQ()
    
    show screen blktone8
    with d3
    stop music fadeout 3.0
    m "Вот он, мой шанс!"
    m "(Псс! Девушка!)"
    $herViewHead.showQ( "body_162.png", posHead )
    her "???"
    $herViewHead.hideQ()
    m "(Красотка, это я! Тут!)"
    $herViewHead.showQ( "body_163.png", posHead )
    her "Профессор Дамблдор?"
    $herViewHead.hideQ()
    m "(Ш-ш-ш! Тише, и иди за мной.)"
    $herViewHead.showQ( "body_163.png", posHead )
    her "А?"
    $herViewHead.hideQ()
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
    
    $herViewHead.showQ( "body_162.png", posHead )
    her "Сэр, что происходит? Почему вы... прячетесь?"
    $herViewHead.hideQ()
    m "Просто помолчи и послушай секундочку! Ты можешь кое-что сделать для меня?"
    $herViewHead.showQ( "body_162.png", posHead )
    play music "music/(Orchestral) Playful Tension by Shadow16nh.mp3" fadein 1 fadeout 1 # SEX THEME.
    her "Да, сэр."
    $herViewHead.hideQ()
    m "Хорошо, есть одна штука... Ну, это..."
    m "Кое-что, что ты должна зна--"
    $herViewHead.showQ( "body_166.png", posHead )
    her "Конечно, сэр!"
    $herViewHead.hideQ()
    m "Что?"
    $herViewHead.showQ( "body_165.png", posHead )
    her "Только позвольте сделать это быстро, хорошо?"
    $herViewHead.hideQ()
    g4 "Позволить сделать что?"
    $herViewHead.showQ( "body_164.png", posHead )
    if end.IsEnding(const_ENDING_STRONG_GIRL): 
        her2 "Я ведь все еще должна вам за платье, верно, сэр?"
    else:
        her2 "Вы хотите, чтобы я поблагодарила вас за платье, верно, сэр?"
    $herViewHead.hideQ()
    m "Платье? Нет, я здесь не поэтому."
    $herViewHead.showQ( "body_165.png", posHead )
    if end.IsEnding(const_ENDING_STRONG_GIRL): 
        her2 "Все нормально, сэр, я ведь действительно Вам должна. "
        her2 "Я могу отдать деньгами, или Вы предпочитаете?..."
    else:
        her "Все хорошо, сэр. Я не против."
    $herViewHead.hideQ()
    m "Слушай меня, девочка! Я совсем не тот, кем ты меня считае--"
    $herViewHead.showQ( "body_167.png", posHead )
    if end.IsEnding(const_ENDING_STRONG_GIRL): 
        her2 "Я поняла, никаких денег, услуга за услугу. \nДумаю, это правильно, сэр."
    else:
        her2 "Пожалуйста, сэр, позвольте мне немного приласкать ваш член."
    $herViewHead.hideQ()
    g4 "Гх--!!!"
    $herViewHead.showQ( "body_167.png", posHead )
    if end.IsEnding(const_ENDING_STRONG_GIRL): 
        her2 "Вы не пожалеете. Я обслужу вас по высшему разряду."
    else:
        her2 "Совсем чуть-чуть. Пожалуйста, я умоляю вас..."
    $herViewHead.hideQ()
    g4 "Черт, проклятая ведьма!"
    g4 "Прекрати! Мне действительно нужно поговорить с тобой!"
    $herViewHead.showQ( "body_164.png", posHead )
    her "Конечно, сэр."
    $herViewHead.showQ( "body_167.png", posHead )
    her "Засунье ваш член мне в рот и говорите со мной."
    her "Поговорите со мной о грязных делишках."
    $herViewHead.hideQ()
    g4 "*рычит!*"
    m "*Вздох....*"
    m "Хорошо, можешь взять его..."
    m "Но ты злоупотребляешь своей силой, девчонка!"
    $herViewHead.showQ( "body_168.png", posHead )
    her "(*Хихикает!*)"
    $herViewHead.hideQ()
    m "И, когда мы закончим, нам нужно будет поговорить!"
    
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
    her "Хах?.........."
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
    her "Скоро должны сделать объявление..."
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
    her "Все уже договорено, сэр."
    m "Что?"
    her "Ой, я хочу сказать - я надеюсь, что стану..."
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
    her "Разве вы не согласны, сэр?!"
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
    her "Отлично. Я знала что вы тоже будете \"за\"."
    $ end_u_1_pic =  "03_hp/17_ending/07.png" #<---- SCREEN
    show screen end_u_1                                            #<---- SCREEN
    with d7                                                                       #<---- SCREEN
    her "*Чавк!* *Чавк!* *Глоть!*"
    m "Ох ... Это великолепно ..."
    her "*Чавк!* *Чавк!* *Глоть!*"
    
    show screen bld1
    with d5
    sna "*Кхм!*"
    sna "Внимание, личинки!" 
    m "(Снейп?)"
    sna "Я сказал, успокоиться всем!"
    sna "Время объявить, кто в этом году станет королевой ежегодного \"Осеннего бала Хогвартса\"."
    
    
    ann "Тихо, тихо все..."
    ann "Сейчас объявят королеву \"Осеннего бала\"."
    hide screen bld1
    with d5
    
    
    her "Чавк--"
    $ end_u_2_pic =  "03_hp/17_ending/04.png" #<---- SCREEN
    show screen end_u_2                                           #<---- SCREEN
    with d7                                                                       #<---- SCREEN
    her "О нет! Они уже начинают!"
    if end.IsEnding(const_ENDING_STRONG_GIRL): 
        her "Но я еще не расплатилась с Вами, сэр..."
    else:
        her "Но я не могу оставить вас в таком..."
        her "...состоянии, сэр."
    
    
    her "Что же мне делать?"
    m "Просто иди, девочка. Мы закончим чуть позже."
    her "Но... Но вы подарили мне это платье, сэр. И..."
    her ".........."
    her "Нет, я просто не могу оставить вас сейчас, сэр."
    m "Отлично! Тогда закончи начатое."
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
    her "Отлично. У нас есть немного времени."
    m "Да! Вот это энтузиазм!"
    
#    if public_whore_ending: #Students talking. Ending "Public whore".
    if end.IsEnding(const_ENDING_PUBLIC_WHORE) or end.IsEnding(const_ENDING_STRONG_GIRL):
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
        her "Сэр, вы думаете что правильно угощать ЭТИМ свою юную студентку?"
        m "Ха!"
        $ end_u_2_pic =  "03_hp/17_ending/08.png" #<---- SCREEN
        show screen end_u_2                                           #<---- SCREEN
        with d7                                                                       #<---- SCREEN
        her "*Чавк!* *Глоть!* *Глоть!*"
        her "*Чавк--"
        $ end_u_1_pic =  "03_hp/17_ending/92.png" #<---- SCREEN
        show screen end_u_1                                           #<---- SCREEN
        with d7                                                                       #<---- SCREEN
        her "Я такая хрупкая и чувствительная..."
        her "Мои родители доверили вам заботиться обо мне..."
        $ end_u_2_pic =  "03_hp/17_ending/93.png" #<---- SCREEN
        show screen end_u_2                                           #<---- SCREEN
        with d7                                                                       #<---- SCREEN
        her "Вы должны были обращаться со мной \"хорошо\", сэр..."
        her "И что же вы сейчас делаете?"
        m "*Кхм!* Да, что же я делаю?"
        $ end_u_1_pic =  "03_hp/17_ending/94.png" #<---- SCREEN
        show screen end_u_1                                           #<---- SCREEN
        with d7                                                                       #<---- SCREEN
        her "Вы положили свой пенис в мой невинный ротик, сэр!"
        $ end_u_2_pic =  "03_hp/17_ending/95.png" #<---- SCREEN
        show screen end_u_2                                           #<---- SCREEN
        with d7                                                                       #<---- SCREEN
        her "*Чавк!* *Чавк!* *Чавк!*"
        g9 "Да, так и есть! Я люблю невинных девочек!"
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
        g4 "О...Да! Отлично! Ох... Да! Ты великолепна!"
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
        her "Я стою на коленях и отсасываю своему директору!"
        $ end_u_2_pic =  "03_hp/17_ending/97.png" #<---- SCREEN
        show screen end_u_2                                           #<---- SCREEN
        with d7                                                                       #<---- SCREEN
        her "*Чавк!* *Чавк!* *Глоть!*"
        m "О, да! Ты - маленькая сучка!"
        her "*Чавк!* *Чавк!* *Чавк!*"
        her "*Чавк!* *Чавк!* *Глоть!*"
        g4 "Ты и правда умеешь говорить похотливые вещи..."
        g9 "Ты должна попробовать писать детские книжки, или что-то типа..."
        $ end_u_1_pic =  "03_hp/17_ending/07.png" #<---- SCREEN
        show screen end_u_1                                           #<---- SCREEN
        with d7                                                                       #<---- SCREEN
        her "*Чавк--"
        $ end_u_2_pic =  "03_hp/17_ending/91.png" #<---- SCREEN
        show screen end_u_2                                           #<---- SCREEN
        with d7                                                                       #<---- SCREEN
        her "Ох, но я не знаю как, сэр..."
        $ end_u_1_pic =  "03_hp/17_ending/92.png" #<---- SCREEN
        show screen end_u_1                                           #<---- SCREEN
        with d7                                                                       #<---- SCREEN
        her "Ведь я и сама - ребенок..."
        g4 "Ты - противная маленькая дрянь..."
        $ end_u_2_pic =  "03_hp/17_ending/97.png" #<---- SCREEN
        show screen end_u_2                                           #<---- SCREEN
        with d7                                                                       #<---- SCREEN
        her "*Чавк!* *Чавк!* *Глоть!* *Чавк!* *Чавк!*"
        
        show screen bld1
        with d5
        sna "Мисс Грейнджер?"
        sna "{size=-4}(Где эта девчонка?){/size}"
        ">Ропот расходится по толпе студентов..."
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
        her "Наградите меня вашей спермой."
        g4 "Агх!"
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
        g4 "{size=+5}Что за...!? Почему ты остановилась?!{/size}"
        g4 "{size=+5}Какого хрена ты делаешь--{/size}"
        hide screen blkfade 
        with d7
        show screen ctc
        pause
        hide screen ctc
        her "{size=+5}Кончите на меня, сэр! Кончите на меня!{/size}"
        with hpunch
        g4 "{size=+5}Что это за херня?!{/size}"
        $ end_u_1_pic =  "03_hp/17_ending/103.png" #<---- SCREEN
        show screen end_u_1                                           #<---- SCREEN
        with d7                                                                       #<---- SCREEN
        her "{size=+5}Кончайте на меня, сэр! Я хочу вашу горячую сперму!{/size}"
        g4 "Аргх! Ты, шлюха!.."
        $ end_u_2_pic =  "03_hp/17_ending/104.png" #<---- SCREEN
        show screen end_u_2                                           #<---- SCREEN
        with d7                                                                       #<---- SCREEN
        her "{size=+5}Да!{/size}"
        her "{size=+5}Именно, я голодная до спермы шлюха, сэр!{/size}"
        with hpunch
        g4 "{size=+7}Аргх!!!{/size}"
        g4 "{size=+7}Получай!!!{/size}"
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
        m "Что это только что было, девочка?"
        $ posHead = gMakePos( 390, 235 )
        $herViewHead.showQ( "body_165.png", posHead )
        her "Что вы имеете в виду, сэр?"
        $herViewHead.hideQ()
        $ end_u_1_pic =  "03_hp/17_ending/02.png" #<---- SCREEN
        show screen end_u_1                                           #<---- SCREEN
        hide screen blkfade
        with d7
        m "Мне что, нужно показать на это?"
        g4 "{size=+5}Показать пальцем?{/size}"
        $herViewHead.showQ( "body_165.png", posHead )
        her "Oх... Вы имеете в виду волосы?"
        $herViewHead.hideQ()
        m "Да...\"твои волосы\"..."
        $herViewHead.showQ( "body_168.png", posHead )
        her "Ну... А чего вы ожидали от меня, сэр?"
        $herViewHead.hideQ()
        m "Да чего угодно..."
        g4 "...но {size=+7}ЭТО!{/size}"
        $herViewHead.showQ( "body_163.png", posHead )
        her "Но... мне нужно идеально выглядеть на коронации..."
        $herViewHead.hideQ()
        m "И прическа, полная спермы, тебе поможет?"
        $herViewHead.showQ( "body_165.png", posHead )
        her "Ну... да..."
        $herViewHead.showQ( "body_163.png", posHead )
        her "Знаете, сперма превосходно фиксирует волосы и--"
        $herViewHead.hideQ()
        
        show screen bld1
        with d5
        stop music fadeout 1.0
        sna "Мисс Грейнджер..................?"
        sna "Вы собираетесь пропустить свою коронацию, девчонка?"
        sna "(Не то, чтобы для меня это было важно...)"
        hide screen bld1
        with d5
        
        $herViewHead.showQ( "body_161.png", posHead )
        her "Коронация! Мне нужно идти!"
        if end.IsEnding(const_ENDING_STRONG_GIRL): 
            her2 "Профессор, еще я должна расплатиться с вами за то, что вы позволили мне возглавить организацию этого бала."
            her2 "Так что я сделаю кое-что, что вам понравится..."
        $herViewHead.hideQ()
        $ renpy.play('sounds/run_03.mp3')    #<--------------------Sound of running off.
        pause 3
        
        m ".............................."
        m "................"
        m "..."
        with hpunch
        g4 "{size=+9}Черт знает что...!!!{/size}"
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
        m "Полижи мои шарики, сучка. Ну!"
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
        her "*Глотает!*"
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
        m "Что-то случилось? Почему остановилась, спермоглотка?!"
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
        m "Может быть, покажем это личико всем?"
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
        sna "{size=-4}(Где эта девчонка?){/size}"
        ">Среди студентов раздается ропот..."
        hide screen bld1
        with d5
        
        m "Отлично, слушай сюда, сучка."
        $ end_u_2_pic =  "03_hp/17_ending/20.png" #<---- SCREEN
        show screen end_u_2                                            #<---- SCREEN
        with d7                                                                        #<---- SCREEN
        her "*Глотает??*"
        m "Я хочу, чтобы ты оставалась здесь еще немного."
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
        m "Это будет весело... расслабься..."
        her "......................................"
        m "Твоя глотка великолепна, сучка."
        her "..........."
        $ end_u_1_pic =  "03_hp/17_ending/23.png" #<---- SCREEN
        show screen end_u_1                                           #<---- SCREEN
        with d7                                                                        #<---- SCREEN
        m "Такая теплая и тугая..."
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
        sna "Вы пропустите свою коронацию, дрянная девчонка!"
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
        m "Смотри, сука!"
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
        g4 "Вот это неплохо. Неплохой взгляд."
        $ end_u_1_pic =  "03_hp/17_ending/31.png" #<---- SCREEN
        show screen end_u_1                                        #<---- SCREEN
        with d7                                                                        #<---- SCREEN
        her "...........................................................*ГЛОТЬ!*"
        with hpunch
        g4 "Гхр!"
        g4 "Надвигается!"
        g4 "Я знаю, ты пытаешься вздохнуть..."
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
        m "О, да..."
        $ end_u_2_pic =  "03_hp/17_ending/36.png" #<---- SCREEN
        show screen end_u_2                                             #<---- SCREEN
        with d7                                                                        #<---- SCREEN
        her "...................................................."
        m "Ну... я думаю, что это всё--"
        with hpunch
        g4 "{size=+5}А?!!{/size}"
        show screen blkfade
        with d3
        stop music fadeout 1.0
        g4 "Эй, что за--"
        ">Гермиона резко встает и убегает, не сказав ни слова..."
        $ renpy.play('sounds/run_03.mp3')    #<--------------------Sound of running off.
        pause 3
        m "Хм...?"
        m "Оу, точно...коронация..."
        m "............."
        m "Но я все равно должен с ней поговорить..."
        ">..............{w}..................{w}...................."
    
    pause 1
    
    
#    if public_whore_ending: #Students talking. Ending "Public whore".
    if end.IsEnding(const_ENDING_PUBLIC_WHORE) or end.IsEnding(const_ENDING_STRONG_GIRL):
        $ s_head_xpos = 330 # x = 330,
        $ s_head_ypos = 340 #Right bottom corner: y = 340. y = 380 - no hand.
        $ s_sprite = "03_hp/10_snape_main/snape_03.png"
        show screen s_head2
        sna "Мисс Грейнджер...?"
        $ s_sprite = "03_hp/10_snape_main/snape_04.png"
        sna2 "Вы, наконец-то, решили показаться?"
        sna2 "Неприятный сюрприз..."
        $herViewHead.showQ( "body_162.png", posHead )
        her "Профессор..."
        $ s_sprite = "03_hp/10_snape_main/snape_10.png"
        show screen s_head2
        sna "Что ж, выходите вперед..."
        sna "Вот ваша корона..."
        sna "И ваш пьедестал..."

        $herViewHead.data().addItem( 'tiara', CharacterExItem( herViewHead.mClothesFolder, "tiara.png", G_Z_FACE + 1 ) )
        $herViewHead.showQ( "body_160.png", posHead )
        her "Спасибо, профессор."
        $herViewHead.hideQ()
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
        her "Я хотела бы посвятить свое выступление каждой девушке в этом зале ..."
        
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
        her "Я не собираюсь говорить громкие слова о том, что я не заслуживаю такой чести..."
        her "Потому что я думаю, что заслуживаю..."
        $ end_u_1_pic =  "03_hp/17_ending/112.png" #<---- SCREEN
        show screen end_u_1                                             #<---- SCREEN
        with d7                                                                        #<---- SCREEN
        her "Но, я действительно благодарна вам за то, что стою сейчас перед вами."
        
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
        her "В особенности, я бы хотела поблагодарить наших учителей за их нелегкий труд."
        
        show screen blktone
        show screen bld1
        with d3
        g4 "Разве она не чувствует этого?"
        g4 "Лучше бы ей закругляться побыстрее."
        hide screen blktone
        hide screen bld1
        with d3
        
        her "Хогвартс стал поистине вторым домом для всех нас..."
        $ end_u_1_pic =  "03_hp/17_ending/114.png" #<---- SCREEN
        show screen end_u_1                                             #<---- SCREEN
        with d7                                                                        #<---- SCREEN
        her "Я уверена, что так думает каждый студент в этом зале."
        
        show screen blktone
        show screen bld1
        with d3
        mal "(Это не похоже на пот, хотя...)"
        mal2 "(Даа...)"
        mal2 "(Какая-то странная фигня стекает с её волос...)"
        fem "(Парни, вы реально {size=+5}настолько{/size} слепы?)"
        mal "(Что?)"
        fem "(Это сперма... очевидно же.)"
        mal2 "(Что? Это бред!)"
        fem "(Я думаю, что знаю, как выглядит сперма, и это она!)"
        mal "(Уверен, что знаешь. *Хихикает*)"
        fem "(Не важно. Просто присмотритесь внимательнее.)"
        fem "(Должно быть какой-то парень засунул член в её прическу и спустил всё туда.)"
        mal "(Хм... Трахать волосы? Это сейчас модно?)"
        mal2 "(Вы, девчонки, делаете абсолютно сумасшедшие вещи!)"
        fem "(*Пф!* Не все мы шлюхи, вы должны знать.)"
        mal "(К сожалению, нет...)"
        fem "(\"К сожалению\"?!)"
        fem "(Пф! Вы, мужчины, абсолютно невежественны.)"
        fem "(Вы никогда не сможете построить прочных отношений со шлюхой!)"
        mal "(Что такое \"прочные отношения\"?)"
        fem "(Это когда ваша девушка - ваш лучший друг.)"
        mal "(Оу, я думаю, что не нуждаюсь в {size=+5}этом{/size}!)"
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
        m "Хах?"
        hide screen blktone
        hide screen bld1
        with d3
        
        her "Напуганная своей силой... ничего не понимающая"
        
        show screen blktone
        show screen bld1
        with d3
        m "Хм..."
        m "Что за... она делает это опять..."
        hide screen blktone
        hide screen bld1
        with d3
        
        her "Кто знает, что бы со мной случилось, если бы я не оказалась в Хогвартсе!"
        show screen blktone
        show screen bld1
        with d3
        m "И опять..."
        m "Хм, почему она так странно подергивает плечом...?"
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
        mal "(Может, у меня глюки?)"
        mal2 "(Похоже что нет... я тоже это вижу...)"
        mal "(Сиськи... Гермионы... Грейнджер...)"
        mal "(Похоже, её платье порвалось, чувак!)"
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
        her "Я бы хотела, чтобы вы увидели, как сильно Хогвартс изменил меня..."
        her "Я бы хотела, чтобы вы могли увидеть вашу девочку сейчас..."
        her "{size=-5}Ах...{/size}{image=textheart.png}"
        show screen ctc
        pause
        hide screen ctc
        
        show screen blktone
        with d7
        g4 "Эта шлюха покраснела! Похоже, она отлично знает, что происходит!"
        g4 "Настоящая шалава!"
        g4 "(Интересно, она спланировала всё это??!)"
        if end.IsEnding(const_ENDING_STRONG_GIRL):
            g4 "Ну конечно, она же сказала 'я сделаю кое-что, что вам понравится...'"
        else :
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
        mal "(Хм, теперь она просто стоит...)"
        mal2 "(Дает возможность как следует рассмотреть?)"
        mal "(Ты думаешь она знает, что её дойки видны всем?)"
        fem "(Стыдно-то как...)"
        fem "(Похоже, я чуть не пожалела настоящую шлюху...)"
        fem "........................"
        with hpunch
        fem "{size=+7}Прикрой сиськи, потаскуха!!!{/size}"
        mal "(!!!)"
        mal2 "(Ты с ума сошла?!)"
        with hpunch
        fem "{size=+7}Гриффиндорская шлюха!!!{/size}"
        hide screen blktone
        with d7
        
        $ end_u_2_pic =  "03_hp/17_ending/121.png" #<---- SCREEN
        show screen end_u_2                                             #<---- SCREEN
        with d7                                                                        #<---- SCREEN
        her "{size=-3}Ах...{/size}{image=textheart.png}"
        her "...............................А-ха...{image=textheart.png}{image=textheart.png}{image=textheart.png}"
        show screen ctc
        pause
        hide screen ctc
        
        show screen bld1
        with d7
        cr1 "Покажи нам обе, Гермиона!"
        cr2 "Смотрите! Её лицо покрыто спермой!"
        cr1 "Ты совсем стыд потеряла?!"
        cr2 "Прикройся, шлюха!"
        hide screen bld1
        with d7
        
        $ end_u_1_pic =  "03_hp/17_ending/122.png" #<---- SCREEN
        show screen end_u_1                                             #<---- SCREEN
        with d7                                                                        #<---- SCREEN
        her "Ох... точно..."
        her "Чуть не забыла..."
        $ end_u_2_pic =  "03_hp/17_ending/123.png" #<---- SCREEN
        show screen end_u_2                                             #<---- SCREEN
        with d7                                                                        #<---- SCREEN
        her "{size=+5}Вперед, Гриффиндор!{/size}"
        $ renpy.play('sounds/applause01.ogg') # APPLAUSE
        "*Дикий свист, вопли и апплодисменты*"
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
        sna "Прекратите сейчас же!"
        sna "Что касается вас, мисс Грейнджер..."
        sna "Я думаю, что это уже слишком."
        sna "Выметайтесь со сцены... Быстро..."
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
        her "Ох? Что это? Не может быть... одна из моих малышек выпала из платья..."
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
        cr1 "Я люблю тебя, Гермиона!"
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
        ">Дикий свист, крики и апплодисменты сопровождают Гермиону, пока она спускается по лестнице..."
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
        
        $ posHead = gMakePos( 390, 235 )
        $herViewHead.showQ( "body_165.png", posHead )
        her "Профессор Дамблдор..."
        if end.IsEnding(const_ENDING_STRONG_GIRL):
            her2 "Вам понравилось? Это было достойным ответным подарком?"
            $herViewHead.hideQ()
            g4 "Ну, сука!"
            her2 "Мне еще вас отблагодарить?"
        else:
            her2 "Вы хотели о чем-то поговорить со мной?"
            $herViewHead.hideQ()
            g4 "Поздно, сука!"
        show screen blkfade
        with d5
        $herViewHead.showQ( "body_164.png", posHead )
        her "Сэр?!"
        $herViewHead.hideQ()
        label tttest:
        g4 "Я тебя теперь {size=+7}ТАК{/size} оттрахаю! Иди сюда!"
        play music "music/(Orchestral) Playful Tension by Shadow16nh.mp3" fadein 1 fadeout 1 # SEX THEME.
        $herViewHead.showQ( "body_181.png", posHead )
        her "Конечно, сэр..."
        $herViewHead.hideQ()
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
        g4 "Твоя речь... это было просто отвратительно, девчонка!"
        $ end_u_2_pic =  "03_hp/17_ending/50.png" #<---- SCREEN
        show screen end_u_2                                             #<---- SCREEN
        with d7   
        if end.IsEnding(const_ENDING_STRONG_GIRL):  
            her "Странно... Почему же тогда у вас такой каменный стояк?"
            her "Мне кажется, все прошло довольно неплохо..."
        else:                                                                   #<---- SCREEN
            her "Мне кажется, все прошло довольно неплохо... Вам не понравилось?"
        g4 "Имеешь в виду твои сиськи, на которые мог глазеть каждый?!"
        $ end_u_1_pic =  "03_hp/17_ending/56.png" #<---- SCREEN
        show screen end_u_1                                             #<---- SCREEN
        with d2                                                                        #<---- SCREEN
        her "Только на одну... ах..."
        g4 "Что?"
        her "Только на одну сиську..."
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
        
        her "Ах! Профессор!"
        g4 "Я сказал, тихо!"
        
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
        her "Да! Жестче, трахайте меня жестче!"
        m "Ты специально стонешь погромче, маленькая шлюшка?"
        g4 "Хочешь быть пойманной?"
        g4 "На профессорском члене?"
        $ end_u_1_pic =  "03_hp/17_ending/125.png" #<---- SCREEN
        show screen end_u_1                                             #<---- SCREEN
        with d5                                                                        #<---- SCREEN
        her "Ах! Может быть..."
        if end.IsEnding(const_ENDING_STRONG_GIRL):
            her "Вы ведь сами этого хотите?..."
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
        her "О! Да! Да! Я шлюха-грязнокровка!"
        g4 "Да похер! {size=-2}(Что за дурацкое слово?){/size}"
        
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
        
        her "ААААААХ! ДААААА!"
        her "ДА!!! ДАААААА! АХ!"
        $ end_u_2_pic =  "03_hp/17_ending/63.png" #<---- SCREEN
        show screen end_u_2                                             #<---- SCREEN
        with d5                                                                        #<---- SCREEN
        her "Трахайте меня! Сильнее! Да!!!"
        g4 "Гхр! Еще сильнее, сучка?!"
        g4 "!!!"
        g4 "Дерьмо! Кто-то идет сюда!"
        $ end_u_1_pic =  "03_hp/17_ending/64.png" #<---- SCREEN
        show screen end_u_1                                             #<---- SCREEN
        with d5                                                                        #<---- SCREEN
        her "Нет, сэр, продолжайте! Отшлепайте меня!"
        g4 "Нет, идиотка! Какие-то придурки идут сюда!"
        $ end_u_2_pic =  "03_hp/17_ending/127.png" #<---- SCREEN
        show screen end_u_2                                             #<---- SCREEN
        with d5                                                                        #<---- SCREEN
        if end.IsEnding(const_ENDING_STRONG_GIRL):
            her "Ну если вы им скажете, они ведь уберутся, сэр?... Или... ах!.. вы хотите разделить меня с придурками?"
        else:
            her "Что?!"
        
        # STUDENTS
        
        sly1 "Так, так, так... что это у нас тут?"
        $ end_u_1_pic =  "03_hp/17_ending/126.png" #<---- SCREEN
        show screen end_u_1                                             #<---- SCREEN
        with d7                                                                        #<---- SCREEN
        show screen ctc
        pause
        hide screen ctc
        her "!!!"
        sly1 "Я так и думал, что это ты - \"гриффиндорская\" дрянь..."
        sly1 "Стонущая шлюха..."
        sly1 "Которую трахает... Ой..."
        with hpunch
        sly1 "Профессор Дамблдор!?"
        m "Привет, парни..."
        her ".........................."
        sly1 "Упс... Эм... Мы не думали..."
        sly1 "Мы уже уходим..."
        m "Что? Не тупи, парень."
        m "Присоединяйтесь!"
        sly1 "Серьезно?"
        $ end_u_2_pic =  "03_hp/17_ending/128.png" #<---- SCREEN
        show screen end_u_2                                             #<---- SCREEN
        with d5                                                                        #<---- SCREEN
        her "ЧТО?!"
        m "Конечно."
        $ end_u_1_pic =  "03_hp/17_ending/129.png" #<---- SCREEN
        show screen end_u_1                                             #<---- SCREEN
        with d7                                     #<---- SCREEN
        if end.IsEnding(const_ENDING_STRONG_GIRL):
            her "Профессор, вы действительно хотите чтобы я сделала это с ними?!!!"
            m "А почему нет, шлюха?"
            m "Что это с тобой стряслось? Вдруг стала такой застенчивой..."
            $ end_u_2_pic =  "03_hp/17_ending/130.png" #<---- SCREEN
            show screen end_u_2                                             #<---- SCREEN
            with d5                                                                        #<---- SCREEN
            her "Разве вы не видите, что это \"Слизеринцы\"?!"
            m "И что?"
            her "Вы же знаете, что наши факультеты... это длинная история."
            m "Эм..."
            m "Что ж, ты станешь неплохим мостиком между \"Слизерином\" и \"Гриффиндором\"!"
            $ end_u_1_pic =  "03_hp/17_ending/129.png" #<---- SCREEN
            show screen end_u_1                                             #<---- SCREEN
            with d7                                                                        #<---- SCREEN
            her "Сэр, если вы думаете, что мне все равно... Я все-таки надеялась, что вы относитесь... я думала..."
            m "Что ты там думала? Ты же конченная шлюха, только прикидываешься стыдливой! Вот и покажи им, какая ты шлюха!"
            $ end_u_2_pic =  "03_hp/17_ending/130.png" #<---- SCREEN
            show screen end_u_2                                             #<---- SCREEN
            with d5
            her "..."                                                                        #<---- SCREEN
            her "Я поняла, сэр, чего вы хотите..."

        else:
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
            her "Наши факультеты... это длинная история."
            m "Эм..."
            m "Что ж, ты станешь не плохим мостиком между \"Слизерином\" и \"Гриффиндором\"!"
            m "Гермиона Грейнджер, миротворец!"
            $ end_u_2_pic =  "03_hp/17_ending/130.png" #<---- SCREEN
            show screen end_u_2                                             #<---- SCREEN
            with d5                                                                        #<---- SCREEN
            her "Нет, сэр! Я стесняюсь!"
            her "И перестаньте долбить меня, пока мы говорим, сэр!"

        m "Парни, чего вы так долго возитесь?"
        m "Я же сказал - эта шлюха в вашем распоряжении!"
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
        
        sly2 "Ха-ха-ха! Неплохо! Взгляните на это тупую морду!"
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

        if end.IsEnding(const_ENDING_STRONG_GIRL):
            her "......"
            her "............"
            her "..................."
            her "Ну, конечно, это было и для вас, мальчики. Вы же должны были увидеть, какая я шлюха."
            sly2 "О, как ты заговорила! Мы все увидели, давалка, еще как увидели!"
        else:
            her "Сэр! Прекратите трахать меня!"
            m "Хах? Разве тебе не нравится?"
        with hpunch
        pause.3
        if end.IsEnding(const_ENDING_STRONG_GIRL):
            with hpunch
            pause.3
            $ end_u_1_pic =  "03_hp/17_ending/133.png" #<---- SCREEN
            show screen end_u_1                                             #<---- SCREEN
            her "Ах-аха! Нет, прекратите, профессор! Я не могу себя контролировать, когда вы так долбите..."
            m "Контролировать? Зачем тебе себя контролировать, шлюха?"
        else:
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
        if end.IsEnding(const_ENDING_STRONG_GIRL):
            her "О, какие... ахх... прелестные малыши!"
            sly1 "Какие еще 'малыши', тупая ты сука?"
            sly2 "Без обид, бро, но думаю, она говорит о твоем... {size=-2}(*смеется*){/size}."
            sly1 "Иди нахрен!"
        else:
            her "Что?! Что вы делаете?!"
        $ end_u_2_pic =  "03_hp/17_ending/137.png" #<---- SCREEN
        show screen end_u_2                                             #<---- SCREEN
        with d5                                                                        #<---- SCREEN
        if end.IsEnding(const_ENDING_STRONG_GIRL):
            her "Ну, смелее, мальчики. Вас учили ими пользоваться? Мамочка очень ждет."
            sly2 "Еще как попользуемся, сучка, ты сейчас в этом убедишься!"
        else:
            her "Уберите от меня ваши грязные члены, придурки!"
        with hpunch
        pause.3
        $ end_u_1_pic =  "03_hp/17_ending/138.png" #<---- SCREEN
        show screen end_u_1                                             #<---- SCREEN
        with d5                                                                        #<---- SCREEN
        her "Ах... Аха..."
        sly1 "Да... Я так давно ждал этого..."
        if end.IsEnding(const_ENDING_STRONG_GIRL):
            $ end_u_1_pic =  "03_hp/17_ending/136.png" #<---- SCREEN
            show screen end_u_1                                             #<---- SCREEN
            her "Давайте ребята, не разочаруйте меня!"
            her "Профессор! Я..."
        else:
            her "Профессор!"
        m "Хах? О, не думай обо мне, девочка."
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
        if end.IsEnding(const_ENDING_STRONG_GIRL):
            her "Отлично, парни, не останавливайтесь. Подарите мамочке настоящий оргазм."
        else:
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
        if end.IsEnding(const_ENDING_STRONG_GIRL):
            her "Отличный двухочковый, парень. Охх.... Мне понравилось! Давай еще раз!"
            sly1 "Закрой рот, манда!"
            her "Если закрою, как же ты тогда в него попадешь?"
        else:
            her "Это было случайно!"
            sly1 "Правда? Давай посмотрим!"
            her "Хах?"
        
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
        with d5

        if end.IsEnding(const_ENDING_STRONG_GIRL):
            her "Парень, ты мой герой. Давай, не останавливайся!"
            sly1 "Сука, ты замолчишь когда-нибудь?! Ты достала своим гавканьем!"
        else:
            her "Это было неожиданно... просто рефлекс!"
            sly1 "Интересный рефлекс!"
            g4 "О... да..."
        with hpunch
        pause.3
        with hpunch
        pause.3
        her "Ах... Ах-аха..."
        if end.IsEnding(const_ENDING_STRONG_GIRL):
            her "Мальчики, ну, расчехляйтесь... скорее, мамочка устала ждать!..."
        else:
            her "Вы за это заплатите, тупые слизери--"
        sly1 "Заткнись, грязнокровка!"
        if end.IsEnding(const_ENDING_STRONG_GIRL):
            $ end_u_2_pic =  "03_hp/17_ending/142.png" #<---- SCREEN
            show screen end_u_2                                             #<---- SCREEN
            her "Мальчики так торопятся на горячий минет. А... ахх... они не боятся, что мамочка им попросту откусит?"            
            sly2 "Что ты несешь, шалава?! Ты... ты не посмеешь!"
            her "Я жду вас, мои сладенькие."            
            sly1 "Твою мать, эта сука на все способна! И что... Что теперь, сэр?"
            m "Послушай, это уже за гранью, Гермиона."
            her "Профессор, вас же здесь нет? Или вы внезапно появились?"
            her "Эти мальчики мне не нравятся. Но я отсосу у них, если мне заплатят."
            m "Заплатят?! Ты хочешь еще очки факультету?"
            her "{size=-2}(*хихикает*) {/size}Я хочу, чтобы они отдали мне свои бумажники со всем, что там есть. "
            her "А иначе им придется просто стоять и поддрачивать, глядя, как вы меня трахаете."
            sly1 "Ха, забирай, дешевка! У меня там сроду не было больше 10 монет. {size=-2}(*бросает бумажник*){/size}"
            sly2 "Тебе хорошо, у меня там чек с деньгами на все каникулы!"
            sly2 "А я как раз накопил на новую модель метлы... На хрен такое!"
            her "{size=-2}(*хихикает*) {/size}Ахх... Не ссорьтесь сладкие. Но... ах! или вы все или никто из вас."
            sly1 "Парни вы что, не понимаете?! Такой шанс выпадает раз в жизни! А что деньги - мусор!"
            sly2 "Я тебе это повторю, когда ты придешь ко мне побираться. {size=-2}(*бросает бумажник*){/size}"
            "> Все бросают бумажники"
            her "{size=-2}(*хихикает*) {/size}Ну вот, видите, мальчики, у вас даже юбочка не помялась. Кто первый?"

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
        her "{size=+7}(*Глотает?!?*){/size}"
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

        if end.IsEnding(const_ENDING_STRONG_GIRL):
            her "Этот мальчик - скорострел, сэр. Боюсь, он разочаровывает девушек. "
            her "Сэр, прошу, порекомендуйте ему какое-нибудь лечение, вас он послушает."
            sly1 "{size=-2}(*задохнувшись*) {/size}Заткнись, долбаная тварь!!!! Сука, я тебя сейчас убью! Я тебя!..."
            her "Я слышала, что иногда это лечится, сэр. Правда."
        else:
            her "Это все на что ты способен? Слабак!"
            sly2 "Ох... Заткнись сучка... Ты высосала меня досуха..."
        $ end_u_2_pic =  "03_hp/17_ending/137.png" #<---- SCREEN
        show screen end_u_2                                             #<---- SCREEN
        with d5                                                                        #<---- SCREEN
        her "Ну же! Кто следующий?!"
        sly2 "Я! Я следующий!"
        if end.IsEnding(const_ENDING_STRONG_GIRL):
            sly2 "Посмотрим что ты скажешь на ЭТО!"
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
        sly2 "Да! Соси, сучка, соси мой член!"
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
        sly2 "{size=+7}Кончаааааююю!{/size}"
        
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
        with d5
        if end.IsEnding(const_ENDING_STRONG_GIRL):
            her "Ты был чуть получше... Г-хха... Если ты его друг,... поучи первого трахаться."
            sly1 "Я тебя сейчас точно прибью, тварина!!!!"
            sly2 "{size=-2}(*снисходительно ухмыляется*) {/size}Да ладно тебе. Лучше трахни ее еще раз."
            sly1 "Из-за этой гребаной шлюхи у меня теперь не вста... То есть, на такую шлюху у меня больше и не встанет. Долбите ее сами, если не брезгуете."
            her "Вам нравится, сэр?"
            her "Мальчики, не задерживаемся, кто там следующий?"
        else:
            her "Следующий! Давайте же! Это все, на что вы способны?"

        sly1 "Я следующий, грязнокровка!"
        $ end_u_2_pic =  "03_hp/17_ending/154.png" #<---- SCREEN
        show screen end_u_2                                             #<---- SCREEN
        with d5                                                                        #<---- SCREEN
        if end.IsEnding(const_ENDING_STRONG_GIRL):
            her "Ах, мне нравится это имя почти так же, как 'шлюха'."
        else:
            her "{size=-5}Ах... Не называй меня так, урод...{/size}{image=textheart.png}"

        sly1 "Трахать твоё лицо действительно здорово, сучка!"
        sly1 "И после того, как я наполню твой рот спермой, ты скажешь мне спасибо!"
        sly1 "Поняла, шлюха-грязнокровка?"
        $ end_u_1_pic =  "03_hp/17_ending/153.png" #<---- SCREEN
        show screen end_u_1                                             #<---- SCREEN
        with d5                                                                        #<---- SCREEN
        if end.IsEnding(const_ENDING_STRONG_GIRL):
            her "Скажу, мой сладенький, но прежде ты мне должен доставить удовольствие."
            sly1 "Я тебя так оттрахаю, что у тебя мозги из ушей вылезут!"
        else:
            her "Иди нахер!"
        
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
        
        
        
        

        sly1 "Вот о чем я мечтал!"
        $ end_u_2_pic =  "03_hp/17_ending/154.png" #<---- SCREEN
        show screen end_u_2                                             #<---- SCREEN
        with d5  

        if end.IsEnding(const_ENDING_STRONG_GIRL):
            her "Ну маленький, ну давай... Ах-ха... Не осрамись перед друзьями."
        else:
            her "Вы слабаки...\"слизери -"
        $ end_u_1_pic =  "03_hp/17_ending/155.png" #<---- SCREEN
        show screen end_u_1                                             #<---- SCREEN
        with d5                                                                   #<---- SCREEN
        her "!!?"
        $ end_u_2_pic =  "03_hp/17_ending/156.png" #<---- SCREEN
        show screen end_u_2                                             #<---- SCREEN
        with d5                                                                        #<---- SCREEN
        her "*Чавк!* *Чавк!* *Чавк!*"
        sly1 "Да! Да! Ты чертова грязнокровка! Соси! Соси мой член!"
        m "Это довольно необычно..."
        sly1 "Сэр?"
        m "Просто..."
        m "Её щель..."
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
        sly1 "И ты тоже наслаждаешься каждым мгновением, верно?"
        sly1 "Верно, грязнокровка?"
        her "*Чавк!* *Чавк!* *Глоть!*"
        m "Ага... Каждый раз, когда ты называл её..."
        m "Хах?"
        m "Что это? Её ноги трясутся!"
        m "Ты кончаешь, девочка?"
        $ end_u_1_pic =  "03_hp/17_ending/157.png" #<---- SCREEN
        show screen end_u_1                                             #<---- SCREEN
        with d5                                                                   #<---- SCREEN
        her "..............................................."
        m "Я так и думал!"
        m "Парни, давайте немного ускоримся!"
        m "Давайте трахать её с двух сторон, пока она кончает, как грязная шлюха!"
        sly1 "Конечно, сэр."
        sly1 "Возьми-ка это, шлюха-грязнокровка!"
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
        sly1 "{size=+3}Да! Принимай ЭТО, сучка!{/size}"
        
        
        
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
        m "Отлично, парни! Давайте-ка завершим эту вечеринку эпическим концом."
        her "{size=+7}Я кончаю!{/size}"
        m "Да, кончай, шлюшка."
        m "Давайте парни, обкончайте её, залейте её целиком!"
        sly1 "Конечно, сэр."
        sly2 "Да, сэр!"
        m "Да, покройте её лицо спермой! Ей нравится это дерьмо."
        $ end_u_2_pic =  "03_hp/17_ending/161.png" #<---- SCREEN
        show screen end_u_2                                             #<---- SCREEN
        with d5                                                                        #<---- SCREEN
        her "{size=+3}Нет! Я не могу... остановиться... Прекратите!{/size}"
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
        
        m "Что ж, спасибо за ваше участие, парни."
        sly1 "Конечно, сэр, проффесор Дамблдор."
        sly2 "Рады были помочь, сэр."
        sly1 "Спасибо вам, профессор."
        sly2 "Ну что, вернемся на бал?"
        sly1 "Да, пошли!"
        sly2 "Пока, грязнокровная шлюшка!"
        sly1 "Да, спасибо за классный отсос, сучка!"
        $herViewHead.showQ( "body_181.png", posHead )
        her ".........................."
        $herViewHead.hideQ()
        $ renpy.play('sounds/footsteps.mp3') #Walking away sound
        # Walking away sound...."
        
        $ end_u_1_pic =  "03_hp/17_ending/02.png" #<---- SCREEN
        
        pause 2
        
        hide screen white
        with d9
        
        sly1 "{size=-4}(Чувак, профессор Дамблдор реально крутой дедок.){/size}"
        sly2 "{size=-4}(Да... Кто бы мог подумать.){/size}"
        sly1 "{size=-4}(Ага. Я не могу не уважать его...){/size}"
        m "Ау... Какие хорошие парни..."
        sly2 "{size=-4}(Да... Я надеюсь, что буду таким же, как он, когда состарюсь.){/size}"
        g4 "Я не старик, это вы - молодые олухи!"
        m "Хотя... в каком-то смысле, я все же стар..."
        
        if end.IsEnding(const_ENDING_STRONG_GIRL):
            stop music fadeout 2.0
            play music "music/Reamonn-Supergirl.mp3" fadein 1 fadeout 1 
            $ renpy.music.set_volume(0.3) #.....установить громкость музыки на 30% 
            sly1 "И вообще, охрененно попользовали шлюху."
            sly2 "Хм, думаешь, это мы попользовали? Я уже не уверен..."
            sly1 "Ты о чем, бро?"
            sly2 "У меня такое чувство, что это она нас поимела за наши же башли!"
            sly1 "Да ладно, чего ты. Теперь мы сможем трахать ее каждый день!"
            sly2 "Имеешь в виду - платить охуенные бабки, чтобы доставить ей удовольствие и слушать, как она при этом стебет тебя?"
            sly2 "Давай, бро! А я пас."
            sly1 "Но под конец-то мы драли ее как последнюю шлюху и ей это нравилось!"
            sly2 "Ну и кто с чем остался? Она со всеми нашими бабками и улетевшая в мультиоргазм."
            sly2 "А мы - по разу спустили... Кое-кто даже не вставлял."
            sly1 "Бро, ты не вкурил тему!"
            sly1 "Представь рожи грифиндорцев, когда мы будем рассказывать, как драли их звезду, как последнюю прошмандов...."
            sly2 "Я поостерегусь об этом трепаться. Чего и вам всем желаю."
            sly1 "...?!"
            sly2 "Если об этом услышат наши девки, тебе придется дружить с правой рукой до самого выпуска."
            sly1 "Девки-то причем?"
            sly2 "{size=-2}(*имитирует женский голос*){/size}\"Ах, эти козлы...\""
            sly2 "\"Они отдали гриффиндорской шлюхе все, что у них было, всего за один отсос!\"" 
            sly2 "Нефиговая реклама Гермионы получилась, не находишь? И, думаешь, эти ревнивые сучки тебе такое простят?"
            sly1 "Да ладно тебе, бро... не преувеличивай."
            sly2 "Я, скорее, преуменьшаю... Вы как хотите, а я с утра сразу же подкачу к ней, попрошу, чтобы молчала."
            sly1 "Че-го?"
            sly2 "Возможно придется поизвиняться и занести еще денег. Надеюсь, за ночь и вы допрете, что это не такая большая плата..."
            "> Студенты уже далеко, и их голоса становятся неслышны."

        $herViewHead.showQ( "body_176.png", posHead )
        her ".........................."
        $herViewHead.hideQ()
        m "Эй, шлюха! Чего притихла?"
        $herViewHead.showQ( "body_177.png", posHead )
        her "Я..."
        her "Я... не уверена..."
        $herViewHead.showQ( "body_176.png", posHead )
        her "Что...? Что это......."
        $herViewHead.hideQ()
        m "Давай, девчонка, возьми себя в руки!"
        $herViewHead.showQ( "body_178.png", posHead )
        if end.IsEnding(const_ENDING_STRONG_GIRL):
            her2 "Простите, сэр. Я пыталась не стать конченной шлюхой перед этими уродами, хотя знала, что вам нравится, чтобы я была именно шлюхой."
            her2 "Но, видно, против природы не пойдешь и все вышло, как вы любите."
            her2 "Мне ведь получилось вам угодить, сэр?"
            $herViewHead.hideQ()
            m "Что ты имеешь в виду?"
            $herViewHead.showQ( "body_178.png", posHead )
            her "Сэр, теперь я вам ничего не должна?"
            $herViewHead.hideQ()
            m "Должна?"
            $herViewHead.showQ( "body_178.png", posHead )
            her2 "Я ничего вам не должна ни за платье, ни за то, что стала организатором бала, ни за что-то другое?"
            $herViewHead.hideQ()
            m "Что за глупости ты говоришь. Я здесь совсем по другому поводу."
            $herViewHead.showQ( "body_178.png", posHead )
            her2 "Это не глупости, сэр! Я хочу быть уверенной, что теперь я с вами полностью расплатилась."
            ">  Поочередно поднимает лежащие на полу \nбумажники двумя пальчиками и \nотносит их в урну."
            $herViewHead.hideQ()
            m "Хм... Ну хорошо, хорошо, ты полностью расплатилась. Но я здесь..."
            $herViewHead.showQ( "body_179.png", posHead )
            her2 "Это замечательно, сэр. Потому что теперь я свободна. Так что все, сэр."
            $herViewHead.hideQ()
            m "Что 'все'?"
            $herViewHead.showQ( "body_178.png", posHead )
            her2 "Вчера я отправила в Министерство Магии доклад о том, что происходит в Хогвартсе. "
            $herViewHead.hideQ()
            m "Прости, что ты сделала?"
            $herViewHead.showQ( "body_178.png", posHead )
            her2 "Я написала и отправила полный отчет о том, что происходит в Хогвартсе."
            her2 "Все эти сексуальные услуги, оплаты за очки, преподаватели, трахающие студенток..."
            her2 "Есть свидетели, которые дадут показания. Есть записи, документы."
            $herViewHead.hideQ()
            m "Ты так хотела мне отомстить, девочка? Мне вообще-то пофиг. Я здесь, чтобы сказать тебе, что ухожу..."
            $herViewHead.showQ( "body_178.png", posHead )
            her2 "Да? Впрочем, это неважно, потому что Ваше имя я в отчет не вносила."
            her2 "Так что, в худшем случае, вас могли привлечь за халатность."
            $herViewHead.hideQ()
            m "Тогда... Не пойму, зачем ты это сделала?"
            $herViewHead.showQ( "body_179.png", posHead )
            her2 "Ну, сэр, однажды вы мне ясно дали понять, что мои проблемы никогда не станут вашими. Я задумалась и сделала выводы."
            her2 "Вы кажется, сказали, что уходите?"
            her2 "Я не спрашиваю куда, сэр, но все так и произошло - вы уходите, а я остаюсь и все мои проблемы остаются со мной."
            her2 "И, значит, я не зря готовилась."
            $herViewHead.hideQ()
            m "Ты сама виновата, девочка. Если бы ты не принялась оголяться на сцене, показывая, как любишь быть публичной, ничего бы этого не случилось!"
            $herViewHead.showQ( "body_178.png", posHead )
            her2 "Мне нужно было отдать вам все долги. И я знала, что такое вам точно понравится."
            $herViewHead.showQ( "body_181.png", posHead )
            her2 "А вообще - да, у меня стало рвать крышу. Хотя, странно, после всего, что я вытворяла на сцене - меня провожали апплодисментами."
            $herViewHead.showQ( "body_179.png", posHead )
            her2 "А после того, что вы позволили сделать парням - меня могут за человека перестать считать."
            her2 "Не знаю, получилось ли у меня что-то исправить, пока я еще что-то соображала."
            $herViewHead.hideQ()
            m "Эй, эй, не надо меня приплетать! Если с тобой что и произошло, в этом виновата ты и только ты!"
            m "Не будь глубоко в тебе спрятана шлюха, ты бы никогда не стала получать от этого удовольствие."
            m "Да и изначально вся затея с очками за услуги... Разве могла нормальная девочка пойти на такое?"
            $herViewHead.showQ( "body_168.png", posHead )
            her2 "{size=-2}(*смеется*){/size} Сэр, я не собираюсь вас обвинять, вам незачем защищаться."
            $herViewHead.showQ( "body_179.png", posHead )
            her2 "Я так благодарна вам, что вы открыли во мне другую, настоящую меня."
            her2 "А то, что вас интересуют только ощущения в члене, и плевать, что будет со мной..."
            her2 "Что ж, я сильная девочка и могу сама о себе позаботиться."
            $herViewHead.showQ( "body_178.png", posHead )
            her2 "Идите же, профессор. Вы говорили, что вам пора."

            $herViewHead.hideQ()
            m "Эм... Погоди, но каким боком министерская проверка к твоим проблемам?"
            $herViewHead.showQ( "body_178.png", posHead )
            her2 "Это самый простой способ перейти из разряда шлюх, которые трахаются со всеми, в разряд шлюх, которые сами выбирают, с кем спать."
            her2 "После ТАКОЙ встряски Хогвартс постарается забыть с чего все начиналось."
            $herViewHead.hideQ()
            m "Ты что, думаешь, тебе удастся проверкой изменить здешние порядки? Наивная чукотская девочка..."
            $herViewHead.showQ( "body_178.png", posHead )
            her2 "Ничего подобного, сэр. Думаю, из Хогвартса всего лишь выгонят несколько особо замаравшихся профессоров."
            her2 "Все на пару месяцев затихнет, а потом опять пойдет по накатанной."
            $herViewHead.showQ( "body_179.png", posHead )
            her2 "А чтобы я не раздувала эту историю, от меня предпочтут откупиться. "
            $herViewHead.showQ( "body_168.png", posHead )
            her2 "Я пока раздумываю, чего бы такого потребовать..."
            $herViewHead.hideQ()
            m "Это очень... цинично."
            $herViewHead.showQ( "body_179.png", posHead )
            her2 "Да, сэр. Я благодарна вам, что вы открыли для меня эту сторону жизни."
            her2 "Это помогает реально смотреть на вещи и добиваться того, чего я хочу."
            her2 "Например, когда я поняла, что сбор сведений тормозится банальным отсутствием денег, то стала подрабатывать проституцией."
            $herViewHead.hideQ()
            m "Я... слышал об этом."
            $herViewHead.showQ( "body_181.png", posHead )
            her2 "И я поняла, что это мне очень нравится. Вы действительно сделали из меня первоклассную шлюху, профессор."
            $herViewHead.showQ( "body_168.png", posHead )
            her2 "Так что {size=-2}(*хихикает*){/size} по крайней одна профессия у меня есть. И я вполне спокойна и за себя, и за будущее факультета."
            $herViewHead.hideQ()
            m "Факультета?"
            $herViewHead.showQ( "body_179.png", posHead )
            her2 "Вы же знаете, сэр, все, что я делала - я делала для факультета. И 'Вперед, Гриффиндор!' для меня не пустые слова."
            $herViewHead.showQ( "body_168.png", posHead )
            her2 "А теперь... Я ведь королева бала. И я хочу танцевать. И так с вами заболталась."
            $herViewHead.hideQ()
            m "Я ухожу..."
            $herViewHead.showQ( "body_179.png", posHead )
            #$ h_body = "03_hp/13_hermione_main/body_176.png" # HERMIONE
            her "Счастливого пути, сэр..."
            $MusicStop()
        else:
            her "Я... Я... Что?"
            her "Я не понимаю... Я..."
            $herViewHead.hideQ()
            m "Хм..."
            m "Я уже должен уходить."
            $herViewHead.showQ( "body_176.png", posHead )
            her "Уходить...?"
            $herViewHead.hideQ()
            m "Да. Возможно ты тоже..."
            m "Иди приведи себя в порядок и отдохни."
            $herViewHead.showQ( "body_178.png", posHead )
            her "Но я не могу уйти... Нет... Я должна..."
            her "Танцевать... Должна..."
            $herViewHead.hideQ()
            m "Танцевать? Ты не можешь танцевать в таком состоянии."
            $herViewHead.showQ( "body_176.png", posHead )
            her "Нет! Я королева бала! Я должна...."
            $herViewHead.hideQ()
            m "Ладно, как хочешь."
            m "Я ухожу..."
            $herViewHead.showQ( "body_176.png", posHead )
            her "До свидания... сэр..."

        $herViewHead.hideQ()
        m "............."
        m "Прощай, девочка."
        
        show screen ctc
        pause
        hide screen ctc
        
        show screen blkfade 
        if end.IsEnding(const_ENDING_STRONG_GIRL):
            $ end_u_2_pic =  "03_hp/17_ending/89.png" #<---- SCREEN
        else:
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

        if end.IsEnding(const_ENDING_STRONG_GIRL):
            m "Наговорила какой-то херни про меня и убежала танцевать..."    
            m "Радуется, что открыл в ней шлюху и в этом же обвиняет."    
            m "Бабы..."    
            stop music fadeout 2.0

        m "Может, мне остаться и посмотреть, как она будет танцевать после мультиоргазма?"
        m "Нет... Бал почти закончился. Это мой последний шанс свалить отсюда."
        
        show screen ctc
        pause
        hide screen ctc
        
        show screen blkfade 
        with d7
        pause.5
        
        
                
        

    else: # Ending "Your whore".
        $ posHead = gMakePos( 330, 340 )
        $ s_sprite = "03_hp/10_snape_main/snape_03.png"
        show screen s_head2
        sna "Мисс Грейнджер...?"
        $ s_sprite = "03_hp/10_snape_main/snape_04.png"
        sna2 "Вы решили все таки показаться. Неприятный сюрприз..."
        $herViewHead.showQ( "body_169.png", posHead )
        her "..............................."
        $ s_sprite = "03_hp/10_snape_main/snape_13.png"
        show screen s_head2
        sna "Что случилось с вашим лицом, девчонка?"
        $herViewHead.showQ( "body_170.png", posHead )
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
        g4 "Какого черта она творит?"
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
        $ renpy.play('sounds/gulp.mp3') #Sound of Глотьing down a liqui
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
        m "Теперь я хочу тебя трахнуть... Черт побери!"
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
        her "И, конечно же, учителей..."
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
        fem "(Пф... Еще бы.)"
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
        fem "(Потому что, если не делает этого, то становится сексуально-одержимой...)"
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
        her "Спасибо большое всем вам за помощь в организации этого мероприятия."
        her "И спасибо вам большое за то, что в этом году снова выбрали меня королевой бала..."
        $ end_u_1_pic =  "03_hp/17_ending/45.png" #<---- SCREEN
        show screen end_u_1                                            #<---- SCREEN
        with d3                                                                        #<---- SCREEN
        her "Это очень приятный и неожиданный сюрприз...!"
        her "И еще кое-что..."
        $ end_u_2_pic =  "03_hp/17_ending/43.png" #<---- SCREEN
        show screen end_u_2                                            #<---- SCREEN
        with d3                                                                        #<---- SCREEN
        her "{size=+5}Вперед, Гриффиндор!{/size}"
        show screen bld1
        with d5
        $ renpy.play('sounds/applause01.ogg') # APPLAUSE
        ">Толпа взрывается громкими апплодисментами и свистом..."
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
        m "Очень возбуждающая...Кхм, я имел ввиду вдохновляющая."

        $herViewHead.data().addItem( 'tiara', CharacterExItem( herViewHead.mClothesFolder, "tiara.png", G_Z_FACE + 1 ) )
        $herViewHead.showQ( "body_165.png", posHead )
        her "Спасибо, сэр."
        $herViewHead.hideQ()
        m "Проглотила все, что было, перед всей школой?"
        g9 "Очень мило вышло."
        $herViewHead.showQ( "body_168.png", posHead )
        her "........................................................"
        $herViewHead.hideQ()
        
        play music "music/(Orchestral) Playful Tension by Shadow16nh.mp3" fadein 1 fadeout 1 # SEX THEME.
        
        $ end_u_2_pic =  "03_hp/17_ending/02.png" #<---- SCREEN
        show screen end_u_2                                            #<---- SCREEN
        with d3                                                                        #<---- SCREEN
        hide screen blkfade 
        with d3
        show screen bld1 
        with d3
        m "Хорошо, девочка, давай поговорим теперь..." 
        $herViewHead.showQ( "body_162.png", posHead )
        her "...................."
        $herViewHead.hideQ()
        m "Есть кое что, что я должен сказать тебе..."
        m "Не знаю, с чего начать..."
        m "........................................"
        m "Ну, прежде всего я--"
        $herViewHead.showQ( "body_163.png", posHead )
        her2 "Сэр, думаю я знаю, что вы имеете ввиду."
        $herViewHead.hideQ()
        m "Ты знаешь?"
        $herViewHead.showQ( "body_163.png", posHead )
        her "Конечно."
        $herViewHead.showQ( "body_164.png", posHead )
        her2 "Одного быстрого минета недостаточно, чтобы отплатить вам за все, я права?"
        $herViewHead.hideQ()
        m "Что? Нет, я совсем не об этом--"
        $herViewHead.hideQ()
        $herViewHead.showQ( "body_164.png", posHead )
        her "Все в порядке, сэр. Правда."
        $herViewHead.showQ( "body_165.png", posHead )
        her2 "Давайте я немного спущу трусики..."
        $herViewHead.hideQ()
        g4 "Черт, девчонка! Дай мне закончить!?"
        $herViewHead.showQ( "body_164.png", posHead )
        her "Конечно, сэр..."
        $herViewHead.hideQ()
        m "Хах?"
        $herViewHead.showQ( "body_167.png", posHead )
        her2 "Просто постарайтесь не запачкать мне платье, хорошо?"
        $herViewHead.hideQ()
        g4 "*Рычание!*"
        g4 "Иди сюда, шлюха!"
        g4 "И считай, что я трахаю тебя в последний раз!"
        $herViewHead.showQ( "body_162.png", posHead )
        her "(Последний раз?)"
        $herViewHead.hideQ()
        show screen ctc
        pause
        hide screen ctc
        show screen blkfade 
        with d7
        
        # INSERTION
        
        $ renpy.play('sounds/gltch.mp3')
        with hpunch
        with kissiris
        
        $ posHead = gMakePos( 390, 340 )
        $herViewHead.showQ( "body_162.png", posHead )
        her2 "{size=+5}Ахх!!!{/size}"
        $herViewHead.hideQ()
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
        her "Это из-за того, что было..."
        m "Что было?"
        m "Хочешь сказать, ты потекла, когда задыхалась от моего члена в своей глотке?"
        her "Ах...{image=textheart.png} Да, сэр..."
        m "Это помогло тебя кончить?"
        $ end_u_2_pic =  "03_hp/17_ending/48.png" #<---- SCREEN
        show screen end_u_2                                            #<---- SCREEN
        with d5                                                                        #<---- SCREEN
        her "Немного..."
        m "Ну что ж, похоже, это тебе понравилось, не так ли?"
        her "Ах......"
        m "Не так ли, шлюха?!"
        her "Ах... Как скажете, сэр."
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
        her "Ох... Я боюсь, что кто-нибудь нас заметит--"
        m "Я думаю, ты просто хочешь, что бы тебя отшлепали!"
        her "Что!?"
        $ renpy.play('sounds/slap.mp3')
        show screen white 
        pause.1
        hide screen white
        with hpunch
        
        $ end_u_2_pic =  "03_hp/17_ending/52.png" #<---- SCREEN
        #show screen end_u_2                                            #<---- SCREEN
        #with d5                                                                        #<---- SCREEN
        her "О-охх!"
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

        her "{size=+7}О-О-ООХХ!!!!{/size}"
        m "Тише, я сказал!"
        m "Или ты хочешь, что бы тебя поймали на члене твоего директора?"
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
        g4 "Отвечай мне, сучка!"
        $ renpy.play('sounds/slap.mp3')
        show screen white 
        pause.3
        hide screen white
        with hpunch
        $ end_u_2_pic =  "03_hp/17_ending/55.png" #<---- SCREEN
        her "Да, сэр! Я хочу этого!!!"
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
        sna "Внимание, личинки!"
        sna "Начинается вальс \"Осеннего Бала Хогвартса\"..."
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
        m "О, я все прекрасно слышу. И я сделаю тебе встречное предложение."
        $ end_u_2_pic =  "03_hp/17_ending/61.png" #<---- SCREEN
        show screen end_u_2                                          #<---- SCREEN
        with d5                                                                        #<---- SCREEN
        her "Сэр?"
        m "Вместо того, чтобы отпустить тебя..."
        m "Я трахну тебя в задницу!"
        m "Хах? Что-то насчет этого?"
        her "Что? Н-но..."
        m "Я думаю, что это отличный план!"
        her "Сэр, нет! Я--"
        m "Погоди, погоди..."
        show screen blkfade
        with d7
        m "Давай-ка я для начала вытащу член из твоей щелки..."
        
        $ renpy.play('sounds/boing.mp3') #Sound of # POP!
        with hpunch
        pause.3
        $herViewHead.showQ( "body_172.png", posHead )
        her "Ах..."
        $herViewHead.showQ( "body_167.png", posHead )
        her "Сэр, нет. Вы должны выслушать меня--"
        $herViewHead.hideQ()
        $ renpy.play('sounds/gltch.mp3')
        with hpunch
        with kissiris
        
        # INSERTION
        $herViewHead.showQ( "body_173.png", posHead )
        her "{size=+7}!!!!!!!!!!!!!!!!!{/size}"
        her "Моя...{w} Моя...{w} Моя..."
        $herViewHead.hideQ()
        m "Заткнись, сучка! Слишком громко."
        with hpunch
        $herViewHead.showQ( "body_173.png", posHead )
        her "{size=+7}МОЯ ЗАДНИЦА!!!!!!!!!!!!!{/size}"
        $herViewHead.hideQ()
        g4 "Черт, девчонка, я же сказал: \"Тише!\"."
        
        $ end_u_2_pic =  "03_hp/17_ending/63.png" #<---- SCREEN
        show screen end_u_2                                          #<---- SCREEN
        with d5                                                                        #<---- SCREEN
        
        hide screen blkfade 
        with d9
        her "{size=+7}Я не могу! Я не хочу! Мне больно!!!{/size}"
        g4 "Может ты и не хочешь, зато я хочу, шлюшка!"
        $ end_u_1_pic =  "03_hp/17_ending/64.png" #<---- SCREEN
        show screen end_u_1                                          #<---- SCREEN
        with d5                                                                        #<---- SCREEN
        her "{size=+5}Ваш член просто огромен!{/size}"
        g4 "Нас поймают из-за тебя, тупая сучка!"
        m "Может быть это поможет тебе заткнуться..." 
        
        # Fishhooking.
        $ end_u_2_pic =  "03_hp/17_ending/65.png" #<---- SCREEN
        show screen end_u_2                                          #<---- SCREEN
        with d5                                                                        #<---- SCREEN
        her "!!!............"
        g4 "Вот так, шлюшка. Веди себя тихо!"
        $ end_u_1_pic =  "03_hp/17_ending/66.png" #<---- SCREEN
        show screen end_u_1                                          #<---- SCREEN
        with d5                                                                        #<---- SCREEN
        her "Ах... Блах..."
        g4 "Твоя дырка... Чертовски узкая..."
        $ end_u_2_pic =  "03_hp/17_ending/67.png" #<---- SCREEN
        show screen end_u_2                                          #<---- SCREEN
        with d5                                                                        #<---- SCREEN
        her "Ах... блах... ах..."
        g4 "Твои слюни текут по моей руке, грязная шлюшка!"
        her "Ах... Блах-блах... ах... бла-aх..."
        
        show screen blktone
        with d5
        stop music fadeout 1.0
        sna "Ну что ж, начнем..."
        sna "Сейчас вы объединитесь в пары..."
        sna "Нет! Пары 'парень - девушка', вы, два кретина! Где, по-вашему, вы находитесь? В лаборатории?"

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
        her "Ах... Я королева осеннего бала... ах..."
        m "Конечно же ты!"
        m "Но еще ты - шлюха!"
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
        g4 "Я больше не могу его двигать!"
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
        her "Хах?"
        # POP
        
        show screen blkfade
        with d7
        g4 "Не могу вытащить!"
        g4 "Расслабь чертову задницу, девчонка!..."
        
        $ renpy.play('sounds/boing.mp3') #Sound of # POP!
        with hpunch
        pause.3
        $herViewHead.showQ( "body_175.png", posHead )
        her "..........."
        $herViewHead.hideQ()
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

        m "Расслабься, я знаю что делаю!"
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
            "- Кончить в киску Гермионы -":
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
                her "Следите, что бы не запачкать мое платье!"
                g4 "Заткнись про платье, шлюха! Ты портишь весь момент!"
                $ end_u_1_pic =  "03_hp/17_ending/87.png" #<---- SCREEN
                show screen end_u_1                                             #<---- SCREEN
                with d5                                                                        #<---- SCREEN
                her "{size=+5}Извините! Ваша шлюха просит прощения!!!!{/size}"
                g4 "Да! Так-то лучше!"
                g4 "Ох......."
        
            "- Кончить в задницу Гермионы -":
                $ d_flag_02 = True #Came into asshole.
                g4 "Твоя задница должна быть уже готова к этому, шлюха!"
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
                her "{size=+5}Нет, я же умру!!!{/size}"
                g4 "Ты не умрешь, грязная девчонка."
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
                her "{size=+5}Ах! Я чувствую это!!!{/size}"
                g4 "Аргх! Да!"
                $ end_u_2_pic =  "03_hp/17_ending/83.png" #<---- SCREEN
                show screen end_u_2                                             #<---- SCREEN
                with d5                                                                        #<---- SCREEN
                her "{size=+5}Оно внутри меня! Наполняет всю меня!!!{/size}"
                g4 "Да! ШЛЮХА! Я заполню тебя до краев своей спермой!"
                $ end_u_1_pic =  "03_hp/17_ending/84.png" #<---- SCREEN
                show screen end_u_1                                             #<---- SCREEN
                with d5                                                                        #<---- SCREEN
                her "Профессор! Платье!"
                g4 "Что?"
                her "Следите, чтобы не запачкать мое платье!"
                g4 "Заткнись про платье, шлюха! Ты портишь весь момент!!"
                $ end_u_2_pic =  "03_hp/17_ending/85.png" #<---- SCREEN
                show screen end_u_2                                             #<---- SCREEN
                with d5                                                                        #<---- SCREEN
                her "{size=+5}Извините! Ваша шлюха просит прощения!!!!{/size}"
                g4 "Да! Так-то лучше!"
        
                
        $ posHead = gMakePos( 390, 235 )            

        show screen ctc
        pause
        hide screen ctc
        show screen blkfade
        with d9
        $herViewHead.showQ( "body_177.png", posHead )
        stop music fadeout 1.0
        her "Ах..."
        her "Я... едва могу... стоять"
        $herViewHead.hideQ()
        g4 "Я знаю, что это значит, девочка."
        g4 "Это был наш с тобой лучший трах!"
        $herViewHead.showQ( "body_177.png", posHead )
        her "Да... Я никогда не забуду этого..."
        her "...сильнейшего оргазма..."
        her "Но я должна идти... танцевать..."
        m "Тогда иди..."
        $herViewHead.showQ( "body_176.png", posHead )
        her "Сэр... Что вы хотели обсудить со мной?..."
        $herViewHead.hideQ()
        m "Да... Знаешь что? Я, на самом деле, написал тебе небольшое письмо по этому поводу..."
        $herViewHead.showQ( "body_178.png", posHead )
        her "Письмо?"
        $herViewHead.hideQ()
        m "Да... Оно должно кое-что прояснить..."
        $herViewHead.showQ( "body_177.png", posHead )
        her "Оу... Хорошо..."
        $herViewHead.hideQ()
        m "Просто прочитай его завтра утром..."
        m "Или когда-нибудь..."
        m "Или не читай вообще, меня это не особо волнует..."
        g4 "............."
        $herViewHead.showQ( "body_179.png", posHead )
        her "Сэр...?"
        $herViewHead.hideQ()
        m "Не делай такие глаза! Я начинаю чувствовать себя неловко..."
        m "Я написал тебе письмо, что-то не так?"
        $herViewHead.showQ( "body_179.png", posHead )
        her "Я думаю... это очень мило............."
        $herViewHead.hideQ()
        g4 "Иди, девочка! Мне кажется, или ты опаздывала на какой-то танец?"
        $herViewHead.showQ( "body_180.png", posHead )
        her "ТАНЕЦ!"
        her "Извините, я должна бежать!"
        her "Увидимся позже, сэр!"
        $herViewHead.hideQ()
        
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
            
        ">Вы ненадолго задержались, глядя, как Гермиона танцует вальс..."
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
            ">Вы видите струйку прозрачной жидкости, стекающей по внутренней стороне ее бедра... никем больше не замеченную..."
        elif d_flag_02: #Came into asshole.
            ">Вы видите, что она сильно напрягает свои ягодицы."
            ">Видимо делает все возможное, чтобы сохранить ощущения, которые вы подарили её задней дырочке..."
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
    
label test:    
    
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
    
    
    
    m "Ну что ж, самое время уходить..."
    
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
#    if public_whore_ending: # PUBLIC WHORE ENDING
#        centered "{size=+7}{color=#cbcbcb}Поздравляем с прохождением игры!{/color}{/size}\n\n\
#              {size=+5}{color=#cbcbcb}Это концовка \"0"+str(1)+"2\" из \"02\".{/color}{/size}"
#    else: # YOUR PERSONAL WHORE
#        centered "{size=+7}{color=#cbcbcb}Поздравляем с прохождением игры!{/color}{/size}\n\n\
#              {size=+5}{color=#cbcbcb}Это концовка \"01\" из \"02\".{/color}{/size}"
    $ temp = end.Congratulation()
    centered "[temp]"

    
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
    centered "{cps=20}{size=+5}{color=#ea91b0}-Тренер Ведьмы 1.3 (русская редакция)-{/color}{/size}\n\n\n\
    {color=#e5e297}-\{Перевод Witch Trainer\}-{/color}\n\n\
    {color=#fff}\
    {a=http://pornolab.net/forum/profile.php?mode=viewprofile&u=14141420}Ave_Fletch{/a}, {a=http://wtrus.ixbb.ru/profile.php?id=4}Nyarkohotep{/a}\n\
    {a=http://pornolab.net/forum/profile.php?mode=viewprofile&u=15155170}Discordnk90{/a}, {a=http://pornolab.net/forum/profile.php?mode=viewprofile&u=8041771}maniac4a{/a}, {a=http://pornolab.net/forum/profile.php?mode=viewprofile&u=4472572}Rio-Violente{/a}\n\
    {a=http://pornolab.net/forum/profile.php?mode=viewprofile&u=16957111}MrFrost1991{/a}, {a=http://pornolab.net/forum/profile.php?mode=viewprofile&u=18304384}babaylolxz{/a}, {a=http://pornolab.net/forum/profile.php?mode=viewprofile&u=15281703}Borzsama{/a}\n\
    {a=http://pornolab.net/forum/profile.php?mode=viewprofile&u=11908608}sn0rk95{/a}, {a=http://wtrus.ixbb.ru/profile.php?id=3}Khan{/a}, {a=http://wtrus.ixbb.ru/profile.php?id=2}Skazochnik{/a}\n\n\
    {color=#cbcbcb}Если кого-то забыли - простите ;){/color} \
    \n\n\n\
    {color=#e5e297}-\{Программирование:\}-{/color}\n\n\
    {color=#fff}\
    {a=http://pornolab.net/forum/profile.php?mode=viewprofile&u=14141420}Ave_Fletch{/a}, {a=http://wtrus.ixbb.ru/profile.php?id=68}Eskelsama{/a},\n\
    {a=http://wtrus.ixbb.ru/profile.php?id=2}Skazochnik{/a}, {a=http://wtrus.ixbb.ru/profile.php?id=65}i11idan{/a}\
    \n\n\n\
    {color=#e5e297}-\{Тексты новых ивентов:\}-{/color}\n\n\
    {color=#fff}\
    {a=http://wtrus.ixbb.ru/profile.php?id=4}Nyarkohotep{/a}, {a=http://wtrus.ixbb.ru/profile.php?id=2}Skazochnik{/a}\n\n\
    \n\n\n\
    {color=#e5e297}-\{Теническая поддержка:\}-{/color}\n\n\
    {color=#fff}\
    {a=http://wtrus.ixbb.ru/profile.php?id=3}Khan{/a}, {a=http://wtrus.ixbb.ru/profile.php?id=46}Dimon_Tools{/a}\n\n\
    \n\n\n\
    "

    centered "{cps=20}{size=+5}{color=#ea91b0}-Witch Trainer-{/color}{/size}\n\n\
    {color=#e5e297}-\{Сценарист и продюссер\}-{/color}\n{size=+5}{color=#cbcbcb}AKABUR{/color}{/size}\n\n\
    {color=#e5e297}-\{Главный программист\}-{/color}\n {size=+5}{color=#cbcbcb}AKABUR{/color}{/size}\n\n\
    {color=#e5e297}-\{Арты\}-{/color}\n   {size=+5}{color=#cbcbcb}AKABUR{/color}{/size}\n\n\
    {color=#e5e297}-\{Дополнительные арты\}-{/color}\n   {size=+5}{color=#cbcbcb}DAHR{/color}{/size}\n\n\
    {color=#e5e297}-\{Тексты\}-{/color}\n   {size=+5}{color=#cbcbcb}LYK.D9{/color}{/size}\n\n\
    {color=#e5e297}-\{Технический менеджер\}-{/color}\n   {size=+5}{color=#cbcbcb}XALJIO{/color}{/size}\n\n\
    {color=#e5e297}-\{Тестеры\}-{/color}\n   {size=+5}{color=#cbcbcb}XALJIO\nLYK.D9\nDAHR\nAKABUR{/color}{/size}\n\n{/cps}"
    
    
    
    nvl clear


    #$ dermo = "ch_hem run_f"
#    $ dermo = "jerking_off_03_ani"
#    show screen credits_chibi
   
  
    $ xder = 160
    $ yder = 160
    $ dermo = "jerking_off_03_ani"
    show screen uni_cr
    hide screen credits_chibi
   
    
    
    

    centered "{cps=40}{size=+5}{color=#e5e297}-\{Звуковые эффекты\}-{/color}{/size}\n{color=#cbcbcb}http://www.freesound.org/{/color}\n\n\
    {size=+5}{color=#e5e297}-\{Музыка предоставлена\}-{/color}{/size}\n\
    {color=#cbcbcb}http://incompetech.com/{/color}{/cps}\n\n\
	{cps=40}{size=+5}{color=#e5e297}-\{Музыка\}-{/color}{/size}\n\n\
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

    centered "{cps=40}{size=+2}{color=#e5e297}-\{Создатели Witch Trainer также выражают благодарность\}-{/color}{/size}\n\n{color=#cbcbcb} \
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
    
    
#    if public_whore_ending: # PUBLIC WHORE ENDING
    if end.IsEnding(const_ENDING_PUBLIC_WHORE) or end.IsEnding(const_ENDING_STRONG_GIRL):
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
        sna "Кто рулит?"
        hide screen s_head2     
        dum2 "Извини?"
        $ s_sprite = "03_hp/10_snape_main/snape_26.png"                                         # SNAPE
        show screen s_head2                                                                                                 # SNAPE
        sna "Кто ... рулит?" # T_T
        hide screen s_head2     
        dum2 "?!?..."
        show screen s_head2                                                                                                 # SNAPE
        sna "Кто рулит?"
        hide screen s_head2     
        dum2 "... рулит чем?"
        show screen s_head2                                                                                                 # SNAPE
        sna "Ака....?"
        hide screen s_head2     
        dum2 "А?"
        $ s_sprite = "03_hp/10_snape_main/snape_27.png"                                         # SNAPE
        show screen s_head2                                                                                                 # SNAPE
        sna "\"Ака....\"?"
        hide screen s_head2     
        dum2 "Это бессмысленно, Северус."
        $ s_sprite = "03_hp/10_snape_main/snape_29.png"                                         # SNAPE
        show screen s_head2                                                                                                 # SNAPE
        sna "Ах, черт бы все побрал..................."
        if end.IsEnding(const_ENDING_STRONG_GIRL):
            sna2 "Гхм, профессор, у нас серьезные проблемы. "
            sna2 "В Хогвартсе полно проверяющих из Министерства Магии! "
            sna2 "Они роются в бумагах, расспрашивают студентов. Я обогнал двоих, которые шли к Вашей башне!"
            hide screen s_head2     
            dum2 "Это очень странно, Северус. Что же они ищут?"
            show screen s_head2     
            sna2 "Я не знаю, Альбус..."
            sna2 "Но, что бы они ни говорили про меня - это все наглая, бессовестная ложь!..."

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
        $ hermione_chibi_ypos = 250
        show screen hermione_02 #Hermione stands still.
        pause.5
        show screen bld1
        with Dissolve(.3)
        
        $ pos = POS_370

        show screen hermione_02
        
        show screen ctc
        pause
        hide screen ctc
        play music "music/Chipper Doodle v2.mp3" fadein 1 fadeout 1 # HERMIONE'S THEME.
        $ herViewHead.data().delItem( 'tiara' )
        $ herViewHead.data().delPose()
        $ posHead = gMakePos( 390, 235 )
        $herViewHead.showQ( "body_120.png", posHead )
        
        her "Вы хотели видеть меня, сэр?"
        her "Сэр, если вы насчет вчерашнего..."
        $herViewHead.hideQ()
        dum "Доброе утро, мисс Грейнджер."
        $herViewHead.showQ( "body_79.png", posHead )
        her2 "На самом деле, мне не настолько уж и понравилось..."
        $herViewHead.hideQ()
        dum "Мисс Грейнджер, я нашел это на своем столе..."
        dum "Это адресовано вам..."
        $herViewHead.showQ( "body_15.png", posHead )
        her "Письмо, сэр?"
        $herViewHead.showQ( "body_24.png", posHead )
        her "Ох, конечно! Это вы мне его написали."
        $herViewHead.hideQ()
        dum "Это письмо не от меня, мисс Грейнджер."
        $herViewHead.showQ( "body_17.png", posHead )
        her "Разве?"
        $herViewHead.showQ( "body_24.png", posHead )
        her "Ох, понятно..."
        her2 "Вы не должны этого стесняться, сэр. Все в порядке."
        $herViewHead.hideQ()
        dum "*эм*... вот."
        $herViewHead.showQ( "body_06.png", posHead )
        her2 "Спасибо, сэр."
        $herViewHead.showQ( "body_73.png", posHead )
        her "Посмотрим...."
        stop music fadeout 7.0
        $herViewHead.hideQ()
        pause.1
        
        
        $ letter_text = "{size=-7}Кому: Гермионе Грейнджер\n\n{/size}{size=-4}Дорогая [word_01]. \nЯ не тот, кто вы думаете... Даже не человек, если честно. В течении нескольких месяцев я выдавал себя за профессор Дамблдора. Но теперь мне нужно вернуться [word_02]. К тому времени, как ты получишь письмо, я буду уже далеко. Мы больше никогда не встретимся, но я буду лелеять воспоминания об этом времени в вашем мире.\n\nПрощай, моя маленькая [word_03]. {size=-3}\n\n-[word_04]-{/size}"

        label last_letter:
        show screen letter
        show screen ctc
        show screen bld1
        with Dissolve(.3)
        pause
        menu:
            "- Закончить чтение -":
                pass    
            "- Продолжить чтение -":
                jump last_letter
        hide screen letter
        hide screen ctc
        hide screen bld1
        with Dissolve(.3)
        
        
     
        show screen bld1
        with d3

        # add shock screen!
        $herViewHead.data().addPose( CharacterExItem( herViewHead.mPoseFolder, 'hermione_bw_final_shock.png', G_Z_FACE + 1 ) )

        # here was body_197, but it replaced with pose                                                                                                 # HERMIONE
        $herViewHead.showQ( None, posHead )
        her "............................................................................................................................................................."
        $herViewHead.hideQ()
        dum "Я полагаю, составитель этого - некий Джинн?"
        dum "Тот, кто выдавал себя за меня все это время?"
        # here was body_197, but it replaced with pose                                                                                                # HERMIONE
        $herViewHead.showQ( None, posHead )
        her "............................................................................................................................................................."
        $herViewHead.hideQ()
        dum "Ну, теперь я вернулся..."
        dum "И я положу конец вашему \"бизнесу по обмену очков\", конечно же."
        $herView.hideQQ()
        $ pos = POS_370

        # del shock screen
        $herView.data().delPose()

        $herView.showQQ( "body_86.png", pos )
        pause.1
        with hpunch
        play music "music/Chipper Doodle v2.mp3" fadein 1 fadeout 1 # HERMIONE'S THEME.
        her "{size=+7}Что?!!{/size}"
        $herView.hideQQ()
        $herView.showQQ( "body_66.png", pos )
        her "Как же я буду получать дополнительные очки?"
        dum "Есть другие пути, мисс Грейнджер."
        $herView.hideQQ()
        $herView.showQQ( "body_186.png", pos )
        her "А...?"
        dum "Усердный труд."
        $herView.hideQQ()
        $herView.showQQ( "body_187.png", pos )
        her "Это так тупо!"
        dum2 "Мисс Грейнджер, вам следует следить за своим языком--"
        ### TITS ###
        #$ only_upper = True
        $herView.hideQ()
        with d5                                                                                                                                                                                                                        #HERMIONE
        $ pos = POS_140

        # show tits!
        $herView.data().addPose( CharacterExItemPoseShowTits( herView.mPoseFolder, 'pose_dress_up.png', G_Z_POSE ) )

        $herView.showQ( "body_81.png", pos )
        with d5                                                                                                                                                                                                                       #HERMIONE
        show screen ctc
        stop music
        pause
        hide screen ctc
        her "..."
        
        dum3 "{size=+4}!!!{/size}"
        $herView.hideQ()
        with d5                                                                                                                                                                                                                        #HERMIONE
        $herView.showQ( "body_86.png", pos )
        with d5                                                                                                                                                                                                                       #HERMIONE
        her "Или вы хотите увидеть мою киску, сэр?"
        $herView.hideQQ()

        # Pussy!
        $herView.data().hideItem( 'panties' )
        $herView.data().addPose( CharacterExItemSkirtLifted( herView.mPoseFolder, 'pose_skirt_up.png', G_Z_POSE ) )
        $herView.showQQ( "body_61.png", pos )
        show screen ctc
        pause
        hide screen ctc

        with hpunch
        dum5 "{size=+7}Арх!!!{/size}"
        
        
        her "Я готова на все ради очков, сэр!"
        $herView.hideQ()
        with d5      
        $herView.data().delPose()
        $herView.data().showItem( 'panties' )                                                                                                                                                                                                               #HERMIONE
        $herView.showQ( "body_86.png", pos )
        with d5                                                                                                                                                                                                                       #HERMIONE
        with hpunch
        her "То есть - {size=+9}АБСОЛЮТНО НА ВСЕ!!!{/size}"
 
        
        
        $herView.hideQQ()
        

        
        
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

        
    $ persistent.game_complete = True # Turns TRUE after you beat the game. Unlocks the gallery.

#    if public_whore_ending:
#        $ persistent.ending_02 = True # Unlocked ending 01.
#    else:
#        $ persistent.ending_01 = True # Unlocked ending 01.
    $ end.UpdatePersistent()

        
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

    $herView.data().loadState()
           
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






