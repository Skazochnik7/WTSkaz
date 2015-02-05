label gallery:
    #play music galm fadeout 1
    scene title2
    with flashbb

    
    a1 "Добро пожаловать в галерею игры \"Воспитание Ведьмы\". Здесь вы можете посмотреть некоторые работы."
    label after_cam:
    menu:
        "- Музыкальная комната -":
            jump music_room
        
        "- Священные свитки. Часть I -":
            jump volone
        
        "- Священные свитки. Часть II -":
            jump voltwo
            
#        "- Gallery volume 02 -":
#            jump volumetwo
        
#        "- Gallery volume 03 -":
#            jump volume_three
        
        "- Окрестности Хогвартса -":
            jump out_hog
        
#        "{color=#858585}- Концовка 01 -{/color}" if not persistent.ending_01:
        "{color=#858585}- Концовка 01 -{/color}" if not (1 in persistent.endings): #end.IsPersistent(1):
            jump after_cam
#        "- Концовка 01 -" if persistent.ending_01:
        "- Концовка 01 -" if (1 in persistent.endings): #end.IsPersistent(1):
            label end_01_men:
            menu:
                "- Первый акт -":
                    jump end01_01
                "- Речь -":
                    jump end01_02
                "- Последний акт -":
                    jump end01_03
                "- Отмена -":
                    jump after_cam
        
#        "{color=#858585}- Концовка 02 -{/color}" if not persistent.ending_02:
        "{color=#858585}- Концовка 02 -{/color}" if not (2 in persistent.endings):# end.IsPersistent(2):
            jump after_cam
#        "- Концовка 02 -" if persistent.ending_02:
        "- Концовка 02 -" if (2 in persistent.endings):#end.IsPersistent(2):
            label end_02_men:
            menu:
                "- Первый акт -":
                    jump end02_01
                "- Речь -":
                    jump end02_02
                "- Последний акт -":
                    jump end02_03
                "- Отмена -":
                    jump after_cam
        
#av-2015.01.04 Ссылки на вторую концовку, переделать на третью
        "{color=#858585}- Концовка 03 -{/color}" if not (3 in persistent.endings):#end.IsPersistent(3):
            jump after_cam
        "- Концовка 03 -" if (3 in persistent.endings):#end.IsPersistent(3):
            label end_02_men:
            menu:
                "- Первый акт -":
                    jump end02_01
                "- Речь -":
                    jump end02_02
                "- Последний акт -":
                    jump end02_03
                "- Отмена -":
                    jump after_cam

            
        "- Комментарии (вкл.) -" if commentaries:
            $ commentaries = False # In the GALLERY turns commentaries ON and OFF. 
            jump after_cam
        
        "- Комментарии (выкл.) -" if not commentaries:
            $ commentaries = True # In the GALLERY turns commentaries ON and OFF. 
            jump after_cam
            
        "- Отмена -":
            return 
            
            
label volone:
    menu:
        "- С.01: [scroll_01_name] -" if persistent.ss_01:
            show image "03_hp/19_extras/01.png" with d3
            if commentaries:
                a1 "Это самый первый эскиз офиса Дамблдора."
                a1 "Не самое лучшее мое творение. Но заключает в себе великую историческую ценность."
            show screen ctc
            pause
            hide screen ctc
            hide image "03_hp/19_extras/01.png" with d3
            pass
        "- С.02: [scroll_02_name] -" if persistent.ss_02:
            show image "03_hp/19_extras/02.png" with d3
            if commentaries:
                a1 "Календарь..."
                a1 "На ранних этапах разработки я планировал сделать внутриигровой календарь и завязать на нем геймплей..."
                a1 "До тех пор, пока не понял, насколько сложнее сделать такую игру..."
                a1 "К тому же мне кажется, что любые временные рамки в любой игре мешают веселью. Так что, я бросил эту затею..."
                a1 "Позже я использовал этот рисунок как пергамент для писем..."

            show screen ctc
            pause
            hide screen ctc
            hide image "03_hp/19_extras/02.png" with d3
            pass
        "- С.03: [scroll_03_name] -" if persistent.ss_03:
            show image "03_hp/19_extras/03.png" with d3
            if commentaries:
                a1 "Несколько самых ранних набросков Гермионы..."
            show screen ctc
            pause
            hide screen ctc
            hide image "03_hp/19_extras/03.png" with d3
            pass
            
        "- С.04: [scroll_04_name] -" if persistent.ss_04:
            show image "03_hp/19_extras/04.png" with d3
            if commentaries:
                a1 "Сцена с глубоким заглотом..."
                a1 "Моя первая попытка."
                a1 "Была признана негодной и оставлена как есть."
            show screen ctc
            pause
            hide screen ctc
            hide image "03_hp/19_extras/04.png" with d3
            pass
            
        "- С.05: [scroll_05_name] -" if persistent.ss_05:
            show image "03_hp/19_extras/05.png" with d3
            if commentaries:
                a1 "Постер игры..."
                a1 "Гермиона - работа Dahr. Остальное - моя..."
            show screen ctc
            pause
            hide screen ctc
            hide image "03_hp/19_extras/05.png" with d3
            pass
            
        "- С.06: [scroll_06_name] -" if persistent.ss_06:
            show image "03_hp/19_extras/06.png" with d3
            if commentaries:
                a1 "Альтернативный постер игры."
                a1 "Этот так и не был выпущен."
            show screen ctc
            pause
            hide screen ctc
            hide image "03_hp/19_extras/06.png" with d3
            pass
            
        "- С.07: [scroll_07_name] -" if persistent.ss_07:
            show image "03_hp/19_extras/07.png" with d3
            if commentaries:
                a1 "Несколько чибиков крупным планом."
                a1 "Они так и не попали в игру..."
            show screen ctc
            pause
            hide screen ctc
            hide image "03_hp/19_extras/07.png" with d3
            pass
            
        "- С.08: [scroll_08_name] -" if persistent.ss_08:
            show image "03_hp/19_extras/08.png" with d3
            if commentaries:
                a1 "Куча вещей, которых я так и не использовал..."
                a1 "Все из-за dahr и его шикарных рисунков."

            show screen ctc
            pause
            hide screen ctc
            hide image "03_hp/19_extras/08.png" with d3
            pass
            
        "- С.09: [scroll_09_name] -" if persistent.ss_09:
            show image "03_hp/19_extras/09.png" with d3
            if commentaries:
                a1 "Рисунок Гермионы с постера. (by Dahr)"
                a1 "Мне больше нравится правая - та, что с трусиками."
            show screen ctc
            pause
            hide screen ctc
            hide image "03_hp/19_extras/09.png" with d3
            pass
            
        "- С.10: [scroll_10_name] -" if persistent.ss_10:
            show image "03_hp/19_extras/10.png" with d3
            if commentaries:
                a1 "Опять вещи, что так и не вошли в игру..."
                a1 "Идея была в том, что чем больше ты бы прокачивал Гермиону, тем больше прищепок она давала бы на себя нацепить..."
                a1 "А цепь для сосков она должна была бы носить во время уроков под своей формой."
    
            show screen ctc
            pause
            hide screen ctc
            hide image "03_hp/19_extras/10.png" with d3
            pass
            
        "- С.11: [scroll_11_name] -" if persistent.ss_11:
            show image "03_hp/19_extras/11.png" with d3
            if commentaries:
                a1 "Бордель домовых... Еще одна вещь, которая так и не сбылась."
            show screen ctc
            pause
            hide screen ctc
            hide image "03_hp/19_extras/11.png" with d3
            pass
            
        "- С.12: [scroll_12_name] -" if persistent.ss_12:
            show image "03_hp/19_extras/12.png" with d3
            if commentaries:
                a1 "Рисунок, где ты очень похож на мага из Дурмстранга, а Лола - на ученицу..."
                a2 "Рисунок рисовал Dahr, конечно."
            show screen ctc
            pause
            hide screen ctc
            hide image "03_hp/19_extras/12.png" with d3
            pass
        
        
        "- С.13: [scroll_13_name] -" if persistent.ss_13:
            show image "03_hp/19_extras/13.png" with d3
            if commentaries:
                a1 "Еще один побочный квест, так и не увидевший свет..."
                a1 "В общем, там-"
                a1 "Нет, пожалуй, нет. Кто знает, быть может мы все-таки введем эти квесты."
            show screen ctc
            pause
            hide screen ctc
            hide image "03_hp/19_extras/13.png" with d3
            pass
        
        "- С.14: [scroll_14_name] -" if persistent.ss_14:
            show image "03_hp/19_extras/14.png" with d3
            if commentaries:
                a1 "Еще один побочный квест..."
                a1 "Этот про волшебный шахматный клуб."
            show screen ctc
            pause
            hide screen ctc
            hide image "03_hp/19_extras/14.png" with d3
            pass
        
        "- С.15: [scroll_15_name] -" if persistent.ss_15:
            show image "03_hp/19_extras/15.png" with d3
            if commentaries:
                a1 "Существует множество способов того, как симпатичная девушка может держать книгу."
                a1 "Я думал, что было бы круто, если бы Гермиона начинала носить держать книги по-другому по мере того, как она учится все новому."
                a1 "Так как вся ветка с репетиторством была отменена, я выкладываю это здесь..."
            show screen ctc
            pause
            hide screen ctc
            hide image "03_hp/19_extras/15.png" with d3
            pass
        
        "Ничего":
            jump after_cam
        
    jump volone
        
        
        
        
