
#####################################################################################################################################################################
### LEVEL 03 ###########################################################################################################################################################
###################REQUEST_08 (Level 03) (Show me tits). #####################################################################################################################
label new_request_08: #LV.3 (Whoring = 6 - 8)
    $herView.hideQQ()
    if IsFirstRun():
#    if request_08_points == 0:
        m "{size=-4}(Я хочу посмотреть на эти сиськи?){/size}"
    else:
        m "{size=-4}(Я хочу посмотреть на эти сиськи снова?){/size}"
    $ menu_x = 0.5 #Default position of the menu (0.5). Version B is $ menu_x = 0.2
    menu:
        "\"(Да, давай попробуем!)\"":
            show screen blktone
            with d3
            pass
        "\"(Не сейчас.)\"":
            $event.NotFinished()
            jump new_personal_request
    
    if whoring <=5:
        jump too_much
        
    
        
    $ current_payout = 25 #Used when haggling about price of th favor.
        
    $ pos = POS_140
    
    # we'll undress her, so save the state
    $herView.data().saveState()

    if IsFirstRun() and whoring <= 11: # LEVEL 04 # FIRST TIME.
        m "Мисс Грейнджер?"
        $herView.hideQQ()
        $ pos = POS_370
        
        $herView.showQQ( "body_03.png", pos )
        her "Да, сэр..."
        m "Сколько очков будет стоить посмотреть на твои сиськи?"
        $herView.hideshowQQ( "body_14.png", pos )
        stop music fadeout 1.0
        her "Сколько стоит посмотреть на...?"
        play music "music/Chipper Doodle v2.mp3" fadein 1 fadeout 1 # HERMIONE'S THEME.
        $herView.hideshowQQ( "body_30.png", pos )
        her "Профессор Дамблдор!"
        m "Хм... Я думал, вашему факультету пригодились бы дополнительные очки..."
        m "Но, видимо, я ошибался..."
        $herView.hideshowQQ( "body_31.png", pos )
        her ".........?"
        m "Ладно, не бери в голову..."
        m "Я всего лишь хотел помочь тебе..."
        $herView.hideshowQQ( "body_29.png", pos )
        her "............."
        $herView.hideshowQQ( "body_33.png", pos )
        her "200 очков, сэр."
        m "Если я дам вам 200 очков, Мисс Грейнджер..."
        m "Вы оголите свою грудь и покажите свои дыньки?"
        $herView.hideshowQQ( "body_47.png", pos )
        her "Профессор Дамблдор! Не надо так выражаться!"
        her "Я думаю, я лучше пойду..."
        menu:
            "\"Стой. 200 очков твои. Показывай!\"":
                $ current_payout = 200 #Used when haggling about price of th favor.
                $herView.hideshowQQ( "body_14.png", pos )
                her "Серьезно?"
                m "Да"
                $herView.hideshowQQ( "body_29.png", pos )
                her "......................................"
                her "Вы обещаете, что не будете трогать их, сэр?"
                m "Конечно, конечно..."
                $herView.hideshowQQ( "body_32.png", pos )
                her "Я делаю это только ради моего факультета, сэр!"

            "\"Я дам тебе 5 очков, если ты покажешь сиськи.\"":
                $herView.hideshowQQ( "body_72.png", pos )
                her "Пять?!"
                $herView.hideshowQQ( "body_76.png", pos )
                her "Профессор, я не собираюсь показывать их за скромные пять очков!"
                m "Ну, твои сиськи, конечно, не стоят 200, девочка!"
                $herView.hideshowQQ( "body_73.png", pos )
                her "(Неужели они так плохи?)"
                $herView.hideshowQQ( "body_69.png", pos )
                her "Может быть, за сто очков?"
                menu:
                    "\"Хорошо. 100 очков твои! Показывай!":
                        $ current_payout = 100 #Used when haggling about price of th favor.
                        her "................."
                        her "Так и быть... за сто баллов..."
                    "\"25 очков - моё финальное предложение!\"":
                        her "..............."
                        her "Ну, так и быть..."
            "\"Отлично, вали. Мне пофиг..\"":
                $mad = +12
                her "Арх!"
                call music_block
                
                jump loadState_and_could_not_flirt
                
                
        hide screen blktone
        with d3
        hide screen bld1
        with d3
        $herView.hideQ( d5 )
        $ menu_x = 0.5 #Default menu position restored.
        show screen ctc
        play music "music/(Orchestral) Playful Tension by Shadow16nh.mp3" fadein 1 fadeout 1 # SEX THEME.
        pause
        show screen hermione_04
        with fade
        pause
        show screen bld1
        with d3
        m "Хм..."
        $her_head_state = 12
        her_head_main "{size=-5}(Ох, я ведь еще никому не позволяла смотреть на мои...){/size}"
        m "Подойди ближе, девочка, дай мне лучше рассмотреть..."
        $her_head_state = 4
        her_head_main "............"
        
        hide screen bld1
        with d3

        show screen blkfade #Completely black screen.
        with Dissolve(1)
        pause.5
        ">Гермиона медленно подходит к вам."
        ">С каждым шагом её сиськи покачиваются..."
       
        hide screen hermione_04 #Stands with tits out.
        hide screen genie
        show screen ctc
        show screen genie_and_tits_01
        with d1
        hide screen blkfade
        with d5
        pause
        show screen bld1
        with d3
        $her_head_state = 1
        her_head_main "............"
        m "Очень хорошо..."
        $her_head_state = 4
        her_head_main "....."


        show screen blktone 
        with d3
        $herView.hideQQ()
        
        $ pos = POS_140
        #$ only_upper = True #No lower body displayed. 
        
        # add tits pose!
        call addTitsPose
    
        $herView.showQQ( "body_81.png", pos )
        pause
        her "...................................."
        
        
    else:
        if whoring >= 6 and whoring <= 8: # LEVEL 03 # <=================================================================================== FIRST EVENT. (HERMIONE IS UNWILLING).
            m "Мисс Грейнджер?"
            $her_head_state = 2
            her_head_main "Да, профессор?"
            m "Я хочу посмотреть на твои сиськи."
            $her_head_state = 4
            her_head_main "............"
            her_head_main "Вы обещаете не трогать их, сэр?"
            m "Конечно."
            hide screen blktone
            with d3
            hide screen bld1
            with d3
            $herView.hideQ( d5 )
            $ menu_x = 0.5 #Default menu position restored.
            show screen ctc
            pause
            show screen hermione_04
            with fade
            pause
            show screen bld1
            with d3
            m "Хм..."
            m "Подойди ближе, девочка, дай лучше рассмотреть их..."
            hide screen bld1
            with d3
            show screen blkfade #Completely black screen.
            with Dissolve(1)
            pause.5
            ">Гермиона медленно подходит к вам."
            hide screen hermione_04 #Stands with tits out.
            hide screen genie
            show screen ctc
            show screen genie_and_tits_01
            with d1
            hide screen blkfade
            with d5
            pause
            show screen bld1
            with d3
            m "Очень хорошо..."
            play music "music/(Orchestral) Playful Tension by Shadow16nh.mp3" fadein 1 fadeout 1 # SEX THEME.
            show screen blktone 
            with d3
            $herView.hideQQ()
            
            # add tits pose!
            call addTitsPose

            $herView.showQQ( "body_81.png", pos )
            #$ only_upper = True #No lower body displayed. 

            pause
            her "...................................."
            
            
            
            
        elif whoring >= 9: # LEVEL 04 and higher# <=================================================================================== SECOND EVENT and THIRD EVENT. (HERMIONE IS INDIFFERENT) 
            m "Я хочу увидеть ваши сиськи, Мисс Грейнджер."
            $her_head_state = 15
            her_head_main "Вы будете только смотреть, сэр?"
            m "Конечно..."
            if whoring >= 15:
                her "Сэр, мы оба знаем, что вам интереснее, не просто смотреть, а делать кое-что еще..."
                m "Может быть это {size=+4}ВАМ{/size} интересно, мисс Грейнджер, чтобы я делал кое-что еще?"
                her "Сэр, не будем играть в игры. Мне нужны очки для факультета, вам нужны сексуальные услуги."
                her "Я не получаю от этого никакого удовольствия, но если это нужно вам, то готова пойти на большее, чтобы заработать."
                m "Вы теперь подрабатываете этим, мисс Грейнджер?"
                her "Что?.. СЭР! Я говорю о том, чтобы заработать очки!"
                m "Ох, простите, а я было подумал..."
                her "Вы подумали неправильно! Я никогда не опущусь до этого!"
                m "Ну хорошо, мисс, если речь идет о том, чтобы заработать побольше очков..."
                her "Только об этом и идет, сэр!"
                m "Тогда давайте займемся вашей попкой."
                if whoring<21:
                    her "Попкой, сэр? Но... Я не имела в виду..." 
                    m "Не имели в виду? А за что по-вашему я должен давать вам больше очков? За рождественскую песенку?"
                    her "Но я не готова, это слишком!"
                    m "Зачем же тогда вы мне морочите голову, мисс, рассказывая, что хотите заработать побольше очков?"
                    her "Я хочу, сэр, но не такой ценой!"
                    m "То есть, вы теперь указываете мне, девушка, за что вам платить?"
                    m "Вы знаете, мисс, я неравнодушен к Гриффиндору..." 
                    m "Но из-за ваших капризов начинаю серьезно подумывать, не ошибся ли я в вас?"
                    m "Может, мне позвать кого-нибудь из слизеринок? Наверняка, они более преданны факультету."
                    m "Да! Как я сразу не сообразил. Мисс Грейнджер, будьте любезны, пригласите профессоры Снейпа." 
                    m "Наверняка он порекомендует мне {size=+4}ДОСТОЙНУЮ{/size} кандидатку."
                    her "Профессор, пожалуйста..."
                    m "Что такое, мисс Грейнджер? Вы и этого не в состоянии сделать?"
                    her "Профессор, я ошиблась... я была неправа,... пожалуйста, простите меня."
                    m "И что будет завтра?"
                    m "Вам опять будет мало очков?"
                    her "Нет, сэр, я поняла. Все справедливо."
                    her "Если вы хотите посмотреть на мои сиськи, значит я должна показать вам сиськи и не торговаться из-за очков."
                    m "..............................."
                    her "............................."
                    m "Вы понимаете, мисс, что вы провинились и должны быть наказаны?"
                    her "На-наверное..."
                    m "То есть, вы не уверены?"
                    her "Нет-нет, я уверена..."
                    m "Я не стану мучать вас сложными наказаниями. Вам просто придется отсосать у меня, это вы любите..."
                    her "Ничего подобного..."
                    m "Мне послышалось?"
                    her "Да, сэр, люблю."
                    m "Полностью, будьте добры!"
                    her "Я люблю отсасывать, сэр."
                    m "Замечательно. Но чтобы наказание не превратилось для вас в сплошное удовольствие, в этот раз я не стану платить вам"
                    her "Да, сэр."
                    m "А наоброт вычту у гриффинодор"


                    .ы опять Профессор, я ошиблась... я была неправа,... пожалуйста, простите меня."
                    m "Вы понимаете, мисс, что я "
            hide screen blktone
            with d3
            hide screen bld1
            with d3
            $herView.hideQ( d5 )
            $ menu_x = 0.5 #Default menu position restored.
            show screen ctc
            pause
            show screen hermione_04
            with fade
            pause
            show screen bld1
            with d3
            m "Хм..."
            m "Подойди ближе, девочка, дай лучше рассмотреть их..."
            hide screen bld1
            with d3
            show screen blkfade #Completely black screen.
            with Dissolve(1)
            pause.5
            ">Гермиона медленно подходит к вам."
            hide screen hermione_04 #Stands with tits out.
            hide screen genie
            show screen ctc
            show screen genie_and_tits_01
            with d1
            hide screen blkfade
            with d5
            pause
            show screen bld1
            with d3
            m "Очень хорошо..."
            show screen blktone 
            with d3
            $herView.hideQQ()
            
            

            # add tits pose!
            call addTitsPose
            
            $herView.showQQ( "body_84.png", pos )
            #$ only_upper = True #No lower body displayed. 
            pause
            her "...................................."
            play music "music/(Orchestral) Playful Tension by Shadow16nh.mp3" fadein 1 fadeout 1 # SEX THEME.
    


    menu:
        "\"Солгать. Схватить за сиськи!\"":
            if whoring >= 6 and whoring <= 8: # LEVEL 03 # <=================================================================================== FIRST EVENT. HERMIONE OUTRAGED.
                $herView.hideQQ()
                show screen blkfade
                with d3
                ">Вы протягиваете руки и хватаете грудь Гермионы..."
                $her_head_state = 7
                her_head_main "Профессор, что вы делаете?"
                hide screen blkfade
                hide screen blktone8
                hide screen blktone
                show screen chair_02 #Genie's chair.
                hide screen bld1
                show screen groping_naked_tits
                with fade
                pause
                show screen bld1
                with d3
                
                m "Расслабься, девочка. Просто стой!"
                m "Oх... Какие же у тебя классные сиськи..."
                play music "music/Chipper Doodle v2.mp3" fadein 1 fadeout 1 # HERMIONE'S THEME.
                $her_head_state = 13
                her_head_main "Нет, сэр, пожалуйста! Вы не должны..."
                m "Это не займет много времени, просто стой."
                $her_head_state = 24
                her_head_main "Сэр, Я не соглашалась на это!"
                with hpunch
                $her_head_state = 23
                her_head_main "Вы должны отпустите меня сейчас же!!!"
                show screen blkfade
                with d5
                ">Гермиона отстраняется от вас и спешно прикрывается."
                $her_head_state = 19
                her_head_main "Думаю, я лучше пойду..."
                hide screen blkfade
                hide screen chair_02 #Genie's chair.
                hide screen groping_naked_tits
                hide screen bld1
                show screen genie
                $ hermione_chibi_xpos = 400 #Near the desk.
                show screen hermione_02 #Hermione stands still.
                with d5
                pause
                show screen bld1
                m "Вали, девочка. Ты не получишь свою оплату..."
                her_head_main "Но я показала свои..."
                $her_head_state = 24
                her_head_main "И вы трогали меня..."
                $her_head_state = 23
                her_head_main "И я ничего не получу?"
                m "Вы провалились, Мисс Грейнджер..."
                $her_head_state = 19
                her_head_main "Гр.................."
                her_head_main "{size=-5}(Гори в аду, ты, ущербный старый---{/size}"
                $ mad += 22
                call music_block
                jump loadState_and_could_not_flirt
            elif whoring >= 9 and whoring <= 11: # LEVEL 04 # <=================================================================================== SECOND EVENT. A BIT ANGRY.
                $herView.hideQQ()
                $ only_upper = False #No lower body displayed. 
                show screen blkfade
                with d3
                ">Вы протягиваете свои руки и хватаете сиськи Гермионы..."
                $her_head_state = 7
                her_head_main "Профессор, что вы делаете?"
                hide screen blkfade
                hide screen blktone8
                hide screen blktone
                show screen chair_02 #Genie's chair.
                hide screen bld1
                show screen groping_naked_tits
                with fade
                pause
                show screen bld1
                with d3
                m "Расслабься, девочка. Просто стой!"
                $her_head_state = 4
                her_head_main "Я не соглашалась на это, сэр..."
                her_head_main "Я не думаю, что вы должны..."
                m "Тебе не нравиться...?"
                $her_head_state = 12
                her_head_main "Что?"
                m "Тебе не нравиться, как я играю и сжимаю твои сиськи?"
                her_head_main "..............."
                m "Признайся, тебе это приятно..."
                her_head_main "{size=-5}(Так странно видеть мои сиськи у кого-то в руках...){/size}"
                $her_head_state = 13
                her_head_main "сэр, Я позволяю вам делать это со мной, чтобы помочь моему факультету, ничего более!"
                play music "music/Chipper Doodle v2.mp3" fadein 1 fadeout 1 # HERMIONE'S THEME.
                $her_head_state = 4
                her_head_main "Пожалуйста, отпустите меня!"
                show screen blkfade
                with d5
                ">Гермиона отстраняется от вас и спешно прикрывается."
                her_head_main "Вы обещали не трогать, профессор..."
                m "Так сложно удержаться..."
                hide screen blkfade
                hide screen chair_02 #Genie's chair.
                hide screen groping_naked_tits
                hide screen bld1
                show screen genie
                $ hermione_chibi_xpos = 400 #Near the desk.
                show screen hermione_02 #Hermione stands still.
                with d5
                pause
                show screen bld1
                $her_head_state = 1
                her_head_main "............."
                $her_head_state = 9
                her_head_main "Могу я получить свою оплату?"
                m "Конечно..."
                $ mad += 9
            elif whoring >= 12: # LEVEL 05 # <=================================================================================== THIRD EVENT. ENJOYS A LITTLE.
                $herView.hideQQ()
                show screen blkfade
                with d3
                ">Вы протягиваете свои руки и хватаете грудь Гермионы..."
                $her_head_state = 7
                her_head_main "Профессор, что вы делаете?"
                hide screen blkfade
                hide screen blktone8
                hide screen blktone
                show screen chair_02 #Genie's chair.
                hide screen bld1
                show screen groping_naked_tits
                with fade
                pause
                show screen bld1
                with d3
                m "Расслабься, девочка. Просто стой!"
                $her_head_state = 12
                her_head_main "Но..."
                $her_head_state = 13
                her_head_main "ах...{image=textheart.png}"
                $her_head_state = 12
                her_head_main " Я не соглашалась на это..."
                m "Но тебе это нравиться, не так ли?"
                $her_head_state = 13
                her_head_main "Несовсем, сэр!{image=textheart.png}"
                show screen blktone
                with d3
                ">Вы несколько раз сжимаете её сиськи..."
                hide screen blktone
                with d3
                $her_head_state = 15
                her_head_main "Сэр, вы обещали не трогать..."
                m "Я знаю, знаю... Но так трудно удержаться..."
                $her_head_state = 20
                her_head_main "................."
                $her_head_state = 6
                her_head_main "....................aх...{image=textheart.png}"
                her_head_main "Cэр, вы должны остановиться..."
                m "Еще чуть-чуть..."
                show screen blktone8
                with d3
                ">Вы продолжаете мять её сиськи..."
                hide screen blktone8
                with d3
                $her_head_state = 37
                her_head_main "сэр... остановитесь..."
                m "Почему? Потому что тебе это очень нравиться?"
                $her_head_state = 18
                her_head_main "Нет, это не так..."
                $her_head_state = 17
                her_head_main "Я считаю..."
                show screen blktone8
                with d3
                ">Вы тянете сиськи в противоположных направлениях, а затем стягиваете их вместе..."
                hide screen blktone8
                with d3
                $her_head_state = 38
                her_head_main "Aх...{image=textheart.png} сэр, я действительно должна идти..."
                if daytime:
                    $her_head_state = 17
                    her_head_main "Хорошо... скоро начнуться уроки..."
                else:
                    her_head_main "Уже поздно..."
                m "Ну, хорошо..."
                show screen blkfade
                with d5
                ">Вы отпускаете ее грудь..."
                ">Гермиона прикрывается..."
                play music "music/Chipper Doodle v2.mp3" fadein 1 fadeout 1 # HERMIONE'S THEME.
                $her_head_state = 25
                her_head_main "Пожалуйста, не думайте, что я забыла ваше обещание, сэр."
                m "Точно..."
                hide screen blkfade
                hide screen chair_02 #Genie's chair.
                hide screen groping_naked_tits
                hide screen bld1
                show screen genie
                $ hermione_chibi_xpos = 400 #Near the desk.
                show screen hermione_02 #Hermione stands still.
                with d5
                pause
                show screen bld1
                $her_head_state = 35
                her_head_main "Могу я получить свои очки?"
                $ mad +=7
   
        "\"Сдержать обещание. Просто смотреть.\"":
            ">Вы долго разглядываете грудь Гермионы..."
            if whoring >= 6 and whoring <= 8: # LEVEL 03 # <=================================================================================== FIRST EVENT.
                pause
                menu:
                    "- Одобрительно кивнуть -":
                        ">Вы смотрите на ее сиськи и киваете в знак одобрения..."
                        her "......................"
                    "- Отрицательно трясти головой -":
                        $ mad += 3
                        ">Вы смотрите на сиськи девушки, а затем в разочаровании трясете головой..."
                        her ".....................?"
            elif whoring >= 9 and whoring <= 11: # LEVEL 04 # <=================================================================================== SECOND EVENT.
                pause
                menu:
                    "\"У тебя отличные сиськи.\"":
                        $herView.hideshowQQ( "body_83.png", pos )
                        pause
                        her "Спасибо--"
                        $herView.hideshowQQ( "body_82.png", pos )
                        play music "music/Chipper Doodle v2.mp3" fadein 1 fadeout 1 # HERMIONE'S THEME.
                        her "..........."
                        $herView.hideshowQQ( "body_81.png", pos )
                        her "В последнее время вы частенько говорите разные неуместные вещи, профессор."
                        
                    "\"Хм... Видел и лучше.\"":
                        $ mad += 7
                        $herView.hideshowQQ( "body_83.png", pos );
                        her "Арх..."
                        her "Теперь мы закончили?"

            elif whoring >= 12: # LEVEL 05 # <=================================================================================== THIRD EVENT.
                pause
                menu:
                    "\"У тебя отличные сиськи, девочка.\"":
                        $herView.hideshowQQ( "body_82.png", pos )
                        her "Вы правда так думаете, профессор?"
                        $herView.hideshowQQ( "body_84.png", pos )
                        her "Мне приятно, что вам они нравятся, сэр..."
                    "\"Ну, так себе сиськи...\"":
                        $herView.hideshowQQ( "body_82.png", pos )
                        her "А?"
                        her "Это значит, что они вам не нравятся, сэр?"
                        $herView.hideshowQQ( "body_85.png", pos )
                        her "Мне жаль..."
            ">Вы пялитесь на ее грудь еще какое-то время..."
            pause
            m "Ладно, ты можешь прикрыться, девочка..."
            her "............."
            $herView.hideQQ()
            
            show screen blkfade
            with d3
            ">Гермиона прикрывается..."
            hide screen chair_02 #Genie's chair.
            hide screen genie_and_tits_01
            hide screen bld1
            hide screen blktone
            show screen genie
            show screen bld1
            $ hermione_chibi_xpos = 400 #Near the desk.
            show screen hermione_02 #Hermione stands still.
            with d5

        "\"Начать дрочить.\"":
            if whoring >= 6 and whoring <= 8: # LEVEL 03 # <=================================================================================== FIRST EVENT.
                $ mad += 2
                $herView.hideQQ()
                ">Вы взяли свой член и начали дрочить..."
                show screen blkfade
                hide screen bld1
                with d3
                play music "music/Chipper Doodle v2.mp3" fadein 1 fadeout 1 # HERMIONE'S THEME.
                $her_head_state = 30
                her_head_main "Профессор?!!"
                m "Просто стой, девочка..."
                hide screen hermione_walk_01
                hide screen genie
                hide screen bld1
                show screen chair_02 #Genie's chair.
                hide screen blkfade
                hide screen blktone
                show screen jerking_off_01
                with d5
                pause
                
                show screen bld1
                with d3
                ">Вы пялитись на сиськи Гермионы голодными глазами..."
                $her_head_state = 13
                her_head_main "Профессор, что вы...?"
                ">Вы продолжаете дрочить свой член..."
                $her_head_state = 12
                her_head_main "Профессор, нет..."
                her_head_main "Вы должны... Убрать это..."
                m "Хватит трепетать девочка. Я же не трогаю тебя?"
                $her_head_state = 19
                her_head_main "Но..."
                $her_head_state = 20
                her_head_main "Но я не соглашалась на это!"
                $her_head_state = 19
                her_head_main "Я..."
                her_head_main "Я думаю, мне лучше уйти!"
                menu:
                    "\"Уйдешь сейчас - не получишь очков!\"":
                        $her_head_state = 21
                        her_head_main "После {size=+5}этого{/size}? Вы издеваетесь, сэр?"
                        her_head_main "Я показала свои..."
                        $her_head_state = 25
                        her_head_main ".........."
                        $her_head_state = 24
                        her_head_main "Я не собираюсь показывать вам больше, профессор!"
                        show screen blkfade
                        with d3
                        ">Гермиона оттолкнула вас и прикрылась..."
                        g4 "Не смей покидать меня в таком состоянии, девочка!"
                        $her_head_state = 10
                        her_head_main "Ноги моей больше не будет в вашем кабинете, сэр!"
                        g4 "Да ладно уже, скажи что нибудь грязное! Я почти кончил!"
                        $her_head_state = 27
                        her_head_main "Вы ужасный человек, сэр..."
                        $ mad += 30
                        call music_block
                        jump loadState_and_could_not_flirt
                    "\"Ладно, ладно. На сегодня достаточно.\"":
                        $ mad +=9
                        pass
                    "- Дрочить быстрее -":
                        $ mad += 35
                        ">Вы начали дрочить очень быстро!"
                        $her_head_state = 23
                        her_head_main "Нет, профессор, стойте!"
                        ">Вы дрочите еще быстрее!"
                        $her_head_state = 25
                        her_head_main "Профессор, думаю, я пойду..."
                        g4 "Нет, подожди, я почти кончил!"
                        show screen blkfade
                        with d3
                        $her_head_state = 10
                        her_head_main "Иу! Профессор!"
                        her_head_main "Я ухожу!"
                        call music_block
                        jump loadState_and_could_not_flirt
            elif whoring >= 9 and whoring <= 11: # LEVEL 04 # <=================================================================================== SECOND EVENT.
                $herView.hideQQ()
                ">Вы взяли свой член и начали дрочить..."
                show screen blkfade
                hide screen bld1
                with d3
                $her_head_state = 30
                her_head_main "Профессор?"
                ">Вы смотрите на сиськи Гермионы с голодными глазами..."
                hide screen hermione_walk_01
                hide screen genie
                hide screen bld1
                show screen chair_02 #Genie's chair.
                hide screen blkfade
                hide screen blktone
                show screen jerking_off_01
                with d5
                pause
                
                show screen bld1
                with d3
                $her_head_state = 13
                her_head_main "Профессор, я не соглашалась на это..."
                m "Чего ты жалуешься, девочка?"
                m "Я не трогаю тебя..."
                her_head_main "Да, но вы трогаете себя, сэр."
                ">Вы подняли темп..."
                m "Просто стой, девочка."
                m "Скоро я закончу."
                her_head_main ".................."
                $her_head_state = 12
                her_head_main "(Он такой большой...)"
                m "Да, вот так..."
                m "Да, с твоими голыми сиськами..."
                her_head_main ".............."
                $her_head_state = 17
                her_head_main "ну, так и быть..."
                her_head_main "Вы можете трогать себя, сэр..."
                $her_head_state = 1
                her_head_main "Но вы должны обещать мне не..."
                $her_head_state = 5
                her_head_main "Не... eм..."
                $her_head_state = 4
                her_head_main "Не закончить на меня..."
                $her_head_state = 8
                her_head_main "Не передо мной, сэр..."
                m "Хорошо..."
                m "Ах, ты, маленькая шлюшка. Ты дикая шлюшка!"
                $her_head_state = 19
                her_head_main "......................."
                "Вы начали дрочить свой член еще быстрее..."
                g4 "Да, ты знаешь что это! Да!"
                her_head_main "................"
                show screen blkfade 
                with d3
                ">Вы собираетесь кончить..."
                menu:
                    "- Сдержаться, как и обещали -":
                        g4 "Ох, отлично..."
                        g4 "Я думаю, стоит остановиться..."
                        $her_head_state = 15
                        her_head_main "..............."
                        ">Гермиона прикрыла груди..."
                    "- Кончить -":
                        #play music "music/Chipper Doodle v2.mp3" fadein 1 fadeout 1 # HERMIONE'S THEME.
                        g4 "Aргх! Ты шлюшка!"
                        $her_head_state = 21
                        her_head_main "Профе-- ??"
                        show screen white 
                        pause.1
                        hide screen white
                        pause.2
                        show screen white 
                        pause .1
                        hide screen white
                        with hpunch
                        g4 "Aргх! ДА!"
                        hide screen bld1
                        with d3
                        $ no_blinking = True #When True - blinking animation is not displayed. 
                        show screen jerking_off_cum
                        hide screen blkfade
                        hide screen bld1
                        with d3
                        pause
                        show screen bld1
                        with d3
                        $her_head_state = 23
                        her_head_main "Профессор, нет! Вы обещали!"
                        g4 "Ох, это здорово, да..."
                        $ no_blinking = False #When True - blinking animation is not displayed. 
                        hide screen jerking_off_cum
                        with d3
                        $her_head_state = 10
                        her_head_main "Профессор, как вы могли...?"
                        m "Ох, это было очень классно..."
                        show screen blktone8
                        with d3

                        #add sperm on tits
                        call addSperm

                        $herView.showQQ( "body_85.png", pos )
                        pause
                        her "Моя форма..."
                        her "Испорчена...."
                        m "Не беспокойся, я дам тебе очки факультета, девочка."
                        m "Ты сделала мне хорошо."
                        her "................"
                        her "Мне нужно очистить себя..."
                        $herView.hideQQ()
                        show screen blkfade
                        with d3
                        show screen genie
                        hide screen jerking_off_01
                        hide screen chair_02
                        show screen hermione_02
                        with d3

                        hide screen blkfade
                        with d5
                        
                        call delSperm

                        
                        
                        #here we'll remove pose and add aftersperm effect
                        call addAfterSperm

                        $herView.showQQ( "body_47.png", pos )
                        pause
                        #play music "music/Chipper Doodle v2.mp3" fadein 1 fadeout 1 # HERMIONE'S THEME.
                        her "Как вы могли сделать это, сэр?!"
                        her "Вы дали слово!"
                        $herView.hideQQ()
                        $ mad += 45
            elif whoring >= 12: # LEVEL 05 # <=================================================================================== THIRD EVENT.
                $herView.hideQQ()
                ">Вы берете свой член и начинаете дрочить..."
                show screen blkfade
                hide screen bld1
                with d3
                $her_head_state = 6
                her_head_main "Профессор?"
                ">Вы смотрите на сиськи Гермионы с голодными глазами..."
                hide screen hermione_walk_01
                hide screen genie
                hide screen bld1
                show screen chair_02 #Genie's chair.
                hide screen blkfade
                hide screen blktone
                show screen jerking_off_01
                with d5
                pause
                
                show screen bld1
                with d3
                $her_head_state = 13
                her_head_main "Профессор, я  не соглашалась на это..."
                m "Чего ты жалуешься, девочка?"
                m "Я тебя не трогаю..."
                her_head_main "Да, но вы... трогаете себя, сэр."
                #">You pick up the pace..."
                m "Просто стой, сука."
                m "Я скоро кончу."
                her_head_main ".................."
                m "Да... да, вот так..."
                m "Да, твои сисечки..."
                $her_head_state = 12
                her_head_main ".............."
                $her_head_state = 17
                her_head_main "Ну, так и быть..."
                $her_head_state = 1
                her_head_main "Но вы должны мне пообещать..."
                $her_head_state = 5
                her_head_main "Не... Эм..."
                $her_head_state = 4
                her_head_main "Не кончать..."
                her_head_main "Не передо мной, сэр..."
                m "Хорошо..."
                m "Ах, ты, маленькая шлюшка. Ты грязная шлюшка!"
                $her_head_state = 12
                her_head_main "......................."
                ">Вы начинаете дрочить еще быстрее..."
                g4 "Да, я знаю, ты хочешь этого! Да!"
                her_head_main "................"
                show screen blkfade 
                with d3
                 # SAME AS PREVIOUS EVENT^^^
                g4 "Aргх! (Я кончаю!)"
                menu:
                    "- Сдержать обещание -":
                        g4 "Ох, ладно..."
                        g4 "Думаю, лучше остановиться..."
                        her_head_main "..............."
                        her_head_main "Эм... Я читала, что это плохо для мужчин, сэр..."
                        m "А?"
                        $her_head_state = 13
                        her_head_main "Это плохо для вашего здоровья - сдерживать себя..."
                        $her_head_state = 12
                        her_head_main "Eм..."
                        $her_head_state = 14
                        her_head_main "Если вы хотите, вы можете--"
                        g4 "Aргх! Ты шлюшка!"
                        $her_head_state = 7
                        her_head_main "???"
                        show screen white 
                        pause.1
                        hide screen white
                        pause.2
                        show screen white 
                        pause .1
                        hide screen white
                        with hpunch
                        g4 "Aргх! ДА!"
                        hide screen bld1
                        with d3
                        $ no_blinking = True #When True - blinking animation is not displayed. 
                        show screen jerking_off_cum
                        hide screen blkfade
                        hide screen bld1
                        with d3
                        pause
                        show screen bld1
                        with d3
                        $her_head_state = 9
                        her_head_main "Профессор, я не имела в виду, что вы можете ... кончить на меня, сэр..."
                        g4 "Ох, это здорово, да..."
                        $ no_blinking = False #When True - blinking animation is not displayed. 
                        hide screen jerking_off_cum
                        with d3
                        $her_head_state = 18
                        her_head_main "Ну, что сделано, то сделано, я полагаю..."
                        m "Ох, это было очень классно..."
                        show screen blktone8
                        with d3

                        call addSperm

                        $herView.showQQ( "body_85.png", pos )
                        pause
                        her "Моя форма испачкана..."
                        m "Не беспокойся, я дам тебе очки для факультета, девочка."
                        m "Ты сделала мне хорошо."
                        $herView.hideshowQQ( "body_84.png", pos )
                        her "Спасибо, сэр."
                        $herView.hideshowQQ( "body_83.png", pos )
                        her "Теперь мне нужно очистить себя..."
                        pause
                        $herView.hideQQ()
                        show screen blkfade
                        with d3
                        show screen genie
                        hide screen jerking_off_01
                        hide screen chair_02
                        show screen hermione_02
                        hide screen blkfade
                        with d5

                        call delSperm
                        
                        #here we remove pose and add aftersperm effect
                        call addAfterSperm

                        $herView.showQ( "body_45.png", pos )
                        pause
                        her "Ну, это следует сделать сейчас..."
                        $herView.hideQQ()
                    "- Кончить -":
                        g4 "Aргх! Ты шлюшка!"
                        $her_head_state = 7
                        her_head_main "???"
                        show screen white 
                        pause.1
                        hide screen white
                        pause.2
                        show screen white 
                        pause .1
                        hide screen white
                        with hpunch
                        g4 "Aргх! Да!"
                        hide screen bld1
                        with d3
                        $ no_blinking = True #When True - blinking animation is not displayed. 
                        show screen jerking_off_cum
                        hide screen blkfade
                        hide screen bld1
                        with d3
                        pause
                        show screen bld1
                        with d3
                        $her_head_state = 13
                        her_head_main "Ах...{image=textheart.png} Так горячо...{image=textheart.png}"
                        $her_head_state = 9
                        her_head_main "Профессор, вы обещали..."
                        g4 "Ох, это здорово, да..."
                        $ no_blinking = False #When True - blinking animation is not displayed. 
                        hide screen jerking_off_cum
                        with d3
                        $her_head_state = 15
                        her_head_main "Ну, что сделано, то сделано, я полагаю..."
                        m "Ох, это было довольно классно.."
                        show screen blktone8
                        with d3

                        call addSperm

                        $herView.showQQ( "body_85.png", pos )
                        pause
                        her "Моя форма испачкана..."
                        m "Не беспокойся, я дам тебе очки факультета, девочка."
                        m "Ты сделала мне хорошо."
                        $herView.hideshowQQ( "body_84.png", pos )
                        her "Спасибо, сэр."
                        $herView.hideshowQQ( "body_83.png", pos )
                        her "Теперь я должна себя очистить..."
                        pause
                        $herView.hideQQ()
                        show screen blkfade
                        with d3
                        show screen genie
                        hide screen jerking_off_01
                        hide screen chair_02
                        show screen hermione_02
                        hide screen blkfade
                        with d5

                        call delSperm

                        
                        # remove pose and add aftersperm
                        call addAfterSperm

                        $herView.showQ( "body_45.png", pos )
                        pause
                        her "Ну, это следует сделать сейчас..."
                        $herView.hideQQ()
                        

    
    hide screen jerking_off_01                   
    hide screen blktone8
    hide screen ctc
    hide screen bld1
    hide screen groping_01
    hide screen groping_02
    show screen hermione_02
    show screen genie
    with fade
    
    hide screen blkfade
    with d3

    $ gryffindor +=current_payout
    m " \"Гриффиндор\" получает [current_payout] очков!"
    stop music fadeout 10.0

   
   
    $ hermione_chibi_xpos = 400 #Near the desk.
    show screen hermione_02 #Hermione stands still.
    show screen bld1
    hide screen blkfade
    with Dissolve(1)
    
    # remove pose here, because sometimes we need to keep added items even here ( like sperm )
    $herView.data().delPose()

    $ pos = POS_370
    $herView.showQQ( "body_29.png", pos )
    her ".................."
    her "Спасибо, сэр..."
    if daytime:
        her "Теперь, если Вы не возражаете, я пойду. Мои занятия начинаются."
    else:
        her" Я лучше пойду сейчас. Пока не слишком поздно..."
    
