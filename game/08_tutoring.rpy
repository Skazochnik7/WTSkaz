label tutoring:

    $ tut_happened = True # Turns TRUE after you click the tutoring button and see th message that tutoring is not a part of this game. Make sure the tutoring button will not be visible after that.
    
    #__#hide screen hermione_main                                                                                                                                                                                   #HERMIONE
    #__#with d3                                                                                                                                                                                                                        #HERMIONE
    $herView.hideQQ()
    #__#$ h_xpos=370 #Defines position of the Hermione's full length sprite. (Default 370). (Center: 140)                                                       #HERMIONE
    $ pos = POS_370
    #__#$ h_body = "03_hp/13_hermione_main/body_14.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
    #__#show screen hermione_main                                                                                                                                                                                 #HERMIONE
    #__#with d3                                                                                                                                                                                                                        #HERMIONE
    $herView.showQQ( "body_14.png", pos )
    
    her "Конечно, сэр."
    her "Я только схожу за своими книгами."
    
    #__#hide screen hermione_main                                                                                                                                                                                   #HERMIONE
    $herView.hideQ() #"WARNING_Z"

    #add pose with the book!
    $herView.data().saveState()
    $herView.data().addPose( CharacterExItemPoseBook( herView.mPoseFolder, "pose_with_book.png", G_Z_POSE ) )

    show screen blkfade
    with d3
    $ renpy.play('sounds/door.mp3') #Sound of a door opening.
    pause 2
    $ renpy.play('sounds/door.mp3') #Sound of a door opening.
    pause.3
    

    #__#$ only_upper = True
    #__#$ ne = False # Desplays a fishnets in hermione_main screen.


    #__#$ h_xpos=140 #Defines position of the Hermione's full length sprite. (Default 370). (Center: 140)                                                       #HERMIONE
    $ pos = POS_140
    #__#$ h_body = "03_hp/13_hermione_main/body_199.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
    #__#show screen hermione_main                                                                                                                                                                                 #HERMIONE
    #__#with d3                                                                                                                                                                                                                        #HERMIONE
    $herView.showQQ( "body_199.png", pos )
    
    
    hide screen blkfade
    with d3
    
    show screen ctc
    pause
    hide screen ctc
    
    #__#hide screen hermione_main                                                                                                                                                                                   #HERMIONE
    #__#with d3                                                                                                                                                                                                                        #HERMIONE
    $herView.hideQQ()
                                                                                                                                                                                                                        #HERMIONE
    if knowledge == 0:
        $ tut_happened = True
        #__#$ h_body = "03_hp/13_hermione_main/body_199.png"
        #__#show screen hermione_main
        #__#with d3
        $herView.showQQ( "body_199.png", pos )
        play music "music/Chipper Doodle v2.mp3" fadein 1 fadeout 1
        her "Еще раз спасибо за то, что делаете это для меня, сэр."
        her "Вы, должно быть, очень заняты школьными делами, но все равно вы нашли время на занятия со мной..."
        her "Я хочу сказать, что очень ценю вашу заботу."
        m "Не стоит благодарностей, мисс Грейнджер. Следить за успеваемостью учеников - одна из главных обязанностей директора."
        g9 "{size=-4}(Кроме того, я собираюсь залезть к тебе в трусики, когда мы закончим.){/size}"
        #__#hide screen hermione_main
        #__#with d3
        $herView.hideQQ()

        # hide books pose
        $herView.data().delPose()

        #__#$ only_upper = False
        #__#$ h_body = "03_hp/13_hermione_main/body_08.png"
        #__#show screen hermione_main
        #__#with d3
        $herView.showQQ( "body_08.png", pos )
        her "Вы что-то сказали, сэр?"                                                                                                                                                                                  #HERMIONE
        m "Кхм... Я сказал, что вы без проблем сдадите любой экзамен, когда мы закончим."
        #__#hide screen hermione_main
        #__#with d3
        $herView.hideQQ()
        #__#$ h_body = "03_hp/13_hermione_main/body_06.png"
        #__#show screen hermione_main
        #__#with d3
        $herView.showQQ( "body_06.png", pos )
        her "Я ни на секунду не сомневалась в этом."
        her "Ведь вы - Альбус Дамблдор - один из самых великих волшебников нашего времени."
        g9 "Еще бы! Я просто шикарен."
        #__#hide screen hermione_main                                                                                                                                                                                   #HERMIONE
        #__#with d3
        $herView.hideQQ()
        #__#$ h_body = "03_hp/13_hermione_main/body_17.png"
        #__#show screen hermione_main
        #__#with d3
        $herView.showQQ( "body_17.png", pos )
        her "..."
        #__#hide screen hermione_main
        #__#with d3        
        $herView.hideQQ()
        #__#$ h_body = "03_hp/13_hermione_main/body_06.png"
        #__#show screen hermione_main
        #__#with d3
        $herView.showQQ( "body_06.png", pos )
        her "Давайте приступим, Профессор?"                                                                                                                                                                                   #HERMIONE
        m "Конечно, дитя. У тебя есть ко мне какие-то вопросы?"
        #__#show screen hermione_main
        #__#with d3
        $herView.showQQ( "body_06.png", pos )
        her "Думаю, пока нет. Хотя..."
        #__#hide screen hermione_main
        #__#with d3
        $herView.hideQQ()
        #__#$ h_body = "03_hp/13_hermione_main/body_14.png"
        #__#show screen hermione_main
        #__#with d3
        $herView.showQQ( "body_14.png", pos )
        her "Есть кое-что, в чем я сомневаюсь, и это не дает мне покоя."
        g9 "И что же это? Не стесняйся, можешь спросить у самого великого волшебника в мире!"
        #__#hide screen hermione_main                                                                                                                                                                                   #HERMIONE
        #__#with d3
        $herView.hideQQ()
        #__#$ h_body = "03_hp/13_hermione_main/body_12.png"
        #__#show screen hermione_main
        #__#with d3
        $herView.showQQ( "body_12.png", pos )
        her "..."
        #__#hide screen hermione_main                                                                                                                                                                                   #HERMIONE
        #__#with d3
        $herView.hideQQ()
        #__#$ h_body = "03_hp/13_hermione_main/body_04.png"
        #__#show screen hermione_main
        #__#with d3
        $herView.showQQ( "body_04.png", pos )
        her "Хорошо..."
        #__#hide screen hermione_main                                                                                                                                                                                   #HERMIONE
        #__#with d3
        $herView.hideQQ()
        #__#$ h_body = "03_hp/13_hermione_main/body_11.png"
        #__#show screen hermione_main
        #__#with d3
        $herView.showQQ( "body_11.png", pos )
        her "Я не совсем уверена, как заклинание \"патискор вальде\" может хорошо работать против перуанских мантикор..."
        her "Ведь в таком случае идеально должно подходить \"гэйли секундум\", но в издании \"Эксцилиус прохороса\" 1831 утверждается обратное..."
        #__#hide screen hermione_main                                                                                                                                                                                   #HERMIONE
        #__#with d3
        $herView.hideQQ()
        #__#$ h_body = "03_hp/13_hermione_main/body_06.png"
        #__#show screen hermione_main
        #__#with d3
        $herView.showQQ( "body_06.png", pos )
        her "Не могли бы вы сказать, в чем моя ошибка?"                                                                                                                                                                                  #HERMIONE
        m "Конечно, дитя..."
        m "..."
        m "..."
        m "..!"
        m "{size=-4}(Что за ахинею она только что несла?){/size}"
        m "{size=-4}(Так, соберись, Джинни...){/size}"
        m "Кхм... Стоит учесть, что мы говорим не о простых мунтикорах, а именно пердуанских..."
        #__#hide screen hermione_main                                                                                                                                                                                   #HERMIONE
        #__#with d3
        $herView.hideQQ()
        #__#$ h_body = "03_hp/13_hermione_main/body_04.png"
        #__#show screen hermione_main
        #__#with d3
        $herView.showQQ( "body_04.png", pos )
        her "\"Перуанских мантикор\", сэр..."
        #__#hide screen hermione_main                                                                                                                                                                                   #HERMIONE
        #__#with d3
        $herView.hideQQ()
        m "Верно! Умница, девочка. Я просто проверял тебя. Назови мне основные признаки этих пер... Существ."
        #__#hide screen hermione_main                                                                                                                                                                                   #HERMIONE
        #__#with d3
        $herView.hideQQ()
        #__#$ h_body = "03_hp/13_hermione_main/body_01.png"
        #__#show screen hermione_main
        #__#with d3
        $herView.showQQ( "body_01.png", pos )
        her "Конечно, сэр."
        #__#$ h_body = "03_hp/13_hermione_main/body_14.png"
        #__#show screen hermione_main
        #__#with d3
        $herView.showQQ( "body_14.png", pos )
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
        #__#hide screen hermione_main                                                                                                                                                                                   #HERMIONE
        #__#with d3
        $herView.hideQQ()
        #__#$ h_body = "03_hp/13_hermione_main/body_13.png"
        #__#show screen hermione_main
        #__#with d3
        $herView.showQQ( "body_13.png", pos )
        her "Эм... Впервые их подробно изучил член Мальбуржской ассоциации магов - Истафар Ариус..."
        #__#hide screen hermione_main                                                                                                                                                                                   #HERMIONE
        #__#with d3
        $herView.hideQQ()
        #__#$ h_body = "03_hp/13_hermione_main/body_11.png"
        #__#show screen hermione_main
        #__#with d3
        $herView.showQQ( "body_11.png", pos )
        her "Я что-то сказала не так..?"
        play music "music/Chipper Doodle v2.mp3" fadein 1 fadeout 1
        m "... нет-нет, все верно..."
        #__#hide screen hermione_main                                                                                                                                                                                   #HERMIONE
        #__#with d3
        $herView.hideQQ()
        #__#$ h_body = "03_hp/13_hermione_main/body_01.png"
        #__#show screen hermione_main
        #__#with d3
        $herView.showQQ( "body_01.png", pos )
        her "Тогда можем ли мы вернуться к моему вопросу, сэр?"        
        m "Ах, да... Вопрос..."
        m "Кхм..."
        m "Мисс Грейнджер, что вы знаете о зябликах?"
        #__#hide screen hermione_main                                                                                                                                                                                   #HERMIONE
        #__#with d3
        $herView.hideQQ()
        #__#$ h_body = "03_hp/13_hermione_main/body_14.png"
        #__#show screen hermione_main
        #__#with d3
        $herView.showQQ( "body_14.png", pos )
        her "Простите, сэр?"
        m "Закройте глаза и представьте зяблика, мисс Грейнджер."
        #__#hide screen hermione_main                                                                                                                                                                                   #HERMIONE
        #__#with d3
        $herView.hideQQ()
        #__#$ h_body = "03_hp/13_hermione_main/body_11.png"
        #__#show screen hermione_main
        #__#with d3
        $herView.showQQ( "body_11.png", pos )
        her "Но..."
        m "Просто представьте."
        #__#hide screen hermione_main                                                                                                                                                                                   #HERMIONE
        #__#with d3
        $herView.hideQQ()
        #__#$ h_body = "03_hp/13_hermione_main/body_17.png"
        #__#show screen hermione_main
        #__#with d3
        $herView.showQQ( "body_17.png", pos )
        her "..."
        #__#hide screen hermione_main                                                                                                                                                                                   #HERMIONE
        #__#with d3
        $herView.hideQQ()
        #__#$ h_body = "03_hp/13_hermione_main/body_16.png"
        #__#show screen hermione_main
        $herView.showQ( "body_16.png", pos ) #"WARNING_Z"
        her "Хорошо."
        #__#hide screen hermione_main                                                                                                                                                                                   #HERMIONE
        #__#with d3
        $herView.hideQQ()
        #__#$ h_body = "03_hp/13_hermione_main/body_207.png"
        #__#show screen hermione_main
        #__#with d3
        $herView.showQQ( "body_207.png", pos )
        m "А теперь представьте эту вашу... Мудакору."
        #__#hide screen hermione_main                                                                                                                                                                                   #HERMIONE
        #__#with d3
        $herView.hideQQ()
        #__#$ h_body = "03_hp/13_hermione_main/body_16.png"
        #__#show screen hermione_main
        #__#with d3
        $herView.showQQ( "body_16.png", pos )
        her "Манти..."
        m "Я знаю. Это была еще одна проверка. Сосредоточьтесь на зяблике и на том существе."
        #__#hide screen hermione_main                                                                                                                                                                                   #HERMIONE
        #__#with d3
        $herView.hideQQ()
        #__#$ h_body = "03_hp/13_hermione_main/body_207.png"
        #__#show screen hermione_main
        #__#with d3
        $herView.showQQ( "body_207.png", pos )
        m "Во всей вселенной существует только два этих существа..."
        m "И ничего более..."
        #__#hide screen hermione_main                                                                                                                                                                                   #HERMIONE
        #__#with d3
        $herView.hideQQ()
        #__#$ h_body = "03_hp/13_hermione_main/body_208.png"
        #__#show screen hermione_main
        #__#with d3
        $herView.showQQ( "body_208.png", pos )
        her "..."
        m "Они занимают весь ваш разум..."
        her "..."
        #__#hide screen hermione_main                                                                                                                                                                                   #HERMIONE
        #__#with d3
        $herView.hideQQ()
        m "А теперь..."
        $ menu_x = 0.5 #Default position of the menu (0.5). Version B is $ menu_x = 0.2
        menu:
            "Эта хрень сжирает зяблика!":
                #__#hide screen hermione_main                                                                                                                                                                                   #HERMIONE
                #__#with d3
                $herView.hideQQ()
                #__#$ h_body = "03_hp/13_hermione_main/body_18.png"
                #__#show screen hermione_main
                #__#with d3
                $herView.showQQ( "body_18.png", pos )
                her "..?!"
                #__#hide screen hermione_main                                                                                                                                                                                   #HERMIONE
                #__#with d3
                $herView.hideQQ()
                #__#$ h_body = "03_hp/13_hermione_main/body_14.png"
                #__#show screen hermione_main
                #__#with d3
                $herView.showQQ( "body_14.png", pos )
                her "Профессор Дамблдор?!"
                m "Это и есть ответ на ваш вопрос, мисс Грейнджер."
                #__#hide screen hermione_main                                                                                                                                                                                   #HERMIONE
                #__#with d3
                $herView.hideQQ()
                #__#$ h_body = "03_hp/13_hermione_main/body_12.png"
                #__#show screen hermione_main
                #__#with d3
                $herView.showQQ( "body_12.png", pos )
                her "Но..."
                m "Если у вас больше нет вопросов, то вы свободны, мисс Грейнджер."
                #__#hide screen hermione_main                                                                                                                                                                                   #HERMIONE
                #__#with d3
                $herView.hideQQ()
                #__#$ h_body = "03_hp/13_hermione_main/body_04.png"
                #__#show screen hermione_main
                #__#with d3
                $herView.showQQ( "body_04.png", pos )
                her "Но..."
                m "Спокойной ночи, мисс Грейнджер."
                #__#hide screen hermione_main                                                                                                                                                                                   #HERMIONE
                #__#with d3
                $herView.hideQQ()
                #__#$ h_body = "03_hp/13_hermione_main/body_12.png"
                #__#show screen hermione_main
                #__#with d3
                $herView.showQQ( "body_12.png", pos )
                her "..."
                her "..до свидания, Профессор."
                her "..."
                #__#hide screen hermione_main                                                                                                                                                                                   #HERMIONE
                #__#with d3
                $herView.hideQQ()
                #__#$ h_body = "03_hp/13_hermione_main/body_13.png"
                #__#show screen hermione_main
                #__#with d3
                $herView.showQQ( "body_13.png", pos )
                her "{size=-4}(И что это было..?){/size}"
                #__#hide screen hermione_main                                                                                                                                                                                   #HERMIONE
                #__#with d3
                $herView.hideQQ()
                #Гермиона уходит
                call hermione_leave_tutoring
             
            "Зяблик сжирает эту хрень!":
                g4 "Он вонзает свой острый как бритва клюв в тушу бедной твари!"
                #__#hide screen hermione_main                                                                                                                                                                                   #HERMIONE
                #__#with d3
                $herView.hideQQ()
                #__#$ h_body = "03_hp/13_hermione_main/body_18.png"
                #__#show screen hermione_main
                #__#with d3
                $herView.showQQ( "body_18.png", pos )
                her "..?!"
                g4 "Разрывает ее тушу на мелкие кусочки и начинает пожирать ее внутренности!"
                g4 "Глаза мантикоры смотрят на маленькую птичку с выражением отчаяния, ужаса и немой мольбы."
                g4 "Но маленькое чудовище просто продолжает пожирать ее внутренности, издавая отвратительные чавкающие звуки..."
                m "{size=-4}(Черт, кажется у меня встал.){/size}"
                #__#hide screen hermione_main                                                                                                                                                                                   #HERMIONE
                #__#with d3
                $herView.hideQQ()
                #__#$ h_body = "03_hp/13_hermione_main/body_04.png"
                #__#show screen hermione_main
                #__#with d3
                $herView.showQQ( "body_04.png", pos )
                her "Профессор Дамблдор!"
                her "Что это за..."
                m "Это ответ на ваш вопрос, барышня."
                m "А теперь оставьте меня."
                m "Мне нужно, эм... Прочистить трубу."
                #__#hide screen hermione_main                                                                                                                                                                                   #HERMIONE
                #__#with d3
                $herView.hideQQ()
                #__#$ h_body = "03_hp/13_hermione_main/body_12.png"
                #__#show screen hermione_main
                #__#with d3
                $herView.showQQ( "body_12.png", pos )
                her "Но..."
                m "Свободны, мисс Грейнджер."
                #__#hide screen hermione_main                                                                                                                                                                                   #HERMIONE
                #__#with d3
                $herView.hideQQ()
                her "..."
                #Гермиона уходит
                call hermione_leave_tutoring

                g9 "А мне пора приступать к \"чистке труб\"."
                show screen blkfade # Затемнение экрана
                g4 "Получи, чертова расчлененная тварь!"
                g4 "{size=+7}АГРХ!!!{/size}"
                hide screen blkfade # Экран посветлел xD
                m "..."
                m "Это было странно."
                
            "Схватить ее за грудь!":
                ">Вы легонько сжимаете ее сиськи в своих руках."
                #__#hide screen hermione_main                                                                                                                                                                                   #HERMIONE
                #__#with d3
                $herView.hideQQ()
                #__#$ h_body = "03_hp/13_hermione_main/body_127.png"
                #__#show screen hermione_main
                $herView.showQQ( "body_127.png", pos )
                her "Профессор, что это?"
                m "Хм? Вы это о чем?"
                #__#hide screen hermione_main                                                                                                                                                                                   #HERMIONE
                #__#with d3
                $herView.hideQQ()
                #__#$ h_body = "03_hp/13_hermione_main/body_33.png"
                #__#show screen hermione_main
                #__#with d3
                $herView.showQQ( "body_33.png", pos )
                her "Я чувствую что с моей грудью... Что-то происходит..."
                m "Ах, это... Это часть медитации. Космическая энергия течет в ваше сердце, чтобы дать ответ на интересующий вас вопрос."
                ">Вы начинаете аккуратно массировать ее грудь."
                #__#hide screen hermione_main                                                                                                                                                                                   #HERMIONE
                #__#with d3
                $herView.hideQQ()
                #__#$ h_body = "03_hp/13_hermione_main/body_32.png"
                #__#show screen hermione_main
                #__#with d3
                $herView.showQQ( "body_32.png", pos )
                her "*Ах!* Космическая энергия? Это что-то... *Ах!* Из индийской магии?"
                m "Точно. А вы очень начитаны, мисс. А теперь сосредоточтесь на космической энергии..."
                #__#hide screen hermione_main                                                                                                                                                                                   #HERMIONE
                #__#with d3
                $herView.hideQQ()
                #__#$ h_body = "03_hp/13_hermione_main/body_74.png"
                #__#show screen hermione_main
                #__#with d3
                $herView.showQQ( "body_74.png", pos )
                her "Хорошо, Профессор."
                her "..."
                ">Жмяк-жмяк..."
                g4 "{size=-4}(Черт, кажется у меня встал!){/size}"
                m "{size=-4}(Думаю, не стоит вываливать на нее слишком много в самом начале тренировок...){/size}"
                m "Урок окончен, можете открывать глаза, мисс Грейнджер."
                #__#hide screen hermione_main                                                                                                                                                                                   #HERMIONE
                #__#with d3
                $herView.hideQQ()
                #__#$ h_body = "03_hp/13_hermione_main/body_124.png"
                #__#show screen hermione_main
                #__#with d3
                $herView.showQQ( "body_124.png", pos )
                her "..."
                m "Ну как? Вы получили ответ на свой вопрос?"
                #__#hide screen hermione_main                                                                                                                                                                                   #HERMIONE
                #__#with d3
                $herView.hideQQ()
                #__#$ h_body = "03_hp/13_hermione_main/body_79.png"
                #__#show screen hermione_main
                #__#with d3
                $herView.showQQ( "body_79.png", pos )
                her "Вообще-то..."
                her "У меня было ощущение, что кто-то трогал мою грудь..."
                her "И больше ничего."
                m "Вам понравилось?"
                #__#hide screen hermione_main                                                                                                                                                                                   #HERMIONE
                #__#with d3
                $herView.hideQQ()
                #__#$ h_body = "03_hp/13_hermione_main/body_76.png"
                #__#show screen hermione_main
                #__#with d3
                $herView.showQQ( "body_76.png", pos )
                her "Профессор?! Да как вы..."
                m "Делиться ощущениями от медитации - важная часть тренировки."
                #__#hide screen hermione_main                                                                                                                                                                                   #HERMIONE
                #__#with d3
                $herView.hideQQ()
                #__#$ h_body = "03_hp/13_hermione_main/body_29.png"
                #__#show screen hermione_main
                $herView.showQ( "body_29.png", pos ) #"WARNING_Z"
                her "..."
                her "Это были... Необычные ощущения."
                her "Но ответа я так и не получила."
                m "Он прийдет со временем, мисс Грейнджер."
                m "А теперь прошу, оставьте меня. Мне нужно, эм..."
                m "Прочистить трубу."
                #__#hide screen hermione_main                                                                                                                                                                                   #HERMIONE
                #__#with d3
                $herView.hideQQ()
                #__#$ h_body = "03_hp/13_hermione_main/body_45.png"
                #__#show screen hermione_main
                $herView.showQ( "body_45.png", pos ) #"WARNING_Z"
                her "...конечно, сэр."
                her "До свидания."
                m "Доброй ночи, мисс Грейнджер."
                $herView.hideQQ()
                #Гермиона уходит
                call hermione_leave_tutoring

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

        $herView.data().loadState()
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


label hermione_leave_tutoring:
    hide screen hermione_02 #Hermione stands still.
    with d3
    $ walk_xpos=400 #Animation of walking chibi. (From)
    $ walk_xpos2=610 #Coordinates of it's movement. (To)
    $ hermione_speed = 02.0 #The speed of moving the walking animation across the screen.
    show screen hermione_walk_01_f 
    pause 2
    hide screen hermione_walk_01_f 
    $ renpy.play('sounds/door.mp3') #Sound of a door opening.
    with Dissolve(.3)

    return