label voltwo:
    menu:
        "- С.16: [scroll_16_name] -" if persistent.ss_16:
            show image "03_hp/19_extras/16.png" with d3
            if commentaries:
                a1 "Парочка вещей, что не попали в финальную версию..."
                a1 "Слева действительно настоящий живой домовой, которого можно подарить."
                a1 "Справа портрет извращенного, но мудрого мага. Должен был помогать с учебой..."

            show screen ctc
            pause
            hide screen ctc
            hide image "03_hp/19_extras/16.png" with d3
            pass
        "- С.17: [scroll_17_name] -" if persistent.ss_17:
            show image "03_hp/19_extras/17.png" with d3
            if commentaries:
                #17.
                a1 "Еще несколько вещиц..."
                a1 "Газета, флакон духов и волшебная шляпа, которая говорит то, что ты хочешь услышать..."

            show screen ctc
            pause
            hide screen ctc
            hide image "03_hp/19_extras/17.png" with d3
            pass
        "- С.18: [scroll_18_name] -" if persistent.ss_18:
            show image "03_hp/19_extras/18.png" with d3
            if commentaries:
                 #18.
                a1 "Книги..."
                a1 "Верхний ряд - мои наброски, нижний ряд - законченный изображения от dahr."
            show screen ctc
            pause
            hide screen ctc
            hide image "03_hp/19_extras/18.png" with d3
            pass
            
        "- С.19: [scroll_19_name] -" if persistent.ss_19:
            show image "03_hp/19_extras/19.png" with d3
            if commentaries:
                #19.
                a1 "Известная певица."
                a1 "Не имеет отношения игре, добавлена сюда без причины, просто так."
            show screen ctc
            pause
            hide screen ctc
            hide image "03_hp/19_extras/19.png" with d3
            pass
            
        "- С.20: [scroll_20_name] -" if persistent.ss_20:
            show image "03_hp/19_extras/20.png" with d3
            if commentaries:
                #20.
                a1 "Я потратил прилично времени, чтобы дать Гермионе подходящую внешность..."
                a1 "Версия \"A\" была моей первой попыткой. И она мне нравилась, пока я не начал ее ненавидеть..."
                a2 "Версия \"B\" была моей второй попыткой. И она хороша. Но ее самоуверенные и полуагрессивные черты не совсем подходили героине..."
                a1 "Версия \C\" та, что прошла кастинг. Гермиона которую мы вырастили и о которой будем заботиться, я уверен."
            show screen ctc
            pause
            hide screen ctc
            hide image "03_hp/19_extras/20.png" with d3
            pass
            
        "- С.21: [scroll_21_name] -" if persistent.ss_21:
            show image "03_hp/19_extras/21.png" with d3
            if commentaries:
                #21 
                a1 "Побочный квест, которого нет."
                a1 "Вам позволено жалеть, что торопили меня."
                a1 "Если вы не торопили меня, вам позволено злиться на тех, кто торопил."

            show screen ctc
            pause
            hide screen ctc
            hide image "03_hp/19_extras/21.png" with d3
            pass
            
        "- С.22: [scroll_22_name] -" if persistent.ss_22:
            show image "03_hp/19_extras/22.png" with d3
            if commentaries:
                #22
                a1 "Гермиона дарит свое тело Джинни..."
                a1 "Это была бы запоминающаяся сцена..."

            show screen ctc
            pause
            hide screen ctc
            hide image "03_hp/19_extras/22.png" with d3
            pass
            
        "- С.23: [scroll_23_name] -" if persistent.ss_23:
            show image "03_hp/19_extras/23.png" with d3
            if commentaries:
                #23. 
                a1 "Не ожидали, ага?"
                a1 "Это все еще Гермиона, если вам любопытно."
            show screen ctc
            pause
            hide screen ctc
            hide image "03_hp/19_extras/23.png" with d3
            pass
            
        "- С.24: [scroll_24_name] -" if persistent.ss_24:
            show image "03_hp/19_extras/24.png" with d3
            if commentaries:
                #24.
                a1 "................................."
                a1 "Сайд-квест, конечно..."
            show screen ctc
            pause
            hide screen ctc
            hide image "03_hp/19_extras/24.png" with d3
            pass
            
        "- С.25: [scroll_25_name] -" if persistent.ss_25:
            show image "03_hp/19_extras/25.png" with d3
            if commentaries:
                #25.
                a1 "Еще один сайд-квест..."
                a1 "Мы много спорили с Dahr о нем..."
                a1 "Я был против квеста, но потом Dahr отправил мне картинки, чем заставил меня заткнуться."
            show screen ctc
            pause
            hide screen ctc
            hide image "03_hp/19_extras/25.png" with d3
            pass
            
        "- С.26: [scroll_26_name] -" if persistent.ss_26:
            show image "03_hp/19_extras/26.png" with d3
            if commentaries:
                #26.
                a1 "На самых ранних стадиях разработки у меня была идея показывать последствия проваленных или успешно выполненых сайд-квестов в виде упрощенных изображений, или фотографий..."
                a1 "Поначалу многие сайд-квесты давали игроку выбор, как потратить бюджет Хогвартса..."
                a1 "Потратить деньги на финансирование школьной команды по квиддичу, или на наем новых учителей? Ну, и в таком духе..."
            show screen ctc
            pause
            hide screen ctc
            hide image "03_hp/19_extras/26.png" with d3
            pass
            
        "- С.27: [scroll_27_name] -" if persistent.ss_27:
            show image "03_hp/19_extras/27.png" with d3
            if commentaries:
                #27.
                a1 "Ну разве она не милашка?"

            show screen ctc
            pause
            hide screen ctc
            hide image "03_hp/19_extras/27.png" with d3
            pass

        
        "- С.28: [scroll_28_name] -" if persistent.ss_28:
            show image "03_hp/19_extras/28.png" with d3
            if commentaries:
                #28.
                a1 "Очередной (довольно большой) сайд-квест..."
            show screen ctc
            pause
            hide screen ctc
            hide image "03_hp/19_extras/28.png" with d3
            pass
        
        "- С.29: [scroll_29_name] -" if persistent.ss_29:
            show image "03_hp/19_extras/29.png" with d3
            if commentaries:
                #29.
                a1 ".........."
            show screen ctc
            pause
            hide screen ctc
            hide image "03_hp/19_extras/29.png" with d3
            pass
        
        "- С.30: [scroll_30_name] -" if persistent.ss_30:
            show image "03_hp/19_extras/30.png" with d3
            if commentaries:
                #30.
                a1 "Одни из самых ранних набросков по сайд-квесту школьной команды по квиддичу..."
            show screen ctc
            pause
            hide screen ctc
            hide image "03_hp/19_extras/30.png" with d3
            pass
        
        "\"Ничего\"":
            jump after_cam
        
    jump voltwo
    
        
        
        
        
        
    
            
               


                

                

                
                
                

                

                

                

                
                

                

                


        
            
            
            
            
        
        
        
        
        
        
        
        
        
    ### OUTSKIRTS OF HOGWARTS CGs ###
