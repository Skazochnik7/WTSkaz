###################REQUEST_22 (Level 06) (55 pt.) (Blowjob). 
label new_request_22: #LV.6 (Whoring = 15 - 17)
    $herView.hideQQ()
    if IsFirstRun():
#    if request_22_points == 0:
        m "{size=-4}(Попросить девчонку сделать мне минет?){/size}"
    else:
        m "{size=-4}(Попросить девчонку сделать мне еще один минет?){/size}"
    $ menu_x = 0.5 #Default position of the menu (0.5). Version B is $ menu_x = 0.2
    menu:
        "\"(Да! Сделаем это!)\"":
            show screen blktone
            with d3
            pass
        "\"(Не сейчас)\"":
            $event.NotFinished()
            jump new_personal_request
            
 
    $ pos = POS_140
    $ herView.data().saveState()

    if IsFirstRun(): # FIRST EVENT <============================================================== EVENT 01
#    if request_22_points == 0: # FIRST EVENT <============================================================== EVENT 01
        m "Мисс Грейнджер?"
        $herView.hideshowQQ( "body_01.png", pos )
        her "Да, профессор?"
        m "Сегодня я планирую дать \"Гриффиндору\" 55 очков..."
        m "Если вы у меня отсосете..."
        if hermi.whoring <=14: # LEVEL 05
            jump too_much
        $herView.hideshowQQ( "body_87.png", pos )
        her "Ох..."
        $herView.hideshowQQ( "body_124.png", pos )
        her "Хорошо."
        m "Серьезно? Вот так сразу?"
        $herView.hideshowQQ( "body_118.png", pos )
        her "Да, я знаю, что должна чувствовать себя неловко..."
        $herView.hideshowQQ( "body_117.png", pos )
        her "Но, почему то я чувствую себя нормально..."
        $herView.hideshowQQ( "body_124.png", pos )
        her "думаю, я просто рада, что могу помочь Гриффиндру...."
        $herView.hideshowQQ( "body_120.png", pos )
        her "И если я должна сделать вам минет, то пусть так и будет..."
        m "Ну что же, хорошо."
        $herView.hideshowQQ( "body_118.png", pos )
        her "Хотя теперь, когда я говорю это вслух, мне это не нравится!.."
        m "Слишком поздно, ты уже сказала \"Да\"!"
        $herView.hideshowQQ( "body_24.png", pos )
        her "Я знаю..."

        label blowjob_jumping:
        # BLOWJOB
        play music "music/(Orchestral) Playful Tension by Shadow16nh.mp3" fadein 1 fadeout 1 # SEX THEME.
        $herView.hideQ()
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
        if (event.Name=="new_request_08") and end.IsEnding(const_ENDING_STRONG_GIRL):
            $music.Start("Supergirl")                                   
            $ hermione_chibi_xpos = -150 #-185 behind the desk. (Also 5 is something).
            $ hermione_chibi_ypos = 10
            $ h_c_u_pic = "hand_ani"
            show screen h_c_u
            hide screen g_c_u
            with d3
            g4 "О, твою мать, что ты делаешь?!.. Ты мне сейчас оторвешь яйца, девчонка!"
            $ posHead = gMakePos( 390, 235 )
            $herViewHead.showQ( "body_100.png", posHead )
            her2 "Я доставляю себе удовольствие, сэр, как вы велели."
            $herViewHead.hideQ()
            m "Что за удовольствие такое? УЙй!.."
            $herViewHead.showQ( "body_47.png", posHead )
            her2 "О, для меня держать вас за яйца - это очень большое удовольствие, сэр!"
            $herViewHead.hideQ()
            m "Отпусти!"
            $herViewHead.showQ( "body_47.png", posHead )
            her "Наказание уже закончилось, профессор?"
            $herViewHead.hideQ()
            g4 "Ты забываешься, девчонка! Ты хоть понимаешь, с кем разговариваешь?!"
            $herViewHead.showQ( "body_206.png", posHead )
            her2 "Я разговариваю с парнем, чьи яйца у меня в руке..."
            her2 "Ох, профессор, когда я понимаю, что у моего любимого факультета вычтут очки..."
            her2 "У меня невольно все начинает трястись... и сжиматься тоже."
            $herViewHead.hideQ()
            g4 "О-о-о-о! Перестань, перестань сейчас же!"
            $herViewHead.showQ( "body_47.png", posHead )
            her2 "От расстройства я готова просто рвать и оторва... и потом метать, сэр!"
            $herViewHead.hideQ()
            g4 "Отпусти, мать твою! Я не собирался вычитать у тебя очки, просто хотел напугать, чтобы ты навсегда запомнила!"
            $current_payout=0
            $herViewHead.showQ( "body_68.png", posHead )
            her "О, сэр... Вы так добры... А я подумала..."
            $herViewHead.hideQ()
            "> Гермиона перестает сжимать ваши яйца и начинает нежно их массировать."
            $herViewHead.showQ( "body_122.png", posHead )
            her2 "Пожалуйста, простите меня, я просто очень расстроилась." 
            her2 "Я сейчас все исправлю, вы получите лучший минет в жизни!"
            $herViewHead.hideQ()
            m "Сомневаюсь! Ты - мелкая..."
            hide screen h_c_u   # SUCKING
            show screen g_c_u # SUCKING
            with d3
            her "*Хлюп* *Чавк!* *Хлюп!*"
            m "О, да-а..."
            her "*Чавк!* *Чавк!* *Хлюп!*"
            $herViewHead.showQ( "body_55.png", posHead )
            her "Ну как вам, сэр?"
            $herViewHead.hideQ()
            m "Для начала неплохо, девочка..."
            $music()
            play music "music/(Orchestral) Playful Tension by Shadow16nh.mp3" fadein 1 fadeout 1 # SEX THEME.

        m "Теперь попробуй глубже..."
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
                
                $herViewHead.showQ( "body_118.png", posHead )
                her "О... да..."
                her "Мы остаемся активны, но..."
                $herViewHead.hideQ()
                hide screen h_c_u   # SUCKING
                show screen g_c_u # SUCKING
                with d3                      #  SUCKING
                her "*Чавк!* *Кулдык!*"
                show screen h_c_u   # NOT SUCKING
                hide screen g_c_u # NOT SUCKING
                with d3                      #  NOT SUCKING
                $herViewHead.showQ( "body_122.png", posHead )
                her2 "Но мы не получаем той популярности и поддержки, какой хотелось бы..."
                hide screen h_c_u   # SUCKING
                show screen g_c_u # SUCKING
                with d3                      #  SUCKING
                $herViewHead.hideQ()
                her "*Чавк!* *Хлюп!* *Хлюп!*"
                m "Охх... Это отлично..."
                her "*Чавк!* *Чавк!* *Чавк!*"
                m "Хмм..."
                m "Итак, вы позволили себе продавать себя за очки для факультета, давать мне играть с вашими сисками и прочее......"
                her "*Кулдык!* *Хлюп!* *Чавк!*"
                m "А потом осуждаете то же самое перед студентами своего факультета."
                her "*Чавк!* *Чавк!* *Хлюп!*"
                m "Извращенка и лицемерка."
                her "*Хлюп..."
                show screen h_c_u   # NOT SUCKING
                hide screen g_c_u # NOT SUCKING
                with d3                      #  NOT SUCKING
                $herViewHead.showQ( "body_117.png", posHead )
                her "Непосредственно услуги - это не то, с чем мы боремся, сэр."
                $herViewHead.hideQ()
                m "Что ты имеешь в виду?"
                $herViewHead.showQ( "body_16.png", posHead )
                her2 "\"ОЗМП\" о половом равенстве."
                her2 "Мы не против обмена очков на услуги для учителей..."
                her2 "Мы против полового неравенства, которое подразумевает под собой этого рода услуги за очки..."
                $herViewHead.hideQ()
                m "Хмм..."
                m "Этот разговор начинает меня утомлять..."
                m "Пососи мой член еще немного, прежде чем мы продолжим."
                $herViewHead.showQ( "body_121.png", posHead )
                her "Конечно, сэр."
                hide screen h_c_u   # SUCKING
                show screen g_c_u # SUCKING
                with d3                      #  SUCKING
                $herViewHead.hideQ()
                her "*Кулдык!* *Хлюп!* *Хлюп!*"
                m "Да, намного лучше..."
                m "Но вы по-прежнему против подобных услуг, верно?"
                her "*Хлюп..."
                show screen h_c_u   # NOT SUCKING
                hide screen g_c_u # NOT SUCKING
                with d3                      #  NOT SUCKING
                $herViewHead.showQ( "body_120.png", posHead )
                her2 "Да, это не одобряется..."
                $herViewHead.hideQ()
                m "И все же, ты - преступница."
                $herViewHead.showQ( "body_120.png", posHead )
                her "Но разве у меня был выбор??"
                her2 "Я была в очень трудном положении..."
                $herViewHead.hideQ()
                m "Мой член, девочка."
                $herViewHead.showQ( "body_120.png", posHead )
                her "Верно, извините..."
                hide screen h_c_u   # SUCKING
                show screen g_c_u # SUCKING
                with d3                      #  SUCKING
                $herViewHead.hideQ()
                her "*Чавк!* *Хлюп!* *Кулдык!*"
                her "*Чавк..."
                show screen h_c_u   # NOT SUCKING
                hide screen g_c_u # NOT SUCKING
                with d3                      #  NOT SUCKING
                $herViewHead.showQ( "body_117.png", posHead )
                her2 "У нас будет встреча сразу после всего этого."
                her2 "Я должна буду выступить с речью в этой форме, грязной, в пятнах."
                her2 "Я чувствую себя ужасно, но я должна буду сделать это..."
                $herViewHead.hideQ()
                m "Попробуй просто получать удовольствие..."
                $herViewHead.showQ( "body_118.png", posHead )
                her "Хорошо..."
                $herViewHead.hideQ()
                m "Просто признай это."
                $herViewHead.showQ( "body_117.png", posHead )
                her "..............."
                $herViewHead.hideQ()
                m "Да, я знал, что тебе это нравится, ведь ты - извращенка."
                $herViewHead.showQ( "body_118.png", posHead )
                her2 "Я думаю, это будет неловко и захватывающе одновременно..."
                her2 "И из-за этого я чувствую себя еще хуже."
                $herViewHead.hideQ()
                m "Бедняжка."
                m "Положи член обратно в рот."
                $herViewHead.showQ( "body_117.png", posHead )
                her "Да, сэр."
                $herViewHead.hideQ()
                hide screen h_c_u   # SUCKING
                show screen g_c_u # SUCKING
                with d3                      #  SUCKING
                

            "\"Твои родители должны гордиться тобой...\"":
                her "*Чавк..."
                $ hermione_chibi_xpos = -150 #-185 behind the desk. (Also 5 is something).
                $ hermione_chibi_ypos = 10
                $ h_c_u_pic = "hand_ani"
                show screen h_c_u
                hide screen g_c_u
                with d3
                $herViewHead.showQ( "body_75.png", posHead )
                her "Да, я думаю, так и есть..."
                $herViewHead.showQ( "body_74.png", posHead )
                her2 "Я отличная студентка, не смотря на то, что родилась в семье магглов..."
                $herViewHead.showQ( "body_117.png", posHead )
                her2 "Хотя сначала они хотели отправить меня в \"Богус\", школу-интернат."
                $herViewHead.showQ( "body_74.png", posHead )
                her2 "Потребовалось некоторое усилие, чтобы убедить их в том, что \"Хогвартс\" - респектабельное учреждение..."
                $herViewHead.hideQ()
                m "Да, действительно респектабельное учреждение."
                m "Положи член обратно в рот, девочка."
                hide screen h_c_u   # SUCKING
                show screen g_c_u # SUCKING
                with d3                      #  SUCKING
                her "*Чавк!* *Хлюп!* *Кулдык!*"
                $herViewHead.hideQ()
                m "Да, просто подержи его там некоторое время..."
                her "*Чавк!* *Хлюп!* *Хлюп!*"
                $herViewHead.hideQ()
                m "Хорошо, хорошо..."
                m "Итак, что сказали бы ваши родители, если бы увидели вас сейчас?"
                her "*Чавк..."
                show screen h_c_u   # NOT SUCKING
                hide screen g_c_u # NOT SUCKING
                with d3                      #  NOT SUCKING
                $herViewHead.showQ( "body_87.png", posHead )
                her "Конечно же, они бы не поняли меня..."
                her "Но меня это не волнует."
                $herViewHead.showQ( "body_120.png", posHead )
                her2 "Я не боюсь \"грязной работы\" и делаю то, что необходимо."
                $herViewHead.hideQ()
                m "Ты немного непослушная, не так ли?"
                $herViewHead.showQ( "body_122.png", posHead )
                her "Хмм, я думаю - я такая."
                $herViewHead.hideQ()
                m "Тогда возвращайся к минету. Покажи своим родителям, какая ты."
                hide screen h_c_u   # SUCKING
                show screen g_c_u # SUCKING
                with d3                      #  SUCKING
                her "*Чавк!* *Чавк!* *Чавк!*"
                

            "\"Расскажи мне о факультете \"Гриффиндор\"\"":
                her "*Чавк..."
                $ hermione_chibi_xpos = -150 #-185 behind the desk. (Also 5 is something).
                $ hermione_chibi_ypos = 10
                $ h_c_u_pic = "hand_ani"
                show screen h_c_u
                hide screen g_c_u
                with d3
                $herViewHead.showQ( "body_13.png", posHead )
                her "Разве я могу вам рассказать что-то, чего вы еще не знаете?"
                $herViewHead.hideQ()
                m "Да... Эмм... конечно, я знаю все."
                m "Но я хочу посмотреть, как много знаешь ты!"
                m "Чтобы проверить уровень твоих знаний."
                show screen blktone
                with d3
                ">Как только вы говорите о \"Проверке\", в глазах Гермионы появляется волнение"
                hide screen blktone
                with d3
                $herViewHead.showQ( "body_80.png", posHead )
                her "Хорошо, но мне нужно немного времени, чтобы собраться с мыслями..."
                $herViewHead.hideQ()
                hide screen h_c_u   # SUCKING
                show screen g_c_u # SUCKING
                with d3                      #  SUCKING
                her "*Чавк!* *Чавк!* *Хлюп!*"
                m "Ох, конечно, готовься столько, сколько требуется."
                her "*Чавк!* *Хлюп!* *Чавк!*"
                her "*Хлюп..."
                show screen h_c_u   # NOT SUCKING
                hide screen g_c_u # NOT SUCKING
                with d3                      #  NOT SUCKING
                hide screen ctc
                $herViewHead.showQ( "body_87.png", posHead )
                her2 "Факультет \"Гриффиндор\" был основан Годриком Гриффиндором, отсюда и название."
                her2 "На гербе \"Гриффиндора\" - Лев..."
                $herViewHead.showQ( "body_127.png", posHead )
                her "Красный и золотой - цвета герба."
                $herViewHead.hideQ()
                hide screen h_c_u   # SUCKING
                show screen g_c_u # SUCKING
                with d3                      #  SUCKING 
                her "*Хлюп!* *Чавк!* *Чавк!*"
                show screen h_c_u   # NOT SUCKING
                hide screen g_c_u # NOT SUCKING
                with d3                      #  NOT SUCKING
                $herViewHead.showQ( "body_127.png", posHead )
                her2 "Профессор Минерва Макгонагалл - глава факультета."
                her2 "\"Гриффиндор\" олицетворяет мужество..."
                her2 "А также смелость, храбрость и благородство..."
                her2 "И, таким образом, его члены, как правило, являются смелыми, но безрассудными..."
                $herViewHead.hideQ()
                hide screen h_c_u   # SUCKING
                show screen g_c_u # SUCKING
                with d3                      #  SUCKING
                her "*Чавк!* *Чавк!* *Чавк!*"
                show screen h_c_u   # NOT SUCKING
                hide screen g_c_u # NOT SUCKING
                with d3                      #  NOT SUCKING
                $herViewHead.showQ( "body_127.png", posHead )
                her2 "\"Гриффиндору\" соответствует стихия огня..."
                her2 "По этой причине и были выбраны красный и золотой цвета."
                $herViewHead.hideQ()
                hide screen h_c_u   # SUCKING
                show screen g_c_u # SUCKING
                with d3                      #  SUCKING
                her "*Чавк!* *Хлюп!* *Чавк!*"
                m "Хмм..."
                m "Ну, я думаю, что могу немного высмеять тебя..."
                $herViewHead.hideQ()
                her "*Чавк??*"
                m "\"Гриффиндору\" соответствует смелость, храбрость и благородство..."
                m "Но тем не менее, ты - шлюха..."
                show screen h_c_u   # NOT SUCKING
                hide screen g_c_u # NOT SUCKING
                with d3                      #  NOT SUCKING
                $herViewHead.showQ( "body_86.png", posHead )
                her "Профессор!"
                $herViewHead.hideQ()
                $herViewHead.hideQ()
                m "Но, честно говоря..."
                m "\"смелость, благородство, храбрость, безрассудство\"..."
                m "это именно про тебя..."
                $herViewHead.showQ( "body_45.png", posHead )
                her "Сэр..."
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
        her "*Чавк..."
        show screen h_c_u   # NOT SUCKING
        hide screen g_c_u # NOT SUCKING
        with d3                      #  NOT SUCKING
        $herViewHead.showQ( "body_87.png", posHead )
        her "Сэр... я... шлюха."
        $herViewHead.hideQ()
        m "Что?"
        hide screen h_c_u   # SUCKING
        show screen g_c_u # SUCKING
        with d3                      #  SUCKING
        her "*Чавк-Чавк-Чавк!*"
        show screen h_c_u   # NOT SUCKING
        hide screen g_c_u # NOT SUCKING
        with d3                      #  NOT SUCKING
        $herViewHead.showQ( "body_117.png", posHead )
        her2 "Я действительно шлюха, я обожаю сосать ваш член..."
        $herViewHead.hideQ()
        m "Ох, говори больше об этом!"
        hide screen h_c_u   # SUCKING
        show screen g_c_u # SUCKING
        with d3                      #  SUCKING
        her "*Чавк!* *Хлюп!* *Чавк!*"
        show screen h_c_u   # NOT SUCKING
        hide screen g_c_u # NOT SUCKING
        with d3                      #  NOT SUCKING
        $herViewHead.showQ( "body_121.png", posHead )
        her "Пожалуйста, сэр, кончайте для меня! "
        $herViewHead.hideQ()
        with hpunch
        g4 "АХХХ, ты маленькая шл!!!..."
        g4 "{size=-4}(Почти кончаю. Должен ли я предупредить её?){/size}"
        menu:
            m "..."
            "- Предупредить её -":
                $herViewHead.showQ( "body_121.png", posHead )
                her "Да, я люблю сосать..."
                $herViewHead.hideQ()
                g4 "Скорее, девочка, я почти кончил!"
                $herViewHead.showQ( "body_18.png", posHead )
                her "!!!"
                $herViewHead.hideQ()
                show screen ctc
                pause
                show screen blkfade
                with d3
                $ g_c_u_pic = "cum_in_mouth_ani"
                hide screen h_c_u   # SUCKING
                show screen g_c_u # SUCKING
                with d3                      #  SUCKING
                ">Гермиона быстро кладет член в рот и продолжает сосать с еще большей страстью."
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
                m "Что ж, я думаю, это все..."
                show screen h_c_u   # NOT SUCKING
                hide screen g_c_u # NOT SUCKING
                with d3                      #  NOT SUCKING
                $herViewHead.showQ( "body_126.png", posHead )
                her ".............."
                $herViewHead.hideQ()
                m "Ты в порядке там, девочка?"
                $herViewHead.showQ( "body_123.png", posHead )
                her "Да, сэр..."
                her "Это было слишком..."
                $herViewHead.hideQ()
                m "Тебе удалось проглотить это все."
                $herViewHead.showQ( "body_123.png", posHead )
                her "Да... Я думала, что задохнусь..."
                her2 "Но я дала себе обещание, что с вашего члена не упадет ни капли!"
                $herViewHead.hideQ()
                m "Хорошая девочка."
                $herViewHead.showQ( "body_123.png", posHead )
                her "Спасибо, сэр."
                her "Но, все-таки, это было слишком..."
                $herViewHead.showQ( "body_121.png", posHead )
                her "Мне кажется, что я только что поела.."
                her "Мой желудок полон..."
                $herViewHead.hideQ()
                g9 "Да, я накормил тебя моей спермой!"
                if daytime:
                    $herViewHead.showQ( "body_121.png", posHead )
                    her2 "Я думаю, что сегодня можно пойти на занятия без обеда."
                else:
                    $herViewHead.showQ( "body_121.png", posHead )
                    her2 "Да, я думаю, сегодня можно пропустить ужин."
                $herViewHead.showQ( "body_122.png", posHead )
                her "Могу я получить оплату?"
                $herViewHead.hideQ()
                show screen ctc
                pause
                hide screen ctc
                show screen blkfade
                with d3
            "- Не беспокоиться -":
                $herViewHead.showQ( "body_121.png", posHead )
                her "Да, я люблю сосать..."
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
                $herViewHead.showQ( "body_48.png", posHead )
                her "!!?"
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
                #$herViewHead.data().addItemKey( 'sperm', CharacterExItem( herViewHead.mMiscFolder, 'sperm_04.png', G_Z_FACE + 1 ) )
                $herViewHead.data().addItem( 'item_sperm', '04' )

                $herViewHead.showQ( "body_48.png", posHead )
                her "Профессор..."
                $herViewHead.hideQ()
                g4 "Не двигайся, девочка."
                g4 "Да, просто оставайся на месте."
                g4 "АХХХ, ты маленькая шлюха, из-за тебя я кончаю сильнее, девочка!"
                $herViewHead.showQ( "body_21.png", posHead )
                her ".............."
                $herViewHead.hideQ()
                m "Вот так..."
                $ g_c_u_pic = "cum_on_face_blink_ani"
                $herViewHead.showQ( "body_33.png", posHead )
                her ".............."
                $herViewHead.hideQ()
                m "Хорошо, я закончил..."
                $herViewHead.showQ( "body_31.png", posHead )
                her "................."
                if daytime:
                    her "Мои занятия скоро начнутся..."
                else:
                    pass
                $herViewHead.hideQ()
                m "Просто протри лицо, и все будет в порядке..."
                $herViewHead.showQ( "body_31.png", posHead )
                her "............"
                $herViewHead.hideQ()
                m "Ведь ты не хочешь, чтобы..."
                $herViewHead.showQ( "body_34.png", posHead )
                her "Хм?"
                $herViewHead.hideQ()
                m "Все..."
                m "Видели, какая ты маленькая шлюха!"
                $herViewHead.showQ( "body_34.png", posHead )
                her "Конечно нет, сэр!"
                $herViewHead.hideQ()
                show screen ctc
                pause
                hide screen ctc
                show screen blkfade
                with d3
                stop music fadeout 1.0
                if daytime:
                    m "Тебе следует поторопиться, чтобы не опоздать на занятия..."
                else:
                    m "Уже поздно..."
                    $herViewHead.showQ( "body_34.png", posHead )
                    her "Да..."
                $herViewHead.showQ( "body_44.png", posHead )
                her "Могу я получить оплату?"
                $herViewHead.hideQ()
                #$herViewHead.data().addItemKey( 'sperm_after', CharacterExItem( herViewHead.mMiscFolder, 'sperm_00_after.png', G_Z_FACE + 2 ) )
                $herViewHead.data().addItem( 'item_sperm_dried' )

        
        
    elif IsRunNumber(2): #  <============================================================== EVENT 02
