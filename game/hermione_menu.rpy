#play music "music/Chipper Doodle v2.mp3" fadein 1 fadeout 1 
#stop music fadeout 2.0
label hermione_approaching:     
         
    $ menu_x = 0.2 #Menu is moved to the left side.
    $ pos = POS_410
                
    $ renpy.play('sounds/door.mp3') #Sound of a door opening.
    $ hermione_chibi_xpos = 400 #Near the desk.
    show screen hermione_02 #Hermione stands still.
    show screen bld1
    with d3

    python:
        for t in [
            (0, "body_01.png", her, "Да, профессор?"),
            (-2, "body_03.png", "", ">Похоже, Гермиона по-прежнему немного расстроена вами..."),
            (-9, "body_03.png", "", ">Вы расстроили Гермиону."),
            (-19, "body_09.png", "", ">Гермиона очень расстроена вами."),
            (-39, "body_05.png", "", ">Гермиона злится на вас."),
            (-49, "body_47.png", "", ">Гермиона очень злится на вас."),
            (-59, "body_47.png", "", ">Гермиона гневается на вас."),
            (-100, "body_47.png", "", ">Гермиона ненавидит вас.")
            ]:
            (_val, _img, _char, _text)=t
            if hermi.liking>=_val:
                herView.showQQ( _img, pos )
                renpy.say(_char, _text)
                break



    label hermione_main_menu:
    menu:
        "- Поговорить -" if not chitchated_with_her:
            $ chitchated_with_her = True #Prevents you from chitchatting with Hermione more then once per time of day. Turns back to False every night. (And every day).
            if hermi.liking >= -7:
                jump hermione_chat
            else:
                her "Мне нечего сказать вам..."    
                jump hermione_main_menu

        "- Обучение -" if not daytime and not tut_happened and hermi.whoring <= 12:
            if hermi.liking==0:
                jump tutoring
            python:
                for t in [
                (-2, "Извините, возможно завтра..."),
                (-19, "Сегодня я не в настроении..."),
                (-100, "После того, что вы сделали?\nЯ думаю - нет...")
                ]:
                    (_val, _text)=t
                    if hermi.liking>=_val:
                        renpy.say(her, _text)
                        break
            jump hermione_main_menu

        "- Купить \"сексуальный\" рейтинг -" if this.Has("her_wants_buy"):#buying_favors_from_hermione_unlocked:
                if hermi.liking==0:
                    jump new_personal_request
                python:
                    for t in [
                    (-2, "Мне жаль, профессор, может быть в другой раз..."),
                    (-9, "Мне не хочется сегодня...\nМожет быть через пару дней..."),
                    (-19, "Нет, спасибо...."),
                    (-29, "После того, что вы сделали?\nЯ так не думаю..."),
                    (-39, "Вы серьезно!?"),
                    (-100, "Это какая-то ваша пошлая шутка?!\nПосле того, что вы сделали, я не хочу повторять это!")
                    ]:
                        (_val, _text)=t
                        if hermi.liking>=_val:
                            renpy.say(her, _text)
                            break
                jump hermione_main_menu
       
        
        
        "- Дать ей подарок -" if not gifted:
            $ choose = RunMenu()
            python:
                for o in hero.Items():
                    if not o.Name in {"wine", "scroll"}:
                        choose.AddItem("- "+o._caption+" -", 
                            "menu_gifts_actions" , True, o.Name)

            $ choose.Show("hermione_main_menu")


                    
        

            
        "- Гардероб -" if dress_code:
            if hermi.liking==0:
                menu:
                    
                    "- Надеть значок -" if (herView.data().getItemKey( G_N_BADGE )==None) and  hermi.Items.Any("badge_01"): #not ba_01 and badge_01 == 7:
                        jump badge_put
                    
                    "- Снять значок -" if (herView.data().getItemKey( G_N_BADGE )!=None) and  hermi.Items.Any("badge_01"): #ba_01 and badge_01 == 7:
                        jump badge_take
                    
                    "- Надеть колготки -" if (herView.data().getItemKey( G_N_NETS )==None) and  hermi.Items.Any("nets"): #not ne_01 and nets == 7: # Не перевел
                        jump nets_put
                    
                    "- Снять колготки -" if (herView.data().getItemKey( G_N_NETS )!=None) and  hermi.Items.Any("nets"): #ne_01 and nets == 7:
                        jump nets_take
                    
                    "- Надеть мини-юбку -" if herView.data().checkItemKeyStyle( G_N_SKIRT, 'default' ) and hermi.Items.Any("miniskirt"): #not legs_02 and gave_miniskirt: #Turns True when Hermione has the miniskirt.:
                        jump mini_on #28_gifts.rpy

                    "- Надеть длинную юбку -" if herView.data().checkItemKeyStyle( G_N_SKIRT, 'short' ) and hermi.Items.Any("miniskirt"): #legs_02 and gave_miniskirt: #Turns True when Hermione has the miniskirt.
                        jump mini_off #28_gifts.rpy
                

                    "- Ничего -":
                        jump hermione_main_menu
            else:
                python:
                    for t in [
                    (-2, "Мне очень жаль, профессор, может быть в другой раз..."),
                    (-9, "Что не так с моей одеждой?"),
                    (-19, "Нет, спасибо...."),
                    (-29, "Я так не думаю..."),
                    (-39, "Нет!"),
                    (-100, "Я никогда не позволю вам снова решать, что мне носить!")
                    ]:
                        (_val, _text)=t
                        if hermi.liking>=_val:
                            renpy.say(her, _text)
                            break
                jump hermione_main_menu
       
        
        "- Попросить уйти -":
