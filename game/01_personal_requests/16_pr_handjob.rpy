#############################################################################################################################
### LEVEL 05 ################################################################################################################   
###################REQUEST_16 (Level 05) (HANDJOB) (Day/Night) #####################################################
label new_request_16: #LV.5 (Whoring = 12 - 14)
    $herView.hideQQ()
    if IsFirstRun():
#    if request_16_points == 0:
        m "{size=-4}(Попросить ее вздрочнуть мне?){/size}"
    else:
        m "{size=-4}(Попросить ее еще раз подрочить мне?){/size}"
    $ menu_x = 0.5 #Default position of the menu (0.5). Version B is $ menu_x = 0.2
    menu:
        "\"(Да, давай попробуем!)\"":
            show screen blktone
            with d3
            pass
        "\"(Не сейчас.)\"":
            $event.NotFinished()
            jump new_personal_request
            
    
    $ pos = POS_140
    $herView.data().saveState()

    $ current_payout = 45 #Used when haggling about price of th favor.  
#    if request_16_points == 0: # FIRST EVENT <============================================================== EVENT 01
    if IsFirstRun(): # FIRST EVENT <============================================================== EVENT 01
        m "Мисс Грейнджер."
        $herView.hideshowQQ( "body_01.png", pos )
        her "Да, профессор?"
        m "Ты знаешь что такое \"работа ручками\"?"
        if hermi.whoring <=11:
            jump too_much
        $herView.hideshowQQ( "body_79.png", pos )
        her "А что?"
        m "Я хочу, чтобы ты сделала это мне..."
        $herView.hideshowQQ( "body_47.png", pos )
        her "Профессор!"
        m "Просто одна услуга. Ничего страшного, да?"
        $herView.hideshowQQ( "body_66.png", pos )
        her "......"
        $herView.hideshowQQ( "body_34.png", pos )
        her "{size=-7}Я хочу 100 очков за это...{/size}"
        m "А? Что это было?"
        $herView.hideshowQQ( "body_32.png", pos )
        her "Я хочу 100 очков за это!!!"
        m "100 очков, да?"
        m "И ты подрочишь мне и все такое, правильно?"
        $herView.hideshowQQ( "body_66.png", pos )
        her "{size=-7}Да...{/size}"
        m "Прости, я не расслышал..."
        $herView.hideshowQQ( "body_32.png", pos )
        her "Да, я сказала да! Я подрочу вам, сэр!"
        label back_to_handjob_choices:
        menu:
            m "..."
            "\"Ты получишь 15 очков.\"":
                $ hermi.liking -=7
                $herView.hideshowQQ( "body_69.png", pos )
                her "За 15 очков вы сможете немного поприставать ко мне, но не более, сэр."
                her "Я не продешевлю и не стану дрочить вам за 15 очков."
                her "Это оскорбительно, сэр."
                jump back_to_handjob_choices
            "\"Ты получишь 45 очков.\"":
                $herView.hideshowQQ( "body_69.png", pos )
                her "....."
                $herView.hideshowQQ( "body_87.png", pos )
                her "45 очков...?"
                her "Это может серьёзно помочь \"Гриффиндору\"!"
                m "Это значит \"Да\"?"
                $herView.hideshowQQ( "body_79.png", pos )
                her "Да! Это значит да, сэр."
                m "Отлично!"
            "\"Ты получишь 100 очков.\"":
                play music "music/Chipper Doodle v2.mp3" fadein 1 fadeout 1 # HERMIONE'S THEME.
                $ current_payout = 100 #Used when haggling about price of th favor.
                $ hermi.liking = 0
                $herView.hideshowQQ( "body_72.png", pos )
                her "100 очков?!"
                her "Это поможет вернуть \"Гриффиндор\" в лидеры!"
                m "Это значит \"Да\"?"
                $herView.hideshowQQ( "body_75.png", pos )
                her "Конечно!"
                $herView.hideshowQQ( "body_80.png", pos )
                her "Если это принесет \"Гриффиндору\" 100 очков, то я согласна прикасаться... к вашей штуке."
        # GENIE STANDS WITH HIS COCK OUT
       
        play music "music/(Orchestral) Playful Tension by Shadow16nh.mp3" fadein 1 fadeout 1 # SEX THEME.
        $herView.hideQ()
        hide screen genie
        $ genie_chibi_xpos = 5 #-185 behind the desk.
        $ genie_chibi_ypos = 10
        $ g_c_u_pic = "jerking_off_02_ani"
        show screen chair_02
        show screen g_c_u
        show screen desk_02

        hide screen blkfade
        hide screen blktone
        hide screen bld1
        show screen ctc
        with fade
        pause
        show screen bld1
        with d3
        $ posHead = gMakePos( 390, 235 )        
        $herViewHead.showQ( "body_31.png", posHead )
        her "..........."
        $herViewHead.hideQ()
        m "Начинай, как будешь готова, девочка."
        $herViewHead.showQ( "body_34.png", posHead )
        her "Хорошо..."
        $herViewHead.hideQ()
        hide screen bld1
        with d3
        $ walk_xpos=400 #Animation of walking chibi. (From)
        $ walk_xpos2=280 #Coordinates of it's movement. (To)
        $ hermione_speed = 03.0 #The speed of moving the walking animation across the screen.
        show screen hermione_walk_01 
        pause.1
        show screen blkfade
        with Dissolve(1)
        pause.3
        label event_01_round_02:
        ">Гермиона берет своими тонкими ручками ваш член..."
        m "Отлично. Теперь дрочи его."
        $herViewHead.showQ( "body_34.png", posHead )
        her "Ага..."
        $herViewHead.hideQ()
        #Stroking the cock.
        $ genie_chibi_xpos = 60 #-185 behind the desk.
        $ genie_chibi_ypos = 10
        $ g_c_u_pic = "handjob_ani"
        hide screen hermione_walk_01 
        hide screen blkfade
        with d3
        show screen ctc
        pause
        play music "music/(Orchestral) Playful Tension by Shadow16nh.mp3" fadein 1 fadeout 1 # SEX THEME.
        hide screen ctc
        show screen bld1
        with d3
        g9 "Отлично..."
