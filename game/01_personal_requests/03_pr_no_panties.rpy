################### REQUEST_03 (Level 02) (Available during daytime only). "Give me your Трусики" ###############################
label new_request_03: #(Whoring = 3 - 5)
    if hermi.whoring <= 2:
        jump too_much
    $herView.hideQQ()
    
    $ pos = POS_370
    
    m "{size=-4}(Попросить ее отдать мне трусики и пойти на занятия?){/size}"
    $ menu_x = 0.5 #Default position of the menu. Version B is $ menu_x = 0.2
    menu:
        "\"(Да, давай попробуем!)\"":
            pass
        "\"(Не сейчас)\"":
            $event.NotFinished()
            jump new_personal_request
    $herView.showQQ( None, pos )
    #show screen hermione_main
    her "Я слушаю, сэр."
    m "Мне нужны ваши трусики..."   
    $herView.hideQQ()
    $ menu_x = 0.5 #Menu is moved to the left side.
    $ pos = POS_120
    show screen blktone 
    show screen ctc
    $herView.showQ( "body_01.png", pos )
    with Dissolve(.3)
    pause
    
    
#    if request_03_points == 0 and whoring <= 5: #First time this event taking place. and LEVEL 02.   <===================================== ONE TIME EVENT.
    if IsFirstRun() and hermi.whoring <= 5: #First time this event taking place. and LEVEL 02.   <===================================== ONE TIME EVENT.
        stop music fadeout 10.0
#        $ new_request_03_01 = True # HEARTS.

#        $ request_03 += 1
        $herView.hideshowQQ( "body_11.png", pos )
        her "Ч-что?"
        her "Мои... Трусики...?"
        her "Профессор Дамблдор, это... как-то..."
        m "Сегодня очки даются за это, Мисс Грейнджер..."
        m "Если вам не интересно, можете уходить."
        her "Нет, мне интересно. Просто это..."
        her "Вам нужны мои...."
        play music "music/Chipper Doodle v2.mp3" fadein 1 fadeout 1 # HERMIONE'S THEME.
        $herView.hideshowQQ( "body_47.png", pos )
        her "...Трусики, сэр?"
        m "Именно..."
        $herView.hideshowQQ( "body_66.png", pos )
        her "Могу я узнать, что вы планируете с ними делать?.."
        m "Эм... Я провожу исследования..."
        her "Но это немного странно, не находите?"
        m "Но вам ведь не нравится, что девушки из \"Слизерина\"..."
        m "Оказывают услуги за очки для факультета, не так ли, Мисс Грейнджер?"
        $herView.hideshowQQ( "body_47.png", pos )
        her "Верно!"
        $herView.hideshowQQ( "body_12.png", pos )
        her "(Эти \"Слизеринские\" шлюхи потеряли всякий стыд!)"
        $herView.hideQQ()
        m "Ну, тогда давайте!"
        $herView.hideshowQQ( "body_66.png", pos )
        her "А?"
        m "Победите их в их же собственной игре!"
        $herView.hideshowQQ( "body_14.png", pos )
        her "Что?"
        m "Да! Вы можете вывести \"Гриффиндор\" снова в лидеры..."
        m "Побив этих девок их же оружием!"
        $herView.hideshowQQ( "body_11.png", pos )
        her "Профессор..."
        m "Директор не может иметь любимчиков, однако вы знаете, что я чувствую к \"Гриффиндору\"..."
        m "И я бы мог просто дать вам очки, если бы только это не разрушило всю систему..."
        show screen blktone8
        $herView.hideQQ()
        ">Внезапно Гермиона протягивает вам руку..."
        ">Вы замечаете, что она сжимает какую-то ткань в кулаке..."
        ">Ее трусики? Вы не можете понять, когда же она успела их снять..."
        m "??!"
        ">Вы получили трусики Гермионы..."
        hide screen blktone8
        with d3
        $herView.hideshowQQ( "body_67.png", pos )
        
        her "Просто возьмите их, сэр..."
        m "Что? Когда ты успела?"
        her "Ваша речь была такой трогательной..."
        her "Вы совершенно правы, сэр! Я должна победить их в этой игре."
        her "Мои занятия вот-вот начнутся. Мне лучше пойти..."
        $herView.hideQQ()

        $ pos = POS_370
        $herView.showQQ( "body_23.png", pos )
        her "..........."
        $herView.hideshowQQ( "body_29.png", pos )
        her "...надеюсь, никто не заметит, что у меня нет белья..."
        $herView.hideshowQQ( "body_31.png", pos )
        her "Ох, я вернусь за ними вечером, сэр."
        m "Конечно. Твои трусики будут лежать на моем столе и ждать тебя..."
        $herView.hideshowQQ( "body_34.png", pos )
        her "............."
        jump request_03_ends

    else: #<========================================================================================== FIRST EVENT!
