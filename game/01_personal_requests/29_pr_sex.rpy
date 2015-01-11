
    
    

###################REQUEST_29 (Level 07) (65 pt.) (Sex). #################################################################
label new_request_29: #LV.7 (Whoring = 18 - 20)

    #__#hide screen hermione_main 
    #__#with d3
    $herView.hideQQ()
    m "{size=-4}(Должен ли я попросить её заняться сексом со мной?){/size}"
    $ menu_x = 0.5 #Default position of the menu (0.5). Version B is $ menu_x = 0.2
    menu:
        "\"(Да, попросить!)\"":
            show screen blktone
            with d3
            pass
        "\"(Не сейчас.)\"":
            jump new_personal_request
            
    
    $ pos = POS_140
    $ posHead = gMakePos( 390, 340 )
    $herView.data().saveState()

    if request_29_points == 0: # FIRST EVENT <============================================================== EVENT 01
        m "Мисс Грейнджер?"
        #__#hide screen hermione_main                                                                                                                                                                                   #HERMIONE
        #__#with d3                                                                                                                                                                                                                        #HERMIONE
        $herView.hideQQ()
        #__#$ h_xpos=140 #Defines position of the Hermione's full length sprite. (Default 370). (Center: 140)                                                       #HERMIONE
        #__#$ h_body = "03_hp/13_hermione_main/body_01.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
        #__#show screen hermione_main                                                                                                                                                                                 #HERMIONE
        #__#with d3                         
        $herView.showQQ( "body_01.png", pos )
        her "Сэр?"
        m "Я бы хотел купить у вас сегодня..."
        #__#hide screen hermione_main                                                                                                                                                                                   #HERMIONE
        #__#with d3                                                                                                                                                                                                                        #HERMIONE
        $herView.hideQQ()
        #__#$ h_xpos=140 #Defines position of the Hermione's full length sprite. (Default 370). (Center: 140)                                                       #HERMIONE
        #__#$ h_body = "03_hp/13_hermione_main/body_06.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
        #__#show screen hermione_main                                                                                                                                                                                 #HERMIONE
        #__#with d3                         
        $herView.showQQ( "body_06.png", pos )
        her ".......?"
        m "Как бы более мягко выразиться...?"
        #__#hide screen hermione_main                                                                                                                                                                                   #HERMIONE
        #__#with d3                                                                                                                                                                                                                        #HERMIONE
        $herView.hideQQ()
        #__#$ h_xpos=140 #Defines position of the Hermione's full length sprite. (Default 370). (Center: 140)                                                       #HERMIONE
        #__#$ h_body = "03_hp/13_hermione_main/body_129.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
        #__#show screen hermione_main                                                                                                                                                                                 #HERMIONE
        #__#with d3                         
        $herView.showQQ( "body_129.png", pos )
        her "Занятся сексом, сэр?"
        m "Вообще-то -  да. Но как вы догадались...?"
        if whoring <=17:
            jump too_much
        #__#hide screen hermione_main                                                                                                                                                                                   #HERMIONE
        #__#with d3                                                                                                                                                                                                                        #HERMIONE
        $herView.hideQQ()
        #__#$ h_xpos=140 #Defines position of the Hermione's full length sprite. (Default 370). (Center: 140)                                                       #HERMIONE
        #__#$ h_body = "03_hp/13_hermione_main/body_128.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
        #__#show screen hermione_main                                                                                                                                                                                 #HERMIONE
        #__#with d3                         
        $herView.showQQ( "body_128.png", pos )
        her "Не сложно было догадаться..."
        m "Вы не будете возражать?"
        #__#hide screen hermione_main                                                                                                                                                                                   #HERMIONE
        #__#with d3                                                                                                                                                                                                                        #HERMIONE
        $herView.hideQQ()
        #__#$ h_xpos=140 #Defines position of the Hermione's full length sprite. (Default 370). (Center: 140)                                                       #HERMIONE
        #__#$ h_body = "03_hp/13_hermione_main/body_120.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
        #__#show screen hermione_main                                                                                                                                                                                 #HERMIONE
        #__#with d3                         
        $herView.showQQ( "body_120.png", pos )
        her "Кончено я буду возражать, сэр!"
        her "Я не проститутка!"
        m "Но всё равно сделаете это??"
        #__#hide screen hermione_main                                                                                                                                                                                   #HERMIONE
        #__#with d3                                                                                                                                                                                                                        #HERMIONE
        $herView.hideQQ()
        #__#$ h_xpos=140 #Defines position of the Hermione's full length sprite. (Default 370). (Center: 140)                                                       #HERMIONE
        #__#$ h_body = "03_hp/13_hermione_main/body_127.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
        #__#show screen hermione_main                                                                                                                                                                                 #HERMIONE
        #__#with d3                         
        $herView.showQQ( "body_127.png", pos )
        her2 "\"Гриффиндор\" снова на грани поражения..."
        her2 "И что, вы думаете, я должна делать?.."
        m "Отлично!"
        #__#hide screen hermione_main                                                                                                                                                                                 #HERMIONE
        $herView.hideQ() #"WARNING_Z"
       
        label your_ass:
            
        show screen blkfade 
        with d7
            
        stop music fadeout 1.0
        #__#$ her_head_xpos=390 #Defines position of the Hermione's full length sprite. (Default 370). 140 - center. Bottom right: 390
        #__#$ her_head_ypos=340 #Defines position of the Hermione's full length sprite. (Default 0). Right bottom corner: 340 - head only. 235 - tits.
        #__#$ posHead = gMakePos( 390, 340 )
        #__#show screen h_head2                                                             # HERMIONE
        $herViewHead.showQ( "body_120.png", posHead )
        #__#$ h_body = "03_hp/13_hermione_main/body_120.png" # HERMIONE
        her "............."
        #__#show screen h_head2                                                             # HERMIONE
        $herViewHead.showQ( "body_119.png", posHead )
        #__#$ h_body = "03_hp/13_hermione_main/body_119.png" # HERMIONE
        her "!!!!!!!!!!!!!!!"
        #__#hide screen h_head2                        
        $herViewHead.hideQ()
        m "Раслабься, девочка. Я только снимаю твои трусики."
        #__#show screen h_head2                                                             # HERMIONE
        $herViewHead.showQ( "body_49.png", posHead )
        #__#$ h_body = "03_hp/13_hermione_main/body_49.png" # HERMIONE
        her ".............."
        #__#hide screen h_head2                        
        $herViewHead.hideQ()
        m "Ты готова?"
        #__#show screen h_head2                                                             # HERMIONE
        $herViewHead.showQ( "body_50.png", posHead )
        #__#$ h_body = "03_hp/13_hermione_main/body_50.png" # HERMIONE
        her "Нет..."
        #__#hide screen h_head2                        
        $herViewHead.hideQ()
        m "Хорошая девочка."
        $ renpy.play('sounds/gltch.mp3')
        with hpunch
        with kissiris
        #__#show screen h_head2                                                             # HERMIONE
        $herViewHead.showQ( "body_130.png", posHead )
        #__#$ h_body = "03_hp/13_hermione_main/body_130.png" # HERMIONE
        her2 "Ааааааааааааааайййййй....{image=textheart.png}"
        #__#hide screen h_head2
        $herViewHead.hideQ()




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
            
            
            
            
        
        
        #FUCKING
        
        g4 "Твоя киска... Такая тугая."
        #__#show screen h_head2                                                             # HERMIONE
        $herViewHead.showQ( "body_33.png", posHead )
        #__#$ h_body = "03_hp/13_hermione_main/body_33.png" # HERMIONE
        her "................"
        #__#hide screen h_head2                       
        $herViewHead.hideQ()
        m "Ты как?"
        #__#show screen h_head2                                                             # HERMIONE
        $herViewHead.showQ( "body_21.png", posHead )
        #__#$ h_body = "03_hp/13_hermione_main/body_21.png" # HERMIONE
        her "Аа-а... Он такой большой..."
        her "Вы разорвете меня на части, сэр!"
        #__#hide screen h_head2        
        $herViewHead.hideQ()
        m "Ты что?! Мой член вполне нормальных размеров."
        m "Я не виноват, что твоя киска такая узкая."
        #__#show screen h_head2                                                             # HERMIONE
        $herViewHead.showQ( "body_33.png", posHead )
        #__#$ h_body = "03_hp/13_hermione_main/body_33.png" # HERMIONE
        her "......................"
        #__#hide screen h_head2         
        $herViewHead.hideQ()
        hide screen ctc
        menu:
            "\"Тебе должно быть стыдно за себя!\"":
                #__#show screen h_head2                                                             # HERMIONE
                $herViewHead.showQ( "body_33.png", posHead )
                #__#$ h_body = "03_hp/13_hermione_main/body_33.png" # HERMIONE
                her "Мне не стыдно, сэр!"
                her "Я делаю всё это для моего факультета...!"
                her "Что бы помочь моему...--"
                #__#show screen h_head2                                                             # HERMIONE
                $herViewHead.showQ( "body_131.png", posHead )
                #__#$ h_body = "03_hp/13_hermione_main/body_131.png" # HERMIONE
                her "А-а-а..."
                her "Мои однокурсники расчитывают на меня... а-а..."
                #__#hide screen h_head2  
                $herViewHead.hideQ()
                m "Ты уверена, что это единственная причина?"
                #__#show screen h_head2                                                             # HERMIONE
                $herViewHead.showQ( "body_33.png", posHead )
                #__#$ h_body = "03_hp/13_hermione_main/body_33.png" # HERMIONE
                her "Я не знаю..--"
                #__#show screen h_head2                                                             # HERMIONE
                $herViewHead.showQ( "body_131.png", posHead )
                #__#$ h_body = "03_hp/13_hermione_main/body_131.png" # HERMIONE
                her2 "А-а..."
                #__#show screen h_head2                                                             # HERMIONE
                $herViewHead.showQ( "body_118.png", posHead )
                #__#$ h_body = "03_hp/13_hermione_main/body_118.png" # HERMIONE
                her2 "Я не знаю, что вы имеете ввиду, сэр."
                #__#hide screen h_head2  
                $herViewHead.hideQ()
                m "Мне кажется, что ты наслаждаешься тем, чем мы с тобой занимаемся."
                #__#show screen h_head2                                                             # HERMIONE
                $herViewHead.showQ( "body_118.png", posHead )
                #__#$ h_body = "03_hp/13_hermione_main/body_118.png" # HERMIONE
                her "Нет, это не так, сэр!"
                #__#hide screen h_head2  
                $herViewHead.hideQ()
                m "Правда?"
                #__#show screen h_head2                                                             # HERMIONE
                $herViewHead.showQ( "body_33.png", posHead )
                #__#$ h_body = "03_hp/13_hermione_main/body_33.png" # HERMIONE
                her "......................"
                #__#hide screen h_head2  
                $herViewHead.hideQ()
                m "И ты говоришь это, когда твоя киска так течет?"
                #__#show screen h_head2                                                             # HERMIONE
                $herViewHead.showQ( "body_131.png", posHead )
                #__#$ h_body = "03_hp/13_hermione_main/body_131.png" # HERMIONE
                her "....................а-а.{image=textheart.png}"
                #__#hide screen h_head2  
                $herViewHead.hideQ()
                m "Признайся, ты наслаждаешься тем, что твой профессор трахает тебя!"
                #__#show screen h_head2                                                             # HERMIONE
                $herViewHead.showQ( "body_33.png", posHead )
                #__#$ h_body = "03_hp/13_hermione_main/body_33.png" # HERMIONE
                her "Нет, я не наслаждаюсь!"
                #__#hide screen h_head2  
                $herViewHead.hideQ()
                m "Упрямая девченка..."
                #__#show screen h_head2                                                             # HERMIONE
                $herViewHead.showQ( "body_131.png", posHead )
                #__#$ h_body = "03_hp/13_hermione_main/body_131.png" # HERMIONE
                her "Ааа...{image=textheart.png}" 
                #__#hide screen h_head2  
                $herViewHead.hideQ()
            "\"Так... Что нового у тебя?\"":
                #__#show screen h_head2                                                             # HERMIONE
                $herViewHead.showQ( "body_31.png", posHead )
                #__#$ h_body = "03_hp/13_hermione_main/body_31.png" # HERMIONE
                her "...Сэр?"
                #__#hide screen h_head2  
                $herViewHead.hideQ()
                m "Я стараюсь поддержать приятную беседу."
                #__#show screen h_head2                                                             # HERMIONE
                $herViewHead.showQ( "body_31.png", posHead )
                #__#$ h_body = "03_hp/13_hermione_main/body_31.png" # HERMIONE
                her "А-а... Но... а..."
                #__#hide screen h_head2  
                $herViewHead.hideQ()
                m "Как поживают твои родственники?"
                #__#show screen h_head2                                                             # HERMIONE
                $herViewHead.showQ( "body_34.png", posHead )
                #__#$ h_body = "03_hp/13_hermione_main/body_34.png" # HERMIONE
                her "Мои родители?"
                #__#show screen h_head2                                                             # HERMIONE
                $herViewHead.showQ( "body_131.png", posHead )
                #__#$ h_body = "03_hp/13_hermione_main/body_131.png" # HERMIONE
                her2 "Профессор, пожалуйста, я не могу сейчас говорить..."
                #__#hide screen h_head2  
                $herViewHead.hideQ()
                m "Почему же? Ты так этим наслаждаешься?"
                #__#show screen h_head2                                                             # HERMIONE
                $herViewHead.showQ( "body_131.png", posHead )
                #__#$ h_body = "03_hp/13_hermione_main/body_131.png" # HERMIONE
                her "Я не... ах...{image=textheart.png}"
                #__#hide screen h_head2  
                $herViewHead.hideQ()
                m "Я думаю, ты кайфуешь от этого."
                #__#show screen h_head2                                                             # HERMIONE
                $herViewHead.showQ( "body_131.png", posHead )
                #__#$ h_body = "03_hp/13_hermione_main/body_131.png" # HERMIONE
                her "Я всего лишь делаю это ради очков, сэр..."
                #__#hide screen h_head2  
                $herViewHead.hideQ()
                m "Ммм, ясно..."
                m "Получается ты - проститутка."
                #__#show screen h_head2                                                             # HERMIONE
                $herViewHead.showQ( "body_117.png", posHead )
                #__#$ h_body = "03_hp/13_hermione_main/body_117.png" # HERMIONE
                her "Что?"
                #__#hide screen h_head2  
                $herViewHead.hideQ()
                m "Я плачу тебе за секс. Как же ты это назовешь?"
                #__#show screen h_head2                                                             # HERMIONE
                $herViewHead.showQ( "body_118.png", posHead )
                #__#$ h_body = "03_hp/13_hermione_main/body_118.png" # HERMIONE
                her "..........."
                #__#show screen h_head2                                                             # HERMIONE
                $herViewHead.showQ( "body_131.png", posHead )
                #__#$ h_body = "03_hp/13_hermione_main/body_131.png" # HERMIONE
                her "Я не проститутка..."
                #__#show screen h_head2                                                             # HERMIONE
                $herViewHead.showQ( "body_21.png", posHead )
                #__#$ h_body = "03_hp/13_hermione_main/body_21.png" # HERMIONE
                her "Почему вы так жестоки со мной, сэр?"
                #__#hide screen h_head2  
                $herViewHead.hideQ()
                m "Мне кажется, тебе нравится, когда я более жесток с тобой."
                #__#show screen h_head2                                                             # HERMIONE
                $herViewHead.showQ( "body_67.png", posHead )
                #__#$ h_body = "03_hp/13_hermione_main/body_67.png" # HERMIONE
                her "Нет!"
                #__#hide screen h_head2  
                $herViewHead.hideQ()
                m "Правда? Тогда почему твоя киска такая влажная?"
                #__#show screen h_head2                                                             # HERMIONE
                $herViewHead.showQ( "body_118.png", posHead )
                #__#$ h_body = "03_hp/13_hermione_main/body_118.png" # HERMIONE
                her "Не из-за этого!"
                #__#hide screen h_head2  
                $herViewHead.hideQ()
                m "Ну, если ты так настаиваешь..."
                #__#show screen h_head2                                                             # HERMIONE
                $herViewHead.showQ( "body_131.png", posHead )
                #__#$ h_body = "03_hp/13_hermione_main/body_131.png" # HERMIONE
                her "А-ах...{image=textheart.png}"
                #__#show screen h_head2                                                             # HERMIONE
                $herViewHead.showQ( "body_132.png", posHead )
                #__#$ h_body = "03_hp/13_hermione_main/body_132.png" # HERMIONE
                her "Я ... ах...{image=textheart.png} не проститутка..."            
                #__#hide screen h_head2  
                $herViewHead.hideQ()
            "\"......................................................\"":
                #__#show screen h_head2                                                             # HERMIONE
                $herViewHead.showQ( "body_131.png", posHead )
                #__#$ h_body = "03_hp/13_hermione_main/body_131.png" # HERMIONE
                her "А-ах... ах..."
                #__#hide screen h_head2  
                $herViewHead.hideQ()
                m "*Дышит всё чаще!*"
                #__#show screen h_head2                                                             # HERMIONE
                $herViewHead.showQ( "body_131.png", posHead )
                #__#$ h_body = "03_hp/13_hermione_main/body_131.png" # HERMIONE
                her "Ах... а-ах..."
                #__#hide screen h_head2  
                $herViewHead.hideQ()
                m "Ох..."
                #__#show screen h_head2                                                             # HERMIONE
                $herViewHead.showQ( "body_131.png", posHead )
                #__#$ h_body = "03_hp/13_hermione_main/body_131.png" # HERMIONE
                her "Ах-аа..."
                #__#hide screen h_head2  
                $herViewHead.hideQ()
                m "......................"
                #__#show screen h_head2                                                             # HERMIONE
                $herViewHead.showQ( "body_131.png", posHead )
                #__#$ h_body = "03_hp/13_hermione_main/body_131.png" # HERMIONE
                her "Ах... а..."
                #__#show screen h_head2                                                             # HERMIONE
                $herViewHead.showQ( "body_31.png", posHead )
                #__#$ h_body = "03_hp/13_hermione_main/body_31.png" # HERMIONE
                her "Ах... Сэр?"
                #__#hide screen h_head2  
                $herViewHead.hideQ()
                m "Что такое?"
                #__#show screen h_head2                                                             # HERMIONE
                $herViewHead.showQ( "body_131.png", posHead )
                #__#$ h_body = "03_hp/13_hermione_main/body_131.png" # HERMIONE
                her "Ах... Вам.... нравится... это...?"
                #__#hide screen h_head2  
                $herViewHead.hideQ()
                m "Нравится ли мне долбить узкую и мокрую киску?"
                m "Очень, малышка. А что?"
                #__#show screen h_head2                                                             # HERMIONE
                $herViewHead.showQ( "body_33.png", posHead )
                #__#$ h_body = "03_hp/13_hermione_main/body_33.png" # HERMIONE
                her "....................."
                #__#show screen h_head2                                                             # HERMIONE
                $herViewHead.showQ( "body_131.png", posHead )
                #__#$ h_body = "03_hp/13_hermione_main/body_131.png" # HERMIONE
                her "Ах... Вы просто так внезапно замолчали..."
                #__#hide screen h_head2  
                $herViewHead.hideQ()
                m "Просто наслаждаюсь моментом, малышка."
                m "А как тебе ощущения? Ты в порядке?"
                #__#show screen h_head2                                                             # HERMIONE
                $herViewHead.showQ( "body_131.png", posHead )
                #__#$ h_body = "03_hp/13_hermione_main/body_131.png" # HERMIONE
                her "А... дааа..."
                #__#show screen h_head2                                                             # HERMIONE
                $herViewHead.showQ( "body_31.png", posHead )
                #__#$ h_body = "03_hp/13_hermione_main/body_31.png" # HERMIONE
                her "Немного больновато, ах..."
                #__#show screen h_head2                                                             # HERMIONE
                $herViewHead.showQ( "body_131.png", posHead )
                #__#$ h_body = "03_hp/13_hermione_main/body_131.png" # HERMIONE
                her "Ваш пенис слишком велик... ах..."
                #__#hide screen h_head2  
                $herViewHead.hideQ()
                m "Хм..."
                m "Ты хочешь, что бы я замедлился?"
                #__#show screen h_head2                                                             # HERMIONE
                $herViewHead.showQ( "body_31.png", posHead )
                #__#$ h_body = "03_hp/13_hermione_main/body_31.png" # HERMIONE
                her "Нет, сэр... Вам не стоит..."
                #__#show screen h_head2                                                             # HERMIONE
                $herViewHead.showQ( "body_33.png", posHead )
                #__#$ h_body = "03_hp/13_hermione_main/body_33.png" # HERMIONE
                her "Пожалуйста, не обращайте на меня внимания... Наслаждайтесь."
                her "Я... ах... привыкну к этому... ах..."
                #__#hide screen h_head2  
                $herViewHead.hideQ()
                m "Как пожелаешь, малышка."
                #__#show screen h_head2                                                             # HERMIONE
                $herViewHead.showQ( "body_131.png", posHead )
                #__#$ h_body = "03_hp/13_hermione_main/body_131.png" # HERMIONE
                her "Ах-a...{image=textheart.png}"
                #__#hide screen h_head2  
                $herViewHead.hideQ()

        m "Да, о да!"
        #__#show screen h_head2                                                             # HERMIONE
        $herViewHead.showQ( "body_131.png", posHead )
        #__#$ h_body = "03_hp/13_hermione_main/body_131.png" # HERMIONE
        her "Ах-а...{image=textheart.png}"
        #__#hide screen h_head2  
        $herViewHead.hideQ()
        if daytime:
            m "Собираешься вернуться в класс после того, как мы с тобой закончим?"
        else:
            m "Собираешься вернуться в кровать после того, как мы с тобой закончим?"
        #__#show screen h_head2                                                             # HERMIONE
        $herViewHead.showQ( "body_131.png", posHead )
        #__#$ h_body = "03_hp/13_hermione_main/body_131.png" # HERMIONE
        her "Да, ах...{image=textheart.png}"
        her "Если я вообще смогу ходить..."
        #__#hide screen h_head2  
        $herViewHead.hideQ()
        g4 "Хм! {image=textheart.png} Да, ты всегда знаешь, что говорить, девочка"
        #__#show screen h_head2                                                             # HERMIONE
        $herViewHead.showQ( "body_132.png", posHead )
        #__#$ h_body = "03_hp/13_hermione_main/body_132.png" # HERMIONE
        her "Ах...{image=textheart.png} ах...{image=textheart.png}{image=textheart.png}"
        with hpunch
        #__#show screen h_head2                                                             # HERMIONE
        $herViewHead.showQ( "body_130.png", posHead )
        #__#$ h_body = "03_hp/13_hermione_main/body_130.png" # HERMIONE
        her "{size=+7}!!!!!!!!!!!!!!!{/size}{image=textheart.png}{image=textheart.png}{image=textheart.png}"
        #__#hide screen h_head2  
        $herViewHead.hideQ()
        m "Ммм? Ты в порядке?"
        show screen blktone8
        with d3
        ">Ноги гермионы затрясись..."
        m "Девочка?"
        #__#show screen h_head2                                                             # HERMIONE
        $herViewHead.showQ( "body_130.png", posHead )
        #__#$ h_body = "03_hp/13_hermione_main/body_130.png" # HERMIONE
        her "{image=textheart.png}{image=textheart.png}{image=textheart.png}Мне кажется, я кончаю, сэр!{image=textheart.png}{image=textheart.png}{image=textheart.png}"
        #__#hide screen h_head2  
        $herViewHead.hideQ()
        g9 "Ха... Ты ненасытная сучка!"
        #__#show screen h_head2                                                             # HERMIONE
        $herViewHead.showQ( "body_133.png", posHead )
        #__#$ h_body = "03_hp/13_hermione_main/body_133.png" # HERMIONE
        her "АААА! Я больше не могу сдерживаться!"
        #__#hide screen h_head2  
        $herViewHead.hideQ()
        g4 "Тебя нужно наказать за это, грязная шлюха!"
        ">Вы натягиваете задницу Гермины всё сильнее и сильнее и трахаете её всё жестче и жестче!"
        $ g_c_u_pic = "sex2_ani"
        with hpunch
        #__#show screen h_head2                                                             # HERMIONE
        $herViewHead.showQ( "body_130.png", posHead )
        #__#$ h_body = "03_hp/13_hermione_main/body_130.png" # HERMIONE
        her "НЕТ! ОСТАНОВИТЕСЬ! ПОЖАЛУЙСТА!"
        #__#hide screen h_head2  
        $herViewHead.hideQ()
        g4 "Кто тебе разрешал кончать, шлюха? Вот твоё наказание!"
        #__#show screen h_head2                                                             # HERMIONE
        $herViewHead.showQ( "body_131.png", posHead )
        #__#$ h_body = "03_hp/13_hermione_main/body_131.png" # HERMIONE
        her "Профессор, нееее...а-ах!{image=textheart.png}"
        #__#show screen h_head2                                                             # HERMIONE
        $herViewHead.showQ( "body_134.png", posHead )
        #__#$ h_body = "03_hp/13_hermione_main/body_134.png" # HERMIONE
        her "Ах-a...{image=textheart.png}Я сейчас сойду с ума!{image=textheart.png}{image=textheart.png}{image=textheart.png}"
        #__#hide screen h_head2  
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
        #__#show screen h_head2                                                             # HERMIONE
        $herViewHead.showQ( "body_134.png", posHead )
        #__#$ h_body = "03_hp/13_hermione_main/body_134.png" # HERMIONE
        her "Нет...{image=textheart.png} ах...{image=textheart.png}"
        her "Похоже я сейчас...{image=textheart.png} кончу...{image=textheart.png}"
        #__#hide screen h_head2  
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


                #__#$ uni_sperm = True
                #__#$ u_sperm = "03_hp/13_hermione_main/auto_08.png"
                $herViewHead.data().addItem( 'sperm', CharacterExItem( herViewHead.mMiscFolder, "sperm_05.png", G_Z_FACE + 1 ) )
                #__#show screen h_head2                                                             # HERMIONE
                $herViewHead.showQ( "body_133.png", posHead )
                #__#$ h_body = "03_hp/13_hermione_main/body_133.png" # HERMIONE
                her2 "Ааа...{image=textheart.png}{image=textheart.png}{image=textheart.png}"
                #__#hide screen h_head2     
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
                #__#show screen h_head2                                                             # HERMIONE
                $herViewHead.showQ( "body_135.png", posHead )
                #__#$ h_body = "03_hp/13_hermione_main/body_135.png" # HERMIONE
                her "*еле дышит*"
                #__#hide screen h_head2
                $herViewHead.hideQ()
                m "Как ты?"
                #__#show screen h_head2                                                             # HERMIONE
                $herViewHead.showQ( "body_133.png", posHead )
                #__#$ h_body = "03_hp/13_hermione_main/body_133.png" # HERMIONE
                her "Ах... да..."
                her "Мои ноги до сих пор трясутся..."
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
                $herViewHead.showQ( "body_133.png", posHead )
                #__#$ h_body = "03_hp/13_hermione_main/body_133.png" # HERMIONE
                if daytime:
                    her "Я думаю, мне пора вернуться в класс..."
                else:
                    her2 "Я думаю, мне пора вернуться в спальню..."
                #__#hide screen h_head2
                $herViewHead.hideQ()
                m "Хорошо."
                m "Тебе понравилось быть оттраханной профессором?"
                #__#show screen h_head2                                                             # HERMIONE
                $herViewHead.showQ( "body_136.png", posHead )
                #__#$ h_body = "03_hp/13_hermione_main/body_136.png" # HERMIONE
                her2 "Сэр, я всего лишь делаю это ради моего факультета."
                #__#hide screen h_head2
                $herViewHead.hideQ()
                m "Ты что, серьезно? Все ещё?"
                #__#show screen h_head2                                                             # HERMIONE
                $herViewHead.showQ( "body_131.png", posHead )
                #__#$ h_body = "03_hp/13_hermione_main/body_131.png" # HERMIONE
                her "Мы можем расчитаться... пожалуйста?"
                #__#hide screen h_head2
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
                #__#$ uni_sperm = True
                #__#$ u_sperm = "03_hp/13_hermione_main/auto_08.png"
                $herViewHead.data().addItem( 'sperm', CharacterExItem( herViewHead.mMiscFolder, "sperm_05.png", G_Z_FACE + 1 ) )
                #__#show screen h_head2                                                             # HERMIONE
                $herViewHead.showQ( "body_133.png", posHead )
                #__#$ h_body = "03_hp/13_hermione_main/body_133.png" # HERMIONE
                her2 "Аааа...{image=textheart.png}{image=textheart.png}{image=textheart.png}"
                #__#hide screen h_head2     
                $herViewHead.hideQ()
                hide screen bld1
                with d3
                show screen ctc
                pause
                hide screen ctc
                show screen bld1
                with d3
                $ g_c_u_pic = "03_hp/08_animation_02/23_cum_19.png"
                #__#show screen h_head2                                                             # HERMIONE
                $herViewHead.showQ( "body_133.png", posHead )
                #__#$ h_body = "03_hp/13_hermione_main/body_133.png" # HERMIONE
                her "Вы кончили в меня..."
                #__#hide screen h_head2
                $herViewHead.hideQ()
                g9 "Да, в тебя."
                hide screen bld1
                with d3
                show screen ctc
                pause
                hide screen ctc
                show screen blkfade
                with d7
                #__#show screen h_head2                                                             # HERMIONE
                $herViewHead.showQ( "body_133.png", posHead )
                #__#$ h_body = "03_hp/13_hermione_main/body_133.png" # HERMIONE
                her "Но..."
                #__#hide screen h_head2
                $herViewHead.hideQ()
                m "Что?"
                #__#show screen h_head2                                                             # HERMIONE
                $herViewHead.showQ( "body_132.png", posHead )
                #__#$ h_body = "03_hp/13_hermione_main/body_132.png" # HERMIONE
                her "Вы не боитесь что я забеременею?"
                #__#hide screen h_head2
                $herViewHead.hideQ()
                m "Не, всё будет хорошо..."
                #__#show screen h_head2                                                             # HERMIONE
                $herViewHead.showQ( "body_132.png", posHead )
                #__#$ h_body = "03_hp/13_hermione_main/body_132.png" # HERMIONE
                her "Откуда вы знаете, сэр?"
                #__#hide screen h_head2
                $herViewHead.hideQ()
                m "Мы, ведьмаки - бесплодны."
                #__#show screen h_head2                                                             # HERMIONE
                $herViewHead.showQ( "body_131.png", posHead )
                #__#$ h_body = "03_hp/13_hermione_main/body_131.png" # HERMIONE
                her "Ведьмаки?"
                #__#hide screen h_head2
                $herViewHead.hideQ()
                m "Конечно... Ты - ведьма, получается я - ведьмак, верно?"
                m "А всем известно, что ведьмаки - бесплодны..."
                #__#show screen h_head2                                                             # HERMIONE
                $herViewHead.showQ( "body_117.png", posHead )
                #__#$ h_body = "03_hp/13_hermione_main/body_117.png" # HERMIONE
                her "Сэр, это бессмысленно..."
                her "Могу я просто расчитаться...?"
                #__#hide screen h_head2
                $herViewHead.hideQ()

    elif request_29_points == 1: # SECOND EVENT <============================================================== EVENT 02
        m "Мисс Грейнджер, вы уже мокрая и готовы, что бы я вошёл в вас?"
        #__#hide screen hermione_main                                                                                                                                                                                   #HERMIONE
        #__#with d3                                                                                                                                                                                                                        #HERMIONE
        $herView.hideQQ()
        #__#$ h_xpos=140 #Defines position of the Hermione's full length sprite. (Default 370). (Center: 140)                                                       #HERMIONE
        #__#$ h_body = "03_hp/13_hermione_main/body_30.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
        #__#show screen hermione_main                                                                                                                                                                                 #HERMIONE
        #__#with d3                         
        $herView.showQQ( "body_30.png", pos )
        her "Профессор!"
        m "Просто скажи \"Я готова\" и иди сюда, девочка."
        #__#hide screen hermione_main                                                                                                                                                                                   #HERMIONE
        #__#with d3                                                                                                                                                                                                                        #HERMIONE
        $herView.hideQQ()
        #__#$ h_xpos=140 #Defines position of the Hermione's full length sprite. (Default 370). (Center: 140)                                                       #HERMIONE
        #__#$ h_body = "03_hp/13_hermione_main/body_31.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
        #__#show screen hermione_main                                                                                                                                                                                 #HERMIONE
        #__#with d3                         
        $herView.showQQ( "body_31.png", pos )
        her "..........."
        #__#hide screen hermione_main                                                                                                                                                                                   #HERMIONE
        #__#with d3                                                                                                                                                                                                                        #HERMIONE
        $herView.hideQQ()
        #__#$ h_xpos=140 #Defines position of the Hermione's full length sprite. (Default 370). (Center: 140)                                                       #HERMIONE
        #__#$ h_body = "03_hp/13_hermione_main/body_118.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
        #__#show screen hermione_main                                                                                                                                                                                 #HERMIONE
        #__#with d3                         
        $herView.showQQ( "body_118.png", pos )
        her "Я готова...."
        #__#hide screen hermione_main    
        $herView.hideQ() #"WARNING_Z"
        jump your_ass

    elif request_29_points >= 2: # THIRD EVENT <============================================================== EVENT 03
        m "Мисс Грейнджер..."
        m "Прошлой ночью у меня был сон..."
        g9 "Вы легли на мой стол, раздвинули ноги и я трахал вашу киску со всей силой..."
        #__#hide screen hermione_main                                                                                                                                                                                   #HERMIONE
        #__#with d3                                                                                                                                                                                                                        #HERMIONE
        $herView.hideQQ()
        #__#$ h_xpos=140 #Defines position of the Hermione's full length sprite. (Default 370). (Center: 140)                                                       #HERMIONE
        #__#$ h_body = "03_hp/13_hermione_main/body_120.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
        #__#show screen hermione_main                                                                                                                                                                                 #HERMIONE
        #__#with d3                         
        $herView.showQQ( "body_120.png", pos )
        her "В этом сне, сэр..."
        #__#hide screen hermione_main                                                                                                                                                                                   #HERMIONE
        #__#with d3                                                                                                                                                                                                                        #HERMIONE
        $herView.hideQQ()
        #__#$ h_xpos=140 #Defines position of the Hermione's full length sprite. (Default 370). (Center: 140)                                                       #HERMIONE
        #__#$ h_body = "03_hp/13_hermione_main/body_47.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
        #__#show screen hermione_main                                                                                                                                                                                 #HERMIONE
        #__#with d3                     
        $herView.showQQ( "body_47.png", pos )
        her "Я получила 65 баллов своему факультету за это?"
        g9 "Да, мисс Грейнджер, получили."
        #__#hide screen hermione_main                                                                                                                                                                                   #HERMIONE
        #__#with d3                                                                                                                                                                                                                        #HERMIONE
        $herView.hideQQ()
        #__#$ h_xpos=140 #Defines position of the Hermione's full length sprite. (Default 370). (Center: 140)                                                       #HERMIONE
        #__#$ h_body = "03_hp/13_hermione_main/body_66.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
        #__#show screen hermione_main                                                                                                                                                                                 #HERMIONE
        #__#with d3                     
        $herView.showQQ( "body_66.png", pos )
        her "..............................."
        her "Дайте мне хотя бы снять свои трусики..."
        stop music fadeout 1.0
        #__#hide screen hermione_main
        #__#with d3
        $herView.hideQQ()
        show screen blkfade
        with d3
        # SEX
        
        #__#$ posHead = gMakePos( 390, 340 )

        $ renpy.play('sounds/gltch.mp3')
        with hpunch
        with kissiris
        #__#show screen h_head2                                                             # HERMIONE
        $herViewHead.showQ( "body_130.png", posHead )
        #__#$ h_body = "03_hp/13_hermione_main/body_130.png" # HERMIONE
        her2 "Ооооооохххх....{image=textheart.png}"
        #__#hide screen h_head2
        $herViewHead.hideQ()
        
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
        play music "music/(Orchestral) Playful Tension by Shadow16nh.mp3" fadein 1 fadeout 1 # SEX THEME.
        show screen bld1
        with d3    


        #__#show screen h_head2                                                             # HERMIONE
        $herViewHead.showQ( "body_131.png", posHead )
        #__#$ h_body = "03_hp/13_hermione_main/body_131.png" # HERMIONE
        her "Ах...{image=textheart.png}"
        #__#hide screen h_head2      
        $herViewHead.hideQ()
        m "Твоя киска сегодня легче приняла мой член..."
        #__#show screen h_head2                                                             # HERMIONE
        $herViewHead.showQ( "body_131.png", posHead )
        #__#$ h_body = "03_hp/13_hermione_main/body_131.png" # HERMIONE    
        her "Да...{image=textheart.png} аааах...?{image=textheart.png}"
        #__#show screen h_head2                                                             # HERMIONE
        $herViewHead.showQ( "body_132.png", posHead )
        #__#$ h_body = "03_hp/13_hermione_main/body_132.png" # HERMIONE    
        her "Это из-за вас, сэр...{image=textheart.png}"
        #__#show screen h_head2                                                             # HERMIONE
        $herViewHead.showQ( "body_134.png", posHead )
        #__#$ h_body = "03_hp/13_hermione_main/body_134.png" # HERMIONE    
        her2 "Вы долбите моё маленькую киску своим гиганстким членом...{image=textheart.png}"
        #__#hide screen h_head2     
        $herViewHead.hideQ()
        g4 "Аааа, шлюха!"
        #__#show screen h_head2                                                             # HERMIONE
        $herViewHead.showQ( "body_134.png", posHead )
        #__#$ h_body = "03_hp/13_hermione_main/body_134.png" # HERMIONE    
        her "Ох...{image=textheart.png}{image=textheart.png}"
        #__#hide screen h_head2     
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
        #__#show screen h_head2                                                             # HERMIONE
        $herViewHead.showQ( "body_128.png", posHead )
        #__#$ h_body = "03_hp/13_hermione_main/body_128.png" # HERMIONE    
        her "Да, сэр..."
        #__#hide screen h_head2  
        $herViewHead.hideQ()
        menu:
            g4 "..."
            "\"Быть нежным, но страстным.\"":
                m "Да, тебе нравится это?"
                #__#show screen h_head2                                                             # HERMIONE
                $herViewHead.showQ( "body_127.png", posHead )
                #__#$ h_body = "03_hp/13_hermione_main/body_127.png" # HERMIONE    
                her "Да, сэр... ах...{image=textheart.png}"
                #__#hide screen h_head2  
                $herViewHead.hideQ()
                m "Хорошая девочка!"
                m "Просто расслабься и прими мой член в себя!"
                #__#show screen h_head2                                                             # HERMIONE
                $herViewHead.showQ( "body_127.png", posHead )
                #__#$ h_body = "03_hp/13_hermione_main/body_127.png" # HERMIONE    
                her "Да... ах...{image=textheart.png}"
                #__#hide screen h_head2  
                $herViewHead.hideQ()
                m "Почти... почти..."
                #__#show screen h_head2                                                             # HERMIONE
                $herViewHead.showQ( "body_131.png", posHead )
                #__#$ h_body = "03_hp/13_hermione_main/body_131.png" # HERMIONE    
                her "Да...{image=textheart.png}{image=textheart.png}"
                #__#hide screen h_head2  
                $herViewHead.hideQ()
                m "Да, моя маленькая принцесса..."
                #__#show screen h_head2                                                             # HERMIONE
                $herViewHead.showQ( "body_119.png", posHead )
                #__#$ h_body = "03_hp/13_hermione_main/body_119.png" # HERMIONE    
                her "Что?"
                #__#show screen h_head2                                                             # HERMIONE
                $herViewHead.showQ( "body_118.png", posHead )
                #__#$ h_body = "03_hp/13_hermione_main/body_118.png" # HERMIONE    
                her "Нет, пожалуйста, не называйте меня так... ах...{image=textheart.png}"
                her2 "Мой папа меня так называл, когда я была маленькая..."
                #__#hide screen h_head2  
                $herViewHead.hideQ()
                m "Ну, сейчас я твой папочка!"
                #__#show screen h_head2                                                             # HERMIONE
                $herViewHead.showQ( "body_121.png", posHead )
                #__#$ h_body = "03_hp/13_hermione_main/body_121.png" # HERMIONE    
                her "Ах...{image=textheart.png} Ах-а...{image=textheart.png}{image=textheart.png}"
                #__#hide screen h_head2  
                $herViewHead.hideQ()
                m "И ты моя маленькая принцесса - шлюха!"
                #__#show screen h_head2                                                             # HERMIONE
                $herViewHead.showQ( "body_123.png", posHead )
                #__#$ h_body = "03_hp/13_hermione_main/body_123.png" # HERMIONE    
                her "Ах...{image=textheart.png} ох...{image=textheart.png}{image=textheart.png}{image=textheart.png}"
            "\"Быть жестким с ней!\"":
                #__#hide screen h_head2  
                $herViewHead.hideQ()
                m "Да, ты шлюха!"
                m "Я научу тебя наслаждаться каждым моментом, когда тебя трахают!"
                show screen blktone
                hide screen ctc
                with d3
                ">Вы увеличиваете темп."
                hide screen blktone
                with d3
                #__#show screen h_head2                                                             # HERMIONE
                $herViewHead.showQ( "body_131.png", posHead )
                #__#$ h_body = "03_hp/13_hermione_main/body_131.png" # HERMIONE    
                her "Ахх...{image=textheart.png} Профессор..."
                #__#hide screen h_head2  
                $herViewHead.hideQ()
                m "Ты - ненасытная шлюха!"
                #__#show screen h_head2                                                             # HERMIONE
                $herViewHead.showQ( "body_132.png", posHead )
                #__#$ h_body = "03_hp/13_hermione_main/body_132.png" # HERMIONE    
                her "А...{image=textheart.png} Ох...{image=textheart.png}"
                #__#hide screen h_head2  
                $herViewHead.hideQ()
                m "Ты - позор для своего факультета!"
                #__#show screen h_head2                                                             # HERMIONE
                $herViewHead.showQ( "body_132.png", posHead )
                #__#$ h_body = "03_hp/13_hermione_main/body_132.png" # HERMIONE    
                her "А-ох...{image=textheart.png}{image=textheart.png}{image=textheart.png}"
                #__#hide screen h_head2  
                $herViewHead.hideQ()
                m "Твои родители послали тебя учиться, а не трахаться со студентами и преподователями!"
                #__#show screen h_head2                                                             # HERMIONE
                $herViewHead.showQ( "body_132.png", posHead )
                #__#$ h_body = "03_hp/13_hermione_main/body_132.png" # HERMIONE    
                her "Ах-а...{image=textheart.png} Но я всё это делаю для...--"
                #__#hide screen h_head2  
                $herViewHead.hideQ()
                m "Всем наплевать, зачем ты это делаешь, любительница членов!"
                m "Посмотри, кем ты стала!"
                m "Скачешь задницей на члене старого профессора, как самая дешевая шлюха!"
                #__#show screen h_head2                                                             # HERMIONE
                $herViewHead.showQ( "body_134.png", posHead )
                #__#$ h_body = "03_hp/13_hermione_main/body_134.png" # HERMIONE    
                her "Ох...{image=textheart.png} Нет...{image=textheart.png} прекратите это говорить...{image=textheart.png} ах...{image=textheart.png}{image=textheart.png}{image=textheart.png}"
                #__#hide screen h_head2  
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
                #__#show screen h_head2                                                             # HERMIONE
                $herViewHead.showQ( "body_123.png", posHead )
                #__#$ h_body = "03_hp/13_hermione_main/body_123.png" # HERMIONE    
                her "................"
                #__#show screen h_head2                                                             # HERMIONE
                $herViewHead.showQ( "body_132.png", posHead )
                #__#$ h_body = "03_hp/13_hermione_main/body_132.png" # HERMIONE    
                her "Ах...{image=textheart.png} Ах....{image=textheart.png}{image=textheart.png}{image=textheart.png}"
                #__#show screen h_head2                                                             # HERMIONE
                $herViewHead.showQ( "body_118.png", posHead )
                #__#$ h_body = "03_hp/13_hermione_main/body_118.png" # HERMIONE    
                her "......................."
                her "{size=-5}Я шлюха...{/size}"
                her "{size=-5}Я шлюха... ах...{/size}"
                #__#hide screen h_head2  
                $herViewHead.hideQ()
        
        m "Да! Вот кто ты есть на самом деле!"
        #__#show screen h_head2                                                             # HERMIONE
        $herViewHead.showQ( "body_118.png", posHead )
        #__#$ h_body = "03_hp/13_hermione_main/body_118.png" # HERMIONE  
        her "Ах... а... а..."
        her "Сэр, вы можете... а..."
        #__#hide screen h_head2  
        $herViewHead.hideQ()
        m "Что?"
        #__#show screen h_head2                                                             # HERMIONE
        $herViewHead.showQ( "body_138.png", posHead )
        #__#$ h_body = "03_hp/13_hermione_main/body_138.png" # HERMIONE  
        her "Вы можете отшлепать меня... ох...?"
        #__#hide screen h_head2  
        $herViewHead.hideQ()
        g4 "С удовольствием!"
        
        $ renpy.play('sounds/slap.mp3')
        show screen white 
        pause.1
        hide screen white
        with hpunch

        #__#show screen h_head2                                                             # HERMIONE
        $herViewHead.showQ( "body_139.png", posHead )
        #__#$ h_body = "03_hp/13_hermione_main/body_139.png" # HERMIONE  
        her "АА-А-АХ!{image=textheart.png}{image=textheart.png}{image=textheart.png}"
        #__#hide screen h_head2  
        $herViewHead.hideQ()
        m "Тебе нравится, а?"
        $ renpy.play('sounds/slap.mp3')
        show screen white 
        pause.1
        hide screen white
        with hpunch
        #__#show screen h_head2                                                             # HERMIONE
        $herViewHead.showQ( "body_138.png", posHead )
        #__#$ h_body = "03_hp/13_hermione_main/body_138.png" # HERMIONE  
        her "А..!{image=textheart.png} ОООО ДА!{image=textheart.png}{image=textheart.png}{image=textheart.png}"
        #__#hide screen h_head2  
        $herViewHead.hideQ()
        m "И ещё... ещё!"
        $ renpy.play('sounds/slap.mp3')
        show screen white 
        pause.1
        hide screen white
        with hpunch
        #__#show screen h_head2                                                             # HERMIONE
        $herViewHead.showQ( "body_138.png", posHead )
        #__#$ h_body = "03_hp/13_hermione_main/body_138.png" # HERMIONE  
        her "Ах! ДА!"
        #__#hide screen h_head2     
        $herViewHead.hideQ()
        show screen blktone
        with d3
        ">Вы заметили, что после каждого шлепка по заднице девченки её киска сжимается на пару секунд и сжимает ваш член..."
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
        #__#show screen h_head2                                                             # HERMIONE
        $herViewHead.showQ( "body_138.png", posHead )
        #__#$ h_body = "03_hp/13_hermione_main/body_138.png" # HERMIONE  
        her "АААА!!!{image=textheart.png}{image=textheart.png}{image=textheart.png} БОЛЬНО!{image=textheart.png}{image=textheart.png}{image=textheart.png}"
        #__#show screen h_head2                                                             # HERMIONE
        $herViewHead.showQ( "body_134.png", posHead )
        #__#$ h_body = "03_hp/13_hermione_main/body_134.png" # HERMIONE  
        her2 "Это больно...{image=textheart.png}{image=textheart.png}{image=textheart.png} больно...{image=textheart.png}{image=textheart.png}{image=textheart.png}"
        #__#hide screen h_head2 
        $herViewHead.hideQ()
        m "М?"
        m "Почему твои ноги так дрожат, малышка?"
        m "Ты кончаешь?"
        #__#show screen h_head2                                                             # HERMIONE
        $herViewHead.showQ( "body_133.png", posHead )
        #__#$ h_body = "03_hp/13_hermione_main/body_133.png" # HERMIONE  
        her "Да...{image=textheart.png}{image=textheart.png}{image=textheart.png}{image=textheart.png}{image=textheart.png}{image=textheart.png}"
        #__#hide screen h_head2 
        $herViewHead.hideQ()
        m "Тогда я последую твоему примеру."
        #__#show screen h_head2                                                             # HERMIONE
        $herViewHead.showQ( "body_133.png", posHead )
        #__#$ h_body = "03_hp/13_hermione_main/body_133.png" # HERMIONE  
        her ".............."
        #__#hide screen h_head2 
        $herViewHead.hideQ()
        show screen blktone 
        with d3
        ">Вы начади трахать Гермиону всё сильнее и жестче!"
        hide screen blktone 
        with d3
        #__#show screen h_head2                                                             # HERMIONE
        $herViewHead.showQ( "body_139.png", posHead )
        #__#$ h_body = "03_hp/13_hermione_main/body_139.png" # HERMIONE  
        her "А! Нет! Я не могу...{image=textheart.png} Я...{image=textheart.png} Ох...{image=textheart.png}{image=textheart.png}{image=textheart.png}"
        #__#hide screen h_head2 
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
                #__#$ uni_sperm = True
                #__#$ u_sperm = "03_hp/13_hermione_main/auto_08.png"
                $herViewHead.data().addItem( 'sperm', CharacterExItem( herViewHead.mMiscFolder, "sperm_05.png", G_Z_FACE + 1 ) )
                #__#show screen h_head2                                                             # HERMIONE
                $herViewHead.showQ( "body_133.png", posHead )
                #__#$ h_body = "03_hp/13_hermione_main/body_133.png" # HERMIONE
                her "!!!"
                her "ААА, вы наполняете меня до краёв!{image=textheart.png}{image=textheart.png}{image=textheart.png}"
                #__#hide screen h_head2  
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
                #__#show screen h_head2                                                             # HERMIONE
                $herViewHead.showQ( "body_139.png", posHead )
                #__#$ h_body = "03_hp/13_hermione_main/body_139.png" # HERMIONE
                her "Ааа, мой живот!"
                #__#hide screen h_head2    
                $herViewHead.hideQ()
                g4 "{size=+5}ШЛЮХА!{/size}"






                #__#hide screen h_head2     
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
                #__#show screen h_head2                                                             # HERMIONE
                $herViewHead.showQ( "body_133.png", posHead )
                #__#$ h_body = "03_hp/13_hermione_main/body_133.png" # HERMIONE
                her "Ааа...{image=textheart.png}"
                #__#hide screen h_head2
                $herViewHead.hideQ()
                m "Ты в порядке, сучка? Всмысле, девочка."
                #__#show screen h_head2                                                             # HERMIONE
                $herViewHead.showQ( "body_133.png", posHead )
                #__#$ h_body = "03_hp/13_hermione_main/body_133.png" # HERMIONE
                her "Да... Я..."
                #__#show screen h_head2                                                             # HERMIONE
                $herViewHead.showQ( "body_135.png", posHead )
                #__#$ h_body = "03_hp/13_hermione_main/body_135.png" # HERMIONE
                her "Я чувствую, как вы меня заполнили..."
                #__#show screen h_head2                                                             # HERMIONE
                $herViewHead.showQ( "body_130.png", posHead )
                #__#$ h_body = "03_hp/13_hermione_main/body_130.png" # HERMIONE
                her "!!!"
                her "Вы кончили в меня, сэр!"
                #__#hide screen h_head2     
                $herViewHead.hideQ()
                m "Да, я залил тебя."
                #__#show screen h_head2                                                             # HERMIONE
                $herViewHead.showQ( "body_131.png", posHead )
                #__#$ h_body = "03_hp/13_hermione_main/body_131.png" # HERMIONE
                her "Вам не стоило этого делать..."
                #__#hide screen h_head2     
                $herViewHead.hideQ()
                m "Разве ты не получила удовольствие от моей горячей спермы?"
                #__#show screen h_head2                                                             # HERMIONE
                $herViewHead.showQ( "body_123.png", posHead )
                #__#$ h_body = "03_hp/13_hermione_main/body_123.png" # HERMIONE
                her "....возможно."
                #__#show screen h_head2                                                             # HERMIONE
                $herViewHead.showQ( "body_121.png", posHead )
                #__#$ h_body = "03_hp/13_hermione_main/body_121.png" # HERMIONE
                her "Помоему, я кончила несколько раз..."
                show screen blkfade
                with d3
                #__#show screen h_head2                                                             # HERMIONE
                $herViewHead.showQ( "body_122.png", posHead )
                #__#$ h_body = "03_hp/13_hermione_main/body_122.png" # HERMIONE
                her2 "Может вы и правы, сэр, и я не должна об этом беспокоиться."
                her "Мы можем расчитаться?"
                #__#hide screen h_head2     
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
                #__#$ uni_sperm = True
                #__#$ u_sperm = "03_hp/13_hermione_main/auto_08.png"
                $herViewHead.data().addItem( 'sperm', CharacterExItem( herViewHead.mMiscFolder, "sperm_05.png", G_Z_FACE + 1 ) )
                #__#show screen h_head2                                                             # HERMIONE
                $herViewHead.showQ( "body_133.png", posHead )
                #__#$ h_body = "03_hp/13_hermione_main/body_133.png" # HERMIONE
                her2 "ААА...{image=textheart.png}{image=textheart.png}{image=textheart.png}"
                #__#hide screen h_head2
                $herViewHead.hideQ()
                g4 "{size=+5}ШЛЮХА! Получи всё!{/size}"
                #__#show screen h_head2                                                             # HERMIONE
                $herViewHead.showQ( "body_138.png", posHead )
                #__#$ h_body = "03_hp/13_hermione_main/body_138.png" # HERMIONE
                her "{size=+5}!!!{/size}"
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
                $ g_c_u_pic = "sex_cum_out_blink_ani"
                
                


                
                m "Это было здорово..."
                #__#show screen h_head2                                                             # HERMIONE
                $herViewHead.showQ( "body_138.png", posHead )
                #__#$ h_body = "03_hp/13_hermione_main/body_138.png" # HERMIONE
                her "Ах...{image=textheart.png}"
                #__#hide screen h_head2                                                             
                $herViewHead.hideQ()
                m "Как ты, шлюха?"
                #__#show screen h_head2                                                             # HERMIONE
                $herViewHead.showQ( "body_133.png", posHead )
                #__#$ h_body = "03_hp/13_hermione_main/body_133.png" # HERMIONE
                her "Да... Я..."
                #__#hide screen h_head2         
                $herViewHead.hideQ()
                m "Ты наслаждалась этим?"
                #__#show screen h_head2                                                             # HERMIONE
                $herViewHead.showQ( "body_123.png", posHead )
                #__#$ h_body = "03_hp/13_hermione_main/body_123.png" # HERMIONE
                her "....думаю, да..."
                #__#hide screen h_head2       
                $herViewHead.hideQ()
                show screen ctc
                pause
                hide screen ctc
                show screen blkfade
                with d3
                #__#show screen h_head2                                                             # HERMIONE
                $herViewHead.showQ( "body_121.png", posHead )
                #__#$ h_body = "03_hp/13_hermione_main/body_121.png" # HERMIONE
                her "Думаю, я кончила несколько раз, сэр..."
                #__#show screen h_head2                                                             # HERMIONE
                $herViewHead.showQ( "body_122.png", posHead )
                #__#$ h_body = "03_hp/13_hermione_main/body_122.png" # HERMIONE
                her "Мы можем расчитаться?"
                #__#hide screen h_head2     
                $herViewHead.hideQ()
        
        
    #__#$ uni_sperm = False #Sperm layer is not displayed in hermione screen.
    if herViewHead.data().getItem( 'sperm' ) != None:
        $herViewHead.data().addItem( 'sperm_after', CharacterExItem( herViewHead.mMiscFolder, "sperm_00_after.png", G_Z_FACE + 1 ) )
    $herViewHead.data().delItem( 'sperm' )
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
    #__#$ h_xpos=140 #Defines position of the Hermione's full length sprite. (Default 370). (Center: 140)
    #__#$ h_body = "03_hp/13_hermione_main/body_13.png" #Flashing panties
    #__#show screen hermione_main
    $herView.showQ( "body_13.png", pos ) #"WARNING_Z"
    hide screen hermione_01_f #Hermione stands still.
    with d3
    her "Спасибо, сэр..."

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

    #call music_block 
    
    if daytime:
        jump night_start
    else:
        jump day_start
                   
