###################REQUEST_22 (Level 06) (55 pt.) (Blowjob). 
label new_request_22: #LV.6 (Whoring = 15 - 17)
    hide screen hermione_main 
    with d3
    if request_22_points == 0:
        m "{size=-4}(Попросить девчонку сделать мне минет?){/size}"
    else:
        m "{size=-4}(Попросить девчонку, сделать мне еще один минет?){/size}"
    $ menu_x = 0.5 #Default position of the menu (0.5). Version B is $ menu_x = 0.2
    menu:
        "\"(Да! Сделаем это!)\"":
            show screen blktone
            with d3
            pass
        "\"(Не сейчас.)\"":
            jump new_personal_request
            
 
    if request_22_points == 0: # FIRST EVENT <============================================================== EVENT 01
        m "Мисс Гренджер??"
        hide screen hermione_main                                                                                                                                                                                   #HERMIONE
        with d3                                                                                                                                                                                                                        #HERMIONE
        $ h_xpos=140 #Defines position of the Hermione's full length sprite. (Default 370). (Center: 140)                                                       #HERMIONE
        $ h_body = "03_hp/13_hermione_main/body_01.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
        show screen hermione_main                                                                                                                                                                                 #HERMIONE
        with d3                                                                                                                                                                                                                        #HERMIONE
        her "Да профессор?"
        m "Сегодня, я планирую дать \"Гриффиндору\" 55 очков..."
        m "Если вы у меня отсосешь..."
        if whoring <=14: # LEVEL 05
            jump too_much
        hide screen hermione_main                                                                                                                                                                                   #HERMIONE
        with d3                                                                                                                                                                                                                        #HERMIONE
        $ h_xpos=140 #Defines position of the Hermione's full length sprite. (Default 370). (Center: 140)                                                       #HERMIONE
        $ h_body = "03_hp/13_hermione_main/body_87.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
        show screen hermione_main                                                                                                                                                                                 #HERMIONE
        with d3                                                                                                                                                                                                                        #HERMIONE
        her "Ох..."
        hide screen hermione_main                                                                                                                                                                                   #HERMIONE
        with d3                                                                                                                                                                                                                        #HERMIONE
        $ h_xpos=140 #Defines position of the Hermione's full length sprite. (Default 370). (Center: 140)                                                       #HERMIONE
        $ h_body = "03_hp/13_hermione_main/body_124.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
        show screen hermione_main                                                                                                                                                                                 #HERMIONE
        with d3                                                                                                                                                                                                                        #HERMIONE
        her "Хорошо."
        m "Серьезно? просто так?"
        hide screen hermione_main                                                                                                                                                                                   #HERMIONE
        with d3                                                                                                                                                                                                                        #HERMIONE
        $ h_xpos=140 #Defines position of the Hermione's full length sprite. (Default 370). (Center: 140)                                                       #HERMIONE
        $ h_body = "03_hp/13_hermione_main/body_118.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
        show screen hermione_main                                                                                                                                                                                 #HERMIONE
        with d3                                                                                                                                                                                                                        #HERMIONE
        her "Да, я знаю что должна чувствовать себя неловко..."
        hide screen hermione_main                                                                                                                                                                                   #HERMIONE
        with d3                                                                                                                                                                                                                        #HERMIONE
        $ h_xpos=140 #Defines position of the Hermione's full length sprite. (Default 370). (Center: 140)                                                       #HERMIONE
        $ h_body = "03_hp/13_hermione_main/body_117.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
        show screen hermione_main                                                                                                                                                                                 #HERMIONE
        with d3                                                                                                                                                                                                                        #HERMIONE
        her "Но, почему то, я чувствую себя нормально..."
        hide screen hermione_main                                                                                                                                                                                   #HERMIONE
        with d3                                                                                                                                                                                                                        #HERMIONE
        $ h_xpos=140 #Defines position of the Hermione's full length sprite. (Default 370). (Center: 140)                                                       #HERMIONE
        $ h_body = "03_hp/13_hermione_main/body_124.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
        show screen hermione_main                                                                                                                                                                                 #HERMIONE
        with d3                                                                                                                                                                                                                        #HERMIONE
        her "Я думаю, я просто рада, что могу помочь Гриффиндру...."
        hide screen hermione_main                                                                                                                                                                                   #HERMIONE
        with d3                                                                                                                                                                                                                        #HERMIONE
        $ h_xpos=140 #Defines position of the Hermione's full length sprite. (Default 370). (Center: 140)                                                       #HERMIONE
        $ h_body = "03_hp/13_hermione_main/body_120.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
        show screen hermione_main                                                                                                                                                                                 #HERMIONE
        with d3                                                                                                                                                                                                                        #HERMIONE
        her "И если я должна сделать вам минет, то пусть так и будет..."
        m "Ну что же, хорошо."
        hide screen hermione_main                                                                                                                                                                                   #HERMIONE
        with d3                                                                                                                                                                                                                        #HERMIONE
        $ h_xpos=140 #Defines position of the Hermione's full length sprite. (Default 370). (Center: 140)                                                       #HERMIONE
        $ h_body = "03_hp/13_hermione_main/body_118.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
        show screen hermione_main                                                                                                                                                                                 #HERMIONE
        with d3                                                                                                                                                                                                                        #HERMIONE
        her "Хотя теперь, когда я говорю это вслух, мне это не нравится!..."
        m "Слишком поздно, ты уже сказала \"Да\"!"
        hide screen hermione_main                                                                                                                                                                                   #HERMIONE
        with d3                                                                                                                                                                                                                        #HERMIONE
        $ h_xpos=140 #Defines position of the Hermione's full length sprite. (Default 370). (Center: 140)                                                       #HERMIONE
        $ h_body = "03_hp/13_hermione_main/body_24.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
        show screen hermione_main                                                                                                                                                                                 #HERMIONE
        with d3                                                                                                                                                                                                                        #HERMIONE
        her "Я знаю..."
        label blowjob_jumping:
        
        # BLOWJOB
        play music "music/(Orchestral) Playful Tension by Shadow16nh.mp3" fadein 1 fadeout 1 # SEX THEME.
        hide screen hermione_main                                                                                                                                                                                   #HERMIONE
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
        m "Теперь попробуй глубже..."
        her "*Хлюп!* *Кулдык!* *Кулдык!*"
        m "Даа, Мне это нравится, Хорошо."
        her "*Чавк!* *!* *Хлюп!*"
        m "Да, Хорошая девочка."
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
                $ her_head_xpos=390 #Defines position of the Hermione's full length sprite. (Default 370). 140 - center. Bottom right: 390
                $ her_head_ypos=235 #Defines position of the Hermione's full length sprite. (Default 0). Right bottom corner: 340 - head only. 235 - tits.
                show screen h_head2                                                             # HERMIONE
                $ h_body = "03_hp/13_hermione_main/body_118.png" # HERMIONE
                her "Охх, хорошо..."
                her "Мы остаемся активны, но..."
                hide screen h_head2       
                hide screen h_c_u   # SUCKING
                show screen g_c_u # SUCKING
                with d3                      #  SUCKING
                her "*Чавк!* *Кулдык!*"
                show screen h_c_u   # NOT SUCKING
                hide screen g_c_u # NOT SUCKING
                with d3                      #  NOT SUCKING
                show screen h_head2                                                             # HERMIONE
                $ h_body = "03_hp/13_hermione_main/body_122.png" # HERMIONE
                her2 "Но мы не получаем той популярости и максимальной поддержки, как должны..."
                hide screen h_c_u   # SUCKING
                show screen g_c_u # SUCKING
                with d3                      #  SUCKING
                hide screen h_head2
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
                show screen h_head2                                                             # HERMIONE
                $ h_body = "03_hp/13_hermione_main/body_117.png" # HERMIONE
                her "Это не то, за что мы выступаем, Сэр."
                hide screen h_head2
                m "что ты имеешь в виду?"
                show screen h_head2                                                             # HERMIONE
                $ h_body = "03_hp/13_hermione_main/body_16.png" # HERMIONE
                her2 "\"ОЗМП\" О половом равенстве."
                her2 "Мы против обмена очков на услуги для учителей..."
                her2 "Мы против полового неравенства, которое подразумевает под собой этого рода услуги за очки..."
                hide screen h_head2
                m "Хмм..."
                m "Этот разговор начинает утомлять меня..."
                m "Пососи мой член еще немного, прежде чем мы продолжим."
                show screen h_head2                                                             # HERMIONE
                $ h_body = "03_hp/13_hermione_main/body_121.png" # HERMIONE
                her "Конечно, сэр."
                hide screen h_c_u   # SUCKING
                show screen g_c_u # SUCKING
                with d3                      #  SUCKING
                hide screen h_head2
                her "*Кулдык!* *Хлюп!* *Хлюп!*"
                m "Да, намного лучше..."
                m "Но вы по прежнему против подобных услуг, верно?"
                her "*Хлюп--"
                show screen h_c_u   # NOT SUCKING
                hide screen g_c_u # NOT SUCKING
                with d3                      #  NOT SUCKING
                show screen h_head2                                                             # HERMIONE
                $ h_body = "03_hp/13_hermione_main/body_120.png" # HERMIONE
                her2 "Да, это не одобряется..."
                hide screen h_head2 
                m "И все же, сегодня, ты преступница."
                show screen h_head2                                                             # HERMIONE
                $ h_body = "03_hp/13_hermione_main/body_120.png" # HERMIONE
                her "Но разве у меня был выбор??"
                her2 "Я была в очень трудном положении..."
                hide screen h_head2
                m "Мой член, Девочка."
                show screen h_head2                                                             # HERMIONE
                $ h_body = "03_hp/13_hermione_main/body_120.png" # HERMIONE
                her "Верно, извините..."
                hide screen h_c_u   # SUCKING
                show screen g_c_u # SUCKING
                with d3                      #  SUCKING
                hide screen h_head2
                her "*Чавк!* *Хлюп!* *Кулдык!*"
                her "*Чавк--"
                show screen h_c_u   # NOT SUCKING
                hide screen g_c_u # NOT SUCKING
                with d3                      #  NOT SUCKING
                show screen h_head2                                                             # HERMIONE
                $ h_body = "03_hp/13_hermione_main/body_117.png" # HERMIONE
                her2 "У нас будет встреча, сразу после всего этого."
                her2 "Я должна буду выступить с речью в этой форме, грязной, в пятнах."
                her2 "Я чувствую себя ужасно, но я должна буду сделать это..."
                hide screen h_head2     
                m "Попробуй просто насладиться этим..."
                show screen h_head2                                                             # HERMIONE
                $ h_body = "03_hp/13_hermione_main/body_118.png" # HERMIONE  
                her "Хорошо..."
                hide screen h_head2        
                m "просто признай это."
                show screen h_head2                                                             # HERMIONE
                $ h_body = "03_hp/13_hermione_main/body_117.png" # HERMIONE
                her "..............."
                hide screen h_head2
                m "Да, я знал это, тебе это нравится, ты извращенка."
                show screen h_head2                                                             # HERMIONE
                $ h_body = "03_hp/13_hermione_main/body_118.png" # HERMIONE
                her2 "Я думаю это было неловко и захватывающе одновременно..."
                her2 "И из за этого я чувствую себя еще хуже."
                hide screen h_head2
                m "Бедняжка."
                m "Положи член обратно в рот."
                show screen h_head2                                                             # HERMIONE
                $ h_body = "03_hp/13_hermione_main/body_117.png" # HERMIONE
                her "Да, сэр."
                hide screen h_head2
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
                $ her_head_xpos=390 #Defines position of the Hermione's full length sprite. (Default 370). 140 - center. Bottom right: 390
                $ her_head_ypos=235 #Defines position of the Hermione's full length sprite. (Default 0). Right bottom corner: 340 - head only. 235 - tits.
                show screen h_head2                                                             # HERMIONE
                $ h_body = "03_hp/13_hermione_main/body_75.png" # HERMIONE
                her "Да, я думаю так и есть..."
                show screen h_head2                                                             # HERMIONE
                $ h_body = "03_hp/13_hermione_main/body_74.png" # HERMIONE
                her2 "Я отличная студентка, не смотря на то, что  родилась в семье магглов..."
                show screen h_head2                                                             # HERMIONE
                $ h_body = "03_hp/13_hermione_main/body_117.png" # HERMIONE
                her2 "Хотя сначала они хотели отправить меня в \"Богус, школу-интернат \"."
                show screen h_head2                                                             # HERMIONE
                $ h_body = "03_hp/13_hermione_main/body_74.png" # HERMIONE
                her2 "Потребовалось некоторое усилие, чтобы убедить их в том, что \"Хогвартс\" является респектабельным учреждением.."
                hide screen h_head2     
                m "Да, действительно респектабельное учреждение."
                m "Положи член обратно в рот, девочка."
                hide screen h_c_u   # SUCKING
                show screen g_c_u # SUCKING
                with d3                      #  SUCKING
                her "*Чавк!* *Хлюп!* *Кулдык!*"
                hide screen h_head2     
                m "Да, просто держи его там некоторое время..."
                her "*Чавк!* *Хлюп!* *Хлюп!*"
                hide screen h_head2     
                m "Хорошо, хорошо..."
                m "Итак, что бы сказали ваши родители, если бы увидели тебя сейчас?"
                her "*Чавк--"
                show screen h_c_u   # NOT SUCKING
                hide screen g_c_u # NOT SUCKING
                with d3                      #  NOT SUCKING
                show screen h_head2                                                             # HERMIONE
                $ h_body = "03_hp/13_hermione_main/body_87.png" # HERMIONE
                her "Конечно же, они бы не поняли меня..."
                her "Но меня это не волнует."
                show screen h_head2                                                             # HERMIONE
                $ h_body = "03_hp/13_hermione_main/body_120.png" # HERMIONE
                her2 "Я не боюсь \"Пачкать руки\" и делать то, что должно быть сделано."
                hide screen h_head2     
                m "Ты немного непослушная, разве нет??"
                show screen h_head2                                                             # HERMIONE
                $ h_body = "03_hp/13_hermione_main/body_122.png" # HERMIONE
                her "Хмм, я думаю я такая."
                hide screen h_head2     
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
                $ her_head_xpos=390 #Defines position of the Hermione's full length sprite. (Default 370). 140 - center. Bottom right: 390
                $ her_head_ypos=235 #Defines position of the Hermione's full length sprite. (Default 0). Right bottom corner: 340 - head only. 235 - tits.
                show screen h_head2                                                             # HERMIONE
                $ h_body = "03_hp/13_hermione_main/body_13.png" # HERMIONE
                her "Разве я могу вам разсказать то - что вы еще не знаете?"
                hide screen h_head2     
                m "Да... Эмм... конечно я знаю все."
                m "Но я хочу посмотреть, как много знаешь ты!"
                m "Чтобы проверить твои знания по этому поводу."
                show screen blktone
                with d3
                ">как только вы говорите о  \"Проверке\"  Глаза Гермионы загораются волнением"
                hide screen blktone
                with d3
                show screen h_head2                                                             # HERMIONE
                $ h_body = "03_hp/13_hermione_main/body_80.png" # HERMIONE
                her "Хорошо, но мне нужно немного времени, что бы собраться с мыслями..."
                hide screen h_head2  
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
                show screen h_head2                                                             # HERMIONE
                $ h_body = "03_hp/13_hermione_main/body_87.png" # HERMIONE
                her2 "Факультет \"Гриффиндор\" был основан Годриком Гриффиндором, отсюда и название."
                her2 "Зверь на гербе \"Гриффиндор\" - Лев..."
                show screen h_head2                                                             # HERMIONE
                $ h_body = "03_hp/13_hermione_main/body_127.png" # HERMIONE
                her "Красный и золотой - цвета герба."
                hide screen h_head2   
                hide screen h_c_u   # SUCKING
                show screen g_c_u # SUCKING
                with d3                      #  SUCKING 
                her "*Хлюп!* *Чавк!* *Чавк!*"
                show screen h_c_u   # NOT SUCKING
                hide screen g_c_u # NOT SUCKING
                with d3                      #  NOT SUCKING
                show screen h_head2                                                             # HERMIONE
                $ h_body = "03_hp/13_hermione_main/body_127.png" # HERMIONE
                her2 "Профессор Минерва Макгонагалл, Глава дома."
                her2 "Дом \"Гриффиндор\" подчеркивает черты мужества..."
                her2 "Так же \"смелости, духа и храбрости\"..."
                her2 "И, таким образом, ее члены, как правило, являются смелыми, но безрассудными..."
                hide screen h_head2     
                hide screen h_c_u   # SUCKING
                show screen g_c_u # SUCKING
                with d3                      #  SUCKING
                her "*Чавк!* *Чавк!* *Чавк!*"
                show screen h_c_u   # NOT SUCKING
                hide screen g_c_u # NOT SUCKING
                with d3                      #  NOT SUCKING
                show screen h_head2                                                             # HERMIONE
                $ h_body = "03_hp/13_hermione_main/body_127.png" # HERMIONE
                her2 "\"Гриффиндор\" соответствует стихии огня..."
                her2 "По этой причинте были выбраны красный и золотой цвет."
                hide screen h_head2     
                hide screen h_c_u   # SUCKING
                show screen g_c_u # SUCKING
                with d3                      #  SUCKING
                her "*Чавк!* *Хлюп!* *Чавк!*"
                m "Хмм..."
                m "Ну, Я думаю, что могу немного высмеять тебя..."
                hide screen h_head2     
                her "*Чавк??*"
                m "В \"Гриффиндоре\" описывается смелость, духх и храбрость..."
                m "Но тем не мение, ты - шлюха..."
                show screen h_c_u   # NOT SUCKING
                hide screen g_c_u # NOT SUCKING
                with d3                      #  NOT SUCKING
                show screen h_head2                                                             # HERMIONE
                $ h_body = "03_hp/13_hermione_main/body_86.png" # HERMIONE
                her "Профессор!"
                hide screen h_head2     
                hide screen h_head2     
                m "Но, честно говоря..."
                m "\"смелость, дух, храбрость, безрассудство\"..."
                m "Хорошо подходит твоей личности..."
                show screen h_head2                                                             # HERMIONE
                $ h_body = "03_hp/13_hermione_main/body_45.png" # HERMIONE
                her "Сэр..."
                hide screen h_head2     
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
        show screen h_head2                                                             # HERMIONE
        $ h_body = "03_hp/13_hermione_main/body_87.png" # HERMIONE
        her "сэр... я... шлюха."
        hide screen h_head2  
        m "Что?"
        hide screen h_c_u   # SUCKING
        show screen g_c_u # SUCKING
        with d3                      #  SUCKING
        her "*Чавк-Чавк-Чавк!*"
        show screen h_c_u   # NOT SUCKING
        hide screen g_c_u # NOT SUCKING
        with d3                      #  NOT SUCKING
        show screen h_head2                                                             # HERMIONE
        $ h_body = "03_hp/13_hermione_main/body_117.png" # HERMIONE
        her2 "Я действительно шлюха, я с наслаждением сосу ваш член..."
        hide screen h_head2  
        m "Ох, говори больше об этом!"
        hide screen h_c_u   # SUCKING
        show screen g_c_u # SUCKING
        with d3                      #  SUCKING
        her "*Чавк!* *Хлюп!* *Чавк!*"
        show screen h_c_u   # NOT SUCKING
        hide screen g_c_u # NOT SUCKING
        with d3                      #  NOT SUCKING
        show screen h_head2                                                             # HERMIONE
        $ h_body = "03_hp/13_hermione_main/body_121.png" # HERMIONE
        her "Пожалуйста, Сэр, Кончайте для меня! "
        hide screen h_head2  
        with hpunch
        g4 "АХХХ, ты маленькая шл--!!!"
        g4 "{size=-4}(Почти кончаю. Должен ли я предупредить её?){/size}"
        menu:
            m "..."
            "- Предупредить её -":
                show screen h_head2                                                             # HERMIONE
                $ h_body = "03_hp/13_hermione_main/body_121.png" # HERMIONE
                her "Да, я люблю сосать --"
                hide screen h_head2  
                g4 "Скорее девочка, я почти кончил!"
                show screen h_head2                                                             # HERMIONE
                $ h_body = "03_hp/13_hermione_main/body_18.png" # HERMIONE
                her "!!!"
                hide screen h_head2      
                show screen ctc
                pause
                show screen blkfade
                with d3
                $ g_c_u_pic = "cum_in_mouth_ani"
                hide screen h_c_u   # SUCKING
                show screen g_c_u # SUCKING
                with d3                      #  SUCKING
                ">Гермиона быстро кладет член обратно в рот, и продолжает сосать его с большей страстью"
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
                m "Чтож, я думаю это все.."
                show screen h_c_u   # NOT SUCKING
                hide screen g_c_u # NOT SUCKING
                with d3                      #  NOT SUCKING
                show screen h_head2                                                             # HERMIONE
                $ h_body = "03_hp/13_hermione_main/body_126.png" # HERMIONE
                her ".............."
                hide screen h_head2  
                m "Ты в порядке там, Девочка?"
                show screen h_head2                                                             # HERMIONE
                $ h_body = "03_hp/13_hermione_main/body_123.png" # HERMIONE
                her "Да, Сэр..."
                her "Это было слишком..."
                hide screen h_head2  
                m "Тебе удалось проглатить это все."
                show screen h_head2                                                             # HERMIONE
                $ h_body = "03_hp/13_hermione_main/body_123.png" # HERMIONE
                her "Да... Я думала что задохнусь..."
                her2 "Но я дала себе обещание, что с вашего члена не упадет ни капли!"
                hide screen h_head2  
                m "Хорошая девочка."
                show screen h_head2                                                             # HERMIONE
                $ h_body = "03_hp/13_hermione_main/body_123.png" # HERMIONE
                her "Спасибо, сэр."
                her "Но всетаки, это было слишком..."
                show screen h_head2                                                             # HERMIONE
                $ h_body = "03_hp/13_hermione_main/body_121.png" # HERMIONE
                her "Мне кажется что я только что поела.."
                her "Мой желудок полон..."
                hide screen h_head2  
                g9 "Да, я накормил тебя моей спермой!"
                if daytime:
                    show screen h_head2                                                             # HERMIONE
                    $ h_body = "03_hp/13_hermione_main/body_121.png" # HERMIONE
                    her2 "я думаю что сегодня можно пойти на занятия без обеда."
                else:
                    show screen h_head2                                                             # HERMIONE
                    $ h_body = "03_hp/13_hermione_main/body_121.png" # HERMIONE
                    her2 "Да, я думаю можно пропустить ужин сегодня вечером"
                show screen h_head2                                                             # HERMIONE
                $ h_body = "03_hp/13_hermione_main/body_122.png" # HERMIONE
                her "Могу я получить оплату?"
                hide screen h_head2  
                show screen ctc
                pause
                hide screen ctc
                show screen blkfade
                with d3
            "- Не беспокоиться -":
                show screen h_head2                                                             # HERMIONE
                $ h_body = "03_hp/13_hermione_main/body_121.png" # HERMIONE
                her "Да, я люблю сосать --"
                hide screen h_head2  
                show screen white 
                pause.1
                hide screen white
                pause.2
                show screen white 
                pause .1
                hide screen white
                with hpunch
                g4 "{size=+7}Шлюха!{/size}"
                show screen h_head2                                                             # HERMIONE
                $ h_body = "03_hp/13_hermione_main/body_48.png" # HERMIONE
                her "!!?"
                hide screen h_head2
                
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
                $ uni_sperm = True
                $ u_sperm = "03_hp/13_hermione_main/auto_07.png"
                show screen h_head2                                                             # HERMIONE
                $ h_body = "03_hp/13_hermione_main/body_48.png" # HERMIONE
                her "Профессор..."
                hide screen h_head2  
                g4 "Не двигайся, девочка."
                g4 "Да, просто оставайся на месте."
                g4 "АХХХ, ты маленька Шлюха, из-за тебя я кончаю сильнее, девочка!"
                show screen h_head2                                                             # HERMIONE
                $ h_body = "03_hp/13_hermione_main/body_21.png" # HERMIONE
                her ".............."
                hide screen h_head2  
                m "Вот так..."
                $ g_c_u_pic = "cum_on_face_blink_ani"
                show screen h_head2                                                             # HERMIONE
                $ h_body = "03_hp/13_hermione_main/body_33.png" # HERMIONE
                her ".............."
                hide screen h_head2  
                m "Хорошо, я закончил..."
                show screen h_head2                                                             # HERMIONE
                $ h_body = "03_hp/13_hermione_main/body_31.png" # HERMIONE
                her "................."
                if daytime:
                    her "Мои занятия скоро начнутся..."
                else:
                    pass
                hide screen h_head2  
                m "Просто протри лицо и все будет в порядке.."
                show screen h_head2                                                             # HERMIONE
                $ h_body = "03_hp/13_hermione_main/body_31.png" # HERMIONE
                her "............"
                hide screen h_head2  
                m "Если ты не хочешь, что бы."
                show screen h_head2                                                             # HERMIONE
                $ h_body = "03_hp/13_hermione_main/body_34.png" # HERMIONE
                her "Хм?"
                hide screen h_head2  
                m "Все кто был снаружи."
                m "Видели какая ты маленькая шлюха."
                show screen h_head2                                                             # HERMIONE
                $ h_body = "03_hp/13_hermione_main/body_34.png" # HERMIONE
                her "Конечно нет, Сэр!"
                hide screen h_head2  
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
                    show screen h_head2                                                             # HERMIONE
                    $ h_body = "03_hp/13_hermione_main/body_34.png" # HERMIONE
                    her "Да..."
                show screen h_head2                                                             # HERMIONE
                $ h_body = "03_hp/13_hermione_main/body_44.png" # HERMIONE
                her "Могу я получить оплату?"
                hide screen h_head2
                $ aftersperm = True

        
        
    elif request_22_points == 1: #  <============================================================== EVENT 02
        m "Мисс Гренджер?"
        hide screen hermione_main                                                                                                                                                                                   #HERMIONE
        with d3                                                                                                                                                                                                                        #HERMIONE
        $ h_xpos=140 #Defines position of the Hermione's full length sprite. (Default 370). (Center: 140)                                                       #HERMIONE
        $ h_body = "03_hp/13_hermione_main/body_01.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
        show screen hermione_main                                                                                                                                                                                 #HERMIONE
        with d3                                         
        her "Сэр?"
        m "Как насчет минета??"
        hide screen hermione_main                                                                                                                                                                                   #HERMIONE
        with d3                                                                                                                                                                                                                        #HERMIONE
        $ h_xpos=140 #Defines position of the Hermione's full length sprite. (Default 370). (Center: 140)                                                       #HERMIONE
        $ h_body = "03_hp/13_hermione_main/body_86.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
        show screen hermione_main                                                                                                                                                                                 #HERMIONE
        with d3                                         
        play music "music/(Orchestral) Playful Tension by Shadow16nh.mp3" fadein 1 fadeout 1 # SEX THEME.
        her "Профессор, как вы смеете предлагать такое вашему ученику?!"
        m "Чт...?"
        hide screen hermione_main                                                                                                                                                                                   #HERMIONE
        with d3                                                                                                                                                                                                                        #HERMIONE
        $ h_xpos=140 #Defines position of the Hermione's full length sprite. (Default 370). (Center: 140)                                                       #HERMIONE
        $ h_body = "03_hp/13_hermione_main/body_86.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
        show screen hermione_main                                                                                                                                                                                 #HERMIONE
        with d3                                         
        her "Это недостойно человека вашей должности!"
        hide screen hermione_main                                                                                                                                                                                   #HERMIONE
        with d3                                                                                                                                                                                                                        #HERMIONE
        $ h_xpos=140 #Defines position of the Hermione's full length sprite. (Default 370). (Center: 140)                                                       #HERMIONE
        $ h_body = "03_hp/13_hermione_main/body_47.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
        show screen hermione_main                                                                                                                                                                                 #HERMIONE
        with d3                                         
        her "Вам должно быть стыдно за себя, сэр!"
        menu:
            m "???"
            "\"Прекрасно. Никаких очков! Уходи!\"":
                play music "music/Chipper Doodle v2.mp3" fadein 1 fadeout 1 # HERMIONE'S THEME.
                hide screen hermione_main                                                                                                                                                                                   #HERMIONE
                with d3                                                                                                                                                                                                                        #HERMIONE
                $ h_xpos=140 #Defines position of the Hermione's full length sprite. (Default 370). (Center: 140)                                                       #HERMIONE
                $ h_body = "03_hp/13_hermione_main/body_24.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
                show screen hermione_main                                                                                                                                                                                 #HERMIONE
                with d3                                         
                her "Сэр, успокойтесь, пожалуйста"
                m "Покиньте кабинет, мисс Грейнджер"
                hide screen hermione_main                                                                                                                                                                                   #HERMIONE
                with d3                                                                                                                                                                                                                        #HERMIONE
                $ h_xpos=140 #Defines position of the Hermione's full length sprite. (Default 370). (Center: 140)                                                       #HERMIONE
                $ h_body = "03_hp/13_hermione_main/body_24.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
                show screen hermione_main                                                                                                                                                                                 #HERMIONE
                with d3                                         
                her "сэр, все что я сказала, было не всерьез."
                m "Что?"
            "\"Эм, извините?\"":
                stop music fadeout 1.0
                hide screen hermione_main                                                                                                                                                                                   #HERMIONE
                with d3                                                                                                                                                                                                                        #HERMIONE
                $ h_xpos=140 #Defines position of the Hermione's full length sprite. (Default 370). (Center: 140)                                                       #HERMIONE
                $ h_body = "03_hp/13_hermione_main/body_06.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
                show screen hermione_main                                                                                                                                                                                 #HERMIONE
                with d3                                         
                her "*хи-хи*"
                m "Хмм?"
                hide screen hermione_main                                                                                                                                                                                   #HERMIONE
                with d3                                                                                                                                                                                                                        #HERMIONE
                $ h_xpos=140 #Defines position of the Hermione's full length sprite. (Default 370). (Center: 140)                                                       #HERMIONE
                $ h_body = "03_hp/13_hermione_main/body_24.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
                show screen hermione_main                                                                                                                                                                                 #HERMIONE
                with d3                                         
                play music "music/Chipper Doodle v2.mp3" fadein 1 fadeout 1 # HERMIONE'S THEME.
                her "Поняла...Сэр."
                m "Что?"
        hide screen hermione_main                                                                                                                                                                                   #HERMIONE
        with d3                                                                                                                                                                                                                        #HERMIONE
        $ h_xpos=140 #Defines position of the Hermione's full length sprite. (Default 370). (Center: 140)                                                       #HERMIONE
        $ h_body = "03_hp/13_hermione_main/body_45.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
        show screen hermione_main                                                                                                                                                                                 #HERMIONE
        with d3                                         
        her "Ну, так много произошло за последнее время..."
        her2 "У меня было так много новых впечатлений, что я изменила свой взгляд на вещи..."
        her2 "Так что я просто пыталась представить себе, как \"я в прошлом\" отреагировала бы на это."
        m "Итак..."
        g4 "вы плохо относитесь ко мне?"
        hide screen hermione_main                                                                                                                                                                                   #HERMIONE
        with d3                                                                                                                                                                                                                        #HERMIONE
        $ h_xpos=140 #Defines position of the Hermione's full length sprite. (Default 370). (Center: 140)                                                       #HERMIONE
        $ h_body = "03_hp/13_hermione_main/body_34.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
        show screen hermione_main                                                                                                                                                                                 #HERMIONE
        with d3                                         
        her "Хм...мне жаль сэр, я не это имела ввиду..."
        g4 "Ты плохая девочка, ты должна быть наказана!"
        g9 "Я накажу тебя моим членом!"
        hide screen hermione_main                                                                                                                                                                                   #HERMIONE
        with d3                                                                                                                                                                                                                        #HERMIONE
        $ h_xpos=140 #Defines position of the Hermione's full length sprite. (Default 370). (Center: 140)                                                       #HERMIONE
        $ h_body = "03_hp/13_hermione_main/body_34.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
        show screen hermione_main                                                                                                                                                                                 #HERMIONE
        with d3                                         
        her "..............................."

        jump blowjob_jumping
  
    elif request_22_points >= 2: # <============================================================== EVENT 03
        play music "music/(Orchestral) Playful Tension by Shadow16nh.mp3" fadein 1 fadeout 1 # SEX THEME.
        m "Соси мой член, девочка."
        hide screen hermione_main                                                                                                                                                                                   #HERMIONE
        with d3                                                                                                                                                                                                                        #HERMIONE
        $ h_xpos=140 #Defines position of the Hermione's full length sprite. (Default 370). (Center: 140)                                                       #HERMIONE
        $ h_body = "03_hp/13_hermione_main/body_45.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
        show screen hermione_main                                                                                                                                                                                 #HERMIONE
        with d3                                                                                                                                                                                                                         #HERMIONE                                                                                                                                                                                                                                          
        her "Конечно..."
        # Sucking.
        
        hide screen hermione_main                                                                                                                                                                                   #HERMIONE
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
        
        $ her_head_xpos=390 #Defines position of the Hermione's full length sprite. (Default 370). 140 - center. Bottom right: 390
        $ her_head_ypos=235 #Defines position of the Hermione's full length sprite. (Default 0). Right bottom corner: 340 - head only. 235 - tits.
        
        show screen h_head2                                                             # HERMIONE
        $ h_body = "03_hp/13_hermione_main/body_48.png" # HERMIONE
        her "(Профессор, что мне делать?)"
        hide screen h_head2
        m "Просто продолжай сосать мой член, девочка. Это тебя не касается."
        sna "Альбус? Ты там? Мне нужно поговорить с тобой."
        show screen h_head2                                                             # HERMIONE
        $ h_body = "03_hp/13_hermione_main/body_117.png" # HERMIONE
        her "(Это профессор Снейп!)"
        her "(Сэр, пожалуйста, скажите что бы он ушел, я прошу вас!)"
        hide screen h_head2
        menu:
            m "..."
            "\"Пожалуйста, заходите, Северус.\"":
                $ mad = 30
                show screen h_head2                                                             # HERMIONE
                $ h_body = "03_hp/13_hermione_main/body_76.png" # HERMIONE
                stop music fadeout 1.0
                her "(Сэр, нет!)"
                hide screen h_head2
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
                sna "Хорошо что ты здесь."
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
                her "{size=-4}(Джинни!!?Кто здесь?!){/size}"
                her "{size=-4}(Нет, пожалуйста! Я умру от стыда!){/size}"
                m "Да, Северус, я в порядке..."
                her "{size=-4}(Что? *Чавк...?* *Чавк...?* *Хлюп...?*){/size}"
                $ s_sprite = "03_hp/10_snape_main/snape_05.png" # SNAPE
                show screen s_head2                                                          # SNAPE
                sna "На что вы смотрите?"
                hide screen s_head2
                m "Эмм... Просто любуюсь...{w} Шкафом."
                m "Пожалуйста продолжайте..."
                $ s_sprite = "03_hp/10_snape_main/snape_05.png" # SNAPE
                show screen s_head2                                                          # SNAPE
                sna "..............."
                hide screen s_head2
                her "{size=-4}(*Чавк...* *Чавк...* *Хлюп...*){/size}"
                m "Вы хотели что-то обсудить?"
                $ s_sprite = "03_hp/10_snape_main/snape_06.png" # SNAPE
                show screen s_head2                                                          # SNAPE
                sna "Да. Девочка Гермиона"
                hide screen s_head2
                her "{size=-4}(*Чавк...!* *Кулдык...!* *Хлюп...!*){/size}"
                m "Ох ... Что с ней?"
                $ s_sprite = "03_hp/10_snape_main/snape_04.png" # SNAPE
                show screen s_head2                                                          # SNAPE
                sna2 "Вы обещали, что вы будете присматривать за маленькой ведьме."
                hide screen s_head2
                her "{size=-4}(*Чавк...* *Чавк...* *Хлюп...*){/size}"
                $ s_sprite = "03_hp/10_snape_main/snape_04.png" # SNAPE
                show screen s_head2                                                          # SNAPE
                sna "Но она по-прежнему досаждает мне!"
                sna "Ее тактика изменилась..."
                $ s_sprite = "03_hp/10_snape_main/snape_03.png" # SNAPE
                show screen s_head2                                                          # SNAPE
                sna2 "Но ей удается довести меня до горя..."
                hide screen s_head2
                m "Я понимаю ... ах ..."
                $ s_sprite = "03_hp/10_snape_main/snape_10.png" # SNAPE
                show screen s_head2                                                          # SNAPE
                sna "Эта девочка сводит меня с ума!"
                hide screen s_head2
                g4 "Да, она сводит меня с ума, а ... ах ..."
                her "{size=-4}(*Чавк...* *Чавк...* *Хлюп...*){/size}"
                $ s_sprite = "03_hp/10_snape_main/snape_04.png" # SNAPE
                show screen s_head2                                                          # SNAPE
                sna "Будете ли вы присматривать за ней?"
                hide screen s_head2
                m "Да. Она получит то, что она заслуживает."
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
                ">Она так растеряна, уязвима и все еще старательно продолжает выполнять свою задачу."
                g4 "(Я почти кончил!)"

                
            "\"Я сейчас занят, Северус.\"":
                show screen h_head2                                                             # HERMIONE
                $ h_body = "03_hp/13_hermione_main/body_117.png" # HERMIONE
                her "(Спасибо вам Сэр.)"
                hide screen h_head2                                                          
                sna "Занят, чем?"
                sna "Все что тебе нужно делать, это сидеть на заднице весь день."
                sna "Мне действительно нужно поговорить с тобой кое о чем."
                m "Я сказал, что занят, Северус."
                m "Понял? Я \"занят\"!"
                sna "Охх, ты имеешь ввиду \"Занят\" занят? Я-я-ясно!"
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
                ">Ее техники не хватает, но она сосет его с усилием"
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
                show screen h_head2                                                             # HERMIONE
                $ h_body = "03_hp/13_hermione_main/body_121.png" # HERMIONE
                her "Сэр?"
                hide screen h_head2          
                m "Хм?"
                show screen h_head2                                                             # HERMIONE
                $ h_body = "03_hp/13_hermione_main/body_121.png" # HERMIONE
                her "Вы кончите мне на лицо сегодня?"
                her "Или вы планируете кончить в рот?"
                hide screen h_head2
                menu:
                    "\"Я планирую забрызгать твое лицо спермой!\"":
                        show screen h_head2                                                             # HERMIONE
                        $ h_body = "03_hp/13_hermione_main/body_121.png" # HERMIONE
                        her "Я понимаю..."
                        hide screen h_head2
                        m "Почему ты спрашиваешь?"
                        show screen h_head2                                                             # HERMIONE
                        $ h_body = "03_hp/13_hermione_main/body_123.png" # HERMIONE
                        her2 "Ох ... Я прочитала в книге, что сперма содержит много антиоксидантов."
                        her "Это хорошо для кожи..."
                        hide screen h_head2
                        m "Отлично."
                        m "Возвращайся к работе."
                    "\"Я планирую кончить тебе в рот!\"":
                        show screen h_head2                                                             # HERMIONE
                        $ h_body = "03_hp/13_hermione_main/body_123.png" # HERMIONE
                        her "Я понимаю..."
                        hide screen h_head2
                        m "Почему ты спрашиваешь?"
                        show screen h_head2                                                             # HERMIONE
                        $ h_body = "03_hp/13_hermione_main/body_121.png" # HERMIONE
                        her "Ну, я пытаюсь следить за потреблением каллорий..."
                        her2 "Мне просто интересно сколько каллорий содержит ваша сперма."
                        her2 "Может мне стоит пропустить следующий прием пищи..."
                        hide screen h_head2
                        m "Девочка."
                        show screen h_head2                                                             # HERMIONE
                        $ h_body = "03_hp/13_hermione_main/body_121.png" # HERMIONE
                        her "Да?"
                        hide screen h_head2
                        m "Положи член в рот."
                    "\"Я не планирую так далеко вперед,.\"":
                        show screen h_head2                                                             # HERMIONE
                        $ h_body = "03_hp/13_hermione_main/body_121.png" # HERMIONE
                        her "я понимаю..."
                        hide screen h_head2
                        m "Ты не любишь сюрпризов?"
                        show screen h_head2                                                             # HERMIONE
                        $ h_body = "03_hp/13_hermione_main/body_121.png" # HERMIONE
                        her "на самом деле, нет..."
                        her "Скорее, мне нравится планировать все наперед..."
                        hide screen h_head2
                        m "Ну некоторые вещи в жизни просто непредсказуемы."
                        m "Существует только один способ узнать наверняка."
                        
                    "\"Что бы ты хотела?\"":
                        show screen h_head2                                                             # HERMIONE
                        $ h_body = "03_hp/13_hermione_main/body_121.png" # HERMIONE
                        her "Если вы все же разрешите мне выбрать, сэр..."
                        if generating_points == 1:
                            show screen h_head2                                                             # HERMIONE
                            $ h_body = "03_hp/13_hermione_main/body_123.png" # HERMIONE
                            her2 "Я бы хотела что бы бы кончили мне на лицо"
                            her2 "Я читала что это хорошо для кожи"
                        else:
                            show screen h_head2                                                             # HERMIONE
                            $ h_body = "03_hp/13_hermione_main/body_123.png" # HERMIONE
                            her2 "Я бы хотела что бы вы кончили мне в рот."
                            her2 "Вы обычно сильно кончаете, и я надеялась пропустить следующий прием пищи..."
                            her2 "И сделать больше домашнего задания."
                        hide screen h_head2
                        m "Хорошо, я подумаю."
                        m "продолжай сосать."
                    
                    
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
                show screen h_head2                                                             # HERMIONE
                $ h_body = "03_hp/13_hermione_main/body_118.png" # HERMIONE
                her "Хмм..."
                show screen h_head2                                                             # HERMIONE
                $ h_body = "03_hp/13_hermione_main/body_117.png" # HERMIONE
                her "Я ем тараканов?"
                hide screen h_head2
                m "Что за Херня?"
                show screen h_head2                                                             # HERMIONE
                $ h_body = "03_hp/13_hermione_main/body_117.png" # HERMIONE
                her "О-они давольно противны, сэр..."
                hide screen h_head2
                m "Нет, девочка, я иммел ввиду что нибудь грязное!"
                m "И не смей говорить \"грязь\"!"
                m "Я имею ввиду что-нибудь в сексуальном направлении!"
                show screen h_head2                                                             # HERMIONE
                $ h_body = "03_hp/13_hermione_main/body_118.png" # HERMIONE
                her "Ох... Эмм..."
                hide screen h_head2
                m "Ох, забудь..."
                show screen h_head2                                                             # HERMIONE
                $ h_body = "03_hp/13_hermione_main/body_117.png" # HERMIONE
                her "Эмм... Извините Сэр."
                hide screen h_head2
                m "Да, плевать, соси мой член сильнее."
                show screen h_head2                                                             # HERMIONE
                $ h_body = "03_hp/13_hermione_main/body_120.png" # HERMIONE
                her "Конечно сэр."
                hide screen h_head2
                
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
                m "Да, точно...ещё чучуть."
                her "*Чавк!* *Хлюп!* *Хлюп!*"
                m "Отлично, малышка, ещё чучуть, ещё немного...."
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
                g4 "Да.малышка,вот сейчас! Готовься быстро всё проглотить!"
                her "!!!"
                
                hide screen h_head2      
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
                g4 "{size=+7}Глап!{/size}"
                g4 "Да,глотай всё, шлюха!"
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
                m "Ну, думаю на сегодня всё."
                m "Ты можешь идти..."
                show screen h_c_u   # NOT SUCKING
                hide screen g_c_u # NOT SUCKING
                with d3                      #  NOT SUCKING
                show screen h_head2                                                             # HERMIONE
                $ h_body = "03_hp/13_hermione_main/body_125.png" # HERMIONE
                her "..........................."
                her "................"
                her "........"
                show screen h_head2                                                             # HERMIONE
                $ h_body = "03_hp/13_hermione_main/body_126.png" # HERMIONE
                $ renpy.play('sounds/gulp.mp3') #Sound of gulping down a liquid.
                her "*Хлюп!*"
                show screen h_head2                                                             # HERMIONE
                $ h_body = "03_hp/13_hermione_main/body_115.png" # HERMIONE
                her "Хлюп-чавк..."
                hide screen h_head2  
                m "Ты в порядке?"
                show screen h_head2                                                             # HERMIONE
                $ h_body = "03_hp/13_hermione_main/body_123.png" # HERMIONE
                play music "music/Chipper Doodle v2.mp3" fadein 1 fadeout 1 # HERMIONE'S THEME.
                her "Да, профессор..."
                hide screen h_head2  
                m "Ты не собираешься идти поесть?"
                show screen h_head2                                                             # HERMIONE
                $ h_body = "03_hp/13_hermione_main/body_123.png" # HERMIONE
                her "Видимо не пойду..."
                her "Вы всегда кончаете так много, сэр..."
                hide screen h_head2  
                m "Хех... Ну и кто же виноват в этом??"
                show screen h_head2                                                             # HERMIONE
                $ h_body = "03_hp/13_hermione_main/body_123.png" # HERMIONE
                her "............." #Smile.
                her "Могу я получить оплату?"
                hide screen h_head2  
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
                show screen h_head2                                                             # HERMIONE
                $ h_body = "03_hp/13_hermione_main/body_123.png" # HERMIONE
                her "Да сэр!"
                hide screen h_head2      
                g4 "Тогда получай!"
                
                hide screen h_head2  
                show screen white 
                pause.1
                hide screen white
                pause.2
                show screen white 
                pause .1
                hide screen white
                with hpunch
                g4 "{size=+7}Шлюха!{/size}"
                show screen h_head2                                                             # HERMIONE
                $ h_body = "03_hp/13_hermione_main/body_48.png" # HERMIONE
                her "!!?"
                hide screen h_head2
                
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
                $ uni_sperm = True
                $ u_sperm = "03_hp/13_hermione_main/auto_07.png"
                show screen h_head2                                                             # HERMIONE
                $ h_body = "03_hp/13_hermione_main/body_48.png" # HERMIONE
                her "Профессор..."
                hide screen h_head2  
                g4 "Всё на твоем грязном лице!"
                show screen h_head2                                                             # HERMIONE
                $ h_body = "03_hp/13_hermione_main/body_123.png" # HERMIONE
                her "Аааа!"
                $ g_c_u_pic = "cum_on_face_blink_ani"
                hide screen h_head2  
                m "Ладно, Я всё."
                show screen h_head2                                                             # HERMIONE
                $ h_body = "03_hp/13_hermione_main/body_123.png" # HERMIONE
                her "...................................."
                hide screen h_head2  
                m "Я сказала всё, девочка."
                show screen h_head2                                                             # HERMIONE
                $ h_body = "03_hp/13_hermione_main/body_123.png" # HERMIONE
                her "Да, я слышала вас,сэр..."
                hide screen h_head2  
                m "Ну и... Ты не собираешься умыться?"
                show screen h_head2                                                             # HERMIONE
                $ h_body = "03_hp/13_hermione_main/body_123.png" # HERMIONE
                her "Секундочку..."
                her2 "Я даю своей коже время, что бы впитать анти-оксиданты..." 
                hide screen h_head2  
                m "Ммм... Вот как,меня это заводит..."
                m "Не торопись, девочка..."
                show screen blkfade
                with d3
                stop music fadeout 1.0 
                ">Минутой позже."
                $ uni_sperm = False
                $ aftersperm = True
                show screen h_head2                                                             # HERMIONE
                $ h_body = "03_hp/13_hermione_main/body_122.png" # HERMIONE
                her "Мне кажется, вам нравится,сэр?"
                hide screen h_head2  
                play music "music/Chipper Doodle v2.mp3" fadein 1 fadeout 1 # HERMIONE'S THEME.
                m "Да, девочка, мне нравится."
                show screen h_head2                                                             # HERMIONE
                $ h_body = "03_hp/13_hermione_main/body_123.png" # HERMIONE
                her "Хорошо, так мы можем расчитаться?"
                hide screen h_head2  
                
                    
                
            
        
    
    $ uni_sperm = False #Sperm layer is not displayed in hermione screen.
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
    
    $ badges = True # Turns the badges layer of hermione_main back on.
    
    m "Да, мисс Грейнджер. 55 очков  \"Гриффиндору\"." 
    $ gryffindor +=55
    $ h_xpos=140 #Defines position of the Hermione's full length sprite. (Default 370). (Center: 140)
    $ h_body = "03_hp/13_hermione_main/body_13.png" #Flashing panties
    show screen hermione_main
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
    hide screen hermione_main
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

    $ aftersperm = False #Show cum stains on Hermione's uniform.

    
    call music_block
    
    if daytime:
        $ hermione_takes_classes = True
        jump night_main_menu
    else:
        $ hermione_sleeping = True
        jump day_main_menu            
   
    
    
    