label out_hog:
    show image  "03_hp/17_ending/171.png" with d3
    show screen ctc
    pause
    
    show image  "03_hp/17_ending/172.png" with d3
    show screen ctc
    pause

    

    show image  "03_hp/17_ending/173.png" 
    with d3
    pause
    
    hide image  "03_hp/17_ending/173.png" 
    hide image  "03_hp/17_ending/172.png" 
    show image  "03_hp/17_ending/174.png" 
    with d3
    pause
    
    hide image  "03_hp/17_ending/174.png" 
    show image  "03_hp/17_ending/175.png" 
    with d3
    pause
    

    hide image  "03_hp/17_ending/175.png" with d3
    
    pause
    
    hide image  "03_hp/17_ending/171.png" 
    hide screen ctc
    with fade
    
    jump after_cam
        
        
        
    ### ENDING 01_01
label end01_01:
    show image  "03_hp/17_ending/01.png" with d3
    show screen ctc
    pause
    
    hide image  "03_hp/17_ending/01.png" 
    show image  "03_hp/17_ending/02.png" 
    with d3
    pause
    
    hide image  "03_hp/17_ending/02.png" 
    show image  "03_hp/17_ending/03.png" 
    with d3
    pause
    
    hide image  "03_hp/17_ending/03.png" 
    show image  "03_hp/17_ending/04.png" 
    with d3
    pause
        
    hide image  "03_hp/17_ending/04.png" 
    show image  "03_hp/17_ending/05.png" 
    with d3
    pause
        
    hide image  "03_hp/17_ending/05.png" 
    show image  "03_hp/17_ending/06.png" 
    with d3
    pause    
        
    hide image  "03_hp/17_ending/06.png" 
    show image  "03_hp/17_ending/07.png" 
    with d3
    pause    
        
    hide image  "03_hp/17_ending/07.png" 
    show image  "03_hp/17_ending/08.png" 
    with d3
    pause
    
    hide image  "03_hp/17_ending/08.png" 
    show image  "03_hp/17_ending/09.png" 
    with d3
    pause
    
    hide image  "03_hp/17_ending/09.png" 
    show image  "03_hp/17_ending/10.png" 
    with d3
    pause
    
    hide image  "03_hp/17_ending/10.png" 
    show image  "03_hp/17_ending/11.png" 
    with d3
    pause
    
    hide image  "03_hp/17_ending/11.png" 
    show image  "03_hp/17_ending/12.png" 
    with d3
    pause
    
    hide image  "03_hp/17_ending/12.png" 
    show image  "03_hp/17_ending/13.png" 
    with d3
    pause
    
    hide image  "03_hp/17_ending/13.png" 
    show image  "03_hp/17_ending/14.png" 
    with d3
    pause
        
    hide image  "03_hp/17_ending/14.png" 
    show image  "03_hp/17_ending/15.png" 
    with d3
    pause
       
    hide image  "03_hp/17_ending/15.png" 
    show image  "03_hp/17_ending/16.png" 
    with d3
    pause   
       
    hide image  "03_hp/17_ending/16.png" 
    show image  "03_hp/17_ending/17.png" 
    with d3
    pause   
       
    hide image  "03_hp/17_ending/17.png" 
    show image  "03_hp/17_ending/18.png" 
    with d3
    pause   
       
    hide image  "03_hp/17_ending/18.png" 
    show image  "03_hp/17_ending/19.png" 
    with d3
    pause   
       
    hide image  "03_hp/17_ending/19.png" 
    show image  "03_hp/17_ending/20.png" 
    with d3
    pause   
       
    hide image  "03_hp/17_ending/20.png" 
    show image  "03_hp/17_ending/21.png" 
    with d3
    pause   
       
    hide image  "03_hp/17_ending/21.png" 
    show image  "03_hp/17_ending/22.png" 
    with d3
    pause
       
    hide image  "03_hp/17_ending/22.png" 
    show image  "03_hp/17_ending/23.png" 
    with d3
    pause
    
    hide image  "03_hp/17_ending/23.png" 
    show image  "03_hp/17_ending/24.png" 
    with d3
    pause
    
    hide image  "03_hp/17_ending/24.png" 
    show image  "03_hp/17_ending/25.png" 
    with d3
    pause
    
    hide image  "03_hp/17_ending/25.png" 
    show image  "03_hp/17_ending/26.png" 
    with d3
    pause
    
    hide image  "03_hp/17_ending/26.png" 
    show image  "03_hp/17_ending/27.png" 
    with d3
    pause
    
    hide image  "03_hp/17_ending/27.png" 
    show image  "03_hp/17_ending/28.png" 
    with d3
    pause
    
    hide image  "03_hp/17_ending/28.png" 
    show image  "03_hp/17_ending/29.png" 
    with d3
    pause
    
    hide image  "03_hp/17_ending/29.png" 
    show image  "03_hp/17_ending/30.png" 
    with d3
    pause
    
    hide image  "03_hp/17_ending/30.png" 
    show image  "03_hp/17_ending/31.png" 
    with d3
    pause
    
    hide image  "03_hp/17_ending/31.png" 
    show image  "03_hp/17_ending/32.png" 
    with d3
    pause
    
    hide image  "03_hp/17_ending/32.png" 
    show image  "03_hp/17_ending/33.png" 
    with d3
    pause
    
    hide image  "03_hp/17_ending/33.png" 
    show image  "03_hp/17_ending/34.png" 
    with d3
    pause
    
    hide image  "03_hp/17_ending/34.png" 
    show image  "03_hp/17_ending/35.png" 
    with d3
    pause
       
    hide image  "03_hp/17_ending/35.png" 
    show image  "03_hp/17_ending/36.png" 
    with d3
    pause
       
    hide image  "03_hp/17_ending/36.png" 
    with fade
    jump end_01_men
        

    ### ENDING 01_02
