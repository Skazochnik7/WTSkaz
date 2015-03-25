
    
    

###################REQUEST_29 (Level 07) (65 pt.) (Sex). #################################################################
label new_request_29: #LV.7 (Whoring = 18 - 20)

    $herView.hideQQ()
    m "{size=-4}(Должен ли я попросить её заняться сексом со мной?){/size}"
    $ menu_x = 0.5 #Default position of the menu (0.5). Version B is $ menu_x = 0.2
    menu:
        "\"(Да, попросить!)\"":
            show screen blktone
            with d3
            pass
        "\"(Не сейчас.)\"":
            $event.NotFinished()
            jump new_personal_request
            
    
    $ pos = POS_140
    $ posHead = gMakePos( 390, 340 )
    $herView.data().saveState()

    if IsFirstRun(): # FIRST EVENT <============================================================== EVENT 01
#    if request_29_points == 0: # FIRST EVENT <============================================================== EVENT 01
        m "Мисс Грейнджер?"
        $herView.hideshowQQ( "body_01.png", pos )
        her "Сэр?"
        m "Я бы хотел купить у вас сегодня..."
        $herView.hideshowQQ( "body_06.png", pos )
        her ".......?"
        m "Как бы помягче выразиться...?"
        $herView.hideshowQQ( "body_129.png", pos )
        her "Занятся сексом, сэр?"
        m "Вообще-то -  да. Но как вы догадались...?"
        if hermi.whoring <=17:
            jump too_much
        $herView.hideshowQQ( "body_128.png", pos )
        her "Не сложно было догадаться..."
        m "Вы не будете возражать?"
        $herView.hideshowQQ( "body_120.png", pos )
        her "Кончено я буду возражать, сэр!"
        her "Я не проститутка!"
        m "Но всё равно сделаете это??"
        $herView.hideshowQQ( "body_127.png", pos )
        her2 "\"Гриффиндор\" снова на грани поражения..."
        her2 "И что, вы думаете, я должна делать?.."
        m "Отлично!"
        $herView.hideQ()
       
        label your_ass:
            
        show screen blkfade 
        with d7
            
        stop music fadeout 1.0
        $herViewHead.showQ( "body_120.png", posHead )
        her "............."
        $herViewHead.showQ( "body_119.png", posHead )
        her "!!!!!!!!!!!!!!!"
        $herViewHead.hideQ()
        m "Раслабься, девочка. Я только снимаю твои трусики."
        $herViewHead.showQ( "body_49.png", posHead )
        her ".............."
        $herViewHead.hideQ()
        m "Ты готова?"
        $herViewHead.showQ( "body_50.png", posHead )
        her "Нет..."
        $herViewHead.hideQ()
        m "Хорошая девочка."
        $ renpy.play('sounds/gltch.mp3')
        with hpunch
        with kissiris
        $herViewHead.showQ( "body_130.png", posHead )
        her2 "Ааааааааааааааайййййй....{image=textheart.png}"
        $herViewHead.hideQ()




        $herView.hideQ()
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
        $herViewHead.showQ( "body_33.png", posHead )
        her "................"
        $herViewHead.hideQ()
        m "Ты как?"
        $herViewHead.showQ( "body_21.png", posHead )
        her "Аа-а... Он такой большой..."
        her "Вы разорвете меня на части, сэр!"
        $herViewHead.hideQ()
        m "Ты что?! Мой член вполне нормальных размеров."
        m "Я не виноват, что твоя киска такая узкая."
        $herViewHead.showQ( "body_33.png", posHead )
        her "......................"
        $herViewHead.hideQ()
        hide screen ctc
        menu:
            "\"Тебе должно быть стыдно за себя!\"":
                $herViewHead.showQ( "body_33.png", posHead )
                her "Мне не стыдно, сэр!"
                her "Я делаю всё это для моего факультета...!"
                her "Чтобы помочь моему...--"
                $herViewHead.showQ( "body_131.png", posHead )
                her "А-а-а..."
                her "Мои однокурсники расчитывают на меня... а-а..."
                $herViewHead.hideQ()
                m "Ты уверена, что это единственная причина?"
                $herViewHead.showQ( "body_33.png", posHead )
                her "Я не знаю..--"
                $herViewHead.showQ( "body_131.png", posHead )
                her2 "А-а..."
                $herViewHead.showQ( "body_118.png", posHead )
                her2 "Я не знаю, что вы имеете ввиду, сэр."
                $herViewHead.hideQ()
                m "Мне кажется, что ты наслаждаешься тем, чем мы с тобой занимаемся."
                $herViewHead.showQ( "body_118.png", posHead )
                her "Нет, это не так, сэр!"
                $herViewHead.hideQ()
                m "Правда?"
                $herViewHead.showQ( "body_33.png", posHead )
                her "......................"
                $herViewHead.hideQ()
                m "И ты говоришь это, когда твоя киска так течет?"
                $herViewHead.showQ( "body_131.png", posHead )
                her "....................а-а.{image=textheart.png}"
                $herViewHead.hideQ()
                m "Признайся, ты наслаждаешься тем, что твой профессор трахает тебя!"
                $herViewHead.showQ( "body_33.png", posHead )
                her "Нет, я не наслаждаюсь!"
                $herViewHead.hideQ()
                m "Упрямая девчонка..."
                $herViewHead.showQ( "body_131.png", posHead )
                her "Ааа...{image=textheart.png}" 
                $herViewHead.hideQ()
            "\"Так... Что нового у тебя?\"":
                $herViewHead.showQ( "body_31.png", posHead )
                her "...Сэр?"
                $herViewHead.hideQ()
                m "Я стараюсь поддержать приятную беседу."
                $herViewHead.showQ( "body_31.png", posHead )
                her "А-а... Но... а..."
                $herViewHead.hideQ()
                m "Как поживают твои родственники?"
                $herViewHead.showQ( "body_34.png", posHead )
                her "Мои родители?"
                $herViewHead.showQ( "body_131.png", posHead )
                her2 "Профессор, пожалуйста, я не могу сейчас говорить..."
                $herViewHead.hideQ()
                m "Почему же? Ты так этим наслаждаешься?"
                $herViewHead.showQ( "body_131.png", posHead )
                her "Я не... ах...{image=textheart.png}"
                $herViewHead.hideQ()
                m "Я думаю, ты кайфуешь от этого."
                $herViewHead.showQ( "body_131.png", posHead )
                her "Я всего лишь делаю это ради очков, сэр..."
                $herViewHead.hideQ()
                m "Ммм, ясно..."
                m "Получается ты - проститутка."
                $herViewHead.showQ( "body_117.png", posHead )
                her "Что?"
                $herViewHead.hideQ()
                m "Я плачу тебе за секс. Как же ты это назовешь?"
                $herViewHead.showQ( "body_118.png", posHead )
                her "..........."
                $herViewHead.showQ( "body_131.png", posHead )
                her "Я не проститутка..."
                $herViewHead.showQ( "body_21.png", posHead )
                her "Почему вы так жестоки со мной, сэр?"
                $herViewHead.hideQ()
                m "Мне кажется, тебе нравится, когда я более жесток с тобой."
                $herViewHead.showQ( "body_67.png", posHead )
                her "Нет!"
                $herViewHead.hideQ()
                m "Правда? Тогда почему твоя киска такая влажная?"
                $herViewHead.showQ( "body_118.png", posHead )
                her "Не из-за этого!"
                $herViewHead.hideQ()
                m "Ну, если ты так настаиваешь..."
                $herViewHead.showQ( "body_131.png", posHead )
                her "А-ах...{image=textheart.png}"
                $herViewHead.showQ( "body_132.png", posHead )
                her "Я ... ах...{image=textheart.png} не проститутка..."            
                $herViewHead.hideQ()
            "\"......................................................\"":
                $herViewHead.showQ( "body_131.png", posHead )
                her "А-ах... ах..."
                $herViewHead.hideQ()
                m "*Дышит всё чаще!*"
                $herViewHead.showQ( "body_131.png", posHead )
                her "Ах... а-ах..."
                $herViewHead.hideQ()
                m "Ох..."
                $herViewHead.showQ( "body_131.png", posHead )
                her "Ах-аа..."
                $herViewHead.hideQ()
                m "......................"
                $herViewHead.showQ( "body_131.png", posHead )
                her "Ах... а..."
                $herViewHead.showQ( "body_31.png", posHead )
                her "Ах... Сэр?"
                $herViewHead.hideQ()
                m "Что такое?"
                $herViewHead.showQ( "body_131.png", posHead )
                her "Ах... Вам.... нравится... это...?"
                $herViewHead.hideQ()
                m "Нравится ли мне долбить узкую и мокрую киску?"
                m "Очень, малышка. А что?"
                $herViewHead.showQ( "body_33.png", posHead )
                her "....................."
                $herViewHead.showQ( "body_131.png", posHead )
                her "Ах... Вы просто так внезапно замолчали..."
                $herViewHead.hideQ()
                m "Просто наслаждаюсь моментом, малышка."
                m "А как тебе ощущения? Ты в порядке?"
                $herViewHead.showQ( "body_131.png", posHead )
                her "А... дааа..."
                $herViewHead.showQ( "body_31.png", posHead )
                her "Немного больновато, ах..."
                $herViewHead.showQ( "body_131.png", posHead )
                her "Ваш пенис слишком велик... ах..."
                $herViewHead.hideQ()
                m "Хм..."
                m "Ты хочешь, чтобы я замедлился?"
                $herViewHead.showQ( "body_31.png", posHead )
                her "Нет, сэр... Вам не стоит..."
                $herViewHead.showQ( "body_33.png", posHead )
                her "Пожалуйста, не обращайте на меня внимания... Наслаждайтесь."
                her "Я... ах... привыкну к этому... ах..."
                $herViewHead.hideQ()
                m "Как пожелаешь, малышка."
                $herViewHead.showQ( "body_131.png", posHead )
                her "Ах-a...{image=textheart.png}"
                $herViewHead.hideQ()

        m "Да, о да!"
        $herViewHead.showQ( "body_131.png", posHead )
        her "Ах-а...{image=textheart.png}"
        $herViewHead.hideQ()
        if daytime:
            m "Собираешься вернуться в класс после того, как мы с тобой закончим?"
        else:
            m "Собираешься вернуться в кровать после того, как мы с тобой закончим?"
        $herViewHead.showQ( "body_131.png", posHead )
        her "Да, ах...{image=textheart.png}"
        her "Если я вообще смогу ходить..."
        $herViewHead.hideQ()
        g4 "Хм! {image=textheart.png} Да, ты всегда знаешь, что говорить, девочка"
        $herViewHead.showQ( "body_132.png", posHead )
        her "Ах...{image=textheart.png} ах...{image=textheart.png}{image=textheart.png}"
        with hpunch
        $herViewHead.showQ( "body_130.png", posHead )
        her "{size=+7}!!!!!!!!!!!!!!!{/size}{image=textheart.png}{image=textheart.png}{image=textheart.png}"
        $herViewHead.hideQ()
        m "Ммм? Ты в порядке?"
        show screen blktone8
        with d3
        ">Ноги Гермионы затряслись..."
        m "Девочка?"
        $herViewHead.showQ( "body_130.png", posHead )
        her "{image=textheart.png}{image=textheart.png}{image=textheart.png}Мне кажется, я кончаю, сэр!{image=textheart.png}{image=textheart.png}{image=textheart.png}"
        $herViewHead.hideQ()
        g9 "Ха... Ты ненасытная сучка!"
        $herViewHead.showQ( "body_133.png", posHead )
        her "АААА! Я больше не могу сдерживаться!"
        $herViewHead.hideQ()
        g4 "Тебя нужно наказать за это, грязная шлюха!"
        ">Вы натягиваете задницу Гермины всё сильнее и сильнее и трахаете её всё жестче и жестче!"
        $ g_c_u_pic = "sex2_ani"
        with hpunch
        $herViewHead.showQ( "body_130.png", posHead )
        her "НЕТ! ОСТАНОВИТЕСЬ! ПОЖАЛУЙСТА!"
        $herViewHead.hideQ()
        g4 "Кто тебе разрешал кончать, шлюха? Вот твоё наказание!"
        $herViewHead.showQ( "body_131.png", posHead )
        her "Профессор, нееее...а-ах!{image=textheart.png}"
        $herViewHead.showQ( "body_134.png", posHead )
        her "Ах-a...{image=textheart.png}Я сейчас сойду с ума!{image=textheart.png}{image=textheart.png}{image=textheart.png}"
        $herViewHead.hideQ()
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
        $herViewHead.showQ( "body_134.png", posHead )
        her "Нет...{image=textheart.png} ах...{image=textheart.png}"
        her "Похоже я сейчас...{image=textheart.png} кончу...{image=textheart.png}"
        $herViewHead.hideQ()
        g4 "ОООО ДА! ШЛЮХА!"
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


                #$herViewHead.data().addItemKey( 'sperm', CharacterExItem( herViewHead.mMiscFolder, "sperm_05.png", G_Z_FACE + 1 ) )
                $herViewHead.data().addItem( 'item_sperm', '05' )
                $herViewHead.showQ( "body_133.png", posHead )
                her2 "Ааа...{image=textheart.png}{image=textheart.png}{image=textheart.png}"
                $herViewHead.hideQ()
                hide screen bld1
                with d3
                show screen ctc
                pause
                hide screen ctc
                show screen bld1
                with d3
                $ g_c_u_pic = "sex_cum_out_blink_ani"

                m "Это было весело..."
                $herViewHead.showQ( "body_135.png", posHead )
                her "*еле дышит*"
                $herViewHead.hideQ()
                m "Как ты?"
                $herViewHead.showQ( "body_133.png", posHead )
                her "Ах... да..."
                her "Мои ноги до сих пор трясутся..."
                $herViewHead.hideQ()
                hide screen bld1
                with d3
                show screen ctc
                pause
                hide screen ctc
                show screen blkfade
                with d7
                $herViewHead.showQ( "body_133.png", posHead )
                if daytime:
                    her "Я думаю, мне пора вернуться в класс..."
                else:
                    her2 "Я думаю, мне пора вернуться в спальню..."
                $herViewHead.hideQ()
                m "Хорошо."
                m "Тебе понравилось быть оттраханной профессором?"
                $herViewHead.showQ( "body_136.png", posHead )
                her2 "Сэр, я всего лишь делаю это ради моего факультета."
                $herViewHead.hideQ()
                m "Ты что, серьезно? Все ещё?"
                $herViewHead.showQ( "body_131.png", posHead )
                her "Мы можем рассчитаться... пожалуйста?"
                $herViewHead.hideQ()
    
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
                #$herViewHead.data().addItemKey( 'sperm', CharacterExItem( herViewHead.mMiscFolder, "sperm_05.png", G_Z_FACE + 1 ) )
                $herViewHead.data().addItem( 'item_sperm', '05' )
                $herViewHead.showQ( "body_133.png", posHead )
                her2 "Аааа...{image=textheart.png}{image=textheart.png}{image=textheart.png}"
                $herViewHead.hideQ()
                hide screen bld1
                with d3
                show screen ctc
                pause
                hide screen ctc
                show screen bld1
                with d3
                $ g_c_u_pic = "03_hp/08_animation_02/23_cum_19.png"
                $herViewHead.showQ( "body_133.png", posHead )
                her "Вы кончили в меня..."
                $herViewHead.hideQ()
                g9 "Да, в тебя."
                hide screen bld1
                with d3
                show screen ctc
                pause
                hide screen ctc
                show screen blkfade
                with d7
                $herViewHead.showQ( "body_133.png", posHead )
                her "Но..."
                $herViewHead.hideQ()
                m "Что?"
                $herViewHead.showQ( "body_132.png", posHead )
                her "Вы не боитесь что я забеременею?"
                $herViewHead.hideQ()
                m "Не, всё будет хорошо..."
                $herViewHead.showQ( "body_132.png", posHead )
                her "Откуда вы знаете, сэр?"
                $herViewHead.hideQ()
                m "Мы, ведьмаки - бесплодны."
                $herViewHead.showQ( "body_131.png", posHead )
                her "Ведьмаки?"
                $herViewHead.hideQ()
                m "Конечно... Ты - ведьма, получается я - ведьмак, верно?"
                m "А всем известно, что ведьмаки - бесплодны..."
                $herViewHead.showQ( "body_117.png", posHead )
                her "Сэр, это бессмысленно..."
                her "Могу я просто получить, что причитается...?"
                $herViewHead.hideQ()

    elif IsRunNumber(2): # SECOND EVENT <============================================================== EVENT 02