###################REQUEST_29 (Level 07) (65 pt.) (Sex). #################################################################
label new_request_29: #LV.7 (Whoring = 18 - 20)

    hide screen hermione_main 
    with d3
    m "{size=-4}(Должен ли я попросить её заняться сексом со мной?){/size}"
    $ menu_x = 0.5 #Default position of the menu (0.5). Version B is $ menu_x = 0.2
    menu:
        "\"(Да, попросить!)\"":
            show screen blktone
            with d3
            pass
        "\"(Не сейчас.)\"":
            jump new_personal_request
            
  
    if request_29_points == 0: # FIRST EVENT <============================================================== EVENT 01
        m "Мисс Грейнджер?"
        hide screen hermione_main                                                                                                                                                                                   #HERMIONE
        with d3                                                                                                                                                                                                                        #HERMIONE
        $ h_xpos=140 #Defines position of the Hermione's full length sprite. (Default 370). (Center: 140)                                                       #HERMIONE
        $ h_body = "03_hp/13_hermione_main/body_01.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
        show screen hermione_main                                                                                                                                                                                 #HERMIONE
        with d3                         
        her "Сэр?"
        m "Я бы хотел купить у вас сегодня..."
        hide screen hermione_main                                                                                                                                                                                   #HERMIONE
        with d3                                                                                                                                                                                                                        #HERMIONE
        $ h_xpos=140 #Defines position of the Hermione's full length sprite. (Default 370). (Center: 140)                                                       #HERMIONE
        $ h_body = "03_hp/13_hermione_main/body_06.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
        show screen hermione_main                                                                                                                                                                                 #HERMIONE
        with d3                         
        her ".......?"
        m "Как бы более мягко выразиться...?"
        hide screen hermione_main                                                                                                                                                                                   #HERMIONE
        with d3                                                                                                                                                                                                                        #HERMIONE
        $ h_xpos=140 #Defines position of the Hermione's full length sprite. (Default 370). (Center: 140)                                                       #HERMIONE
        $ h_body = "03_hp/13_hermione_main/body_129.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
        show screen hermione_main                                                                                                                                                                                 #HERMIONE
        with d3                         
        her "Занятся сексом, сэр?"
        m "Вообще-то да. Как вы догадались...?"
        if whoring <=17:
            jump too_much
        hide screen hermione_main                                                                                                                                                                                   #HERMIONE
        with d3                                                                                                                                                                                                                        #HERMIONE
        $ h_xpos=140 #Defines position of the Hermione's full length sprite. (Default 370). (Center: 140)                                                       #HERMIONE
        $ h_body = "03_hp/13_hermione_main/body_128.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
        show screen hermione_main                                                                                                                                                                                 #HERMIONE
        with d3                         
        her "Не сложно было догадаться..."
        m "Вы не будете возражать?"
        hide screen hermione_main                                                                                                                                                                                   #HERMIONE
        with d3                                                                                                                                                                                                                        #HERMIONE
        $ h_xpos=140 #Defines position of the Hermione's full length sprite. (Default 370). (Center: 140)                                                       #HERMIONE
        $ h_body = "03_hp/13_hermione_main/body_120.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
        show screen hermione_main                                                                                                                                                                                 #HERMIONE
        with d3                         
        her "Кончено я буду возражать, сэр!"
        her "Я не проститутка!"
        m "Но всё равно сделаете это??"
        hide screen hermione_main                                                                                                                                                                                   #HERMIONE
        with d3                                                                                                                                                                                                                        #HERMIONE
        $ h_xpos=140 #Defines position of the Hermione's full length sprite. (Default 370). (Center: 140)                                                       #HERMIONE
        $ h_body = "03_hp/13_hermione_main/body_127.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
        show screen hermione_main                                                                                                                                                                                 #HERMIONE
        with d3                         
        her2 "\"Гриффиндор\" снова на грани поражения..."
        her2 "И что вы думаете я должна делать...?"
        m "Отлично!"
        hide screen hermione_main                                                                                                                                                                                 #HERMIONE
       
        label your_ass:
            
        show screen blkfade 
        with d7
            
        stop music fadeout 1.0
        $ her_head_xpos=390 #Defines position of the Hermione's full length sprite. (Default 370). 140 - center. Bottom right: 390
        $ her_head_ypos=340 #Defines position of the Hermione's full length sprite. (Default 0). Right bottom corner: 340 - head only. 235 - tits.
        show screen h_head2                                                             # HERMIONE
        $ h_body = "03_hp/13_hermione_main/body_120.png" # HERMIONE
        her "............."
        show screen h_head2                                                             # HERMIONE
        $ h_body = "03_hp/13_hermione_main/body_119.png" # HERMIONE
        her "!!!!!!!!!!!!!!!"
        hide screen h_head2                        
        m "Раслабься, девочка. Я только снимаю твои трусики."
        show screen h_head2                                                             # HERMIONE
        $ h_body = "03_hp/13_hermione_main/body_49.png" # HERMIONE
        her ".............."
        hide screen h_head2                        
        m "Ты готова?"
        show screen h_head2                                                             # HERMIONE
        $ h_body = "03_hp/13_hermione_main/body_50.png" # HERMIONE
        her "Нет..."
        hide screen h_head2                        
        m "Хорошая девочка."
        $ renpy.play('sounds/gltch.mp3')
        with hpunch
        with kissiris
        show screen h_head2                                                             # HERMIONE
        $ h_body = "03_hp/13_hermione_main/body_130.png" # HERMIONE
        her2 "Ааааааааааааааайййййй....{image=textheart.png}"
        hide screen h_head2




        hide screen hermione_main                                                                                                                                                                                   #HERMIONE
        hide screen genie
        $ genie_chibi_xpos = -210 #-185 behind the desk. (Also 5 is something).
        $ genie_chibi_ypos = 10
        $ g_c_u_pic = "sex_ani"
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
        play music "music/(Orchestral) Playful Tension by Shadow16nh.mp3" fadein 1 fadeout 1 # SEX THEME.
            
            
            
            
        
        
        #FUCKING
        
        g4 "Твоя киска... Такая тугая."
        show screen h_head2                                                             # HERMIONE
        $ h_body = "03_hp/13_hermione_main/body_33.png" # HERMIONE
        her "................"
        hide screen h_head2                       
        m "Ты как?"
        show screen h_head2                                                             # HERMIONE
        $ h_body = "03_hp/13_hermione_main/body_21.png" # HERMIONE
        her "Аа-а... Он такой большой..."
        her "Вы разорвете меня на части, сэр!"
        hide screen h_head2        
        m "Ты что?! Мой член вполне нормальных размеров."
        m "Я не виноват, что твоя киска такая узкая."
        show screen h_head2                                                             # HERMIONE
        $ h_body = "03_hp/13_hermione_main/body_33.png" # HERMIONE
        her "......................"
        hide screen h_head2         
        hide screen ctc
        menu:
            "\"Тебе должно быть стыдно за себя!\"":
                show screen h_head2                                                             # HERMIONE
                $ h_body = "03_hp/13_hermione_main/body_33.png" # HERMIONE
                her "Мне не стыдно, сэр!"
                her "я делаю это всё для моего факультета...!"
                her "Что бы помочь моему...--"
                show screen h_head2                                                             # HERMIONE
                $ h_body = "03_hp/13_hermione_main/body_131.png" # HERMIONE
                her "А-а-а..."
                her "Мои однокурсники расчитывают на меня... а-а..."
                hide screen h_head2  
                m "Ты уверена что это единственная причина?"
                show screen h_head2                                                             # HERMIONE
                $ h_body = "03_hp/13_hermione_main/body_33.png" # HERMIONE
                her "Я не знаю..--"
                show screen h_head2                                                             # HERMIONE
                $ h_body = "03_hp/13_hermione_main/body_131.png" # HERMIONE
                her2 "а-а..."
                show screen h_head2                                                             # HERMIONE
                $ h_body = "03_hp/13_hermione_main/body_118.png" # HERMIONE
                her2 "Я не знаю,что вы имеете ввиду, сэр."
                hide screen h_head2  
                m "Мне кажется,что ты очень наслаждаешься от того,чем мы с тобой занимаемся."
                show screen h_head2                                                             # HERMIONE
                $ h_body = "03_hp/13_hermione_main/body_118.png" # HERMIONE
                her "Нет,это не так, сэр!"
                hide screen h_head2  
                m "Правда?"
                show screen h_head2                                                             # HERMIONE
                $ h_body = "03_hp/13_hermione_main/body_33.png" # HERMIONE
                her "......................"
                hide screen h_head2  
                m "Вот почему твоя киска так течет?"
                show screen h_head2                                                             # HERMIONE
                $ h_body = "03_hp/13_hermione_main/body_131.png" # HERMIONE
                her "....................а-а.{image=textheart.png}"
                hide screen h_head2  
                m "Признайся, ты наслаждаешься тем, что твой професср трахает тебя!"
                show screen h_head2                                                             # HERMIONE
                $ h_body = "03_hp/13_hermione_main/body_33.png" # HERMIONE
                her "Нет, я не наслаждаюсь!"
                hide screen h_head2  
                m "Упрямая девченка..."
                show screen h_head2                                                             # HERMIONE
                $ h_body = "03_hp/13_hermione_main/body_131.png" # HERMIONE
                her "Ааа...{image=textheart.png}" 
                hide screen h_head2  
            "\"Так... Что нового у тебя?\"":
                show screen h_head2                                                             # HERMIONE
                $ h_body = "03_hp/13_hermione_main/body_31.png" # HERMIONE
                her "...Сэр?"
                hide screen h_head2  
                m "Я стараюсь поддержать приятную беседу."
                show screen h_head2                                                             # HERMIONE
                $ h_body = "03_hp/13_hermione_main/body_31.png" # HERMIONE
                her "А-а... Но... а..."
                hide screen h_head2  
                m "Как поживают твои родственники?"
                show screen h_head2                                                             # HERMIONE
                $ h_body = "03_hp/13_hermione_main/body_34.png" # HERMIONE
                her "Мои родители?"
                show screen h_head2                                                             # HERMIONE
                $ h_body = "03_hp/13_hermione_main/body_131.png" # HERMIONE
                her "Профессор, пожалуйста, я не могу сейчас говорить..."
                hide screen h_head2  
                m "Почему же? Ты так этим наслаждаешься?"
                show screen h_head2                                                             # HERMIONE
                $ h_body = "03_hp/13_hermione_main/body_131.png" # HERMIONE
                her "Я не... ах...{image=textheart.png}"
                hide screen h_head2  
                m "Я думаю ты кайфуешь от этого."
                show screen h_head2                                                             # HERMIONE
                $ h_body = "03_hp/13_hermione_main/body_131.png" # HERMIONE
                her "Я всего лишь делаю это ради очков, сэр..."
                hide screen h_head2  
                m "Ммм, ясно..."
                m "Получается ты - проститутка."
                show screen h_head2                                                             # HERMIONE
                $ h_body = "03_hp/13_hermione_main/body_117.png" # HERMIONE
                her "Что?"
                hide screen h_head2  
                m "Я плачу тебе, за секс. Как же ты это назовёшь?"
                show screen h_head2                                                             # HERMIONE
                $ h_body = "03_hp/13_hermione_main/body_118.png" # HERMIONE
                her "..........."
                show screen h_head2                                                             # HERMIONE
                $ h_body = "03_hp/13_hermione_main/body_131.png" # HERMIONE
                her "Я не проститутка..."
                show screen h_head2                                                             # HERMIONE
                $ h_body = "03_hp/13_hermione_main/body_21.png" # HERMIONE
                her "Почему вы так жестоки со мной, сэр?"
                hide screen h_head2  
                m "Мне кажется тебе нравится, когда я более жесток с тобой."
                show screen h_head2                                                             # HERMIONE
                $ h_body = "03_hp/13_hermione_main/body_67.png" # HERMIONE
                her "Нет!"
                hide screen h_head2  
                m "Правда? Тогда почему твоя киска такая влажная?"
                show screen h_head2                                                             # HERMIONE
                $ h_body = "03_hp/13_hermione_main/body_118.png" # HERMIONE
                her "Не из-за этого!"
                hide screen h_head2  
                m "Если ты так настаиваешь..."
                show screen h_head2                                                             # HERMIONE
                $ h_body = "03_hp/13_hermione_main/body_131.png" # HERMIONE
                her "А-ах...{image=textheart.png}"
                show screen h_head2                                                             # HERMIONE
                $ h_body = "03_hp/13_hermione_main/body_132.png" # HERMIONE
                her "Я ... ах...{image=textheart.png} не проститутка..."            
                hide screen h_head2  
            "\"......................................................\"":
                show screen h_head2                                                             # HERMIONE
                $ h_body = "03_hp/13_hermione_main/body_131.png" # HERMIONE
                her "А-ах... ах..."
                hide screen h_head2  
                m "*Дышит всё чаще!*"
                show screen h_head2                                                             # HERMIONE
                $ h_body = "03_hp/13_hermione_main/body_131.png" # HERMIONE
                her "Ах... а-ах..."
                hide screen h_head2  
                m "Ох..."
                show screen h_head2                                                             # HERMIONE
                $ h_body = "03_hp/13_hermione_main/body_131.png" # HERMIONE
                her "Ах-аа..."
                hide screen h_head2  
                m "......................"
                show screen h_head2                                                             # HERMIONE
                $ h_body = "03_hp/13_hermione_main/body_131.png" # HERMIONE
                her "Ах... а..."
                show screen h_head2                                                             # HERMIONE
                $ h_body = "03_hp/13_hermione_main/body_31.png" # HERMIONE
                her "Ах... Сэр?"
                hide screen h_head2  
                m "Что такое?"
                show screen h_head2                                                             # HERMIONE
                $ h_body = "03_hp/13_hermione_main/body_131.png" # HERMIONE
                her "Ах... Вам.... нравится...это...?"
                hide screen h_head2  
                m "Нравится ли мне долбить узкую и мокрую киску?"
                m "Очень, малышка. А что?"
                show screen h_head2                                                             # HERMIONE
                $ h_body = "03_hp/13_hermione_main/body_33.png" # HERMIONE
                her "....................."
                show screen h_head2                                                             # HERMIONE
                $ h_body = "03_hp/13_hermione_main/body_131.png" # HERMIONE
                her "Ах... Вы просто так внезапно замолчали..."
                hide screen h_head2  
                m "Просто наслаждаюсь моментом,малышка."
                m "А как тебе ощущения? Ты в порядке?"
                show screen h_head2                                                             # HERMIONE
                $ h_body = "03_hp/13_hermione_main/body_131.png" # HERMIONE
                her "А... дааа..."
                show screen h_head2                                                             # HERMIONE
                $ h_body = "03_hp/13_hermione_main/body_31.png" # HERMIONE
                her "Немного больновато, ах..."
                show screen h_head2                                                             # HERMIONE
                $ h_body = "03_hp/13_hermione_main/body_131.png" # HERMIONE
                her "Ваш пенис слишком велик... ах..."
                hide screen h_head2  
                m "Хм..."
                m "Ты хочешь что бы я замедлился?"
                show screen h_head2                                                             # HERMIONE
                $ h_body = "03_hp/13_hermione_main/body_31.png" # HERMIONE
                her "Нет, сэр... Вам не стоит..."
                show screen h_head2                                                             # HERMIONE
                $ h_body = "03_hp/13_hermione_main/body_33.png" # HERMIONE
                her "Пожалуйста, не обращайте на меня внимания... Наслаждайтесь."
                her "Я... ах... привыкну к этому... ах..."
                hide screen h_head2  
                m "Как пожелаешь, малышка."
                show screen h_head2                                                             # HERMIONE
                $ h_body = "03_hp/13_hermione_main/body_131.png" # HERMIONE
                her "Ах-a...{image=textheart.png}"
                hide screen h_head2  

        m "Да, о да!"
        show screen h_head2                                                             # HERMIONE
        $ h_body = "03_hp/13_hermione_main/body_131.png" # HERMIONE
        her "Ах-а...{image=textheart.png}"
        hide screen h_head2  
        if daytime:
            m "Собераешься вернуться в класс после того как мы с тобой закончим?"
        else:
            m "Собераешься вернуться в кровать после того как мы с тобой закончим?"
        show screen h_head2                                                             # HERMIONE
        $ h_body = "03_hp/13_hermione_main/body_131.png" # HERMIONE
        her "Да, ах...{image=textheart.png}"
        her "Если я вообще смогу ходить..."
        hide screen h_head2  
        g4 "Хм! {image=textheart.png} Да,ты всегда знаешь что говорить, девочка"
        show screen h_head2                                                             # HERMIONE
        $ h_body = "03_hp/13_hermione_main/body_132.png" # HERMIONE
        her "Ах...{image=textheart.png} ах...{image=textheart.png}{image=textheart.png}"
        with hpunch
        show screen h_head2                                                             # HERMIONE
        $ h_body = "03_hp/13_hermione_main/body_130.png" # HERMIONE
        her "{size=+7}!!!!!!!!!!!!!!!{/size}{image=textheart.png}{image=textheart.png}{image=textheart.png}"
        hide screen h_head2  
        m "Ммм? Ты в порядке?"
        show screen blktone8
        with d3
        ">Ноги гермионы затрясись..."
        m "Девочка?"
        show screen h_head2                                                             # HERMIONE
        $ h_body = "03_hp/13_hermione_main/body_130.png" # HERMIONE
        her "{image=textheart.png}{image=textheart.png}{image=textheart.png}Мне кажется, я кончаю, сэр!{image=textheart.png}{image=textheart.png}{image=textheart.png}"
        hide screen h_head2  
        g9 "Ха... Ты ненасытная сучка!"
        show screen h_head2                                                             # HERMIONE
        $ h_body = "03_hp/13_hermione_main/body_133.png" # HERMIONE
        her "АААА! Я больше не могу сдерживаться!"
        hide screen h_head2  
        g4 "Тебя нужно наказать за это,грязная шлюха!"
        ">Вы натягиваете задницу Гермины всё сильнее и сильнее и трахаете её всё жестче жестче!"
        $ g_c_u_pic = "sex2_ani"
        with hpunch
        show screen h_head2                                                             # HERMIONE
        $ h_body = "03_hp/13_hermione_main/body_130.png" # HERMIONE
        her "НЕТ! ОСТАНОВИТЕСЬ! ПОЖАЛУЙСТА!"
        hide screen h_head2  
        g4 "Кто тебе разрешал кончать, шлюха? Вот твоё наказание!"
        show screen h_head2                                                             # HERMIONE
        $ h_body = "03_hp/13_hermione_main/body_131.png" # HERMIONE
        her "Профессор, нееее...а-ах!{image=textheart.png}"
        show screen h_head2                                                             # HERMIONE
        $ h_body = "03_hp/13_hermione_main/body_134.png" # HERMIONE
        her "Ах-a...{image=textheart.png}Я сейчас сойду с ума!{image=textheart.png}{image=textheart.png}{image=textheart.png}"
        hide screen h_head2  
        g4 "{size=+7}Грааарх!{/size}"
        hide screen blktone8
        with d3
        hide screen bld1
        with d3
        show screen ctc
        pause
        hide screen ctc
        show screen bld1
        with d3
        show screen h_head2                                                             # HERMIONE
        $ h_body = "03_hp/13_hermione_main/body_134.png" # HERMIONE
        her "Нет...{image=textheart.png} ах...{image=textheart.png}"
        her "Похоже я сейчас...{image=textheart.png} кончу...{image=textheart.png}"
        hide screen h_head2  
        g4 "ООООДА! ШЛЮХА!"
        menu:
            "- Обкончать Гермиону -":
                with hpunch
                g4 "{size=+7}Аааа!!!{/size}"
                

                show screen white 
                pause.1
                hide screen white
                pause.2
                show screen white 
                pause .1
                hide screen white
                with hpunch
                g4 "{size=+15}Аааа!!!!!!!!!!!!!!!!{/size}"
                $ g_c_u_pic = "sex_cum_out_ani"
                show screen white 
                pause.1
                hide screen white
                pause.2
                show screen white 
                pause .1
                hide screen white
                with hpunch
                show screen ctc
                pause
                hide screen ctc
                $ uni_sperm = True
                $ u_sperm = "03_hp/13_hermione_main/auto_08.png"
                show screen h_head2                                                             # HERMIONE
                $ h_body = "03_hp/13_hermione_main/body_133.png" # HERMIONE
                her2 "Ааа...{image=textheart.png}{image=textheart.png}{image=textheart.png}"
                hide screen h_head2     
                hide screen bld1
                with d3
                show screen ctc
                pause
                hide screen ctc
                show screen bld1
                with d3
                $ g_c_u_pic = "sex_cum_out_blink_ani"

                m "Это было весело..."
                show screen h_head2                                                             # HERMIONE
                $ h_body = "03_hp/13_hermione_main/body_135.png" # HERMIONE
                her "*еле дышит*"
                hide screen h_head2
                m "Как ты?"
                show screen h_head2                                                             # HERMIONE
                $ h_body = "03_hp/13_hermione_main/body_133.png" # HERMIONE
                her "Ах... да..."
                her "Мои ноги до сих пор трясутся..."
                hide screen h_head2
                hide screen bld1
                with d3
                show screen ctc
                pause
                hide screen ctc
                show screen blkfade
                with d7
                show screen h_head2                                                             # HERMIONE
                $ h_body = "03_hp/13_hermione_main/body_133.png" # HERMIONE
                if daytime:
                    her "Я думаю, мне пора вернуться в класс..."
                else:
                    her2 "Я думаю мне пора вернуться в спальню..."
                hide screen h_head2
                m "Хорошо."
                m "Тебе понравилось быть отраханной профессором?"
                show screen h_head2                                                             # HERMIONE
                $ h_body = "03_hp/13_hermione_main/body_136.png" # HERMIONE
                her "Сэр, Я всего лишь делаю это для моего факультета."
                hide screen h_head2
                m "Ты что серьезно? Все ещё?"
                show screen h_head2                                                             # HERMIONE
                $ h_body = "03_hp/13_hermione_main/body_131.png" # HERMIONE
                her "Мы можем расчитаться... пожалуйста?"
                hide screen h_head2
    
            "- Кончить в Гермиону -":
                with hpunch
                g4 "{size=+7}Аргх!!!{/size}"
                
                
                
                
                show screen white 
                pause.1
                hide screen white
                pause.2
                show screen white 
                pause .1
                hide screen white
                with hpunch
                g4 "{size=+15}Ааа!!!!!!!!!!!!!!!!{/size}"
                $ g_c_u_pic = "sex_cum_in_ani"
                show screen white 
                pause.1
                hide screen white
                pause.2
                show screen white 
                pause .1
                hide screen white
                with hpunch
                show screen ctc
                pause
                hide screen ctc
                $ uni_sperm = True
                $ u_sperm = "03_hp/13_hermione_main/auto_08.png"
                show screen h_head2                                                             # HERMIONE
                $ h_body = "03_hp/13_hermione_main/body_133.png" # HERMIONE
                her2 "Аааа...{image=textheart.png}{image=textheart.png}{image=textheart.png}"
                hide screen h_head2     
                hide screen bld1
                with d3
                show screen ctc
                pause
                hide screen ctc
                show screen bld1
                with d3
                $ g_c_u_pic = "03_hp/08_animation_02/23_cum_19.png"
                show screen h_head2                                                             # HERMIONE
                $ h_body = "03_hp/13_hermione_main/body_133.png" # HERMIONE
                her "Вы кончили в меня..."
                hide screen h_head2
                g9 "Да, в тебя."
                hide screen bld1
                with d3
                show screen ctc
                pause
                hide screen ctc
                show screen blkfade
                with d7
                show screen h_head2                                                             # HERMIONE
                $ h_body = "03_hp/13_hermione_main/body_133.png" # HERMIONE
                her "Но..."
                hide screen h_head2
                m "Что?"
                show screen h_head2                                                             # HERMIONE
                $ h_body = "03_hp/13_hermione_main/body_132.png" # HERMIONE
                her "Вы не боитесь что я забеременнею?"
                hide screen h_head2
                m "Не, всё будет хорошо..."
                show screen h_head2                                                             # HERMIONE
                $ h_body = "03_hp/13_hermione_main/body_132.png" # HERMIONE
                her "Откуда вы знаете,сэр?"
                hide screen h_head2
                m "Мы ведьмаки - бесплодны."
                show screen h_head2                                                             # HERMIONE
                $ h_body = "03_hp/13_hermione_main/body_131.png" # HERMIONE
                her "Ведьмаки?"
                hide screen h_head2
                m "Конечно... Ты ведьма, получается мы - ведьмаки, верно?"
                m "И всем известно что ведьмаки - бесплодны..."
                show screen h_head2                                                             # HERMIONE
                $ h_body = "03_hp/13_hermione_main/body_117.png" # HERMIONE
                her "Сэр,это бессмысленно..."
                her "Могу я просто расчитаться...?"
                hide screen h_head2

    elif request_29_points == 1: # SECOND EVENT <============================================================== EVENT 02
        m "Мисс Грейнджер, вы уже мокрая и готовы,что бы я вошёл в вас?"
        hide screen hermione_main                                                                                                                                                                                   #HERMIONE
        with d3                                                                                                                                                                                                                        #HERMIONE
        $ h_xpos=140 #Defines position of the Hermione's full length sprite. (Default 370). (Center: 140)                                                       #HERMIONE
        $ h_body = "03_hp/13_hermione_main/body_30.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
        show screen hermione_main                                                                                                                                                                                 #HERMIONE
        with d3                         
        her "Профессор!"
        m "Просто скажи \"Я готова\" и иди сюда, девочка."
        hide screen hermione_main                                                                                                                                                                                   #HERMIONE
        with d3                                                                                                                                                                                                                        #HERMIONE
        $ h_xpos=140 #Defines position of the Hermione's full length sprite. (Default 370). (Center: 140)                                                       #HERMIONE
        $ h_body = "03_hp/13_hermione_main/body_31.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
        show screen hermione_main                                                                                                                                                                                 #HERMIONE
        with d3                         
        her "..........."
        hide screen hermione_main                                                                                                                                                                                   #HERMIONE
        with d3                                                                                                                                                                                                                        #HERMIONE
        $ h_xpos=140 #Defines position of the Hermione's full length sprite. (Default 370). (Center: 140)                                                       #HERMIONE
        $ h_body = "03_hp/13_hermione_main/body_118.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
        show screen hermione_main                                                                                                                                                                                 #HERMIONE
        with d3                         
        her "Я готова...."
        hide screen hermione_main    
        jump your_ass

    elif request_29_points >= 2: # THIRD EVENT <============================================================== EVENT 03
        m "Мисс Грейнджер..."
        m "Прошлой ночью у меня был сон..."
        g9 "Вы легли на мой стол, раздвинули ноги и я трахал вашу киску со всей силы..."
        hide screen hermione_main                                                                                                                                                                                   #HERMIONE
        with d3                                                                                                                                                                                                                        #HERMIONE
        $ h_xpos=140 #Defines position of the Hermione's full length sprite. (Default 370). (Center: 140)                                                       #HERMIONE
        $ h_body = "03_hp/13_hermione_main/body_120.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
        show screen hermione_main                                                                                                                                                                                 #HERMIONE
        with d3                         
        her "В этом сне, Сэр..."
        hide screen hermione_main                                                                                                                                                                                   #HERMIONE
        with d3                                                                                                                                                                                                                        #HERMIONE
        $ h_xpos=140 #Defines position of the Hermione's full length sprite. (Default 370). (Center: 140)                                                       #HERMIONE
        $ h_body = "03_hp/13_hermione_main/body_47.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
        show screen hermione_main                                                                                                                                                                                 #HERMIONE
        with d3                     
        her "Я получила 65 баллов своему факультету за это?"
        g9 "Да мисс Грейнджер, получили."
        hide screen hermione_main                                                                                                                                                                                   #HERMIONE
        with d3                                                                                                                                                                                                                        #HERMIONE
        $ h_xpos=140 #Defines position of the Hermione's full length sprite. (Default 370). (Center: 140)                                                       #HERMIONE
        $ h_body = "03_hp/13_hermione_main/body_66.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
        show screen hermione_main                                                                                                                                                                                 #HERMIONE
        with d3                     
        her "..............................."
        her "Дайте мне хотя бы снять свои трусики..."
        stop music fadeout 1.0
        hide screen hermione_main
        with d3
        show screen blkfade
        with d3
        # SEX
        
        $ renpy.play('sounds/gltch.mp3')
        with hpunch
        with kissiris
        show screen h_head2                                                             # HERMIONE
        $ h_body = "03_hp/13_hermione_main/body_130.png" # HERMIONE
        her2 "Ооооооохххх....{image=textheart.png}"
        hide screen h_head2
        
        hide screen hermione_main                                                                                                                                                                                   #HERMIONE
        hide screen genie
        $ genie_chibi_xpos = -210 #-185 behind the desk. (Also 5 is something).
        $ genie_chibi_ypos = 10
        $ g_c_u_pic = "sex_ani"
        show screen chair_02
        show screen g_c_u
        
        hide screen hermione_02 #Hermione stands still.
        hide screen blkfade
        hide screen blktone
        hide screen bld1
        show screen ctc
        with fade
        pause
        play music "music/(Orchestral) Playful Tension by Shadow16nh.mp3" fadein 1 fadeout 1 # SEX THEME.
        show screen bld1
        with d3    


        show screen h_head2                                                             # HERMIONE
        $ h_body = "03_hp/13_hermione_main/body_131.png" # HERMIONE
        her "Ах...{image=textheart.png}"
        hide screen h_head2      
        m "Твоя киска сегодня легче приняла мой член сегодня..."
        show screen h_head2                                                             # HERMIONE
        $ h_body = "03_hp/13_hermione_main/body_131.png" # HERMIONE    
        her "Да...{image=textheart.png} аааах...?{image=textheart.png}"
        show screen h_head2                                                             # HERMIONE
        $ h_body = "03_hp/13_hermione_main/body_132.png" # HERMIONE    
        her "Это из-за вас, Сэр...{image=textheart.png}"
        show screen h_head2                                                             # HERMIONE
        $ h_body = "03_hp/13_hermione_main/body_134.png" # HERMIONE    
        her2 "Вы долбите моё маленькую киску своим гиганстким членом...{image=textheart.png}"
        hide screen h_head2     
        g4 "Аааа, шлюха!"
        show screen h_head2                                                             # HERMIONE
        $ h_body = "03_hp/13_hermione_main/body_134.png" # HERMIONE    
        her "Ох...{image=textheart.png}{image=textheart.png}"
        hide screen h_head2     

        
        