#                        if daytime:
#                            play music "music/Brittle Rille.mp3" fadein 1 fadeout 1
#                        else:
#                            play music "music/Music for Manatees.mp3" fadein 1 fadeout 1
            $ menu_x = 0.5 #Menu position is back to default. (Center).
            if daytime:
                if hermi.liking>=-2:
                    her "О, хорошо! Тогда я пойду на уроки."
                elif hermi.liking >= -6:
                    her "..............................."
                else: 
                    her "*Гм!*..."
            else:
                if hermi.liking>=-2:
                    her "О, хорошо! Тогда я пойду спать."
                elif hermi.liking >= -6:
                    her "..............................."
                else: 
                    her "Пф!..."

            hide screen bld1
            $herView.hideQ() 
            hide screen blktone 
            hide screen hermione_02
            hide screen ctc
            with d3

            if daytime:
                $ hermione_takes_classes = True
                jump day_main_menu
            else:
                $ hermione_sleeping = True
                jump night_main_menu

label hermione_chat:
    menu:
        "Спросить насчет учебников" if teacher_jinn_quest == 3:
            jump hermione_bookbuying
            
        "Купить учебники" if teacher_jinn_quest == 4:
            jump hermione_bookbuying
            
        "Болтать":
            jump chit_chat_hermione             

        
