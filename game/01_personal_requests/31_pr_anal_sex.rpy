
###############################################################################################################################
### LEVEL 09 ##################################################################################################################
###################REQUEST_31 (Level 08) (75 pt.) (Anal sex).  #####################################################
label new_request_31: #LV.8 (Whoring = 21 - 23)
    $herView.hideQQ()
    m "{size=-4}(Попросить у неё анальный секс?){/size}"
    $ menu_x = 0.5 #Default position of the menu (0.5). Version B is $ menu_x = 0.2
    menu:
        "\"(Да, давай!)\"":
            show screen blktone
            with d3
            pass
        "\"(Не сейчас)\"":
            $event.NotFinished()
            jump new_personal_request
 
    label new_request_31_start:
    $ pos = POS_140
    $ posHead = gMakePos( 390, 340 )
    $ herView.data().saveState()
 
    if IsFirstRun(): # FIRST EVENT <============================================================== EVENT 01
#    if request_31_points == 0: # FIRST EVENT <============================================================== EVENT 01
        m "Мисс Грейнджер..."
        $herView.hideshowQQ( "body_17.png", pos )
        her "Сэр?.."
        m "Известен ли вам термин \"Анальный секс\"?"
        if hermi.whoring <=20:
            jump too_much
        $herView.hideshowQQ( "body_79.png", pos )
        her "90 очков..."
        m "Что?"
        $herView.hideshowQQ( "body_66.png", pos )
        her "............................."
        m "Хорошо, пусть будет так. 90 очков."
        $herView.hideQ()
        
        
        label lucky_guess:
            
        show screen blkfade
        with d3
        
        stop music fadeout 1.0
        
        $herViewHead.showQ( "body_29.png", posHead )
        her "..........."
        $herViewHead.hideQ()
        m "Давай посмотрим..."
        $herViewHead.showQ( "body_34.png", posHead )
        her "................."
        $herViewHead.hideQ()
        m "Хм..."
        $herViewHead.showQ( "body_18.png", posHead )
        her "!!!"
        $herViewHead.hideQ()
        g4 "Да ладно!.."
        $herViewHead.showQ( "body_20.png", posHead )
        her "АЙ!"
        $herViewHead.hideQ()
        m "Просто постарайся расслабиться немного, хорошо?"
        $herViewHead.showQ( "body_21.png", posHead )
        her "Я стараюсь!"
        $herViewHead.hideQ()
        m "Хорошо, что если я сделаю так?.."
        $herViewHead.showQ( "body_20.png", posHead )
        her "АЙ! Что вы делаете, cэр?"
        $herViewHead.hideQ()
        m "Ладно, это не сработает..."
        m "Хм..."
        m "Ладно, я знаю, что мы сделаем."
        menu:
            m "..."
            "\"Хорошо, попробую всунуть член и посильнее войти!\"":
                play music "music/(Orchestral) Playful Tension by Shadow16nh.mp3" fadein 1 fadeout 1 # SEX THEME.
                $herViewHead.showQ( "body_18.png", posHead )
                her "Посильнее войти, cэр?!"
                $herViewHead.hideQ()
                $ renpy.play('sounds/spit.mp3') #Sound of spiting. 
                g3 "*Хлоп!*"
                $herViewHead.showQ( "body_32.png", posHead )
                her "Ааааааааааааааайййййй!"
                $herViewHead.showQ( "body_31.png", posHead )
                her2 "Нет, cэр, подождите! Может быть, я просто расслаблюсь..."
                $herViewHead.hideQ()
                m "Не надо, я уже вхожу!"
                with hpunch
                $herViewHead.showQ( "body_22.png", posHead )
                her "ААААА!"
                $herViewHead.showQ( "body_20.png", posHead )
                her "АЙ! АЙ! АЙ!"
                $herViewHead.hideQ()
                g4 "Почти вошёл!"
                $herViewHead.showQ( "body_32.png", posHead )
                her "Нет, мне больно! Мне больно!"
                $herViewHead.hideQ()
                g4 "Почти! Почти!"
                $herViewHead.showQ( "body_32.png", posHead )
                her "АЙ! Больно!"
                $herViewHead.hideQ()
                g4 "Заткнись, девчонка! Я делаю тебе одолжение!"
                g4 "Твой анус такой узкий, и почти невозможно трахнуть тебя в задницу, а я исправляю это!"
                $herViewHead.showQ( "body_20.png", posHead )
                her "Тогда остановитесь, пожалуйста!"
                $herViewHead.hideQ()
                m "Нет! Нам нужно расширить твою дырочку!"
                $herViewHead.showQ( "body_20.png", posHead )
                her "Но я не хочу, чтобы вы это делали!"
                $herViewHead.hideQ()
                m "Правда? Как ты тогда думаешь, люди будут иметь тебя в задницу?"
                $herViewHead.showQ( "body_132.png", posHead )
                her "Какие люди?"
                $herViewHead.hideQ()
                g4 "Ну ты знаешь... люди."
                g4 "Аааа, черт... Моему члену теперь тоже больно...."
                $herViewHead.showQ( "body_131.png", posHead )
                her "Остановитесь тогда! Остановитесь, сэр!"
                her "Я передумала! Мне не нужно 90 баллов!"
                $herViewHead.hideQ()
                g4 "По-моему, я почти..."
                
                $ renpy.play('sounds/gltch.mp3')
                with hpunch
                with kissiris
                $herViewHead.showQ( "body_130.png", posHead )
                her2 "{size=+5}Ааааай!!!{/size}"
                $herViewHead.hideQ()
                g4 "Да!!!"
                $herViewHead.showQ( "body_130.png", posHead )
                her "AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA!"
                $herViewHead.hideQ()
                g4 "Давай наполним эту маленькую дырочку спермой?"
                $herViewHead.showQ( "body_137.png", posHead )
                her "ДА... Пожалуйста, я хочу, чтобы все поскорее закончилось..."
                $herViewHead.hideQ()




                $herView.hideQ()
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
                $herViewHead.showQ( "body_139.png", posHead )
                her "*всхлип* Как?"
                $herViewHead.hideQ()
                g4 "Ты знаешь..."
                $herViewHead.showQ( "body_139.png", posHead )
                her "Ох..."
                $herViewHead.showQ( "body_140.png", posHead )
                her "Я шлюха??"
                $herViewHead.hideQ()
                g9 "Да, вот кто ты!"
                $herViewHead.showQ( "body_141.png", posHead )
                her "*Хнык!* Я шлюха..."
                her "Я люблю сосать члены..."
                $herViewHead.showQ( "body_142.png", posHead )
                her2 "И моя узкая дырочка сейчас будет разорвана на части... *Хнык!*"
                $herViewHead.hideQ()
                g4 "Да! Даа!"
                g4 "Аааа! Да!"
                $herViewHead.showQ( "body_144.png", posHead )
                her "Нет! Он ещё больше увеличился во мне?! Я боюсь!"
                $herViewHead.hideQ()
                g4 "Аааа!"

                
            "\"Отсоси сначала у меня, смажь мой член!\"":
                $herViewHead.showQ( "body_31.png", posHead )
                her "Аа... Хорошо..."
                $herViewHead.hideQ()
                play music "music/(Orchestral) Playful Tension by Shadow16nh.mp3" fadein 1 fadeout 1 # SEX THEME.
                #SUCKING
                
                hide screen blkfade
                
                
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
                        
                
                
                
                
                
                
                
                her "*Хлюп-хлюп-хлюп-хлюп!*"
                $herViewHead.hideQ()
                m "Да... хорошо..."
                her "*Хлюп!* *Хлюп!* *Хлюп!*"
                $herViewHead.hideQ()
                m "Отлично. Думаю, достаточно. Ложись обратно на стол."
                show screen blkfade
                with d3

                
                #ON THE DESK
                $herViewHead.showQ( "body_31.png", posHead )
                her "............."
                $herViewHead.hideQ()
                g4 "Да! Почти!"
                $herViewHead.showQ( "body_32.png", posHead )
                her "Ау!"
                $herViewHead.hideQ()
                m "Расслабься. Почти вошёл."
                
                $ renpy.play('sounds/gltch.mp3')
                with hpunch
                with kissiris
                $herViewHead.showQ( "body_130.png", posHead )
                her2 "{size=+5}AAAAAAAA!!!{/size}"
                $herViewHead.hideQ()
                g4 "ДА!!!"
                $herViewHead.showQ( "body_130.png", posHead )
                her "Моя... моя..."
                $herViewHead.showQ( "body_132.png", posHead )
                her "Больно!"
                $herViewHead.hideQ()
                g4 "Давай заполним эту дырочку спермой до отказа?"
                $herViewHead.showQ( "body_141.png", posHead )
                her "....................."
                $herViewHead.hideQ()
                
                # SEX
                
                $herView.hideQ()
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


                $herViewHead.showQ( "body_139.png", posHead )
                her "....................."
                $herViewHead.hideQ()
                m "Как ты, шлюшка?"
                $herViewHead.showQ( "body_140.png", posHead )
                her2 "Ааа... Вы... разорвали у меня все внутри... сэр."
                $herViewHead.showQ( "body_141.png", posHead )
                her "И до сих пор болит..."
                $herViewHead.hideQ()
                m "Хм..."
                m "Может, было недостаточно смазки...?"
                m "Успокойся, девочка. Пососи мой член ещё."
                $herViewHead.showQ( "body_140.png", posHead )
                her "Что? Но..."
                $herViewHead.showQ( "body_139.png", posHead )
                her "Он грязный... Он уже был в моей попке."
                $herViewHead.hideQ()
                m "Да, он был в тебе, но это не означает, что он грязный."
                m "Расслабься, девочка. Соси давай."
                $herViewHead.showQ( "body_139.png", posHead )
                her "..........."
                $herViewHead.hideQ()
                show screen blkfade
                with d3
                
                
                #SUCKING
                
                hide screen blkfade
                
                
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
                
                
                
                
                her "*Хлюп!* *Хлюп!* *Хлюп!*"
                m "Да... хорошо..."
                her "*Чавк!* *Чавк!* *Чавк!*"
                m "Чувствуешь вкус своей попки на моём члене?"
                her "*Чавк!* *Хлюп!* *Чавк!*"
                m "Ладно, наверное, хватит."
                show screen blkfade
                with d3
               

                
                #ON DESK AGAIN.
                
                
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
                
                $herViewHead.showQ( "body_139.png", posHead )
                her "Ах..."
                $herViewHead.hideQ()
                m "Уже лучше?"
                $herViewHead.showQ( "body_140.png", posHead )
                her "Всё ещё больно..."
                her "Но, думаю, всё будет в порядке..."
                $herViewHead.hideQ()
                m "Тогда я буду входить помедленнее..."
                $herViewHead.showQ( "body_141.png", posHead )
                her "Ах... спасибо, сэр."
                $herViewHead.hideQ()
                m "О... да... вот так лучше... да..."
                $herViewHead.showQ( "body_139.png", posHead )
                her "..........."
                $herViewHead.hideQ()
                m "Ммм...да... Такая узкая..."
                $herViewHead.showQ( "body_143.png", posHead )
                her "................"
                $herViewHead.hideQ()
                m "Почему ты замолчала, девочка?"
                $herViewHead.showQ( "body_140.png", posHead )
                her "Просто это больно..."
                her2 "И я просто хочу, чтобы вы поскорее кончили, сэр..."
                $herViewHead.hideQ()
                m "Ты пытаешься сдержать слёзы от боли?"
                $herViewHead.showQ( "body_142.png", posHead )
                her "Да, сэр. *Хнык!*"
                $herViewHead.hideQ()
                m "Не надо сдерживаться."
                m "Плачь, кричи, рыдай столько, сколько захочешь!"
                $herViewHead.showQ( "body_140.png", posHead )
                her "Н-но..."
                $herViewHead.hideQ()
                m "Тогда я кончу быстрее."
                $herViewHead.showQ( "body_142.png", posHead )
                her "Правда? *Хнык!*"
                $herViewHead.showQ( "body_139.png", posHead )
                her2 "*Хнык!* Больно! *Хнык!* Как же это больно! *Хнык!*"
                $herViewHead.hideQ()
                m "Да, ещё..."
                $herViewHead.showQ( "body_145.png", posHead )
                her "*Хнык!*"
                $herViewHead.hideQ()
                m "Бедное маленькое дитя..."
                m "Большой и злой человек разрывает твою узкую задницу своим членом!"
                $herViewHead.showQ( "body_146.png", posHead )
                her "*Хнык!* Дааааа! *Хнык!*"
                $herViewHead.hideQ()
                g4 "О-да!"
                $herViewHead.showQ( "body_147.png", posHead )
                her "Нет, мне страшно! *Хнык!*"
                $herViewHead.hideQ()
        
        menu:
            "- Заполнить Гермиону спермой -":
                g4 "Оооо!"
                $herViewHead.showQ( "body_130.png", posHead )
                her "Нет! АХ!"
                $herViewHead.hideQ()
                
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
                #$herViewHead.data().addItemKey( 'sperm', CharacterExItem( herViewHead.mMiscFolder, "sperm_05.png", G_Z_FACE + 1 ) )
                $herViewHead.data().addItem( 'item_sperm', '05' )
                $herViewHead.showQ( "body_144.png", posHead )
                her "ААА! Я ЧУВСТВУЮ, КАК ВЫ МЕНЯ ЗАПОЛНЯЕТЕ !{image=textheart.png}{image=textheart.png}{image=textheart.png}"
                $herViewHead.hideQ()
                
                
                g4 "ДА, ТЫ ПОТАСКУХА! ДАА!"
                $herViewHead.showQ( "body_145.png", posHead )
                her "БОЛЬНО, БОЛЬНО!"
                $herViewHead.hideQ()
                g4 "Заткнись!"
                with hpunch
                $herViewHead.showQ( "body_149.png", posHead )
                her2 "Нет, в меня больше не влезет! Перестаньте кончать, ВЫ! УБЛЮДОК!"
                $herViewHead.hideQ()
                g4 "Закрой пасть, шлюха! Я ещё не закончил!"
                $herViewHead.showQ( "body_146.png", posHead )
                her "Нет! Пожалуйста! АААА, МОЙ ЖИВОТ! Я СЕЙЧАС ЛОПНУ!"
                $herViewHead.hideQ()
                g4 "ААА!"
                $herViewHead.showQ( "body_144.png", posHead )
                her "Нет! Я сейчас взорвусь..."
                $herViewHead.hideQ()
                with hpunch
                $herViewHead.showQ( "body_150.png", posHead )
                play sound "sounds/burp.mp3"
                her "{size=+7}*ХЛЮП!*!!!!!{/size}"
                $herViewHead.showQ( "body_151.png", posHead )
                her "......................."
                her "............."
                $herViewHead.showQ( "body_126.png", posHead )
                $ renpy.play('sounds/gulp.mp3') #Sound of gulping down a liquid.
                her "{size=+7}*ХЛЮП!*{/size}"  
                $herViewHead.showQ( "body_145.png", posHead )
                her "*Хнык!* Я НЕНАВИЖУ ВАС..."
                $herViewHead.showQ( "body_148.png", posHead )
                her2 "{size=+5}Я НЕНАВИЖУ ВАС И ВАШ ГРЯЗНЫЙ СТАРЫЙ ЧЛЕН!{/size}"
                her "{size=+5}Я НЕНАВИЖУ ВАС! ВЫ СЛЫШИТЕ МЕНЯ?!{/size}"
                $herViewHead.hideQ()
                g4 "Аррр... Заткнись, шлюха!"
                $herViewHead.showQ( "body_145.png", posHead )
                her "*Хнык!* *Хнык!*..."
                $herViewHead.hideQ()
                
                
                
                
                
                
                
                # AFTER CUM INSIDE
                
                hide screen bld1
                with d3
                show screen ctc
                pause
                hide screen ctc
                show screen bld1
                with d3
                $ g_c_u_pic = "03_hp/08_animation_02/23_cum_19.png"
                $herViewHead.showQ( "body_142.png", posHead )
                her "*Хнык!*..."
                $herViewHead.hideQ()
                m "УАУ!... Думаю, я закончил."
                m "Ты в порядке?"
                $herViewHead.showQ( "body_142.png", posHead )
                her "Да... *Хнык!*"
                $herViewHead.hideQ()
                m "Ты плачешь?"
                $herViewHead.showQ( "body_142.png", posHead )
                her "Моя попка болит, но я в порядке, сэр..."
                $herViewHead.hideQ()
                m "Ну, я должен сказать, что ты стойко приняла мой член..."
                $herViewHead.showQ( "body_142.png", posHead )
                her "Спасибо, сэр..."
                $herViewHead.hideQ()

                hide screen bld1
                with d3
                show screen ctc
                pause
                hide screen ctc
                show screen blkfade
                with d7
                $herViewHead.showQ( "body_152.png", posHead )
                her "Извините, что я сказала, что ненавижу вас, сэр..."
                her "И ваш ненасытный член..."
                $herViewHead.showQ( "body_153.png", posHead )
                her "Не знаю, что на меня нашло..."
                $herViewHead.hideQ()
                g9 "Мой член!"
                $herViewHead.showQ( "body_153.png", posHead )
                her2 "Думаю, это произошло тогда, когда вы меня назвали \"шлюхой\". Я знаю, вы не это имели ввиду..."
                $herViewHead.hideQ()
                m "Да, конечно..."
                m "Всё ещё болит?"
                $herViewHead.showQ( "body_154.png", posHead )
                her "Немного..."
                $herViewHead.showQ( "body_155.png", posHead )
                her "До сих пор ощущаю внутри горячую сперму..."
                $herViewHead.hideQ()
                m "Ты собираешься так её и оставить? Ну, я имею в виду - сперму."
                $herViewHead.showQ( "body_156.png", posHead )
                her "Да..."
                if daytime:
                    her2 "Надеюсь, она не будет хлюпать, пока я сижу на занятиях..."
                else:
                    her2 "Надеюсь, она не будет хлюпать, пока я иду в свою комнату..."
                $herViewHead.hideQ()
                m "Ну, тогда - удачно добраться."
                $herViewHead.showQ( "body_155.png", posHead )
                her "Мы можем рассчитаться?"
                $herViewHead.hideQ()
                
                    
                
                
                
                
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
                #$herViewHead.data().addItemKey( 'sperm', CharacterExItem( herViewHead.mMiscFolder, "sperm_05.png", G_Z_FACE + 1 ) )
                $herViewHead.data().addItem( 'item_sperm', '05' )
                $herViewHead.showQ( "body_133.png", posHead )
                her2 "Аа...{image=textheart.png}{image=textheart.png}{image=textheart.png}"

                $herViewHead.hideQ()
                g4 "Да!!! Всё на твоей попке!"
                $herViewHead.showQ( "body_134.png", posHead )
                her "Оуу... Она горячая!"
                $herViewHead.hideQ()

                
                $herViewHead.hideQ()
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
                $herViewHead.showQ( "body_138.png", posHead )
                her "Да, сэр..."
                $herViewHead.hideQ()
                m "Ты как?"
                $herViewHead.showQ( "body_139.png", posHead )
                her "Всё ещё больновато, сэр. Но..."
                $herViewHead.hideQ()
                m "Что - \"Но\"...?"
                $herViewHead.showQ( "body_138.png", posHead )
                her "Но мне даже понравилось... сэр."
                $herViewHead.hideQ()
                m "Понравилось??"
                g9 "Хах... А ты, видимо, маленькая мазохистка."
                $herViewHead.showQ( "body_138.png", posHead )
                her "Мы можем рассчитаться, сэр?"
                $herViewHead.hideQ()

        
    elif IsRunNumber(2): # FIRST EVENT <============================================================== EVENT 02