#        if request_03_points == 0 and whoring < 12:
        if IsFirstRun() and hermi.whoring < 12:
            her "Эмм..."
            her " Это несколько неожиданно, сэр, но..."
        if not IsFirstRun():
            her "Снова, сэр?"
            m "Да, снова..."
        her "Вот..."
        if hermi.whoring >= 12: #LEVEL 05
            $herView.hideQQ()
            ">Гермиона достает свои трусики из кармана..."
            m "Что?"
            $herView.hideshowQQ( "body_45.png", pos )
            her "Да, у меня было ощущение, что вы их попросите сегодня, сэр."
            m "Было ощущение?"
            $herView.hideshowQQ( "body_68.png", pos )
            her "Ну, если быть честной, то я теперь не всегда их надеваю..."
            if hermi.whoring >= 15: #LEVEL 05
                $herView.hideshowQQ( "body_78.png", pos )
                her "Возможны разные ситуации, и трусики будут только мешать."
                m "Мешать?.."
                $herView.hideshowQQ( "body_68.png", pos )
                her "Ах, это неважно, сэр."
        else:
            $herView.hideQQ()
            ">Гермиона снимает трусики и отдает их вам..."
        $herView.hideQQ()
        ">Получены трусики Гермионы."
        $herView.showQQ( "body_15.png", pos )
        her "Ну, мне стоит идти на занятия. Они вот-вот начнутся..."

        
    label request_03_ends:
    $ request_03 = True #True when Hermione has no Трусики on.
    if hermi.whoring <= 5:
        $ hermi.whoring +=1
        
    hide screen bld1
    $herView.hideQ()
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

    $ hermione_takes_classes = True


    ### MUSIC BLOCK ###
    if daytime:
        play music "music/Brittle Rille.mp3" fadein 1 fadeout 1 # DAY MUSIC
    else:
        play music "music/Music for Manatees.mp3" fadein 1 fadeout 1 # NIGHT MUSIC
    ### END OF BLOCK ###
    $event.Finalize()
    jump day_main_menu
    
    
        
label new_request_03_complete: # WHORING LEVEL 02 <=================
    
    $ walk_xpos=610 #Animation of walking chibi. (From)
    $ walk_xpos2=400 #Coordinates of it's movement. (To)
    $ hermione_speed = 03.0 #The speed of moving the walking animation across the screen.
    $ renpy.play('sounds/door.mp3') #Sound of a door opening.
    show screen hermione_walk_01 
    with d4
    pause 2.5
    $ hermione_chibi_xpos = 400 #Near the desk.
    show screen hermione_02 #Hermione stands still.
    pause.5
    show screen bld1
    with Dissolve(.3)
    
    $ pos = POS_370
    $herView.showQ( "body_01.png", pos )
    show screen hermione_02
    with Dissolve(.3)

    $ pos = POS_120
    
    "Добрый вечер, сэр..."
    play music "music/Chipper Doodle v2.mp3" fadein 1 fadeout 1 # HERMIONE'S THEME.
    menu:
        "\"Вот твои трусики\"":
            if have_cum_soaced_panties:
                jump panties_soaked_in_cum
            else:
                her "Спасибо, сэр."
                her "И моя оплата?"
                m "Конечно."
        "\"Как прошел ваш день, Мисс Грейнджер?\"":
            if  hermi.whoring <= 5: #LEVEL 02. EVENT LEVEL: 01
#                $ new_request_03_01 = True # HEARTS.

                $herView.hideQQ()
                $ pos = POS_120
                $herView.showQQ( "body_15.png", pos )
                her "Ох..."
                her "Довольно обычно..."
                $herView.hideshowQQ( "body_13.png", pos )
                her "Хотя я не уверена, возможно кто-то мог заметить, что я..."
                $herView.hideshowQQ( "body_29.png", pos )
                her "....."
                $herView.hideshowQQ( "body_31.png", pos )
                her "Могу я получить свои трусики назад?"
                m "Конечно..."
                $herView.hideQQ()
                ">Вы отдаете Гермионе ее трусики..."
                if have_cum_soaced_panties:
                    jump panties_soaked_in_cum
                else:
                    $herView.hideshowQQ( "body_31.png", pos )
                    her "И мои очки?"
                    m "Да, да..."
            elif hermi.whoring >= 6 and hermi.whoring <= 8: #LEVEL 03. EVENT LEVEL 02.