### CHITCHAT WITH HERMIONE ###
label chit_chat_hermione:
    $ one_of_ten = renpy.random.randint(1, 10) #Generating one number out of three for various porpoises.
    $ pos = POS_410
    
    if hermi.whoring >= 0 and hermi.whoring <= 2: # WHORING LEVEL 01.
        if one_of_ten == 1:
            $herView.hideshowQQ( "body_04.png", pos )
            her "Может быть, если я буду работать быстрее, я смогу втиснуть пару занятий в мое рассписание..."
            $herView.hideshowQQ( "body_03.png", pos )
        
        elif one_of_ten == 2:
            $herView.hideshowQQ( "body_04.png", pos )
            her "В общем-то, мне нравится когда меня зовут \"Всезнайка\"."
            her "Возможно, я даже краснею от этого..."
            $herView.hideshowQQ( "body_03.png", pos )
        elif one_of_ten == 3:
            $herView.hideshowQQ( "body_04.png", pos )
            her "Василиск, также известен как король змей."
            her "Герпо Фол первый осеменил Василиска."
            her "Он сделал это с помощью--"
            $herView.hideshowQQ( "body_10.png", pos )
            her "Ой, извините, профессор, у нас еще один тест завтра..."
            her "Я просто хочу быть уверенной, что я готова..."
            $herView.hideshowQQ( "body_01.png", pos )
        elif one_of_ten == 4:
            $herView.hideshowQQ( "body_10.png", pos )
            her "Если бы мое тело не требовало сна..."
            $herView.hideshowQQ( "body_18.png", pos )
            her "Я могла бы заниматся в два раза больше!?"
            $herView.hideshowQQ( "body_14.png", pos )
            her "Надеюсь, есть заклинание для этого..."
            $herView.hideshowQQ( "body_03.png", pos )
        
        elif one_of_ten == 5:
            $herView.hideshowQQ( "body_04.png", pos )
            her "До сих пор профессор Трелони не дал мне даже капельки полезных знаний, сэр."
            $herView.hideshowQQ( "body_03.png", pos )
       
        elif one_of_ten == 6:
            $herView.hideshowQQ( "body_04.png", pos )
            her "Если бы только студенты были честными, они бы полюбили ответственность."
            $herView.hideshowQQ( "body_03.png", pos )
      
        elif one_of_ten == 7:
            $herView.hideshowQQ( "body_04.png", pos )
            her "Как люди могу быть такими безразличными к мировым проблемам?"
            her "Лично я считаю, что мы все должны работать вместе, чтобы мир стал лучше."
            $herView.hideshowQQ( "body_03.png", pos )
            
        elif one_of_ten == 8:
            $herView.hideshowQQ( "body_10.png", pos )
            her "В последнее время дождь льет чаще..."
            $herView.hideshowQQ( "body_01.png", pos )
    
        elif one_of_ten == 9:
            $herView.hideshowQQ( "body_10.png", pos )
            her "Очень мало людей знает..."
            $herView.hideshowQQ( "body_06.png", pos )
            her "...что я очень люблю шоколад."
            $herView.hideshowQQ( "body_01.png", pos )
       
        elif one_of_ten == 10:
            $herView.hideshowQQ( "body_06.png", pos )
            her "Извините сэр, но у меня нету времени на разговоры..."
            $herView.hideshowQQ( "body_03.png", pos )


    if hermi.whoring >= 3 and hermi.whoring <= 5: # WHORING LEVEL 02
        if one_of_ten == 1:
            $herView.hideshowQQ( "body_04.png", pos )
            her "Я где то прочитала что полная луна помогает сосредоточится..."
            $herView.hideshowQQ( "body_03.png", pos )
            
        elif one_of_ten == 2:
            $herView.hideshowQQ( "body_06.png", pos )
            her "Я обожаю сидеть с книгой у огня, когда льет дождь..."
            $herView.hideshowQQ( "body_01.png", pos )
            
        elif one_of_ten == 3:
            $herView.hideshowQQ( "body_10.png", pos )
            her "Прошел слух, что профессор Снейп что-то замышляет в школе..."
            $herView.hideshowQQ( "body_15.png", pos )
            her "Хотя, наверное, это пустяки..."
            $herView.hideshowQQ( "body_03.png", pos )
            
        elif one_of_ten == 4:
            $herView.hideshowQQ( "body_04.png", pos )
            her "Несмотря на сомнительность услуг, которые я вам оказывала, сэр..."
            her "Я благодарна вам за вашу помощь..."
            $herView.hideshowQQ( "body_09.png", pos )
            her "Гриффиндор нуждается в этих очках больше, чем когда либо..."
            $herView.hideshowQQ( "body_03.png", pos )
            
        elif one_of_ten == 5:
            $herView.hideshowQQ( "body_04.png", pos )
            her "Почему квиддич так популярен среди девочек? Я не понимаю..."
            $herView.hideshowQQ( "body_03.png", pos )
            
        elif one_of_ten == 6:
            $herView.hideshowQQ( "body_04.png", pos )
            her "Наше \"Общество Защиты Прав Мужчин\" набирает популярность."
            her "Это очень важно знать, что вы помогаете развивать наше общество."
            $herView.hideshowQQ( "body_03.png", pos )
            
        elif one_of_ten == 7:
            $herView.hideshowQQ( "body_04.png", pos )
            her "Хогвартс имеет внушительную библиотеку..."
            $herView.hideshowQQ( "body_08.png", pos )
            her "Но я хочу, чтобы она была еще больше..."
            $herView.hideshowQQ( "body_03.png", pos )
            
        elif one_of_ten == 8:
            $herView.hideshowQQ( "body_10.png", pos )
            her "Как один из лучших студентов академии, я должна поддерживать свою репутацию..."
            her "Люди уважают меня..."
            $herView.hideshowQQ( "body_31.png", pos )
            her "...так что я очень ценю ваше внимание, сэр."
            $herView.hideshowQQ( "body_29.png", pos )
            
        elif one_of_ten == 9:
            $herView.hideshowQQ( "body_11.png", pos )
            her "Услуги которые я вам оказала тогда, сэр..."
            $herView.hideshowQQ( "body_33.png", pos )
            her "......."
            $herView.hideshowQQ( "body_87.png", pos )
            her "Я пошла на это только для моего факультета."
            $herView.hideshowQQ( "body_120.png", pos )
            her "Я просто хотела, чтобы вы знали это, сэр..."
            
        elif one_of_ten == 10:
            $herView.hideshowQQ( "body_04.png", pos )
            her "Наш \"Осенний бал\" будет через несколько месяцев..."
            $herView.hideshowQQ( "body_11.png", pos )
            her "Но некоторые девочки уже обсуждают что они наденут на бал..."
            $herView.hideshowQQ( "body_185.png", pos )

  
    if hermi.whoring >= 6 and hermi.whoring <= 8: # WHORING LEVEL 03.
        if one_of_ten == 1:
            $herView.hideshowQQ( "body_04.png", pos )
            her "Вы помните, как вы просили мои трусики в первый раз?"
            her "Я тогда так сильно разозлилась..."
            $herView.hideshowQQ( "body_09.png", pos )
            her "Тепеь я вижу, что я была неправа..."
            her "Ведь судьба целого факультета в моих руках..."
            $herView.hideshowQQ( "body_07.png", pos )
            her "Все остальное не должно меня волновать!"
            
        elif one_of_ten == 2:
            $herView.hideshowQQ( "body_04.png", pos )
            her "Скорость, с которой Слизерин набирает очки в последнее время просто невозможна."
            $herView.hideshowQQ( "body_05.png", pos )
            her "Я думаю, за этим стоит профессор Снейп."
            $herView.hideshowQQ( "body_04.png", pos )
            her "Вам нужно разобраться в ситуации, сэр."
            $herView.hideshowQQ( "body_03.png", pos )
            
        elif one_of_ten == 3:
            $herView.hideshowQQ( "body_10.png", pos )
            her "Яйца Эшвендэра, корень розы, лунный камень..."
            $herView.hideshowQQ( "body_11.png", pos )
            her "Ах? Я опять размышляла вслух?"
            $herView.hideshowQQ( "body_24.png", pos )
            her "Извините..."
            $herView.hideshowQQ( "body_13.png", pos )
            her "Просто скоро снова тест..."

        elif one_of_ten == 4:
            $herView.hideshowQQ( "body_77.png", pos )
            her "Я ненавижу факультет Слизерина всем своим сердцем, сэр."
            
        elif one_of_ten == 5:
            $herView.hideshowQQ( "body_16.png", pos )
            her "Хогвартс стал для меня новым домом в последнее время..."
            $herView.hideshowQQ( "body_71.png", pos )
            her "Я даже почти не скучаю по родителям..."
            $herView.hideshowQQ( "body_18.png", pos )
            her "Если подумать, я не скучаю по ним совсем..."
            $herView.hideshowQQ( "body_118.png", pos )
            her "Я - ужасная дочь..."

        elif one_of_ten == 6:
            $herView.hideshowQQ( "body_70.png", pos )
            her "*Зевок!* Я прочитала о технике, которая помогает в два раза меньше спать..."
            $herView.hideshowQQ( "body_73.png", pos )
            her "Но, кажется, она не работает.... *Зевок!*"

        elif one_of_ten == 7:
            $herView.hideshowQQ( "body_04.png", pos )
            her "Даже когда я закончу Хогвартс я буду продолжать совершенствоваться."
            $herView.hideshowQQ( "body_02.png", pos )
            her "Если я отдам себя всю этому миру он станет лучше, я знаю это!"
            $herView.hideshowQQ( "body_03.png", pos )
           
        elif one_of_ten == 8:
            $herView.hideshowQQ( "body_11.png", pos )
            her "Мне кажется, что этот год будет важнейшим в моей жизни..."
            $herView.hideshowQQ( "body_13.png", pos )
  
        elif one_of_ten == 9:
            $herView.hideshowQQ( "body_04.png", pos )
            her "Некоторые школьные коридоры пыльные и грязные..."
            her "Пожалуйста позаботьтесь об этом, сэр..."
            $herView.hideshowQQ( "body_03.png", pos )
       
        elif one_of_ten == 10:
            $herView.hideshowQQ( "body_14.png", pos )
            her "Я читала об этом. Называется \"Маховик времени\"."            
            her "Он позволяет владельцу контролировать время..."
            $herView.hideshowQQ( "body_16.png", pos )
            her "Если бы он был у меня, я бы творила чудеса со своим расписанием..."
            $herView.hideshowQQ( "body_17.png", pos )
        

    if hermi.whoring >= 9 and hermi.whoring <= 11: # WHORING LEVEL 04.
        if one_of_ten == 1:
            $herView.hideshowQQ( "body_11.png", pos )
            her "Мое \"Общество по Защите Прав Мужчин\" в последнее время теряет популярность..."
            $herView.hideshowQQ( "body_12.png", pos )
            her "Похоже это никого не волнует!"

        elif one_of_ten == 2:
            $herView.hideshowQQ( "body_04.png", pos )
            her "Спасибо вам за все эти очки, сэр."
            $herView.hideshowQQ( "body_07.png", pos )
            her "Некоторые, конечно, достались весьма странным образом, но ..."
            $herView.hideshowQQ( "body_04.png", pos )
            her "Но это не важно, до тех пор, пока это дает \"Гриффиндору\" преимущество в гонке со \"Слизерином\"."
            $herView.hideshowQQ( "body_03.png", pos )

        elif one_of_ten == 3:
            $herView.hideshowQQ( "body_77.png", pos )
            her "Квиддич это глупо!"
            $herView.hideshowQQ( "body_17.png", pos )
            her "Вот. Я сказала это."
            
        elif one_of_ten == 4:
            $herView.hideshowQQ( "body_02.png", pos )
            her "Сэр, есть кое-что, что вы должны знать о профессоре Снейпе..."
            $herView.hideshowQQ( "body_10.png", pos )
            her "................."
            $herView.hideshowQQ( "body_09.png", pos )
            her "........................."
            $herView.hideshowQQ( "body_04.png", pos )
            her "Ух... Ничего..."
            $herView.hideshowQQ( "body_03.png", pos )
 
        elif one_of_ten == 5:
            $herView.hideshowQQ( "body_04.png", pos )
            her "Некоторые из \"Слизеринских\" девок в последнее время среди бела дня продаются за очки..."
            $herView.hideshowQQ( "body_02.png", pos )
            her "Вы должны положить этому конец, сэр."
            $herView.hideshowQQ( "body_69.png", pos )
            her "(Я едва поспеваю за ними...)"

        elif one_of_ten == 6:
            $herView.hideshowQQ( "body_10.png", pos )
            her "Жизнь устроена очень странно..."
            $herView.hideshowQQ( "body_08.png", pos )
            her "Вы согласны, сэр?"
            $herView.hideshowQQ( "body_13.png", pos )

        elif one_of_ten == 7:
            $herView.hideshowQQ( "body_76.png", pos )
            her "Слизеринцы..."
            $herView.hideshowQQ( "body_77.png", pos )
            
        elif one_of_ten == 8:
            $herView.hideshowQQ( "body_10.png", pos )
            her "В последнее время я так много времени провела в вашем кабинете..."
            $herView.hideshowQQ( "body_11.png", pos )
            her "Если я буду неосторожна, некоторые могут заметить и решить, что я стала вашей любовниц..."
            $herView.hideshowQQ( "body_34.png", pos )
            her "Я хотела сказать, любимчиком..."
            $herView.hideshowQQ( "body_33.png", pos )

        elif one_of_ten == 9:
            $herView.hideshowQQ( "body_02.png", pos )
            her "Мой любимый цвет?"
            $herView.hideshowQQ( "body_02.png", pos )
            her "Алый и золотой, конечно же!"
            $herView.hideshowQQ( "body_03.png", pos )
       
        elif one_of_ten == 10:
            $herView.hideshowQQ( "body_10.png", pos )
            her "Это странно, что мои лучшие друзья это мальчики?"
            $herView.hideshowQQ( "body_01.png", pos )
        

        
    if hermi.whoring >= 12 and hermi.whoring <= 14: # WHORING LEVEL 05.
        if one_of_ten == 1:
            $herView.hideshowQQ( "body_07.png", pos )
            her "Сэр, при всем уважении..."
            her "Профессор Снейп распускает руки!"
            $herView.hideshowQQ( "body_11.png", pos )
            her "Вы должны сделать что-то..."
            $herView.hideshowQQ( "body_03.png", pos )

        elif one_of_ten == 2:
            $herView.hideshowQQ( "body_04.png", pos )
            her "Я готова пойти на все, лишь бы \"Гриффиндор\" лидировал..."
            her "Но это не значит, что я с удовольствием отдаюсь вам за очки для факультета."
            $herView.hideshowQQ( "body_118.png", pos )
            her "{size=-4}(Как какая-то ведьма-проститутка...){/size}"

        elif one_of_ten == 3:
            $herView.hideshowQQ( "body_79.png", pos )
            her "Что на сегодня, сэр?"
            
        elif one_of_ten == 4:
            $herView.hideshowQQ( "body_11.png", pos )
            her "Раньше я училась лучше, чем сейчас..."
            $herView.hideshowQQ( "body_10.png", pos )
            her "Я теряю мотивацию?"
            $herView.hideshowQQ( "body_13.png", pos )
            
        elif one_of_ten == 5:
            $herView.hideshowQQ( "body_08.png", pos )
            her "Мой нелюбимый предмет?"
            $herView.hideshowQQ( "body_09.png", pos )
            her "Гадание." 
            
        elif one_of_ten == 6:
            $herView.hideshowQQ( "body_14.png", pos )
            her "Мой отец сказал: \"Магия это наука, которую мы не можем понять\"."
            $herView.hideshowQQ( "body_10.png", pos )
            her "Он, конечно же, мог ошибаться..."
            $herView.hideshowQQ( "body_13.png", pos )
            
        elif one_of_ten == 7:
            $herView.hideshowQQ( "body_04.png", pos )
            her "Несмотря ни на что..."
            $herView.hideshowQQ( "body_10.png", pos )
            her "Я благодарна, что вы позволяете мне получать дополнительные очки..."
            $herView.hideshowQQ( "body_13.png", pos )
            
        elif one_of_ten == 8:
            $herView.hideshowQQ( "body_14.png", pos )
            her "Сегодня довольно холодно, не так ли?"
            $herView.hideshowQQ( "body_15.png", pos )
            
        elif one_of_ten == 9:
            $herView.hideshowQQ( "body_14.png", pos )
            her "\"Осенний бал\" совсем скоро..."
            $herView.hideshowQQ( "body_15.png", pos )
            
        elif one_of_ten == 10:
            $herView.hideshowQQ( "body_10.png", pos )
            her "Люди вряд ли посетят наше \"Общество по Защите Прав Мужчин\" еще когда-либо..."
            $herView.hideshowQQ( "body_13.png", pos )
    
    
    
    
    
    
        
    if hermi.whoring >= 15 and hermi.whoring <= 17:  # WHORING LEVEL 06.
        if one_of_ten == 1:
            $herView.hideshowQQ( "body_87.png", pos )
            her "Хотите, чтобы я показала вам свою грудь?"
            $herView.hideshowQQ( "body_78.png", pos )
            her "Да... Я хочу, чтобы вы использовали меня..."
            $herView.hideshowQQ( "body_79.png", pos )
            her "Вот настолько я самоотверженна!"
           
        elif one_of_ten == 2:
            $herView.hideshowQQ( "body_14.png", pos )
            her "С этим ничего не поделать, но я чувствую себя не очень, когда домовые эльфы стирают за мной вещи..."
            $herView.hideshowQQ( "body_87.png", pos )
            her "То есть, все эти пятна спермы..."
            $herView.hideshowQQ( "body_118.png", pos )

        elif one_of_ten == 3:
            $herView.hideshowQQ( "body_02.png", pos )
            her "Не имеет значения, сколько раз вы спросите меня..."
            her "Ответ будет один и тот же..."
            $herView.hideshowQQ( "body_47.png", pos )
            her "Я жутко возмущена \"Слизеринцами\"!"
            $herView.hideshowQQ( "body_69.png", pos )
        
        
        elif one_of_ten == 4:
            $herView.hideshowQQ( "body_02.png", pos )
            her "Когда я думаю обо всем, на что мне пришлось пойти в обмен на очки..."
            $herView.hideshowQQ( "body_87.png", pos )
            her "Я чувствую себя немного неловко..."
            $herView.hideshowQQ( "body_120.png", pos )
            her "Но так же я очень горжусь собой."
            
        elif one_of_ten == 5:
            $herView.hideshowQQ( "body_14.png", pos )
            her "До сих пор я посвящаю очень много времени обучению..."
            her "Но не так много, как раньше..."
            $herView.hideshowQQ( "body_11.png", pos )
            her "Вообще мне теперь не очень-то и нравится учиться..."
            $herView.hideshowQQ( "body_13.png", pos )
        
        elif one_of_ten == 6:
            $herView.hideshowQQ( "body_04.png", pos )
            her "Гриффиндор должен получить кубок в этому году!"
            $herView.hideshowQQ( "body_118.png", pos )
            her "{size=-4}(Даже если это будет стоить мне моей чести...){/size}"
            $herView.hideshowQQ( "body_120.png", pos )
           
           
        elif one_of_ten == 7:
            $herView.hideshowQQ( "body_14.png", pos )
            her "Я ничего не имею против осенней погоды..."
            $herView.hideshowQQ( "body_16.png", pos )
            her "Но мое любимое время года это зима."
            $herView.hideshowQQ( "body_15.png", pos )
        
        elif one_of_ten == 8:
            $herView.hideshowQQ( "body_14.png", pos )
            her "Раньше я смотрела свысока на девушек, которые беспокоятся о своей внешности..."
            her "Но я была не права.."
            her "Я начала понимать, насколько важно девушке выглядеть симпатичной."
            $herView.hideshowQQ( "body_29.png", pos )
            her "..............."
            $herView.hideshowQQ( "body_122.png", pos )
            her "С недавнего времени я на диете..."
            $herView.hideshowQQ( "body_34.png", pos )
            $herView.hideshowQQ( "body_33.png", pos )
       
        elif one_of_ten == 9:
            $herView.hideshowQQ( "body_14.png", pos )
            her "Последнее время я чувствую себя довольно уверенно при мальчиках..."
            $herView.hideshowQQ( "body_06.png", pos )
            her "Я думаю, что должна быть благодарна вам за это."
            
        elif one_of_ten == 10:
            $herView.hideshowQQ( "body_14.png", pos )
            her "Мой любимый предмет?"
            $herView.hideshowQQ( "body_13.png", pos )
            her "Хм..."
            $herView.hideshowQQ( "body_14.png", pos )
            her "Думаю это \"чары\"..."
            $herView.hideshowQQ( "body_15.png", pos )
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
    if hermi.whoring >= 18 and hermi.whoring <= 20: # WHORING LEVEL 07.
        if one_of_ten == 1:
            $herView.hideshowQQ( "body_04.png", pos )
            her "Просто дайте знать, что вы хотите от меня сегодня, сэр."
            $herView.hideshowQQ( "body_03.png", pos )
           
        elif one_of_ten == 2:
            $herView.hideshowQQ( "body_11.png", pos )
            her "Я почти не учусь теперь..."
            her "Несмотря на это, моя популярность, кажется, растет..."
            $herView.hideshowQQ( "body_13.png", pos )
            her "Хм..."
                 
        elif one_of_ten == 3:
            $herView.hideshowQQ( "body_64.png", pos )
            her "Я бы не отказалась от бутылки сливочного пива ..."
            $herView.hideshowQQ( "body_68.png", pos )
        
        elif one_of_ten == 4:
            $herView.hideshowQQ( "body_06.png", pos )
            her "Что это сэр? У вас еще один подарок для меня?"
            $herView.hideshowQQ( "body_12.png", pos )
            her "Ох... Понятно..."

        elif one_of_ten == 5:
            $herView.hideshowQQ( "body_06.png", pos )
            her "Все в порядке, спасибо, что спросили."

        elif one_of_ten == 6:
            $herView.hideshowQQ( "body_11.png", pos )
            her "Я выгляжу толстой?"
            $herView.hideshowQQ( "body_29.png", pos )
            her "Надеюсь, диета сработает..."
           
        elif one_of_ten == 7:
            $herView.hideshowQQ( "body_16.png", pos )
            her "Помню я говорила, что книги мои лучшие друзья..."
            $herView.hideshowQQ( "body_24.png", pos )
            her "Теперь это звучит так неубедительно."
            $herView.hideshowQQ( "body_15.png", pos )
        
        elif one_of_ten == 8:
            $herView.hideshowQQ( "body_04.png", pos )
            her "Добавим яйца Эшвиндера..."
            her "Затем подкову и шапку красноголовика..."
            her "Затем сок морской капусты..."
            $herView.hideshowQQ( "body_10.png", pos )
            her "Или сначала тимьян?"
            $herView.hideshowQQ( "body_13.png", pos )
            her ".............."
            $herView.hideshowQQ( "body_24.png", pos )
            her "Ох, какая разница?"
            $herView.hideshowQQ( "body_06.png", pos )
       
        elif one_of_ten == 9:
            $herView.hideshowQQ( "body_14.png", pos )
            her "Вы думаете, я нанесла достаточно макияжа?" 
            her "Если его будет слишком много, то это будет выглядеть вульгарно..."
            $herView.hideshowQQ( "body_13.png", pos )
            her "Но и слишком мало тоже плохо..."
            $herView.hideshowQQ( "body_12.png", pos )
            her "Я не должна выглядеть как простушка!"
            
        elif one_of_ten == 10:
            $herView.hideshowQQ( "body_64.png", pos )
            her "Вы хотите посмотреть на мои сиськи, сэр?" 
            $herView.hideshowQQ( "body_111.png", pos )
            her "25 очков, пожалуйста."
            $herView.hideshowQQ( "body_120.png", pos )
    
   
    if hermi.whoring >= 21: # hermi.whoring LEVEL 08+.
        
        if one_of_ten == 1:
            $herView.hideshowQQ( "body_189.png", pos )
            her "У вас есть еще ненужные журналы для взрослых, сэр?"
            $herView.hideshowQQ( "body_188.png", pos )

        elif one_of_ten == 2:
            $herView.hideshowQQ( "body_31.png", pos )
            her "Извиняюсь, что беспокою вас..."
            her "Но не найдется ли у вас несколько презервативов?"
            $herView.hideshowQQ( "body_34.png", pos )
            her "Конечно же, это не для меня... Для друзей..."
                 
        elif one_of_ten == 3:
            $herView.hideshowQQ( "body_14.png", pos )
            her "В последнее время очень холодно..."
            $herView.hideshowQQ( "body_06.png", pos )
            her "Я надеюсь, что скоро выпадет снег..."
        
        elif one_of_ten == 4:
            $herView.hideshowQQ( "body_127.png", pos )
            her "Прыгать и кричать 'За Гриффиндор!'"
            $herView.hideshowQQ( "body_80.png", pos )
            her "Смелые, удалые, красно-золотые!"
            $herView.hideshowQQ( "body_06.png", pos )

        elif one_of_ten == 5:
            $herView.hideshowQQ( "body_10.png", pos )
            her "Я надеюсь, что бал пройдет гладко..."
            $herView.hideshowQQ( "body_13.png", pos )

        elif one_of_ten == 6:
            $herView.hideshowQQ( "body_06.png", pos )
            her "Интересно, что наденет Джинни на бал..."
        
        elif one_of_ten == 7:
            $herView.hideshowQQ( "body_16.png", pos )
            her "Учитывая, как теперь все устроено с очками... Вы можете продолжать меня пользовать, сэр..."
            $herView.hideshowQQ( "body_11.png", pos )
            her "И кстати, нынче я редко надеваю белье..."
        
        elif one_of_ten == 8:
            $herView.hideshowQQ( "body_117.png", pos )
            her "Сэр, хотите вставить свой член мне в рот?"
            $herView.hideshowQQ( "body_135.png", pos )
            her "Сэр, я прошу вас..........."
            $herView.hideshowQQ( "body_111.png", pos )
            her "Отлично! Пятьдесят пять очков, будьте добры!"
            $herView.hideshowQQ( "body_122.png", pos )

        elif one_of_ten == 9:
            $herView.hideshowQQ( "body_127.png", pos )
            her "Прочитала статью, в которой говорится о положительном влиянии спермы на кожу женщины..."
            $herView.hideshowQQ( "body_128.png", pos )
            her "Интересно, как они это узнают..."
            $herView.hideshowQQ( "body_122.png", pos )
            her "Журнал проводит какие-то исследования?"
            $herView.hideshowQQ( "body_128.png", pos )

        elif one_of_ten == 10:
            $herView.hideshowQQ( "body_127.png", pos )
            her "Это похоже на..."
            her "Сначала Гриффиндор, потом Когтевран, потом Пуффендуй..."
            $herView.hideshowQQ( "body_186.png", pos )
            her "И Слизерин не попадает в этот список!"
            $herView.hideshowQQ( "body_120.png", pos )

    jump hermione_main_menu

