###################REQUEST_24 (Level 07) (65 pt.) (Blowjob to a boy). (Available during daytime only).
label new_request_24: #LV.7 (Whoring = 18 - 20)
    
    hide screen hermione_main 
    with d3
    m "{size=-4}(Попросить её сделать минет одному из ее одноклассников?){/size}"
    $ menu_x = 0.5 #Default position of the menu (0.5). Version B is $ menu_x = 0.2
    menu:
        "\"(Да, давай сделаем это!)\"":
            pass
        "\"(Не сейчас.)\"":
            jump new_personal_request
            
    
    
    if request_24_points == 0: # <================================================================================ FIRST TIME
        
        m "Мисс Грейнджер, сегодня я хочу купить у вас еще одну услугу."
        hide screen hermione_main                                                                                                                                                                                   #HERMIONE
        with d3                                                                                                                                                                                                                        #HERMIONE
        $ h_xpos=140 #Defines position of the Hermione's full length sprite. (Default 370). (Center: 140)                                                       #HERMIONE
        $ h_body = "03_hp/13_hermione_main/body_16.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
        show screen hermione_main                                                                                                                                                                                 #HERMIONE
        with d3                                                                                                                                                                                                                        #HERMIONE
        her "Спасибо, сэр. Я правда ценю это."
        m "Конечно, всегда рад помочь."
        m "Я хочу, чтобы вы отсосали у одного из своих одноклассников."
        hide screen hermione_main                                                                                                                                                                                   #HERMIONE
        with d3                                                                                                                                                                                                                        #HERMIONE
        $ h_body = "03_hp/13_hermione_main/body_48.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
        show screen hermione_main                                                                                                                                                                                 #HERMIONE
        with d3                                                                                                                                                                                                                        #HERMIONE
        stop music fadeout 1.0
        her "!!!"
        her "...ртом?"
        if whoring <=17 or request_23_points <= 1: # Counts how many times you sent Hermione to give a handjob to a boy.
            jump too_much
        play music "music/Chipper Doodle v2.mp3" fadein 1 fadeout 1 # HERMIONE'S THEME.
        m "Да, это то, как это обычно делается..."
        hide screen hermione_main                                                                                                                                                                                   #HERMIONE
        with d3                                                                                                                                                                                                                        #HERMIONE
        $ h_body = "03_hp/13_hermione_main/body_120.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
        show screen hermione_main                                                                                                                                                                                 #HERMIONE
        with d3                                                                                                                                                                                                                        #HERMIONE
        her "Сэр, я..."
        hide screen hermione_main                                                                                                                                                                                   #HERMIONE
        with d3                                                                                                                                                                                                                        #HERMIONE
        $ h_body = "03_hp/13_hermione_main/body_186.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
        show screen hermione_main                                                                                                                                                                                 #HERMIONE
        with d3                                                                                                                                                                                                                        #HERMIONE
        her "Я отказываюсь от настолько развратной услуги как эта, сэр."
        hide screen hermione_main                                                                                                                                                                                   #HERMIONE
        with d3                                                                                                                                                                                                                        #HERMIONE
        $ h_body = "03_hp/13_hermione_main/body_131.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
        show screen hermione_main                                                                                                                                                                                 #HERMIONE
        with d3                                                                                                                                                                                                                        #HERMIONE
        her "Могу я просто поцеловать другую девушку?"
        her "Я не против..." 
        m "Мисс Грейнджер, прекратите тратить мое время..."
        m "Если вы не в настроении продавать услуги сегодня..."
        m "Дверь там."
        hide screen hermione_main                                                                                                                                                                                   #HERMIONE
        with d3                                                                                                                                                                                                                        #HERMIONE
        $ h_body = "03_hp/13_hermione_main/body_120.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
        show screen hermione_main                                                                                                                                                                                 #HERMIONE
        with d3                                                                                                                                                                                                                        #HERMIONE
        her "Но мне нужны очки, сэр. Вы знаете это."
        m "Знаете, мисс Грейнджер, как говорится..."
        m "\"Если ты можешь отсосать член за это, значит тебе это не нужно.\""
        hide screen hermione_main                                                                                                                                                                                   #HERMIONE
        with d3                                                                                                                                                                                                                        #HERMIONE
        $ h_body = "03_hp/13_hermione_main/body_187.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
        show screen hermione_main                                                                                                                                                                                 #HERMIONE
        with d3                                                                                                                                                                                                                        #HERMIONE
        her "Пф..."
        her "............................"
        m ".........................................."
        hide screen hermione_main                                                                                                                                                                                   #HERMIONE
        with d3                                                                                                                                                                                                                        #HERMIONE
        $ h_body = "03_hp/13_hermione_main/body_69.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
        show screen hermione_main                                                                                                                                                                                 #HERMIONE
        with d3                                                                                                                                                                                                                        #HERMIONE
        her "...ладно."
        her "Я согласна..."
        m "Тогда идите и выполняйте!"
        m "Отчитаетесь мне после уроков."
        hide screen hermione_main                                                                                                                                                                                   #HERMIONE
        with d3                                                                                                                                                                                                                        #HERMIONE
        $ h_body = "03_hp/13_hermione_main/body_187.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
        show screen hermione_main                                                                                                                                                                                 #HERMIONE
        with d3                                                                                                                                                                                                                        #HERMIONE
        her "......................................................................"
        her "......................................................................"
        her "......................................................................"
        m "Можете идти, мисс Грейнджер."
        her "........."
        
    else: # <================================================================================ NOT FIRST TIME
        if whoring >= 18 and whoring <= 20: # LEVEL 07 FIRST EVENT.
            m "Иди и сделай какому-нибудь счастливцу минет, девочка."
            hide screen hermione_main                                                                                                                                                                                   #HERMIONE
            with d3                                                                                                                                                                                                                        #HERMIONE
            $ h_xpos=140 #Defines position of the Hermione's full length sprite. (Default 370). (Center: 140)                                                       #HERMIONE
            $ h_body = "03_hp/13_hermione_main/body_66.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
            show screen hermione_main                                                                                                                                                                                 #HERMIONE
            with d3                                                                                                                                                                                                                        #HERMIONE
            her "......Опять?"
            m "Да, опять."
            hide screen hermione_main                                                                                                                                                                                   #HERMIONE
            with d3                                                                                                                                                                                                                        #HERMIONE
            $ h_body = "03_hp/13_hermione_main/body_79.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
            show screen hermione_main                                                                                                                                                                                 #HERMIONE
            with d3                                                                                                                                                                                                                        #HERMIONE
            her ".........."
        elif whoring >= 21: # LEVEL 08+ SECOND EVENT.
            play music "music/Chipper Doodle v2.mp3" fadein 1 fadeout 1 # HERMIONE'S THEME.
            m "Мисс Грейнджер..."
            m "Вы верите в гороскоп?"
            hide screen hermione_main                                                                                                                                                                                   #HERMIONE
            with d3                                                                                                                                                                                                                        #HERMIONE
            $ h_xpos=140 #Defines position of the Hermione's full length sprite. (Default 370). (Center: 140)                                                       #HERMIONE
            $ h_body = "03_hp/13_hermione_main/body_12.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
            show screen hermione_main                                                                                                                                                                                 #HERMIONE
            with d3                                                                                                                                                                                                                        #HERMIONE
            her "Ни капли, сэр..."
            m "Что ж, а стоило бы..."
            hide screen hermione_main                                                                                                                                                                                   #HERMIONE
            with d3                                                                                                                                                                                                                        #HERMIONE
            $ h_body = "03_hp/13_hermione_main/body_14.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
            show screen hermione_main                                                                                                                                                                                 #HERMIONE
            with d3                                                                                                                                                                                                                        #HERMIONE
            her "...?"
            m "Потому что прямо здесь у меня есть ваш и в нем говорится..."
            m "\"Посвятите сегодняшний день чему-нибудь, что вы делаете хорошо\"..."
            hide screen hermione_main                                                                                                                                                                                   #HERMIONE
            with d3                                                                                                                                                                                                                        #HERMIONE
            $ h_body = "03_hp/13_hermione_main/body_13.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
            show screen hermione_main                                                                                                                                                                                 #HERMIONE
            with d3                                                                                                                                                                                                                        #HERMIONE
            her "Что-то, что я делаю хорошо...?"
            m "Иди и отсоси еще парочку членов, девочка."
            hide screen hermione_main                                                                                                                                                                                   #HERMIONE
            with d3                                                                                                                                                                                                                        #HERMIONE
            $ h_body = "03_hp/13_hermione_main/body_79.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
            show screen hermione_main                                                                                                                                                                                 #HERMIONE
            with d3                                                                                                                                                                                                                        #HERMIONE
            her "....................." # :(
            m "Как обычно - отчитаешься мне после уроков..."
            hide screen hermione_main                                                                                                                                                                                   #HERMIONE
            with d3                                                                                                                                                                                                                        #HERMIONE
            $ h_body = "03_hp/13_hermione_main/body_69.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
            show screen hermione_main                                                                                                                                                                                 #HERMIONE
            with d3                                                                                                                                                                                                                        #HERMIONE
            her "Конечно..."
        
        
    
    
   
    
    
    $ request_24 = True

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

    call music_block

    $ hermione_takes_classes = True
    jump day_main_menu
    
    
    
    

    

        

