label event_00:
    
    play music "music/Dark Fog.mp3" fadein 1 fadeout 1 
   
    
    $ renpy.play('sounds/door.mp3') #Sound of a door opening.

    $snape.chibi.State("door", speed="go").Trans(d3, "blink")
    pause.3
    $screens.ShowD3("bld1")

    $hero(g4, "#(Туземная форма жизни!?)")

    $screens.HideD3("bld1").ShowPos(d3, "thought", gMakePos( 650, 180 )).Pause(1).ShowD3("bld1")

    $hero(m,    "#(Выглядит, как человек...)// #(Может быть, если я буду вести себя тихо, оно уйдет...?)")

    $screens.HideD3("bld1", "thought")

    $snape.LoadDefItemSets() # Эта функция просто перечитывает значения из xml. Актуальна, если что-то поменялось в наборах xml при отладке

    $snape.chibi.Trans("go center", "blink")
    $screens.ShowD3("bld1")
    $snape.State("doorleft").Visibility("body", transition=Dissolve(.5))
    $screens.ShowHide(d3, "ctc", 0.0)

    $snape("~01",    who2, "Альбус... есть минута?")
    $hero("#(\"Альбус\"? Это, должно быть, мое имя, или это так люди этого мира приветствуют друг друга?)")

    menu:
        m "..."
        "\"На самом деле я немного занят.\"":
            $snape("~04", who2, "Но ведь не постоянно?")                            
        "\"Конечно. Что там?\"":
            pass                       
        "\"И Альбус тоже.\"":
            $snape("~05", who2, "Что?",
                   "~04", who2, "Альбус, я не в настроении для ваших... издевательств.") 
        "\"Отведи меня к своему боссу.\"":
            $snape("~01", who2, "Что?// Хм...// Вы имели в виду министра магии?",
                   "~03", who2, "Я бы предпочел не иметь дел с этими бюрократами...")
            $hero("Ладно, проехали... Чем могу помочь?")

            
    $snape("~06", who2, "У меня есть важный разговор к вам...// Я думаю, нам стоит пересмотреть условия приема и отчисления.")
    $hero(              "................?")
    $snape("~03", who2, "Половина моих...так называемых \"учеников\" просто надоедливые личинки, которые отравляют каждый день моей жизни.")
    $hero(              "................")
    $snape("~07", who2, "Почти все они из \"Гриффиндора\", конечно же...")
    $hero(              "......?")
    $snape( "~07", who2,"Жалкие Уизли, шумная Грейнджер и, конечно же, герой всех несовершеннолетних правонарушителей....",
            "~08", who2,"МАЛЬЧИШКА ПОТТЕР!",
            "~01", who2,"Запомни мои слова, Альбус. \"Гриффиндор\" станет погибелью этой школы!")
    $hero(              "......................")

    $snape( "~01", who2,"Как маги они - нули без палочки!",
            "~06", who2,"Сидели бы тихо, но нет, они еще и распространяют грязные слухи о преподавателях!// В том числе, о вашем покорном слуге...")
    $hero(              "......................")
    $snape("~05", who2,"Вы ведь не верите этим слухам, правда, Альбус?")

    menu:
        m ".............."
        "\"Ну, нет конечно!\"":
            $snape( "~09", who2,"Хорошо...// Вы слишком хорошо меня знаете, чтобы верить в это... Мне не стоило переживать...")
        "\"Не бывает дыма без огня.\"":
            $snape( "~10", who2,"Альбус!? Вы серьезно?!// Это все грязная ложь, уверяю вас!")

    
    $hero(".........................")
    $snape( "~04", who2,"Эти жалкие дети совершенно достали меня. Думаю, стоит отдохнуть от всего этого сегодня.",
            "~09", who2,"................")
    
    $snape.Visibility("body", False, Dissolve(.5))


    stop music fadeout 1.0
    $screens.HideD3("bld1")
    $snape.chibi.Trans("goout door")
    $ renpy.play('sounds/door.mp3') #Sound of a door opening.
    $snape.chibi.Hide(d4)
    pause.5
    $screens.ShowD3("bld1")

    $hero("Хм...// Итак, этот высокий задумчивый парень принял меня за другого...?// Следовательно я, по всей вероятности, под действием маскирующего заклинания...",
            ".........",
            "В свою очередь я - джинн, замаскированный под человека, который, в свою очередь, замаскирован под другого человека...// Нет, все это очень глупо...",
        a4, "Заткнись! Никто не понимает истинных гениев.", m)

    $ days_without_an_event = 0
    
    $this.event_02.Finalize() # Сюда попадаем из ивента event_02
    jump day_start




###############################################################################################################################################################

label event_01: #First event in the game. Gennie finds himself at the desk.
    $screens.ShowD3("bld1")
    $hero(  m,  "..................?// Ваше высочество?// .......................................................",
            g4, "Я сделал это снова?// Телепортировал себя непонятно куда...",
            m,  "Что с этими ингредиентами?// Похоже, они мощнее, чем я думал.// Ну, не важно что это за место, дел у меня тут нет...// Лучше обернуть заклинание вспять, иначе принцесса будет снова злиться на меня...//"
                ".....................// Хотя...// Есть в этом месте что-то странное... это...// Оно наполненно.... // МАГИЕЙ?!//"
                " Да... магия, я чувствую. Такая мощная и в то же время...// ...чужая.// Интересно...// Думаю, нужно здесь осмотреться...")

    $screens.HideD3("bld1")
    $this.event_01.Finalize()
    return
###############################################################################################################################################################
label event_02:
    $ letters += 1 #Adds one letter in waiting list to be read. Displays owl with envelope.
    #$ mail_from_her = True #Comented out because replaced with $ letters += 1 
    play sound "sounds/owl.mp3"  #Quiet...
    $screens.ShowD3("owl", "bld1")
    $hero("Что? Сова?")
    $screens.HideD3("bld1")
    return
    
###############################################################################################################################################################
label event_03: 
    play music "music/Dark Fog.mp3" fadein 1 fadeout 1 
    
    $ renpy.play('sounds/door.mp3') #Sound of a door opening.
    $ snapes_speed = 02.0 #The speed of moving the walking animation across the screen.
    $ walk_xpos=470 #Animation of walking chibi. (From)
    $ walk_xpos2=360 #Coordinates of it's movement. (To)
    show screen snape_walk_01 
    with d3
    pause 1.5
    show screen snape_02 #Snape stands still.
    pause.1
    show screen bld1
    with Dissolve(.3)
    m "{size=-3}(Снова этот задумчивый парень...){/size}"
    $ tt_xpos=300 #Defines position of the Snape's full length sprite.
    $ tt_ypos=0
    $ s_sprite = "03_hp/10_snape_main/snape_01.png"
    show screen snape_main
    with Dissolve(.3)
    who2 "Альбус!"
    m "Эй.......... ты..."
    who2 "Вам что-то нужно сделать с этой девченкой Грейнджер..."
    hide screen snape_main                                                                                                                                  #SNAPE
    with d3                                                                                                                                                                  #SNAPE
    $ s_sprite = "03_hp/10_snape_main/snape_06.png"                                                                               #SNAPE
    show screen snape_main                                                                                                                                #SNAPE
    with d3                                                                                                                                                                  #SNAPE
    who2 "Честно... Я намекаю на наказания... как..."
    hide screen snape_main                                                                                                                                  #SNAPE
    with d3                                                                                                                                                                  #SNAPE
    $ s_sprite = "03_hp/10_snape_main/snape_04.png"                                                                               #SNAPE
    show screen snape_main                                                                                                                                #SNAPE
    with d3                                                                                                                                                                  #SNAPE
    who2 "Эта маленькая ведьма!"
    menu:
        m "..."
        "\"Грейнджер? Гермиона Грейнджер, так?\"":
            who2 "Да, она..."
            who2 "Она одна из \"группировки Поттера\"."
        "\"Я на вашей стороне, Джэк, ведьмы просто сумашедшие!\"":
            who2 "Что...? Альбус, вы ведете себя странно в последнее время."
            who2 "Все в порядке?"
            menu:
                m "..."
                "\"Да, все отлично. Продолжай.\"":
                    who2 "Как скажете..."
                "\"Ты меня знаешь. Обожаю подкалывать.\"":
                    who2 "Хм....."

        "\".....................................................\"":
            pass        
    who2 "Помните, как раньше пороли студентов?"
    who2 "Я клянусь, наши проблемы решились бы в миг, если бы мы вернули все обратно..."
    who2 "Да... Я бы с удовольствием выпорол эту девку перед всей школой..."
    hide screen snape_main                                                                                                                                  #SNAPE
    with d3                                                                                                                                                                  #SNAPE
    $ s_sprite = "03_hp/10_snape_main/snape_20.png"                                                                               #SNAPE
    show screen snape_main                                                                                                                                #SNAPE
    with d3                                                                                                                                                                  #SNAPE
    who2 "Затем поднял юбку и..."
    hide screen snape_main                                                                                                                                  #SNAPE
    with d3                                                                                                                                                                  #SNAPE
    $ s_sprite = "03_hp/10_snape_main/snape_12.png"                                                                               #SNAPE
    show screen snape_main                                                                                                                                #SNAPE
    with d3                                                                                                                                                                  #SNAPE
    who2 "*Кхм!* К сожалению, на данный момент учителя очень ограничены в возможностях наказания учеников..."
    who2 "Я знаю, что вы так же бессильны, как и я, но я говорю вам, что этой девке лучше прекратить испытывать мое терпение."
    menu:
        m "..."

        "\"Я позабочусь об этой шлюхе!\"":
            hide screen snape_main                                                                                                                                  #SNAPE
            with d3                                                                                                                                                                  #SNAPE
            $ s_sprite = "03_hp/10_snape_main/snape_05.png"                                                                               #SNAPE
            show screen snape_main                                                                                                                                #SNAPE
            with d3                                                                                                                                                                  #SNAPE
            who2 "...?!"
            who2 "Альбус..."
            who2 "Вы ведете себя странно..."
        "\"Никто не говорил, что будет легко.\"":
            hide screen snape_main                                                                                                                                  #SNAPE
            with d3                                                                                                                                                                  #SNAPE
            $ s_sprite = "03_hp/10_snape_main/snape_06.png"                                                                               #SNAPE
            show screen snape_main                                                                                                                                #SNAPE
            with d3                                                                                                                                                                  #SNAPE
            who2 "Иногда мне кажется, что уж лучше оказаться в комнате, полной дементоров..."
        "\"Вам лучше отдохнуть сегодня.\"":
            hide screen snape_main                                                                                                                                  #SNAPE
            with d3                                                                                                                                                                  #SNAPE
            $ s_sprite = "03_hp/10_snape_main/snape_06.png"                                                                               #SNAPE
            show screen snape_main                                                                                                                                #SNAPE
            with d3                                                                                                                                                                  #SNAPE
            who2 "Вы, как всегда, добры..."
    who2 "Хм..."
    hide screen snape_main                                                                                                                                  #SNAPE
    with d3                                                                                                                                                                  #SNAPE
    $ s_sprite = "03_hp/10_snape_main/snape_06.png"                                                                               #SNAPE
    show screen snape_main                                                                                                                                #SNAPE
    with d3                                                                                                                                                                  #SNAPE
    who2 "Может быть, мне лучше вздремнуть."
    who2 "Мне нужно быть в отличной форме завтра утром..."
    who2 "Если вы дадите слабину с этими детьми, то они сожрут вас целиком..."
    hide screen snape_main                                                                                                                                  #SNAPE
    with d3                                                                                                                                                                  #SNAPE
    $ s_sprite = "03_hp/10_snape_main/24.png"                                                                               #SNAPE
    show screen snape_main                                                                                                                                #SNAPE
    with d3                                                                                                                                                                  #SNAPE
    who2 "Доброй ночи, Альбус."
    
    
    hide screen snape_main
    hide screen bld1
    with d3
    $ walk_xpos=360 #Animation of walking chibi. (From desk)
    $ walk_xpos2=610 #Coordinates of it's movement. (To the door)
    $ snapes_speed = 03.0 #The speed of moving the walking animation across the screen.
    show screen snape_walk_01_f 
    pause 3
    hide screen snape_walk_01_f 
    show screen snape_01_f #Snape stands still. (Mirrored).
    pause.2
    who2 "................."
    who2 "Еще кое что..."
    show screen bld1
    show screen snape_main
    with Dissolve(.3)
    who2 "Игнорируйте любую ложь обо мне и тех девченках из Слизерина..."
    m "Само собой."
    hide screen bld1
    hide screen snape_main
    hide screen snape_01_f #Snape stands still. (Mirrored).
    with Dissolve(.3)
    $ renpy.play('sounds/door.mp3') #Sound of a door opening.
    $this.event_03.Finalize()
    jump day_start
###############################################################################################################################################################
label event_04:
    m "Ну, уже три дня прошло..."
    m "Интересно, что стало с этим двуличным чуваком?"
    return
###############################################################################################################################################################    
label event_05: #Snape comes in, has a talk with Genie, then the duel starts.
    
    play music "music/Dark Fog.mp3" fadein 1 fadeout 1 
    
    $ renpy.play('sounds/door.mp3') #Sound of a door opening.
    $ snapes_speed = 02.0 #The speed of moving the walking animation across the screen.
    $ walk_xpos=470 #Animation of walking chibi. (From)
    $ walk_xpos2=360 #Coordinates of it's movement. (To)
    show screen snape_walk_01 
    with d3
    pause 1.5
    show screen snape_02 #Snape stands still.
    show screen bld1
    with Dissolve(.3)
    $ tt_xpos=300 #Defines position of the Snape's full length sprite.
    $ tt_ypos=0
    $ s_sprite = "03_hp/10_snape_main/snape_01.png"
    show screen snape_main
    show screen ctc
    with Dissolve(.3)
    who2 "Добрый вечер, Альбус."
    who2 "Я хочу поговорить с вами о тех проклятых детях..."
    who2 "Но сначала хочу у вас кое-что спросить..."
    hide screen snape_main                                                                                                                                  #SNAPE
    with d3                                                                                                                                                                  #SNAPE
    $ s_sprite = "03_hp/10_snape_main/snape_05.png"                                                                               #SNAPE
    show screen snape_main                                                                                                                                #SNAPE
    with d3                                                                                                                                                                  #SNAPE
    who2 "Заметили ли вы, что-нибудь странное здесь в последнее время?"
    menu:
        m "..."
        "{size=-2}\"Как то, что вы постоянно ноете?\"{/size}":
            who2 "Что? Н-но... Эти дети..."
            hide screen snape_main                                                                                                                                  #SNAPE
            with d3                                                                                                                                                                  #SNAPE
            $ s_sprite = "03_hp/10_snape_main/snape_06.png"                                                                               #SNAPE
            show screen snape_main                                                                                                                                #SNAPE
            with d3                                                                                                                                                                  #SNAPE
            who2 "Ну, все же ты прав..."
        "{size=-2}\"Эта сова приносит мне письма, чувак!\"{/size}":
            who2 "Сова? Что-то не так?"
            hide screen snape_main                                                                                                                                  #SNAPE
            with d3                                                                                                                                                                  #SNAPE
            $ s_sprite = "03_hp/10_snape_main/snape_25.png"                                                                               #SNAPE
            show screen snape_main                                                                                                                                #SNAPE
            with d3                                                                                                                                                                  #SNAPE
            who2 "Это не то, что я имею в виду..."
            hide screen snape_main                                                                                                                                  #SNAPE
            with d3                                                                                                                                                                  #SNAPE
            $ s_sprite = "03_hp/10_snape_main/snape_29.png"                                                                               #SNAPE
            show screen snape_main                                                                                                                                #SNAPE
            with d3                                                                                                                                                                  #SNAPE
            who2 "Ладно, забудь..."
