label menu_reading_book:
    $choose=None
    if choose==None:
        $ choose = RunMenu()
    else:
        $choose.Clear()
    python:
        for e in this.List:
            if e.GetValue("block")==_block and e._status>=0: # Нужно ставить GetValue("block")  а не _block - у ивента такого объекта может не быть
                choose.AddItem("- Книга: "+e._caption+" - "+("{image=check_08.png}" if e.IsDone() else ""), 
                    "reading_book_done" if e.IsDone() else "menu_reading_book_2", True, e.Name)
        choose.AddItem("- Ничего -", "books_list", True, "")

    $ choose.Show()

    label menu_reading_book_2:
        $ the_gift = event._img#"03_hp/18_store/08.png" # Copper book of spirit.
        show screen gift
        with d3

        "\"[event._caption]\"" "[event._description]"#" Вы хотите прочитать ее?"
        menu:
            "- Читать книгу -":
# Проверяем, что освоены предыдущие ступени навыка:
                if event.GetValue("block")=="books_edu":
                    if event.prevInList.GetValue("block")!=event.GetValue("block") or event.prevInList.IsDone():
                        jump reading_book_xx
                    else:
                        m "Эта книга пока слишком сложна для меня."
                        hide screen gift
                        jump books_list
                else:
                    if event.Name=="book_05_b" and not this.book_05.IsDone():
                        m "Есть странные люди, которые приступают к книге со второй ее части. Но я не из таких."
                        jump expression _label
                    else:
                        jump reading_book_xx #"reading_book_01"
            "- Ничего -":
                hide screen gift
                jump expression _label #books_on_improvement

    label reading_book_done:
        $ the_gift = event._img#"03_hp/18_store/08.png" # Copper book of spirit.
        show screen gift
        with d3
        "\"[event._caption]\"" "[event._description]."


# Отдельная обработка для Вайфу - ее нужно читать несколько раз                                
        if event.Name=="book_07":
            if waifu_book_completed:
                m "Я не думаю, что повторное чтение этой книги даст мне хоть что-то."
                hide screen gift
                jump fiction_books

            if dear_waifu_completed_once:
                if book_07_units == 0:
                    m "Не думаю, что повторное чтение этой книги даст мне хоть что-то. Прочесть ее просто ради удовольствия?"
                    menu:
                        "- Читать книгу снова -":
                            hide screen gift
                            jump reading_book_xx
                        "- Ничего -":
                            hide screen gift
                            jump fiction_books
                else:
                    m "Я уже закончил ее, но решил прочесть еще раз ради удовольствия..."
                    hide screen gift
                    jump reading_book_xx
        else:
            m "Я уже закончил ее. "
            if event._block=="books_edu" and event._conclusion!="":
                m "Она дала мне новый навык: [event._conclusion]"
            else:
                m "[event._conclusion]"

            if event.Name=="book_04":
                g4 "Я обуздал свой дух!"
                g9 "Мой дух - моя сучка!"

        hide screen gift
        jump expression _label