#        if not ask_me_once: #Turns true after Hermione asks you about your true identity, during sex.
#            $ ask_me_once = True #Turns true after Hermione asks you about your true identity, during sex.
#            her "Профессор, могу я у вас кое что попросить?"
#            m "Что такое,девоччка?"
#            her "Ах... О, не так глубоко,пожалуйста..."
#            her "О... Я... а..."
#            her "?!!"
#            her "Профессор? Почему вы не остановились?"
#            m "Что ты хочешь у меня попросить, девочка?"
#            her "Мне кажется,я готова кончить..."
#            m "Уже? Хорошо,что я не остановился."
#            her "Сэр, пожалуйста..."
#            her "Я хочу у вас кое что спросить,Сэр..."
#            her "Пока вы трахаете меня..."
#            her "Ааа..."
#            her "Сэр, Я просто хочу знать..."
#            her "Вы правда профессор Дамбалдор?"
#            g4 "ЧТО!?"
#            menu:
#                m "!!!"
#                "\"Да! Альбус Дамбалдор! Это я!\"":
#                    her "Оо..."
#                    her "Вы в последнее время какой-то сам не свой..."
#                    g4 "Ты шлюха! Твоя маленькая киска самая лучшая!"
#                    her "Я думаю мне просто показалось..."
#                    her "А-ах-ааах..."
#                "\"Ты поймала меня... Правда в том,что...\"":
        m "Да! Тебе нравится,когда я трахаю тебя так?"
        show screen h_head2                                                             # HERMIONE
        $ h_body = "03_hp/13_hermione_main/body_128.png" # HERMIONE    
        her "Да, Сэр..."
        hide screen h_head2  
        menu:
            g4 "..."
            "\"Быть нежным,но страстным.\"":
                m "Да, тебе нравится это?"
                show screen h_head2                                                             # HERMIONE
                $ h_body = "03_hp/13_hermione_main/body_127.png" # HERMIONE    
                her "Да, сэр... ах...{image=textheart.png}"
                hide screen h_head2  
                m "Хорошая девочка!"
                m "Просто расслабься и прими мой член в себя!"
                show screen h_head2                                                             # HERMIONE
                $ h_body = "03_hp/13_hermione_main/body_127.png" # HERMIONE    
                her "Да... ах...{image=textheart.png}"
                hide screen h_head2  
                m "Почти... почти..."
                show screen h_head2                                                             # HERMIONE
                $ h_body = "03_hp/13_hermione_main/body_131.png" # HERMIONE    
                her "Да...{image=textheart.png}{image=textheart.png}"
                hide screen h_head2  
                m "Да, моя маленькая принцесса..."
                show screen h_head2                                                             # HERMIONE
                $ h_body = "03_hp/13_hermione_main/body_119.png" # HERMIONE    
                her "Что?"
                show screen h_head2                                                             # HERMIONE
                $ h_body = "03_hp/13_hermione_main/body_118.png" # HERMIONE    
                her "Нет, пожалуйста, не называйте меня так... ах...{image=textheart.png}"
                her2 "Мой папа меня так называл,когда я была маленькая..."
                hide screen h_head2  
                m "Ну, сейчас я твой папочка!"
                show screen h_head2                                                             # HERMIONE
                $ h_body = "03_hp/13_hermione_main/body_121.png" # HERMIONE    
                her "Ах...{image=textheart.png} Ах-а...{image=textheart.png}{image=textheart.png}"
                hide screen h_head2  
                m "И ты моя маленькая принцесса - шлюха!"
                show screen h_head2                                                             # HERMIONE
                $ h_body = "03_hp/13_hermione_main/body_123.png" # HERMIONE    
                her "Ах...{image=textheart.png} ох...{image=textheart.png}{image=textheart.png}{image=textheart.png}"
            "\"Быть жестким с ней!\"":
                hide screen h_head2  
                m "Да,ты шлюха!"
                m "Я научу тебя наслаждаться каждым моментом, когда трахаю!"
                show screen blktone
                hide screen ctc
                with d3
                ">Вы увеличиваете темп."
                hide screen blktone
                with d3
                show screen h_head2                                                             # HERMIONE
                $ h_body = "03_hp/13_hermione_main/body_131.png" # HERMIONE    
                her "Ахх...{image=textheart.png} Профессор..."
                hide screen h_head2  
                m "Ты - ненасытная шлюха!"
                show screen h_head2                                                             # HERMIONE
                $ h_body = "03_hp/13_hermione_main/body_132.png" # HERMIONE    
                her "А...{image=textheart.png} Ох...{image=textheart.png}"
                hide screen h_head2  
                m "Ты - позор для своего факультета!"
                show screen h_head2                                                             # HERMIONE
                $ h_body = "03_hp/13_hermione_main/body_132.png" # HERMIONE    
                her "А-ох...{image=textheart.png}{image=textheart.png}{image=textheart.png}"
                hide screen h_head2  
                m "Твои родители послали тебя учиться, а не трахаться со студентами и преподователями!"
                show screen h_head2                                                             # HERMIONE
                $ h_body = "03_hp/13_hermione_main/body_132.png" # HERMIONE    
                her "Ах-а...{image=textheart.png} Но я всё это делаю для...--"
                hide screen h_head2  
                m "Всем наплевать, зачем ты это делаешь, любительница членов!"
                m "Посмотри кем ты стала!"
                m "Скачешь задницей на члене старого профессора, как самая дешевая шлюха!"
                show screen h_head2                                                             # HERMIONE
                $ h_body = "03_hp/13_hermione_main/body_134.png" # HERMIONE    
                her "Ох...{image=textheart.png} Нет...{image=textheart.png} прекратите это говорить...{image=textheart.png} ах...{image=textheart.png}{image=textheart.png}{image=textheart.png}"
                hide screen h_head2  
                show screen blktone
                with d3
                ">Вы увеличиваете снова темп."
                $ g_c_u_pic = "sex2_ani"
                ">Комнату наполняет звук шлёпания и стонов..."
                hide screen blktone
                with d3
                m "Ты позволила мне лапать тебя... Ты сосешь мой член..."
                m "Так скажи мне, кто ты после этого!?"
                show screen h_head2                                                             # HERMIONE
                $ h_body = "03_hp/13_hermione_main/body_123.png" # HERMIONE    
                her "................"
                show screen h_head2                                                             # HERMIONE
                $ h_body = "03_hp/13_hermione_main/body_132.png" # HERMIONE    
                her "Ах...{image=textheart.png} Ах....{image=textheart.png}{image=textheart.png}{image=textheart.png}"
                show screen h_head2                                                             # HERMIONE
                $ h_body = "03_hp/13_hermione_main/body_118.png" # HERMIONE    
                her "......................."
                her "{size=-5}Я шлюха...{/size}"
                her "{size=-5}Я шлюха... ах...{\size}"
                hide screen h_head2  
        
        m "Да! Вот кто ты есть на самом деле!"
        show screen h_head2                                                             # HERMIONE
        $ h_body = "03_hp/13_hermione_main/body_118.png" # HERMIONE  
        her "Ах... а... а..."
        her "Сэр, вы можете... а..."
        hide screen h_head2  
        m "Что?"
        show screen h_head2                                                             # HERMIONE
        $ h_body = "03_hp/13_hermione_main/body_138.png" # HERMIONE  
        her "Вы можете отшлепать меня... ох...?"
        hide screen h_head2  
        g4 "С удовольствием!"
        
        $ renpy.play('sounds/slap.mp3')
        show screen white 
        pause.1
        hide screen white
        with hpunch

        show screen h_head2                                                             # HERMIONE
        $ h_body = "03_hp/13_hermione_main/body_139.png" # HERMIONE  
        her "АА-А-АХ!{image=textheart.png}{image=textheart.png}{image=textheart.png}"
        hide screen h_head2  
        m "Тебе нравится, а?"
        $ renpy.play('sounds/slap.mp3')
        show screen white 
        pause.1
        hide screen white
        with hpunch
        show screen h_head2                                                             # HERMIONE
        $ h_body = "03_hp/13_hermione_main/body_138.png" # HERMIONE  
        her "А..!{image=textheart.png} ОООО ДА!{image=textheart.png}{image=textheart.png}{image=textheart.png}"
        hide screen h_head2  
        m "И ещё...ещё!"
        $ renpy.play('sounds/slap.mp3')
        show screen white 
        pause.1
        hide screen white
        with hpunch
        show screen h_head2                                                             # HERMIONE
        $ h_body = "03_hp/13_hermione_main/body_138.png" # HERMIONE  
        her "Ах! ДА!"
        hide screen h_head2     
        show screen blktone
        with d3
        ">Вы заметили, что после каждого шлепка по заднице девченки, её киска сжимается на пару секунд и сжимает ваш член..."
        ">Вам нравятся эти ощущения..."
        ">Вы продолжали шлёпать по попке Гермионы."
        ">Каждый удар по заднице сопровождался вздохами наслаждения Гермионы."
        $ renpy.play('sounds/slap.mp3')
        show screen white 
        pause.1
        hide screen white
        with hpunch
        $ renpy.play('sounds/slap.mp3')
        show screen white 
        pause.1
        hide screen white
        with hpunch
        $ renpy.play('sounds/slap.mp3')
        show screen white 
        pause.1
        hide screen white
        with hpunch
        $ renpy.play('sounds/slap.mp3')
        show screen white 
        pause.1
        hide screen white
        with hpunch
        $ renpy.play('sounds/slap.mp3')
        show screen white 
        pause.1
        hide screen white
        with hpunch
        show screen h_head2                                                             # HERMIONE
        $ h_body = "03_hp/13_hermione_main/body_138.png" # HERMIONE  
        her "АААА!!!{image=textheart.png}{image=textheart.png}{image=textheart.png} БОЛЬНО!{image=textheart.png}{image=textheart.png}{image=textheart.png}"
        show screen h_head2                                                             # HERMIONE
        $ h_body = "03_hp/13_hermione_main/body_134.png" # HERMIONE  
        her2 "Это больно...{image=textheart.png}{image=textheart.png}{image=textheart.png} больно...{image=textheart.png}{image=textheart.png}{image=textheart.png}"
        hide screen h_head2 
        m "М?"
        m "Почему твои ноги так дрожат, малышка?"
        m "Ты кончаешь?"
        show screen h_head2                                                             # HERMIONE
        $ h_body = "03_hp/13_hermione_main/body_133.png" # HERMIONE  
        her "Да...{image=textheart.png}{image=textheart.png}{image=textheart.png}{image=textheart.png}{image=textheart.png}{image=textheart.png}"
        hide screen h_head2 
        m "Тогда я последую твоему примеру."
        show screen h_head2                                                             # HERMIONE
        $ h_body = "03_hp/13_hermione_main/body_133.png" # HERMIONE  
        her ".............."
        hide screen h_head2 
        show screen blktone 
        with d3
        ">Вы стали трахать Гермиону всё сильнее и жестче!"
        hide screen blktone 
        with d3
        show screen h_head2                                                             # HERMIONE
        $ h_body = "03_hp/13_hermione_main/body_139.png" # HERMIONE  
        her "А! Нет! Я не могу...{image=textheart.png} Я...{image=textheart.png} Ох...{image=textheart.png}{image=textheart.png}{image=textheart.png}"
        hide screen h_head2 
        m "Заткнись, шлюха!"
        g4 "Ах"
        menu:
            "- Кончить в Гермиону -":
                with hpunch
                g4 "{size=+7}Да, почувствуй всё до капали!!!{/size}"
                show screen white 
                pause.1
                hide screen white
                pause.2
                show screen white 
                pause .1
                hide screen white
                with hpunch
                g4 "{size=+15}АРГХ!!!!!!!!!!!!!!!!{/size}"
                $ g_c_u_pic = "sex_cum_in_ani"
                show screen white 
                pause.1
                hide screen white
                pause.2
                show screen white 
                pause .1
                hide screen white
                with hpunch
                show screen ctc
                pause
                hide screen ctc
                $ uni_sperm = True
                $ u_sperm = "03_hp/13_hermione_main/auto_08.png"
                show screen h_head2                                                             # HERMIONE
                $ h_body = "03_hp/13_hermione_main/body_133.png" # HERMIONE
                her "!!!"
                her "ААА, Вы наполняете меня до краёв!{image=textheart.png}{image=textheart.png}{image=textheart.png}"
                hide screen h_head2  
                g4 "Я ещё не закончил,сучка!"
                g4 "{size=+15}Аааа!!!!!!!!!!!!!!!!{/size}"
                show screen white 
                pause.1
                hide screen white
                pause.2
                show screen white 
                pause .1
                hide screen white
                with hpunch
                show screen h_head2                                                             # HERMIONE
                $ h_body = "03_hp/13_hermione_main/body_139.png" # HERMIONE
                her "Ааа,мой живот!"
                hide screen h_head2    
                g4 "{size=+5}ШЛЮХА!{/size}"






                hide screen h_head2     
                hide screen bld1
                with d3
                show screen ctc
                pause
                hide screen ctc
                show screen bld1
                with d3
                $ g_c_u_pic = "03_hp/08_animation_02/23_cum_19.png"

                show screen blktone
                with d7
               

                
                
                
                
    
 
                
                m "Это было великолепно..."
                show screen h_head2                                                             # HERMIONE
                $ h_body = "03_hp/13_hermione_main/body_133.png" # HERMIONE
                her "Ааа...{image=textheart.png}"
                hide screen h_head2
                m "Ты в порядке, сучка? Всмысле девочка."
                show screen h_head2                                                             # HERMIONE
                $ h_body = "03_hp/13_hermione_main/body_133.png" # HERMIONE
                her "Да... Я..."
                show screen h_head2                                                             # HERMIONE
                $ h_body = "03_hp/13_hermione_main/body_135.png" # HERMIONE
                her "Я чувствую как вы меня заполнили..."
                show screen h_head2                                                             # HERMIONE
                $ h_body = "03_hp/13_hermione_main/body_130.png" # HERMIONE
                her "!!!"
                her "Вы кончили в меня, Сэр!"
                hide screen h_head2     
                m "Да я заполнил тебя."
                show screen h_head2                                                             # HERMIONE
                $ h_body = "03_hp/13_hermione_main/body_131.png" # HERMIONE
                her "Вам не стоило этого делать..."
                hide screen h_head2     
                m "Разве ты не получила удовольствие от моей горячей спермы?"
                show screen h_head2                                                             # HERMIONE
                $ h_body = "03_hp/13_hermione_main/body_123.png" # HERMIONE
                her "....возможно."
                show screen h_head2                                                             # HERMIONE
                $ h_body = "03_hp/13_hermione_main/body_121.png" # HERMIONE
                her "Помоему я кончила несколько раз..."
                show screen blkfade
                with d3
                show screen h_head2                                                             # HERMIONE
                $ h_body = "03_hp/13_hermione_main/body_122.png" # HERMIONE
                her2 "Может вы и правы,Сэр, и я не должна об этом беспокоиться."
                her "Мы можем расчитаться?"
                hide screen h_head2     

            "- Обкончать Гермиону -":
                
                with hpunch
                g4 "{size=+7}Аргх!!!{/size}"
                

                show screen white 
                pause.1
                hide screen white
                pause.2
                show screen white 
                pause .1
                hide screen white
                with hpunch
                g4 "{size=+15}ААА!!!!!!!!!!!!!!!!{/size}"
                $ g_c_u_pic = "sex_cum_out_ani"
                show screen white 
                pause.1
                hide screen white
                pause.2
                show screen white 
                pause .1
                hide screen white
                with hpunch
                show screen ctc
                pause
                hide screen ctc
                $ uni_sperm = True
                $ u_sperm = "03_hp/13_hermione_main/auto_08.png"
                show screen h_head2                                                             # HERMIONE
                $ h_body = "03_hp/13_hermione_main/body_133.png" # HERMIONE
                her2 "ААА...{image=textheart.png}{image=textheart.png}{image=textheart.png}"
                hide screen h_head2
                g4 "{size=+5}ШЛЮХА! Получи всё!{/size}"
                show screen h_head2                                                             # HERMIONE
                $ h_body = "03_hp/13_hermione_main/body_138.png" # HERMIONE
                her "{size=+5}!!!{/size}"
                hide screen h_head2
                hide screen h_head2     
                hide screen bld1
                with d3
                show screen ctc
                pause
                hide screen ctc
                show screen bld1
                with d3
                $ g_c_u_pic = "sex_cum_out_blink_ani"
                
                


                
                m "Это было здорово..."
                show screen h_head2                                                             # HERMIONE
                $ h_body = "03_hp/13_hermione_main/body_138.png" # HERMIONE
                her "Ах...{image=textheart.png}"
                hide screen h_head2                                                             
                m "Как ты, шлюха??"
                show screen h_head2                                                             # HERMIONE
                $ h_body = "03_hp/13_hermione_main/body_133.png" # HERMIONE
                her "Да... Я..."
                hide screen h_head2         
                m "Ты наслаждалась этим?"
                show screen h_head2                                                             # HERMIONE
                $ h_body = "03_hp/13_hermione_main/body_123.png" # HERMIONE
                her "....думаю да..."
                hide screen h_head2       
                show screen ctc
                pause
                hide screen ctc
                show screen blkfade
                with d3
                show screen h_head2                                                             # HERMIONE
                $ h_body = "03_hp/13_hermione_main/body_121.png" # HERMIONE
                her "Думаю,я кончила несколько раз,Сэр..."
                show screen h_head2                                                             # HERMIONE
                $ h_body = "03_hp/13_hermione_main/body_122.png" # HERMIONE
                her "Мы можем расчитаться?"
                hide screen h_head2     
        
        
    $ uni_sperm = False #Sperm layer is not displayed in hermione screen.
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
    hide screen blktone
    with d3
    
    stop music fadeout 4.0
    m "Да, мисс Грейнджер, 65 очков \"Гриффиндору\" ." 
    $ gryffindor +=65
    $ h_xpos=140 #Defines position of the Hermione's full length sprite. (Default 370). (Center: 140)
    $ h_body = "03_hp/13_hermione_main/body_13.png" #Flashing panties
    show screen hermione_main
    hide screen hermione_01_f #Hermione stands still.
    with d3
    her "Спасибо, Сэр..."

    if whoring <= 20: # Level 07 <
        $ whoring +=1




    if request_29_points == 0:
        $ new_request_29_01 = True # HEARTS
    if request_29_points == 1:
        $ new_request_29_02 = True # HEARTS
    if request_29_points >= 2:
        $ new_request_29_03 = True # HEARTS



    $ request_29_points += 1

    hide screen bld1
    hide screen hermione_main
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

    $ aftersperm = False #Show cum stains on Hermione's uniform.

    #call music_block 
    
    if daytime:
        jump night_start
    else:
        jump day_start
                   
   

 
 