#        "\"I Saw a dude with two faces the other day.\"":
#            who2 "?!"
#            who2 "What's that supposed to mean...?"
        "{size=-2}\"Нет, не совсем. Все как обычно.\"{/size}":
            who2 "Хм... Может я начал параноить..."
    hide screen snape_main                                                                                                                                  #SNAPE
    with d3                                                                                                                                                                  #SNAPE
    $ s_sprite = "03_hp/10_snape_main/24.png"                                                                               #SNAPE
    show screen snape_main                                                                                                                                #SNAPE
    with d3                                                                                                                                                                  #SNAPE
    who2 "Я здесь из-за этой \"группировки Поттера\""
    hide screen snape_main                                                                                                                                  #SNAPE
    with d3                                                                                                                                                                  #SNAPE
    $ s_sprite = "03_hp/10_snape_main/snape_01.png"                                                                               #SNAPE
    show screen snape_main                                                                                                                                #SNAPE
    with d3                                                                                                                                                                  #SNAPE
    who2 "Есть несколько моментов, из-за которых стоит вычесть очки у Гриффиндора"
    who2 "И Грейнджер стала худшим примером из всех них за последнее время..."
    hide screen snape_main                                                                                                                                  #SNAPE
    with d3                                                                                                                                                                  #SNAPE
    $ s_sprite = "03_hp/10_snape_main/snape_06.png"                                                                               #SNAPE
    show screen snape_main                                                                                                                                #SNAPE
    with d3                                                                                                                                                                  #SNAPE
    who2 "Она, фактически, давит на меня."
    hide screen snape_main                                                                                                                                  #SNAPE
    with d3                                                                                                                                                                  #SNAPE
    $ s_sprite = "03_hp/10_snape_main/snape_05.png"                                                                               #SNAPE
    show screen snape_main                                                                                                                                #SNAPE
    with d3                                                                                                                                                                  #SNAPE
    who2 "Кстати, она не присылала вам какие-либо письма недавно?"
    menu:
        m "..."
        "\"Гермиона Грейнджер? Нет, ничего не было.\"":
            who2 "Понятно... Видимо, она блефует."
            hide screen snape_main                                                                                                                                  #SNAPE
            with d3                                                                                                                                                                  #SNAPE
            $ s_sprite = "03_hp/10_snape_main/snape_16.png"                                                                               #SNAPE
            show screen snape_main                                                                                                                                #SNAPE
            with d3                                                                                                                                                                  #SNAPE
            who2 "Что за тупая ведьма."
        "\"Да... Каждый чертов день...\"":
            who2 "Действительно?"
            who2 "Есть что-то обо мне в частности?"
            who2 "Я надеюсь вы хорошо меня знаете и не будете слушать ее..."
    
    hide screen snape_main                                                                                                                                  #SNAPE
    with d3                                                                                                                                                                  #SNAPE
    $ s_sprite = "03_hp/10_snape_main/snape_03.png"                                                                               #SNAPE
    show screen snape_main                                                                                                                                #SNAPE
    with d3                                                                                                                                                                  #SNAPE
    who2 "Она никогда не признается, но именно она распространяет эти скверные слухи обо мне..."
    hide screen snape_main                                                                                                                                  #SNAPE
    with d3                                                                                                                                                                  #SNAPE
    $ s_sprite = "03_hp/10_snape_main/snape_29.png"                                                                               #SNAPE
    show screen snape_main                                                                                                                                #SNAPE
    with d3                                                                                                                                                                  #SNAPE
    who2 "Ох... Эта шумная маленькая ведьма..."
    hide screen snape_main                                                                                                                                  #SNAPE
    with d3                                                                                                                                                                  #SNAPE
    $ s_sprite = "03_hp/10_snape_main/snape_09.png"                                                                               #SNAPE
    show screen snape_main                                                                                                                                #SNAPE
    with d3                                                                                                                                                                  #SNAPE
    who2 "Я бы никогда не опустился до того, чтобы обменивать сексуальные утехи за очки для дома."
    who2 "Я имею в виду, мы используем очки, чтобы мотивировать студентов, чтобы..."
    who2 "Я не могу говорить за других..."
    hide screen snape_main                                                                                                                                  #SNAPE
    with d3                                                                                                                                                                  #SNAPE
    $ s_sprite = "03_hp/10_snape_main/snape_13.png"                                                                               #SNAPE
    show screen snape_main                                                                                                                                #SNAPE
    with d3                                                                                                                                                                  #SNAPE
    who2 "Истории, которые я слышу о Минерве МакГонагалл и этих бедных первокурсников Гриффиндора могут быть правдой..."
    hide screen snape_main                                                                                                                                  #SNAPE
    with d3                                                                                                                                                                  #SNAPE
    $ s_sprite = "03_hp/10_snape_main/snape_01.png"                                                                               #SNAPE
    show screen snape_main                                                                                                                                #SNAPE
    with d3                                                                                                                                                                  #SNAPE
    who2 "Ну, я хотел бы убедиться, что вы не принимаете слухи всерьез..."
    who2 "Эту скверную ложь распространяют дети."
    

    who2 "О.... Перед тем, как я уйду..."
    who2 "Есть один вопрос, который я обязан вам задать..."
    hide screen snape_main                                                                                                                                  #SNAPE
    with d3                                                                                                                                                                  #SNAPE
    $ s_sprite = "03_hp/10_snape_main/snape_09.png"                                                                               #SNAPE
    show screen snape_main                                                                                                                                #SNAPE
    with d3                                                                                                                                                                  #SNAPE
    who2 "........................."
    hide screen snape_main                                                                                                                                  #SNAPE
    with d3                                                                                                                                                                  #SNAPE
    $ s_sprite = "03_hp/10_snape_main/snape_05.png"                                                                               #SNAPE
    show screen snape_main                                                                                                                                #SNAPE
    with d3                                                                                                                                                                  #SNAPE
    who2 "Как меня зовут?"
    menu:
        m "..."
        "\"Что? Что это вообще за вопрос?\"":
            hide screen snape_main                                                                                                                                  #SNAPE
            with d3                                                                                                                                                                  #SNAPE
            $ s_sprite = "03_hp/10_snape_main/snape_06.png"                                                                               #SNAPE
            show screen snape_main                                                                                                                                #SNAPE
            with d3                                                                                                                                                                  #SNAPE
            who2 "Вы правы..."
            who2 "Простите меня... Я последнее время слишком параною..."
            hide screen snape_main                                                                                                                                  #SNAPE
            with d3                                                                                                                                                                  #SNAPE
            $ s_sprite = "03_hp/10_snape_main/snape_05.png"                                                                               #SNAPE
            show screen snape_main                                                                                                                                #SNAPE
            with d3                                                                                                                                                                  #SNAPE
            who2 "Но вам стоит быть осторожнее со слухами о том, что \"сами знаете кто\" жив и все такое..."
        "\"Высокий задумчивый парень\"":
            hide screen snape_main                                                                                                                                  #SNAPE
            with d3                                                                                                                                                                  #SNAPE
            $ s_sprite = "03_hp/10_snape_main/snape_06.png"                                                                               #SNAPE
            show screen snape_main                                                                                                                                #SNAPE
            with d3                                                                                                                                                                  #SNAPE
            who2 "Альбус, в последнее время у вас весьма своеобразное чувство юмора..."
            who2 "Вероятно, вам стоит тратить меньше времени в компании с этим здоровяком Хагридом."
        "- \{Использовать магию для получения правильного ответа\} -":
            $ d_flag_01 = True
            hide screen snape_main
            with d3
            show screen blktone
            with d3
            ">Вы можете использовать ваши феноменальные космические силы, чтобы заглянуть в саму материю Вселенной и получить правильный ответ."
            hide screen blktone
            with d3
            $ s_sprite = "03_hp/10_snape_main/snape_03.png"                                                                               #SNAPE
            show screen snape_main                                                                                                                                #SNAPE
            with d3                                                                                                                                                                  #SNAPE
            who2 "!!?"
            m "Что за вопрос, Северус?"
            who2 "Простите меня... Последнее время я параною, вероятно."


    hide screen snape_main                                                                                                                                  #SNAPE
    with d3                                                                                                                                                                  #SNAPE
    $ s_sprite = "03_hp/10_snape_main/snape_06.png"                                                                               #SNAPE
    show screen snape_main                                                                                                                                #SNAPE
    with d3                                                                                                                                                                  #SNAPE
    who2 "В таком случае, доброй ночи, Альбус."
    hide screen snape_main
    hide screen bld1
    with d3
    $ walk_xpos=360 #Animation of walking chibi. (From desk)
    $ walk_xpos2=610 #Coordinates of it's movement. (To the door)
    $ snapes_speed = 03.0 #The speed of moving the walking animation across the screen.
    show screen snape_walk_01_f 
    pause 3
    hide screen snape_walk_01_f 
    show screen snape_01_f #Snape stands still. (Mirrored).
    pause.2
    
    
    
    
    stop music fadeout 1.0
    who2 "........................"
    hide screen snape_01_f
    hide screen bld1
    hide screen snape_main
    hide screen snape_02 #Snape stands still. 
    #hide screen genie
    show screen blkfade
    with d3
    $ renpy.play('sounds/07_run.mp3') 
    pause 2
    g4 "???"
    
    show screen snape_defends
    hide screen blkfade
    with d3
    show screen ctc
    
    
    
    play music "music/hitman.mp3" fadein 1 fadeout 1 # TENSE THEME 
    
    
    pause
    hide screen ctc
    show screen bld1
    with d3
    if d_flag_01:
        $sna_head_state = 6
        sna_head_main "Кто ты такой, сволочь!"
        g4 "Что? Это я... эм... Абиус! То есть, Альбус!"
        $sna_head_state = 4
        sna_head_main "Ты не надуришь меня."
        sna_head_main "Только что ты использовал какую-то чужеродную магию!"
        $sna_head_state = 6
        sna_head_main "Яви для меня свою истинную сущность, дьявол! Кто ты такой?!"
    else:
        $sna_head_state = 1
        sna_head_main "Мое имя Северус Снейп!"
        sna_head_main "Теперь твоя очередь...?"
        
    g4 "!!!"
    sna_head_main "Полегче... Просто ответь на мой вопрос."
    
    m "Ладно, ладно. Можешь просто успокоиться?..."
    sna_head_main "........"
    $ d_points = 0
    $ d_flag_01 = False
    $ d_flag_02 = False
    $ d_flag_03 = False
    label no_wait:
    menu:
        m "..."
        "\"Я тебе не враг.\"" if not d_flag_01:
            $ d_flag_01 = True
            $ d_points +=1
            sna_head_main "Это первое, что сказал бы враг."
        "\"Я просто турист. Я уже ухожу.\"" if not d_flag_02:
            $ d_flag_02 = True
            $ d_points +=1
            sna_head_main "У тебя ничего не выйдет."
        "\"Я работаю на Альбиса Думблдора!\"" if not d_flag_03:
            $ d_flag_03 = True
            $ d_points +=1
            sna_head_main "Его зовут Альбус Дамблдор, ты, придурок!"
    if d_points == 2:
        pass
    else:
        jump no_wait

    sna_head_main "Кто тебя послал сюда? Что ты сделал с настоящим Альбусом?"
    sna_head_main "Покажи свою истинную сущность, последнее предупреждение!"
    $ d_points = 0
    $ d_flag_01 = False
    $ d_flag_02 = False
    $ d_flag_03 = False
    label no_wait_2:
    menu:
        m "..."

        "\"Я не могу. Это сложно объяснить...\"" if not d_flag_01:
            $ d_flag_01 = True
            $ d_points +=1
            sna_head_main "Можешь ничего не объяснять. Я все равно не поверю ни единому слову!"
        "\"Хватит угрожать мне, человек!\"" if not d_flag_02:
            $ d_flag_02 = True
            $ d_points +=1
            sna_head_main "\"Человек\"?"
            sna_head_main "Ты намекаешь на то, что ты {size=+5}не{/size} один из нас?"
            sna_head_main "Что ты такое!? Немедленно отвечай, иначе я применю чары для снятия твоей маскировки!"
        "\"Я не причиню тебе вреда, клянусь!\"" if not d_flag_03:
            $ d_flag_03 = True
            $ d_points +=1
            sna_head_main "Точно?"
            sna_head_main "Докажи это. Сними свою маскировку немедленно!"

    if d_points == 2:
        pass
    else:
        jump no_wait_2

            
            
    sna_head_main "Я услышал достаточно!"
    g4 "Во имя великих песков пустыни! Человек, ты дашь мне объясниться?!"
    sna_head_main "Уже нечего объяснять!"
    sna_head_main "Пока вы отказываетесь сотрудничать, вы будете под стражей!"
    g4 "Что?! Подожди!"
    
    
    # Небольшое дополнение
    translators "Вы можете просто пропустить \"сражение\". Пропускаем?"
    menu:
        "- Пропустить дуэль -":
            $ skip_duel = True 
        "- Начать дуэль -":
            $ skip_duel = False
            stop music 
            $ renpy.play('sounds/glass_break.mp3') #Sound of a door opening.
            play music "music/Final Fantasy VII Boss Theme.mp3" fadein 1 fadeout 1
            # $ end_u_1_pic =  "glass"
            # pause.1
            # show screen end_u_1
            hide screen snape_defends
            # pause 3
    jump duel

###############################################################################################################################################################
label event_06: #THE TALK AFTER THE DUEL ENDS.
    $ potions = 0 #Makes sure there are no potions left in the possessions. 
    
    #play music "music/Final Fantasy VII - Victory Fanfare.mp3" fadein 1 fadeout 1 
    stop music fadeout 2.0
    g4 "*Задыхаясь*"
    g4 "Теперь ты готов поговорить?!"
    $sna_head_state = 8
    sna_head_main "(...н-невероятно...)"
    
    play music "music/Dark Fog.mp3" fadein 1 fadeout 1 
    
    hide ch_gen
    show image "03_hp/04_duel/no_magic.png" at Position(xpos=550, ypos=250, xanchor="center", yanchor="center") 
    
    m "Я сказал, что ты мне не ровня..."
    show screen bld1
    with d3
    m "Хотя, ты оказался неплох..."
    $sna_head_state = 1
    sna_head_main "Ты колдовал заклинания голыми руками..."
    sna_head_main "Если ты не человек, то... кто-"
    $sna_head_state = 4
    sna_head_main "{size=+5}Что ты такое?{/size}"
    $sna_head_state = 1
    sna_head_main "Какой-то демон, призванный \"сам знаешь кем\"?"
    m "Призванный кем?"
    $sna_head_state = 2
    sna_head_main "\"Сам знаешь кем\"!"
    m "Что?"
    $sna_head_state = 7
    sna_head_main "......................"
    m "............................"
    m "Послушай, я не демон..."
    m "И, само собой, я не работаю на \"сам не знаю кого\"!"
    $sna_head_state = 1
    sna_head_main "............................."
    m "Я был хм..."
    m "...Я проводил эксперимент в своем мире и что-то пошло не так, вот я и здесь."
    m "Это все..."
    sna_head_main ".........................."
    sna_head_main "Тогда, что же стало с настоящим Альбусом Дамблдором?"
    m "Я уверен, он в порядке."
    m "Он, вероятно, очень удивлен, оказавшись в чужом мире. Собственно, как и я..."
    sna_head_main "...................................."
    sna_head_main "Когда это произошло?"
    m "Дня четыре назад..."
    sna_head_main "Ты можешь вернуться назад?"
    m "Я думаю, что да..."
    $sna_head_state = 2
    sna_head_main "Почему ты еще не сделал этого?"
    m "Не знаю..."
    m "В этом мире очень странная магия... Мне просто стало любопытно."
    $sna_head_state = 1
    sna_head_main "..................."
    sna_head_main "Тебе нужно все исправить..."
    m "Исправить что?"
    $sna_head_state = 4
    sna_head_main "Все. Тебе нужно вернуть Альбуса и самому вернуться обратно."
    menu:
        m "..."

        "\"Да, да, знаю. Тогда я пойду.\"":
            m "Да, да, я знаю..."
            m "Ну, тогда я пойду. Извини за все это."
            $sna_head_state = 1
            sna_head_main "Хорошо, что никто не пострадал..."
        "\"Но мне нравится здесь! Могу я остаться?\"":
            sna_head_main "Категорически нет."
            sna_head_main "Кем бы ты не был, ты не из этого мира."
            sna_head_main "Твое присутствие здесь сильно нарушает порядок вещей в мире."
            sna_head_main "И в эти дни школа нуждается в хорошем директоре, как никогда ранее."
    sna_head_main "Безопаснее всего вернуться обратно именно сейчас."
    m "Хм ... Спасибо, господин Северус. Удачи с вашими студентами и \"шайкой Поттера\"."
    sna_head_main "\"Шайка Поттера\"?"
    $sna_head_state = 7
    sna_head_main "Ах, точно, эти пидерасты..."
    menu:
        "- Отменить заклинание -":
            pass
    menu:
        "- Отменить заклинание -":
            pass
    menu:
        "- Отменить заклинание -":
            pass

    $sna_head_state = 1
    sna_head_main "Сработало? Это вы, Альбус?"
    menu:
        m "..."
        "\"Да, это Я. Как хорошо вернуться обратно!\"":
            sna_head_main "Рад, что вы здесь. Вы в порядке?"
            m "Я в порядке, Северус, спасибо."
            sna_head_main "Как там, в другом мире?"
            m "Очень много песка и довольно жарко, но все-таки относительно неплохо."
            sna_head_main "Понимаю... Вы соскучились по своему брату?"
            menu:
                m "..."
                "\"Да, я соскучился по тебе очень сильно!\"":
                    sna_head_main "......................."
                    sna_head_main "Да, точно...."
                "\"У меня нет брата, Северус.\"":
                     sna_head_main "........................"
                     sna_head_main "У вас может и нет, но у настоящего Альбуса Дамблдора он есть."
                "- Использовать магию, для получения правильного ответа -":
                    show screen bld1
                    with d3
                    ">Вы используете свою космическу силу, чтобы заглянуть в саму материю Вселенной и узнать правильный ответ."
                    hide screen bld1
                    with d3
                    m "Мой младший брат Аберфорт? Почему я должен соскучиться по нему?"
                    sna_head_main "Я каждый раз чувствую, когда ты используешь свою странную магию..."
        "\"Не-а. Это все еще я. Не человеческий-чувак.\"":
            pass


    sna_head_main "Почему ты все еще здесь, существо?"
    m "Я не уверен... Я пытался обратить заклинание, но ничего не вышло..."


    $sna_head_state = 7
    sna_head_main "Чудеса..."
    $sna_head_state = 1
    sna_head_main "Что это значит? Ты собрался остаться здесь навсегда?"
    m "Конечно нет..."
    m "Я здесь, возможно, только потому, что заклинание компенсации дисбаланса вызвало само себя..."
    m "Если отменить заклинание, то я должен вернуться обратно в свой мир."
    m "Кроме того, твой друг Дамблдор тоже должен будет вернуться обратно сюда."
    sna_head_main "Понимаю..."
    sna_head_main "Как долго заклинание будет действовать?"
    menu:
        m "..."
        "\"Пару дней.\"":
            sna_head_main "Понятно..."
        "\"Неделя или...\"":
            sna_head_main "Хм.... Неделя, хух..."
        "\"Может быть месяцы...\"":
             sna_head_main "Так долго?"
             sna_head_main "Почему все настолько \"плохо\"?"
        "\"Я понятия не имею...\"":
            sna_head_main "....................."
            $sna_head_state = 2
            sna_head_main "Великолепно..."

    m "Хорошо, если честно, я не уверен, куда идти теперь..."
    m "Все это время, я думал, что смогу отметить заклинание когда захочу..."
    $sna_head_state = 1
    sna_head_main "..................................................."
    sna_head_main ".................................."
    sna_head_main "..................."
    m "Снейп?"
    sna_head_main "..................................................."
    m "Северус?"
    $sna_head_state = 6
    sna_head_main "Да, да ..."
    $sna_head_state = 1
    sna_head_main "Слушай, уже поздно и очень многое успело произойти..."
    $sna_head_state = 7
    sna_head_main "Мне следует обдумать все это."
    $sna_head_state = 1
    sna_head_main "Увидимся завтра, я зайду после занятий."
    $sna_head_state = 6
    sna_head_main "До тех пор, держи свою истинную личность и наш разговор в тайне, идет?"
    m "Без проблем."
    $sna_head_state = 1
    sna_head_main "Отлично, тогда..."
    sna_head_main "Но перед тем, как я уйду, один вопрос..."
    m "Я слушаю..."
    $sna_head_state = 2
    sna_head_main "........"
    $sna_head_state = 1
    sna_head_main "Если ты не человек, тогда..."
    $sna_head_state = 7
    sna_head_main "Что ты?"
    m "...Я - джинн."
    $sna_head_state = 1
    sna_head_main "Джинн?"
    m "Да, я обладаю крутой космической силой и все такое..."
    sna_head_main "Серьезно?"
    m "О, да."
    sna_head_main "Невероятно..."
    sna_head_main "Ну, увидимся завтра.... джинн."
    m "Я буду здесь..."

    $sna_head_state = 7
    sna_head_main "(Джинн? Что-то новое...)"
    $this.event_05.Finalize()
    jump day_start