label end01_02:
    show image  "03_hp/17_ending/37.png" with d3
    show screen ctc
    pause
    
    hide image  "03_hp/17_ending/37.png" 
    show image  "03_hp/17_ending/38.png" 
    with d3
    pause

    hide image  "03_hp/17_ending/38.png" 
    show image  "03_hp/17_ending/39.png" 
    with d3
    pause
    
    hide image  "03_hp/17_ending/39.png" 
    show image  "03_hp/17_ending/40.png" 
    with d3
    pause
    
    hide image  "03_hp/17_ending/40.png" 
    show image  "03_hp/17_ending/41.png" 
    with d3
    pause
    
    hide image  "03_hp/17_ending/41.png" 
    show image  "03_hp/17_ending/42.png" 
    with d3
    pause
    
    hide image  "03_hp/17_ending/42.png" 
    show image  "03_hp/17_ending/43.png" 
    with d3
    pause
    
    hide image  "03_hp/17_ending/43.png" 
    show image  "03_hp/17_ending/44.png" 
    with d3
    pause
    
    hide image  "03_hp/17_ending/44.png" 
    show image  "03_hp/17_ending/45.png" 
    with d3
    pause
    
    hide image  "03_hp/17_ending/45.png" 
    with fade
    jump end_01_men
    
    
    
    
   ### ENDING 01_03
label end01_03:
    show image  "03_hp/17_ending/46.png" with d3
    show screen ctc
    pause
    
    hide image  "03_hp/17_ending/46.png" 
    show image  "03_hp/17_ending/47.png" 
    with d3
    pause
    
    hide image  "03_hp/17_ending/47.png" 
    show image  "03_hp/17_ending/48.png" 
    with d3
    pause
    
    hide image  "03_hp/17_ending/48.png" 
    show image  "03_hp/17_ending/49.png" 
    with d3
    pause
    
    hide image  "03_hp/17_ending/49.png" 
    show image  "03_hp/17_ending/50.png" 
    with d3
    pause
    
    hide image  "03_hp/17_ending/50.png" 
    show image  "03_hp/17_ending/51.png" 
    with d3
    pause
    
    hide image  "03_hp/17_ending/51.png" 
    show image  "03_hp/17_ending/52.png" 
    with d3
    pause
    
    hide image  "03_hp/17_ending/52.png" 
    show image  "03_hp/17_ending/53.png" 
    with d3
    pause
    
    hide image  "03_hp/17_ending/53.png" 
    show image  "03_hp/17_ending/54.png" 
    with d3
    pause
    
    hide image  "03_hp/17_ending/54.png" 
    show image  "03_hp/17_ending/55.png" 
    with d3
    pause
    
    hide image  "03_hp/17_ending/55.png" 
    show image  "03_hp/17_ending/56.png" 
    with d3
    pause
    
    hide image  "03_hp/17_ending/56.png" 
    show image  "03_hp/17_ending/57.png" 
    with d3
    pause
    
    hide image  "03_hp/17_ending/57.png" 
    show image  "03_hp/17_ending/58.png" 
    with d3
    pause
    hide image  "03_hp/17_ending/58.png" 
    show image  "03_hp/17_ending/59.png" 
    with d3
    pause
    hide image  "03_hp/17_ending/59.png" 
    show image  "03_hp/17_ending/60.png" 
    with d3
    pause
    
    hide image  "03_hp/17_ending/60.png" 
    show image  "03_hp/17_ending/61.png" 
    with d3
    pause
    
    hide image  "03_hp/17_ending/61.png" 
    show image  "03_hp/17_ending/62.png" 
    with d3
    pause
    
    hide image  "03_hp/17_ending/62.png" 
    show image  "03_hp/17_ending/63.png" 
    with d3
    pause
    
    hide image  "03_hp/17_ending/63.png" 
    show image  "03_hp/17_ending/64.png" 
    with d3
    pause
    
    hide image  "03_hp/17_ending/64.png" 
    show image  "03_hp/17_ending/65.png" 
    with d3
    pause
    
    hide image  "03_hp/17_ending/65.png" 
    show image  "03_hp/17_ending/66.png" 
    with d3
    pause
    
    
    hide image  "03_hp/17_ending/66.png" 
    show image  "03_hp/17_ending/67.png" 
    with d3
    pause
    
    hide image  "03_hp/17_ending/67.png" 
    show image  "03_hp/17_ending/68.png" 
    with d3
    pause
    
    hide image  "03_hp/17_ending/68.png" 
    show image  "03_hp/17_ending/69.png" 
    with d3
    pause
    
    hide image  "03_hp/17_ending/69.png" 
    show image  "03_hp/17_ending/70.png" 
    with d3
    pause
    
    hide image  "03_hp/17_ending/70.png" 
    show image  "03_hp/17_ending/71.png" 
    with d3
    pause
    
    hide image  "03_hp/17_ending/71.png" 
    show image  "03_hp/17_ending/72.png" 
    with d3
    pause
    
    hide image  "03_hp/17_ending/72.png" 
    show image  "03_hp/17_ending/73.png" 
    with d3
    pause
    
    hide image  "03_hp/17_ending/73.png" 
    show image  "03_hp/17_ending/74.png" 
    with d3
    pause
    
    hide image  "03_hp/17_ending/74.png" 
    show image  "03_hp/17_ending/75.png" 
    with d3
    pause
    
    hide image  "03_hp/17_ending/75.png" 
    show image  "03_hp/17_ending/76.png" 
    with d3
    pause
    
    hide image  "03_hp/17_ending/76.png" 
    show image  "03_hp/17_ending/77.png" 
    with d3
    pause
    
    hide image  "03_hp/17_ending/77.png" 
    show image  "03_hp/17_ending/78.png" 
    with d3
    pause
    
    hide image  "03_hp/17_ending/78.png" 
    show image  "03_hp/17_ending/79.png" 
    with d3
    pause
    
    hide image  "03_hp/17_ending/79.png" 
    show image  "03_hp/17_ending/80.png" 
    with d3
    pause
    
    hide image  "03_hp/17_ending/80.png" 
    show image  "03_hp/17_ending/81.png" 
    with d3
    pause
    
    hide image  "03_hp/17_ending/81.png" 
    show image  "03_hp/17_ending/82.png" 
    with d3
    pause
    
    hide image  "03_hp/17_ending/82.png" 
    show image  "03_hp/17_ending/83.png" 
    with d3
    pause
    
    hide image  "03_hp/17_ending/83.png" 
    show image  "03_hp/17_ending/84.png" 
    with d3
    pause
    
    hide image  "03_hp/17_ending/84.png" 
    show image  "03_hp/17_ending/85.png" 
    with d3
    pause
    
    hide image  "03_hp/17_ending/85.png" 
    show image  "03_hp/17_ending/86.png" 
    with d3
    pause
    
    hide image  "03_hp/17_ending/86.png" 
    show image  "03_hp/17_ending/87.png" 
    with d3
    pause
    
    hide image  "03_hp/17_ending/87.png" 
    show image  "03_hp/17_ending/88.png" 
    with d3
    pause
    
    hide image  "03_hp/17_ending/88.png" 
    show image  "03_hp/17_ending/89.png" 
    with d3
    pause
    
    hide image  "03_hp/17_ending/89.png" 
    with fade
    jump end_01_men
    
    
      ### ENDING 02_01