#        if request_16_points == 0:
        if IsFirstRun():
            $herViewHead.showQ( "body_48.png", posHead )
            her "!!!"
            her "Как насчет кончить, сэр?!"
            $herViewHead.hideQ()
            m "Кончить?"
            m "Не будь глупа, мы только начали."
            $herViewHead.showQ( "body_34.png", posHead )
            her "Ох..."
            her "......"
            $herViewHead.showQ( "body_44.png", posHead )
            her2 "Вы предупредите меня, сэр?"
            $herViewHead.hideQ()
        else:
            $herViewHead.showQ( "body_34.png", posHead )
            her "Сэр...?"
            $herViewHead.hideQ()
            m "Что такое?"
            $herViewHead.showQ( "body_34.png", posHead )
            her2 "Вы могли бы предупредить меня... э-эм... когда вы..."
            $herViewHead.hideQ()
        $ d_flag_01 = False #If TRUE Genie promised to warn her.
        menu:
            m "..."
            "\"Конечно я скажу тебе, когда буду кончать.\"":
                $ d_flag_01 = True #If TRUE Genie promised to warn her.
                $herViewHead.showQ( "body_33.png", posHead )
                her "Спасибо, сэр."
                $herViewHead.hideQ()
            "\"Я и сам не всегда уверен...\"":
                $herViewHead.showQ( "body_31.png", posHead )
                her "Правда? Но я думала..."
                $herViewHead.showQ( "body_33.png", posHead )
                her "Ну, тогда ладно..."
                $herViewHead.hideQ()
        $herViewHead.showQ( "body_31.png", posHead )
        her "........"
        $herViewHead.hideQ()
        m "............."
        $herViewHead.showQ( "body_33.png", posHead )
        her "............."
        $herViewHead.showQ( "body_33.png", posHead )
        her "Э-э... сэр?"
        $herViewHead.hideQ()
        m "Да, что такое?"
        $herViewHead.showQ( "body_31.png", posHead )
        her "Как долго мне придется это делать?"
        $herViewHead.hideQ()
        m "В смысле?"
        if daytime:
            $herViewHead.showQ( "body_44.png", posHead )
            her2 "Просто, мои занятия вот-вот начнутся..."
        else: 
            $herViewHead.showQ( "body_44.png", posHead )
            her2 "Ну, мне нужно заниматься, и хотелось бы закончить это побыстрее..."
            her2 "Завтра рано вставать, а уже довольно поздно..."
        $herViewHead.hideQ()
        m "Вам нужны очки или нет?"
        $herViewHead.showQ( "body_74.png", posHead )
        her "Да, сэр! Мне жаль..."
        her "Просто я никогда не дрочила мужчине..."
        $herViewHead.hideQ()
        m "Ну, есть кое-что, чтобы ускорить процесс..."
        $herViewHead.showQ( "body_45.png", posHead )
        her "Правда? Что же это, сэр?"
        $herViewHead.hideQ()
        menu:
            m "..."
            "\"Скажи мне насколько ты распутная шлюха!\"":
                $herViewHead.showQ( "body_47.png", posHead )
                her "Что?"
                her "Но я не..."
                $herViewHead.hideQ()
                m "Не нужно быть честной, девочка."
                m "Просто сделай это."
                $herViewHead.showQ( "body_44.png", posHead )
                her "Правда?"
                $herViewHead.hideQ()
                m "Конечно. Мы немного повеселимся."
                $herViewHead.showQ( "body_87.png", posHead )
                her "Ну, раз так..."
                her "Я... я шлюха."
                $herViewHead.hideQ()
                m "Хех... великолепно. Продолжай."
                $herViewHead.showQ( "body_87.png", posHead )
                her "Я самая большая шлюха..."
                $herViewHead.hideQ()
                m "Да, именно."
                $herViewHead.showQ( "body_79.png", posHead )
                her "Я самая распутная шлюха во всей Англии!"
                her2 "Я пытаюсь казаться невинной, но на самом деле все, о чем я думаю - это члены!"
                $herViewHead.hideQ()
                m "Да, ты малолетняя шлюха!"
                $herViewHead.showQ( "body_69.png", posHead )
                her "Да! Я шлюха!"
                her "Я постоянно жажду членов!"
                $herViewHead.hideQ()
                m "Очень хорошо!"
                m "Но, как я уже сказал, не нужно быть честной."
                $herViewHead.showQ( "body_48.png", posHead )
                her "Что?"
                $herViewHead.showQ( "body_44.png", posHead )
                her "Сэр, все это неправда!"
                $herViewHead.hideQ()
                g9 "Хех... Я знаю. Я просто шучу."
                $herViewHead.showQ( "body_66.png", posHead )
                her "Сэр!"
                $herViewHead.hideQ()
                m "Ты все делаешь отлично. Продолжай!"
                $herViewHead.showQ( "body_87.png", posHead )
                her "....."
                her "Я обожаю члены..."
                $herViewHead.showQ( "body_88.png", posHead )
                her "И я люблю когда... меня шлепают..."
                her "И сперму..."
                her "Я люблю глотать сперму..."
                $herViewHead.showQ( "body_65.png", posHead )
                her "Я хочу, чтобы вы накормили меня спермой, сэр!"
                $herViewHead.hideQ()
                g4 "!!!"
                $herViewHead.showQ( "body_64.png", posHead )
                her2 "Или лучше, наполните меня ею, сэр!"
                hide screen ctc
                $herViewHead.hideQ()
                with hpunch
                g4 "{size=-4}(Я почти готов! Стоит ли мне ее предупредить?){/size}"
            
            "\"Высунь свой язык и смотри на меня!\"":
                $herViewHead.showQ( "body_45.png", posHead )
                her "Что?"
                $herViewHead.hideQ()
                m "Просто сделай это, шлюха."
                $herViewHead.showQ( "body_38.png", posHead )
                her "Вот так?"
                $herViewHead.hideQ()
                m "Да, отлично. Продолжай смотреть мне в глаза и дрочи."
                $herViewHead.showQ( "body_115.png", posHead )
                her "....................."
                $herViewHead.hideQ()
                m "Да... Отлично..."
                $herViewHead.showQ( "body_115.png", posHead )
                her "..........."
                her "..........."
                $herViewHead.showQ( "body_31.png", posHead )
                her2 "Я не могу так долго сидеть с открытым ртом, сэр. У меня потекут слюни..."
                $herViewHead.hideQ()
                m "Но я хочу, чтобы они потекли..."
                $herViewHead.showQ( "body_31.png", posHead )
                her "Что? Я буду выглядеть глупо!"
                $herViewHead.hideQ()
                m "Именно это мне и нужно, девочка!"
                $herViewHead.showQ( "body_29.png", posHead )
                her "......."
                $herViewHead.hideQ()
                m "Разве ты не хочешь, чтобы я кончил как можно быстрее?"
                $herViewHead.showQ( "body_33.png", posHead )
                her "............"
                $herViewHead.showQ( "body_115.png", posHead )
                her "А-ха....."
                $herViewHead.hideQ()
                m "Отлично."
                $herViewHead.showQ( "body_115.png", posHead )
                her ".............."
                $herViewHead.hideQ()
                m "Да, продолжай дрочить мой член."
                $herViewHead.showQ( "body_115.png", posHead )
                her ".................."
                $herViewHead.hideQ()
                g4 "Ох... Я хочу проскользнуть членом в твой влажный ротик!"
                $herViewHead.showQ( "body_40.png", posHead )
                her "................."
                $herViewHead.hideQ()
                m "Нет, смотри на меня!"
                $herViewHead.showQ( "body_115.png", posHead )
                her "....................."
                $herViewHead.hideQ()
                m "Да, маленькая шлюха!"
                $herViewHead.showQ( "body_116.png", posHead )
                her "......................"
                $herViewHead.hideQ()
                m "Я хочу кончить в этот ротик, да..."
                $herViewHead.showQ( "body_116.png", posHead )
                her "................"
                $herViewHead.hideQ()
                with hpunch
                g4 "{size=-4}(Я почти! Стоит мне предупредить ее?){/size}"

            "\"Поцелуй мой член!\"":
                $herViewHead.showQ( "body_47.png", posHead )
                her "Простите, что?"
                $herViewHead.hideQ()
                m "Ты верно услышала, просто поцелуй его своими губами."
                $herViewHead.showQ( "body_47.png", posHead )
                her "............."
                $herViewHead.showQ( "body_48.png", posHead )
                her "...губами?"
                $herViewHead.hideQ()
                m "Конечно... это сильно ускорит приближение кульминации."
                $herViewHead.showQ( "body_87.png", posHead )
                her "*вздох!*.............."
                her "Ну, я могла бы попробовать, наверное..."
                $herViewHead.hideQ()
                ">Гермиона нежно целует вашу головку."
                
                $ g_c_u_pic = "kiss_ani"
                $ renpy.play('sounds/kiss.mp3') 
                with kissiris
                pause
                show screen blkfade
                with d3
                $ g_c_u_pic = "handjob_ani"
                hide screen blkfade
                with d3

                $herViewHead.showQ( "body_87.png", posHead )
                her "Вот так?"
                $herViewHead.hideQ()
                m "Ничего страшного, правда?"
                $herViewHead.showQ( "body_44.png", posHead )
                her "Нет, кажется нет..."
                $herViewHead.hideQ()
                m "Можешь сделать это снова?"
                $herViewHead.showQ( "body_33.png", posHead )
                her "Вероятно..."
                $herViewHead.hideQ()
                m "Сделай это!"
                $herViewHead.showQ( "body_31.png", posHead )
                her "Ну, ладно..."
                $herViewHead.hideQ()
                ">Гермиона еще раз целует головку вашего члена..."
                $ g_c_u_pic = "kiss_ani"
                $ renpy.play('sounds/kiss.mp3') 
                with kissiris
                pause
                ">В этот раз поцелуй длится чуть дольше..."
                show screen blkfade
                with d3
                $ g_c_u_pic = "handjob_ani"
                hide screen blkfade
                with d3

                $herViewHead.hideQ()
                m "Великолепно... Теперь сделай это еще разочек, но еще дольше."
                $herViewHead.showQ( "body_31.png", posHead )
                her "Вы имеете в виду - поцеловать ваш... член, сэр?"
                $herViewHead.showQ( "body_29.png", posHead )
                her "Нет, я выгляжу глупо..."
                $herViewHead.hideQ()
                m "Не глупи, девочка. Никто не смотрит."
                $herViewHead.showQ( "body_87.png", posHead )
                her "Вы смотрите, сэр."
                $herViewHead.hideQ()
                m "Но в этом весь смысл!"
                $herViewHead.showQ( "body_79.png", posHead )
                her "......"
                $herViewHead.hideQ()
                m "Это поможет мне кончить почти сразу же!"
                $herViewHead.showQ( "body_69.png", posHead )
                her "..............."
                $herViewHead.hideQ()
                m "И после этого вы сможете просто уйти, не заботясь о наших делах на сегодня."
                $herViewHead.showQ( "body_66.png", posHead )
                her "............."
                $herViewHead.showQ( "body_87.png", posHead )
                her "Ну, тогда ладно...."
                $herViewHead.hideQ()
                ">Гермиона снова касается вашего члена своими губками..."
                ">Она касается головки вашего члена своими губами и остается в таком положении..."
                $ g_c_u_pic = "kiss_ani"
                $ renpy.play('sounds/kiss.mp3') 
                with kissiris
                pause
                $herViewHead.hideQ()
                show screen blktone
                with d3
                m "Очень хорошо..."
                m "Теперь дотронься до него языком."
                her "??!"
                $herViewHead.hideQ()
                m "Это последнее, что я попрошу на сегодня."
                her "............"
                ">Вы чувствуете, как кончик языка Гермионы мягко касается головки вашего члена..."
                $herViewHead.hideQ()
                m "Да, вот так..."
                ">Гермиона немного шевелит своим язычком...."
                $herViewHead.hideQ()
                m "Да... Отлично..."
                show screen blkfade
                with d3
                $ g_c_u_pic = "handjob_ani"
                hide screen blkfade
                with d3
                $herViewHead.showQ( "body_87.png", posHead )
                her2 "Ну, сработало? Вы готовы... кончить, профессор?"
                $herViewHead.hideQ()
                g4 "{size=-4}(Удивительно, но да! Я сейчас кончу! Мне стоит предупредить ее?){/size}"
                hide screen blktone
        menu:
            m "..."
            "- Предупредить ее -":
                g4 "Почти кончил! Тебе лучше подготовиться!"
                $herViewHead.showQ( "body_48.png", posHead )
                her "Что? Так быстро?!"
                $herViewHead.hideQ()
                g4 "{size=+5}Да, отличная работа!!!{/size}"
                g4 "{size=+5}Маленькая шлюха!!!{/size}"
                hide screen bld1
                with d3
                show screen ctc
                pause
                hide screen ctc
                show screen blkfade 
                with d5
                $herViewHead.showQ( "body_117.png", posHead )
                her "Нет, профессор, подождите, я..."
                $herViewHead.hideQ()
                g4 "{size=+5}Слишком поздно, шлюха!{/size}"
                $herViewHead.showQ( "body_118.png", posHead )
                her2 "*хныкает*"
                $herViewHead.hideQ()
                ">Гермиона резко засовывает ваш член себе под рубашку..."
                g4 "?!!"
                ">Ощущение трения вашего члена о ее мягую, теплую кожу переполняет вас и вы люто извергаетесь спермой."
                $herViewHead.hideQ()
                
                show screen white 
                pause.1
                hide screen white
                pause.2
                show screen white 
                pause .1
                hide screen white
                with hpunch
                g4 "{size=+5}АРГХ! ДА!!!{/size}"
              
                
                
                
                
                
                $herViewHead.showQ( "body_48.png", posHead )
                her "!!!!!!!!!!!"
                $herViewHead.hideQ()
                
                

                $ genie_chibi_xpos = 60 #-185 behind the desk.
                $ genie_chibi_ypos = 10
                $ g_c_u_pic = "undershirt_cum_ani"
                hide screen hermione_walk_01 
                hide screen blkfade
                with d3
                stop music fadeout 1.0
                pause 
                        
                #$herViewHead.data().addItem( 'sperm_after', CharacterExItem( herViewHead.mMiscFolder, "sperm_00_after.png", G_Z_FACE + 1 ) )
                $herViewHead.data().addItem( 'item_sperm_dried' )
                $ posHead = gMakePos( 390, 300 )
                $herViewHead.showQ( "body_119.png", posHead )
                her2 "......................."
                $herViewHead.hideQ()
                m "..........................."
                $herViewHead.showQ( "body_119.png", posHead )
                her2 "......................."
                $herViewHead.hideQ()
                m "....................?"
                $herViewHead.showQ( "body_118.png", posHead )
                her2 "......................."
                $herViewHead.hideQ()
                m "...Что за херня сейчас произошла?"
                show screen bld1
                with d3
                $herViewHead.showQ( "body_34.png", posHead )
                play music "music/Chipper Doodle v2.mp3" fadein 1 fadeout 1 # HERMIONE'S THEME.
                her "Я не знаю... Я запаниковала..."
                $herViewHead.hideQ()
                if daytime:
                    $herViewHead.showQ( "body_34.png", posHead )
                    her2 "Мои занятия вот-вот начнутся и я не хотела, чтобы вы испортили мою форму..."
                    $herViewHead.hideQ()
                    m "И ты пойдешь на занятия вот так?"
                    m "В форме, заполненой спермой?"
                    $herViewHead.showQ( "body_118.png", posHead )
                    her2 "У меня есть другой выбор?"
                    her2 "Я могу просто пропустить занятия..."
                    $herViewHead.hideQ()
                else:
                    $herViewHead.showQ( "body_34.png", posHead )
                    her2 "Сейчас общая комната \"Гриффиндора\" будет полна людей..."
                    her2 "И я не хотела бы вернуться туда покрытая вашей спермой, сэр."
                    $herViewHead.showQ( "body_117.png", posHead )
                    her2 "Ох, уже совсем поздно..."
                    $herViewHead.hideQ()
                    m "И ты вот так пойдешь?"
                    m "В форме, заполненой спермой?"
                    $herViewHead.showQ( "body_118.png", posHead )
                    her "У меня есть другой выбор?"
                    $herViewHead.hideQ()
                    
                show screen ctc
                pause
                hide screen ctc
                show screen blkfade
                with d7
                ">Гермиона отпускает ваш все еще пульсирующий член."
                
                show screen hermione_01 
                hide screen chair_02
                hide screen desk_02
                show screen genie
                hide screen g_c_u
                $ posHead = gMakePos( 390, 235 )
                $herViewHead.showQ( "body_118.png", posHead )
                her "Фи... Ваша сперма, сэр..."
                $herViewHead.showQ( "body_117.png", posHead )
                her "Она повсюду на форме..."
                $herViewHead.hideQ()
                m "Просто бери его в рот в следующий раз."
                $herViewHead.showQ( "body_79.png", posHead )
                her "Я... так не думаю, сэр."
                her2 "Мне правда нужно идти. Могу я получить свои очки?"
                $herViewHead.hideQ()
                
                
                
                
                
                