#    elif request_22_points == 1: #  <============================================================== EVENT 02
        m "Мисс Гренджер?"
        $herView.hideshowQQ( "body_01.png", pos )
        her "Сэр?"
        m "Как насчет минета?"
        $herView.hideshowQQ( "body_86.png", pos )
        play music "music/(Orchestral) Playful Tension by Shadow16nh.mp3" fadein 1 fadeout 1 # SEX THEME.
        her "Профессор, как вы можете предлагать такое вашему ученику?!"
        m "Чт...?"
        $herView.hideshowQQ( "body_86.png", pos )
        her "Это недостойно директора!"
        $herView.hideshowQQ( "body_47.png", pos )
        her "Вам должно быть стыдно, сэр!"
        menu:
            m "???"
            "\"Прекрасно. Никаких очков! Уходи!\"":
                play music "music/Chipper Doodle v2.mp3" fadein 1 fadeout 1 # HERMIONE'S THEME.
                $herView.hideshowQQ( "body_24.png", pos )
                her "Сэр, успокойтесь, пожалуйста."
                m "Покиньте кабинет, мисс Грейнджер!"
                $herView.hideshowQQ( "body_24.png", pos )
                her "Cэр, все что я сказала - было не всерьез."
                m "Что?"
            "\"Эм, извините?\"":
                stop music fadeout 1.0
                $herView.hideshowQQ( "body_06.png", pos )
                her "*хи-хи*"
                m "Хмм?"
                $herView.hideshowQQ( "body_24.png", pos )
                play music "music/Chipper Doodle v2.mp3" fadein 1 fadeout 1 # HERMIONE'S THEME.
                her "Поняла... cэр."
                m "Что?"
        $herView.hideshowQQ( "body_45.png", pos )
        her "Ну, так много произошло за последнее время..."
        her2 "У меня было так много новых впечатлений, что я изменила свой взгляд на некоторые вещи..."
        her2 "Так что я просто пыталась представить себе, как \"я в прошлом\" отреагировала бы на это."
        m "Итак..."
        g4 "Вы плохо относитесь ко мне?"
        $herView.hideshowQQ( "body_34.png", pos )
        her "Хм... мне жаль сэр, я не это имела в виду..."
        g4 "Ты плохая девочка, ты должна быть наказана!"
        g9 "Я накажу тебя своим членом!"
        $herView.hideshowQQ( "body_34.png", pos )
        her "..............................."

        jump blowjob_jumping
  
  
    elif IsRunNumberOrMore(3): # <============================================================== EVENT 03
