###################REQUEST_24 (Level 07) (65 pt.) (Blowjob to a boy). (Available during daytime only).
label new_request_24: #LV.7 (Whoring = 18 - 20)
    
    $herView.hideQQ()
    m "{size=-4}(Попросить её сделать минет одному из ее одноклассников?){/size}"
    $ menu_x = 0.5 #Default position of the menu (0.5). Version B is $ menu_x = 0.2
    menu:
        "\"(Да, давай сделаем это!)\"":
            pass
        "\"(Не сейчас.)\"":
            $event.NotFinished()
            jump new_personal_request
            
    
    $ pos = POS_140

    if request_24_points == 0: # <================================================================================ FIRST TIME
        
        m "Мисс Грейнджер, сегодня я хочу купить у вас еще одну услугу."
        $herView.hideshowQQ( "body_16.png", pos )
        her "Спасибо, сэр. Я правда ценю это."
        m "Конечно, всегда рад помочь."
        m "Я хочу, чтобы вы отсосали у одного из своих одноклассников."
        $herView.hideshowQQ( "body_48.png", pos )
        stop music fadeout 1.0
        her "!!!"
        her "...ртом?"
        if hermi.whoring <=17 or request_23_points <= 1: # Counts how many times you sent Hermione to give a handjob to a boy.
            jump too_much
        play music "music/Chipper Doodle v2.mp3" fadein 1 fadeout 1 # HERMIONE'S THEME.
        m "Да, так это обычно и делается..."
        $herView.hideshowQQ( "body_120.png", pos )
        her "Сэр, я..."
        $herView.hideshowQQ( "body_186.png", pos )
        her "Я отказываюсь от настолько развратной услуги, сэр."
        $herView.hideshowQQ( "body_131.png", pos )
        her "Могу я просто поцеловать другую девушку?"
        her "Я не против..." 
        m "Мисс Грейнджер, прекратите тратить мое время..."
        m "Если вы не в настроении продавать услуги сегодня..."
        m "Дверь - там."
        $herView.hideshowQQ( "body_120.png", pos )
        her "Но мне нужны очки, сэр. Вы знаете это."
        m "Знаете, мисс Грейнджер, как говорится..."
        m "\"Если ты не можешь отсосать член за это, значит - тебе это не нужно.\""
        $herView.hideshowQQ( "body_187.png", pos )
        her "Пф..."
        her "............................"
        m ".........................................."
        $herView.hideshowQQ( "body_69.png", pos )
        her "...ладно."
        her "Я согласна..."
        m "Тогда идите и выполняйте!"
        m "Отчитаетесь мне после уроков."
        $herView.hideshowQQ( "body_187.png", pos )
        her "......................................................................"
        her "......................................................................"
        her "......................................................................"
        m "Можете идти, мисс Грейнджер."
        her "........."
        
    else: # <================================================================================ NOT FIRST TIME
        if hermi.whoring >= 18 and hermi.whoring <= 20: # LEVEL 07 FIRST EVENT.
            m "Иди и сделай какому-нибудь счастливцу минет, девочка."
            $herView.hideshowQQ( "body_66.png", pos )
            her "......Опять?"
            m "Да, опять."
            $herView.hideshowQQ( "body_79.png", pos )
            her ".........."
        elif hermi.whoring >= 21: # LEVEL 08+ SECOND EVENT.
            play music "music/Chipper Doodle v2.mp3" fadein 1 fadeout 1 # HERMIONE'S THEME.
            m "Мисс Грейнджер..."
            m "Вы верите в гороскоп?"
            $herView.hideshowQQ( "body_12.png", pos )
            her "Ни капли, сэр..."
            m "Что ж, а стоило бы..."
            $herView.hideshowQQ( "body_14.png", pos )
            her "...?"
            m "Потому что прямо здесь у меня есть ваш гороскоп, и в нем говорится..."
            m "\"Посвятите сегодняшний день чему-нибудь, что вы делаете хорошо\"..."
            $herView.hideshowQQ( "body_13.png", pos )
            her "Что-то, что я делаю хорошо...?"
            m "Иди и отсоси еще парочку членов, девочка."
            $herView.hideshowQQ( "body_79.png", pos )
            her "....................." # :(
            m "Как обычно - отчитаешься мне после уроков..."
            $herView.hideshowQQ( "body_69.png", pos )
            her "Конечно..."
        
        
    
    
   
    
    
    $ request_24 = True

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
    
    
    
    

    

        

