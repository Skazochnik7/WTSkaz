
###############################################################################################################################
### LEVEL 09 ##################################################################################################################
###################REQUEST_31 (Level 08) (75 pt.) (Anal sex).  #####################################################
label new_request_31: #LV.8 (Whoring = 21 - 23)
    #__#hide screen hermione_main 
    #__#with d3
    $herView.hideQQ()
    m "{size=-4}(Должен ли я попросить её заняться со мной анальным сексом?){/size}"
    $ menu_x = 0.5 #Default position of the menu (0.5). Version B is $ menu_x = 0.2
    menu:
        "\"(Да, давай!)\"":
            show screen blktone
            with d3
            pass
        "\"(Не сейчас.)\"":
            jump new_personal_request
 
    $ pos = POS_140
    $ posHead = gMakePos( 390, 340 )
    $ herView.data().saveState()
 
    if request_31_points == 0: # FIRST EVENT <============================================================== EVENT 01
        m "Мисс Грейнджер..."
        #__#hide screen hermione_main                                                                                                                                                                                   #HERMIONE
        #__#with d3                                                                                                                                                                                                                        #HERMIONE
        $herView.hideQQ()
        #__#$ h_xpos=140 #Defines position of the Hermione's full length sprite. (Default 370). (Center: 140)                                                       #HERMIONE
        #__#$ h_body = "03_hp/13_hermione_main/body_17.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
        #__#show screen hermione_main                                                                                                                                                                                 #HERMIONE
        #__#with d3                         
        $herView.showQQ( "body_17.png", pos )
        her "Сэр..?"
        m "Насколько вы знакомы с термином \"Анальный секс\"?"
        if whoring <=20:
            jump too_much
        #__#hide screen hermione_main                                                                                                                                                                                   #HERMIONE
        #__#with d3                                                                                                                                                                                                                        #HERMIONE
        $herView.hideQQ()
        #__#$ h_xpos=140 #Defines position of the Hermione's full length sprite. (Default 370). (Center: 140)                                                       #HERMIONE
        #__#$ h_body = "03_hp/13_hermione_main/body_79.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
        #__#show screen hermione_main                                                                                                                                                                                 #HERMIONE
        #__#with d3                         
        $herView.showQQ( "body_79.png", pos )
        her "90 очков..."
        m "Что?"
        #__#hide screen hermione_main                                                                                                                                                                                   #HERMIONE
        #__#with d3                                                                                                                                                                                                                        #HERMIONE
        $herView.hideQQ()
        #__#$ h_xpos=140 #Defines position of the Hermione's full length sprite. (Default 370). (Center: 140)                                                       #HERMIONE
        #__#$ h_body = "03_hp/13_hermione_main/body_66.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
        #__#show screen hermione_main                                                                                                                                                                                 #HERMIONE
        #__#with d3                                                                                                                                                                                                                        #HERMIONE          
        $herView.showQQ( "body_66.png", pos )
        her "............................."
        m "Хорошо, пусть будет так. 90 очков."
        #__#hide screen hermione_main   
        $herView.hideQ() #"WARNING_Z"
        
        
        label lucky_guess:
            
        show screen blkfade
        with d3
        
        stop music fadeout 1.0
        
        #__#$ her_head_xpos=390 #Defines position of the Hermione's full length sprite. (Default 370). 140 - center. Bottom right: 390
        #__#$ her_head_ypos=340 #Defines position of the Hermione's full length sprite. (Default 0). Right bottom corner: 340 - head only. 235 - tits.
        #__#$ posHead = gMakePos( 390, 340 )
        #__#show screen h_head2                                                             # HERMIONE
        $herViewHead.showQ( "body_29.png", posHead )
        #__#$ h_body = "03_hp/13_hermione_main/body_29.png" # HERMIONE
        her "..........."
        #__#hide screen h_head2      
        $herViewHead.hideQ()
        m "Давай посмотрим..."
        #__#show screen h_head2                                                             # HERMIONE
        $herViewHead.showQ( "body_34.png", posHead )
        #__#$ h_body = "03_hp/13_hermione_main/body_34.png" # HERMIONE
        her "................."
        #__#hide screen h_head2      
        $herViewHead.hideQ()
        m "Хм..."
        #__#show screen h_head2                                                             # HERMIONE
        $herViewHead.showQ( "body_18.png", posHead )
        #__#$ h_body = "03_hp/13_hermione_main/body_18.png" # HERMIONE
        her "!!!"
        #__#hide screen h_head2      
        $herViewHead.hideQ()
        g4 "Да ладно...!"
        #__#show screen h_head2                                                             # HERMIONE
        $herViewHead.showQ( "body_20.png", posHead )
        #__#$ h_body = "03_hp/13_hermione_main/body_20.png" # HERMIONE
        her "АЙ!"
        #__#hide screen h_head2      
        $herViewHead.hideQ()
        m "Просто постарайся расслабиться немного, хорошо?"
        #__#show screen h_head2                                                             # HERMIONE
        $herViewHead.showQ( "body_21.png", posHead )
        #__#$ h_body = "03_hp/13_hermione_main/body_21.png" # HERMIONE
        her "Я стараюсь!"
        #__#hide screen h_head2      
        $herViewHead.hideQ()
        m "Хорошо, что если я сделаю так..?"
        #__#show screen h_head2                                                             # HERMIONE
        $herViewHead.showQ( "body_20.png", posHead )
        #__#$ h_body = "03_hp/13_hermione_main/body_20.png" # HERMIONE
        her "АЙ! Что вы делаете, cэр?"
        #__#hide screen h_head2      
        $herViewHead.hideQ()
        m "Ладно, это не сработает..."
        m "Хм..."
        m "Хорошо, я знаю что мы сделаем."
        menu:
            m "..."
            "\"Хорошо, попробую всунуть член и посильнее войти!\"":
                play music "music/(Orchestral) Playful Tension by Shadow16nh.mp3" fadein 1 fadeout 1 # SEX THEME.
                #__#show screen h_head2                                                             # HERMIONE
                $herViewHead.showQ( "body_18.png", posHead )
                #__#$ h_body = "03_hp/13_hermione_main/body_18.png" # HERMIONE
                her "Посильнее войти, cэр?!"
                #__#hide screen h_head2      
                $herViewHead.hideQ()
                $ renpy.play('sounds/spit.mp3') #Sound of spiting. 
                g3 "*Хлоп!*"
                #__#show screen h_head2                                                             # HERMIONE
                $herViewHead.showQ( "body_32.png", posHead )
                #__#$ h_body = "03_hp/13_hermione_main/body_32.png" # HERMIONE
                her "Ааааааааааааааайййййй!"
                #__#show screen h_head2                                                             # HERMIONE
                $herViewHead.showQ( "body_31.png", posHead )
                #__#$ h_body = "03_hp/13_hermione_main/body_31.png" # HERMIONE
                her2 "Нет, cэр, подождите! Может быть, я просто расслаблюсь-"
                #__#hide screen h_head2      
                $herViewHead.hideQ()
                m "Не надо, я уже вхожу!"
                with hpunch
                #__#show screen h_head2                                                             # HERMIONE
                $herViewHead.showQ( "body_22.png", posHead )
                #__#$ h_body = "03_hp/13_hermione_main/body_22.png" # HERMIONE
                her "ААААА!"
                #__#show screen h_head2                                                             # HERMIONE
                $herViewHead.showQ( "body_20.png", posHead )
                #__#$ h_body = "03_hp/13_hermione_main/body_20.png" # HERMIONE
                her "АЙ! АЙ! АЙ!"
                #__#hide screen h_head2      
                $herViewHead.hideQ()
                g4 "Почти вошёл!"
                #__#show screen h_head2                                                             # HERMIONE
                $herViewHead.showQ( "body_32.png", posHead )
                #__#$ h_body = "03_hp/13_hermione_main/body_32.png" # HERMIONE
                her "Нет, мне больно! Мне больно!"
                #__#hide screen h_head2      
                $herViewHead.hideQ()
                g4 "Почти! Почти!"
                #__#show screen h_head2                                                             # HERMIONE
                $herViewHead.showQ( "body_32.png", posHead )
                #__#$ h_body = "03_hp/13_hermione_main/body_32.png" # HERMIONE
                her "АЙ! Больно!"
                #__#hide screen h_head2      
                $herViewHead.hideQ()
                g4 "Заткнись, девченка! Я делаю тебе одолжение!"
                g4 "Твой анус такой узкий и почти невозможно тебя трахнуть в задницу, а я исправляю это!"
                #__#show screen h_head2                                                             # HERMIONE
                $herViewHead.showQ( "body_20.png", posHead )
                #__#$ h_body = "03_hp/13_hermione_main/body_20.png" # HERMIONE
                her "Тогда остановитесь, пожалуйста!"
                #__#hide screen h_head2      
                $herViewHead.hideQ()
                m "Нет! Нам нужно расширить твою дырочку!"
                #__#show screen h_head2                                                             # HERMIONE
                $herViewHead.showQ( "body_20.png", posHead )
                #__#$ h_body = "03_hp/13_hermione_main/body_20.png" # HERMIONE
                her "Но я не хочу, что бы вы это делали!"
                #__#hide screen h_head2      
                $herViewHead.hideQ()
                m "Правда? Как ты тогда думаешь, люди буду иметь тебя в задницу?"
                #__#show screen h_head2                                                             # HERMIONE
                $herViewHead.showQ( "body_132.png", posHead )
                #__#$ h_body = "03_hp/13_hermione_main/body_132.png" # HERMIONE
                her "Какие люди?"
                #__#hide screen h_head2      
                $herViewHead.hideQ()
                g4 "Ну ты знаешь... люди."
                g4 "Аааа, черт... Моему члену теперь тоже больно...."
                #__#show screen h_head2                                                             # HERMIONE
                $herViewHead.showQ( "body_131.png", posHead )
                #__#$ h_body = "03_hp/13_hermione_main/body_131.png" # HERMIONE
                her "Остановитесь тогда! Остановитесь, сэр!"
                her "Я передумала! Мне не нужно 90 баллов!"
                #__#hide screen h_head2      
                $herViewHead.hideQ()
                g4 "Помоему я почти..."
                
                $ renpy.play('sounds/gltch.mp3')
                with hpunch
                with kissiris
                #__#show screen h_head2                                                             # HERMIONE
                $herViewHead.showQ( "body_130.png", posHead )
                #__#$ h_body = "03_hp/13_hermione_main/body_130.png" # HERMIONE
                her2 "{size=+5}Ааааай!!!{/size}"
                #__#hide screen h_head2
                $herViewHead.hideQ()
                g4 "Да!!!"
                #__#show screen h_head2                                                             # HERMIONE
                $herViewHead.showQ( "body_130.png", posHead )
                #__#$ h_body = "03_hp/13_hermione_main/body_130.png" # HERMIONE
                her "AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA!"
                #__#hide screen h_head2
                $herViewHead.hideQ()
                g4 "Давай наполним эту маленькую дырочку спермой?"
                #__#show screen h_head2                                                             # HERMIONE
                $herViewHead.showQ( "body_137.png", posHead )
                #__#$ h_body = "03_hp/13_hermione_main/body_137.png" # HERMIONE
                her "ДА... Пожалуйста, я уже хочу закончить это..."
                #__#hide screen h_head2
                $herViewHead.hideQ()




                #__#hide screen hermione_main                                                                                                                                                                                   #HERMIONE
                $herView.hideQ() #"WARNING_Z"
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
                #__#show screen h_head2                                                             # HERMIONE
                $herViewHead.showQ( "body_139.png", posHead )
                #__#$ h_body = "03_hp/13_hermione_main/body_139.png" # HERMIONE
                her "*всхлип* Как?"
                #__#hide screen h_head2       
                $herViewHead.hideQ()
                g4 "Ты знаешь..."
                #__#show screen h_head2                                                             # HERMIONE
                $herViewHead.showQ( "body_139.png", posHead )
                #__#$ h_body = "03_hp/13_hermione_main/body_139.png" # HERMIONE
                her "Ох..."
                #__#show screen h_head2                                                             # HERMIONE
                $herViewHead.showQ( "body_140.png", posHead )
                #__#$ h_body = "03_hp/13_hermione_main/body_140.png" # HERMIONE
                her "Я шлюха??"
                #__#hide screen h_head2    
                $herViewHead.hideQ()
                g9 "Да, вот кто ты!"
                #__#show screen h_head2                                                             # HERMIONE
                $herViewHead.showQ( "body_141.png", posHead )
                #__#$ h_body = "03_hp/13_hermione_main/body_141.png" # HERMIONE
                her "*Хнык!* Я шлюха..."
                her "Я люблю сосать члены..."
                #__#show screen h_head2                                                             # HERMIONE
                $herViewHead.showQ( "body_142.png", posHead )
                #__#$ h_body = "03_hp/13_hermione_main/body_142.png" # HERMIONE
                her2 "И моя узкая дырочка сейчас будет разорвана на части... *Хнык!*"
                #__#hide screen h_head2    
                $herViewHead.hideQ()
                g4 "Да! Даа!"
                g4 "Аааа! Да!"
                #__#show screen h_head2                                                             # HERMIONE
                $herViewHead.showQ( "body_144.png", posHead )
                #__#$ h_body = "03_hp/13_hermione_main/body_144.png" # HERMIONE
                her "Нет! Он ещё больше вырос во мне?! Я боюсь!"
                #__#hide screen h_head2    
                $herViewHead.hideQ()
                g4 "Аааа!"

                
            "\"Отсоси сначала у меня, смажь мой член!\"":
                #__#show screen h_head2                                                             # HERMIONE
                $herViewHead.showQ( "body_31.png", posHead )
                #__#$ h_body = "03_hp/13_hermione_main/body_31.png" # HERMIONE
                her "Аа... Хорошо..."
                #__#hide screen h_head2    
                $herViewHead.hideQ()
                play music "music/(Orchestral) Playful Tension by Shadow16nh.mp3" fadein 1 fadeout 1 # SEX THEME.
                #SUCKING
                
                hide screen blkfade
                
                
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
                        
                
                
                
                
                
                
                
                her "*Хлюп-хлюп-хлюп-хлюп!*"
                #__#hide screen h_head2    
                $herViewHead.hideQ()
                m "Да... хорошо..."
                her "*Хлюп!* *Хлюп!* *Хлюп!*"
                #__#hide screen h_head2    
                $herViewHead.hideQ()
                m "Отлично. Думаю, достаточно. Ложись обратно на стол."
                show screen blkfade
                with d3

                
                #ON THE DESK
                #__#show screen h_head2                                                             # HERMIONE
                $herViewHead.showQ( "body_31.png", posHead )
                #__#$ h_body = "03_hp/13_hermione_main/body_31.png" # HERMIONE
                her "............."
                #__#hide screen h_head2    
                $herViewHead.hideQ()
                g4 "Да! Почти!"
                #__#show screen h_head2                                                             # HERMIONE
                $herViewHead.showQ( "body_32.png", posHead )
                #__#$ h_body = "03_hp/13_hermione_main/body_32.png" # HERMIONE
                her "Ау!"
                #__#hide screen h_head2    
                $herViewHead.hideQ()
                m "Расслабся. Почти вошёл."
                
                $ renpy.play('sounds/gltch.mp3')
                with hpunch
                with kissiris
                #__#show screen h_head2                                                             # HERMIONE
                $herViewHead.showQ( "body_130.png", posHead )
                #__#$ h_body = "03_hp/13_hermione_main/body_130.png" # HERMIONE
                her2 "{size=+5}AAAAAAAA!!!{/size}"
                #__#hide screen h_head2
                $herViewHead.hideQ()
                g4 "ДА!!!"
                #__#show screen h_head2                                                             # HERMIONE
                $herViewHead.showQ( "body_130.png", posHead )
                #__#$ h_body = "03_hp/13_hermione_main/body_130.png" # HERMIONE
                her "Моя... моя..."
                #__#show screen h_head2                                                             # HERMIONE
                $herViewHead.showQ( "body_132.png", posHead )
                #__#$ h_body = "03_hp/13_hermione_main/body_132.png" # HERMIONE
                her "Больно!"
                #__#hide screen h_head2
                $herViewHead.hideQ()
                g4 "Давай заполним эту дырочку спермой до отказа?"
                #__#show screen h_head2                                                             # HERMIONE
                $herViewHead.showQ( "body_141.png", posHead )
                #__#$ h_body = "03_hp/13_hermione_main/body_141.png" # HERMIONE
                her "....................."
                #__#hide screen h_head2               
                $herViewHead.hideQ()
                
                # SEX
                
                #__#hide screen hermione_main                                                                                                                                                                                   #HERMIONE
                $herView.hideQ() #"WARNING_Z"
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


                #__#show screen h_head2                                                             # HERMIONE
                $herViewHead.showQ( "body_139.png", posHead )
                #__#$ h_body = "03_hp/13_hermione_main/body_139.png" # HERMIONE
                her "....................."
                #__#hide screen h_head2    
                $herViewHead.hideQ()
                m "Как ты, шлюшка?"
                #__#show screen h_head2                                                             # HERMIONE
                $herViewHead.showQ( "body_140.png", posHead )
                #__#$ h_body = "03_hp/13_hermione_main/body_140.png" # HERMIONE
                her2 "Ааа... Вы... разорвали меня изнутри... сэр."
                #__#show screen h_head2                                                             # HERMIONE
                $herViewHead.showQ( "body_141.png", posHead )
                #__#$ h_body = "03_hp/13_hermione_main/body_141.png" # HERMIONE
                her "И до сих пор болит..."
                #__#hide screen h_head2    
                $herViewHead.hideQ()
                m "Хм..."
                m "Может, было недостаточно смазки...?"
                m "Успокойся, девочка. Пососи мой член ещё."
                #__#show screen h_head2                                                             # HERMIONE
                $herViewHead.showQ( "body_140.png", posHead )
                #__#$ h_body = "03_hp/13_hermione_main/body_140.png" # HERMIONE
                her "Что? Но..."
                #__#show screen h_head2                                                             # HERMIONE
                $herViewHead.showQ( "body_139.png", posHead )
                #__#$ h_body = "03_hp/13_hermione_main/body_139.png" # HERMIONE
                her "Он грязный... Он уже был в моей попке."
                #__#hide screen h_head2    
                $herViewHead.hideQ()
                m "Да, он был в тебе, но это не означает, что он уже грязный."
                m "Раслабься, девочка. Соси давай."
                #__#show screen h_head2                                                             # HERMIONE
                $herViewHead.showQ( "body_139.png", posHead )
                #__#$ h_body = "03_hp/13_hermione_main/body_139.png" # HERMIONE
                her "..........."
                #__#hide screen h_head2   
                $herViewHead.hideQ()
                show screen blkfade
                with d3
                
                
                #SUCKING
                
                hide screen blkfade
                
                
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
                
                
                
                
                her "*Хлюп!* *Хлюп!* *Хлюп!*"
                m "Да... хорошо..."
                her "*Чавк!* *Чавк!* *Чавк!*"
                m "Чувствуешь вкус своей попки на моём члене?"
                her "*Чавк!* *Хлюп!* *Чавк!*"
                m "Ладно, может хватит."
                show screen blkfade
                with d3
               

                
                #ON DESK AGAIN.
                
                
                #__#hide screen hermione_main                                                                                                                                                                                   #HERMIONE
                $herView.hideQ() #"WARNING_Z"
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
                
                #__#show screen h_head2                                                             # HERMIONE
                $herViewHead.showQ( "body_139.png", posHead )
                #__#$ h_body = "03_hp/13_hermione_main/body_139.png" # HERMIONE
                her "Ах..."
                #__#hide screen h_head2     
                $herViewHead.hideQ()
                m "Уже лучше?"
                #__#show screen h_head2                                                             # HERMIONE
                $herViewHead.showQ( "body_140.png", posHead )
                #__#$ h_body = "03_hp/13_hermione_main/body_140.png" # HERMIONE
                her "Всё ещё больно..."
                her "Но, думаю, всё будет в порядке..."
                #__#hide screen h_head2     
                $herViewHead.hideQ()
                m "Тогда я буду входить помедленнее..."
                #__#show screen h_head2                                                             # HERMIONE
                $herViewHead.showQ( "body_141.png", posHead )
                #__#$ h_body = "03_hp/13_hermione_main/body_141.png" # HERMIONE
                her "Ах... спасибо, сэр."
                #__#hide screen h_head2     
                $herViewHead.hideQ()
                m "О... да... вот так лучше... да..."
                #__#show screen h_head2                                                             # HERMIONE
                $herViewHead.showQ( "body_139.png", posHead )
                #__#$ h_body = "03_hp/13_hermione_main/body_139.png" # HERMIONE
                her "..........."
                #__#hide screen h_head2     
                $herViewHead.hideQ()
                m "Ммм...да... Такая узкая..."
                #__#show screen h_head2                                                             # HERMIONE
                $herViewHead.showQ( "body_143.png", posHead )
                #__#$ h_body = "03_hp/13_hermione_main/body_143.png" # HERMIONE
                her "................"
                #__#hide screen h_head2     
                $herViewHead.hideQ()
                m "Почему ты замолчала, девочка?"
                #__#show screen h_head2                                                             # HERMIONE
                $herViewHead.showQ( "body_140.png", posHead )
                #__#$ h_body = "03_hp/13_hermione_main/body_140.png" # HERMIONE
                her "Просто это больно..."
                her2 "И я просто хочу, что бы вы поскорее кончили, сэр..."
                #__#hide screen h_head2     
                $herViewHead.hideQ()
                m "Ты пытаешься сдержать слёзы от боли?"
                #__#show screen h_head2                                                             # HERMIONE
                $herViewHead.showQ( "body_142.png", posHead )
                #__#$ h_body = "03_hp/13_hermione_main/body_142.png" # HERMIONE
                her "Да, сэр. *Хнык!*"
                #__#hide screen h_head2     
                $herViewHead.hideQ()
                m "Не надо сдерживаться."
                m "Плачь, кричи, рыдай столько, сколько захочешь!"
                #__#show screen h_head2                                                             # HERMIONE
                $herViewHead.showQ( "body_140.png", posHead )
                #__#$ h_body = "03_hp/13_hermione_main/body_140.png" # HERMIONE
                her "Н-но--"
                #__#hide screen h_head2     
                $herViewHead.hideQ()
                m "Тогда я кончу быстрее."
                #__#show screen h_head2                                                             # HERMIONE
                $herViewHead.showQ( "body_142.png", posHead )
                #__#$ h_body = "03_hp/13_hermione_main/body_142.png" # HERMIONE
                her "Правда? *Хнык!*"
                #__#show screen h_head2                                                             # HERMIONE
                $herViewHead.showQ( "body_139.png", posHead )
                #__#$ h_body = "03_hp/13_hermione_main/body_139.png" # HERMIONE
                her2 "*Хнык!* Больно! *Хнык!* Как же это больно! *Хнык!*"
                #__#hide screen h_head2     
                $herViewHead.hideQ()
                m "Да, ещё..."
                #__#show screen h_head2                                                             # HERMIONE
                $herViewHead.showQ( "body_145.png", posHead )
                #__#$ h_body = "03_hp/13_hermione_main/body_145.png" # HERMIONE
                her "*Хнык!*"
                #__#hide screen h_head2     
                $herViewHead.hideQ()
                m "Бедное, маленькое дитя..."
                m "Большой и злой человек разрывает твою узкую задницу своим членом!"
                #__#show screen h_head2                                                             # HERMIONE
                $herViewHead.showQ( "body_146.png", posHead )
                #__#$ h_body = "03_hp/13_hermione_main/body_146.png" # HERMIONE
                her "*Хнык!* Дааааа! *Хнык!*"
                #__#hide screen h_head2     
                $herViewHead.hideQ()
                g4 "О-да!"
                #__#show screen h_head2                                                             # HERMIONE
                $herViewHead.showQ( "body_147.png", posHead )
                #__#$ h_body = "03_hp/13_hermione_main/body_147.png" # HERMIONE
                her "Нет, мне страшно! *Хнык!*"
                #__#hide screen h_head2   
                $herViewHead.hideQ()
        
        menu:
            "- Заполнить Гермиону спермой -":
                g4 "Оооо!"
                #__#show screen h_head2                                                             # HERMIONE
                $herViewHead.showQ( "body_130.png", posHead )
                #__#$ h_body = "03_hp/13_hermione_main/body_130.png" # HERMIONE  
                her "Нет! АХ!"
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
                #__#$ uni_sperm = True
                #__#$ u_sperm = "03_hp/13_hermione_main/auto_08.png"
                $herViewHead.data().addItem( 'sperm', CharacterExItem( herViewHead.mMiscFolder, "sperm_05.png", G_Z_FACE + 1 ) )
                #__#show screen h_head2                                                             # HERMIONE
                $herViewHead.showQ( "body_144.png", posHead )
                #__#$ h_body = "03_hp/13_hermione_main/body_144.png" # HERMIONE
                her "ААА! Я ЧУВСТВУЮ КАК ВЫ МЕНЯ ЗАПОЛНЯЕТЕ !{image=textheart.png}{image=textheart.png}{image=textheart.png}"
                #__#hide screen h_head2  
                $herViewHead.hideQ()
                
                
                g4 "ДА, ТЫ ПОТАСКУХА! ДАА!"
                #__#show screen h_head2                                                             # HERMIONE
                $herViewHead.showQ( "body_145.png", posHead )
                #__#$ h_body = "03_hp/13_hermione_main/body_145.png" # HERMIONE
                her "БОЛЬНО, БОЛЬНО!"
                #__#hide screen h_head2         
                $herViewHead.hideQ()
                g4 "Заткнись!"
                with hpunch
                #__#show screen h_head2                                                             # HERMIONE
                $herViewHead.showQ( "body_149.png", posHead )
                #__#$ h_body = "03_hp/13_hermione_main/body_149.png" # HERMIONE
                her2 "Нет, в меня больше не влезет! Перестаньте кончать, ВЫ! УБЛЮДОК!"
                #__#hide screen h_head2      
                $herViewHead.hideQ()
                g4 "Закрой пасть, шлюха! Я ещё не закончил!"
                #__#show screen h_head2                                                             # HERMIONE
                $herViewHead.showQ( "body_146.png", posHead )
                #__#$ h_body = "03_hp/13_hermione_main/body_146.png" # HERMIONE
                her "Нет! Пожалуйста! АААА, МОЙ ЖИВОТ! Я СЕЙЧАС ЛОПНУ!"
                #__#hide screen h_head2   
                $herViewHead.hideQ()
                g4 "ААА!"
                #__#show screen h_head2                                                             # HERMIONE
                $herViewHead.showQ( "body_144.png", posHead )
                #__#$ h_body = "03_hp/13_hermione_main/body_144.png" # HERMIONE
                her "Нет! Я сейчас взорвусь..."
                #__#hide screen h_head2    
                $herViewHead.hideQ()
                with hpunch
                #__#show screen h_head2                                                             # HERMIONE
                $herViewHead.showQ( "body_150.png", posHead )
                #__#$ h_body = "03_hp/13_hermione_main/body_150.png" # HERMIONE
                play sound "sounds/burp.mp3"
                her "{size=+7}*ХЛЮП!*!!!!!{/size}"
                #__#show screen h_head2                                                             # HERMIONE
                $herViewHead.showQ( "body_151.png", posHead )
                #__#$ h_body = "03_hp/13_hermione_main/body_151.png" # HERMIONE
                her "......................."
                her "............."
                #__#show screen h_head2                                                             # HERMIONE
                $herViewHead.showQ( "body_126.png", posHead )
                #__#$ h_body = "03_hp/13_hermione_main/body_126.png" # HERMIONE
                $ renpy.play('sounds/gulp.mp3') #Sound of gulping down a liquid.
                her "{size=+7}*ХЛЮП!*{/size}"  
                #__#show screen h_head2                                                             # HERMIONE
                $herViewHead.showQ( "body_145.png", posHead )
                #__#$ h_body = "03_hp/13_hermione_main/body_145.png" # HERMIONE
                her "*Хнык!* Я НЕНАВИЖУ ВАС..."
                #__#show screen h_head2                                                             # HERMIONE
                $herViewHead.showQ( "body_148.png", posHead )
                #__#$ h_body = "03_hp/13_hermione_main/body_148.png" # HERMIONE
                her2 "{size=+5}Я НЕНАВИЖУ ВАС И ВАШ ГРЯЗНЫЙ СТАРЫЙ ЧЛЕН!{/size}"
                her "{size=+5}Я НЕНАВИЖУ ВАС! ВЫ СЛЫШИТЕ МЕНЯ?!{/size}"
                #__#hide screen h_head2   
                $herViewHead.hideQ()
                g4 "Аррр... Заткнись, шлюха!"
                #__#show screen h_head2                                                             # HERMIONE
                $herViewHead.showQ( "body_145.png", posHead )
                #__#$ h_body = "03_hp/13_hermione_main/body_145.png" # HERMIONE
                her "*Хнык!* *Хнык!*..."
                #__#hide screen h_head2
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
                #__#show screen h_head2                                                             # HERMIONE
                $herViewHead.showQ( "body_142.png", posHead )
                #__#$ h_body = "03_hp/13_hermione_main/body_142.png" # HERMIONE
                her "*Хнык!*..."
                #__#hide screen h_head2
                $herViewHead.hideQ()
                m "УАУ!... Думаю я закончил."
                m "Ты в порядке?"
                #__#show screen h_head2                                                             # HERMIONE
                $herViewHead.showQ( "body_142.png", posHead )
                #__#$ h_body = "03_hp/13_hermione_main/body_142.png" # HERMIONE
                her "Да... *Хнык!*"
                #__#hide screen h_head2 
                $herViewHead.hideQ()
                m "Ты плачешь?"
                #__#show screen h_head2                                                             # HERMIONE
                $herViewHead.showQ( "body_142.png", posHead )
                #__#$ h_body = "03_hp/13_hermione_main/body_142.png" # HERMIONE
                her "Моя попка болит, но я в порядке, сэр..."
                #__#hide screen h_head2 
                $herViewHead.hideQ()
                m "Ну, я должен сказать, что ты стойко приняла мой член..."
                #__#show screen h_head2                                                             # HERMIONE
                $herViewHead.showQ( "body_142.png", posHead )
                #__#$ h_body = "03_hp/13_hermione_main/body_142.png" # HERMIONE
                her "Спасибо, сэр..."
                #__#hide screen h_head2 
                $herViewHead.hideQ()

                hide screen bld1
                with d3
                show screen ctc
                pause
                hide screen ctc
                show screen blkfade
                with d7
                #__#show screen h_head2                                                             # HERMIONE
                $herViewHead.showQ( "body_152.png", posHead )
                #__#$ h_body = "03_hp/13_hermione_main/body_152.png" # HERMIONE
                her "Извините, что я сказала, что ненавижу вас, сэр..."
                her "И ваш ненасытный член..."
                #__#show screen h_head2                                                             # HERMIONE
                $herViewHead.showQ( "body_153.png", posHead )
                #__#$ h_body = "03_hp/13_hermione_main/body_153.png" # HERMIONE
                her "Не знаю, что на меня нашло..."
                #__#hide screen h_head2
                $herViewHead.hideQ()
                g9 "Мой член!"
                #__#show screen h_head2                                                             # HERMIONE
                $herViewHead.showQ( "body_153.png", posHead )
                #__#$ h_body = "03_hp/13_hermione_main/body_153.png" # HERMIONE
                her2 "Думаю, это произошло тогда, когда вы меня назвали \"шлюхой\". Я знаю, вы не это имели ввиду..."
                #__#hide screen h_head2    
                $herViewHead.hideQ()
                m "Да, конечно..."
                m "Всё ещё болит?"
                #__#show screen h_head2                                                             # HERMIONE
                $herViewHead.showQ( "body_154.png", posHead )
                #__#$ h_body = "03_hp/13_hermione_main/body_154.png" # HERMIONE  
                her "Немного..."
                #__#show screen h_head2                                                             # HERMIONE
                $herViewHead.showQ( "body_155.png", posHead )
                #__#$ h_body = "03_hp/13_hermione_main/body_155.png" # HERMIONE
                her "До сих пор ощущаю внутри горячую сперму..."
                #__#hide screen h_head2      
                $herViewHead.hideQ()
                m "Ты собираешься так её и оставить? Ну, я имею в виду - сперму."
                #__#show screen h_head2                                                             # HERMIONE
                $herViewHead.showQ( "body_156.png", posHead )
                #__#$ h_body = "03_hp/13_hermione_main/body_156.png" # HERMIONE     
                her "Да..."
                if daytime:
                    her2 "Надеюсь, она не будет хлюпать, пока я сижу на занятиях..."
                else:
                    her2 "Надеюсь, она не будет хлюпать, пока я иду в свою комнату..."
                #__#hide screen h_head2 
                $herViewHead.hideQ()
                m "Ну, тогда - удачно добраться."
                #__#show screen h_head2                                                             # HERMIONE
                $herViewHead.showQ( "body_155.png", posHead )
                #__#$ h_body = "03_hp/13_hermione_main/body_155.png" # HERMIONE  
                her "Мы можем расчитаться?"
                #__#hide screen h_head2 
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
                #__#$ uni_sperm = True
                #__#$ u_sperm = "03_hp/13_hermione_main/auto_08.png"
                $herViewHead.data().addItem( 'sperm', CharacterExItem( herViewHead.mMiscFolder, "sperm_05.png", G_Z_FACE + 1 ) )
                #__#show screen h_head2                                                             # HERMIONE
                $herViewHead.showQ( "body_133.png", posHead )
                #__#$ h_body = "03_hp/13_hermione_main/body_133.png" # HERMIONE
                her2 "Аа...{image=textheart.png}{image=textheart.png}{image=textheart.png}"

                #__#hide screen h_head2     
                $herViewHead.hideQ()
                g4 "Да!!! Всё на твоей попке!"
                #__#show screen h_head2                                                             # HERMIONE
                $herViewHead.showQ( "body_134.png", posHead )
                #__#$ h_body = "03_hp/13_hermione_main/body_134.png" # HERMIONE
                her "Оуу... Она горячая!"
                #__#hide screen h_head2          
                $herViewHead.hideQ()

                
                #__#hide screen h_head2     
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
                #__#show screen h_head2                                                             # HERMIONE
                $herViewHead.showQ( "body_138.png", posHead )
                #__#$ h_body = "03_hp/13_hermione_main/body_138.png" # HERMIONE
                her "Да, сэр..."
                #__#hide screen h_head2     
                $herViewHead.hideQ()
                m "Ты как?"
                #__#show screen h_head2                                                             # HERMIONE
                $herViewHead.showQ( "body_139.png", posHead )
                #__#$ h_body = "03_hp/13_hermione_main/body_139.png" # HERMIONE
                her "Всё ещё больновато, сэр. Но..."
                #__#hide screen h_head2     
                $herViewHead.hideQ()
                m "Что - \"Но\"...?"
                #__#show screen h_head2                                                             # HERMIONE
                $herViewHead.showQ( "body_138.png", posHead )
                #__#$ h_body = "03_hp/13_hermione_main/body_138.png" # HERMIONE
                her "Но мне даже понравилось... сэр."
                #__#hide screen h_head2     
                $herViewHead.hideQ()
                m "Понравилось??"
                g9 "Хах... А ты, видимо, маленькая мазохистка."
                #__#show screen h_head2                                                             # HERMIONE
                $herViewHead.showQ( "body_138.png", posHead )
                #__#$ h_body = "03_hp/13_hermione_main/body_138.png" # HERMIONE
                her "Мы можем расчитаться, сэр?"
                #__#hide screen h_head2 
                $herViewHead.hideQ()

        
    elif request_31_points == 1: # FIRST EVENT <============================================================== EVENT 02
        m "Девочка?"
        #__#hide screen hermione_main                                                                                                                                                                                   #HERMIONE
        #__#with d3                                                                                                                                                                                                                        #HERMIONE
        $herView.hideQQ()
        #__#$ h_xpos=140 #Defines position of the Hermione's full length sprite. (Default 370). (Center: 140)                                                       #HERMIONE
        #__#$ h_body = "03_hp/13_hermione_main/body_15.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
        #__#show screen hermione_main                                                                                                                                                                                 #HERMIONE
        #__#with d3                                                                                                                                                                                                                        #HERMIONE                     
        $herView.showQQ( "body_15.png", pos )
        her "Профессор?"
        m "Я куплю сегодня у тебя другую услугу..."
        #__#hide screen hermione_main                                                                                                                                                                                   #HERMIONE
        #__#with d3                                                                                                                                                                                                                        #HERMIONE
        $herView.hideQQ()
        #__#$ h_xpos=140 #Defines position of the Hermione's full length sprite. (Default 370). (Center: 140)                                                       #HERMIONE
        #__#$ h_body = "03_hp/13_hermione_main/body_08.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
        #__#show screen hermione_main                                                                                                                                                                                 #HERMIONE
        #__#with d3                                                                                                                                                                                                                        #HERMIONE    
        $herView.showQQ( "body_08.png", pos )
        her "............."
        m "Попытайся догадаться, что это будет?"
        m "У тебя три попытки."
        #__#hide screen hermione_main                                                                                                                                                                                   #HERMIONE
        #__#with d3                                                                                                                                                                                                                        #HERMIONE
        $herView.hideQQ()
        #__#$ h_xpos=140 #Defines position of the Hermione's full length sprite. (Default 370). (Center: 140)                                                       #HERMIONE
        #__#$ h_body = "03_hp/13_hermione_main/body_09.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
        #__#show screen hermione_main                                                                                                                                                                                 #HERMIONE
        #__#with d3                                                                                                                                                                                                                        #HERMIONE    
        $herView.showQQ( "body_09.png", pos )
        her "..........."
        #__#hide screen hermione_main                                                                                                                                                                                   #HERMIONE
        #__#with d3                                                                                                                                                                                                                        #HERMIONE
        $herView.hideQQ()
        #__#$ h_xpos=140 #Defines position of the Hermione's full length sprite. (Default 370). (Center: 140)                                                       #HERMIONE
        #__#$ h_body = "03_hp/13_hermione_main/body_66.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
        #__#show screen hermione_main                                                                                                                                                                                 #HERMIONE
        #__#with d3                                                                                                                                                                                                                        #HERMIONE    
        $herView.showQQ( "body_66.png", pos )
        her "Анальный секс?"
        g4 "Что..........?!"
        g4 "Как ты...?"
        #__#hide screen hermione_main                                                                                                                                                                                   #HERMIONE
        #__#with d3                                                                                                                                                                                                                        #HERMIONE
        $herView.hideQQ()
        #__#$ h_xpos=140 #Defines position of the Hermione's full length sprite. (Default 370). (Center: 140)                                                       #HERMIONE
        #__#$ h_body = "03_hp/13_hermione_main/body_47.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
        #__#show screen hermione_main                                                                                                                                                                                 #HERMIONE
        #__#with d3                                                                                                                                                                                                                        #HERMIONE    
        $herView.showQQ( "body_47.png", pos )
        her "Просто повезло, сэр..."
        m "Иногда ты меня пугаешь, девочка..."
        #__#hide screen hermione_main                                                                                                                                                                                   #HERMIONE
        #__#with d3 
        $herView.hideQQ()
        jump lucky_guess
        
        
        
        
        
    elif request_31_points >= 2: # FIRST EVENT <============================================================== EVENT 03
        m "Как насчет повторить анальный секс, малышка?"
        #__#hide screen hermione_main                                                                                                                                                                                   #HERMIONE
        #__#with d3                                                                                                                                                                                                                        #HERMIONE
        $herView.hideQQ()
        #__#$ h_xpos=140 #Defines position of the Hermione's full length sprite. (Default 370). (Center: 140)                                                       #HERMIONE
        #__#$ h_body = "03_hp/13_hermione_main/body_17.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
        #__#show screen hermione_main                                                                                                                                                                                 #HERMIONE
        #__#with d3                                                                                                                                                                                                                        #HERMIONE     
        $herView.showQQ( "body_17.png", pos )
        her "Как насчет ещё 90 баллов, сэр?"
        g9 "Иди сюда, маленькая мазохистка!"
        #__#hide screen hermione_main     
        #__#with d3
        $herView.hideQQ()
        # SEX
        show screen blkfade
        with d3
        
        stop music fadeout 1.0
        
        #__#$ her_head_xpos=390 #Defines position of the Hermione's full length sprite. (Default 370). 140 - center. Bottom right: 390
        #__#$ her_head_ypos=340 #Defines position of the Hermione's full length sprite. (Default 0). Right bottom corner: 340 - head only. 235 - tits.
        #__#$ posHead = gMakePos( 390, 340 )
        #__#show screen h_head2                                                             # HERMIONE
        $herViewHead.showQ( "body_29.png", posHead )
        #__#$ h_body = "03_hp/13_hermione_main/body_29.png" # HERMIONE
        her "........"
        #__#hide screen h_head2               
        $herViewHead.hideQ()
        m "Хм..."
        #__#show screen h_head2                                                             # HERMIONE
        $herViewHead.showQ( "body_31.png", posHead )
        #__#$ h_body = "03_hp/13_hermione_main/body_31.png" # HERMIONE
        her "..........."
        #__#hide screen h_head2
        $herViewHead.hideQ()
        
        
        $ renpy.play('sounds/gltch.mp3')
        with hpunch
        with kissiris
        #__#show screen h_head2                                                             # HERMIONE
        $herViewHead.showQ( "body_130.png", posHead )
        #__#$ h_body = "03_hp/13_hermione_main/body_130.png" # HERMIONE
        her2 "Оооооооо....{image=textheart.png}"
        #__#hide screen h_head2
        $herViewHead.hideQ()
        g4 "О, дааа!"
        #__#show screen h_head2                                                             # HERMIONE
        $herViewHead.showQ( "body_121.png", posHead )
        #__#$ h_body = "03_hp/13_hermione_main/body_121.png" # HERMIONE
        her "Ах..."
        #__#hide screen h_head2
        $herViewHead.hideQ()
        m "Сегодня я легче вхожу в твою дырочку."
        #__#show screen h_head2                                                             # HERMIONE
        $herViewHead.showQ( "body_128.png", posHead )
        #__#$ h_body = "03_hp/13_hermione_main/body_128.png" # HERMIONE
        her "Ах... До сих пор больновато...."
        #__#show screen h_head2                                                             # HERMIONE
        $herViewHead.showQ( "body_129.png", posHead )
        #__#$ h_body = "03_hp/13_hermione_main/body_129.png" # HERMIONE
        her "И, пожалуйста, называйте меня \"шлюхой\", сэр."
        #__#hide screen h_head2
        $herViewHead.hideQ()
        g4 "Аррр! Ты потаскуха! Мне всегда нравится, когда ты так говоришь!"



        
        
        
        
        #__#hide screen hermione_main                                                                                                                                                                                   #HERMIONE
        $herView.hideQ() #"WARNING_Z"
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
        #__#show screen h_head2                                                             # HERMIONE
        $herViewHead.showQ( "body_127.png", posHead )
        #__#$ h_body = "03_hp/13_hermione_main/body_127.png" # HERMIONE
        her "Ах... Ах..."
        her "Ах..."
        #__#show screen h_head2                                                             # HERMIONE
        $herViewHead.showQ( "body_128.png", posHead )
        #__#$ h_body = "03_hp/13_hermione_main/body_128.png" # HERMIONE
        her "Сэр?"
        #__#hide screen h_head2
        $herViewHead.hideQ()
        m "Да, шлюшка?"
        #__#show screen h_head2                                                             # HERMIONE
        $herViewHead.showQ( "body_117.png", posHead )
        #__#$ h_body = "03_hp/13_hermione_main/body_117.png" # HERMIONE
        her "Эм..."
        #__#hide screen h_head2
        $herViewHead.hideQ()
        hide screen ctc
        #__#show screen h_head2                                                             # HERMIONE
        $herViewHead.showQ( "body_118.png", posHead )
        #__#$ h_body = "03_hp/13_hermione_main/body_118.png" # HERMIONE
        her "Вы возьмете меня в жены, сэр?"
        #__#hide screen h_head2
        $herViewHead.hideQ()
        with hpunch
        g4 "{size=+9} ЧТО?!{/size}"
        g4 "Только не говори мне, что ты беременна!"
        #__#show screen h_head2                                                             # HERMIONE
        $herViewHead.showQ( "body_122.png", posHead )
        #__#$ h_body = "03_hp/13_hermione_main/body_122.png" # HERMIONE
        her2 "Я не могу забеременеть от того, что вы трахаете меня в попку..."
        #__#hide screen h_head2
        $herViewHead.hideQ()
        m "Тогда какие разговоры о свадьбе?"
        #__#show screen h_head2                                                             # HERMIONE
        $herViewHead.showQ( "body_117.png", posHead )
        #__#$ h_body = "03_hp/13_hermione_main/body_117.png" # HERMIONE
        her "Вы не поняли меня, сэр."
        #__#show screen h_head2                                                             # HERMIONE
        $herViewHead.showQ( "body_118.png", posHead )
        #__#$ h_body = "03_hp/13_hermione_main/body_118.png" # HERMIONE
        her "Я хочу узнать, могли бы вы взять в жены {size=+5}такую девушку{/size} как Я?"
        #__#show screen h_head2                                                             # HERMIONE
        $herViewHead.showQ( "body_34.png", posHead )
        #__#$ h_body = "03_hp/13_hermione_main/body_34.png" # HERMIONE
        her2 "Я никогда не предалагала ни одному мужчине трахнуть меня в попку, сэр..."
        #__#hide screen h_head2
        $herViewHead.hideQ()
        m "Хорошо. Потому что я думаю, что нормальный мужчина ответит тебе \"нет\" в такой момент."
        #__#show screen h_head2                                                             # HERMIONE
        $herViewHead.showQ( "body_127.png", posHead )
        #__#$ h_body = "03_hp/13_hermione_main/body_127.png" # HERMIONE
        her "Ах{image=textheart.png}..."
        #__#show screen h_head2                                                             # HERMIONE
        $herViewHead.showQ( "body_118.png", posHead )
        #__#$ h_body = "03_hp/13_hermione_main/body_118.png" # HERMIONE
        her2 "Я имела ввиду... ах{image=textheart.png} {w} ...хотела сказать{image=textheart.png}... {w}...как вы думаете, кто нибудь женится{image=textheart.png}... {w} ...на такой девушке, как я?"
        #__#hide screen h_head2
        $herViewHead.hideQ()
        m "Хм?"
        #__#show screen h_head2                                                             # HERMIONE
        $herViewHead.showQ( "body_118.png", posHead )
        #__#$ h_body = "03_hp/13_hermione_main/body_118.png" # HERMIONE
        her2 "Я имею в виду, после всего того, что произошло со мной... ах{image=textheart.png}..."
        her "Я чувствую себя грязной... ущербной."
        her "И не могу смыть с себя всё это..."
        #__#show screen h_head2                                                             # HERMIONE
        $herViewHead.showQ( "body_117.png", posHead )
        #__#$ h_body = "03_hp/13_hermione_main/body_117.png" # HERMIONE
        her "Кто же захочет такую жену?"
        #__#hide screen h_head2  
        $herViewHead.hideQ()
        menu:
            m "..."
            "\"Я бы женился на тебе по велению сердца!\"":
                #__#show screen h_head2                                                             # HERMIONE
                $herViewHead.showQ( "body_31.png", posHead )
                #__#$ h_body = "03_hp/13_hermione_main/body_31.png" # HERMIONE
                her "ЧТО?"
                #__#hide screen h_head2  
                $herViewHead.hideQ()
                m "Ну, гипотетически конечно..."
                #__#show screen h_head2                                                             # HERMIONE
                $herViewHead.showQ( "body_54.png", posHead )
                #__#$ h_body = "03_hp/13_hermione_main/body_54.png" # HERMIONE
                her "...конечно...{image=textheart.png}"
                #__#show screen h_head2                                                             # HERMIONE
                $herViewHead.showQ( "body_53.png", posHead )
                #__#$ h_body = "03_hp/13_hermione_main/body_53.png" # HERMIONE
                her ".............."
                #__#show screen h_head2                                                             # HERMIONE
                $herViewHead.showQ( "body_55.png", posHead )
                #__#$ h_body = "03_hp/13_hermione_main/body_55.png" # HERMIONE
                her "Но почему вы так сказали, сэр?"
                #__#hide screen h_head2  
                $herViewHead.hideQ()
                m "Ммм?"
                m "Что ты имеешь ввиду под словом \"почему\", сучка?"
                m "Ты молода и привлекательна..."
                m "Узкая задница, хорошие сиськи и мокрая киска..."
                #__#show screen h_head2                                                             # HERMIONE
                $herViewHead.showQ( "body_127.png", posHead )
                #__#$ h_body = "03_hp/13_hermione_main/body_127.png" # HERMIONE
                her "Ах...{image=textheart.png}"
                #__#hide screen h_head2  
                $herViewHead.hideQ()
                m "Однажды, ты осчастливишь какого-нибудь везунчика, шлюха."
                m "Эм, всмысле, мисс Грейнджер."
                #__#show screen h_head2                                                             # HERMIONE
                $herViewHead.showQ( "body_134.png", posHead )
                #__#$ h_body = "03_hp/13_hermione_main/body_134.png" # HERMIONE
                her2 "Нет, \"шлюха\" лучше звучит. Называйте меня так, сэр."
                #__#hide screen h_head2  
                $herViewHead.hideQ()
                m "Вот, видишь? Ты схватываешь всё на лету, шлюха."
                #__#show screen h_head2                                                             # HERMIONE
                $herViewHead.showQ( "body_134.png", posHead )
                #__#$ h_body = "03_hp/13_hermione_main/body_142.png" # HERMIONE
                her "Ах...{image=textheart.png} Спасибо, сэр."
                #__#hide screen h_head2  
                $herViewHead.hideQ()
                m "А?"
                m "Ты плачешь?"
                label among_other_things:
                #__#show screen h_head2                                                             # HERMIONE
                $herViewHead.showQ( "body_133.png", posHead )
                #__#$ h_body = "03_hp/13_hermione_main/body_133.png" # HERMIONE
                her "Между прочим, сэр...{image=textheart.png}{image=textheart.png}{image=textheart.png}"
                #__#hide screen h_head2  
                $herViewHead.hideQ()
                m "Между прочим?"
                #__#show screen h_head2                                                             # HERMIONE
                $herViewHead.showQ( "body_135.png", posHead )
                #__#$ h_body = "03_hp/13_hermione_main/body_135.png" # HERMIONE
                her "Я кончаю, сэр...{image=textheart.png}{image=textheart.png}{image=textheart.png}"
                #__#hide screen h_head2  
                $herViewHead.hideQ()
                g4 "Ааа! Мой член!" 
                g4 "Немного расслабься там!"
                #__#show screen h_head2                                                             # HERMIONE
                $herViewHead.showQ( "body_131.png", posHead )
                #__#$ h_body = "03_hp/13_hermione_main/body_131.png" # HERMIONE
                her "НО Я КОНЧАЮ!{image=textheart.png}{image=textheart.png}{image=textheart.png}"
                #__#hide screen h_head2  
                $herViewHead.hideQ()
                g4 "Отлично, тогда кончай, шлюха!"
                with hpunch
                #__#show screen h_head2                                                             # HERMIONE
                $herViewHead.showQ( "body_130.png", posHead )
                #__#$ h_body = "03_hp/13_hermione_main/body_130.png" # HERMIONE
                her "{size=+7}Ааааа!!! Я кончаю!!!{/size}"
                #__#hide screen h_head2  
                $herViewHead.hideQ()
                g4 "{size=+7}Аррр!{/size}"
                
            "\"Свадьба не для тебя.\"":
                #__#show screen h_head2                                                             # HERMIONE
                $herViewHead.showQ( "body_143.png", posHead )
                #__#$ h_body = "03_hp/13_hermione_main/body_143.png" # HERMIONE
                her "Вот о чем я и думала..."
                #__#hide screen h_head2  
                $herViewHead.hideQ()
                m "Ооо... Мне просто нравится твоя маленькая и узкая задница!"
                #__#show screen h_head2                                                             # HERMIONE
                $herViewHead.showQ( "body_142.png", posHead )
                #__#$ h_body = "03_hp/13_hermione_main/body_142.png" # HERMIONE
                her "....................."
                her2 "Да... После всего того, что мне пришлось сделать для своего факультета..."
                #__#show screen h_head2                                                             # HERMIONE
                $herViewHead.showQ( "body_145.png", posHead )
                #__#$ h_body = "03_hp/13_hermione_main/body_145.png" # HERMIONE
                her "...никто не захочет меня..."
                #__#hide screen h_head2  
                $herViewHead.hideQ()
                m "Ооо, они захотят тебя!"
                #__#show screen h_head2                                                             # HERMIONE
                $herViewHead.showQ( "body_144.png", posHead )
                #__#$ h_body = "03_hp/13_hermione_main/body_144.png" # HERMIONE
                her "Что? Но вы сказали..."
                #__#hide screen h_head2  
                $herViewHead.hideQ()
                m "Свадьба, малышка. Свадьба не для тебя."
                m "Но как шлюха, удовлетворяющая мужчин - ты шикарна!"
                #__#show screen h_head2                                                             # HERMIONE
                $herViewHead.showQ( "body_144.png", posHead )
                #__#$ h_body = "03_hp/13_hermione_main/body_144.png" # HERMIONE
                her "Правда?"
                #__#hide screen h_head2  
                $herViewHead.hideQ()
                m "Ты шутишь?!"
                m "Юная, горячая, ненасытная! Да ты можешь иметь всё, что захочешь!"
                m "Магия и всё, что можешь пожелать..."
                #__#show screen h_head2                                                             # HERMIONE
                $herViewHead.showQ( "body_157.png", posHead )
                #__#$ h_body = "03_hp/13_hermione_main/body_157.png" # HERMIONE
                her "Наверно, вы правы, Сэр."
                #__#hide screen h_head2  
                $herViewHead.hideQ()
                m "Я знаю, что я прав, потаскуха."
                m "А сейчас, поработай немного своей попкой."
                #__#show screen h_head2                                                             # HERMIONE
                $herViewHead.showQ( "body_138.png", posHead )
                #__#$ h_body = "03_hp/13_hermione_main/body_138.png" # HERMIONE
                her "Вот так?"
                #__#hide screen h_head2  
                $herViewHead.hideQ()
                m  "Да, именно так, шлюха."
                #__#show screen h_head2                                                             # HERMIONE
                $herViewHead.showQ( "body_133.png", posHead )
                #__#$ h_body = "03_hp/13_hermione_main/body_133.png" # HERMIONE
                her "Я потаскуха, да?"
                #__#hide screen h_head2  
                $herViewHead.hideQ()
                m "Ты только что продала мне свою задницу за 90 очков. Как ты себя после этого назовёшь?"
                #__#show screen h_head2                                                             # HERMIONE
                $herViewHead.showQ( "body_138.png", posHead )
                #__#$ h_body = "03_hp/13_hermione_main/body_138.png" # HERMIONE
                her "Да, даааа...{image=textheart.png} Я шлюха...{image=textheart.png}"
                #__#hide screen h_head2  
                $herViewHead.hideQ()
                m "Ты плачешь?"
                jump among_other_things
                
        menu:
            g4 "!!!"
            "- Кончить в Гермиону -":
                #__#show screen h_head2                                                             # HERMIONE
                $herViewHead.showQ( "body_130.png", posHead )
                #__#$ h_body = "03_hp/13_hermione_main/body_130.png" # HERMIONE
                her "!!!"
                #__#hide screen h_head2 
                $herViewHead.hideQ()
                m "Да! арррр!"
                #__#show screen h_head2                                                             # HERMIONE
                $herViewHead.showQ( "body_134.png", posHead )
                #__#$ h_body = "03_hp/13_hermione_main/body_134.png" # HERMIONE
                her "Ах!{image=textheart.png} Вы заполняете меня!{image=textheart.png} Я чувствую!{image=textheart.png}"
                #__#hide screen h_head2 
                $herViewHead.hideQ()
                m "Заткнись, сучка!"
                #__#show screen h_head2                                                             # HERMIONE
                $herViewHead.showQ( "body_137.png", posHead )
                #__#$ h_body = "03_hp/13_hermione_main/body_137.png" # HERMIONE
                her "Ах! Я потаскуха!!!!{image=textheart.png}{image=textheart.png}{image=textheart.png}"
                #__#hide screen h_head2 
                $herViewHead.hideQ()
                m "Арр!"
                #__#show screen h_head2                                                             # HERMIONE
                $herViewHead.showQ( "body_144.png", posHead )
                #__#$ h_body = "03_hp/13_hermione_main/body_144.png" # HERMIONE
                her "Ах...{image=textheart.png} вы кончаете, сэр...{image=textheart.png}"
                #__#hide screen h_head2 
                $herViewHead.hideQ()
                m "ДА, ОООО ДА..."
                #__#show screen h_head2                                                             # HERMIONE
                $herViewHead.showQ( "body_145.png", posHead )
                #__#$ h_body = "03_hp/13_hermione_main/body_145.png" # HERMIONE
                her "Ааа...{image=textheart.png}"
                #__#hide screen h_head2          
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
                #__#$ uni_sperm = True
                #__#$ u_sperm = "03_hp/13_hermione_main/auto_08.png"
                $herViewHead.data().addItem( 'sperm', CharacterExItem( herViewHead.mMiscFolder, "sperm_05.png", G_Z_FACE + 1 ) )
                #__#show screen h_head2                                                             # HERMIONE
                $herViewHead.showQ( "body_133.png", posHead )
                #__#$ h_body = "03_hp/13_hermione_main/body_133.png" # HERMIONE
                her "Ааа! Вы кончаете! {image=textheart.png}{image=textheart.png}{image=textheart.png}"
                #__#hide screen h_head2    
                $herViewHead.hideQ()
                g4 "{size=+7}Вот именно, шлюха!{/size}"
                #__#show screen h_head2                                                             # HERMIONE
                $herViewHead.showQ( "body_147.png", posHead )
                #__#$ h_body = "03_hp/13_hermione_main/body_147.png" # HERMIONE
                her "Ааа, я тоже! Я тоже!"
                #__#hide screen h_head2    
                $herViewHead.hideQ()
                g4 "{size=+7}Долбанная потаскуха!{/size}"
                #__#show screen h_head2                                                             # HERMIONE
                $herViewHead.showQ( "body_142.png", posHead )
                #__#$ h_body = "03_hp/13_hermione_main/body_142.png" # HERMIONE
                her "Аааа...{image=textheart.png} ваша сперма...{image=textheart.png}"
                her "Так много...{image=textheart.png}{image=textheart.png}{image=textheart.png}"


                #__#hide screen h_head2     
                $herViewHead.hideQ()
                g4 "ДА!!! Всё на твоей заднице!"
                #__#show screen h_head2                                                             # HERMIONE
                $herViewHead.showQ( "body_134.png", posHead )
                #__#$ h_body = "03_hp/13_hermione_main/body_134.png" # HERMIONE
                her "Ах... Такая горячая!"
                #__#hide screen h_head2          
                $herViewHead.hideQ()

                
                #__#hide screen h_head2     
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
        #__#show screen h_head2                                                             # HERMIONE
        $herViewHead.showQ( "body_158.png", posHead )
        #__#$ h_body = "03_hp/13_hermione_main/body_158.png" # HERMIONE
        her "Ах-ах...{image=textheart.png} a...{image=textheart.png}"
        #__#hide screen h_head2   
        $herViewHead.hideQ()
        m "Как ты, малышка?"
        #__#show screen h_head2                                                             # HERMIONE
        $herViewHead.showQ( "body_158.png", posHead )
        #__#$ h_body = "03_hp/13_hermione_main/body_158.png" # HERMIONE
        her "Я думаю... Я не уверена..."
        #__#show screen h_head2                                                             # HERMIONE
        $herViewHead.showQ( "body_158.png", posHead )
        #__#$ h_body = "03_hp/13_hermione_main/body_158.png" # HERMIONE
        her "Я, видимо, ещё кончаю..., Сэр."
        #__#show screen h_head2                                                             # HERMIONE
        $herViewHead.showQ( "body_158.png", posHead )
        #__#$ h_body = "03_hp/13_hermione_main/body_158.png" # HERMIONE
        her "А может и нет..."
        her "Всё как в тумане... и мои ноги... я еле хожу..."
        her "Мы можем рассчитаться, сэр?"
        #__#hide screen h_head2                                                             # HERMIONE
        $herViewHead.hideQ()

        
    
    stop music fadeout 1.0
    
    #__#$ uni_sperm = False #Sperm layer is not displayed in hermione screen.
    if herViewHead.data().getItem( 'sperm' ) != None:
        $herViewHead.data().addItem( 'sperm_after', CharacterExItem( herViewHead.mMiscFolder, "sperm_00_after.png", G_Z_FACE + 1 ) )
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
 
    m "Да, мисс Грейнджер, 90 очков \"Гриффиндору\"." 
    $ gryffindor +=90
    #__#$ h_xpos=140 #Defines position of the Hermione's full length sprite. (Default 370). (Center: 140)
    #__#$ h_body = "03_hp/13_hermione_main/body_141.png" #Flashing panties
    #__#show screen hermione_main
    $herView.showQ( "body_141.png", pos ) #"WARNING_Z"
    hide screen hermione_01_f #Hermione stands still.
    with d3
    her "Спасибо, сэр..."

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
   

    