#                g4 "You whore! You little nasty wore!"
#                g4 "There! Allover your fucking belly and tits!"
#                her "Ah! It's so hot!"
#                hide screen h_head2 

#                g4 "Ох, yes, this is so good!"
#                her "Ah..."
#                hide screen h_head2 

#                m "..............."
#                her "............"
#                hide screen h_head2 

#                m "I think I'm done..."
#                her "Ох..."
#                ">Hermione releases your still pulsating cock."
#                her "Ew... Your sperm, сэр..."
#                her "It's everywhere under my uniform..."
#                hide screen h_head2 
#                m "What possessed you to put my cock there, м?"
                

            "- Просто начать кончать -":
                hide screen ctc
                with hpunch
                g4 "АРГХ!"
                show screen blkfade
                with d3
                $herViewHead.showQ( "body_48.png", posHead )
                her "ЧТО?!"
                $herViewHead.hideQ()
                g4 "Вот тебе!"

                $herViewHead.hideQ()
                
                show screen white 
                pause.1
                hide screen white
                pause.2
                show screen white 
                pause .1
                hide screen white
                with hpunch
                g4 "{size=+5}АРГХ! ДА!!!{/size}"
                
                
                
                  
                $herViewHead.showQ( "body_48.png", posHead )
                her "!!!!!!!!!!!"
                $herViewHead.hideQ()
                
                

                $ genie_chibi_xpos = 60 #-185 behind the desk.
                $ genie_chibi_ypos = 10
                $ g_c_u_pic = "on_shirt_cum_ani"
                hide screen hermione_walk_01 
                hide screen blkfade
                with d3
                show screen ctc
                hide screen bld1
                with d3
                pause
                show screen bld1
                with d3
                        
                #$herViewHead.data().addItem( 'sperm_after', CharacterExItem( herViewHead.mMiscFolder, "sperm_00_after.png", G_Z_FACE + 1 ) )
                $herViewHead.data().addItem( 'item_sperm_dried' )
                $ posHead = gMakePos( 390, 300 )
                $herViewHead.showQ( "body_119.png", posHead )
                her2 "......................."
                $herViewHead.hideQ()
                m "Да... Теперь мне лучше..."
                pause
                $ g_c_u_pic = "03_hp/08_animation_02/15_cum_21.png"
                
                #$herViewHead.data().addItem( 'sperm', CharacterExItem( herViewHead.mMiscFolder, "sperm_03_blowjob.png", G_Z_FACE + 1 ) )
                $herViewHead.data().addItem( 'item_sperm', '03' )
               
                $ pos.xpos = 130
                $herView.showQ( "body_19.png", pos )
                with d5
                pause
                her ".........."
                m "Ну, я думаю это все..."
                show screen hermione_01 
                hide screen chair_02
                hide screen desk_02
                hide screen g_c_u
                show screen genie
                $herView.hideQ()
                with fade                                                                                                                                                                                                                      #HERMIONE
                $ pos = POS_140
                $herView.showQQ( "body_32.png", pos )
                her "Профессор! Что вы наделали?!"
                m "Что?"
                if d_flag_01: #If TRUE Genie promised to warn her.
                    play music "music/Chipper Doodle v2.mp3" fadein 1 fadeout 1 # HERMIONE'S THEME.
                    $ hermi.liking -= 11
                    $herView.hideQQ()
                    $herView.showQQ( "body_47.png", pos )
                    her "Вы обещали предупредить меня, сэр!"
                    m "Ох, верно... Моя оплошность."
                    $herView.hideshowQQ( "body_69.png", pos )
                    her "Моя форма испорчена..."
                    her "...Я хочу получить свои очки."
                    $herView.hideQQ()
                else:
                    if daytime:
                        $herView.hideshowQQ( "body_69.png", pos )
                        her "Моя форма испорчена!"
                        $herView.hideshowQQ( "body_87.png", pos )
                        her "Мои занятия вот-вот начнутся и я не могу вот так пойти на них!"
                        m "Конечно можешь, просто вытри ее и все..."
                        m "Никто даже не заметит."
                        $herView.hideshowQQ( "body_79.png", pos )
                        her "...Я хочу получить свои очки."
                        $herView.hideQQ()
                        #$herViewHead.data().addItem( 'sperm_after', CharacterExItem( herViewHead.mMiscFolder, "sperm_00_after.png", G_Z_FACE + 1 ) )
                        $herViewHead.data().addItem( 'item_sperm_dried' )
                    else:
                        $herView.hideshowQQ( "body_69.png", pos )
                        her "Моя форма испорчена!"
                        her "И как я вернусь в комнату \"Гриффиндора\" в таком виде?!"
                        m "Почему нет? Ты выглядишь горячо, девочка!"
                        $herView.hideshowQQ( "body_79.png", pos )
                        her "Профессор!!!"
                        m "Ладно, хорошо. Просто вытри ее и все."
                        m "Никто и не заметит."
                        $herView.hideshowQQ( "body_79.png", pos )
                        her "...Я хочу получить свои очки."
                        $herView.hideQQ()
                        #$herViewHead.data().addItem( 'sperm_after', CharacterExItem( herViewHead.mMiscFolder, "sperm_00_after.png", G_Z_FACE + 1 ) )
                        $herViewHead.data().addItem( 'item_sperm_dried' )
        #her "Могу я получить свои очки?"

    elif IsRunNumber(2): # SECOND EVENT <============================================================== EVENT 02