label desk:
    menu:
        "- Осмотреть -" if not desk_examined:
            $ desk_examined = True
            m "Обычный стол..."
            jump day_main_menu
        "- Делать бумажную работу -" if finished_report < 6 and not got_paycheck and not day == 1 and work_unlock2:
            jump paperwork
        "{color=#858585}- Делать бумажную работу -{/color}" if finished_report >= 6 and not got_paycheck:
            m "Я уже завершил шесть отчетов на этой неделе."
            jump desk
        "{color=#858585}- Делать бумажную работу -{/color}" if got_paycheck: # When TRUE paycheck is in the mail.
            m "Сначала мне нужно получить оплату."
            jump desk
         
        "- Книжная коллекция -" if not day == 1 and cataloug_found: 
            label books_list:
                $choose=None
                menu:
                    "- Обучающие книги -":
                        label books_on_improvement:
                            $_label="books_on_improvement"
                            $_block="books_edu"
                            jump menu_reading_book

                    "- Фантастика -":
                        label fiction_books:
                            $_label="fiction_books"
                            $_block="books_fict"
                            jump menu_reading_book

                    "- Ничего -":
                        jump desk

        "- Продолжить чтение -" if currentBook!=None:
            $event=this(currentBook)
            jump reading_book_xx 
          
        
                    
                    
                    
        #"- The muggle oddities -" if have_catalogue: #Real thing
        "- Приблуды Дахра -" if cataloug_found: 
            if order_placed or package_is_here:
                show screen bld1
                with d3
                dahr "Пожалуйста, потерпите чуть-чуть. Сова уже в пути."
                hide screen bld1
                with d3
                jump desk
            else:
                 jump the_oddities
        
        
        

        # "- Подрочить на трусики Гермионы -" if request_03: #True when Hermione has no panties on.
        #     jump jerk_off
        "- Передернуть -" if not day < 5:
            jump jerk_off 
        "- Состояние Гермионы -" if this.Has("her_wants_buy"): #summoning_hermione_unlocked and buying_favors_from_hermione_unlocked: 
            "> Распутство: {color=#B40000}{size=+4}{b}[whoring]{/b}{/size}{/color}-я степень."
            "> Злость: {color=#B40000}{size=+4}{b}[mad]{/b}{/size}{/color}-я степень"
            if mad >=1 and mad < 3:
                "> Гермиона по-прежнему {b}немного расстроена{/b} вами..."
            elif mad >=3 and mad < 10:
                "> Вы {b}расстроили{/b} Гермиону."
            elif mad >=10 and mad < 20:
                "> Гермиона {b}очень расстроена{/b} вами."
            elif mad >=20 and mad < 40:
                "> Гермиона {b}злится{/b} на вас."
            elif mad >=40 and mad < 50:
                "> Гермиона {b}очень злится{/b} на вас."
            elif mad >=50 and mad < 60:
                "> Гермиона {b}гневается{/b} на вас."
            elif mad >=60:
                "> Гермиона {b}ненавидит{/b} вас."
            else:
                "> Гермиона {b}не злится{/b} на вас"
            jump desk
        "- Дремать -" if daytime and not day == 1:
            jump night_start
        "- Спать -" if not daytime and not day == 1:
            jump day_start
            

        "- Ничего -":
            call screen main_menu_01
            
            

        
  
            
            


    
### READING ###

label reading_book_xx:

### Plays sound effects appropriate for reading. 
# Music
    stop music fadeout 2.0
    if fire_in_fireplace:
        play bg_sounds "sounds/fire02.mp3" fadeout 1.0 fadein 1.0 #Quiet...
    else:
        call fire_out #Shows Genie reading a book near the window.

    if daytime and not raining:
        #play bg_sounds "sounds/day.mp3" fadeout 1.0 fadein 1.0 #Quiet...
        play weather "sounds/day.mp3" fadeout 1.0 fadein 1.0 #Quiet...

    
    if not daytime and not raining:
        play weather "sounds/night.mp3" fadeout 1.0 fadein 1.0 #Quiet...


    if raining:
        play weather "sounds/rain.mp3" fadeout 1.0 fadein 1.0 #Quiet...


    hide screen gift
    with d3
    if fire_in_fireplace:
        call fire_in #Shows Genie reading a book near the fireplace.
    else:
        call fire_out #Shows Genie reading a book near the window.


    if raining:
        ">Вы читаете книгу [event._caption], слушая дождь, барабанящий по крыше вашей башни."
    else:
        ">Вы читаете книгу [event._caption]..."
   
    call chap_finished_xx
    
    call chapter_check_book_xx #Checks if the chapter just finished was the last one.
    
    