###############################################################################################################################################################        
label event_07: #THE TALK WITH SNAPE THE DAY AFTER THE DUEL.
    play music "music/Dark Fog.mp3" fadein 1 fadeout 1 
    $ renpy.play('sounds/door.mp3') #Sound of a door opening.
    $ snapes_speed = 02.0 #The speed of moving the walking animation across the screen.
    $ walk_xpos=470 #Animation of walking chibi. (From)
    $ walk_xpos2=360 #Coordinates of it's movement. (To)
    show screen snape_walk_01 
    with d3
    pause 1.5
    show screen snape_02 #Snape stands still.
    show screen bld1
    with Dissolve(.3)
    $ tt_xpos=300 #Defines position of the Snape's full length sprite.
    $ tt_ypos=0
    $ s_sprite = "03_hp/10_snape_main/snape_01.png"
    show screen snape_main
    show screen ctc
    with Dissolve(.3)
    sna "..................."
    hide screen snape_main
    with d3
    m "Добрый вечер..."
    show screen snape_main
    with d3
    sna "Заклинание все еще работает?"
    hide screen snape_main
    with d3
    m "Да, до сих пор."
    show screen snape_main
    with d3

    sna "Понятно..."
    sna "Прошлой ночью я...ломал голову над нашей головоломкой."
    sna "И мне кажется, у меня есть решение..."
    m "Действительно? Отлично! Я слушаю."
    hide screen snape_main                                                                                                                                  #SNAPE
    with d3                                                                                                                                                                  #SNAPE
    $ tt_xpos=300 #Defines position of the Snape's full length sprite. Right - 300  # 120 - center.          #SNAPE
    $ s_sprite = "03_hp/10_snape_main/snape_29.png"                                                                               #SNAPE
    show screen snape_main                                                                                                                                #SNAPE
    with d3                                                                                                                                                                  #SNAPE
    sna "Давай просто продолжим эту игру..."
    m "Что?"
    hide screen snape_main                                                                                                                                  #SNAPE
    with d3                                                                                                                                                                  #SNAPE
    $ s_sprite = "03_hp/10_snape_main/snape_06.png"                                                                               #SNAPE
    show screen snape_main                                                                                                                                #SNAPE
    with d3                                                                                                                                                                  #SNAPE
    sna "Ну, а что еще мы можешь сделать"
    sna "Обычно я предупредил бы министерство магии и уже они позаботились бы об этом..."
    sna "Но лучше я избегу каких-либо отношений с этими бюрократами..."
    hide screen snape_main                                                                                                                                  #SNAPE
    with d3                                                                                                                                                                  #SNAPE
    $ s_sprite = "03_hp/10_snape_main/snape_10.png"                                                                               #SNAPE
    show screen snape_main                                                                                                                                #SNAPE
    with d3                                                                                                                                                                  #SNAPE
    sna "Кроме того, потеря директора, хоть и временная, может сильно ранить репутацию школы..."
    sna "А что если твое заклинание спадет завтра или даже сегодня ночью?"
    hide screen snape_main                                                                                                                                  #SNAPE
    with d3                                                                                                                                                                  #SNAPE
    $ s_sprite = "03_hp/10_snape_main/snape_09.png"                                                                               #SNAPE
    show screen snape_main                                                                                                                                #SNAPE
    with d3                                                                                                                                                                  #SNAPE
    sna "Я не вижу причин для паники..."
    m "Хм..."
    hide screen snape_main                                                                                                                                  #SNAPE
    with d3                                                                                                                                                                  #SNAPE
    $ s_sprite = "03_hp/10_snape_main/snape_03.png"                                                                               #SNAPE
    show screen snape_main                                                                                                                                #SNAPE
    with d3                                                                                                                                                                  #SNAPE
    sna "Исходя из всего этого, нам стоит просто играть свои роли..."

    m "Что именно делать?"
    hide screen snape_main                                                                                                                                  #SNAPE
    with d3                                                                                                                                                                  #SNAPE
    $ s_sprite = "03_hp/10_snape_main/snape_05.png"                                                                               #SNAPE
    show screen snape_main                                                                                                                                #SNAPE
    with d3                                                                                                                                                                  #SNAPE
    sna "Просто делай все как Альбус: не выходи из башни и не контактируй с людьми..." 
    m "Это...."
    m "Звучит..."
    g4 "Невероятно скучно!"
    g4 "Чем мне здесь заниматься?"
    hide screen snape_main                                                                                                                                  #SNAPE
    with d3                                                                                                                                                                  #SNAPE
    $ s_sprite = "03_hp/10_snape_main/snape_01.png"                                                                               #SNAPE
    show screen snape_main                                                                                                                                #SNAPE
    with d3                                                                                                                                                                  #SNAPE
    sna "Ты джинн. Сотвори что-нибудь для себя."
    m "Моя магия толком не работает здесь..."
    m "И моя лампа вообще в другом мире..."
    hide screen snape_main                                                                                                                                  #SNAPE
    with d3                                                                                                                                                                  #SNAPE
    $ s_sprite = "03_hp/10_snape_main/snape_03.png"                                                                               #SNAPE
    show screen snape_main                                                                                                                                #SNAPE
    with d3                                                                                                                                                                  #SNAPE
    sna "Ну, а что ты скажешь насчет этого?"
    sna "Может быть прислать тебе парочку девок из Слизерина?"
    g9 "Понятия не имею, что такое \"Слизерин\", но думаю, это поможет..."
    hide screen snape_main                                                                                                                                  #SNAPE
    with d3                                                                                                                                                                  #SNAPE
    $ s_sprite = "03_hp/10_snape_main/snape_04.png"                                                                               #SNAPE
    show screen snape_main                                                                                                                                #SNAPE
    with d3                                                                                                                                                                  #SNAPE
    sna "Это шутка."
    hide screen snape_main                                                                                                                                  #SNAPE
    with d3                                                                                                                                                                  #SNAPE
    $ s_sprite = "03_hp/10_snape_main/snape_09.png"                                                                               #SNAPE
    show screen snape_main                                                                                                                                #SNAPE
    with d3                                                                                                                                                                  #SNAPE
    sna "Хотя..."
    sna "Хм..."
    hide screen snape_main                                                                                                                                  #SNAPE
    with d3                                                                                                                                                                  #SNAPE
    $ s_sprite = "03_hp/10_snape_main/snape_01.png"                                                                               #SNAPE
    show screen snape_main                                                                                                                                #SNAPE
    with d3                                                                                                                                                                  #SNAPE
    sna "Ну, в любом случае я не представляю как развлечь {size=+7}тебя{/size} в этой ситуации."
    m "Да, но это!"
    m "Я бессмертен и всемогущ..."
    m "Это самое скучное, что могло произойти со мной!"
    g4 "Я нахожусь в маленьком запертом помещении и мне абсолютно нечего делать!"
    g4 "Я могу потерять сознание..."
    g4 "Ох! Ах! Я думаю уже начал!"
    hide screen snape_main                                                                                                                                  #SNAPE
    with d3                                                                                                                                                                  #SNAPE
    $ s_sprite = "03_hp/10_snape_main/snape_03.png"                                                                               #SNAPE
    show screen snape_main                                                                                                                                #SNAPE
    with d3                                                                                                                                                                  #SNAPE
    sna "......."
    g4 "Я теряю сознание! Становится труднее дышать!"
    hide screen snape_main                                                                                                                                  #SNAPE
    with d3                                                                                                                                                                  #SNAPE
    $ s_sprite = "03_hp/10_snape_main/snape_04.png"                                                                               #SNAPE
    show screen snape_main                                                                                                                                #SNAPE
    with d3                                                                                                                                                                  #SNAPE
    sna "...."
    g4 "Очень темно..."
    g4 "Ты все еще здесь?"
    hide screen snape_main                                                                                                                                  #SNAPE
    with d3                                                                                                                                                                  #SNAPE
    $ s_sprite = "03_hp/10_snape_main/snape_03.png"                                                                               #SNAPE
    show screen snape_main                                                                                                                                #SNAPE
    with d3                                                                                                                                                                  #SNAPE
    sna "..."
    m "........."
    hide screen snape_main                                                                                                                                  #SNAPE
    with d3                                                                                                                                                                  #SNAPE
    $ s_sprite = "03_hp/10_snape_main/snape_10.png"                                                                               #SNAPE
    show screen snape_main                                                                                                                                #SNAPE
    with d3                                                                                                                                                                  #SNAPE
    sna "Ты закончил?"
    m "Да..."
    m "Серьезно, я сомневаюсь, что это пойдет мне на пользу."
    hide screen snape_main                                                                                                                                  #SNAPE
    with d3                                                                                                                                                                  #SNAPE
    $ s_sprite = "03_hp/10_snape_main/snape_01.png"                                                                               #SNAPE
    show screen snape_main                                                                                                                                #SNAPE
    with d3                                                                                                                                                                  #SNAPE
    sna "У тебя есть другое предложение?"
    m "Я могу..."
    m "Вместо того, чтобы просто сидеть на заднице в этом кабинете, я бы мог исследовать ваш мир..."
    hide screen snape_main                                                                                                                                  #SNAPE
    with d3                                                                                                                                                                  #SNAPE
    $ s_sprite = "03_hp/10_snape_main/snape_03.png"                                                                               #SNAPE
    show screen snape_main                                                                                                                                #SNAPE
    with d3                                                                                                                                                                  #SNAPE
    sna "Хм..."
    hide screen snape_main                                                                                                                                  #SNAPE
    with d3                                                                                                                                                                  #SNAPE
    $ s_sprite = "03_hp/10_snape_main/snape_01.png"                                                                               #SNAPE
    show screen snape_main                                                                                                                                #SNAPE
    with d3                                                                                                                                                                  #SNAPE
    sna "Хорошо, что ты хочешь?" 
    m "Научи меня твоей магии..."
    hide screen snape_main                                                                                                                                  #SNAPE
    with d3                                                                                                                                                                  #SNAPE
    $ s_sprite = "03_hp/10_snape_main/snape_05.png"                                                                               #SNAPE
    show screen snape_main                                                                                                                                #SNAPE
    with d3                                                                                                                                                                  #SNAPE
    sna "Моей магии?"
    m "Да... Как вы колдуете заклинания..."
    m "Интригует..."
    hide screen snape_main                                                                                                                                  #SNAPE
    with d3                                                                                                                                                                  #SNAPE
    $ s_sprite = "03_hp/10_snape_main/snape_04.png"                                                                               #SNAPE
    show screen snape_main                                                                                                                                #SNAPE
    with d3                                                                                                                                                                  #SNAPE
    sna "Хм..."
    hide screen snape_main                                                                                                                                  #SNAPE
    with d3                                                                                                                                                                  #SNAPE
    $ s_sprite = "03_hp/10_snape_main/snape_06.png"                                                                               #SNAPE
    show screen snape_main                                                                                                                                #SNAPE
    with d3                                                                                                                                                                  #SNAPE
    sna "Ладно, да будет так..."
    m "О, и пришли мне пару этих \"Слизеринских\" девок конечно же.."
    hide screen snape_main                                                                                                                                  #SNAPE
    with d3                                                                                                                                                                  #SNAPE
    $ s_sprite = "03_hp/10_snape_main/snape_05.png"                                                                               #SNAPE
    show screen snape_main                                                                                                                                #SNAPE
    with d3                                                                                                                                                                  #SNAPE
    sna "..............."
    sna "........................."
    hide screen snape_main                                                                                                                                  #SNAPE
    with d3                                                                                                                                                                  #SNAPE
    $ s_sprite = "03_hp/10_snape_main/snape_28.png"                                                                               #SNAPE
    show screen snape_main                                                                                                                                #SNAPE
    with d3                                                                                                                                                                  #SNAPE
    sna "Ха-ха-ха!!!"
    m "Что? Что я такого сказал?"
    hide screen snape_main                                                                                                                                  #SNAPE
    with d3                                                                                                                                                                  #SNAPE
    $ s_sprite = "03_hp/10_snape_main/snape_28.png"                                                                               #SNAPE
    show screen snape_main                                                                                                                                #SNAPE
    with d3                                                                                                                                                                  #SNAPE
    sna "А-ха-ха-ха-ха.."
    hide screen snape_main                                                                                                                                  #SNAPE
    with d3                                                                                                                                                                  #SNAPE
    $ s_sprite = "03_hp/10_snape_main/snape_02.png"                                                                               #SNAPE
    show screen snape_main                                                                                                                                #SNAPE
    with d3                                                                                                                                                                  #SNAPE
    sna "Нет, нет, прости..."
    sna "Это просто...ты все еще выглядишь и говоришь для меня как Альбус..."
    sna "Услышать от профессора Дамблода что-то вроде \"Пришли мне этих девок\"..."
    hide screen snape_main                                                                                                                                  #SNAPE
    with d3                                                                                                                                                                  #SNAPE
    $ s_sprite = "03_hp/10_snape_main/snape_22.png"                                                                               #SNAPE
    show screen snape_main                                                                                                                                #SNAPE
    with d3                                                                                                                                                                  #SNAPE
    sna "У меня истерика... "
    hide screen snape_main                                                                                                                                  #SNAPE
    with d3                                                                                                                                                                  #SNAPE
    $ s_sprite = "03_hp/10_snape_main/snape_09.png"                                                                               #SNAPE
    show screen snape_main                                                                                                                                #SNAPE
    with d3                                                                                                                                                                  #SNAPE
    sna "Но ты не понял..."
    m "Хех..."
    g9 "Отправь мне этих шлюх, Северус. Я очень одинок вечерами."
    hide screen snape_main                                                                                                                                  #SNAPE
    with d3                                                                                                                                                                  #SNAPE
    $ s_sprite = "03_hp/10_snape_main/snape_28.png"                                                                               #SNAPE
    show screen snape_main                                                                                                                                #SNAPE
    with d3                                                                                                                                                                  #SNAPE
    sna "Ха-ха-ха! Прекрати, ты убьешь меня!"
    sna "А-ха-ха-ха!"
    m "Нет, я серьезно... Это возможно?"
    hide screen snape_main                                                                                                                                  #SNAPE
    with d3                                                                                                                                                                  #SNAPE
    $ s_sprite = "03_hp/10_snape_main/snape_02.png"                                                                               #SNAPE
    show screen snape_main                                                                                                                                #SNAPE
    with d3                                                                                                                                                                  #SNAPE
    sna "Хм..."
    sna "Увидим..."
    sna "Ты, в роли нашего директора, очень полезен для меня..."
    sna "Мне нужно некоторое время, чтобы выяснить, как я могу использовать нашу ситуацию в моих интересах."
    m "Ты имеешь в виду {size=+7}наших{/size} интересах, верно?"
    hide screen snape_main                                                                                                                                  #SNAPE
    with d3                                                                                                                                                                  #SNAPE
    $ s_sprite = "03_hp/10_snape_main/snape_06.png"                                                                               #SNAPE
    show screen snape_main                                                                                                                                #SNAPE
    with d3                                                                                                                                                                  #SNAPE
    sna "О, да,да конечно..."
    sna "Ну, думаю на сегодня мы закончили..."
    hide screen snape_main                                                                                                                                  #SNAPE
    with d3                                                                                                                                                                  #SNAPE
    $ s_sprite = "03_hp/10_snape_main/24.png"                                                                               #SNAPE
    show screen snape_main                                                                                                                                #SNAPE
    with d3                                                                                                                                                                  #SNAPE
    sna "Доброй ночи... Джинн."
    m "Да, доброй ночи, Северус."

    hide screen snape_main
    hide screen ctc
    hide screen bld1
    with d3
    $ walk_xpos=360 #Animation of walking chibi. (From desk)
    $ walk_xpos2=610 #Coordinates of it's movement. (To the door)
    $ snapes_speed = 03.0 #The speed of moving the walking animation across the screen.
    show screen snape_walk_01_f 
    pause 3
    hide screen snape_walk_01_f 
    show screen snape_01_f #Snape stands still. (Mirrored).
    pause.2
    
    $ s_head_xpos = 330 # x = 330,                                                                              # SNAPE
    $ s_head_ypos = 380 #Right bottom corner: y = 340. y = 380 - no hand.       # SNAPE
    $ s_sprite = "03_hp/10_snape_main/snape_06.png"                                         # SNAPE
    show screen s_head2                                                                                                 # SNAPE
    sna "................."
    $ s_sprite = "03_hp/10_snape_main/snape_28.png"                                         # SNAPE
    show screen s_head2                                                                                                 # SNAPE
    sna "\"Пришли мне этих шлюх, Северус!\" Ха-ха-ха..."
    hide screen s_head2  
    $ renpy.play('sounds/door.mp3') #Sound of a door opening.
    hide screen snape_01_f #Snape stands still. (Mirrored).
    with d3
    m "Хм... "
    m "Полагаю, я просто свернусь клубком на этом столе и посплю..."
    pause.2
    show screen notes
    $ renpy.play('sounds/win2.mp3') 
    show screen blktone
    with d3
    ">Теперь вы можете вызывать Снейпа в свой кабинет."
    hide screen blktone
    with d3
#    $ hanging_with_snape = True
    $this.event_07.Finalize()
    jump day_start

###############################################################################################################################################################
label event_08: # HERMONE SHOWS UP FOR THE FIRST TIME. IN USE.
    #"EVENT_08"
    stop music fadeout 1.0
    pause 1
    $ renpy.play('sounds/knocking.mp3') #Sound someone knocking on the door.
    "*Тук-тук-тук*"
    $hero("Хах?")
    $ renpy.play('sounds/knocking.mp3') #Sound someone knocking on the door.
    "*Тук-тук-тук*"
    pause.7

    $hero("Кто-то стучит в дверь...// Черт... Я должен избегать любых контактов с людьми!// Хм... Каковы шансы, что это стучится не человек?// Ага, достаточно малы...")

    $ renpy.play('sounds/knocking.mp3') #Sound someone knocking on the door.
    "*Тук-тук-тук*"

    $hero("Настойчивый ублюдок...")
    $ d_flag_01 = False #When False Genie doesn't know Hermione's name.
    $ d_flag_02 = False #When TRUE Genie knows it's a girl knocking on the door.
    $hermi.Visibility()
    menu:
        m "..."
        "\"Кто это?\"":
            $ d_flag_01 = True
            $hermi(who, "Это я, профессор...// Гермиона Грейнджер. Могу я войти?")
            $hero("#(Это та девка, которая засыпала меня своими письмами...)")
            $hermi(her)
            menu: 
                m "..."
                "\"Уходи, пожалуйста. Я занят.\"":
                    jump event_08_saygoout
                "\"Да, да. Конечно входи.\"":
                    pass          
        "\"Входите!\"":
            pass
        "\"Уходи!\"":
            label event_08_saygoout:
            $ d_flag_02 = True #When TRUE Genie knows it's a girl knocking on the door.
            $hermi(who, "Но, профессор, мне действительно нужно поговорить с вами...")
            $hero("...........................................")
            $hermi("Профессор? Я вхожу!")
            $hero("#(Дерьмо...)")
        "\"................\"":
            $hermi(who, "Профессор, вы здесь?")
            $hero("#(Уходи...)")
            jump event_08_saygoout


    $ renpy.play('sounds/door.mp3') #Sound of a door opening.