#    elif request_22_points >= 2: # <============================================================== EVENT 03
        play music "music/(Orchestral) Playful Tension by Shadow16nh.mp3" fadein 1 fadeout 1 # SEX THEME.
        m "Соси мой член, девочка."
        $herView.hideshowQQ( "body_45.png", pos )
        her "Конечно..."
        # Sucking.
        
        $herView.hideQ()
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
        
        $ posHead = gMakePos( 390, 235 )

        $herViewHead.showQ( "body_48.png", posHead )
        her "(Профессор, что мне делать?)"
        $herViewHead.hideQ()
        m "Просто продолжай сосать мой член, девочка. Это тебя не касается."
        sna "Альбус? Ты там? Мне нужно поговорить с тобой."
        $herViewHead.showQ( "body_117.png", posHead )
        her "(Это профессор Снейп!)"
        her2 "(Сэр, пожалуйста, скажите, чтобы он ушел, я прошу вас!)"
        $herViewHead.hideQ()
        menu:
            m "..."
            "\"Пожалуйста, заходите, Северус.\"":
                $ hermi.liking -= 30
                $herViewHead.showQ( "body_76.png", posHead )
                stop music fadeout 1.0
                her "(Сэр, нет!)"
                $herViewHead.hideQ()
                show screen blktone
                with d3
                with hpunch
                ">Гермиона крепко сжимает ваши яйца."
                hide screen blktone
                with d3
                g4 "ОЙ!"
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
                sna "Слушай, надо кое-что обсудить..."
                $ s_sprite = "03_hp/10_snape_main/snape_05.png" # SNAPE
                show screen s_head2                                                          # SNAPE
                sna "Хмм...?"
                sna "Джинни? Ты в порядке??"
                hide screen s_head2
                her "{size=-4}(Джинни!!? И она здесь?!){/size}"
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
                sna "Да. Девчонку Грейнджер."
                hide screen s_head2
                her "{size=-4}(*Чавк...!* *Кулдык...!* *Хлюп...!*){/size}"
                m "Ох... Что с ней?"
                $ s_sprite = "03_hp/10_snape_main/snape_04.png" # SNAPE
                show screen s_head2                                                          # SNAPE
                sna2 "Вы обещали присматривать за маленькой ведьмой."
                hide screen s_head2
                her "{size=-4}(*Чавк...* *Чавк...* *Хлюп...*){/size}"
                $ s_sprite = "03_hp/10_snape_main/snape_04.png" # SNAPE
                show screen s_head2                                                          # SNAPE
                sna "Но она по-прежнему как заноза в моей заднице."
                sna "Ее поведение изменилось..."
                $ s_sprite = "03_hp/10_snape_main/snape_03.png" # SNAPE
                show screen s_head2                                                          # SNAPE
                sna2 "Но проблем не стало меньше..."
                hide screen s_head2
                m "Я понимаю... ах..."
                $ s_sprite = "03_hp/10_snape_main/snape_10.png" # SNAPE
                show screen s_head2                                                          # SNAPE
                sna "Эта девчонка сводит меня с ума!"
                hide screen s_head2
                g4 "Да, она сводит меня с ума и меня, а... ах..."
                her "{size=-4}(*Чавк...* *Чавк...* *Хлюп...*){/size}"
                $ s_sprite = "03_hp/10_snape_main/snape_04.png" # SNAPE
                show screen s_head2                                                          # SNAPE
                sna "Будете ли вы присматривать за ней?"
                hide screen s_head2
                m "О, да. Она получит по заслугам."
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
                    sna "И тебе..."
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
                ">Гермиона не сказала ни слова. Она покраснела от смущения и волнения."
                ">Однако, даже растерянная и обиженная, она все еще старательно продолжает отсасывать."
                g4 "(Я почти кончил!)"

                
            "\"Я сейчас занят, Северус.\"":
                $herViewHead.showQ( "body_117.png", posHead )
                her "(Спасибо, сэр.)"
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
                ">Гермиона продложает усердно сосать ваш член"
                ">Ей не хватает опыта, но она старается изо всех сил"
                hide screen blktone
                with d3
                m "Да ... Я люблю твой жадный маленький рот, девочка ..."
                her "*Кулдык!* *Кулдык!* *Кулдык!*"
                $ hermione_chibi_xpos = -150 #-185 behind the desk. (Also 5 is something).
                $ hermione_chibi_ypos = 10
                $ h_c_u_pic = "hand_ani" # Not sucking
                show screen h_c_u   # NOT SUCKING
                hide screen g_c_u # NOT SUCKING
                with d3                      #  NOT SUCKING
                $herViewHead.showQ( "body_121.png", posHead )
                her "Сэр?"
                $herViewHead.hideQ()
                m "Хм?"
                $herViewHead.showQ( "body_121.png", posHead )
                her "Вы кончите мне на лицо сегодня?"
                her "Или вы планируете кончить в рот?"
                $herViewHead.hideQ()
                menu:
                    "\"Я планирую забрызгать твое лицо спермой!\"":
                        $herViewHead.showQ( "body_121.png", posHead )
                        her "Я понимаю..."
                        $herViewHead.hideQ()
                        m "Почему ты спрашиваешь?"
                        $herViewHead.showQ( "body_123.png", posHead )
                        her2 "Ох... Я прочитала, что сперма содержит много антиоксидантов."
                        her "Они полезны для кожи..."
                        $herViewHead.hideQ()
                        m "Отлично."
                        m "Возвращайся к работе."
                    "\"Я планирую кончить тебе в рот!\"":
                        $herViewHead.showQ( "body_123.png", posHead )
                        her "Я понимаю..."
                        $herViewHead.hideQ()
                        m "Почему ты спрашиваешь?"
                        $herViewHead.showQ( "body_121.png", posHead )
                        her2 "Ну, я пытаюсь следить за потреблением калорий..."
                        her2 "Мне просто интересно, сколько калорий содержит ваша сперма."
                        her2 "Может, мне стоит пропустить следующий прием пищи..."
                        $herViewHead.hideQ()
                        m "Девочка."
                        $herViewHead.showQ( "body_121.png", posHead )
                        her "Да?"
                        $herViewHead.hideQ()
                        m "Положи член в рот."
                    "\"Я не планирую так далеко вперед,.\"":
                        $herViewHead.showQ( "body_121.png", posHead )
                        her "Я понимаю..."
                        $herViewHead.hideQ()
                        m "Ты не любишь сюрпризы?"
                        $herViewHead.showQ( "body_121.png", posHead )
                        her "На самом деле, не то, что бы не люблю..."
                        her "Скорее, мне нравится планировать все наперед..."
                        $herViewHead.hideQ()
                        m "Ну, некоторые вещи в жизни просто непредсказуемы."
                        m "Существует только один способ узнать наверняка."
                        
                    "\"А что бы ты хотела?\"":
                        $herViewHead.showQ( "body_121.png", posHead )
                        her "Если вы все же разрешите мне выбрать, сэр..."
                        if generating_points == 1:
                            $herViewHead.showQ( "body_123.png", posHead )
                            her2 "Я бы хотела, что бы вы кончили мне на лицо"
                            her2 "Я читала, что это хорошо для кожи"
                        else:
                            $herViewHead.showQ( "body_123.png", posHead )
                            her2 "Я бы хотела, что бы вы кончили мне в рот."
                            her2 "Вы обычно обильно кончаете, и я надеялась пропустить следующий прием пищи..."
                            her2 "И сделать больше домашних заданий."
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
                her "*Чавк?.."
                $ hermione_chibi_xpos = -150 #-185 behind the desk. (Also 5 is something).
                $ hermione_chibi_ypos = 10
                $ h_c_u_pic = "hand_ani" # Not sucking
                show screen h_c_u   # NOT SUCKING
                hide screen g_c_u # NOT SUCKING
                with d3                      #  NOT SUCKING
                $herViewHead.showQ( "body_118.png", posHead )
                her "Хмм..."
                $herViewHead.showQ( "body_117.png", posHead )
                her "Я ем тараканов?"
                $herViewHead.hideQ()
                m "...Что за херня?"
                $herViewHead.showQ( "body_117.png", posHead )
                her "О-они довольно противны, сэр..."
                $herViewHead.hideQ()
                m "Нет, девочка, я имел ввиду что-нибудь грязное!"
                m "И не смей говорить \"грязь\"!"
                m "Я имею в виду, что-нибудь в плане секса!"
                $herViewHead.showQ( "body_118.png", posHead )
                her "Ох... Эмм..."
                $herViewHead.hideQ()
                m "Ох, забудь..."
                $herViewHead.showQ( "body_117.png", posHead )
                her "Эмм... Извините, сэр."
                $herViewHead.hideQ()
                m "Да плевать, соси мой член сильнее."
                $herViewHead.showQ( "body_120.png", posHead )
                her "Конечно сэр."
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
                g4 "Покажи, что ты умеешь...."
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
                g4 "Да, малышка, вот сейчас! Скорей готовься всё проглотить!"
                her "!!!"
                
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
                her "{size=+7}Глап!{/size}"
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
                $herViewHead.showQ( "body_125.png", posHead )
                her "..........................."
                her "................"
                her "........"
                $herViewHead.showQ( "body_126.png", posHead )
                $ renpy.play('sounds/gulp.mp3') #Sound of gulping down a liquid.
                her "*Хлюп!*"
                $herViewHead.showQ( "body_115.png", posHead )
                her "Хлюп-чавк..."
                $herViewHead.hideQ()
                m "Ты в порядке?"
                $herViewHead.showQ( "body_123.png", posHead )
                play music "music/Chipper Doodle v2.mp3" fadein 1 fadeout 1 # HERMIONE'S THEME.
                her "Да, профессор..."
                $herViewHead.hideQ()
                m "Ты не собираешься идти на ужин?"
                $herViewHead.showQ( "body_123.png", posHead )
                her "Видимо, не пойду..."
                her "Вы всегда кончаете так обильно, сэр..."
                $herViewHead.hideQ()
                m "Хех... Ну и кто же виноват в этом??"
                $herViewHead.showQ( "body_123.png", posHead )
                her "............." #Smile.
                her "Могу я получить оплату?"
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
                $herViewHead.showQ( "body_123.png", posHead )
                her "Да, сэр!"
                $herViewHead.hideQ()
                g4 "Тогда получай!"
                
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
                $herViewHead.showQ( "body_48.png", posHead )
                her "!!?"
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
                #$herViewHead.data().addItemKey( 'sperm', CharacterExItem( herViewHead.mMiscFolder, 'sperm_04.png', G_Z_FACE + 1 ) )
                $herViewHead.data().addItem( 'item_sperm', '04' )
                $herViewHead.showQ( "body_48.png", posHead )
                her "Профессор..."
                $herViewHead.hideQ()
                g4 "Всё на твоем грязном лице!"
                $herViewHead.showQ( "body_123.png", posHead )
                her "Аааа!"
                $ g_c_u_pic = "cum_on_face_blink_ani"
                $herViewHead.hideQ()
                m "Ладно, я всё."
                $herViewHead.showQ( "body_123.png", posHead )
                her "...................................."
                $herViewHead.hideQ()
                m "Я сказал - всё, девочка."
                $herViewHead.showQ( "body_123.png", posHead )
                her "Да, я слышала вас, сэр..."
                $herViewHead.hideQ()
                m "Ну и... Ты не собираешься умыться?"
                $herViewHead.showQ( "body_123.png", posHead )
                her "Секундочку..."
                her2 "Я даю своей коже время впитать антиоксиданты..." 
                $herViewHead.hideQ()
                m "Ммм... Вот как, меня это заводит..."
                m "Не торопись, девочка..."
                show screen blkfade
                with d3
                stop music fadeout 1.0 
                ">Минутой позже."
                $herViewHead.data().delItem( 'item_sperm' )
                #$herViewHead.data().addItemKey( 'sperm_after', CharacterExItem( herViewHead.mMiscFolder, 'sperm_00_after.png', G_Z_FACE + 1 ) )
                $herViewHead.data().addItem( 'item_sperm_dried' )
                $herViewHead.showQ( "body_122.png", posHead )
                her "Мне кажется, вам нравится, сэр?"
                $herViewHead.hideQ()
                play music "music/Chipper Doodle v2.mp3" fadein 1 fadeout 1 # HERMIONE'S THEME.
                m "Да, девочка, мне нравится."
                $herViewHead.showQ( "body_123.png", posHead )
                her "Хорошо, так мы можем рассчитаться?"
                $herViewHead.hideQ()
                
                    
                
            
        
    
    $herViewHead.data().delItem( 'item_sperm' )
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
    
    if event.Name=="new_request_08":
        jump new_request_08_finish
    
    m "Да, мисс Грейнджер. 55 очков \"Гриффиндору\"." 
    $ gryffindor +=55
    $herView.showQ( "body_13.png", pos )
    hide screen hermione_01_f #Hermione stands still.
    with d3
    her "Спасибо, сэр..."

    if hermi.whoring <= 17:
        $ hermi.whoring +=1

    
    
#    if request_22_points == 0:
#        $ new_request_22_01 = True #  HEARTS
#    if request_22_points == 1:
#        $ new_request_22_02 = True #  HEARTS
#    if request_22_points >= 2:
#        $ new_request_22_03 = True #  HEARTS

#    $ request_22_points += 1

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
    $SetHearts(GetStage(event._finishCount,1,3,1))
    if daytime:
        $ hermione_takes_classes = True
        jump night_main_menu
    else:
        $ hermione_sleeping = True
        jump day_main_menu            