#    elif request_31_points == 1: # FIRST EVENT <============================================================== EVENT 02
        m "Девочка?"
        $herView.hideshowQQ( "body_15.png", pos )
        her "Профессор?"
        m "Я куплю сегодня у тебя другую услугу..."
        $herView.hideshowQQ( "body_08.png", pos )
        her "............."
        m "Попытайся догадаться, что это будет?"
        m "У тебя три попытки."
        $herView.hideshowQQ( "body_09.png", pos )
        her "..........."
        $herView.hideshowQQ( "body_66.png", pos )
        her "Анальный секс?"
        g4 "Что..........?!"
        g4 "Как ты...?"
        $herView.hideshowQQ( "body_47.png", pos )
        her "Просто повезло, сэр..."
        m "Иногда ты меня пугаешь, девочка..."
        $herView.hideQQ()
        jump lucky_guess
        
        
        
        
        
    elif IsRunNumberOrMore(3): # FIRST EVENT <============================================================== EVENT 03
#    elif request_31_points >= 2: # FIRST EVENT <============================================================== EVENT 03
        m "Как насчет повторить анальный секс, малышка?"
        $herView.hideshowQQ( "body_17.png", pos )
        her "Как насчет ещё 90 баллов, сэр?"
        g9 "Иди сюда, маленькая мазохистка!"
        $herView.hideQQ()
        # SEX
        show screen blkfade
        with d3
        
        stop music fadeout 1.0
        
        $herViewHead.showQ( "body_29.png", posHead )
        her "........"
        $herViewHead.hideQ()
        m "Хм..."
        $herViewHead.showQ( "body_31.png", posHead )
        her "..........."
        $herViewHead.hideQ()
        
        
        $ renpy.play('sounds/gltch.mp3')
        with hpunch
        with kissiris
        $herViewHead.showQ( "body_130.png", posHead )
        her2 "Оооооооо....{image=textheart.png}"
        $herViewHead.hideQ()
        g4 "О, дааа!"
        $herViewHead.showQ( "body_121.png", posHead )
        her "Ах..."
        $herViewHead.hideQ()
        m "Сегодня я легче вхожу в твою дырочку."
        $herViewHead.showQ( "body_128.png", posHead )
        her "Ах... До сих пор больновато...."
        $herViewHead.showQ( "body_129.png", posHead )
        her "И, пожалуйста, называйте меня \"шлюхой\", сэр."
        $herViewHead.hideQ()
        g4 "Аррр! Ты потаскуха! Мне всегда нравится, когда ты так говоришь!"



        
        
        
        
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
        
        # INSERTION
        $herViewHead.showQ( "body_127.png", posHead )
        her "Ах... Ах..."
        her "Ах..."
        $herViewHead.showQ( "body_128.png", posHead )
        her "Сэр?"
        $herViewHead.hideQ()
        m "Да, шлюшка?"
        $herViewHead.showQ( "body_117.png", posHead )
        her "Эм..."
        $herViewHead.hideQ()
        hide screen ctc
        $herViewHead.showQ( "body_118.png", posHead )
        her "Вы возьмете меня в жены, сэр?"
        $herViewHead.hideQ()
        with hpunch
        g4 "{size=+9} ЧТО?!{/size}"
        g4 "Только не говори мне, что ты беременна!"
        $herViewHead.showQ( "body_122.png", posHead )
        her2 "Я не могу забеременеть оттого, что вы трахаете меня в попку..."
        $herViewHead.hideQ()
        m "Тогда какие разговоры о свадьбе?"
        $herViewHead.showQ( "body_117.png", posHead )
        her "Вы не поняли меня, сэр."
        $herViewHead.showQ( "body_118.png", posHead )
        her "Я хочу узнать, могли бы вы взять в жены {size=+5}такую девушку{/size} как Я?"
        $herViewHead.showQ( "body_34.png", posHead )
        her2 "Я никогда не предлагала ни одному мужчине трахнуть меня в попку, сэр..."
        $herViewHead.hideQ()
        m "Хорошо. Потому что я думаю, что нормальный мужчина ответит тебе \"нет\" в такой момент."
        $herViewHead.showQ( "body_127.png", posHead )
        her "Ах{image=textheart.png}..."
        $herViewHead.showQ( "body_118.png", posHead )
        her2 "Я имела ввиду... ах{image=textheart.png} {w} ...хотела сказать{image=textheart.png}... {w}...как вы думаете, кто нибудь женится{image=textheart.png}... {w} ...на такой девушке, как я?"
        $herViewHead.hideQ()
        m "Хм?"
        $herViewHead.showQ( "body_118.png", posHead )
        her2 "Я имею в виду, после всего того, что произошло со мной... ах{image=textheart.png}..."
        her "Я чувствую себя грязной... ущербной."
        her "И не могу смыть с себя всё это..."
        $herViewHead.showQ( "body_117.png", posHead )
        her "Кто же захочет такую жену?"
        $herViewHead.hideQ()
        menu:
            m "..."
            "\"Я бы женился на тебе по велению сердца!\"":
                $herViewHead.showQ( "body_31.png", posHead )
                her "ЧТО?"
                $herViewHead.hideQ()
                m "Ну, гипотетически конечно..."
                $herViewHead.showQ( "body_54.png", posHead )
                her "...конечно...{image=textheart.png}"
                $herViewHead.showQ( "body_53.png", posHead )
                her ".............."
                $herViewHead.showQ( "body_55.png", posHead )
                her "Но почему вы так сказали, сэр?"
                $herViewHead.hideQ()
                m "Ммм?"
                m "Что ты имеешь в виду под словом \"почему\", сучка?"
                m "Ты молода и привлекательна..."
                m "Узкая задница, хорошие сиськи и мокрая киска..."
                $herViewHead.showQ( "body_127.png", posHead )
                her "Ах...{image=textheart.png}"
                $herViewHead.hideQ()
                m "Однажды, ты осчастливишь какого-нибудь везунчика, шлюха."
                m "Эм, в смысле, мисс Грейнджер."
                $herViewHead.showQ( "body_134.png", posHead )
                her2 "Нет, \"шлюха\" лучше звучит. Называйте меня так, сэр."
                $herViewHead.hideQ()
                m "Вот, видишь? Ты схватываешь всё на лету, шлюха."
                $herViewHead.showQ( "body_134.png", posHead )
                her "Ах...{image=textheart.png} Спасибо, сэр."
                $herViewHead.hideQ()
                m "А?"
                m "Ты плачешь?"
                label among_other_things:
                $herViewHead.showQ( "body_133.png", posHead )
                her "Между прочим, сэр...{image=textheart.png}{image=textheart.png}{image=textheart.png}"
                $herViewHead.hideQ()
                m "Между прочим?"
                $herViewHead.showQ( "body_135.png", posHead )
                her "Я кончаю, сэр...{image=textheart.png}{image=textheart.png}{image=textheart.png}"
                $herViewHead.hideQ()
                g4 "Ааа! Мой член!" 
                g4 "Немного расслабься там!"
                $herViewHead.showQ( "body_131.png", posHead )
                her "НО Я КОНЧАЮ!{image=textheart.png}{image=textheart.png}{image=textheart.png}"
                $herViewHead.hideQ()
                g4 "Отлично, тогда кончай, шлюха!"
                with hpunch
                $herViewHead.showQ( "body_130.png", posHead )
                her "{size=+7}Ааааа!!! Я кончаю!!!{/size}"
                $herViewHead.hideQ()
                g4 "{size=+7}Аррр!{/size}"
                
            "\"Свадьба не для тебя.\"":
                $herViewHead.showQ( "body_143.png", posHead )
                her "Вот о чем я и думала..."
                $herViewHead.hideQ()
                m "Ооо... Мне просто нравится твоя маленькая и узкая задница!"
                $herViewHead.showQ( "body_142.png", posHead )
                her "....................."
                her2 "Да... После всего того, что мне пришлось сделать для своего факультета..."
                $herViewHead.showQ( "body_145.png", posHead )
                her "...никто не захочет меня..."
                $herViewHead.hideQ()
                m "Ооо, они захотят тебя!"
                $herViewHead.showQ( "body_144.png", posHead )
                her "Что? Но вы сказали..."
                $herViewHead.hideQ()
                m "Свадьба, малышка. Свадьба не для тебя."
                m "Но как шлюха, удовлетворяющая мужчин - ты шикарна!"
                $herViewHead.showQ( "body_144.png", posHead )
                her "Правда?"
                $herViewHead.hideQ()
                m "Ты шутишь?!"
                m "Юная, горячая, ненасытная! Да ты можешь иметь всё, что захочешь!"
                m "Магия и всё, что можешь пожелать..."
                $herViewHead.showQ( "body_157.png", posHead )
                her "Наверно, вы правы, Сэр."
                $herViewHead.hideQ()
                m "Я знаю, что я прав, потаскуха."
                m "А сейчас, поработай немного своей попкой."
                $herViewHead.showQ( "body_138.png", posHead )
                her "Вот так?"
                $herViewHead.hideQ()
                m  "Да, именно так, шлюха."
                $herViewHead.showQ( "body_133.png", posHead )
                her "Я потаскуха, да?"
                $herViewHead.hideQ()
                m "Ты только что продала мне свою задницу за 90 очков. Как ты себя после этого назовёшь?"
                $herViewHead.showQ( "body_138.png", posHead )
                her "Да, даааа...{image=textheart.png} Я шлюха...{image=textheart.png}"
                $herViewHead.hideQ()
                m "Ты плачешь?"
                jump among_other_things
                
        menu:
            g4 "!!!"
            "- Кончить в Гермиону -":
                $herViewHead.showQ( "body_130.png", posHead )
                her "!!!"
                $herViewHead.hideQ()
                m "Да! арррр!"
                $herViewHead.showQ( "body_134.png", posHead )
                her "Ах!{image=textheart.png} Вы заполняете меня!{image=textheart.png} Я чувствую!{image=textheart.png}"
                $herViewHead.hideQ()
                m "Заткнись, сучка!"
                $herViewHead.showQ( "body_137.png", posHead )
                her "Ах! Я потаскуха!!!!{image=textheart.png}{image=textheart.png}{image=textheart.png}"
                $herViewHead.hideQ()
                m "Арр!"
                $herViewHead.showQ( "body_144.png", posHead )
                her "Ах...{image=textheart.png} вы кончаете, сэр...{image=textheart.png}"
                $herViewHead.hideQ()
                m "ДА, ОООО ДА..."
                $herViewHead.showQ( "body_145.png", posHead )
                her "Ааа...{image=textheart.png}"
                $herViewHead.hideQ()
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
                #$herViewHead.data().addItemKey( 'sperm', CharacterExItem( herViewHead.mMiscFolder, "sperm_05.png", G_Z_FACE + 1 ) )
                $herViewHead.data().addItem( 'item_sperm', '05' )
                $herViewHead.showQ( "body_133.png", posHead )
                her "Ааа! Вы кончаете! {image=textheart.png}{image=textheart.png}{image=textheart.png}"
                $herViewHead.hideQ()
                g4 "{size=+7}Вот именно, шлюха!{/size}"
                $herViewHead.showQ( "body_147.png", posHead )
                her "Ааа, я тоже! Я тоже!"
                $herViewHead.hideQ()
                g4 "{size=+7}Долбаная потаскуха!{/size}"
                $herViewHead.showQ( "body_142.png", posHead )
                her "Аааа...{image=textheart.png} ваша сперма...{image=textheart.png}"
                her "Так много...{image=textheart.png}{image=textheart.png}{image=textheart.png}"


                $herViewHead.hideQ()
                g4 "ДА!!! Всё на твоей заднице!"
                $herViewHead.showQ( "body_134.png", posHead )
                her "Ах... Такая горячая!"
                $herViewHead.hideQ()

                
                $herViewHead.hideQ()
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
        m "Ну, это было здорово..."
        $herViewHead.showQ( "body_158.png", posHead )
        her "Ах-ах...{image=textheart.png} a...{image=textheart.png}"
        $herViewHead.hideQ()
        m "Как ты, малышка?"
        $herViewHead.showQ( "body_158.png", posHead )
        her "Я думаю... Я не уверена..."
        $herViewHead.showQ( "body_158.png", posHead )
        her "Я, видимо, ещё кончаю..., Сэр."
        $herViewHead.showQ( "body_158.png", posHead )
        her "А может, и нет..."
        her "Всё как в тумане... и мои ноги... я еле хожу..."
        her "Мы можем рассчитаться, сэр?"
        $herViewHead.hideQ()

        
    
    stop music fadeout 1.0
    
    if herViewHead.data().getItem( 'item_sperm' ) != None:
        $herViewHead.data().addItem( 'item_sperm_dried' )
        #$herViewHead.data().addItemKey( 'sperm_after', CharacterExItem( herViewHead.mMiscFolder, "sperm_00_after.png", G_Z_FACE + 1 ) )
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
    m "Да, мисс Грейнджер, 90 очков \"Гриффиндору\"." 
    $ gryffindor +=90
    $herView.showQ( "body_141.png", pos )
    hide screen hermione_01_f #Hermione stands still.
    with d3
    her "Спасибо, сэр..."

    if hermi.whoring <= 23: # Level 08 <
        $ hermi.whoring +=1

#    if request_31_points == 0:
#        $ new_request_31_01 = True # HEARTS.
#    if request_31_points == 1:
#        $ new_request_31_02 = True # HEARTS.
#    if request_31_points >= 2:
#        $ new_request_31_03 = True # HEARTS.


#    $ request_31_points += 1


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
   

    