# Нельзя комментировать, переменные должны быть инициированы, используются в старом коде
    $ hermione_chibi_xpos = 610  
    $ hermione_chibi_ypos = 250
    $ walk_xpos=610 #Animation of walking chibi. (From)
    $ walk_xpos2=400 #Coordinates of it's movement. (To)
    $ pos = POS_370  # Присвоение не комментировать, будет использовать дальше в старом коде
                        #    $herView.showQ( "body_01.png", pos )
                        #    $herView.hideQ( )
    $ posHead = gMakePos( 390, 235 )

    $hermi.chibi.State("door", speed="go").Trans(Dissolve(.5), "blink")
    

    pause.3
    if not d_flag_01:
        m "?!!"
    if not d_flag_02: #When TRUE Genie knows it's a girl knocking on the door.
        m "{size=-3}(Девочка?){/size}"
        
    play music "music/Chipper Doodle v2.mp3" fadein 1 fadeout 1

    $hermi.chibi.Trans("go center", "blink")
    pause.5
    $screens.ShowD3("bld1" )

    $hermi.Visibility("body+", transition=d3)

    $screens.ShowD3("ctc").Pause()
    $hermi("Доброе утро, профессор.","~body_03.png")
    $screens.HideD3("ctc")
    menu:
        "\"Доброе утро... девочка.\"":
            $hermi("#(\"Девочка\"?)")
        "\"Доброе утро, Гермиона.\"" if d_flag_01:
            pass
        "\"Доброе утро, Дитя.\"":
            $hermi("#(\"Дитя\"?)")
        "\"................................\"":
            pass
    $hermi(                 "Я была очень занята, но сегодня утром у меня есть немного времени, чтобы встретится с вами, профессор.",
                            "Вы, наверное, знаете, почему я здесь.",
            "~body_04.png", "Тот вопрос, на который я безуспешно пыталась обратить Ваше внимание в последнее время...",
                            "Я не могу понять, почему вы ничего не предпринимаете, чтобы остановить этот абсурд!",
            "~body_02.png", "Это ситуация начинает сказываться на соревновании факультетов...",
                            "И все потому, что мы более честны, нежели остальные...",
                            "Как вы думаете, это справедливо, что те кто заслуживают быть лидерами, оказываются в отстающих?",
                            "Как вы думаете? Справедливо?", 
            "~body_03.png")

    $hero("#(Вы только посмотрите на эту очаровашку!)// #(Только посмотрите ... Она восхитительна!)// #(Великие пески, я не видел женщину целую неделю!)")

    menu:
        "\"(Подрочить под столом, пока она говорит.)\"":
            $ jerk_off_session = True #Affects next conversation with Snape.
            $ d_flag_01 = True #If TRUE genie jerks off under the desk.    
        "\"(Нет, это глупо! Мне нужно вести себя нормально!)\"":
            $ d_flag_01 = False #NOT JERKING OFF.
            pass
    if d_flag_01:
        $hermi.Visibility()
        $screens.HideD3("bld1").ShowD3( "blktone8" )
        ">Вы опустили руки под стол и обхватили свой член..."
        $screens.HideD3( "blktone8", None, "genie" ).ShowD3( "genie_jerking_off")

    $hero("Да, продолжай, дорогая.")
    $screens.ShowD3( "bld1" )

    $hermi.Visibility("body+")("~body_05.png",  "\"Да\"?! То есть это справедливо?")
    $hero(                  "О, конечно нет, я хотел сказать \"нет\". Но все равно продолжай...")
    $hermi("~body_03.png",  "Стало легче на душе. Я рада, что вы согласны со мной, профессор...",
           "~body_04.png",  "Как я уже говорила, это просто смешно, и я не могу поверить, что это происходит сейчас и с нами!")

    if d_flag_01:
        $hermi.Visibility()
        $screens.HideD3("bld1").ShowD3( "blktone8").Say(">*Фап!* *Фап!* *Фап!*// >Вы продолжаете дрочить свой член...").HideD3( "blktone8").ShowD3( "bld1")
        $hermi.Visibility("body+")
    else:
        m "Понятно..."

    $hermi("Я поняла бы, если бы это происходило несколько сотен лет назад...// Но мы живем не в темные века, не так ли?")

    if d_flag_01:
        $hero(g9, "#(Вы только посмотрите на эти розовые щечки? Хочу потыкать в них своим членом.)",m)
        $hermi.Visibility()
        $screens.ShowD3( "blktone8").Say(">Вы продолжаете дрочить...").HideD3( "blktone8")
        $hermi.Visibility("body+")
    else:
        $hero("Эм... Я полагаю, что вы сделаете, то есть, мы сделаем все, что нужно.")

    $hermi("Это вредит системе распределения очков для факультетов.// И мало того!// Это навредит всей системе образования...// Из-за этого падает мотивация студентов!")

    if d_flag_01:
        $hero(  "#(Что за огромные сиськи!)// #(Да... Я хочу зажать свой член между ними...)")

    $hermi("Как видите, ситуация весьма тяжелая...// ~body_02.png// Но мы все еще можем исправить...// У меня, как у представителя Школьного Студенческого Совета...// Есть пара предложений, как сделать это более эффективно.")


    if not d_flag_01:
        $hero ("..............")

    $hermi("Прежде всего, система очков для факультетов должна стать более сложной!// ~body_03.png// Вам нужно контролировать распределение очков чуть лучше, сэр.")        
    if d_flag_01:
        $hero (g4, "#(Да, шлюха... Грязная шлюха... Бьюсь об заклад, ты обожаешь сосать члены... Не так ли? Да, уверен в этом...)")
        $hermi.Visibility()
        $screens.Show(d4, "blktone8").Say(">Вы неистово надрачиваете свой твердейший член!").Hide(d4, "blktone8")
        $hermi.Visibility("body+")
    $hermi("Вы ведь согласны со мной, профессор, не так ли?")
    if d_flag_01:
        $hero(g4,               "{size=-4}*Тяжело дыша*{/size}")
        $hermi("~body_07.png// Профессор...?")
        $hero("#(Вот дерьмо. О чем она только что трещала?)// Да, это так. Продолжай...")
        $hermi(                 "Эм... Итак, как я сказала...")
        $hermi.Visibility()
        $hero(m,"#(Ох... Отлично вздрочнул, но я уже близок к \"великому финалу\".)// #(Может, прекратить пока не произошло чего?)")
        menu:
            "\"(Да, думаю стоит послушать ее.)\"":
                $screens.ShowD3("genie")
                $ d_flag_01 = False #NOT JERKING OFF ANY MORE.
            "\"(Нет! Я должен закончить!)\"":
                pass
        $hermi.Visibility("body+")
    else:
        $hero("#(Нужно ли мне контролировать? Да плевать...)// Хм... Наверное нужно...")
        $hermi("#(Наверное?)// #(Когда это профессор Дамблдор стал таким безразличным?...)")

    $hermi("~body_04.png// Еще одна мера, которую стоит принять - это более жесткий контроль за сотрудниками...// Особенно за преподавателями...",
           "~body_03.png// Я надеюсь, что не переступаю черту, но некоторые преподаватели действительно требуют надзора...")

    if d_flag_01:
        $hero(g4,            "{size=-4}(Да! Ты маленькая шлюха! Тупая маленькая шлюха!) *Задыхаясь*{/size}")
    else:
        $hero(m,            ".......................")
    $hermi("~body_04.png",  "Я понимаю, что у вас нет времени на все это. Вы директор академии, очень важный и занятой человек.",
                            "Временами, мне непросто быть лучшей студенткой, это словно на пьедестале стоять...")

    if d_flag_01:
#        translators "{size=-4}(Здесь была игра слов \"hard on(тяжело)\" и \"hard-on(стояк)\") которую мы не смогли перевести. \nПростите нас :({/size}"
        $hero(g4, "{size=-4}(Она сказала \"стояк\"!?) *задыхаясь*{/size}")
    $hermi("Но вы могли бы поручить эту задачу мне, и я справлюсь...// Просто... просто внедрите вашу уверенность и твердость в меня!" )

    if d_flag_01: 
        $hermi("~body_01.png", "Да, сэр! Просто внедрите это в меня!")

        stop music fadeout 1.0
        $screens.ShowHide("white", 0.1).Pause(0.2).Show("white").Pause(0.1).Hide(hpunch,"white")

        $hero(g4, "{size=-4}(О дерьмо, что она наделала!) *Аргх!*{/size}")
        $hermi.Visibility()

        $screens.HideD3("bld1").ShowD3("genie_jerking_sperm").Pause(3.0).ShowD3("bld1")

        $hermi.Visibility("body+")("~body_18.png", "Профессор!? Что происходит...?")
        $screens.ShowD3("genie_jerking_sperm_02")
        $hero(g4, "АА... ДААААА.....!")
        $hermi("???")
        $hero(g4, "*Тяжело дыша* Да! Да....")
        $screens.ShowD3("genie")
        $hero(g4, "Да, девочка, да. Все именно так, как ты говоришь. И я... позабочусь обо всем этом.", m)
    else:
        $hero(m,       "Хорошо, я подумаю о твоем предложении. Обещаю.")   

    $hermi("~body_07.png// Правда?// Хм...........")

    play music "music/Chipper Doodle v2.mp3" fadein 1 fadeout 1 
    $hermi("~body_04.png",  "Это обнадеживает. Спасибо, Профессор.")

    if d_flag_01:
        $hero("Нет, нет. Спасибо тебе...")
        $hermi("~body_07.png// Хм...")

    $hermi("~body_04.png// Мои занятия вот-вот начнутся. Мне надо идти.// Спасибо, что уделили мне время...")

    $screens.HideD3("bld1")
    $hermi.Visibility(transition=d3)
    $hermi.chibi.Trans("goout door").Hide(d3)    
    $ renpy.play('sounds/door.mp3') #Sound of a door opening.
    pause.5

    if d_flag_01:
        $hero("#(Это офигительно...) *Задыхаясь*// #(Мои трусы просто уничтожены...)")  
    else: 
        $hero(".................// #(Симпатичная, но чересчур увлечена работой...)")

    $screens.HideD3("bld1").HideD3("genie_jerking_sperm_02")

    play music "music/Brittle Rille.mp3" fadein 1 fadeout 1
    $this.event_08.Finalize()
    return

### FOLLOWING EVENT IS NOT IN USE ANYMORE ###
###############################################################################################################################################################    
label event_08_02:
#    "EVENT_08_02"
    $ renpy.play('sounds/knocking.mp3') #Sound someone knocking on the door.
    "*Тук-тук-тук!*"
    menu:
        "\"Кто это?\"":
            $hermi("Это я, Гермиона Грейнджер.")
            $hero("#(Снова эта молоденькая ведьма...)")
            jump event_08_02_inmenu
        "\"Да, входи...\"":
            pass
        "\"...................................\"":
            $ renpy.play('sounds/knocking.mp3') #Sound someone knocking on the door.
            "*Тук-тук-тук!*"
#            m "............................."
            label event_08_02_inmenu:
            $hermi("Профессор, я вхожу...")
            $hero("#(Дерьмо!)")
    
    $ renpy.play('sounds/door.mp3') #Sound of a door opening.
    $hermi.chibi.State("door", speed="go").Trans(d4, "blink").Trans("go center", "blink") # Если делать dissolve в движении, то сбивается счетчик времени. Лучше выполнить появление чибика стоя, затем уже двигать его 
    pause.5
    $screens.ShowD3("bld1")

    $hermi("~body_01.png").Visibility("body+", transition=d3)("Доброе утро, профессор Дамблдор.")
    menu:
        "\"Доброе утро, мисс Грейнджер.\"":
            pass
        "\"Доброе утро, дитя.\"":
            $hermi("~body_07.png// #(\"Дитя\"? Почему он настолько снисходителен все время?)")
            $hero("Что-то не так?")
            $hermi("~body_202.png// Нет, ничего сэр...")
        "\"Доброе утро, шлюха.\"":
            $hermi("~body_18.png// Э-э... Что?")
            $hero(g4, "#Это было глупо... Джинни, Джинни, ты торопишь события.",
                    m, "*Кхм* Извините, что-то застряло в горле... Доброе утро, мисс Грейнджер.")
            $hermi("~body_202.png// #(Он назвал меня.... нет, показалось.)")
            
    $hermi("~body_02.png// Профессор Дамблдор, я здесь, чтобы поговорить с вами, как  президент \"ОЗПМ\" - Общества по Защите Мужских Прав...")
    $hero("Защите прав?.............")
    $hermi("Мы провели чрезвычайное заседание вчера...// Главным вопросом была \"Хогвартская\" униформа для девочек...//"
        " Мы пришли к выводу, что существующий дресс-код является весьма нецелесообразным для нашего образовательного учреждения...")

    $screens.Show("ctc").Pause()

    $hermi("...")
    $hero("Серьезно?")

    $screens.Hide("ctc")

    $hermi("~body_04.png//Да, профессор. Уверяю вас, я очень серьезна.// То, как вы заставляете одеваться наших бедных девочек абсолютно неприемлемо  ...//"
        "Сейчас они носят легкомысленные наряды и отвлекают ребят от учебы, ставя их в невыгодное положение...// ~body_07.png// Все эти отвлекающие факторы...// И бедные парни...")
    $hero("Кто-нибудь из ребят жалуется на это?")
    $hermi("~body_04.png//Мы не будем ждать, пока проблема проявится, сэр! Мы уничтожим ее в зародыше!//"
        "~body_07.png//Ни один человек не должен находиться в невыгодном положении, просто из-за своего пола.// Это называется \"Сексизм\" в мире Маглов, сэр.")
    $hero("Как по мне, ваша мысль слишком извилиста, мисс Грейнджер.// Вы что, предлагаете заставить всех студенток академии носить паранджу?")
    $hermi("~body_207.png//Будет достаточно удвоить длину юбки девочек, сэр...")

    menu:

        "{size=-4}\"Это смешно. Отказано!\"{/size}":
            $ d_flag_05 = True #Notion refused. Will take affect in the next event.
            $hermi("~body_05.png//Что... Н-но? Мы приняли решение...")
            $hero("Мисс Грейнджер, мне жаль вас прерывать, но пока еще я директор этой академии...// И принимать решения - моя прерогатива!")
            $hermi("~body_07.png//Значит, вы игнорируете голос народа, сэр?")
            $hero("Единственный голос, который я слышу - ваш, мисс Грейнджер.")
            $hermi("~body_05.png//Разве вы не знаете, что происходит с тиранами, которые игнорируют народную волю?// Их свергают!")
            $hero("Осторожно. Ваши слова пахнут изменой, юная леди.// Разве вы не знаете, что происходит с изменниками?// Их вешают!")
            $hermi("~body_47.png//!!!// Пф!// Я добьюсь, чтобы вы восприняли наше решение всерьез, профессор!")
        
        "{size=-4}\"Нет сексизму. Просьба удовлетворена!\"{/size}":
            $hermi("~body_01.png//Великолепно. Я дам всем знать.// Спасибо, профессор.")
          
    $screens.HideD3("bld1")
    $hermi.Visibility(transition=d3).chibi.Trans("goout door").Hide(d3)    
    $ renpy.play('sounds/door.mp3') #Sound of a door opening.
    pause.5

    $hero("...................................// Я начинаю наслаждаться нашими встречами все меньше и меньше...")

    $this.event_08_02.Finalize()
    return
#NOT IN USE###############################################################################################################################################################    
label event_08_03:
#    "EVENT_08_03"
    $ renpy.play('sounds/knocking.mp3') #Sound someone knocking on the door.
    "*Тук-тук-тук!*"
    $hero("Кто...")
    $hermi("Профессор, я вхожу...")

    $ renpy.play('sounds/door.mp3') #Sound of a door opening.

    $hermi.chibi.State("door", speed="go").Trans(d4, "blink").Trans("go center", "blink") # Если делать dissolve в движении, то сбивается счетчик времени. Лучше выполнить появление чибика стоя, затем уже двигать его 
    pause.5
    $screens.ShowD3("bld1")

    $hermi("~body_01.png").Visibility("body+")("Доброе утро, профессор Дамблдор.")

    menu:
        "\"Доброе утро, мисс Грейнджер.\"":
            pass
        "\"Доброе утро, дитя.\"":
            $hermi("~body_07.png// (\"Дитя\"? Ему обязательно быть настолько снисходительным все время? Противный старый хрен!)")
            $hero("Что-то не так?")
            $hermi("~body_202.png// Нет, ничего сэр...")
        "\"Доброе утро, мисс президент.\"":
            $hermi("~body_202.png// #(Очень похоже на сарказм...)")
            
    if not d_flag_05:
        $hermi("~body_07.png// Вы обещали принять меры, профессор...// Но ничего не изменилось с момента нашего последнего разговора...")

        menu:
            "\"Я солгал...\"":
                $hermi("~body_203.png// Н-но...// Но вы директор школы, сэр. Вы слово должно означать что-то...")
            "\"Я забыл\"":
                $hermi("~body_05.png// Вы забыли, сэр?// Вы это серьезно?// Или, может быть, вы просто не хотите заниматься этим?")
            "\"Меня просто это не волнует.\"":
                $hermi("~body_203.png// Н-но....?// Профессор Дамблдор, это серьезный вопрос!")

    else:
         $hermi("~body_07.png// Профессор Дамблдор, вы отвергли предложение, которое я озвучила вам на нашей прошлой встрече...// И теперь мы пожинаем плоды...")

    $hermi("Парням трудно сосредоточиться на учебе...")
    $hero("О, у меня есть решение!// Давай наденем на головы девушкам бумажные пакеты!")
    $hermi("Это тоже сексизм...// Другой пример сексизма...// Это называется \"Женоненавистничество\".")
    $hero("\"Женоненавистничество\" - это общая неприязнь к женщинам, мисс Грейнджер.// Здоровый мужчина биологически не может испытывать антипатию ко всем женщинам...// Иначе человечество давным-давно бы вымерло...")
    $hermi("~body_202.png// Профессор, сейчас не время играть словами.// Вся школа находится в опасности!")
    $hero("Неужели..?")
    $hermi("~body_04.png// Вчера было еще одно заседание \"ОЗМП\", и--")
    $hero("Ох, опять...// А есть хоть один парень в вашем маленьком \"Обществе по защите мужских прав\"?")
    $hermi("~body_50.png// Это не относится к делу.")
    $hero("А я считаю, что относится...")
    $hermi("~body_191.png// Это не имеет значения...")
    $hero("Как это не имеет значения? Это единственное, что {size=+7}имеет{/size} значение!")
    $hermi("~body_206.png// Позвольте мне закончить мою мысль, пожалуйста.// Я официально к вам обращаюсь, как президент \"ОЗМП\"...// И как представитель этой школы ...//"
        "Мы требуем соблюдения этих новых норм...// ~body_120.png// Во-первых...// Ни один преподаватель не должен повышать голос или нелестно отзываться о студенте...")
    $hero("Что?")
    $hermi("Во-вторых...// Все школьные призраки должны быть заключены в заброшенной башне в Северном крыле школы.")
    $hero("У Вас есть привидения? Это очень круто!")
    $hermi("В-третьих...// ~body_186.png// Каждый учитель, и особенно профессор Северус Снейп, должен проходить проверку квалификации каждые три месяца...")
    $hero("Это все?")
    $hermi("Это все, сэр.")

    menu:
        m "..."
        "\"Хорошо. Ваши требования будут удовлетворены.\"":
            $hermi("~body_03.png// Спасибо, профессор.// Я, как представитель студентов , благодарю за ваше сотрудничество.")
        "\"Звучит как бред. Вы свободны\"":
            $hermi("~body_47.png// Что? Я...// Но это ... вы не можете...")
            $hero("Свободны!")
            $hermi("~body_51.png// Пф!")

    $screens.HideD3("bld1")
    $hermi.Visibility(transition=d3).chibi.Trans("goout door").Hide(d3)    
    $ renpy.play('sounds/door.mp3') #Sound of a door opening.
    pause.5

    $hero("....................")

    $this.event_08_03.Finalize()
    return

            
            
            