#                $ new_request_03_02 = True # HEARTS.

                $herView.hideQQ()
                $ pos = POS_120
                $herView.showQQ( "body_15.png", pos )
                her "Ох..."
                her "Все как всегда..."
                her "Я была какое-то время с одноклассниками..."
                her "И у нас было короткое собрание \"ОЗМП\"..."
                translators "Напоминание.\nОЗМП - Общество по Защите Мужских Прав."
                $herView.hideshowQQ( "body_16.png", pos )
                her "Я произнесла небольшую речь на тему \"Почему нельзя обменивать очки для факультета на сексуальные услуги\"..."
                $herView.hideshowQQ( "body_12.png", pos )
                her "Я чувствовала себя не очень, так как была без белья..."
                menu:
                    "\"Ах ты, маленькая лицемерка!\"":
                        $ hermi.liking -=5
                        $herView.hideshowQQ( "body_14.png", pos )
                        her "Профессор?"
                        m "Утром ты обменяла свои трусики на очки..."
                        m "А через несколько часов осуждала подобное..."
                        #m "What would you call this?"
                        $herView.hideshowQQ( "body_69.png", pos )
                        #her "I know you are right, профессор..."
                        her "(Но нам нужны эти очки...)"
                        $herView.hideshowQQ( "body_66.png", pos )
                        her "Могу я получить свои очки?"
                        m "Что насчет трусиков?"
                        $herView.hideshowQQ( "body_34.png", pos )
                        her "Ох, их, конечно же, тоже..." 
                        if have_cum_soaced_panties:
                            jump panties_soaked_in_cum
                        else:
                            pass
                    "\"Это для блага...\"":
                        her "Именно!"
                        her "Нам очень нужны эти очки..."
                        her "Это не моя ошибка, это дыра в системе образования..."
                        $herView.hideshowQQ( "body_16.png", pos )
                        her "для остальных я буду оставаться идеалом!"
                        $herView.hideshowQQ( "body_31.png", pos )
                        her "Могу я получить свои трусики обратно, пожалуйста?"
                        if have_cum_soaced_panties:
                            jump panties_soaked_in_cum
                        else:
                            her "И мои очки."
            elif hermi.whoring >= 9: #LEVEL 04. EVENT LEVEL 03.
#                $ new_request_03_03 = True # HEARTS.

                $herView.hideQQ()
                $ pos = POS_120
                $herView.showQQ( "body_16.png", pos )
                her "Еще один обычный день в Хогвартсе..."
                her "Ничего примечательного..."
                if hermi.whoring>=15:
                    m "Отсутствие белья больше не доставляет вам неудобств, мисс Грейнджер?"
                    $herView.hideshowQQ( "body_29.png", pos )
                    her "Неудобства, сэр? О чем вы... Ах, это!"
                    her "Ну, мы же взрослые люди, профессор. Если девушка не носит белье, что в этом такого?.."
                    m "Хм... Действительно."
                else:
                    $herView.hideshowQQ( "body_29.png", pos )
                    her "Хотя, должна признаться..."
                    her "Я была по-странному свободна без белья..."
                    her "Хм..."
                $herView.hideshowQQ( "body_45.png", pos )
                her "Я могу получить свои трусики назад?"
                m "Конечно..."
                $herView.hideQQ()
                ">Вы отдаете Гермионе ее трусики..."
                if have_cum_soaced_panties:
                    jump panties_soaked_in_cum
                else:
                    $herView.hideshowQQ( "body_45.png", pos )
                    her "И мои очки?"
                    m "Да, да..."

    label back_from_panties:
    $ gryffindor +=15
    m "Пятнадцать очков \"Гриффиндору\", мисс Грейнджер. Вы заслужили." 
    her "Спасибо, сэр..."
    m "Можешь идти."
    her "Доброй ночи, сэр."
    m "Да, доброй ночи..."

    hide screen bld1
    $herView.hideQ()
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



#    $ request_03_points += 1 #Leveling up the event.
    $ request_03 = False #When False - you gave her her Трусики back.
    $ hermione_sleeping = True

    play music "music/Music for Manatees.mp3" fadein 1 fadeout 1 # NIGHT MUSIC

    if hermi.whoring<15:
        $SetHearts(GetStage(hermi.whoring, 3, 3, 3), this.new_request_03)
    else:
        $SetHearts(4, this.new_request_03)

    $event.Finalize()    
    return 
    
    
    
