###################REQUEST_22 (Level 06) (55 pt.) (Blowjob). 
label new_request_22: #LV.6 (Whoring = 15 - 17)
    #__#hide screen hermione_main 
    #__#with d3
    $herView.hideQQ()
    if request_22_points == 0:
        m "{size=-4}(Попросить девчонку сделать мне минет?){/size}"
    else:
        m "{size=-4}(Попросить девчонку сделать мне еще один минет?){/size}"
    $ menu_x = 0.5 #Default position of the menu (0.5). Version B is $ menu_x = 0.2
    menu:
        "\"(Да! Сделаем это!)\"":
            show screen blktone
            with d3
            pass
        "\"(Не сейчас.)\"":
            jump new_personal_request
            
 
    $ pos = POS_140
    $ herView.data().saveState()

    if request_22_points == 0: # FIRST EVENT <============================================================== EVENT 01
        m "Мисс Гренджер??"
        #__#hide screen hermione_main                                                                                                                                                                                   #HERMIONE
        #__#with d3                                                                                                                                                                                                                        #HERMIONE
        $herView.hideQQ()
        #__#$ h_xpos=140 #Defines position of the Hermione's full length sprite. (Default 370). (Center: 140)                                                       #HERMIONE
        #__#$ h_body = "03_hp/13_hermione_main/body_01.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
        #__#show screen hermione_main                                                                                                                                                                                 #HERMIONE
        #__#with d3                                                                                                                                                                                                                        #HERMIONE
        $herView.showQQ( "body_01.png", pos )
        her "Да, профессор?"
        m "Сегодня я планирую дать \"Гриффиндору\" 55 очков..."
        m "Если вы у меня отсосете..."
        if whoring <=14: # LEVEL 05
            jump too_much
        #__#hide screen hermione_main                                                                                                                                                                                   #HERMIONE
        #__#with d3                                                                                                                                                                                                                        #HERMIONE
        $herView.hideQQ()
        #__#$ h_xpos=140 #Defines position of the Hermione's full length sprite. (Default 370). (Center: 140)                                                       #HERMIONE
        #__#$ h_body = "03_hp/13_hermione_main/body_87.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
        #__#show screen hermione_main                                                                                                                                                                                 #HERMIONE
        #__#with d3                                                                                                                                                                                                                        #HERMIONE
        $herView.showQQ( "body_87.png", pos )
        her "Ох..."
        #__#hide screen hermione_main                                                                                                                                                                                   #HERMIONE
        #__#with d3                                                                                                                                                                                                                        #HERMIONE
        $herView.hideQQ()
        #__#$ h_xpos=140 #Defines position of the Hermione's full length sprite. (Default 370). (Center: 140)                                                       #HERMIONE
        #__#$ h_body = "03_hp/13_hermione_main/body_124.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
        #__#show screen hermione_main                                                                                                                                                                                 #HERMIONE
        #__#with d3                                                                                                                                                                                                                        #HERMIONE
        $herView.showQQ( "body_124.png", pos )
        her "Хорошо."
        m "Серьезно? Просто так?"
        #__#hide screen hermione_main                                                                                                                                                                                   #HERMIONE
        #__#with d3                                                                                                                                                                                                                        #HERMIONE
        $herView.hideQQ()
        #__#$ h_xpos=140 #Defines position of the Hermione's full length sprite. (Default 370). (Center: 140)                                                       #HERMIONE
        #__#$ h_body = "03_hp/13_hermione_main/body_118.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
        #__#show screen hermione_main                                                                                                                                                                                 #HERMIONE
        #__#with d3                                                                                                                                                                                                                        #HERMIONE
        $herView.showQQ( "body_118.png", pos )
        her "Да, я знаю, что должна чувствовать себя неловко..."
        #__#hide screen hermione_main                                                                                                                                                                                   #HERMIONE
        #__#with d3                                                                                                                                                                                                                        #HERMIONE
        $herView.hideQQ()
        #__#$ h_xpos=140 #Defines position of the Hermione's full length sprite. (Default 370). (Center: 140)                                                       #HERMIONE
        #__#$ h_body = "03_hp/13_hermione_main/body_117.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
        #__#show screen hermione_main                                                                                                                                                                                 #HERMIONE
        #__#with d3                                                                                                                                                                                                                        #HERMIONE
        $herView.showQQ( "body_117.png", pos )
        her "Но, почему то, я чувствую себя нормально..."
        #__#hide screen hermione_main                                                                                                                                                                                   #HERMIONE
        #__#with d3                                                                                                                                                                                                                        #HERMIONE
        $herView.hideQQ()
        #__#$ h_xpos=140 #Defines position of the Hermione's full length sprite. (Default 370). (Center: 140)                                                       #HERMIONE
        #__#$ h_body = "03_hp/13_hermione_main/body_124.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
        #__#show screen hermione_main                                                                                                                                                                                 #HERMIONE
        #__#with d3                                                                                                                                                                                                                        #HERMIONE
        $herView.showQQ( "body_124.png", pos )
        her "Я думаю, я просто рада, что могу помочь Гриффиндру...."
        #__#hide screen hermione_main                                                                                                                                                                                   #HERMIONE
        #__#with d3                                                                                                                                                                                                                        #HERMIONE
        $herView.hideQQ()
        #__#$ h_xpos=140 #Defines position of the Hermione's full length sprite. (Default 370). (Center: 140)                                                       #HERMIONE
        #__#$ h_body = "03_hp/13_hermione_main/body_120.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
        #__#show screen hermione_main                                                                                                                                                                                 #HERMIONE
        #__#with d3                                                                                                                                                                                                                        #HERMIONE
        $herView.showQQ( "body_120.png", pos )
        her "И если я должна сделать вам минет, то пусть так и будет..."
        m "Ну что же, хорошо."
        #__#hide screen hermione_main                                                                                                                                                                                   #HERMIONE
        #__#with d3                                                                                                                                                                                                                        #HERMIONE
        $herView.hideQQ()
        #__#$ h_xpos=140 #Defines position of the Hermione's full length sprite. (Default 370). (Center: 140)                                                       #HERMIONE
        #__#$ h_body = "03_hp/13_hermione_main/body_118.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
        #__#show screen hermione_main                                                                                                                                                                                 #HERMIONE
        #__#with d3                                                                                                                                                                                                                        #HERMIONE
        $herView.showQQ( "body_118.png", pos )
        her "Хотя теперь, когда я говорю это вслух, мне это не нравится!..."
        m "Слишком поздно, ты уже сказала \"Да\"!"
        #__#hide screen hermione_main                                                                                                                                                                                   #HERMIONE
        #__#with d3                                                                                                                                                                                                                        #HERMIONE
        $herView.hideQQ()
        #__#$ h_xpos=140 #Defines position of the Hermione's full length sprite. (Default 370). (Center: 140)                                                       #HERMIONE
        #__#$ h_body = "03_hp/13_hermione_main/body_24.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
        #__#show screen hermione_main                                                                                                                                                                                 #HERMIONE
        #__#with d3                                                                                                                                                                                                                        #HERMIONE
        $herView.showQQ( "body_24.png", pos )
        her "Я знаю..."

        label blowjob_jumping:
        # BLOWJOB
        play music "music/(Orchestral) Playful Tension by Shadow16nh.mp3" fadein 1 fadeout 1 # SEX THEME.
        #__#hide screen hermione_main                                                                                                                                                                                   #HERMIONE
        $herView.hideQ() #"WARNING_Z"
        hide screen genie
        $ genie_chibi_xpos = -150 #-185 behind the desk. (Also 5 is something).
        $ genie_chibi_ypos = 10
        $ g_c_u_pic = "blowjob_ani"
        show screen chair_02
        show screen g_c_u
        
        hide screen hermione_02 #Hermione stands still.
        hide screen blkfade
        hide screen blktone
        hide screen bld1
        show screen ctc
        with fade
        pause
        show screen bld1
        with d3
