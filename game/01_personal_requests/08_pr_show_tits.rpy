
#####################################################################################################################################################################
### LEVEL 03 ###########################################################################################################################################################
###################REQUEST_08 (Level 03) (Show me tits). #####################################################################################################################
label new_request_08: #LV.3 (Whoring = 6 - 8)
    #__#hide screen hermione_main 
    #__#with d3
    $herView.hideQQ()
    if request_08_points == 0:
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
            jump new_personal_request
    
    if whoring <=5:
        jump too_much
        
    
        
    $ current_payout = 25 #Used when haggling about price of th favor.
        
    $ pos = POS_140
    
    # we'll undress her, so save the state
    $herView.data().saveState()

    if request_08_points == 0 and whoring <= 11: # LEVEL 04 # FIRST TIME.
        m "Мисс Грейнджер?"
        #__#hide screen hermione_main
        #__#with d3
        $herView.hideQQ()
        #__#$ h_xpos=370 #Defines position of the Hermione's full length sprite. (Default 370). (Center: 140)
        $ pos = POS_370
        
        #__#$ h_body = "03_hp/13_hermione_main/body_03.png" #Sprite of Hermione's upper body.
        #__#show screen hermione_main
        #__#with d3
        $herView.showQQ( "body_03.png", pos )
        her "Да, сэр..."
        m "Сколько очков будет стоить посмотреть на твои сиськи?"
        #__#hide screen hermione_main
        #__#with d3
        $herView.hideQQ()
        #__#$ h_body = "03_hp/13_hermione_main/body_14.png" #Sprite of Hermione's upper body.
        #__#$ h_xpos=370 #Defines position of the Hermione's full length sprite. (Default 370). (Center: 140)
        #__#show screen hermione_main
        #__#with d3
        $herView.showQQ( "body_14.png", pos )
        stop music fadeout 1.0
        her "Сколько вы можете предложить...?"
        play music "music/Chipper Doodle v2.mp3" fadein 1 fadeout 1 # HERMIONE'S THEME.
        #__#hide screen hermione_main
        #__#with d3
        $herView.hideQQ()
        #__#$ h_body = "03_hp/13_hermione_main/body_30.png" #Sprite of Hermione's upper body.
        #__#$ h_xpos=370 #Defines position of the Hermione's full length sprite. (Default 370). (Center: 140)
        #__#show screen hermione_main
        #__#with d3
        $herView.showQQ( "body_30.png", pos )
        her "Профессор Дамблдор!"
        m "Хм... Я думал ваш факультет может получить дополнительные очки..."
        m "Но я думаю, что был неправ..."
        #__#hide screen hermione_main
        #__#with d3
        $herView.hideQQ()
        #__#$ h_body = "03_hp/13_hermione_main/body_31.png" #Sprite of Hermione's upper body.
        #__#$ h_xpos=370 #Defines position of the Hermione's full length sprite. (Default 370). (Center: 140)
        #__#show screen hermione_main
        #__#with d3
        $herView.showQQ( "body_31.png", pos )
        her ".........?"
        m "Пожалуйста, не противься мне..."
        m "Все что я хочу - это помочь тебе..."
        #__#hide screen hermione_main
        #__#with d3
        $herView.hideQQ()
        #__#$ h_body = "03_hp/13_hermione_main/body_29.png" #Sprite of Hermione's upper body.
        #__#$ h_xpos=370 #Defines position of the Hermione's full length sprite. (Default 370). (Center: 140)
        #__#show screen hermione_main
        #__#with d3
        $herView.showQQ( "body_29.png", pos )
        her "............."
        #__#hide screen hermione_main
        #__#with d3
        $herView.hideQQ()
        #__#$ h_body = "03_hp/13_hermione_main/body_33.png" #Sprite of Hermione's upper body.
        #__#$ h_xpos=370 #Defines position of the Hermione's full length sprite. (Default 370). (Center: 140)
        #__#show screen hermione_main
        #__#with d3
        $herView.showQQ( "body_33.png", pos )
        her "200 очков, сэр."
        m "Если я дам вам 200 очков, Мисс Грейнджер..."
        m "Вы оголите свою грудь и покажите свои дыньки?"
        #__#hide screen hermione_main
        #__#with d3
        $herView.hideQQ()
        #__#$ h_body = "03_hp/13_hermione_main/body_47.png" #Sprite of Hermione's upper body.
        #__#$ h_xpos=370 #Defines position of the Hermione's full length sprite. (Default 370). (Center: 140)
        #__#show screen hermione_main
        #__#with d3
        $herView.showQQ( "body_47.png", pos )
        her "Профессор Дамблдор! Не надо так выражаться!"
        her "Я думаю, я лучше пойду..."
        menu:
            "\"Стой. 200 очков твои. Показывай!\"":
                $ current_payout = 200 #Used when haggling about price of th favor.
                #__#hide screen hermione_main
                #__#with d3
                $herView.hideQQ()
                #__#$ h_body = "03_hp/13_hermione_main/body_14.png" #Sprite of Hermione's upper body.
                #__#$ h_xpos=370 #Defines position of the Hermione's full length sprite. (Default 370). (Center: 140)
                #__#show screen hermione_main
                #__#with d3
                $herView.showQQ( "body_14.png", pos )
                her "Серьезно?"
                m "Да"
                #__#hide screen hermione_main
                #__#with d3
                $herView.hideQQ()
                #__#$ h_body = "03_hp/13_hermione_main/body_29.png" #Sprite of Hermione's upper body.
                #__#$ h_xpos=370 #Defines position of the Hermione's full length sprite. (Default 370). (Center: 140)
                #__#show screen hermione_main
                #__#with d3
                $herView.showQQ( "body_29.png", pos )
                her "......................................"
                her "Вы обещаете, что не будете трогать их, сэр?"
                m "Конечно, конечно..."
                #__#hide screen hermione_main
                #__#with d3
                $herView.hideQQ()
                #__#$ h_body = "03_hp/13_hermione_main/body_32.png" #Sprite of Hermione's upper body.
                #__#$ h_xpos=370 #Defines position of the Hermione's full length sprite. (Default 370). (Center: 140)
                #__#show screen hermione_main
                #__#with d3
                $herView.showQQ( "body_32.png", pos )
                her "Я делаю это только ради моего факультета, сэр!"

            "\"Я дам тебе 5 очков, если ты покажешь сиськи.\"":
                #__#hide screen hermione_main
                #__#with d3
                $herView.hideQQ()
                #__#$ h_body = "03_hp/13_hermione_main/body_72.png" #Sprite of Hermione's upper body.
                #__#$ h_xpos=370 #Defines position of the Hermione's full length sprite. (Default 370). (Center: 140)
                #__#show screen hermione_main
                #__#with d3
                $herView.showQQ( "body_72.png", pos )
                her "Пять?!"
                #__#hide screen hermione_main
                #__#with d3
                $herView.hideQQ()
                #__#$ h_body = "03_hp/13_hermione_main/body_76.png" #Sprite of Hermione's upper body.
                #__#$ h_xpos=370 #Defines position of the Hermione's full length sprite. (Default 370). (Center: 140)
                #__#show screen hermione_main
                #__#with d3
                $herView.showQQ( "body_76.png", pos )
                her "Профессор, я не собираюсь показывать их за скромные пять очков!"
                m "Ну, твои сиськи, конечно, не стоят 200, девочка!"
                #__#hide screen hermione_main
                #__#with d3
                $herView.hideQQ()
                #__#$ h_body = "03_hp/13_hermione_main/body_73.png" #Sprite of Hermione's upper body.
                #__#$ h_xpos=370 #Defines position of the Hermione's full length sprite. (Default 370). (Center: 140)
                #__#show screen hermione_main
                #__#with d3
                $herView.showQQ( "body_73.png", pos )
                her "(Неужели они так плохи?)"
                #__#hide screen hermione_main
                #__#with d3
                $herView.hideQQ()
                #__#$ h_body = "03_hp/13_hermione_main/body_69.png" #Sprite of Hermione's upper body.
                #__#$ h_xpos=370 #Defines position of the Hermione's full length sprite. (Default 370). (Center: 140)
                #__#show screen hermione_main
                #__#with d3
                $herView.showQQ( "body_69.png", pos )
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
        #__#hide screen hermione_main
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
        #__#her_12 "{size=-5}(Мои сисечки сейчас взорвуться...){/size}"
        $her_head_state = 12
        her_head_main "{size=-5}(Мои сисечки сейчас взорвуться...){/size}"
        m "Подойди ближе, девочка, дай мне лучше рассмотреть..."
        #__#her_04 "............"
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
        #__#her_01 "............"
        $her_head_state = 1
        her_head_main "............"
        m "Очень хорошо..."
        #__#her_04 "....."
        $her_head_state = 4
        her_head_main "....."

        #__#$ badges = False # Hides any badges from hermione_main screen.

        show screen blktone 
        with d3
        #__#hide screen hermione_main
        #__#with d3
        $herView.hideQQ()
        
        #__#$ h_xpos=140 #Defines position of the Hermione's full length sprite. (Default 370). (Center: 140)
        $ pos = POS_140
        #$ only_upper = True #No lower body displayed. 
        #__#$ h_body = "03_hp/13_hermione_main/body_81.png" #Sprite of Hermione's upper body.
        #__#show screen hermione_main
        #__#with d3
        
        # add tits pose!
        call addTitsPose
    
        $herView.showQQ( "body_81.png", pos )
        pause
        her "...................................."
        
        
    else:
        if whoring >= 6 and whoring <= 8: # LEVEL 03 # <=================================================================================== FIRST EVENT. (HERMIONE IS UNWILLING).
            m "Мисс Грейнджер?"
            #__#her_02 "Да, профессор?"
            $her_head_state = 2
            her_head_main "Да, профессор?"
            m "Я хочу посмотреть на твои сиськи."
            #__#her_04 "............"
            $her_head_state = 4
            her_head_main "............"
            #__#her_04 "Вы обещаете не трогать их, сэр?"
            her_head_main "Вы обещаете не трогать их, сэр?"
            m "Конечно."
            hide screen blktone
            with d3
            hide screen bld1
            with d3
            #__#hide screen hermione_main
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
            #__#hide screen hermione_main
            #__#with d3
            $herView.hideQQ()
            #__#$ h_body = "03_hp/13_hermione_main/body_81.png" #Sprite of Hermione's upper body.
            #__#$ h_xpos=140 #Defines position of the Hermione's full length sprite. (Default 370). (Center: 140)
            #__#$ pos = POS_140
            
            # add tits pose!
            call addTitsPose

            $herView.showQQ( "body_81.png", pos )
            #$ only_upper = True #No lower body displayed. 
            #__#$ badges = False # Hides any badges from hermione_main screen.

            #__#show screen hermione_main
            #__#with d3
            pause
            her "...................................."
            
            
            
            
        elif whoring >= 9: # LEVEL 04 and higher# <=================================================================================== SECOND EVENT and THIRD EVENT. (HERMIONE IS INDIFFERENT) 
            m "Я хочу увидеть твои сиськи, Мисс Грейнджер."
            #__#her_15 "Вы будете только смотреть, сэр?"
            $her_head_state = 15
            her_head_main "Вы будете только смотреть, сэр?"
            m "Конечно..."
            hide screen blktone
            with d3
            hide screen bld1
            with d3
            #__#hide screen hermione_main
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
            #__#hide screen hermione_main
            #__#with d3
            $herView.hideQQ()
            
            #__#$ badges = False # Hides the layer with badges.
            
            #__#$ h_body = "03_hp/13_hermione_main/body_84.png" #Sprite of Hermione's upper body.
            #__#$ h_xpos=140 #Defines position of the Hermione's full length sprite. (Default 370). (Center: 140)
            #__#$ pos = POS_140

            # add tits pose!
            call addTitsPose
            
            $herView.showQQ( "body_84.png", pos )
            #$ only_upper = True #No lower body displayed. 
            #__#show screen hermione_main
            #__#with d3
            pause
            her "...................................."
            play music "music/(Orchestral) Playful Tension by Shadow16nh.mp3" fadein 1 fadeout 1 # SEX THEME.
    


    menu:
        "\"Солгать. Схватить за сиськи!\"":
            if whoring >= 6 and whoring <= 8: # LEVEL 03 # <=================================================================================== FIRST EVENT. HERMIONE OUTRAGED.
                #__#hide screen hermione_main
                $herView.hideQQ()
                #__#$ only_upper = False #No lower body displayed. 
                #__#with d3
                show screen blkfade
                with d3
                ">Вы протягиваете руки и хватаете грудь Гермионы..."
                #__#her_07 "Профессор, что вы делаете?"
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
                #__#her_13 "Нет, сэр, пожалуйста! Вы не должны..."
                $her_head_state = 13
                her_head_main "Нет, сэр, пожалуйста! Вы не должны..."
                m "Это не займет много времени, просто стой."
                #__#her_24 "Сэр, Я не соглашалась на это!"
                $her_head_state = 24
                her_head_main "Сэр, Я не соглашалась на это!"
                with hpunch
                #__#her_23 "Вы должны отпустите меня сейчас же!!!"
                $her_head_state = 23
                her_head_main "Вы должны отпустите меня сейчас же!!!"
                show screen blkfade
                with d5
                ">Гермиона отстраняется от вас и спешно прикрывается."
                #__#her_19 "Думаю я лучше пойду..."
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
                #__#her_19 "Но я показала свои..."
                her_head_main "Но я показала свои..."
                #__#her_24 "И вы трогали меня..."
                $her_head_state = 24
                her_head_main "И вы трогали меня..."
                #__#her_23 "И я ничего не получу?"
                $her_head_state = 23
                her_head_main "И я ничего не получу?"
                m "Вы провалились, Мисс Грейнджер..."
                #__#her_19  "Гр.................."
                $her_head_state = 19
                her_head_main "Гр.................."
                #__#her_19 "{size=-5}(Burn in hell, you wretched old---{/size}"
                her_head_main "{size=-5}(Гори в аду, ты, ущербный старый---{/size}"
                $ mad += 22
                call music_block
                jump loadState_and_could_not_flirt
            elif whoring >= 9 and whoring <= 11: # LEVEL 04 # <=================================================================================== SECOND EVENT. A BIT ANGRY.
                #__#hide screen hermione_main
                #__#with d3
                $herView.hideQQ()
                $ only_upper = False #No lower body displayed. 
                show screen blkfade
                with d3
                ">Вы протягиваете свои руки и хватаете сиськи Гермионы..."
                #__#her_07 "Профессор, что вы делаете?"
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
                #__#her_04 "Я не соглашалась на это, сэр..."
                $her_head_state = 4
                her_head_main "Я не соглашалась на это, сэр..."
                #__#her_04 "Я не думаю что вы должны..."
                her_head_main "Я не думаю, что вы должны..."
                m "Тебе не нравиться...?"
                #__#her_12 "Что?"
                $her_head_state = 12
                her_head_main "Что?"
                m "Тебе не нравиться, как я играю и сжимаю твои сиськи?"
                #__#her_12 "..............."
                her_head_main "..............."
                m "Признайся, тебе это приятно..."
                #__#her_12 "{size=-5}(Так странно видеть мои сиськи у кого-то в руках...){/size}"
                her_head_main "{size=-5}(Так странно видеть мои сиськи у кого-то в руках...){/size}"
                #__#her_13 "сэр, Я позволяю вам делать это со мной, чтобы помочь моему факультету, ничего более!"
                $her_head_state = 13
                her_head_main "сэр, Я позволяю вам делать это со мной, чтобы помочь моему факультету, ничего более!"
                play music "music/Chipper Doodle v2.mp3" fadein 1 fadeout 1 # HERMIONE'S THEME.
                #__#her_04 "Пожалуйста,отпустите меня!"
                $her_head_state = 4
                her_head_main "Пожалуйста, отпустите меня!"
                show screen blkfade
                with d5
                ">Гермиона отстраняется от вас и спешно прикрывается."
                #__#her_04 "Вы обещали не трогать, профессор..."
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
                #__#her_01 "............."
                $her_head_state = 1
                her_head_main "............."
                #__#her_09 "Могу я получить свою оплату?"
                $her_head_state = 9
                her_head_main "Могу я получить свою оплату?"
                m "Конечно..."
                $ mad += 9
            elif whoring >= 12: # LEVEL 05 # <=================================================================================== THIRD EVENT. ENJOYS A LITTLE.
                #__#hide screen hermione_main
                #__#with d3
                $herView.hideQQ()
                #__#$ only_upper = False #No lower body displayed. 
                show screen blkfade
                with d3
                ">Вы протягиваете свои руки и хватаете грудь Гермионы..."
                #__#her_07 "Профессор, что вы делаете?"
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
                #__#her_12 "Но..."
                $her_head_state = 12
                her_head_main "Но..."
                #__#her_13 "ах...{image=textheart.png}"
                $her_head_state = 13
                her_head_main "ах...{image=textheart.png}"
                #__#her_12 " Я не соглашалась на это..."
                $her_head_state = 12
                her_head_main " Я не соглашалась на это..."
                m "Но тебе это нравиться, не так ли?"
                #__#her_13 "Несовсем, сэр!{image=textheart.png}"
                $her_head_state = 13
                her_head_main "Несовсем, сэр!{image=textheart.png}"
                show screen blktone
                with d3
                ">Вы несколько раз сжимаете её сиськи..."
                hide screen blktone
                with d3
                #__#her_15 "сэр,вы обещали не трогать..."
                $her_head_state = 15
                her_head_main "Сэр, вы обещали не трогать..."
                m "Я знаю, знаю... Но так трудно удержаться..."
                #__#her_20 "................."
                $her_head_state = 20
                her_head_main "................."
                #__#her_06 "....................aх...{image=textheart.png}"
                $her_head_state = 6
                her_head_main "....................aх...{image=textheart.png}"
                #__#her_06 "сэр,вы должны остановиться..."
                her_head_main "сэр, вы должны остановиться..."
                m "Еще чуть-чуть..."
                show screen blktone8
                with d3
                ">Вы продолжаете мять её сиськи..."
                hide screen blktone8
                with d3
                #__#her_37 "сэр... остановитесь..."
                $her_head_state = 37
                her_head_main "сэр... остановитесь..."
                m "Почему? Потому что тебе это очень нравиться?"
                #__#her_18 "Нет,это не так..."
                $her_head_state = 18
                her_head_main "Нет, это не так..."
                #__#her_17 "Я считаю..."
                $her_head_state = 17
                her_head_main "Я считаю..."
                show screen blktone8
                with d3
                ">Вы тянете сиськи в противоположных направлениях, а затем стягиваете их вместе..."
                hide screen blktone8
                with d3
                #__#her_38 "Aх...{image=textheart.png} сэр, я действительно должна идти..."
                $her_head_state = 38
                her_head_main "Aх...{image=textheart.png} сэр, я действительно должна идти..."
                if daytime:
                    #__#her_17 "Хорошо... скоро начнуться укроки..."
                    $her_head_state = 17
                    her_head_main "Хорошо... скоро начнуться уроки..."
                else:
                    #__#her_17 "Уже поздно..."
                    her_head_main "Уже поздно..."
                m "Ну, хорошо..."
                show screen blkfade
                with d5
                ">Вы отпускаете ее грудь..."
                ">Гермиона прикрывается..."
                play music "music/Chipper Doodle v2.mp3" fadein 1 fadeout 1 # HERMIONE'S THEME.
                #__#her_25 "Пожалуйста не думайте,что я забыла ваше обещание, сэр."
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
                #__#her_35 "Могу я получить свои очки?"
                $her_head_state = 35
                her_head_main "Могу я получить свои очки?"
                $ mad +=7
   
        "\"Сдержать обещание. Просто смотреть.\"":
            ">Вы долго всматриваетесь в грудь Гермионы..."
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
                        #__#hide screen hermione_main
                        #__#with d3
                        $herView.hideQQ()
                        #__#$ h_body = "03_hp/13_hermione_main/body_83.png" #Sprite of Hermione's upper body.
                        #__#$ h_xpos=140 #Defines position of the Hermione's full length sprite. (Default 370). (Center: 140)
                        #__#$ pos = POS_140
                        #__#show screen hermione_main
                        #__#with d3
                        $herView.showQQ( "body_83.png", pos )
                        pause
                        her "Спасибо--"
                        #__#hide screen hermione_main
                        #__#with d3
                        $herView.hideQQ()
                        #__#$ h_body = "03_hp/13_hermione_main/body_82.png" #Sprite of Hermione's upper body.
                        #__#$ h_xpos=140 #Defines position of the Hermione's full length sprite. (Default 370). (Center: 140)
                        #__#show screen hermione_main
                        #__#with d3
                        $herView.showQQ( "body_82.png", pos )
                        play music "music/Chipper Doodle v2.mp3" fadein 1 fadeout 1 # HERMIONE'S THEME.
                        her "..........."
                        #__#hide screen hermione_main
                        #__#with d3
                        $herView.hideQQ()
                        #__#$ h_body = "03_hp/13_hermione_main/body_81.png" #Sprite of Hermione's upper body.
                        #__#$ h_xpos=140 #Defines position of the Hermione's full length sprite. (Default 370). (Center: 140)
                        #__#show screen hermione_main
                        #__#with d3
                        $herView.showQQ( "body_81.png", pos )
                        her "В последнее время вы частенько говорите разные неуместные вещи, профессор."
                        
                    "\"Хм... Видел и лучше.\"":
                        $ mad += 7
                        $herView.hideQQ()
                        $herView.showQQ( "body_83.png", pos );
                        her "Арх..."
                        her "Теперь мы закончили?"

            elif whoring >= 12: # LEVEL 05 # <=================================================================================== THIRD EVENT.
                pause
                menu:
                    "\"У тебя отличные сиськи, девочка.\"":
                        #__#hide screen hermione_main
                        #__#with d3
                        $herView.hideQQ()
                        #__#$ h_body = "03_hp/13_hermione_main/body_82.png" #Sprite of Hermione's upper body.
                        #__#$ h_xpos=140 #Defines position of the Hermione's full length sprite. (Default 370). (Center: 140)
                        #__#$ pos = POS_140
                        #__#show screen hermione_main
                        #__#with d3
                        $herView.showQQ( "body_82.png", pos )
                        her "Вы правда так думаете, профессор?"
                        #__#hide screen hermione_main
                        #__#with d3
                        $herView.hideQQ()
                        #__#$ h_body = "03_hp/13_hermione_main/body_84.png" #Sprite of Hermione's upper body.
                        #__#$ h_xpos=140 #Defines position of the Hermione's full length sprite. (Default 370). (Center: 140)
                        #__#show screen hermione_main
                        #__#with d3
                        $herView.showQQ( "body_84.png", pos )
                        her "Мне приятно, что вам они нравятся, сэр..."
                    "\"Ну, так себе сиськи...\"":
                        #__#hide screen hermione_main
                        #__#with d3
                        $herView.hideQQ()
                        #__#$ h_body = "03_hp/13_hermione_main/body_82.png" #Sprite of Hermione's upper body.
                        #__#$ h_xpos=140 #Defines position of the Hermione's full length sprite. (Default 370). (Center: 140)
                        #__#$ pos = POS_140
                        #__#show screen hermione_main
                        #__#with d3
                        $herView.showQQ( "body_82.png", pos )
                        her "А?"
                        her "Это значит, что они вам не нравятся, сэр?"
                        #__#hide screen hermione_main
                        #__#with d3
                        $herView.hideQQ()
                        #__#$ h_body = "03_hp/13_hermione_main/body_85.png" #Sprite of Hermione's upper body.
                        #__#$ h_xpos=140 #Defines position of the Hermione's full length sprite. (Default 370). (Center: 140)
                        #__#show screen hermione_main
                        #__#with d3
                        $herView.showQQ( "body_85.png", pos )
                        her "Мне жаль..."
            ">Вы смотрите на ее грудь немного дольше..."
            pause
            m "Ладно, ты можешь прикрыться, девочка..."
            her "............."
            #__#hide screen hermione_main
            #__#with d3
            $herView.hideQQ()
            #__#$ only_upper = False #No lower body displayed. 
            
            show screen blkfade
            with d3
            ">Гермиона прикрылась..."
            #__#$ badges = True # Shows layer with badges.
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
                #__#hide screen hermione_main
                #__#with d3
                $herView.hideQQ()
                ">Вы взяли свой член и начали дрочить..."
                show screen blkfade
                hide screen bld1
                with d3
                play music "music/Chipper Doodle v2.mp3" fadein 1 fadeout 1 # HERMIONE'S THEME.
                #__#her_30 "Профессор?!!"
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
                #__#her_13 "Профессор, что вы...?"
                $her_head_state = 13
                her_head_main "Профессор, что вы...?"
                ">Вы продолжаете дрочить свой член..."
                #__#her_12 "Профессор, нет..."
                $her_head_state = 12
                her_head_main "Профессор, нет..."
                #__#her_12 "Вы должны... Убрать это..."
                her_head_main "Вы должны... Убрать это..."
                m "Хватит трепетать девочка. Я же не трогаю тебя?"
                #__#her_19 "Но..."
                $her_head_state = 19
                her_head_main "Но..."
                #__#her_20 "Но я не соглашалась на это!"
                $her_head_state = 20
                her_head_main "Но я не соглашалась на это!"
                #__#her_19"Я..."
                $her_head_state = 19
                her_head_main "Я..."
                #__#her_19 "Я думаю мне лучше уйти!"
                her_head_main "Я думаю, мне лучше уйти!"
                menu:
                    "\"Уйдешь сейчас - не получишь очков!\"":
                        #__#$ only_upper = False
                        #__#her_21 "После {size=+5}этого{/size}? Вы издиваетесь, сэр?"
                        $her_head_state = 21
                        her_head_main "После {size=+5}этого{/size}? Вы издеваетесь, сэр?"
                        #__#her_21 "Я показала свои..."
                        her_head_main "Я показала свои..."
                        #__#her_25 ".........."
                        $her_head_state = 25
                        her_head_main ".........."
                        #__#her_24 "Я не собираюсь показывать вам больше, профессор!"
                        $her_head_state = 24
                        her_head_main "Я не собираюсь показывать вам больше, профессор!"
                        show screen blkfade
                        with d3
                        ">Гермиона оттолкнула вас и прикрылась..."
                        g4 "Не смей покидать меня в таком состоянии, девочка!"
                        #__#her_10 "Ноги моей больше не будет в вашем кабинете, сэр!"
                        $her_head_state = 10
                        her_head_main "Ноги моей больше не будет в вашем кабинете, сэр!"
                        g4 "Да ладно уже, скажи что нибудь грязное! Я почти кончил!"
                        #__#her_27 "Вы ужасный человек, сэр..."
                        $her_head_state = 27
                        her_head_main "Вы ужасный человек, сэр..."
                        $ mad += 30
                        call music_block
                        jump loadState_and_could_not_flirt
                    "\"Ладно, ладно. На сегодня достаточно.\"":
                        $ mad +=9
                        #__#$ only_upper = False
                        pass
                    "- Дрочить быстрее -":
                        $ mad += 35
                        #__#$ only_upper = False
                        ">Вы начали дрочить очень быстро!"
                        #__#her_23 "Нет,профессор,стойте!"
                        $her_head_state = 23
                        her_head_main "Нет, профессор, стойте!"
                        ">Вы дрочите еще быстрее!"
                        #__#her_25 "Профессор, думаю,  я пойду..."
                        $her_head_state = 25
                        her_head_main "Профессор, думаю, я пойду..."
                        g4 "Нет, подожди, я почти кончил!"
                        show screen blkfade
                        with d3
                        #__#her_10 "Иу! Профессор!"
                        $her_head_state = 10
                        her_head_main "Иу! Профессор!"
                        #__#her_10 "Я ухожу!"
                        her_head_main "Я ухожу!"
                        call music_block
                        jump loadState_and_could_not_flirt
            elif whoring >= 9 and whoring <= 11: # LEVEL 04 # <=================================================================================== SECOND EVENT.
                #__#hide screen hermione_main
                #__#with d3
                $herView.hideQQ()
                ">Вы взяли свой член и начали дрочить..."
                show screen blkfade
                hide screen bld1
                with d3
                #__#her_30 "Профессор?"
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
                #__#her_13 "Профессор,я не соглашалась на это..."
                $her_head_state = 13
                her_head_main "Профессор, я не соглашалась на это..."
                m "Чего ты жалуешься, девочка?"
                m "Я не трогаю тебя..."
                #__#her_13 "Да,но вы трогаете себя, сэр."
                her_head_main "Да, но вы трогаете себя, сэр."
                ">Вы подняли темп..."
                m "Просто стой, девочка."
                m "Скоро я закончу."
                #__#her_13 ".................."
                her_head_main ".................."
                #__#her_12 "(Он такой большой...)"
                $her_head_state = 12
                her_head_main "(Он такой большой...)"
                m "Да, вот так..."
                m "Да, с твоими голыми сиськами..."
                #__#her_12 ".............."
                her_head_main ".............."
                #__#her_17 "ну, так и быть..."
                $her_head_state = 17
                her_head_main "ну, так и быть..."
                #__#her_17 "Вы можете трогать себя, сэр..."
                her_head_main "Вы можете трогать себя, сэр..."
                #__#her_01 "Но вы должны обещать мне не..."
                $her_head_state = 1
                her_head_main "Но вы должны обещать мне не..."
                #__#her_05 "Не... eм..."
                $her_head_state = 5
                her_head_main "Не... eм..."
                #__#her_04 "Не закончить на меня..."
                $her_head_state = 4
                her_head_main "Не закончить на меня..."
                #__#her_08 "Не передо мной, сэр..."
                $her_head_state = 8
                her_head_main "Не передо мной, сэр..."
                m "Хорошо..."
                m "Ах, ты, маленькая шлюшка. Ты дикая шлюшка!"
                #__#her_19 "......................."
                $her_head_state = 19
                her_head_main "......................."
                "Вы начали дрочить свой член еще быстрее..."
                g4 "Да, ты знаешь что это! Да!"
                #__#her_19 "................"
                her_head_main "................"
                show screen blkfade 
                with d3
                ">Вы собираетесь кончить..."
                menu:
                    "- Сдержаться, как и обещали -":
                        g4 "Ох, отлично..."
                        g4 "Я думаю, стоит остановиться..."
                        #__#her_15 "..............."
                        $her_head_state = 15
                        her_head_main "..............."
                        ">Гермиона прикрыла груди..."
                    "- Кончить -":
                        #play music "music/Chipper Doodle v2.mp3" fadein 1 fadeout 1 # HERMIONE'S THEME.
                        g4 "Aргх! Ты шлюшка!"
                        #__#her_21 "Профе-- ??"
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
                        #__#her_23 "Профессор, нет, вы обещали!"
                        $her_head_state = 23
                        her_head_main "Профессор, нет! Вы обещали!"
                        g4 "Ох, это здорово, да..."
                        $ no_blinking = False #When True - blinking animation is not displayed. 
                        hide screen jerking_off_cum
                        with d3
                        #__#her_10 "Профессор, как вы могли...?"
                        $her_head_state = 10
                        her_head_main "Профессор, как вы могли...?"
                        m "Ох, это было очень классно..."
                        show screen blktone8
                        with d3
                        #__#$ badges = False # Turns off badges from hermione_main screen.
                        #__#$ sperm_on_tits = True
                        #__#$ h_body = "03_hp/13_hermione_main/body_85.png" #Sprite of Hermione's upper body.
                        #__#show screen hermione_main
                        #__#with d3

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
                        #__#hide screen hermione_main
                        #__#with d3
                        $herView.hideQQ()
                        show screen blkfade
                        with d3
                        show screen genie
                        hide screen jerking_off_01
                        hide screen chair_02
                        show screen hermione_02
                        with d3
                        #__#$ sperm_on_tits = False
                        #__#$ only_upper = False
                        #__#$ aftersperm = True
                        #__#$ h_body = "03_hp/13_hermione_main/body_47.png" #Sprite of Hermione's upper body.
                        hide screen blkfade
                        with d5
                        
                        #__#$ badges = True # Turns badges back on from hermione_main screen.
                        
                        #__#show screen hermione_main
                        #__#with d3
                        
                        #here we'll remove pose and add aftersperm effect
                        call addAfterSperm

                        $herView.showQQ( "body_47.png", pos )
                        pause
                        #play music "music/Chipper Doodle v2.mp3" fadein 1 fadeout 1 # HERMIONE'S THEME.
                        her "Как вы могли сделать это, сэр?!"
                        her "Вы дали слово!"
                        #__#hide screen hermione_main
                        #__#with d3
                        $herView.hideQQ()
                        $ mad += 45
            elif whoring >= 12: # LEVEL 05 # <=================================================================================== THIRD EVENT.
                #__#hide screen hermione_main
                #__#with d3
                $herView.hideQQ()
                ">Вы берете свой член и начинаете дрочить..."
                show screen blkfade
                hide screen bld1
                with d3
                #__#her_06 "Профессор?"
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
                #__#her_13 "Профессор, я  не соглашалась на это..."
                $her_head_state = 13
                her_head_main "Профессор, я  не соглашалась на это..."
                m "Чего ты жалуешься, девочка?"
                m "Я тебя не трогаю..."
                #__#her_13 "Да, но вы... трогаете себя, сэр."
                her_head_main "Да, но вы... трогаете себя, сэр."
                #">You pick up the pace..."
                m "Просто стой, сука."
                m "Я скоро кончу."
                #__#her_13 ".................."
                her_head_main ".................."
                m "Да... да, вот так..."
                m "Да, твои сисечки..."
                #__#her_12 ".............."
                $her_head_state = 12
                her_head_main ".............."
                #__#her_17 "ну, так и быть..."
                $her_head_state = 17
                her_head_main "ну, так и быть..."
                #__#her_01 "Но вы должны мне пообещать..."
                $her_head_state = 1
                her_head_main "Но вы должны мне пообещать..."
                #__#her_05 "Не... Эм..."
                $her_head_state = 5
                her_head_main "Не... Эм..."
                #__#her_04 "Не кончать..."
                $her_head_state = 4
                her_head_main "Не кончать..."
                #__#her_04 "Не передо мной, сэр..."
                her_head_main "Не передо мной, сэр..."
                m "Хорошо..."
                m "Ах, ты, маленькая шлюшка. Ты грязная шлюшка!"
                #__#her_12 "......................."
                $her_head_state = 12
                her_head_main "......................."
                ">Вы начинаете дрочить еще быстрее..."
                g4 "Да, я знаю, ты хочешь этого! Да!"
                #__#her_12 "................"
                her_head_main "................"
                show screen blkfade 
                with d3
                 # SAME AS PREVIOUS EVENT^^^
                g4 "Aргх! (Я кончаю!)"
                menu:
                    "- Сдержать обещание -":
                        g4 "Ох, ладно..."
                        g4 "Думаю, лучше остановиться..."
                        #__#her_12 "..............."
                        her_head_main "..............."
                        #__#her_12 "Эм... Я читала,что это плохо для мужчин, сэр..."
                        her_head_main "Эм... Я читала, что это плохо для мужчин, сэр..."
                        m "А?"
                        #__#her_13 "Это плохо для вашего здоровья сдерживать себя..."
                        $her_head_state = 13
                        her_head_main "Это плохо для вашего здоровья - сдерживать себя..."
                        #__#her_12 "Eм..."
                        $her_head_state = 12
                        her_head_main "Eм..."
                        #__#her_14 "Если вы хотите вы можете--"
                        $her_head_state = 14
                        her_head_main "Если вы хотите, вы можете--"
                        g4 "Aргх! Ты шлюшка!"
                        #__#her_07 "???"
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
                        #__#her_09 "Профессор, я не имел в виду, что вы можете ... кончить на меня, сэр..."
                        $her_head_state = 9
                        her_head_main "Профессор, я не имела в виду, что вы можете ... кончить на меня, сэр..."
                        g4 "Ох, это здорово, да..."
                        $ no_blinking = False #When True - blinking animation is not displayed. 
                        hide screen jerking_off_cum
                        with d3
                        #__#her_18 "Ну, что сделано, то сделано, я полагаю..."
                        $her_head_state = 18
                        her_head_main "Ну, что сделано, то сделано, я полагаю..."
                        m "Ох, это было очень классно..."
                        show screen blktone8
                        with d3
                        #__#$ sperm_on_tits = True
                        #__#$ h_body = "03_hp/13_hermione_main/body_85.png" #Sprite of Hermione's upper body.
                        #__#$ badges = False # Hides any badges from hermione_main screen.
                        #__#show screen hermione_main
                        #__#with d3
                        call addSperm
                        $herView.showQQ( "body_85.png", pos )
                        pause
                        her "Моя форма испачкана..."
                        m "Не беспокойся, я дам тебе очки для факультета, девочка."
                        m "Ты сделала мне хорошо."
                        #__#hide screen hermione_main
                        #__#with d3
                        $herView.hideQQ()
                        #__#$ h_body = "03_hp/13_hermione_main/body_84.png" #Sprite of Hermione's upper body.
                        #__#show screen hermione_main
                        #__#with d3
                        $herView.showQQ( "body_84.png", pos )
                        her "Спасибо, сэр."
                        #__#hide screen hermione_main
                        #__#with d3
                        $herView.hideQQ()
                        #__#$ h_body = "03_hp/13_hermione_main/body_83.png" #Sprite of Hermione's upper body.
                        #__#show screen hermione_main
                        #__#with d3
                        $herView.showQQ( "body_83.png", pos )
                        her "Теперь мне нужно очистить себя..."
                        pause
                        #__#hide screen hermione_main
                        #__#with d3
                        $herView.hideQQ()
                        show screen blkfade
                        with d3
                        show screen genie
                        hide screen jerking_off_01
                        hide screen chair_02
                        show screen hermione_02
                        #__#$ badges = True # Shows badges on hermione_main screen.
                        #__#$ sperm_on_tits = False
                        #__#$ only_upper = False
                        #__#$ aftersperm = True
                        #__#$ h_body = "03_hp/13_hermione_main/body_45.png" #Sprite of Hermione's upper body.
                        hide screen blkfade
                        with d5
                        
                        #here we remove pose and add aftersperm effect
                        call addAfterSperm
                        #__#show screen hermione_main
                        $herView.showQ( "body_45.png", pos )
                        pause
                        her "Ну, это следует сделать сейчас..."
                        #__#hide screen hermione_main
                        #__#with d3
                        $herView.hideQQ()
                    "- Кончить -":
                        g4 "Aргх! Ты шлюшка!"
                        #__#her_07 "???"
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
                        #__#her_13 "aх...{image=textheart.png} Так горячо...{image=textheart.png}"
                        $her_head_state = 13
                        her_head_main "Ах...{image=textheart.png} Так горячо...{image=textheart.png}"
                        #__#her_09 "Профессор,вы обещали..."
                        $her_head_state = 9
                        her_head_main "Профессор, вы обещали..."
                        g4 "Ох, это здорово, да..."
                        $ no_blinking = False #When True - blinking animation is not displayed. 
                        hide screen jerking_off_cum
                        with d3
                        #__#her_15 "Ну, что сделано, то сделано, я полагаю..."
                        $her_head_state = 15
                        her_head_main "Ну, что сделано, то сделано, я полагаю..."
                        m "Ох, это было довольно классно.."
                        show screen blktone8
                        with d3
                        #__#$ badges = False # Hides any badges from hermione_main screen.
                        #__#$ sperm_on_tits = True
                        #__#$ h_body = "03_hp/13_hermione_main/body_85.png" #Sprite of Hermione's upper body.
                        #__#show screen hermione_main
                        #__#with d3
                        call addSperm
                        $herView.showQQ( "body_85.png", pos )
                        pause
                        her "Моя форма испачкана..."
                        m "Не беспокойся, я дам тебе очки факультета, девочка."
                        m "Ты сделала мне хорошо."
                        #__#hide screen hermione_main
                        #__#with d3
                        $herView.hideQQ()
                        #__#$ h_body = "03_hp/13_hermione_main/body_84.png" #Sprite of Hermione's upper body.
                        #__#show screen hermione_main
                        #__#with d3
                        $herView.showQQ( "body_84.png", pos )
                        her "Спасибо, сэр."
                        #__#hide screen hermione_main
                        #__#with d3
                        $herView.hideQQ()
                        #__#$ h_body = "03_hp/13_hermione_main/body_83.png" #Sprite of Hermione's upper body.
                        #__#show screen hermione_main
                        #__#with d3
                        $herView.showQQ( "body_83.png", pos )
                        her "Теперь я должна себя очистить..."
                        pause
                        #__#hide screen hermione_main
                        #__#with d3
                        $herView.hideQQ()
                        show screen blkfade
                        with d3
                        show screen genie
                        hide screen jerking_off_01
                        hide screen chair_02
                        show screen hermione_02
                        #__#$ badges = True # Turns the badges layer back on.
                        #__#$ sperm_on_tits = False
                        #__#$ only_upper = False
                        #__#$ aftersperm = True
                        #__#$ h_body = "03_hp/13_hermione_main/body_45.png" #Sprite of Hermione's upper body.
                        hide screen blkfade
                        with d5
                        #__#$ badges = True # Hides any badges from hermione_main screen.
                        #__#show screen hermione_main
                        
                        # remove pose and add aftersperm
                        call addAfterSperm
                        $herView.showQ( "body_45.png", pos )
                        pause
                        her "Ну, это следует сделать сейчас..."
                        #__#hide screen hermione_main
                        #__#with d3
                        $herView.hideQQ()
                        

    #__#$ badges = True # Hides any badges from hermione_main screen.
    
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

    #__#$ h_xpos=370 #Defines position of the Hermione's full length sprite.
    #__#$ h_ypos=0
    $ pos = POS_370
    #__#$ h_body = "03_hp/13_hermione_main/body_29.png" #Sprite of Hermione's upper body.
    #__#show screen hermione_main
    #__#with d3
    $herView.showQQ( "body_29.png", pos )
    her ".................."
    her "Спасибо сэр..."
    if daytime:
        her "Теперь, если Вы не возражаете, я лучше пойду. Мои занятия начинаются."
    else:
        her" Я лучше пойду сейчас. Пока не слишком поздно..."
    
    if whoring >= 6 and whoring <= 8:
        $ level = "03"
        $ new_request_08_01 = True # HEARTS.
    if whoring >= 9 and whoring <= 11:
        $ level = "04"
        $ new_request_08_02 = True # HEARTS.
    if whoring >= 12:
        $ level = "05"
        $ new_request_08_03 = True # HEARTS.

    hide screen bld1
    #__#hide screen hermione_main
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
        #__#her_12 "(Как унизительно... кем я стала...?)"
        $her_head_state = 12
        her_head_main "(Как унизительно... кем я стала...?)"
        $ renpy.play('sounds/door.mp3') #Sound of a door opening.
        hide screen hermione_01_f #Hermione stands still.
        with Dissolve(.3)
    elif whoring >= 9 and whoring <= 11: # LEVEL 04 # <=================================================================================== SECOND EVENT.
        #__#her_12 "........................"
        her_head_main "........................"
        $ renpy.play('sounds/door.mp3') #Sound of a door opening.
        hide screen hermione_01_f #Hermione stands still.
        with Dissolve(.3)  
    elif whoring >= 12: # LEVEL 05 # <=================================================================================== THIRD EVENT.
        #__#her_06 "{size=-5}(Как унизительно...){/size}"
        $her_head_state = 6
        her_head_main "{size=-5}(Как унизительно...){/size}"
        #__#her_24 "{size=-5}(Нет, Гермиона, ты глупая девочка!){/size}"
        $her_head_state = 24
        her_head_main "{size=-5}(Нет, Гермиона, ты глупая девочка!){/size}"
        #__#her_24 "{size=-5}(Мы делаем это, чтобы защитить честь нашего факультета!){/size}"
        her_head_main "{size=-5}(Мы делаем это, чтобы защитить честь нашего факультета!){/size}"
        #__#her_19 "................................."
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
        

    $ request_08_points += 1
        
    #__#$ aftersperm = False #Shows cum stains on Hermione's uniform.

    # load from pose with tits and that sperm!
    $herView.data().loadState()
    
    call music_block
    
    if daytime:
        $ hermione_takes_classes = True
        jump day_main_menu
    else:
        $ hermione_sleeping = True
        jump night_main_menu



label addTitsPose:
    # add tits pose!
    $herView.data().addPose( CharacterExItemPoseShowTits( herView.mPoseFolder, 'pose_dress_up.png', G_Z_POSE ) )
    return
    
label addSperm:
    # add sperm item!
    $herView.data().addItem( 'sperm', CharacterExItem( herView.mMiscFolder, 'sperm_00.png', G_Z_FACE + 1 ) )
    return
    
label addAfterSperm:
    # del pose and add aftersperm
    $herView.data().delPose()
    $herView.data().addItem( 'sperm', CharacterExItem( herView.mMiscFolder, 'sperm_00_after.png', G_Z_FACE + 1 ) )
    return
    
label loadState_and_could_not_flirt:
    $herView.data().loadState()
    jump could_not_flirt