### Трусики SOAKED IN CUM ###
label panties_soaked_in_cum:
    $ have_cum_soaced_panties = False #TRUE when you have the Трусики in your possession (before you return them to Hermione).
    $ she_knows_about_cum = False
    $ pos = POS_120
    
    if hermi.whoring >= 3 and hermi.whoring <= 5: # LEVEL 02
        $herView.hideshowQQ( "body_71.png", pos )
        her "Хм....?"
        $herView.hideshowQQ( "body_05.png", pos )
        her "Сэр? Что это такое?"
        her "Что вы с ними сделали?"
        $herView.hideshowQQ( "body_07.png", pos )
        her "Они в чем-то скользком..."
        menu:
            "\"Эксперимент провалился.\"":
                $herView.hideshowQQ( "body_02.png", pos )
                her "Эсперимент провалился, сэр?"
                m "Да...Или, лучше сказать..."
                g9 "\"Эксперимент прошел очень хорошо\"? Хе-хе..."
                $herView.hideshowQQ( "body_07.png", pos )
                her ".....................?"
                her "Что это был за эксперимент?"
                m "Что? Ох..."
                m "Я провожу пару сверхсекретных исследований."
                m "И не могу обсуждать их со студентами."
                $herView.hideshowQQ( "body_05.png", pos )
                her "................................"
            "\"Вы мне дали их такими!\"":
                her "Я уверена, что это не так, сэр!"
                her ".........................."
        $herView.hideshowQQ( "body_71.png", pos )
        her "Ну, необходимо сперва привести их в порядок..."
        m "Или можешь надеть их прямо сейчас."
        $herView.hideshowQQ( "body_14.png", pos )
        her "Что?"
        $herView.hideshowQQ( "body_13.png", pos )
        her "Честно говоря, мне бы этого не хотелось, сэр..."
        menu:
            "\"Надень их, или потеряешь очки!\"":
                $ hermi.liking -=7
                $herView.hideshowQQ( "body_72.png", pos )
                her "Что?"
                her "Профессор, вы шутите, да?"
                m "Вообще-то нет..."
                $herView.hideshowQQ( "body_31.png", pos )
                her "Н-но..."
                $herView.hideshowQQ( "body_33.png", pos )
                her "........................................"
                $herView.hideshowQQ( "body_47.png", pos )
                her "(ВЫ всегда настаиваете на своем, сэр?)"
                m "Что такое, Мисс Грейнджер?"
                $herView.hideshowQQ( "body_30.png", pos )
                her "Ничего, сэр."
                her "Верните мне трусики!"
                $herView.hideQQ()
                show screen blktone8
                with d3
                ">Гермиона нерешительно надевает трусики..."
                ">Несколько капель спермы стекают по ее ноге..."
                ">Гермионе, видимо, очень неудобно..."
                hide screen blktone8
                with d3
                $herView.hideshowQQ( "body_34.png", pos )
                her "......................"
            "\"Ну, как хочешь...\"":
                pass
    if hermi.whoring >= 6 and hermi.whoring <= 8: # LEVEL 03 (SECOND EVENT)
        $herView.hideshowQQ( "body_71.png", pos )
        her "Мои трусики..."
        $herView.hideshowQQ( "body_73.png", pos )
        her "Что произошло с ними, сэр?"
        menu: 
            "\"Эксперимент не увенчался успехом.\"":
                her "Хм..."
                her "Понятно..."
            "\"Вы мне дали их такими!\"":
                her "Да? Ох, ясно..."
        $herView.hideQQ()
        ">Гермиона, усмехаясь, берет свои пропитанные спермой трусики..."
        $herView.hideshowQQ( "body_71.png", pos )
        her "Вероятно, их стоит привести в порядок, прежде чем надевать..."
        m "Почему бы не надеть их прямо сейчас?"
        $herView.hideshowQQ( "body_17.png", pos )
        her "Хм....?"
        $herView.hideshowQQ( "body_71.png", pos )
        her "Ну, думаю, можно их надеть еще раз, прежде чем стирать..."
        $herView.hideQQ()
        show screen blktone8
        with d3
        ">Гермиона надевает свои трусики..."
        hide screen blktone8
        with d3
        $herView.hideshowQQ( "body_34.png", pos )
        her "(Забавное ощущение...)"
        $herView.hideshowQQ( "body_44.png", pos )
        her "Это все, сэр?"
    if hermi.whoring >= 9: #LEVEL 04+ (THIRD EVENT)
        $herView.hideshowQQ( "body_71.png", pos )
        her "Мои трусики..."
        if not IsFirstRun():
            her "Они снова в чем-то скользком..."
        else:
            her "Они покрыты чем-то скользким..."
        her "И забавно пахнут..."
        $herView.hideshowQQ( "body_29.png", pos )
        her "Хм... Этот запах..."
        her "Какой-то знакомый..."
        $herView.hideshowQQ( "body_45.png", pos )
        her "Что вы с ними делали, сэр?"
        menu:
            "\"Эксперимент не увенчался успехом\"":
                her "Эксперимент, да?"
                her "Какого рода?"
                $herView.hideshowQQ( "body_46.png", pos )
                her "Нет, не отвечайте... Кажется, я знаю..."
            "\"Вы мне дали их такими!\"":
                her "Я так не думаю, сэр."
                her "Но впрочем, если вы не хотите говорить, сэр..."
                her "Я догадываюсь, что с ними произошло..."
            "\"Я кончил на них!\"":
                $ she_knows_about_cum = True
                $herView.hideshowQQ( "body_64.png", pos )
                her "Я знала это..."
                her "Они пахнут спермой!"
        $herView.hideshowQQ( "body_68.png", pos )
        her "Хм..."
        her "Похоже, стоит их постирать, прежде чем надевать..."
        $herView.hideshowQQ( "body_64.png", pos )
        her "Или вы хотите, чтобы я надела их сейчас, сэр?.."
        menu: 
            "\"Да! Надень их сейчас, девочка!\"":
                her "Ну, если так надо..."
            "\"Мне плевать. Делай, что хочешь.\"":
                her "Почему бы не надеть их еще раз?"
        
        $herView.hideshowQQ( "body_74.png", pos )
        her "Я делаю это только для того, чтобы выиграть кубок в этом году..."
        m "Верно..."
        
        $herView.hideQQ()
        
        show screen blktone8
        with d3
        ">Гермиона быстро натягивает свои влажные трусики..."
        hide screen blktone8
        with d3
        
        # NEW Branch :)
        $pos = POS_120
        if she_knows_about_cum == True and hermi.whoring >= 12:
            $herView.showQQ( "body_58.png", pos )
            her "...Сэр?"
            m "Да?"
            $herView.hideQQ()
            
            $herView.showQQ( "body_58.png", pos )
            her "Одна подруга говорила мне, что парням нравятся всякие извращения."
            $herView.hideshowQQ( "body_129.png", pos )
            her "Это правда, сэр?"
            m "Кхм, ну, если ты спрашиваешь..."
            m "Что конкретно ты имеешь в виду?"
            $herView.hideshowQQ( "body_84.png", pos )
            her "Ну, например..."
            $herView.hideQQ()
            
            $herView.data().saveState()
            #$herView.data().addPose( CharacterExItemSkirtLifted( herView.mPoseFolder, 'pose_skirt_up.png', G_Z_POSE ) )
            $herView.data().addItem( 'item_pose_lifted_skirt' )
            #$herView.data().addItemKey( 'panties_cum', CharacterExItem( herView.mMiscFolder, 'panties_sperm.png', G_Z_PANTIES + 1, 'panties' ) )
            $herView.data().addItem( 'item_panties_sperm' )
            
            $herView.showQQ( "185.png", pos )
            her "...если девушка будет в трусиках, пропитанных спермой?"
            pause
            menu:
                "\"Разумеется, парни будут в восторге!\"":
                    $herView.hideshowQQ( "body_128.png", pos )
                    her "Я так и думала, профессор."
                    $herView.hideQQ()
                    $herView.data().loadState()
                    $herView.showQQ( "body_52.png", pos )
                    her "Тогда я пойду?"
                    m "Хм, да-да, мисс Грейнджер..."
                    $herView.hideshowQQ( "body_64.png", pos )
                    her "Вы ничего не забыли, сэр?"
                    m "Ох..."
                    $herView.hideshowQQ( "body_45.png", pos )

                "\"Я думаю, это грязно!\"":
                    $hermi.liking -= 15
                    $herView.hideQQ()
                    $herView.data().loadState()
                    $herView.showQQ( "body_51.png", pos )
                    her "Хм!"
                    $herView.hideshowQQ( "body_191.png", pos )
                    her "Мои очки, сэр!"
                    
                    
    jump back_from_panties