###############################################################################################################################
### LEVEL 09 ##################################################################################################################
###################REQUEST_31 (Level 08) (75 pt.) (Anal sex).  #####################################################
label new_request_31: #LV.8 (Whoring = 21 - 23)
    hide screen hermione_main 
    with d3
    m "{size=-4}(Должен ли я попросить её заняться со мной анальным сексом?){/size}"
    $ menu_x = 0.5 #Default position of the menu (0.5). Version B is $ menu_x = 0.2
    menu:
        "\"(Да, давай!)\"":
            show screen blktone
            with d3
            pass
        "\"(Не сейчас.)\"":
            jump new_personal_request
            
 
    if request_31_points == 0: # FIRST EVENT <============================================================== EVENT 01
        m "Мисс Грейнджер..."
        hide screen hermione_main                                                                                                                                                                                   #HERMIONE
        with d3                                                                                                                                                                                                                        #HERMIONE
        $ h_xpos=140 #Defines position of the Hermione's full length sprite. (Default 370). (Center: 140)                                                       #HERMIONE
        $ h_body = "03_hp/13_hermione_main/body_17.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
        show screen hermione_main                                                                                                                                                                                 #HERMIONE
        with d3                         
        her "Сэр..?"
        m "Насколько вы знакомы с термином \"Анальный секс\"?"
        if whoring <=20:
            jump too_much
        hide screen hermione_main                                                                                                                                                                                   #HERMIONE
        with d3                                                                                                                                                                                                                        #HERMIONE
        $ h_xpos=140 #Defines position of the Hermione's full length sprite. (Default 370). (Center: 140)                                                       #HERMIONE
        $ h_body = "03_hp/13_hermione_main/body_79.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
        show screen hermione_main                                                                                                                                                                                 #HERMIONE
        with d3                         
        her "90 очков..."
        m "Что?"
        hide screen hermione_main                                                                                                                                                                                   #HERMIONE
        with d3                                                                                                                                                                                                                        #HERMIONE
        $ h_xpos=140 #Defines position of the Hermione's full length sprite. (Default 370). (Center: 140)                                                       #HERMIONE
        $ h_body = "03_hp/13_hermione_main/body_66.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
        show screen hermione_main                                                                                                                                                                                 #HERMIONE
        with d3                                                                                                                                                                                                                        #HERMIONE          
        her "............................."
        m "Хорошо,пусть будет так. 90 очков."
        hide screen hermione_main   
        
        
        label lucky_guess:
            
        show screen blkfade
        with d3
        
        stop music fadeout 1.0
        
        $ her_head_xpos=390 #Defines position of the Hermione's full length sprite. (Default 370). 140 - center. Bottom right: 390
        $ her_head_ypos=340 #Defines position of the Hermione's full length sprite. (Default 0). Right bottom corner: 340 - head only. 235 - tits.
        show screen h_head2                                                             # HERMIONE
        $ h_body = "03_hp/13_hermione_main/body_29.png" # HERMIONE
        her "..........."
        hide screen h_head2      
        m "Давай посмотрим..."
        show screen h_head2                                                             # HERMIONE
        $ h_body = "03_hp/13_hermione_main/body_34.png" # HERMIONE
        her "................."
        hide screen h_head2      
        m "Хм..."
        show screen h_head2                                                             # HERMIONE
        $ h_body = "03_hp/13_hermione_main/body_18.png" # HERMIONE
        her "!!!"
        hide screen h_head2      
        g4 "Да ладно...!"
        show screen h_head2                                                             # HERMIONE
        $ h_body = "03_hp/13_hermione_main/body_20.png" # HERMIONE
        her "АЙ!"
        hide screen h_head2      
        m "Просто постарайся расслабиться немного,хорошо?"
        show screen h_head2                                                             # HERMIONE
        $ h_body = "03_hp/13_hermione_main/body_21.png" # HERMIONE
        her "Я стараюсь!"
        hide screen h_head2      
        m "Хорошо,что если я сделаю так..?"
        show screen h_head2                                                             # HERMIONE
        $ h_body = "03_hp/13_hermione_main/body_20.png" # HERMIONE
        her "АЙ! Что вы делаете, Сэр?"
        hide screen h_head2      
        m "Ладно, это не сработает..."
        m "Хм..."
        m "Хорошо,я знаю что мы сделаем."
        menu:
            m "..."
            "\"Хорошо,попробую всунуть член и посильнее войти!\"":
                play music "music/(Orchestral) Playful Tension by Shadow16nh.mp3" fadein 1 fadeout 1 # SEX THEME.
                show screen h_head2                                                             # HERMIONE
                $ h_body = "03_hp/13_hermione_main/body_18.png" # HERMIONE
                her "Посильнее войти, Сэр?!"
                hide screen h_head2      
                $ renpy.play('sounds/spit.mp3') #Sound of spiting. 
                g3 "*Хлоп!*"
                show screen h_head2                                                             # HERMIONE
                $ h_body = "03_hp/13_hermione_main/body_32.png" # HERMIONE
                her "Ааааааааааааааайййййй!"
                show screen h_head2                                                             # HERMIONE
                $ h_body = "03_hp/13_hermione_main/body_31.png" # HERMIONE
                her "Нет,Сэр, подождите! Может быть я просто расслаблюсь-"
                hide screen h_head2      
                m "Не надо, Я уже вхожу!"
                with hpunch
                show screen h_head2                                                             # HERMIONE
                $ h_body = "03_hp/13_hermione_main/body_22.png" # HERMIONE
                her "ААААА!"
                show screen h_head2                                                             # HERMIONE
                $ h_body = "03_hp/13_hermione_main/body_20.png" # HERMIONE
                her "АЙ! АЙ! АЙ!"
                hide screen h_head2      
                g4 "Почти вошёл!"
                show screen h_head2                                                             # HERMIONE
                $ h_body = "03_hp/13_hermione_main/body_32.png" # HERMIONE
                her "Нет, Мне больно! Мне больно!"
                hide screen h_head2      
                g4 "Почти! Почти!"
                show screen h_head2                                                             # HERMIONE
                $ h_body = "03_hp/13_hermione_main/body_32.png" # HERMIONE
                her "АЙ! Больно!"
                hide screen h_head2      
                g4 "Заткнись,девченка! Я делаю тебе одолжение!"
                g4 "Твой анус такой узкий и почти не возможно тебя трахнуть в задницу,а я исправляют это!"
                show screen h_head2                                                             # HERMIONE
                $ h_body = "03_hp/13_hermione_main/body_20.png" # HERMIONE
                her "Тогда остановитесь, пожалуйста!"
                hide screen h_head2      
                m "Нет! Нам нужно расширить твою дырочку!"
                show screen h_head2                                                             # HERMIONE
                $ h_body = "03_hp/13_hermione_main/body_20.png" # HERMIONE
                her "Но я не хочу,что бы вы это делали!"
                hide screen h_head2      
                m "Правда? Как ты тогда думаешь, люди буду иметь тебя в задницу?"
                show screen h_head2                                                             # HERMIONE
                $ h_body = "03_hp/13_hermione_main/body_132.png" # HERMIONE
                her "Какие люди?"
                hide screen h_head2      
                g4 "Ну ты знаешь... люди."
                g4 "Аааа,черт... Моему члену теперь тоже больно...."
                show screen h_head2                                                             # HERMIONE
                $ h_body = "03_hp/13_hermione_main/body_131.png" # HERMIONE
                her "Остановитесь тогда! Остановитесь,Сэр!"
                her "Я передумала! Мне не нужно 90 баллов!"
                hide screen h_head2      
                g4 "Помоему я почти..."
                
                $ renpy.play('sounds/gltch.mp3')
                with hpunch
                with kissiris
                show screen h_head2                                                             # HERMIONE
                $ h_body = "03_hp/13_hermione_main/body_130.png" # HERMIONE
                her2 "{size=+5}Ааааай!!!{/size}"
                hide screen h_head2
                g4 "Да!!!"
                show screen h_head2                                                             # HERMIONE
                $ h_body = "03_hp/13_hermione_main/body_130.png" # HERMIONE
                her "AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA!"
                hide screen h_head2
                g4 "Давай наполним это маленькую дырочку спермой?"
                show screen h_head2                                                             # HERMIONE
                $ h_body = "03_hp/13_hermione_main/body_137.png" # HERMIONE
                her "ДА... Пожалуйста,я уже хочу закончить это..."
                hide screen h_head2




                hide screen hermione_main                                                                                                                                                                                   #HERMIONE
                hide screen genie
                $ genie_chibi_xpos = -210 #-185 behind the desk. (Also 5 is something).
                $ genie_chibi_ypos = 10
                $ g_c_u_pic = "sex_slow_ani"
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
                        
                        
                        
                
                
                
                
                #SCHUSH!
                
               
                g4 "Ааа... Ты хочешь побыстрее закончить?"
                g4 "Помоги мне тогда!"
                show screen h_head2                                                             # HERMIONE
                $ h_body = "03_hp/13_hermione_main/body_139.png" # HERMIONE
                her "*всхлип* Как?"
                hide screen h_head2       
                g4 "Ты знаешь..."
                show screen h_head2                                                             # HERMIONE
                $ h_body = "03_hp/13_hermione_main/body_139.png" # HERMIONE
                her "Ох..."
                show screen h_head2                                                             # HERMIONE
                $ h_body = "03_hp/13_hermione_main/body_140.png" # HERMIONE
                her "Я шлюха??"
                hide screen h_head2    
                g9 "Да,вот кто ты!"
                show screen h_head2                                                             # HERMIONE
                $ h_body = "03_hp/13_hermione_main/body_141.png" # HERMIONE
                her "*Хнык!* Я шлюха..."
                her "Я люблю сосать члены..."
                show screen h_head2                                                             # HERMIONE
                $ h_body = "03_hp/13_hermione_main/body_142.png" # HERMIONE
                her2 "И моя узкая дырочка сейчас будет разорвана на части... *Хнык!*"
                hide screen h_head2    
                g4 "Да! Даа!"
                g4 "Аааа! Да!"
                show screen h_head2                                                             # HERMIONE
                $ h_body = "03_hp/13_hermione_main/body_144.png" # HERMIONE
                her "Нет! Он ещё растёт во мне?! Я боюсь!"
                hide screen h_head2    
                g4 "Аааа!"

                
            "\"Отсоси сначала у меня, смажь мой член!\"":
                show screen h_head2                                                             # HERMIONE
                $ h_body = "03_hp/13_hermione_main/body_31.png" # HERMIONE
                her "Аа... Хорошо..."
                hide screen h_head2    
                play music "music/(Orchestral) Playful Tension by Shadow16nh.mp3" fadein 1 fadeout 1 # SEX THEME.
                #SUCKING
                
                hide screen blkfade
                
                
                hide screen hermione_main                                                                                                                                                                                   #HERMIONE
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
                        
                
                
                
                
                
                
                
                her "*Хлюп-хлюп-хлюп-хлюп!*"
                hide screen h_head2    
                m "Да... хорошо..."
                her "*Хлюп!* *Хлюп!* *Хлюп!*"
                hide screen h_head2    
                m "Отлично, Думаю, достаточно. Ложись обратно на стол."
                show screen blkfade
                with d3

                
                #ON THE DESK
                show screen h_head2                                                             # HERMIONE
                $ h_body = "03_hp/13_hermione_main/body_31.png" # HERMIONE
                her "............."
                hide screen h_head2    
                g4 "Да! Почти!"
                show screen h_head2                                                             # HERMIONE
                $ h_body = "03_hp/13_hermione_main/body_32.png" # HERMIONE
                her "Ау!"
                hide screen h_head2    
                m "Раслабься. Почти вошёл."
                
                $ renpy.play('sounds/gltch.mp3')
                with hpunch
                with kissiris
                show screen h_head2                                                             # HERMIONE
                $ h_body = "03_hp/13_hermione_main/body_130.png" # HERMIONE
                her2 "{size=+5}AAAAAAAA!!!{/size}"
                hide screen h_head2
                g4 "ДА!!!"
                show screen h_head2                                                             # HERMIONE
                $ h_body = "03_hp/13_hermione_main/body_130.png" # HERMIONE
                her "Моя... моя..."
                show screen h_head2                                                             # HERMIONE
                $ h_body = "03_hp/13_hermione_main/body_132.png" # HERMIONE
                her "Больно!"
                hide screen h_head2
                g4 "Давай заполним эту дырочку спермой до отказа?"
                show screen h_head2                                                             # HERMIONE
                $ h_body = "03_hp/13_hermione_main/body_141.png" # HERMIONE
                her "....................."
                hide screen h_head2               
                
                # SEX
                
                hide screen hermione_main                                                                                                                                                                                   #HERMIONE
                hide screen genie
                $ genie_chibi_xpos = -210 #-185 behind the desk. (Also 5 is something).
                $ genie_chibi_ypos = 10
                $ g_c_u_pic = "sex_slow_ani"
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


                show screen h_head2                                                             # HERMIONE
                $ h_body = "03_hp/13_hermione_main/body_139.png" # HERMIONE
                her "....................."
                hide screen h_head2    
                m "Как ты, шлюшка?"
                show screen h_head2                                                             # HERMIONE
                $ h_body = "03_hp/13_hermione_main/body_140.png" # HERMIONE
                her2 "Ааа... Вы... разорвали меня изнутри... сэр."
                show screen h_head2                                                             # HERMIONE
                $ h_body = "03_hp/13_hermione_main/body_141.png" # HERMIONE
                her "И до сих пор болит..."
                hide screen h_head2    
                m "Хм..."
                m "Может было недостаточно смазки...?"
                m "Успокойся, девочка. Пососи мой член ещё."
                show screen h_head2                                                             # HERMIONE
                $ h_body = "03_hp/13_hermione_main/body_140.png" # HERMIONE
                her "Что? Но..."
                show screen h_head2                                                             # HERMIONE
                $ h_body = "03_hp/13_hermione_main/body_139.png" # HERMIONE
                her "Он грязный... Он уже был в моей попке."
                hide screen h_head2    
                m "Да,он был в тебе, но это не означает что он грязный уже."
                m "Раслабься,девочка. Соси давай."
                show screen h_head2                                                             # HERMIONE
                $ h_body = "03_hp/13_hermione_main/body_139.png" # HERMIONE
                her "..........."
                hide screen h_head2   
                show screen blkfade
                with d3
                
                
                #SUCKING
                
                hide screen blkfade
                
                
                hide screen hermione_main                                                                                                                                                                                   #HERMIONE
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
                
                
                
                
                her "*Хлюп!* *Хлюп!* *Хлюп!*"
                m "ДА... хорошо..."
                her "*Чавк!* *Чавк!* *Чавк!*"
                m "Чувствуешь вкус своей попки на моём члене?"
                her "*Чавк!* *Хлюп!* *Чавк!*"
                m "Ладно, может хватит."
                show screen blkfade
                with d3
               

                
                #ON DESK AGAIN.
                
                
                hide screen hermione_main                                                                                                                                                                                   #HERMIONE
                hide screen genie
                $ genie_chibi_xpos = -210 #-185 behind the desk. (Also 5 is something).
                $ genie_chibi_ypos = 10
                $ g_c_u_pic = "sex_ani"
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
                
                show screen h_head2                                                             # HERMIONE
                $ h_body = "03_hp/13_hermione_main/body_139.png" # HERMIONE
                her "Ах..."
                hide screen h_head2     
                m "Уже лучше?"
                show screen h_head2                                                             # HERMIONE
                $ h_body = "03_hp/13_hermione_main/body_140.png" # HERMIONE
                her "Всё ещё больно..."
                her "Но думаю всё будет в порядке..."
                hide screen h_head2     
                m "Я тогда буду входить по медленнее..."
                show screen h_head2                                                             # HERMIONE
                $ h_body = "03_hp/13_hermione_main/body_141.png" # HERMIONE
                her "Ах... спасибо, Сэр."
                hide screen h_head2     
                m "О... да... вот так лучше...да..."
                show screen h_head2                                                             # HERMIONE
                $ h_body = "03_hp/13_hermione_main/body_139.png" # HERMIONE
                her "..........."
                hide screen h_head2     
                m "Ммм...да... Такая узкая..."
                show screen h_head2                                                             # HERMIONE
                $ h_body = "03_hp/13_hermione_main/body_143.png" # HERMIONE
                her "................"
                hide screen h_head2     
                m "Почему ты замолчала,девочка?"
                show screen h_head2                                                             # HERMIONE
                $ h_body = "03_hp/13_hermione_main/body_140.png" # HERMIONE
                her "Просто это больно..."
                her "И я просто хочу, что бы вы по скорее кончили, Сэр..."
                hide screen h_head2     
                m "Ты пытаешься сдержать слёзы от боли?"
                show screen h_head2                                                             # HERMIONE
                $ h_body = "03_hp/13_hermione_main/body_142.png" # HERMIONE
                her "Да, сэр. *Хнык!*"
                hide screen h_head2     
                m "Не надо сдерживаться."
                m "Плачь, кричи, рыдай столько,сколько захочешь!"
                show screen h_head2                                                             # HERMIONE
                $ h_body = "03_hp/13_hermione_main/body_140.png" # HERMIONE
                her "Н-но--"
                hide screen h_head2     
                m "Тогда я кончу быстрее."
                show screen h_head2                                                             # HERMIONE
                $ h_body = "03_hp/13_hermione_main/body_142.png" # HERMIONE
                her "Правда? *Хнык!*"
                show screen h_head2                                                             # HERMIONE
                $ h_body = "03_hp/13_hermione_main/body_139.png" # HERMIONE
                her "*Хнык!* Больно! *Хнык!* Как же это больно! *Хнык!*"
                hide screen h_head2     
                m "Да, ещё..."
                show screen h_head2                                                             # HERMIONE
                $ h_body = "03_hp/13_hermione_main/body_145.png" # HERMIONE
                her "*Хнык!*"
                hide screen h_head2     
                m "Бедное маленькое дитя..."
                m "Большой и злой человек разрывает твою узкую задницу своим членом!"
                show screen h_head2                                                             # HERMIONE
                $ h_body = "03_hp/13_hermione_main/body_146.png" # HERMIONE
                her "*Хнык!* Дааааа! *Хнык!*"
                hide screen h_head2     
                g4 "О-да!"
                show screen h_head2                                                             # HERMIONE
                $ h_body = "03_hp/13_hermione_main/body_147.png" # HERMIONE
                her "Нет, мне страшно! *Хнык!*"
                hide screen h_head2   
        
        menu:
            "- Заполнить Гермиону спермой -":
                g4 "Оооо!"
                show screen h_head2                                                             # HERMIONE
                $ h_body = "03_hp/13_hermione_main/body_130.png" # HERMIONE  
                her "Нет! АХ!"
                hide screen h_head2    
                
                show screen white 
                pause.1
                hide screen white
                pause.2
                show screen white 
                pause .1
                hide screen white
                with hpunch
                g4 "{size=+15}О-да!!!!!!!!!!!!!!!!{/size}"
                $ g_c_u_pic = "sex_cum_in_ani"
                show screen white 
                pause.1
                hide screen white
                pause.2
                show screen white 
                pause .1
                hide screen white
                with hpunch
                hide screen bld1
                with d3
                show screen ctc
                pause
                hide screen ctc
                $ uni_sperm = True
                $ u_sperm = "03_hp/13_hermione_main/auto_08.png"
                show screen h_head2                                                             # HERMIONE
                $ h_body = "03_hp/13_hermione_main/body_144.png" # HERMIONE
                her "ААА! Я ЧУВСТВУЮ КАК ВЫ МЕНЯ ЗАПОЛНЯЕТЕ !{image=textheart.png}{image=textheart.png}{image=textheart.png}"
                hide screen h_head2  
                
                
                g4 "ДА, ТЫ ПОТАСКУХА! ДАА!"
                show screen h_head2                                                             # HERMIONE
                $ h_body = "03_hp/13_hermione_main/body_145.png" # HERMIONE
                her "БОЛЬНО, БОЛЬНО!"
                hide screen h_head2         
                g4 "Заткнись!"
                with hpunch
                show screen h_head2                                                             # HERMIONE
                $ h_body = "03_hp/13_hermione_main/body_149.png" # HERMIONE
                her "Нет,в меня больше не влезет! Перестань кончать, ТЫ! УБЛЮДОК!"
                hide screen h_head2      
                g4 "Закрой пасть, шлюха! Я ещё не закончил!"
                show screen h_head2                                                             # HERMIONE
                $ h_body = "03_hp/13_hermione_main/body_146.png" # HERMIONE
                her "Нет! Пожалуйста! АААА, МОЙ ЖИВОТ! Я СЕЙЧАС ЛОПНУ!"
                hide screen h_head2   
                g4 "ААА!"
                show screen h_head2                                                             # HERMIONE
                $ h_body = "03_hp/13_hermione_main/body_144.png" # HERMIONE
                her "Нет! Я сейчас взорвусь..."
                hide screen h_head2    
                with hpunch
                show screen h_head2                                                             # HERMIONE
                $ h_body = "03_hp/13_hermione_main/body_150.png" # HERMIONE
                play sound "sounds/burp.mp3"
                her "{size=+7}*ХЛЮП!*!!!!!{/size}"
                show screen h_head2                                                             # HERMIONE
                $ h_body = "03_hp/13_hermione_main/body_151.png" # HERMIONE
                her "......................."
                her "............."
                show screen h_head2                                                             # HERMIONE
                $ h_body = "03_hp/13_hermione_main/body_126.png" # HERMIONE
                $ renpy.play('sounds/gulp.mp3') #Sound of gulping down a liquid.
                her "{size=+7}*ХЛЮП!*{/size}"  
                show screen h_head2                                                             # HERMIONE
                $ h_body = "03_hp/13_hermione_main/body_145.png" # HERMIONE
                her "*Хнык!* Я НЕНАВИЖУ ВАС..."
                show screen h_head2                                                             # HERMIONE
                $ h_body = "03_hp/13_hermione_main/body_148.png" # HERMIONE
                her "{size=+5}Я НЕНАВИЖУ ВАС И ВАШ ГРЯЗНЫЙ СТАРЫЙ ЧЛЕН!{/size}"
                her "{size=+5}Я НЕНАВИЖУ ВАС! ВЫ СЛЫШИТЕ МЕНЯ?!{/size}"
                hide screen h_head2   
                g4 "Аррр...Заткнись, шлюха!"
                show screen h_head2                                                             # HERMIONE
                $ h_body = "03_hp/13_hermione_main/body_145.png" # HERMIONE
                her "*Хнык!* *Хнык!*..."
                hide screen h_head2
                
                
                
                
                
                
                
                # AFTER CUM INSIDE
                
                hide screen bld1
                with d3
                show screen ctc
                pause
                hide screen ctc
                show screen bld1
                with d3
                $ g_c_u_pic = "03_hp/08_animation_02/23_cum_19.png"
                show screen h_head2                                                             # HERMIONE
                $ h_body = "03_hp/13_hermione_main/body_142.png" # HERMIONE
                her "*Хнык!*..."
                hide screen h_head2
                m "УАУ!... Думаю я закончил."
                m "Ты в порядке?"
                show screen h_head2                                                             # HERMIONE
                $ h_body = "03_hp/13_hermione_main/body_142.png" # HERMIONE
                her "Да... *Хнык!*"
                hide screen h_head2 
                m "Ты плачешь?"
                show screen h_head2                                                             # HERMIONE
                $ h_body = "03_hp/13_hermione_main/body_142.png" # HERMIONE
                her "Моя попка болит,но я в порядке,Сэр..."
                hide screen h_head2 
                m "Ну,я должен сказать,что ты стойко приняла мой член..."
                show screen h_head2                                                             # HERMIONE
                $ h_body = "03_hp/13_hermione_main/body_142.png" # HERMIONE
                her "Спасибо,Сэр..."
                hide screen h_head2 

                hide screen bld1
                with d3
                show screen ctc
                pause
                hide screen ctc
                show screen blkfade
                with d7
                show screen h_head2                                                             # HERMIONE
                $ h_body = "03_hp/13_hermione_main/body_152.png" # HERMIONE
                her "Извините, что я сказала что ненавижу вас,Сэр..."
                her "И ваш ненасытный член..."
                show screen h_head2                                                             # HERMIONE
                $ h_body = "03_hp/13_hermione_main/body_153.png" # HERMIONE
                her "Не знаю,что на меня нашло..."
                hide screen h_head2
                g9 "Мой член!"
                show screen h_head2                                                             # HERMIONE
                $ h_body = "03_hp/13_hermione_main/body_153.png" # HERMIONE
                her2 "Думаю,это произошло тогда,когда вы меня назвали \"шлюхой\". Я знаю,вы не это имелли ввиду..."
                hide screen h_head2    
                m "Да, конечно..."
                m "Всё ещё болит?"
                show screen h_head2                                                             # HERMIONE
                $ h_body = "03_hp/13_hermione_main/body_154.png" # HERMIONE  
                her "Немного..."
                show screen h_head2                                                             # HERMIONE
                $ h_body = "03_hp/13_hermione_main/body_155.png" # HERMIONE
                her "До сих пор чувствую внутири горячую сперму..."
                hide screen h_head2      
                m "Ты собираешься так её оставить? Ну я имею в виду сперму."
                show screen h_head2                                                             # HERMIONE
                $ h_body = "03_hp/13_hermione_main/body_156.png" # HERMIONE     
                her "Да..."
                if daytime:
                    her2 "Надеюсь она не будет хлюпать, пока я сижу на занятии..."
                else:
                    her2 "Надеюсь она не будет хлюпать, пока я иду в свою комнату..."
                hide screen h_head2 
                m "Ну удачно добраться тогда."
                show screen h_head2                                                             # HERMIONE
                $ h_body = "03_hp/13_hermione_main/body_155.png" # HERMIONE  
                her "Мы можем расчитаться?"
                hide screen h_head2 
                
                    
                
                
                
                
            "- Вытащить и кончить на Гермиону -":
                
                $ g_c_u_pic = "sex_cum_out_ani"
                show screen white 
                pause.1
                hide screen white
                pause.2
                show screen white 
                pause .1
                hide screen white
                with hpunch
                show screen ctc
                pause
                hide screen ctc
                $ uni_sperm = True
                $ u_sperm = "03_hp/13_hermione_main/auto_08.png"
                show screen h_head2                                                             # HERMIONE
                $ h_body = "03_hp/13_hermione_main/body_133.png" # HERMIONE
                her2 "Аа...{image=textheart.png}{image=textheart.png}{image=textheart.png}"

                hide screen h_head2     
                g4 "Да!!! Всё на твоей попке!"
                show screen h_head2                                                             # HERMIONE
                $ h_body = "03_hp/13_hermione_main/body_134.png" # HERMIONE
                her "Оуу... Она горячая!"
                hide screen h_head2          

                
                hide screen h_head2     
                hide screen bld1
                with d3
                show screen ctc
                pause
                hide screen ctc
                show screen bld1
                with d3


                
                
                show screen blkfade
                with d7
                
                m "Ну что ж, я закончил... Можешь проваливать с моего стола."
                show screen h_head2                                                             # HERMIONE
                $ h_body = "03_hp/13_hermione_main/body_138.png" # HERMIONE
                her "Да, Сэр..."
                hide screen h_head2     
                m "Ты как?"
                show screen h_head2                                                             # HERMIONE
                $ h_body = "03_hp/13_hermione_main/body_139.png" # HERMIONE
                her "Всё ещё больновато,Сэр.Но..."
                hide screen h_head2     
                m "Что НО...?"
                show screen h_head2                                                             # HERMIONE
                $ h_body = "03_hp/13_hermione_main/body_138.png" # HERMIONE
                her "Но мне даже нравится... Сэр."
                hide screen h_head2     
                m "Нравится??"
                g9 "Хах... А ты видимо маленькая мазохистка."
                show screen h_head2                                                             # HERMIONE
                $ h_body = "03_hp/13_hermione_main/body_138.png" # HERMIONE
                her "Мы можем расчитаться, Сэр?"
                hide screen h_head2 

        
    elif request_31_points == 1: # FIRST EVENT <============================================================== EVENT 02
        m "Девочка?"
        hide screen hermione_main                                                                                                                                                                                   #HERMIONE
        with d3                                                                                                                                                                                                                        #HERMIONE
        $ h_xpos=140 #Defines position of the Hermione's full length sprite. (Default 370). (Center: 140)                                                       #HERMIONE
        $ h_body = "03_hp/13_hermione_main/body_15.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
        show screen hermione_main                                                                                                                                                                                 #HERMIONE
        with d3                                                                                                                                                                                                                        #HERMIONE                     
        her "Профессор?"
        m "Я куплю сегодня у тебя другую услугу..."
        hide screen hermione_main                                                                                                                                                                                   #HERMIONE
        with d3                                                                                                                                                                                                                        #HERMIONE
        $ h_xpos=140 #Defines position of the Hermione's full length sprite. (Default 370). (Center: 140)                                                       #HERMIONE
        $ h_body = "03_hp/13_hermione_main/body_08.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
        show screen hermione_main                                                                                                                                                                                 #HERMIONE
        with d3                                                                                                                                                                                                                        #HERMIONE    
        her "............."
        m "Попытайся догадаться что это будет?"
        m "У тебя три попытки."
        hide screen hermione_main                                                                                                                                                                                   #HERMIONE
        with d3                                                                                                                                                                                                                        #HERMIONE
        $ h_xpos=140 #Defines position of the Hermione's full length sprite. (Default 370). (Center: 140)                                                       #HERMIONE
        $ h_body = "03_hp/13_hermione_main/body_09.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
        show screen hermione_main                                                                                                                                                                                 #HERMIONE
        with d3                                                                                                                                                                                                                        #HERMIONE    
        her "..........."
        hide screen hermione_main                                                                                                                                                                                   #HERMIONE
        with d3                                                                                                                                                                                                                        #HERMIONE
        $ h_xpos=140 #Defines position of the Hermione's full length sprite. (Default 370). (Center: 140)                                                       #HERMIONE
        $ h_body = "03_hp/13_hermione_main/body_66.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
        show screen hermione_main                                                                                                                                                                                 #HERMIONE
        with d3                                                                                                                                                                                                                        #HERMIONE    
        her "Анальный секс?"
        g4 "Что..........?!"
        g4 "Как ты...?"
        hide screen hermione_main                                                                                                                                                                                   #HERMIONE
        with d3                                                                                                                                                                                                                        #HERMIONE
        $ h_xpos=140 #Defines position of the Hermione's full length sprite. (Default 370). (Center: 140)                                                       #HERMIONE
        $ h_body = "03_hp/13_hermione_main/body_47.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
        show screen hermione_main                                                                                                                                                                                 #HERMIONE
        with d3                                                                                                                                                                                                                        #HERMIONE    
        her "Просто повезло, Сэр..."
        m "Иногда ты меня пугаешь,девочка..."
        hide screen hermione_main                                                                                                                                                                                   #HERMIONE
        with d3 
        jump lucky_guess
        
        
        
        
        
    elif request_31_points >= 2: # FIRST EVENT <============================================================== EVENT 03
        m "Как на счет повторить анальный секс, малышка?"
        hide screen hermione_main                                                                                                                                                                                   #HERMIONE
        with d3                                                                                                                                                                                                                        #HERMIONE
        $ h_xpos=140 #Defines position of the Hermione's full length sprite. (Default 370). (Center: 140)                                                       #HERMIONE
        $ h_body = "03_hp/13_hermione_main/body_17.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
        show screen hermione_main                                                                                                                                                                                 #HERMIONE
        with d3                                                                                                                                                                                                                        #HERMIONE     
        her "Как на счет ещё 90 баллов, Сэр?"
        g9 "Иди сюда, маленькая мазохистка!"
        hide screen hermione_main     
        with d3
        # SEX
        show screen blkfade
        with d3
        
        stop music fadeout 1.0
        
        $ her_head_xpos=390 #Defines position of the Hermione's full length sprite. (Default 370). 140 - center. Bottom right: 390
        $ her_head_ypos=340 #Defines position of the Hermione's full length sprite. (Default 0). Right bottom corner: 340 - head only. 235 - tits.
        show screen h_head2                                                             # HERMIONE
        $ h_body = "03_hp/13_hermione_main/body_29.png" # HERMIONE
        her "........"
        hide screen h_head2               
        m "Хм..."
        show screen h_head2                                                             # HERMIONE
        $ h_body = "03_hp/13_hermione_main/body_31.png" # HERMIONE
        her "..........."
        hide screen h_head2
        
        
        $ renpy.play('sounds/gltch.mp3')
        with hpunch
        with kissiris
        show screen h_head2                                                             # HERMIONE
        $ h_body = "03_hp/13_hermione_main/body_130.png" # HERMIONE
        her2 "Оооооооо....{image=textheart.png}"
        hide screen h_head2
        g4 "О, дааа!"
        show screen h_head2                                                             # HERMIONE
        $ h_body = "03_hp/13_hermione_main/body_121.png" # HERMIONE
        her "Ах..."
        hide screen h_head2
        m "Сегодня я легче вхожу в твою дырочку."
        show screen h_head2                                                             # HERMIONE
        $ h_body = "03_hp/13_hermione_main/body_128.png" # HERMIONE
        her "Ах... До сих пор больновато...."
        show screen h_head2                                                             # HERMIONE
        $ h_body = "03_hp/13_hermione_main/body_129.png" # HERMIONE
        her "И пожалуйста, называйте меня \"шлюхой\", сэр."
        hide screen h_head2
        g4 "Аррр! Ты потаскуха! Мне всегда нравится, когда ты так говоришь!"



        
        
        
        
        hide screen hermione_main                                                                                                                                                                                   #HERMIONE
        hide screen genie
        $ genie_chibi_xpos = -210 #-185 behind the desk. (Also 5 is something).
        $ genie_chibi_ypos = 10
        $ g_c_u_pic = "sex_ani"
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
        
        
        
        
        
        
        play music "music/(Orchestral) Playful Tension by Shadow16nh.mp3" fadein 1 fadeout 1 # SEX THEME.
        
        # INSERTION
        show screen h_head2                                                             # HERMIONE
        $ h_body = "03_hp/13_hermione_main/body_127.png" # HERMIONE
        her "Ах... Ах..."
        her "Ах..."
        show screen h_head2                                                             # HERMIONE
        $ h_body = "03_hp/13_hermione_main/body_128.png" # HERMIONE
        her "Сэр?"
        hide screen h_head2
        m "Да, шлюшка?"
        show screen h_head2                                                             # HERMIONE
        $ h_body = "03_hp/13_hermione_main/body_117.png" # HERMIONE
        her "Эм..."
        hide screen h_head2
        hide screen ctc
        show screen h_head2                                                             # HERMIONE
        $ h_body = "03_hp/13_hermione_main/body_118.png" # HERMIONE
        her "Вы возьмете меня в жены, Сэр?"
        hide screen h_head2
        with hpunch
        g4 "{size=+9} ЧТО?!{/size}"
        g4 "Только не говори мне что ты беременна!"
        show screen h_head2                                                             # HERMIONE
        $ h_body = "03_hp/13_hermione_main/body_122.png" # HERMIONE
        her "Я не могу забеременеть от того, что вы меня трахаете в попку..."
        hide screen h_head2
        m "Тогда какие разговоры о свадьбе?"
        show screen h_head2                                                             # HERMIONE
        $ h_body = "03_hp/13_hermione_main/body_117.png" # HERMIONE
        her "Вы не поняли меня,Сэр."
        show screen h_head2                                                             # HERMIONE
        $ h_body = "03_hp/13_hermione_main/body_118.png" # HERMIONE
        her "Я хочу узнать, могли бы вы взять в жены {size=+5}такую девушку{/size} как Я?"
        show screen h_head2                                                             # HERMIONE
        $ h_body = "03_hp/13_hermione_main/body_34.png" # HERMIONE
        her2 "Я никогда не предалагала ни одному мужчине трахнуть меня в попку, сэр..."
        hide screen h_head2
        m "Хорошо. Потому что я думаю, что нормальный мужчина ответит тебе  \"нет\" в такой момент."
        show screen h_head2                                                             # HERMIONE
        $ h_body = "03_hp/13_hermione_main/body_127.png" # HERMIONE
        her "Ах{image=textheart.png}..."
        show screen h_head2                                                             # HERMIONE
        $ h_body = "03_hp/13_hermione_main/body_118.png" # HERMIONE
        her2 "Я имела ввиду... ах{image=textheart.png} {w} ...хотела сказать{image=textheart.png}... {w}...как вы думаете, кто нибудь женится{image=textheart.png}... {w} ...на такой девушке как я?"
        hide screen h_head2
        m "Хм?"
        show screen h_head2                                                             # HERMIONE
        $ h_body = "03_hp/13_hermione_main/body_118.png" # HERMIONE
        her "Я имею ввиду после всего того, что произошло со мной... ах{image=textheart.png}..."
        her "Я чувствую себя грязной... ущербной."
        her "И не могу смыть с себя всё это..."
        show screen h_head2                                                             # HERMIONE
        $ h_body = "03_hp/13_hermione_main/body_117.png" # HERMIONE
        her "Кто же захочет такую жену?"
        hide screen h_head2  
        menu:
            m "..."
            "\"Я бы женился на тебе по велению сердца!\"":
                show screen h_head2                                                             # HERMIONE
                $ h_body = "03_hp/13_hermione_main/body_31.png" # HERMIONE
                her "ЧТО?"
                hide screen h_head2  
                m "НУ, гипотетически конечно..."
                show screen h_head2                                                             # HERMIONE
                $ h_body = "03_hp/13_hermione_main/body_54.png" # HERMIONE
                her "...конечно...{image=textheart.png}"
                show screen h_head2                                                             # HERMIONE
                $ h_body = "03_hp/13_hermione_main/body_53.png" # HERMIONE
                her ".............."
                show screen h_head2                                                             # HERMIONE
                $ h_body = "03_hp/13_hermione_main/body_55.png" # HERMIONE
                her "Но почему вы так сказали, сэр?"
                hide screen h_head2  
                m "Ммм?"
                m "Что ты имеешь ввиду по словом \"почему\", сучка?"
                m "Ты молода и привлекательна..."
                m "Узкая задница, хорошие сиськи и мокрая киска..."
                show screen h_head2                                                             # HERMIONE
                $ h_body = "03_hp/13_hermione_main/body_127.png" # HERMIONE
                her "Ах...{image=textheart.png}"
                hide screen h_head2  
                m "Однажды, ты осчастливышь кого-нибудь везунчика, шлюха."
                m "Эм, всмысле, мисс Грейнджер."
                show screen h_head2                                                             # HERMIONE
                $ h_body = "03_hp/13_hermione_main/body_134.png" # HERMIONE
                her "Нет, \"шлюха\" лучше звучит. Называйте меня так, Сэр."
                hide screen h_head2  
                m "Вот,видишь? Ты схватываешь всё на лету, шлюха."
                show screen h_head2                                                             # HERMIONE
                $ h_body = "03_hp/13_hermione_main/body_142.png" # HERMIONE
                her "Ах...{image=textheart.png} Спасибо, Сэр."
                hide screen h_head2  
                m "А?"
                m "Ты плачешь?"
                label among_other_things:
                show screen h_head2                                                             # HERMIONE
                $ h_body = "03_hp/13_hermione_main/body_133.png" # HERMIONE
                her "Между прочим, Сэр...{image=textheart.png}{image=textheart.png}{image=textheart.png}"
                hide screen h_head2  
                m "Между прочим?"
                show screen h_head2                                                             # HERMIONE
                $ h_body = "03_hp/13_hermione_main/body_135.png" # HERMIONE
                her "Я кончаю, Сэр...{image=textheart.png}{image=textheart.png}{image=textheart.png}"
                hide screen h_head2  
                g4 "Ааа! Мой член!" 
                g4 "Немного расслабься там!"
                show screen h_head2                                                             # HERMIONE
                $ h_body = "03_hp/13_hermione_main/body_131.png" # HERMIONE
                her "НО Я КОНЧАЮ!{image=textheart.png}{image=textheart.png}{image=textheart.png}"
                hide screen h_head2  
                g4 "Отлично, тогда кончай,шлюха!"
                with hpunch
                show screen h_head2                                                             # HERMIONE
                $ h_body = "03_hp/13_hermione_main/body_130.png" # HERMIONE
                her "{size=+7}Ааааа!!! Я кончаю!!!{/size}"
                hide screen h_head2  
                g4 "{size=+7}Аррр!{/size}"
                
            "\"Свадьба не для тебя.\"":
                show screen h_head2                                                             # HERMIONE
                $ h_body = "03_hp/13_hermione_main/body_143.png" # HERMIONE
                her "Вот о чем я и думала..."
                hide screen h_head2  
                m "Ооо... Мне просто нравится твоя маленькая и узкая задница!"
                show screen h_head2                                                             # HERMIONE
                $ h_body = "03_hp/13_hermione_main/body_142.png" # HERMIONE
                her "....................."
                her2 "Да... После всего того, что мне пришлось сделать для своего факультета..."
                show screen h_head2                                                             # HERMIONE
                $ h_body = "03_hp/13_hermione_main/body_145.png" # HERMIONE
                her "...никто не захочет меня..."
                hide screen h_head2  
                m "Ооо,они захотят тебя!"
                show screen h_head2                                                             # HERMIONE
                $ h_body = "03_hp/13_hermione_main/body_144.png" # HERMIONE
                her "Что? Но вы сказали..."
                hide screen h_head2  
                m "Свадьба, малышка. Свадьба не для тебя."
                m "Но как шлюха, удовлетворяющая мужчин, ты шикарна!"
                show screen h_head2                                                             # HERMIONE
                $ h_body = "03_hp/13_hermione_main/body_144.png" # HERMIONE
                her "Правда?"
                hide screen h_head2  
                m "Ты шутишь?!"
                m "Юная, горячая, ненасытная! Да ты можешь иметь всё что захочешь!"
                m "Магия и всё что можешь пожелать..."
                show screen h_head2                                                             # HERMIONE
                $ h_body = "03_hp/13_hermione_main/body_157.png" # HERMIONE
                her "Наверно вы правы,Сэр."
                hide screen h_head2  
                m "Я знаю,я прав, потаскуха."
                m "А сейчас поработай немного своей попкой."
                show screen h_head2                                                             # HERMIONE
                $ h_body = "03_hp/13_hermione_main/body_138.png" # HERMIONE
                her "Вот так?"
                hide screen h_head2  
                m  "Да, вот именно так,шлюха."
                show screen h_head2                                                             # HERMIONE
                $ h_body = "03_hp/13_hermione_main/body_133.png" # HERMIONE
                her "Я потаскуха, да?"
                hide screen h_head2  
                m "Ты только что продала мне свою задницу за 90 очков. Как ты себя после этого назовёшь?"
                show screen h_head2                                                             # HERMIONE
                $ h_body = "03_hp/13_hermione_main/body_138.png" # HERMIONE
                her "Да, даааа...{image=textheart.png} Я шлюха...{image=textheart.png}"
                hide screen h_head2  
                m "Ты плачешь?"
                jump among_other_things
                
        menu:
            g4 "!!!"
            "- Кончить в Гермиону -":
                show screen h_head2                                                             # HERMIONE
                $ h_body = "03_hp/13_hermione_main/body_130.png" # HERMIONE
                her "!!!"
                hide screen h_head2 
                m "Да! арррр!"
                show screen h_head2                                                             # HERMIONE
                $ h_body = "03_hp/13_hermione_main/body_134.png" # HERMIONE
                her "Ах!{image=textheart.png} Вы заполняете меня!{image=textheart.png} Я чувствую!{image=textheart.png}"
                hide screen h_head2 
                m "Заткнись, сучка!"
                show screen h_head2                                                             # HERMIONE
                $ h_body = "03_hp/13_hermione_main/body_137.png" # HERMIONE
                her "Ах! Я потаскуха!!!!{image=textheart.png}{image=textheart.png}{image=textheart.png}"
                hide screen h_head2 
                m "Арр!"
                show screen h_head2                                                             # HERMIONE
                $ h_body = "03_hp/13_hermione_main/body_144.png" # HERMIONE
                her "Ах...{image=textheart.png} вы кончаете, Сэр...{image=textheart.png}"
                hide screen h_head2 
                m "ДА, ООООДА..."
                show screen h_head2                                                             # HERMIONE
                $ h_body = "03_hp/13_hermione_main/body_145.png" # HERMIONE
                her "Ааа...{image=textheart.png}"
                hide screen h_head2          
                m "......"
                hide screen bld1
                with d3
                show screen ctc
                pause
                hide screen ctc
                show screen bld1
                with d3


                
                
                show screen blkfade
                with d7
            "- Обкончать Гермиону -":
                
                $ g_c_u_pic = "sex_cum_out_ani"
                show screen white 
                pause.1
                hide screen white
                pause.2
                show screen white 
                pause .1
                hide screen white
                with hpunch
                show screen ctc
                pause
                hide screen ctc
                $ uni_sperm = True
                $ u_sperm = "03_hp/13_hermione_main/auto_08.png"
                show screen h_head2                                                             # HERMIONE
                $ h_body = "03_hp/13_hermione_main/body_133.png" # HERMIONE
                her "Ааа! Вы кончаете! {image=textheart.png}{image=textheart.png}{image=textheart.png}"
                hide screen h_head2    
                g4 "{size=+7}Вот именно, шлюха!{/size}"
                show screen h_head2                                                             # HERMIONE
                $ h_body = "03_hp/13_hermione_main/body_147.png" # HERMIONE
                her "Ааа,я тоже! Я тоже!"
                hide screen h_head2    
                g4 "{size=+7}Долбанная потаскуха!{/size}"
                show screen h_head2                                                             # HERMIONE
                $ h_body = "03_hp/13_hermione_main/body_142.png" # HERMIONE
                her "Аааа...{image=textheart.png} ваша сперма...{image=textheart.png}"
                her "Так много...{image=textheart.png}{image=textheart.png}{image=textheart.png}"


                hide screen h_head2     
                g4 "ДА!!! Всё на твоей заднице!"
                show screen h_head2                                                             # HERMIONE
                $ h_body = "03_hp/13_hermione_main/body_134.png" # HERMIONE
                her "Ах... Такая горячая!"
                hide screen h_head2          

                
                hide screen h_head2     
                hide screen bld1
                with d3
                show screen ctc
                pause
                hide screen ctc
                show screen bld1
                with d3


                
                
                show screen blkfade
                with d7

                
                
                
                
                
                
                
                
                
                
                
               
              
        #Ending
        m "Ну это было здорово..."
        show screen h_head2                                                             # HERMIONE
        $ h_body = "03_hp/13_hermione_main/body_158.png" # HERMIONE
        her "Ах-ах...{image=textheart.png} a...{image=textheart.png}"
        hide screen h_head2   
        m "Как ты,малышка?"
        show screen h_head2                                                             # HERMIONE
        $ h_body = "03_hp/13_hermione_main/body_158.png" # HERMIONE
        her "Я думаю... Я не уверена..."
        show screen h_head2                                                             # HERMIONE
        $ h_body = "03_hp/13_hermione_main/body_158.png" # HERMIONE
        her "Я видимо ещё кончаю..., Сэр."
        show screen h_head2                                                             # HERMIONE
        $ h_body = "03_hp/13_hermione_main/body_158.png" # HERMIONE
        her "А может нет..."
        her "Всё как в тумане... и мои ноги...я еле хожу..."
        her "Мы можем рассчитаться, Сэр?"
        hide screen h_head2                                                             # HERMIONE

        
    
    stop music fadeout 1.0
    
    $ uni_sperm = False #Sperm layer is not displayed in hermione screen.
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
 
    m "Да, мисс Грейнджер 90 очков \"Гриффиндору\"." 
    $ gryffindor +=90
    $ h_xpos=140 #Defines position of the Hermione's full length sprite. (Default 370). (Center: 140)
    $ h_body = "03_hp/13_hermione_main/body_141.png" #Flashing panties
    show screen hermione_main
    hide screen hermione_01_f #Hermione stands still.
    with d3
    her "Спасибо, Сэр..."

    if whoring <= 23: # Level 08 <
        $ whoring +=1

    if request_31_points == 0:
        $ new_request_31_01 = True # HEARTS.
    if request_31_points == 1:
        $ new_request_31_02 = True # HEARTS.
    if request_31_points >= 2:
        $ new_request_31_03 = True # HEARTS.


    $ request_31_points += 1

    hide screen bld1
    hide screen hermione_main
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

    $ aftersperm = False #Show cum stains on Hermione's uniform.

    call music_block
    
    if daytime:
        $ hermione_takes_classes = True
        jump night_main_menu
    else:
        $ hermione_sleeping = True
        jump day_main_menu            
   

    