##################################################################################################################
label event_09: #Second visit from Hermione. Says she sent a letter to the Minestry. 
                #Takes place after first special event with Snape, where he just complains about Hermione.
    
    #"EVENT_09"
    stop music fadeout 3.0
    $ renpy.play('sounds/knocking.mp3') #Sound someone knocking on the door.
    "*Тук-тук-тук!*"
    menu:
        "\"Кто это?\"":
            her "Это я, Гермиона Грейнджер." 
            m "Снова эта маленькая ведьма..." 
            her "Могу я войти, сэр?"
            menu:
                m "..."
                "\"Конечно нет! Я занят! Возвращайся позже!\"":
                    her "Но..."
                    her "Хорошо... Тогда я зайду к вам завтра..."
                    $event.NotFinished()
                    return 
                "\"Конечно. Входи.\"":
                    pass
        "\"Я занят. Приходи позже.\"":
            her "Но..."
            her "Ладно, хорошо..."
            $event.NotFinished()
            return 
        "\"Да, входи.\"":
            pass
        "\"...................................\"":
            $ renpy.play('sounds/knocking.mp3') #Sound someone knocking on the door.
            "*Тук-тук-тук!*"
            m "............................."
            her "Профессор, я вхожу..."
            m "{size=-4}(Дерьмо!){/size}"

    $ event09 = True #You let Hermione in. This event will stop looping now.
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
    
    play music "music/Chipper Doodle v2.mp3" fadein 1 fadeout 1 
    
    $ pos = POS_370
    $herView.showQ( "body_03.png", pos )
    show screen hermione_02
    with Dissolve(.3)
    show screen ctc
    pause
    $herView.hideshowQQ( "body_04.png", pos )

    her "Доброе утро, профессор Дамблдор."
    hide screen ctc
    menu:

        "\"Доброе утро, дитя.\"":
            $herView.hideshowQQ( "body_09.png", pos )
            her "{size=-4}(Опять назвал меня \"дитя\"...){/size}"
            $herView.hideshowQQ( "body_04.png", pos )
            her "Сэр, я была бы признательна, если бы вы обращались ко мне как к ровне..."
            m "{size=-4}(Я фактически старше тебя на миллионы лет, ведьма. Мы вообще не можем быть равны.){/size}"
            m "...................."
            $herView.hideshowQQ( "body_09.png", pos )
            her "................"
        "\"Доброе утро, мисс Грейнджер.\"":
            her "Эм... так вот, о причине, по которой я к вам зашла..."
        "\"Да, да, пофигу...\"":
            pass
    
    her "Я вижу, что независимо от того, что я делаю - я не могу до вас достучаться, сэр."
    $herView.hideshowQQ( "body_04.png", pos )
    her "Вследствие вашего пренебрежительного отношения к своим обязанностям, я решила взять все на себя!"
    m "Ты... что...?"
    her "Да! Мы, гордые студенты Хогвартса терпеть не можем сексизм..."
    her "Не следует думать, что какой-то пол в чем-то лучше другого."
    m "Но-"
    $herView.hideshowQQ( "body_05.png", pos )
    her "Пожалуйста, дайте мне закончить, профессор!"
    $herView.hideshowQQ( "body_04.png", pos )
    her "Вы знаете, я создала \"Общество по защите мужских прав\" в нашей школе!"
    g4 "Да, я уже слышал от вас ..."
    g4 "Это типично для вас винить во всем-"
    stop music fadeout 1.0
#    m "Стоп, ты сказала {size=+5}МУЖСКИХ{/size} прав?"
    m "Ну и как же мы защищаем {size=+5}МУЖСКИЕ{/size} права?"
    $herView.hideshowQQ( "body_11.png", pos )
    play music "music/Chipper Doodle v2.mp3" fadein 1 fadeout 1 
    her "Вы понятия не имеете, каково быть мальчиком в нашей школе, особенно в наше время..."
    menu:
        "\"Ну, думаю, они справляются...\"":
            $herView.hideshowQQ( "body_04.png", pos )
            her "Нет, вы не знаете, потому что отказываетесь слушать нас, сэр!"
            her "Но теперь вы услышите нас..."
        "{size=-3}\"Эта общество - самая глупая идея, которую я когда-либо слышал.\"{/size}":
            $herView.hideshowQQ( "body_07.png", pos )
            her "Я была уверена, что вы скажете что-то вроде этого..."

    $herView.hideshowQQ( "body_09.png", pos )
    her "Вы знаете, что девушки оказывают некоторые услуги, чтобы заработать очки для факультета?"
    her "Иногда даже за хорошую оценку..."
    m "Правда?"
    $herView.hideshowQQ( "body_04.png", pos )
    her "В \"Гриффиндоре\" никто этим не занимается, конечно же..."
    her "И вот что ставит нас в невыгодное положение - наша честность!"
    her "А что до мальчиков, то они должны трудиться в десять раз больше, чем девочки, которым сдать тест не составит труда..."
    her "Или, если они достаточно удачливы, получить какое-то ничтожное одно очко..."
    $herView.hideshowQQ( "body_02.png", pos )
    her "Это сексизм в чистом виде!"
    menu:
        m "..."
        "\"Что ты хочешь, чтобы я сделал?\"":
            $herView.hideshowQQ( "body_03.png", pos )
            her "Ничего!"
            m "Отлично. Я рад."
        "\"Даже не знаю, что сказать...\"":
            $herView.hideshowQQ( "body_03.png", pos )
            her "Вам не нужно больше ничего говорить, профессор."
        "\"Ты смешна!\"":
            $herView.hideshowQQ( "body_07.png", pos )
            her "Я? Ну, увидим..."

    $herView.hideshowQQ( "body_04.png", pos )
    her "Я уже отправила письмо в министерство магии."
    with hpunch
    g4 "{size=+7}Что ты сделала?!{/size}"
    m "{size=-4}(Стоп, меня действительно это так заботит?){/size}"
    her "Мне очень жаль, но вы не оставили мне выбора, профессор."

    her "Теперь, прошу простить меня, мне пора на занятия..."
    hide screen bld1
    $herView.hideQ()
    with Dissolve(.3)
    $ walk_xpos=400 #Animation of walking chibi. (From)
    $ walk_xpos2=610 #Coordinates of it's movement. (To)
    $ hermione_speed = 02.0 #The speed of moving the walking animation across the screen.
    show screen hermione_walk_01_f 
    pause 2
    hide screen hermione_walk_01_f 
    $ renpy.play('sounds/door.mp3') #Sound of a door opening.
    with Dissolve(.3)
    pause.5
    m "...................."
    

#    $ hermione_is_waiting_01 = False #Makes sure this event is not repeated.
#    $ snape_against_hermione_02 = True #Turns True after event_09. Activates second event when hanging out with Snape.
    
    play music "music/Brittle Rille.mp3" fadein 1 fadeout 1
    $this.event_09.Finalize()
    return






            
            
            
            
            
            
            
            
            
            
            
            

#NOT IN USE###############################################################################################################################################################
label event_09_2: #Takes place after second special event with Snape, where he just complains about Hermione.
    "EVENT_09"
    $ renpy.play('sounds/knocking.mp3') #Sound someone knocking on the door.
    "*Тук-тук-тук!*"
    menu:
        "\"Кто это?\"":
            her "Это я, Гермиона Грейнджер." 
            m "(Снова эта молоденькая ведьма...)" 
            her "Могу я войти, сэр?"
            menu:
                m "..."
                "\"Категорически нет! Я занят! Возвращайся позднее!\"":
                    her "Но..."
                    her "Хорошо... Я вернусь завтра..."
                    return
                "\"Конечно, входи.\"":
                    pass
        "\"Я занят. Приходи позже.\"":
            her "Но..."
            her "Хорошо..."
            return
        "\"Да, входи.\"":
            pass
        "\"...................................\"":
            $ renpy.play('sounds/knocking.mp3') #Sound someone knocking on the door.
            "*Тук-тук-тук!*"
            m "............................."
            her "Профессор, я вхожу..."
            m "{size=-4}(Дерьмо!){/size}"

    $ event09 = True #You let Hermione in. This event will stop looping now.
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
    her "Доброе утро, профессор Дамблдор."
    menu:
        "\"Доброе утро, мисс Грейнджер.\"":
            pass
        "\"Доброе утро, дитя.\"":
            her "{size=-5}(\"Дитя\"? Он должнен быть настолько снисходительной все время? Противный старый хрен!){/size}"
            m "Что-то не так?"
            her "Ничего, сэр..."
        "\"...............\"":
            her "...................."
            
            
    her "Мои занятия скоро начнуться, так что у меня не так много времени..."
    her "Быть отличником-это не легко, поэтому я надеюсь, вы понимаете, что другие ученики в нашей школе берут пример с меня."
    m "{size=-4}(Неужели...?){/size}"
    her "Я понимаю, что вы очень важно персона..."
    her "Но немогли бы вы  уделить немного своего времени, чтобы выполнять ваши обязанности как директора школы?"
    menu:
        "\"Прости,я не понял?\"":
            her "Да, я отказываюсь потакать вам больше!"
        "\"...................\"":
            pass
    her "Я принесла столько идей для школы ..."
    her "И вы, сэр, игнорируете, каждый из них!"
    her "Знаете ли вы, что некоторые девочки из \"Слизерина\" предлогают сексуальные услуги в обмен на очки факультета?"
    m "Что они?"
    her "Вы не понимаете что происходит?"
    her "Студенты не должны больше работать, не надо учиться, все, что им нужно делать, это показать свои тела..."
    her "Это ужасно!"
    her "Я предупреждаю, профессор..."
    menu:
        "\" Вы \"Пердупреждаете меня\" Мисс Грейнджер?\"":
            her "Да, профессор. Я предупреждаю вас."
            her "Если Вы не готовы выслушать меня, я найду кого-то, кто выслушает!"
        "\"..............................................................\"":
            pass
    her "Если Вы не примите меры, тогда вы не оставивите мне выбора, профессор..."
    her "Мне придется обратиться в Министерство магии..."
    m "{size=-4}(Министерство магии? Меня это так волнует?){/size}"
    menu:

        "\"Успокойтесь пожалуйста, мисс Грейнджер.\"":
            her "Я не могу оставаться спокойной, смотря на  ваше невежество, сэр!"
        "\"Я услышал, вас. Я приму меры, я обещаю.\"":
            her "В самом деле? Ну, я рада, что мы наконец пришли к пониманию, сэр."
            her "Или вы просто будете игнорировать мои просьбы, как обычно?"
        "\"Из моего кабинета, девушка! Вон, я сказал!!!\"":
            her "Что?"
            m "Вон из моего кабинета!"
            her "Н-но..."
            with hpunch
            g4 "{size=+7}ВЫШЛА Я СКАЗАЛ!!!{/size}"
            her "{size=-6}(Оу... никогда не видел его таким грозным...){/size}"
            her "{size=-6}(Мне лучше уйти, прежде чем он поймает инсульт или что-то подобное...){/size}"
            her "..............."
            jump pissed_me_off

    her "Ох... я уже опаздываю на занятия. Я должна идти."
    m "Хорошего дня... {size=-5}ведьма!{/size}"
    her "Спасибо, профессор."
    label pissed_me_off:
    hide screen bld1
    $herView.hideQ()
    with Dissolve(.3)
    $ walk_xpos=400 #Animation of walking chibi. (From)
    $ walk_xpos2=610 #Coordinates of it's movement. (To)
    $ hermione_speed = 02.0 #The speed of moving the walking animation across the screen.
    show screen hermione_walk_01_f 
    pause 2
    hide screen hermione_walk_01_f 
    $ renpy.play('sounds/door.mp3') #Sound of a door opening.
    with Dissolve(.3)
    pause.5
    m "...................."
    
#    $ hermione_is_waiting_01 = False #Makes sure this event is not repeated.
#    $ snape_against_hermione_02 = True #Turns True after event_09. Activates second event when hanging out with Snape.
    return

   



#NOT IN USE###############################################################################################################################################################
label event_10: #Takes place after second special even with Snape where Ginie is worried that Hermione is still in power.
    #Hermione says that she sent the letter to the Ministry of Magic."
    "EVENT_10"
    $ renpy.play('sounds/knocking.mp3') #Sound someone knocking on the door.
    "*Тук-тук-тук!*"
    menu:
        "\"Кто это?\"":
            her "Это я, Гермиона Грейнджер." 
            m "(Снова эта молоденькая ведьма...)" 
            her "Могу я войти, сэр?"
            menu:
                m "..."
                "\"Абсолютно нет! Я занят! Приходите по позже!\"":
                    her "Но..."
                    her "Хорошо... Тогда я вернусь позднее..."
                    return
                "\"Конечно, входи.\"":
                    pass
        "\"Я занят. Приходите по позже.\"":
            her "Но..."
            her "Хорошо..."
            return
        "\"Да, входи.\"":
            pass
        "\"...................................\"":
            $ renpy.play('sounds/knocking.mp3') #Sound someone knocking on the door.
            "*Тук-тук-тук!*"
            m "............................."
            her "Профессор, я вхожу..."
            m "{size=-4}(Дерьмо!){/size}"

    $ event10 = True #You let Hermione in. This event will stop looping now.
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
    her "Доброе утро, профессор Дамблдор."
    menu:
        "\"Доброе утро, дитя.\"":
            her "{size=-4}(Опять \"дитя\"...){/size}"
            her "Сэр, я был бы очень признателен, если вы могли бы относиться ко мне как к ровне..."
            m "{size=-4}(Я на миллионы лет старше тебя, ведьма. Ты мне не ровня.){/size}"
        "\"Доброе утро, мисс Грейнджер.\"":
            her "Эм... та, причина, по которой я здесь сегодня..."
        "\"Да, Да, выкладывай...\"":
            her "Eм..."
    her "Я вижу, что вам не  неважно, чтобы я не делала, я просто не могу достучаться до вас, сэр."
    her "Так что в свете вашей халатности и по отношению к вашим обязанностям в качестве директора школы..."
    her "Я решила взять инициативу в свои руки!"
#    m "Did you now...?"
#    her "Yes! And since I detest sexism..."
#    m "You do, do you?"
#    her "Yes, I do. No individual shall be treated differently based on his or her gender."
#    m "This doesn't make any sence, girl!"
#    her "Let me finish, professor!"
#    her "I'm organizing a \"Men's rights movement\" in our school!"
#    m "Oh, this is just typical! Blame everything on- -"
#    m "Wait, did you say {size=+5}MEN'S{/size} rights?"
#    her "You have no idea how hard it is to be a boy in our school these days..."
#    menu:
#        "\"Didn't see this one coming...\"":
#            her "No, you did not, because you refuse to listen to me, sir!"
#        "\"Literally stupidest thing I've ever heard.\"":
#            her "I knew you will say something like that..."
    her "Половина девочек в этой школе сейчас продают себя ради очков факультета..."
    her "Иногда даже за хорошие отметки..."
    her "Никто из \"Гриффиндора\" не занимается, конечно..."
    her "И это то, что ставит нас в невыгодное положение - наша честность!"
    her "Немыслимо..."
    her "Мальчикам намного труднее, - они должны работать в десять раз упорнее, тогда как  девочкам достаточно просто пройти тест..."
    her "Или, если им повезет, получить одно очко факультета..."
    her "Это сексизм в чистом виде!"
    menu:
        "\"Что вы хотите чтобы {size=+7}Я{/size} сделал?\"":
            her "Ничего!"
        "\"Не уверен, что сказать...\"":
            her "Вам не нужно ничего говорить , профессор."
        "\"Вы смешны!\"":
            her "Я? Вот увидите..."
    her "Я уже направила письмо в Министерство магии."
    with hpunch
    g4 "{size=+7}Вы сделали, что?!{/size}"
    m "{size=-4}(Подожди, меня действительно это волнует?){/size}"
    her "Я сожалею, но Вы не оставили мне выбора, профессор."
    her "Теперь, если вы простите меня, я должна успеть на мои занятия..."

    hide screen bld1
    $herView.hideQ()
    with Dissolve(.3)
    $ walk_xpos=400 #Animation of walking chibi. (From)
    $ walk_xpos2=610 #Coordinates of it's movement. (To)
    $ hermione_speed = 02.0 #The speed of moving the walking animation across the screen.
    show screen hermione_walk_01_f 
    pause 2
    hide screen hermione_walk_01_f 
    $ renpy.play('sounds/door.mp3') #Sound of a door opening.
    with Dissolve(.3)
    pause.5
    m "Эта девушка тихо высасывает всю радость из меня..."
   
    $ hermione_takes_classes = True
   
#    $ hermione_is_waiting_02 = False #Makes sure this event is not repeated.
#    $ days_without_an_event = 0 #Resets the counter. This counts how many days have passed since this event happened.
    return