#    if whoring >= 6 and whoring <= 8:
#        $ level = "03"
#        $ new_request_08_01 = True # HEARTS.
#    if whoring >= 9 and whoring <= 11:
#        $ level = "04"
#        $ new_request_08_02 = True # HEARTS.
#    if whoring >= 12:
#        $ level = "05"
#        $ new_request_08_03 = True # HEARTS.

    $SetHearts(GetStage(whoring, 6, 3, 4))


    hide screen bld1
    $herView.hideQ( Dissolve(.3) )
    $ walk_xpos=400 #Animation of walking chibi. (From)
    $ walk_xpos2=610 #Coordinates of it's movement. (To)
    $ hermione_speed = 02.0 #The speed of moving the walking animation across the screen.
    show screen hermione_walk_01_f 
    pause 2
    hide screen hermione_walk_01_f 
    $ hermione_chibi_xpos = 610 #Near the desk.
    show screen hermione_01_f #Hermione stands still.
    with Dissolve(.3)    
        
    if whoring >= 6 and whoring <= 8: # LEVEL 03 # <=================================================================================== FIRST EVENT.    
        $her_head_state = 12
        her_head_main "(Как унизительно... кем я стала...?)"
        $ renpy.play('sounds/door.mp3') #Sound of a door opening.
        hide screen hermione_01_f #Hermione stands still.
        with Dissolve(.3)
    elif whoring >= 9 and whoring <= 11: # LEVEL 04 # <=================================================================================== SECOND EVENT.
        her_head_main "........................"
        $ renpy.play('sounds/door.mp3') #Sound of a door opening.
        hide screen hermione_01_f #Hermione stands still.
        with Dissolve(.3)  
    elif whoring >= 12: # LEVEL 05 # <=================================================================================== THIRD EVENT.
        $her_head_state = 6
        her_head_main "{size=-5}(Как унизительно...){/size}"
        $her_head_state = 24
        her_head_main "{size=-5}(Нет, Гермиона, ты глупая девочка!){/size}"
        her_head_main "{size=-5}(Мы делаем это, чтобы защитить честь нашего факультета!){/size}"
        $her_head_state = 19
        her_head_main "................................."
        $ renpy.play('sounds/door.mp3') #Sound of a door opening.
        hide screen hermione_01_f #Hermione stands still.
        with Dissolve(.3)  
    else:
        $ renpy.play('sounds/door.mp3') #Sound of a door opening.
        hide screen hermione_01_f #Hermione stands still.
        with Dissolve(.3)  


        
    if whoring <= 8:
        $ whoring +=1
        

#    $ request_08_points += 1
        

    # load from pose with tits and that sperm!
    $herView.data().loadState()
    
    jump finish_daytime_event



label addTitsPose:
    # add tits pose!
    $herView.data().addPose( CharacterExItemPoseShowTits( herView.mPoseFolder, 'pose_dress_up.png', G_Z_POSE ) )
    return
    
label addSperm:
    # add sperm item!
    $herView.data().addItem( 'sperm', CharacterExItem( herView.mMiscFolder, 'sperm_00.png', G_Z_FACE + 1 ) )
    return

label delSperm:
    # add sperm item!
    $herView.data().delItem( 'sperm' )
    return
    
label addAfterSperm:
    # del pose and add aftersperm
    $herView.data().delPose()
    $herView.data().addItem( 'sperm_after', CharacterExItem( herView.mMiscFolder, 'sperm_00_after.png', G_Z_FACE + 1 ) )
    return
    
label loadState_and_could_not_flirt:
    $herView.data().loadState()
    call could_not_flirt
    jump finish_daytime_event