###################REQUEST_12 (Level 04) (Play with her tits.) (Day/Night) ############################################################################
label new_request_12: #LV.4 (Whoring = 9 - 11)
    hide screen hermione_main 
    with d3
    if request_12_points == 0:
        m "{size=-4}(Кажется пора поиграть с её сиськами.){/size}"
    else:
        m "{size=-4}(Пора ещё раз поразвлечься с её сиськами.){/size}"
    $ menu_x = 0.5 #Default position of the menu (0.5). Version B is $ menu_x = 0.2
    menu:
        "\"(Да,давай попробую!)\"":
            show screen blktone
            with d3
            pass
        "\"(Нет, не сейчас.)\"":
            jump new_personal_request
    
    if whoring <=8:
        jump too_much
        
    if request_12_points == 0 and whoring <= 14: # LEVEL 05 (one level higher then level at which it unlocks - 04) # FIRST TIME.
        m "Мисс Грейнджер."
        hide screen hermione_main                                                                                                                                                                                   #HERMIONE
        with d3                                                                                                                                                                                                                        #HERMIONE
        $ h_xpos=140 #Defines position of the Hermione's full length sprite. (Default 370). (Center: 140)                                                        #HERMIONE
        $ h_body = "03_hp/13_hermione_main/body_01.png" #Sprite of Hermione's upper body.                                                                    #HERMIONE
        show screen hermione_main                                                                                                                                                                                 #HERMIONE
        with d3                                                                                                                                                                                                                        #HERMIONE
        her "Да, Сэр?"
        m "Как насчет еще одной услуги?"
        hide screen hermione_main                                                                                                                                                                                   #HERMIONE
        with d3                                                                                                                                                                                                                        #HERMIONE
        $ h_xpos=140 #Defines position of the Hermione's full length sprite. (Default 370). (Center: 140)                                                        #HERMIONE
        $ h_body = "03_hp/13_hermione_main/body_02.png" #Sprite of Hermione's upper body.                                                                    #HERMIONE
        show screen hermione_main                                                                                                                                                                                 #HERMIONE
        with d3                                                                                                                                                                                                                        #HERMIONE
        her "Эм... Ладно..."
        her "Какой, Сэр?"
        m "Ну, как на счет того, что бы ты подошла ко мне ближе и дала бы мне полапать твою грудь...?"
        hide screen hermione_main                                                                                                                                                                                   #HERMIONE
        with d3                                                                                                                                                                                                                        #HERMIONE
        $ h_xpos=140 #Defines position of the Hermione's full length sprite. (Default 370). (Center: 140)                                                        #HERMIONE
        $ h_body = "03_hp/13_hermione_main/body_31.png" #Sprite of Hermione's upper body.                                                                    #HERMIONE
        show screen hermione_main                                                                                                                                                                                 #HERMIONE
        with d3                                                                                                                                                                                                                        #HERMIONE
        her "!!!"
        m "Я бы хотел её потрогать."
        hide screen hermione_main                                                                                                                                                                                   #HERMIONE
        with d3                                                                                                                                                                                                                        #HERMIONE
        $ h_xpos=140 #Defines position of the Hermione's full length sprite. (Default 370). (Center: 140)                                                        #HERMIONE
        $ h_body = "03_hp/13_hermione_main/body_66.png" #Sprite of Hermione's upper body.                                                                    #HERMIONE
        show screen hermione_main                                                                                                                                                                                 #HERMIONE
        with d3                                                                                                                                                                                                                        #HERMIONE
        her "Профессор Дамбалдор! Вам не кажется, что это перебор?"
        m "Ты думаешь?"
        her "Я не такая распутная, как эти девченки из \"Слизерина\", ну вы знаете..."
        m "Я знаю... Ты из \"Гриффиндор\"... или как там..." #<- GRYFFINDOR MISSPELLED ON PERPOUSE   I KNOW
        hide screen hermione_main                                                                                                                                                                                   #HERMIONE
        with d3                                                                                                                                                                                                                        #HERMIONE
        $ h_xpos=140 #Defines position of the Hermione's full length sprite. (Default 370). (Center: 140)                                                        #HERMIONE
        $ h_body = "03_hp/13_hermione_main/body_29.png" #Sprite of Hermione's upper body.                                                                    #HERMIONE
        show screen hermione_main                                                                                                                                                                                 #HERMIONE
        with d3                                                                                                                                                                                                                        #HERMIONE
        her "И раз я не такая, то я не буду продавать ещё одну услугу, Сэр!"
        m "Конечно..."
        hide screen hermione_main                                                                                                                                                                                   #HERMIONE
        with d3                                                                                                                                                                                                                        #HERMIONE
        $ h_xpos=140 #Defines position of the Hermione's full length sprite. (Default 370). (Center: 140)                                                        #HERMIONE
        $ h_body = "03_hp/13_hermione_main/body_69.png" #Sprite of Hermione's upper body.                                                                    #HERMIONE
        show screen hermione_main                                                                                                                                                                                 #HERMIONE
        with d3                                                                                                                                                                                                                        #HERMIONE
        her "..................."
        m "Я дам тебе за это 35 очков."
        hide screen hermione_main                                                                                                                                                                                   #HERMIONE
        with d3                                                                                                                                                                                                                        #HERMIONE
        $ h_xpos=140 #Defines position of the Hermione's full length sprite. (Default 370). (Center: 140)                                                        #HERMIONE
        $ h_body = "03_hp/13_hermione_main/body_66.png" #Sprite of Hermione's upper body.                                                                    #HERMIONE
        show screen hermione_main                                                                                                                                                                                 #HERMIONE
        with d3                                                                                                                                                                                                                        #HERMIONE
        her "......................."
        her "Вы ведь будете только смотреть, Сэр?"
        m "Вообще-то,я бы хотел потрогать и помять..."
        her "...................................."


    else: # Intro. Not first time.
        if whoring >= 9 and whoring <= 14: # LEVEL 04 AND LEVEL 05 # NOT A WHORE YET.
            m "Мисс Грейнджер..."
            hide screen hermione_main                                                                                                                                                                                   #HERMIONE
            with d3                                                                                                                                                                                                                        #HERMIONE
            $ h_xpos=140 #Defines position of the Hermione's full length sprite. (Default 370). (Center: 140)                                                        #HERMIONE
            $ h_body = "03_hp/13_hermione_main/body_01.png" #Sprite of Hermione's upper body.                                                                    #HERMIONE
            show screen hermione_main                                                                                                                                                                                 #HERMIONE
            with d3                                                                                                                                                                                                                        #HERMIONE
            her "Сэр?"
            m "Я бы хотел поиграть немного с вашей грудью..."
            hide screen hermione_main                                                                                                                                                                                   #HERMIONE
            with d3                                                                                                                                                                                                                        #HERMIONE
            $ h_xpos=140 #Defines position of the Hermione's full length sprite. (Default 370). (Center: 140)                                                        #HERMIONE
            $ h_body = "03_hp/13_hermione_main/body_79.png" #Sprite of Hermione's upper body.                                                                    #HERMIONE
            show screen hermione_main                                                                                                                                                                                 #HERMIONE
            with d3                                                                                                                                                                                                                        #HERMIONE
            her "Сэр... Лучше бы вы не делали мне таких предложения..."
            m "А что? Тяжело отказаться?"
            her "Ничего подобного,Сэр."
            m "Я дам тебе 35 очков за это..."
            hide screen hermione_main                                                                                                                                                                                   #HERMIONE
            with d3                                                                                                                                                                                                                        #HERMIONE
            $ h_xpos=140 #Defines position of the Hermione's full length sprite. (Default 370). (Center: 140)                                                        #HERMIONE
            $ h_body = "03_hp/13_hermione_main/body_69.png" #Sprite of Hermione's upper body.                                                                    #HERMIONE
            show screen hermione_main                                                                                                                                                                                 #HERMIONE
            with d3                                                                                                                                                                                                                        #HERMIONE
            her ".................."
            her "Ладно... Вы можете потрогать их немного..."
        elif whoring >= 15: # LEVEL 06 and higher # NASTY WHORE.
            m "Мисс Грейнджер..."
            
            hide screen hermione_main                                                                                                                                                                                   #HERMIONE
            with d3                                                                                                                                                                                                                        #HERMIONE
            $ h_xpos=140 #Defines position of the Hermione's full length sprite. (Default 370). (Center: 140)                                                        #HERMIONE
            $ h_body = "03_hp/13_hermione_main/body_01.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
            show screen hermione_main                                                                                                                                                                                 #HERMIONE
            with d3                                                                                                                                                                                                                        #HERMIONE              
            her "Сэр?"
            m "Я могу моиграть с вашей грудью немного..."
            hide screen hermione_main                                                                                                                                                                                   #HERMIONE
            with d3                                                                                                                                                                                                                        #HERMIONE
            $ h_xpos=140 #Defines position of the Hermione's full length sprite. (Default 370). (Center: 140)                                                        #HERMIONE
            $ h_body = "03_hp/13_hermione_main/body_78.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
            show screen hermione_main                                                                                                                                                                                 #HERMIONE
            with d3                                                                                                                                                                                                                        #HERMIONE
            her "Конечно, Сэр..."
    
    hide screen hermione_main
    with d3
    hide screen blktone
    with d3
    hide screen bld1
    with d3
    $ walk_xpos=400 #Animation of walking chibi. (From)
    $ walk_xpos2=280 #Coordinates of it's movement. (To)
    $ hermione_speed = 03.0 #The speed of moving the walking animation across the screen.
    show screen hermione_walk_01 
    pause 1
    show screen blkfade
    with Dissolve(1)
    pause.5


    hide screen hermione_walk_01
    hide screen genie
    show screen ctc
    #show screen chair_02 #Genie's chair.
    hide screen genie
    show screen genie_and_tits_01
    with d1
    hide screen blkfade
    with d5
    stop music fadeout 1.0
    pause
    play music "music/(Orchestral) Playful Tension by Shadow16nh.mp3" fadein 1 fadeout 1 # SEX THEME.
    show screen blktone 
    with d3
    hide screen hermione_main
    with d3
    $ h_body = "03_hp/13_hermione_main/body_82.png" #Sprite of Hermione's upper body.
    $ h_xpos=140 #Defines position of the Hermione's full length sprite. (Default 370). (Center: 140)
    #$ only_upper = True #No lower body displayed. 
    $ badges = False
    show screen hermione_main
    with d3
    pause
    her "...................................."
    
    
    
    
    
    menu:
        m "..."
        "- Схватить грудь -":
            label no_smacking_tits:
                pass
            hide screen hermione_main
            with d3
            show screen blkfade
            with d5
            hide screen hermione_04 #Stands with tits out.
            hide screen genie
            show screen groping_naked_tits
            with d1
            hide screen blkfade
            hide screen blktone
            with d5
            pause
            show screen bld1
            with d3
            

            
            if whoring >= 9 and whoring <= 14: # LEVEL 04 AND LEVEL 05 # <=================================================================================== FIRST EVENT. (HERMIONE IS UNWILLING).

                $ her_head_xpos=390 #Defines position of the Hermione's full length sprite. (Default 370). 140 - center. Bottom right: 390
                $ her_head_ypos=340 #Defines position of the Hermione's full length sprite. (Default 0). Right bottom corner: 340 - head only. 235 - tits.
                show screen h_head2                                                             # HERMIONE
                $ h_body = "03_hp/13_hermione_main/body_118.png" # HERMIONE
                her ".............................."
                hide screen h_head2    
                m "У вас прекрасная грудь, мисс Грейнджер..."
                show screen h_head2                                                             # HERMIONE
                $ h_body = "03_hp/13_hermione_main/body_118.png" # HERMIONE
                her "...................................."
                hide screen h_head2 
                m "Вам нравится когда я сжимаю их так?"
                show screen h_head2                                                             # HERMIONE
                $ h_body = "03_hp/13_hermione_main/body_120.png" # HERMIONE
                her2 "Извините сэр,но вы меня путаете с пошлыми развратными девченками,я не такая..."
                her2 "Я позволила вам трогать мою грудь, лишь потому что вы заплатите мне за это..."
                her "Не потому что мне нравится это..."
                hide screen h_head2 
                m "Ясно..."
                m "Тогда ты больше похожа на проститутку..."
                show screen h_head2                                                             # HERMIONE
                $ h_body = "03_hp/13_hermione_main/body_119.png" # HERMIONE
                her "Профессор Дамблдор!"
                her "Проституткам платят за секс..."
                show screen h_head2                                                             # HERMIONE
                $ h_body = "03_hp/13_hermione_main/body_120.png" # HERMIONE
                her "Я никогда не опущусь до такого!"
                hide screen h_head2 
                show screen blktone
                with d3
                ">Вы сжали одну грудь девочки и начали жадно сосать её."
                hide screen blktone
                with d3
                show screen h_head2                                                             # HERMIONE
                $ h_body = "03_hp/13_hermione_main/body_131.png" # HERMIONE
                her "Ааах..."
                hide screen h_head2 
                m "Наслаждаетесь,мисс Грейнджер?"
                if whoring >= 9 and whoring <= 11: # LEVEL 04 #  <=================================================================================== FIRST EVENT.
                    show screen h_head2                                                                 # HERMIONE
                    $ h_body = "03_hp/13_hermione_main/body_120.png"   # HERMIONE
                    her "Сэр, Я всего лишь делаю это--"
                    hide screen h_head2 
                    show screen blktone
                    with d3
                    ">Вы начали сильнее сжимать грудь..."
                    hide screen blktone
                    with d3
                    show screen h_head2                                                                 # HERMIONE
                    $ h_body = "03_hp/13_hermione_main/body_132.png"   # HERMIONE
                    her "Ах..."
                    hide screen h_head2 
                    m "Скажи мне,что тебе нравится,девченка!"
                    show screen h_head2                                                                 # HERMIONE
                    $ h_body = "03_hp/13_hermione_main/body_131.png"   # HERMIONE
                    her "Сэр,я дала вам делать так,только потому--"
                    hide screen h_head2 
                    m "Знаю, знаю...."
                    m "Ты начинаешь говорить как сломанный магнитофон."
                    show screen h_head2                                                                 # HERMIONE
                    $ h_body = "03_hp/13_hermione_main/body_79.png"   # HERMIONE
                    her "...."
                    hide screen h_head2 
                    show screen blktone
                    with d3
                    show screen blkfade
                    with d7

                    show screen genie
                    hide screen groping_naked_tits
                    hide screen ctc
                    $ only_upper = False #Bottom is displayed.

            
                    ">Вы отпускаете грудь девочки..."
                else:  # LEVEL 05 # <=================================================================================== SECOND EVENT.
                    show screen h_head2                                                                 # HERMIONE
                    $ h_body = "03_hp/13_hermione_main/body_87.png"   # HERMIONE
                    her "Ах..."
                    hide screen h_head2
                    show screen blktone
                    with d3
                    ">Вы ещё пару раз сжимаете её грудь,а потом снова жадно посасываете её..."
                    hide screen blktone
                    with d3
                    show screen h_head2                                                                 # HERMIONE
                    $ h_body = "03_hp/13_hermione_main/body_31.png"   # HERMIONE
                    her "Ах... Сэр..."
                    hide screen h_head2
                    m "Что? Тебе нравится это,правда?"
                    show screen h_head2                                                                 # HERMIONE
                    $ h_body = "03_hp/13_hermione_main/body_31.png"   # HERMIONE
                    her "Нет... Я..."
                    hide screen h_head2
                    m "Не ври своему директору, девченка!"
                    show screen blktone
                    with d3
                    ">Вы снова сжимаете её грудь..."
                    hide screen blktone 
                    with d3
                    show screen h_head2                                                                 # HERMIONE
                    $ h_body = "03_hp/13_hermione_main/body_87.png"   # HERMIONE
                    her "Ах..."
                    her "Я не вру, Сэр..."
                    show screen h_head2                                                                 # HERMIONE
                    $ h_body = "03_hp/13_hermione_main/body_31.png"   # HERMIONE
                    her "С чего бы мне наслаждаться этим?"
                    hide screen h_head2
                    m "Я не знаю,это ты мне расскажи."
                    show screen blktone
                    with d3
                    ">Вы продолжаете играть с её грудью..."
                    hide screen blktone
                    with d3
                    show screen h_head2                                                                 # HERMIONE
                    $ h_body = "03_hp/13_hermione_main/body_31.png"   # HERMIONE
                    her "Ах... Я..."
                    hide screen h_head2
                    m "Да,что такое?"
                    show screen h_head2                                                                 # HERMIONE
                    $ h_body = "03_hp/13_hermione_main/body_117.png"   # HERMIONE
                    her "Нич... ничего,Сэр..."
                    hide screen h_head2
                    m "А я думаю как раз кое что...."
                    m "Я думаю, тебе нравится когда я сжимаю и играю с твоими сиськами."      
                    show screen h_head2                                                                 # HERMIONE
                    $ h_body = "03_hp/13_hermione_main/body_118.png"   # HERMIONE
                    her "Сэр, пожалуйста..."
                    if daytime:
                        her "Скоро начнутся уроки..."
                    else: 
                        her "Уже поздно..."
                    show screen h_head2                                                                 # HERMIONE
                    $ h_body = "03_hp/13_hermione_main/body_117.png"   # HERMIONE
                    her "Я могу идти,Сэр? Пожалуйста?"
                    hide screen h_head2
                    show screen blkfade 
                    with d3
                    m "Конечно, ступай..."
                    show screen h_head2                                                                 # HERMIONE
                    $ h_body = "03_hp/13_hermione_main/body_118.png"   # HERMIONE
                    her "..............."
                    show screen h_head2                                                                 # HERMIONE
                    $ h_body = "03_hp/13_hermione_main/body_117.png"   # HERMIONE
                    her "Сэр,вы продолжаете... Держать меня..."
                    hide screen h_head2
                    m "О,правда... моя вина...."
                    ">Вы отпускаете грудь Гермионы..."
                    
                    show screen genie
                    hide screen groping_naked_tits
                    hide screen ctc
                    $ only_upper = False #Bottom is displayed.

            elif whoring >= 15: # LEVEL 06 and higher # <=================================================================================== THIRD EVENT. 
               
                $ her_head_xpos=390 #Defines position of the Hermione's full length sprite. (Default 370). 140 - center. Bottom right: 390
                $ her_head_ypos=340 #Defines position of the Hermione's full length sprite. (Default 0). Right bottom corner: 340 - head only. 235 - tits.
                show screen h_head2                                                                 # HERMIONE
                $ h_body = "03_hp/13_hermione_main/body_121.png"   # HERMIONE
                her "Ах..."
                hide screen h_head2
                m "Ты сегодня более чувствительная,да?"
                show screen h_head2                                                                 # HERMIONE
                $ h_body = "03_hp/13_hermione_main/body_128.png"   # HERMIONE
                her "Наверное..."
                show screen h_head2                                                                 # HERMIONE
                $ h_body = "03_hp/13_hermione_main/body_131.png"   # HERMIONE
                her "Ах..."
                hide screen h_head2
                m "Тебе нравится,когда я играю с твоими сиськами?"
                show screen h_head2                                                                 # HERMIONE
                $ h_body = "03_hp/13_hermione_main/body_128.png"   # HERMIONE
                her "Да,Сэр... Ах..."
                hide screen h_head2
                m "Хех..."
                m "Что если я ущипну твой сосок?"
                show screen blktone
                with d5
                show screen h_head2                                                                 # HERMIONE
                $ h_body = "03_hp/13_hermione_main/body_117.png"   # HERMIONE
                her "!!!"
                show screen h_head2                                                                 # HERMIONE
                $ h_body = "03_hp/13_hermione_main/body_131.png"   # HERMIONE
                her "Ах! Сэр..."
                hide screen h_head2
                m "Или сделаю вот так?"
                show screen blktone8
                with d3
                ">Вы схватили грудь девочки сильнее и начали массировать стоячие соски..."
                hide screen blktone8
                with d3
                show screen h_head2                                                                 # HERMIONE
                $ h_body = "03_hp/13_hermione_main/body_132.png"   # HERMIONE
                her "Ах... ааа... аааааа... Сэр..."
                hide screen h_head2
                m "А если я поиграю с ними жестче?"
                show screen h_head2                                                                 # HERMIONE
                $ h_body = "03_hp/13_hermione_main/body_130.png"   # HERMIONE
                her "Ааа... Сэр, пожалуйста..."
                hide screen h_head2
                show screen blktone8
                with d3
                ">Гермиона схватилась за стол, что бы не сделать случайный шаг к вам..."
                hide screen blktone8
                with d3
                m "Умница..."
                show screen h_head2                                                                 # HERMIONE
                $ h_body = "03_hp/13_hermione_main/body_123.png"   # HERMIONE
                her "*Тяжело вздыхает*"
                hide screen h_head2
                m "Тебе нравится это?"
                show screen h_head2                                                                 # HERMIONE
                $ h_body = "03_hp/13_hermione_main/body_139.png"   # HERMIONE
                her "Вы делаете мне больно,Сэр..."
                hide screen h_head2
                m "Но тебе это нравится?"
                show screen h_head2                                                                 # HERMIONE
                $ h_body = "03_hp/13_hermione_main/body_140.png"   # HERMIONE
                her "Ах... Да, Сэр... Не знаю почему, но мне нравится..."
                hide screen h_head2
                m "Хорошая девочка..."
                show screen blktone8
                with d3
                ">Вы отпустили её сосочки..."
                hide screen blktone8
                with d3
                show screen h_head2                                                                 # HERMIONE
                $ h_body = "03_hp/13_hermione_main/body_138.png"   # HERMIONE
                her "Ах..."
                hide screen h_head2
                show screen blkfade
                with d5
                m "На сегодня всё, мисс Грейнджер..."
                show screen h_head2                                                                 # HERMIONE
                $ h_body = "03_hp/13_hermione_main/body_139.png"   # HERMIONE
                her "Ооо...?"
                hide screen h_head2
                m "Что такое? У вас разочарованный вид."
                m "Я заплачу вам, конечно же..."
                show screen h_head2                                                                 # HERMIONE
                $ h_body = "03_hp/13_hermione_main/body_141.png"   # HERMIONE
                her "Не в этом дело..."
                her "А..."
                show screen h_head2                                                                 # HERMIONE
                $ h_body = "03_hp/13_hermione_main/body_139.png"   # HERMIONE
                if daytime:
                    her2 "У меня всё ещё есть время перед уроками и..."
                else:
                    her "Сейчас ещё ведь не поздно?"
                her "ммм..."
                her "..................."
                hide screen h_head2
                m "Вы хотите,что бы я продолжил,да?"
                show screen h_head2                                                                 # HERMIONE
                $ h_body = "03_hp/13_hermione_main/body_139.png"   # HERMIONE
                her "Я...не то что бы \"хочу\"... "
                show screen h_head2                                                                 # HERMIONE
                $ h_body = "03_hp/13_hermione_main/body_138.png"   # HERMIONE
                her "Но если вы настаиваете...."
                hide screen h_head2
                m "Конечно,я настаиваю... видимо."
                show screen h_head2                                                                 # HERMIONE
                $ h_body = "03_hp/13_hermione_main/body_138.png"   # HERMIONE
                her "Ах..."
                hide screen h_head2
                hide screen blkfade
                with d5
                
                show screen ctc
                pause
                hide screen ctc
                
                #BLACK FADE
                show screen blkfade
                with d7
                ">Еще немного вы играетесь с грудью Гермионы..."
                
                show screen genie
                hide screen groping_naked_tits
                hide screen ctc
                $ only_upper = False #Bottom is displayed.

        "- Шлепнуть по ней -":
            hide screen hermione_main
            with d5
            ">Вы громко и мощно шлепнули грудь Гермионы!"
            $ renpy.play('sounds/slap.mp3') #SLAP!
            show screen white
            with hpunch
            pause.08
            hide screen white
            show screen bld1
            if whoring >= 9 and whoring <= 11: # LEVEL 04 # <=================================================================================== FIRST EVENT. (HERMIONE IS UNWILLING).
                hide screen hermione_main                                                                                                                                                                                   #HERMIONE
                with d3                                                                                                                                                                                                                        #HERMIONE
                $ h_xpos=140 #Defines position of the Hermione's full length sprite. (Default 370). (Center: 140)                                                        #HERMIONE
                $ h_body = "03_hp/13_hermione_main/182.png" #Sprite of Hermione's upper body.                                                                           #HERMIONE
                show screen hermione_main                                                                                                                                                                                 #HERMIONE
                her "!!!"
                hide screen hermione_main                                                                                                                                                                                   #HERMIONE
                with d3                                                                                                                                                                                                                        #HERMIONE
                $ h_xpos=140 #Defines position of the Hermione's full length sprite. (Default 370). (Center: 140)                                                        #HERMIONE
                $ h_body = "03_hp/13_hermione_main/183.png" #Sprite of Hermione's upper body.                                                                           #HERMIONE
                show screen hermione_main                                                                                                                                                                                 #HERMIONE
                her "Ау! Это больно! *Хнык!*"
                m "Но тебе всё равно нравится это?"
                hide screen hermione_main                                                                                                                                                                                   #HERMIONE
                with d3                                                                                                                                                                                                                        #HERMIONE
                $ h_xpos=140 #Defines position of the Hermione's full length sprite. (Default 370). (Center: 140)                                                        #HERMIONE
                $ h_body = "03_hp/13_hermione_main/body_81.png" #Sprite of Hermione's upper body.                                                                    #HERMIONE
                show screen hermione_main                                                                                                                                                                                 #HERMIONE
                her "Мне правда... должно \"нравится\" это, сэр..?"
                her "Какой же девушке в здравом уме понравится это?"
                hide screen hermione_main                                                                                                                                                                                   #HERMIONE
                with d3                                                                                                                                                                                                                        #HERMIONE
                $ h_xpos=140 #Defines position of the Hermione's full length sprite. (Default 370). (Center: 140)                                                        #HERMIONE
                $ h_body = "03_hp/13_hermione_main/184.png" #Sprite of Hermione's upper body.                                                                           #HERMIONE
                show screen hermione_main                                                                                                                                                                                 #HERMIONE
                with d3
                stop music fadeout 1.0
                her "Вы чокнутый и сумасшедший старик!"
                hide screen hermione_main                                                                                                                                                                                 #HERMIONE
                with d3
                show screen blkfade
                with d3
                # RUNS OFF
                $ mad += 20
                m "............"
                m "Ну тогда никаких очков \"Гриффиндору\"..."
                
                show screen genie
                hide screen groping_naked_tits
                hide screen ctc
                $ only_upper = False #Bottom is displayed.
                hide screen genie_and_tits_01
                call music_block
                jump could_not_flirt #Sent here when choose "Favor failed! No points for you!" (Hermione is leaving without getting any points).
                
                    
            elif whoring >= 12 and whoring <= 14: # LEVEL 05 # <=================================================================================== SECOND EVENT.
                hide screen hermione_main                                                                                                                                                                                   #HERMIONE
                with d3                                                                                                                                                                                                                        #HERMIONE
                $ h_xpos=140 #Defines position of the Hermione's full length sprite. (Default 370). (Center: 140)                                                        #HERMIONE
                $ h_body = "03_hp/13_hermione_main/182.png" #Sprite of Hermione's upper body.                                                                           #HERMIONE
                show screen hermione_main                                                                                                                                                                                 #HERMIONE
                her "!!!"
                hide screen hermione_main                                                                                                                                                                                   #HERMIONE
                with d3                                                                                                                                                                                                                        #HERMIONE
                $ h_xpos=140 #Defines position of the Hermione's full length sprite. (Default 370). (Center: 140)                                                        #HERMIONE
                $ h_body = "03_hp/13_hermione_main/183.png" #Sprite of Hermione's upper body.                                                                           #HERMIONE
                show screen hermione_main                                                                                                                                                                                 #HERMIONE
                her "Ау!"
                her "Зачем вы так делаете,Сэр?"
                m "Хммм... мне показалось это хорошей идеей..."
                m "Тебе нравится?"
                hide screen hermione_main                                                                                                                                                                                   #HERMIONE
                with d3                                                                                                                                                                                                                        #HERMIONE
                $ h_xpos=140 #Defines position of the Hermione's full length sprite. (Default 370). (Center: 140)                                                        #HERMIONE
                $ h_body = "03_hp/13_hermione_main/body_83.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
                show screen hermione_main                                                                                                                                                                                 #HERMIONE
                her "...Конечно нет, Сэр."
                m "Давай попробуем ещё раз, тогда."
                hide screen hermione_main                                                                                                                                                                                   #HERMIONE
                with d3                                                                                                                                                                                                                        #HERMIONE
                $ h_xpos=140 #Defines position of the Hermione's full length sprite. (Default 370). (Center: 140)                                                        #HERMIONE
                $ h_body = "03_hp/13_hermione_main/body_82.png" #Sprite of Hermione's upper body.                                                                           #HERMIONE
                show screen hermione_main                                                                                                                                                                                 #HERMIONE
                her "Что?"
                hide screen hermione_main                                                                                                                                                                                   #HERMIONE
                with d3   
                $ renpy.play('sounds/slap.mp3') #SLAP!
                show screen white
                with hpunch
                pause.08
                hide screen white
                hide screen hermione_main                                                                                                                                                                                   #HERMIONE
                with d3                                                                                                                                                                                                                        #HERMIONE
                $ h_xpos=140 #Defines position of the Hermione's full length sprite. (Default 370). (Center: 140)                                                        #HERMIONE
                $ h_body = "03_hp/13_hermione_main/182.png" #Sprite of Hermione's upper body.                                                                           #HERMIONE
                show screen hermione_main                                                                                                                                                                                 #HERMIONE
                her "!!!"
                her "Ау! Прекратите,мне больно!"
                m "Заметил, что тебе понравилось."
                hide screen hermione_main                                                                                                                                                                                   #HERMIONE
                with d3                                                                                                                                                                                                                        #HERMIONE
                $ h_xpos=140 #Defines position of the Hermione's full length sprite. (Default 370). (Center: 140)                                                        #HERMIONE
                $ h_body = "03_hp/13_hermione_main/body_85.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
                show screen hermione_main                                                                                                                                                                                 #HERMIONE
                her "Но это не так..."
                her "И если вы собираетесь продолжить, Сэр..."
                hide screen hermione_main                                                                                                                                                                                   #HERMIONE
                with d3                                                                                                                                                                                                                        #HERMIONE
                $ h_xpos=140 #Defines position of the Hermione's full length sprite. (Default 370). (Center: 140)                                                        #HERMIONE
                $ h_body = "03_hp/13_hermione_main/body_81.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
                show screen hermione_main                                                                                                                                                                                 #HERMIONE
                her "...тогда я собираюсь уйти."
                m "Ладно, ладно..."
                hide screen hermione_main
                with d3
                jump no_smacking_tits #Jumps to usual tits molesting scene.

            elif whoring >= 15: # LEVEL 06 and higher # <=================================================================================== THIRD EVENT. 
                hide screen hermione_main                                                                                                                                                                                   #HERMIONE
                with d3                                                                                                                                                                                                                        #HERMIONE
                $ h_xpos=140 #Defines position of the Hermione's full length sprite. (Default 370). (Center: 140)                                                        #HERMIONE
                $ h_body = "03_hp/13_hermione_main/182.png" #Sprite of Hermione's upper body.                                                                           #HERMIONE
                show screen hermione_main                                                                                                                                                                                 #HERMIONE
                her "Ах!!!"
                hide screen hermione_main                                                                                                                                                                                   #HERMIONE
                with d3                                                                                                                                                                                                                        #HERMIONE
                $ h_xpos=140 #Defines position of the Hermione's full length sprite. (Default 370). (Center: 140)                                                        #HERMIONE
                $ h_body = "03_hp/13_hermione_main/185.png" #Sprite of Hermione's upper body.                                                                           #HERMIONE
                show screen hermione_main                                                                                                                                                                                 #HERMIONE
                her "Сэр, Зачем вы сделали это?"
                m "Хм... Мне показалось этой хорощей идеей..."
                m "Тебе понравилось?"
                hide screen hermione_main                                                                                                                                                                                   #HERMIONE
                with d3                                                                                                                                                                                                                        #HERMIONE
                $ h_xpos=140 #Defines position of the Hermione's full length sprite. (Default 370). (Center: 140)                                                        #HERMIONE
                $ h_body = "03_hp/13_hermione_main/body_82.png" #Sprite of Hermione's upper body.                                                                    #HERMIONE
                show screen hermione_main                                                                                                                                                                                 #HERMIONE
                her ".........."
                her "Я не извращенка..."
                hide screen hermione_main
                with d3
                show screen blktone8
                with d3
                ">Вы ещё раз смачно шлепнули грудь Гермионы!"
                hide screen blktone8
                with d3
                $ renpy.play('sounds/slap.mp3') #SLAP!
                show screen white
                with hpunch
                pause.08
                hide screen white
                hide screen hermione_main                                                                                                                                                                                   #HERMIONE
                with d3                                                                                                                                                                                                                        #HERMIONE
                $ h_xpos=140 #Defines position of the Hermione's full length sprite. (Default 370). (Center: 140)                                                        #HERMIONE
                $ h_body = "03_hp/13_hermione_main/186.png" #Sprite of Hermione's upper body.                                                                           #HERMIONE
                show screen hermione_main                                                                                                                                                                                 #HERMIONE
                her "Аа!!!"
                m "Скажи что тебе нравится!"
                her "Сэр... Я..."
                hide screen hermione_main
                with d3
                show screen blktone8
                with d5
                ">Вы ещё несколько раз шлепнули по груди!"
                $ renpy.play('sounds/slap.mp3') #SLAP!
                show screen white
                with hpunch
                pause.05
                hide screen white
                pause.3
                $ renpy.play('sounds/slap.mp3') #SLAP!
                show screen white
                with hpunch
                pause.05
                hide screen white
                pause.3
                $ renpy.play('sounds/slap.mp3') #SLAP!
                show screen white
                with hpunch
                pause.05
                hide screen white
                pause.3
                ">Сиськи Гермионы прыгали как шарики..."
                hide screen blktone8
                with d5
                hide screen hermione_main                                                                                                                                                                                   #HERMIONE
                with d3                                                                                                                                                                                                                        #HERMIONE
                $ h_xpos=140 #Defines position of the Hermione's full length sprite. (Default 370). (Center: 140)                                                        #HERMIONE
                $ h_body = "03_hp/13_hermione_main/187.png" #Sprite of Hermione's upper body.                                                                           #HERMIONE
                show screen hermione_main                                                                                                                                                                                 #HERMIONE
                her "А-аах!!! АА!!! А-ах-ааах!!!"
                m "Тебе нравится это. Признайся."
                hide screen hermione_main                                                                                                                                                                                   #HERMIONE
                with d3                                                                                                                                                                                                                        #HERMIONE
                $ h_xpos=140 #Defines position of the Hermione's full length sprite. (Default 370). (Center: 140)                                                        #HERMIONE
                $ h_body = "03_hp/13_hermione_main/188.png" #Sprite of Hermione's upper body.                                                                           #HERMIONE
                show screen hermione_main                                                                                                                                                                                 #HERMIONE
                her "..........."
                hide screen hermione_main
                hide screen ctc
                with d3
                ">Вы шлепнули по груди ещё раз."
                $ renpy.play('sounds/slap.mp3') #SLAP!
                show screen white
                with hpunch
                pause.05
                hide screen white
                pause.3
                $ renpy.play('sounds/slap.mp3') #SLAP!
                show screen white
                with hpunch
                pause.05
                hide screen white
                pause.3
                $ renpy.play('sounds/slap.mp3') #SLAP!
                show screen white
                with hpunch
                pause.05
                hide screen white
                pause.3
                hide screen hermione_main                                                                                                                                                                                   #HERMIONE
                with d3                                                                                                                                                                                                                        #HERMIONE
                $ h_xpos=140 #Defines position of the Hermione's full length sprite. (Default 370). (Center: 140)                                                        #HERMIONE
                $ h_body = "03_hp/13_hermione_main/187.png" #Sprite of Hermione's upper body.                                                                           #HERMIONE
                show screen hermione_main                                                                                                                                                                                 #HERMIONE
                with d3
                her "А-а! Да! Мне нравится, Мне нравится! А-а..."
                hide screen hermione_main                                                                                                                                                                                   #HERMIONE
                with d3                                                                                                                                                                                                                        #HERMIONE
                $ h_xpos=140 #Defines position of the Hermione's full length sprite. (Default 370). (Center: 140)                                                        #HERMIONE
                $ h_body = "03_hp/13_hermione_main/184.png" #Sprite of Hermione's upper body.                                                                           #HERMIONE
                show screen hermione_main                                                                                                                                                                                 #HERMIONE
                with d3
                her "...получается я извращенка, Сэр?"
                m "Что?"
                m "Перестань быть глупой, девченка."
                m "Это вполне естественно для девочки, наслаждаться тем, что с её грудью играют."
                her "......"
                her "Вы уверены , Сэр?"
                m "Да. Поверь мне, Я знаю."
                hide screen hermione_main
                with d3
                ">Вы начали снова шлепать её грудь!"
                $ renpy.play('sounds/slap.mp3') #SLAP!
                show screen white
                with hpunch
                pause.05
                hide screen white
                pause.3
                hide screen hermione_main                                                                                                                                                                                   #HERMIONE
                with d3                                                                                                                                                                                                                        #HERMIONE
                $ h_xpos=140 #Defines position of the Hermione's full length sprite. (Default 370). (Center: 140)                                                        #HERMIONE
                $ h_body = "03_hp/13_hermione_main/187.png" #Sprite of Hermione's upper body.                                                                           #HERMIONE
                show screen hermione_main                                                                                                                                                                                 #HERMIONE
                with d3
                her "Да-да... да... Спасибо, Сэр."
                hide screen hermione_main
                with d3
                m "Ну что-ж... Достаточно со шлепками на сегодня..."
                jump no_smacking_tits #Jumps to usual tits molesting scene.

    
    $ uni_sperm = False #Sperm layer is not displayed in hermione screen.
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
    
    stop music fadeout 1.0
    m "Да, мисс Грейнджер. 35 очков \"Гриффиндору\"." 
    $ gryffindor +=35
    $ h_xpos=140 #Defines position of the Hermione's full length sprite. (Default 370). (Center: 140)
    $ h_body = "03_hp/13_hermione_main/body_13.png" #Flashing panties
    $ badges = True
    show screen hermione_main
    hide screen hermione_01_f #Hermione stands still.
    with d3
    her "Спасибо, Сэр..."

    if whoring <= 11: # If still of level of unlocking - 04
        $ whoring +=1

    $ request_12_points += 1

    if whoring >= 9 and whoring <= 11:
        $ level = "04"
        $ new_request_12_01 = True # HEARTS.
    if whoring >= 12 and whoring <= 14:
        $ level = "05"
        $ new_request_12_02 = True # HEARTS.
    if whoring >= 15:
        $ level = "06"
        $ new_request_12_03 = True # HEARTS.


    hide screen bld1
    hide screen hermione_main
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

    $ aftersperm = False #Show cum stains on Hermione's uniform.
    call music_block
    if daytime:
        $ hermione_takes_classes = True
        jump night_main_menu
    else:
        $ hermione_sleeping = True
        jump day_main_menu            
   
    





