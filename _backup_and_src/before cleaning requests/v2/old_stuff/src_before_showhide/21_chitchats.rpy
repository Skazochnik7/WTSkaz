label snape_chitchat:
    if not chitchat_event_01_happened and tutoring_hermione_unlocked and days_without_an_event >=2:
        jump chitchat_event_01
    
    

    $ one_of_ten = renpy.random.randint(1, 10) #Generating one number out of three for various porpoises.
    
    ### CHIT CHATS WITH SNAPE ###
    if whoring >= 0 and whoring <= 2: # WHORING LEVEL 01.
        if one_of_ten == 1:
            hide screen snape_main                                                                                                                   #SNAPE
            with d3                                                                                                                                                  #SNAPE
            $ s_sprite = "03_hp/10_snape_main/24.png"                                                                            #SNAPE
            show screen snape_main                                                                                                                  #SNAPE
            with d3                                                                                                                                                   #SNAPE
            sna "Ты действительно думаешь что сделаешь это?"
            hide screen snape_main                                                                                                                   #SNAPE
            with d3                                                                                                                                                  #SNAPE
            $ s_sprite = "03_hp/10_snape_main/snape_25.png"                                                                            #SNAPE
            show screen snape_main                                                                                                                  #SNAPE
            with d3                                                                                                                                                   #SNAPE
            sna "Ты действительно думаешь что сломаешь девчонку?"
        
        elif one_of_ten == 2:
            hide screen snape_main                                                                                                                   #SNAPE
            with d3                                                                                                                                                  #SNAPE
            $ s_sprite = "03_hp/10_snape_main/snape_01.png"                                                                            #SNAPE
            show screen snape_main                                                                                                                  #SNAPE
            with d3                                                                                                                                                   #SNAPE
            sna "Ты тоже ненавидишь эту жалкую, солнечную погоду?"
            hide screen snape_main                                                                                                                   #SNAPE
            with d3                                                                                                                                                  #SNAPE
            $ s_sprite = "03_hp/10_snape_main/snape_06.png"                                                                            #SNAPE
            show screen snape_main                                                                                                                  #SNAPE
            with d3                                                                                                                                                   #SNAPE
            sna "Я хотел бы, чтобы дождь был каждый день." 
            
        elif one_of_ten == 3:
            hide screen snape_main                                                                                                                   #SNAPE
            with d3                                                                                                                                                  #SNAPE
            $ s_sprite = "03_hp/10_snape_main/snape_06.png"                                                                            #SNAPE
            show screen snape_main                                                                                                                  #SNAPE
            with d3                                                                                                                                                   #SNAPE
            sna "Кажется я снова сомневаюсь в нашем плане..."
            
        elif one_of_ten == 4:
            hide screen snape_main                                                                                                                   #SNAPE
            with d3                                                                                                                                                  #SNAPE
            $ s_sprite = "03_hp/10_snape_main/snape_05.png"                                                                            #SNAPE
            show screen snape_main                                                                                                                  #SNAPE
            with d3                                                                                                                                                   #SNAPE
            sna "Ты уверен что ты не Альбус Дамблдор?"
            sna "Иногда мне всё еще трудно в это поверить..."
  
        elif one_of_ten == 5:
            hide screen snape_main                                                                                                                   #SNAPE
            with d3                                                                                                                                                  #SNAPE
            $ s_sprite = "03_hp/10_snape_main/snape_01.png"                                                                            #SNAPE
            show screen snape_main                                                                                                                  #SNAPE
            with d3                                                                                                                                                   #SNAPE
            sna "Однажды я убил ученика."
            hide screen snape_main                                                                                                                   #SNAPE
            with d3                                                                                                                                                  #SNAPE
            $ s_sprite = "03_hp/10_snape_main/snape_02.png"                                                                            #SNAPE
            show screen snape_main                                                                                                                  #SNAPE
            with d3                                                                                                                                                   #SNAPE
            sna "Да... Я задушил недомерка своими руками."
            hide screen snape_main                                                                                                                   #SNAPE
            with d3                                                                                                                                                  #SNAPE
            $ s_sprite = "03_hp/10_snape_main/snape_03.png"                                                                            #SNAPE
            show screen snape_main                                                                                                                  #SNAPE
            with d3                                                                                                                                                   #SNAPE
            sna "........*Тихо ворчит*."
            hide screen snape_main                                                                                                                   #SNAPE
            with d3                                                                                                                                                  #SNAPE
            $ s_sprite = "03_hp/10_snape_main/snape_05.png"                                                                            #SNAPE
            show screen snape_main                                                                                                                  #SNAPE
            with d3                                                                                                                                                   #SNAPE
            sna "Это звучало правдопадобно?"
            hide screen snape_main                                                                                                                   #SNAPE
            with d3                                                                                                                                                  #SNAPE
            $ s_sprite = "03_hp/10_snape_main/snape_06.png"                                                                            #SNAPE
            show screen snape_main                                                                                                                  #SNAPE
            with d3                                                                                                                                                   #SNAPE
            sna "Когда эти животные перестанут меня боятся, мне конец."
            hide screen snape_main                                                                                                                   #SNAPE
            with d3                                                                                                                                                  #SNAPE
            $ s_sprite = "03_hp/10_snape_main/snape_26.png"                                                                            #SNAPE
            show screen snape_main                                                                                                                  #SNAPE
            with d3                                                                                                                                                   #SNAPE
            sna "Вселять страх в сердца своих студентов это важная задача для учителей."

        elif one_of_ten == 6:
            hide screen snape_main                                                                                                                   #SNAPE
            with d3                                                                                                                                                  #SNAPE
            $ s_sprite = "03_hp/10_snape_main/snape_04.png"                                                                            #SNAPE
            show screen snape_main                                                                                                                  #SNAPE
            with d3                                                                                                                                                   #SNAPE
            sna "Эти ничтожества Уизли..."
            hide screen snape_main                                                                                                                   #SNAPE
            with d3                                                                                                                                                  #SNAPE
            $ s_sprite = "03_hp/10_snape_main/snape_07.png"                                                                            #SNAPE
            show screen snape_main                                                                                                                  #SNAPE
            with d3                                                                                                                                                   #SNAPE
            sna "Однажды я просто не выдержу, обещаю."

        elif one_of_ten == 7:
            hide screen snape_main                                                                                                                   #SNAPE
            with d3                                                                                                                                                  #SNAPE
            $ s_sprite = "03_hp/10_snape_main/snape_05.png"                                                                            #SNAPE
            show screen snape_main                                                                                                                  #SNAPE
            with d3                                                                                                                                                   #SNAPE
            sna "Эта совиная почта нелепа, разве не так?"
            sna "Я бы предпочёл использовать воронов."
            
        elif one_of_ten == 8:
            hide screen snape_main                                                                                                                   #SNAPE
            with d3                                                                                                                                                  #SNAPE
            $ s_sprite = "03_hp/10_snape_main/snape_06.png"                                                                            #SNAPE
            show screen snape_main                                                                                                                  #SNAPE
            with d3                                                                                                                                                   #SNAPE
            sna "У меня был худший день в моей жизни..."
            sna "Так что я не в настроение для разговоров..."
            
        elif one_of_ten == 9:
            hide screen snape_main                                                                                                                   #SNAPE
            with d3                                                                                                                                                  #SNAPE
            $ s_sprite = "03_hp/10_snape_main/snape_04.png"                                                                            #SNAPE
            show screen snape_main                                                                                                                  #SNAPE
            with d3                                                                                                                                                   #SNAPE
            sna "Быть волшебником это значит работать 24 часа в сутки..."
            hide screen snape_main                                                                                                                   #SNAPE
            with d3                                                                                                                                                  #SNAPE
            $ s_sprite = "03_hp/10_snape_main/snape_03.png"                                                                            #SNAPE
            show screen snape_main                                                                                                                  #SNAPE
            with d3                                                                                                                                                   #SNAPE
            sna "7 дней в неделю..."
            hide screen snape_main                                                                                                                   #SNAPE
            with d3                                                                                                                                                  #SNAPE
            $ s_sprite = "03_hp/10_snape_main/snape_04.png"                                                                            #SNAPE
            show screen snape_main                                                                                                                  #SNAPE
            with d3                                                                                                                                                   #SNAPE
            sna "365 дней в году."
            sna "И без отпуска..."
            
        elif one_of_ten == 10:
            hide screen snape_main                                                                                                                   #SNAPE
            with d3                                                                                                                                                  #SNAPE
            $ s_sprite = "03_hp/10_snape_main/snape_04.png"                                                                            #SNAPE
            show screen snape_main                                                                                                                  #SNAPE
            with d3                                                                                                                                                   #SNAPE
            sna "Квиддич..."
            hide screen snape_main                                                                                                                   #SNAPE
            with d3                                                                                                                                                  #SNAPE
            $ s_sprite = "03_hp/10_snape_main/snape_10.png"                                                                            #SNAPE
            show screen snape_main                                                                                                                  #SNAPE
            with d3                                                                                                                                                   #SNAPE
            sna "Что за трата ресурсов!"
            hide screen snape_main                                                                                                                   #SNAPE
            with d3                                                                                                                                                  #SNAPE
            $ s_sprite = "03_hp/10_snape_main/snape_04.png"                                                                            #SNAPE
            show screen snape_main                                                                                                                  #SNAPE
            with d3                                                                                                                                                   #SNAPE
            
            
        
        
    
    if whoring >= 3 and whoring <= 5: # WHORING LEVEL 02.
        if one_of_ten == 1:
            hide screen snape_main                                                                                                                   #SNAPE
            with d3                                                                                                                                                  #SNAPE
            $ s_sprite = "03_hp/10_snape_main/24.png"                                                                            #SNAPE
            show screen snape_main                                                                                                                  #SNAPE
            with d3                                                                                                                                                   #SNAPE
            sna "Я не замечаю никаких изменений в поведение мисс Греинджер..."
            hide screen snape_main                                                                                                                   #SNAPE
            with d3                                                                                                                                                  #SNAPE
            $ s_sprite = "03_hp/10_snape_main/snape_05.png"                                                                            #SNAPE
            show screen snape_main                                                                                                                  #SNAPE
            with d3                                                                                                                                                   #SNAPE
            sna "Ты уверен, что знаешь, что ты делаешь?"
            hide screen snape_main                                                                                                                   #SNAPE
            with d3                                                                                                                                                  #SNAPE
            $ s_sprite = "03_hp/10_snape_main/snape_09.png"                                                                            #SNAPE
            show screen snape_main                                                                                                                  #SNAPE
            with d3                                                                                                                                                   #SNAPE
        
        elif one_of_ten == 2:
            hide screen snape_main                                                                                                                   #SNAPE
            with d3                                                                                                                                                  #SNAPE
            $ s_sprite = "03_hp/10_snape_main/24.png"                                                                            #SNAPE
            show screen snape_main                                                                                                                  #SNAPE
            with d3                                                                                                                                                   #SNAPE
            sna "Я чувствую власть, награждая факультеты очками или отнимая их когда захочу."
            sna "Мой авторитет среди студентов растёт с каждым днём..."
            hide screen snape_main                                                                                                                   #SNAPE
            with d3                                                                                                                                                  #SNAPE
            $ s_sprite = "03_hp/10_snape_main/snape_02.png"                                                                            #SNAPE
            show screen snape_main                                                                                                                  #SNAPE
            with d3                                                                                                                                                   #SNAPE
            sna "И когда я говорю \"авторитет\" я имею в виду \"страх\"."

        elif one_of_ten == 3:
            hide screen snape_main                                                                                                                   #SNAPE
            with d3                                                                                                                                                  #SNAPE
            $ s_sprite = "03_hp/10_snape_main/24.png"                                                                            #SNAPE
            show screen snape_main                                                                                                                  #SNAPE
            with d3                                                                                                                                                   #SNAPE
            sna "Ты знал что полная луна влияет на мужскую силу?"
            sna "Она также помогает сосредоточится на деле, делая тебя более собраным."
            hide screen snape_main                                                                                                                   #SNAPE
            with d3                                                                                                                                                  #SNAPE
            $ s_sprite = "03_hp/10_snape_main/snape_28.png"                                                                            #SNAPE
            show screen snape_main                                                                                                                  #SNAPE
            with d3                                                                                                                                                    #SNAPE
            sna "Но кого это волнует, верно?"
            hide screen snape_main                                                                                                                   #SNAPE
            with d3                                                                                                                                                  #SNAPE
            $ s_sprite = "03_hp/10_snape_main/snape_29.png"                                                                            #SNAPE
            show screen snape_main                                                                                                                  #SNAPE
            with d3                                                                                                                                                   #SNAPE

        elif one_of_ten == 4:
            hide screen snape_main                                                                                                                   #SNAPE
            with d3                                                                                                                                                  #SNAPE
            $ s_sprite = "03_hp/10_snape_main/snape_06.png"                                                                            #SNAPE
            show screen snape_main                                                                                                                  #SNAPE
            with d3                                                                                                                                                   #SNAPE
            sna "Мои драгоценные Слизеринки делают эту пытку стоящей..."
            hide screen snape_main                                                                                                                   #SNAPE
            with d3                                                                                                                                                  #SNAPE
            $ s_sprite = "03_hp/10_snape_main/snape_19.png"                                                                            #SNAPE
            show screen snape_main                                                                                                                  #SNAPE
            with d3                                                                                                                                                   #SNAPE
            sna "Их юбки становятся короче с каждой неделей, честно."
  
        elif one_of_ten == 5:
            hide screen snape_main                                                                                                                   #SNAPE
            with d3                                                                                                                                                  #SNAPE
            $ s_sprite = "03_hp/10_snape_main/snape_06.png"                                                                            #SNAPE
            show screen snape_main                                                                                                                  #SNAPE
            with d3                                                                                                                                                   #SNAPE
            sna "Было время когда я был молод и полон надежды..."
            hide screen snape_main                                                                                                                   #SNAPE
            with d3                                                                                                                                                  #SNAPE
            $ s_sprite = "03_hp/10_snape_main/snape_28.png"                                                                            #SNAPE
            show screen snape_main                                                                                                                  #SNAPE
            with d3                                                                                                                                                   #SNAPE
            sna "Ха-ха... я просто шучу, приятель"
            hide screen snape_main                                                                                                                   #SNAPE
            with d3                                                                                                                                                  #SNAPE
            $ s_sprite = "03_hp/10_snape_main/snape_29.png"                                                                            #SNAPE
            show screen snape_main                                                                                                                  #SNAPE
            with d3                                                                                                                                                   #SNAPE
            sna "Я никогда не был полон надежды..."

        elif one_of_ten == 6:
            hide screen snape_main                                                                                                                   #SNAPE
            with d3                                                                                                                                                  #SNAPE
            $ s_sprite = "03_hp/10_snape_main/snape_09.png"                                                                            #SNAPE
            show screen snape_main                                                                                                                  #SNAPE
            with d3                                                                                                                                                   #SNAPE
            sna "Дуэли это одна из моих сильных сторон, ну ты понимаешь..."

        elif one_of_ten == 7:
            hide screen snape_main                                                                                                                   #SNAPE
            with d3                                                                                                                                                  #SNAPE
            $ s_sprite = "03_hp/10_snape_main/snape_05.png"                                                                            #SNAPE
            show screen snape_main                                                                                                                  #SNAPE
            with d3                                                                                                                                                   #SNAPE
            sna "Хех, \"Движение прав человека\"...?"
            hide screen snape_main                                                                                                                   #SNAPE
            with d3                                                                                                                                                  #SNAPE
            $ s_sprite = "03_hp/10_snape_main/snape_04.png"                                                                            #SNAPE
            show screen snape_main                                                                                                                  #SNAPE
            with d3                                                                                                                                                   #SNAPE
            sna "Что дальше? Ассоциация по восстановлению независимости эльфов?"
            hide screen snape_main                                                                                                                   #SNAPE
            with d3                                                                                                                                                  #SNAPE
            $ s_sprite = "03_hp/10_snape_main/snape_06.png"                                                                            #SNAPE
            show screen snape_main                                                                                                                  #SNAPE
            with d3                                                                                                                                                   #SNAPE
            sna "Как может лучший студент быть таким глупым?"
            
        elif one_of_ten == 8:
            hide screen snape_main                                                                                                                   #SNAPE
            with d3                                                                                                                                                  #SNAPE
            $ s_sprite = "03_hp/10_snape_main/snape_05.png"                                                                            #SNAPE
            show screen snape_main                                                                                                                  #SNAPE
            with d3                                                                                                                                                   #SNAPE
            sna "У меня нет любимчиков среди моих студентов."
            hide screen snape_main                                                                                                                   #SNAPE
            with d3                                                                                                                                                  #SNAPE
            $ s_sprite = "03_hp/10_snape_main/snape_04.png"                                                                            #SNAPE
            show screen snape_main                                                                                                                  #SNAPE
            with d3                                                                                                                                                   #SNAPE
            sna "Я просто терплю некоторых и ненавижу остальных."
  
        elif one_of_ten == 9:
            hide screen snape_main                                                                                                                   #SNAPE
            with d3                                                                                                                                                  #SNAPE
            $ s_sprite = "03_hp/10_snape_main/24.png"                                                                            #SNAPE
            show screen snape_main                                                                                                                  #SNAPE
            with d3                                                                                                                                                   #SNAPE
            sna "В Хогвартсе есть четыре факультета..."
            sna "Слизерин, Когтевран, Гриффиндор и..."
            hide screen snape_main                                                                                                                   #SNAPE
            with d3                                                                                                                                                  #SNAPE
            $ s_sprite = "03_hp/10_snape_main/snape_05.png"                                                                            #SNAPE
            show screen snape_main                                                                                                                  #SNAPE
            with d3                                                                                                                                                   #SNAPE
            sna "...и Хафф-что то..."
            hide screen snape_main                                                                                                                   #SNAPE
            with d3                                                                                                                                                  #SNAPE
            $ s_sprite = "03_hp/10_snape_main/snape_29.png"                                                                            #SNAPE
            show screen snape_main                                                                                                                  #SNAPE
            with d3                                                                                                                                                   #SNAPE
            sna "Всем без разницы."
            hide screen snape_main                                                                                                                   #SNAPE
            with d3                                                                                                                                                  #SNAPE
            $ s_sprite = "03_hp/10_snape_main/snape_09.png"                                                                            #SNAPE
            show screen snape_main                                                                                                                  #SNAPE
            with d3                                                                                                                                                   #SNAPE
 
        elif one_of_ten == 10:
            hide screen snape_main                                                                                                                   #SNAPE
            with d3                                                                                                                                                  #SNAPE
            $ s_sprite = "03_hp/10_snape_main/24.png"                                                                            #SNAPE
            show screen snape_main                                                                                                                  #SNAPE
            with d3                                                                                                                                                   #SNAPE
            sna "Мётлы для детей и ведьм."
            hide screen snape_main                                                                                                                   #SNAPE
            with d3                                                                                                                                                  #SNAPE
            $ s_sprite = "03_hp/10_snape_main/snape_05.png"                                                                            #SNAPE
            show screen snape_main                                                                                                                  #SNAPE
            with d3                                                                                                                                                   #SNAPE
            sna "Ты никогда не увидишь уважающего себя колдуна летающего вокруг на метле."
            hide screen snape_main                                                                                                                   #SNAPE
            with d3                                                                                                                                                  #SNAPE
            $ s_sprite = "03_hp/10_snape_main/snape_09.png"                                                                            #SNAPE
            show screen snape_main                                                                                                                  #SNAPE
            with d3                                                                                                                                                   #SNAPE
        
        
        
        
        
        
        
        
        
    
    if whoring >= 6 and whoring <= 8: # WHORING LEVEL 03.
        if one_of_ten == 1:
            hide screen snape_main                                                                                                                   #SNAPE
            with d3                                                                                                                                                  #SNAPE
            $ s_sprite = "03_hp/10_snape_main/24.png"                                                                            #SNAPE
            show screen snape_main                                                                                                                  #SNAPE
            with d3                                                                                                                                                   #SNAPE
            sna "Есть ли прогресс по сломлению нашей мисс всезнайки?"
            hide screen snape_main                                                                                                                   #SNAPE
            with d3                                                                                                                                                  #SNAPE
            $ s_sprite = "03_hp/10_snape_main/snape_09.png"                                                            #SNAPE
            show screen snape_main                                                                                                                  #SNAPE
            with d3                                                                                                                                                   #SNAPE
        
        elif one_of_ten == 2:
            hide screen snape_main                                                                                                                   #SNAPE
            with d3                                                                                                                                                  #SNAPE
            $ s_sprite = "03_hp/10_snape_main/24.png"                                                                            #SNAPE
            show screen snape_main                                                                                                                  #SNAPE
            with d3                                                                                                                                                   #SNAPE
            sna "Однажды девченка продала мне свои трусы за пять очков факультета."
            hide screen snape_main                                                                                                                   #SNAPE
            with d3                                                                                                                                                  #SNAPE
            $ s_sprite = "03_hp/10_snape_main/snape_14.png"                                                                            #SNAPE
            show screen snape_main                                                                                                                  #SNAPE
            with d3                                                                                                                                                   #SNAPE
            sna "Самое главное, что она была очень рада этому..."
            hide screen snape_main                                                                                                                   #SNAPE
            with d3                                                                                                                                                  #SNAPE
            $ s_sprite = "03_hp/10_snape_main/snape_19.png"                                                                            #SNAPE
            show screen snape_main                                                                                                                  #SNAPE
            with d3                                                                                                                                                   #SNAPE
            sna "Я считаю, что она отдала бы их бесплатно лишь бы задобрить меня."
            hide screen snape_main                                                                                                                   #SNAPE
            with d3                                                                                                                                                  #SNAPE
            $ s_sprite = "03_hp/10_snape_main/snape_09.png"                                                                            #SNAPE
            show screen snape_main                                                                                                                  #SNAPE
            with d3                                                                                                                                                   #SNAPE

        elif one_of_ten == 3:
            hide screen snape_main                                                                                                                   #SNAPE
            with d3                                                                                                                                                  #SNAPE
            $ s_sprite = "03_hp/10_snape_main/23.png"                                                                            #SNAPE
            show screen snape_main                                                                                                                  #SNAPE
            with d3                                                                                                                                                   #SNAPE
            sna "Я думаю это очень хорошее начало дня..."
            hide screen snape_main                                                                                                                   #SNAPE
            with d3                                                                                                                                                  #SNAPE
            $ s_sprite = "03_hp/10_snape_main/snape_02.png"                                                                            #SNAPE
            show screen snape_main                                                                                                                  #SNAPE
            with d3                                                                                                                                                   #SNAPE
            sna "Спорим ты не думал что я скажу это?"

        elif one_of_ten == 4:
            hide screen snape_main                                                                                                                   #SNAPE
            with d3                                                                                                                                                  #SNAPE
            $ s_sprite = "03_hp/10_snape_main/24.png"                                                                            #SNAPE
            show screen snape_main                                                                                                                  #SNAPE
            with d3                                                                                                                                                   #SNAPE
            sna "Квиддич с годами набирает все больше популярности..."
            hide screen snape_main                                                                                                                   #SNAPE
            with d3                                                                                                                                                  #SNAPE
            $ s_sprite = "03_hp/10_snape_main/snape_04.png"                                                            #SNAPE
            show screen snape_main                                                                                                                  #SNAPE
            with d3                                                                                                                                                   #SNAPE
            sna "Как это печально..."

        elif one_of_ten == 5:
            hide screen snape_main                                                                                                                   #SNAPE
            with d3                                                                                                                                                  #SNAPE
            $ s_sprite = "03_hp/10_snape_main/24.png"                                                                            #SNAPE
            show screen snape_main                                                                                                                  #SNAPE
            with d3                                                                                                                                                   #SNAPE
            sna "Моя жизнь была скучна до твоего появления..."
            hide screen snape_main                                                                                                                   #SNAPE
            with d3                                                                                                                                                  #SNAPE
            $ s_sprite = "03_hp/10_snape_main/snape_05.png"                                                                            #SNAPE
            show screen snape_main                                                                                                                  #SNAPE
            with d3                                                                                                                                                   #SNAPE
            sna "А теперь она..."
            hide screen snape_main                                                                                                                   #SNAPE
            with d3                                                                                                                                                  #SNAPE
            $ s_sprite = "03_hp/10_snape_main/snape_02.png"                                                                            #SNAPE
            show screen snape_main                                                                                                                  #SNAPE
            with d3                                                                                                                                                   #SNAPE
            sna "...менее печальна."

        elif one_of_ten == 6:
            hide screen snape_main                                                                                                                   #SNAPE
            with d3                                                                                                                                                  #SNAPE
            $ s_sprite = "03_hp/10_snape_main/snape_05.png"                                                                            #SNAPE
            show screen snape_main                                                                                                                  #SNAPE
            with d3                                                                                                                                                   #SNAPE
            sna "Сожалеть? Я не знаю значения этого слова!"
            hide screen snape_main                                                                                                                   #SNAPE
            with d3                                                                                                                                                  #SNAPE
            $ s_sprite = "03_hp/10_snape_main/snape_06.png"                                                                            #SNAPE
            show screen snape_main                                                                                                                  #SNAPE
            with d3                                                                                                                                                   #SNAPE
            sna "Я живу очень интересной жизнью."
            hide screen snape_main                                                                                                                   #SNAPE
            with d3                                                                                                                                                  #SNAPE
            $ s_sprite = "03_hp/10_snape_main/snape_28.png"                                                                            #SNAPE
            show screen snape_main                                                                                                                  #SNAPE
            with d3                                                                                                                                                   #SNAPE
            sna "Ха-ха-ха! Извини, я просто не могу спокойно произнести это."
            hide screen snape_main                                                                                                                   #SNAPE
            with d3                                                                                                                                                  #SNAPE
            $ s_sprite = "03_hp/10_snape_main/snape_26.png"                                                                            #SNAPE
            show screen snape_main                                                                                                                  #SNAPE
            with d3                                                                                                                                                   #SNAPE

        elif one_of_ten == 7:
            hide screen snape_main                                                                                                                   #SNAPE
            with d3                                                                                                                                                  #SNAPE
            $ s_sprite = "03_hp/10_snape_main/24.png"                                                                            #SNAPE
            show screen snape_main                                                                                                                  #SNAPE
            with d3                                                                                                                                                   #SNAPE
            sna "Нет места ошибкам во время моих занятий."
            hide screen snape_main                                                                                                                   #SNAPE
            with d3                                                                                                                                                  #SNAPE
            $ s_sprite = "03_hp/10_snape_main/snape_04.png"                                                                            #SNAPE
            show screen snape_main                                                                                                                  #SNAPE
            with d3                                                                                                                                                   #SNAPE
            sna "Один промах и эти чертовы ублюдки разорвут тебя на части."

        elif one_of_ten == 8:
            hide screen snape_main                                                                                                                   #SNAPE
            with d3                                                                                                                                                  #SNAPE
            $ s_sprite = "03_hp/10_snape_main/snape_04.png"                                                                            #SNAPE
            show screen snape_main                                                                                                                  #SNAPE
            with d3                                                                                                                                                   #SNAPE
            sna "Ты единственный человек перед кем я отвечаю..."
            hide screen snape_main                                                                                                                   #SNAPE
            with d3                                                                                                                                                  #SNAPE
            $ s_sprite = "03_hp/10_snape_main/snape_05.png"                                                                            #SNAPE
            show screen snape_main                                                                                                                  #SNAPE
            with d3                                                                                                                                                   #SNAPE
            sna "Так что теперь я практически могу делать всё что угодно..."
            hide screen snape_main                                                                                                                   #SNAPE
            with d3                                                                                                                                                  #SNAPE
            $ s_sprite = "03_hp/10_snape_main/snape_09.png"                                                                            #SNAPE
            show screen snape_main                                                                                                                  #SNAPE
            with d3                                                                                                                                                   #SNAPE
            sna "..............."
            hide screen snape_main                                                                                                                   #SNAPE
            with d3                                                                                                                                                  #SNAPE
            $ s_sprite = "03_hp/10_snape_main/snape_06.png"                                                                            #SNAPE
            show screen snape_main                                                                                                                  #SNAPE
            with d3                                                                                                                                                   #SNAPE
            sna "Так вот что такое свобода, да?"

        elif one_of_ten == 9:
            hide screen snape_main                                                                                                                   #SNAPE
            with d3                                                                                                                                                  #SNAPE
            $ s_sprite = "03_hp/10_snape_main/snape_06.png"                                                                            #SNAPE
            show screen snape_main                                                                                                                  #SNAPE
            with d3                                                                                                                                                   #SNAPE
            sna "Осень... самое грустное время года..."
            hide screen snape_main                                                                                                                   #SNAPE
            with d3                                                                                                                                                  #SNAPE
            $ s_sprite = "03_hp/10_snape_main/snape_02.png"                                                                            #SNAPE
            show screen snape_main                                                                                                                  #SNAPE
            with d3                                                                                                                                                   #SNAPE
            sna "Обожаю его!"
            hide screen snape_main                                                                                                                   #SNAPE
            with d3                                                                                                                                                  #SNAPE
            $ s_sprite = "03_hp/10_snape_main/23.png"                                                                            #SNAPE
            show screen snape_main                                                                                                                  #SNAPE
            with d3                                                                                                                                                   #SNAPE

        elif one_of_ten == 10:
            hide screen snape_main                                                                                                                   #SNAPE
            with d3                                                                                                                                                  #SNAPE
            $ s_sprite = "03_hp/10_snape_main/24.png"                                                                            #SNAPE
            show screen snape_main                                                                                                                  #SNAPE
            with d3                                                                                                                                                   #SNAPE
            sna "В моей комнате висит магический портрет стриптизерши."
            hide screen snape_main                                                                                                                   #SNAPE
            with d3                                                                                                                                                  #SNAPE
            $ s_sprite = "03_hp/10_snape_main/snape_22.png"                                                                            #SNAPE
            show screen snape_main                                                                                                                  #SNAPE
            with d3                                                                                                                                                   #SNAPE
            sna "Одна из моих драгоценных вещей."
            hide screen snape_main                                                                                                                   #SNAPE
            with d3                                                                                                                                                  #SNAPE
            $ s_sprite = "03_hp/10_snape_main/snape_09.png"                                                                            #SNAPE
            show screen snape_main                                                                                                                  #SNAPE
            with d3                                                                                                                                                   #SNAPE
        
        
        
        
        
        
        
        
        
        
        
       
    if whoring >= 9 and whoring <= 11: # WHORING LEVEL 04.
        if one_of_ten == 1:
            hide screen snape_main                                                                                                                   #SNAPE
            with d3                                                                                                                                                  #SNAPE
            $ s_sprite = "03_hp/10_snape_main/24.png"                                                                            #SNAPE
            show screen snape_main                                                                                                                  #SNAPE
            with d3                                                                                                                                                   #SNAPE
            sna  "В последнее время мисс Греинджер стала очень агрессивной..."
            hide screen snape_main                                                                                                                   #SNAPE
            with d3                                                                                                                                                  #SNAPE
            $ s_sprite = "03_hp/10_snape_main/snape_05.png"                                                                            #SNAPE
            show screen snape_main                                                                                                                  #SNAPE
            with d3                                                                                                                                                   #SNAPE
            sna "Надеюсь ты знаешь, что делаешь..."
            hide screen snape_main                                                                                                                   #SNAPE
            with d3                                                                                                                                                  #SNAPE
            $ s_sprite = "03_hp/10_snape_main/snape_09.png"                                                                            #SNAPE
            show screen snape_main                                                                                                                  #SNAPE
            with d3                                                                                                                                                   #SNAPE

        elif one_of_ten == 2:
            hide screen snape_main                                                                                                                   #SNAPE
            with d3                                                                                                                                                  #SNAPE
            $ s_sprite = "03_hp/10_snape_main/snape_26.png"                                                                            #SNAPE
            show screen snape_main                                                                                                                  #SNAPE
            with d3                                                                                                                                                   #SNAPE
            sna "Меня не должна мучать совесть после секса с моими студентами, верно?"
            hide screen snape_main                                                                                                                   #SNAPE
            with d3                                                                                                                                                  #SNAPE
            $ s_sprite = "03_hp/10_snape_main/snape_05.png"                                                                            #SNAPE
            show screen snape_main                                                                                                                  #SNAPE
            with d3                                                                                                                                                   #SNAPE
            sna "Если бы ты видел какую некоторые из этих девченок носят форму..."
            hide screen snape_main                                                                                                                   #SNAPE
            with d3                                                                                                                                                  #SNAPE
            $ s_sprite = "03_hp/10_snape_main/snape_13.png"                                                                            #SNAPE
            show screen snape_main                                                                                                                  #SNAPE
            with d3                                                                                                                                                   #SNAPE
            sna "Они просто напрашиваются на это."
            hide screen snape_main                                                                                                                   #SNAPE
            with d3                                                                                                                                                  #SNAPE
            $ s_sprite = "03_hp/10_snape_main/snape_12.png"                                                                            #SNAPE
            show screen snape_main                                                                                                                  #SNAPE
            with d3                                                                                                                                                   #SNAPE

        elif one_of_ten == 3:
            hide screen snape_main                                                                                                                   #SNAPE
            with d3                                                                                                                                                  #SNAPE
            $ s_sprite = "03_hp/10_snape_main/23.png"                                                                            #SNAPE
            show screen snape_main                                                                                                                  #SNAPE
            with d3                                                                                                                                                   #SNAPE
            sna "В последнее время дождь льет чаще..."
            hide screen snape_main                                                                                                                   #SNAPE
            with d3                                                                                                                                                  #SNAPE
            $ s_sprite = "03_hp/10_snape_main/snape_02.png"                                                                            #SNAPE
            show screen snape_main                                                                                                                  #SNAPE
            with d3                                                                                                                                                   #SNAPE
            sna "Думаю мне нравится такая погода, потому что она делает других печальнее..."
            hide screen snape_main                                                                                                                   #SNAPE
            with d3                                                                                                                                                  #SNAPE
            $ s_sprite = "03_hp/10_snape_main/23.png"                                                                            #SNAPE
            show screen snape_main                                                                                                                  #SNAPE
            with d3                                                                                                                                                   #SNAPE

        elif one_of_ten == 4:
            hide screen snape_main                                                                                                                   #SNAPE
            with d3                                                                                                                                                  #SNAPE
            $ s_sprite = "03_hp/10_snape_main/24.png"                                                                            #SNAPE
            show screen snape_main                                                                                                                  #SNAPE
            with d3                                                                                                                                                   #SNAPE
            sna "Благодаря последним наблюдениям я уверен, что 9 из 10 девочек мечтают, что бы их соблазнил учитель."
            hide screen snape_main                                                                                                                   #SNAPE
            with d3                                                                                                                                                  #SNAPE
            $ s_sprite = "03_hp/10_snape_main/snape_03.png"                                                                            #SNAPE
            show screen snape_main                                                                                                                  #SNAPE
            with d3                                                                                                                                                   #SNAPE
            sna "Я так же уверен, что десятая - это Гермиона Греинджер ."
            hide screen snape_main                                                                                                                   #SNAPE
            with d3                                                                                                                                                  #SNAPE
            $ s_sprite = "03_hp/10_snape_main/snape_01.png"                                                                            #SNAPE
            show screen snape_main                                                                                                                  #SNAPE
            with d3                                                                                                                                                   #SNAPE

        elif one_of_ten == 5:
            hide screen snape_main                                                                                                                   #SNAPE
            with d3                                                                                                                                                  #SNAPE
            $ s_sprite = "03_hp/10_snape_main/24.png"                                                                            #SNAPE
            show screen snape_main                                                                                                                  #SNAPE
            with d3                                                                                                                                                   #SNAPE
            sna "В такие дни мне нужно стараться, что бы быть в плохом настроение."
            hide screen snape_main                                                                                                                   #SNAPE
            with d3                                                                                                                                                  #SNAPE
            $ s_sprite = "03_hp/10_snape_main/23.png"                                                                            #SNAPE
            show screen snape_main                                                                                                                  #SNAPE
            with d3                                                                                                                                                   #SNAPE

        elif one_of_ten == 6:
            hide screen snape_main                                                                                                                   #SNAPE
            with d3                                                                                                                                                  #SNAPE
            $ s_sprite = "03_hp/10_snape_main/24.png"                                                                            #SNAPE
            show screen snape_main                                                                                                                  #SNAPE
            with d3                                                                                                                                                   #SNAPE
            her "У тебя есть пара лишних презервативов?"
            hide screen snape_main                                                                                                                   #SNAPE
            with d3                                                                                                                                                  #SNAPE
            $ s_sprite = "03_hp/10_snape_main/snape_25.png"                                                                            #SNAPE
            show screen snape_main                                                                                                                  #SNAPE
            with d3                                                                                                                                                   #SNAPE
            her "У меня была полная пачка..."
            hide screen snape_main                                                                                                                   #SNAPE
            with d3                                                                                                                                                  #SNAPE
            $ s_sprite = "03_hp/10_snape_main/snape_06.png"                                                                            #SNAPE
            show screen snape_main                                                                                                                  #SNAPE
            with d3                                                                                                                                                   #SNAPE
            her "...они кончились год назад..."
            hide screen snape_main                                                                                                                   #SNAPE
            with d3                                                                                                                                                  #SNAPE
            $ s_sprite = "03_hp/10_snape_main/snape_02.png"                                                                            #SNAPE
            show screen snape_main                                                                                                                  #SNAPE
            with d3                                                                                                                                                   #SNAPE
            her "Мне нравится, как ты изменил мою жизнь, приятель."
            hide screen snape_main                                                                                                                   #SNAPE
            with d3                                                                                                                                                  #SNAPE
            $ s_sprite = "03_hp/10_snape_main/23.png"                                                                            #SNAPE
            show screen snape_main                                                                                                                  #SNAPE
            with d3                                                                                                                                                   #SNAPE

        elif one_of_ten == 7:
            hide screen snape_main                                                                                                                   #SNAPE
            with d3                                                                                                                                                  #SNAPE
            $ s_sprite = "03_hp/10_snape_main/24.png"                                                                            #SNAPE
            show screen snape_main                                                                                                                  #SNAPE
            with d3                                                                                                                                                   #SNAPE
            sna "Думаешь мы сможем превратить Хогвартс в школу \"только для девочек\" ?"
            hide screen snape_main                                                                                                                   #SNAPE
            with d3                                                                                                                                                  #SNAPE
            $ s_sprite = "03_hp/10_snape_main/23.png"                                                                            #SNAPE
            show screen snape_main                                                                                                                  #SNAPE
            with d3                                                                                                                                                   #SNAPE
            sna "Академия девочек Хогвартс!"
            hide screen snape_main                                                                                                                   #SNAPE
            with d3                                                                                                                                                  #SNAPE
            $ s_sprite = "03_hp/10_snape_main/snape_13.png"                                                                            #SNAPE
            show screen snape_main                                                                                                                  #SNAPE
            with d3                                                                                                                                                   #SNAPE
            sna "Это было бы идеально... не считая Локхарта."

        elif one_of_ten == 8:
            hide screen snape_main                                                                                                                   #SNAPE
            with d3                                                                                                                                                  #SNAPE
            $ s_sprite = "03_hp/10_snape_main/24.png"                                                                            #SNAPE
            show screen snape_main                                                                                                                  #SNAPE
            with d3                                                                                                                                                   #SNAPE
            sna "Почему учитель перешел дорогу?"
            hide screen snape_main                                                                                                                   #SNAPE
            with d3                                                                                                                                                  #SNAPE
            $ s_sprite = "03_hp/10_snape_main/snape_25.png"                                                                            #SNAPE
            show screen snape_main                                                                                                                  #SNAPE
            with d3                                                                                                                                                   #SNAPE
            sna "Что бы сбежать от студентов!"
            hide screen snape_main                                                                                                                   #SNAPE
            with d3                                                                                                                                                  #SNAPE
            $ s_sprite = "03_hp/10_snape_main/snape_28.png"                                                                            #SNAPE
            show screen snape_main                                                                                                                  #SNAPE
            with d3                                                                                                                                                   #SNAPE
            sna "Ха-ха-ха! Шутка на все времена!"
            hide screen snape_main                                                                                                                   #SNAPE
            with d3                                                                                                                                                  #SNAPE
            $ s_sprite = "03_hp/10_snape_main/snape_25.png"                                                                            #SNAPE
            show screen snape_main                                                                                                                  #SNAPE
            with d3                                                                                                                                                   #SNAPE

        elif one_of_ten == 9:
            hide screen snape_main                                                                                                                   #SNAPE
            with d3                                                                                                                                                  #SNAPE
            $ s_sprite = "03_hp/10_snape_main/24.png"                                                                            #SNAPE
            show screen snape_main                                                                                                                  #SNAPE
            with d3                                                                                                                                                   #SNAPE
            sna "Хочешь услышать забавную историю?"
            hide screen snape_main                                                                                                                   #SNAPE
            with d3                                                                                                                                                  #SNAPE
            $ s_sprite = "03_hp/10_snape_main/snape_06.png"                                                                            #SNAPE
            show screen snape_main                                                                                                                  #SNAPE
            with d3                                                                                                                                                   #SNAPE
            sna "Ну, я не знаю таких..."

        elif one_of_ten == 10:
            hide screen snape_main                                                                                                                   #SNAPE
            with d3                                                                                                                                                  #SNAPE
            $ s_sprite = "03_hp/10_snape_main/snape_05.png"                                                                            #SNAPE
            show screen snape_main                                                                                                                  #SNAPE
            with d3                                                                                                                                                   #SNAPE
            sna "Ты знаешь что такое \"Королевский Кубок\" ?"
            hide screen snape_main                                                                                                                   #SNAPE
            with d3                                                                                                                                                  #SNAPE
            $ s_sprite = "03_hp/10_snape_main/snape_13.png"                                                                            #SNAPE
            show screen snape_main                                                                                                                  #SNAPE
            with d3                                                                                                                                                   #SNAPE
            sna "Ты знаешь, верно?"
            hide screen snape_main                                                                                                                   #SNAPE
            with d3                                                                                                                                                  #SNAPE
            $ s_sprite = "03_hp/10_snape_main/23.png"                                                                            #SNAPE
            show screen snape_main                                                                                                                  #SNAPE
            with d3                                                                                                                                                   #SNAPE
        
        
        
        
        
        
        
        
        
    
    if whoring >= 12 and whoring <= 14: # WHORING LEVEL 05.
        if one_of_ten == 1:
            hide screen snape_main                                                                                                                   #SNAPE
            with d3                                                                                                                                                  #SNAPE
            $ s_sprite = "03_hp/10_snape_main/24.png"                                                                            #SNAPE
            show screen snape_main                                                                                                                  #SNAPE
            with d3                                                                                                                                                   #SNAPE
            sna "15 очков за работу ртом справедливо, верно?"
            hide screen snape_main                                                                                                                   #SNAPE
            with d3                                                                                                                                                  #SNAPE
            $ s_sprite = "03_hp/10_snape_main/23.png"                                                                            #SNAPE
            show screen snape_main                                                                                                                  #SNAPE
            with d3                                                                                                                                                   #SNAPE

        elif one_of_ten == 2:
            hide screen snape_main                                                                                                                   #SNAPE
            with d3                                                                                                                                                  #SNAPE
            $ s_sprite = "03_hp/10_snape_main/24.png"                                                                            #SNAPE
            show screen snape_main                                                                                                                  #SNAPE
            with d3                                                                                                                                                   #SNAPE
            sna "Ты был когда нибудь влюблен, приятель?"
            hide screen snape_main                                                                                                                   #SNAPE
            with d3                                                                                                                                                  #SNAPE
            $ s_sprite = "03_hp/10_snape_main/snape_02.png"                                                                            #SNAPE
            show screen snape_main                                                                                                                  #SNAPE
            with d3                                                                                                                                                   #SNAPE
            sna "Ты был когда нибудь влюблен в школьницу?"
            hide screen snape_main                                                                                                                   #SNAPE
            with d3                                                                                                                                                  #SNAPE
            $ s_sprite = "03_hp/10_snape_main/snape_22.png"                                                                            #SNAPE
            show screen snape_main                                                                                                                  #SNAPE
            with d3                                                                                                                                                   #SNAPE
            sna "А как на счет сразу нескольких?"
            hide screen snape_main                                                                                                                   #SNAPE
            with d3                                                                                                                                                  #SNAPE
            $ s_sprite = "03_hp/10_snape_main/snape_20.png"                                                                            #SNAPE
            show screen snape_main                                                                                                                  #SNAPE
            with d3                                                                                                                                                   #SNAPE

        elif one_of_ten == 3:
            hide screen snape_main                                                                                                                   #SNAPE
            with d3                                                                                                                                                  #SNAPE
            $ s_sprite = "03_hp/10_snape_main/snape_20.png"                                                                            #SNAPE
            show screen snape_main                                                                                                                  #SNAPE
            with d3                                                                                                                                                   #SNAPE
            sna "Прошлой ночью между мной и одной из Слизеринских шлюх произошло что-то невероятное."
            hide screen snape_main                                                                                                                   #SNAPE
            with d3                                                                                                                                                  #SNAPE
            $ s_sprite = "03_hp/10_snape_main/snape_22.png"                                                                            #SNAPE
            show screen snape_main                                                                                                                  #SNAPE
            with d3                                                                                                                                                   #SNAPE
            sna "Вкратце, все мои мышцы болят и я чуствую себя опусташенным..."
            hide screen snape_main                                                                                                                   #SNAPE
            with d3                                                                                                                                                  #SNAPE
            $ s_sprite = "03_hp/10_snape_main/snape_13.png"                                                                            #SNAPE
            show screen snape_main                                                                                                                  #SNAPE
            with d3                                                                                                                                                   #SNAPE

        elif one_of_ten == 4:
            hide screen snape_main                                                                                                                   #SNAPE
            with d3                                                                                                                                                  #SNAPE
            $ s_sprite = "03_hp/10_snape_main/24.png"                                                                            #SNAPE
            show screen snape_main                                                                                                                  #SNAPE
            with d3                                                                                                                                                   #SNAPE
            sna "В последнее время становится холоднее..."
            hide screen snape_main                                                                                                                   #SNAPE
            with d3                                                                                                                                                  #SNAPE
            $ s_sprite = "03_hp/10_snape_main/23.png"                                                                            #SNAPE
            show screen snape_main                                                                                                                  #SNAPE
            with d3                                                                                                                                                   #SNAPE
            sna "Зима близко..."
         
        elif one_of_ten == 5:
            hide screen snape_main                                                                                                                   #SNAPE
            with d3                                                                                                                                                  #SNAPE
            $ s_sprite = "03_hp/10_snape_main/24.png"                                                                            #SNAPE
            show screen snape_main                                                                                                                  #SNAPE
            with d3                                                                                                                                                   #SNAPE
            sna "Ты когда нибудь видел как магловские женщины одеваются в ведьм?"
            hide screen snape_main                                                                                                                   #SNAPE
            with d3                                                                                                                                                  #SNAPE
            $ s_sprite = "03_hp/10_snape_main/snape_19.png"                                                                            #SNAPE
            show screen snape_main                                                                                                                  #SNAPE
            with d3                                                                                                                                                   #SNAPE
            sna "Так восхитительно."

        elif one_of_ten == 6:
            hide screen snape_main                                                                                                                   #SNAPE
            with d3                                                                                                                                                  #SNAPE
            $ s_sprite = "03_hp/10_snape_main/24.png"                                                                            #SNAPE
            show screen snape_main                                                                                                                  #SNAPE
            with d3                                                                                                                                                   #SNAPE
            sna "Ты знаешь что такое \"Интернет\" ?"
            hide screen snape_main                                                                                                                   #SNAPE
            with d3                                                                                                                                                  #SNAPE
            $ s_sprite = "03_hp/10_snape_main/snape_02.png"                                                                            #SNAPE
            show screen snape_main                                                                                                                  #SNAPE
            with d3                                                                                                                                                   #SNAPE
            sna "Он позволяет тебе \" быть внутри сети \" и смотреть магические фотографии голых женщин маглов." # SNAPE SAYS "ON THE LINE" ON PURPOSE. I KNOW THAT WAS REALLY OBVIOUS MAESTRO
            hide screen snape_main                                                                                                                   #SNAPE
            with d3                                                                                                                                                  #SNAPE
            $ s_sprite = "03_hp/10_snape_main/snape_26.png"                                                                            #SNAPE
            show screen snape_main                                                                                                                  #SNAPE
            with d3                                                                                                                                                   #SNAPE
            sna "Жаль, что у нас нет этого в Хогвартсе."
            hide screen snape_main                                                                                                                   #SNAPE
            with d3                                                                                                                                                  #SNAPE
            $ s_sprite = "03_hp/10_snape_main/snape_09.png"                                                                            #SNAPE
            show screen snape_main                                                                                                                  #SNAPE
            with d3                                                                                                                                                   #SNAPE

        elif one_of_ten == 7:
            hide screen snape_main                                                                                                                   #SNAPE
            with d3                                                                                                                                                  #SNAPE
            $ s_sprite = "03_hp/10_snape_main/24.png"                                                                            #SNAPE
            show screen snape_main                                                                                                                  #SNAPE
            with d3                                                                                                                                                   #SNAPE
            sna "В моей жизни есть два влечения..."
            sna "Темные искуства..."
            hide screen snape_main                                                                                                                   #SNAPE
            with d3                                                                                                                                                  #SNAPE
            $ s_sprite = "03_hp/10_snape_main/snape_12.png"                                                                            #SNAPE
            show screen snape_main                                                                                                                  #SNAPE
            with d3                                                                                                                                                   #SNAPE
            sna "......"
            hide screen snape_main                                                                                                                   #SNAPE
            with d3                                                                                                                                                  #SNAPE
            $ s_sprite = "03_hp/10_snape_main/snape_13.png"                                                                            #SNAPE
            show screen snape_main                                                                                                                  #SNAPE
            with d3                                                                                                                                                   #SNAPE
            sna "...и шлюхи."

        elif one_of_ten == 8:
            hide screen snape_main                                                                                                                   #SNAPE
            with d3                                                                                                                                                  #SNAPE
            $ s_sprite = "03_hp/10_snape_main/24.png"                                                                            #SNAPE
            show screen snape_main                                                                                                                  #SNAPE
            with d3                                                                                                                                                   #SNAPE
            sna "Ты думаешь я не смогу отказаться от выпивки?"
            hide screen snape_main                                                                                                                   #SNAPE
            with d3                                                                                                                                                  #SNAPE
            $ s_sprite = "03_hp/10_snape_main/snape_06.png"                                                                            #SNAPE
            show screen snape_main                                                                                                                  #SNAPE
            with d3                                                                                                                                                   #SNAPE
            sna "Ведь моя жизнь наполнена стресом..."
            hide screen snape_main                                                                                                                   #SNAPE
            with d3                                                                                                                                                  #SNAPE
            $ s_sprite = "03_hp/10_snape_main/snape_09.png"                                                                            #SNAPE
            show screen snape_main                                                                                                                  #SNAPE
            with d3                                                                                                                                                   #SNAPE
            sna "Хм..."
            hide screen snape_main                                                                                                                   #SNAPE
            with d3                                                                                                                                                  #SNAPE
            $ s_sprite = "03_hp/10_snape_main/snape_06.png"                                                                            #SNAPE
            show screen snape_main                                                                                                                  #SNAPE
            with d3                                                                                                                                                   #SNAPE
            sna "Я могу попробовать отказаться от нее..."
            hide screen snape_main                                                                                                                   #SNAPE
            with d3                                                                                                                                                  #SNAPE
            $ s_sprite = "03_hp/10_snape_main/snape_21.png"                                                                            #SNAPE
            show screen snape_main                                                                                                                  #SNAPE
            with d3                                                                                                                                                   #SNAPE
            sna "В замен на дикий секс с моими студентами!"
            hide screen snape_main                                                                                                                   #SNAPE
            with d3                                                                                                                                                  #SNAPE
            $ s_sprite = "03_hp/10_snape_main/snape_19.png"                                                                            #SNAPE
            show screen snape_main                                                                                                                  #SNAPE
            with d3                                                                                                                                                   #SNAPE

        elif one_of_ten == 9:
            hide screen snape_main                                                                                                                   #SNAPE
            with d3                                                                                                                                                  #SNAPE
            $ s_sprite = "03_hp/10_snape_main/24.png"                                                                            #SNAPE
            show screen snape_main                                                                                                                  #SNAPE
            with d3                                                                                                                                                   #SNAPE
            sna "Мисс Греинджер в последнее время притихла..."
            hide screen snape_main                                                                                                                   #SNAPE
            with d3                                                                                                                                                  #SNAPE
            $ s_sprite = "03_hp/10_snape_main/snape_03.png"                                                                            #SNAPE
            show screen snape_main                                                                                                                  #SNAPE
            with d3                                                                                                                                                   #SNAPE
            sna "Я уверен она замышляет что-то..."
            hide screen snape_main                                                                                                                   #SNAPE
            with d3                                                                                                                                                  #SNAPE
            $ s_sprite = "03_hp/10_snape_main/snape_01.png"                                                                            #SNAPE
            show screen snape_main                                                                                                                  #SNAPE
            with d3                                                                                                                                                   #SNAPE

        elif one_of_ten == 10:
            hide screen snape_main                                                                                                                   #SNAPE
            with d3                                                                                                                                                  #SNAPE
            $ s_sprite = "03_hp/10_snape_main/24.png"                                                                            #SNAPE
            show screen snape_main                                                                                                                  #SNAPE
            with d3                                                                                                                                                   #SNAPE
            sna "Написать книгу и убить почти всех персонажей ради драматической сцены очень легко..."
            sna "Но поставить своих персонажей в не выгодное положение и помочь им выжить звучит убедительнее..."
            hide screen snape_main                                                                                                                   #SNAPE
            with d3                                                                                                                                                  #SNAPE
            $ s_sprite = "03_hp/10_snape_main/snape_02.png"                                                                            #SNAPE
            show screen snape_main                                                                                                                  #SNAPE
            with d3                                                                                                                                                   #SNAPE
            sna "Сейчас {size=+7}это{/size} требует навыка."
            hide screen snape_main                                                                                                                   #SNAPE
            with d3                                                                                                                                                  #SNAPE
            $ s_sprite = "03_hp/10_snape_main/23.png"                                                                            #SNAPE
            show screen snape_main                                                                                                                  #SNAPE
            with d3                                                                                                                                                   #SNAPE
        
        
        
        
        
        
        
        
        

    if whoring >= 15 and whoring <= 17: # WHORING LEVEL 06.
        if one_of_ten == 1:
            hide screen snape_main                                                                                                                   #SNAPE
            with d3                                                                                                                                                  #SNAPE
            $ s_sprite = "03_hp/10_snape_main/snape_11.png"                                                                            #SNAPE
            show screen snape_main                                                                                                                  #SNAPE
            with d3                                                                                                                                                   #SNAPE
            sna "А что если не мы играемся с девченкой, а она с нами?"
            hide screen snape_main                                                                                                                   #SNAPE
            with d3                                                                                                                                                  #SNAPE
            $ s_sprite = "03_hp/10_snape_main/snape_26.png"                                                                            #SNAPE
            show screen snape_main                                                                                                                  #SNAPE
            with d3                                                                                                                                                   #SNAPE

        elif one_of_ten == 2:
            hide screen snape_main                                                                                                                   #SNAPE
            with d3                                                                                                                                                  #SNAPE
            $ s_sprite = "03_hp/10_snape_main/24.png"                                                                            #SNAPE
            show screen snape_main                                                                                                                  #SNAPE
            with d3                                                                                                                                                   #SNAPE
            sna "Слышал ли ты о \"Слизневом клубе\"?"
            sna "Что если я сам сделаю клуб?"
            hide screen snape_main                                                                                                                   #SNAPE
            with d3                                                                                                                                                  #SNAPE
            $ s_sprite = "03_hp/10_snape_main/23.png"                                                                            #SNAPE
            show screen snape_main                                                                                                                  #SNAPE
            with d3                                                                                                                                                   #SNAPE
            sna "Я назову его \"Клуб Снейпа\"!"
            sna "Я бы пригласил туда девченок, предложил бы им чай и кексики..."
            hide screen snape_main                                                                                                                   #SNAPE
            with d3                                                                                                                                                  #SNAPE
            $ s_sprite = "03_hp/10_snape_main/snape_13.png"                                                                            #SNAPE
            show screen snape_main                                                                                                                  #SNAPE
            with d3                                                                                                                                                   #SNAPE
            sna "Разболтал бы их немного..."
            hide screen snape_main                                                                                                                   #SNAPE
            with d3                                                                                                                                                  #SNAPE
            $ s_sprite = "03_hp/10_snape_main/snape_22.png"                                                                            #SNAPE
            show screen snape_main                                                                                                                  #SNAPE
            with d3                                                                                                                                                   #SNAPE
            sna "Гениально!"
            hide screen snape_main                                                                                                                   #SNAPE
            with d3                                                                                                                                                  #SNAPE
            $ s_sprite = "03_hp/10_snape_main/snape_02.png"                                                                            #SNAPE
            show screen snape_main                                                                                                                  #SNAPE
            with d3                                                                                                                                                   #SNAPE

        elif one_of_ten == 3:
            hide screen snape_main                                                                                                                   #SNAPE
            with d3                                                                                                                                                  #SNAPE
            $ s_sprite = "03_hp/10_snape_main/snape_02.png"                                                                            #SNAPE
            show screen snape_main                                                                                                                  #SNAPE
            with d3                                                                                                                                                   #SNAPE
            sna "Скажи мне Джинни... тебе когда нибудь вылизывала зад молодая ведьмочка?"
            hide screen snape_main                                                                                                                   #SNAPE
            with d3                                                                                                                                                  #SNAPE
            $ s_sprite = "03_hp/10_snape_main/snape_21.png"                                                                            #SNAPE
            show screen snape_main                                                                                                                  #SNAPE
            with d3                                                                                                                                                   #SNAPE
            sna "Незабываемые ощущения, не больше, не меньше..."
            hide screen snape_main                                                                                                                   #SNAPE
            with d3                                                                                                                                                  #SNAPE
            $ s_sprite = "03_hp/10_snape_main/snape_02.png"                                                                            #SNAPE
            show screen snape_main                                                                                                                  #SNAPE
            with d3                                                                                                                                                   #SNAPE

        elif one_of_ten == 4:
            hide screen snape_main                                                                                                                   #SNAPE
            with d3                                                                                                                                                  #SNAPE
            $ s_sprite = "03_hp/10_snape_main/24.png"                                                                            #SNAPE
            show screen snape_main                                                                                                                  #SNAPE
            with d3                                                                                                                                                   #SNAPE
            sna "Итак, как продвигается обучение?"
            sna "Все по плану надеюсь?"
            hide screen snape_main                                                                                                                   #SNAPE
            with d3                                                                                                                                                  #SNAPE
            $ s_sprite = "03_hp/10_snape_main/snape_05.png"                                                                            #SNAPE
            show screen snape_main                                                                                                                  #SNAPE
            with d3                                                                                                                                                   #SNAPE

        elif one_of_ten == 5:
            hide screen snape_main                                                                                                                   #SNAPE
            with d3                                                                                                                                                  #SNAPE
            $ s_sprite = "03_hp/10_snape_main/snape_06.png"                                                                            #SNAPE
            show screen snape_main                                                                                                                  #SNAPE
            with d3                                                                                                                                                   #SNAPE
            sna "Ты знаешь... Я вижу Фестралов."
            hide screen snape_main                                                                                                                   #SNAPE
            with d3                                                                                                                                                  #SNAPE
            $ s_sprite = "03_hp/10_snape_main/snape_09.png"                                                                            #SNAPE
            show screen snape_main                                                                                                                  #SNAPE
            with d3                                                                                                                                                   #SNAPE

        elif one_of_ten == 6:
            hide screen snape_main                                                                                                                   #SNAPE
            with d3                                                                                                                                                  #SNAPE
            $ s_sprite = "03_hp/10_snape_main/24.png"                                                                            #SNAPE
            show screen snape_main                                                                                                                  #SNAPE
            with d3                                                                                                                                                   #SNAPE
            sna "Ты знаешь что я люблю в Квиддиче?"
            hide screen snape_main                                                                                                                   #SNAPE
            with d3                                                                                                                                                  #SNAPE
            $ s_sprite = "03_hp/10_snape_main/snape_15.png"                                                                            #SNAPE
            show screen snape_main                                                                                                                  #SNAPE
            with d3                                                                                                                                                   #SNAPE
            sna "Ничего! Абсолютно ничего!"
            hide screen snape_main                                                                                                                   #SNAPE
            with d3                                                                                                                                                  #SNAPE
            $ s_sprite = "03_hp/10_snape_main/snape_16.png"                                                                            #SNAPE
            show screen snape_main                                                                                                                  #SNAPE
            with d3                                                                                                                                                   #SNAPE

        elif one_of_ten == 7:
            hide screen snape_main                                                                                                                   #SNAPE
            with d3                                                                                                                                                  #SNAPE
            $ s_sprite = "03_hp/10_snape_main/24.png"                                                                            #SNAPE
            show screen snape_main                                                                                                                  #SNAPE
            with d3                                                                                                                                                   #SNAPE
            sna "Хогвартс сильно вознесся с твоим приходом."
            hide screen snape_main                                                                                                                   #SNAPE
            with d3                                                                                                                                                  #SNAPE
            $ s_sprite = "03_hp/10_snape_main/snape_02.png"                                                                            #SNAPE
            show screen snape_main                                                                                                                  #SNAPE
            with d3                                                                                                                                                   #SNAPE
            sna "И когда я говорю \"Хогвартс\" я имею в виду \"Себя\"."
            hide screen snape_main                                                                                                                   #SNAPE
            with d3                                                                                                                                                  #SNAPE
            $ s_sprite = "03_hp/10_snape_main/23.png"                                                                            #SNAPE
            show screen snape_main                                                                                                                  #SNAPE
            with d3                                                                                                                                                   #SNAPE

        elif one_of_ten == 8:
            hide screen snape_main                                                                                                                   #SNAPE
            with d3                                                                                                                                                  #SNAPE
            $ s_sprite = "03_hp/10_snape_main/24.png"                                                                            #SNAPE
            show screen snape_main                                                                                                                  #SNAPE
            with d3                                                                                                                                                   #SNAPE
            sna "Настоящие волшебники носят черное."
            hide screen snape_main                                                                                                                   #SNAPE
            with d3                                                                                                                                                  #SNAPE
            $ s_sprite = "03_hp/10_snape_main/snape_02.png"                                                                            #SNAPE
            show screen snape_main                                                                                                                  #SNAPE
            with d3                                                                                                                                                   #SNAPE
            sna "Ведь так?"
            hide screen snape_main                                                                                                                   #SNAPE
            with d3                                                                                                                                                  #SNAPE
            $ s_sprite = "03_hp/10_snape_main/23.png"                                                                            #SNAPE
            show screen snape_main                                                                                                                  #SNAPE
            with d3                                                                                                                                                   #SNAPE

        elif one_of_ten == 9:
            hide screen snape_main                                                                                                                   #SNAPE
            with d3                                                                                                                                                  #SNAPE
            $ s_sprite = "03_hp/10_snape_main/24.png"                                                                            #SNAPE
            show screen snape_main                                                                                                                  #SNAPE
            with d3                                                                                                                                                   #SNAPE
            sna "Некоторые девочки Слизерина восхищаются мной..."
            hide screen snape_main                                                                                                                   #SNAPE
            with d3                                                                                                                                                  #SNAPE
            $ s_sprite = "03_hp/10_snape_main/snape_05.png"                                                                            #SNAPE
            show screen snape_main                                                                                                                  #SNAPE
            with d3                                                                                                                                                   #SNAPE
            sna "Я бы предпочел что бы меня боялись..."
            hide screen snape_main                                                                                                                   #SNAPE
            with d3                                                                                                                                                  #SNAPE
            $ s_sprite = "03_hp/10_snape_main/23.png"                                                                            #SNAPE
            show screen snape_main                                                                                                                  #SNAPE
            with d3                                                                                                                                                   #SNAPE
            sna "Но я думаю что всё в порядке..."

        elif one_of_ten == 10:
            hide screen snape_main                                                                                                                   #SNAPE
            with d3                                                                                                                                                  #SNAPE
            $ s_sprite = "03_hp/10_snape_main/24.png"                                                                            #SNAPE
            show screen snape_main                                                                                                                  #SNAPE
            with d3                                                                                                                                                   #SNAPE
            sna "В последнее время ты слишком щедр с очками Гриффиндора, приятель."
            hide screen snape_main                                                                                                                   #SNAPE
            with d3                                                                                                                                                  #SNAPE
            $ s_sprite = "03_hp/10_snape_main/snape_25.png"                                                                            #SNAPE
            show screen snape_main                                                                                                                  #SNAPE
            with d3                                                                                                                                                   #SNAPE
            sna "Я почти не успеваю за тобой..."
            hide screen snape_main                                                                                                                   #SNAPE
            with d3                                                                                                                                                  #SNAPE
            $ s_sprite = "03_hp/10_snape_main/snape_29.png"                                                                            #SNAPE
            show screen snape_main                                                                                                                  #SNAPE
            with d3                                                                                                                                                   #SNAPE
        
        
        
        
   
        
    if whoring >= 18 and whoring <= 20: # WHORING LEVEL 07.
        if one_of_ten == 1:
            hide screen snape_main                                                                                                                   #SNAPE
            with d3                                                                                                                                                  #SNAPE
            $ s_sprite = "03_hp/10_snape_main/24.png"                                                                            #SNAPE
            show screen snape_main                                                                                                                  #SNAPE
            with d3                                                                                                                                                   #SNAPE
            sna "Мисс Греинджер меняется. И это становится заметно..."
            sna "Ее оценки идут вниз и даже поведенее стало далеко от идеала..."
            hide screen snape_main                                                                                                                   #SNAPE
            with d3                                                                                                                                                  #SNAPE
            $ s_sprite = "03_hp/10_snape_main/snape_10.png"                                                                            #SNAPE
            show screen snape_main                                                                                                                  #SNAPE
            with d3                                                                                                                                                   #SNAPE
            sna "Но не смотря на это, она все еще заноза в моей заднице!"
            hide screen snape_main                                                                                                                   #SNAPE
            with d3                                                                                                                                                  #SNAPE
            $ s_sprite = "03_hp/10_snape_main/snape_01.png"                                                                            #SNAPE
            show screen snape_main                                                                                                                  #SNAPE
            with d3                                                                                                                                                   #SNAPE

        elif one_of_ten == 2:
            hide screen snape_main                                                                                                                   #SNAPE
            with d3                                                                                                                                                  #SNAPE
            $ s_sprite = "03_hp/10_snape_main/snape_05.png"                                                                            #SNAPE
            show screen snape_main                                                                                                                  #SNAPE
            with d3                                                                                                                                                   #SNAPE
            sna "Мой самый не любимый цвет?"
            hide screen snape_main                                                                                                                   #SNAPE
            with d3                                                                                                                                                  #SNAPE
            $ s_sprite = "03_hp/10_snape_main/snape_07.png"                                                                            #SNAPE
            show screen snape_main                                                                                                                  #SNAPE
            with d3                                                                                                                                                   #SNAPE
            sna "Их два. Красный и золотой."
            hide screen snape_main                                                                                                                   #SNAPE
            with d3                                                                                                                                                  #SNAPE
            $ s_sprite = "03_hp/10_snape_main/snape_04.png"                                                                            #SNAPE
            show screen snape_main                                                                                                                  #SNAPE
            with d3                                                                                                                                                   #SNAPE

        elif one_of_ten == 3:
            hide screen snape_main                                                                                                                   #SNAPE
            with d3                                                                                                                                                  #SNAPE
            $ s_sprite = "03_hp/10_snape_main/24.png"                                                                            #SNAPE
            show screen snape_main                                                                                                                  #SNAPE
            with d3                                                                                                                                                   #SNAPE
            sna "Я слышал что тема вампиров популярна среди девочек."
            hide screen snape_main                                                                                                                   #SNAPE
            with d3                                                                                                                                                  #SNAPE
            $ s_sprite = "03_hp/10_snape_main/snape_05.png"                                                                            #SNAPE
            show screen snape_main                                                                                                                  #SNAPE
            with d3                                                                                                                                                   #SNAPE
            sna "Из меня бы получился отличный вампир?"
            sna "Может я куплю пару фальшивых клыков..."
            hide screen snape_main                                                                                                                   #SNAPE
            with d3                                                                                                                                                  #SNAPE
            $ s_sprite = "03_hp/10_snape_main/snape_21.png"                                                                            #SNAPE
            show screen snape_main                                                                                                                  #SNAPE
            with d3                                                                                                                                                   #SNAPE
            sna "Просто, что бы завести этих сумасшедших шлюх."
            hide screen snape_main                                                                                                                   #SNAPE
            with d3                                                                                                                                                  #SNAPE
            $ s_sprite = "03_hp/10_snape_main/snape_02.png"                                                                            #SNAPE
            show screen snape_main                                                                                                                  #SNAPE
            with d3                                                                                                                                                   #SNAPE

        elif one_of_ten == 4:
            hide screen snape_main                                                                                                                   #SNAPE
            with d3                                                                                                                                                  #SNAPE
            $ s_sprite = "03_hp/10_snape_main/24.png"                                                                            #SNAPE
            show screen snape_main                                                                                                                  #SNAPE
            with d3                                                                                                                                                   #SNAPE
            sna "Я ...ненавижу свою жизнь."
            hide screen snape_main                                                                                                                   #SNAPE
            with d3                                                                                                                                                  #SNAPE
            $ s_sprite = "03_hp/10_snape_main/snape_16.png"                                                                            #SNAPE
            show screen snape_main                                                                                                                  #SNAPE
            with d3                                                                                                                                                   #SNAPE
            sna "Нет, постой, перефразирую..."
            hide screen snape_main                                                                                                                   #SNAPE
            with d3                                                                                                                                                  #SNAPE
            $ s_sprite = "03_hp/10_snape_main/snape_17.png"                                                                            #SNAPE
            show screen snape_main                                                                                                                  #SNAPE
            with d3                                                                                                                                                   #SNAPE
            sna "Я ...ненавижу свою жизнь."
            hide screen snape_main                                                                                                                   #SNAPE
            with d3                                                                                                                                                  #SNAPE
            $ s_sprite = "03_hp/10_snape_main/snape_25.png"                                                                            #SNAPE
            show screen snape_main                                                                                                                  #SNAPE
            with d3                                                                                                                                                   #SNAPE
            sna "Блин! Я пытаюсь сказать \"люблю\" но у меня не получается..."
            hide screen snape_main                                                                                                                   #SNAPE
            with d3                                                                                                                                                  #SNAPE
            $ s_sprite = "03_hp/10_snape_main/snape_29.png"                                                                            #SNAPE
            show screen snape_main                                                                                                                  #SNAPE
            with d3                                                                                                                                                   #SNAPE
            sna "Я не думаю, что я когда либо использовал слова \"Люблю\" и \"Жизнь\" в одном предложение."
            hide screen snape_main                                                                                                                   #SNAPE
            with d3                                                                                                                                                  #SNAPE
            $ s_sprite = "03_hp/10_snape_main/snape_06.png"                                                                            #SNAPE
            show screen snape_main                                                                                                                  #SNAPE
            with d3                                                                                                                                                   #SNAPE
            sna "Попробую снова..."
            hide screen snape_main                                                                                                                   #SNAPE
            with d3                                                                                                                                                  #SNAPE
            $ s_sprite = "03_hp/10_snape_main/snape_10.png"                                                                            #SNAPE
            show screen snape_main                                                                                                                  #SNAPE
            with d3                                                                                                                                                   #SNAPE
            sna "Я не... лю... люблю свою жизнь!"
            hide screen snape_main                                                                                                                   #SNAPE
            with d3                                                                                                                                                  #SNAPE
            $ s_sprite = "03_hp/10_snape_main/23.png"                                                                            #SNAPE
            show screen snape_main                                                                                                                  #SNAPE
            with d3                                                                                                                                                   #SNAPE
            sna "Отлично, я люблю свою жизнь..."

        elif one_of_ten == 5:
            hide screen snape_main                                                                                                                   #SNAPE
            with d3                                                                                                                                                  #SNAPE
            $ s_sprite = "03_hp/10_snape_main/snape_01.png"                                                                            #SNAPE
            show screen snape_main                                                                                                                  #SNAPE
            with d3                                                                                                                                                   #SNAPE
            sna "Солнце, шоколад, квиддич, кошки и апельсиновый сок..."
            sna "Это список вещей которые я не люблю..."
            hide screen snape_main                                                                                                                   #SNAPE
            with d3                                                                                                                                                  #SNAPE
            $ s_sprite = "03_hp/10_snape_main/snape_02.png"                                                                            #SNAPE
            show screen snape_main                                                                                                                  #SNAPE
            with d3                                                                                                                                                   #SNAPE
            sna "А теперь короткий список того что люблю..."
            hide screen snape_main                                                                                                                   #SNAPE
            with d3                                                                                                                                                  #SNAPE
            $ s_sprite = "03_hp/10_snape_main/23.png"                                                                            #SNAPE
            show screen snape_main                                                                                                                  #SNAPE
            with d3                                                                                                                                                   #SNAPE
            sna "Темные искуства, вино и девочки."

        elif one_of_ten == 6:
            hide screen snape_main                                                                                                                   #SNAPE
            with d3                                                                                                                                                  #SNAPE
            $ s_sprite = "03_hp/10_snape_main/snape_02.png"                                                                            #SNAPE
            show screen snape_main                                                                                                                  #SNAPE
            with d3                                                                                                                                                   #SNAPE
            sna "Ты видел колдунов в кулачной драке?"
            hide screen snape_main                                                                                                                   #SNAPE
            with d3                                                                                                                                                  #SNAPE
            $ s_sprite = "03_hp/10_snape_main/snape_28.png"                                                                            #SNAPE
            show screen snape_main                                                                                                                  #SNAPE
            with d3                                                                                                                                                   #SNAPE
            sna "Просто отвратительно!"
            hide screen snape_main                                                                                                                   #SNAPE
            with d3                                                                                                                                                  #SNAPE
            $ s_sprite = "03_hp/10_snape_main/23.png"                                                                            #SNAPE
            show screen snape_main                                                                                                                  #SNAPE
            with d3                                                                                                                                                   #SNAPE

        elif one_of_ten == 7:
            hide screen snape_main                                                                                                                   #SNAPE
            with d3                                                                                                                                                  #SNAPE
            $ s_sprite = "03_hp/10_snape_main/snape_14.png"                                                                            #SNAPE
            show screen snape_main                                                                                                                  #SNAPE
            with d3                                                                                                                                                   #SNAPE
            sna "То чуство, когда ты кончил девушке в рот, а она произносит: \"Спасибо, профессор\"."
            hide screen snape_main                                                                                                                   #SNAPE
            with d3                                                                                                                                                  #SNAPE
            $ s_sprite = "03_hp/10_snape_main/snape_13.png"                                                                            #SNAPE
            show screen snape_main                                                                                                                  #SNAPE
            with d3                                                                                                                                                   #SNAPE
            sna "Оно великолепно правда?"
            hide screen snape_main                                                                                                                   #SNAPE
            with d3                                                                                                                                                  #SNAPE
            $ s_sprite = "03_hp/10_snape_main/23.png"                                                                            #SNAPE
            show screen snape_main                                                                                                                  #SNAPE
            with d3                                                                                                                                                   #SNAPE

        elif one_of_ten == 8:
            hide screen snape_main                                                                                                                   #SNAPE
            with d3                                                                                                                                                  #SNAPE
            $ s_sprite = "03_hp/10_snape_main/24.png"                                                                            #SNAPE
            show screen snape_main                                                                                                                  #SNAPE
            with d3                                                                                                                                                   #SNAPE
            sna "Как думаешь, призраки Хогвартса подглядывают за девочками в душе?"
            hide screen snape_main                                                                                                                   #SNAPE
            with d3                                                                                                                                                  #SNAPE
            $ s_sprite = "03_hp/10_snape_main/snape_13.png"                                                                            #SNAPE
            show screen snape_main                                                                                                                  #SNAPE
            with d3                                                                                                                                                   #SNAPE
            sna "Если бы я был призраком я бы так и делал."
            hide screen snape_main                                                                                                                   #SNAPE
            with d3                                                                                                                                                  #SNAPE
            $ s_sprite = "03_hp/10_snape_main/23.png"                                                                            #SNAPE
            show screen snape_main                                                                                                                  #SNAPE
            with d3                                                                                                                                                   #SNAPE

        elif one_of_ten == 9:
            hide screen snape_main                                                                                                                   #SNAPE
            with d3                                                                                                                                                  #SNAPE
            $ s_sprite = "03_hp/10_snape_main/snape_19.png"                                                                            #SNAPE
            show screen snape_main                                                                                                                  #SNAPE
            with d3                                                                                                                                                   #SNAPE
            sna "Однажды девченка поведала мне, что она хочет быть изнасилована этим сквибом Мистером Филтчем."
            hide screen snape_main                                                                                                                   #SNAPE
            with d3                                                                                                                                                  #SNAPE
            $ s_sprite = "03_hp/10_snape_main/snape_14.png"                                                                            #SNAPE
            show screen snape_main                                                                                                                  #SNAPE
            with d3                                                                                                                                                   #SNAPE
            sna "Думаю мне стоит это утроить. Верно?"
            hide screen snape_main                                                                                                                   #SNAPE
            with d3                                                                                                                                                  #SNAPE
            $ s_sprite = "03_hp/10_snape_main/snape_02.png"                                                                            #SNAPE
            show screen snape_main                                                                                                                  #SNAPE
            with d3                                                                                                                                                   #SNAPE

        elif one_of_ten == 10:
            hide screen snape_main                                                                                                                   #SNAPE
            with d3                                                                                                                                                  #SNAPE
            $ s_sprite = "03_hp/10_snape_main/24.png"                                                                            #SNAPE
            show screen snape_main                                                                                                                  #SNAPE
            with d3                                                                                                                                                   #SNAPE
            sna "Я привык ненавидеть свою работу..."
            hide screen snape_main                                                                                                                   #SNAPE
            with d3                                                                                                                                                  #SNAPE
            $ s_sprite = "03_hp/10_snape_main/snape_06.png"                                                                            #SNAPE
            show screen snape_main                                                                                                                  #SNAPE
            with d3                                                                                                                                                   #SNAPE
            sna "Ненависть чиста, проста и уверенна..."
            hide screen snape_main                                                                                                                   #SNAPE
            with d3                                                                                                                                                  #SNAPE
            $ s_sprite = "03_hp/10_snape_main/snape_03png"                                                                            #SNAPE
            show screen snape_main                                                                                                                  #SNAPE
            with d3                                                                                                                                                   #SNAPE
            sna "А теперь, не пойми меня не правильно - я все еще ненавижу ее."
            hide screen snape_main                                                                                                                   #SNAPE
            with d3                                                                                                                                                  #SNAPE
            $ s_sprite = "03_hp/10_snape_main/snape_05.png"                                                                            #SNAPE
            show screen snape_main                                                                                                                  #SNAPE
            with d3                                                                                                                                                   #SNAPE
            sna "Но также я теперь люблю ее..."
            sna "Как не делать этого? Особенно с тем что происходит в последнее время?"
            hide screen snape_main                                                                                                                   #SNAPE
            with d3                                                                                                                                                  #SNAPE
            $ s_sprite = "03_hp/10_snape_main/snape_06.png"                                                                            #SNAPE
            show screen snape_main                                                                                                                  #SNAPE
            with d3                                                                                                                                                   #SNAPE
            sna "Ненавидеть и любить в равных пропорциях..."
            hide screen snape_main                                                                                                                   #SNAPE
            with d3                                                                                                                                                  #SNAPE
            $ s_sprite = "03_hp/10_snape_main/snape_19.png"                                                                            #SNAPE
            show screen snape_main                                                                                                                  #SNAPE
            with d3                                                                                                                                                   #SNAPE
            sna "Это как влюбится снова..."
            hide screen snape_main                                                                                                                   #SNAPE
            with d3                                                                                                                                                  #SNAPE
            $ s_sprite = "03_hp/10_snape_main/snape_06.png"                                                                            #SNAPE
            show screen snape_main                                                                                                                  #SNAPE
            with d3                                                                                                                                                   #SNAPE
        
        
    if whoring >= 21: # WHORING LEVEL 08+.
        if one_of_ten == 1:
            hide screen snape_main                                                                                                                   #SNAPE
            with d3                                                                                                                                                  #SNAPE
            $ s_sprite = "03_hp/10_snape_main/24.png"                                                                            #SNAPE
            show screen snape_main                                                                                                                  #SNAPE
            with d3                                                                                                                                                   #SNAPE
            sna "Ты знаешь что такое \"буккакэ\" а?"
            sna "А как на счет \"глубокого заглота\"?"
            sna "Так же есть \"изнасилование\"."
            hide screen snape_main                                                                                                                   #SNAPE
            with d3                                                                                                                                                  #SNAPE
            $ s_sprite = "03_hp/10_snape_main/snape_05.png"                                                                            #SNAPE
            show screen snape_main                                                                                                                  #SNAPE
            with d3                                                                                                                                                   #SNAPE
            sna "Что за дети пошли, приятель..."
            sna "У них есть клички для всего."
            hide screen snape_main                                                                                                                   #SNAPE
            with d3                                                                                                                                                  #SNAPE
            $ s_sprite = "03_hp/10_snape_main/snape_06.png"                                                                            #SNAPE
            show screen snape_main                                                                                                                  #SNAPE
            with d3                                                                                                                                                   #SNAPE
            sna "Так или иначе \"изнасилование\" был всегда..."
            hide screen snape_main                                                                                                                   #SNAPE
            with d3                                                                                                                                                  #SNAPE
            $ s_sprite = "03_hp/10_snape_main/snape_02.png"                                                                            #SNAPE
            show screen snape_main                                                                                                                  #SNAPE
            with d3                                                                                                                                                   #SNAPE
            sna "В мои дни мы называли его просто \"секс\"."

        elif one_of_ten == 2:
            hide screen snape_main                                                                                                                   #SNAPE
            with d3                                                                                                                                                  #SNAPE
            $ s_sprite = "03_hp/10_snape_main/snape_22.png"                                                                            #SNAPE
            show screen snape_main                                                                                                                  #SNAPE
            with d3                                                                                                                                                   #SNAPE
            sna "Приятель, мой член готов к \"Воспитание принцессы золотое издание\"!"
            hide screen snape_main                                                                                                                   #SNAPE
            with d3                                                                                                                                                  #SNAPE
            $ s_sprite = "03_hp/10_snape_main/snape_09.png"                                                                            #SNAPE
            show screen snape_main                                                                                                                  #SNAPE
            with d3                                                                                                                                                   #SNAPE
            sna "*Кашель!* Я имел в виду, Слизерин рулит, я ненавижу Гриффиндор и так далее..."

        elif one_of_ten == 3:
            hide screen snape_main                                                                                                                   #SNAPE
            with d3                                                                                                                                                  #SNAPE
            $ s_sprite = "03_hp/10_snape_main/24.png"                                                                            #SNAPE
            show screen snape_main                                                                                                                  #SNAPE
            with d3                                                                                                                                                   #SNAPE
            sna "Недавно я устроил вечеринку..."
            sna "Одна девочка и три парня..."
            hide screen snape_main                                                                                                                   #SNAPE
            with d3                                                                                                                                                  #SNAPE
            $ s_sprite = "03_hp/10_snape_main/snape_13.png"                                                                            #SNAPE
            show screen snape_main                                                                                                                  #SNAPE
            with d3                                                                                                                                                   #SNAPE
            sna "Они насиловали ее, а я смотрел..."
            hide screen snape_main                                                                                                                   #SNAPE
            with d3                                                                                                                                                  #SNAPE
            $ s_sprite = "03_hp/10_snape_main/snape_29.png"                                                                            #SNAPE
            show screen snape_main                                                                                                                  #SNAPE
            with d3                                                                                                                                                   #SNAPE
            sna "........................."
            hide screen snape_main                                                                                                                   #SNAPE
            with d3                                                                                                                                                  #SNAPE
            $ s_sprite = "03_hp/10_snape_main/snape_05.png"                                                                            #SNAPE
            show screen snape_main                                                                                                                  #SNAPE
            with d3                                                                                                                                                   #SNAPE
            sna "Ты думаешь я слишком поддался своей темной стороне?"
            hide screen snape_main                                                                                                                   #SNAPE
            with d3                                                                                                                                                  #SNAPE
            $ s_sprite = "03_hp/10_snape_main/snape_06.png"                                                                            #SNAPE
            show screen snape_main                                                                                                                  #SNAPE
            with d3                                                                                                                                                   #SNAPE

        elif one_of_ten == 4:
            hide screen snape_main                                                                                                                   #SNAPE
            with d3                                                                                                                                                  #SNAPE
            $ s_sprite = "03_hp/10_snape_main/24.png"                                                                            #SNAPE
            show screen snape_main                                                                                                                  #SNAPE
            with d3                                                                                                                                                   #SNAPE
            sna "У меня кончились все презервативы, приятель."
            hide screen snape_main                                                                                                                   #SNAPE
            with d3                                                                                                                                                  #SNAPE
            $ s_sprite = "03_hp/10_snape_main/snape_02.png"                                                                            #SNAPE
            show screen snape_main                                                                                                                  #SNAPE
            with d3                                                                                                                                                   #SNAPE
            sna "Подкинешь пару?"
            hide screen snape_main                                                                                                                   #SNAPE
            with d3                                                                                                                                                  #SNAPE
            $ s_sprite = "03_hp/10_snape_main/snape_01.png"                                                                            #SNAPE
            show screen snape_main                                                                                                                  #SNAPE
            with d3                                                                                                                                                   #SNAPE     

        elif one_of_ten == 5:
            hide screen snape_main                                                                                                                   #SNAPE
            with d3                                                                                                                                                  #SNAPE
            $ s_sprite = "03_hp/10_snape_main/24.png"                                                                            #SNAPE
            show screen snape_main                                                                                                                  #SNAPE
            with d3                                                                                                                                                   #SNAPE
            sna "Я тайно варю зелье которое заставляет течь женскую грудь..."
            hide screen snape_main                                                                                                                   #SNAPE
            with d3                                                                                                                                                  #SNAPE
            $ s_sprite = "03_hp/10_snape_main/snape_13.png"                                                                            #SNAPE
            show screen snape_main                                                                                                                  #SNAPE
            with d3                                                                                                                                                   #SNAPE
            sna "Великолепно, да?"
            hide screen snape_main                                                                                                                   #SNAPE
            with d3                                                                                                                                                  #SNAPE
            $ s_sprite = "03_hp/10_snape_main/23.png"                                                                            #SNAPE
            show screen snape_main                                                                                                                  #SNAPE
            with d3                                                                                                                                                   #SNAPE

        elif one_of_ten == 6:
            hide screen snape_main                                                                                                                   #SNAPE
            with d3                                                                                                                                                  #SNAPE
            $ s_sprite = "03_hp/10_snape_main/24.png"                                                                            #SNAPE
            show screen snape_main                                                                                                                  #SNAPE
            with d3                                                                                                                                                   #SNAPE
            sna "Итак, эта ведьма взяла мой член в свой рот, верно?"
            hide screen snape_main                                                                                                                   #SNAPE
            with d3                                                                                                                                                  #SNAPE
            $ s_sprite = "03_hp/10_snape_main/snape_02.png"                                                                            #SNAPE
            show screen snape_main                                                                                                                  #SNAPE
            with d3                                                                                                                                                   #SNAPE
            sna "Ее горячие подружки занимались моим задом..."
            sna "В это время третья девченка ждала меня на коленях с открытым ртом, ожидая что я сейчас кончу..."
            sna "Каждый раз когда я извергался, она говорила: \"Благодарю вас, профессор Снейп\"."
            hide screen snape_main                                                                                                                   #SNAPE
            with d3                                                                                                                                                  #SNAPE
            $ s_sprite = "03_hp/10_snape_main/snape_22.png"                                                                            #SNAPE
            show screen snape_main                                                                                                                  #SNAPE
            with d3                                                                                                                                                   #SNAPE
            sna "Это был очень выматывающий вечер..."
            hide screen snape_main                                                                                                                   #SNAPE
            with d3                                                                                                                                                  #SNAPE
            $ s_sprite = "03_hp/10_snape_main/snape_02.png"                                                                            #SNAPE
            show screen snape_main                                                                                                                  #SNAPE
            with d3                                                                                                                                                   #SNAPE

        elif one_of_ten == 7:
            hide screen snape_main                                                                                                                   #SNAPE
            with d3                                                                                                                                                  #SNAPE
            $ s_sprite = "03_hp/10_snape_main/snape_06.png"                                                                            #SNAPE
            show screen snape_main                                                                                                                  #SNAPE
            with d3                                                                                                                                                   #SNAPE
            sna "Одна из девченок меня приследует и умоляет, что бы я мочился ей в рот..."
            sna "Настойчивая маленькая шлюха..."
            hide screen snape_main                                                                                                                   #SNAPE
            with d3                                                                                                                                                  #SNAPE
            $ s_sprite = "03_hp/10_snape_main/snape_05.png"                                                                            #SNAPE
            show screen snape_main                                                                                                                  #SNAPE
            with d3                                                                                                                                                   #SNAPE
            sna "Может мне помочь ей?"
            hide screen snape_main                                                                                                                   #SNAPE
            with d3                                                                                                                                                  #SNAPE
            $ s_sprite = "03_hp/10_snape_main/23.png"                                                                            #SNAPE
            show screen snape_main                                                                                                                  #SNAPE
            with d3                                                                                                                                                   #SNAPE

        elif one_of_ten == 8:
            hide screen snape_main                                                                                                                   #SNAPE
            with d3                                                                                                                                                  #SNAPE
            $ s_sprite = "03_hp/10_snape_main/snape_04.png"                                                                            #SNAPE
            show screen snape_main                                                                                                                  #SNAPE
            with d3                                                                                                                                                   #SNAPE
            sna "Я одинаково доминирую над всеми студентами..."
            hide screen snape_main                                                                                                                   #SNAPE
            with d3                                                                                                                                                  #SNAPE
            $ s_sprite = "03_hp/10_snape_main/snape_22.png"                                                                            #SNAPE
            show screen snape_main                                                                                                                  #SNAPE
            with d3                                                                                                                                                   #SNAPE
            sna "Но у меня к каждому свой подход."
            hide screen snape_main                                                                                                                   #SNAPE
            with d3                                                                                                                                                  #SNAPE
            $ s_sprite = "03_hp/10_snape_main/23.png"                                                                            #SNAPE
            show screen snape_main                                                                                                                  #SNAPE
            with d3                                                                                                                                                   #SNAPE

        elif one_of_ten == 9:
            hide screen snape_main                                                                                                                   #SNAPE
            with d3                                                                                                                                                  #SNAPE
            $ s_sprite = "03_hp/10_snape_main/23.png"                                                                            #SNAPE
            show screen snape_main                                                                                                                  #SNAPE
            with d3                                                                                                                                                   #SNAPE
            sna "Я люблю свою жизнь!"
            hide screen snape_main                                                                                                                   #SNAPE
            with d3                                                                                                                                                  #SNAPE
            $ s_sprite = "03_hp/10_snape_main/snape_16.png"                                                                            #SNAPE
            show screen snape_main                                                                                                                  #SNAPE
            with d3                                                                                                                                                   #SNAPE
            sna "Но все еще ненавижу свою работу..."
            hide screen snape_main                                                                                                                   #SNAPE
            with d3                                                                                                                                                  #SNAPE
            $ s_sprite = "03_hp/10_snape_main/snape_14.png"                                                                            #SNAPE
            show screen snape_main                                                                                                                  #SNAPE
            with d3                                                                                                                                                   #SNAPE
            sna "Если бы я мог забросить преподавание, но продолжать веселится."
            hide screen snape_main                                                                                                                   #SNAPE
            with d3                                                                                                                                                  #SNAPE
            $ s_sprite = "03_hp/10_snape_main/23.png"                                                                            #SNAPE
            show screen snape_main                                                                                                                  #SNAPE
            with d3                                                                                                                                                   #SNAPE

        elif one_of_ten == 10:
            hide screen snape_main                                                                                                                   #SNAPE
            with d3                                                                                                                                                  #SNAPE
            $ s_sprite = "03_hp/10_snape_main/24.png"                                                                            #SNAPE
            show screen snape_main                                                                                                                  #SNAPE
            with d3                                                                                                                                                   #SNAPE
            sna "Мне почти стыдно за мои похождения."
            hide screen snape_main                                                                                                                   #SNAPE
            with d3                                                                                                                                                  #SNAPE
            $ s_sprite = "03_hp/10_snape_main/snape_14.png"                                                                            #SNAPE
            show screen snape_main                                                                                                                  #SNAPE
            with d3                                                                                                                                                   #SNAPE
            sna "Хочешь пришлю тебе пару шлюх?"
            hide screen snape_main                                                                                                                   #SNAPE
            with d3                                                                                                                                                  #SNAPE
            $ s_sprite = "03_hp/10_snape_main/23.png"                                                                            #SNAPE
            show screen snape_main                                                                                                                  #SNAPE
            with d3                                                                                                                                                   #SNAPE

        
    
    
    
    
    
    
    
    
    jump snape_ready
    
    
    