label new_request_24_complete:  # <=================================================================================================== EVENING
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
    $ herView.data().saveState()

    if hermi.whoring >= 18 and hermi.whoring <= 20: # LEVEL 07                    
        if one_out_of_three == 1: ### EVENT (A)
            play music "music/Chipper Doodle v2.mp3" fadein 1 fadeout 1 # HERMIONE'S THEME.
            m "Ты знаешь правила, девочка. Начинай рассказывать."
            show screen blktone
            with d3
            $herView.hideshowQQ( "body_66.png", pos )
            her "Я завершила ваше задание, сэр."
            m "Хорошо. Расскажи поподробнее."
            $herView.hideshowQQ( "body_69.png", pos )
            her "Что тут можно рассказать, сэр?"
            her "Сегодня я отсосала у одного из моих одноклассников..."
            her "Вот и все..."
            m "Хм... Понятно..."
            m "..............."
            $herView.hideshowQQ( "body_118.png", pos )
            her "...................................."
            m "Ты проглотила?"
            $herView.hideshowQQ( "body_79.png", pos )
            her "..........................."
            m "Мисс Грейнджер, вы проглотили все, как полагается?"
            $herView.hideshowQQ( "body_47.png", pos )
            her "Да, сэр."
            m "Что ж, тогда, пожалуй, сойдет..."

            
        elif one_out_of_three == 2: ### EVENT (B)
            m "Мисс Грейнджер, вы выполнили задание?"
            show screen blktone
            with d3
            $herView.hideshowQQ( "body_118.png", pos )
            play music "music/Despair_by_erenik.mp3" fadein 1 fadeout 1 # SAD THEME.
            her "Сэр, я..."
            her "Я пыталась, но..."
            $herView.hideshowQQ( "body_67.png", pos )
            her "Меня отшили, сэр..."
            $herView.hideshowQQ( "body_22.png", pos )
            her "Я не могу поверить в то, что это произошло на самом деле..."
            her "Я, одна из лучших учениц в этой школе!"
            her "Одна из самых популярных..."
            
            #$herView.data().addItemKey( 'tears', CharacterExItem( herView.mMiscFolder, "tears_01.png", G_Z_FACE + 1 ) )
            $herView.data().addItem( 'item_tears', '01' )
            
            $herView.hideshowQQ( "body_47.png", pos )
            her "И он меня отшил?"
            her "Да как он посмел меня так оскорбить?!"
            m "Так ты оскорблена, потому что тот парень отказался положить свой член тебе в рот?"
            $herView.hideQQ()
            #$herView.data().addItemKey( 'tears', CharacterExItem( herView.mMiscFolder, "tears_02.png", G_Z_FACE + 1 ) )
            $herView.data().addItem( 'item_tears', '02' )
            $herView.showQQ( "body_47.png", pos )
            her "А вы бы не оскорбились, сэр?"
            m "Думаю, я бы довольно легко это пережил..."
            $herView.hideshowQQ( "body_187.png", pos )
            her "Он отверг меня, сэр..."
            her "Да за кого он себя держит?!"
            $herView.hideshowQQ( "body_186.png", pos )
            her "При всем уважении, сэр, вам не понять..."
            m "Ну, в любом случае, я не могу заплатить тебе за это."
            $herView.hideQQ()
            #$herView.data().addItemKey( 'tears', CharacterExItem( herView.mMiscFolder, "tears_01.png", G_Z_FACE + 1 ) )
            $herView.data().addItem( 'item_tears', '01' )
            $herView.showQQ( "body_79.png", pos )
            her "Конечно... Я и не ждала этого, сэр."
            her "Я провалила свое задание и не заслуживаю никакой награды..."
            her "И вы не должны платить мне из жалости..."
            $herView.hideshowQQ( "body_69.png", pos )
            her "Я только еще больше разозлюсь..."
            m "Хм... В таком случае, может мне все-таки заплатить тебе..."
            $herView.hideshowQQ( "body_79.png", pos )
            her "Нет, сэр. Я не приму этого..."
            m "Хм... Тогда, на сегодня все."
            her "Спокойной ночи, сэр."
            $herView.hideQQ()
            $herView.data().delItem( 'item_tears' )
            
            $ request_24_points += 1 
            $ request_24 = False 
            $ hermione_sleeping = True
            call music_block
            jump could_not_flirt #Sent here when choose "Favor failed! No points for you!" (Hermione is leaving without getting any points).

        elif one_out_of_three == 3: ### EVENT (C)
            #play music "music/Despair_by_erenik.mp3" fadein 1 fadeout 1 # SAD THEME.
            m "Мисс Грейнджер, как все прошло?"
            show screen blktone
            with d3
            $herView.hideshowQQ( "body_69.png", pos )
            her "Я все еще считаю идею продавать такие услуги отвратительной, сэр."
            $herView.hideshowQQ( "body_79.png", pos )
            her "Но в остальном - все прошло на удивление хорошо..."
            play music "music/(Orchestral) Playful Tension by Shadow16nh.mp3" fadein 1 fadeout 1 # SEX THEME.
            her "Я сделала хороший минет тому шикарному парню из \"Когтеврана\"..."
            $herView.hideshowQQ( "body_87.png", pos )
            her "И он был таким джентельменом..."
            $herView.hideshowQQ( "body_118.png", pos )
            her "Он даже предупредил меня перед тем, как кончить."
            m "В самом деле, настоящий джентельмен."
            m "Ты проглотила?"
            $herView.hideshowQQ( "body_120.png", pos )
            her "Конечно, сэр."
            her "Я ведь сказала - я сделала парню хороший минет."
            $herView.hideshowQQ( "body_118.png", pos )
            her "Меньшее, что я могу сделать для кого-то, кто, для разнообразия, отнесся ко мне с уважением..."
            m "В таком случае, ладно."
            
    if hermi.whoring >= 21: # LEVEL 08 =+               
        if one_out_of_three == 1: ### EVENT (A)
            stop music fadeout 1.0
            # HERMIONE ALL MESSED UP, WITH RUNNING MASCARA.
            #$herView.data().addItemKey( 'tears', CharacterExItem( herView.mMiscFolder, "tears_03.png", G_Z_FACE + 1 ) )
            $herView.data().addItem( 'item_tears', '03' )
            #$herView.data().addItemKey( 'sperm', CharacterExItem( herView.mMiscFolder, "sperm_05.png", G_Z_FACE + 2 ) )
            $herView.data().addItem( 'item_sperm', '05' )
            #$herView.data().addItemKey( 'sperm_after', CharacterExItem( herView.mMiscFolder, "sperm_00_after.png", G_Z_FACE + 3 ) )
            $herView.data().addItem( 'item_sperm_dried' )

            show screen blktone
            with d3
            $herView.hideshowQQ( "body_47.png", pos )
            show screen ctc
            pause
            hide screen ctc
            m "Мисс Грейнджер..."
            m "Вы будто из ада вылезли..."
            play music "music/Chipper Doodle v2.mp3" fadein 1 fadeout 1 # HERMIONE'S THEME.
            $herView.hideshowQQ( "body_30.png", pos )
            her "Сэр, меня изнасиловали."
            m "Серьезно?"
            $herView.hideshowQQ( "body_79.png", pos )
            her "Да, сэр!"
            her "Тот противный парень из \"Слизерина\" изнасиловал меня..."
            $herView.hideshowQQ( "body_87.png", pos )
            her "Хотя, скорее, изнасиловал мое лицо..."
            her "И--"
            $herView.hideshowQQ( "body_132.png", pos )
            play sound "sounds/burp.mp3"
            her "*Отрыжка!*..."
            $herView.hideshowQQ( "body_118.png", pos )
            her "Простите."
            $herView.hideshowQQ( "body_86.png", pos )
            her "Он кончил так много, что я с трудом смогла все проглотить..."
            her "Чертов ублюдок!"
            $herView.hideshowQQ( "body_187.png", pos )
            her "Как вы думаете, я могу написать жалобу, сэр?"
            m "Хм... Наверное..."
            m "Но имей в виду, что как только мы втянем министерство в это ..."
            m "Всю эту \"лавочку по продаже услуг\" прийдется немедленно прикрыть."
            $herView.hideshowQQ( "body_189.png", pos )
            her "Ох...?"
            her ".................."
            $herView.hideshowQQ( "body_74.png", pos )
            her "Простите, забудьте о том, что я только что сказала..."
            m "Ты уверена? Ты выглядишь довольно помятой."
            her "Нет, нет. Это мелочи..."
            her "Все-таки это я предложила ему минет..."
            her "Он всего лишь стал обращаться со мной немного грубо под конец, вот и все..."
            her "Думаю, я просто преувеличиваю..."
            m "Понятно..."
            her "Могу я просто--"
            $herView.hideshowQQ( "body_48.png", pos )
            play sound "sounds/burp.mp3"
            her "*Отрыжка!*..."
            $herView.hideshowQQ( "body_118.png", pos )
            her "Простите, сэр."
            $herView.hideshowQQ( "body_34.png", pos )
            her "{size=-3}(Он продолжал кончать... Мой живот так набит...){/size}"
            $herView.hideshowQQ( "body_31.png", pos )
            her "Могу я получить свою плату, пожалуйста?"
            
        elif one_out_of_three == 2: ### EVENT (B)
            # HERMIONE COVERED IN CUM
            label suked_off_them_both:
                pass
            stop music fadeout 1.0
            #$herView.data().addItemKey( 'sperm', CharacterExItem( herView.mMiscFolder, "sperm_06.png", G_Z_FACE + 1 ) )
            $herView.data().addItem( 'item_sperm', '06' )
            show screen blktone
            with d3
            $herView.hideshowQQ( "body_78.png", pos )
            show screen ctc
            pause
            hide screen ctc
            her "Добрый вечер, сэр..."
            g4 "Мисс Грейнджер?!"
            g4 "Что с вами произошло, девушка?"
            g4 "Все, что я просил - сделать минет одному из ваших одноклассников."
            $herView.hideshowQQ( "body_118.png", pos )
            play music "music/(Orchestral) Playful Tension by Shadow16nh.mp3" fadein 1 fadeout 1 # SEX THEME.
            her "Это... это именно то, что я сделала, сэр."
            m "Девушка, вы покрыта спермой с ног до головы."
            $herView.hideshowQQ( "body_121.png", pos )
            her "Да?"
            her "Ох... Я забыла привести себя в порядок?"
            $herView.hideshowQQ( "body_128.png", pos )
            her "Как неловко..."
            her "Думаю, то действо в мужском туалете несколько разрослось..."
            her "Прежде чем я поняла, что происходит, я уже была окружена большими пульсирующими членами..."
            $herView.hideshowQQ( "body_133.png", pos )
            her "Ох... Просто разговор об этом заставляет меня трястись в экстазе... эээ.."
            $herView.hideshowQQ( "body_136.png", pos )
            her "...то есть в страхе... нет, не страхе..."
            $herView.hideshowQQ( "body_188.png", pos )
            her "Смущении?"
            m "Вы меня спрашиваете?"
            $herView.hideshowQQ( "body_123.png", pos )
            her "Ох, простите, сэр... Мне немного сложновато думать..."
            her "Я думаю, что мне нужно ненадолго прилечь..."
            m "Не забудьте сначала принять душ."
            $herView.hideshowQQ( "body_128.png", pos )
            her "Душ? Зачем?"
            m "Не важно..."
            show screen ctc
            pause
            hide screen ctc


        elif one_out_of_three == 3: ### EVENT (C)
            if  suked_off_ron_and_har:
                jump suked_off_them_both
            else:
                 $ suked_off_ron_and_har = True #In public events. Give blowjob to a classmate. Event level 03. Event # 3. "Sukerd off Harrt and Ron". Turns True after that.


            m "Мисс Грейнджер, как все прошло?"
            show screen blktone
            with d3
            $herView.hideshowQQ( "body_74.png", pos )
            her "Великолепно, сэр. Просто великолепно."
            m "Правда? Рассказывай."
            $herView.hideshowQQ( "body_78.png", pos )
            play music "music/(Orchestral) Playful Tension by Shadow16nh.mp3" fadein 1 fadeout 1 # SEX THEME.
            her "Сегодня я сделала то, что я хотела сделать очень давно..."
            her "Но не могла набраться смелости..."
            m "Хм..?"
            $herView.hideshowQQ( "body_121.png", pos )
            her "Сегодня я отсосала у двух моих лучших друзей во всем мире!"
            $herView.hideshowQQ( "body_124.png", pos )
            her "И это было прекрасней, чем я могла себе представить."
            $herView.hideshowQQ( "body_123.png", pos )
            her "Их члены были такими мокрыми из-за моей слюны..."
            her "Я не забыла и про их яйца..."
            $herView.hideshowQQ( "body_134.png", pos )
            her "Но лучшая часть - это выражения их лиц..."
            her "Парни не могли поверить, что это и впрямь происходит..."
            $herView.hideshowQQ( "body_133.png", pos )
            her "Если честно, и я не могла..."
            her "Я, Гермиона Грейнджер - девушка, которую они знали годами..."
            $herView.hideshowQQ( "body_135.png", pos )
            her "Сосет у них члены..."
            $herView.hideshowQQ( "body_139.png", pos )
            her "Как какая-то мерзкая, мелкая шлюшка..."
            m "Ты любишь этих парней, девочка?"
            $herView.hideshowQQ( "body_74.png", pos )
            her "Я не знаю, сэр... Может быть..."
            her "Можно мне получить свою плату?"
            m "Конечно..."
            
            

    
    
    $ gryffindor += 65 #65
    m "65 очков \"Гриффиндору\"!"
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


 


    $herView.data().loadState()

#    $ public_whore_ending = True #Activates "Public Whore" ending.
    $ end.SetEndingValue(const_ENDING_PUBLIC_WHORE,2)
    
    $ request_24_points += 1 
    $ request_24 = False 
    $ hermione_sleeping = True

    call music_block
    
    $event.Finalize()    
    return