###############################################################################################################################################################
label event_11: #Third visit, after second special date with Snape. Hermione complains that she almost failed a test. (EVENING EVENT!)
    #"EVENT_11"
    stop music fadeout 1.0
    $ renpy.play('sounds/knocking.mp3') #Sound someone knocking on the door.
    "*Тук-тук-тук!*"
    her "Профессор, я вхожу!"
    m "...."
    play music "music/Chipper Doodle v2.mp3" fadein 1 fadeout 1 

    $ walk_xpos=570 #Animation of walking chibi. (From)
    $ walk_xpos2=400 #Coordinates of it's movement. (To)
    $ hermione_speed = 02.1 #The speed of moving the walking animation across the screen.
    $ renpy.play('sounds/door.mp3') #Sound of a door opening.
    # show screen hermione_walk_01 
    show screen hermione_chibi_robe #Hermione. Chibi. Walking. Wearing a robe.
    with d4
    pause 1.8
    $ hermione_chibi_xpos = 400 #Near the desk.
    #show screen hermione_02 #Hermione stands still.
    show screen hermione_02_b #Hermione stands still wearing a robe.
    show screen bld1
    with Dissolve(.3)
    
    #$ herView.data().addItemKey( 'robe', CharacterExItemRobe( herView.mClothesFolder, "robe.png", G_Z_DRESS + 1, 'body' ) )
    $herView.data().addItem( 'item_robe_study' )
    
    $ pos = POS_370
    $herView.showQ( "body_09.png", pos )
    show screen ctc
    with Dissolve(.3)   
    pause

    $herView.hideshowQQ( "body_12.png", pos )
    her "Добрый вечер, профессор."
    hide screen ctc
    menu:
        "\"- Взгляд полный ненависти -\"":
            $herView.hideshowQQ( "body_07.png", pos )
            her "Можете смотреть на меня как угодно, сэр."
            her "Это не поможет решить проблемы школы."
        "*Раздражительный вздох*":
            $herView.hideshowQQ( "body_03.png", pos )
            her "Не вовремя?"
            $herView.hideshowQQ( "body_02.png", pos )
            her "Ну, я уже здесь..."
        "\"....................................\"":
            $herView.hideshowQQ( "body_02.png", pos )
            her "Профессор?"
            m "Да, да..."
    $herView.hideshowQQ( "body_04.png", pos )
    her "Что-то...странное произошло сегодня..."
    $herView.hideshowQQ( "body_07.png", pos )
    her "Я не знаю, как это объяснить..."
    $herView.hideshowQQ( "body_09.png", pos )
    her "................................"
    $herView.hideshowQQ( "body_12.png", pos )
    her "Я почти провалила тест..."
    menu:
        "\"Такое бывает со студентами.\"":
            $herView.hideshowQQ( "body_12.png", pos )
            her "С другими студентами. Но не со мной, сэр!"
            $herView.hideshowQQ( "body_13.png", pos )
            her "Я никогда..."
        "\"(Прекращай, Снейп!)\"":
            $herView.hideshowQQ( "body_03.png", pos )
            her "Простите?"
            m "Что?"
            m "Ох, Я сказал, что это очень плохо. Как ты себя чувствуешь?"
            $herView.hideshowQQ( "body_07.png", pos )
            her "................."
        "\"Расскажи мне почему?\"":
            her "Потому что... это не обычный тест!"

    her "Я не уверена, что происходит..."
    m "Все зло настроено против вас, мисс Грейнджер?"
    $herView.hideshowQQ( "body_03.png", pos )
    her "Это не смешно, сэр."
    $herView.hideshowQQ( "body_04.png", pos )
    her "Вы должны считать меня \"мерилом\" нашей системы образования."
    her "Если я \"почти\" провалила тест, вероятно остальные вообще не сдали его."
    m "И...?"
    $herView.hideshowQQ( "body_07.png", pos )
    her "Да, профессор. Сегодня что-то пошло не так..."
    $herView.hideshowQQ( "body_12.png", pos )
    her "................................."
    $herView.hideshowQQ( "body_11.png", pos )
    her "Но что, если это не так?"
    her "Что, если отныне все тесты будут такие сложные?"
    $herView.hideshowQQ( "body_10.png", pos )
    her "Мне нужно лучше заниматься!"
    label cant_say:
    menu:
        "\"Я могу обучать вас, мисс Грейнджер.\"":
            $herView.hideshowQQ( "body_14.png", pos )
            her "Вы?"
            $herView.hideshowQQ( "body_15.png", pos )
            her "О, благодарю вас за предложение, но не думаю, что в этом есть необходимость, сэр."
            $herView.hideshowQQ( "body_16.png", pos )
            her "Лучший репетитор это книга и вся библиотека Хогвартса в моем распоряжении."
        "\"Мудрое решение, мисс Грейнджер.\"":
            $herView.hideshowQQ( "body_15.png", pos )
            her "Спасибо, профессор."
        "\"Тебе нужно взять мой член в свой ротик.\"":
            m "Тебе нужно взять мой чле-"
            $herView.hideshowQQ( "body_15.png", pos )
            her "А?"
            m "{size=-4}(Нет, я не могу этого сказать...){/size}"
            $herView.hideshowQQ( "body_17.png", pos )
            her "......?"
            jump cant_say
    m "............"
    $herView.hideshowQQ( "body_16.png", pos )
    her "Ну, если это все, то мне стоит скорректировать свое расписание."
    m "Как пожелаете..."
    
    hide screen bld1
    $herView.hideQ()
    with Dissolve(.3)
    $ walk_xpos=400 #Animation of walking chibi. (From)
    $ walk_xpos2=610 #Coordinates of it's movement. (To)
    $ hermione_speed = 02.0 #The speed of moving the walking animation across the screen.
    show screen hermione_chibi_robe_f #Hermione. Chibi. Walking. Wearing a robe.
    #show screen hermione_walk_01_f 
    pause 2
    hide screen hermione_chibi_robe_f #Hermione. Chibi. Walking. Wearing a robe.
    $ renpy.play('sounds/door.mp3') #Sound of a door opening.
    with Dissolve(.3)
    pause.5
    
    $ herView.data().delItem( 'item_robe_study' )
    
    $ event11_happened = True #Allows next event to start.
    $ days_without_an_event = 0 #Resets the counter. This counts how many days have passed since this event happened.
    
    play music "music/Music for Manatees.mp3" fadein 1 fadeout 1
    $this.event_11.Finalize()
    return


###############################################################################################################################################################
label event_12: # Hermione complains that she did failed a test. (EVENING EVENT!)
    #"EVENT_12"
    play music "music/Chipper Doodle v2.mp3" fadein 1 fadeout 1 
    $ renpy.play('sounds/door.mp3') #Sound of a door opening.
    
    $ walk_xpos=570 #Animation of walking chibi. (From)
    $ walk_xpos2=400 #Coordinates of it's movement. (To)
    $ hermione_speed = 02.1 #The speed of moving the walking animation across the screen.
    $ renpy.play('sounds/door.mp3') #Sound of a door opening.
    show screen hermione_walk_01 
    with d4
    pause 1.8
    $ hermione_chibi_xpos = 400 #Near the desk.
    show screen hermione_02 #Hermione stands still.
    with d3
    her "Профессор! Мне нужно поговорить с вами!"
    m "(Теперь она даже не удосужилась постучаться?)"
    show screen bld1
    with Dissolve(.3)
    $ pos = POS_370
    $herView.hideshowQQ( "body_11.png", pos )

    her "Профессор, сегодня что-то пошло не так!"
    her "Думаю, что я сегодня завалила тест..."
    her "Не могу поверить, что это произошло!"
    $herView.hideshowQQ( "body_18.png", pos )
    her "Как это вообще возможно?!"
    menu:
        "\"Тебе стоит лучше учиться, девочка!\"":
            $herView.hideshowQQ( "body_19.png", pos )
            her "Но я занималась всю ночь!"
        "\"Ну же... Все не так страшно.\"":
            $herView.hideshowQQ( "body_20.png", pos )
            her "Нет! Это катастрофа!" 

    $herView.hideshowQQ( "body_21.png", pos )
    her "И хуже того, мне кажется, что я единственная, кто его завалила..."
    $herView.hideshowQQ( "body_22.png", pos )
    her "На кого я теперь похожа?"
    $herView.hideshowQQ( "body_23.png", pos )
    her "Нужно узнать результаты, но..."
    $herView.hideshowQQ( "body_13.png", pos )
    her "Да, я уверена, что кто-нибудь еще завалил его..."
    $herView.hideshowQQ( "body_11.png", pos )
    her "Я имею в виду, как без этого, верно?"
    $herView.hideshowQQ( "body_13.png", pos )
    her "....................."
    $herView.hideshowQQ( "body_11.png", pos )
    her "....верно?"
    menu:
        "{size=-3}\"Конечно. В конце концов вы лучший ученик.\"{/size}":
            $herView.hideshowQQ( "body_09.png", pos )
            her "Именно..."
            her "Или, по крайней мере была им, до сегодняшнего дня..."
            $herView.hideshowQQ( "body_20.png", pos )
            her "Не могу поверить, что это произошло!"
        "{size=-3}\"Вы можете стать лучше, если я буду вас обучать.\"{/size}":
            $ tutoring_offer_made = True #Affects conversation in the next event.
            $herView.hideshowQQ( "body_17.png", pos )
            her "Хм..."
            $herView.hideshowQQ( "body_13.png", pos )
            her "Да, это может мне помочь, я полагаю..."
            $herView.hideshowQQ( "body_14.png", pos )
            her "Я благодарна вам за предложение, но..."
            her "Могу я подумать над этим?"
            m "Только не затягивай..."
        "{size=-3}\"Я думаю, что мы скоро все узнаем.\"{/size}":
            $herView.hideshowQQ( "body_15.png", pos )
            her "Да, думаю так..."

    $herView.hideshowQQ( "body_24.png", pos )
    her "Извините, профессор, возможно я была чересчур эмоциональна..."
    $herView.hideshowQQ( "body_14.png", pos )
    her "Но вы должны понимать, что на кону моя репутация!"
    $herView.hideshowQQ( "body_12.png", pos )
    her "Что-то должно быть не так с этим тестом..."
    her "И несмотря на то, что мне не удалось его сдать, скорее всего у меня больше всех баллов..."
    her "Как обычно..."
    $herView.hideshowQQ( "body_04.png", pos )
    

    her "Ну, мне лучше пойти. У нас еще одно \"ОЗМП\" собрание сегодня."
    her "Я дам вам знать о новых идеях."
    m "Не могу дождаться..."



    hide screen bld1
    $herView.hideQ()
    with Dissolve(.3)
    $ walk_xpos=400 #Animation of walking chibi. (From)
    $ walk_xpos2=610 #Coordinates of it's movement. (To)
    $ hermione_speed = 02.0 #The speed of moving the walking animation across the screen.
    show screen hermione_walk_01_f 
    pause 2
    hide screen hermione_walk_01_f 
    $ renpy.play('sounds/door.mp3') #Sound of a door opening.
    with Dissolve(.3)
    pause.5





    $ event12_happened = True #Allows next event to start.
    $ days_without_an_event = 0 #Resets the counter. This counts how many days have passed since this event happened.
    $this.event_12.Finalize()
    return


###############################################################################################################################################################
label event_13: # Hermione complains that she almost failed a test. (EVENING EVENT!)
    #"EVENT_13"
    $ renpy.play('sounds/door.mp3') #Sound of a door opening.
    


    $ walk_xpos=570 #Animation of walking chibi. (From)
    $ walk_xpos2=500 #Coordinates of it's movement. (To)
    $ hermione_speed = 02.0 #The speed of moving the walking animation across the screen.
    show screen hermione_walk_01 
    with d4
    pause 1.3
    $ hermione_chibi_xpos = 500 #Near the desk.
    show screen hermione_02 #Hermione stands still.
    with d3
    her "....................."
    m "???"
    
    $ walk_xpos=500 #Animation of walking chibi. (From)
    $ walk_xpos2=400 #Coordinates of it's movement. (To)
    $ hermione_speed = 02.0 #The speed of moving the walking animation across the screen.
    show screen hermione_walk_01 
    hide screen hermione_02 #Hermione stands still.
    pause 1.8
    $ hermione_chibi_xpos = 400 #Near the desk.
    show screen hermione_02 #Hermione stands still.
    with d3
    her "............"
    m "Мисс Грейнджер?" 
    her "..............................."
    m "Мисс Грейнджер?!!" 
    show screen bld1
    with d3
    $ pos = POS_370
    $herView.hideshowQQ( "body_26.png", pos )
    show screen ctc
    pause
    her "А?"
    hide screen ctc
    her "О, я уже здесь?"
    her "Извините, сэр... Я..."
    her ".................."
    her "Кажется, я..."
    her "Кажется... ух..."
    her "... Я все-таки завалила тест."
    her "Я..."
    $herView.hideshowQQ( "body_27.png", pos )
    her "Извините, профессор..."
    her "Я не знаю, почему я пришла к вам..."
    her "Я думаю, лучше мне уйти..."
    m "..................."
    hide screen bld1
    $herView.hideQ()
    with Dissolve(.3)
    
    
    $ walk_xpos=400 #Animation of walking chibi. (From)
    $ walk_xpos2=610 #Coordinates of it's movement. (To)
    $ hermione_speed = 01.0 #The speed of moving the walking animation across the screen.
    hide screen bld1
    with d3
    show screen hermione_run

    pause.9
    hide screen hermione_run
    with Dissolve(.3)
    $ renpy.play('sounds/door.mp3') #Sound of a door opening.
  
    pause.3
    m "............."
    m "Она будет в порядке..."
    m "Надеюсь..."



    
    
    
    
    
#    $ renpy.play('sounds/door.mp3') #Sound of a door opening.
#    $ hermione_chibi_xpos = 400 #Middle of the room.
#    show screen hermione_01_f #Hermione stands still.
#    with d3
#    her "................."
#    $ walk_xpos=400 #Animation of walking chibi. (From)
#    $ walk_xpos2=510 #Coordinates of it's movement. (To)
#    $ hermione_speed = 02.0 #The speed of moving the walking animation across the screen.
#    show screen hermione_walk_01_f 
#    pause 2
#    hide screen hermione_walk_01_f 
#    $ renpy.play('sounds/door.mp3') #Sound of a door opening.
#    $ hermione_chibi_xpos = 500 #Middle of the room.
#    show screen hermione_01_f #Hermione stands still.
#    with Dissolve(.3)
#    her "................"
    
#    $ walk_xpos=500 #Animation of walking chibi. (From)
#    $ walk_xpos2=610 #Coordinates of it's movement. (To)
#    $ hermione_speed = 02.0 #The speed of moving the walking animation across the screen.
#    show screen hermione_walk_01_f 
#    pause 2
#    hide screen hermione_walk_01_f 
#    $ renpy.play('sounds/door.mp3') #Sound of a door opening.
#    with Dissolve(.3)
#    pause.5



    $ event13_happened = True #Allows next event to start.
    $ days_without_an_event = 0 #Resets the counter. This counts how many days have passed since this event happened.
    $this.event_13.Finalize()
    return



###############################################################################################################################################################
label event_14: # Hermione comes after her breakdown (when she failed the test). She is asking for tutoring. Tutoring unlocked.
    #"EVENT_14"
    $ renpy.play('sounds/door.mp3') #Sound of a door opening.
    
    play music "music/Chipper Doodle v2.mp3" fadein 1 fadeout 1 

    $ walk_xpos=570 #Animation of walking chibi. (From)
    $ walk_xpos2=400 #Coordinates of it's movement. (To)
    $ hermione_speed = 02.1 #The speed of moving the walking animation across the screen.
    $ renpy.play('sounds/door.mp3') #Sound of a door opening.
    show screen hermione_walk_01 
    with d4
    pause 1.8
    $ hermione_chibi_xpos = 400 #Near the desk.
    show screen hermione_02 #Hermione stands still.
    with d3
    show screen bld1
    with Dissolve(.3)
    $ pos = POS_370
    $herView.showQ( "body_01.png", pos )
    show screen hermione_02
    with Dissolve(.3)   

    her "Доброе утро, Профессор."
    m "Я могу чем-то вам помочь, Мисс Грейнджер?"
    $herView.hideshowQQ( "body_04.png", pos )
    her "Ну, прежде всего, я хотела бы извиниться за вчерашнее..."
    $herView.hideshowQQ( "body_08.png", pos )
    her "Я никогда не заваливала тесты и поэтому не знала, как реагировать..."
    $herView.hideshowQQ( "body_04.png", pos )
    her "Но сейчас все намного лучше..."
    m "Понятно..." 
    her "Я не займу вас надолго, обещаю..."
    if tutoring_offer_made:
        her "Я здесь, чтобы принять ваше предложение."
        menu:
            "\"Какое предложение?\"":
                her "Ранее вы предложили обучать меня, сэр..."
                menu:
                    "\"Ох...уже поздно.\"":
                        $herView.hideshowQQ( "body_14.png", pos )
                        her "Уже..."
                        her "Поздно, сэр?"
                        her "Н-но...."
                        $herView.hideshowQQ( "body_11.png", pos )
                        her "Но мне нужны уроки, а вы умнейший волшебник, которого я знаю..."
                        $herView.hideshowQQ( "body_28.png", pos )
                        her "Пожалуйста, сэр, мне очень нужна ваша помощь."
                        menu:
                            "\"Покажи мне свои сиськи и мы договорились!\"":
                                $herView.hideshowQQ( "body_18.png", pos )
                                her "М-мои...?"
                                $herView.hideshowQQ( "body_29.png", pos )
                                her "............"
                                her "....."
                                $herView.hideshowQQ( "body_30.png", pos )
                                with hpunch
                                her "{size=+5}Профессор Дамблдор!!!{/size}"
                                m "{size=-5}(Ну, я хотя бы попытался...){/size}"
                                her "Я вам не \"Слизеринская\" шлюха!"
                                m "Конечно нет, мисс Грейнджер."
                                m "Это испытание... Ты прошла его. Хорошая работа."
                                $herView.hideshowQQ( "body_31.png", pos )
                                her "Что...?"
                                $herView.hideshowQQ( "body_24.png", pos )
                                her "О, конечно. Я иногда туплю. Простите за крик, сэр."
                                m "Мое предложение в силе, если хотите, чтобы я вас обучал - я займусь этим."
                                $herView.hideshowQQ( "body_29.png", pos )
                                her ".............."
                            "\"Ну, ладно, отлично...\"":
                                pass
                    "\"Ох, Отлично. Превосходно.\"":
                        pass

            "\"Чудно! Начнем сегодня?\"":
                pass
    else:
        $herView.hideshowQQ( "body_07.png", pos )
        her "Я... эм..."
        her "Сэр Дамблдор, я надеюсь, что не слишком многого прошу..."
        m "Да?"
        her "Эм... было бы неплохо, если..."
        her "..............."
        $herView.hideshowQQ( "body_09.png", pos )
        her "Вы могли бы немного обучить меня, сэр?"
        menu:
            "\"Я уверен, что это возможно.\"":
                pass
            "\"Хм... Я несколько занят.\"":
                $herView.hideshowQQ( "body_11.png", pos )
                her "Сэр, пожалуйста, вы лучший волшебник, которого я знаю!"
                m "{size=-4}(Ты и представить себе не можешь, маленькая ведьма){/size}"
                m "Я думаю, можно устроить, да..."
    $herView.hideshowQQ( "body_01.png", pos )
    her "Благодарю, сэр. Я очень признательна вам."
    $herView.hideshowQQ( "body_16.png", pos )

    her "Просто скажите мне и я принесу свои книжки."

    $herView.hideshowQQ( "body_09.png", pos )
    her "Теперь я должна учиться еще более усердно..."
    $herView.hideshowQQ( "body_06.png", pos )
    her "И я буду брать частные уроки у вас как можно чаще, сэр."
    $herView.hideshowQQ( "body_07.png", pos )
    her "Но это не все..."
    her "В \"ОЗМП\" мы исседуем нашу систему образования более детально..."
    her "Я думаю, кто-то играет не совсем честно..."
    m "Не может быть!"
    her "У меня есть список подозреваемых, я принесу его позже...."
    m "Эм... ладно..."
    $herView.hideshowQQ( "body_10.png", pos )
    her "О, занятия уже начинаются. Мне лучше пойти..."
    
    hide screen bld1
    $herView.hideQ()
    with Dissolve(.3)
    $ walk_xpos=400 #Animation of walking chibi. (From)
    $ walk_xpos2=610 #Coordinates of it's movement. (To)
    $ hermione_speed = 02.0 #The speed of moving the walking animation across the screen.
    show screen hermione_walk_01_f 
    pause 2
    hide screen hermione_walk_01_f 
    $ renpy.play('sounds/door.mp3') #Sound of a door opening.
    with Dissolve(.3)
    pause.5



    stop music fadeout 1.0

    $ event14_happened = True #Allows next event to start.
    $ days_without_an_event = 0 #Resets the counter. This counts how many days have passed since this event happened.
    
    show screen blktone
    with d3
    show screen notes
    $ renpy.play('sounds/win2.mp3') 
    ">Теперь вы можете вызывать Гермиону Грейнджер в кабинет."
    hide screen blktone
    with d3
