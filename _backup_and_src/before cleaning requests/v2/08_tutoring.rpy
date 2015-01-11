label tutoring:

    $ tut_happened = True # Turns TRUE after you click the tutoring button and see th message that tutoring is not a part of this game. Make sure the tutoring button will not be visible after that.
    
    hide screen hermione_main                                                                                                                                                                                   #HERMIONE
    with d3                                                                                                                                                                                                                        #HERMIONE
    $ h_xpos=370 #Defines position of the Hermione's full length sprite. (Default 370). (Center: 140)                                                       #HERMIONE
    $ h_body = "03_hp/13_hermione_main/body_14.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
    show screen hermione_main                                                                                                                                                                                 #HERMIONE
    with d3                                                                                                                                                                                                                        #HERMIONE
    
    her "Конечно, сэр."
    her "Я только схожу за своими книгами."
    
    
    hide screen hermione_main                                                                                                                                                                                   #HERMIONE

    show screen blkfade
    with d3
    $ renpy.play('sounds/door.mp3') #Sound of a door opening.
    pause 2
    $ renpy.play('sounds/door.mp3') #Sound of a door opening.
    pause.3
    

    $ only_upper = True
    $ ne = False # Desplays a fishnets in hermione_main screen.


    $ h_xpos=140 #Defines position of the Hermione's full length sprite. (Default 370). (Center: 140)                                                       #HERMIONE
    $ h_body = "03_hp/13_hermione_main/body_199.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
    show screen hermione_main                                                                                                                                                                                 #HERMIONE
    with d3                                                                                                                                                                                                                        #HERMIONE
    
    
    hide screen blkfade
    with d3
    
    show screen ctc
    pause
    hide screen ctc
    
    hide screen hermione_main                                                                                                                                                                                   #HERMIONE
    with d3                                                                                                                                                                                                                        #HERMIONE
                                                                                                                                                                                                                        #HERMIONE
    if knowledge == 0:
        $ tut_happened = True
        $ h_body = "03_hp/13_hermione_main/body_199.png"
        show screen hermione_main
        with d3
        play music "music/Chipper Doodle v2.mp3" fadein 1 fadeout 1
        her "Еще раз спасибо, за то, что делаете это для меня, сэр."
        her "Вы, должно быть, очень заняты школьными делами, но все равно вы нашли время на занятия со мной..."
        her "Я хочу сказать, что очень ценю вашу заботу."
        m "Не стоит благодарностей, мисс Грейнджер. Следить за успеваемостью учеников - одна из главных обязанностей директора."
        g9 "{size=-4}(Кроме того, я собираюсь залезть к тебе в трусики, когда мы закончим.){/size}"
        hide screen hermione_main
        with d3
        $ only_upper = False
        $ h_body = "03_hp/13_hermione_main/body_08.png"
        show screen hermione_main
        with d3
        her "Вы что-то сказали, сэр?"                                                                                                                                                                                  #HERMIONE
        m "Кхм... Я сказал, что вы без проблем сдадите любой экзамен, когда мы закончим."
        hide screen hermione_main
        with d3
        $ h_body = "03_hp/13_hermione_main/body_06.png"
        show screen hermione_main
        with d3
        her "Я ни на секунду не сомневалась в этом."
        her "Ведь вы - Альбус Дамблдор - один из самых великих волшебников нашего времени."
        g9 "Еще бы! Я просто шикарен."
        hide screen hermione_main                                                                                                                                                                                   #HERMIONE
        with d3
        $ h_body = "03_hp/13_hermione_main/body_17.png"
        show screen hermione_main
        with d3
        her "..."
        hide screen hermione_main
        with d3        
        $ h_body = "03_hp/13_hermione_main/body_06.png"
        show screen hermione_main
        with d3
        her "Давайте приступим, Профессор?"                                                                                                                                                                                   #HERMIONE
        m "Конечно, дитя. У тебя есть ко мне какие-то вопросы?"
        show screen hermione_main
        with d3
        her "Думаю, пока нет. Хотя..."
        hide screen hermione_main
        with d3
        $ h_body = "03_hp/13_hermione_main/body_14.png"
        show screen hermione_main
        with d3
        her "Есть кое-что, в чем я сомневаюсь, и это не дает мне покоя."
        g9 "И что же это? Не стесняйся, можешь спросить у самого великого волшебника в мире!"
        hide screen hermione_main                                                                                                                                                                                   #HERMIONE
        with d3
        $ h_body = "03_hp/13_hermione_main/body_12.png"
        show screen hermione_main
        with d3
        her "..."
        hide screen hermione_main                                                                                                                                                                                   #HERMIONE
        with d3
        $ h_body = "03_hp/13_hermione_main/body_04.png"
        show screen hermione_main
        with d3
        her "Хорошо..."
        hide screen hermione_main                                                                                                                                                                                   #HERMIONE
        with d3
        $ h_body = "03_hp/13_hermione_main/body_11.png"
        show screen hermione_main
        with d3
        her "Я не совсем уверена, как заклинание \"патискор вальде\" может хорошо работать против перуанских мантикор..."
        her "Ведь в таком случае идеально должно подходить \"гэйли секундум\", но в издании \"Эксцилиус прохороса\" 1831 утверждается обратное..."
        hide screen hermione_main                                                                                                                                                                                   #HERMIONE
        with d3
        $ h_body = "03_hp/13_hermione_main/body_06.png"
        show screen hermione_main
        with d3
        her "Не могли бы вы сказать, в чем моя ошибка?"                                                                                                                                                                                  #HERMIONE
        m "Конечно, дитя..."
        m "..."
        m "..."
        m "..!"
        m "{size=-4}(Что за ахинею она только что несла?){/size}"
        m "{size=-4}(Так, соберись, Джинни...){/size}"
        m "Кхм... Стоит учесть, что мы говорим не о простых мунтикорах, а именно пердуанских..."
        hide screen hermione_main                                                                                                                                                                                   #HERMIONE
        with d3
        $ h_body = "03_hp/13_hermione_main/body_04.png"
        show screen hermione_main
        with d3
        her "\"Перуанских мантикор\", сэр..."
        hide screen hermione_main                                                                                                                                                                                   #HERMIONE
        with d3
        m "Верно! Умница, девочка. Я просто проверял тебя. Назови мне основные признаки этих пер... Существ."
        hide screen hermione_main                                                                                                                                                                                   #HERMIONE
        with d3
        $ h_body = "03_hp/13_hermione_main/body_01.png"
        show screen hermione_main
        with d3
        her "Конечно, сэр."
        $ h_body = "03_hp/13_hermione_main/body_14.png"
        show screen hermione_main
        with d3
        her "Перуанские мантикоры - мантикоры, живущие в районе Перу, размах крыльев достигает..."
        her "*Пщщщщщщщщщщщщщщщщ*"
        her "*пщщщщщщщщщщщ*"
        m "..."
        her "Бз-бззз-бзззбз-бззззз..."
        her "Пффффшшшшшууууп"
        m "..."
        g9 "{size=-4}(А это даже забавно.){/size}"
        her "Ня-ня-ня-ня-ня-ня-ня..."
        her "Ня-ня-ня-{b}член{/b}-ня-ня."
        m "..."
        stop music 
        $ renpy.play('sounds/scratch.wav')
        m "..!"
        m "Что вы сказали, мисс Грейнджер?!"
        hide screen hermione_main                                                                                                                                                                                   #HERMIONE
        with d3
        $ h_body = "03_hp/13_hermione_main/body_13.png"
        show screen hermione_main
        with d3
        her "Эм... Впервые их подробно изучил член Мальбуржской ассоциации магов - Истафар Ариус..."
        hide screen hermione_main                                                                                                                                                                                   #HERMIONE
        with d3
        $ h_body = "03_hp/13_hermione_main/body_11.png"
        show screen hermione_main
        with d3
        her "Я что-то сказала не так..?"
        play music "music/Chipper Doodle v2.mp3" fadein 1 fadeout 1
        m "... нет-нет, все верно..."
        hide screen hermione_main                                                                                                                                                                                   #HERMIONE
        with d3
        $ h_body = "03_hp/13_hermione_main/body_01.png"
        show screen hermione_main
        with d3
        her "Тогда можем мы вернуться к моему вопросу, сэр?"        
        m "Ах, да... Вопрос..."
        m "Кхм..."
        m "Мисс Грейнджер, что вы знаете о зябликах?"
        hide screen hermione_main                                                                                                                                                                                   #HERMIONE
        with d3
        $ h_body = "03_hp/13_hermione_main/body_14.png"
        show screen hermione_main
        with d3
        her "Простите, сэр?"
        m "Закройте глаза и представьте зяблика, мисс Грейнджер."
        hide screen hermione_main                                                                                                                                                                                   #HERMIONE
        with d3
        $ h_body = "03_hp/13_hermione_main/body_11.png"
        show screen hermione_main
        with d3
        her "Но..."
        m "Просто представьте."
        hide screen hermione_main                                                                                                                                                                                   #HERMIONE
        with d3
        $ h_body = "03_hp/13_hermione_main/body_17.png"
        show screen hermione_main
        with d3
        her "..."
        hide screen hermione_main                                                                                                                                                                                   #HERMIONE
        with d3
        $ h_body = "03_hp/13_hermione_main/body_16.png"
        show screen hermione_main
        her "Хорошо."
        hide screen hermione_main                                                                                                                                                                                   #HERMIONE
        with d3
        $ h_body = "03_hp/13_hermione_main/body_207.png"
        show screen hermione_main
        with d3
        m "А теперь представьте эту вашу... Мудакору."
        hide screen hermione_main                                                                                                                                                                                   #HERMIONE
        with d3
        $ h_body = "03_hp/13_hermione_main/body_16.png"
        show screen hermione_main
        with d3
        her "Манти..."
        m "Я знаю. Это была еще одна проверка. Сосредоточьтесь на зяблике и на том существе."
        hide screen hermione_main                                                                                                                                                                                   #HERMIONE
        with d3
        $ h_body = "03_hp/13_hermione_main/body_207.png"
        show screen hermione_main
        with d3
        m "Во всей вселенной существует только два этих существа..."
        m "И ничего более..."
        hide screen hermione_main                                                                                                                                                                                   #HERMIONE
        with d3
        $ h_body = "03_hp/13_hermione_main/body_208.png"
        show screen hermione_main
        with d3
        her "..."
        m "Они занимают весь ваш разум..."
        her "..."
        hide screen hermione_main                                                                                                                                                                                   #HERMIONE
        with d3
        m "А теперь..."
        menu:
            "Эта хрень сжирает зяблика!":
                hide screen hermione_main                                                                                                                                                                                   #HERMIONE
                with d3
                $ h_body = "03_hp/13_hermione_main/body_18.png"
                show screen hermione_main
                with d3
                her "..?!"
                hide screen hermione_main                                                                                                                                                                                   #HERMIONE
                with d3
                $ h_body = "03_hp/13_hermione_main/body_14.png"
                show screen hermione_main
                with d3
                her "Профессор Дамблдор?!"
                m "Это и есть ответ на ваш вопрос, мисс Грейнджер."
                hide screen hermione_main                                                                                                                                                                                   #HERMIONE
                with d3
                $ h_body = "03_hp/13_hermione_main/body_12.png"
                show screen hermione_main
                with d3
                her "Но..."
                m "Если у вас больше нет вопросов, то вы свободны, мисс Грейнджер."
                hide screen hermione_main                                                                                                                                                                                   #HERMIONE
                with d3
                $ h_body = "03_hp/13_hermione_main/body_04.png"
                show screen hermione_main
                with d3
                her "Но..."
                m "Спокойной ночи, мисс Грейнджер."
                hide screen hermione_main                                                                                                                                                                                   #HERMIONE
                with d3
                $ h_body = "03_hp/13_hermione_main/body_12.png"
                show screen hermione_main
                with d3
                her "..."
                her "..до свидания, Профессор."
                her "..."
                hide screen hermione_main                                                                                                                                                                                   #HERMIONE
                with d3
                $ h_body = "03_hp/13_hermione_main/body_13.png"
                show screen hermione_main
                with d3
                her "{size=-4}(И что это было..?){/size}"
                hide screen hermione_main                                                                                                                                                                                   #HERMIONE
                with d3
                #Гермиона уходит
             
            "Зяблик сжирает эту хрень!":
                g4 "Он вонзает свой острый как бритва клюв в тушу бедной твари!"
                hide screen hermione_main                                                                                                                                                                                   #HERMIONE
                with d3
                $ h_body = "03_hp/13_hermione_main/body_18.png"
                show screen hermione_main
                with d3
                her "..?!"
                g4 "Разрывает ее тушу на мелкие кусочки и начинает пожирать ее внутренности!"
                g4"Глаза мантикоры смотрят на маленькую птичку с выражением отчаяния, ужаса и немой мольбы."
                g4 "Но маленькое чудовище просто продолжает пожирать ее внутренности, издавая отвратительные чавкающие звуки..."
                m "{size=-4}(Черт, кажется у меня встал.){/size}"
                hide screen hermione_main                                                                                                                                                                                   #HERMIONE
                with d3
                $ h_body = "03_hp/13_hermione_main/body_04.png"
                show screen hermione_main
                with d3
                her "Профессор Дамблдор!"
                her "Что это за..."
                m "Это ответ на ваш вопрос, барышня."
                m "А теперь оставьте меня."
                m "Мне нужно, эм... Прочистить трубу."
                hide screen hermione_main                                                                                                                                                                                   #HERMIONE
                with d3
                $ h_body = "03_hp/13_hermione_main/body_12.png"
                show screen hermione_main
                with d3
                her "Но..."
                m "Свободны, мисс Грейнджер."
                hide screen hermione_main                                                                                                                                                                                   #HERMIONE
                with d3
                her "..."
                #Гермиона уходит
                g9 "А мне пора приступать к \"чистке труб\"."
                show screen blkfade # Затемнение экрана
                g4 "Получи, чертова расчлененная тварь!"
                g4 "{size=+7}АГРХ!!!{/size}"
                hide screen blkfade # Экран посветлел xD
                m "..."
                m "Это было странно."
                
            "Схватить ее за грудь!":
                ">Вы легонько сжимаете ее сиськи в своих руках."
                hide screen hermione_main                                                                                                                                                                                   #HERMIONE
                with d3
                $ h_body = "03_hp/13_hermione_main/body_127.png"
                show screen hermione_main
                her "Профессор, что это?"
                m "Хм? Вы это о чем?"
                hide screen hermione_main                                                                                                                                                                                   #HERMIONE
                with d3
                $ h_body = "03_hp/13_hermione_main/body_33.png"
                show screen hermione_main
                with d3
                her "Я чувствую что с моей грудью... Что-то происходит..."
                m "Ах, это... Это часть медитации. Космическая энергия течет в ваше сердце, чтобы дать ответ на интересующий ваш вопрос."
                ">Вы начинаете аккуратно массировать ее грудь."
                hide screen hermione_main                                                                                                                                                                                   #HERMIONE
                with d3
                $ h_body = "03_hp/13_hermione_main/body_32.png"
                show screen hermione_main
                with d3
                her "*Ах!* Космическая энергия? Это что-то... *Ах!* Из индийской магии?"
                m "Точно. А вы очень начитаны, мисс. А теперь сосредоточтесь на космической энергии..."
                hide screen hermione_main                                                                                                                                                                                   #HERMIONE
                with d3
                $ h_body = "03_hp/13_hermione_main/body_74.png"
                show screen hermione_main
                with d3
                her "Хорошо, Профессор."
                her "..."
                ">Жмяк-жмяк..."
                g4 "{size=-4}(Черт, кажется у меня встал!){/size}"
                m "{size=-4}(Думаю не стоит вываливать на нее слишком много в самом начале тренировки...){/size}"
                m "Урок окончен, можете открывать глаза, мисс Грейнджер."
                hide screen hermione_main                                                                                                                                                                                   #HERMIONE
                with d3
                $ h_body = "03_hp/13_hermione_main/body_124.png"
                show screen hermione_main
                with d3
                her "..."
                m "Ну как? Вы получили ответ на свой вопрос?"
                hide screen hermione_main                                                                                                                                                                                   #HERMIONE
                with d3
                $ h_body = "03_hp/13_hermione_main/body_79.png"
                show screen hermione_main
                with d3
                her "Вообще-то..."
                her "У меня было ощущение, что кто-то трогал мою грудь..."
                her "И больше ничего."
                m "Вам понравилось?"
                hide screen hermione_main                                                                                                                                                                                   #HERMIONE
                with d3
                $ h_body = "03_hp/13_hermione_main/body_76.png"
                show screen hermione_main
                with d3
                her "Профессор?! Да как вы..."
                m "Делиться ощущениями от медитации - важная часть тренировки."
                hide screen hermione_main                                                                                                                                                                                   #HERMIONE
                with d3
                $ h_body = "03_hp/13_hermione_main/body_29.png"
                show screen hermione_main
                her "..."
                her "Это были... Необычные ощущения."
                her "Но ответа я так и не получила."
                m "Он прийдет со временем, мисс Грейнджер."
                m "А теперь прошу, оставьте меня. Мне нужно, эм..."
                m "Прочистить трубу."
                hide screen hermione_main                                                                                                                                                                                   #HERMIONE
                with d3
                $ h_body = "03_hp/13_hermione_main/body_45.png"
                show screen hermione_main
                her "...конечно, сэр."
                her "До свидания."
                m "Доброй ночи, мисс Грейнджер."
                #Гермиона уходит
                g9 "Что ж, пора приступать к \"чистке труб\"."
                show screen blkfade # Экран темнеет
                g4 "Получай, маленькая сисястая ведьма!"
                g4 "{size=+7}АГРХ!!!{/size}"
                hide screen blkfade # Экран светлеет
                m "... это было освежающе."
                pass
        
        m "..."
        m "Вряд ли я смогу обучать ее, сам ничего толком не зная об этом мире..."
        m "Думаю, мне стоит поговорить об этом со Снейпом."
        jump day_start    
        #$ knowledge +=1
    
    # "You spend the evening tutoring Hermione. Hermione become a bit smarter."
    
    elif knowledge >= 5 and tutoring_events == 0 and whoring >= 1:
        $ tutoring_events += 1
        "Event 01"
        
    elif knowledge >= 10 and tutoring_events == 1 and whoring >= 2: #LEVEL 02
        $ tutoring_events += 1
        "Event 02"
        
    elif knowledge >= 15 and tutoring_events == 2 and whoring >= 3: #LEVEL 03
        $ tutoring_events += 1
        "Event 03"
        
    elif knowledge >= 20 and tutoring_events == 3 and whoring >= 4: #LEVEL 04
        $ tutoring_events += 1
        "Event 04"
        
    elif knowledge >= 25 and tutoring_events == 4 and whoring >= 5: #LEVEL 05
        $ tutoring_events += 1
        "Event 05"
        
    elif knowledge >= 30 and tutoring_events == 5 and whoring >= 7: #LEVEL 06
        $ tutoring_events += 1
        "Event 06"
        
    elif knowledge >= 35 and tutoring_events == 6 and whoring >= 8: #LEVEL 07
        $ tutoring_events += 1
        "Event 07"
         
    if knowledge >= 40 and tutoring_events == 7 and whoring >= 9: #LEVEL 08
        $ tutoring_events += 1
        "Event 08"
        
    elif knowledge >= 45 and tutoring_events == 8 and whoring >= 11: #LEVEL 09
        $ tutoring_events += 1
        "Event 09"
        
    elif knowledge >= 50 and tutoring_events == 9 and whoring >= 13: #EVENT 10
        $ tutoring_events += 1
        "Event 10"
        
    elif knowledge >= 55 and tutoring_events == 10 and whoring >= 14: #EVENT 10
        $ tutoring_events += 1
        "Event 11"
        
    elif knowledge >= 60 and tutoring_events == 11 and whoring >= 16: #EVENT 11
        $ tutoring_events += 1
        "Event 12"
         
    elif knowledge >= 65 and tutoring_events == 12 and whoring >= 18: #EVENT 12
        $ tutoring_events += 1
        "Event 13"
        
    elif knowledge >= 70 and tutoring_events == 13 and whoring >= 20: #EVENT 13
        $ tutoring_events += 1
        "Event 14"
        
    elif knowledge >= 75 and tutoring_events == 14 and whoring >= 21: #EVENT 14
        $ tutoring_events += 1
        "Event 15"
        
 
    
   
    # $ knowledge +=1
    "> Вы отпускаете Гермиону."
    jump day_start