#        $ her_head_xpos=390 #Defines position of the Hermione's full length sprite. (Default 370). 140 - center. Bottom right: 390
#        $ her_head_ypos=235 #Defines position of the Hermione's full length sprite. (Default 0). Right bottom corner: 340 - head only. 235 - tits.
#        show screen h_head2                                                             # HERMIONE
#        $ h_body = "03_hp/13_hermione_main/body_31.png" # HERMIONE


        

        
        her "*Хлюп* *Чавк!* *Хлюп!*"
        m "Даа..."
        m "Теперь, попробуй глубже..."
        her "*Хлюп!* *Кулдык!* *Кулдык!*"
        m "Даа, мне это нравится, хорошо."
        her "*Чавк!* *!* *Хлюп!*"
        m "Да, хорошая девочка."

        $ posHead = gMakePos( 390, 235 )
        menu:
            m "Хмм..."
            "\"Что там с твоим \"ОЗМП\" клубом?\"":
                her "*Чавк?*"
                
                $ hermione_chibi_xpos = -150 #-185 behind the desk. (Also 5 is something).
                $ hermione_chibi_ypos = 10
                $ h_c_u_pic = "hand_ani"
                show screen h_c_u
                hide screen g_c_u
                with d3
                #__#$ her_head_xpos=390 #Defines position of the Hermione's full length sprite. (Default 370). 140 - center. Bottom right: 390
                #__#$ her_head_ypos=235 #Defines position of the Hermione's full length sprite. (Default 0). Right bottom corner: 340 - head only. 235 - tits.
                
                #__#show screen h_head2                                                             # HERMIONE
                $herViewHead.showQ( "body_118.png", posHead )
                #__#$ h_body = "03_hp/13_hermione_main/body_118.png" # HERMIONE
                her "Ох, хорошо..."
                her "Мы остаемся активны, но..."
                #__#hide screen h_head2       
                $herViewHead.hideQ()
                hide screen h_c_u   # SUCKING
                show screen g_c_u # SUCKING
                with d3                      #  SUCKING
                her "*Чавк!* *Кулдык!*"
                show screen h_c_u   # NOT SUCKING
                hide screen g_c_u # NOT SUCKING
                with d3                      #  NOT SUCKING
                #__#show screen h_head2                                                             # HERMIONE
                $herViewHead.showQ( "body_122.png", posHead )
                #__#$ h_body = "03_hp/13_hermione_main/body_122.png" # HERMIONE
                her2 "Но мы не получаем той популярости и максимальной поддержки, какой хотелось бы..."
                hide screen h_c_u   # SUCKING
                show screen g_c_u # SUCKING
                with d3                      #  SUCKING
                #__#hide screen h_head2
                $herViewHead.hideQ()
                her "*Чавк!* *Хлюп!* *Хлюп!*"
                m "Охх... Это отлично..."
                her "*Чавк!* *Чавк!* *Чавк!*"
                m "Хмм..."
                m "Итак, вы позволили себе продавать себя за очки для факультета, давать мне играть с вашими сисками и прочее......"
                her "*Кулдык!* *Хлюп!* *Чавк!*"
                m "А потом осуждаете такое перед всеми студентами своего факультета."
                her "*Чавк!* *Чавк!* *Хлюп!*"
                m "Извращенка и лицемерка."
                her "*Хлюп--"
                show screen h_c_u   # NOT SUCKING
                hide screen g_c_u # NOT SUCKING
                with d3                      #  NOT SUCKING
                #__#show screen h_head2                                                             # HERMIONE
                $herViewHead.showQ( "body_117.png", posHead )
                #__#$ h_body = "03_hp/13_hermione_main/body_117.png" # HERMIONE
                her "Это не то, за что мы выступаем, сэр."
                #__#hide screen h_head2
                $herViewHead.hideQ()
                m "Что ты имеешь в виду?"
                #__#show screen h_head2                                                             # HERMIONE
                $herViewHead.showQ( "body_16.png", posHead )
                #__#$ h_body = "03_hp/13_hermione_main/body_16.png" # HERMIONE
                her2 "\"ОЗМП\" О половом равенстве."
                her2 "Мы не против обмена очков на услуги для учителей..."
                her2 "Мы против полового неравенства, которое подразумевает под собой этого рода услуги за очки..."
                #__#hide screen h_head2
                $herViewHead.hideQ()
                m "Хмм..."
                m "Этот разговор начинает утомлять меня..."
                m "Пососи мой член еще немного, прежде чем мы продолжим."
                #__#show screen h_head2                                                             # HERMIONE
                $herViewHead.showQ( "body_121.png", posHead )
                #__#$ h_body = "03_hp/13_hermione_main/body_121.png" # HERMIONE
                her "Конечно, сэр."
                hide screen h_c_u   # SUCKING
                show screen g_c_u # SUCKING
                with d3                      #  SUCKING
                #__#hide screen h_head2
                $herViewHead.hideQ()
                her "*Кулдык!* *Хлюп!* *Хлюп!*"
                m "Да, намного лучше..."
                m "Но вы по прежнему против подобных услуг, верно?"
                her "*Хлюп--"
                show screen h_c_u   # NOT SUCKING
                hide screen g_c_u # NOT SUCKING
                with d3                      #  NOT SUCKING
                #__#show screen h_head2                                                             # HERMIONE
                $herViewHead.showQ( "body_120.png", posHead )
                #__#$ h_body = "03_hp/13_hermione_main/body_120.png" # HERMIONE
                her2 "Да, это не одобряется..."
                #__#hide screen h_head2 
                $herViewHead.hideQ()
                m "И все же, сегодня ты преступница."
                #__#show screen h_head2                                                             # HERMIONE
                $herViewHead.showQ( "body_120.png", posHead )
                #__#$ h_body = "03_hp/13_hermione_main/body_120.png" # HERMIONE
                her "Но разве у меня был выбор??"
                her2 "Я была в очень трудном положении..."
                #__#hide screen h_head2
                $herViewHead.hideQ()
                m "Мой член, девочка."
                #__#show screen h_head2                                                             # HERMIONE
                $herViewHead.showQ( "body_120.png", posHead )
                #__#$ h_body = "03_hp/13_hermione_main/body_120.png" # HERMIONE
                her "Верно, извините..."
                hide screen h_c_u   # SUCKING
                show screen g_c_u # SUCKING
                with d3                      #  SUCKING
                #__#hide screen h_head2
                $herViewHead.hideQ()
                her "*Чавк!* *Хлюп!* *Кулдык!*"
                her "*Чавк--"
                show screen h_c_u   # NOT SUCKING
                hide screen g_c_u # NOT SUCKING
                with d3                      #  NOT SUCKING
                #__#show screen h_head2                                                             # HERMIONE
                $herViewHead.showQ( "body_117.png", posHead )
                #__#$ h_body = "03_hp/13_hermione_main/body_117.png" # HERMIONE
                her2 "У нас будет встреча, сразу после всего этого."
                her2 "Я должна буду выступить с речью в этой форме, грязной, в пятнах."
                her2 "Я чувствую себя ужасно, но я должна буду сделать это..."
                #__#hide screen h_head2     
                $herViewHead.hideQ()
                m "Попробуй просто насладиться этим..."
                #__#show screen h_head2                                                             # HERMIONE
                $herViewHead.showQ( "body_118.png", posHead )
                #__#$ h_body = "03_hp/13_hermione_main/body_118.png" # HERMIONE  
                her "Хорошо..."
                #__#hide screen h_head2        
                $herViewHead.hideQ()
                m "Просто признай это."
                #__#show screen h_head2                                                             # HERMIONE
                $herViewHead.showQ( "body_117.png", posHead )
                #__#$ h_body = "03_hp/13_hermione_main/body_117.png" # HERMIONE
                her "..............."
                #__#hide screen h_head2
                $herViewHead.hideQ()
                m "Да, я знал это, тебе это нравится, ведь ты - извращенка."
                #__#show screen h_head2                                                             # HERMIONE
                $herViewHead.showQ( "body_118.png", posHead )
                #__#$ h_body = "03_hp/13_hermione_main/body_118.png" # HERMIONE
                her2 "Я думаю, это было неловко и захватывающе одновременно..."
                her2 "И из за этого я чувствую себя еще хуже."
                #__#hide screen h_head2
                $herViewHead.hideQ()
                m "Бедняжка."
                m "Положи член обратно в рот."
                #__#show screen h_head2                                                             # HERMIONE
                $herViewHead.showQ( "body_117.png", posHead )
                #__#$ h_body = "03_hp/13_hermione_main/body_117.png" # HERMIONE
                her "Да, сэр."
                #__#hide screen h_head2
                $herViewHead.hideQ()
                hide screen h_c_u   # SUCKING
                show screen g_c_u # SUCKING
                with d3                      #  SUCKING
                

            "\"Твои родители должны гордиться тобой...\"":
                her "*Чавк--"
                $ hermione_chibi_xpos = -150 #-185 behind the desk. (Also 5 is something).
                $ hermione_chibi_ypos = 10
                $ h_c_u_pic = "hand_ani"
                show screen h_c_u
                hide screen g_c_u
                with d3
                #__#$ her_head_xpos=390 #Defines position of the Hermione's full length sprite. (Default 370). 140 - center. Bottom right: 390
                #__#$ her_head_ypos=235 #Defines position of the Hermione's full length sprite. (Default 0). Right bottom corner: 340 - head only. 235 - tits.
                #__#$ posHead = gMakePos( 390, 235 )
                #__#show screen h_head2                                                             # HERMIONE
                $herViewHead.showQ( "body_75.png", posHead )
                #__#$ h_body = "03_hp/13_hermione_main/body_75.png" # HERMIONE
                her "Да, я думаю, так и есть..."
                #__#show screen h_head2                                                             # HERMIONE
                $herViewHead.showQ( "body_74.png", posHead )
                #__#$ h_body = "03_hp/13_hermione_main/body_74.png" # HERMIONE
                her2 "Я отличная студентка, не смотря на то, что родилась в семье магглов..."
                #__#show screen h_head2                                                             # HERMIONE
                $herViewHead.showQ( "body_117.png", posHead )
                #__#$ h_body = "03_hp/13_hermione_main/body_117.png" # HERMIONE
                her2 "Хотя сначала они хотели отправить меня в \"Богус\", школу-интернат."
                #__#show screen h_head2                                                             # HERMIONE
                $herViewHead.showQ( "body_74.png", posHead )
                #__#$ h_body = "03_hp/13_hermione_main/body_74.png" # HERMIONE
                her2 "Потребовалось некоторое усилие, чтобы убедить их в том, что \"Хогвартс\" является респектабельным учреждением..."
                #__#hide screen h_head2     
                $herViewHead.hideQ()
                m "Да, действительно респектабельное учреждение."
                m "Положи член обратно в рот, девочка."
                hide screen h_c_u   # SUCKING
                show screen g_c_u # SUCKING
                with d3                      #  SUCKING
                her "*Чавк!* *Хлюп!* *Кулдык!*"
                #__#hide screen h_head2     
                $herViewHead.hideQ()
                m "Да, просто подержи его там некоторое время..."
                her "*Чавк!* *Хлюп!* *Хлюп!*"
                #__#hide screen h_head2     
                $herViewHead.hideQ()
                m "Хорошо, хорошо..."
                m "Итак, что бы сказали ваши родители, если бы увидели вас сейчас?"
                her "*Чавк--"
                show screen h_c_u   # NOT SUCKING
                hide screen g_c_u # NOT SUCKING
                with d3                      #  NOT SUCKING
                #__#show screen h_head2                                                             # HERMIONE
                $herViewHead.showQ( "body_87.png", posHead )
                #__#$ h_body = "03_hp/13_hermione_main/body_87.png" # HERMIONE
                her "Конечно же, они бы не поняли меня..."
                her "Но меня это не волнует."
                #__#show screen h_head2                                                             # HERMIONE
                $herViewHead.showQ( "body_120.png", posHead )
                #__#$ h_body = "03_hp/13_hermione_main/body_120.png" # HERMIONE
                her2 "Я не боюсь \"пачкать руки\" и делать то, что должно быть сделано."
                #__#hide screen h_head2     
                $herViewHead.hideQ()
                m "Ты немного непослушная, не так ли?"
                #__#show screen h_head2                                                             # HERMIONE
                $herViewHead.showQ( "body_122.png", posHead )
                #__#$ h_body = "03_hp/13_hermione_main/body_122.png" # HERMIONE
                her "Хмм, я думаю - я такая."
                #__#hide screen h_head2     
                $herViewHead.hideQ()
                m "Тогда возвращайся к минету. Покажи своим родителям какая ты."
                hide screen h_c_u   # SUCKING
                show screen g_c_u # SUCKING
                with d3                      #  SUCKING
                her "*Чавк!* *Чавк!* *Чавк!*"
                

            "\"Расскажи мне о факультете \"Гриффиндор\"\"":
                her "*Чавк-"
                $ hermione_chibi_xpos = -150 #-185 behind the desk. (Also 5 is something).
                $ hermione_chibi_ypos = 10
                $ h_c_u_pic = "hand_ani"
                show screen h_c_u
                hide screen g_c_u
                with d3
                #__#$ her_head_xpos=390 #Defines position of the Hermione's full length sprite. (Default 370). 140 - center. Bottom right: 390
                #__#$ her_head_ypos=235 #Defines position of the Hermione's full length sprite. (Default 0). Right bottom corner: 340 - head only. 235 - tits.
                #__#$ posHead = gMakePose( 390, 235 )
                #__#show screen h_head2                                                             # HERMIONE
                $herViewHead.showQ( "body_13.png", posHead )
                #__#$ h_body = "03_hp/13_hermione_main/body_13.png" # HERMIONE
                her "Разве я могу вам разсказать то, чего вы еще не знаете?"
                #__#hide screen h_head2     
                $herViewHead.hideQ()
                m "Да... Эмм... конечно я знаю все."
                m "Но я хочу посмотреть, как много знаешь ты!"
                m "Чтобы проверить твои знания по этому поводу."
                show screen blktone
                with d3
                ">Как только вы говорите о \"Проверке\", глаза Гермионы загораются волнением"
                hide screen blktone
                with d3
                #__#show screen h_head2                                                             # HERMIONE
                $herViewHead.showQ( "body_80.png", posHead )
                #__#$ h_body = "03_hp/13_hermione_main/body_80.png" # HERMIONE
                her "Хорошо, но мне нужно немного времени, что бы собраться с мыслями..."
                #__#hide screen h_head2  
                $herViewHead.hideQ()
                hide screen h_c_u   # SUCKING
                show screen g_c_u # SUCKING
                with d3                      #  SUCKING
                her "*Чавк!* *Чавк!* *Хлюп!*"
                m "Ох, конечно, используй столько времени, сколько потребуется."
                her "*Чавк!* *Хлюп!* *Чавк!*"
                her "*Хлюп--"
                show screen h_c_u   # NOT SUCKING
                hide screen g_c_u # NOT SUCKING
                with d3                      #  NOT SUCKING
                hide screen ctc
                #__#show screen h_head2                                                             # HERMIONE
                $herViewHead.showQ( "body_87.png", posHead )
                #__#$ h_body = "03_hp/13_hermione_main/body_87.png" # HERMIONE
                her2 "Факультет \"Гриффиндор\" был основан Годриком Гриффиндором, отсюда и название."
                her2 "Зверь на гербе \"Гриффиндор\" - Лев..."
                #__#show screen h_head2                                                             # HERMIONE
                $herViewHead.showQ( "body_127.png", posHead )
                #__#$ h_body = "03_hp/13_hermione_main/body_127.png" # HERMIONE
                her "Красный и золотой - цвета герба."
                #__#hide screen h_head2   
                $herViewHead.hideQ()
                hide screen h_c_u   # SUCKING
                show screen g_c_u # SUCKING
                with d3                      #  SUCKING 
                her "*Хлюп!* *Чавк!* *Чавк!*"
                show screen h_c_u   # NOT SUCKING
                hide screen g_c_u # NOT SUCKING
                with d3                      #  NOT SUCKING
                #__#show screen h_head2                                                             # HERMIONE
                $herViewHead.showQ( "body_127.png", posHead )
                #__#$ h_body = "03_hp/13_hermione_main/body_127.png" # HERMIONE
                her2 "Профессор Минерва Макгонагалл - глава дома."
                her2 "Дом \"Гриффиндор\" подчеркивает черты мужества..."
                her2 "Так же \"смелости, духа и храбрости\"..."
                her2 "И, таким образом, его члены, как правило, являются смелыми, но безрассудными..."
                #__#hide screen h_head2     
                $herViewHead.hideQ()
                hide screen h_c_u   # SUCKING
                show screen g_c_u # SUCKING
                with d3                      #  SUCKING
                her "*Чавк!* *Чавк!* *Чавк!*"
                show screen h_c_u   # NOT SUCKING
                hide screen g_c_u # NOT SUCKING
                with d3                      #  NOT SUCKING
                #__#show screen h_head2                                                             # HERMIONE
                $herViewHead.showQ( "body_127.png", posHead )
                #__#$ h_body = "03_hp/13_hermione_main/body_127.png" # HERMIONE
                her2 "\"Гриффиндор\" соответствует стихии огня..."
                her2 "По этой причине и были выбраны красный и золотой цвета."
                #__#hide screen h_head2     
                $herViewHead.hideQ()
                hide screen h_c_u   # SUCKING
                show screen g_c_u # SUCKING
                with d3                      #  SUCKING
                her "*Чавк!* *Хлюп!* *Чавк!*"
                m "Хмм..."
                m "Ну, я думаю, что могу немного высмеять тебя..."
                #__#hide screen h_head2     
                $herViewHead.hideQ()
                her "*Чавк??*"
                m "В \"Гриффиндоре\" описывается смелость, дух и храбрость..."
                m "Но тем не менее, ты - шлюха..."
                show screen h_c_u   # NOT SUCKING
                hide screen g_c_u # NOT SUCKING
                with d3                      #  NOT SUCKING
                #__#show screen h_head2                                                             # HERMIONE
                $herViewHead.showQ( "body_86.png", posHead )
                #__#$ h_body = "03_hp/13_hermione_main/body_86.png" # HERMIONE
                her "Профессор!"
                #__#hide screen h_head2     
                $herViewHead.hideQ()
                #__#hide screen h_head2     
                $herViewHead.hideQ()
                m "Но, честно говоря..."
                m "\"смелость, дух, храбрость, безрассудство\"..."
                m "Хорошо подходит твоей личности..."
                #__#show screen h_head2                                                             # HERMIONE
                $herViewHead.showQ( "body_45.png", posHead )
                #__#$ h_body = "03_hp/13_hermione_main/body_45.png" # HERMIONE
                her "Сэр..."
                #__#hide screen h_head2     
                $herViewHead.hideQ()
                hide screen h_c_u   # SUCKING
                show screen g_c_u # SUCKING
                with d3                      #  SUCKING
                her "*Кулдык!* *Хлюп!!* *Кулдык!!!*"
                m "Хорошая девочка..."
        
        m "Хорошо..."
        her "*Кулдык!* *Чавк!* *Чавк!*"
        m "Хорошо... Назад-вперед, Назад-вперед... Хорошая девочка."
        her "*Чавк!* *Чавк!* *Чавк!*"
        her "*Чавк--"
        show screen h_c_u   # NOT SUCKING
        hide screen g_c_u # NOT SUCKING
        with d3                      #  NOT SUCKING
        #__#show screen h_head2                                                             # HERMIONE
        $herViewHead.showQ( "body_87.png", posHead )
        #__#$ h_body = "03_hp/13_hermione_main/body_87.png" # HERMIONE
        her "Сэр... я... шлюха."
        #__#hide screen h_head2  
        $herViewHead.hideQ()
        m "Что?"
        hide screen h_c_u   # SUCKING
        show screen g_c_u # SUCKING
        with d3                      #  SUCKING
        her "*Чавк-Чавк-Чавк!*"
        show screen h_c_u   # NOT SUCKING
        hide screen g_c_u # NOT SUCKING
        with d3                      #  NOT SUCKING
        #__#show screen h_head2                                                             # HERMIONE
        $herViewHead.showQ( "body_117.png", posHead )
        #__#$ h_body = "03_hp/13_hermione_main/body_117.png" # HERMIONE
        her2 "Я действительно шлюха, я с наслаждением сосу ваш член..."
        #__#hide screen h_head2  
        $herViewHead.hideQ()
        m "Ох, говори больше об этом!"
        hide screen h_c_u   # SUCKING
        show screen g_c_u # SUCKING
        with d3                      #  SUCKING
        her "*Чавк!* *Хлюп!* *Чавк!*"
        show screen h_c_u   # NOT SUCKING
        hide screen g_c_u # NOT SUCKING
        with d3                      #  NOT SUCKING
        #__#show screen h_head2                                                             # HERMIONE
        $herViewHead.showQ( "body_121.png", posHead )
        #__#$ h_body = "03_hp/13_hermione_main/body_121.png" # HERMIONE
        her "Пожалуйста, сэр, кончайте для меня! "
        #__#hide screen h_head2  
        $herViewHead.hideQ()
        with hpunch
        g4 "АХХХ, ты маленькая шл--!!!"
        g4 "{size=-4}(Почти кончаю. Должен ли я предупредить её?){/size}"
        menu:
            m "..."
            "- Предупредить её -":
                #__#show screen h_head2                                                             # HERMIONE
                $herViewHead.showQ( "body_121.png", posHead )
                #__#$ h_body = "03_hp/13_hermione_main/body_121.png" # HERMIONE
                her "Да, я люблю сосать--"
                #__#hide screen h_head2  
                $herViewHead.hideQ()
                g4 "Скорее девочка, я почти кончил!"
                #__#show screen h_head2                                                             # HERMIONE
                $herViewHead.showQ( "body_18.png", posHead )
                #__#$ h_body = "03_hp/13_hermione_main/body_18.png" # HERMIONE
                her "!!!"
                #__#hide screen h_head2      
                $herViewHead.hideQ()
                show screen ctc
                pause
                show screen blkfade
                with d3
                $ g_c_u_pic = "cum_in_mouth_ani"
                hide screen h_c_u   # SUCKING
                show screen g_c_u # SUCKING
                with d3                      #  SUCKING
                ">Гермиона быстро кладет член в рот и продолжает сосать его с большей страстью"
                show screen white 
                pause.1
                hide screen white
                pause.2
                show screen white 
                pause .1
                hide screen white
                with hpunch
                g4 "{size=+7}АРГХ!{/size}"
                #Cumming.
                her "*Хлюп!-Хлюп!-Хлюп!*"
                with hpunch
                g4 "Еще немного!"
                her "*Хлюп!* *Хлюп!* *Хлюп!*"
                hide screen blkfade
                hide screen bld1
                with d3
                show screen ctc
                pause
                hide screen ctc
                show screen bld1
                with d3
                m "Что ж, я думаю, это все.."
                show screen h_c_u   # NOT SUCKING
                hide screen g_c_u # NOT SUCKING
                with d3                      #  NOT SUCKING
                #__#show screen h_head2                                                             # HERMIONE
                $herViewHead.showQ( "body_126.png", posHead )
                #__#$ h_body = "03_hp/13_hermione_main/body_126.png" # HERMIONE
                her ".............."
                #__#hide screen h_head2  
                $herViewHead.hideQ()
                m "Ты в порядке там, девочка?"
                #__#show screen h_head2                                                             # HERMIONE
                $herViewHead.showQ( "body_123.png", posHead )
                #__#$ h_body = "03_hp/13_hermione_main/body_123.png" # HERMIONE
                her "Да, сэр..."
                her "Это было слишком..."
                #__#hide screen h_head2  
                $herViewHead.hideQ()
                m "Тебе удалось проглотить это все."
                #__#show screen h_head2                                                             # HERMIONE
                $herViewHead.showQ( "body_123.png", posHead )
                #__#$ h_body = "03_hp/13_hermione_main/body_123.png" # HERMIONE
                her "Да... Я думала, что задохнусь..."
                her2 "Но я дала себе обещание, что с вашего члена не упадет ни капли!"
                #__#hide screen h_head2  
                $herViewHead.hideQ()
                m "Хорошая девочка."
                #__#show screen h_head2                                                             # HERMIONE
                $herViewHead.showQ( "body_123.png", posHead )
                #__#$ h_body = "03_hp/13_hermione_main/body_123.png" # HERMIONE
                her "Спасибо, сэр."
                her "Но, все-таки, это было слишком..."
                #__#show screen h_head2                                                             # HERMIONE
                $herViewHead.showQ( "body_121.png", posHead )
                #__#$ h_body = "03_hp/13_hermione_main/body_121.png" # HERMIONE
                her "Мне кажется, что я только что поела.."
                her "Мой желудок полон..."
                #__#hide screen h_head2  
                $herViewHead.hideQ()
                g9 "Да, я накормил тебя моей спермой!"
                if daytime:
                    #__#show screen h_head2                                                             # HERMIONE
                    $herViewHead.showQ( "body_121.png", posHead )
                    #__#$ h_body = "03_hp/13_hermione_main/body_121.png" # HERMIONE
                    her2 "Я думаю, что сегодня можно пойти на занятия без обеда."
                else:
                    #__#show screen h_head2                                                             # HERMIONE
                    $herViewHead.showQ( "body_121.png", posHead )
                    #__#$ h_body = "03_hp/13_hermione_main/body_121.png" # HERMIONE
                    her2 "Да, я думаю, можно пропустить ужин сегодня вечером"
                #__#show screen h_head2                                                             # HERMIONE
                $herViewHead.showQ( "body_122.png", posHead )
                #__#$ h_body = "03_hp/13_hermione_main/body_122.png" # HERMIONE
                her "Могу я получить оплату?"
                #__#hide screen h_head2  
                $herViewHead.hideQ()
                show screen ctc
                pause
                hide screen ctc
                show screen blkfade
                with d3
            "- Не беспокоиться -":
                #__#show screen h_head2                                                             # HERMIONE
                $herViewHead.showQ( "body_121.png", posHead )
                #__#$ h_body = "03_hp/13_hermione_main/body_121.png" # HERMIONE
                her "Да, я люблю сосать--"
                #__#hide screen h_head2  
                $herViewHead.hideQ()
                show screen white 
                pause.1
                hide screen white
                pause.2
                show screen white 
                pause .1
                hide screen white
                with hpunch
                g4 "{size=+7}Шлюха!{/size}"
                #__#show screen h_head2                                                             # HERMIONE
                $herViewHead.showQ( "body_48.png", posHead )
                #__#$ h_body = "03_hp/13_hermione_main/body_48.png" # HERMIONE
                her "!!?"
                #__#hide screen h_head2
                $herViewHead.hideQ()
                
                $ g_c_u_pic = "cum_on_face_ani"
                hide screen h_c_u   # SUCKING
                show screen g_c_u # SUCKING
                with d3                      #  SUCKING
                show screen ctc
                hide screen bld1
                with d3
                pause
                hide screen ctc
                show screen bld1
                with d3
                
                #Cumming.
                #__#$ uni_sperm = True
                #__#$ u_sperm = "03_hp/13_hermione_main/auto_07.png"
                $herViewHead.data().addItem( 'sperm', CharacterExItem( herViewHead.mMiscFolder, 'sperm_04.png', G_Z_FACE + 1 ) )

                #__#show screen h_head2                                                             # HERMIONE
                $herViewHead.showQ( "body_48.png", posHead )
                #__#$ h_body = "03_hp/13_hermione_main/body_48.png" # HERMIONE
                her "Профессор..."
                #__#hide screen h_head2  
                $herViewHead.hideQ()
                g4 "Не двигайся, девочка."
                g4 "Да, просто оставайся на месте."
                g4 "АХХХ, ты маленька шлюха, из-за тебя я кончаю сильнее, девочка!"
                #__#show screen h_head2                                                             # HERMIONE
                $herViewHead.showQ( "body_21.png", posHead )
                #__#$ h_body = "03_hp/13_hermione_main/body_21.png" # HERMIONE
                her ".............."
                #__#hide screen h_head2  
                $herViewHead.hideQ()
                m "Вот так..."
                $ g_c_u_pic = "cum_on_face_blink_ani"
                #__#show screen h_head2                                                             # HERMIONE
                $herViewHead.showQ( "body_33.png", posHead )
                #__#$ h_body = "03_hp/13_hermione_main/body_33.png" # HERMIONE
                her ".............."
                #__#hide screen h_head2  
                $herViewHead.hideQ()
                m "Хорошо, я закончил..."
                #__#show screen h_head2                                                             # HERMIONE
                $herViewHead.showQ( "body_31.png", posHead )
                #__#$ h_body = "03_hp/13_hermione_main/body_31.png" # HERMIONE
                her "................."
                if daytime:
                    her "Мои занятия скоро начнутся..."
                else:
                    pass
                #__#hide screen h_head2  
                $herViewHead.hideQ()
                m "Просто протри лицо и все будет в порядке.."
                #__#show screen h_head2                                                             # HERMIONE
                $herViewHead.showQ( "body_31.png", posHead )
                #__#$ h_body = "03_hp/13_hermione_main/body_31.png" # HERMIONE
                her "............"
                #__#hide screen h_head2  
                $herViewHead.hideQ()
                m "Ведь ты не хочешь, что бы..."
                #__#show screen h_head2                                                             # HERMIONE
                $herViewHead.showQ( "body_34.png", posHead )
                #__#$ h_body = "03_hp/13_hermione_main/body_34.png" # HERMIONE
                her "Хм?"
                #__#hide screen h_head2  
                $herViewHead.hideQ()
                m "Все..."
                m "Видели, какая ты маленькая шлюха!"
                #__#show screen h_head2                                                             # HERMIONE
                $herViewHead.showQ( "body_34.png", posHead )
                #__#$ h_body = "03_hp/13_hermione_main/body_34.png" # HERMIONE
                her "Конечно нет, сэр!"
                #__#hide screen h_head2  
                $herViewHead.hideQ()
                show screen ctc
                pause
                hide screen ctc
                show screen blkfade
                with d3
                stop music fadeout 1.0
                if daytime:
                    m "Тебе лучше пойти, что бы не опоздать на занятия.."
                else:
                    m "Осталось немного времени..."
                    #__#show screen h_head2                                                             # HERMIONE
                    $herViewHead.showQ( "body_34.png", posHead )
                    #__#$ h_body = "03_hp/13_hermione_main/body_34.png" # HERMIONE
                    her "Да..."
                #__#show screen h_head2                                                             # HERMIONE
                $herViewHead.showQ( "body_44.png", posHead )
                #__#$ h_body = "03_hp/13_hermione_main/body_44.png" # HERMIONE
                her "Могу я получить оплату?"
                #__#hide screen h_head2
                $herViewHead.hideQ()
                #__#$ aftersperm = True
                $herViewHead.data().addItem( 'sperm_after', CharacterExItem( herViewHead.mMiscFolder, 'sperm_00_after.png', G_Z_FACE + 2 ) )

        
        
    elif request_22_points == 1: #  <============================================================== EVENT 02
        m "Мисс Гренджер?"
        #__#hide screen hermione_main                                                                                                                                                                                   #HERMIONE
        #__#with d3                                                                                                                                                                                                                        #HERMIONE
        $herView.hideQQ()
        #__#$ h_xpos=140 #Defines position of the Hermione's full length sprite. (Default 370). (Center: 140)                                                       #HERMIONE
        #__#$ h_body = "03_hp/13_hermione_main/body_01.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
        #__#show screen hermione_main                                                                                                                                                                                 #HERMIONE
        #__#with d3                                         
        $herView.showQQ( "body_01.png", pos )
        her "Сэр?"
        m "Как насчет минета??"
        #__#hide screen hermione_main                                                                                                                                                                                   #HERMIONE
        #__#with d3                                                                                                                                                                                                                        #HERMIONE
        $herView.hideQQ()
        #__#$ h_xpos=140 #Defines position of the Hermione's full length sprite. (Default 370). (Center: 140)                                                       #HERMIONE
        #__#$ h_body = "03_hp/13_hermione_main/body_86.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
        #__#show screen hermione_main                                                                                                                                                                                 #HERMIONE
        #__#with d3                                         
        $herView.showQQ( "body_86.png", pos )
        play music "music/(Orchestral) Playful Tension by Shadow16nh.mp3" fadein 1 fadeout 1 # SEX THEME.
        her "Профессор, как вы смеете предлагать такое вашему ученику?!"
        m "Чт...?"
        #__#hide screen hermione_main                                                                                                                                                                                   #HERMIONE
        #__#with d3                                                                                                                                                                                                                        #HERMIONE
        $herView.hideQQ()
        #__#$ h_xpos=140 #Defines position of the Hermione's full length sprite. (Default 370). (Center: 140)                                                       #HERMIONE
        #__#$ h_body = "03_hp/13_hermione_main/body_86.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
        #__#show screen hermione_main                                                                                                                                                                                 #HERMIONE
        #__#with d3                                         
        $herView.showQQ( "body_86.png", pos )
        her "Это недостойно человека вашей должности!"
        #__#hide screen hermione_main                                                                                                                                                                                   #HERMIONE
        #__#with d3                                                                                                                                                                                                                        #HERMIONE
        $herView.hideQQ()
        #__#$ h_xpos=140 #Defines position of the Hermione's full length sprite. (Default 370). (Center: 140)                                                       #HERMIONE
        #__#$ h_body = "03_hp/13_hermione_main/body_47.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
        #__#show screen hermione_main                                                                                                                                                                                 #HERMIONE
        #__#with d3                                         
        $herView.showQQ( "body_47.png", pos )
        her "Вам должно быть стыдно за себя, сэр!"
        menu:
            m "???"
            "\"Прекрасно. Никаких очков! Уходи!\"":
                play music "music/Chipper Doodle v2.mp3" fadein 1 fadeout 1 # HERMIONE'S THEME.
                #__#hide screen hermione_main                                                                                                                                                                                   #HERMIONE
                #__#with d3                                                                                                                                                                                                                        #HERMIONE
                $herView.hideQQ()
                #__#$ h_xpos=140 #Defines position of the Hermione's full length sprite. (Default 370). (Center: 140)                                                       #HERMIONE
                #__#$ h_body = "03_hp/13_hermione_main/body_24.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
                #__#show screen hermione_main                                                                                                                                                                                 #HERMIONE
                #__#with d3                                         
                $herView.showQQ( "body_24.png", pos )
                her "Сэр, успокойтесь, пожалуйста"
                m "Покиньте кабинет, мисс Грейнджер"
                #__#hide screen hermione_main                                                                                                                                                                                   #HERMIONE
                #__#with d3                                                                                                                                                                                                                        #HERMIONE
                $herView.hideQQ()
                #__#$ h_xpos=140 #Defines position of the Hermione's full length sprite. (Default 370). (Center: 140)                                                       #HERMIONE
                #__#$ h_body = "03_hp/13_hermione_main/body_24.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
                #__#show screen hermione_main                                                                                                                                                                                 #HERMIONE
                #__#with d3                                         
                $herView.showQQ( "body_24.png", pos )
                her "Cэр, все что я сказала - было не всерьез."
                m "Что?"
            "\"Эм, извините?\"":
                stop music fadeout 1.0
                #__#hide screen hermione_main                                                                                                                                                                                   #HERMIONE
                #__#with d3                                                                                                                                                                                                                        #HERMIONE
                $herView.hideQQ()
                #__#$ h_xpos=140 #Defines position of the Hermione's full length sprite. (Default 370). (Center: 140)                                                       #HERMIONE
                #__#$ h_body = "03_hp/13_hermione_main/body_06.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
                #__#show screen hermione_main                                                                                                                                                                                 #HERMIONE
                #__#with d3                                         
                $herView.showQQ( "body_06.png", pos )
                her "*хи-хи*"
                m "Хмм?"
                #__#hide screen hermione_main                                                                                                                                                                                   #HERMIONE
                #__#with d3                                                                                                                                                                                                                        #HERMIONE
                $herView.hideQQ()
                #__#$ h_xpos=140 #Defines position of the Hermione's full length sprite. (Default 370). (Center: 140)                                                       #HERMIONE
                #__#$ h_body = "03_hp/13_hermione_main/body_24.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
                #__#show screen hermione_main                                                                                                                                                                                 #HERMIONE
                #__#with d3                                         
                $herView.showQQ( "body_24.png", pos )
                play music "music/Chipper Doodle v2.mp3" fadein 1 fadeout 1 # HERMIONE'S THEME.
                her "Поняла... cэр."
                m "Что?"
        #__#hide screen hermione_main                                                                                                                                                                                   #HERMIONE
        #__#with d3                                                                                                                                                                                                                        #HERMIONE
        $herView.hideQQ()
        #__#$ h_xpos=140 #Defines position of the Hermione's full length sprite. (Default 370). (Center: 140)                                                       #HERMIONE
        #__#$ h_body = "03_hp/13_hermione_main/body_45.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
        #__#show screen hermione_main                                                                                                                                                                                 #HERMIONE
        #__#with d3                                         
        $herView.showQQ( "body_45.png", pos )
        her "Ну, так много произошло за последнее время..."
        her2 "У меня было так много новых впечатлений, что я изменила свой взгляд на некоторые вещи..."
        her2 "Так что я просто пыталась представить себе, как \"я в прошлом\" отреагировала бы на это."
        m "Итак..."
        g4 "Вы плохо относитесь ко мне?"
        #__#hide screen hermione_main                                                                                                                                                                                   #HERMIONE
        #__#with d3                                                                                                                                                                                                                        #HERMIONE
        $herView.hideQQ()
        #__#$ h_xpos=140 #Defines position of the Hermione's full length sprite. (Default 370). (Center: 140)                                                       #HERMIONE
        #__#$ h_body = "03_hp/13_hermione_main/body_34.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
        #__#show screen hermione_main                                                                                                                                                                                 #HERMIONE
        #__#with d3                                         
        $herView.showQQ( "body_34.png", pos )
        her "Хм... мне жаль сэр, я не это имела ввиду..."
        g4 "Ты плохая девочка, ты должна быть наказана!"
        g9 "Я накажу тебя моим членом!"
        #__#hide screen hermione_main                                                                                                                                                                                   #HERMIONE
        #__#with d3                                                                                                                                                                                                                        #HERMIONE
        $herView.hideQQ()
        #__#$ h_xpos=140 #Defines position of the Hermione's full length sprite. (Default 370). (Center: 140)                                                       #HERMIONE
        #__#$ h_body = "03_hp/13_hermione_main/body_34.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
        #__#show screen hermione_main                                                                                                                                                                                 #HERMIONE
        #__#with d3                                         
        $herView.showQQ( "body_34.png", pos )
        her "..............................."

        jump blowjob_jumping
  
    elif request_22_points >= 2: # <============================================================== EVENT 03
        play music "music/(Orchestral) Playful Tension by Shadow16nh.mp3" fadein 1 fadeout 1 # SEX THEME.
        m "Соси мой член, девочка."
        #__#hide screen hermione_main                                                                                                                                                                                   #HERMIONE
        #__#with d3                                                                                                                                                                                                                        #HERMIONE
        $herView.hideQQ()
        #__#$ h_xpos=140 #Defines position of the Hermione's full length sprite. (Default 370). (Center: 140)                                                       #HERMIONE
        #__#$ h_body = "03_hp/13_hermione_main/body_45.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
        #__#show screen hermione_main                                                                                                                                                                                 #HERMIONE
        #__#with d3                                                                                                                                                                                                                         #HERMIONE                                                                                                                                                                                                                                          
        $herView.showQQ( "body_45.png", pos )
        her "Конечно..."
        # Sucking.
        
        #__#hide screen hermione_main                                                                                                                                                                                   #HERMIONE
        $herView.hideQ() #"WARNING_Z"
        hide screen genie
        $ genie_chibi_xpos = -150 #-185 behind the desk. (Also 5 is something).
        $ genie_chibi_ypos = 10
        $ g_c_u_pic = "blowjob_ani"
        show screen chair_02
        show screen g_c_u
        
        hide screen hermione_02 #Hermione stands still.
        hide screen blkfade
        hide screen blktone
        hide screen bld1
        show screen ctc
        with fade
        pause
        show screen bld1
        with d3
        
        her "*Чавк!* *Чавк!* *Чавк!*"
        m "Да, хорошая девочка..."
        her "*Чавк!* *Кулдык!* *Чавк!*"
        
        $ renpy.play('sounds/knocking.mp3') #Sound someone knocking on the door.
        "> *Тук-тук-тук!*"
        her "{size=+7}!!!{/size}"
        m "Хм?"
        if daytime:
            m "Кто бы это мог быть?"
        else:
            m "Кто бы это мог быть в такой час?"
        $ hermione_chibi_xpos = -150 #-185 behind the desk. (Also 5 is something).
        $ hermione_chibi_ypos = 10
        $ h_c_u_pic = "hand_ani" # Not sucking
        show screen h_c_u   # NOT SUCKING
        hide screen g_c_u # NOT SUCKING
        with d3                      #  NOT SUCKING
        
        #__#$ her_head_xpos=390 #Defines position of the Hermione's full length sprite. (Default 370). 140 - center. Bottom right: 390
        #__#$ her_head_ypos=235 #Defines position of the Hermione's full length sprite. (Default 0). Right bottom corner: 340 - head only. 235 - tits.
        $ posHead = gMakePos( 390, 235 )

        #__#show screen h_head2                                                             # HERMIONE
        $herViewHead.showQ( "body_48.png", posHead )
        #__#$ h_body = "03_hp/13_hermione_main/body_48.png" # HERMIONE
        her "(Профессор, что мне делать?)"
        #__#hide screen h_head2
        $herViewHead.hideQ()
        m "Просто продолжай сосать мой член, девочка. Это тебя не касается."
        sna "Альбус? Ты там? Мне нужно поговорить с тобой."
        #__#show screen h_head2                                                             # HERMIONE
        $herViewHead.showQ( "body_117.png", posHead )
        #__#$ h_body = "03_hp/13_hermione_main/body_117.png" # HERMIONE
        her "(Это профессор Снейп!)"
        her2 "(Сэр, пожалуйста, скажите что бы он ушел, я прошу вас!)"
        #__#hide screen h_head2
        $herViewHead.hideQ()
        menu:
            m "..."
            "\"Пожалуйста, заходите, Северус.\"":
                $ mad = 30
                #__#show screen h_head2                                                             # HERMIONE
                $herViewHead.showQ( "body_76.png", posHead )
                #__#$ h_body = "03_hp/13_hermione_main/body_76.png" # HERMIONE
                stop music fadeout 1.0
                her "(Сэр, нет!)"
                #__#hide screen h_head2
                $herViewHead.hideQ()
                show screen blktone
                with d3
                with hpunch
                ">Гермиона крепко сжимает ваши яйца."
                hide screen blktone
                with d3
                g4 "АУЧЬ!"
                hide screen bld1
                with d3
                # SNAPE COMES IN
                $ renpy.play('sounds/door.mp3') #Sound of a door opening.
                $ walk_xpos=610 #Animation of walking chibi. (From)
                $ walk_xpos2=360 #Coordinates of it's movement. (To)
                $ snapes_speed = 04.0 #The speed of moving the walking animation across the screen.
                show screen snape_walk_01 
                pause 4
                show screen snape_02 #Snape stands still.
                show screen bld1
                with d3
                $ s_head_xpos = 330 # x = 330,
                $ s_head_ypos = 340 #Right bottom corner: y = 340. y = 380 - no hand.
                $ s_sprite = "03_hp/10_snape_main/snape_01.png"
                show screen s_head2

                play music "music/Dark Fog.mp3" fadein 1 fadeout 1 # SNAPE'S THEME
                sna "Хорошо, что ты здесь."
                hide screen s_head2
                
                $ g_c_u_pic = "blowjob_ani" # sucking
                hide screen h_c_u   # SUCKING
                show screen g_c_u # SUCKING
                with d3                      #  SUCKING
                her "{size=-4}(*Чавк...* *Чавк...* *Хлюп...*){/size}"
                $ s_sprite = "03_hp/10_snape_main/snape_06.png" # SNAPE
                show screen s_head2                                                          # SNAPE
                sna "Слушай, есть кое что, что я хочу обсудить..."
                $ s_sprite = "03_hp/10_snape_main/snape_05.png" # SNAPE
                show screen s_head2                                                          # SNAPE
                sna "Хмм...?"
                sna "Джинни? Ты в порядке??"
                hide screen s_head2
                her "{size=-4}(Джинни!!? Кто здесь?!){/size}"
                her "{size=-4}(Нет, пожалуйста! Я умру от стыда!){/size}"
                m "Да, Северус, я в порядке..."
                her "{size=-4}(Что? *Чавк...?* *Чавк...?* *Хлюп...?*){/size}"
                $ s_sprite = "03_hp/10_snape_main/snape_05.png" # SNAPE
                show screen s_head2                                                          # SNAPE
                sna "На что вы смотрите?"
                hide screen s_head2
                m "Эмм... Просто любуюсь...{w} шкафом."
                m "Пожалуйста, продолжайте..."
                $ s_sprite = "03_hp/10_snape_main/snape_05.png" # SNAPE
                show screen s_head2                                                          # SNAPE
                sna "..............."
                hide screen s_head2
                her "{size=-4}(*Чавк...* *Чавк...* *Хлюп...*){/size}"
                m "Вы хотели что-то обсудить?"
                $ s_sprite = "03_hp/10_snape_main/snape_06.png" # SNAPE
                show screen s_head2                                                          # SNAPE
                sna "Да. Девченку Грейнджер."
                hide screen s_head2
                her "{size=-4}(*Чавк...!* *Кулдык...!* *Хлюп...!*){/size}"
                m "Ох... Что с ней?"
                $ s_sprite = "03_hp/10_snape_main/snape_04.png" # SNAPE
                show screen s_head2                                                          # SNAPE
                sna2 "Вы обещали, что вы будете присматривать за маленькой ведьмой."
                hide screen s_head2
                her "{size=-4}(*Чавк...* *Чавк...* *Хлюп...*){/size}"
                $ s_sprite = "03_hp/10_snape_main/snape_04.png" # SNAPE
                show screen s_head2                                                          # SNAPE
                sna "Но она по-прежнему досаждает мне!"
                sna "Ее тактика изменилась..."
                $ s_sprite = "03_hp/10_snape_main/snape_03.png" # SNAPE
                show screen s_head2                                                          # SNAPE
                sna2 "Но ей все еще удается довести меня до горя..."
                hide screen s_head2
                m "Я понимаю... ах..."
                $ s_sprite = "03_hp/10_snape_main/snape_10.png" # SNAPE
                show screen s_head2                                                          # SNAPE
                sna "Эта девочка сводит меня с ума!"
                hide screen s_head2
                g4 "Да, она сводит меня с ума, а... ах..."
                her "{size=-4}(*Чавк...* *Чавк...* *Хлюп...*){/size}"
                $ s_sprite = "03_hp/10_snape_main/snape_04.png" # SNAPE
                show screen s_head2                                                          # SNAPE
                sna "Будете ли вы присматривать за ней?"
                hide screen s_head2
                m "Да. Она получит то, что заслуживает."
                $ s_sprite = "03_hp/10_snape_main/snape_06.png" # SNAPE
                show screen s_head2                                                          # SNAPE
                sna "Хорошо. Это все, что я хотел услышать."
                if daytime:
                    hide screen s_head2
                    m "Ну, у нас был хороший день, Северус."
                    $ s_sprite = "03_hp/10_snape_main/snape_06.png" # SNAPE
                    show screen s_head2                                                          # SNAPE
                    sna "Да, спасибо."
                else:
                    hide screen s_head2
                    m "Спокойной ночи, Северус."
                    $ s_sprite = "03_hp/10_snape_main/snape_06.png" # SNAPE
                    show screen s_head2                                                          # SNAPE
                    sna "Верно..."
                # SNAPE LEAVES
                hide screen s_head2
                hide screen ctc
                
                hide screen bld1
                with d3
                $ walk_xpos=360 #Animation of walking chibi. (From desk)
                $ walk_xpos2=610 #Coordinates of it's movement. (To the door)
                $ snapes_speed = 03.0 #The speed of moving the walking animation across the screen.
                show screen snape_walk_01_f 
                pause 3
                $ renpy.play('sounds/door.mp3') #Sound of a door opening.
                hide screen snape_walk_01_f 
                with d4
                pause.5
                show screen ctc
                stop music fadeout 1.0
                pause
                hide screen ctc
                show screen blkfade
                with d5
    
                play music "music/(Orchestral) Playful Tension by Shadow16nh.mp3" fadein 1 fadeout 1 # SEX THEME.
                ">Гермиона не сказала ни слова. Ее лицо покраснело из-за смущения, вины и волнения."
                ">Однако, не смотря на то, что она так растеряна и уязвима, она все еще старательно продолжает выполнять свою задачу."
                g4 "(Я почти кончил!)"

                
            "\"Я сейчас занят, Северус.\"":
                #__#show screen h_head2                                                             # HERMIONE
                $herViewHead.showQ( "body_117.png", posHead )
                #__#$ h_body = "03_hp/13_hermione_main/body_117.png" # HERMIONE
                her "(Спасибо вам, сэр.)"
                #__#hide screen h_head2                                                          
                $herViewHead.hideQ()
                sna "Занят чем?"
                sna "Все, что тебе нужно делать - это сидеть на заднице весь день."
                sna "Мне действительно нужно поговорить с тобой кое о чем."
                m "Я сказал, что занят, Северус."
                m "Понял? Я \"занят\"!"
                sna "Охх, ты имеешь ввиду то самое \"Занят\"? Я-я-ясно!"
                sna "Ну, тогда я зайду позже."
                #">Hermione keeps sucking on your cock with a rather fierce determination."
                
                $ hermione_chibi_xpos = -150 #-185 behind the desk. (Also 5 is something).
                $ hermione_chibi_ypos = 10
                $ h_c_u_pic = "hand_ani" # Not sucking
                hide screen h_c_u   # SUCKING
                show screen g_c_u # SUCKING
                with d3                      #  SUCKING                
                #">Hermione is working hard to please you..."
                her "*Чавк!* *Чавк!* *Хлюп!*"
                show screen blktone
                with d3
                ">Гермиона продолжает усерднее сосать ваш член"
                ">Ей не хватает техники, но она сосет его с особым усилием"
                hide screen blktone
                with d3
                m "Да ... Я люблю ваш жадный, маленький рот, девочка ..."
                her "*Кулдык!* *Кулдык!* *Кулдык!*"
                $ hermione_chibi_xpos = -150 #-185 behind the desk. (Also 5 is something).
                $ hermione_chibi_ypos = 10
                $ h_c_u_pic = "hand_ani" # Not sucking
                show screen h_c_u   # NOT SUCKING
                hide screen g_c_u # NOT SUCKING
                with d3                      #  NOT SUCKING
                #__#show screen h_head2                                                             # HERMIONE
                $herViewHead.showQ( "body_121.png", posHead )
                #__#$ h_body = "03_hp/13_hermione_main/body_121.png" # HERMIONE
                her "Сэр?"
                #__#hide screen h_head2          
                $herViewHead.hideQ()
                m "Хм?"
                #__#show screen h_head2                                                             # HERMIONE
                $herViewHead.showQ( "body_121.png", posHead )
                #__#$ h_body = "03_hp/13_hermione_main/body_121.png" # HERMIONE
                her "Вы кончите мне на лицо сегодня?"
                her "Или вы планируете кончить в рот?"
                #__#hide screen h_head2
                $herViewHead.hideQ()
                menu:
                    "\"Я планирую забрызгать твое лицо спермой!\"":
                        #__#show screen h_head2                                                             # HERMIONE
                        $herViewHead.showQ( "body_121.png", posHead )
                        #__#$ h_body = "03_hp/13_hermione_main/body_121.png" # HERMIONE
                        her "Я понимаю..."
                        #__#hide screen h_head2
                        $herViewHead.hideQ()
                        m "Почему ты спрашиваешь?"
                        #__#show screen h_head2                                                             # HERMIONE
                        $herViewHead.showQ( "body_123.png", posHead )
                        #__#$ h_body = "03_hp/13_hermione_main/body_123.png" # HERMIONE
                        her2 "Ох... Я прочитала в книге, что сперма содержит много антиоксидантов."
                        her "Это хорошо для кожи..."
                        #__#hide screen h_head2
                        $herViewHead.hideQ()
                        m "Отлично."
                        m "Возвращайся к работе."
                    "\"Я планирую кончить тебе в рот!\"":
                        #__#show screen h_head2                                                             # HERMIONE
                        $herViewHead.showQ( "body_123.png", posHead )
                        #__#$ h_body = "03_hp/13_hermione_main/body_123.png" # HERMIONE
                        her "Я понимаю..."
                        #__#hide screen h_head2
                        $herViewHead.hideQ()
                        m "Почему ты спрашиваешь?"
                        #__#show screen h_head2                                                             # HERMIONE
                        $herViewHead.showQ( "body_121.png", posHead )
                        #__#$ h_body = "03_hp/13_hermione_main/body_121.png" # HERMIONE
                        her2 "Ну, я пытаюсь следить за потреблением каллорий..."
                        her2 "Мне просто интересно, сколько каллорий содержит ваша сперма."
                        her2 "Может, мне стоит пропустить следующий прием пищи..."
                        #__#hide screen h_head2
                        $herViewHead.hideQ()
                        m "Девочка."
                        #__#show screen h_head2                                                             # HERMIONE
                        $herViewHead.showQ( "body_121.png", posHead )
                        #__#$ h_body = "03_hp/13_hermione_main/body_121.png" # HERMIONE
                        her "Да?"
                        #__#hide screen h_head2
                        $herViewHead.hideQ()
                        m "Положи член в рот."
                    "\"Я не планирую так далеко вперед,.\"":
                        #__#show screen h_head2                                                             # HERMIONE
                        $herViewHead.showQ( "body_121.png", posHead )
                        #__#$ h_body = "03_hp/13_hermione_main/body_121.png" # HERMIONE
                        her "Я понимаю..."
                        #__#hide screen h_head2
                        $herViewHead.hideQ()
                        m "Ты не любишь сюрпризов?"
                        #__#show screen h_head2                                                             # HERMIONE
                        $herViewHead.showQ( "body_121.png", posHead )
                        #__#$ h_body = "03_hp/13_hermione_main/body_121.png" # HERMIONE
                        her "На самом деле, не то, что бы не люблю..."
                        her "Скорее, мне нравится планировать все наперед..."
                        #__#hide screen h_head2
                        $herViewHead.hideQ()
                        m "Ну, некоторые вещи в жизни просто непредсказуемы."
                        m "Существует только один способ узнать наверняка."
                        
                    "\"А что бы ты хотела?\"":
                        #__#show screen h_head2                                                             # HERMIONE
                        $herViewHead.showQ( "body_121.png", posHead )
                        #__#$ h_body = "03_hp/13_hermione_main/body_121.png" # HERMIONE
                        her "Если вы все же разрешите мне выбрать, сэр..."
                        if generating_points == 1:
                            #__#show screen h_head2                                                             # HERMIONE
                            $herViewHead.showQ( "body_123.png", posHead )
                            #__#$ h_body = "03_hp/13_hermione_main/body_123.png" # HERMIONE
                            her2 "Я бы хотела, что бы вы кончили мне на лицо"
                            her2 "Я читала, что это хорошо для кожи"
                        else:
                            #__#show screen h_head2                                                             # HERMIONE
                            $herViewHead.showQ( "body_123.png", posHead )
                            #__#$ h_body = "03_hp/13_hermione_main/body_123.png" # HERMIONE
                            her2 "Я бы хотела, что бы вы кончили мне в рот."
                            her2 "Вы обычно обильно кончаете, и я надеялась пропустить следующий прием пищи..."
                            her2 "И сделать больше домашнего задания."
                        #__#hide screen h_head2
                        $herViewHead.hideQ()
                        m "Хорошо, я подумаю."
                        m "Продолжай сосать."
                    
                    
                $ hermione_chibi_xpos = -150 #-185 behind the desk. (Also 5 is something).
                $ hermione_chibi_ypos = 10
                $ h_c_u_pic = "hand_ani" # Not sucking
                hide screen h_c_u   # SUCKING
                show screen g_c_u # SUCKING
                with d3                      #  SUCKING   
                her "*Чавк!* *Чавк!* *Чавк!*"
                m "Хм..."
                m "У тебя получается всё лучше и лучше."
                her "*Чавк!* *Чавк!* *Хлюп!*"
                m "Хорошо, скажи какую-нибудь гадость..."
                her "*Чавк--?"
                $ hermione_chibi_xpos = -150 #-185 behind the desk. (Also 5 is something).
                $ hermione_chibi_ypos = 10
                $ h_c_u_pic = "hand_ani" # Not sucking
                show screen h_c_u   # NOT SUCKING
                hide screen g_c_u # NOT SUCKING
                with d3                      #  NOT SUCKING
                #__#show screen h_head2                                                             # HERMIONE
                $herViewHead.showQ( "body_118.png", posHead )
                #__#$ h_body = "03_hp/13_hermione_main/body_118.png" # HERMIONE
                her "Хмм..."
                #__#show screen h_head2                                                             # HERMIONE
                $herViewHead.showQ( "body_117.png", posHead )
                #__#$ h_body = "03_hp/13_hermione_main/body_117.png" # HERMIONE
                her "Я ем тараканов?"
                #__#hide screen h_head2
                $herViewHead.hideQ()
                m "...Что за херня?"
                #__#show screen h_head2                                                             # HERMIONE
                $herViewHead.showQ( "body_117.png", posHead )
                #__#$ h_body = "03_hp/13_hermione_main/body_117.png" # HERMIONE
                her "О-они довольно противны, сэр..."
                #__#hide screen h_head2
                $herViewHead.hideQ()
                m "Нет, девочка, я иммел ввиду что нибудь грязное!"
                m "И не смей говорить \"грязь\"!"
                m "Я имею ввиду что-нибудь в сексуальном направлении!"
                #__#show screen h_head2                                                             # HERMIONE
                $herViewHead.showQ( "body_118.png", posHead )
                #__#$ h_body = "03_hp/13_hermione_main/body_118.png" # HERMIONE
                her "Ох... Эмм..."
                #__#hide screen h_head2
                $herViewHead.hideQ()
                m "Ох, забудь..."
                #__#show screen h_head2                                                             # HERMIONE
                $herViewHead.showQ( "body_117.png", posHead )
                #__#$ h_body = "03_hp/13_hermione_main/body_117.png" # HERMIONE
                her "Эмм... Извините сэр."
                #__#hide screen h_head2
                $herViewHead.hideQ()
                m "Да плевать, соси мой член сильнее."
                #__#show screen h_head2                                                             # HERMIONE
                $herViewHead.showQ( "body_120.png", posHead )
                #__#$ h_body = "03_hp/13_hermione_main/body_120.png" # HERMIONE
                her "Конечно сэр."
                #__#hide screen h_head2
                $herViewHead.hideQ()
                
                $ hermione_chibi_xpos = -150 #-185 behind the desk. (Also 5 is something).
                $ hermione_chibi_ypos = 10
                $ h_c_u_pic = "hand_ani" # Not sucking
                hide screen h_c_u   # SUCKING
                show screen g_c_u # SUCKING
                with d3                      #  SUCKING 
                
                her "*Чавк!* *Хлюп!* *Хлюп!*"
                m "Да, вот так... хорошо..."
                her "*Хлюп!* *Хлюп!* *Хлюп!*"
                m "Знаешь... Я уже почти...."
                her "*Хлюп!* *Хлюп!* *Хлюп!*"
                m "Да, точно... ещё чуть-чуть."
                her "*Чавк!* *Хлюп!* *Хлюп!*"
                m "Отлично, малышка, ещё чуть-чуть, ещё немного...."
                g4 "Покажи что ты умеешь...."
                her "!!! *Хлюп-хлюп-хлюп-хлюп!* !!!"
                g4 "Да, да, вот так!"
                her "{size=+5}!!! *Хлюп-Хлюп-чавк-хлюп!* !!!{/size}"
                g4 "{size=+5}Да! Да! Да! Да!{/size}"
                g4 "Чавк!!!"
                
        menu:
            g4 "!!!"
            "- Кончить в её рот -":
                hide screen blkfade
                with d3
                g4 "Да, малышка, вот сейчас! Готовься быстро всё проглотить!"
                her "!!!"
                
                #__#hide screen h_head2      
                $herViewHead.hideQ()
                show screen ctc
                pause
                show screen blkfade
                with d3
                $ g_c_u_pic = "cum_in_mouth_ani"
                hide screen h_c_u   # SUCKING
                show screen g_c_u # SUCKING
                with d3                      #  SUCKING
                show screen white 
                pause.1
                hide screen white
                pause.2
                show screen white 
                pause .1
                hide screen white
                with hpunch
                рук "{size=+7}Глап!{/size}"
                g4 "Да, глотай всё, шлюха!"
                #Cumming.
                her "*Хлюп!-Хлюп!-Хлюп!*"
                with hpunch
                g4 "Да! Глотай своим грязным ртом!"
                her "*Хлюп-хлюп-Хлюп-Хлюп-хлюп!*"
                hide screen blkfade
                hide screen bld1
                with d3
                show screen ctc
                stop music fadeout 1.0
                pause
                hide screen ctc
                show screen bld1
                with d3
                m "Ну, думаю, на сегодня всё."
                m "Ты можешь идти..."
                show screen h_c_u   # NOT SUCKING
                hide screen g_c_u # NOT SUCKING
                with d3                      #  NOT SUCKING
                #__#show screen h_head2                                                             # HERMIONE
                $herViewHead.showQ( "body_125.png", posHead )
                #__#$ h_body = "03_hp/13_hermione_main/body_125.png" # HERMIONE
                her "..........................."
                her "................"
                her "........"
                #__#show screen h_head2                                                             # HERMIONE
                $herViewHead.showQ( "body_126.png", posHead )
                #__#$ h_body = "03_hp/13_hermione_main/body_126.png" # HERMIONE
                $ renpy.play('sounds/gulp.mp3') #Sound of gulping down a liquid.
                her "*Хлюп!*"
                #__#show screen h_head2                                                             # HERMIONE
                $herViewHead.showQ( "body_115.png", posHead )
                #__#$ h_body = "03_hp/13_hermione_main/body_115.png" # HERMIONE
                her "Хлюп-чавк..."
                #__#hide screen h_head2  
                $herViewHead.hideQ()
                m "Ты в порядке?"
                #__#show screen h_head2                                                             # HERMIONE
                $herViewHead.showQ( "body_123.png", posHead )
                #__#$ h_body = "03_hp/13_hermione_main/body_123.png" # HERMIONE
                play music "music/Chipper Doodle v2.mp3" fadein 1 fadeout 1 # HERMIONE'S THEME.
                her "Да, профессор..."
                #__#hide screen h_head2  
                $herViewHead.hideQ()
                m "Ты не собираешься идти поесть?"
                #__#show screen h_head2                                                             # HERMIONE
                $herViewHead.showQ( "body_123.png", posHead )
                #__#$ h_body = "03_hp/13_hermione_main/body_123.png" # HERMIONE
                her "Видимо, не пойду..."
                her "Вы всегда кончаете так обильно, сэр..."
                #__#hide screen h_head2  
                $herViewHead.hideQ()
                m "Хех... Ну и кто же виноват в этом??"
                #__#show screen h_head2                                                             # HERMIONE
                $herViewHead.showQ( "body_123.png", posHead )
                #__#$ h_body = "03_hp/13_hermione_main/body_123.png" # HERMIONE
                her "............." #Smile.
                her "Могу я получить оплату?"
                #__#hide screen h_head2  
                $herViewHead.hideQ()
                show screen ctc
                pause
                hide screen ctc
                show screen blkfade
                with d3

                
            "- Кончить на её лицо -":
                show screen bld1
                hide screen blkfade
                $ hermione_chibi_xpos = -150 #-185 behind the desk. (Also 5 is something).
                $ hermione_chibi_ypos = 10
                $ h_c_u_pic = "hand_ani" # Not sucking
                show screen h_c_u   # NOT SUCKING
                hide screen g_c_u # NOT SUCKING
                with d3                      #  NOT SUCKING
                g4 "Готова почувствовать сперму на лице, девочка?"
                #__#show screen h_head2                                                             # HERMIONE
                $herViewHead.showQ( "body_123.png", posHead )
                #__#$ h_body = "03_hp/13_hermione_main/body_123.png" # HERMIONE
                her "Да, сэр!"
                #__#hide screen h_head2      
                $herViewHead.hideQ()
                g4 "Тогда получай!"
                
                #__#hide screen h_head2  
                $herViewHead.hideQ()
                show screen white 
                pause.1
                hide screen white
                pause.2
                show screen white 
                pause .1
                hide screen white
                with hpunch
                g4 "{size=+7}Шлюха!{/size}"
                #__#show screen h_head2                                                             # HERMIONE
                $herViewHead.showQ( "body_48.png", posHead )
                #__#$ h_body = "03_hp/13_hermione_main/body_48.png" # HERMIONE
                her "!!?"
                #__#hide screen h_head2
                $herViewHead.hideQ()
                
                $ g_c_u_pic = "cum_on_face_ani"
                hide screen h_c_u   # SUCKING
                show screen g_c_u # SUCKING
                with d3                      #  SUCKING
                show screen ctc
                hide screen bld1
                with d3
                pause
                hide screen ctc
                show screen bld1
                with d3
                
                #Cumming.
                #__#$ uni_sperm = True
                #__#$ u_sperm = "03_hp/13_hermione_main/auto_07.png"
                $herViewHead.data().addItem( 'sperm', CharacterExItem( herViewHead.mMiscFolder, 'sperm_04.png', G_Z_FACE + 1 ) )
                #__#show screen h_head2                                                             # HERMIONE
                $herViewHead.showQ( "body_48.png", posHead )
                #__#$ h_body = "03_hp/13_hermione_main/body_48.png" # HERMIONE
                her "Профессор..."
                #__#hide screen h_head2  
                $herViewHead.hideQ()
                g4 "Всё на твоем грязном лице!"
                #__#show screen h_head2                                                             # HERMIONE
                $herViewHead.showQ( "body_123.png", posHead )
                #__#$ h_body = "03_hp/13_hermione_main/body_123.png" # HERMIONE
                her "Аааа!"
                $ g_c_u_pic = "cum_on_face_blink_ani"
                #__#hide screen h_head2  
                $herViewHead.hideQ()
                m "Ладно, я всё."
                #__#show screen h_head2                                                             # HERMIONE
                $herViewHead.showQ( "body_123.png", posHead )
                #__#$ h_body = "03_hp/13_hermione_main/body_123.png" # HERMIONE
                her "...................................."
                #__#hide screen h_head2  
                $herViewHead.hideQ()
                m "Я сказал всё, девочка."
                #__#show screen h_head2                                                             # HERMIONE
                $herViewHead.showQ( "body_123.png", posHead )
                #__#$ h_body = "03_hp/13_hermione_main/body_123.png" # HERMIONE
                her "Да, я слышала вас, сэр..."
                #__#hide screen h_head2  
                $herViewHead.hideQ()
                m "Ну и... Ты не собираешься умыться?"
                #__#show screen h_head2                                                             # HERMIONE
                $herViewHead.showQ( "body_123.png", posHead )
                #__#$ h_body = "03_hp/13_hermione_main/body_123.png" # HERMIONE
                her "Секундочку..."
                her2 "Я даю своей коже время, что бы впитать антиоксиданты..." 
                #__#hide screen h_head2  
                $herViewHead.hideQ()
                m "Ммм... Вот как, меня это заводит..."
                m "Не торопись, девочка..."
                show screen blkfade
                with d3
                stop music fadeout 1.0 
                ">Минутой позже."
                #__#$ uni_sperm = False
                $herViewHead.data().delItem( 'sperm' )
                $herViewHead.data().addItem( 'sperm_after', CharacterExItem( herViewHead.mMiscFolder, 'sperm_00_after.png', G_Z_FACE + 1 ) )
                #__#$ aftersperm = True
                #__#show screen h_head2                                                             # HERMIONE
                $herViewHead.showQ( "body_122.png", posHead )
                #__#$ h_body = "03_hp/13_hermione_main/body_122.png" # HERMIONE
                her "Мне кажется, вам нравится, сэр?"
                #__#hide screen h_head2  
                $herViewHead.hideQ()
                play music "music/Chipper Doodle v2.mp3" fadein 1 fadeout 1 # HERMIONE'S THEME.
                m "Да, девочка, мне нравится."
                #__#show screen h_head2                                                             # HERMIONE
                $herViewHead.showQ( "body_123.png", posHead )
                #__#$ h_body = "03_hp/13_hermione_main/body_123.png" # HERMIONE
                her "Хорошо, так мы можем расчитаться?"
                #__#hide screen h_head2  
                $herViewHead.hideQ()
                
                    
                
            
        
    
    #__#$ uni_sperm = False #Sperm layer is not displayed in hermione screen.
    $herViewHead.data().delItem( 'sperm' )
    $ gryffindor += current_payout #35
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
    
    #__#$ badges = True # Turns the badges layer of hermione_main back on.
    
    m "Да, мисс Грейнджер. 55 очков \"Гриффиндору\"." 
    $ gryffindor +=55
    #__#$ h_xpos=140 #Defines position of the Hermione's full length sprite. (Default 370). (Center: 140)
    #__#$ h_body = "03_hp/13_hermione_main/body_13.png" #Flashing panties
    #__#show screen hermione_main
    $herView.showQ( "body_13.png", pos ) #"WARNING_Z"
    hide screen hermione_01_f #Hermione stands still.
    with d3
    her "Спасибо, сэр..."

    if whoring <= 17:
        $ whoring +=1

    
    
    if request_22_points == 0:
        $ new_request_22_01 = True #  HEARTS
    if request_22_points == 1:
        $ new_request_22_02 = True #  HEARTS
    if request_22_points >= 2:
        $ new_request_22_03 = True #  HEARTS

    $ request_22_points += 1

    hide screen bld1
    #__#hide screen hermione_main
    $herView.hideQ() #"WARNING_Z"
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

    #__#$ aftersperm = False #Show cum stains on Hermione's uniform.
    $herView.data().loadState()
    
    call music_block
    
    if daytime:
        $ hermione_takes_classes = True
        jump night_main_menu
    else:
        $ hermione_sleeping = True
        jump day_main_menu            