#    $ summoning_hermione_unlocked = True #Unlocks after event_14. Adds "Summon Hermione" button to the door.
    $ hermione_takes_classes = True
#    $ tutoring_hermione_unlocked = True
    $ days_without_an_event = 0 #Resets the counter. This counts how many days have passed since this event happened.
    
    
    play music "music/Brittle Rille.mp3" fadein 1 fadeout 1
    $this.event_14.Finalize()
    return




###############################################################################################################################################################
label event_15: # Hermione comes and asks to buy a favour from her.
    
    #"EVENT_15"
    
#    $ slytherin +=49
#    hide screen s_p_u
#    $ s_p_u_pic = "what_49_points"
#    show screen s_p_u
    
    $ renpy.play('sounds/knocking.mp3') #Sound someone knocking on the door.
    "*Тук-тук-тук!*"
    menu:
        "\"Кто это?\"":
            her "Это я, Гермиона Грейнджер." 
            m "(Снова эта молоденькая ведьма...)" 
            her "Могу я войти, сэр?"
            menu:
                m "..."
                "\"Категорически нет! Я занят! Возвращайся позднее!\"":
                    her "Но..."
                    her "Ладно... Тогда я вернусь позднее..."
                    $event.NotFinished()
                    return 
                "\"Конечно, входи.\"":
                    pass
        "\"Я занят. Приходи позже.\"":
            her "Но..."
            her "Ну, ладно..."
            $event.NotFinished()
            return
        "\"Да, входи.\"":
            pass
        "\"...................................\"":
            $ renpy.play('sounds/knocking.mp3') #Sound someone knocking on the door.
            "*Тук-тук-тук!*"
            m "............................."
            her "Профессор, я вхожу..."
            m "{size=-4}(Дерьмо!){/size}"

   
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
    $herView.showQ( "body_13.png", pos )
    show screen hermione_02
    with Dissolve(.3)
    her "Добрый вечер, профессор..."
    her "........................"
    $herView.hideshowQQ( "body_29.png", pos )
    her "........................"
    her "........................"
    $herView.hideshowQQ( "body_31.png", pos )
    her "Эм......"
    $herView.hideshowQQ( "body_29.png", pos )
    her "................."
    m "Что такое, Мисс Грейнджер?"
    $herView.hideshowQQ( "body_31.png", pos )
    her "Ну, Эм..."
    her "Понимаете ли... \"Гриффиндор\" больше не лидирует..."
    $herView.hideshowQQ( "body_29.png", pos )
    her "И... все очень трудятся..."
    her "И они надеются на мою помощь, но я не знаю что делать..."
    m "............................"
    her "Профессор Дамблдор...."
    $herView.hideshowQQ( "body_32.png", pos )
    stop music fadeout 2.0
    her "Я хочу купить очки для факультета за мои услуги!"
    $herView.hideshowQQ( "body_33.png", pos )
    menu:
        "\"Ты имеешь в виду сексуальные услуги?\"":
            $herView.hideshowQQ( "body_34.png", pos )
            her "Эм... Я не уверена..."
            her "Те, которые дадут нашему факультету дополнительные очки..."
            $herView.hideshowQQ( "body_31.png", pos )
            her "Я бы могла написать эссе вам или..."
            $herView.hideshowQQ( "body_34.png", pos )
            her "Или может быть почистить вашу башню..?"
            m "{size=-4}(Почистить мою башню? Хех... Эта вероятно грязная шуточка или вроде того...){/size}"
            m "Ну, хорошо. Мы что-нибудь придумаем."
        "\"Ну, если вы настаиваете...\"":
            pass
        "\"Я так не думаю, мисс Грейнджер.\"":
            $herView.hideshowQQ( "body_31.png", pos )
            her "Н-но... Нам нужны очки..."
            her "Профессор, пожалуйста, я в безвыходном положении..."
            m "В безвыходном, вы говорите..?"
            m "Ну, ладно..."
    $herView.hideshowQQ( "body_01.png", pos )
    play music "music/Chipper Doodle v2.mp3" fadein 1 fadeout 1 
    her "Спасибо, профессор..."
    label choose_favor_agagin:
    $ d_flag_01 = False
    $ d_flag_02 = False
    $ d_flag_03 = False
    $ d_flag_04 = False
    her "Итак... Чего вы хотите?"
    menu:
        "\"Покажи мне свой язык...\"":
            $ d_flag_01 = True
            pass
        "\"Стой здесь. Дай мне взглянуть на тебя.\"":
            $ d_flag_02 = True
            pass
        "\"Корчи рожицы...\"":
            $ d_flag_03 = True
            pass
        "\"Скажи \"Я была очень плохой девочкой\".\"":
            $ d_flag_04 = True
            pass

    her "Эм..."
    her "Как много очков вы мне дадите за это...?"
    $ d_flag_05 = False # 20 Points.
    $ d_flag_06 = False # 40 Points.
    $ d_flag_07 = False # 10 Points.
    $ d_flag_08 = False # 1 Point.
    menu:
        "\"1 очко.\"":
            if d_flag_02: #Stand there.
                $ d_flag_08 = True # 1 Point.
                pass
            else:
                her "Я не думаю, что это стоит того..."
                jump choose_favor_agagin
        "\"10 очков.\"":
            if d_flag_02: #Stand there.
                $ d_flag_07 = True # 10 Points.
                pass
            else:
                her "Я не думаю, что это стоит того..."
                jump choose_favor_agagin
        "\"20 очков.\"":
            $ d_flag_05 = True
            her "Так мало...?"
            pass
        "\"40 очков.\"":
            $ d_flag_06 = True
            pass

    
    
    $ pos = POS_140
    her "Эм, ладно..."
    if d_flag_01: #Show me your tongue.
        $herView.hideshowQQ( "body_24.png", pos )
        herView "М-мой... язык, сэр?"
        m "Да, девочка, открой свой рот и покажи мне свой язычок."
        $herView.hideshowQQ( "body_12.png", pos )
        her "{size=-7}(Что за извращенец...){/size}"
        $herView.hideQQ()
        
        $ herView.showQQ( "body_07.png", pos )
        her "Эм...ну, ладно тогда..."
        $ herView.hideQQ()
        
        $ herView.showQQ( "body_08.png", pos )
        her "Вот..."
        $herView.hideshowQQ( "body_35.png", pos )
        her "............."
        her "............."
        $herView.hideshowQQ( "body_36.png", pos )
        her "................."
        show screen ctc
        pause
        menu: 
            "\"Очень хорошо. Вот твои очки.\"":
                pass
            "\"Плохо. Ты можешь лучше.\"":
                $herView.hideshowQQ( "body_12.png", pos )
                her "..............."
                her "Ладно, я попробую получше, сэр..."
                $herView.hideshowQQ( "body_11.png", pos )
                her "Как насчет этого?"
                $herView.hideshowQQ( "body_37.png", pos )
                her "А-а-а.................."
                $herView.hideshowQQ( "body_38.png", pos )
                "............................"
                $herView.hideshowQQ( "body_39.png", pos )
                her "......................................"
                her "..................................................."
                her "...................................................................."
                $herView.hideshowQQ( "body_40.png", pos )
                her "......................................................................................................."

    if d_flag_02: #Stand still...
#    if d_flag_01: #STAND STILL.
        $herView.hideshowQQ( "body_06.png", pos )
        her "И так, я просто буду стоять здесь...?"
        m "Отлично... Теперь повернись... Медленно."
        her "Ух... Ладно..."
        $herView.hideQ()
        hide screen bld1
        with d3
        pause.5
        show screen hermione_01_f #Hermione stands still.
        with Dissolve(.7)

        $her_head_state = 2
        her_head_main "................................."
        menu:
            m "Hm..."
            "\"Униформа очень идет вам, мисс Грейнджер...\"":
                $her_head_state = 1
                her_head_main "............"
                $her_head_state = 5
                her_head_main "Спасибо, Профессор Дамблдор..."
            "\"У вас отличное тело, мисс Грейнджер...\"":
                $her_head_state = 3
                her_head_main "!?"
                $her_head_state = 4
                her_head_main ".............."
                her_head_main "Спасибо, профессор..."
            "\"Достаточно. Вот твои очки...\"":
               
                
               
                show screen hermione_01 #Hermione stands still.
                with Dissolve(.7)
                pause.5
                show screen bld1
                with d3
                jump stupid_enogh
                                                        
            

        
        
        m "Очень хорошо. Теперь можешь повернуться обратно..."
        show screen hermione_01 #Hermione stands still.
        with Dissolve(.7)
        pause.7
        $ herView.showQQ( None, pos )
        show screen bld1
        with d3
        her "................."
   
    
    
#    if d_flag_02: #Pretend to be a monkey.
#        her "A monkey then..."
#        her "ooh ooh...."
#        her "ooh ooh ooh...."
#        m "Good, but you can do better..."
#        her "ooh ooh ooh...."
#        her "ooh ooh ooh... eee eee eee aah aah aah..."
#        m "Very well..."
    if d_flag_03: #STUPID FACE
        $herView.hideshowQQ( "body_24.png", pos )

        her "Скорчить глупую рожицу, значит..."
        her "Посмотрим..."
        label stupid_faces:
        $herView.hideshowQQ( "body_41.png", pos )
        her "Как насчет этого?"
        menu:
            "\"Отлично! очень тупо! Я имею в виду, глупо.\"":
                jump stupid_enogh
            "\"Не совсем глупая.\"":
                pass
        $herView.hideshowQQ( "body_12.png", pos )
        her "........."
        $herView.hideshowQQ( "body_43.png", pos )
        her "А так?"
        menu:
            "\"Ха-ха! Ты похожа на идиота!\"":
                jump stupid_enogh
            "\"Не достаточно глупо.\"":
                pass
        $herView.hideshowQQ( "body_12.png", pos )
        her "........."
        $herView.hideshowQQ( "body_42.png", pos )
        her "А что, если я сделаю так?"
        menu:
            "\"Отлично! Очень смешно!\"":
                jump stupid_enogh
            "\"Не достаточно глупо.\"":
                jump stupid_faces
    
    if d_flag_04: #BAD GIRL
        $herView.hideshowQQ( "body_07.png", pos )
        her "Я..."
        her "Я была очень плохой девочкой..."
        g9 "Ты была очень, очень, очень плохой девочкой?"
        her "Да, сэр..."
        her "Я была очень, очень, очень, очень плохой девочкой..."
        label to_early_for_sucking_cocks:
        menu:
            g9 "..."
            "\"Тебя нужно наказать?\"":
                $herView.hideshowQQ( "body_11.png", pos )
                her "Нужно ли меня... наказать?"
                $herView.hideshowQQ( "body_13.png", pos )
                her "Эм..."
                her "....................."
                $herView.hideshowQQ( "body_12.png", pos )
                her "Ну, я не идеальная, если вы об этом, сэр..."
                $herView.hideshowQQ( "body_13.png", pos )
                her "Но нужно ли меня наказывать... Хм?"
                $herView.hideshowQQ( "body_07.png", pos )
                her "На самом ли деле это мне решать...? Я имею в виду..."
                her "Какое это имеет значение?"
                m "Ты слишком самокритичная, девочка."
                m "Просто скажи, что тебя нужно наказать!"
                $herView.hideshowQQ( "body_05.png", pos )
                her "Ладно. Меня следует наказать!"
                $herView.hideshowQQ( "body_33.png", pos )
                her "{size=-5}(И я действительно так думаю иногда...){/size}"
                m "Хорошая девочка."
                $herView.hideshowQQ( "body_44.png", pos )
                her "................??"
                m "Это было так трудно?"
                $herView.hideshowQQ( "body_29.png", pos )
                her "Н-нет , сэр..."
                m "Ладно, значит..."
            "\"Хочешь чтобы тебя отшлепали?\"":
                $herView.hideshowQQ( "body_11.png", pos )
                her "Хочу ли я..."
                $herView.hideshowQQ( "body_18.png", pos )
                her "Чтобы меня отшлепали??"
                $herView.hideshowQQ( "body_05.png", pos )
                her "?!"
                $herView.hideshowQQ( "body_04.png", pos )
                her "Профессор, мне не очень уютно от таких вопросах- -"
                m "Извиняюсь, позволь мне перефразировать вопрос..."
                m "Как сильно тебе нужны эти очки?"
                $herView.hideshowQQ( "body_09.png", pos )
                her ".................."
                $herView.hideshowQQ( "body_04.png", pos )
                her "Да, сэр. Я хочу, чтобы меня ошлпепали"
                m "Отлично. Думаю достаточно на сегодня..."
                $herView.hideshowQQ( "body_07.png", pos )
                her "{size=-4}(На сегодня?){/size}"
            "\"Иди сюда и пососи мой член!\"":
                m "{size=-5}(Слишком рано для этого... Для начала мне следует цепануть ее.){/size}"
                jump to_early_for_sucking_cocks
            
        

    label stupid_enogh:
    if d_flag_05:
        m "20 очков \"Гриффиндору\"."
        $ gryffindor +=20
    elif d_flag_06:
        m "40 очков \"Гриффиндору\"."
        $ gryffindor +=40
    elif d_flag_07:
        m "10 очков \"Гриффиндору\"."
        $ gryffindor +=10
    elif d_flag_08:
        m "1 очко \"Гриффиндору\"."
        $ gryffindor +=1
    
    
    $herView.hideshowQQ( "body_24.png", pos )
    her "Да!.............."
    her "Это было довольно легко..."
    her "Вы думаете я могла бы покупать еще очки за подобные услуги в будущем, профессор?"
    menu:
        "\"Я не думаю, что это хорошая идея.\"":
            $herView.hideshowQQ( "body_28.png", pos )
            her "Пожалуйста, профессор..."
            her "Нам действительно нужны эти очки..."
            m "......."
            $herView.hideshowQQ( "body_29.png", pos )
            her "Вы очень уважаемый волшебник и, честно говоря..."
            her "Единственный человек в этой школе, у которого я могу попросить такое..."
            m "Ну, если ты настаиваешь..."
        "\"Возможно...\"":
            pass
            
    $herView.hideshowQQ( "body_06.png", pos )
    her "Спасибо, профессор. Огромное спасибо."
    $herView.hideshowQQ( "body_01.png", pos )
    her "Ну, я думаю мне стоит идти..."
    m "............"

    hide screen bld1
    $herView.hideQ()
    with Dissolve(.3)
    $ walk_xpos=400 #Animation of walking chibi. (From)
    $ walk_xpos2=610 #Coordinates of it's movement. (To)
    $ hermione_speed = 02.0 #The speed of moving the walking animation across the screen.
    show screen hermione_walk_01_f 
    pause 2
    $ hermione_chibi_xpos = 610 #Near the desk.
    hide screen hermione_walk_01_f 
    show screen hermione_01_f #Hermione stands still.
    with Dissolve(.3)

    if d_flag_01: #Show me your tongue
        her "{size=-4}(Хм...){/size}"
        her "{size=-4}(Студенты все время демонстрируют свои языки учителям...){/size}"
        her "{size=-4}(Хотя, учитель в это время обычно не смотрит...){/size}"
        her "{size=-4}(Но нет ничего плохого в том, что я сделала сегодня...){/size}"
        her "{size=-4}(Я получила нужные факультету очки...){/size}"
        
    if d_flag_02: #Stand still...
        her "{size=-4}(Я могу просто стоять здесь, а профессор будет смотреть на меня...){/size}"
        her "{size=-4}(В этом нет ничего плохого...вообще ничего...){/size}"
#        her "{size=-4}(ooh ooh ooh... eee eee eee aah aah aah...){/size}"
#        her "{size=-4}(I'm a monkey... I'm a money... I need to practice more...){/size}"
    if d_flag_03:
        her "{size=-4}(Глупое лицо...){/size}"
        her "{size=-4}(Глупое лицо...){/size}"
        her "{size=-4}(Мне нужно потренироваться с этим.){/size}"
    if d_flag_04:
        her "{size=-4}(Я плохая девчонка...){/size}"
        her "{size=-4}(Я очень плохая девчонка...){/size}"
        her "{size=-4}(Да, я могу легко говорить такое...){/size}"
        her "{size=-4}(В этом нет ничего плохого...вообще ничего...){/size}"


    $ renpy.play('sounds/door.mp3') #Sound of a door opening.
    hide screen hermione_01_f #Hermione stands still.
    with Dissolve(.3)


    $ event15_happened = True #Allows next event to start. This one stops looping when you not let Hermione in.
    $ days_without_an_event = 0 #Resets the counter. This counts how many days have passed since this event happened.
    stop music fadeout 1.0
    show screen blktone
    with d3
    show screen notes
    $ renpy.play('sounds/win2.mp3') 
    ">Теперь вы можете покупать сексуальные услуги Гермионы за очки для факультета."
    hide screen blktone
    with d3
    $ buying_favors_from_hermione_unlocked = True 
    $ days_without_an_event = 0 #Resets the counter. This counts how many days have passed since this event happened.
    $ event15_happened = True #Turns TRUE after event_15
    $this.event_15.Finalize()
    return