#    elif request_16_points == 1: # SECOND EVENT <============================================================== EVENT 02
        m "Мисс Грейнджер?"
        $herView.hideQQ()
        $ pos = POS_140
        $herView.showQQ( "body_01.png", pos )
        her "Да, сэр?"
        m "Что вы знаете о \"работе ручками\"?"
        $herView.hideshowQQ( "body_66.png", pos )
        her "Вы меня уже спрашивали, сэр."
        m "Ах, верно."
        m "Ну, я хочу, чтобы вы снова поиграли с моим членом."
        $herView.hideshowQQ( "body_120.png", pos )
        her "Сэр, вы опять начинаете пошлить..."
        m "Ладно, ладно."
        m "Мисс Грейнджер, как насчет некоторой услуги на сегодня."
        $herView.hideshowQQ( "body_69.png", pos )
        her "Конечно, сэр."
        g9 "Услуга заключается в том, что вы должны поиграть с моим членом!"
        $herView.hideshowQQ( "body_66.png", pos )
        her ".............."
        m "Ох, да ладно. Ради чести \"Гриффиндора\"?"
        $herView.hideshowQQ( "body_47.png", pos )
        her "............."
        g9 "Поиграй с моим членом ради чести \"Гриффиндора\"!"
        $herView.hideshowQQ( "body_86.png", pos )
        her "Хватит так говорить, сэр..."
        #Genie with his cock out
        m "Ну же, девочка, я же не прошу тебя сделать это за просто так."
        $herView.hideshowQQ( "body_69.png", pos )
        her "......."
        stop music fadeout 4.0
        

        $herView.hideQ()
        hide screen bld1
        with d3
        $ walk_xpos=400 #Animation of walking chibi. (From)
        $ walk_xpos2=280 #Coordinates of it's movement. (To)
        $ hermione_speed = 03.0 #The speed of moving the walking animation across the screen.
        show screen hermione_walk_01 
        pause.1
        show screen blkfade
        with Dissolve(1)
        pause.3                                                                                                                                                                      #HERMIONE
        hide screen genie
        $ genie_chibi_xpos = 5 #-185 behind the desk.
        $ genie_chibi_ypos = 10
        $ g_c_u_pic = "jerking_off_02_ani"
        show screen chair_02
        show screen g_c_u
        show screen desk_02
        hide screen blktone

        jump event_01_round_02


    elif IsRunNumberOrMore(3): # THIRD EVENT <========================================================================================================= EVENT 03