###################REQUEST_10 (Level 03) (25 pt.) (Let a classmate touch you). (Available during daytime only).
label new_request_10:
    
    hide screen hermione_main 
    with d3
    m "{size=-4}(Сказать ей, что бы её одноклассник облапал её?){/size}"
    $ menu_x = 0.5 #Default position of the menu (0.5). Version B is $ menu_x = 0.2
    menu:
        "\"(Да, сделать это!)\"":
            pass
        "\"(Не сейчас.)\"":
            jump new_personal_request
            
    
    if request_10_points == 0: # <================================================================================ FIRST TIME
        m "Мисс Грейнджер?"
        $ h_xpos=140 #Defines position of the Hermione's full length sprite. (Default 370). 140 - center.
        $ h_body = "03_hp/13_hermione_main/body_01.png" #Flashing panties
        show screen hermione_main
        with d3
        her "Сэр?"
        m "Тебе нравятся мальчики твоего возраста, не правда ли?"
        hide screen hermione_main                                                                  # HERMIONE
        with d3                                                                                                       # HERMIONE
        $ h_body = "03_hp/13_hermione_main/body_03.png"                # HERMIONE
        show screen hermione_main                                                               # HERMIONE
        with d3                                                                                                      # HERMIONE
        her "...?"
        m "Может быть кто-то из одноклассников?"
        hide screen hermione_main                                                                  # HERMIONE
        with d3                                                                                                       # HERMIONE
        $ h_body = "03_hp/13_hermione_main/body_10.png"                # HERMIONE
        show screen hermione_main                                                               # HERMIONE
        with d3                                                                                                      # HERMIONE
        her "Ну..."
        her "Ну...Я должна обсуждать с вами такие вопросы.... Сэр?"
        hide screen hermione_main                                                                  # HERMIONE
        with d3                                                                                                       # HERMIONE
        $ h_body = "03_hp/13_hermione_main/body_29.png"                # HERMIONE
        show screen hermione_main                                                               # HERMIONE
        with d3                                                                                                      # HERMIONE
        her "Я немного стесняюсь..."
        m "Конечно,я понимаю. Мне не стоит знать детали..."
        m "Но вот что мне нужно,что бы вы сделали, мисс Грейнджер."
        m "Подойдите к какому нибудь мальчику. Тому мальчику,  \"о ком мечтаешь\", который нравится..."
        hide screen hermione_main                                                                  # HERMIONE
        with d3                                                                                                       # HERMIONE
        $ h_body = "03_hp/13_hermione_main/body_31.png"                # HERMIONE
        show screen hermione_main                                                               # HERMIONE
        with d3                                                                                                      # HERMIONE
        her ".......?"
        m "И пусть он потрогает тебя..."
        if whoring <=5 or request_02_c_points <= 1: # Counts how many times Hermione been sent to flirt with teachers.
            jump too_much
        hide screen hermione_main                                                                  # HERMIONE
        with d3                                                                                                       # HERMIONE
        $ h_body = "03_hp/13_hermione_main/body_31.png"                # HERMIONE
        show screen hermione_main                                                               # HERMIONE
        with d3                                                                                                      # HERMIONE
        her "Дать ему потрогать меня..., сэр?"
        m "Да, потрогать тебя. Как мальчики трогают девочек?"
        m "Сколько тебе лет? Ты выглядишь достаточно взрослой..."
        m "Неужели твои родители еще не \"говорили\" с тобой?"
        hide screen hermione_main                                                                  # HERMIONE
        with d3                                                                                                       # HERMIONE
        $ h_body = "03_hp/13_hermione_main/body_34.png"                # HERMIONE
        show screen hermione_main                                                               # HERMIONE
        with d3                                                                                                      # HERMIONE
        her "\"Говорила\", Сэр?"
        m "Да-да, \"говорила\"! О том, как мальчики отличаются от девочек...?"
        m "У мальчиков есть \"пиписька\" и девочкам нравится брать \"пипиську\" в рот?"
        hide screen hermione_main                                                                  # HERMIONE
        with d3                                                                                                       # HERMIONE
        $ h_body = "03_hp/13_hermione_main/body_03.png"                # HERMIONE
        show screen hermione_main                                                               # HERMIONE
        with d3                                                                                                      # HERMIONE
        her "!!!"
        hide screen hermione_main                                                                  # HERMIONE
        with d3                                                                                                       # HERMIONE
        $ h_body = "03_hp/13_hermione_main/body_47.png"                # HERMIONE
        show screen hermione_main                                                               # HERMIONE
        with d3                                                                                                      # HERMIONE
        her "Какие же родители будут такое говорить своим детям?"
        m "Думаю, Акабур будет."
        hide screen hermione_main                                                                  # HERMIONE
        with d3                                                                                                       # HERMIONE
        $ h_body = "03_hp/13_hermione_main/body_17.png"                # HERMIONE
        show screen hermione_main                                                               # HERMIONE
        with d3                                                                                                      # HERMIONE
        her "Извините, Сэр?"
        m "*Кхем!* Я имею ввиду, отвественный и заботливый!"
        m "Ну, в любом случае. Вот ваше задание на сегодня, мисс Грейнджер."
        m "Найти себе мальчика и уговорить его поласкать тебя..."
        hide screen hermione_main                                                                  # HERMIONE
        with d3                                                                                                       # HERMIONE
        $ h_body = "03_hp/13_hermione_main/body_69.png"                # HERMIONE
        show screen hermione_main                                                               # HERMIONE
        with d3                                                                                                      # HERMIONE
        her ".........."
        m "Ты симпатичная девочка, и это будет не трудно для тебя."
        her "....................."
        hide screen hermione_main                                                                  # HERMIONE
        with d3                                                                                                       # HERMIONE
        $ h_body = "03_hp/13_hermione_main/body_66.png"                # HERMIONE
        show screen hermione_main                                                               # HERMIONE
        with d3                                                                                                      # HERMIONE
        her "Сколько очков я получу за выполнение этого задания, Сэр?"
        m "Хм... Думаю 25 очков хватит..."
        hide screen hermione_main                                                                  # HERMIONE
        with d3                                                                                                       # HERMIONE
        $ h_body = "03_hp/13_hermione_main/body_69.png"                # HERMIONE
        show screen hermione_main                                                               # HERMIONE
        with d3                                                                                                      # HERMIONE
        her "25 очков..."
        her "...."
        hide screen hermione_main                                                                  # HERMIONE
        with d3                                                                                                       # HERMIONE
        $ h_body = "03_hp/13_hermione_main/body_66.png"                # HERMIONE
        show screen hermione_main                                                               # HERMIONE
        with d3                                                                                                      # HERMIONE
        her "Ладно,договорились..."
        m "Отлично..."
        hide screen hermione_main                                                                  # HERMIONE
        with d3                                                                                                       # HERMIONE
        $ h_body = "03_hp/13_hermione_main/body_05.png"                # HERMIONE
        show screen hermione_main                                                               # HERMIONE
        with d3                                                                                                      # HERMIONE
        her "Я наверно пойду. Скоро начнутся уроки..."
        hide screen hermione_main
    else:
        if whoring >= 6 and whoring <= 8: # LEVEL 03 
            m "Мисс Грейнджер?"
            $ h_xpos=140 #Defines position of the Hermione's full length sprite. (Default 370). 140 - center.
            $ h_body = "03_hp/13_hermione_main/body_01.png" #Flashing panties
            show screen hermione_main
            with d3
            her "Сэр"
            m "Как насчет того,что бы дать вашему однокласснику полапать Вас?"
            hide screen hermione_main                                                                  # HERMIONE
            with d3                                                                                                       # HERMIONE
            $ h_body = "03_hp/13_hermione_main/body_120.png"                # HERMIONE
            show screen hermione_main                                                               # HERMIONE
            with d3                                                                                                      # HERMIONE
            her "........"
            m "25 очков, мисс Грейнджер."
            hide screen hermione_main                                                                  # HERMIONE
            with d3                                                                                                       # HERMIONE
            $ h_body = "03_hp/13_hermione_main/body_69.png"                # HERMIONE
            show screen hermione_main                                                               # HERMIONE
            with d3                                                                                                      # HERMIONE
            her "Сэр, это только..."
            hide screen hermione_main                                                                  # HERMIONE
            with d3                                                                                                       # HERMIONE
            $ h_body = "03_hp/13_hermione_main/body_79.png"                # HERMIONE
            show screen hermione_main                                                               # HERMIONE
            with d3                                                                                                      # HERMIONE
            her "Я не понимаю,зачем мне делать такие вещи..."
            m "Что бы помочь своему факультету?"
            hide screen hermione_main                                                                  # HERMIONE
            with d3                                                                                                       # HERMIONE
            $ h_body = "03_hp/13_hermione_main/body_66.png"                # HERMIONE
            show screen hermione_main                                                               # HERMIONE
            with d3                                                                                                      # HERMIONE
            her "Я не про это..."
            hide screen hermione_main                                                                  # HERMIONE
            with d3                                                                                                       # HERMIONE
            $ h_body = "03_hp/13_hermione_main/body_69.png"                # HERMIONE
            show screen hermione_main                                                               # HERMIONE
            with d3                                                                                                      # HERMIONE
            her "Ладно, не обращайте внимание..."
            her "Скоро будет звонок,я наверное пойду..."
            m "Ты сделаешь это?"
            hide screen hermione_main                                                                  # HERMIONE
            with d3                                                                                                       # HERMIONE
            $ h_body = "03_hp/13_hermione_main/body_66.png"                # HERMIONE
            show screen hermione_main                                                               # HERMIONE
            with d3                                                                                                      # HERMIONE
            her "Я не знаю... Наверное..."
            hide screen hermione_main
        elif whoring >= 9 and whoring <= 11: # LEVEL 04
            m "Мисс Грейнджер, нужно что бы вы подошли к своему однокласснику, и предложили ему полапать вас."
            $ h_xpos=140 #Defines position of the Hermione's full length sprite. (Default 370). 140 - center.
            $ h_body = "03_hp/13_hermione_main/body_01.png" #Flashing panties
            show screen hermione_main
            with d3
            her "Я поняла, сэр..."
            m "Тогда ступай."
            her "..........."
            hide screen hermione_main
        elif whoring >= 12: # LEVEL 05+
            m "Мисс Грейнджер, я хочу,что бы вы вышли..."
            m "Нашли привлекательного парня и дали ему себя облапать!"
            $ h_xpos=140 #Defines position of the Hermione's full length sprite. (Default 370). 140 - center.
            $ h_body = "03_hp/13_hermione_main/body_01.png" #Flashing panties
            show screen hermione_main
            with d3
            her "В каком смысле...?"
            hide screen hermione_main                                                                                                                                                                                   #HERMIONE
            with d3                                                                                                                                                                                                                        #HERMIONE
            $ h_body = "03_hp/13_hermione_main/body_122.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
            show screen hermione_main                                                                                                                                                                                 #HERMIONE
            with d3                                                                                                                                                                                                                        #HERMIONE
            her "В сексуальном, Сэр?"
            m "Что? Не, Я имею ввиду, что бы он потрогал вас под одеждой..."
            hide screen hermione_main                                                                                                                                                                                   #HERMIONE
            with d3                                                                                                                                                                                                                        #HERMIONE
            $ h_body = "03_hp/13_hermione_main/body_24.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
            show screen hermione_main                                                                                                                                                                                 #HERMIONE
            with d3                                                                                                                                                                                                                        #HERMIONE
            her "А, понятно..."
            hide screen hermione_main                                                                                                                                                                                   #HERMIONE
            with d3                                                                                                                                                                                                                        #HERMIONE
            $ h_body = "03_hp/13_hermione_main/body_68.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
            show screen hermione_main                                                                                                                                                                                 #HERMIONE
            with d3                                                                                                                                                                                                                        #HERMIONE
            her "Хотелось бы что бы это был..."
            hide screen hermione_main                                                                                                                                                                                   #HERMIONE
            with d3                                                                                                                                                                                                                        #HERMIONE
            $ h_body = "03_hp/13_hermione_main/body_117.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
            show screen hermione_main                                                                                                                                                                                 #HERMIONE
            with d3                                                                                                                                                                                                                        #HERMIONE
            her "А ничего, если это будет не один парень,ладно?"
            m "Ты ещё спрашиваешь! Конечно нет!"
            m "Если кто нибудь будет - это считается." 
            hide screen hermione_main                                                                                                                                                                                   #HERMIONE
            with d3                                                                                                                                                                                                                        #HERMIONE
            $ h_body = "03_hp/13_hermione_main/body_122.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
            show screen hermione_main                                                                                                                                                                                 #HERMIONE
            with d3                                                                                                                                                                                                                        #HERMIONE
            her "Отлично. Я зайду к вам после учебы, Сэр. Как обычно."
            m "Хорошо. Удачи."
            hide screen hermione_main

   

    $ request_10 = True

    hide screen bld1
    hide screen hermione_main
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


    $ hermione_takes_classes = True
    jump day_main_menu

        