#    $ snape_busy = True
    
#    hide screen snape_02 #Snape stands still.
#    hide screen bld1
#    hide screen snape_main
#    with d3
#    $ renpy.play('sounds/door.mp3') #Sound of a door opening.
            
  
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    

### CHITCHAT EVENTS ###
label chitchat_event_01: #Snape says: so you tutor her now?". Happens after tutoring unlocks.
    hide screen snape_main
    with d3
    sna_01 "Итак..."
    sna_01 "Я слышал что мисс Греинджер начала заниматься с вами наедине?"
    m "Да, полагаю это так..."
    m "Не думаю что это входит в наш план."
    sna_09 "Что ты имеешь в виду? Все идет отлично."
    sna_09 "Я лично и пара учителей делаем ее занятия не выносимыми!"
    sna_09 "И в результате она стала заниматься больше..."
    sna_09 "Даже заниматся наедине..."
    sna_18 "И теперь у нее все меньше и меньше времени докучать мне."
    m "Понятно..."
    sna_10 "Да, да... ну, что бы ты знал..."
    sna_10 "Только не учи ее ничему полезному, ладно?"
    m "Я постараюсь."
    sna_01 "Ладно, на сегодня всё..."
    
    
    
    

    hide screen bld1
    with d3
    $ walk_xpos=360 #Animation of walking chibi. (From desk)
    $ walk_xpos2=610 #Coordinates of it's movement. (To the door)
    $ snapes_speed = 03.0 #The speed of moving the walking animation across the screen.
    show screen snape_walk_01_f 
    pause 3
    $ renpy.play('sounds/door.mp3') #Sound of a door opening.
    hide screen snape_walk_01_f 
    with d3

    $ chitchat_event_01_happened = True #Activates next event - Event_15 Hermione sells her first favour.
    $ snape_busy = True
    $ days_without_an_event = 0
    
    play music "music/Brittle Rille.mp3" fadein 1 fadeout 1
    
    jump day_main_menu