#    elif request_16_points >= 2: # THIRD EVENT <========================================================================================================= EVENT 03
#        $ new_request_16_03 = True #  Hearts
        
        m "Мисс Грейнджер?"
        $herView.hideshowQQ( "body_01.png", pos )
        her "Сэр?"
        m "Как насчет дрочки?"
        $herView.hideshowQQ( "body_68.png", pos )
        her "Пока вы даете мне очки..."
        m "Ну, тогда начнем. Заработай пару очков."
        
        label new_request_16_jerkonly:
        $herView.hideQ()
        hide screen bld1
        with d3
        $ walk_xpos=400 #Animation of walking chibi. (From)
        $ walk_xpos2=280 #Coordinates of it's movement. (To)
        $ hermione_speed = 03.0 #The speed of moving the walking animation across the screen.
        show screen hermione_walk_01 
        pause.1
        show screen blkfade
        with Dissolve(1)
        pause.3

        hide screen genie
        $ genie_chibi_xpos = 5 #-185 behind the desk.
        $ genie_chibi_ypos = 10
        $ g_c_u_pic = "jerking_off_02_ani"
        show screen chair_02
        show screen g_c_u
        show screen desk_02
        hide screen blktone
        
        
        
        ">Гермиона хватает ваш член своими худенькими пальчками..."
        $ posHead = gMakePos( 390, 290 )
        $herViewHead.showQ( "body_68.png", posHead )
        stop music fadeout 3.0
        her "Вам нравится, когда я делаю вот так, сэр?"
        $herViewHead.hideQ()
        g9 "Да! Очень хорошо!"
        play music "music/Chipper Doodle v2.mp3" fadein 1 fadeout 1 # HERMIONE'S THEME.
        $herViewHead.hideQ()
        #Stroking the cock.
        $ genie_chibi_xpos = 60 #-185 behind the desk.
        $ genie_chibi_ypos = 10
        $ g_c_u_pic = "handjob_ani"
        hide screen hermione_walk_01 
        hide screen blkfade
        with d7
        show screen ctc
        pause
        hide screen ctc
        show screen bld1
        with d3

        m "Да, да, вот так..."
        m "Хм... Ты, однако, наловчилась."
        $herViewHead.showQ( "body_74.png", posHead )
        her "Спасибо, сэр."
        her2 "Я поняла, что лучше я буду делать это качественнее и быстрее."
        $herViewHead.hideQ()
        m "Хм..."
        menu:
            m "..."
            "\"Что ты думаешь о моем члене?\"":
                $herViewHead.showQ( "body_31.png", posHead )
                her "А?"
                her2 "Ох, он неплохой..."
                $herViewHead.showQ( "body_34.png", posHead )
                her2 "Ой, мне же нужно похвалить ваш член! Совсем забыла об этом!"
                $herViewHead.hideQ()
                m "Ну, ты не должна--"
                $herViewHead.showQ( "body_120.png", posHead )
                her "Сэр, позвольте мне быть честной с вами..."
                $herViewHead.hideQ()
                m "Да?"
                $herViewHead.showQ( "body_111.png", posHead )
                her2 "У вас самый большой пенис, который я когда-либо видела!"
                $herViewHead.hideQ()
                m "Ну, я полагаю--"
                $herViewHead.showQ( "body_30.png", posHead )
                her "Это еще не все!"
                $herViewHead.hideQ()
                m "Прошу прощения."
                $herViewHead.showQ( "body_118.png", posHead )
                her "Ваш член настолько большой, что пугает меня!"
                $herViewHead.hideQ()
                g9 "Ах ты маленькая потаскуха. Ты знаешь, что нужно говорить..."
                $herViewHead.showQ( "body_121.png", posHead )
                her "И, конечно же, я жажду его..."
                her2 "Любая женщина была бы рада ощутить его в себе!"
                $herViewHead.hideQ()
                m "...а ты хороша!"
                $herViewHead.showQ( "body_30.png", posHead )
                her "Не перебивайте!"
                $herViewHead.hideQ()
                her "Несмотря ни на что..."
                $herViewHead.showQ( "body_30.png", posHead )
                her2 "Я думаю, что ваш член - это благословение для всего мира!"
                $herViewHead.hideQ()
                m "Ну, не стал бы так преувеличивать..."
                $herViewHead.showQ( "body_30.png", posHead )
                her2 "Послушайте меня, сэр!"
                her2 "Я считаю, что стоит установить статуи в каждом городе на земле, посвященные вашему члену!"
                her2 "Так, чтобы люди всего мира могли поклоняться вашему члену!"
                $herViewHead.hideQ()
                m "Все, хватит."
                $herViewHead.showQ( "body_112.png", posHead )
                her "Перебор?"
                $herViewHead.hideQ()
                m "Ага, немного."
                $herViewHead.showQ( "body_34.png", posHead )
                her "Простите..."
                $herViewHead.hideQ()
                m "Ничего. Продолжай дрочить."
                $herViewHead.showQ( "body_121.png", posHead )
                her2 "................."
                $herViewHead.hideQ()
                show screen blktone
                with d3
                ">Гермиона продолжает дрочить ваш член."
                ">у нее это отлично получается."  
                hide screen blktone
                with d3
                m "Да, да... Вот так."
                
            "\"Назови себя шлюхой!\"":
                $herViewHead.showQ( "body_31.png", posHead )
                her "Простите?"
                $herViewHead.showQ( "body_17.png", posHead )
                her2 "Ох, точно! Я должна унижать себя, да?"
                $herViewHead.hideQ()
                m "Ну, не обязательно, но..."
                $herViewHead.showQ( "body_120.png", posHead )
                her2 "Это отлично, я не возражаю."
                $herViewHead.showQ( "body_45.png", posHead )
                her "И так. Я шлюха!"
                $herViewHead.hideQ()
                m "Отлично. Рад, что мы выяснили это."
                m "Теперь, я хочу, чтобы ты сказала..."
                menu:
                    m "..."
                    "\"Я дешевая шлюха!\"":
                        $herViewHead.showQ( "body_122.png", posHead )
                        her "Конечно."
                        $herViewHead.showQ( "body_121.png", posHead )
                        her "Я дешевая шлюха."
                        her "Грязная, маленькая шлюшка - вот кто я такая."
                        $herViewHead.hideQ()
                        m "Да! Отлично!"
                    "\"Я живу, чтобы сосать член!\"":
                        $herViewHead.showQ( "body_122.png", posHead )
                        her "Эмм..."
                        $herViewHead.showQ( "body_45.png", posHead )
                        her2 "Я живу, чтобы сосать пенис... То есть, член..."
                        $herViewHead.hideQ()
                        m "Правда? Почему тогда ты сейчас его не отсасываешь?"
                        $herViewHead.showQ( "body_111.png", posHead )
                        her2 "Сэр, я просто повторяю за вами..."
                        $herViewHead.hideQ()
                        m "Да ну? Может, ты меня обманываешь...."
                        $herViewHead.showQ( "body_122.png", posHead )
                        her2 "...................."
                        $herViewHead.hideQ()
                        m ".................."
                    "\"Я люблю глотать сперму!\"":
                        $herViewHead.showQ( "body_122.png", posHead )
                        her "Я люблю... Эм... глотать сперму."
                        $herViewHead.hideQ()
                        m "Вы как-то неуверенно это произносите."
                        $herViewHead.showQ( "body_122.png", posHead )
                        her "Да, я знаю...."
                        her "Дайте мне начать снова..."
                        $herViewHead.showQ( "body_121.png", posHead )
                        her "Я люблю глотать сперму!"
                        her "Глотать сперму - это самое лучшее!"
                        her "Я люблю это!"
                        $herViewHead.showQ( "body_123.png", posHead )
                        her2 "..................................."
                        $herViewHead.showQ( "body_122.png", posHead )
                        her "Как вам это, сэр?"
                        $herViewHead.hideQ()
                        m "Идеально." 
            "\"Это действительно неплохо. Ты практиковалась?\"":
                $herViewHead.showQ( "body_74.png", posHead )
                her "Хм?"
                her "Вроде того... На самом деле - нет..."
                $herViewHead.showQ( "body_122.png", posHead )
                her "Я говорила с девочками, и..."
                $herViewHead.hideQ()
                m "Про мастурбацию?"
                $herViewHead.showQ( "body_80.png", posHead )
                her "Помимо других вещей..."
                $herViewHead.hideQ()
                m "Так эти твои подружки, они много об этом знают?"
                $herViewHead.showQ( "body_48.png", posHead )
                her "На самом деле - да. Я была удивлена."
                $herViewHead.showQ( "body_68.png", posHead )
                her2 "Судя по всему, много странных и изощренных видов секса случались в нашей школе..."
                her "Не скажу, что я это одобряю..."
                $herViewHead.showQ( "body_74.png", posHead )
                her "Но они научили меня некоторым... приемам."
                $herViewHead.hideQ()
                m "Хм? И каким например?"
                $herViewHead.showQ( "body_124.png", posHead )
                her "Давайте посмотрим..."
                her "Если я положу одну руку сюда..."
                her "А другую сюда..."
                $herViewHead.hideQ()
                m "О, я вижу... Да, это довольно приятно."
                $herViewHead.showQ( "body_122.png", posHead )
                her "Да?"
                $herViewHead.showQ( "body_68.png", posHead )
                her "Джинни была права насчет этого..."
                $herViewHead.hideQ()
                g4 "Что ты сказала?"
                $herViewHead.showQ( "body_74.png", posHead )
                her "Джинни Уизли, она научила меня этому."
                $herViewHead.hideQ()
                m "О, ясно..."
                $herViewHead.showQ( "body_124.png", posHead )
                her2 "Она сказала, что любой парень влюбится в меня, если я ему так сделаю..."
                her2 "Есть еще одна вещь, когда я делаю колечко из моих пальцев..."
                her2 "И потом вставляю палец сюда..."
                $herViewHead.hideQ()
                m "Хм... Я ничего не чувствую..."
                $herViewHead.showQ( "body_118.png", posHead )
                her "Правда?"
                her "Хм..."
                $herViewHead.showQ( "body_124.png", posHead )
                her "О! Точно!"
                her "Палец нужно вставит сюда! Какая же я глупая!"
                $herViewHead.hideQ()
                with hpunch
                with kissiris
                g4 "О!!! Во имя великих песков пустыни, да!"
                $herViewHead.showQ( "body_80.png", posHead )
                her "Да? Вам хорошо?"
                $herViewHead.showQ( "body_124.png", posHead )
                her2 "Что, если я продолжу, но вставлю палец сюда и немного нажму..."
                $herViewHead.hideQ()
                g4 "Девочка, ты меня убиваешь!"
                $herViewHead.showQ( "body_80.png", posHead )
                her "Правда? Правда?!"
                her "Это действительно довольно весело!"
                $herViewHead.showQ( "body_122.png", posHead )
                her "Эмм... Я имею в виду..."
                her2 "Я, конечно же, делаю это только для моего факультета..."
                $herViewHead.hideQ()
                m "Да, да...  \"Гриффиндор\" гордится этим."
                m "Просто продолжай гладить это место..."
                m "О, да..."
                $herViewHead.showQ( "body_124.png", posHead )
                her "..............."
                $herViewHead.hideQ()
        m "Да..."
        $herViewHead.showQ( "body_122.png", posHead )
        her ".............."
        $herViewHead.hideQ()
        m "Теперь я хочу, чтобы ты кое-что сказала..."
        menu:
            m "..."
            "{size=-4}\"Я мечтаю, чтобы меня изнасиловал отец.\"{/size}":
                $ hermi.liking -= 11
                $herViewHead.showQ( "body_77.png", posHead )
                her "Я не мечтаю об этом!"
                $herViewHead.hideQ()
                m "Я знаю. Просто скажи это."
                $herViewHead.showQ( "body_76.png", posHead )
                her "Мой отец? Это отвратительно, сэр!"
                $herViewHead.hideQ()
                m "Сделай, что я сказал."
                $herViewHead.showQ( "body_79.png", posHead )
                her "..........."
                $herViewHead.showQ( "body_87.png", posHead )
                her "Что же..."
                her "Иногда я мечтаю быть изнасилованной..."
                her "......."
                $herViewHead.hideQ()
                m "Я вижу. И в твоих фантазиях..."
                m "Кто тебя насилует?"
                $herViewHead.showQ( "body_117.png", posHead )
                her "Мой отец...?"
                $herViewHead.hideQ()
                m "Тебе это нравится?"
                $herViewHead.showQ( "body_118.png", posHead )
                her "Нет! Я плачу и умоляю его остановиться!"
                $herViewHead.hideQ()
                m "Хех... Неплохо."
                $herViewHead.showQ( "body_118.png", posHead )
                her "......."
                $herViewHead.hideQ()
                m "Разве это было сложно?.."
                $herViewHead.showQ( "body_67.png", posHead )
                her "Я зову мамочку, но она до сих пор на работе..."
                $herViewHead.hideQ()
                m "Хм?"
                $herViewHead.showQ( "body_33.png", posHead )
                her "Мой папа несет меня в мою комнату..."
                her "И кидает меня на кровать!"
                $herViewHead.showQ( "body_32.png", posHead )
                her "Я плачу \"Нет, папочка, я еще девственница!\""
                $herViewHead.showQ( "body_123.png", posHead )
                $ g_c_u_pic= "03_hp/08_animation_02/12_handjob_01.png"
                her2 "Но он не слушает! Он просто срывает мои трусики!"
                $herViewHead.showQ( "body_22.png", posHead )
                her "Я умоляю его остановиться! Я все кричу и кричу!"
                $herViewHead.hideQ()
                m "Мм, девочка?"
                $herViewHead.showQ( "body_21.png", posHead )
                her "Да?"
                $herViewHead.hideQ()
                m "Ты больше не дрочишь мой член..."
                $herViewHead.showQ( "body_24.png", posHead )
                her "О, я прошу прощения, сэр."
                her "Я просто увлеклась..."
                $ g_c_u_pic = "handjob_ani"
                $herViewHead.showQ( "body_31.png", posHead )
                her "Но все, что я сказала - это, конечно же, неправда!"
                her "Я никогда о таком не фантазирую!"
                $herViewHead.hideQ()
                m "Хорошо."
            "{size=-4}\"Иногда мне становится одиноко и я даю моему псу трахнуть меня.\"{/size}":
                $herViewHead.showQ( "body_18.png", posHead )
                her "Что?!"
                $herViewHead.showQ( "body_17.png", posHead )
                her "Это отвратительно."
                $herViewHead.showQ( "body_16.png", posHead )
                her "Собаки - разносчики {size=+5}болезней{/size}, сэр."
                $herViewHead.hideQ()
                m "На самом деле, человеческие и собачьи {size=+5}болезни{/size} сильно отличаются..."
                m "Что означает, что они не смогут тебя заразить."
                $herViewHead.showQ( "body_08.png", posHead )
                her "............"
                $herViewHead.hideQ()
                m "Я слышал, кстати, что многие женщины любят быть \"связанными\" ."
                $herViewHead.showQ( "body_07.png", posHead )
                her "В каком смысле - \"связанными\"?"
                $herViewHead.hideQ()
                m "Эм... Ну..."
                m "Не имеет значения."
                m "Просто скажи это!"
                $herViewHead.showQ( "body_03.png", posHead )
                her "Хорошо!"
                $herViewHead.showQ( "body_08.png", posHead )
                her2 "Иногда мне становится одиноко и я даю моему псу трахнуть меня."
                $herViewHead.hideQ()
                m "Звучит не очень..."
                $herViewHead.showQ( "body_07.png", posHead )
                her "Потому что у нас даже собаки нет!"
                $herViewHead.hideQ()
                m "Да все равно, просто продолжай..."
            "{size=-4}\"- Ввести вручную то, что нужно сказать -\"{/size}":
                window hide
                # The phrase in the brackets is the text that the game will display to prompt 
                # the player to enter the name they've chosen.
                $ jasname = renpy.input("(Используйте клавиатуру, чтобы ввести предложение.)")

                $ jasname = jasname.strip()
                # The .strip() instruction removes any extra spaces the player may have typed by accident.

                #  If the player can't be bothered to choose a name, then we
                #  choose a suitable one for them:
                if jasname == "":
                    $ jasname="Я шлюха."
                    $herViewHead.showQ( "body_29.png", posHead )
                    her2 "Хм...?"
                    her2 "Должна ли я сказать \"Я шлюха\", как обычно?"
                    $herViewHead.hideQ()
                if one_out_of_three == 1:
                    $herViewHead.showQ( "body_29.png", posHead )
                    her "Я не хочу этого говорить..."
                    $herViewHead.hideQ()
                    m "О, просто сделай это, девочка."
                    $herViewHead.showQ( "body_29.png", posHead )
                    her "..........."
                    $herViewHead.showQ( "body_30.png", posHead )
                    her2 "[jasname]"
                    $herViewHead.hideQ()
                    g9 "Хе-хе..."
                    $herViewHead.hideQ()
                elif one_out_of_three == 2:
                    $herViewHead.showQ( "body_29.png", posHead )
                    her "А?"
                    her2 "Что это значит?"
                    $herViewHead.hideQ()
                    m "Просто скажи это."
                    $herViewHead.showQ( "body_29.png", posHead )
                    her "......"
                    $herViewHead.hideQ()
                    m "Давай, развлеки меня."
                    $herViewHead.showQ( "body_30.png", posHead )
                    her2 "[jasname]"
                    $herViewHead.hideQ()
                    g9 "Хе-хе..."
                    $herViewHead.hideQ()
                elif one_out_of_three == 3:
                    $herViewHead.showQ( "body_29.png", posHead )
                    her "..........."
                    her2 "Я должна сделать это?"
                    $herViewHead.hideQ()
                    m "Просто скажи."
                    $herViewHead.showQ( "body_30.png", posHead )
                    her2 "[jasname]"
                    $herViewHead.hideQ()
                    g9 "Хе-хе..."
        
        #CUMMING
        m "Хм..."
        m "Мне нравится то, что ты делаешь ладонью!"
        $herViewHead.showQ( "body_30.png", posHead )
        her2 "Вы заметили...?"
        her2 "Мне продолжить?"
        $herViewHead.hideQ()
        show screen blkfade
        with d3
        ">Гермиона прижимает ладонью ваш член и начинает очень нежно тереть его..."
        m "О да!!!"
        stop music fadeout 1.0
        g4 "{size=-5}(Я думаю что я сейчас кончу! Нужно ли мне предупредить ее?){/size}"
        menu:
            m "..."
            "\"(Да, лучше сказать ей об этом).\"":
                g4 "Я думаю я близок к--"
                if hermi.whoring >= 18: # LEVEL 07
                    jump kiss_suck
                else:
                    pass
                ">Гермиона быстро поднимает свою блузку..."
                ">И накрывает ваш член ею"
                ">Ощущение ее кожи на вашем разгоряченном члене вызывает у вас легкое головокружение..."
                ">Гермиона прижимает ваш член чуть выше, чем вы ожидали..."
                ">Вы чувствуете ее невероятно мягкую грудь, трущуюся о ваш член..."
               
                
                
                show screen white 
                pause.1
                hide screen white
                pause.2
                show screen white 
                pause .1
                hide screen white
                with hpunch
                g4 "{size=+5}АГРХ! ДА!!!{/size}"
              
                
                play music "music/Chipper Doodle v2.mp3" fadein 1 fadeout 1 # HERMIONE'S THEME.
                
                
                
                $herViewHead.showQ( "body_48.png", posHead )
                her "!!!!!!!!!!!"
                $herViewHead.hideQ()
                
                

                $ genie_chibi_xpos = 60 #-185 behind the desk.
                $ genie_chibi_ypos = 10
                $ g_c_u_pic = "undershirt_cum_ani"
                hide screen hermione_walk_01 
                hide screen blkfade
                with d3
                show screen ctc
                pause 
                        
                #$herViewHead.data().addItem( 'sperm_after', CharacterExItem( herViewHead.mMiscFolder, "sperm_00_after.png", G_Z_FACE + 1 ) )
                $herViewHead.data().addItem( 'item_sperm_dried' )
                $ posHead = gMakePos( 390, 300 )

                
                
                g4 "Агрх! Ты шлюха!"
                $herViewHead.showQ( "body_124.png", posHead )
                her2 "Да, сэр! Просто спустите все!"
                $herViewHead.hideQ()
                g4 "Да! Ебаная шлюха!"
                #Cuming.
                $herViewHead.showQ( "body_64.png", posHead )
                her2 "Ах!! Она такая горячая!"
                $herViewHead.showQ( "body_121.png", posHead )
                her2 "И она просто везде! Ее так много!.."
                her2 "...профессор."
                $herViewHead.hideQ()
                g4 "Агрх!!!"
                m "............"
                m "Я думаю, я закончил..."
                $herViewHead.showQ( "body_122.png", posHead )
                her2 "Ах, хорошо..."
                $herViewHead.showQ( "body_124.png", posHead )
                her2 ".............."
                $herViewHead.showQ( "body_121.png", posHead )
                her2 "Вы так много накончали на меня сегодня, сэр..."
                $herViewHead.hideQ()
                show screen ctc
                pause
                hide screen ctc
                show screen blkfade
                with d5
                ">Гермиона отпускает ваш все еще пульсирующий член."
                
                show screen hermione_01 
                hide screen chair_02
                hide screen desk_02
                show screen genie
                hide screen g_c_u
                $ posHead = gMakePos( 390, 235 )
                hide screen blkfade
                with d5
                
               
                
                
                
                
                if daytime:
                    $herViewHead.showQ( "body_45.png", posHead )
                    her2 "Наверное, мне лучше уйти... мои уроки скоро начнутся."
                else:
                    $herViewHead.showQ( "body_45.png", posHead )
                    her2 "Наверное, мне лучше уйти... Уже довольно поздно."
                $herViewHead.hideQ()
                m "Тебе нормально в такой одежде?"
                $herViewHead.showQ( "body_87.png", posHead )
                her "Что?"
                $herViewHead.showQ( "body_68.png", posHead )
                her "О. Да, со мной будет все в порядке..."
                $herViewHead.showQ( "body_74.png", posHead )
                her2 "Она может немного впитаться здесь и немного здесь, но я надеюсь, что никто не заметит."
                $herViewHead.hideQ()
                m "Хм... Тебе стоит заглотить мой член в следующий раз..."
                $herViewHead.showQ( "body_122.png", posHead )
                her "И проглотить вашу горячую сперму, сэр?"
                $herViewHead.hideQ()
                m "По крайней мере, твоя одежда будет чиста."
                $herViewHead.showQ( "body_120.png", posHead )
                her "Со всем уважением, сэр..."
                $herViewHead.showQ( "body_122.png", posHead )
                her2 "45 очков за это будет мало..."
                her2 "Кстати об этом. Могу ли я получить оплату?"
                $herViewHead.hideQ()
                

            "\"(А, не нужно!).\"":
                g4 "Вот! Получай, шлюха!"
                if hermi.whoring >= 18: # LEVEL 07
                    jump kiss_suck
                else:
                    pass
                with hpunch
                g4 "АГРХ!"
                show screen blkfade
                with d3
                $herViewHead.showQ( "body_48.png", posHead )
                her "ЧТО?!"
                $herViewHead.hideQ()
                g4 "Получай!"

                $herViewHead.hideQ()
                
                show screen white 
                pause.1
                hide screen white
                pause.2
                show screen white 
                pause .1
                hide screen white
                with hpunch
                g4 "{size=+5}АГРРРХ! ДА!!!{/size}"
                
                
                
                  
                $herViewHead.showQ( "body_48.png", posHead )
                her "!!!!!!!!!!!"
                $herViewHead.hideQ()
                
                

                $ genie_chibi_xpos = 60 #-185 behind the desk.
                $ genie_chibi_ypos = 10
                $ g_c_u_pic = "on_shirt_cum_ani"
                hide screen hermione_walk_01 
                hide screen blkfade
                with d3
                show screen ctc
                hide screen bld1
                with d3
                pause
                show screen bld1
                with d3
                        
                #$herViewHead.data().addItem( 'sperm_after', CharacterExItem( herViewHead.mMiscFolder, "sperm_00_after.png", G_Z_FACE + 1 ) )
                $herViewHead.data().addItem( 'item_sperm_dried' )
                $ posHead = gMakePos( 390, 300 )
                $herViewHead.showQ( "body_119.png", posHead )
                her2 "......................."
                $herViewHead.hideQ()
                m "Да... Я чувствую себя намного лучше..."
                pause
                $ g_c_u_pic = "03_hp/08_animation_02/15_cum_21.png"
                
                #$herViewHead.data().addItem( 'sperm', CharacterExItem( herViewHead.mMiscFolder, "sperm_03_blowjob.png", G_Z_FACE + 1 ) )
                $herViewHead.data().addItem( 'item_sperm', '03' )
                $ pos.xpos = 130
                $herView.showQ( "body_19.png", pos, d5 )
                pause
                her ".........."
                m "Ну, кажется, это все..."
                show screen hermione_01 
                hide screen chair_02
                hide screen desk_02
                hide screen g_c_u
                show screen genie
                $herView.hideQ( fade )                                                                                                                                                                                                         #HERMIONE
                $ pos = POS_140
                $herView.showQQ( "body_32.png", pos )
                her "Профессор! Что вы сделали?"
                play music "music/Chipper Doodle v2.mp3" fadein 1 fadeout 1 # HERMIONE'S THEME.
                m "Что?"
                $herView.hideshowQQ( "body_32.png", pos )
                her "Вы меня всю обкончали, сэр..."
                $herView.hideshowQQ( "body_118.png", pos )
                her "Что за ужас..."
                $herView.hideshowQQ( "body_120.png", pos )
                her2 "Профессор, вы должны были предупредить меня."
                m "Это все твоя вина!"
                $herView.hideshowQQ( "body_117.png", pos )
                her2 "Моя вина?"
                m "Да! Ты делала мне так хорошо..."
                m "Что я позабыл обо всем на свете..."     
                $herView.hideshowQQ( "body_122.png", pos )
                her2 "О..."
                her2 "Ну, что сделано, то сделано..."
                $herView.hideshowQQ( "body_123.png", pos )
                her "Я просто вытрусь и буду надеяться, что никто ничего не заметит..."
                $herView.hideshowQQ( "body_122.png", pos )
                her2 "Могу я получить свою оплату?"
                $herView.hideQ()
                with fade  
    
    label done_with_handjob:

#    $ gryffindor += current_payout #35 Дважды суммировалось
    hide screen h_c_u
    hide screen g_c_u
    hide screen g_c_c_u # Genie's sperm. Universal.
    hide screen ctc
    hide screen chair_02
    hide screen desk_02
    show screen genie
    show screen bld1
    $ hermione_chibi_xpos = 400 #Near the desk.
    $ hermione_chibi_ypos = 250 #Default: 250
    show screen hermione_02 #Hermione stands still.
    pause.1
    hide screen blkfade
    with d3
    

    m "Да, мисс Грейнджер. [current_payout] очков \"Гриффиндору\"." 
    $ gryffindor +=current_payout
    $ pos = POS_140
    $herView.showQ( "body_13.png", pos )
    hide screen hermione_01_f #Hermione stands still.
    with d3
    her "Спасибо, сэр..."

    if event.Name=="new_request_02": 
        jump new_request_16_jerkonly_to_02

    $herViewHead.data().delItem( 'item_sperm' )

    if hermi.whoring <= 14:
        $ hermi.whoring +=1

    
    
#    if whoring >= 12 and whoring <= 14:
#        $ level = "05"
#        $ new_request_16_01 = True #  Hearts
#    if whoring >= 15 and whoring <= 17:
#        $ level = "06"
#        $ new_request_16_02 = True #  Hearts
    
    if IsRunNumberOrMore(3): 
        $SetHearts(3)
    else:
        $SetHearts(GetStage(hermi.whoring,12,3,2))