label event_16: #Учебники доставлены
    $ teacher_jinn_quest = 6
    m "..."
    m "Есть ли смысл в жизни?"
    m "..."
    g4 "Кто делает порноигры, в которых протагонисты успевают отвлекаться на подобную хрень?"
    #стук-перестук, заходит гермиона
    $ renpy.play('sounds/door.mp3') #Sound of a door opening.
    $ hermione_chibi_xpos = 400 #Near the desk.
    show screen hermione_02 #Hermione stands still.
    show screen bld1
    with d3
    $herView.hideshowQQ( "body_01.png", pos )
    her "Добрый вечер, профессор Дамблдор."
    her "Ваши учебники прибыли."
    m "Три дня, да..?"
    m "Почему все так часто используют цифру 3 в выдуманных историях?"
    g4 "Цифра 29 тоже стильно выглядит!"
    $herView.hideshowQQ( "body_09.png", pos )
    her "Эм... Профессор?"
    m "... что-то я отвлекся."
    m "Философское настроение, знаете ли."
    m "Вы что-то говорили про учебники?"
    $herView.hideshowQQ( "body_11.png", pos )
    her "Эм, да... Ваши книги доставили."
    g9 "Прекрасно! И где же они?"
    $herView.hideshowQQ( "body_15.png", pos )
    her "Лежат за дверью. Их так много, что Гарри и Рону потребовалось полтора часа, чтобы перенести их все из башни Гриффиндора."
    g4 "(И она еще говорила что-то о равноправии полов... Лицемерная сучка!)"
    m "Отлично! Несите их сюда!"
    $herView.hideshowQQ( "body_11.png", pos )
    her "Боюсь, что Гарри и Рон уже ушли, да и эта комната слишком мала."
    m "Слишком мала? Сколько же там книг?"
    her "438, не считая брошюр Гарри Томпсона по приручению кракенов."
    m "(Это будет определенно жаркая ночка...)"
    m "Спасибо, не поможешь занести их сюда?"
    $herView.hideshowQQ( "body_10.png", pos )
    her "Но куда мы их..."
    m "Не волнуйся, у меня есть идея, куда их можно поставить..."
    show screen blkfade 
    "..."
    hide screen blkfade
    $herView.hideshowQQ( "body_13.png", pos )
    her "Как я не подумала о том, что у такого волшебника как вы есть волшебный шкаф?"
    g9 "Ну, это скорее волшебный винный погреб. Хотя в него отлично влезает и прочее барахло."
    $herView.hideshowQQ( "body_184.png", pos )
    her "..."
    m "Так или иначе, большое спасибо, вы оказали мне и науке большую услугу!"
    m "А теперь, если позволите, то мне нужно начать исследования."
    $herView.hideshowQQ( "body_14.png", pos )
    her "Но сэр, я ведь помогла вам, верно?"
    $herView.hideshowQQ( "body_13.png", pos )
    her "Да и Гарри с Роном очень старались..."
    m "... и?"
    $herView.hideshowQQ( "body_06.png", pos )
    her "Было бы справедливо наградить Гриффиндор очками факультета, ведь так?"
    m "Хм..."
    menu:
        "Дать 5 очков":
            m "Ладно, ладно..."
            m "Пять очков Гриффиндору!"
            $ gryffindor +=5
            $herView.hideshowQQ( "body_16.png", pos )
            her "Как?! Пять жалких очков?!"
            $herView.hideshowQQ( "body_28.png", pos )
            her "Я потратила два часа своей жизни, работая грузчиком и получила за это пять очков?!"
            $herView.hideshowQQ( "body_110.png", pos )
            her "Скряга!"
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
            $hermi.liking -= 15 #Потом возможно добавить больше?
            m "Тебе хватит тех десяти тысяч, что я вбухал в этот квест."
        "Дать 15 очков":
            m "Хорошо, думаю вы заслужили."
            m "Пятнадцать очков Гриффиндору!"
            $ gryffindor +=15
            $herView.hideshowQQ( "body_01.png", pos )
            her "Спасибо, сэр."
            her "Доброй ночи."
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
        "Дать 100 очков":
            m "Конечно, почему нет?"
            m "Сто очков Гриффиндору!"
            $ gryffindor +=100
            $herView.hideshowQQ( "body_72.png", pos )
            her "Сто очков?!"
            $herView.hideshowQQ( "body_15.png", pos )
            her "Но мы же всего лишь принесли книги..."
            m "Что-то не устраивает? Я всегда могу забрать их назад..."
            $herView.hideshowQQ( "body_75.png", pos )
            her "Нет... Конечно нет!"
            $herView.hideshowQQ( "body_15.png", pos )
            her "Большое спасибо, сэр."
            $herView.hideshowQQ( "body_16.png", pos )
            her "Если вам что-нибудь понадобится, только позовите, Гриффиндор всегда готов помочь!"
            $herView.hideshowQQ( "body_06.png", pos )
            her "Доброй ночи."
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
            show screen bld1
            with d3
            m "Десять тысяч монеток и сто очков факультета..."
            m "Мой бюджет еще долго не оправится от такого."
        "Обойдутся!":
            m "Конечно нет, что за глупости."
            $herView.hideshowQQ( "body_18.png", pos )
            her "Что..?"
            $herView.hideshowQQ( "body_76.png", pos )
            her "Но..."
            m "Ведь вы делали это во благо науки, а не корыстных побуждений, ведь так?"
            m "Именно поэтому я доверил это вам, студентам гордого Гриффиндора!"
            m "Я думал, что вам не нужна награда."
            $herView.hideshowQQ( "body_16.png", pos )
            her "Но ведь система очков была придумана для того, чтобы поощрять учеников за..."
            m "Вы абсолютно правы. Но, судя по вашим словам, я ошибался. Ошибался в вас. Можете забирать свои очки и выметаться из моего кабинета."
            $herView.hideshowQQ( "body_77.png", pos )
            her "..."
            $herView.hideshowQQ( "body_73.png", pos )
            her "..."
            her "{size=-4}Извините...{/size}" #мелким шрифтом
            m "Что, простите?"
            $herView.hideshowQQ( "body_07.png", pos )
            her "Вы... Вы абсолютно правы..."
            $herView.hideshowQQ( "body_01.png", pos )
            her "В погоне за победой, мы начали забывать о кое-чем важном."
            $herView.hideshowQQ( "body_11.png", pos )
            her "Мне нужно подумать об этом..."
            $herView.hideshowQQ( "body_07.png", pos )
            her "Прошу прощения." #Возможно после этого Гермиона перестанет продавать очки обучения? На будущее 
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
            show screen bld1
            with d3
            m "Надеюсь, я не перестарался...?"
            m "Впрочем, какая разница? Моя работа - превращать недоступных девушек в шлюх, а не беспокоиться об их чувствах."
    m "Что ж, пора вызывать Снейпа."
    m "Хм... Интересно, как работает система вызова людей в эту комнату?"
    m "Вроде бы я ничего не делаю, а они..."
    #входит Снейп
    play music "music/Dark Fog.mp3" fadein 1 fadeout 1 
    
    $ renpy.play('sounds/door.mp3') #Sound of a door opening.
    $ snapes_speed = 02.0 #The speed of moving the walking animation across the screen.
    $ walk_xpos=470 #Animation of walking chibi. (From)
    $ walk_xpos2=360 #Coordinates of it's movement. (To)
    show screen snape_walk_01 
    with d3
    pause 1.5
    show screen snape_02 #Snape stands still.
    show screen bld1
    with Dissolve(.3)
    $ tt_xpos=300 #Defines position of the Snape's full length sprite.
    $ tt_ypos=0
    $ s_sprite = "03_hp/10_snape_main/snape_01.png"                                                                            #SNAPE
    show screen snape_main
    with Dissolve(.3)                                                                                                               #SNAPE
    with d3  
    sna "Ты звал, Джинни?"
    m "..."
    m "Как ты это делаешь?"
    hide screen snape_main                                                                                                                   #SNAPE
    with d3                                                                                                                                                  #SNAPE
    $ s_sprite = "03_hp/10_snape_main/snape_05.png"                                                                            #SNAPE
    show screen snape_main                                                                                                                  #SNAPE
    with d3  
    sna "Что ты имеешь в виду?"
    m "Как ты появляешься в этой комнате, стоит мне лишь об этом подумать?"
    sna "Разве твоя волшебная секретарша с помощью заклинания громкоговорения не кричит на всю школу имя того, кого ты хочешь вызвать?"
    m "Хм... Звучит правдоподобно..."
    stop music 
    $ renpy.play('sounds/scratch.wav')
    m "..!"
    m "у меня..."
    m "есть..."
    g4 "{size=+4}ГРЕБАНАЯ СЕКРЕТАРША??!{/size}"
    hide screen snape_main                                                                                                                   #SNAPE
    with d3                                                                                                                                                  #SNAPE
    $ s_sprite = "03_hp/10_snape_main/snape_11.png"                                                                            #SNAPE
    show screen snape_main                                                                                                                  #SNAPE
    with d3  
    sna "Ну, да... А ты не знал?"
    "{size=+4}ОТКУДА?!{/size}"
    "{size=+4}КАК ТЫ МОГ СКРЫТЬ ОТ МЕНЯ ПЕРСОНАЖА ЖЕНСКОГО ПОЛА??!!{/size}"
    "{size=+4}ТАЩИ ЕЕ СЮДА!!!{/size}"
    sna"..."
    "{size=+4}ЧЕГО ВСТАЛ?!! БЫСТРО ВЕДИ ЕЕ СЮДА!!!{/size}"
    sna "..."
    "{size=+4}ТЫ ОГЛОХ?!{/size}"
    sna "..."
    "Хм... Снейп?"
    sna "..."
    m "..."
    sna "..."
    m "Да брось, это не смешно!"
    sna "..."
    g9 "Ладно, мы можем трахнуть ее вместе!"
    sna"..."
    m "Отлично, он завис."
    g4  "Кто занимался оптимизацией и тестингом, а?!"
    "Мистический голос" "Может хватит?" #мистический голос
    "Мистический голос" "Всех уже достали шутки про то, что ты знаешь, что находишься в игре!"
    m "Но.."
    "Мистический голос" "И забудь про секретаршу. По крайней мере пока."#мистический голос
    m "Так ведь..."
    "Мистический голос" "Будешь спорить - твоей секретаршей станет хозяйка борделя из Аграбы." #мистический голос
    "Мистический голос" "И она будет нимфоманкой."
    m  "*сглотнул*"
    g9 "Ладно-ладно, думаю, я могу обойтись и без секретарши..."
    g4 "*вздох* И как можно работать в таких условиях?"
    play music "music/Dark Fog.mp3" fadein 1 fadeout 1
    hide screen snape_main                                                                                                                   #SNAPE
    with d3                                                                                                                                                  #SNAPE
    $ s_sprite = "03_hp/10_snape_main/snape_05.png"                                                                            #SNAPE
    show screen snape_main                                                                                                                  #SNAPE
    with d3  
    sna "Ты что-то сказал, Джинни?" #snape
    m "Кхм, да, я спросил, готова ли настойка?"
    hide screen snape_main                                                                                                                   #SNAPE
    with d3                                                                                                                                                  #SNAPE
    $ s_sprite = "03_hp/10_snape_main/snape_06.png"                                                                            #SNAPE
    show screen snape_main                                                                                                                  #SNAPE
    with d3  
    sna "\"Зелье\", Джинни."
    #Шутки про "зелье" возможно допишу позже
    hide screen snape_main                                                                                                                   #SNAPE
    with d3                                                                                                                                                  #SNAPE
    $ s_sprite = "03_hp/10_snape_main/snape_02.png"                                                                            #SNAPE
    show screen snape_main                                                                                                                  #SNAPE
    with d3  
    sna "Да, я как раз только что закончил его приготовление."
    sna "Ты довольно удачно подгадал момент."
    g4 "{size=-4}Ну и как тут не шутить о разработчиках?{/size}" #мелкий шрифт
    m "Ладно... Тогда приступим?"
    hide screen snape_main                                                                                                                   #SNAPE
    with d3                                                                                                                                                  #SNAPE
    $ s_sprite = "03_hp/10_snape_main/snape_05.png"                                                                            #SNAPE
    show screen snape_main                                                                                                                  #SNAPE
    with d3  
    sna "Конечно, можешь приступать. Вот твое ботанойдное зелье, а мне пора... Почистить котлы... Ботанчик."
    hide screen snape_main
    hide screen bld1
    with d3
    hide screen snape_01_f
    hide screen bld1
    hide screen snape_main
    hide screen snape_02 #Snape stands still. 
    #hide screen genie
    show screen blkfade
    with d3
    $ renpy.play('sounds/07_run.mp3') 
    pause 2
    $ renpy.play('sounds/door.mp3')
    show screen bld1
    g4 "{size=+4}КАК ТЫ МЕНЯ НАЗВАЛ??!!{/size}"
    g4 "Гррр, я ему это припомню..."
    "Новый квест! Отомстить Снейпу."
    m "Надеюсь, эта настойка меня успокоит."
    #желательно-звук открывающийся бутылки
    "*чпок!*"
    g4 "Ух, ну и запашок..."
    m "Сомневаюсь, что после бутылки этого пойла я наутро буду что-нибудь помнить..."
    m "Ну, по крайней мере, эта штука дорогая."
    #звук того, как кто-то пьет :D
    m "Хм... Я ничего не чувствую."
    g4 "Неужели Снейп просто надул меня?"
    m "Да еще и эти шуточки с названием..."
    m "Ладно, думаю, стоит ему шанс..."
    if zyablik_switch == 1:
        m "Начну, пожалуй, с самой большой книги."
        m "Она называется... \"Мифологическая биология для чайников\"."
        "\"Глава 1 - Мантикоры\"..."
        #найти звук удара по клавишам
        g4 "{size=+4}Серьезно?!{/size}"
        m "Тут еще и картинки есть..."
        m "..."
        m "..."
        m "Пошло все к черту."
        "Спустя ночь, наполненную учебой и... Ну, вы знаете чем."
        $ renpy.play('sounds/door.mp3')                                                                                                                                                  #SNAPE
        $ s_sprite = "03_hp/10_snape_main/snape_28.png"                                         # SNAPE
        show screen s_head2                                                                                                                  #SNAPE  
        sna2 "Эй, ну и как там поживает наш..."
        hide screen s_head2                                                                                                                  #SNAPE                                                                                                                                                  #SNAPE
        $ s_sprite = "03_hp/10_snape_main/snape_11.png"                                         # SNAPE
        show screen s_head2
        sna2 "!!!"
        sna2 "{size=+4}КАКОГОЧЕРТАТУТТВОРИТСЯ??!!{/size}"
        hide screen s_head2
        m "{size=-4}О, Снейп, дружище...{/size}" #хорошо бы нарисовать измотанного Джина, но это уже на совести художников
        m "{size=-4}Как у тебя дела, друг?{/size}"
        $ s_sprite = "03_hp/10_snape_main/snape_15.png" 
        sna2"{size=+4}ЭТО Я ТЕБЯ ДОЛЖЕН СПРАШИВАТЬ!!!{/size}"
        hide screen s_head2                                                                                                                   #SNAPE                                                                                                                                                #SNAPE
        $ s_sprite = "03_hp/10_snape_main/snape_16.png"                                                                            #SNAPE
        show screen s_head2                                                                                              #SNAPE
        sna2 "Комната выглядит как будто по ней прошло стадо минотавров в брачный период."
        hide screen s_head2                                                                                                                   #SNAPE                                                                                                                                                #SNAPE
        $ s_sprite = "03_hp/10_snape_main/snape_03.png"                                                                            #SNAPE
        show screen s_head2                                                                                                                  #SNAPE
        sna2 "Только не говори мне, что..."
        m "Не волнуйся, настойка сработала."
        g9 "Я изучил всю школьную программу... Досконально."
        hide screen s_head2                                                                                               #SNAPE                                          #SNAPE
        $ s_sprite = "03_hp/10_snape_main/snape_08.png"                                                                            #SNAPE
        show screen s_head2                                                                                                                  #SNAPE
        sna2 "Тогда, что, черт возьми..."
        hide screen s_head2                                                                                                                   #SNAPE                                                                                                                                                 #SNAPE
        $ s_sprite = "03_hp/10_snape_main/snape_04.png"                                                                            #SNAPE
        show screen s_head2                                                                                                                  #SNAPE
        sna2 "Хотя, забудь. Я определенно не хочу об этом знать."
        hide screen s_head2                                                                                                                  #SNAPE                                                                                                                                                 #SNAPE
        $ s_sprite = "03_hp/10_snape_main/snape_09.png"                                                                            #SNAPE
        show screen s_head2                                                                                                                  #SNAPE
        sna2 "Увидимся позже."
        sna2 "..."
        hide screen s_head2                                                                                                                   #SNAPE                                                                                                                                               #SNAPE
        $ s_sprite = "03_hp/10_snape_main/snape_29.png"                                                                            #SNAPE
        show screen s_head2                                                                                                                 #SNAPE
        sna "И вот еще, приберись тут."
        hide screen s_head2 
        $ s_sprite = "03_hp/10_snape_main/snape_03.png"                                                                            #SNAPE
        show screen s_head2
        sna2 "Я не хочу подскользнуться на... этом и проломить себе череп."
        hide screen s_head2 
        m "Конечно, нет проблем."
        $ renpy.play('sounds/door.mp3')
        m "..."
        m "У меня складывается ощущение, что сюжет развивается в неверном направлении."
        m "Ладно, надо тут прибраться..."
        "Квест выполнен! Джинни получает +50 к интеллекту и возможность обучать Гермиону! (в будущих обновлениях, конечно)"
        "Бонусная награда! Джинни получает странный фетиш!"
        g4 "Неправда! Это было в последний раз!"
    else:
        m "Начну пожалуй с этой странной книжки..."
        stop music
        m "..!"
        # тут должна быть эпичная музыка
        g4 "{size=+4}Я чувствую... МОЩЬ!{/size}"
        "{size=+4}ПОНЕСЛАААААААААААААСЬ!!!!{/size}"
        "{size=+4}GIGA-GINNIE-BREEEEKAAAAAR!!!!!{/size}"
        "{size=+4}Спустя ночь, полную учебы и пафосных выкриков.{/size}"
        $ renpy.play('sounds/door.mp3')                                                                                                                 #SNAPE                                                                                                                                               #SNAPE
        $ s_sprite = "03_hp/10_snape_main/snape_17.png"                                                                            #SNAPE
        show screen s_head2                                                                                                                 #SNAPE
        sna2 "Как поживает наш бо... Трудолюбивый ученик?"
        hide screen s_head2
        m "{size=-4}... Снейп...{/size}" #опять же, пикча уставшего Джинна бы не помешала
        m "{size=-4}... настойка рабочая...{/size}"
        m "{size=-4}... даже слишком.{/size}"
        m "{size=-4}Есть чем-нибудь похмелиться..?{/size}"                                                                                                                   #SNAPE
        $ s_sprite = "03_hp/10_snape_main/snape_03.png"                                                                            #SNAPE
        show screen s_head2  
        sna2 "..."
        $ s_sprite = "03_hp/10_snape_main/snape_17.png"                                                                            #SNAPE
        sna2 "Счастливого дня, Джинни."
        hide screen s_head2                                                                                                                                                #SNAPE
        $ renpy.play('sounds/door.mp3')
        g4 "{size=-4}Вернииииись...{/size}"
        g4 "{size=-4}Предатель...{/size}"
        "Новый квест! Жестоко отомстить Снейпу!"
        m "... паршивец."
        m "По крайней мере, я могу приступить к обучению девчонки..."
        "Квест выполнен! Джинни получает +50 к интеллекту и возможность обучать Гермиону! (в будущих обновлениях, конечно)"
        g4 "Будущие обновления? Значит все это было напрасно?"
        m "... пошло все к черту..."
    if daytime:
        jump night_start
    else: 
        jump day_start



    





