label snape_chitchat:
    $this.CHITCHAT.RunStep()
#    if not chitchat_event_01_happened and tutoring_hermione_unlocked and days_without_an_event >=2:
#        jump chitchat_event_01
    
    

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
            sna "Ты действительно думаешь, что сломаешь девчонку?"
        
        elif one_of_ten == 2:
            hide screen snape_main                                                                                                                   #SNAPE
            with d3                                                                                                                                                  #SNAPE
            $ s_sprite = "03_hp/10_snape_main/snape_01.png"                                                                            #SNAPE
            show screen snape_main                                                                                                                  #SNAPE
            with d3                                                                                                                                                   #SNAPE
            sna "Ты тоже ненавидишь эту мерзкую солнечную погоду?"
            hide screen snape_main                                                                                                                   #SNAPE
            with d3                                                                                                                                                  #SNAPE
            $ s_sprite = "03_hp/10_snape_main/snape_06.png"                                                                            #SNAPE
            show screen snape_main                                                                                                                  #SNAPE
            with d3                                                                                                                                                   #SNAPE
            sna "Хотел бы я, чтобы дождь шел круглые сутки..." 
            
        elif one_of_ten == 3:
            hide screen snape_main                                                                                                                   #SNAPE
            with d3                                                                                                                                                  #SNAPE
            $ s_sprite = "03_hp/10_snape_main/snape_06.png"                                                                            #SNAPE
            show screen snape_main                                                                                                                  #SNAPE
            with d3                                                                                                                                                   #SNAPE
            sna "Знаешь, меня одолевают сомнения относительно нашего плана..."
            
        elif one_of_ten == 4:
            hide screen snape_main                                                                                                                   #SNAPE
            with d3                                                                                                                                                  #SNAPE
            $ s_sprite = "03_hp/10_snape_main/snape_05.png"                                                                            #SNAPE
            show screen snape_main                                                                                                                  #SNAPE
            with d3                                                                                                                                                   #SNAPE
            sna "Ты уверен, что ты не Альбус Дамблдор?"
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
            sna "........*Негромко рычит*."
            hide screen snape_main                                                                                                                   #SNAPE
            with d3                                                                                                                                                  #SNAPE
            $ s_sprite = "03_hp/10_snape_main/snape_05.png"                                                                            #SNAPE
            show screen snape_main                                                                                                                  #SNAPE
            with d3                                                                                                                                                   #SNAPE
            sna "Это звучало правдоподобно?"
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
            sna "Вселять страх в сердца студентов это важная задача учителей."

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
            sna "Однажды я просто не выдержу, Богом клянусь!"

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
            sna "Так что у меня нет настроения разговаривать..."
            
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
            sna "Что за бессмысленная трата ресурсов!"
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
            sna "Я не замечаю никаких изменений в поведение мисс Грейнджер..."
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
            sna "Она также помогает сосредоточится на деле, делает тебя более собраным."
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
            sna "Дуэли - это одна из моих сильных сторон, ну ты понимаешь..."

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
            sna "...и Хафф-что-то..."
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
            sna "Ты никогда не увидишь, чтобы уважающий себя колдун летал на метле."
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
            sna "Есть ли прогресс в обработке нашей Мисс Всезнайки?"
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
            sna "Думаю, она  отдала бы их и бесплатно, лишь бы задобрить меня."
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
            sna "Я думаю, это очень хорошее начало дня..."
            hide screen snape_main                                                                                                                   #SNAPE
            with d3                                                                                                                                                  #SNAPE
            $ s_sprite = "03_hp/10_snape_main/snape_02.png"                                                                            #SNAPE
            show screen snape_main                                                                                                                  #SNAPE
            with d3                                                                                                                                                   #SNAPE
            sna "Спорим, ты не думал, что я это скажу?"

        elif one_of_ten == 4:
            hide screen snape_main                                                                                                                   #SNAPE
            with d3                                                                                                                                                  #SNAPE
            $ s_sprite = "03_hp/10_snape_main/24.png"                                                                            #SNAPE
            show screen snape_main                                                                                                                  #SNAPE
            with d3                                                                                                                                                   #SNAPE
            sna "Квиддич с годами становится все популярнее..."
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
            sna "Ха-ха-ха! Прости, я просто не могу спокойно произнести это."
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
            sna "На занятиях ты не можешь ошибиться."
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
            sna "Ты - единственный человек перед кем я отвечаю..."
            hide screen snape_main                                                                                                                   #SNAPE
            with d3                                                                                                                                                  #SNAPE
            $ s_sprite = "03_hp/10_snape_main/snape_05.png"                                                                            #SNAPE
            show screen snape_main                                                                                                                  #SNAPE
            with d3                                                                                                                                                   #SNAPE
            sna "Так что теперь я  могу делать практически всё что угодно..."
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
            sna  "В последнее время мисс Грейнджер стала очень агрессивной..."
            hide screen snape_main                                                                                                                   #SNAPE
            with d3                                                                                                                                                  #SNAPE
            $ s_sprite = "03_hp/10_snape_main/snape_05.png"                                                                            #SNAPE
            show screen snape_main                                                                                                                  #SNAPE
            with d3                                                                                                                                                   #SNAPE
            sna "Надеюсь, ты знаешь, что делаешь..."
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
            sna "Если бы ты видел какую форму носят некоторые из этих девченок..."
            hide screen snape_main                                                                                                                   #SNAPE
            with d3                                                                                                                                                  #SNAPE
            $ s_sprite = "03_hp/10_snape_main/snape_13.png"                                                                            #SNAPE
            show screen snape_main                                                                                                                  #SNAPE
            with d3                                                                                                                                                   #SNAPE
            sna "Они просто напрашиваются на ЭТО."
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
            sna "Мои последние наблюдения показывают, что 9 из 10 девочек мечтают, что бы их соблазнил учитель."
            hide screen snape_main                                                                                                                   #SNAPE
            with d3                                                                                                                                                  #SNAPE
            $ s_sprite = "03_hp/10_snape_main/snape_03.png"                                                                            #SNAPE
            show screen snape_main                                                                                                                  #SNAPE
            with d3                                                                                                                                                   #SNAPE
            sna "Я так же уверен, что десятая - это Гермиона Грейнджер ."
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
            sna "В такие дни мне нужно стараться, чтобы быть в плохом настроение."
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
            sna "Думаешь, мы сможем превратить Хогвартс в школу \"только для девочек\" ?"
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
            sna "Чтобы сбежать от студентов!"
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
            sna "Вкратце, все мои мышцы болят и я чуствую себя опустошенным..."
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
            sna "Ты думаешь, я не смогу отказаться от выпивки?"
            hide screen snape_main                                                                                                                   #SNAPE
            with d3                                                                                                                                                  #SNAPE
            $ s_sprite = "03_hp/10_snape_main/snape_06.png"                                                                            #SNAPE
            show screen snape_main                                                                                                                  #SNAPE
            with d3                                                                                                                                                   #SNAPE
            sna "Ведь моя жизнь наполнена стрессом..."
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
            sna "Взамен на дикий секс с моими студентками!"
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
            sna "Мисс Грейнджер в последнее время притихла..."
            hide screen snape_main                                                                                                                   #SNAPE
            with d3                                                                                                                                                  #SNAPE
            $ s_sprite = "03_hp/10_snape_main/snape_03.png"                                                                            #SNAPE
            show screen snape_main                                                                                                                  #SNAPE
            with d3                                                                                                                                                   #SNAPE
            sna "Я уверен, она замышляет что-то..."
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
            sna "Но поставить своих персонажей в невыгодное положение и помочь им выжить звучит убедительнее..."
            hide screen snape_main                                                                                                                   #SNAPE
            with d3                                                                                                                                                  #SNAPE
            $ s_sprite = "03_hp/10_snape_main/snape_02.png"                                                                            #SNAPE
            show screen snape_main                                                                                                                  #SNAPE
            with d3                                                                                                                                                   #SNAPE
            sna "Сейчас {size=+7}это{/size} настоящее мастерство."
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
            sna "А что если не мы играем с девченкой, а она с нами?"
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
            sna "Полапал бы их немного..."
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
            sna "Скажи мне, Джинни... тебе когда нибудь вылизывала зад молодая ведьмочка?"
            hide screen snape_main                                                                                                                   #SNAPE
            with d3                                                                                                                                                  #SNAPE
            $ s_sprite = "03_hp/10_snape_main/snape_21.png"                                                                            #SNAPE
            show screen snape_main                                                                                                                  #SNAPE
            with d3                                                                                                                                                   #SNAPE
            sna "Незабываемые ощущения, скажу я тебе..."
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
            sna "Все по плану, надеюсь?"
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
            sna "Ты знаешь, что я люблю в Квиддиче?"
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
            sna "И когда я говорю \"Хогвартс\", я имею в виду \"Себя\"."
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
            sna "Я бы предпочел, чтобы меня боялись..."
            hide screen snape_main                                                                                                                   #SNAPE
            with d3                                                                                                                                                  #SNAPE
            $ s_sprite = "03_hp/10_snape_main/23.png"                                                                            #SNAPE
            show screen snape_main                                                                                                                  #SNAPE
            with d3                                                                                                                                                   #SNAPE
            sna "Но, я думаю, с этим тоже всё в порядке..."

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
            sna "Мисс Грейнджер меняется. И это становится заметно..."
            sna "Ее оценки идут вниз и даже поведение стало далеко от идеала..."
            hide screen snape_main                                                                                                                   #SNAPE
            with d3                                                                                                                                                  #SNAPE
            $ s_sprite = "03_hp/10_snape_main/snape_10.png"                                                                            #SNAPE
            show screen snape_main                                                                                                                  #SNAPE
            with d3                                                                                                                                                   #SNAPE
            sna "Но несмотря на это, она все еще заноза в моей заднице!"
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
            sna "Из меня получился бы отличный вампир?"
            sna "Может, я куплю пару фальшивых клыков..."
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
            sna "Это список вещей, которые я не люблю..."
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
            sna "То чувство, когда ты кончил студентке в рот, а она произносит: \"Спасибо, профессор\"."
            hide screen snape_main                                                                                                                   #SNAPE
            with d3                                                                                                                                                  #SNAPE
            $ s_sprite = "03_hp/10_snape_main/snape_13.png"                                                                            #SNAPE
            show screen snape_main                                                                                                                  #SNAPE
            with d3                                                                                                                                                   #SNAPE
            sna "Оно великолепно, правда?"
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
            sna "Если бы я был призраком, я бы так и делал."
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
            sna "Однажды девчонка поведала мне, что хочет быть изнасилованной этим сквибом Мистером Филтчем."
            hide screen snape_main                                                                                                                   #SNAPE
            with d3                                                                                                                                                  #SNAPE
            $ s_sprite = "03_hp/10_snape_main/snape_14.png"                                                                            #SNAPE
            show screen snape_main                                                                                                                  #SNAPE
            with d3                                                                                                                                                   #SNAPE
            sna "Думаю, мне стоит это устроить. Что думаешь?"
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
            sna "А теперь, не пойми меня неправильно - я все еще ненавижу ее."
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
            sna "Ты знаешь что такое \"буккакэ\", а?"
            sna "А как насчет \"глубокого заглота\"?"
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
            sna "Так или иначе \"изнасилование\" было всегда..."
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
            sna "Я тайно варю зелье, которое заставляет течь женскую грудь..."
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
            sna "Может, мне помочь ей?"
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
            sna "Если бы я только мог забросить преподавание, но продолжать веселится..."
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
            sna "Хочешь, пришлю тебе пару шлюх?"
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
    $sna_head_state = 1
    sna_head_main "Итак..."
    sna_head_main "Я слышал что мисс Грейнджер начала заниматься с тобой наедине?"
    m "Да, так и есть..."
    m "Хотя не уверен, что это входит в наш план."
    $sna_head_state = 9
    sna_head_main "О чем ты? Все идет отлично."
    sna_head_main "Я лично и пара учителей делаем ее занятия невыносимыми!"
    sna_head_main "И в результате она стала заниматься больше..."
    sna_head_main "Теперь вот берет частные уроки..."
    $sna_head_state = 18
    sna_head_main "И значит у нее все меньше и меньше времени докучать мне!"
    m "Понятно..."
    $sna_head_state = 10
    sna_head_main "И еще... Ты, конечно и сам знаешь,...  но просто на всякий случай..."
    sna_head_main "Не учи ее ничему полезному, ладно?"
    m "Я постараюсь."
    $sna_head_state = 1
    sna_head_main "Ладно, на сегодня всё..."
    
    
    
    

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
    $ pos = POS_410
    
    if whoring >= 0 and whoring <= 2: # WHORING LEVEL 01.
        if one_of_ten == 1:
            $herView.hideQQ()
            $herView.showQQ( "body_04.png", pos )
            her "Может быть, если я буду работать быстрее, я смогу втиснуть пару занятий в мое рассписание..."
            $herView.hideQQ()
            $herView.showQQ( "body_03.png", pos )
        
        elif one_of_ten == 2:
            $herView.hideQQ()
            $herView.showQQ( "body_04.png", pos )
            her "В общем-то, мне нравится когда меня зовут \"Всезнайка\"."
            her "Возможно, я даже краснею от этого..."
            $herView.hideQQ()
            $herView.showQQ( "body_03.png", pos )
        elif one_of_ten == 3:
            $herView.hideQQ()
            $herView.showQQ( "body_04.png", pos )
            her "Василиск, также известен как король змей."
            her "Герпо Фол первый осеменил Василиска."
            her "Он сделал это с помощью--"
            $herView.hideQQ()
            $herView.showQQ( "body_10.png", pos )
            her "Ой, извините, профессор, у нас еще один тест завтра..."
            her "Я просто хочу быть уверенной, что я готова..."
            $herView.hideQQ()
            $herView.showQQ( "body_01.png", pos )
        elif one_of_ten == 4:
            $herView.hideQQ()
            $herView.showQQ( "body_10.png", pos )
            her "Если бы мое тело не требовало сна..."
            $herView.hideQQ()
            $herView.showQQ( "body_18.png", pos )
            her "Я могла бы заниматся в два раза больше!?"
            $herView.hideQQ()
            $herView.showQQ( "body_14.png", pos )
            her "Надеюсь, есть заклинание для этого..."
            $herView.hideQQ()
            $herView.showQQ( "body_03.png", pos )
        
        elif one_of_ten == 5:
            $herView.hideQQ()
            $herView.showQQ( "body_04.png", pos )
            her "До сих пор профессор Трелони не дал мне даже капельки полезных знаний, сэр."
            $herView.hideQQ()
            $herView.showQQ( "body_03.png", pos )
       
        elif one_of_ten == 6:
            $herView.hideQQ()
            $herView.showQQ( "body_04.png", pos )
            her "Если бы только студенты были честными, они бы полюбили ответственность."
            $herView.hideQQ()
            $herView.showQQ( "body_03.png", pos )
      
        elif one_of_ten == 7:
            $herView.hideQQ()
            $herView.showQQ( "body_04.png", pos )
            her "Как люди могу быть такими безразличными к мировым проблемам?"
            her "Лично я считаю, что мы все должны работать вместе, чтобы мир стал лучше."
            $herView.hideQQ()
            $herView.showQQ( "body_03.png", pos )
            
        elif one_of_ten == 8:
            $herView.hideQQ()
            $herView.showQQ( "body_10.png", pos )
            her "В последнее время дождь льет чаще..."
            $herView.hideQQ()
            $herView.showQQ( "body_01.png", pos )
    
        elif one_of_ten == 9:
            $herView.hideQQ()
            $herView.showQQ( "body_10.png", pos )
            her "Очень мало людей знает..."
            $herView.hideQQ()
            $herView.showQQ( "body_06.png", pos )
            her "...что я очень люблю шоколад."
            $herView.hideQQ()
            $herView.showQQ( "body_01.png", pos )
       
        elif one_of_ten == 10:
            $herView.hideQQ()
            $herView.showQQ( "body_06.png", pos )
            her "Извините сэр, но у меня нету времени на разговоры..."
            $herView.hideQQ()
            $herView.showQQ( "body_03.png", pos )


    if whoring >= 3 and whoring <= 5: # WHORING LEVEL 02
        if one_of_ten == 1:
            $herView.hideQQ()
            $herView.showQQ( "body_04.png", pos )
            her "Я где то прочитала что полная луна помогает сосредоточится..."
            $herView.hideQQ()
            $herView.showQQ( "body_03.png", pos )
            
        elif one_of_ten == 2:
            $herView.hideQQ()
            $herView.showQQ( "body_06.png", pos )
            her "Я обожаю сидеть с книгой у огня, когда льет дождь..."
            $herView.hideQQ()
            $herView.showQQ( "body_01.png", pos )
            
        elif one_of_ten == 3:
            $herView.hideQQ()
            $herView.showQQ( "body_10.png", pos )
            her "Прошел слух, что профессор Снейп что-то замышляет в школе..."
            $herView.hideQQ()
            $herView.showQQ( "body_15.png", pos )
            her "Хотя, наверное, это пустяки..."
            $herView.hideQQ()
            $herView.showQQ( "body_03.png", pos )
            
        elif one_of_ten == 4:
            $herView.hideQQ()
            $herView.showQQ( "body_04.png", pos )
            her "Несмотря на сомнительность услуг, которые я вам оказывала, сэр..."
            her "Я благодарна вам за вашу помощь..."
            $herView.hideQQ()
            $herView.showQQ( "body_09.png", pos )
            her "Гриффиндор нуждается в этих очках больше, чем когда либо..."
            $herView.hideQQ()
            $herView.showQQ( "body_03.png", pos )
            
        elif one_of_ten == 5:
            $herView.hideQQ()
            $herView.showQQ( "body_04.png", pos )
            her "Почему квиддич так популярен среди девочек? Я не понимаю..."
            $herView.hideQQ()
            $herView.showQQ( "body_03.png", pos )
            
        elif one_of_ten == 6:
            $herView.hideQQ()
            $herView.showQQ( "body_04.png", pos )
            her "Наше \"Общество Защиты Прав Мужчин\" набирает популярность."
            her "Это очень важно знать, что вы помогаете развивать наше общество."
            $herView.hideQQ()
            $herView.showQQ( "body_03.png", pos )
            
        elif one_of_ten == 7:
            $herView.hideQQ()
            $herView.showQQ( "body_04.png", pos )
            her "Хогвартс имеет внушительную библиотеку..."
            $herView.hideQQ()
            $herView.showQQ( "body_08.png", pos )
            her "Но я хочу, чтобы она была еще больше..."
            $herView.hideQQ()
            $herView.showQQ( "body_03.png", pos )
            
        elif one_of_ten == 8:
            $herView.hideQQ()
            $herView.showQQ( "body_10.png", pos )
            her "Как один из лучших студентов академии, я должна поддерживать свою репутацию..."
            her "Люди уважают меня..."
            $herView.hideQQ()
            $herView.showQQ( "body_31.png", pos )
            her "...так что я очень ценю ваше внимание, сэр."
            $herView.hideQQ()
            $herView.showQQ( "body_29.png", pos )
            
        elif one_of_ten == 9:
            $herView.hideQQ()
            $herView.showQQ( "body_11.png", pos )
            her "Услуги которые я вам оказала тогда, сэр..."
            $herView.hideQQ()
            $herView.showQQ( "body_33.png", pos )
            her "......."
            $herView.hideQQ()
            $herView.showQQ( "body_87.png", pos )
            her "Я пошла на это только для моего факультета."
            $herView.hideQQ()
            $herView.showQQ( "body_120.png", pos )
            her "Я просто хотела, чтобы вы знали это, сэр..."
            
        elif one_of_ten == 10:
            $herView.hideQQ()
            $herView.showQQ( "body_04.png", pos )
            her "Наш \"Осенний бал\" будет через несколько месяцев..."
            $herView.hideQQ()
            $herView.showQQ( "body_11.png", pos )
            her "Но некоторые девочки уже обсуждают что они наденут на бал..."
            $herView.hideQQ()
            $herView.showQQ( "body_185.png", pos )

  
    if whoring >= 6 and whoring <= 8: # WHORING LEVEL 03.
        if one_of_ten == 1:
            $herView.hideQQ()
            $herView.showQQ( "body_04.png", pos )
            her "Вы помните, как вы просили мои трусики в первый раз?"
            her "Я тогда так сильно разозлилась..."
            $herView.hideQQ()
            $herView.showQQ( "body_09.png", pos )
            her "Тепеь я вижу, что я была неправа..."
            her "Ведь судьба целого факультета в моих руках..."
            $herView.hideQQ()
            $herView.showQQ( "body_07.png", pos )
            her "Все остальное не должно меня волновать!"
            
        elif one_of_ten == 2:
            $herView.hideQQ()
            $herView.showQQ( "body_04.png", pos )
            her "Скорость, с которой Слизерин набирает очки в последнее время просто невозможна."
            $herView.hideQQ()
            $herView.showQQ( "body_05.png", pos )
            her "Я думаю, за этим стоит профессор Снейп."
            $herView.hideQQ()
            $herView.showQQ( "body_04.png", pos )
            her "Вам нужно разобраться в ситуации, сэр."
            $herView.hideQQ()
            $herView.showQQ( "body_03.png", pos )
            
        elif one_of_ten == 3:
            $herView.hideQQ()
            $herView.showQQ( "body_10.png", pos )
            her "Яйца Эшвендэра, корень розы, лунный камень..."
            $herView.hideQQ()
            $herView.showQQ( "body_11.png", pos )
            her "Ах? Я опять размышляла вслух?"
            $herView.hideQQ()
            $herView.showQQ( "body_24.png", pos )
            her "Извините..."
            $herView.hideQQ()
            $herView.showQQ( "body_13.png", pos )
            her "Просто скоро снова тест..."

        elif one_of_ten == 4:
            $herView.hideQQ()
            $herView.showQQ( "body_77.png", pos )
            her "Я ненавижу факультет Слизерина всем своим сердцем, сэр."
            
        elif one_of_ten == 5:
            $herView.hideQQ()
            $herView.showQQ( "body_16.png", pos )
            her "Хогвартс стал для меня новым домом в последнее время..."
            $herView.hideQQ()
            $herView.showQQ( "body_71.png", pos )
            her "Я даже почти не скучаю по родителям..."
            $herView.hideQQ()
            $herView.showQQ( "body_18.png", pos )
            her "Если подумать, я не скучаю по ним совсем..."
            $herView.hideQQ()
            $herView.showQQ( "body_118.png", pos )
            her "Я - ужасная дочь..."

        elif one_of_ten == 6:
            $herView.hideQQ()
            $herView.showQQ( "body_70.png", pos )
            her "*Зевок!* Я прочитала о технике, которая помогает в два раза меньше спать..."
            $herView.hideQQ()
            $herView.showQQ( "body_73.png", pos )
            her "Но, кажется, она не работает.... *Зевок!*"

        elif one_of_ten == 7:
            $herView.hideQQ()
            $herView.showQQ( "body_04.png", pos )
            her "Даже когда я закончу Хогвартс я буду продолжать совершенствоваться."
            $herView.hideQQ()
            $herView.showQQ( "body_02.png", pos )
            her "Если я отдам себя всю этому миру он станет лучше, я знаю это!"
            $herView.hideQQ()
            $herView.showQQ( "body_03.png", pos )
           
        elif one_of_ten == 8:
            $herView.hideQQ()
            $herView.showQQ( "body_11.png", pos )
            her "Мне кажется, что этот год будет важнейшим в моей жизни..."
            $herView.hideQQ()
            $herView.showQQ( "body_13.png", pos )
  
        elif one_of_ten == 9:
            $herView.hideQQ()
            $herView.showQQ( "body_04.png", pos )
            her "Некоторые школьные коридоры пыльные и грязные..."
            her "Пожалуйста позаботьтесь об этом, сэр..."
            $herView.hideQQ()
            $herView.showQQ( "body_03.png", pos )
       
        elif one_of_ten == 10:
            $herView.hideQQ()
            $herView.showQQ( "body_14.png", pos )
            her "Я читала об этом. Называется \"Маховик времени\"."            
            her "Он позволяет владельцу контролировать время..."
            $herView.hideQQ()
            $herView.showQQ( "body_16.png", pos )
            her "Если бы он был у меня, я бы творила чудеса со своим расписанием..."
            $herView.hideQQ()
            $herView.showQQ( "body_17.png", pos )
        

    if whoring >= 9 and whoring <= 11: # WHORING LEVEL 04.
        if one_of_ten == 1:
            $herView.hideQQ()
            $herView.showQQ( "body_11.png", pos )
            her "Мое \"Общество по Защите Прав Мужчин\" в последнее время теряет популярность..."
            $herView.hideQQ()
            $herView.showQQ( "body_12.png", pos )
            her "Похоже это никого не волнует!"

        elif one_of_ten == 2:
            $herView.hideQQ()
            $herView.showQQ( "body_04.png", pos )
            her "Спасибо вам за все эти очки, сэр."
            $herView.hideQQ()
            $herView.showQQ( "body_07.png", pos )
            her "Некоторые, конечно, достались весьма странным образом, но ..."
            $herView.hideQQ()
            $herView.showQQ( "body_04.png", pos )
            her "Но это не важно, до тех пор, пока это дает \"Гриффиндору\" преимущество в гонке со \"Слизерином\"."
            $herView.hideQQ()
            $herView.showQQ( "body_03.png", pos )

        elif one_of_ten == 3:
            $herView.hideQQ()
            $herView.showQQ( "body_77.png", pos )
            her "Квиддич это глупо!"
            $herView.hideQQ()
            $herView.showQQ( "body_17.png", pos )
            her "Вот. Я сказала это."
            
        elif one_of_ten == 4:
            $herView.hideQQ()
            $herView.showQQ( "body_02.png", pos )
            her "Сэр, есть кое-что, что вы должны знать о профессоре Снейпе..."
            $herView.hideQQ()
            $herView.showQQ( "body_10.png", pos )
            her "................."
            $herView.hideQQ()
            $herView.showQQ( "body_09.png", pos )
            her "........................."
            $herView.hideQQ()
            $herView.showQQ( "body_04.png", pos )
            her "Ух... Ничего..."
            $herView.hideQQ()
            $herView.showQQ( "body_03.png", pos )
 
        elif one_of_ten == 5:
            $herView.hideQQ()
            $herView.showQQ( "body_04.png", pos )
            her "Некоторые из \"Слизеринских\" девок в последнее время среди бела дня продаются за очки..."
            $herView.hideQQ()
            $herView.showQQ( "body_02.png", pos )
            her "Вы должны положить этому конец, сэр."
            $herView.hideQQ()
            $herView.showQQ( "body_69.png", pos )
            her "(Я едва поспеваю за ними...)"

        elif one_of_ten == 6:
            $herView.hideQQ()
            $herView.showQQ( "body_10.png", pos )
            her "Жизнь устроена очень странно..."
            $herView.hideQQ()
            $herView.showQQ( "body_08.png", pos )
            her "Вы согласны, сэр?"
            $herView.hideQQ()
            $herView.showQQ( "body_13.png", pos )

        elif one_of_ten == 7:
            $herView.hideQQ()
            $herView.showQQ( "body_76.png", pos )
            her "Слизеринцы..."
            $herView.hideQQ()
            $herView.showQQ( "body_77.png", pos )
            
        elif one_of_ten == 8:
            $herView.hideQQ()
            $herView.showQQ( "body_10.png", pos )
            her "В последнее время я так много времени провела в вашем кабинете..."
            $herView.hideQQ()
            $herView.showQQ( "body_11.png", pos )
            her "Если я буду неосторожна, некоторые могут заметить и решить, что я стала вашей любовниц..."
            $herView.hideQQ()
            $herView.showQQ( "body_34.png", pos )
            her "Я хотела сказать, любимчиком..."
            $herView.hideQQ()
            $herView.showQQ( "body_33.png", pos )

        elif one_of_ten == 9:
            $herView.hideQQ()
            $herView.showQQ( "body_02.png", pos )
            her "Мой любимый цвет?"
            $herView.hideQQ()
            $herView.showQQ( "body_02.png", pos )
            her "Алый и золотой, конечно же!"
            $herView.hideQQ()
            $herView.showQQ( "body_03.png", pos )
       
        elif one_of_ten == 10:
            $herView.hideQQ()
            $herView.showQQ( "body_10.png", pos )
            her "Это странно, что мои лучшие друзья это мальчики?"
            $herView.hideQQ()
            $herView.showQQ( "body_01.png", pos )
        

        
    if whoring >= 12 and whoring <= 14: # WHORING LEVEL 05.
        if one_of_ten == 1:
            $herView.hideQQ()
            $herView.showQQ( "body_07.png", pos )
            her "Сэр, при всем уважении..."
            her "Профессор Снейп распускает руки!"
            $herView.hideQQ()
            $herView.showQQ( "body_11.png", pos )
            her "Вы должны сделать что-то..."
            $herView.hideQQ()
            $herView.showQQ( "body_03.png", pos )

        elif one_of_ten == 2:
            $herView.hideQQ()
            $herView.showQQ( "body_04.png", pos )
            her "Я готова пойти на все, лишь бы \"Гриффиндор\" лидировал..."
            her "Но это не значит, что я с удовольствием отдаюсь вам за очки для факультета."
            $herView.hideQQ()
            $herView.showQQ( "body_118.png", pos )
            her "{size=-4}(Как какая-то ведьма-проститутка...){/size}"

        elif one_of_ten == 3:
            $herView.hideQQ()
            $herView.showQQ( "body_79.png", pos )
            her "Что на сегодня, сэр?"
            
        elif one_of_ten == 4:
            $herView.hideQQ()
            $herView.showQQ( "body_11.png", pos )
            her "Раньше я училась лучше, чем сейчас..."
            $herView.hideQQ()
            $herView.showQQ( "body_10.png", pos )
            her "Я теряю мотивацию?"
            $herView.hideQQ()
            $herView.showQQ( "body_13.png", pos )
            
        elif one_of_ten == 5:
            $herView.hideQQ()
            $herView.showQQ( "body_08.png", pos )
            her "Мой нелюбимый предмет?"
            $herView.hideQQ()
            $herView.showQQ( "body_09.png", pos )
            her "Гадание." 
            
        elif one_of_ten == 6:
            $herView.hideQQ()
            $herView.showQQ( "body_14.png", pos )
            her "Мой отец сказал: \"Магия это наука, которую мы не можем понять\"."
            $herView.hideQQ()
            $herView.showQQ( "body_10.png", pos )
            her "Он, конечно же, мог ошибаться..."
            $herView.hideQQ()
            $herView.showQQ( "body_13.png", pos )
            
        elif one_of_ten == 7:
            $herView.hideQQ()
            $herView.showQQ( "body_04.png", pos )
            her "Несмотря ни на что..."
            $herView.hideQQ()
            $herView.showQQ( "body_10.png", pos )
            her "Я благодарна, что вы позволяете мне получать дополнительные очки..."
            $herView.hideQQ()
            $herView.showQQ( "body_13.png", pos )
            
        elif one_of_ten == 8:
            $herView.hideQQ()
            $herView.showQQ( "body_14.png", pos )
            her "Сегодня довольно холодно, не так ли?"
            $herView.hideQQ()
            $herView.showQQ( "body_15.png", pos )
            
        elif one_of_ten == 9:
            $herView.hideQQ()
            $herView.showQQ( "body_14.png", pos )
            her "\"Осенний бал\" совсем скоро..."
            $herView.hideQQ()
            $herView.showQQ( "body_15.png", pos )
            
        elif one_of_ten == 10:
            $herView.hideQQ()
            $herView.showQQ( "body_10.png", pos )
            her "Люди вряд ли посетят наше \"Общество по Защите Прав Мужчин\" еще когда-либо..."
            $herView.hideQQ()
            $herView.showQQ( "body_13.png", pos )
    
    
    
    
    
    
        
    if whoring >= 15 and whoring <= 17:  # WHORING LEVEL 06.
        if one_of_ten == 1:
            $herView.hideQQ()
            $herView.showQQ( "body_87.png", pos )
            her "Хотите, чтобы я показала вам свою грудь?"
            $herView.hideQQ()
            $herView.showQQ( "body_78.png", pos )
            her "Да... Я хочу, чтобы вы использовали меня..."
            $herView.hideQQ()
            $herView.showQQ( "body_79.png", pos )
            her "Вот настолько я самоотверженна!"
           
        elif one_of_ten == 2:
            $herView.hideQQ()
            $herView.showQQ( "body_14.png", pos )
            her "С этим ничего не подулаешь, но я чувствую себя не очень, когда домовые эльфы стирают за мной вещи..."
            $herView.hideQQ()
            $herView.showQQ( "body_87.png", pos )
            her "То есть, все эти пятна от спермы..."
            $herView.hideQQ()
            $herView.showQQ( "body_118.png", pos )

        elif one_of_ten == 3:
            $herView.hideQQ()
            $herView.showQQ( "body_02.png", pos )
            her "Не имеет значения, сколько раз вы спросите меня..."
            her "Ответ будет один и тот же..."
            $herView.hideQQ()
            $herView.showQQ( "body_47.png", pos )
            her "Я жутко возмущена \"Слизеринцами\"!"
            $herView.hideQQ()
            $herView.showQQ( "body_69.png", pos )
        
        
        elif one_of_ten == 4:
            $herView.hideQQ()
            $herView.showQQ( "body_02.png", pos )
            her "Когда я думаю обо всем, на что мне пришлось пойти в обмен на очки..."
            $herView.hideQQ()
            $herView.showQQ( "body_87.png", pos )
            her "Я чувствую себя немного неловко..."
            $herView.hideQQ()
            $herView.showQQ( "body_120.png", pos )
            her "Но так же я очень горжусь собой."
            
        elif one_of_ten == 5:
            $herView.hideQQ()
            $herView.showQQ( "body_14.png", pos )
            her "До сих пор я посвящаю очень много времени обучению..."
            her "Но не так много, как раньше..."
            $herView.hideQQ()
            $herView.showQQ( "body_11.png", pos )
            her "Вообще мне теперь не очень-то и нравится учиться..."
            $herView.hideQQ()
            $herView.showQQ( "body_13.png", pos )
        
        elif one_of_ten == 6:
            $herView.hideQQ()
            $herView.showQQ( "body_04.png", pos )
            her "Гриффиндор должен получить кубок в этому году!"
            $herView.hideQQ()
            $herView.showQQ( "body_118.png", pos )
            her "{size=-4}(Даже если это будет стоить мне моей чести...){/size}"
            $herView.hideQQ()
            $herView.showQQ( "body_120.png", pos )
           
           
        elif one_of_ten == 7:
            $herView.hideQQ()
            $herView.showQQ( "body_14.png", pos )
            her "Я ничего не имею против осенней погоды..."
            $herView.hideQQ()
            $herView.showQQ( "body_16.png", pos )
            her "Но мое любимое время года это зима."
            $herView.hideQQ()
            $herView.showQQ( "body_15.png", pos )
        
        elif one_of_ten == 8:
            $herView.hideQQ()
            $herView.showQQ( "body_14.png", pos )
            her "Раньше я смотрела свысока на девушек, которые беспокоятся о своей внешности..."
            her "Но я была не права.."
            her "Я начала понимать, насколько важно девушке выглядеть симпатичной."
            $herView.hideQQ()
            $herView.showQQ( "body_29.png", pos )
            her "..............."
            $herView.hideQQ()
            $herView.showQQ( "body_122.png", pos )
            her "С недавнего времени я на диете..."
            $herView.hideQQ()
            $herView.showQQ( "body_34.png", pos )
            $herView.hideQQ()
            $herView.showQQ( "body_33.png", pos )
       
        elif one_of_ten == 9:
            $herView.hideQQ()
            $herView.showQQ( "body_14.png", pos )
            her "Последнее время я чувствую себя довольно уверенно при мальчиках..."
            $herView.hideQQ()
            $herView.showQQ( "body_06.png", pos )
            her "Я думаю, что должна быть благодарна вам за это."
            
        elif one_of_ten == 10:
            $herView.hideQQ()
            $herView.showQQ( "body_14.png", pos )
            her "Мой любимый предмет?"
            $herView.hideQQ()
            $herView.showQQ( "body_13.png", pos )
            her "Хм..."
            $herView.hideQQ()
            $herView.showQQ( "body_14.png", pos )
            her "Думаю это \"чары\"..."
            $herView.hideQQ()
            $herView.showQQ( "body_15.png", pos )
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
    if whoring >= 18 and whoring <= 20: # WHORING LEVEL 07.
        if one_of_ten == 1:
            $herView.hideQQ()
            $herView.showQQ( "body_04.png", pos )
            her "Просто дайте знать, что вы хотите от меня сегодня, сэр."
            $herView.hideQQ()
            $herView.showQQ( "body_03.png", pos )
           
        elif one_of_ten == 2:
            $herView.hideQQ()
            $herView.showQQ( "body_11.png", pos )
            her "Я почти не учусь теперь..."
            her "Несмотря на это, моя популярность, кажется, растет..."
            $herView.hideQQ()
            $herView.showQQ( "body_13.png", pos )
            her "Хм..."
                 
        elif one_of_ten == 3:
            $herView.hideQQ()
            $herView.showQQ( "body_64.png", pos )
            her "Я бы не отказалась от бутылки сливочного пива ..."
            $herView.hideQQ()
            $herView.showQQ( "body_68.png", pos )
        
        elif one_of_ten == 4:
            $herView.hideQQ()
            $herView.showQQ( "body_06.png", pos )
            her "Что это сэр? У вас еще один подарок для меня?"
            $herView.hideQQ()
            $herView.showQQ( "body_12.png", pos )
            her "Ох... Понятно..."

        elif one_of_ten == 5:
            $herView.hideQQ()
            $herView.showQQ( "body_06.png", pos )
            her "Все в порядке, спасибо, что спросили."

        elif one_of_ten == 6:
            $herView.hideQQ()
            $herView.showQQ( "body_11.png", pos )
            her "Я выгляжу толстой?"
            $herView.hideQQ()
            $herView.showQQ( "body_29.png", pos )
            her "Надеюсь, диета сработает..."
           
        elif one_of_ten == 7:
            $herView.hideQQ()
            $herView.showQQ( "body_16.png", pos )
            her "Помню я говорила, что книги мои лучшие друзья..."
            $herView.hideQQ()
            $herView.showQQ( "body_24.png", pos )
            her "Теперь это звучит так неубедительно."
            $herView.hideQQ()
            $herView.showQQ( "body_15.png", pos )
        
        elif one_of_ten == 8:
            $herView.hideQQ()
            $herView.showQQ( "body_04.png", pos )
            her "Добавим яйца Эшвиндера..."
            her "Затем подкову и шапку красноголовика..."
            her "Затем сок морской капусты..."
            $herView.hideQQ()
            $herView.showQQ( "body_10.png", pos )
            her "Или сначала тимьян?"
            $herView.hideQQ()
            $herView.showQQ( "body_13.png", pos )
            her ".............."
            $herView.hideQQ()
            $herView.showQQ( "body_24.png", pos )
            her "Ох, какая разница?"
            $herView.hideQQ()
            $herView.showQQ( "body_06.png", pos )
       
        elif one_of_ten == 9:
            $herView.hideQQ()
            $herView.showQQ( "body_14.png", pos )
            her "Вы думаете, я нанесла достаточно макияжа?" 
            her "Если его будет слишком много, то это будет выглядеть вульгарно..."
            $herView.hideQQ()
            $herView.showQQ( "body_13.png", pos )
            her "Но и слишком мало тоже плохо..."
            $herView.hideQQ()
            $herView.showQQ( "body_12.png", pos )
            her "Я не должна выглядеть как простушка!"
            
        elif one_of_ten == 10:
            $herView.hideQQ()
            $herView.showQQ( "body_64.png", pos )
            her "Вы хотите посмотреть на мои сиськи, сэр?" 
            $herView.hideQQ()
            $herView.showQQ( "body_111.png", pos )
            her "25 очков, пожалуйста."
            $herView.hideQQ()
            $herView.showQQ( "body_120.png", pos )
    
   
    if whoring >= 21: # WHORING LEVEL 08+.
        
        if one_of_ten == 1:
            $herView.hideQQ()
            $herView.showQQ( "body_189.png", pos )
            her "У вас есть еще ненужные журналы для взрослых, сэр?"
            $herView.hideQQ()
            $herView.showQQ( "body_188.png", pos )

        elif one_of_ten == 2:
            $herView.hideQQ()
            $herView.showQQ( "body_31.png", pos )
            her "Извиняюсь, что беспокою вас..."
            her "Но не найдется ли у вас несколько презервативов?"
            $herView.hideQQ()
            $herView.showQQ( "body_34.png", pos )
            her "Конечно же, это не для меня... Для друзей..."
                 
        elif one_of_ten == 3:
            $herView.hideQQ()
            $herView.showQQ( "body_14.png", pos )
            her "В последнее время очень холодно..."
            $herView.hideQQ()
            $herView.showQQ( "body_06.png", pos )
            her "Я надеюсь, что скоро выпадет снег..."
        
        elif one_of_ten == 4:
            $herView.hideQQ()
            $herView.showQQ( "body_127.png", pos )
            her "Прыгать и кричать 'За Гриффиндор!'"
            $herView.hideQQ()
            $herView.showQQ( "body_80.png", pos )
            her "Смелые, удалые, красно-золотые!"
            $herView.hideQQ()
            $herView.showQQ( "body_06.png", pos )

        elif one_of_ten == 5:
            $herView.hideQQ()
            $herView.showQQ( "body_10.png", pos )
            her "Я надеюсь, что бал пройдет гладко..."
            $herView.hideQQ()
            $herView.showQQ( "body_13.png", pos )

        elif one_of_ten == 6:
            $herView.hideQQ()
            $herView.showQQ( "body_06.png", pos )
            her "Интересно, что наденет Джинни на бал..."
        
        elif one_of_ten == 7:
            $herView.hideQQ()
            $herView.showQQ( "body_16.png", pos )
            her "Учитывая, как теперь все устроено с очками... Вы можете продолжать меня пользовать, сэр..."
            $herView.hideQQ()
            $herView.showQQ( "body_11.png", pos )
            her "И кстати, нынче я редко надеваю белье..."
        
        elif one_of_ten == 8:
            $herView.hideQQ()
            $herView.showQQ( "body_117.png", pos )
            her "Сэр, хотите вставить свой член мне в рот?"
            $herView.hideQQ()
            $herView.showQQ( "body_135.png", pos )
            her "Сэр, я прошу вас..........."
            $herView.hideQQ()
            $herView.showQQ( "body_111.png", pos )
            her "Отлично! Пятьдесят пять очков, будьте добры!"
            $herView.hideQQ()
            $herView.showQQ( "body_122.png", pos )

        elif one_of_ten == 9:
            $herView.hideQQ()
            $herView.showQQ( "body_127.png", pos )
            her "Прочитала статью, в которой говорится о положительном влиянии спермы на кожу женщины..."
            $herView.hideQQ()
            $herView.showQQ( "body_128.png", pos )
            her "Интересно, как они это узнают..."
            $herView.hideQQ()
            $herView.showQQ( "body_122.png", pos )
            her "Журнал проводит какие-то исследования?"
            $herView.hideQQ()
            $herView.showQQ( "body_128.png", pos )

        elif one_of_ten == 10:
            $herView.hideQQ()
            $herView.showQQ( "body_127.png", pos )
            her "Это похоже на..."
            her "Сначала Гриффиндор, потом Когтевран, потом Пуффендуй..."
            $herView.hideQQ()
            $herView.showQQ( "body_186.png", pos )
            her "И Слизерин не попадает в этот список!"
            $herView.hideQQ()
            $herView.showQQ( "body_120.png", pos )

    jump day_time_requests

#    if daytime:
#        jump night_main_menu
#    else:
#        $ hermione_sleeping = True
#        jump day_main_menu            
    
