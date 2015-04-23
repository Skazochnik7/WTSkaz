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
            $_scrollSection=0
            jump volone 
        
        "- Священные свитки. Часть II -":
            $_scrollSection=1
            jump volone 
            
        "- Священные свитки. Часть III -":
            $_scrollSection=2
            jump volone 

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
    $ choose = RunMenu()
    python:
        _itemCount=0
        if persistent.itemSet!=None:
            _itemCount=persistent.itemSet.get("scroll")
            _itemCount=0 if _itemCount==None else _itemCount
        for i in range(_scrollSection*15+1, _scrollSection*15+15):
            if i<=_itemCount:
                choose.AddItem("- C."+str(i)+": Священный свиток #"+str(i)+" -", 
                    "vol_description" , i)
    $ choose.Show("after_cam")

label vol_description:

    $_descrs=[
    ["Это самый первый эскиз офиса Дамблдора.", "Не самое лучшее мое творение. Но заключает в себе великую историческую ценность."],
    ["Календарь...", "На ранних этапах разработки я планировал сделать внутриигровой календарь и завязать на нем геймплей...","До тех пор, пока не понял, насколько сложнее сделать такую игру...",
        "К тому же мне кажется, что любые временные рамки в любой игре мешают веселью. Так что, я бросил эту затею...", "Позже я использовал этот рисунок как пергамент для писем..."],
    ["Несколько самых ранних набросков Гермионы..."],
    ["Сцена с глубоким заглотом...", "Моя первая попытка.", "Была признана негодной и оставлена как есть."],
    ["Постер игры...", "Гермиона - работа Dahr. Остальное - моя..."],
    ["Альтернативный постер игры.", "Этот так и не был выпущен."],
    ["Несколько чибиков крупным планом.", "Они так и не попали в игру..."],
    ["Куча вещей, которых я так и не использовал...", "Все из-за dahr и его шикарных рисунков."],
    ["Рисунок Гермионы с постера. (by Dahr)", "Мне больше нравится правая - та, что с трусиками."],
    ["Опять вещи, что так и не вошли в игру...", "Идея была в том, что чем больше ты бы прокачивал Гермиону, тем больше прищепок она давала бы на себя нацепить...","А цепь для сосков она должна была бы носить во время уроков под своей формой."],
    ["Бордель домовых... Еще одна вещь, которая так и не сбылась."],
    ["Рисунок, где ты очень похож на мага из Дурмстранга, а Лола - на ученицу...", "Рисунок рисовал Dahr, конечно."],
    ["Еще один побочный квест, так и не увидевший свет...", "В общем, там-","Нет, пожалуй, нет. Кто знает, быть может мы все-таки введем эти квесты."],
    ["Еще один побочный квест...", "Этот про волшебный шахматный клуб."],
    ["Существует множество способов того, как симпатичная девушка может держать книгу.", "Я думал, что было бы круто, если бы Гермиона начинала носить держать книги по-другому по мере того, как она учится все новому.","Так как вся ветка с репетиторством была отменена, я выкладываю это здесь..."],


    ["Парочка вещей, что не попали в финальную версию...", "Слева действительно настоящий живой домовой, которого можно подарить.","Справа портрет извращенного, но мудрого мага. Должен был помогать с учебой..."],
    ["Еще несколько вещиц...", "Газета, флакон духов и волшебная шляпа, которая говорит то, что ты хочешь услышать..."],
    ["Книги...", "Верхний ряд - мои наброски, нижний ряд - законченный изображения от dahr."],
    ["Известная певица.", "Не имеет отношения игре, добавлена сюда без причины, просто так."],
    ["Я потратил прилично времени, чтобы дать Гермионе подходящую внешность...", "Версия \"A\" была моей первой попыткой. И она мне нравилась, пока я не начал ее ненавидеть...",
        "Версия \"B\" была моей второй попыткой. И она хороша. Но ее самоуверенные и полуагрессивные черты не совсем подходили героине...","Версия \C\" та, что прошла кастинг. Гермиона которую мы вырастили и о которой будем заботиться, я уверен."],
    ["Побочный квест, которого нет.", "Вам позволено жалеть, что торопили меня.","Если вы не торопили меня, вам позволено злиться на тех, кто торопил."],
    ["Гермиона дарит свое тело Джину...", "Это была бы запоминающаяся сцена..."],
    ["Не ожидали, ага?", "Это все еще Гермиона, если вам любопытно."],
    [".................................", "Сайд-квест, конечно..."],
    ["Еще один сайд-квест...", "Мы много спорили с Dahr о нем...","Я был против квеста, но потом Dahr отправил мне картинки, чем заставил меня заткнуться."],
    ["На самых ранних стадиях разработки у меня была идея показывать последствия проваленных или успешно выполненых сайд-квестов в виде упрощенных изображений, или фотографий...", 
        "Поначалу многие сайд-квесты давали игроку выбор, как потратить бюджет Хогвартса...",
        "Потратить деньги на финансирование школьной команды по квиддичу, или на наем новых учителей? Ну, и в таком духе..."],
    ["Ну разве она не милашка?"],
    ["Очередной (довольно большой) сайд-квест..."],
    [".........."],
    ["Одни из самых ранних набросков по сайд-квесту школьной команды по квиддичу..."]
    ]

    
    show image "03_hp/19_extras/"+str(choose.choice).zfill(2)+".png" with d3
    if commentaries:
        python:
            if _itemCount<2:
                for i in range(len(_descrs[choose.choice-1])):
                    renpy.say(a1,_descrs[choose.choice-1][i])
    show screen ctc
    pause
    hide screen ctc
    hide image "03_hp/19_extras/"+str(choose.choice).zfill(2)+".png" with d3
    jump volone
        

        
        
    
            
               


                

                

                
                
                

                

                

                

                
                

                

                


        
            
            
            
            
        
        
        
        
        
        
        
        
        
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