#    $ request_16_points += 1

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

    $herView.data().loadState()

    call music_block

    $event.Finalize()    

    if daytime:
        $ hermione_takes_classes = True
        jump night_main_menu
    else:
        $ hermione_sleeping = True
        jump day_main_menu            
   

        
        
### KISS SUCK! ###

label kiss_suck: #Jumps here after event #03 and if WHORING >= LEVEL 07
    ">Гермиона нежно тянется своими губами к вашему члену и целует его..."
    ">Это простое действие заставило ваш член практически взорваться потоком спермы."
    show screen white 
    pause.1
    hide screen white
    pause.2
    show screen white 
    pause .1
    hide screen white
    with hpunch
    g4 "{size=+5}Агрх! ДА!!!{/size}"
    $ genie_chibi_xpos = 60 #-185 behind the desk.
    $ genie_chibi_ypos = 10
    $ g_c_u_pic = "kiss_cum_ani"
    
    hide screen blkfade
    with d3
    show screen ctc
    hide screen bld1
    with d3
    pause
    
    
    
    show screen bld1
    with d3
                        
   
    her2 "*Глп!-Глп!-Глп!*"
    $herViewHead.hideQ()
    g4 "Аргх! Ты маленькая шлюха!"
    g4 "Да, блядь! Пей мою сперму! Выпей ее всю!"
    her2 "*Глп!-Глп!-Глп!*"
    g4 "Арх... Да!"
    ">Вы замечаете, что Гермиона едва справляется с таким потоком спермы в своем рту."
    her2 "*Глп!-Глп!-Глп!*"
    g4 "Ах..."
    g4 "Просто великолепное чувство..."
    her2 "*Глп!-Глп!-Глп!*"
    m "Я думаю, это все, девочка..."
    m "Можешь идти..."
    pause
    show screen blkfade
    with d5
    show screen hermione_01 
    hide screen chair_02
    hide screen desk_02
    hide screen g_c_u
    show screen genie
    $herView.hideQ()
                                                                                                                                                                                                                         #HERMIONE
    $ pos = POS_140
    $herView.showQQ( "body_125.png", pos )
    show screen ctc
    pause
    her2 "........................................."
    $herView.hideshowQQ( "body_126.png", pos )
    her2 "ГЛП!!!"
    $herView.hideshowQQ( "body_39.png", pos )
    her2 "Гу-а-а..."
    hide screen blkfade
    with d3
    $herView.hideshowQQ( "body_123.png", pos )
    her2 "Я проглотила ее всю, сэр!"
    m "Хорошая девочка..."
    $herView.hideshowQQ( "body_123.png", pos )
    her "В какой-то момент я подумала, что задохнусь..."
    her2 "Ее было так много..."
    $herViewHead.hideQ()
    m "Что же, дело сделано и твоя форма идеально чиста."
    $herView.hideshowQQ( "body_124.png", pos )
    her2 "Да! Я знаю! Этот вариант намного лучше!"
    if daytime:
        $herView.hideshowQQ( "body_122.png", pos )
        her "Я лучше просто пойду в класс, как будто бы ничего и не было."
    else:
        $herView.hideshowQQ( "body_124.png", pos )
        her "Я могу просто пойти и провести время с парнями в Общей Комнате и никто ничего не узнает..."
    $herViewHead.hideQ()
    m "Да... С полным животом спермы..."
    $herView.hideQQ()
    $herView.showQQ( "body_117.png", pos )
    her2 "Профессор!"
    her2 "...Могу ли я получить оплату, сэр?"
    $herViewHead.hideQ()
    jump done_with_handjob #^^^ (<-That's to a smiley. That's a arrow up).
    
     
     