label new_request_10_complete: #<==========================================================================EVENING
    
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
    
    $ h_xpos=370 #Defines position of the Hermione's full length sprite.
    $ h_ypos=0
    $ h_body = "03_hp/13_hermione_main/body_01.png" #Sprite of Hermione's upper body.
    show screen hermione_main
    show screen hermione_02
    with Dissolve(.3)
    
    her "Добрый вечер, Сэр."
    m "Мисс Грейнджер..."
    m "Вы выполнили задание?"
    her "Я сделала так как вы просили..."
    menu:
        "\"Отлично. Вот твои очки.\"":
            pass
        "\"Расскажи подробнее.\"":
            hide screen hermione_main
            with d3
            m "Расскажи подробнее."
            show screen blktone
            with d3
            
            if whoring >= 6 and whoring <= 8: # LEVEL 03 # EVENT LEVEL 01.
                stop music fadeout 3.0
                hide screen hermione_main                                                                                                                                                                                   #HERMIONE
                with d3                                                                                                                                                                                                                        #HERMIONE
                $ h_xpos=370 #Defines position of the Hermione's full length sprite. (Default 370). (Center: 140)                                                       #HERMIONE
                $ h_body = "03_hp/13_hermione_main/body_12.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
                show screen hermione_main                                                                                                                                                                                 #HERMIONE
                with d3                                                                                                                                                                                                                        #HERMIONE
                her "......"
                hide screen hermione_main                                                                                                                                                                                   #HERMIONE
                with d3                                                                                                                                                                                                                        #HERMIONE
                $ h_body = "03_hp/13_hermione_main/body_13.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
                show screen hermione_main                                                                                                                                                                                 #HERMIONE
                with d3                                                                                                                                                                                                                        #HERMIONE
                her "Ну... Эм..."
                m "Говори, девочка."
                m "Ты дала себя потрогать какому нибудь везунчику?"
                    
                if one_out_of_three == 1: ### EVENT (A)
                    her "Да,дала, Сэр..."
                    m "Ну же? Расскажи."
                    her "Ну вообще-то, мало чего рассказывать..."
                    hide screen hermione_main                                                                                                                                                                                   #HERMIONE
                    with d3                                                                                                                                                                                                                        #HERMIONE
                    $ h_body = "03_hp/13_hermione_main/body_31.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
                    show screen hermione_main                                                                                                                                                                                 #HERMIONE
                    with d3                                                                                                                                                                                                                        #HERMIONE
                    her "Я сказала одному парню,что он может меня потрогать немного, если захочет..."
                    hide screen hermione_main                                                                                                                                                                                   #HERMIONE
                    with d3                                                                                                                                                                                                                        #HERMIONE
                    $ h_body = "03_hp/13_hermione_main/body_29.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
                    show screen hermione_main                                                                                                                                                                                 #HERMIONE
                    with d3                                                                                                                                                                                                                        #HERMIONE
                    her "Он подумал что это шутка сначала..."
                    hide screen hermione_main                                                                                                                                                                                   #HERMIONE
                    with d3                                                                                                                                                                                                                        #HERMIONE
                    $ h_body = "03_hp/13_hermione_main/body_33.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
                    show screen hermione_main                                                                                                                                                                                 #HERMIONE
                    with d3                                                                                                                                                                                                                        #HERMIONE
                    her "Так стыдно..."
                    m "Так, он трогал тебя или нет?"
                    hide screen hermione_main                                                                                                                                                                                   #HERMIONE
                    with d3                                                                                                                                                                                                                        #HERMIONE
                    $ h_body = "03_hp/13_hermione_main/body_33.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
                    show screen hermione_main                                                                                                                                                                                 #HERMIONE
                    with d3                                                                                                                                                                                                                        #HERMIONE
                    play music "music/(Orchestral) Playful Tension by Shadow16nh.mp3" fadein 1 fadeout 1 # SEX THEME.
                    her "Да,трогал..."
                    m "Ну и где же он тебя трогал?"
                    hide screen hermione_main                                                                                                                                                                                   #HERMIONE
                    with d3                                                                                                                                                                                                                        #HERMIONE
                    $ h_body = "03_hp/13_hermione_main/body_29.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
                    show screen hermione_main                                                                                                                                                                                 #HERMIONE
                    with d3                                                                                                                                                                                                                        #HERMIONE
                    her "Эм... мои ноги..."
                    her "И мою грудь немного..."
                    m "Это всё?"
                    hide screen hermione_main                                                                                                                                                                                   #HERMIONE
                    with d3                                                                                                                                                                                                                        #HERMIONE
                    $ h_body = "03_hp/13_hermione_main/body_31.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
                    show screen hermione_main                                                                                                                                                                                 #HERMIONE
                    with d3                                                                                                                                                                                                                        #HERMIONE
                    her "Да, сэр..."
                    hide screen hermione_main                                                                                                                                                                                   #HERMIONE
                    with d3                                                                                                                                                                                                                        #HERMIONE
                    $ h_body = "03_hp/13_hermione_main/body_33.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
                    show screen hermione_main                                                                                                                                                                                 #HERMIONE
                    with d3                                                                                                                                                                                                                        #HERMIONE
                    her "Уже поздно... я думаю мне пора..."
                    hide screen hermione_main                                                                                                                                                                                   #HERMIONE
                    with d3                                                                                                                                                                                                                        #HERMIONE
                    $ h_body = "03_hp/13_hermione_main/body_34.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
                    show screen hermione_main                                                                                                                                                                                 #HERMIONE
                    with d3                                                                                                                                                                                                                        #HERMIONE
                    her "Извините, Сэр..."
                    m "Тебе не стоит извиняться, девочка."
                    m "Ты молодец. Этого достаточно пока что."
                    
                elif one_out_of_three == 2: ### EVENT (B)
                    stop music fadeout 3.0
                    hide screen hermione_main                                                                                                                                                                                   #HERMIONE
                    with d3                                                                                                                                                                                                                        #HERMIONE
                    $ h_body = "03_hp/13_hermione_main/body_69.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
                    show screen hermione_main                                                                                                                                                                                 #HERMIONE
                    with d3                                                                                                                                                                                                                        #HERMIONE
                    her "Я сделала это, Сэр."
                    her "Но это было так отвратительно и стыдно..."
                    m "Это всё что ты хочешь сказать мне?."
                    m "Лучше расскажи где он тебя трогал..."
                    play music "music/(Orchestral) Playful Tension by Shadow16nh.mp3" fadein 1 fadeout 1 # SEX THEME.
                    her "Эм..."
                    hide screen hermione_main                                                                                                                                                                                   #HERMIONE
                    with d3                                                                                                                                                                                                                        #HERMIONE
                    $ h_body = "03_hp/13_hermione_main/body_117.png" #Sprite of Hermione's upper body.                                                                 #HERMIONE
                    show screen hermione_main                                                                                                                                                                                 #HERMIONE
                    with d3                                                                                                                                                                                                                        #HERMIONE
                    her "Ну он трогал меня под юбкой немного..."
                    her "Я дала ему потрогать мою..."
                    hide screen hermione_main                                                                                                                                                                                   #HERMIONE
                    with d3                                                                                                                                                                                                                        #HERMIONE
                    $ h_body = "03_hp/13_hermione_main/body_118.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
                    show screen hermione_main                                                                                                                                                                                 #HERMIONE
                    with d3                                                                                                                                                                                                                        #HERMIONE
                    her "...киску через юбку, сэр."
                    m "Хорошо. Что было потом?"
                    hide screen hermione_main                                                                                                                                                                                   #HERMIONE
                    with d3                                                                                                                                                                                                                        #HERMIONE
                    $ h_body = "03_hp/13_hermione_main/body_131.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
                    show screen hermione_main                                                                                                                                                                                 #HERMIONE
                    with d3                                                                                                                                                                                                                        #HERMIONE
                    her "Затем он начал трогать себя..."
                    her "Потом я решила уйти..."
                    m "Ясно..."
                    hide screen hermione_main                                                                                                                                                                                   #HERMIONE
                    with d3                                                                                                                                                                                                                        #HERMIONE
                    $ h_body = "03_hp/13_hermione_main/body_33.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
                    show screen hermione_main                                                                                                                                                                                 #HERMIONE
                    with d3                                                                                                                                                                                                                        #HERMIONE
                    her "............."
                    
                elif one_out_of_three == 3: ### EVENT (C)
                    her "Я сделала это, сэр..."
                    hide screen hermione_main                                                                                                                                                                                   #HERMIONE
                    with d3                                                                                                                                                                                                                        #HERMIONE
                    $ h_body = "03_hp/13_hermione_main/body_31.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
                    show screen hermione_main                                                                                                                                                                                 #HERMIONE
                    with d3                                                                                                                                                                                                                        #HERMIONE
                    play music "music/(Orchestral) Playful Tension by Shadow16nh.mp3" fadein 1 fadeout 1 # SEX THEME.
                    her "Я завела одного парня из \"Пуффендуя\" в пустую комнату и предложила ему потрогать себя, если он захочет."
                    her "И..."
                    hide screen hermione_main                                                                                                                                                                                   #HERMIONE
                    with d3                                                                                                                                                                                                                        #HERMIONE
                    $ h_body = "03_hp/13_hermione_main/body_29.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
                    show screen hermione_main                                                                                                                                                                                 #HERMIONE
                    with d3                                                                                                                                                                                                                        #HERMIONE
                    her "..........."
                    m "И?"
                    hide screen hermione_main                                                                                                                                                                                   #HERMIONE
                    with d3                                                                                                                                                                                                                        #HERMIONE
                    $ h_body = "03_hp/13_hermione_main/body_31.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
                    show screen hermione_main                                                                                                                                                                                 #HERMIONE
                    with d3                                                                                                                                                                                                                        #HERMIONE
                    her "Ну, он сначала трогал меня..."
                    hide screen hermione_main                                                                                                                                                                                   #HERMIONE
                    with d3                                                                                                                                                                                                                        #HERMIONE
                    $ h_body = "03_hp/13_hermione_main/body_33.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
                    show screen hermione_main                                                                                                                                                                                 #HERMIONE
                    with d3                                                                                                                                                                                                                        #HERMIONE
                    her "......"
                    m "Не заставляй меня вытаскивать из тебя каждое слово!"
                    m "Что произошло потом?"
                    hide screen hermione_main                                                                                                                                                                                   #HERMIONE
                    with d3                                                                                                                                                                                                                        #HERMIONE
                    $ h_body = "03_hp/13_hermione_main/body_87.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
                    show screen hermione_main                                                                                                                                                                                 #HERMIONE
                    with d3                                                                                                                                                                                                                        #HERMIONE
                    her "Ну..."
                    stop music fadeout 1.0
                    her "Я думала ему понравилось лапать {size=+5}меня{/size} {size=+5}собой{/size}..."
                    hide screen hermione_main                                                                                                                                                                                   #HERMIONE
                    with d3                                                                                                                                                                                                                        #HERMIONE
                    $ h_body = "03_hp/13_hermione_main/body_44.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
                    show screen hermione_main                                                                                                                                                                                 #HERMIONE
                    with d3                                                                                                                                                                                                                        #HERMIONE
                    her "Он просил меня называть его \"Сисястым мальчиком\"..."
                    play music "music/Despair_by_erenik.mp3" fadein 1 fadeout 1 # SAD THEME.
                    hide screen hermione_main                                                                                                                                                                                   #HERMIONE
                    with d3                                                                                                                                                                                                                        #HERMIONE
                    $ h_body = "03_hp/13_hermione_main/body_31.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
                    show screen hermione_main                                                                                                                                                                                 #HERMIONE
                    with d3                                                                                                                                                                                                                        #HERMIONE
                    her "И потом он рассказал мне, что у него очень маленький член..."
                    hide screen hermione_main                                                                                                                                                                                   #HERMIONE
                    with d3                                                                                                                                                                                                                        #HERMIONE
                    $ h_body = "03_hp/13_hermione_main/body_22.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
                    show screen hermione_main                                                                                                                                                                                 #HERMIONE
                    with d3                                                                                                                                                                                                                        #HERMIONE
                    her "Он просто повторял это *всхлип*..."
                    hide screen hermione_main                                                                                                                                                                                   #HERMIONE
                    with d3                                                                                                                                                                                                                        #HERMIONE
                    $ h_body = "03_hp/13_hermione_main/body_21.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
                    show screen hermione_main                                                                                                                                                                                 #HERMIONE
                    with d3                                                                                                                                                                                                                        #HERMIONE
                    her "Почему есть такие идиоты как он?"
                    her "*Хнык!* Я больше не могла находиться рядом с ним и убежала...."
                    m "Извините что рассказываю вам это..."
                    hide screen hermione_main                                                                                                                                                                                   #HERMIONE
                    with d3                                                                                                                                                                                                                        #HERMIONE
                    $ h_body = "03_hp/13_hermione_main/body_21.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
                    show screen hermione_main                                                                                                                                                                                 #HERMIONE
                    with d3                                                                                                                                                                                                                        #HERMIONE
                    her "Это было просто ужасно, Сэр..."
                    m "Ладно тебе, ладно..."
                    hide screen hermione_main                                                                                                                                                                                   #HERMIONE
                    with d3                                                                                                                                                                                                                        #HERMIONE
                    $ h_body = "03_hp/13_hermione_main/body_23.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
                    show screen hermione_main                                                                                                                                                                                 #HERMIONE
                    with d3                                                                                                                                                                                                                        #HERMIONE
                    her "*Хнык!*"
                    m "Если я накину тебе 10 дополнительных очков,тебе будет легче?"
                    hide screen hermione_main                                                                                                                                                                                   #HERMIONE
                    with d3                                                                                                                                                                                                                        #HERMIONE
                    $ h_body = "03_hp/13_hermione_main/body_19.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
                    show screen hermione_main                                                                                                                                                                                 #HERMIONE
                    with d3                                                                                                                                                                                                                        #HERMIONE
                    her "М? Это было бы мило с вашей стороны."
                    m "Конечно... 10 дополнительных очков \"Гриффиндору\"."
                    hide screen hermione_main                                                                                                                                                                                   #HERMIONE
                    with d3                                                                                                                                                                                                                        #HERMIONE
                    $ h_body = "03_hp/13_hermione_main/body_140.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
                    show screen hermione_main                                                                                                                                                                                 #HERMIONE
                    with d3                                                                                                                                                                                                                        #HERMIONE
                    her "Спасибо,Сэр..."
                    m "И вот остальные баллы..."
            
            elif whoring >= 9 and whoring <= 11: # LEVEL 04
                if one_out_of_three == 1: ### EVENT (A)
                    hide screen hermione_main                                                                                                                                                                                   #HERMIONE
                    with d3                                                                                                                                                                                                                        #HERMIONE
                    $ h_xpos=370 #Defines position of the Hermione's full length sprite. (Default 370). (Center: 140)                                                       #HERMIONE
                    $ h_body = "03_hp/13_hermione_main/body_16.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
                    show screen hermione_main                                                                                                                                                                                 #HERMIONE
                    with d3                                                                                                                                                                                                                        #HERMIONE
                    her "Ну... Тут нечего рассказывать..."
                    her "Я нашла одного мальчика из \"Когтерван\"..."
                    her "Завела его в свободную аудиторию в восточном крыле..."
                    her "Он подумал,что я хочу посмотреть на его мускулы..."
                    her "Но я сказала, что хочу,что бы он потрогал меня..."
                    hide screen hermione_main                                                                                                                                                                                   #HERMIONE
                    with d3                                                                                                                                                                                                                        #HERMIONE
                    $ h_body = "03_hp/13_hermione_main/body_33.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
                    show screen hermione_main                                                                                                                                                                                 #HERMIONE
                    with d3                                                                                                                                                                                                                        #HERMIONE
                    her "...ну и он начал меня трогать."
                    m "Ясно..."
                    m "Хорошая работа, Мисс Грейнджер."
                    hide screen hermione_main                                                                                                                                                                                   #HERMIONE
                    with d3                                                                                                                                                                                                                        #HERMIONE
                    $ h_xpos=370 #Defines position of the Hermione's full length sprite. (Default 370). (Center: 140)                                                       #HERMIONE
                    $ h_body = "03_hp/13_hermione_main/body_44.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
                    show screen hermione_main                                                                                                                                                                                 #HERMIONE
                    with d3                                                                                                                                                                                                                        #HERMIONE
                    her "Я получу свои очки,Сэр?"
                    m "Одну минуту, мисс Грейнджер. Я хочу получить ответ на вопрос, который сейчас задам."
                    hide screen hermione_main                                                                                                                                                                                   #HERMIONE
                    with d3                                                                                                                                                                                                                        #HERMIONE
                    $ h_xpos=370 #Defines position of the Hermione's full length sprite. (Default 370). (Center: 140)                                                       #HERMIONE
                    $ h_body = "03_hp/13_hermione_main/body_31.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
                    show screen hermione_main                                                                                                                                                                                 #HERMIONE
                    with d3                                                                                                                                                                                                                        #HERMIONE
                    her "???"
                    m "Вам понравилось?"
                    m "Вам понравилось то чувство,когда он трогал вас?"
                    hide screen hermione_main                                                                                                                                                                                   #HERMIONE
                    with d3                                                                                                                                                                                                                        #HERMIONE
                    $ h_xpos=370 #Defines position of the Hermione's full length sprite. (Default 370). (Center: 140)                                                       #HERMIONE
                    $ h_body = "03_hp/13_hermione_main/body_127.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
                    show screen hermione_main                                                                                                                                                                                 #HERMIONE
                    with d3                                                                                                                                                                                                                        #HERMIONE
                    her "Хм..."
                    her "Ну, он был симпатичным..."
                    hide screen hermione_main                                                                                                                                                                                   #HERMIONE
                    with d3                                                                                                                                                                                                                        #HERMIONE
                    $ h_xpos=370 #Defines position of the Hermione's full length sprite. (Default 370). (Center: 140)                                                       #HERMIONE
                    $ h_body = "03_hp/13_hermione_main/body_120.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
                    show screen hermione_main                                                                                                                                                                                 #HERMIONE
                    with d3                                                                                                                                                                                                                        #HERMIONE
                    her "Я не была зла на него,что он трогает меня, если вы это хотели услышать, Сэр..."
                    m "Ясно..."
                    
                elif one_out_of_three == 2: ### EVENT (B)
                    hide screen hermione_main                                                                                                                                                                                   #HERMIONE
                    with d3                                                                                                                                                                                                                        #HERMIONE
                    $ h_xpos=370 #Defines position of the Hermione's full length sprite. (Default 370). (Center: 140)                                                       #HERMIONE
                    $ h_body = "03_hp/13_hermione_main/body_16.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
                    show screen hermione_main                                                                                                                                                                                 #HERMIONE
                    with d3                                                                                                                                                                                                                        #HERMIONE
                    her "Ну..."
                    her "Я не уверена в том,что это вы хотите услышать, но..."
                    her "Во время того, как нас учили собирать траву..."
                    hide screen hermione_main                                                                                                                                                                                   #HERMIONE
                    with d3                                                                                                                                                                                                                        #HERMIONE
                    $ h_body = "03_hp/13_hermione_main/body_44.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
                    show screen hermione_main                                                                                                                                                                                 #HERMIONE
                    with d3                                                                                                                                                                                                                        #HERMIONE
                    her "Я дала одному парну дотронуться до себя под юбкой..."
                    her "И пока профессор Стебель обьясняла разницу между \"мандрейк\" и \"мандрагоры\"..."
                    hide screen hermione_main                                                                                                                                                                                   #HERMIONE
                    with d3                                                                                                                                                                                                                        #HERMIONE
                    $ h_body = "03_hp/13_hermione_main/body_08.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
                    show screen hermione_main                                                                                                                                                                                 #HERMIONE
                    with d3                                                                                                                                                                                                                        #HERMIONE
                    her "Конечно,кое что я знала уже..."
                    hide screen hermione_main                                                                                                                                                                                   #HERMIONE
                    with d3                                                                                                                                                                                                                        #HERMIONE
                    $ h_body = "03_hp/13_hermione_main/body_44.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
                    show screen hermione_main                                                                                                                                                                                 #HERMIONE
                    with d3                                                                                                                                                                                                                        #HERMIONE
                    her "Я дала потрогать своему партнеру по лабораторным, потрогать мою попу..."
                    her "Ну вот и всё..."
                    m "Хм..."
                    menu:
                        "\"Ты могла бы и постараться,что бы выполнить задание.\"":
                            hide screen hermione_main                                                                                                                                                                                   #HERMIONE
                            with d3                                                                                                                                                                                                                        #HERMIONE
                            $ h_body = "03_hp/13_hermione_main/body_31.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
                            show screen hermione_main                                                                                                                                                                                 #HERMIONE
                            with d3                                                                                                                                                                                                                        #HERMIONE
                            her "Да,я знаю,извините."
                            m "Просто постарайся в следующий раз лучше."
                            her "Хорошо,я постараюсь, Сэр."
                        "\"Хвалю,что сделала это во время занятий.\"":
                            hide screen hermione_main                                                                                                                                                                                   #HERMIONE
                            with d3                                                                                                                                                                                                                        #HERMIONE
                            $ h_body = "03_hp/13_hermione_main/body_74.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
                            show screen hermione_main                                                                                                                                                                                 #HERMIONE
                            with d3                                                                                                                                                                                                                        #HERMIONE
                            her "Спасибо, Сэр."
                            m "Вижу,что ты заслужила награду."
                            
                elif one_out_of_three == 3: ### EVENT (C)
                    stop music fadeout 1.0
                    hide screen hermione_main                                                                                                                                                                                   #HERMIONE
                    with d3                                                                                                                                                                                                                        #HERMIONE
                    $ h_xpos=370 #Defines position of the Hermione's full length sprite. (Default 370). (Center: 140)                                                       #HERMIONE
                    $ h_body = "03_hp/13_hermione_main/body_69.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
                    show screen hermione_main                                                                                                                                                                                 #HERMIONE
                    with d3                                                                                                                                                                                                                        #HERMIONE
                    her "................."
                    m "???"
                    hide screen hermione_main                                                                                                                                                                                   #HERMIONE
                    with d3                                                                                                                                                                                                                        #HERMIONE
                    $ h_body = "03_hp/13_hermione_main/body_69.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
                    show screen hermione_main                                                                                                                                                                                 #HERMIONE
                    with d3                                                                                                                                                                                                                        #HERMIONE
                    
                    play music "music/(Orchestral) Playful Tension by Shadow16nh.mp3" fadein 1 fadeout 1 # SEX THEME.
                    
                    her "Я не хочу говорить об этом, Сэр..." 
                    m "Что случилось,малышка. Выговорись."
                    hide screen hermione_main                                                                                                                                                                                   #HERMIONE
                    with d3                                                                                                                                                                                                                        #HERMIONE
                    $ h_body = "03_hp/13_hermione_main/body_79.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
                    show screen hermione_main                                                                                                                                                                                 #HERMIONE
                    with d3                                                                                                                                                                                                                        #HERMIONE
                    her "................."
                    hide screen hermione_main                                                                                                                                                                                   #HERMIONE
                    with d3                                                                                                                                                                                                                        #HERMIONE
                    $ h_body = "03_hp/13_hermione_main/body_31.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
                    show screen hermione_main                                                                                                                                                                                 #HERMIONE
                    with d3                                                                                                                                                                                                                        #HERMIONE
                    her "Но... мне так стыдно..."
                    hide screen hermione_main                                                                                                                                                                                   #HERMIONE
                    with d3                                                                                                                                                                                                                        #HERMIONE
                    $ h_body = "03_hp/13_hermione_main/body_33.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
                    show screen hermione_main                                                                                                                                                                                 #HERMIONE
                    with d3                                                                                                                                                                                                                        #HERMIONE
                    her "Мне правда нужно рассказывать, Сэр?"
                    m "Да, Я люблю слушать такие вещи!"
                    hide screen hermione_main                                                                                                                                                                                   #HERMIONE
                    with d3                                                                                                                                                                                                                        #HERMIONE
                    $ h_body = "03_hp/13_hermione_main/body_69.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
                    show screen hermione_main                                                                                                                                                                                 #HERMIONE
                    with d3                                                                                                                                                                                                                        #HERMIONE
                    her "................."
                    her "Ладно..."
                    her "Я подошла к парню,которого всегда считала привлекательным..."
                    her "Нашла в себе силы и попросила его идти за мной..."
                    hide screen hermione_main                                                                                                                                                                                   #HERMIONE
                    with d3                                                                                                                                                                                                                        #HERMIONE
                    $ h_body = "03_hp/13_hermione_main/body_31.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
                    show screen hermione_main                                                                                                                                                                                 #HERMIONE
                    with d3                                                                                                                                                                                                                        #HERMIONE
                    her "Обычно я бы даже не подошла к нему..."
                    her "Но факт того,что я делаю задание, каким-то образом заставило меня собрать свою волю в кулак..."
                    her "это дало мне смелость..."
                    m "Рад помочь, Мисс Грейнджер."
                    hide screen hermione_main                                                                                                                                                                                   #HERMIONE
                    with d3                                                                                                                                                                                                                        #HERMIONE
                    $ h_body = "03_hp/13_hermione_main/body_87.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
                    show screen hermione_main                                                                                                                                                                                 #HERMIONE
                    with d3                                                                                                                                                                                                                        #HERMIONE
                    her "Я завела его в библиотеку..."
                    her "Мы нашли тихое место, между книжными шкафами..."
                    her "И я сказала ему,что он может меня трогать как пожелает..."                 
                    her "И...."
                    hide screen hermione_main                                                                                                                                                                                   #HERMIONE
                    with d3                                                                                                                                                                                                                        #HERMIONE
                    $ h_body = "03_hp/13_hermione_main/body_88.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
                    show screen hermione_main                                                                                                                                                                                 #HERMIONE
                    with d3                                                                                                                                                                                                                        #HERMIONE
                    her ".........."
                    m "Что?"
                    hide screen hermione_main                                                                                                                                                                                   #HERMIONE
                    with d3                                                                                                                                                                                                                        #HERMIONE
                    $ h_body = "03_hp/13_hermione_main/body_33.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
                    show screen hermione_main                                                                                                                                                                                 #HERMIONE
                    with d3                                                                                                                                                                                                                        #HERMIONE
                    her "....................."
                    hide screen hermione_main                                                                                                                                                                                   #HERMIONE
                    with d3                                                                                                                                                                                                                        #HERMIONE
                    $ h_body = "03_hp/13_hermione_main/body_32.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
                    show screen hermione_main                                                                                                                                                                                 #HERMIONE
                    with d3                                                                                                                                                                                                                        #HERMIONE
                    play music "music/Despair_by_erenik.mp3" fadein 1 fadeout 1 # SAD THEME.
                    her "Он начал трогать мои... ноги, Сэр."
                    m "Эм?"
                    m "Ваши \"ноги\"? Это как тот малый с большими сиськами на днях?"
                    hide screen hermione_main                                                                                                                                                                                   #HERMIONE
                    with d3                                                                                                                                                                                                                        #HERMIONE
                    $ h_body = "03_hp/13_hermione_main/body_66.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
                    show screen hermione_main                                                                                                                                                                                 #HERMIONE
                    with d3                                                                                                                                                                                                                        #HERMIONE
                    her "Нет, сэр..."
                    her "Он попросил,что бы я сняла свою обувь..."
                    her "Потом он..."
                    hide screen hermione_main                                                                                                                                                                                   #HERMIONE
                    with d3                                                                                                                                                                                                                        #HERMIONE
                    $ h_body = "03_hp/13_hermione_main/body_21.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
                    show screen hermione_main                                                                                                                                                                                 #HERMIONE
                    with d3                                                                                                                                                                                                                        #HERMIONE
                    her "Он стал нюхать мои ладыжки, Сэр!"
                    hide screen hermione_main                                                                                                                                                                                   #HERMIONE
                    with d3                                                                                                                                                                                                                        #HERMIONE
                    $ h_body = "03_hp/13_hermione_main/body_22.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
                    show screen hermione_main                                                                                                                                                                                 #HERMIONE
                    with d3                                                                                                                                                                                                                        #HERMIONE
                    her "Я почувствовала себя такой... разбитой!"
                    m "И он даже не притронулся к твоей груди или попке?"
                    hide screen hermione_main                                                                                                                                                                                   #HERMIONE
                    with d3                                                                                                                                                                                                                        #HERMIONE
                    $ h_body = "03_hp/13_hermione_main/body_143.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
                    show screen hermione_main                                                                                                                                                                                 #HERMIONE
                    with d3                                                                                                                                                                                                                        #HERMIONE
                    her "Нет, Сэр... *хнык!*"
                    m "Ладно, что случилось потом?"
                    hide screen hermione_main                                                                                                                                                                                   #HERMIONE
                    with d3                                                                                                                                                                                                                        #HERMIONE
                    $ h_body = "03_hp/13_hermione_main/body_142.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
                    show screen hermione_main                                                                                                                                                                                 #HERMIONE
                    with d3                                                                                                                                                                                                                        #HERMIONE
                    her "Ничего! Я не выдержала этого унижения и... убежала..."
                    her "Я даже забыла там свою обувь и спустя пару часов пришлось возвращаться за ней..."
                    hide screen hermione_main                                                                                                                                                                                   #HERMIONE
                    with d3                                                                                                                                                                                                                        #HERMIONE
                    $ h_body = "03_hp/13_hermione_main/body_145.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
                    show screen hermione_main                                                                                                                                                                                 #HERMIONE
                    with d3                                                                                                                                                                                                                        #HERMIONE
                    her "*Хнык!*............"
                    m "Хм..."
                    m "Получается он тебя облапал..."
                    m "Правда немного в своеобразной манере..."
                    hide screen hermione_main                                                                                                                                                                                   #HERMIONE
                    with d3                                                                                                                                                                                                                        #HERMIONE
                    $ h_body = "03_hp/13_hermione_main/body_145.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
                    show screen hermione_main                                                                                                                                                                                 #HERMIONE
                    with d3                                                                                                                                                                                                                        #HERMIONE
                    her "*Хнык!* Как бы я хотела, что бы он просто потрогал мою грудь или попу,как обычный мальчик, Сэр... *Хнык!*"
                    m "Успокойся, успокойся..."
                    m "Ты заработала свою награду сегодня..."
        
        
        
            elif whoring >= 12: # LEVEL 05+
                if one_out_of_three == 1: ### EVENT (A)
                    stop music fadeout 1.0
                    hide screen hermione_main                                                                                                                                                                                   #HERMIONE
                    with d3                                                                                                                                                                                                                        #HERMIONE
                    $ h_body = "03_hp/13_hermione_main/body_29.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
                    show screen hermione_main                                                                                                                                                                                 #HERMIONE
                    with d3                                                                                                                                                                                                                        #HERMIONE
                    her "......"
                    hide screen hermione_main                                                                                                                                                                                   #HERMIONE
                    with d3                                                                                                                                                                                                                        #HERMIONE
                    $ h_body = "03_hp/13_hermione_main/body_31.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
                    show screen hermione_main                                                                                                                                                                                 #HERMIONE
                    with d3       
                    her "Ну..."
                    her "Во время зельеварения, сегодня..."
                    her "Я написала записку на клочке бумаги..."
                    her "И передала её моему партнёру по лабораторным работам, и затем..."
                    hide screen hermione_main                                                                                                                                                                                   #HERMIONE
                    with d3                                                                                                                                                                                                                        #HERMIONE
                    $ h_body = "03_hp/13_hermione_main/body_69.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
                    show screen hermione_main                                                                                                                                                                                 #HERMIONE
                    with d3       
                    play music "music/Chipper Doodle v2.mp3" fadein 1 fadeout 1 # HERMIONE'S THEME.
                    her "Профессор Снейп вытащил её из моей руки..."
                    hide screen hermione_main                                                                                                                                                                                   #HERMIONE
                    with d3                                                                                                                                                                                                                        #HERMIONE
                    $ h_body = "03_hp/13_hermione_main/body_79.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
                    show screen hermione_main                                                                                                                                                                                 #HERMIONE
                    with d3       
                    her "Он прочитал её перед всем классом, который был заполнен полностью..."
                    m "О чем говорилось в записке?"
                    hide screen hermione_main                                                                                                                                                                                   #HERMIONE
                    with d3                                                                                                                                                                                                                        #HERMIONE
                    $ h_body = "03_hp/13_hermione_main/body_87.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
                    show screen hermione_main                                                                                                                                                                                 #HERMIONE
                    with d3       
                    her "Ну..."
                    her "Там было сказано: \"Ты можешь потрогать мою попку,если захочешь. Я думаю Профессор Снейп не догадается.\""
                    hide screen hermione_main                                                                                                                                                                                   #HERMIONE
                    with d3                                                                                                                                                                                                                        #HERMIONE
                    $ h_body = "03_hp/13_hermione_main/body_118.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
                    show screen hermione_main                                                                                                                                                                                 #HERMIONE
                    with d3       
                    her "Все смеялись..."
                    her "Было так стыдно,что я хотела провалиться на месте..."
                    hide screen hermione_main                                                                                                                                                                                   #HERMIONE
                    with d3                                                                                                                                                                                                                        #HERMIONE
                    $ h_body = "03_hp/13_hermione_main/body_47.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
                    show screen hermione_main                                                                                                                                                                                 #HERMIONE
                    with d3       
                    her "Я ненавижу профессора Снейпа, Сэр..."
                    m "Что случилось потом?"
                    hide screen hermione_main                                                                                                                                                                                   #HERMIONE
                    with d3                                                                                                                                                                                                                        #HERMIONE
                    $ h_body = "03_hp/13_hermione_main/body_87.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
                    show screen hermione_main                                                                                                                                                                                 #HERMIONE
                    with d3       
                    her "Ничего..."
                    play music "music/(Orchestral) Playful Tension by Shadow16nh.mp3" fadein 1 fadeout 1 # SEX THEME.
                    her "Но когда закончились занятия..."
                    her "Я заметила как три парня из \"Слизерин\" жадно и пошло смотрят на меня..."
                    her "Вообще-то они для меня ничего не значат..."
                    her "По этому мы ждали пока все выйдут из класса..."
                    hide screen hermione_main                                                                                                                                                                                   #HERMIONE
                    with d3                                                                                                                                                                                                                        #HERMIONE
                    $ h_body = "03_hp/13_hermione_main/body_117.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
                    show screen hermione_main                                                                                                                                                                                 #HERMIONE
                    with d3       
                    her "И потом я дала им потрогать себя..."
                    her "Они трогали меня везде, профессор..."
                    m "\"Везде\"?"
                    her "Да... Везде, Сэр..."
                    hide screen hermione_main                                                                                                                                                                                   #HERMIONE
                    with d3                                                                                                                                                                                                                        #HERMIONE
                    $ h_body = "03_hp/13_hermione_main/body_128.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
                    show screen hermione_main                                                                                                                                                                                 #HERMIONE
                    with d3       
                    her "Их руки были под моей юбкой, под моей блузкой..."
                    her "И потом моё дыхание участилось..."
                    hide screen hermione_main                                                                                                                                                                                   #HERMIONE
                    with d3                                                                                                                                                                                                                        #HERMIONE
                    $ h_body = "03_hp/13_hermione_main/body_121.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
                    show screen hermione_main                                                                                                                                                                                 #HERMIONE
                    with d3       
                    her "И один из них засунул свои пальчики ко мне в рот..."
                    her "И их прикосновения были такими... ненасытными..." 
                    her "У меня аж закружилась голова..."
                    hide screen hermione_main                                                                                                                                                                                   #HERMIONE
                    with d3                                                                                                                                                                                                                        #HERMIONE
                    $ h_body = "03_hp/13_hermione_main/body_128.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
                    show screen hermione_main                                                                                                                                                                                 #HERMIONE
                    with d3       
                    her "Это было очень возбуждающе, Сэр."
                    m "Очень хорого, Мисс Грейнджер. Просто прекрасно."
                    
                    
                if one_out_of_three == 2: ### EVENT (B)
                    hide screen hermione_main                                                                                                                                                                                   #HERMIONE
                    with d3                                                                                                                                                                                                                        #HERMIONE
                    $ h_body = "03_hp/13_hermione_main/body_01.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
                    show screen hermione_main                                                                                                                                                                                 #HERMIONE
                    with d3                                                                                                                                                                                                                        #HERMIONE
                    her "Вообще-то коечто необычное произошло сегодня со мной, Сэр..."
                    her "После занятий по Защите от темных чар..."
                    her "Ко мне подошёл кореннастый парень из  \"Пуффендуя\" ..."
                    hide screen hermione_main                                                                                                                                                                                   #HERMIONE
                    with d3                                                                                                                                                                                                                        #HERMIONE
                    $ h_body = "03_hp/13_hermione_main/body_122.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
                    show screen hermione_main                                                                                                                                                                                 #HERMIONE
                    with d3                                                                                                                                                                                                                        #HERMIONE
                    play music "music/(Orchestral) Playful Tension by Shadow16nh.mp3" fadein 1 fadeout 1 # SEX THEME.
                    her "Он рассказал, что до него дошли слухи, что я даю мальчикам трогать себя..."
                    hide screen hermione_main                                                                                                                                                                                   #HERMIONE
                    with d3                                                                                                                                                                                                                        #HERMIONE
                    $ h_body = "03_hp/13_hermione_main/body_128.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
                    show screen hermione_main                                                                                                                                                                                 #HERMIONE
                    with d3                                                                                                                                                                                                                        #HERMIONE
                    her "Обычно,я бы даже ничего не сделала..."
                    her "Но я решила не упускать возможность..."
                    hide screen hermione_main                                                                                                                                                                                   #HERMIONE
                    with d3                                                                                                                                                                                                                        #HERMIONE
                    $ h_body = "03_hp/13_hermione_main/body_78.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
                    show screen hermione_main                                                                                                                                                                                 #HERMIONE
                    with d3                                                                                                                                                                                                                        #HERMIONE
                    her "Я завела парня в тихое место и разрешила ему потрогать себя..."
                    her "Я позволила ему потрогать меня под одеждой..."
                    her "Потом сказала ему потрогать мою грудь..."
                    hide screen hermione_main                                                                                                                                                                                   #HERMIONE
                    with d3                                                                                                                                                                                                                        #HERMIONE
                    $ h_body = "03_hp/13_hermione_main/body_128.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
                    show screen hermione_main                                                                                                                                                                                 #HERMIONE
                    with d3                                                                                                                                                                                                                        #HERMIONE
                    her "Ну в общем как обычно..."
                    m "Отлично, Мисс Грейнджер."
                    
                if one_out_of_three == 3: ### EVENT (C)
                    stop music fadeout 1.0
                    hide screen hermione_main                                                                                                                                                                                   #HERMIONE
                    with d3                                                                                                                                                                                                                        #HERMIONE
                    $ h_xpos=370 #Defines position of the Hermione's full length sprite. (Default 370). (Center: 140)                                                       #HERMIONE
                    $ h_body = "03_hp/13_hermione_main/body_44.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
                    show screen hermione_main                                                                                                                                                                                 #HERMIONE
                    with d3                                                                                                                                                                                                                        #HERMIONE
                    her "Ну..."
                    her "Я сделала то,что вы просили меня сделать, Сэр..."
                    her "Но... в некотором роде... эм.."
                    hide screen hermione_main                                                                                                                                                                                   #HERMIONE
                    with d3                                                                                                                                                                                                                        #HERMIONE
                    $ h_body = "03_hp/13_hermione_main/body_78.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
                    show screen hermione_main                                                                                                                                                                                 #HERMIONE
                    with d3                                                                                                                                                                                                                        #HERMIONE
                    her "Но в некотором роде,это задание перешло в кое что другое..."
                    play music "music/(Orchestral) Playful Tension by Shadow16nh.mp3" fadein 1 fadeout 1 # SEX THEME.
                    m "Хм?"
                    hide screen hermione_main                                                                                                                                                                                   #HERMIONE
                    with d3                                                                                                                                                                                                                        #HERMIONE
                    $ h_body = "03_hp/13_hermione_main/body_44.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
                    show screen hermione_main                                                                                                                                                                                 #HERMIONE
                    with d3                                                                                                                                                                                                                        #HERMIONE
                    her "Хм..."
                    her "Ну в общем... я была поймана за тем,что давала поторагать свою грудь одному мальчику..."
                    m "Ты была поймана? Учителем?"
                    hide screen hermione_main                                                                                                                                                                                   #HERMIONE
                    with d3                                                                                                                                                                                                                        #HERMIONE
                    $ h_body = "03_hp/13_hermione_main/body_45.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
                    show screen hermione_main                                                                                                                                                                                 #HERMIONE
                    with d3                                                                                                                                                                                                                        #HERMIONE
                    her "Нет, Сэр..."
                    hide screen hermione_main                                                                                                                                                                                   #HERMIONE
                    with d3                                                                                                                                                                                                                        #HERMIONE
                    $ h_body = "03_hp/13_hermione_main/body_46.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
                    show screen hermione_main                                                                                                                                                                                 #HERMIONE
                    with d3                                                                                                                                                                                                                        #HERMIONE
                    her "Девушкой этого парня..."
                    m "Интересно..."
                    hide screen hermione_main                                                                                                                                                                                   #HERMIONE
                    with d3                                                                                                                                                                                                                        #HERMIONE
                    $ h_body = "03_hp/13_hermione_main/body_117.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
                    show screen hermione_main                                                                                                                                                                                 #HERMIONE
                    with d3                                                                                                                                                                                                                        #HERMIONE
                    her "Сначала, она была зла на него..."
                    hide screen hermione_main                                                                                                                                                                                   #HERMIONE
                    with d3                                                                                                                                                                                                                        #HERMIONE
                    $ h_body = "03_hp/13_hermione_main/body_122.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
                    show screen hermione_main                                                                                                                                                                                 #HERMIONE
                    with d3                                                                                                                                                                                                                        #HERMIONE
                    her "Но потом..."
                    hide screen hermione_main                                                                                                                                                                                   #HERMIONE
                    with d3                                                                                                                                                                                                                        #HERMIONE
                    $ h_body = "03_hp/13_hermione_main/body_124.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
                    show screen hermione_main                                                                                                                                                                                 #HERMIONE
                    with d3                                                                                                                                                                                                                        #HERMIONE
                    her "Эмм... Она начала трогать мою грудь..."
                    hide screen hermione_main                                                                                                                                                                                   #HERMIONE
                    with d3                                                                                                                                                                                                                        #HERMIONE
                    $ h_body = "03_hp/13_hermione_main/body_111.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
                    show screen hermione_main                                                                                                                                                                                 #HERMIONE
                    with d3                                                                                                                                                                                                                        #HERMIONE
                    her "Точно так же как минуту назад меня трогал её парень..."
                    her "Затем она повернулась к нему и сказала..."
                    hide screen hermione_main                                                                                                                                                                                   #HERMIONE
                    with d3                                                                                                                                                                                                                        #HERMIONE
                    $ h_body = "03_hp/13_hermione_main/body_16.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
                    show screen hermione_main                                                                                                                                                                                 #HERMIONE
                    with d3                                                                                                                                                                                                                        #HERMIONE
                    her "\"Я люблю тебя, дорогой, И хочу разделить с тобой всё...\""
                    her "\"...включая твоих шлюх.\""
                    hide screen hermione_main                                                                                                                                                                                   #HERMIONE
                    with d3                                                                                                                                                                                                                        #HERMIONE
                    $ h_body = "03_hp/13_hermione_main/body_117.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
                    show screen hermione_main                                                                                                                                                                                 #HERMIONE
                    with d3                                                                                                                                                                                                                        #HERMIONE
                    her "Я была возмущена тем,что она назвала меня шлюхой..."
                    hide screen hermione_main                                                                                                                                                                                   #HERMIONE
                    with d3                                                                                                                                                                                                                        #HERMIONE
                    $ h_body = "03_hp/13_hermione_main/body_06.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
                    show screen hermione_main                                                                                                                                                                                 #HERMIONE
                    with d3                                                                                                                                                                                                                        #HERMIONE
                    her "Но это был такой милый и романтический жест..."
                    her "Вы согласны со мной, Сэр?"
                    m "Абсолютно..."
                    m "Вот что значит настоящая любовь {size=+5} должна {/size} проходить через всё."
                    m "И что же случилось потом?"
                    hide screen hermione_main                                                                                                                                                                                   #HERMIONE
                    with d3                                                                                                                                                                                                                        #HERMIONE
                    $ h_body = "03_hp/13_hermione_main/body_24.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
                    show screen hermione_main                                                                                                                                                                                 #HERMIONE
                    with d3                                                                                                                                                                                                                        #HERMIONE
                    her "Эм... Он поцеловались, конечно же..."
                    hide screen hermione_main                                                                                                                                                                                   #HERMIONE
                    with d3                                                                                                                                                                                                                        #HERMIONE
                    $ h_body = "03_hp/13_hermione_main/body_44.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
                    show screen hermione_main                                                                                                                                                                                 #HERMIONE
                    with d3                                                                                                                                                                                                                        #HERMIONE
                    her "И парень начал трогать меня снова..."
                    hide screen hermione_main                                                                                                                                                                                   #HERMIONE
                    with d3                                                                                                                                                                                                                        #HERMIONE
                    $ h_body = "03_hp/13_hermione_main/body_29.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
                    show screen hermione_main                                                                                                                                                                                 #HERMIONE
                    with d3                                                                                                                                                                                                                        #HERMIONE
                    her "И потом он трогал её и она трогала его..."
                    her "И они целовались..."
                    her "Я почувствовала себя третьей лишней и просто решила тихо удалиться......"
                    m "Ясно..."
                    

    $ gryffindor +=25
    m " \"Гриффиндор\" получает 25 очков!"
    her "Спасибо, сэр."
    
    hide screen bld1
    hide screen hermione_main
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



    $ touched_by_boy = True #Makes sure that Public favours do not get locked after reaching Whoring level 05.
    
    call music_block
    
    $ request_10_points += 1 
    $ request_10 = False 
    $ hermione_sleeping = True
    return