label new_request_24_complete:  # <=================================================================================================== EVENING
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

    


    if whoring >= 18 and whoring <= 20: # LEVEL 07                    
        if one_out_of_three == 1: ### EVENT (A)
            play music "music/Chipper Doodle v2.mp3" fadein 1 fadeout 1 # HERMIONE'S THEME.
            m "Ты знаешь правила, девочка. Начинай рассказывать."
            show screen blktone
            with d3
            hide screen hermione_main                                                                                                                                                                                   #HERMIONE
            with d3                                                                                                                                                                                                                        #HERMIONE
            $ h_xpos=370 #Defines position of the Hermione's full length sprite. (Default 370). (Center: 140)                                                       #HERMIONE
            $ h_body = "03_hp/13_hermione_main/body_66.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
            show screen hermione_main                                                                                                                                                                                 #HERMIONE
            with d3                                                                                                                                                                                                                        #HERMIONE
            her "Я завершила ваше задание, сэр."
            m "Хорошо. Расскажи мне больше."
            hide screen hermione_main                                                                                                                                                                                   #HERMIONE
            with d3                                                                                                                                                                                                                        #HERMIONE
            $ h_body = "03_hp/13_hermione_main/body_69.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
            show screen hermione_main                                                                                                                                                                                 #HERMIONE
            with d3                                                                                                                                                                                                                        #HERMIONE
            her "Что тут можно рассказать, сэр?"
            her "Сегодня я отсосала у одного из моих одноклассников..."
            her "Вот и все..."
            m "Хм... Понятно..."
            m "..............."
            hide screen hermione_main                                                                                                                                                                                   #HERMIONE
            with d3                                                                                                                                                                                                                        #HERMIONE
            $ h_body = "03_hp/13_hermione_main/body_118.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
            show screen hermione_main                                                                                                                                                                                 #HERMIONE
            with d3                                                                                                                                                                                                                        #HERMIONE
            her "...................................."
            m "Ты проглотила?"
            hide screen hermione_main                                                                                                                                                                                   #HERMIONE
            with d3                                                                                                                                                                                                                        #HERMIONE
            $ h_body = "03_hp/13_hermione_main/body_79.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
            show screen hermione_main                                                                                                                                                                                 #HERMIONE
            with d3                                                                                                                                                                                                                        #HERMIONE
            her "..........................."
            m "Мисс Грейнджер, вы проглотили все как полагается?"
            hide screen hermione_main                                                                                                                                                                                   #HERMIONE
            with d3                                                                                                                                                                                                                        #HERMIONE
            $ h_body = "03_hp/13_hermione_main/body_47.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
            show screen hermione_main                                                                                                                                                                                 #HERMIONE
            with d3                                                                                                                                                                                                                        #HERMIONE
            her "Да, сэр."
            m "Чтож, тогда, пожалуй, сойдет..."

            
        elif one_out_of_three == 2: ### EVENT (B)
            m "Мисс Грейнджер, вы выполнили задание?"
            show screen blktone
            with d3
            hide screen hermione_main                                                                                                                                                                                   #HERMIONE
            with d3                                                                                                                                                                                                                        #HERMIONE
            $ h_xpos=370 #Defines position of the Hermione's full length sprite. (Default 370). (Center: 140)                                                       #HERMIONE
            $ h_body = "03_hp/13_hermione_main/body_118.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
            show screen hermione_main                                                                                                                                                                                 #HERMIONE
            with d3                                                                                                                                                                                                                        #HERMIONE
            play music "music/Despair_by_erenik.mp3" fadein 1 fadeout 1 # SAD THEME.
            her "Сэр, я..."
            her "Я пыталась, но..."
            hide screen hermione_main                                                                                                                                                                                   #HERMIONE
            with d3                                                                                                                                                                                                                        #HERMIONE
            $ h_body = "03_hp/13_hermione_main/body_67.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
            show screen hermione_main                                                                                                                                                                                 #HERMIONE
            with d3                                                                                                                                                                                                                        #HERMIONE
            her "Меня отшили, сэр..."
            hide screen hermione_main                                                                                                                                                                                   #HERMIONE
            with d3                                                                                                                                                                                                                        #HERMIONE
            $ h_body = "03_hp/13_hermione_main/body_22.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
            show screen hermione_main                                                                                                                                                                                 #HERMIONE
            with d3                                                                                                                                                                                                                        #HERMIONE
            her "Я не могу поверить в то, что это произошло на самом деле..."
            her "Я одна из лучших учениц в этой школе!"
            her "Одна из самых популярных..."
            
            $ u_tears_pic = "03_hp/13_hermione_main/tears_01.png"
            $ h_tears = True
            
            hide screen hermione_main                                                                                                                                                                                   #HERMIONE
            with d3                                                                                                                                                                                                                        #HERMIONE
            $ h_body = "03_hp/13_hermione_main/body_47.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
            show screen hermione_main                                                                                                                                                                                 #HERMIONE
            with d3                                                                                                                                                                                                                        #HERMIONE
            her "И он меня отшил?"
            her "Как он мог меня так оскорбить?!"
            m "Так ты оскорблена, потому что тот парень отказался положить свой член тебе в рот?"
            hide screen hermione_main                                                                                                                                                                                   #HERMIONE
            with d3                                                                                                                                                                                                                        #HERMIONE
            $ u_tears_pic = "03_hp/13_hermione_main/tears_02.png"
            $ h_body = "03_hp/13_hermione_main/body_47.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
            show screen hermione_main                                                                                                                                                                                 #HERMIONE
            with d3                                                                                                                                                                                                                        #HERMIONE
            her "А вы бы не оскорбились, сэр?"
            m "Думаю, я бы довольно-таки легко это пережил..."
            hide screen hermione_main                                                                                                                                                                                   #HERMIONE
            with d3                                                                                                                                                                                                                        #HERMIONE
            $ h_body = "03_hp/13_hermione_main/body_187.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
            show screen hermione_main                                                                                                                                                                                 #HERMIONE
            with d3                                                                                                                                                                                                                        #HERMIONE
            her "Он отверг меня, сэр..."
            her "Да за кого он себя держит?!"
            hide screen hermione_main                                                                                                                                                                                   #HERMIONE
            with d3                                                                                                                                                                                                                        #HERMIONE
            $ h_body = "03_hp/13_hermione_main/body_186.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
            show screen hermione_main                                                                                                                                                                                 #HERMIONE
            with d3                                                                                                                                                                                                                        #HERMIONE
            her "При всем уважении сэр, вам не понять..."
            m "Ну, в любом случае, я не могу заплатить тебе за это."
            hide screen hermione_main                                                                                                                                                                                   #HERMIONE
            with d3                                                                                                                                                                                                                        #HERMIONE
            $ u_tears_pic = "03_hp/13_hermione_main/tears_01.png"
            $ h_body = "03_hp/13_hermione_main/body_79.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
            show screen hermione_main                                                                                                                                                                                 #HERMIONE
            with d3                                                                                                                                                                                                                        #HERMIONE
            her "Конечно... Я и не ждала этого, сэр."
            her "Я провалила свое задание и не заслуживаю никакой награды..."
            her "И вы не должны платить мне из жалости..."
            hide screen hermione_main                                                                                                                                                                                   #HERMIONE
            with d3                                                                                                                                                                                                                        #HERMIONE
            $ h_body = "03_hp/13_hermione_main/body_69.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
            show screen hermione_main                                                                                                                                                                                 #HERMIONE
            with d3                                                                                                                                                                                                                        #HERMIONE
            her "Я только еще больше разозлюсь..."
            m "Хм... В таком случае, может мне все-таки заплатить тебе..."
            hide screen hermione_main                                                                                                                                                                                   #HERMIONE
            with d3                                                                                                                                                                                                                        #HERMIONE
            $ h_body = "03_hp/13_hermione_main/body_79.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
            show screen hermione_main                                                                                                                                                                                 #HERMIONE
            with d3                                                                                                                                                                                                                        #HERMIONE
            her "Нет, сэр. Я не приму этого..."
            m "Хм... Тогда на сегодня все."
            her "Спокойной ночи, сэр."
            hide screen hermione_main                                                                                                                                                                                 #HERMIONE
            with d3   
            $ h_tears = False
            
            $ request_24_points += 1 
            $ request_24 = False 
            $ hermione_sleeping = True
            call music_block
            jump could_not_flirt #Sent here when choose "Favor failed! No points for you!" (Hermione is leaving without getting any points).

        elif one_out_of_three == 3: ### EVENT (C)
            #play music "music/Despair_by_erenik.mp3" fadein 1 fadeout 1 # SAD THEME.
            m "Мисс Грейнджер, как все прошло?"
            show screen blktone
            with d3
            hide screen hermione_main                                                                                                                                                                                   #HERMIONE
            with d3                                                                                                                                                                                                                        #HERMIONE
            $ h_xpos=370 #Defines position of the Hermione's full length sprite. (Default 370). (Center: 140)                                                       #HERMIONE
            $ h_body = "03_hp/13_hermione_main/body_69.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
            show screen hermione_main                                                                                                                                                                                 #HERMIONE
            with d3                                                                                                                                                                                                                        #HERMIONE
            her "Я все еще считаю идею продавать такие услуги отвратительной, сэр."
            hide screen hermione_main                                                                                                                                                                                   #HERMIONE
            with d3                                                                                                                                                                                                                        #HERMIONE
            $ h_body = "03_hp/13_hermione_main/body_79.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
            show screen hermione_main                                                                                                                                                                                 #HERMIONE
            with d3                                                                                                                                                                                                                        #HERMIONE
            her "Но в остальном все прошло на удивление хорошо..."
            play music "music/(Orchestral) Playful Tension by Shadow16nh.mp3" fadein 1 fadeout 1 # SEX THEME.
            her "Я сделала хороший минет тому шикарному парню из \"Когтеврана\"..."
            hide screen hermione_main                                                                                                                                                                                   #HERMIONE
            with d3                                                                                                                                                                                                                        #HERMIONE
            $ h_body = "03_hp/13_hermione_main/body_87.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
            show screen hermione_main                                                                                                                                                                                 #HERMIONE
            with d3                                                                                                                                                                                                                        #HERMIONE
            her "И он был таким джентельменом..."
            hide screen hermione_main                                                                                                                                                                                   #HERMIONE
            with d3                                                                                                                                                                                                                        #HERMIONE
            $ h_body = "03_hp/13_hermione_main/body_118.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
            show screen hermione_main                                                                                                                                                                                 #HERMIONE
            with d3                                                                                                                                                                                                                        #HERMIONE
            her "Он даже предупредил меня перед тем как кончить."
            m "В самом деле, настоящий джентельмен."
            m "Ты проглотила?"
            hide screen hermione_main                                                                                                                                                                                   #HERMIONE
            with d3                                                                                                                                                                                                                        #HERMIONE
            $ h_body = "03_hp/13_hermione_main/body_120.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
            show screen hermione_main                                                                                                                                                                                 #HERMIONE
            with d3                                                                                                                                                                                                                        #HERMIONE
            her "Конечно, сэр."
            her "Я ведь сказала - я сделала парню хороший минет."
            hide screen hermione_main                                                                                                                                                                                   #HERMIONE
            with d3                                                                                                                                                                                                                        #HERMIONE
            $ h_body = "03_hp/13_hermione_main/body_118.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
            show screen hermione_main                                                                                                                                                                                 #HERMIONE
            with d3                                                                                                                                                                                                                        #HERMIONE
            her "Меньшее, что я могу сделать для кого-то, кто для разнообразия отнесся ко мне с уважением..."
            m "В таком случае, ладно."
            
    if whoring >= 21: # LEVEL 08 =+               
        if one_out_of_three == 1: ### EVENT (A)
            stop music fadeout 1.0
            # HERMIONE ALL MESSED UP, WITH RUNNING MASCARA.
            $ u_tears_pic = "03_hp/13_hermione_main/tears_03.png"
            $ h_tears = True
            $ aftersperm = True
            $ uni_sperm = True
            $ u_sperm = "03_hp/13_hermione_main/auto_08.png"
            show screen blktone
            with d3
            hide screen hermione_main                                                                                                                                                                                   #HERMIONE
            with d3                                                                                                                                                                                                                        #HERMIONE
            $ h_xpos=370 #Defines position of the Hermione's full length sprite. (Default 370). (Center: 140)                                                       #HERMIONE
            $ h_body = "03_hp/13_hermione_main/body_47.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
            show screen hermione_main                                                                                                                                                                                 #HERMIONE
            with d3                                                                                                                                                                                                                        #HERMIONE
            show screen ctc
            pause
            hide screen ctc
            m "Мисс Грейнджер..."
            m "Вы будто из ада вылезли..."
            play music "music/Chipper Doodle v2.mp3" fadein 1 fadeout 1 # HERMIONE'S THEME.
            hide screen hermione_main                                                                                                                                                                                   #HERMIONE
            with d3                                                                                                                                                                                                                        #HERMIONE
            $ h_body = "03_hp/13_hermione_main/body_30.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
            show screen hermione_main                                                                                                                                                                                 #HERMIONE
            with d3                                                                                                                                                                                                                        #HERMIONE
            her "Сэр, меня изнасиловали."
            m "Серьезно?"
            hide screen hermione_main                                                                                                                                                                                   #HERMIONE
            with d3                                                                                                                                                                                                                        #HERMIONE
            $ h_body = "03_hp/13_hermione_main/body_79.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
            show screen hermione_main                                                                                                                                                                                 #HERMIONE
            with d3                                                                                                                                                                                                                        #HERMIONE
            her "Да, сэр."
            her "Тот противный парень из \"Слизерина\" изнасиловал меня..."
            hide screen hermione_main                                                                                                                                                                                   #HERMIONE
            with d3                                                                                                                                                                                                                        #HERMIONE
            $ h_body = "03_hp/13_hermione_main/body_87.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
            show screen hermione_main                                                                                                                                                                                 #HERMIONE
            with d3                                                                                                                                                                                                                        #HERMIONE
            her "Хотя, скорее изнасиловал мое лицо..."
            her "И--"
            hide screen hermione_main                                                                                                                                                                                   #HERMIONE
            with d3                                                                                                                                                                                                                        #HERMIONE
            $ h_body = "03_hp/13_hermione_main/body_132.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
            show screen hermione_main                                                                                                                                                                                 #HERMIONE
            with d3                                                                                                                                                                                                                        #HERMIONE
            play sound "sounds/burp.mp3"
            her "*Отрыжка!*..."
            hide screen hermione_main                                                                                                                                                                                   #HERMIONE
            with d3                                                                                                                                                                                                                        #HERMIONE
            $ h_body = "03_hp/13_hermione_main/body_118.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
            show screen hermione_main                                                                                                                                                                                 #HERMIONE
            with d3                                                                                                                                                                                                                        #HERMIONE
            her "Простите."
            hide screen hermione_main                                                                                                                                                                                   #HERMIONE
            with d3                                                                                                                                                                                                                        #HERMIONE
            $ h_body = "03_hp/13_hermione_main/body_86.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
            show screen hermione_main                                                                                                                                                                                 #HERMIONE
            with d3                                                                                                                                                                                                                        #HERMIONE
            her "Он кончил так много, что я с трудом смогла все проглотить..."
            her "Чертов ублюдок!"
            hide screen hermione_main                                                                                                                                                                                   #HERMIONE
            with d3                                                                                                                                                                                                                        #HERMIONE
            $ h_body = "03_hp/13_hermione_main/body_187.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
            show screen hermione_main                                                                                                                                                                                 #HERMIONE
            with d3                                                                                                                                                                                                                        #HERMIONE
            her "Как вы думаете, я могу написать жалобу, сэр?"
            m "Хм... Наверное..."
            m "Но имей в виду, что как только мы втянем министерство в это ..."
            m "Всю эту \"лавочку по продаже услуг\" прийдется немедленно прикрыть."
            hide screen hermione_main                                                                                                                                                                                   #HERMIONE
            with d3                                                                                                                                                                                                                        #HERMIONE
            $ h_body = "03_hp/13_hermione_main/body_189.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
            show screen hermione_main                                                                                                                                                                                 #HERMIONE
            with d3                                                                                                                                                                                                                        #HERMIONE
            her "Ох...?"
            her ".................."
            hide screen hermione_main                                                                                                                                                                                   #HERMIONE
            with d3                                                                                                                                                                                                                        #HERMIONE
            $ h_body = "03_hp/13_hermione_main/body_74.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
            show screen hermione_main                                                                                                                                                                                 #HERMIONE
            with d3                                                                                                                                                                                                                        #HERMIONE
            her "Простите, забудьте о том, что я только что сказала..."
            m "Ты уверена? Ты выглядишь довольно помятой."
            her "Нет, нет. Это мелочи..."
            her "Все-таки это я предложила ему минет..."
            her "Он всего лишь стал обращаться со мной немного грубо под конец, вот и все..."
            her "Думаю, я просто преувеличиваю..."
            m "Понятно..."
            her "Могу я просто--"
            hide screen hermione_main                                                                                                                                                                                   #HERMIONE
            with d3                                                                                                                                                                                                                        #HERMIONE
            $ h_body = "03_hp/13_hermione_main/body_48.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
            show screen hermione_main                                                                                                                                                                                 #HERMIONE
            with d3                                                                                                                                                                                                                        #HERMIONE
            play sound "sounds/burp.mp3"
            her "*Отрыжка!*..."
            hide screen hermione_main                                                                                                                                                                                   #HERMIONE
            with d3                                                                                                                                                                                                                        #HERMIONE
            $ h_body = "03_hp/13_hermione_main/body_118.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
            show screen hermione_main                                                                                                                                                                                 #HERMIONE
            with d3                                                                                                                                                                                                                        #HERMIONE
            her "Простите, сэр."
            hide screen hermione_main                                                                                                                                                                                   #HERMIONE
            with d3                                                                                                                                                                                                                        #HERMIONE
            $ h_body = "03_hp/13_hermione_main/body_34.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
            show screen hermione_main                                                                                                                                                                                 #HERMIONE
            with d3                                                                                                                                                                                                                        #HERMIONE
            her "{size=-3}(Он продолжал кончать... Мой живот так набит...){/size}"
            hide screen hermione_main                                                                                                                                                                                   #HERMIONE
            with d3                                                                                                                                                                                                                        #HERMIONE
            $ h_body = "03_hp/13_hermione_main/body_31.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
            show screen hermione_main                                                                                                                                                                                 #HERMIONE
            with d3                                                                                                                                                                                                                        #HERMIONE
            her "Могу я получить свою плату,пожалуйста?"
            
        elif one_out_of_three == 2: ### EVENT (B)
            # HERMIONE COVERED IN CUM
            label suked_off_them_both:
                pass
            stop music fadeout 1.0
            $ uni_sperm = True
            $ u_sperm = "03_hp/13_hermione_main/auto_10.png"
            show screen blktone
            with d3
            hide screen hermione_main                                                                                                                                                                                   #HERMIONE
            with d3                                                                                                                                                                                                                        #HERMIONE
            $ h_xpos=370 #Defines position of the Hermione's full length sprite. (Default 370). (Center: 140)                                                       #HERMIONE
            $ h_body = "03_hp/13_hermione_main/body_78.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
            show screen hermione_main                                                                                                                                                                                 #HERMIONE
            with d3                                                                                                                                                                                                                        #HERMIONE
            show screen ctc
            pause
            hide screen ctc
            her "Добрый вечер, сэр..."
            g4 "Мисс Грейнджер?!"
            g4 "Что с вами произошло, девушка?"
            g4 "Все что я просил - сделать минет одному из ваших одноклассников."
            hide screen hermione_main                                                                                                                                                                                   #HERMIONE
            with d3                                                                                                                                                                                                                        #HERMIONE
            $ h_body = "03_hp/13_hermione_main/body_118.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
            show screen hermione_main                                                                                                                                                                                 #HERMIONE
            with d3                                                                                                                                                                                                                        #HERMIONE
            play music "music/(Orchestral) Playful Tension by Shadow16nh.mp3" fadein 1 fadeout 1 # SEX THEME.
            her "Это... это именно то что я сделала, сэр."
            m "Девушка, вы покрыта спермой с ног до головы."
            hide screen hermione_main                                                                                                                                                                                   #HERMIONE
            with d3                                                                                                                                                                                                                        #HERMIONE
            $ h_body = "03_hp/13_hermione_main/body_121.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
            show screen hermione_main                                                                                                                                                                                 #HERMIONE
            with d3                                                                                                                                                                                                                        #HERMIONE
            her "Да?"
            her "Ох... Я забыла привести себя в порядок?"
            hide screen hermione_main                                                                                                                                                                                   #HERMIONE
            with d3                                                                                                                                                                                                                        #HERMIONE
            $ h_body = "03_hp/13_hermione_main/body_128.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
            show screen hermione_main                                                                                                                                                                                 #HERMIONE
            with d3                                                                                                                                                                                                                        #HERMIONE
            her "Как неловко..."
            her "Думаю,что то действие в мужском туалете несколько разрослось..."
            her "Прежде чем я поняла, что происхожит я была окружена большими пульсирующими членами..."
            hide screen hermione_main                                                                                                                                                                                   #HERMIONE
            with d3                                                                                                                                                                                                                        #HERMIONE
            $ h_body = "03_hp/13_hermione_main/body_133.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
            show screen hermione_main                                                                                                                                                                                 #HERMIONE
            with d3                                                                                                                                                                                                                        #HERMIONE
            her "Ох... Просто разговор об этом заставляет меня трсястись в экстазе... эээ.."
            hide screen hermione_main                                                                                                                                                                                   #HERMIONE
            with d3                                                                                                                                                                                                                        #HERMIONE
            $ h_body = "03_hp/13_hermione_main/body_136.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
            show screen hermione_main                                                                                                                                                                                 #HERMIONE
            with d3                                                                                                                                                                                                                        #HERMIONE
            her "...то есть в страхе... нет, не страхе..."
            hide screen hermione_main                                                                                                                                                                                   #HERMIONE
            with d3                                                                                                                                                                                                                        #HERMIONE
            $ h_body = "03_hp/13_hermione_main/body_188.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
            show screen hermione_main                                                                                                                                                                                 #HERMIONE
            with d3                                                                                                                                                                                                                        #HERMIONE
            her "Смущении?"
            m "Вы меня спрашиваете?"
            hide screen hermione_main                                                                                                                                                                                   #HERMIONE
            with d3                                                                                                                                                                                                                        #HERMIONE
            $ h_body = "03_hp/13_hermione_main/body_123.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
            show screen hermione_main                                                                                                                                                                                 #HERMIONE
            with d3                                                                                                                                                                                                                        #HERMIONE
            her "Ох, простите, сэр... Мне немного сложновато думать..."
            her "Я думаю, что мне нужно ненадолго прилечь..."
            m "Не забудьте сначала принять душ."
            hide screen hermione_main                                                                                                                                                                                   #HERMIONE
            with d3                                                                                                                                                                                                                        #HERMIONE
            $ h_body = "03_hp/13_hermione_main/body_128.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
            show screen hermione_main                                                                                                                                                                                 #HERMIONE
            with d3                                                                                                                                                                                                                        #HERMIONE
            her "Душ? Зачем?"
            m "Не важно..."
            show screen ctc
            pause
            hide screen ctc


        elif one_out_of_three == 3: ### EVENT (C)
            if  suked_off_ron_and_har:
                jump suked_off_them_both
            else:
                 $ suked_off_ron_and_har = True #In public events. Give blowjob to a classmate. Event level 03. Event # 3. "Sukerd off Harrt and Ron". Turns True after that.


            m "Мисс Грейнджер, как все прошло?"
            show screen blktone
            with d3
            hide screen hermione_main                                                                                                                                                                                   #HERMIONE
            with d3                                                                                                                                                                                                                        #HERMIONE
            $ h_xpos=370 #Defines position of the Hermione's full length sprite. (Default 370). (Center: 140)                                                       #HERMIONE
            $ h_body = "03_hp/13_hermione_main/body_74.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
            show screen hermione_main                                                                                                                                                                                 #HERMIONE
            with d3                                                                                                                                                                                                                        #HERMIONE
            her "Великолепно, сэр. Просто великолепно."
            m "Правда? Рассказывай."
            hide screen hermione_main                                                                                                                                                                                   #HERMIONE
            with d3                                                                                                                                                                                                                        #HERMIONE
            $ h_body = "03_hp/13_hermione_main/body_78.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
            show screen hermione_main                                                                                                                                                                                 #HERMIONE
            with d3                                                                                                                                                                                                                        #HERMIONE
            play music "music/(Orchestral) Playful Tension by Shadow16nh.mp3" fadein 1 fadeout 1 # SEX THEME.
            her "Сегодня я сделала то, что я хотела сделать очень долгое время..."
            her "Но не могла набраться смелости..."
            m "Хм..?"
            hide screen hermione_main                                                                                                                                                                                   #HERMIONE
            with d3                                                                                                                                                                                                                        #HERMIONE
            $ h_body = "03_hp/13_hermione_main/body_121.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
            show screen hermione_main                                                                                                                                                                                 #HERMIONE
            with d3                                                                                                                                                                                                                        #HERMIONE
            her "Сегодня я отсосала у двух моих лучших друзей во всем мире!"
            hide screen hermione_main                                                                                                                                                                                   #HERMIONE
            with d3                                                                                                                                                                                                                        #HERMIONE
            $ h_body = "03_hp/13_hermione_main/body_124.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
            show screen hermione_main                                                                                                                                                                                 #HERMIONE
            with d3                                                                                                                                                                                                                        #HERMIONE
            her "И это было прекрасней, чем я могла себе представить."
            hide screen hermione_main                                                                                                                                                                                   #HERMIONE
            with d3                                                                                                                                                                                                                        #HERMIONE
            $ h_body = "03_hp/13_hermione_main/body_123.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
            show screen hermione_main                                                                                                                                                                                 #HERMIONE
            with d3                                                                                                                                                                                                                        #HERMIONE
            her "Их члены были такими мокрыми из-за моей слюны..."
            her "Я не забыла и про их яйца..."
            hide screen hermione_main                                                                                                                                                                                   #HERMIONE
            with d3                                                                                                                                                                                                                        #HERMIONE
            $ h_body = "03_hp/13_hermione_main/body_134.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
            show screen hermione_main                                                                                                                                                                                 #HERMIONE
            with d3                                                                                                                                                                                                                        #HERMIONE
            her "Но лучшая часть это выражения их лиц..."
            her "Парни не могли поверить, что это и впрямь происходит..."
            hide screen hermione_main                                                                                                                                                                                   #HERMIONE
            with d3                                                                                                                                                                                                                        #HERMIONE
            $ h_body = "03_hp/13_hermione_main/body_133.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
            show screen hermione_main                                                                                                                                                                                 #HERMIONE
            with d3                                                                                                                                                                                                                        #HERMIONE
            her "Если честно, и я не могла..."
            her "Я, Гермиона Грейнджер - девушка, которую они знали годами..."
            hide screen hermione_main                                                                                                                                                                                   #HERMIONE
            with d3                                                                                                                                                                                                                        #HERMIONE
            $ h_body = "03_hp/13_hermione_main/body_135.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
            show screen hermione_main                                                                                                                                                                                 #HERMIONE
            with d3                                                                                                                                                                                                                        #HERMIONE
            her "Сосет у них члены..."
            hide screen hermione_main                                                                                                                                                                                   #HERMIONE
            with d3                                                                                                                                                                                                                        #HERMIONE
            $ h_body = "03_hp/13_hermione_main/body_139.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
            show screen hermione_main                                                                                                                                                                                 #HERMIONE
            with d3                                                                                                                                                                                                                        #HERMIONE
            her "Как какая-то мерзкая мелкая шлюшка..."
            m "Ты любишь этих парней, девочка?"
            hide screen hermione_main                                                                                                                                                                                   #HERMIONE
            with d3                                                                                                                                                                                                                        #HERMIONE
            $ h_body = "03_hp/13_hermione_main/body_74.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
            show screen hermione_main                                                                                                                                                                                 #HERMIONE
            with d3                                                                                                                                                                                                                        #HERMIONE
            her "Я не знаю, сэр... Может быть..."
            her "Можно мне получить свою плату?"
            m "Конечно..."
            
            
            
                 
            
    
    
    
    
    $ gryffindor += 65 #65
    m "65 очков \"Гриффиндору\"!"
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


 

    $ h_tears = False
    $ aftersperm = False
    $ uni_sperm = False

#    $ public_whore_ending = True #Activates "Public Whore" ending.
    $ end.SetEndingValue(const_ENDING_PUBLIC_WHORE,2)
    
    $ request_24_points += 1 
    $ request_24 = False 
    $ hermione_sleeping = True

    call music_block
    
    return