#    elif request_29_points == 1: # SECOND EVENT <============================================================== EVENT 02
        m "Мисс Грейнджер, вы уже мокрая и готовы, чтобы я вошёл в вас?"
        $herView.hideshowQQ( "body_30.png", pos )
        her "Профессор!"
        m "Просто скажи \"Я готова\" и иди сюда, девочка."
        $herView.hideshowQQ( "body_31.png", pos )
        her "..........."
        $herView.hideshowQQ( "body_118.png", pos )
        her "Я готова...."
        $herView.hideQ()
        jump your_ass

    elif IsRunNumberOrMore(3): # THIRD EVENT <============================================================== EVENT 03
#    elif request_29_points >= 2: # THIRD EVENT <============================================================== EVENT 03
        m "Мисс Грейнджер..."
        m "Прошлой ночью у меня был сон..."
        g9 "Вы легли на мой стол, раздвинули ноги и я трахал вашу киску со всей силой..."
        $herView.hideshowQQ( "body_120.png", pos )
        her "В этом сне, сэр..."
        $herView.hideshowQQ( "body_47.png", pos )
        her "Я получила 65 баллов своему факультету за это?"
        g9 "Да, мисс Грейнджер, получили."
        $herView.hideshowQQ( "body_66.png", pos )
        her "..............................."
        her "Дайте мне, хотя бы, снять трусики..."
        stop music fadeout 1.0
        $herView.hideQQ()
        show screen blkfade
        with d3
        # SEX
        

        $ renpy.play('sounds/gltch.mp3')
        with hpunch
        with kissiris
        $herViewHead.showQ( "body_130.png", posHead )
        her2 "Ооооооохххх....{image=textheart.png}"
        $herViewHead.hideQ()
        
        $herView.hideQ()
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


        $herViewHead.showQ( "body_131.png", posHead )
        her "Ах...{image=textheart.png}"
        $herViewHead.hideQ()
        m "Твоя киска сегодня легче приняла мой член..."
        $herViewHead.showQ( "body_131.png", posHead )
        her "Да...{image=textheart.png} аааах...?{image=textheart.png}"
        $herViewHead.showQ( "body_132.png", posHead )
        her "Это из-за вас, сэр...{image=textheart.png}"
        $herViewHead.showQ( "body_134.png", posHead )
        her2 "Вы долбите моё маленькую киску своим гиганстким членом...{image=textheart.png}"
        $herViewHead.hideQ()
        g4 "Аааа, шлюха!"
        $herViewHead.showQ( "body_134.png", posHead )
        her "Ох...{image=textheart.png}{image=textheart.png}"
        $herViewHead.hideQ()

        
        
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
        m "Да! Тебе нравится, когда я так тебя трахаю?"
        $herViewHead.showQ( "body_128.png", posHead )
        her "Да, сэр..."
        $herViewHead.hideQ()
        menu:
            g4 "..."
            "\"Быть нежным, но страстным.\"":
                m "Да, тебе нравится это?"
                $herViewHead.showQ( "body_127.png", posHead )
                her "Да, сэр... ах...{image=textheart.png}"
                $herViewHead.hideQ()
                m "Хорошая девочка!"
                m "Просто расслабься и прими мой член в себя!"
                $herViewHead.showQ( "body_127.png", posHead )
                her "Да... ах...{image=textheart.png}"
                $herViewHead.hideQ()
                m "Почти... почти..."
                $herViewHead.showQ( "body_131.png", posHead )
                her "Да...{image=textheart.png}{image=textheart.png}"
                $herViewHead.hideQ()
                m "Да, моя маленькая принцесса..."
                $herViewHead.showQ( "body_119.png", posHead )
                her "Что?"
                $herViewHead.showQ( "body_118.png", posHead )
                her "Нет, пожалуйста, не называйте меня так... ах...{image=textheart.png}"
                her2 "Мой папа меня так называл, когда я была маленькая..."
                $herViewHead.hideQ()
                m "Ну, сейчас я твой папочка!"
                $herViewHead.showQ( "body_121.png", posHead )
                her "Ах...{image=textheart.png} Ах-а...{image=textheart.png}{image=textheart.png}"
                $herViewHead.hideQ()
                m "И ты моя маленькая принцесса - шлюха!"
                $herViewHead.showQ( "body_123.png", posHead )
                her "Ах...{image=textheart.png} ох...{image=textheart.png}{image=textheart.png}{image=textheart.png}"
            "\"Быть жестким с ней!\"":
                $herViewHead.hideQ()
                m "Да, ты шлюха!"
                m "Я научу тебя наслаждаться каждым моментом, когда тебя трахают!"
                show screen blktone
                hide screen ctc
                with d3
                ">Вы увеличиваете темп."
                hide screen blktone
                with d3
                $herViewHead.showQ( "body_131.png", posHead )
                her "Ахх...{image=textheart.png} Профессор..."
                $herViewHead.hideQ()
                m "Ты - ненасытная шлюха!"
                $herViewHead.showQ( "body_132.png", posHead )
                her "А...{image=textheart.png} Ох...{image=textheart.png}"
                $herViewHead.hideQ()
                m "Ты - позор для своего факультета!"
                $herViewHead.showQ( "body_132.png", posHead )
                her "А-ох...{image=textheart.png}{image=textheart.png}{image=textheart.png}"
                $herViewHead.hideQ()
                m "Твои родители послали тебя учиться, а не трахаться со студентами и преподавателями!"
                $herViewHead.showQ( "body_132.png", posHead )
                her "Ах-а...{image=textheart.png} Но я всё это делаю для...--"
                $herViewHead.hideQ()
                m "Всем наплевать, зачем ты это делаешь, любительница членов!"
                m "Посмотри, кем ты стала!"
                m "Скачешь задницей на члене старого профессора, как самая дешевая шлюха!"
                $herViewHead.showQ( "body_134.png", posHead )
                her "Ох...{image=textheart.png} Нет...{image=textheart.png} прекратите это говорить...{image=textheart.png} ах...{image=textheart.png}{image=textheart.png}{image=textheart.png}"
                $herViewHead.hideQ()
                show screen blktone
                with d3
                ">Вы увеличиваете снова темп."
                $ g_c_u_pic = "sex2_ani"
                ">Комнату наполняет звук шлёпания и стонов..."
                hide screen blktone
                with d3
                m "Ты позволила мне лапать тебя... Ты сосешь мой член..."
                m "Так скажи мне, кто ты после этого!?"
                $herViewHead.showQ( "body_123.png", posHead )
                her "................"
                $herViewHead.showQ( "body_132.png", posHead )
                her "Ах...{image=textheart.png} Ах....{image=textheart.png}{image=textheart.png}{image=textheart.png}"
                $herViewHead.showQ( "body_118.png", posHead )
                her "......................."
                her "{size=-5}Я шлюха...{/size}"
                her "{size=-5}Я шлюха... ах...{/size}"
                $herViewHead.hideQ()
        
        m "Да! Вот кто ты есть на самом деле!"
        $herViewHead.showQ( "body_118.png", posHead )
        her "Ах... а... а..."
        her "Сэр, вы можете... а..."
        $herViewHead.hideQ()
        m "Что?"
        $herViewHead.showQ( "body_138.png", posHead )
        her "Вы можете отшлепать меня... ох...?"
        $herViewHead.hideQ()
        g4 "С удовольствием!"
        
        $ renpy.play('sounds/slap.mp3')
        show screen white 
        pause.1
        hide screen white
        with hpunch

        $herViewHead.showQ( "body_139.png", posHead )
        her "АА-А-АХ!{image=textheart.png}{image=textheart.png}{image=textheart.png}"
        $herViewHead.hideQ()
        m "Тебе нравится, а?"
        $ renpy.play('sounds/slap.mp3')
        show screen white 
        pause.1
        hide screen white
        with hpunch
        $herViewHead.showQ( "body_138.png", posHead )
        her "А..!{image=textheart.png} ОООО ДА!{image=textheart.png}{image=textheart.png}{image=textheart.png}"
        $herViewHead.hideQ()
        m "И ещё... ещё!"
        $ renpy.play('sounds/slap.mp3')
        show screen white 
        pause.1
        hide screen white
        with hpunch
        $herViewHead.showQ( "body_138.png", posHead )
        her "Ах! ДА!"
        $herViewHead.hideQ()
        show screen blktone
        with d3
        ">Вы заметили, что после каждого шлепка по заднице девчонки её киска сжимается на пару секунд и сжимает ваш член..."
        ">Вам нравятся эти ощущения..."
        ">Вы продолжаете шлёпать попку Гермионы."
        ">Каждый удар по заднице сопровождается её вздохами наслаждения."
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
        $herViewHead.showQ( "body_138.png", posHead )
        her "АААА!!!{image=textheart.png}{image=textheart.png}{image=textheart.png} БОЛЬНО!{image=textheart.png}{image=textheart.png}{image=textheart.png}"
        $herViewHead.showQ( "body_134.png", posHead )
        her2 "Это больно...{image=textheart.png}{image=textheart.png}{image=textheart.png} больно...{image=textheart.png}{image=textheart.png}{image=textheart.png}"
        $herViewHead.hideQ()
        m "М?"
        m "Почему твои ноги так дрожат, малышка?"
        m "Ты кончаешь?"
        $herViewHead.showQ( "body_133.png", posHead )
        her "Да...{image=textheart.png}{image=textheart.png}{image=textheart.png}{image=textheart.png}{image=textheart.png}{image=textheart.png}"
        $herViewHead.hideQ()
        m "Тогда я последую твоему примеру."
        $herViewHead.showQ( "body_133.png", posHead )
        her ".............."
        $herViewHead.hideQ()
        show screen blktone 
        with d3
        ">Вы начади трахать Гермиону всё сильнее и жестче!"
        hide screen blktone 
        with d3
        $herViewHead.showQ( "body_139.png", posHead )
        her "А! Нет! Я не могу...{image=textheart.png} Я...{image=textheart.png} Ох...{image=textheart.png}{image=textheart.png}{image=textheart.png}"
        $herViewHead.hideQ()
        m "Заткнись, шлюха!"
        g4 "Ах"
        menu:
            "- Кончить в Гермиону -":
                with hpunch
                g4 "{size=+7}Да, почувствуй всё до капли!!!{/size}"
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
                #$herViewHead.data().addItemKey( 'sperm', CharacterExItem( herViewHead.mMiscFolder, "sperm_05.png", G_Z_FACE + 1 ) )
                $herViewHead.data().addItem( 'item_sperm', '05' )
                $herViewHead.showQ( "body_133.png", posHead )
                her "!!!"
                her "ААА, вы наполняете меня до краёв!{image=textheart.png}{image=textheart.png}{image=textheart.png}"
                $herViewHead.hideQ()
                g4 "Я ещё не закончил, сучка!"
                g4 "{size=+15}Аааа!!!!!!!!!!!!!!!!{/size}"
                show screen white 
                pause.1
                hide screen white
                pause.2
                show screen white 
                pause .1
                hide screen white
                with hpunch
                $herViewHead.showQ( "body_139.png", posHead )
                her "Ааа, мой живот!"
                $herViewHead.hideQ()
                g4 "{size=+5}ШЛЮХА!{/size}"






                $herViewHead.hideQ()
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
                $herViewHead.showQ( "body_133.png", posHead )
                her "Ааа...{image=textheart.png}"
                $herViewHead.hideQ()
                m "Ты в порядке, сучка? То есть, девочка."
                $herViewHead.showQ( "body_133.png", posHead )
                her "Да... Я..."
                $herViewHead.showQ( "body_135.png", posHead )
                her "Я чувствую, как вы меня заполнили..."
                $herViewHead.showQ( "body_130.png", posHead )
                her "!!!"
                her "Вы кончили в меня, сэр!"
                $herViewHead.hideQ()
                m "Да, я залил тебя."
                $herViewHead.showQ( "body_131.png", posHead )
                her "Вам не стоило этого делать..."
                $herViewHead.hideQ()
                m "Разве ты не получила удовольствие от моей горячей спермы?"
                $herViewHead.showQ( "body_123.png", posHead )
                her "....возможно."
                $herViewHead.showQ( "body_121.png", posHead )
                her "По-моему, я кончила несколько раз..."
                show screen blkfade
                with d3
                $herViewHead.showQ( "body_122.png", posHead )
                her2 "Может вы и правы, сэр, и я не должна об этом беспокоиться."
                her "Мы можем рассчитаться?"
                $herViewHead.hideQ()

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
                #$herViewHead.data().addItemKey( 'sperm', CharacterExItem( herViewHead.mMiscFolder, "sperm_05.png", G_Z_FACE + 1 ) )
                $herView.data().addItem( 'item_sperm', '05' )
                $herViewHead.showQ( "body_133.png", posHead )
                her2 "ААА...{image=textheart.png}{image=textheart.png}{image=textheart.png}"
                $herViewHead.hideQ()
                g4 "{size=+5}ШЛЮХА! Получи всё!{/size}"
                $herViewHead.showQ( "body_138.png", posHead )
                her "{size=+5}!!!{/size}"
                $herViewHead.hideQ()
                $herViewHead.hideQ()
                hide screen bld1
                with d3
                show screen ctc
                pause
                hide screen ctc
                show screen bld1
                with d3
                $ g_c_u_pic = "sex_cum_out_blink_ani"
                
                


                
                m "Это было здорово..."
                $herViewHead.showQ( "body_138.png", posHead )
                her "Ах...{image=textheart.png}"
                $herViewHead.hideQ()
                m "Как ты, шлюха?"
                $herViewHead.showQ( "body_133.png", posHead )
                her "Да... Я..."
                $herViewHead.hideQ()
                m "Ты наслаждалась этим?"
                $herViewHead.showQ( "body_123.png", posHead )
                her "....думаю, да..."
                $herViewHead.hideQ()
                show screen ctc
                pause
                hide screen ctc
                show screen blkfade
                with d3
                $herViewHead.showQ( "body_121.png", posHead )
                her "Думаю, я кончила несколько раз, сэр..."
                $herViewHead.showQ( "body_122.png", posHead )
                her "Мы можем рассчитаться?"
                $herViewHead.hideQ()
        
        
    if herViewHead.data().getItem( 'item_sperm' ) != None:
        $herViewHead.data().addItem( 'item_sperm_dried' )
        #$herViewHead.data().addItemKey( 'sperm_after', CharacterExItem( herViewHead.mMiscFolder, "sperm_00_after.png", G_Z_FACE + 1 ) )
    $herViewHead.data().delItem( 'item_sperm' )
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
    $herView.showQ( "body_13.png", pos )
    hide screen hermione_01_f #Hermione stands still.
    with d3
    her "Спасибо, сэр..."

    if hermi.whoring <= 20: # Level 07 <
        $ hermi.whoring +=1




#    if request_29_points == 0:
#        $ new_request_29_01 = True # HEARTS
#    if request_29_points == 1:
#        $ new_request_29_02 = True # HEARTS
#    if request_29_points >= 2:
#        $ new_request_29_03 = True # HEARTS
    


#    $ request_29_points += 1


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

    #call music_block 
    
    $event.Finalize()    
    $SetHearts(GetStage(event._finishCount,1,3,1))
    if daytime:
        jump night_start
    else:
        jump day_start
                   