label end02_01:
    show image  "03_hp/17_ending/01.png" with d3
    show screen ctc
    pause
    
    hide image  "03_hp/17_ending/01.png" 
    show image  "03_hp/17_ending/02.png" 
    with d3
    pause
    
    hide image  "03_hp/17_ending/02.png" 
    show image  "03_hp/17_ending/03.png" 
    with d3
    pause
    
    hide image  "03_hp/17_ending/03.png" 
    show image  "03_hp/17_ending/91.png" 
    with d3
    pause

    hide image  "03_hp/17_ending/91.png" 
    show image  "03_hp/17_ending/92.png" 
    with d3
    pause
    
    hide image  "03_hp/17_ending/92.png" 
    show image  "03_hp/17_ending/93.png" 
    with d3
    pause
    
    hide image  "03_hp/17_ending/93.png" 
    show image  "03_hp/17_ending/94.png" 
    with d3
    pause
    
    hide image  "03_hp/17_ending/94.png" 
    show image  "03_hp/17_ending/95.png" 
    with d3
    pause
    
    hide image  "03_hp/17_ending/95.png" 
    show image  "03_hp/17_ending/96.png" 
    with d3
    pause
    
    hide image  "03_hp/17_ending/96.png" 
    show image  "03_hp/17_ending/97.png" 
    with d3
    pause
    
    hide image  "03_hp/17_ending/97.png" 
    show image  "03_hp/17_ending/98.png" 
    with d3
    pause
    
    hide image  "03_hp/17_ending/98.png" 
    show image  "03_hp/17_ending/99.png" 
    with d3
    pause
    
    hide image  "03_hp/17_ending/99.png" 
    show image  "03_hp/17_ending/100.png" 
    with d3
    pause
    
    hide image  "03_hp/17_ending/100.png" 
    show image  "03_hp/17_ending/101.png" 
    with d3
    pause
    
    hide image  "03_hp/17_ending/101.png" 
    show image  "03_hp/17_ending/102.png" 
    with d3
    pause
    
    hide image  "03_hp/17_ending/102.png" 
    show image  "03_hp/17_ending/103.png" 
    with d3
    pause
    
    hide image  "03_hp/17_ending/103.png" 
    show image  "03_hp/17_ending/104.png" 
    with d3
    pause
    
    hide image  "03_hp/17_ending/104.png" 
    show image  "03_hp/17_ending/105.png" 
    with d3
    pause
    
    hide image  "03_hp/17_ending/105.png" 
    show image  "03_hp/17_ending/106.png" 
    with d3
    pause
    
    hide image  "03_hp/17_ending/106.png" 
    show image  "03_hp/17_ending/107.png" 
    with d3
    pause
    
    hide image  "03_hp/17_ending/107.png" 
    with fade
    jump end_02_men
    

    
      ### ENDING 02_02
label end02_02:
    show image  "03_hp/17_ending/108.png" with d3
    show screen ctc
    pause
    
    hide image  "03_hp/17_ending/108.png" 
    show image  "03_hp/17_ending/109.png" 
    with d3
    pause
    
    hide image  "03_hp/17_ending/109.png" 
    show image  "03_hp/17_ending/110.png" 
    with d3
    pause
    
    hide image  "03_hp/17_ending/110.png" 
    show image  "03_hp/17_ending/111.png" 
    with d3
    pause
    
    hide image  "03_hp/17_ending/111.png" 
    show image  "03_hp/17_ending/112.png" 
    with d3
    pause
    
    hide image  "03_hp/17_ending/112.png" 
    show image  "03_hp/17_ending/113.png" 
    with d3
    pause
    
    hide image  "03_hp/17_ending/113.png" 
    show image  "03_hp/17_ending/114.png" 
    with d3
    pause
    
    hide image  "03_hp/17_ending/114.png" 
    show image  "03_hp/17_ending/115.png" 
    with d3
    pause
    
    hide image  "03_hp/17_ending/115.png" 
    show image  "03_hp/17_ending/116.png" 
    with d3
    pause
    
    hide image  "03_hp/17_ending/116.png" 
    show image  "03_hp/17_ending/117.png" 
    with d3
    pause
    
    hide image  "03_hp/17_ending/117.png" 
    show image  "03_hp/17_ending/118.png" 
    with d3
    pause
    
    hide image  "03_hp/17_ending/118.png" 
    show image  "03_hp/17_ending/119.png" 
    with d3
    pause
    
    hide image  "03_hp/17_ending/119.png" 
    show image  "03_hp/17_ending/120.png" 
    with d3
    pause
    hide image  "03_hp/17_ending/120.png" 
    show image  "03_hp/17_ending/121.png" 
    with d3
    pause
    
    hide image  "03_hp/17_ending/121.png" 
    show image  "03_hp/17_ending/122.png" 
    with d3
    pause
    
    hide image  "03_hp/17_ending/122.png" 
    show image  "03_hp/17_ending/123.png" 
    with d3
    pause
    
    hide image  "03_hp/17_ending/123.png" 
    with fade
    jump end_02_men


         ### ENDING 02_03