### CHITCHAT WITH HERMIONE ###
label chit_chat:
    $ one_of_ten = renpy.random.randint(1, 10) #Generating one number out of three for various porpoises.
    $ herView.change( 0 )
    $ pos = gMakePos( h_xpos, h_ypos )
    if whoring >= 0 and whoring <= 2: # WHORING LEVEL 01.
        if one_of_ten == 1:
            #__#hide screen hermione_main                                                                                                                                                                                   #HERMIONE
            #__#with d3                                                                                                                                                                                                                        #HERMIONE
            $ herView.hideQQ()
            #__#$ h_body = "03_hp/13_hermione_main/body_04.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
            #__#show screen hermione_main                                                                                                                                                                                 #HERMIONE
            #__#with d3                                                                                                                                                                                                                        #HERMIONE
            $herView.showQQ( "body_04.png", pos )
            her "Может быть, если я буду работать быстрее, я смогу втиснуть пару занятий в мое рассписание..."
            #__#hide screen hermione_main                                                                                                                                                                                   #HERMIONE
            #__#with d3                                                                                                                                                                                                                        #HERMIONE
            $herView.hideQQ()
            #__#$ h_body = "03_hp/13_hermione_main/body_03.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
            #__#show screen hermione_main                                                                                                                                                                                 #HERMIONE
            #__#with d3                                                                                                                                                                                                                        #HERMIONE
            $herView.showQQ( "body_03.png", pos )
        
        elif one_of_ten == 2:
            #__#hide screen hermione_main                                                                                                                                                                                   #HERMIONE
            #__#with d3                                                                                                                                                                                                                        #HERMIONE
            $herView.hideQQ()
            #__#$ h_body = "03_hp/13_hermione_main/body_04.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
            #__#show screen hermione_main                                                                                                                                                                                 #HERMIONE
            #__#with d3                                                                                                                                                                                                                        #HERMIONE
            $herView.showQQ( "body_04.png", pos )
            her "Вобщем-то мне нравится когда меня зовут \"Всезнайка\"."
            her "Возможно я даже краснею от этого..."
            #__#hide screen hermione_main                                                                                                                                                                                   #HERMIONE
            #__#with d3                                                                                                                                                                                                                        #HERMIONE
            $herView.hideQQ()
            #__#$ h_body = "03_hp/13_hermione_main/body_03.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
            #__#show screen hermione_main                                                                                                                                                                                 #HERMIONE
            #__#with d3                                                                                                                                                                                                                        #HERMIONE
            $herView.showQQ( "body_03.png", pos )
        elif one_of_ten == 3:
            #__#hide screen hermione_main                                                                                                                                                                                   #HERMIONE
            #__#with d3                                                                                                                                                                                                                        #HERMIONE
            $herView.hideQQ()
            #__#$ h_body = "03_hp/13_hermione_main/body_04.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
            #__#show screen hermione_main                                                                                                                                                                                 #HERMIONE
            #__#with d3                                                                                                                                                                                                                        #HERMIONE
            $herView.showQQ( "body_04.png", pos )
            her "Василиск, также известен как король змей."
            her "Герпо Фол первый осеменил Василиска."
            her "Он сделал это с помощью--"
            #__#hide screen hermione_main                                                                                                                                                                                   #HERMIONE
            #__#with d3                                                                                                                                                                                                                        #HERMIONE
            $herView.hideQQ()
            #__#$ h_body = "03_hp/13_hermione_main/body_10.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
            #__#show screen hermione_main                                                                                                                                                                                 #HERMIONE
            #__#with d3                                                                                                                                                                                                                        #HERMIONE
            $herView.showQQ( "body_10.png", pos )
            her "Ой, Извините, профессор, у нас еще один тест завтра..."
            her "Я просто хочу знать, что я готова..."
            #__#hide screen hermione_main                                                                                                                                                                                   #HERMIONE
            #__#with d3                                                                                                                                                                                                                        #HERMIONE
            $herView.hideQQ()
            #__#$ h_body = "03_hp/13_hermione_main/body_01.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
            #__#show screen hermione_main                                                                                                                                                                                 #HERMIONE
            #__#with d3                                                                                                                                                                                                                        #HERMIONE
            $herView.showQQ( "body_01.png", pos )
        elif one_of_ten == 4:
            #__#hide screen hermione_main                                                                                                                                                                                   #HERMIONE
            #__#with d3                                                                                                                                                                                                                        #HERMIONE
            $herView.hideQQ()
            #__#$ h_body = "03_hp/13_hermione_main/body_10.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
            #__#show screen hermione_main                                                                                                                                                                                 #HERMIONE
            #__#with d3                                                                                                                                                                                                                        #HERMIONE
            $herView.showQQ( "body_10.png", pos )
            her "Если бы мое тело не требовало сна..."
            #__#hide screen hermione_main                                                                                                                                                                                   #HERMIONE
            #__#with d3                                                                                                                                                                                                                        #HERMIONE
            $herView.hideQQ()
            #__#$ h_body = "03_hp/13_hermione_main/body_18.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
            #__#show screen hermione_main                                                                                                                                                                                 #HERMIONE
            #__#with d3                                                                                                                                                                                                                        #HERMIONE
            $herView.showQQ( "body_18.png", pos )
            her "Тогда бы я могла заниматся в два раза больше!?"
            #__#hide screen hermione_main                                                                                                                                                                                   #HERMIONE
            #__#with d3                                                                                                                                                                                                                        #HERMIONE
            $herView.hideQQ()
            #__#$ h_body = "03_hp/13_hermione_main/body_14.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
            #__#show screen hermione_main                                                                                                                                                                                 #HERMIONE
            #__#with d3                                                                                                                                                                                                                        #HERMIONE
            $herView.showQQ( "body_14.png", pos )
            her "Надеюсь есть заклинание для этого..."
            #__#hide screen hermione_main                                                                                                                                                                                   #HERMIONE
            #__#with d3                                                                                                                                                                                                                        #HERMIONE
            $herView.hideQQ()
            #__#$ h_body = "03_hp/13_hermione_main/body_03.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
            #__#show screen hermione_main                                                                                                                                                                                 #HERMIONE
            #__#with d3                                                                                                                                                                                                                        #HERMIONE
            $herView.showQQ( "body_03.png", pos )
        
        elif one_of_ten == 5:
            #__#hide screen hermione_main                                                                                                                                                                                   #HERMIONE
            #__#with d3                                                                                                                                                                                                                        #HERMIONE
            $herView.hideQQ()
            #__#$ h_body = "03_hp/13_hermione_main/body_04.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
            #__#show screen hermione_main                                                                                                                                                                                 #HERMIONE
            #__#with d3                                                                                                                                                                                                                        #HERMIONE
            $herView.showQQ( "body_04.png", pos )
            her "Пока профессор Трелони не обучил меня хотябы капелькой каких-либо фактических знаний, сэр."
            #__#hide screen hermione_main                                                                                                                                                                                   #HERMIONE
            #__#with d3                                                                                                                                                                                                                        #HERMIONE
            $herView.hideQQ()
            #__#$ h_body = "03_hp/13_hermione_main/body_03.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
            #__#show screen hermione_main                                                                                                                                                                                 #HERMIONE
            #__#with d3                                                                                                                                                                                                                        #HERMIONE
            $herView.showQQ( "body_03.png", pos )
            
        elif one_of_ten == 6:
            #__#hide screen hermione_main                                                                                                                                                                                   #HERMIONE
            #__#with d3                                                                                                                                                                                                                        #HERMIONE
            $herView.hideQQ()
            #__#$ h_body = "03_hp/13_hermione_main/body_04.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
            #__#show screen hermione_main                                                                                                                                                                                 #HERMIONE
            #__#with d3                                                                                                                                                                                                                        #HERMIONE
            $herView.showQQ( "body_04.png", pos )
            her "Если бы только студенты были честными, они бы полюбили ответственность."
            #__#hide screen hermione_main                                                                                                                                                                                   #HERMIONE
            #__#with d3                                                                                                                                                                                                                        #HERMIONE
            $herView.hideQQ()
            #__#$ h_body = "03_hp/13_hermione_main/body_03.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
            #__#show screen hermione_main                                                                                                                                                                                 #HERMIONE
            #__#with d3                                                                                                                                                                                                                        #HERMIONE
            $herView.showQQ( "body_03.png", pos )
      
        elif one_of_ten == 7:
            #__#hide screen hermione_main                                                                                                                                                                                   #HERMIONE
            #__#with d3                                                                                                                                                                                                                        #HERMIONE
            $herView.hideQQ()
            #__#$ h_body = "03_hp/13_hermione_main/body_04.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
            #__#show screen hermione_main                                                                                                                                                                                 #HERMIONE
            #__#with d3                                                                                                                                                                                                                        #HERMIONE
            $herView.showQQ( "body_04.png", pos )
            her "Как люди могу быть такими безразличными к мировым проблемам?"
            her "Лично я считаю, что мы все должны работать вместе, чтобы мир стал лучше."
            #__#hide screen hermione_main                                                                                                                                                                                   #HERMIONE
            #__#with d3                                                                                                                                                                                                                        #HERMIONE
            $herView.hideQQ()
            #__#$ h_body = "03_hp/13_hermione_main/body_03.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
            #__#show screen hermione_main                                                                                                                                                                                 #HERMIONE
            #__#with d3                                                                                                                                                                                                                        #HERMIONE
            $herView.showQQ( "body_03.png", pos )
            
        elif one_of_ten == 8:
            #__#hide screen hermione_main                                                                                                                                                                                   #HERMIONE
            #__#with d3                                                                                                                                                                                                                        #HERMIONE
            $herView.hideQQ()
            #__#$ h_body = "03_hp/13_hermione_main/body_10.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
            #__#show screen hermione_main                                                                                                                                                                                 #HERMIONE
            #__#with d3                                                                                                                                                                                                                        #HERMIONE
            $herView.showQQ( "body_10.png", pos )
            her "В последнее время дождь льет чаще..."
            #__#hide screen hermione_main                                                                                                                                                                                   #HERMIONE
            #__#with d3                                                                                                                                                                                                                        #HERMIONE
            $herView.hideQQ()
            #__#$ h_body = "03_hp/13_hermione_main/body_01.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
            #__#show screen hermione_main                                                                                                                                                                                 #HERMIONE
            #__#with d3                                                                                                                                                                                                                        #HERMIONE
            $herView.showQQ( "body_01.png", pos )
    
        elif one_of_ten == 9:
            #__#hide screen hermione_main                                                                                                                                                                                   #HERMIONE
            #__#with d3                                                                                                                                                                                                                        #HERMIONE
            $herView.hideQQ()
            #__#$ h_body = "03_hp/13_hermione_main/body_10.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
            #__#show screen hermione_main                                                                                                                                                                                 #HERMIONE
            #__#with d3                                                                                                                                                                                                                        #HERMIONE
            $herView.showQQ( "body_10.png", pos )
            her "Очень мало людей знает..."
            #__#hide screen hermione_main                                                                                                                                                                                   #HERMIONE
            #__#with d3                                                                                                                                                                                                                        #HERMIONE
            $herView.hideQQ()
            #__#$ h_body = "03_hp/13_hermione_main/body_06.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
            #__#show screen hermione_main                                                                                                                                                                                 #HERMIONE
            #__#with d3                                                                                                                                                                                                                        #HERMIONE
            $herView.showQQ( "body_06.png", pos )
            her "...что я очень люблю шоколад."
            #__#hide screen hermione_main                                                                                                                                                                                   #HERMIONE
            #__#with d3                                                                                                                                                                                                                        #HERMIONE
            $herView.hideQQ()
            #__#$ h_body = "03_hp/13_hermione_main/body_01.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
            #__#show screen hermione_main                                                                                                                                                                                 #HERMIONE
            #__#with d3                                                                                                                                                                                                                        #HERMIONE
            $herView.showQQ( "body_01.png", pos )
       
        elif one_of_ten == 10:
            #__#hide screen hermione_main                                                                                                                                                                                   #HERMIONE
            #__#with d3                                                                                                                                                                                                                        #HERMIONE
            $herView.hideQQ()
            #__#$ h_body = "03_hp/13_hermione_main/body_06.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
            #__#show screen hermione_main                                                                                                                                                                                 #HERMIONE
            #__#with d3                                                                                                                                                                                                                        #HERMIONE
            $herView.showQQ( "body_06.png", pos )
            her "Извините сэр, но у меня нету времени на разговоры..."
            #__#hide screen hermione_main                                                                                                                                                                                   #HERMIONE
            #__#with d3                                                                                                                                                                                                                        #HERMIONE
            $herView.hideQQ()
            #__#$ h_body = "03_hp/13_hermione_main/body_03.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
            #__#show screen hermione_main                                                                                                                                                                                 #HERMIONE
            #__#with d3                                                                                                                                                                                                                        #HERMIONE
            $herView.showQQ( "body_03.png", pos )
            

    if whoring >= 3 and whoring <= 5: # WHORING LEVEL 02
        if one_of_ten == 1:
            #__#hide screen hermione_main                                                                                                                                                                                   #HERMIONE
            #__#with d3                                                                                                                                                                                                                        #HERMIONE
            $herView.hideQQ()
            #__#$ h_body = "03_hp/13_hermione_main/body_04.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
            #__#show screen hermione_main                                                                                                                                                                                 #HERMIONE
            #__#with d3                                                                                                                                                                                                                        #HERMIONE
            $herView.showQQ( "body_04.png", pos )
            her "Я где то прочитала что полная луна помогает сосредоточится..."
            #__#hide screen hermione_main                                                                                                                                                                                   #HERMIONE
            #__#with d3                                                                                                                                                                                                                        #HERMIONE
            $herView.hideQQ()
            #__#$ h_body = "03_hp/13_hermione_main/body_03.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
            #__#show screen hermione_main                                                                                                                                                                                 #HERMIONE
            #__#with d3                                                                                                                                                                                                                        #HERMIONE
            $herView.showQQ( "body_03.png", pos )
            
        elif one_of_ten == 2:
            #__#hide screen hermione_main                                                                                                                                                                                   #HERMIONE
            #__#with d3                                                                                                                                                                                                                        #HERMIONE
            $herView.hideQQ()
            #__#$ h_body = "03_hp/13_hermione_main/body_06.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
            #__#show screen hermione_main                                                                                                                                                                                 #HERMIONE
            #__#with d3                                                                                                                                                                                                                        #HERMIONE
            $herView.showQQ( "body_06.png", pos )
            her "Я обожаю сидеть с книгой у огня когда льет дождь..."
            #__#hide screen hermione_main                                                                                                                                                                                   #HERMIONE
            #__#with d3                                                                                                                                                                                                                        #HERMIONE
            $herView.hideQQ()
            #__#$ h_body = "03_hp/13_hermione_main/body_01.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
            #__#show screen hermione_main                                                                                                                                                                                 #HERMIONE
            #__#with d3                                                                                                                                                                                                                        #HERMIONE
            $herView.showQQ( "body_01.png", pos )
            
        elif one_of_ten == 3:
            #__#hide screen hermione_main                                                                                                                                                                                   #HERMIONE
            #__#with d3                                                                                                                                                                                                                        #HERMIONE
            $herView.hideQQ()
            #__#$ h_body = "03_hp/13_hermione_main/body_10.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
            #__#show screen hermione_main                                                                                                                                                                                 #HERMIONE
            #__#with d3                                                                                                                                                                                                                        #HERMIONE
            $herView.showQQ( "body_10.png", pos )
            her "Есть слух что профессор Снейп что-то замышляет в школе..."
            #__#hide screen hermione_main                                                                                                                                                                                   #HERMIONE
            #__#with d3                                                                                                                                                                                                                        #HERMIONE
            $herView.hideQQ()
            #__#$ h_body = "03_hp/13_hermione_main/body_15.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
            #__#show screen hermione_main                                                                                                                                                                                 #HERMIONE
            #__#with d3                                                                                                                                                                                                                        #HERMIONE
            $herView.showQQ( "body_15.png", pos )
            her "Нет, пожалуй ничего..."
            #__#hide screen hermione_main                                                                                                                                                                                   #HERMIONE
            #__#with d3                                                                                                                                                                                                                        #HERMIONE
            $herView.hideQQ()
            #__#$ h_body = "03_hp/13_hermione_main/body_03.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
            #__#show screen hermione_main                                                                                                                                                                                 #HERMIONE
            #__#with d3                                                                                                                                                                                                                        #HERMIONE
            $herView.showQQ( "body_03.png", pos )
            
        elif one_of_ten == 4:
            #__#hide screen hermione_main                                                                                                                                                                                   #HERMIONE
            #__#with d3                                                                                                                                                                                                                        #HERMIONE
            $herView.hideQQ()
            #__#$ h_body = "03_hp/13_hermione_main/body_04.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
            #__#show screen hermione_main                                                                                                                                                                                 #HERMIONE
            #__#with d3                                                                                                                                                                                                                        #HERMIONE
            $herView.showQQ( "body_04.png", pos )
            her "Не смотря на сомнительность услуг, которые я вам оказывала, сэр..."
            her "Я благодарна вам за вашу помощь..."
            #__#hide screen hermione_main                                                                                                                                                                                   #HERMIONE
            #__#with d3                                                                                                                                                                                                                        #HERMIONE
            $herView.hideQQ()
            #__#$ h_body = "03_hp/13_hermione_main/body_09.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
            #__#show screen hermione_main                                                                                                                                                                                 #HERMIONE
            #__#with d3                                                                                                                                                                                                                        #HERMIONE
            $herView.showQQ( "body_09.png", pos )
            her "Гриффиндор нуждается в этих очках больше чем когда либо..."
            #__#hide screen hermione_main                                                                                                                                                                                   #HERMIONE
            #__#with d3                                                                                                                                                                                                                        #HERMIONE
            $herView.hideQQ()
            #__#$ h_body = "03_hp/13_hermione_main/body_03.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
            #__#show screen hermione_main                                                                                                                                                                                 #HERMIONE
            #__#with d3                                                                                                                                                                                                                        #HERMIONE
            $herView.showQQ( "body_03.png", pos )
            
        elif one_of_ten == 5:
            #__#hide screen hermione_main                                                                                                                                                                                   #HERMIONE
            #__#with d3                                                                                                                                                                                                                        #HERMIONE
            $herView.hideQQ()
            #__#$ h_body = "03_hp/13_hermione_main/body_04.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
            #__#show screen hermione_main                                                                                                                                                                                 #HERMIONE
            #__#with d3                                                                                                                                                                                                                        #HERMIONE
            $herView.showQQ( "body_04.png", pos )
            her "Почему квиддич так популярен среди девочек я не могу понять..."
            #__#hide screen hermione_main                                                                                                                                                                                   #HERMIONE
            #__#with d3                                                                                                                                                                                                                        #HERMIONE
            $herView.hideQQ()
            #__#$ h_body = "03_hp/13_hermione_main/body_03.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
            #__#show screen hermione_main                                                                                                                                                                                 #HERMIONE
            #__#with d3                                                                                                                                                                                                                        #HERMIONE
            $herView.showQQ( "body_03.png", pos )
            
        elif one_of_ten == 6:
            #__#hide screen hermione_main                                                                                                                                                                                   #HERMIONE
            #__#with d3                                                                                                                                                                                                                        #HERMIONE
            $herView.hideQQ()
            #__#$ h_body = "03_hp/13_hermione_main/body_04.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
            #__#show screen hermione_main                                                                                                                                                                                 #HERMIONE
            #__#with d3                                                                                                                                                                                                                        #HERMIONE
            $herView.showQQ( "body_04.png", pos )
            her "Наше \"Движение прав человека\" набирает популярность."
            her "Это очень важно знать, что вы помогаете развивать наше общество."
            #__#hide screen hermione_main                                                                                                                                                                                   #HERMIONE
            #__#with d3                                                                                                                                                                                                                        #HERMIONE
            $herView.hideQQ()
            #__#$ h_body = "03_hp/13_hermione_main/body_03.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
            #__#show screen hermione_main                                                                                                                                                                                 #HERMIONE
            #__#with d3                                                                                                                                                                                                                        #HERMIONE
            $herView.showQQ( "body_03.png", pos )
            
        elif one_of_ten == 7:
            #__#hide screen hermione_main                                                                                                                                                                                   #HERMIONE
            #__#with d3                                                                                                                                                                                                                        #HERMIONE
            $herView.hideQQ()
            #__#$ h_body = "03_hp/13_hermione_main/body_04.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
            #__#show screen hermione_main                                                                                                                                                                                 #HERMIONE
            #__#with d3                                                                                                                                                                                                                        #HERMIONE
            $herView.showQQ( "body_04.png", pos )
            her "Хогвартс имеет внушительную библеотеку..."
            #__#hide screen hermione_main                                                                                                                                                                                   #HERMIONE
            #__#with d3                                                                                                                                                                                                                        #HERMIONE
            $herView.hideQQ()
            #__#$ h_body = "03_hp/13_hermione_main/body_08.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
            #__#show screen hermione_main                                                                                                                                                                                 #HERMIONE
            #__#with d3                                                                                                                                                                                                                        #HERMIONE
            $herView.showQQ( "body_08.png", pos )
            her "Но я все еще хочу, чтобы она была больше..."
            #__#hide screen hermione_main                                                                                                                                                                                   #HERMIONE
            #__#with d3                                                                                                                                                                                                                        #HERMIONE
            $herView.hideQQ()
            #__#$ h_body = "03_hp/13_hermione_main/body_03.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
            #__#show screen hermione_main                                                                                                                                                                                 #HERMIONE
            #__#with d3                                                                                                                                                                                                                        #HERMIONE
            $herView.showQQ( "body_03.png", pos )
            
        elif one_of_ten == 8:
            #__#hide screen hermione_main                                                                                                                                                                                   #HERMIONE
            #__#with d3                                                                                                                                                                                                                        #HERMIONE
            $herView.hideQQ()
            #__#$ h_body = "03_hp/13_hermione_main/body_10.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
            #__#show screen hermione_main                                                                                                                                                                                 #HERMIONE
            #__#with d3                                                                                                                                                                                                                        #HERMIONE
            $herView.showQQ( "body_10.png", pos )
            her "Как и все студенты школы у меня есть репутация..."
            her "Люди смотрят на меня..."
            #__#hide screen hermione_main                                                                                                                                                                                   #HERMIONE
            #__#with d3                                                                                                                                                                                                                        #HERMIONE
            $herView.hideQQ()
            #__#$ h_body = "03_hp/13_hermione_main/body_31.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
            #__#show screen hermione_main                                                                                                                                                                                 #HERMIONE
            #__#with d3                                                                                                                                                                                                                        #HERMIONE
            $herView.showQQ( "body_31.png", pos )
            her "...я очень ценю, что вы присматриваете за мной, сэр."
            #__#hide screen hermione_main                                                                                                                                                                                   #HERMIONE
            #__#with d3                                                                                                                                                                                                                        #HERMIONE
            $herView.hideQQ()
            #__#$ h_body = "03_hp/13_hermione_main/body_29.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
            #__#show screen hermione_main                                                                                                                                                                                 #HERMIONE
            #__#with d3                                                                                                                                                                                                                        #HERMIONE
            $herView.showQQ( "body_29.png", pos )
            
        elif one_of_ten == 9:
            #__#hide screen hermione_main                                                                                                                                                                                   #HERMIONE
            #__#with d3                                                                                                                                                                                                                        #HERMIONE
            $herView.hideQQ()
            #__#$ h_body = "03_hp/13_hermione_main/body_11.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
            #__#show screen hermione_main                                                                                                                                                                                 #HERMIONE
            #__#with d3                                                                                                                                                                                                                        #HERMIONE
            $herView.showQQ( "body_11.png", pos )
            her "Услуги которые я вам оказала тогда, сэр..."
            #__#hide screen hermione_main                                                                                                                                                                                   #HERMIONE
            #__#with d3                                                                                                                                                                                                                        #HERMIONE
            $herView.hideQQ()
            #__#$ h_body = "03_hp/13_hermione_main/body_33.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
            #__#show screen hermione_main                                                                                                                                                                                 #HERMIONE
            #__#with d3                                                                                                                                                                                                                        #HERMIONE
            $herView.showQQ( "body_33.png", pos )
            her "......."
            #__#hide screen hermione_main                                                                                                                                                                                   #HERMIONE
            #__#with d3                                                                                                                                                                                                                        #HERMIONE
            $herView.hideQQ()
            #__#$ h_body = "03_hp/13_hermione_main/body_87.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
            #__#show screen hermione_main                                                                                                                                                                                 #HERMIONE
            #__#with d3                                                                                                                                                                                                                        #HERMIONE
            $herView.showQQ( "body_87.png", pos )
            her "Я согласилась на это только изза моего факультета."
            #__#hide screen hermione_main                                                                                                                                                                                   #HERMIONE
            #__#with d3                                                                                                                                                                                                                        #HERMIONE
            $herView.hideQQ()
            #__#$ h_body = "03_hp/13_hermione_main/body_120.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
            #__#show screen hermione_main                                                                                                                                                                                 #HERMIONE
            #__#with d3                                                                                                                                                                                                                        #HERMIONE
            $herView.showQQ( "body_120.png", pos )
            her "Я просто хотела, чтобы вы знали это, сэр..."
            
        elif one_of_ten == 10:
            #__#hide screen hermione_main                                                                                                                                                                                   #HERMIONE
            #__#with d3                                                                                                                                                                                                                        #HERMIONE
            $herView.hideQQ()
            #__#$ h_body = "03_hp/13_hermione_main/body_04.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
            #__#show screen hermione_main                                                                                                                                                                                 #HERMIONE
            #__#with d3                                                                                                                                                                                                                        #HERMIONE
            $herView.showQQ( "body_04.png", pos )
            her "Наш \"Осенний бал\" будет через несколько месяцев..."
            #__#hide screen hermione_main                                                                                                                                                                                   #HERMIONE
            #__#with d3                                                                                                                                                                                                                        #HERMIONE
            $herView.hideQQ()
            #__#$ h_body = "03_hp/13_hermione_main/body_11.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
            #__#show screen hermione_main                                                                                                                                                                                 #HERMIONE
            #__#with d3                                                                                                                                                                                                                        #HERMIONE
            $herView.showQQ( "body_11.png", pos )
            her "Но уже некоторые девочки обсуждают что они наденут на бал..."
            #__#hide screen hermione_main                                                                                                                                                                                   #HERMIONE
            #__#with d3                                                                                                                                                                                                                        #HERMIONE
            $herView.hideQQ()
            #__#$ h_body = "03_hp/13_hermione_main/body_185.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
            #__#show screen hermione_main                                                                                                                                                                                 #HERMIONE
            #__#with d3                                                                                                                                                                                                                        #HERMIONE
            $herView.showQQ( "body_185.png", pos )
            
  
    if whoring >= 6 and whoring <= 8: # WHORING LEVEL 03.
        if one_of_ten == 1:
            #__#hide screen hermione_main                                                                                                                                                                                   #HERMIONE
            #__#with d3                                                                                                                                                                                                                        #HERMIONE
            $herView.hideQQ()
            #__#$ h_body = "03_hp/13_hermione_main/body_04.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
            #__#show screen hermione_main                                                                                                                                                                                 #HERMIONE
            #__#with d3                                                                                                                                                                                                                        #HERMIONE
            $herView.showQQ( "body_04.png", pos )
            her "Вы помните как вы просили мои трусики в первый раз?"
            her "Я тогда так сильно разозлилась..."
            #__#hide screen hermione_main                                                                                                                                                                                   #HERMIONE
            #__#with d3                                                                                                                                                                                                                        #HERMIONE
            $herView.hideQQ()
            #__#$ h_body = "03_hp/13_hermione_main/body_09.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
            #__#show screen hermione_main                                                                                                                                                                                 #HERMIONE
            #__#with d3                                                                                                                                                                                                                        #HERMIONE
            $herView.showQQ( "body_09.png", pos )
            her "Тепеь я вижу что я была не права..."
            her "Ведь судьба факультета на мне..."
            #__#hide screen hermione_main                                                                                                                                                                                   #HERMIONE
            #__#with d3                                                                                                                                                                                                                        #HERMIONE
            $herView.hideQQ()
            #__#$ h_body = "03_hp/13_hermione_main/body_07.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
            #__#show screen hermione_main                                                                                                                                                                                 #HERMIONE
            #__#with d3                                                                                                                                                                                                                        #HERMIONE
            $herView.showQQ( "body_07.png", pos )
            her "Все остальное не должно меня волновать!"
            
        elif one_of_ten == 2:
            #__#hide screen hermione_main                                                                                                                                                                                   #HERMIONE
            #__#with d3                                                                                                                                                                                                                        #HERMIONE
            $herView.hideQQ()
            #__#$ h_body = "03_hp/13_hermione_main/body_04.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
            #__#show screen hermione_main                                                                                                                                                                                 #HERMIONE
            #__#with d3                                                                                                                                                                                                                        #HERMIONE
            $herView.showQQ( "body_04.png", pos )
            her "Скорость с которой Слизерин набирает очки в последнее время просто невозможная."
            #__#hide screen hermione_main                                                                                                                                                                                   #HERMIONE
            #__#with d3                                                                                                                                                                                                                        #HERMIONE
            $herView.hideQQ()
            #__#$ h_body = "03_hp/13_hermione_main/body_05.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
            #__#show screen hermione_main                                                                                                                                                                                 #HERMIONE
            #__#with d3                                                                                                                                                                                                                        #HERMIONE
            $herView.showQQ( "body_05.png", pos )
            her "Я думаю профессор Снейп стоит за этим."
            #__#hide screen hermione_main                                                                                                                                                                                   #HERMIONE
            #__#with d3                                                                                                                                                                                                                        #HERMIONE
            $herView.hideQQ()
            #__#$ h_body = "03_hp/13_hermione_main/body_04.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
            #__#show screen hermione_main                                                                                                                                                                                 #HERMIONE
            #__#with d3                                                                                                                                                                                                                        #HERMIONE
            $herView.showQQ( "body_04.png", pos )
            her "Вам нужно проследить за этим, сэр."
            #__#hide screen hermione_main                                                                                                                                                                                   #HERMIONE
            #__#with d3                                                                                                                                                                                                                        #HERMIONE
            $herView.hideQQ()
            #__#$ h_body = "03_hp/13_hermione_main/body_03.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
            #__#show screen hermione_main                                                                                                                                                                                 #HERMIONE
            #__#with d3                                                                                                                                                                                                                        #HERMIONE
            $herView.showQQ( "body_03.png", pos )
            
        elif one_of_ten == 3:
            #__#hide screen hermione_main                                                                                                                                                                                   #HERMIONE
            #__#with d3                                                                                                                                                                                                                        #HERMIONE
            $herView.hideQQ()
            #__#$ h_body = "03_hp/13_hermione_main/body_10.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
            #__#show screen hermione_main                                                                                                                                                                                 #HERMIONE
            #__#with d3                                                                                                                                                                                                                        #HERMIONE
            $herView.showQQ( "body_10.png", pos )
            her "Яица Эшвендэра, корень розы, лунный камень..."
            #__#hide screen hermione_main                                                                                                                                                                                   #HERMIONE
            #__#with d3                                                                                                                                                                                                                        #HERMIONE
            $herView.hideQQ()
            #__#$ h_body = "03_hp/13_hermione_main/body_11.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
            #__#show screen hermione_main                                                                                                                                                                                 #HERMIONE
            #__#with d3                                                                                                                                                                                                                        #HERMIONE
            $herView.showQQ( "body_11.png", pos )
            her "Ах? Я опять размышляла в слух?"
            #__#hide screen hermione_main                                                                                                                                                                                   #HERMIONE
            #__#with d3                                                                                                                                                                                                                        #HERMIONE
            $herView.hideQQ()
            #__#$ h_body = "03_hp/13_hermione_main/body_24.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
            #__#show screen hermione_main                                                                                                                                                                                 #HERMIONE
            #__#with d3                                                                                                                                                                                                                        #HERMIONE
            $herView.showQQ( "body_24.png", pos )
            her "Извините..."
            #__#hide screen hermione_main                                                                                                                                                                                   #HERMIONE
            #__#with d3                                                                                                                                                                                                                        #HERMIONE
            $herView.hideQQ()
            #__#$ h_body = "03_hp/13_hermione_main/body_13.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
            #__#show screen hermione_main                                                                                                                                                                                 #HERMIONE
            #__#with d3                                                                                                                                                                                                                        #HERMIONE
            $herView.showQQ( "body_13.png", pos )
            her "Просто скоро снова тест..."

        elif one_of_ten == 4:
            #__#hide screen hermione_main                                                                                                                                                                                   #HERMIONE
            #__#with d3                                                                                                                                                                                                                        #HERMIONE
            $herView.hideQQ()
            #__#$ h_body = "03_hp/13_hermione_main/body_77.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
            #__#show screen hermione_main                                                                                                                                                                                 #HERMIONE
            #__#with d3                                                                                                                                                                                                                        #HERMIONE
            $herView.showQQ( "body_77.png", pos )
            her "Я ненавижу весь факультет Слизерина всем своим сердцем, сэр."
            
        elif one_of_ten == 5:
            #__#hide screen hermione_main                                                                                                                                                                                   #HERMIONE
            #__#with d3                                                                                                                                                                                                                        #HERMIONE
            $herView.hideQQ()
            #__#$ h_body = "03_hp/13_hermione_main/body_16.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
            #__#show screen hermione_main                                                                                                                                                                                 #HERMIONE
            #__#with d3                                                                                                                                                                                                                        #HERMIONE
            $herView.showQQ( "body_16.png", pos )
            her "Хогвартс стал для меня новым домом в последнее время..."
            #__#hide screen hermione_main                                                                                                                                                                                   #HERMIONE
            #__#with d3                                                                                                                                                                                                                        #HERMIONE
            $herView.hideQQ()
            #__#$ h_body = "03_hp/13_hermione_main/body_71.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
            #__#show screen hermione_main                                                                                                                                                                                 #HERMIONE
            #__#with d3                                                                                                                                                                                                                        #HERMIONE
            $herView.showQQ( "body_71.png", pos )
            her "Иногда я даже не скучаю по родителям..."
            #__#hide screen hermione_main                                                                                                                                                                                   #HERMIONE
            #__#with d3                                                                                                                                                                                                                        #HERMIONE
            $herView.hideQQ()
            #__#$ h_body = "03_hp/13_hermione_main/body_18.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
            #__#show screen hermione_main                                                                                                                                                                                 #HERMIONE
            #__#with d3                                                                                                                                                                                                                        #HERMIONE
            $herView.showQQ( "body_18.png", pos )
            her "Если подумать я не скучаю по ним совсем..."
            #__#hide screen hermione_main                                                                                                                                                                                   #HERMIONE
            #__#with d3                                                                                                                                                                                                                        #HERMIONE
            $herView.hideQQ()
            #__#$ h_body = "03_hp/13_hermione_main/body_118.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
            #__#show screen hermione_main                                                                                                                                                                                 #HERMIONE
            #__#with d3                                                                                                                                                                                                                        #HERMIONE
            $herView.showQQ( "body_118.png", pos )
            her "Я ужасная дочь..."

        elif one_of_ten == 6:
            #__#hide screen hermione_main                                                                                                                                                                                   #HERMIONE
            #__#with d3                                                                                                                                                                                                                        #HERMIONE
            $herView.hideQQ()
            #__#$ h_body = "03_hp/13_hermione_main/body_70.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
            #__#show screen hermione_main                                                                                                                                                                                 #HERMIONE
            #__#with d3                                                                                                                                                                                                                        #HERMIONE
            $herView.showQQ( "body_70.png", pos )
            her "*Зевок!* Я прочитала о технике которая помогает сократить сон на половину..."
            #__#hide screen hermione_main                                                                                                                                                                                   #HERMIONE
            #__#with d3                                                                                                                                                                                                                        #HERMIONE
            $herView.hideQQ()
            #__#$ h_body = "03_hp/13_hermione_main/body_73.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
            #__#show screen hermione_main                                                                                                                                                                                 #HERMIONE
            #__#with d3                                                                                                                                                                                                                        #HERMIONE
            $herView.showQQ( "body_73.png", pos )
            her "Но кажется она не работает.... *Зевок!*"

        elif one_of_ten == 7:
            #__#hide screen hermione_main                                                                                                                                                                                   #HERMIONE
            #__#with d3                                                                                                                                                                                                                        #HERMIONE
            $herView.hideQQ()
            #__#$ h_body = "03_hp/13_hermione_main/body_04.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
            #__#show screen hermione_main                                                                                                                                                                                 #HERMIONE
            #__#with d3                                                                                                                                                                                                                        #HERMIONE
            $herView.showQQ( "body_04.png", pos )
            her "Даже когда я закончу Хогвартс я буду стараться совершенствоваться."
            #__#hide screen hermione_main                                                                                                                                                                                   #HERMIONE
            #__#with d3                                                                                                                                                                                                                        #HERMIONE
            $herView.hideQQ()
            #__#$ h_body = "03_hp/13_hermione_main/body_02.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
            #__#show screen hermione_main                                                                                                                                                                                 #HERMIONE
            #__#with d3                                                                                                                                                                                                                        #HERMIONE
            $herView.showQQ( "body_02.png", pos )
            her "Если я отдам себя всю этому миру он станет лучше, я знаю это!"
            #__#hide screen hermione_main                                                                                                                                                                                   #HERMIONE
            #__#with d3                                                                                                                                                                                                                        #HERMIONE
            $herView.hideQQ()
            #__#$ h_body = "03_hp/13_hermione_main/body_03.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
            #__#show screen hermione_main                                                                                                                                                                                 #HERMIONE
            #__#with d3                                                                                                                                                                                                                        #HERMIONE
            $herView.showQQ( "body_03.png", pos )
            
        elif one_of_ten == 8:
            #__#hide screen hermione_main                                                                                                                                                                                   #HERMIONE
            #__#with d3                                                                                                                                                                                                                        #HERMIONE
            $herView.hideQQ()
            #__#$ h_body = "03_hp/13_hermione_main/body_11.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
            #__#show screen hermione_main                                                                                                                                                                                 #HERMIONE
            #__#with d3                                                                                                                                                                                                                        #HERMIONE
            $herView.showQQ( "body_11.png", pos )
            her "Мне кажется что этот год будет важнейшим в моей жизни..."
            #__#hide screen hermione_main                                                                                                                                                                                   #HERMIONE
            #__#with d3                                                                                                                                                                                                                        #HERMIONE
            $herView.hideQQ()
            #__#$ h_body = "03_hp/13_hermione_main/body_13.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
            #__#show screen hermione_main                                                                                                                                                                                 #HERMIONE
            #__#with d3                                                                                                                                                                                                                        #HERMIONE
            $herView.showQQ( "body_13.png", pos )
  
        elif one_of_ten == 9:
            #__#hide screen hermione_main                                                                                                                                                                                   #HERMIONE
            #__#with d3                                                                                                                                                                                                                        #HERMIONE
            $herView.hideQQ()
            #__#$ h_body = "03_hp/13_hermione_main/body_04.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
            #__#show screen hermione_main                                                                                                                                                                                 #HERMIONE
            #__#with d3                                                                                                                                                                                                                        #HERMIONE
            $herView.showQQ( "body_04.png", pos )
            her "Некоторые школьные корридоры пыльные и грязные..."
            her "Пожалуйста позаботьтесь об этом, сэр..."
            #__#hide screen hermione_main                                                                                                                                                                                   #HERMIONE
            #__#with d3                                                                                                                                                                                                                        #HERMIONE
            $herView.hideQQ()
            #__#$ h_body = "03_hp/13_hermione_main/body_03.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
            #__#show screen hermione_main                                                                                                                                                                                 #HERMIONE
            #__#with d3                                                                                                                                                                                                                        #HERMIONE
            $herView.showQQ( "body_03.png", pos )
            
        elif one_of_ten == 10:
            #__#hide screen hermione_main                                                                                                                                                                                   #HERMIONE
            #__#with d3                                                                                                                                                                                                                        #HERMIONE
            $herView.hideQQ()
            #__#$ h_body = "03_hp/13_hermione_main/body_14.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
            #__#show screen hermione_main                                                                                                                                                                                 #HERMIONE
            #__#with d3
            $herView.showQQ( "body_14.png", pos )
            her "Я читала об этом. Называется \"Маховик времени\"."            
            her "Он позволяет владельцу контролировать время..."
            #__#hide screen hermione_main                                                                                                                                                                                   #HERMIONE
            #__#with d3                                                                                                                                                                                                                        #HERMIONE
            $herView.hideQQ()
            #__#$ h_body = "03_hp/13_hermione_main/body_16.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
            #__#show screen hermione_main                                                                                                                                                                                 #HERMIONE
            #__#with d3                                                                                                                                                                                                                        #HERMIONE
            $herView.showQQ( "body_16.png", pos )
            her "Если бы он был у меня, то я бы творила чудеса со своим расписанием..."
            #__#hide screen hermione_main                                                                                                                                                                                   #HERMIONE
            #__#with d3                                                                                                                                                                                                                        #HERMIONE
            $herView.hideQQ()
            #__#$ h_body = "03_hp/13_hermione_main/body_17.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
            #__#show screen hermione_main                                                                                                                                                                                 #HERMIONE
            #__#with d3                                                                                                                                                                                                                        #HERMIONE
            $herView.showQQ( "body_17.png", pos )


    if whoring >= 9 and whoring <= 11: # WHORING LEVEL 04.
        if one_of_ten == 1:
            #__#hide screen hermione_main                                                                                                                                                                                   #HERMIONE
            #__#with d3                                                                                                                                                                                                                        #HERMIONE
            $herView.hideQQ()
            #__#$ h_body = "03_hp/13_hermione_main/body_11.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
            #__#show screen hermione_main                                                                                                                                                                                 #HERMIONE
            #__#with d3                                                                                                                                                                                                                        #HERMIONE
            $herView.showQQ( "body_11.png", pos )
            her "Мое \"общество по защите прав мужчин\" последнее время теряет популярность..."
            #__#hide screen hermione_main                                                                                                                                                                                   #HERMIONE
            #__#with d3                                                                                                                                                                                                                        #HERMIONE
            $herView.hideQQ()
            #__#$ h_body = "03_hp/13_hermione_main/body_12.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
            #__#show screen hermione_main                                                                                                                                                                                 #HERMIONE
            #__#with d3                                                                                                                                                                                                                        #HERMIONE
            $herView.showQQ( "body_12.png", pos )
            her "Похоже это никого не волнует!"

        elif one_of_ten == 2:
            #__#hide screen hermione_main                                                                                                                                                                                   #HERMIONE
            #__#with d3                                                                                                                                                                                                                        #HERMIONE
            $herView.hideQQ()
            #__#$ h_body = "03_hp/13_hermione_main/body_04.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
            #__#show screen hermione_main                                                                                                                                                                                 #HERMIONE
            #__#with d3                                                                                                                                                                                                                        #HERMIONE
            $herView.showQQ( "body_04.png", pos )
            her "Спасибо вам за все эти очки, сэр."
            #__#hide screen hermione_main                                                                                                                                                                                   #HERMIONE
            #__#with d3                                                                                                                                                                                                                        #HERMIONE
            $herView.hideQQ()
            #__#$ h_body = "03_hp/13_hermione_main/body_07.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
            #__#show screen hermione_main                                                                                                                                                                                 #HERMIONE
            #__#with d3                                                                                                                                                                                                                        #HERMIONE
            $herView.showQQ( "body_07.png", pos )
            her "Некоторые, конечно, достались весьма странным образом, но ..."
            #__#hide screen hermione_main                                                                                                                                                                                   #HERMIONE
            #__#with d3                                                                                                                                                                                                                        #HERMIONE
            $herView.hideQQ()
            #__#$ h_body = "03_hp/13_hermione_main/body_04.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
            #__#show screen hermione_main                                                                                                                                                                                 #HERMIONE
            #__#with d3                                                                                                                                                                                                                        #HERMIONE
            $herView.showQQ( "body_04.png", pos )
            her "Но это не важно, до тех пор, пока это дает \"Гриффиндору\" преимущество в гонке со \"Слизерином\"."
            #__#hide screen hermione_main                                                                                                                                                                                   #HERMIONE
            #__#with d3                                                                                                                                                                                                                        #HERMIONE
            $herView.hideQQ()
            #__#$ h_body = "03_hp/13_hermione_main/body_03.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
            #__#show screen hermione_main                                                                                                                                                                                 #HERMIONE
            #__#with d3                                                                                                                                                                                                                        #HERMIONE
            $herView.showQQ( "body_03.png", pos )
            
        elif one_of_ten == 3:
            #__#hide screen hermione_main                                                                                                                                                                                   #HERMIONE
            #__#with d3                                                                                                                                                                                                                        #HERMIONE
            $herView.hideQQ()
            #__#$ h_body = "03_hp/13_hermione_main/body_77.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
            #__#show screen hermione_main                                                                                                                                                                                 #HERMIONE
            #__#with d3                                                                                                                                                                                                                        #HERMIONE
            $herView.showQQ( "body_77.png", pos )
            her "Квиддич это глупо!"
            #__#hide screen hermione_main                                                                                                                                                                                   #HERMIONE
            #__with d3                                                                                                                                                                                                                        #HERMIONE
            $herView.hideQQ()
            #__#$ h_body = "03_hp/13_hermione_main/body_17.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
            #__#show screen hermione_main                                                                                                                                                                                 #HERMIONE
            #__#with d3                                                                                                                                                                                                                        #HERMIONE
            $herView.showQQ( "body_17.png", pos )
            her "Вот. Я сказала это."
            
        elif one_of_ten == 4:
            #__#hide screen hermione_main                                                                                                                                                                                   #HERMIONE
            #__#with d3                                                                                                                                                                                                                        #HERMIONE
            $herView.hideQQ()
            #__#$ h_body = "03_hp/13_hermione_main/body_02.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
            #__#show screen hermione_main                                                                                                                                                                                 #HERMIONE
            #__#with d3                                                                                                                                                                                                                        #HERMIONE
            $herView.showQQ( "body_02.png", pos )
            her "Сэр, есть кое-что, что вы должны знать о профессоре Снейпе..."
            #__#hide screen hermione_main                                                                                                                                                                                   #HERMIONE
            #__#with d3                                                                                                                                                                                                                        #HERMIONE
            $herView.hideQQ()
            #__#$ h_body = "03_hp/13_hermione_main/body_10.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
            #__#show screen hermione_main                                                                                                                                                                                 #HERMIONE
            #__#with d3                                                                                                                                                                                                                        #HERMIONE
            $herView.showQQ( "body_10.png", pos )
            her "................."
            #__#hide screen hermione_main                                                                                                                                                                                   #HERMIONE
            #__#with d3                                                                                                                                                                                                                        #HERMIONE
            $herView.hideQQ()
            #__#$ h_body = "03_hp/13_hermione_main/body_09.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
            #__#show screen hermione_main                                                                                                                                                                                 #HERMIONE
            #__#with d3                                                                                                                                                                                                                        #HERMIONE
            $herView.showQQ( "body_09.png", pos )
            her "........................."
            #__#hide screen hermione_main                                                                                                                                                                                   #HERMIONE
            #__#with d3                                                                                                                                                                                                                        #HERMIONE
            $herView.hideQQ()
            #__#$ h_body = "03_hp/13_hermione_main/body_04.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
            #__#show screen hermione_main                                                                                                                                                                                 #HERMIONE
            #__#with d3                                                                                                                                                                                                                        #HERMIONE
            $herView.showQQ( "body_04.png", pos )
            her "Ух... Ничего..."
            #__#hide screen hermione_main                                                                                                                                                                                   #HERMIONE
            #__#with d3                                                                                                                                                                                                                        #HERMIONE
            $herView.hideQQ()
            #__#$ h_body = "03_hp/13_hermione_main/body_03.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
            #__#show screen hermione_main                                                                                                                                                                                 #HERMIONE
            #__#with d3                                                                                                                                                                                                                        #HERMIONE
            $herView.showQQ( "body_03.png", pos )
 
        elif one_of_ten == 5:
            #__#hide screen hermione_main                                                                                                                                                                                   #HERMIONE
            #__#with d3                                                                                                                                                                                                                        #HERMIONE
            $herView.hideQQ()
            #__#$ h_body = "03_hp/13_hermione_main/body_04.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
            #__#show screen hermione_main                                                                                                                                                                                 #HERMIONE
            #__#with d3                                                                                                                                                                                                                        #HERMIONE
            $herView.showQQ( "body_04.png", pos )
            her "Некоторые из \"Слизеринских\" девок в последнее время посреди дня продаются за очки..."
            #__#hide screen hermione_main                                                                                                                                                                                   #HERMIONE
            #__#with d3                                                                                                                                                                                                                        #HERMIONE
            $herView.hideQQ()
            #__#$ h_body = "03_hp/13_hermione_main/body_02.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
            #__#show screen hermione_main                                                                                                                                                                                 #HERMIONE
            #__#with d3                                                                                                                                                                                                                        #HERMIONE
            $herView.showQQ( "body_02.png", pos )
            her "Вы должны положить этому конец, сэр."
            #__#hide screen hermione_main                                                                                                                                                                                   #HERMIONE
            #__#with d3                                                                                                                                                                                                                        #HERMIONE
            $herView.hideQQ()
            #__#$ h_body = "03_hp/13_hermione_main/body_69.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
            #__#show screen hermione_main                                                                                                                                                                                 #HERMIONE
            #__#with d3                                                                                                                                                                                                                        #HERMIONE
            $herView.showQQ( "body_69.png", pos )
            her "(Я едва поспеваю за ними...)"

        elif one_of_ten == 6:
            #__#hide screen hermione_main                                                                                                                                                                                   #HERMIONE
            #__#with d3                                                                                                                                                                                                                        #HERMIONE
            $herView.hideQQ()
            #__#$ h_body = "03_hp/13_hermione_main/body_10.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
            #__#show screen hermione_main                                                                                                                                                                                 #HERMIONE
            #__#with d3                                                                                                                                                                                                                        #HERMIONE
            $herView.showQQ( "body_10.png", pos )
            her "Жизнь устроена очень странно..."
            #__#hide screen hermione_main                                                                                                                                                                                   #HERMIONE
            #__#with d3                                                                                                                                                                                                                        #HERMIONE
            $herView.hideQQ()
            #__#$ h_body = "03_hp/13_hermione_main/body_08.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
            #__#show screen hermione_main                                                                                                                                                                                 #HERMIONE
            #__#with d3                                                                                                                                                                                                                        #HERMIONE
            $herView.showQQ( "body_08.png", pos )
            her "Вы согласны, сэр?"
            #__#hide screen hermione_main                                                                                                                                                                                   #HERMIONE
            #__#with d3                                                                                                                                                                                                                        #HERMIONE
            $herView.hideQQ()
            #__#$ h_body = "03_hp/13_hermione_main/body_13.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
            #__#show screen hermione_main                                                                                                                                                                                 #HERMIONE
            #__#with d3                                                                                                                                                                                                                        #HERMIONE
            $herView.showQQ( "body_13.png", pos )

        elif one_of_ten == 7:
            #__#hide screen hermione_main                                                                                                                                                                                   #HERMIONE
            #__#with d3                                                                                                                                                                                                                        #HERMIONE
            $herView.hideQQ()
            #__#$ h_body = "03_hp/13_hermione_main/body_76.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
            #__#show screen hermione_main                                                                                                                                                                                 #HERMIONE
            #__#with d3                                                                                                                                                                                                                        #HERMIONE
            $herView.showQQ( "body_76.png", pos )
            her "Слизеринцы..."
            #__#hide screen hermione_main                                                                                                                                                                                   #HERMIONE
            #__#with d3                                                                                                                                                                                                                        #HERMIONE
            $herView.hideQQ()
            #__#$ h_body = "03_hp/13_hermione_main/body_77.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
            #__#show screen hermione_main                                                                                                                                                                                 #HERMIONE
            #__#with d3                                                                                                                                                                                                                        #HERMIONE
            $herView.showQQ( "body_77.png", pos )
            
        elif one_of_ten == 8:
            #__#hide screen hermione_main                                                                                                                                                                                   #HERMIONE
            #__#with d3                                                                                                                                                                                                                        #HERMIONE
            $herView.hideQQ()
            #__#$ h_body = "03_hp/13_hermione_main/body_10.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
            #__#show screen hermione_main                                                                                                                                                                                 #HERMIONE
            #__#with d3                                                                                                                                                                                                                        #HERMIONE
            $herView.showQQ( "body_10.png", pos )
            her "В последнее время я так много времени провела в вашем кабинете..."
            #__#hide screen hermione_main                                                                                                                                                                                   #HERMIONE
            #__#with d3                                                                                                                                                                                                                        #HERMIONE
            $herView.hideQQ()
            #__#$ h_body = "03_hp/13_hermione_main/body_11.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
            #__#show screen hermione_main                                                                                                                                                                                 #HERMIONE
            #__#with d3                                                                                                                                                                                                                        #HERMIONE
            $herView.showQQ( "body_11.png", pos )
            her "Если я была неосторожна, некоторые могли бы заметить и подумать, что я стала вашим питомцем..."
            #__#hide screen hermione_main                                                                                                                                                                                   #HERMIONE
            #__#with d3                                                                                                                                                                                                                        #HERMIONE
            $herView.hideQQ()
            #__#$ h_body = "03_hp/13_hermione_main/body_34.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
            #__#show screen hermione_main                                                                                                                                                                                 #HERMIONE
            #__#with d3                                                                                                                                                                                                                        #HERMIONE
            $herView.showQQ( "body_34.png", pos )
            her "Я хотела сказать, любимчиком..."
            #__#hide screen hermione_main                                                                                                                                                                                   #HERMIONE
            #__#with d3                                                                                                                                                                                                                        #HERMIONE
            $herView.hideQQ()
            #__#$ h_body = "03_hp/13_hermione_main/body_33.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
            #__#show screen hermione_main                                                                                                                                                                                 #HERMIONE
            #__#with d3                                                                                                                                                                                                                        #HERMIONE
            $herView.showQQ( "body_33.png", pos )

        elif one_of_ten == 9:
            #__#hide screen hermione_main                                                                                                                                                                                   #HERMIONE
            #__#with d3                                                                                                                                                                                                                        #HERMIONE
            $herView.hideQQ()
            #__#$ h_body = "03_hp/13_hermione_main/body_02.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
            #__#show screen hermione_main                                                                                                                                                                                 #HERMIONE
            #__#with d3                                                                                                                                                                                                                        #HERMIONE
            $herView.showQQ( "body_02.png", pos )
            her "Мой любимый цвет?"
            #__#hide screen hermione_main                                                                                                                                                                                   #HERMIONE
            #__#with d3                                                                                                                                                                                                                        #HERMIONE
            $herView.hideQQ()
            #__#$ h_body = "03_hp/13_hermione_main/body_02.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
            #__#show screen hermione_main                                                                                                                                                                                 #HERMIONE
            #__#with d3                                                                                                                                                                                                                        #HERMIONE
            $herView.showQQ( "body_02.png", pos )
            her "Алый и золотой, конечно же!"
            #__#hide screen hermione_main                                                                                                                                                                                   #HERMIONE
            #__#with d3                                                                                                                                                                                                                        #HERMIONE
            $herView.hideQQ()
            #__#$ h_body = "03_hp/13_hermione_main/body_03.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
            #__#show screen hermione_main                                                                                                                                                                                 #HERMIONE
            #__#with d3                                                                                                                                                                                                                        #HERMIONE
            $herView.showQQ( "body_03.png", pos )
       
        elif one_of_ten == 10:
            #__#hide screen hermione_main                                                                                                                                                                                   #HERMIONE
            #__#with d3                                                                                                                                                                                                                        #HERMIONE
            $herView.hideQQ()
            #__#$ h_body = "03_hp/13_hermione_main/body_10.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
            #__#show screen hermione_main                                                                                                                                                                                 #HERMIONE
            #__#with d3                                                                                                                                                                                                                        #HERMIONE
            $herView.showQQ( "body_10.png", pos )
            her "Странно, что мои лучшие друзья это мальчики?"
            #__#hide screen hermione_main                                                                                                                                                                                   #HERMIONE
            #__#with d3                                                                                                                                                                                                                        #HERMIONE
            $herView.hideQQ()
            #__#$ h_body = "03_hp/13_hermione_main/body_01.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
            #__#show screen hermione_main                                                                                                                                                                                 #HERMIONE
            #__#with d3                                                                                                                                                                                                                        #HERMIONE
            $herView.showQQ( "body_01.png", pos )
        

        
    if whoring >= 12 and whoring <= 14: # WHORING LEVEL 05.
        if one_of_ten == 1:
            #__#hide screen hermione_main                                                                                                                                                                                   #HERMIONE
            #__#with d3                                                                                                                                                                                                                        #HERMIONE
            $herView.hideQQ()
            #__#$ h_body = "03_hp/13_hermione_main/body_07.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
            #__#show screen hermione_main                                                                                                                                                                                 #HERMIONE
            #__#with d3                                                                                                                                                                                                                        #HERMIONE
            $herView.showQQ( "body_07.png", pos )
            her "Сэр, при всем уважении..."
            her "Профессор Снейп распускает руки!"
            #__#hide screen hermione_main                                                                                                                                                                                   #HERMIONE
            #__#with d3                                                                                                                                                                                                                        #HERMIONE
            $herView.hideQQ()
            #__#$ h_body = "03_hp/13_hermione_main/body_11.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
            #__#show screen hermione_main                                                                                                                                                                                 #HERMIONE
            #__#with d3                                                                                                                                                                                                                        #HERMIONE
            $herView.showQQ( "body_11.png", pos )
            her "Вы должны сделать что-то."
            #__#hide screen hermione_main                                                                                                                                                                                   #HERMIONE
            #__#with d3                                                                                                                                                                                                                        #HERMIONE
            $herView.hideQQ()
            #__#$ h_body = "03_hp/13_hermione_main/body_03.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
            #__#show screen hermione_main                                                                                                                                                                                 #HERMIONE
            #__#with d3                                                                                                                                                                                                                        #HERMIONE
            $herView.showQQ( "body_03.png", pos )

        elif one_of_ten == 2:
            #__#hide screen hermione_main                                                                                                                                                                                   #HERMIONE
            #__#with d3                                                                                                                                                                                                                        #HERMIONE
            $herView.hideQQ()
            #__#$ h_body = "03_hp/13_hermione_main/body_04.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
            #__#show screen hermione_main                                                                                                                                                                                 #HERMIONE
            #__#with d3                                                                                                                                                                                                                        #HERMIONE
            $herView.showQQ( "body_04.png", pos )
            her "Я готова пойти на все, лишь бы \"Гриффиндор\" лидировал..."
            her "Но это не значит, что я с удовольствием отдамся вам за очки для факультета."
            #__#hide screen hermione_main                                                                                                                                                                                   #HERMIONE
            #__#with d3                                                                                                                                                                                                                        #HERMIONE
            $herView.hideQQ()
            #__#$ h_body = "03_hp/13_hermione_main/body_118.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
            #__#show screen hermione_main                                                                                                                                                                                 #HERMIONE
            #__#with d3                                                                                                                                                                                                                        #HERMIONE
            $herView.showQQ( "body_118.png", pos )
            her "{size=-4}(Как какая-то шлюха-ведьма...){/size}"

        elif one_of_ten == 3:
            #__#hide screen hermione_main                                                                                                                                                                                   #HERMIONE
            #__#with d3                                                                                                                                                                                                                        #HERMIONE
            $herView.hideQQ()
            #__#$ h_body = "03_hp/13_hermione_main/body_79.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
            #__#show screen hermione_main                                                                                                                                                                                 #HERMIONE
            #__#with d3                                                                                                                                                                                                                        #HERMIONE
            $herView.showQQ( "body_79.png", pos )
            her "Что на сегодня, сэр?"
            
        elif one_of_ten == 4:
            #__#hide screen hermione_main                                                                                                                                                                                   #HERMIONE
            #__#with d3                                                                                                                                                                                                                        #HERMIONE
            $herView.hideQQ()
            #__#$ h_body = "03_hp/13_hermione_main/body_11.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
            #__#show screen hermione_main                                                                                                                                                                                 #HERMIONE
            #__#with d3                                                                                                                                                                                                                        #HERMIONE
            $herView.showQQ( "body_11.png", pos )
            her "Раньше я училась лучше, чем сейчас..."
            #__#hide screen hermione_main                                                                                                                                                                                   #HERMIONE
            #__#with d3                                                                                                                                                                                                                        #HERMIONE
            $herView.hideQQ()
            #__#$ h_body = "03_hp/13_hermione_main/body_10.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
            #__#show screen hermione_main                                                                                                                                                                                 #HERMIONE
            #__#with d3                                                                                                                                                                                                                        #HERMIONE
            $herView.showQQ( "body_10.png", pos )
            her "Я теряю мотивацию?"
            #__#hide screen hermione_main                                                                                                                                                                                   #HERMIONE
            #__#with d3                                                                                                                                                                                                                        #HERMIONE
            $herView.hideQQ()
            #__#$ h_body = "03_hp/13_hermione_main/body_13.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
            #__#show screen hermione_main                                                                                                                                                                                 #HERMIONE
            #__#with d3                                                                                                                                                                                                                        #HERMIONE
            $herView.showQQ( "body_13.png", pos )

        elif one_of_ten == 5:
            #__#hide screen hermione_main                                                                                                                                                                                   #HERMIONE
            #__#with d3                                                                                                                                                                                                                        #HERMIONE
            $herView.hideQQ()
            #__#$ h_body = "03_hp/13_hermione_main/body_08.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
            #__#show screen hermione_main                                                                                                                                                                                 #HERMIONE
            #__#with d3                                                                                                                                                                                                                        #HERMIONE
            $herView.showQQ( "body_08.png", pos )
            her "Мой нелюбимый предмет?"
            #__#hide screen hermione_main                                                                                                                                                                                   #HERMIONE
            #__#with d3                                                                                                                                                                                                                        #HERMIONE
            $herView.hideQQ()
            #__#$ h_body = "03_hp/13_hermione_main/body_09.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
            #__#show screen hermione_main                                                                                                                                                                                 #HERMIONE
            #__#with d3                                                                                                                                                                                                                        #HERMIONE
            $herView.showQQ( "body_09.png", pos )
            her "Гадание." 
            
        elif one_of_ten == 6:
            #__#hide screen hermione_main                                                                                                                                                                                   #HERMIONE
            #__#with d3                                                                                                                                                                                                                        #HERMIONE
            $herView.hideQQ()
            #__#$ h_body = "03_hp/13_hermione_main/body_14.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
            #__#show screen hermione_main                                                                                                                                                                                 #HERMIONE
            #__#with d3                                                                                                                                                                                                                        #HERMIONE
            $herView.showQQ( "body_14.png", pos )
            her "Мой отец сказал: \"Магия это наука, которую мы не можем понять\"."
            #__#hide screen hermione_main                                                                                                                                                                                   #HERMIONE
            #__#with d3                                                                                                                                                                                                                        #HERMIONE
            $herView.hideQQ()
            #__#$ h_body = "03_hp/13_hermione_main/body_10.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
            #__#show screen hermione_main                                                                                                                                                                                 #HERMIONE
            #__#with d3                                                                                                                                                                                                                        #HERMIONE
            $herView.showQQ( "body_10.png", pos )
            her "Он, конечно же, мог ошибаться..."
            #__#hide screen hermione_main                                                                                                                                                                                   #HERMIONE
            #__#with d3                                                                                                                                                                                                                        #HERMIONE
            $herView.hideQQ()
            #__#$ h_body = "03_hp/13_hermione_main/body_13.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
            #__#show screen hermione_main                                                                                                                                                                                 #HERMIONE
            #__#with d3                                                                                                                                                                                                                        #HERMIONE
            $herView.showQQ( "body_13.png", pos )
            
        elif one_of_ten == 7:
            #__#hide screen hermione_main                                                                                                                                                                                   #HERMIONE
            #__#with d3                                                                                                                                                                                                                        #HERMIONE
            $herView.hideQQ()
            #__#$ h_body = "03_hp/13_hermione_main/body_04.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
            #__#show screen hermione_main                                                                                                                                                                                 #HERMIONE
            #__#with d3                                                                                                                                                                                                                        #HERMIONE
            $herView.showQQ( "body_04.png", pos )
            her "Несмотря ни на что..."
            #__#hide screen hermione_main                                                                                                                                                                                   #HERMIONE
            #__#with d3                                                                                                                                                                                                                        #HERMIONE
            $herView.hideQQ()
            #__#$ h_body = "03_hp/13_hermione_main/body_10.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
            #__#show screen hermione_main                                                                                                                                                                                 #HERMIONE
            #__#with d3                                                                                                                                                                                                                        #HERMIONE
            $herView.showQQ( "body_10.png", pos )
            her "Я благодарна, что вы позволяете мне получать дополнительные очки..."
            #__#hide screen hermione_main                                                                                                                                                                                   #HERMIONE
            #__#with d3                                                                                                                                                                                                                        #HERMIONE
            $herView.hideQQ()
            #__#$ h_body = "03_hp/13_hermione_main/body_13.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
            #__#show screen hermione_main                                                                                                                                                                                 #HERMIONE
            #__#with d3                                                                                                                                                                                                                        #HERMIONE
            $herView.showQQ( "body_13.png", pos )
            
        elif one_of_ten == 8:
            #__#hide screen hermione_main                                                                                                                                                                                   #HERMIONE
            #__#with d3                                                                                                                                                                                                                        #HERMIONE
            $herView.hideQQ()
            #__#$ h_body = "03_hp/13_hermione_main/body_14.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
            #__#show screen hermione_main                                                                                                                                                                                 #HERMIONE
            #__#with d3                                                                                                                                                                                                                        #HERMIONE
            $herView.showQQ( "body_14.png", pos )
            her "Сегодня довольно холодно, не так ли?"
            #__#hide screen hermione_main                                                                                                                                                                                   #HERMIONE
            #__#with d3                                                                                                                                                                                                                        #HERMIONE
            $herView.hideQQ()
            #__#$ h_body = "03_hp/13_hermione_main/body_15.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
            #__#show screen hermione_main                                                                                                                                                                                 #HERMIONE
            #__#with d3                                                                                                                                                                                                                        #HERMIONE
            $herView.showQQ( "body_15.png", pos )
            
        elif one_of_ten == 9:
            #__#hide screen hermione_main                                                                                                                                                                                   #HERMIONE
            #__#with d3                                                                                                                                                                                                                        #HERMIONE
            $herView.hideQQ()
            #__#$ h_body = "03_hp/13_hermione_main/body_14.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
            #__#show screen hermione_main                                                                                                                                                                                 #HERMIONE
            #__#with d3                                                                                                                                                                                                                        #HERMIONE
            $herView.showQQ( "body_14.png", pos )
            her "\"Осенний бал\" совсем скоро..."
            #__#hide screen hermione_main                                                                                                                                                                                   #HERMIONE
            #__#with d3                                                                                                                                                                                                                        #HERMIONE
            $herView.hideQQ()
            #__#$ h_body = "03_hp/13_hermione_main/body_15.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
            #__#show screen hermione_main                                                                                                                                                                                 #HERMIONE
            #__#with d3                                                                                                                                                                                                                        #HERMIONE
            $herView.showQQ( "body_15.png", pos )

        elif one_of_ten == 10:
            #__#hide screen hermione_main                                                                                                                                                                                   #HERMIONE
            #__#with d3                                                                                                                                                                                                                        #HERMIONE
            $herView.hideQQ()
            #__#$ h_body = "03_hp/13_hermione_main/body_10.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
            #__#show screen hermione_main                                                                                                                                                                                 #HERMIONE
            #__#with d3                                                                                                                                                                                                                        #HERMIONE
            $herView.showQQ( "body_10.png", pos )
            her "Люди врядли посетят наше \"общество по защите прав мужчин\" еще когда-либо..."
            #__#hide screen hermione_main                                                                                                                                                                                   #HERMIONE
            #__#with d3                                                                                                                                                                                                                        #HERMIONE
            $herView.hideQQ()
            #__#$ h_body = "03_hp/13_hermione_main/body_13.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
            #__#show screen hermione_main                                                                                                                                                                                 #HERMIONE
            #__#with d3                                                                                                                                                                                                                     
            $herView.showQQ( "body_13.png", pos )
    
    
    
    
    
        
    if whoring >= 15 and whoring <= 17:  # WHORING LEVEL 06.
        if one_of_ten == 1:
            hide screen hermione_main                                                                                                                                                                                   #HERMIONE
            with d3                                                                                                                                                                                                                        #HERMIONE
            $ h_body = "03_hp/13_hermione_main/body_87.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
            show screen hermione_main                                                                                                                                                                                 #HERMIONE
            with d3                                                                                                                                                                                                                        #HERMIONE
            her "Хотите, чтобы я показала вам свою грудь?"
            hide screen hermione_main                                                                                                                                                                                   #HERMIONE
            with d3                                                                                                                                                                                                                        #HERMIONE
            $ h_body = "03_hp/13_hermione_main/body_78.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
            show screen hermione_main                                                                                                                                                                                 #HERMIONE
            with d3                                                                                                                                                                                                                        #HERMIONE
            her "Да...Я хочу, чтобы вы использовали меня..."
            hide screen hermione_main                                                                                                                                                                                   #HERMIONE
            with d3                                                                                                                                                                                                                        #HERMIONE
            $ h_body = "03_hp/13_hermione_main/body_79.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
            show screen hermione_main                                                                                                                                                                                 #HERMIONE
            with d3                                                                                                                                                                                                                        #HERMIONE
            her "Вот настолько я самоотверженна!"
           
        elif one_of_ten == 2:
            hide screen hermione_main                                                                                                                                                                                   #HERMIONE
            with d3                                                                                                                                                                                                                        #HERMIONE
            $ h_body = "03_hp/13_hermione_main/body_14.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
            show screen hermione_main                                                                                                                                                                                 #HERMIONE
            with d3                                                                                                                                                                                                                        #HERMIONE
            her "Я не могу ничего поделать, но чувствую себя не очень, когда домовые эльфы стирают за мной вещи..."
            hide screen hermione_main                                                                                                                                                                                   #HERMIONE
            with d3                                                                                                                                                                                                                        #HERMIONE
            $ h_body = "03_hp/13_hermione_main/body_87.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
            show screen hermione_main                                                                                                                                                                                 #HERMIONE
            with d3                                                                                                                                                                                                                        #HERMIONE
            her "То есть, все эти пятна от спермы..."
            hide screen hermione_main                                                                                                                                                                                   #HERMIONE
            with d3                                                                                                                                                                                                                        #HERMIONE
            $ h_body = "03_hp/13_hermione_main/body_118.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
            show screen hermione_main                                                                                                                                                                                 #HERMIONE
            with d3                                                                                                                                                                                                                        #HERMIONE

        elif one_of_ten == 3:
            hide screen hermione_main                                                                                                                                                                                   #HERMIONE
            with d3                                                                                                                                                                                                                        #HERMIONE
            $ h_body = "03_hp/13_hermione_main/body_02.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
            show screen hermione_main                                                                                                                                                                                 #HERMIONE
            with d3                                                                                                                                                                                                                        #HERMIONE
            her "Не имеет значения, сколько раз вы спросите меня..."
            her "Ответ будет один и тот же..."
            hide screen hermione_main                                                                                                                                                                                   #HERMIONE
            with d3                                                                                                                                                                                                                        #HERMIONE
            $ h_body = "03_hp/13_hermione_main/body_47.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
            show screen hermione_main                                                                                                                                                                                 #HERMIONE
            with d3                                                                                                                                                                                                                        #HERMIONE
            her "У меня нет ничего, кроме обиды на \"Слизеринцев\"!"
            hide screen hermione_main                                                                                                                                                                                   #HERMIONE
            with d3                                                                                                                                                                                                                        #HERMIONE
            $ h_body = "03_hp/13_hermione_main/body_69.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
            show screen hermione_main                                                                                                                                                                                 #HERMIONE
            with d3                                                                                                                                                                                                                        #HERMIONE
        
        
        elif one_of_ten == 4:
            hide screen hermione_main                                                                                                                                                                                   #HERMIONE
            with d3                                                                                                                                                                                                                        #HERMIONE
            $ h_body = "03_hp/13_hermione_main/body_02.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
            show screen hermione_main                                                                                                                                                                                 #HERMIONE
            with d3                                                                                                                                                                                                                        #HERMIONE
            her "Когда я думаю обо всем, на что мне пришлось пойти в обмен на очки..."
            hide screen hermione_main                                                                                                                                                                                   #HERMIONE
            with d3                                                                                                                                                                                                                        #HERMIONE
            $ h_body = "03_hp/13_hermione_main/body_87.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
            show screen hermione_main                                                                                                                                                                                 #HERMIONE
            with d3                                                                                                                                                                                                                        #HERMIONE
            her "Я чувствую себя немного неловко..."
            hide screen hermione_main                                                                                                                                                                                   #HERMIONE
            with d3                                                                                                                                                                                                                        #HERMIONE
            $ h_body = "03_hp/13_hermione_main/body_120.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
            show screen hermione_main                                                                                                                                                                                 #HERMIONE
            with d3                                                                                                                                                                                                                        #HERMIONE
            her "Но так же я очень горжусь собой."
            
        elif one_of_ten == 5:
            hide screen hermione_main                                                                                                                                                                                   #HERMIONE
            with d3                                                                                                                                                                                                                        #HERMIONE
            $ h_body = "03_hp/13_hermione_main/body_14.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
            show screen hermione_main                                                                                                                                                                                 #HERMIONE
            with d3                                                                                                                                                                                                                        #HERMIONE
            her "До сих пор я посвящаю очень много времени обучению..."
            her "Но далеко не столько, как раньше..."
            hide screen hermione_main                                                                                                                                                                                   #HERMIONE
            with d3                                                                                                                                                                                                                        #HERMIONE
            $ h_body = "03_hp/13_hermione_main/body_11.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
            show screen hermione_main                                                                                                                                                                                 #HERMIONE
            with d3                                                                                                                                                                                                                        #HERMIONE
            her "Вообще мне теперь не очень то и нравится учиться..."
            hide screen hermione_main                                                                                                                                                                                   #HERMIONE
            with d3                                                                                                                                                                                                                        #HERMIONE
            $ h_body = "03_hp/13_hermione_main/body_13.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
            show screen hermione_main                                                                                                                                                                                 #HERMIONE
            with d3                                                                                                                                                                                                                        #HERMIONE
        
        elif one_of_ten == 6:
            hide screen hermione_main                                                                                                                                                                                   #HERMIONE
            with d3                                                                                                                                                                                                                        #HERMIONE
            $ h_body = "03_hp/13_hermione_main/body_04.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
            show screen hermione_main                                                                                                                                                                                 #HERMIONE
            with d3                                                                                                                                                                                                                        #HERMIONE
            her "Гриффиндор должен получить кубок в этому году!"
            hide screen hermione_main                                                                                                                                                                                   #HERMIONE
            with d3                                                                                                                                                                                                                        #HERMIONE
            $ h_body = "03_hp/13_hermione_main/body_118.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
            show screen hermione_main                                                                                                                                                                                 #HERMIONE
            with d3                                                                                                                                                                                                                        #HERMIONE
            her "{size=-4}(Даже если это будет стоить мне моей чести...){/size}"
            hide screen hermione_main                                                                                                                                                                                   #HERMIONE
            with d3                                                                                                                                                                                                                        #HERMIONE
            $ h_body = "03_hp/13_hermione_main/body_120.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
            show screen hermione_main                                                                                                                                                                                 #HERMIONE
            with d3                                                                                                                                                                                                                        #HERMIONE
           
           
        elif one_of_ten == 7:
            hide screen hermione_main                                                                                                                                                                                   #HERMIONE
            with d3                                                                                                                                                                                                                        #HERMIONE
            $ h_body = "03_hp/13_hermione_main/body_14.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
            show screen hermione_main                                                                                                                                                                                 #HERMIONE
            with d3                                                                                                                                                                                                                        #HERMIONE
            her "Я ничего не имею против осенней погоды..."
            hide screen hermione_main                                                                                                                                                                                   #HERMIONE
            with d3                                                                                                                                                                                                                        #HERMIONE
            $ h_body = "03_hp/13_hermione_main/body_16.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
            show screen hermione_main                                                                                                                                                                                 #HERMIONE
            with d3                                                                                                                                                                                                                        #HERMIONE
            her "Но мое любимое время года это зима."
            hide screen hermione_main                                                                                                                                                                                   #HERMIONE
            with d3                                                                                                                                                                                                                        #HERMIONE
            $ h_body = "03_hp/13_hermione_main/body_15.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
            show screen hermione_main                                                                                                                                                                                 #HERMIONE
            with d3                                                                                                                                                                                                                        #HERMIONE
        
        elif one_of_ten == 8:
            hide screen hermione_main                                                                                                                                                                                   #HERMIONE
            with d3                                                                                                                                                                                                                        #HERMIONE
            $ h_body = "03_hp/13_hermione_main/body_14.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
            show screen hermione_main                                                                                                                                                                                 #HERMIONE
            with d3                                                                                                                                                                                                                        #HERMIONE
            her "Я смотрю с высока на девушек, которые очень беспокоятся о внешнем виде..."
            her "Но я была не права.."
            her "Я начала понимать, насколько важно девушке выглядеть мило и красиво"
            hide screen hermione_main                                                                                                                                                                                   #HERMIONE
            with d3                                                                                                                                                                                                                        #HERMIONE
            $ h_body = "03_hp/13_hermione_main/body_29.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
            show screen hermione_main                                                                                                                                                                                 #HERMIONE
            with d3                                                                                                                                                                                                                        #HERMIONE
            her "..............."
            hide screen hermione_main                                                                                                                                                                                   #HERMIONE
            with d3                                                                                                                                                                                                                        #HERMIONE
            $ h_body = "03_hp/13_hermione_main/body_122.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
            show screen hermione_main                                                                                                                                                                                 #HERMIONE
            with d3                                                                                                                                                                                                                        #HERMIONE
            her "С недавнего времени я на диете..."
            hide screen hermione_main                                                                                                                                                                                   #HERMIONE
            with d3                                                                                                                                                                                                                        #HERMIONE
            $ h_body = "03_hp/13_hermione_main/body_34.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
            show screen hermione_main                                                                                                                                                                                 #HERMIONE
            with d3                                                                                                                                                                                                                        #HERMIONE
            hide screen hermione_main                                                                                                                                                                                   #HERMIONE
            with d3                                                                                                                                                                                                                        #HERMIONE
            $ h_body = "03_hp/13_hermione_main/body_33.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
            show screen hermione_main                                                                                                                                                                                 #HERMIONE
            with d3                                                                                                                                                                                                                        #HERMIONE
       
        elif one_of_ten == 9:
            hide screen hermione_main                                                                                                                                                                                   #HERMIONE
            with d3                                                                                                                                                                                                                        #HERMIONE
            $ h_body = "03_hp/13_hermione_main/body_14.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
            show screen hermione_main                                                                                                                                                                                 #HERMIONE
            with d3                                                                                                                                                                                                                        #HERMIONE
            her "Последнее время я чувствую себя довольно уверенно при мальчиках..."
            hide screen hermione_main                                                                                                                                                                                   #HERMIONE
            with d3                                                                                                                                                                                                                        #HERMIONE
            $ h_body = "03_hp/13_hermione_main/body_06.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
            show screen hermione_main                                                                                                                                                                                 #HERMIONE
            with d3                                                                                                                                                                                                                        #HERMIONE
            her "Я думаю, что должна быть благодарна вам за это."
            
        elif one_of_ten == 10:
            hide screen hermione_main                                                                                                                                                                                   #HERMIONE
            with d3                                                                                                                                                                                                                        #HERMIONE
            $ h_body = "03_hp/13_hermione_main/body_14.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
            show screen hermione_main                                                                                                                                                                                 #HERMIONE
            with d3                                                                                                                                                                                                                        #HERMIONE
            her "Мой любимый предмет?"
            hide screen hermione_main                                                                                                                                                                                   #HERMIONE
            with d3                                                                                                                                                                                                                        #HERMIONE
            $ h_body = "03_hp/13_hermione_main/body_13.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
            show screen hermione_main                                                                                                                                                                                 #HERMIONE
            with d3                                                                                                                                                                                                                        #HERMIONE
            her "Хм..."
            hide screen hermione_main                                                                                                                                                                                   #HERMIONE
            with d3                                                                                                                                                                                                                        #HERMIONE
            $ h_body = "03_hp/13_hermione_main/body_14.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
            show screen hermione_main                                                                                                                                                                                 #HERMIONE
            with d3                                                                                                                                                                                                                        #HERMIONE
            her "Думаю это \"чары\"..."
            hide screen hermione_main                                                                                                                                                                                   #HERMIONE
            with d3                                                                                                                                                                                                                        #HERMIONE
            $ h_body = "03_hp/13_hermione_main/body_15.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
            show screen hermione_main                                                                                                                                                                                 #HERMIONE
            with d3                                                                                                                                                                                                                        #HERMIONE
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
    if whoring >= 18 and whoring <= 20: # WHORING LEVEL 07.
        if one_of_ten == 1:
            hide screen hermione_main                                                                                                                                                                                   #HERMIONE
            with d3                                                                                                                                                                                                                        #HERMIONE
            $ h_body = "03_hp/13_hermione_main/body_04.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
            show screen hermione_main                                                                                                                                                                                 #HERMIONE
            with d3                                                                                                                                                                                                                        #HERMIONE
            her "Просто дайте знать, что вы хотите от меня сегодня, сэр."
            hide screen hermione_main                                                                                                                                                                                   #HERMIONE
            with d3                                                                                                                                                                                                                        #HERMIONE
            $ h_body = "03_hp/13_hermione_main/body_03.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
            show screen hermione_main                                                                                                                                                                                 #HERMIONE
            with d3                                                                                                                                                                                                                        #HERMIONE
           
        elif one_of_ten == 2:
            hide screen hermione_main                                                                                                                                                                                   #HERMIONE
            with d3                                                                                                                                                                                                                        #HERMIONE
            $ h_body = "03_hp/13_hermione_main/body_11.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
            show screen hermione_main                                                                                                                                                                                 #HERMIONE
            with d3                                                                                                                                                                                                                        #HERMIONE
            her "Я почти не учусь теперь..."
            her "Несмотря на это, моя популярность, кажется, растет..."
            hide screen hermione_main                                                                                                                                                                                   #HERMIONE
            with d3                                                                                                                                                                                                                        #HERMIONE
            $ h_body = "03_hp/13_hermione_main/body_13.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
            show screen hermione_main                                                                                                                                                                                 #HERMIONE
            with d3                                                                                                                                                                                                                        #HERMIONE
            her "Хм..."
                 
        elif one_of_ten == 3:
            hide screen hermione_main                                                                                                                                                                                   #HERMIONE
            with d3                                                                                                                                                                                                                        #HERMIONE
            $ h_body = "03_hp/13_hermione_main/body_64.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
            show screen hermione_main                                                                                                                                                                                 #HERMIONE
            with d3                                                                                                                                                                                                                        #HERMIONE
            her "Я бы не отказалась от бутылки сливочного пива ..."
            hide screen hermione_main                                                                                                                                                                                   #HERMIONE
            with d3                                                                                                                                                                                                                        #HERMIONE
            $ h_body = "03_hp/13_hermione_main/body_68.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
            show screen hermione_main                                                                                                                                                                                 #HERMIONE
            with d3                                                                                                                                                                                                                        #HERMIONE
        
        elif one_of_ten == 4:
            hide screen hermione_main                                                                                                                                                                                   #HERMIONE
            with d3                                                                                                                                                                                                                        #HERMIONE
            $ h_body = "03_hp/13_hermione_main/body_06.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
            show screen hermione_main                                                                                                                                                                                 #HERMIONE
            with d3                                                                                                                                                                                                                        #HERMIONE
            her "Что это сэр? У вас еще один подарок для меня?"
            hide screen hermione_main                                                                                                                                                                                   #HERMIONE
            with d3                                                                                                                                                                                                                        #HERMIONE
            $ h_body = "03_hp/13_hermione_main/body_12.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
            show screen hermione_main                                                                                                                                                                                 #HERMIONE
            with d3                                                                                                                                                                                                                        #HERMIONE
            her "Ох... Понятно..."

        elif one_of_ten == 5:
            hide screen hermione_main                                                                                                                                                                                   #HERMIONE
            with d3                                                                                                                                                                                                                        #HERMIONE
            $ h_body = "03_hp/13_hermione_main/body_06.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
            show screen hermione_main                                                                                                                                                                                 #HERMIONE
            with d3                                                                                                                                                                                                                        #HERMIONE
            her "Все в порядке, спасибо, что спросили."

        elif one_of_ten == 6:
            hide screen hermione_main                                                                                                                                                                                   #HERMIONE
            with d3                                                                                                                                                                                                                        #HERMIONE
            $ h_body = "03_hp/13_hermione_main/body_11.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
            show screen hermione_main                                                                                                                                                                                 #HERMIONE
            with d3                                                                                                                                                                                                                        #HERMIONE
            her "Я выгляжу толстой?"
            hide screen hermione_main                                                                                                                                                                                   #HERMIONE
            with d3                                                                                                                                                                                                                        #HERMIONE
            $ h_body = "03_hp/13_hermione_main/body_29.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
            show screen hermione_main                                                                                                                                                                                 #HERMIONE
            with d3                                                                                                                                                                                                                        #HERMIONE
            her "Надеюсь, диета сработает..."
           
        elif one_of_ten == 7:
            hide screen hermione_main                                                                                                                                                                                   #HERMIONE
            with d3                                                                                                                                                                                                                        #HERMIONE
            $ h_body = "03_hp/13_hermione_main/body_16.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
            show screen hermione_main                                                                                                                                                                                 #HERMIONE
            with d3                                                                                                                                                                                                                        #HERMIONE
            her "Помню я говорила, что книги мои лучшие друзья..."
            hide screen hermione_main                                                                                                                                                                                   #HERMIONE
            with d3                                                                                                                                                                                                                        #HERMIONE
            $ h_body = "03_hp/13_hermione_main/body_24.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
            show screen hermione_main                                                                                                                                                                                 #HERMIONE
            with d3                                                                                                                                                                                                                        #HERMIONE
            her "Теперь это звучит так неубедительно."
            hide screen hermione_main                                                                                                                                                                                   #HERMIONE
            with d3                                                                                                                                                                                                                        #HERMIONE
            $ h_body = "03_hp/13_hermione_main/body_15.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
            show screen hermione_main                                                                                                                                                                                 #HERMIONE
            with d3                                                                                                                                                                                                                        #HERMIONE
        
        elif one_of_ten == 8:
            hide screen hermione_main                                                                                                                                                                                   #HERMIONE
            with d3                                                                                                                                                                                                                        #HERMIONE
            $ h_body = "03_hp/13_hermione_main/body_04.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
            show screen hermione_main                                                                                                                                                                                 #HERMIONE
            with d3                                                                                                                                                                                                                        #HERMIONE
            her "Добавим яйца Эшвиндера..."
            her "Затем подкову и шапку красноголовика..."
            her "Затем сок морской капусты..."
            hide screen hermione_main                                                                                                                                                                                   #HERMIONE
            with d3                                                                                                                                                                                                                        #HERMIONE
            $ h_body = "03_hp/13_hermione_main/body_10.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
            show screen hermione_main                                                                                                                                                                                 #HERMIONE
            with d3                                                                                                                                                                                                                        #HERMIONE
            her "Или сначала тимьян?"
            hide screen hermione_main                                                                                                                                                                                   #HERMIONE
            with d3                                                                                                                                                                                                                        #HERMIONE
            $ h_body = "03_hp/13_hermione_main/body_13.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
            show screen hermione_main                                                                                                                                                                                 #HERMIONE
            with d3                                                                                                                                                                                                                        #HERMIONE
            her ".............."
            hide screen hermione_main                                                                                                                                                                                   #HERMIONE
            with d3                                                                                                                                                                                                                        #HERMIONE
            $ h_body = "03_hp/13_hermione_main/body_24.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
            show screen hermione_main                                                                                                                                                                                 #HERMIONE
            with d3                                                                                                                                                                                                                        #HERMIONE
            her "Ох, какая разница?"
            hide screen hermione_main                                                                                                                                                                                   #HERMIONE
            with d3                                                                                                                                                                                                                        #HERMIONE
            $ h_body = "03_hp/13_hermione_main/body_06.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
            show screen hermione_main                                                                                                                                                                                 #HERMIONE
            with d3                                                                                                                                                                                                                        #HERMIONE
       
        elif one_of_ten == 9:
            hide screen hermione_main                                                                                                                                                                                   #HERMIONE
            with d3                                                                                                                                                                                                                        #HERMIONE
            $ h_body = "03_hp/13_hermione_main/body_14.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
            show screen hermione_main                                                                                                                                                                                 #HERMIONE
            with d3                                                                                                                                                                                                                        #HERMIONE
            her "Вы думаете, я нанесла достаточно макияжа?" 
            her "Если его будет слишком много, то это будет выглядеть вульгарно..."
            hide screen hermione_main                                                                                                                                                                                   #HERMIONE
            with d3                                                                                                                                                                                                                        #HERMIONE
            $ h_body = "03_hp/13_hermione_main/body_13.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
            show screen hermione_main                                                                                                                                                                                 #HERMIONE
            with d3                                                                                                                                                                                                                        #HERMIONE
            her "Но и слишком мало тоже плохо..."
            hide screen hermione_main                                                                                                                                                                                   #HERMIONE
            with d3                                                                                                                                                                                                                        #HERMIONE
            $ h_body = "03_hp/13_hermione_main/body_12.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
            show screen hermione_main                                                                                                                                                                                 #HERMIONE
            with d3                                                                                                                                                                                                                        #HERMIONE
            her "Я не хочу выглядеть как простушка!"
            
        elif one_of_ten == 10:
            hide screen hermione_main                                                                                                                                                                                   #HERMIONE
            with d3                                                                                                                                                                                                                        #HERMIONE
            $ h_body = "03_hp/13_hermione_main/body_64.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
            show screen hermione_main                                                                                                                                                                                 #HERMIONE
            with d3                                                                                                                                                                                                                        #HERMIONE
            her "Вы хотите посмотреть на мои сиськи, сэр?" 
            hide screen hermione_main                                                                                                                                                                                   #HERMIONE
            with d3                                                                                                                                                                                                                        #HERMIONE
            $ h_body = "03_hp/13_hermione_main/body_111.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
            show screen hermione_main                                                                                                                                                                                 #HERMIONE
            with d3                                                                                                                                                                                                                        #HERMIONE
            her "25 очков, пожалуйста."
            hide screen hermione_main                                                                                                                                                                                   #HERMIONE
            with d3                                                                                                                                                                                                                        #HERMIONE
            $ h_body = "03_hp/13_hermione_main/body_120.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
            show screen hermione_main                                                                                                                                                                                 #HERMIONE
            with d3                                                                                                                                                                                                                        #HERMIONE
    
   
    if whoring >= 21: # WHORING LEVEL 08+.
        
        if one_of_ten == 1:
            hide screen hermione_main                                                                                                                                                                                   #HERMIONE
            with d3                                                                                                                                                                                                                        #HERMIONE
            $ h_body = "03_hp/13_hermione_main/body_189.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
            show screen hermione_main                                                                                                                                                                                 #HERMIONE
            with d3                                                                                                                                                                                                                        #HERMIONE
            her "У вас есть еще ненужные журналы для взрослых, сэр"
            hide screen hermione_main                                                                                                                                                                                   #HERMIONE
            with d3                                                                                                                                                                                                                        #HERMIONE
            $ h_body = "03_hp/13_hermione_main/body_188.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
            show screen hermione_main                                                                                                                                                                                 #HERMIONE
            with d3                                                                                                                                                                                                                        #HERMIONE

        elif one_of_ten == 2:
            hide screen hermione_main                                                                                                                                                                                   #HERMIONE
            with d3                                                                                                                                                                                                                        #HERMIONE
            $ h_body = "03_hp/13_hermione_main/body_31.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
            show screen hermione_main                                                                                                                                                                                 #HERMIONE
            with d3                                                                                                                                                                                                                        #HERMIONE
            her "Извиняюсь, что беспокою вас..."
            her "Но не найдется ли у вас несколько презервативов?"
            hide screen hermione_main                                                                                                                                                                                   #HERMIONE
            with d3                                                                                                                                                                                                                        #HERMIONE
            $ h_body = "03_hp/13_hermione_main/body_34.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
            show screen hermione_main                                                                                                                                                                                 #HERMIONE
            with d3                                                                                                                                                                                                                        #HERMIONE
            her "Конечно же это не для меня... Для друзей..."
                 
        elif one_of_ten == 3:
            hide screen hermione_main                                                                                                                                                                                   #HERMIONE
            with d3                                                                                                                                                                                                                        #HERMIONE
            $ h_body = "03_hp/13_hermione_main/body_14.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
            show screen hermione_main                                                                                                                                                                                 #HERMIONE
            with d3                                                                                                                                                                                                                        #HERMIONE
            her "В последнее время очень холодно..."
            hide screen hermione_main                                                                                                                                                                                   #HERMIONE
            with d3                                                                                                                                                                                                                        #HERMIONE
            $ h_body = "03_hp/13_hermione_main/body_06.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
            show screen hermione_main                                                                                                                                                                                 #HERMIONE
            with d3                                                                                                                                                                                                                        #HERMIONE
            her "Я надеюсь, что скоро выпадет снег..."
        
        elif one_of_ten == 4:
            hide screen hermione_main                                                                                                                                                                                   #HERMIONE
            with d3                                                                                                                                                                                                                        #HERMIONE
            $ h_body = "03_hp/13_hermione_main/body_127.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
            show screen hermione_main                                                                                                                                                                                 #HERMIONE
            with d3                                                                                                                                                                                                                        #HERMIONE
            her "Прыгать и кричать за Гриффиндор!"
            hide screen hermione_main                                                                                                                                                                                   #HERMIONE
            with d3                                                                                                                                                                                                                        #HERMIONE
            $ h_body = "03_hp/13_hermione_main/body_80.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
            show screen hermione_main                                                                                                                                                                                 #HERMIONE
            with d3                                                                                                                                                                                                                        #HERMIONE
            her "Смелые, удалые, красно и золотые!"
            hide screen hermione_main                                                                                                                                                                                   #HERMIONE
            with d3                                                                                                                                                                                                                        #HERMIONE
            $ h_body = "03_hp/13_hermione_main/body_06.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
            show screen hermione_main                                                                                                                                                                                 #HERMIONE
            with d3                                                                                                                                                                                                                        #HERMIONE

        elif one_of_ten == 5:
            hide screen hermione_main                                                                                                                                                                                   #HERMIONE
            with d3                                                                                                                                                                                                                        #HERMIONE
            $ h_body = "03_hp/13_hermione_main/body_10.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
            show screen hermione_main                                                                                                                                                                                 #HERMIONE
            with d3                                                                                                                                                                                                                        #HERMIONE
            her "Я надеюсь, что бал пройдет гладко..."
            hide screen hermione_main                                                                                                                                                                                   #HERMIONE
            with d3                                                                                                                                                                                                                        #HERMIONE
            $ h_body = "03_hp/13_hermione_main/body_13.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
            show screen hermione_main                                                                                                                                                                                 #HERMIONE
            with d3                                                                                                                                                                                                                        #HERMIONE

        elif one_of_ten == 6:
            hide screen hermione_main                                                                                                                                                                                   #HERMIONE
            with d3                                                                                                                                                                                                                        #HERMIONE
            $ h_body = "03_hp/13_hermione_main/body_06.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
            show screen hermione_main                                                                                                                                                                                 #HERMIONE
            with d3                                                                                                                                                                                                                        #HERMIONE
            her "Интересно, что наденет Джинни на бал..."
        
        elif one_of_ten == 7:
            hide screen hermione_main                                                                                                                                                                                   #HERMIONE
            with d3                                                                                                                                                                                                                        #HERMIONE
            $ h_body = "03_hp/13_hermione_main/body_16.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
            show screen hermione_main                                                                                                                                                                                 #HERMIONE
            with d3                                                                                                                                                                                                                        #HERMIONE
            her "Учитвая все, вы можете продолжать использовать меня, взамен на очки..."
            hide screen hermione_main                                                                                                                                                                                   #HERMIONE
            with d3                                                                                                                                                                                                                        #HERMIONE
            $ h_body = "03_hp/13_hermione_main/body_11.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
            show screen hermione_main                                                                                                                                                                                 #HERMIONE
            with d3                                                                                                                                                                                                                        #HERMIONE
            her "Нынче я редко надеваю белье..."
        
        elif one_of_ten == 8:
            hide screen hermione_main                                                                                                                                                                                   #HERMIONE
            with d3                                                                                                                                                                                                                        #HERMIONE
            $ h_body = "03_hp/13_hermione_main/body_117.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
            show screen hermione_main                                                                                                                                                                                 #HERMIONE
            with d3                                                                                                                                                                                                                        #HERMIONE
            her "Сэр, хотите вставить свой член мне в рот?"
            hide screen hermione_main                                                                                                                                                                                   #HERMIONE
            with d3                                                                                                                                                                                                                        #HERMIONE
            $ h_body = "03_hp/13_hermione_main/body_135.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
            show screen hermione_main                                                                                                                                                                                 #HERMIONE
            with d3                                                                                                                                                                                                                        #HERMIONE
            her "Сэр, я прошу вас..."
            hide screen hermione_main                                                                                                                                                                                   #HERMIONE
            with d3                                                                                                                                                                                                                        #HERMIONE
            $ h_body = "03_hp/13_hermione_main/body_111.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
            show screen hermione_main                                                                                                                                                                                 #HERMIONE
            with d3                                                                                                                                                                                                                        #HERMIONE
            her "Пятьдесят очков, пожалуйста!"
            hide screen hermione_main                                                                                                                                                                                   #HERMIONE
            with d3                                                                                                                                                                                                                        #HERMIONE
            $ h_body = "03_hp/13_hermione_main/body_122.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
            show screen hermione_main                                                                                                                                                                                 #HERMIONE
            with d3                                                                                                                                                                                                                        #HERMIONE

        elif one_of_ten == 9:
            hide screen hermione_main                                                                                                                                                                                   #HERMIONE
            with d3                                                                                                                                                                                                                        #HERMIONE
            $ h_body = "03_hp/13_hermione_main/body_127.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
            show screen hermione_main                                                                                                                                                                                 #HERMIONE
            with d3                                                                                                                                                                                                                        #HERMIONE
            her "Прочитала статью, в которой говорится о положительном влиянии спермы на кожу женщины..."
            hide screen hermione_main                                                                                                                                                                                   #HERMIONE
            with d3                                                                                                                                                                                                                        #HERMIONE
            $ h_body = "03_hp/13_hermione_main/body_128.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
            show screen hermione_main                                                                                                                                                                                 #HERMIONE
            with d3                                                                                                                                                                                                                        #HERMIONE
            her "Интересно, как они это узнают..."
            hide screen hermione_main                                                                                                                                                                                   #HERMIONE
            with d3                                                                                                                                                                                                                        #HERMIONE
            $ h_body = "03_hp/13_hermione_main/body_122.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
            show screen hermione_main                                                                                                                                                                                 #HERMIONE
            with d3                                                                                                                                                                                                                        #HERMIONE
            her "Журнал проводит какие-то исследования?"
            hide screen hermione_main                                                                                                                                                                                   #HERMIONE
            with d3                                                                                                                                                                                                                        #HERMIONE
            $ h_body = "03_hp/13_hermione_main/body_128.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
            show screen hermione_main                                                                                                                                                                                 #HERMIONE
            with d3                                                                                                                                                                                                                        #HERMIONE

        elif one_of_ten == 10:
            hide screen hermione_main                                                                                                                                                                                   #HERMIONE
            with d3                                                                                                                                                                                                                        #HERMIONE
            $ h_body = "03_hp/13_hermione_main/body_127.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
            show screen hermione_main                                                                                                                                                                                 #HERMIONE
            with d3                                                                                                                                                                                                                        #HERMIONE
            her "Это похоже на..."
            her "Сначала Гриффиндор, потом Когтевран, потом Пуффендуй..."
            hide screen hermione_main                                                                                                                                                                                   #HERMIONE
            with d3                                                                                                                                                                                                                        #HERMIONE
            $ h_body = "03_hp/13_hermione_main/body_186.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
            show screen hermione_main                                                                                                                                                                                 #HERMIONE
            with d3                                                                                                                                                                                                                        #HERMIONE
            her "И Слизерин не попадает в этот список!"
            hide screen hermione_main                                                                                                                                                                                   #HERMIONE
            with d3                                                                                                                                                                                                                        #HERMIONE
            $ h_body = "03_hp/13_hermione_main/body_120.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
            show screen hermione_main                                                                                                                                                                                 #HERMIONE
            with d3                                                                                                                                                                                                                        #HERMIONE

    jump day_time_requests

#    if daytime:
#        jump night_main_menu
#    else:
#        $ hermione_sleeping = True
#        jump day_main_menu            
    
    
    