###Hermione dialogues ###

label hermione_bookbuying:
    if teacher_jinn_quest == 3 : 
        m "Мисс Грейнджер."
        m "Могу ли я купить ваши учебники?"
        $herView.hideshowQQ( "body_15.png", pos )
        her "Простите?"
        m "Мне нужны ваши учебники."
        $herView.hideshowQQ( "body_14.png", pos )
        her"Но зачем вам, Альбусу Дамблдору, учебники простой ученицы?"
        m "Хм, понимаешь..."
        m "Я проводил сложные магические исследования."
        m "Но совсем недавно они зашли в тупик."
        m "И я решил прибегнуть к последнему средству."
        m "Я говорил с зябликом."
        $herView.hideshowQQ( "body_205.png", pos )
        her "Что?!"
        m "Да, с {i}тем самым{/i}."
        m "Он поведал, что мне стоит вернуться к самым истокам."
        m "Что истина лежит в начале пути, и тому подобную хрень."
        $herView.hideshowQQ( "body_09.png", pos )
        her "..."
        m "Поэтому я хочу еще раз повторить весь материал, с самого начала."
        m "Так что... Не одолжите ли свои книги?"
        $herView.hideshowQQ( "body_06.png", pos )
        her "Профессор..."
        $herView.hideshowQQ( "body_14.png", pos )
        her "Конечно, я бы с радостью пожертвовала свои книги во благо науки!"
        $herView.hideshowQQ( "body_07.png", pos )
        her "Но вы же сами понимаете, что мне сейчас нужно заниматься, как никогда."
        $herView.hideshowQQ( "body_11.png", pos )
        her "Почему бы вам не заказать их на азазоне?"
        m "Где, прости?"
        her "На азазоне. Неужели вы ни разу не слышали о сово-магазине azazon.mag?"
        her "Крупнейшем магическом магазине с доставкой по всему миру?"
        m "Звучит... Знакомо. Даже слишком знакомо."
        m "Знаешь, я не слишком разбираюсь во всем этом, не могла бы ты сделать заказ за меня?"
        $herView.hideshowQQ( "body_01.png", pos )
        her "Конечно. Какие именно книги вас интересуют?"
        m "Все книги по всем предметам, которые преподают в этой школе."
        $herView.hideshowQQ( "body_10.png", pos )
        her "Что же, думаю это будет стоить тысячи три, не меньше..."
        m "..."
        g4 "{size=-4}Дорого же мне обходится твое \"обучение\", маленькая стерва...{/size}" #маленький размер
        g4 "{size=-4}Черт, быть может мне все же остановиться на роуте, где я просто делаю из тебя шлюху, продающую свой зад за очки?{/size}" #маленький размер
        g9 "Эх, выборы-выборы..."
        $herView.hideshowQQ( "body_08.png", pos )
        her "Вы что-то сказали?"
        m "Нет-нет, я просто размышлял над выбором... Школьной политики."
        $herView.hideshowQQ( "body_06.png", pos )
        her "Так вы все-таки решили подумать над моими предложениями..?"
        $herView.hideshowQQ( "body_12.png", pos )
        her "Я думала, что вы забыли..."
        m "Я ничего не забываю, девочка."
        $herView.hideshowQQ( "body_45.png", pos )
        her "..."
        m "Кто знает, быть может со следующим обновлением..."
        $herView.hideshowQQ( "body_13.png", pos )
        her "Что?"
        m "Кхм, не важно."
        m "В общем, спасибо за помощь. Я сообщу вам, когда у меня появится нужная сумма."
        $herView.hideshowQQ( "body_06.png", pos )
        her "Всегда рада помочь."
        $ teacher_jinn_quest = 4
        jump hermione_main_menu
        
    elif teacher_jinn_quest == 4 and gold >= 3000:
        m "Я по поводу покупки учебников, мисс Грейнджер."
        m "У меня есть нужная сумма."
        $herView.hideshowQQ( "body_06.png", pos )
        her "Хорошо, тогда я немедленно пойду и закажу все необходимое."
        # гермиона уходит
        hide screen bld1
        $herView.hideQ( Dissolve(.3) )
        $ walk_xpos=400 #Animation of walking chibi. (From)
        $ walk_xpos2=610 #Coordinates of it's movement. (To)
        $ hermione_speed = 02.0 #The speed of moving the walking animation across the screen.
        show screen hermione_walk_01_f 
        pause 2
        hide screen hermione_walk_01_f 
        $ hermione_chibi_xpos = 610 #Near the desk.
        show screen hermione_01_f #Hermione stands still.
        with Dissolve(.3)
        $ renpy.play('sounds/door.mp3') #Sound of a door opening.
        hide screen hermione_01_f #Hermione stands still.
        with Dissolve(.3)
        $ gold -=3000
        $ hermione_takes_classes = True
        $ hermione_sleeping = True
        $ teacher_jinn_quest = 5
        m "...."
        m "..."
        m "Интересно, сколько шлюх можно было купить на эти деньги?"
        m "..."
        m "Надо передернуть."
                        
        if daytime:
            jump night_main_menu
                        
        else:
            jump day_main_menu
                            
    else:
        m "{size=-4}(Нужно больше золота!){/size}"
        m "(У меня такое ощущение, что где-то я уже слышал эту фразу...)"
        jump hermione_main_menu