label end02_03:
    show image  "03_hp/17_ending/124.png" with d3
    show screen ctc
    pause
    
    hide image  "03_hp/17_ending/124.png" 
    show image  "03_hp/17_ending/125.png" 
    with d3
    pause
    
    hide image  "03_hp/17_ending/125.png" 
    show image  "03_hp/17_ending/126.png" 
    with d3
    pause
    
    hide image  "03_hp/17_ending/126.png" 
    show image  "03_hp/17_ending/127.png" 
    with d3
    pause
    
    hide image  "03_hp/17_ending/127.png" 
    show image  "03_hp/17_ending/128.png" 
    with d3
    pause
    
    hide image  "03_hp/17_ending/128.png" 
    show image  "03_hp/17_ending/129.png" 
    with d3
    pause
    
    hide image  "03_hp/17_ending/129.png" 
    show image  "03_hp/17_ending/130.png" 
    with d3
    pause
    
    hide image  "03_hp/17_ending/130.png" 
    show image  "03_hp/17_ending/131.png" 
    with d3
    pause
    
    hide image  "03_hp/17_ending/131.png" 
    show image  "03_hp/17_ending/132.png" 
    with d3
    pause
    
    hide image  "03_hp/17_ending/132.png" 
    show image  "03_hp/17_ending/133.png" 
    with d3
    pause
    
    hide image  "03_hp/17_ending/133.png" 
    show image  "03_hp/17_ending/134.png" 
    with d3
    pause
    
    hide image  "03_hp/17_ending/134.png" 
    show image  "03_hp/17_ending/135.png" 
    with d3
    pause
    
    hide image  "03_hp/17_ending/135.png" 
    show image  "03_hp/17_ending/136.png" 
    with d3
    pause
    
    hide image  "03_hp/17_ending/136.png" 
    show image  "03_hp/17_ending/137.png" 
    with d3
    pause
    hide image  "03_hp/17_ending/137.png" 
    show image  "03_hp/17_ending/138.png" 
    with d3
    pause
    
    hide image  "03_hp/17_ending/138.png" 
    show image  "03_hp/17_ending/139.png" 
    with d3
    pause
    
    hide image  "03_hp/17_ending/139.png" 
    show image  "03_hp/17_ending/140.png" 
    with d3
    pause
    
    hide image  "03_hp/17_ending/140.png" 
    show image  "03_hp/17_ending/141.png" 
    with d3
    pause
    
    hide image  "03_hp/17_ending/141.png" 
    show image  "03_hp/17_ending/142.png" 
    with d3
    pause
    
    hide image  "03_hp/17_ending/142.png" 
    show image  "03_hp/17_ending/143.png" 
    with d3
    pause
    
    hide image  "03_hp/17_ending/143.png" 
    show image  "03_hp/17_ending/144.png" 
    with d3
    pause
    
    hide image  "03_hp/17_ending/144.png" 
    show image  "03_hp/17_ending/145.png" 
    with d3
    pause
    
    hide image  "03_hp/17_ending/145.png" 
    show image  "03_hp/17_ending/146.png" 
    with d3
    pause
    
    hide image  "03_hp/17_ending/146.png" 
    show image  "03_hp/17_ending/147.png" 
    with d3
    pause
    
    hide image  "03_hp/17_ending/147.png" 
    show image  "03_hp/17_ending/148.png" 
    with d3
    pause
    hide image  "03_hp/17_ending/148.png" 
    show image  "03_hp/17_ending/149.png" 
    with d3
    pause
    
    hide image  "03_hp/17_ending/149.png" 
    show image  "03_hp/17_ending/150.png" 
    with d3
    pause
    
    hide image  "03_hp/17_ending/150.png" 
    show image  "03_hp/17_ending/151.png" 
    with d3
    pause
    
    hide image  "03_hp/17_ending/151.png" 
    show image  "03_hp/17_ending/152.png" 
    with d3
    pause
    
    hide image  "03_hp/17_ending/152.png" 
    show image  "03_hp/17_ending/153.png" 
    with d3
    pause
    
    hide image  "03_hp/17_ending/153.png" 
    show image  "03_hp/17_ending/154.png" 
    with d3
    pause
    
    hide image  "03_hp/17_ending/154.png" 
    show image  "03_hp/17_ending/155.png" 
    with d3
    pause
    
    hide image  "03_hp/17_ending/155.png" 
    show image  "03_hp/17_ending/156.png" 
    with d3
    pause
    
    hide image  "03_hp/17_ending/156.png" 
    show image  "03_hp/17_ending/157.png" 
    with d3
    pause
    
    hide image  "03_hp/17_ending/157.png" 
    show image  "03_hp/17_ending/158.png" 
    with d3
    pause
    
    hide image  "03_hp/17_ending/158.png" 
    show image  "03_hp/17_ending/159.png" 
    with d3
    pause
    
    hide image  "03_hp/17_ending/159.png" 
    show image  "03_hp/17_ending/160.png" 
    with d3
    pause
    
    hide image  "03_hp/17_ending/160.png" 
    show image  "03_hp/17_ending/161.png" 
    with d3
    pause
    
    hide image  "03_hp/17_ending/161.png" 
    show image  "03_hp/17_ending/162.png" 
    with d3
    pause
    
    hide image  "03_hp/17_ending/162.png" 
    show image  "03_hp/17_ending/163.png" 
    with d3
    pause
    
    hide image  "03_hp/17_ending/163.png" 
    show image  "03_hp/17_ending/164.png" 
    with d3
    pause
    
    hide image  "03_hp/17_ending/164.png" 
    show image  "03_hp/17_ending/165.png" 
    with d3
    pause
    
    hide image  "03_hp/17_ending/165.png" 
    show image  "03_hp/17_ending/166.png" 
    with d3
    pause
    
    hide image  "03_hp/17_ending/166.png" 
    show image  "03_hp/17_ending/167.png" 
    with d3
    pause
    
    hide image  "03_hp/17_ending/167.png" 
    show image  "03_hp/17_ending/168.png" 
    with d3
    pause
    
    hide image  "03_hp/17_ending/168.png" 
    show image  "03_hp/17_ending/169.png" 
    with d3
    pause
    
    hide image  "03_hp/17_ending/169.png" 
    show image  "03_hp/17_ending/170.png" 
    with d3
    pause
    
    hide image  "03_hp/17_ending/170.png" 
    with fade
    jump end_02_men

    
    
    
    ### INTRO ###
    label intro:
        play music "music/TheKiss.mp3" fadein 1 fadeout 1 
        
        centered "{size=+7}{color=#cbcbcb}Ранее в  \"МАГИЧЕСКОЙ ЛАВКЕ\"...{/color}{/size}"
        show intro_01 with flashbb # WHITE FLASH.
        pause
        hide intro_01 
        show intro_02 
        with flashbulb # WHITE FLASH.
        pause
        hide intro_02 
        show intro_03
        with flashbulb # WHITE FLASH.
        pause
        hide intro_03 
        show intro_04 
        with flashbulb # WHITE FLASH.
        pause
        hide intro_04 
        show intro_05 
        with flashbulb # WHITE FLASH.
        pause
        hide intro_05 
        show intro_06 
        with hpunch
        pause
        hide intro_06 
        with flashbulb # WHITE FLASH.
        
        centered "{size=+7}{color=#cbcbcb}И теперь в \"Воспитании Ведьмы\"...{/color}{/size}"
        jump hp
        
        
    ### MUSIC ROOM ###