#===### SPEED READING FOR DUMMIES BONUS CHECK ###
    if s_reading_lvl>0:
        $ speed_dummies = Rand([60,30,20][s_reading_lvl-1]//turbo)  # Массив содержит размер интервала для расчета вероятности. Первая книга 10/60 шансов прочитать доп. главу, вторая 10/30, 3-я 10/20 . В режиме турбо интервал уменьшается вдвое
        if speed_dummies <= 10: #Success.
            ">Используя изученные вами начальные методы скорочтения, вы рациональнее используете время и продолжаете читать."
            call chap_finished_xx
            call chapter_check_book_xx #Checks if the chapter just finished was the last one.
#            ">Осталось еще несколько глав."

#===#############################################       

    if raining:
        if not fire_in_fireplace:
            ">Дождь за окном успокаивает вас, и вы отлично себя чувствуете, читая..."
            ">Вы пытаетесь продолжить читать, но вскоре понимаете, что воздух в комнате слишком влажный."
        else:
            ">Дождь за окном успокаивает вас, и вы отлично себя чувствуете, читая..."
            call chap_finished_xx
            call chapter_check_book_xx #Checks if the chapter just finished was the last one.
#            ">Осталось еще несколько глав."

    ">Осталось еще несколько глав."       
    $currentBook=event.Name

    if fire_in_fireplace:
        hide screen reading_near_fire
    else:
        hide screen reading

    if daytime:
        jump night_start #pered_menu#
    else: 
        jump day_start
        
######    
label chap_finished_xx:
    if event.Name=="book_05":
        $event.IncValue("status", 1)  #+=1
        $renpy.say("Глава [event._status]", 
        [
         "Повествуется о Галадриэли - нежной и доброй эльфийской принцессе.",
         "Повествуется об отце Галадриэли - Короле Метисе и его друге детства - Мофоселисе.",
         "Король Метис объявляет о помолвке своей дочери, принцессы Галадриэль с канцлером Мофоселисом.",
         "Галадриэль отказывается выйти замуж за человека, который в три раза старше ее и которого, до этой поры, она считала своим дядей.",
         "Король Метис не слушает \"глупые\" жалобы дочери. Галадриэль решает бежать.",
         "Галадриэль удается покинуть королевские покои ночью ...",
         "Король Метис в ярости из-за побега дочери. Он решает лично возглавить поиски.",
         "Галадриэль едет на своей кобыле \"Белая голубка\" через лес. Принцесса наслаждается свободой... Вскоре она встречает всадника - весьма приятного человеческого дворянина...",
         "Галадриэль едет вместе с дворянином. Они обмениваются шутками, и он очень забавляет ее. Вдруг дворянин нападает на принцессу и сильным ударом лишает сознания!...",
         "Галадриэль приходит в себя. Она с ужасом чувствует, что дворянин входит в нее. Галадриэль зовет на помощь, но красавчик крепко держит ее и жестоко насилует.",
         "Галадриэль безуспешно пытается вырваться. И тут она замечает, что ее окружает полдюжины мужчин, которые злобно ухмыляются.",
         "После того, как дворянин заканчивает с Галадриэль, его люди пускают эльфийскую принцессу по кругу. Галадриэль плачет и умоляет их прекратить.",
         "Галадриэль приходит в себя в клетке на каком-то рынке. Ее руки связаны, ее благородные одежды разорваны в клочья, а волосы полны веток и сухой спермы.",
         "Жирный, богатый мужчина покупает Галадриэль и приводит ее в свой дом. Принцесса больше не плачет. Она счастлива выбраться из клетки.",
         "Галадриэль позволили принять ванну, после чего раб приносит ей чистую одежду и еду.",
         "Галадриэль начинает надеяться, что ее беды позади, но это не так. Вскоре она понимает, что это за место: бордель.",
         "Эльфийская принцесса вынуждена работать шлюхой. Она ненавидит свою новую жизнь, но у нее не остается выбора.",
         "Галадриэль быстро набирает популярность. Люди, Темные Эльфы и даже карлики, она раздвигает ноги для всех.",
         "Слава о молодой и красивой эльфийской шлюхе распространяется окрест. Галадриэль принимает свою новую жизнь в борделе.",
         "Но внезапно все резко меняется. Галадриэль узнает, что она беременна. - Конец первой книги -"
        ][event._status-1]
        )


    if event.Name=="book_05_b":
        $event.IncValue("status", 1)  #+=1
        $renpy.say("Глава [event._status]",
        [   
         "Галадриэль беременна уже несколько месяцев. К удивлению принцессы, ее популярность растет, как будто в прямой зависимости от размера ее живота.",
         "Хотя Галадриэль и ведет себя, как послушная шлюха, на самом деле, она продумывает побег из борделя.",
         "Эльфийская принцесса-шлюха ничего не знает о жизни за стенами борделя. Но это не влияет на ее решимость спастись.",
         "Планирование побега из борделя занимает много времени, но в конце-концов Галадриэль удается бежать.",
         "Галадриэль теряется в огромном городе и вынуждена провести ночь на улице.",
         "На улицах трудно найти еду. Галадриэль борется со стаей бродячих собак, и одна из них кусает Галадриэль за руку.",
         "Беременная Галадриэль предлагает составить компанию  паре грязных бездомных мужчин в обмен на еду. С ними она проводит ночи.",
         "Галадриэль понимает, что ее жизнь в борделе была раем по сравнению с тем, что она имеет теперь. Она решает вернуться обратно.",
         "Владелец Галадриэль - жирный, богатый человек не наказывает Галадриэль за побег. Наоборот, он счастлив, что одна из его самых популярных девушек вернулась.",
         "Галадриэль снова в тепле и чистоте, ее хорошо кормят. Она рада, что вернулась и популярна, как никогда.",
         "Галадриэль обслуживает клиентов на протяжении всей беременности. Ребенок вот-вот родится...",
         "Богатый человек в маске заказывает Галадриэль на весь день. Лениво ублажая клиента, Галадриэль гадает кто бы это мог быть.",
         "Таинственный человек целый день развлекается с Галадриэль. Из наполненных грудей принцессы капает молоко, в то время, как человек трахает ее.",
         "Человек в маске кончает на лицо Галадриэль во второй раз за сегодня. Затем он решает снять маску и показать лицо.",
         "Галадриэль обнаруживает, что этот человек - ее отец, король Метис. Только тут и он понимает, что беременная шлюха, которую он трахал несколько часов - его дочь.",
        # Only now he realizes that the pregnant whore he fucked for hours is his daughter.
         "Он обнимает свое потерявшее дар речи дитя. Глаза Галадриэль пусты. Сперма отца капает с ее лица...",
         "Галадриэль в ужасе кричит. К ее удивлению, она обнаруживает себя в королевских покоях, в своей постели.",
         "Проходит несколько минут, пока она понимает, что она никогда не была беременна. Все приключения - это лишь сон.",
         "Галадриэль бросается к отцу и обнимает его. Девушка пережила слишком многое в \"прошлой жизни\". Она счастлива и соглашается выйти замуж за канцлера Мофоселиса.",
         "{size=-1}Галадриэль стоит у алтаря. Она довольна и счастлива. Вдруг она замечает нечто, что наполняет ее сердце ужасом. На ее руке - шрам. Место укуса собаки. - Конец -{/size}"
        ][event._status-1]
        )

    if event.Name=="book_06":
        $event.IncValue("status", 1)  #+=1
        $renpy.say("Глава [event._status]", 
        [
        "Семейство благородных северян.",
        "Королевская семья и король.",
        "Другое семейство.",
        "Инцест между братом и его сестрой-королевой.",
        "Покушение на ребенка. Он чудом выживает, но находится в коме.",
        "Другие персонажи.",
        "Одни персонажи строят козни против других.",
        "Короля отравили и он умирает. Еще несколько инцестов между братом и сестрой.",
        "Казнили некоторых персонажей, за которых вы болели.", # НЕ ПЕРЕВЕДЕНо
        "Появилось несколько новых персонажей.",
        "Некоторые женщины были изнасилованы и жестоко убиты.",
        "Еще несколько членов дворянской семьи северян безвременно почили.",
        "Еще больше женщин изнасилованы. Некоторым из них удается выжить. (Разумеется, чтобы их изнасиловали чуть позже).", 
        "Персонажи, которых вы ненавидите сталкиваются в эпической битве против персонажей, за которых вы болеете.",
        "Большинство персонажей, которых вы ненавидите пережили сражение. Все, за кого вы болели, мертвы.",
        "Еще несколько изнасилований и убийств... (Вас это уже не трогает...)", 
        "Новые персонажи появляются в истории. Вы, вроде, начинаете болеть за одного из них.",
        "Персонаж, за которого вы болеете, влюбляется в милую девушку.",
        "Персонаж, за которого вы болели, зверски убит. Его девушку насилуют и тоже убивают.",
        "Новая раса наполовину замороженной нежити включается в историю. Продолжение следует..."
        ][event._status-1]
        )

    if event.Name=="book_07":
        $ book_07_units +=1
        $event._status=book_07_units
        call waifu
        
    $ renpy.play('sounds/win_04.mp3')   #Not loud.
    hide screen notes
    show screen notes
    if event._block=="books_edu": 
#        $event._status=this.GetCall(event.Name).SetValue("status", event._status+1)  #event.SetValue("status", event._status+1)  #+=1
        $event.IncValue("status", 1)    
    ">Вы закончили \"главу [event._status]\" этой книги."
    return
    
###
label chapter_check_book_xx: #Checks if the chapter just finished was the last one.
    if (event.IsDone() and event.Name!="book_07") or (event.Name=="book_07" and book_07_units == 20):#book_xx_units == 10:
        if fire_in_fireplace:
            show screen done_reading_02  
            hide screen reading_near_fire
        else:
            show screen done_reading  
            hide screen reading

        $ renpy.play('sounds/win_04.mp3')   #Not loud.
        hide screen notes
        show screen notes
        ">Это была последняя глава. Вы закончили эту книгу."
        $currentBook=None

        if event.Name=="book_06":
            g4 "Что за херня! Я ненавижу человека, который это написал!"
            m "Впрочем, все эти изнасилования натолкнули меня на пару идей..."


        if event.Name=="book_07":
            if complited_leena_already and complited_shea_already and complited_stevens_already and victoria >= 1 and shea >= 1 and leena >= 1: #Harem ending. The DAHR's ticket.
                m "Вау! Отличная книга! Это было неплохо!"
                
                #m "No, I mean it! What a great peace of fiction! That Akabur dude must be a genius!"
                if not found_dahrs_ticket_once:
                    m "Хм...?"
                    m "Что это...? Закладка?"
                    $ the_gift = "03_hp/18_store/06.png" # The DAHR's ticket.
                    show screen gift
                    with d3
                    $ renpy.play('sounds/win2.mp3') #Sound of finding an item.
                    ">Вы нашли ваучер Дахра."
                    hide screen gift
                    with d3
                    m "Хм..."
                    $ vouchers += 1 #Shows the amount of DAHR's vouchers in your possession.
                    $ found_dahrs_ticket_once = True # Turns TRUE after you complete "My Dear Waifu" with the harem ending and "Dahr's voucher" fall out.
                    $ waifu_book_completed = True
            elif shea_waifu and shea >= 8: 
                if not complited_shea_already: #Finished with Shea for the first time.
                    m "Неплохо. Я действительно готов заботиться о Ши ..."
                    g9 "Ну, о ней и ее анальной девственности..."
                    $ complited_shea_already = True
                else: #Finished with Shea for the second time.
                    m "Значит в конце я снова с Ши?"
                    m "Хм... Может быть, я должен попробовать и выбирать другие варианты в следующий раз...?"
            elif victoria_waifu and victoria >= 7:
                if not complited_stevens_already: #Finished with Ms.Stevens for the first time.
                    m "Неплохо, неплохо. Госпожа Стивенс оказалась той еще шлюхой..."
                    $ complited_stevens_already = True
                else: #Finished with Shea for the second time.
                    m "Значит в конце я снова с госпожой Стивенс?"
                    m "Хм... Может быть, я должен попробовать и выбирать другие варианты в следующий раз...?"
            elif leena_waifu and leena >= 8:
                if not complited_leena_already: #Finished with Leena for the first time.
                    g9 "Славненько! Обожаю хэппи энды!"
                    $ complited_leena_already = True
                else: #Finished with Shea for the second time.
                    m "Значит, в конце я снова со светленькой девахой?"
                    m "Хм... Может, в следующий раз попробовать выбирать другие варианты...?"

            else:
                m "Хм ... Конец очень разочаровал..."
                m "Может, я должен прочитать ее еще раз когда-нибудь..."
            
            $ book_07_units = 0 #RESTING THE BOOK FOR ANOTHER PLAYTHORUGH.
            $ shea = 0 #RESETING SHEA'S POINTS FOR THE NEXT PLAYTHOURGH.
            $ victoria = 0
            $ leena = 0

            if not dear_waifu_completed_once:
                $ dear_waifu_completed_once = True # Turns TRUE when complete the book for the first time with any ending. Makes sure you get +1 imagination only once.
                $ imagination +=1


        $ renpy.play('sounds/win_04.mp3')   #Not loud.
        hide screen notes
        show screen notes
        if event._conclusion!="":
            if event._block=="books_edu":
                m "Новый навык: [event._conclusion]"
            else:
                m "[event._conclusion]"

# Изменения навыка по завершению книги (кроме Вайфу - book_07 в ней навык меняется отдельно)
# Можно было сделать через событие, но тогда получится более громоздко. Так что пока так:
        if event.Name in ["book_01", "book_02", "book_03", "book_04"]:
            $ concentration += 1
        if event.Name in ["book_05", "book_05_b", "book_06"]:     
            $ imagination +=1
        if event.Name in ["book_08", "book_09", "book_10"]:
            $ s_reading_lvl +=1
        if event.Name in ["book_12", "book_13", "book_14", "book_15"]:
            $ speedwriting += 1

        
        if fire_in_fireplace:
            hide screen reading_near_fire
        else:
            hide screen reading
        
        if daytime:
            jump night_start
        else: 
            jump day_start
    else:
        return        
    
 

###
label fire_in: #Shows Genie reading a book near the fireplace.
    hide screen chair
    hide screen genie
    show screen reading_near_fire
    with Dissolve(0.3)
    return
###
label fire_out: #Shows Genie reading a book near the window.
    hide screen chair
    hide screen genie
    show screen reading
    with Dissolve(0.3)
    return
    
 
 
    
    
    
    
        
    
    
### PAPERWORK ###
label paperwork:
    stop music fadeout 1.0
    if daytime:
        play bg_sounds "sounds/day.mp3" fadeout 1.0 fadein 1.0 #Quiet...
    else: 
        play bg_sounds "sounds/night.mp3" fadeout 1.0 fadein 1.0 #Quiet...
    
    if raining:
        play weather "sounds/rain.mp3" fadeout 1.0 fadein 1.0 #Quiet...
        stop bg_sounds 
    
    
    hide screen genie
    show screen paperwork
    with Dissolve(0.3)
    ">Вы делаете отчет."
    
    call finished_working_chapter #Chapter finished. $ report_chapters += 1
    
    call report_chapters_check #Checks whether or not the completed chapter was the final one.
        
    if daytime: # Makes sure that check happens only at nighttime. 
        pass
    else:
        if wather_generator >= 31 and wather_generator <= 40: # FULL MOON
            call f_moon_bonus
        if wather_generator >= 51 and wather_generator <= 60: # FULL MOON
            call f_moon_bonus
           
    call report_chapters_check #Checks whether or not the completed chapter was the final one.
    
    ### CONCENTRATION CHECK ###========================================================================
    if concentration == 1:
        $ concentraton_check = renpy.random.randint(1, 6) #Copper book.
        if concentraton_check == 1:
            call concentration_label
    if concentration == 2:
        $ concentraton_check = renpy.random.randint(1, 4) #Bronze book.
        if concentraton_check == 1:
            call concentration_label
    if concentration == 3:
        $ concentraton_check = renpy.random.randint(1, 2) #Silver book.
        if concentraton_check == 1:
            call concentration_label
    if concentration == 4:                                                               #Golden book.
        call concentration_label
#    if concentration == 5:
#        $ concentraton_check = renpy.random.randint(1, 2) #Platinum book.
#        if concentraton_check == 1:
#            call concentration_label
#    if concentration == 6:
#            call concentration_label
    ###==============================================================================================
    
    call report_chapters_check #Checks whether or not the completed chapter was the final one.
    
    ### SPEEDWRITING CHECK ###========================================================================
    if speedwriting == 1:
        $ speedwriting_check = renpy.random.randint(1, 6) #"\"Speedwriting for dummies.\"" # 1/10 chance
        if speedwriting_check == 1:
            call speedwriting_label
    if speedwriting == 2:
        $ speedwriting_check = renpy.random.randint(1, 4) #"\"Speedwriting for beginners.\"" # 1/8 chance of it to pop up.
        if speedwriting_check == 1:
            call speedwriting_label
    if speedwriting == 3:
        $ speedwriting_check = renpy.random.randint(1, 2) #"\"Speedwriting for intermediate.\"" # 1/6 chance of it to pop up.
        if speedwriting_check == 1:
            call speedwriting_label
    if speedwriting == 4:
            call speedwriting_label
#    if speedwriting == 5:
#        $ speedwriting_check = renpy.random.randint(1, 2) #"\"Speedwriting for experts.\"" # 1/2 chance of it to pop up.
#        if speedwriting_check == 1:
#            call speedwriting_label
#    if speedwriting == 6:
#        call speedwriting_label #""\"Speedwriting for maniacs.\"" # 1 (sure) chance of it to pop up.
    
    call report_chapters_check #Checks whether or not the completed chapter was the final one.
            

    show screen genie
    hide screen paperwork
    
    
    
    if daytime:
        jump night_start
    else: 
        jump day_start    
    
### 
label report_chapters_check:
    if report_chapters >= 7:
        ">Вы закончили отчет."
        $ report_chapters = 0
        $ finished_report += 1
    return
### FULL MOON BONUS ###
label f_moon_bonus:
    $ renpy.play('sounds/win_04.mp3')   #Not loud.
    hide screen notes
    show screen notes
    $ report_chapters += 1
    ">Полнолуние сделало вас более продуктивным.\n>Вы закончили [report_chapters]-ю главу."
    return
###
label finished_working_chapter:
    $ report_chapters += 1
    $ renpy.play('sounds/win_04.mp3')   #Not loud.
    hide screen notes
    show screen notes
    ">Вы закончили [report_chapters]-ю главу."
    return
### CONCENTRATION
label concentration_label:
    $ renpy.play('sounds/win_04.mp3')   #Not loud.
    hide screen notes
    show screen notes
    $ report_chapters += 1
    ">Во время работы вы идеально сконцентрированы.\n>И заканчиваете дополнительную главу.\n>Вы закончили [report_chapters]-ю главу."
    return
### SPEEDWRITING
label speedwriting_label:
    $ renpy.play('sounds/win_04.mp3')   #Not loud.
    hide screen notes
    show screen notes
    $ report_chapters += 1
    ">Вы используете свой навык скорописания.\n>И заканчиваете дополнительную главу.\n>Вы закончили [report_chapters]-ю главу."
    return
    
    
### READING GALADRIEL BOOKS IN PROPER ORDER ###
label gal_proper:
    m "Чтение книг не дает мне ничего."
    hide screen gift
    return
    
    
    
### READING A BOOK BLOCK ### Sends here to make sure that proper SFX is played during reading a book.
label reading_block:
    stop music fadeout 2.0
    if fire_in_fireplace:
        play bg_sounds "sounds/fire02.mp3" fadeout 1.0 fadein 1.0 #Quiet...
    else:
        call fire_out #Shows Genie reading a book near the window.

    if daytime and not raining:
        #play bg_sounds "sounds/day.mp3" fadeout 1.0 fadein 1.0 #Quiet...
        play weather "sounds/day.mp3" fadeout 1.0 fadein 1.0 #Quiet...

    
    if not daytime and not raining:
        play weather "sounds/night.mp3" fadeout 1.0 fadein 1.0 #Quiet...


    if raining:
        play weather "sounds/rain.mp3" fadeout 1.0 fadein 1.0 #Quiet...
    
    return