label music_room:
    $ d_flag_01 = False
    $ d_flag_02 = False
    $ d_flag_03 = False
    $ d_flag_04 = False
    $ d_flag_05 = False
    $ d_flag_06 = False
    $ d_flag_07 = False
    $ d_flag_08 = False
    $ d_flag_09 = False
    $ d_flag_10 = False
    $ d_flag_11 = False
    $ d_flag_12 = False
    $ d_flag_13 = False
    $ d_flag_14 = False
    $ d_flag_15 = False
    
    label music_room2:
        pass
    
    menu:
        "{image=note2.png} Playful Tension by Shadow16nh {image=note2.png}" if d_flag_01:
            pass
        "Playful Tension by Shadow16nh" if not d_flag_01:
            $ d_flag_01 = True
            $ d_flag_02 = False
            $ d_flag_03 = False
            $ d_flag_04 = False
            $ d_flag_05 = False
            $ d_flag_06 = False
            $ d_flag_07 = False
            $ d_flag_08 = False
            $ d_flag_09 = False
            $ d_flag_10 = False
            $ d_flag_11 = False
            $ d_flag_12 = False
            $ d_flag_13 = False
            $ d_flag_14 = False
            $ d_flag_15 = False
            play music "music/(Orchestral) Playful Tension by Shadow16nh.mp3" fadein 1 fadeout 1 # SEX THEME.
        
        "{image=note2.png} Shanghai Honey by Orange Range {image=note2.png}" if d_flag_02:
            pass
        "Shanghai Honey by Orange Range" if not d_flag_02:
            $ d_flag_01 = False
            $ d_flag_02 = True
            $ d_flag_03 = False
            $ d_flag_04 = False
            $ d_flag_05 = False
            $ d_flag_06 = False
            $ d_flag_07 = False
            $ d_flag_08 = False
            $ d_flag_09 = False
            $ d_flag_10 = False
            $ d_flag_11 = False
            $ d_flag_12 = False
            $ d_flag_13 = False
            $ d_flag_14 = False
            $ d_flag_15 = False
            play music "music/02 - Shanghai Honey.mp3" fadein 1 fadeout 1 
       
        
        
        
        
        "{image=note2.png} Introducing Colin Harry Potter OST {image=note2.png}" if d_flag_03:
            pass
        "Introducing Colin Harry Potter OST" if not d_flag_03:
            $ d_flag_01 = False
            $ d_flag_02 = False
            $ d_flag_03 = True
            $ d_flag_04 = False
            $ d_flag_05 = False
            $ d_flag_06 = False
            $ d_flag_07 = False
            $ d_flag_08 = False
            $ d_flag_09 = False
            $ d_flag_10 = False
            $ d_flag_11 = False
            $ d_flag_12 = False
            $ d_flag_13 = False
            $ d_flag_14 = False
            $ d_flag_15 = False
            play music "music/07 Introducing Colin2.mp3" fadein 1 fadeout 1 
        
        "{image=note2.png} Neville's Waltz Harry Potter OST {image=note2.png}" if d_flag_04:
            pass
        "Neville's Waltz Harry Potter OST" if not d_flag_04:
            $ d_flag_01 = False
            $ d_flag_02 = False
            $ d_flag_03 = False
            $ d_flag_04 = True
            $ d_flag_05 = False
            $ d_flag_06 = False
            $ d_flag_07 = False
            $ d_flag_08 = False
            $ d_flag_09 = False
            $ d_flag_10 = False
            $ d_flag_11 = False
            $ d_flag_12 = False
            $ d_flag_13 = False
            $ d_flag_14 = False
            $ d_flag_15 = False
            play music "music/11 Neville's Waltz.mp3" fadein 1 fadeout 1 
            
            
            
            
        "{image=note2.png} The Quidditch Match Harry Potter OST {image=note2.png}" if d_flag_05:
            pass
        "The Quidditch Match Harry Potter OST" if not d_flag_05:
            $ d_flag_01 = False
            $ d_flag_02 = False
            $ d_flag_03 = False
            $ d_flag_04 = False
            $ d_flag_05 = True
            $ d_flag_06 = False
            $ d_flag_07 = False
            $ d_flag_08 = False
            $ d_flag_09 = False
            $ d_flag_10 = False
            $ d_flag_11 = False
            $ d_flag_12 = False
            $ d_flag_13 = False
            $ d_flag_14 = False
            $ d_flag_15 = False
            play music "music/11 The Quidditch Match.mp3" fadein 1 fadeout 1 
        
        
        "{image=note2.png} Anguish by Kevin MacLeod {image=note2.png}" if d_flag_06:
            pass
        "Anguish by Kevin MacLeod" if not d_flag_06:
            $ d_flag_01 = False
            $ d_flag_02 = False
            $ d_flag_03 = False
            $ d_flag_04 = False
            $ d_flag_05 = False
            $ d_flag_06 = True
            $ d_flag_07 = False
            $ d_flag_08 = False
            $ d_flag_09 = False
            $ d_flag_10 = False
            $ d_flag_11 = False
            $ d_flag_12 = False
            $ d_flag_13 = False
            $ d_flag_14 = False
            $ d_flag_15 = False
            play music "music/Anguish.mp3" fadein 1 fadeout 1 
            
            
            
            
        "{image=note2.png} Brittle Rille by Kevin MacLeod {image=note2.png}" if d_flag_07:
            pass
        "Brittle Rille by Kevin MacLeod" if not d_flag_07:
            $ d_flag_01 = False
            $ d_flag_02 = False
            $ d_flag_03 = False
            $ d_flag_04 = False
            $ d_flag_05 = False
            $ d_flag_06 = False
            $ d_flag_07 = True
            $ d_flag_08 = False
            $ d_flag_09 = False
            $ d_flag_10 = False
            $ d_flag_11 = False
            $ d_flag_12 = False
            $ d_flag_13 = False
            $ d_flag_14 = False
            $ d_flag_15 = False
            play music "music/Brittle Rille.mp3" fadein 1 fadeout 1 
            
            
            
            
            
        "{image=note2.png} Chipper Doodle v2 by Kevin MacLeod {image=note2.png}" if d_flag_08:
            pass
        "Chipper Doodle v2 by Kevin MacLeod" if not d_flag_08:
            $ d_flag_01 = False
            $ d_flag_02 = False
            $ d_flag_03 = False
            $ d_flag_04 = False
            $ d_flag_05 = False
            $ d_flag_06 = False
            $ d_flag_07 = False
            $ d_flag_08 = True
            $ d_flag_09 = False
            $ d_flag_10 = False
            $ d_flag_11 = False
            $ d_flag_12 = False
            $ d_flag_13 = False
            $ d_flag_14 = False
            $ d_flag_15 = False
            play music "music/Chipper Doodle v2.mp3" fadein 1 fadeout 1



 
        "{image=note2.png} Dark Fog by Kevin MacLeod {image=note2.png}" if d_flag_09:
            pass
        "Dark Fog by Kevin MacLeod" if not d_flag_09:
            $ d_flag_01 = False
            $ d_flag_02 = False
            $ d_flag_03 = False
            $ d_flag_04 = False
            $ d_flag_05 = False
            $ d_flag_06 = False
            $ d_flag_07 = False
            $ d_flag_08 = False
            $ d_flag_09 = True
            $ d_flag_10 = False
            $ d_flag_11 = False
            $ d_flag_12 = False
            $ d_flag_13 = False
            $ d_flag_14 = False
            $ d_flag_15 = False
            play music "music/Dark Fog.mp3" fadein 1 fadeout 1 



        "{image=note2.png} Final Fantasy VII Game Over Theme {image=note2.png}" if d_flag_10:
            pass
        "Final Fantasy VII Game Over Theme" if not d_flag_10:
            $ d_flag_01 = False
            $ d_flag_02 = False
            $ d_flag_03 = False
            $ d_flag_04 = False
            $ d_flag_05 = False
            $ d_flag_06 = False
            $ d_flag_07 = False
            $ d_flag_08 = False
            $ d_flag_09 = False
            $ d_flag_10 = True
            $ d_flag_11 = False
            $ d_flag_12 = False
            $ d_flag_13 = False
            $ d_flag_14 = False
            $ d_flag_15 = False
            play music "music/Final Fantasy 7 Game Over Theme.mp3" fadein 1 fadeout 1


 
        "{image=note2.png} Final Fantasy VII Boss Theme {image=note2.png}" if d_flag_11:
            pass
        "Final Fantasy VII Boss Theme" if not d_flag_11:
            $ d_flag_01 = False
            $ d_flag_02 = False
            $ d_flag_03 = False
            $ d_flag_04 = False
            $ d_flag_05 = False
            $ d_flag_06 = False
            $ d_flag_07 = False
            $ d_flag_08 = False
            $ d_flag_09 = False
            $ d_flag_10 = False
            $ d_flag_11 = True
            $ d_flag_12 = False
            $ d_flag_13 = False
            $ d_flag_14 = False
            $ d_flag_15 = False
            play music "music/Final Fantasy VII Boss Theme.mp3" fadein 1 fadeout 1



 
        "{image=note2.png} Hitman by Kevin MacLeod {image=note2.png}" if d_flag_12:
            pass
        "Hitman by Kevin MacLeod" if not d_flag_12:
            $ d_flag_01 = False
            $ d_flag_02 = False
            $ d_flag_03 = False
            $ d_flag_04 = False
            $ d_flag_05 = False
            $ d_flag_06 = False
            $ d_flag_07 = False
            $ d_flag_08 = False
            $ d_flag_09 = False
            $ d_flag_10 = False
            $ d_flag_11 = False
            $ d_flag_12 = True
            $ d_flag_13 = False
            $ d_flag_14 = False
            $ d_flag_15 = False
            play music "music/Hitman.mp3" fadein 1 fadeout 1



 
        "{image=note2.png} Music for Manatees by Kevin MacLeod {image=note2.png}" if d_flag_13:
            pass
        "Music for Manatees by Kevin MacLeod" if not d_flag_13:
            $ d_flag_01 = False
            $ d_flag_02 = False
            $ d_flag_03 = False
            $ d_flag_04 = False
            $ d_flag_05 = False
            $ d_flag_06 = False
            $ d_flag_07 = False
            $ d_flag_08 = False
            $ d_flag_09 = False
            $ d_flag_10 = False
            $ d_flag_11 = False
            $ d_flag_12 = False
            $ d_flag_13 = True
            $ d_flag_14 = False
            $ d_flag_15 = False
            play music "music/Music for Manatees.mp3" fadein 1 fadeout 1



 
        "{image=note2.png} Plaint by Kevin MacLeod {image=note2.png}" if d_flag_14:
            pass
        "Plaint by Kevin MacLeod" if not d_flag_14:
            $ d_flag_01 = False
            $ d_flag_02 = False
            $ d_flag_03 = False
            $ d_flag_04 = False
            $ d_flag_05 = False
            $ d_flag_06 = False
            $ d_flag_07 = False
            $ d_flag_08 = False
            $ d_flag_09 = False
            $ d_flag_10 = False
            $ d_flag_11 = False
            $ d_flag_12 = False
            $ d_flag_13 = False
            $ d_flag_14 = True
            $ d_flag_15 = False
            play music "music/Plaint.mp3" fadein 1 fadeout 1



 
        "{image=note2.png} Under-the-Radar by PhobyAk {image=note2.png}" if d_flag_15:
            pass
        "Under-the-Radar by PhobyAk" if not d_flag_15:
            $ d_flag_01 = False
            $ d_flag_02 = False
            $ d_flag_03 = False
            $ d_flag_04 = False
            $ d_flag_05 = False
            $ d_flag_06 = False
            $ d_flag_07 = False
            $ d_flag_08 = False
            $ d_flag_09 = False
            $ d_flag_10 = False
            $ d_flag_11 = False
            $ d_flag_12 = False
            $ d_flag_13 = False
            $ d_flag_14 = False
            $ d_flag_15 = True
            play music "music/Under-the-Radar by PhobyAk.mp3" fadein 1 fadeout 1 
            
            
            
            
        "- Остановить мелодию -":
            stop music fadeout 1.0
            jump music_room
        "- Продолжать проигрывать текущию мелодию -":
            jump gallery
    jump music_room2
        
        
        
        
        
        
        
        
        
        
        
        

        
    ### MESSAGES ###
        
label gallery_locked:
    $ end_u_2_pic =  "title2.jpg" #<---- SCREEN
    show screen end_u_2                                             #<---- SCREEN
    ">Пройдите игру, чтобы разблокировать галлерею."
    hide screen end_u_2                                             #<---- SCREEN
    show screen extras
    return
