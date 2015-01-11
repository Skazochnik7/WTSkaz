label event_00:
    
    play music "music/Dark Fog.mp3" fadein 1 fadeout 1 
    
    
    #show screen snape_01 #OWL SITTING ON A PACKAGE.
    $ renpy.play('sounds/door.mp3') #Sound of a door opening.
    show screen snape_01 #Snape stands still.
    with Dissolve(.5)
    pause.3
    show screen bld1
    with d3
    g4 "{size=-3}(Коренные формы жизни!?){/size}"
    hide screen bld1
    with d3
    $ tt_xpos=650
    $ tt_ypos=180
    show screen thought 
    with Dissolve(.3)
    pause 1
    show screen bld1
    with d3
    m "{size=-3}(Выглядит как человек...){/size}"
    m "{size=-3}(Может быть, если я буду вести себя тихо, оно уйдет...?){/size}"
    hide screen bld1
    with d3
    hide screen thought 
    with Dissolve(.3)
    
    $ walk_xpos=610 #Animation of walking chibi. (From) 610
    $ walk_xpos2=360 #Coordinates of it's movement. (To) 360
    
    
    
    $ snapes_speed = 04.0 #The speed of moving the walking animation across the screen.
    show screen snape_walk_01 
    pause 4
    show screen snape_02 #Snape stands still.
    pause.5
    show screen bld1
    with Dissolve(.3)
    $ tt_xpos=300 #Defines position of the Snape's full length sprite.
    $ tt_ypos=0
    $ s_sprite = "03_hp/10_snape_main/snape_01.png"
    show screen snape_main
    show screen ctc
    with Dissolve(.3)
    pause
    sna "Альбус...есть минута?"
    hide screen snape_main
    hide screen ctc
    
#    show screen ctc
#    pause
#    pat "I hate to ask but its been bugging me for awhile."
#    pat "What is your Guesstimated time of completion for the game?"
#    pat "No pressure to give an answer if you don't want to."
#    show screen snape_main
#    with d3
#    sna "Mister silvarius..."
#    sna "This is your first strike..."
#    sna "If I hear this question from you again, then it will cost your house 100 points."
    
#    hide screen snape_main
#    with d3
#    show screen emo
#    her "Professor... *gulp!* I-- I can't breathe!"
#    hide screen emo
#    show screen snape_main
#    with d3
#    sna "I will be with you in a moment, мисс Грейнджер..."
#    hide screen snape_main
#    with d3
#    show screen emo
#    her "!!!"
#    hide screen emo
#    show screen snape_main
#    with d3
#    sna "I hope we came to an understanding, here, mister silvarius."
#    sna "Didn't we?"
    

    m "{size=-3}(\"Альбус\"? Это должно быть мое имя или это просто, как люди этого мира приветствуют друг друга?){/size}"
    menu:
        m "..."
        "\"На самом деле я немного занят.\"":
            $ s_sprite = "03_hp/10_snape_main/snape_04.png"
            show screen snape_main
            with d3
            sna "Но ведь не постоянно?"                            
        "\"Конечно. Что там?\"":
            pass                       
        "\"И Альбус тоже.\"":
            $ s_sprite = "03_hp/10_snape_main/snape_05.png"
            show screen snape_main
            with d3
            sna "Что?"
            $ s_sprite = "03_hp/10_snape_main/snape_04.png"
            sna "Альбус, я не в настроении для ваших... издевательств."
        "\"Отведи меня к своему боссу.\"":
            $ s_sprite = "03_hp/10_snape_main/snape_01.png"
            show screen snape_main
            with d3
            sna "Что?"
            hide screen snape_main
            with d3
            $ s_sprite = "03_hp/10_snape_main/snape_01.png"
            show screen snape_main
            with d3
            sna "Хм...?"
            sna "Вы имели в виду министра магии?"
            hide screen snape_main
            with d3
            $ s_sprite = "03_hp/10_snape_main/snape_03.png"
            show screen snape_main
            with d3
            sna "Я хотел бы избежать каких-либо дел с этими бюрократами..."
            m "Ладно, проехали... Как я могу помочь тебе?"
            
    $ s_sprite = "03_hp/10_snape_main/snape_06.png"
    sna "У меня есть важный разговор к вам..."
    sna "Я думаю, нам стоит пересмотреть политику допуска." 
    hide screen snape_main
    with d2
    m "................?"
    $ s_sprite = "03_hp/10_snape_main/snape_03.png"
    show screen snape_main
    with d2
    sna "Половина моих...так называемых \"учеников\" не что иное, как раздражающие личинки, которые портят мне жизнь день ото дня"
    hide screen snape_main
    with d2
    m "................"
    $ s_sprite = "03_hp/10_snape_main/snape_07.png"
    show screen snape_main
    sna "Большинство из них из \"Гриффиндора\", конечно же..." 
    hide screen snape_main
    with d2
    m "......?"
    show screen snape_main
    sna "Несчастные Уизли, шумная Грейнджер и, конечно же, герой всех несовершеннолетних правонарушителей...."
    $ s_sprite = "03_hp/10_snape_main/snape_08.png"
    sna "{size=+3}Мальчишка Поттер!{/size}"
    $ s_sprite = "03_hp/10_snape_main/snape_01.png"
    sna "Запомни мои слова, Альбус. \"Гриффиндор\" станет погибелью для это школы!"
    hide screen snape_main
    m "...................."
    show screen snape_main
    sna "Многие из них не представляют абсолютно ничего!"
    $ s_sprite = "03_hp/10_snape_main/snape_06.png"
    sna "И если этого не достаточно то вот: они распространили разные слухи о преподавателях!"
    sna "В частности и о вашем покорном слуге..."
    hide screen snape_main
    m "......................"
    $ s_sprite = "03_hp/10_snape_main/snape_05.png"
    show screen snape_main
    sna "Вы ведь не верите в эти слухи, так, Альбус?"
    hide screen snape_main
    menu:
        m ".............."
        "\"Ну, нет конечно!\"":
            $ s_sprite = "03_hp/10_snape_main/snape_09.png"
            show screen snape_main
            sna "Хорошо..."
            sna "Вы знаете меня лучше, чем я сам. Меня бы не волновали такие вещи..."
        "\"Не бывает дыма без огня.\"":
            $ s_sprite = "03_hp/10_snape_main/snape_10.png"
            show screen snape_main
            sna "Альбус!? Вы серьезно?!"
            sna "Я вам говорю, это все грязная ложь!"
    hide screen snape_main
    m "........................."
    $ s_sprite = "03_hp/10_snape_main/snape_04.png"
    show screen snape_main
    sna "Ну, эти жалкие дети достали меня сегодня, я думаю, что следует отдохнуть от всего сегодня."
    $ s_sprite = "03_hp/10_snape_main/snape_09.png"
    sna "................"
    
    stop music fadeout 1.0
    
    hide screen snape_main
    hide screen bld1
    with d3
    $ walk_xpos=360 #Animation of walking chibi. (From desk) 360 
    $ walk_xpos2=610 #Coordinates of it's movement. (To the door) 610
    $ snapes_speed = 03.0 #The speed of moving the walking animation across the screen. Default - .03
    show screen snape_walk_01_f 
    pause 3
    $ renpy.play('sounds/door.mp3') #Sound of a door opening.
    hide screen snape_walk_01_f 
    with d4
    pause.5
    show screen bld1
    with d3
    m "Хм..."
    m "И так, этот высокий задумчивый парень принял меня за другого...?"
    m "Следовательно я, по всей вероятности, под действием маскирующего заклинания..."
    m "........."
    m "В свою очерень я джинн, замаскированный под человека, который в свою очередь замаскирован под другого человека..."
    m "Нет, все это очень глупо..."
    a4 "Заткнись! Никто не понимает истинных гениев."
    
#    who2 "Professor Dumbldore, do you have a minute?"
#    m "{size=-3}(What? Another one?){/size}"
#    who2 "Let me speak to him!"
#    m "Excuse me?"
#    who2 "Y-yes master..."
#    who2 "Greetings to you, oh almighty genie..."
#    with hpunch
#    g4 "{size=+7}What the hell?!{/size}"
#    g4 "{size=+7}Stay away from me, you demon!!!{/size}"
#    g4 "{size=+7}Body snatchers are among us!\nI'm outta here!{/size}"
#    m "...wait a second."
#    m "How did you just call me?"
#    who2 "An almighty genie. That is what you are, is it not?"
#    g4 "How did you... Who the hell are you?"
#    who2 "Oh, but of course. Forgive me my poor manners..."
#    who2 "Master's name is Tom Riddle..."
#    who2 "No! You sniveling maggot! we hate that name!"
#    who2 "We want to be called Lord Voldemort!"
#    who2 "Forgive me, master..."
#    m "Эм... mr. Lord- -"
#    with hpunch
#    who2 "No! No! \"lord\" is not master's name, \"lord\" is master's title, you idiot!"
#    who2 "Watch your tone, worm! That is an immortal being before you."
#    who2 "He may look human, but his powers topple mine by far."
#    who2 "Please take no offense, oh almighty one. My servant is quite dim."
#    menu:
#        m "..."
#        "\"Does the sun take offense from an ant?\"":
#            who2 "And yet it is prudent for an ant to know it's place, wouldn't you agree?"
#        "\"Watch it, mortal! I'll smite you!\"":
#            who2 "My humble apologies. The worthless servant shall be punished properly."
#            who2 "M-master...?"
#        "\"Apology accepted. What do you want?\"":
#            who2 "You are unusually forgiving for a genie. But we shall not test your patience anymore..."
            
#    vol "Correct me if we are wrong, but you came to our world due to an accident..."
#    m ".................."
#    vol "And you find our world intriguing, do you not?"
#    m "You have two faces growing out of your head. So yeah, colour me curious."
#    who2 "Splendid..."
#    who2 "In that case we want to make you an offer..."
#    who2 "We...."
#    who2 "We...."
#    m "???"
#    who2 "We are tired... Cover us..."
#    who2 "Of course, master."
#    m "What? What's going on?"
#    vol "My apologies, oh immortal one. My master needs to rest now."
#    vol "We will visit you again soon..."
#    m "..................."
#    g4 "What the....?"
#    m "Ah, hell. May as well stay for one more day..."
    
    $ days_without_an_event = 0
    
    jump day_start




###############################################################################################################################################################

label event_01: #First event in the game. Gennie finds himself at the desk.
    
    
    show screen bld1
    with d3
    m "..................?"
    m "Ваше высочество?"
    m "......................................................."
    g4 "Я сделал это снова?"
    g4 "Телепортировал себя не понятно куда..."
    m "Что с этими ингредиентами?"
    m "Они кажется мощнее, чем я думал."
    m "Ну, не важно что это за место, дел у меня тут нет..."
    m "Лучше обернуть заклинание вспять, иначе принцесса будет снова злиться на меня..."
    m "....................."
    m "Хотя..."
    m "Есть в этом месте что-то странное... это..."
    m "Оно наполненно...."
    g4 "{size=+5}МАГИЕЙ?!{/size}"
    m "Да... магия, я чувствую. Такая мощная и в свою очередь..."
    m "...чужая."
    m "Интересно..."
    m "Я думаю, необходимо осмотреться здесь..."
    hide screen bld1
    with d3
    return
###############################################################################################################################################################
label event_02:
    $ letters += 1 #Adds one letter in waiting list to be read. Displays owl with envelope.
    #$ mail_from_her = True #Comented out because replaced with $ letters += 1 
    play sound "sounds/owl.mp3"  #Quiet...
    show screen owl
    show screen bld1
    with d3
    m "Что? Сова?"
    hide screen bld1
    with d3
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
            who2 " Она одна из \"группировки Поттера\"."
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
    who2 "Да... Я бы с удовольствием отпорол эту девку перед всей школой..."
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
    who2 "Я знаю, что вы так же, бессильны, как и я, но я говорю вам, что этой девке лучше прекратить испытывать мое терпение."
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
            who2 "Иногда мне кажется, что уж лучше оказаться в комнате полной дементоров..."
        "\"Вам лучше отдохнуть сегодня.\"":
            hide screen snape_main                                                                                                                                  #SNAPE
            with d3                                                                                                                                                                  #SNAPE
            $ s_sprite = "03_hp/10_snape_main/snape_06.png"                                                                               #SNAPE
            show screen snape_main                                                                                                                                #SNAPE
            with d3                                                                                                                                                                  #SNAPE
            who2 "Вы как всегда добры..."
    who2 "Хм..."
    hide screen snape_main                                                                                                                                  #SNAPE
    with d3                                                                                                                                                                  #SNAPE
    $ s_sprite = "03_hp/10_snape_main/snape_06.png"                                                                               #SNAPE
    show screen snape_main                                                                                                                                #SNAPE
    with d3                                                                                                                                                                  #SNAPE
    who2 "Может быть мне лучше вздремнуть."
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
    who2 "Она фактически идет под натиском."
    hide screen snape_main                                                                                                                                  #SNAPE
    with d3                                                                                                                                                                  #SNAPE
    $ s_sprite = "03_hp/10_snape_main/snape_05.png"                                                                               #SNAPE
    show screen snape_main                                                                                                                                #SNAPE
    with d3                                                                                                                                                                  #SNAPE
    who2 "Кстати, она не присылала вам какие-либо письма недавно?"
    menu:
        m "..."
        "\"Гермиона Грейнджер? Нет, ничего не было.\"":
            who2 "Понятно... Видимо она блефует."
            hide screen snape_main                                                                                                                                  #SNAPE
            with d3                                                                                                                                                                  #SNAPE
            $ s_sprite = "03_hp/10_snape_main/snape_16.png"                                                                               #SNAPE
            show screen snape_main                                                                                                                                #SNAPE
            with d3                                                                                                                                                                  #SNAPE
            who2 "Что за тупая ведьма."
        "\"Да... Каждый чертов день...\"":
            who2 "Действительно?"
            who2 "Есть что-то обо мне в частности?"
            who2 "Я надеюсь вы знаете меня хорошо и не будете слушать ее..."
    
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
        sna_06 "Кто ты такой, сволочь!"
        g4 "Что? Это я... эм... Абиус! То есть, Альбус!"
        sna_04 "Ты не надуришь меня."
        sna_04 "Только что ты использовал какую-то чужеродную магию!"
        sna_06 "Яви для меня свою истинную сущность, дьявол! Кто ты такой?!"
    else:
        sna_01 "Мое имя Северус Снейп!"
        sna_01 "Теперь твоя очередь...?"
        
    g4 "!!!"
    sna_01 "Полегче... Просто ответь на мой вопрос."
    
    m "Ладно, ладно. Можешь просто успокоиться?..."
    sna_01 "........"
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
            sna_01 "Это первое, что сказал бы враг."
        "\"Я просто турист. Я уже ухожу.\"" if not d_flag_02:
            $ d_flag_02 = True
            $ d_points +=1
            sna_01 "У тебя ничего не выйдет."
        "\"Я работаю на Альбиса Думблдора!\"" if not d_flag_03:
            $ d_flag_03 = True
            $ d_points +=1
            sna_01 "Его зовут Альбус Дамблдор, ты, придурок!"
    if d_points == 2:
        pass
    else:
        jump no_wait

    sna_01 "Кто тебя послал сюда? Что ты сделал с настоящим Альбусом?"
    sna_01 "Покажи свои истинную сущность, последнее предупреждение!"
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
            sna_01 "У меня нет малейшего интереса к твоим объяснениям. Я бы все равно не поверил ни единому слову!"
        "\"Хватит угрожать мне, человек!\"" if not d_flag_02:
            $ d_flag_02 = True
            $ d_points +=1
            sna_01 "\"Человек\"?"
            sna_01 "Ты намекаешь на то, что ты {size=+5}не{/size} один из нас?"
            sna_01 "Что ты такое!? Немедленно отвечай, иначе я применю чары для снятия твоей маскировки!"
        "\"Я не причиню тебе вреда, клянусь!\"" if not d_flag_03:
            $ d_flag_03 = True
            $ d_points +=1
            sna_01 "Точно?"
            sna_01 "Докажи это. Сними свою маскировку немедленно!"

    if d_points == 2:
        pass
    else:
        jump no_wait_2

            
            
    sna_01 "Я услышал достаточно!"
    g4 "Во имя великих песков пустыни! Человек, ты дашь мне объясниться?!"
    sna_01 "Уже нечего объяснять!"
    sna_01 "Пока вы отказываетесь сотрудничать, вы будете под стражей!"
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
    sna_08 "(...н-невероятно...)"
    
    play music "music/Dark Fog.mp3" fadein 1 fadeout 1 
    
    hide ch_gen
    show image "03_hp/04_duel/no_magic.png" at Position(xpos=550, ypos=250, xanchor="center", yanchor="center") 
    
    m "Я сказал, что ты мне не ровня..."
    show screen bld1
    with d3
    m "Хотя, ты оказался неплох..."
    sna_01 "Ты колдовал заклинания голыми руками..."
    sna_01 "Если ты не человек, то... кто-"
    sna_04 "{size=+5}Что ты такое?{/size}"
    sna_01 "Какой-то демон, призванный \"сам знаешь кем\"?"
    m "Призванный кем?"
    sna_02 "\"Сам знаешь кем\"!"
    m "Что?"
    sna_07 "......................"
    m "............................"
    m "Послушай, я не демон..."
    m "И само собой я не работаю на  \"сам не знаю кого\"!"
    sna_01 "............................."
    m "Я был хм..."
    m "...Я проводил эксперимент в своем мире и что-то пошло не так, вот я и здесь."
    m "Это все..."
    sna_01 ".........................."
    sna_01 "Тогда, что же стало с настоящим Альбусом Дамблдором?"
    m "Я уверен, он в порядке."
    m "Он, вероятно, очень удивлен, оказавшись в чужом мире, собственно как и я..."
    sna_01 "...................................."
    sna_01 "Когда это произошло?"
    m "Дня четыре назад..."
    sna_01 "Ты можешь вернуться назад?"
    m "Я думаю, что..."
    sna_02 "Почему ты еще не сделал этого?"
    m "Не уверен..."
    m "В этом мире очень странная магия... Мне просто стало любопытно."
    sna_01 "..................."
    sna_01 "Тебе нужно все исправить..."
    m "Исправить что?"
    sna_04 "Все. Тебе нужно вернуть Альбуса и самому вернуться обратно."
    menu:
        m "..."

        "\"Да, да, знаю. Тогда я пойду.\"":
            m "Да, да, я знаю..."
            m "Ну, тогда я пойду. Извини за все это."
            sna_01 "Хорошо, что никто не пострадал..."
        "\"Но мне нравится здесь! Могу я остаться?\"":
            sna_01 "Категорически нет."
            sna_01 "Кем бы ты не был, ты не из этого мира."
            sna_01 "Твое присутствие здесь сильно нарушает порядок вещей в мире."
            sna_01 "И в эти дни школа нуждается в хорошем директоре, как никогда ранее."
    sna_01 "Безопаснее всего венуться обратно именно сейчас."
    m "Хм ... Спасибо, господин Северус. Удачи с вашими студентами и \"шайкой Поттера\"."
    sna_01 "\"Шайка Поттера\"?"
    sna_07 "Ах, точно, эти пидерасты..."
    menu:
        "- Отменить заклинание -":
            pass
    menu:
        "- Отменить заклинание -":
            pass
    menu:
        "- Отменить заклинание -":
            pass

    sna_01 "Сработало? Это вы, Альбус?"
    menu:
        m "..."
        "\"Да, это Я. Как хорошо вернуться обратно!\"":
            sna_01 "Рад, что вы здесь. Вы в порядке?"
            m "Я в порядке, Северус, спасибо."
            sna_01 "Как там, в другом мире?"
            m "Очень много песка и довольно жарко, но все таки относительно неплохо."
            sna_01 "Понимаю... Вы соскучились по своему брату?"
            menu:
                m "..."
                "\"Да, я соскучился по тебе очень сильно!\"":
                    sna_01 "......................."
                    sna_01 "Да, точно...."
                "\"У меня нет брата, Северус.\"":
                     sna_01 "........................"
                     sna_01 "У вас может и нет, но у настоящего Альбуса Дамблдора он есть."
                "- Использовать магию, для получения правильного ответа -":
                    show screen bld1
                    with d3
                    ">Вы используете свою космическу силу, чтобы заглянуть в саму материю Вселенной и узнать правильный ответ."
                    hide screen bld1
                    with d3
                    m "Мой младший брат Аберфорт? Почему я должен соскучиться по нему?"
                    sna_01 "Я каждый раз чувствую, когда ты используешь свою странную магию..."
        "\"Не-а. Это все еще я. Не человеческий-чувак.\"":
            pass


    sna_01 "Почему ты все еще здесь, существо?"
    m "Я не уверен... Я пытался обратить заклинание, но ничего не вышло..."


    sna_07 "Чудеса..."
    sna_01 "Что это значит? Ты собрался остаться здесь навсегда?"
    m "Конечно нет..."
    m "Я здесь, возможно, только по тому, что заклинание компенсации дисбаланса вызвало само себя..."
    m "Если отменить заклинание, то я должен вернуться обратно в свой мир."
    m "Кроме того, твой друг Дамблдор тоже должен будет вернуться обратно сюда."
    sna_01 "Понимаю..."
    sna_01 "Как долго заклинание будет действовать?"
    menu:
        m "..."
        "\"Пару дней.\"":
            sna_01 "Понятно..."
        "\"Неделя или...\"":
            sna_01 "Хм.... Неделя, хух..."
        "\"Может быть месяцы...\"":
             sna_01 "Так долго?"
             sna_01 "Почему все настолько \"плохо\"?"
        "\"Я понятия не имею...\"":
            sna_01 "....................."
            sna_02 "Великолепно..."

    m "Хорошо, если честно, я не уверен, куда идти теперь..."
    m "Все это время, я думал, что смогу отметить заклинание когда захочу..."
    sna_01 "..................................................."
    sna_01 ".................................."
    sna_01 "..................."
    m "Снейп?"
    sna_01 "..................................................."
    m "Северус?"
    sna_06 "Да, да ..."
    sna_01 "Слушай, уже поздно и очень многое успело произойти..."
    sna_07 "Мне следует обдумать все это."
    sna_01 "Увидимся завтра, я зайду после занятий."
    sna_06 "До тех пор, держи свою истинную личность и наш разговор в тайне, идет?"
    m "Без проблем."
    sna_01 "Отлично, тогда..."
    sna_01 "Но перед тем, как я уйду, один вопрос..."
    m "Я слушаю..."
    sna_02 "........"
    sna_01 "Если ты не человек, тогда..."
    sna_07 "Что ты?"
    m "...Я джинн."
    sna_01 "Джинн?"
    m "Да, я обладаю крутой космической силой и все такое..."
    sna_01 "Серьезно?"
    m "О, да."
    sna_01 "Невероятно..."
    sna_01 "Ну, увидимся завтра.... джинн."
    m "Я буду здесь..."

    sna_07 "(Джинн? Что-то новое...)"
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
    m "Серьезно, я сомневаюсь, что это пойдет мне напользу"
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
    $ hanging_with_snape = True
    
    jump day_start

###############################################################################################################################################################
label event_08: # HERMONE SHOWS UP FOR THE FIRST TIME. IN USE.
    #"EVENT_08"
    stop music fadeout 1.0
    pause 1
    $ renpy.play('sounds/knocking.mp3') #Sound someone knocking on the door.
    "*Тук-тук-тук*"
    m "Хах?"
    $ renpy.play('sounds/knocking.mp3') #Sound someone knocking on the door.
    "*Тук-тук-тук*"
    pause.7
    m "Кто-то стучит в дверь..."
    m "Черт... Я должен избегать любых контактов с людьми!"
    m "Хм... Каковы шансы, что это стучится не человек?"
    m "Ага, достаточно малы..."
    $ renpy.play('sounds/knocking.mp3') #Sound someone knocking on the door.
    "*Тук-тук-тук*"
    m "Настойчивый ублюдок..."
    $ d_flag_01 = False #When False Genie doesn't know Hermione's name.
    $ d_flag_02 = False #When TRUE Genie knows it's a girl knocking on the door.
    menu:
        m "..."
        "\"Кто это?\"":
            $ d_flag_01 = True
            who "Это я, профессор..."
            who "Гермиона Грейнджер. Могу я войти?"
            m "{size=-4}(Это та девка, которая засыпала меня своими письмами...){/size}"
            menu: 
                m "..."
                "\"Уходи, пожалуйста. Я занят.\"":
                    her "Но, профессор, мне действительно нужно поговорить с вами..."
                    m "..........................................."
                    her "Профессор? Я вхожу!"
                    m "{size=-4}(Дерьмо...){/size}"
                "\"Да, да. Конечно входи.\"":
                    pass          
        "\"Входите!\"":
            pass
        "\"Уходи!\"":
            $ d_flag_02 = True #When TRUE Genie knows it's a girl knocking on the door.
            who "Но, профессор, мне действительно нужно поговорить с вами..."
            m "..........................................."
            who "Профессор? Я вхожу!"
            m "{size=-4}(Дерьмо...){/size}"
        "\"................\"":
            $ d_flag_02 = True #When TRUE Genie knows it's a girl knocking on the door.
            who "Профессор, вы здесь?"
            m "{size=-4}(Уходи...){/size}"
            who "Но, профессор, мне действительно нужно поговорить с вами..."
            m "..........................................."
            her "Профессор? Я вхожу!"
            m "{size=-4}(Дерьмо...){/size}"


    $ renpy.play('sounds/door.mp3') #Sound of a door opening.
    $ hermione_chibi_xpos = 610
    $ hermione_chibi_ypos = 250
    show screen hermione_02 #Hermione stands still.
    with Dissolve(.5)
    pause.3
    if not d_flag_01:
        m "?!!"
    if not d_flag_02: #When TRUE Genie knows it's a girl knocking on the door.
        m "{size=-3}(Девочка?){/size}"
        
    play music "music/Chipper Doodle v2.mp3" fadein 1 fadeout 1 
    $ walk_xpos=610 #Animation of walking chibi. (From)
    $ walk_xpos2=400 #Coordinates of it's movement. (To)
    $ hermione_speed = 03.0 #The speed of moving the walking animation across the screen.
    show screen hermione_walk_01 
    pause 3
    $ hermione_chibi_xpos = 400 #Near the desk.
    show screen hermione_02 #Hermione stands still.
    pause.5
    show screen bld1
    with Dissolve(.3)
    
    $ h_xpos=370 #Defines position of the Hermione's full length sprite.
    $ h_ypos=0
    $ h_body = "03_hp/13_hermione_main/body_01.png" #Sprite of Hermione's upper body.
    show screen hermione_main
    show screen hermione_02
    show screen ctc
    with Dissolve(.3)
    pause
    hide screen hermione_main
    with d3
    $ h_body = "03_hp/13_hermione_main/body_03.png" #Sprite of Hermione's upper body.
    show screen hermione_main
    with d3
    her "Доброе утро профессор."
    hide screen ctc
    menu:
        "\"Доброе утро... девочка.\"":
            her "{size=-4}(\"Девочка\"?){/size}"
            pass
        "\"Доброе утро, Гермиона.\"" if d_flag_01:
            pass
        "\"Доброе утро, Дитя.\"":
            her "{size=-4}(\"Дитя\"...?){/size}"
        "\"................................\"":
            pass
    her "Я была очень занята , но сегодня утром у меня есть немного времени, чтобы встретится с вами, профессор."
    her "Вы, наверное, знаете почему я здесь."
    hide screen hermione_main
    with d3
    $ h_body = "03_hp/13_hermione_main/body_04.png" #Sprite of Hermione's upper body.
    show screen hermione_main
    with d3
    her "Тот вопрос, который я безуспешно пыталась довести до вашего внимания в последнее время."
    her "Я не могу понять, почему вы ничего не предпринимаете, чтобы остановить это!"
    her "Это не может больше продолжаться!"
    hide screen hermione_main
    with d3
    $ h_body = "03_hp/13_hermione_main/body_02.png" #Sprite of Hermione's upper body.
    show screen hermione_main
    with d3
    her "Такого рода неравенство начинает сказываться на факультетах..."
    her "Все потому, что мы более сплоченны, нежели остальные..."
    her "Как вы думаете, это справедливо, что те кто заслуживают быть лидерами, отстают от других?"
    her "Как вы думаете? Справедливо?"
    hide screen hermione_main
    with d3
    $ h_body = "03_hp/13_hermione_main/body_03.png" #Sprite of Hermione's upper body.
    show screen hermione_main
    with d3
    m "{size=-4}(Вы только посмотрите на эту миленькую девчушку){/size}"
    m "{size=-4}(Только посмотрите ... Она восхитительна.){/size}"
    m "{size=-4}(Черт, я не видел женщину целую неделю){/size}"
    menu:
        "\"(Подрочить под столом, пока она говорит.)\"":
            $ jerk_off_session = True #Affects next conversation with Snape.
            $ d_flag_01 = True #If TRUE genie jerks off under the desk.    
        "\"(Нет, это глупо! Мне нужно вести себя нормально!)\"":
            $ d_flag_01 = False #NOT JERKING OFF.
            pass
    if d_flag_01:
        hide screen hermione_main
        hide screen bld1
        with d3
        show screen blktone8
        with d3
        ">Вы опустили руки под стол и обхватили свой член..."
        hide screen blktone8
        with d3
        hide screen genie
        show screen genie_jerking_off
        with d3
    m "Да, продолжай, дорогая."
    $ h_body = "03_hp/13_hermione_main/body_05.png" #Sprite of Hermione's upper body.
    show screen hermione_main
    show screen bld1
    with d3
    her "\"Да\"?! То есть это справедливо?"
    m "О, конечно нет, я хотел сказать \"нет\". Но все равно продолжай..."
    hide screen hermione_main
    with d3
    $ h_body = "03_hp/13_hermione_main/body_03.png" #Sprite of Hermione's upper body.
    show screen hermione_main
    with d3
    her "Стало легче на душе. Я рада, что вы согласны со мной, профессор..."
    hide screen hermione_main
    with d3
    $ h_body = "03_hp/13_hermione_main/body_04.png" #Sprite of Hermione's upper body.
    show screen hermione_main
    with d3
    her "Как я уже говорила, это просто смешно, и я не могу поверить, что это происходит сейчас и с нами!"
    if d_flag_01:
        hide screen hermione_main
        hide screen bld1
        show screen blktone8
        with d3
        ">*Фап!* *Фап!* *Фап!*"
        ">Вы продолжаете дрочить свой член..."
        hide screen blktone8
        with d3
        show screen hermione_main
        show screen bld1
        with d3
    else:
        m "Понятно..."
    her "Я хочу сказать, что поняла, если бы это произошло несколько сотен лет назад..."
    her "Но мы давно прошли это, не так ли?"
    if d_flag_01:
        g9 "{size=-4}(Вы только посмотрите на эти розовые щечки? Хочу потыкать в них своим членом.){/size}"
        hide screen hermione_main
        show screen blktone8
        with d3
        ">Вы продолжаете дрочить..."
        hide screen blktone8
        show screen hermione_main
        with d3
    else:
        m "Эм... Я полагаю, что вы сделаете, то есть мы сделаем все, что нужно."
    her "Это навредит системе распределения очков для факультетов."
    her "Но и это не конец!"
    her "Так же это навредит нашей системе образования..."
    her "И что еще более важно - мотивация среди студентов неуклонно сокращается из-за этого!"
    if d_flag_01:
        m "{size=-4}(Посмотрите на эти огромные сиськи.){/size}"
        m "{size=-4}(Да... Я хочу зажать свой член между ними...){/size}"
    her "Как вы можете наблюдать, ситуация весьма тяжелая..."
    hide screen hermione_main
    with d3
    $ h_body = "03_hp/13_hermione_main/body_02.png" #Sprite of Hermione's upper body.
    show screen hermione_main
    with d3
    her "Но мы все еще можем уладить..."
    her "Как сообщил представитель нашего Школьного Студентческого Совета..."
    her "У меня есть пара предложений, как сделать это более эффективно."
    if not d_flag_01:
        m ".............."
    her "Прежде всего, система очков для факультетов должна стать более сложной!"
    hide screen hermione_main
    with d3
    $ h_body = "03_hp/13_hermione_main/body_03.png" #Sprite of Hermione's upper body.
    show screen hermione_main
    with d3
    her "Вам нужно контролировать распределение очков чуть лучше, сэр."
    if d_flag_01:
        g4 "{size=-4}(Да, шлюха... Грязная шлюха... Бьюсь об заклад, ты обожаешь сосать члены... Не так ли? Да, уверен в этом...){/size}"
        hide screen hermione_main
        with d3
        show screen blktone8
        with d4
        ">Вы неистово надрачиваете свой твердейший член!"
        hide screen blktone8 
        with d4
        show screen hermione_main
        with d3
    her "Конечно, вы согласны со мной, профессор, не так ли?"
    if d_flag_01:
        g4 "{size=-4}*Тяжело дыша*{/size}"
        hide screen hermione_main
        with d3
        $ h_body = "03_hp/13_hermione_main/body_07.png" #Sprite of Hermione's upper body.
        show screen hermione_main
        with d3
        her "Профессор...?"
        g4 "{size=-4}(Дерьмо. О чем она только что говорила?){/size}"
        g4 "Да, это так. Продолжай..."
        her "Эм... И так, как я сказала..."
        hide screen hermione_main
        with d3
        m "{size=-4}(Ох... Отлично вздрочнул, но я уже близок к \"великому финалу\".){/size}" 
        m "{size=-4}(Может быть мне стоит прекратить пока не произошло чего.){/size}"
        menu:
            "\"(Да, думаю стоит послушать ее.)\"":
                show screen genie
                with d3
                $ d_flag_01 = False #NOT JERKING OFF ANY MORE.
                pass
            "\"(Нет! Я должен закончить!)\"":
                pass
    else:
        m "{size=-4}(Должен ли Я? Да плевать...){/size}"
        m "Хм... Предпологаю, что должен..."
        her "{size=-4}(\"Пологаете\"?){/size}"
        her "{size=-4}(Почему-то профессор Дамблдор такой... равнодушный.){/size}"
    hide screen hermione_main
    with d3
    $ h_body = "03_hp/13_hermione_main/body_04.png" #Sprite of Hermione's upper body.
    show screen hermione_main
    with d3
    her "Еще одна мера, которую стоит принять это более жестокий контроль за сотрудниками..."
    her "Особенно за учителями..."
    hide screen hermione_main
    with d3
    $ h_body = "03_hp/13_hermione_main/body_03.png" #Sprite of Hermione's upper body.
    show screen hermione_main
    with d3
    her "Я надеюсь, что не переступаю черту, но некоторые учителя действительно требуют надзора..."
    if d_flag_01:
        g4 "{size=-4}(Да! Ты маленькая шлюха! Тупая маленькая шлюха!) *Задыхаясь*{/size}"
    else:
        m "......................."
    hide screen hermione_main
    with d3
    $ h_body = "03_hp/13_hermione_main/body_04.png" #Sprite of Hermione's upper body.
    show screen hermione_main
    with d3
    her "Я понимаю, что у вас нет времени на все это. Вы деректор нашей школы и очень важный и занятой человек."
    her "Временами, оставаться лучшей ученицей довольно трудно для меня..."
    if d_flag_01:
        translators "{size=-4}(Здесь была игра слов \"hard on(тяжело)\" и \"hard-on(стояк)\") которую мы не смогли перевести. \nПростите нас :({/size}"
        g4 "{size=-4}(Она сказала \"стояк\"!?) *задыхаясь*{/size}"
    her "Но вы могли бы предоставить эту задачу мне..."
    her "Просто всадить свою веру в меня." 
    if d_flag_01: 
        hide screen hermione_main
        with d3
        $ h_body = "03_hp/13_hermione_main/body_01.png" #Sprite of Hermione's upper body.
        show screen hermione_main
        with d3
        her "Да, вы должны! Просто всадите ее в меня!"
        stop music fadeout 1.0
        show screen white 
        pause.1
        hide screen white
        pause.2
        show screen white 
        pause .1
        hide screen white
        with hpunch
        g4 "{size=-4}(О дерьмо, что она наделала!) *Аргх!*{/size}"
        hide screen hermione_main
        with d3
        hide screen bld1
        with d3
        show screen genie_jerking_sperm
        with d3
        pause 3
        
        $ h_body = "03_hp/13_hermione_main/body_18.png" #Sprite of Hermione's upper body.
        show screen bld1
        with d3
        show screen hermione_main
        with d3
        her "Профессор!? Что происходит...?"
        show screen genie_jerking_sperm_02
        with d3
        g4 "А... ДААААА.....!"
        her "???"
        g4 "*Тяжело дыша* Да! Да...."
        show screen genie
        #show screen genie_jerking_off
        with d3
        m "Да, девочка. Все именно так, как ты говоришь. Я позабочусь обо всем этом."
    else:
        m "Хорошо, я подумаю о твоем предложении. Обещаю."
    hide screen hermione_main
    with d3
    $ h_body = "03_hp/13_hermione_main/body_07.png" #Sprite of Hermione's upper body.
    show screen hermione_main
    with d3
    her "Правда?"
    her "Хм..........."
    play music "music/Chipper Doodle v2.mp3" fadein 1 fadeout 1 
    hide screen hermione_main
    with d3
    $ h_body = "03_hp/13_hermione_main/body_04.png" #Sprite of Hermione's upper body.
    show screen hermione_main
    with d3
    her "Это обнадеживает. Спасибо, Профессор."
    if d_flag_01:
        m "Нет, нет. Спасибо тебе..."
        hide screen hermione_main
        with d3
        $ h_body = "03_hp/13_hermione_main/body_07.png" #Sprite of Hermione's upper body.
        show screen hermione_main
        with d3
        her "Хм..."
    hide screen hermione_main
    with d3
    $ h_body = "03_hp/13_hermione_main/body_04.png" #Sprite of Hermione's upper body.
    show screen hermione_main
    with d3
    her "Мои занятия вот-вот начнутся. Мне лучше пойти."
    her "Спасибо за уделенное время..."
    hide screen bld1
    hide screen hermione_main
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
    if d_flag_01:
        m "{size=-4}(Это офигительно...) *Задыхаясь*{/size}"
        m "{size=-4}(Мои трусы просто уничтожены...){/size}"
    else:
        m "................."
        m "(Она симпатичная, но довольно трудолюбивая...)"
    hide screen genie_jerking_sperm_02
    with d3
    $ snape_against_hermione = True #Turns True after event_08. Activates special date with Snape # 01.
    $ event08_happened = True
    play music "music/Brittle Rille.mp3" fadein 1 fadeout 1
    return

### FOLLOWING EVENT IS NOT IN USE ANYMORE ###
###############################################################################################################################################################    
label event_08_02:
    "EVENT_08_02"
    $ renpy.play('sounds/knocking.mp3') #Sound someone knocking on the door.
    "*Тук-тук-тук!*"
    menu:
        "\"Кто это?\"":
            her "Это я, Гермиона Грейнджер." 
            m "(Снова эта молоденькая ведьма...)" 
            her "Профессор, я вхожу..."
            m "{size=-4}(Crap!){/size}"
        "\"Да, входи...\"":
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
    
    $ h_xpos=370 #Defines position of the Hermione's full length sprite.
    $ h_ypos=0
    $ h_body = "03_hp/13_hermione_main/body_01.png" #Sprite of Hermione's upper body.
    show screen hermione_main
    show screen hermione_02
    with Dissolve(.3)

    her "Доброе утро, профессор Дамблдор."
    menu:
        "\"Доброе утро, мисс Грейнджер.\"":
            pass
        "\"Доброе утро, дитя.\"":
            her "{size=-5}(\"Дитя\"? Почему он настолько снисходительный все время?){/size}"
            m "Что-то не так?"
            her "Нет, ничего сэр..."
        "\"Доброе утро, шлюха.\"":
            her "Eм... Что?"
            g4 "{size=-4}(ОК, это было глупо. Контролировать гнев, контролировать гнев !){/size}"
            m "*Кхм* Извините, что-то застряло в горле... Доброе утро, мисс Грейнджер."
            her "{size=-5}(Он назвал меня.... нет, показалось.){/size}"
            
    her "Профессор Дамблдор, Я здесь, чтобы поговорить с вами, как  президент \"ОПЗМП\"..."
    m "............."
    her "Мы провели чрезвычайное собрание вчера..."
    her "Главным вопросом была \"Хогвартская\"униформа для девочек..."
    her "Мы пришли к выводу, что в настоящее время дресс-код является весьма нецелесообразным для образовательного учреждения..." 
    show screen ctc
    pause
    her "..."
    m "Серьезно?"
    hide screen ctc
    her "Да, профессор, Уверяю вас, я очень серьезна."
    her "Мы ищем способ заставить наших бедных девочек носить  платье ..."
    her "Сейчас они носят легкомысленные наряды и отвлекает мужчин от учебы, ставя их в невыгодное положение..."
    her "Все это отвлекающие факторы..."
    her "Бедные души..."
    m "Кто-нибудь из ребят жалуется на это?"
    her "Мы не будем ждать, пока проблема существует, сэр! Мы будем бороться с ней!"
    her "Ни один человек не должен находиться в невыгодном положении, в зависимости от пола."
    her "Это называется \"Сексизм\" в мире Маглов, сэр."
    m "Ваши объяснения  слишком запутанные, на мой взгляд, мисс Грейнджер."
    m "Скажите мне, что вы предлагаете , заставить каждую женщину носить паранджу в школе?"
    her "Удвоение длины юбки для девочек в школе было бы достаточно..."
    menu:

        "{size=-4}\"Это смешно. Отказано!\"{/size}":
            $ d_flag_05 = True #Notion refused. Will take affect in the next event.
            her "Что... Н-но? Мы приняли решение..."
            m "Мисс Грейнджер, Мне жаль , но я все еще директор этой школы..."
            m "И все решения  зависят от моего слова!"
            her "Значит вы игнорируете выбор народа, сэр?"
            m "Единственный голос, который я слышу ваш, мисс Грейнджер."
            her "Разве вы не знаете, что происходит с тиранами, которые недооценивают силы народа?"
            her "Их свергают!"
            m "Осторожно. Ваши слова пахнут изменой, юная леди."
            m "Разве вы не знаете, что происходит с предателями?"
            m "Их вешают!"
            her "!!!"
            her "Тцк!"
            her "Я добьюсь,чтобы вы восприняли наше решение всерьез, профессор!"
        
        "{size=-4}\"Нет сексизму. Просьба удовлетворена!\"{/size}":
            her "Великолепно. Я все сделаю."
            her "Спасибо профессор."
            hide screen bld1
            hide screen hermione_main
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
           

    hide screen bld1
    hide screen hermione_main
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
    m "Я начинаю наслаждаться нашими встречами все меньше и меньше..."
    return
#NOT IN USE###############################################################################################################################################################    
label event_08_03:
    "EVENT_08_03"
    $ renpy.play('sounds/knocking.mp3') #Sound someone knocking on the door.
    "*Тук-тук-тук!*"
    m "Кто..."
    her "Профессор, я вхожу..."
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
    her "Доброе утро, профессор Дамблдор."
    show screen bld1
    with Dissolve(.3)
    
    $ h_xpos=370 #Defines position of the Hermione's full length sprite.
    $ h_ypos=0
    $ h_body = "03_hp/13_hermione_main/body_01.png" #Sprite of Hermione's upper body.
    show screen hermione_main
    show screen hermione_02
    with Dissolve(.3)
    
    menu:
        "\"Доброе утро, мисс Грейнджер.\"":
            pass
        "\"Доброе утро, дитя.\"":
            her "{size=-5}(\"Дитя\"? Он должны быть настолько снисходительной все время? Противный старый хер!){/size}"
            m "Что-то не так?"
            her "Ничего сэр..."
        "\"Доброе утро, мисс президент.\"":
            her "{size=-4}(Это звучало как сарказм?){/size}"
            

    if not d_flag_05:
        her "Вы мне обещали принять меры, профессор..."
        her "Но ничего не изменилось с момента нашего последнего разговора..."
        menu:

            "\"Я солгал...\"":
                her "Н-но..."
                her "Но вы директор школы, сэр. Вы слово должно означать что-то..."

            "\"Я забыл\"":
                her "Вы забыли, сэр?"
                her "Вы это серьезно?"
                her "Или, может быть, вы просто не хотите заниматься этим?"
            "\"Меня просто это не волнует.\"":
                her "Н-но....?"
                her "Профессор Дамблдор, это серьезный вопрос!"

    else:
        her "Профессор Дамблдор,вы отвергли предложение которое я дала вам когда мы встречались в прошлый раз..."
        her "И теперь мы пожинаем плоды..."
    her "Ребятам все  еще трудно сосредоточиться на учебе..."
    m "О, у меня есть решение,!"
    m "Давай наденем на головы девушкам бумажные пакеты!"
    her "Это тоже сексизм..."
    her "Другой пример сексизма..."
    her "Это называется \"Женоненавистничество\"."
    m "\"Женоненавистничество\" - это общая неприязнь к женщинам, мисс Грейнджер."
    m "Здоровый мужчина биологически не способен противиться самкам его же вида..."
    m "В противном случае человечество бы вымерло давным-давно..."
    her "Профессор, у нас нет времени для семантики."
    her "Вся школа находится в опасности!"
    m "Неужели..?"
    her "Вчера была встреча \"ОЗМП\", и--"
    m "Нет, опять..."
    m "Существуют ли какие-либо мужские члены в вашем маленьком \"Обществе по защите мужских прав\"?"
    her "Это не относиться к делу"
    m "А я считаю, что относиться..."
    her "Это не имеет значения..."
    m "Как это не имеет значения? {size=+7}Это{/size} единственное, что имеет значение!"
    her "Позвольте мне закончить мое предложение, пожалуйста."
    her "Я официально к вам обращаюсь, как президент \"ОЗМП\"..."
    her "И как представитель этой школы ..."
    her "Мы требуем чтобы эти новые нормы, подлежали соблюдению..."
    her "Во-первых..."
    her "Чтобы ни один школьный учитель не позволял повышать голос в сторону студента или обзывать студента..."
    m "Что?"
    her "Во-вторых..."
    her "Все школьные призраки должны быть заключены только в заброшенной башни в Северном крыле школы."
    m "У Вас есть привидения? Это очень круто!"
    her "В-третьих..."
    her "Каждый учитель, и особенно профессор Северус Снейп должны проходить проверку квалификации каждые три месяца..."
    m "Это все?"
    her "Это все, сэр."
    menu:
        m "..."
        "\"Хорошо. Ваши требования будут удовлетворены.\"":
            her "Спасибо, профессор."
            her "Я, как представитель студентов , благодарю за ваше сотрудничество."
        "\"Звучит как бред. Вы свободны\"":
            her "Что? Я..."
            her "Но это ... вы не можете..."
            m "Свободны!"
            her "Тцк..."       
    hide screen bld1
    hide screen hermione_main
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
    
    $ snape_against_hermione = True #Turns True after event_08_03. Activates event_09 when hanging out with Snape next time.

    
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
                    return
                "\"Конечно. Входи.\"":
                    pass
        "\"Я занят. Приходи позже.\"":
            her "Но..."
            her "Ладно, хорошо..."
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
    
    $ h_xpos=370 #Defines position of the Hermione's full length sprite.
    $ h_ypos=0
    $ h_body = "03_hp/13_hermione_main/body_03.png" #Sprite of Hermione's upper body.
    show screen hermione_main
    show screen hermione_02
    with Dissolve(.3)
    show screen ctc
    pause
    hide screen hermione_main
    with d3
    $ h_body = "03_hp/13_hermione_main/body_04.png" #Sprite of Hermione's upper body.
    show screen hermione_main
    with d3

    her "Доброе утро, профессор Дамблдор."
    hide screen ctc
    menu:

        "\"Доброе утро, дитя.\"":
            hide screen hermione_main
            with d3
            $ h_body = "03_hp/13_hermione_main/body_09.png" #Sprite of Hermione's upper body.
            show screen hermione_main
            with d3
            her "{size=-4}(Опять назвал меня \"дитя\"...){/size}"
            hide screen hermione_main
            with d3
            $ h_body = "03_hp/13_hermione_main/body_04.png" #Sprite of Hermione's upper body.
            show screen hermione_main
            with d3
            her "Сэр, я была бы признательна, если бы вы обращались ко мне как к ровне..."
            m "{size=-4}(Я фактически старше тебя на миллионы лет, ведьма. Мы вообще не можем быть равны.){/size}"
            m "...................."
            hide screen hermione_main
            with d3
            $ h_body = "03_hp/13_hermione_main/body_09.png" #Sprite of Hermione's upper body.
            show screen hermione_main
            with d3
            her "................"
        "\"Доброе утро, мисс Грейнджер.\"":
            her "Эм... так вот, о причине, по которой я к вам зашла..."
        "\"Да, да, пофигу...\"":
            pass
    
    her "Я вижу, что независимо от того, что я делаю - я не могу до вас достучаться, сэр."
    hide screen hermione_main
    with d3
    $ h_body = "03_hp/13_hermione_main/body_04.png" #Sprite of Hermione's upper body.
    show screen hermione_main
    with d3
    her "В следствии вашего пренебрежительного отношения к своим обязанностям, я решила взять все на себя!"
    m "Ты что...?"
    her "Да! Мы, гордые студенты Хогвартса терпеть не можем сексизм..."
    her "Не следует думать, что какой-то пол в чем-то лучше другого."
    m "Но-"
    hide screen hermione_main
    with d3
    $ h_body = "03_hp/13_hermione_main/body_05.png" #Sprite of Hermione's upper body.
    show screen hermione_main
    with d3
    her "Пожалуйста, дайте мне закончить, профессор!"
    hide screen hermione_main
    with d3
    $ h_body = "03_hp/13_hermione_main/body_04.png" #Sprite of Hermione's upper body.
    show screen hermione_main
    with d3
    her "Я организовала \"Организацию по защите мужских прав\" в нашей школе!"
    g4 "Ох, как это типично для вас."
    g4 "Винить во всем-"
    stop music fadeout 1.0
    m "Стоп, ты сказала {size=+5}МУЖСКИХ{/size} прав?"
    hide screen hermione_main
    with d3
    $ h_body = "03_hp/13_hermione_main/body_11.png" #Sprite of Hermione's upper body.
    show screen hermione_main
    with d3
    play music "music/Chipper Doodle v2.mp3" fadein 1 fadeout 1 
    her "Вы понятия не имеете, какого быть мальчиком в нашей школе, особенно в эти дни..."
    menu:
        "\"Сомневаюсь, что это подает надежды...\"":
            hide screen hermione_main
            with d3
            $ h_body = "03_hp/13_hermione_main/body_04.png" #Sprite of Hermione's upper body.
            show screen hermione_main
            with d3
            her "Нет, вы не сделали этого, потому что просто отказываетесь слушать нас, сэр!"
            her "Но теперь вы услышите нас..."
        "{size=-3}\"Эта самая глупая идея, которую я когда-либо слышал.\"{/size}":
            hide screen hermione_main
            with d3
            $ h_body = "03_hp/13_hermione_main/body_07.png" #Sprite of Hermione's upper body.
            show screen hermione_main
            with d3
            her "Я была уверена, что вы скажете что-то вроде этого..."

    hide screen hermione_main
    with d3
    $ h_body = "03_hp/13_hermione_main/body_09.png" #Sprite of Hermione's upper body.
    show screen hermione_main
    with d3
    her "Вы знаете, что девушки оказывают некоторые услуги, чтобы заработать очки для факультета?"
    her "Иногда даже для хороших оценок..."
    m "Правда?"
    hide screen hermione_main
    with d3
    $ h_body = "03_hp/13_hermione_main/body_04.png" #Sprite of Hermione's upper body.
    show screen hermione_main
    with d3
    her "В \"Гриффиндоре\" никто этим не занимается, конечно же..."
    her "И вот, что ставит нас в невыгодное положение - наша честность!"
    her "Что насчет мальчиков - они должны трудиться в десять раз лучше, чем девочки, которым сдать тест не составит труда..."
    her "Или, если они достаточно удачливы, получить какое-то ничтожное одно очко..."
    hide screen hermione_main
    with d3
    $ h_body = "03_hp/13_hermione_main/body_02.png" #Sprite of Hermione's upper body.
    show screen hermione_main
    with d3
    her "Это сексизм в чистом виде!"
    menu:
        m "..."
        "\"Что ты хочешь, чтобы я сделал?\"":
            hide screen hermione_main
            with d3
            $ h_body = "03_hp/13_hermione_main/body_03.png" #Sprite of Hermione's upper body.
            show screen hermione_main
            with d3
            her "Ничего!"
            m "Отлично. Я рад."
        "\"Я не уверен, что ты хочешь мне донести...\"":
            hide screen hermione_main
            with d3
            $ h_body = "03_hp/13_hermione_main/body_03.png" #Sprite of Hermione's upper body.
            show screen hermione_main
            with d3
            her "Вам не нужно больше ничего говорить, профессор."
        "\"Ты смешна!\"":
            hide screen hermione_main
            with d3
            $ h_body = "03_hp/13_hermione_main/body_07.png" #Sprite of Hermione's upper body.
            show screen hermione_main
            with d3
            her "Я? Ну, увидим..."

    hide screen hermione_main
    with d3
    $ h_body = "03_hp/13_hermione_main/body_04.png" #Sprite of Hermione's upper body.
    show screen hermione_main
    with d3
    her "Я уже отправила письмо в министерство магии"
    with hpunch
    g4 "{size=+7}Что ты сделала?!{/size}"
    m "{size=-4}(Стоп, меня действительно это так заботит?){/size}"
    her "Мне очень жаль, но вы мне оставили мне выбора, профессор."

    her "Теперь, прошу простить меня, мне пора на занятия..."
    hide screen bld1
    hide screen hermione_main
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
    

    $ hermione_is_waiting_01 = False #Makes sure this event is not repeated.
    $ snape_against_hermione_02 = True #Turns True after event_09. Activates second event when hanging out with Snape.
    
    play music "music/Brittle Rille.mp3" fadein 1 fadeout 1
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
    
    $ h_xpos=370 #Defines position of the Hermione's full length sprite.
    $ h_ypos=0
    $ h_body = "03_hp/13_hermione_main/body_01.png" #Sprite of Hermione's upper body.
    show screen hermione_main
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
    hide screen hermione_main
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
    
    $ hermione_is_waiting_01 = False #Makes sure this event is not repeated.
    $ snape_against_hermione_02 = True #Turns True after event_09. Activates second event when hanging out with Snape.
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
            m "(Снвоа эта молоденькая ведьма...)" 
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
    
    $ h_xpos=370 #Defines position of the Hermione's full length sprite.
    $ h_ypos=0
    $ h_body = "03_hp/13_hermione_main/body_01.png" #Sprite of Hermione's upper body.
    show screen hermione_main
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
    hide screen hermione_main
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
   
    $ hermione_is_waiting_02 = False #Makes sure this event is not repeated.
    $ days_without_an_event = 0 #Resets the counter. This counts how many days have passed since this event happened.
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
    
    $ robeon = True #Hermione is wearing a robe.
    $ only_upper = True #Otherwise skirt shows up under the robe.
    
    $ h_xpos=370 #Defines position of the Hermione's full length sprite.
    $ h_ypos=0
    $ h_body = "03_hp/13_hermione_main/body_09.png" #Sprite of Hermione's upper body.
    show screen hermione_main
    show screen ctc
    with Dissolve(.3)   
    pause

    hide screen hermione_main
    with d3
    $ h_body = "03_hp/13_hermione_main/body_12.png" #Sprite of Hermione's upper body.
    show screen hermione_main
    with d3
    her "Добрый вечер, профессор."
    hide screen ctc
    menu:
        "\"- Взгляд полный ненависти -\"":
            hide screen hermione_main
            with d3
            $ h_body = "03_hp/13_hermione_main/body_07.png" #Sprite of Hermione's upper body.
            show screen hermione_main
            with d3
            her "Можете смотреть на меня как угодно, сэр."
            her "Это не поможет решить проблемы школы."
        "*Раздражительный вздох*":
            hide screen hermione_main
            with d3
            $ h_body = "03_hp/13_hermione_main/body_03.png" #Sprite of Hermione's upper body.
            show screen hermione_main
            with d3
            her "Не вовремя?"
            hide screen hermione_main
            with d3
            $ h_body = "03_hp/13_hermione_main/body_02.png" #Sprite of Hermione's upper body.
            show screen hermione_main
            with d3
            her "Ну, я уже здесь..."
        "\"....................................\"":
            hide screen hermione_main
            with d3
            $ h_body = "03_hp/13_hermione_main/body_02.png" #Sprite of Hermione's upper body.
            show screen hermione_main
            with d3
            her "Профессор?"
            m "Да, да..."
    hide screen hermione_main
    with d3
    $ h_body = "03_hp/13_hermione_main/body_04.png" #Sprite of Hermione's upper body.
    show screen hermione_main
    with d3
    her "Что-то...странное произошло сегодня..."
    hide screen hermione_main
    with d3
    $ h_body = "03_hp/13_hermione_main/body_07.png" #Sprite of Hermione's upper body.
    show screen hermione_main
    with d3
    her "Я не знаю, как это объяснить..."
    hide screen hermione_main
    with d3
    $ h_body = "03_hp/13_hermione_main/body_09.png" #Sprite of Hermione's upper body.
    show screen hermione_main
    with d3
    her "................................"
    hide screen hermione_main
    with d3
    $ h_body = "03_hp/13_hermione_main/body_12.png" #Sprite of Hermione's upper body.
    show screen hermione_main
    with d3
    her "Я почти провалила тест..."
    menu:
        "\"Такое бывает со студентами.\"":
            hide screen hermione_main
            with d3
            $ h_body = "03_hp/13_hermione_main/body_12.png" #Sprite of Hermione's upper body.
            show screen hermione_main
            with d3
            her "С другими студентами. Но не со мной, сэр!"
            hide screen hermione_main
            with d3
            $ h_body = "03_hp/13_hermione_main/body_13.png" #Sprite of Hermione's upper body.
            show screen hermione_main
            with d3
            her "Я никогда..."
        "\"(Прекращай, Снейп!)\"":
            hide screen hermione_main
            with d3
            $ h_body = "03_hp/13_hermione_main/body_03.png" #Sprite of Hermione's upper body.
            show screen hermione_main
            with d3
            her "Простите?"
            m "Что?"
            m "Ох, Я сказал, что это очень плохо. Как ты себя чувствуешь?"
            hide screen hermione_main
            with d3
            $ h_body = "03_hp/13_hermione_main/body_07.png" #Sprite of Hermione's upper body.
            show screen hermione_main
            with d3
            her "................."
        "\"Расскажи мне почему?\"":
            her "Потому что... это не обычный тест!"

    her "Я не уверена, что происходит..."
    m "Все зло настроено против вас, мисс Грейнджер?"
    hide screen hermione_main
    with d3
    $ h_body = "03_hp/13_hermione_main/body_03.png" #Sprite of Hermione's upper body.
    show screen hermione_main
    with d3
    her "Это не смешно, сэр."
    hide screen hermione_main
    with d3
    $ h_body = "03_hp/13_hermione_main/body_04.png" #Sprite of Hermione's upper body.
    show screen hermione_main
    with d3
    her "Вы должны считать меня \"мерилом\" нашей системы образования."
    her "Если я \"почти\" провалила тест, вероятно остальные вообще не сдали его."
    m "И...?"
    hide screen hermione_main
    with d3
    $ h_body = "03_hp/13_hermione_main/body_07.png" #Sprite of Hermione's upper body.
    show screen hermione_main
    with d3
    her "Да, профессор. Сегодня что-то пошло не так..."
    hide screen hermione_main
    with d3
    $ h_body = "03_hp/13_hermione_main/body_12.png" #Sprite of Hermione's upper body.
    show screen hermione_main
    with d3
    her "................................."
    hide screen hermione_main
    with d3
    $ h_body = "03_hp/13_hermione_main/body_11.png" #Sprite of Hermione's upper body.
    show screen hermione_main
    with d3
    her "Но что, если это не так?"
    her "Что, если отныне все тесты будут такие сложные?"
    hide screen hermione_main
    with d3
    $ h_body = "03_hp/13_hermione_main/body_10.png" #Sprite of Hermione's upper body.
    show screen hermione_main
    with d3
    her "Мне нужно лучше заниматься!"
    label cant_say:
    menu:
        "\"Я могу обучать вас, мисс Грейнджер.\"":
            hide screen hermione_main
            with d3
            $ h_body = "03_hp/13_hermione_main/body_14.png" #Sprite of Hermione's upper body.
            show screen hermione_main
            with d3
            her "Вы?"
            hide screen hermione_main
            with d3
            $ h_body = "03_hp/13_hermione_main/body_15.png" #Sprite of Hermione's upper body.
            show screen hermione_main
            with d3
            her "О, благодарю вас за предложение, но не думаю, что в этом есть необходимость, сэр."
            hide screen hermione_main
            with d3
            $ h_body = "03_hp/13_hermione_main/body_16.png" #Sprite of Hermione's upper body.
            show screen hermione_main
            with d3
            her "Лучший репетитор это книга и вся библиотека Хогвартса в моем распоряжении."
        "\"Мудрое решение, мисс Грейнджер.\"":
            hide screen hermione_main
            with d3
            $ h_body = "03_hp/13_hermione_main/body_15.png" #Sprite of Hermione's upper body.
            show screen hermione_main
            with d3
            her "Спасибо, профессор."
        "\"Тебе нужно взять мой член в свой ротик.\"":
            m "Тебе нужно взять мой чле-"
            hide screen hermione_main
            with d3
            $ h_body = "03_hp/13_hermione_main/body_15.png" #Sprite of Hermione's upper body.
            show screen hermione_main
            with d3
            her "А?"
            m "{size=-4}(Нет, я не могу этого сказать...){/size}"
            hide screen hermione_main
            with d3
            $ h_body = "03_hp/13_hermione_main/body_17.png" #Sprite of Hermione's upper body.
            show screen hermione_main
            with d3
            her "......?"
            jump cant_say
    m "............"
    hide screen hermione_main
    with d3
    $ h_body = "03_hp/13_hermione_main/body_16.png" #Sprite of Hermione's upper body.
    show screen hermione_main
    with d3
    her "Ну, если это все, то мне стоит скорректировать свое расписание."
    m "Как пожелаете..."
    
    hide screen bld1
    hide screen hermione_main
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
    
    $ robeon = False #Hermione is NOT wearing a robe.
    $ only_upper = False #Otherwise skirt shows up under the robe.
    
    $ event11_happened = True #Allows next event to start.
    $ days_without_an_event = 0 #Resets the counter. This counts how many days have passed since this event happened.
    
    play music "music/Music for Manatees.mp3" fadein 1 fadeout 1

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
    $ h_xpos=370 #Defines position of the Hermione's full length sprite.
    $ h_ypos=0
    hide screen hermione_main
    with d3
    $ h_body = "03_hp/13_hermione_main/body_11.png" #Sprite of Hermione's upper body.
    show screen hermione_main
    with d3 

    her "Профессор, сегодня что-то пошло не так!"
    her "Сегодня я завалила тест..."
    her "Не могу поверить, что это произошло!"
    hide screen hermione_main
    with d3
    $ h_body = "03_hp/13_hermione_main/body_18.png" #Sprite of Hermione's upper body.
    show screen hermione_main
    with d3 
    her "Как это вообще возможно?!"
    menu:
        "\"Тебе стоит лучше учиться, девочка!\"":
            hide screen hermione_main
            with d3
            $ h_body = "03_hp/13_hermione_main/body_19.png" #Sprite of Hermione's upper body.
            show screen hermione_main
            with d3 
            her "Но я занималась всю ночь!"
        "\"Ну же... Все в порядке.\"":
            hide screen hermione_main
            with d3
            $ h_body = "03_hp/13_hermione_main/body_20.png" #Sprite of Hermione's upper body.
            show screen hermione_main
            with d3 
            her "Нет! Это катастрофа!" 

    hide screen hermione_main
    with d3
    $ h_body = "03_hp/13_hermione_main/body_21.png" #Sprite of Hermione's upper body.
    show screen hermione_main
    with d3 
    her "И хуже того, мне кажется, что я единственная кто его завалила..."
    hide screen hermione_main
    with d3
    $ h_body = "03_hp/13_hermione_main/body_22.png" #Sprite of Hermione's upper body.
    show screen hermione_main
    with d3 
    her "На кого я теперь похожа?"
    hide screen hermione_main
    with d3
    $ h_body = "03_hp/13_hermione_main/body_23.png" #Sprite of Hermione's upper body.
    show screen hermione_main
    with d3 
    her "Нужно узнать результаты, но..."
    hide screen hermione_main
    with d3
    $ h_body = "03_hp/13_hermione_main/body_13.png" #Sprite of Hermione's upper body.
    show screen hermione_main
    with d3 
    her "Да, я уверена, что кто-нибудь еще завалил его..."
    hide screen hermione_main
    with d3
    $ h_body = "03_hp/13_hermione_main/body_11.png" #Sprite of Hermione's upper body.
    show screen hermione_main
    with d3 
    her "Я имею в виду, как без этого, верно?"
    hide screen hermione_main
    with d3
    $ h_body = "03_hp/13_hermione_main/body_13.png" #Sprite of Hermione's upper body.
    show screen hermione_main
    with d3 
    her "....................."
    hide screen hermione_main
    with d3
    $ h_body = "03_hp/13_hermione_main/body_11.png" #Sprite of Hermione's upper body.
    show screen hermione_main
    with d3 
    her "....верно?"
    menu:
        "{size=-3}\"Конечно. В конце концов вы лучший ученик.\"{/size}":
            hide screen hermione_main
            with d3
            $ h_body = "03_hp/13_hermione_main/body_09.png" #Sprite of Hermione's upper body.
            show screen hermione_main
            with d3 
            her "Именно..."
            her "Или по крайней мере была им, до сегодняшнего дня..."
            hide screen hermione_main
            with d3
            $ h_body = "03_hp/13_hermione_main/body_20.png" #Sprite of Hermione's upper body.
            show screen hermione_main
            with d3 
            her "Не могу поверить, что это произошло!"
        "{size=-3}\"Вы можете стать лучше, если я буду вас обучать.\"{/size}":
            $ tutoring_offer_made = True #Affects conversation in the next event.
            hide screen hermione_main
            with d3
            $ h_body = "03_hp/13_hermione_main/body_17.png" #Sprite of Hermione's upper body.
            show screen hermione_main
            with d3 
            her "Хм..."
            hide screen hermione_main
            with d3
            $ h_body = "03_hp/13_hermione_main/body_13.png" #Sprite of Hermione's upper body.
            show screen hermione_main
            with d3 
            her "Да, это может помочь мне, я полагаю..."
            hide screen hermione_main
            with d3
            $ h_body = "03_hp/13_hermione_main/body_14.png" #Sprite of Hermione's upper body.
            show screen hermione_main
            with d3 
            her "Я благодарна вам за предложение, но..."
            her "Могу я подумать над этим?"
            m "Только не затягивай..."
        "{size=-3}\"Я думаю, что мы скоро все узнаем.\"{/size}":
            hide screen hermione_main
            with d3
            $ h_body = "03_hp/13_hermione_main/body_15.png" #Sprite of Hermione's upper body.
            show screen hermione_main
            with d3 
            her "Да, думаю так..."

    hide screen hermione_main
    with d3
    $ h_body = "03_hp/13_hermione_main/body_24.png" #Sprite of Hermione's upper body.
    show screen hermione_main
    with d3 
    her "Извините, профессор, возможно я была чересчур эмоциональна..."
    hide screen hermione_main
    with d3
    $ h_body = "03_hp/13_hermione_main/body_14.png" #Sprite of Hermione's upper body.
    show screen hermione_main
    with d3 
    her "Но вы должны понимать, что на кону моя репутация!"
    hide screen hermione_main
    with d3
    $ h_body = "03_hp/13_hermione_main/body_12.png" #Sprite of Hermione's upper body.
    show screen hermione_main
    with d3 
    her "Что-то должно быть не так с этим тестом..."
    her "И несмотря на то, что мне не удалось его сдать, скорее всего у меня больше всех баллов..."
    her "Как обычно..."
    hide screen hermione_main
    with d3
    $ h_body = "03_hp/13_hermione_main/body_04.png" #Sprite of Hermione's upper body.
    show screen hermione_main
    with d3 
    

    her "Ну, мне лучше пойти. У нас еще одно \"ОЗМП\" собрание сегодня."
    her "Я дам вам знать о новых идеях."
    m "Не могу дождаться..."



    hide screen bld1
    hide screen hermione_main
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
    
    call day_start


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
    hide screen hermione_main
    with d3
    $ h_body = "03_hp/13_hermione_main/body_26.png" #Sprite of Hermione's upper body.
    show screen hermione_main
    with d3 
    show screen ctc
    pause
    her "А?"
    hide screen ctc
    her "О, я уже здесь?"
    her "Извините, сэр... Я..."
    her ".................."
    her "Кажется я..."
    her "Кажется... ух..."
    her "... Я все таки завалила тест."
    her "Я..."
    hide screen hermione_main
    with d3
    $ h_body = "03_hp/13_hermione_main/body_27.png" #Sprite of Hermione's upper body.
    show screen hermione_main
    with d3 
    her "Извините, профессор..."
    her "Я не знаю, почему я пришла к вам..."
    her "Я думаю лучше мне уйти..."
    m "..................."
    hide screen bld1
    hide screen hermione_main
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
    
    call day_start



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
    $ h_xpos=370 #Defines position of the Hermione's full length sprite.
    $ h_ypos=0
    $ h_body = "03_hp/13_hermione_main/body_01.png" #Sprite of Hermione's upper body.
    show screen hermione_main
    show screen hermione_02
    with Dissolve(.3)   

    her "Доброе утро, Профессор."
    m "Я могу чем-то вам помочь, Мисс Грейнджер?"
    hide screen hermione_main
    with d3
    $ h_body = "03_hp/13_hermione_main/body_04.png" #Sprite of Hermione's upper body.
    show screen hermione_main
    with d3 
    her "Ну, прежде всего я хотела бы извиниться за вчерашнее..."
    hide screen hermione_main
    with d3
    $ h_body = "03_hp/13_hermione_main/body_08.png" #Sprite of Hermione's upper body.
    show screen hermione_main
    with d3 
    her "Я никогда не заваливала тесты и поэтому не знала, как реагировать..."
    hide screen hermione_main
    with d3
    $ h_body = "03_hp/13_hermione_main/body_04.png" #Sprite of Hermione's upper body.
    show screen hermione_main
    with d3 
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
                        hide screen hermione_main
                        with d3
                        $ h_body = "03_hp/13_hermione_main/body_14.png" #Sprite of Hermione's upper body.
                        show screen hermione_main
                        with d3     
                        her "Уже..."
                        her "Поздно, сэр?"
                        her "Н-но...."
                        hide screen hermione_main
                        with d3
                        $ h_body = "03_hp/13_hermione_main/body_11.png" #Sprite of Hermione's upper body.
                        show screen hermione_main
                        with d3     
                        her "Но мне нужны уроки, а вы умнейший волшебник, которого я знаю..."
                        hide screen hermione_main
                        with d3
                        $ h_body = "03_hp/13_hermione_main/body_28.png" #Sprite of Hermione's upper body.
                        show screen hermione_main
                        with d3     
                        her "Пожалуйста, сэр, мне очень нужна ваша помощь."
                        menu:
                            "\"Покажи мне свои сиськи и мы договорились!\"":
                                hide screen hermione_main
                                with d3
                                $ h_body = "03_hp/13_hermione_main/body_18.png" #Sprite of Hermione's upper body.
                                show screen hermione_main
                                with d3     
                                her "М-мои...?"
                                hide screen hermione_main
                                with d3
                                $ h_body = "03_hp/13_hermione_main/body_29.png" #Sprite of Hermione's upper body.
                                show screen hermione_main
                                with d3     
                                her "............"
                                her "....."
                                hide screen hermione_main
                                with d3
                                $ h_body = "03_hp/13_hermione_main/body_30.png" #Sprite of Hermione's upper body.
                                show screen hermione_main
                                with d3     
                                with hpunch
                                her "{size=+5}Профессор Дамблдор!!!{/size}"
                                m "{size=-5}(Ну, я хотя бы попытался...){/size}"
                                her "Я вам не \"Слизеринская\" шлюха!"
                                m "Конечно нет, мисс Грейнджер."
                                m "Это испытание... Ты прошла его. Хорошая работа."
                                hide screen hermione_main
                                with d3
                                $ h_body = "03_hp/13_hermione_main/body_31.png" #Sprite of Hermione's upper body.
                                show screen hermione_main
                                with d3  
                                her "Что...?"
                                hide screen hermione_main
                                with d3
                                $ h_body = "03_hp/13_hermione_main/body_24.png" #Sprite of Hermione's upper body.
                                show screen hermione_main
                                with d3  
                                her "О, конечно. Я иногда туплю. Простите за крик, сэр."
                                m "Мое предложение в силе, если хотите, чтобы я вас обучал - я займусь этим."
                                hide screen hermione_main
                                with d3
                                $ h_body = "03_hp/13_hermione_main/body_29.png" #Sprite of Hermione's upper body.
                                show screen hermione_main
                                with d3  
                                her ".............."
                            "\"Ну, ладно, отлично...\"":
                                pass
                    "\"Ох, Отлично. Превосходно.\"":
                        pass

            "\"Чудно! Начнем сегодня?\"":
                pass
    else:
        hide screen hermione_main
        with d3
        $ h_body = "03_hp/13_hermione_main/body_07.png" #Sprite of Hermione's upper body.
        show screen hermione_main
        with d3 
        her "Я... эм..."
        her "Сэр Дамблдор, я надеюсь, что не слишком многого прошу..."
        m "Да?"
        her "Эм... было бы неплохо, если..."
        her "..............."
        hide screen hermione_main
        with d3
        $ h_body = "03_hp/13_hermione_main/body_09.png" #Sprite of Hermione's upper body.
        show screen hermione_main
        with d3 
        her "Вы могли бы немного обучить меня, сэр?"
        menu:
            "\"Я уверен, что это возможно.\"":
                pass
            "\"Хм... Я несколько занят.\"":
                hide screen hermione_main
                with d3
                $ h_body = "03_hp/13_hermione_main/body_11.png" #Sprite of Hermione's upper body.
                show screen hermione_main
                with d3 
                her "Сэр, пожалуйста, вы лучший волшебник, которого я знаю!"
                m "{size=-4}(Ты и представить себе не можешь, маленькая ведьма){/size}"
                m "Я думаю, можно устроить, да..."
    hide screen hermione_main
    with d3
    $ h_body = "03_hp/13_hermione_main/body_01.png" #Sprite of Hermione's upper body.
    show screen hermione_main
    with d3 
    her "Благодарю, сэр. Я очень признательна вам."
    hide screen hermione_main
    with d3
    $ h_body = "03_hp/13_hermione_main/body_16.png" #Sprite of Hermione's upper body.
    show screen hermione_main
    with d3     

    her "Просто скажите мне и я принесу свои книжки."

    hide screen hermione_main
    with d3
    $ h_body = "03_hp/13_hermione_main/body_09.png" #Sprite of Hermione's upper body.
    show screen hermione_main
    with d3     
    her "Теперь я должна учиться еще более усердно..."
    hide screen hermione_main
    with d3
    $ h_body = "03_hp/13_hermione_main/body_06.png" #Sprite of Hermione's upper body.
    show screen hermione_main
    with d3     
    her "И я буду брать частные уроки у вас как можно чаще, сэр."
    hide screen hermione_main
    with d3
    $ h_body = "03_hp/13_hermione_main/body_07.png" #Sprite of Hermione's upper body.
    show screen hermione_main
    with d3     
    her "Но это не все..."
    her "В \"ОЗМП\" мы исседуем нашу систему образования более детально..."
    her "Я думаю, кто-то играет не совсем честно..."
    m "Не может быть!"
    her "У меня есть список подозреваемых, я принесу его позже...."
    m "Эм... ладно..."
    hide screen hermione_main
    with d3
    $ h_body = "03_hp/13_hermione_main/body_10.png" #Sprite of Hermione's upper body.
    show screen hermione_main
    with d3     
    her "О, занятия уже начинаются. Мне лучше пойти..."
    
    hide screen bld1
    hide screen hermione_main
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
    $ summoning_hermione_unlocked = True #Unlocks after event_14. Adds "Summon Hermione" button to the door.
    $ hermione_takes_classes = True
    $ tutoring_hermione_unlocked = True
    $ days_without_an_event = 0 #Resets the counter. This counts how many days have passed since this event happened.
    
    
    play music "music/Brittle Rille.mp3" fadein 1 fadeout 1

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
            m "(Снвоа эта молоденькая ведьма...)" 
            her "Могу я войти, сэр?"
            menu:
                m "..."
                "\"Категорически нет! Я занят! Возвращайся позднее!\"":
                    her "Но..."
                    her "Ладно... Тогда я вернусь позднее..."
                    return
                "\"Конечно, входи.\"":
                    pass
        "\"Я занят. Приходи позже.\"":
            her "Но..."
            her "Ну, ладно..."
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
    
    $ h_xpos=370 #Defines position of the Hermione's full length sprite.
    $ h_ypos=0
    $ h_body = "03_hp/13_hermione_main/body_13.png" #Sprite of Hermione's upper body.
    show screen hermione_main
    show screen hermione_02
    with Dissolve(.3)
    her "Добрый вечер, профессор..."
    her "........................"
    hide screen hermione_main
    with d3
    $ h_body = "03_hp/13_hermione_main/body_29.png" #Sprite of Hermione's upper body.
    show screen hermione_main
    with d3   
    her "........................"
    her "........................"
    hide screen hermione_main
    with d3
    $ h_body = "03_hp/13_hermione_main/body_31.png" #Sprite of Hermione's upper body.
    show screen hermione_main
    with d3   
    her "Эм......"
    hide screen hermione_main
    with d3
    $ h_body = "03_hp/13_hermione_main/body_29.png" #Sprite of Hermione's upper body.
    show screen hermione_main
    with d3  
    her "................."
    m "Что такое, Мисс Грейнджер?"
    hide screen hermione_main
    with d3
    $ h_body = "03_hp/13_hermione_main/body_31.png" #Sprite of Hermione's upper body.
    show screen hermione_main
    with d3   
    her "Ну, Эм..."
    her "Понимаете ли... \"Гриффиндор\" больше не лидирует..."
    hide screen hermione_main
    with d3
    $ h_body = "03_hp/13_hermione_main/body_29.png" #Sprite of Hermione's upper body.
    show screen hermione_main
    with d3   
    her "И... все очень трудятся..."
    her "И они надеятся на мою помощь, но я не знаю что делать..."
    m "............................"
    her "Профессор Дамблдор...."
    hide screen hermione_main
    with d3
    $ h_body = "03_hp/13_hermione_main/body_32.png" #Sprite of Hermione's upper body.
    show screen hermione_main
    with d3   
    stop music fadeout 2.0
    her "Я хочу купить очки для факультета за мои услуги!"
    hide screen hermione_main
    with d3
    $ h_body = "03_hp/13_hermione_main/body_33.png" #Sprite of Hermione's upper body.
    show screen hermione_main
    with d3   
    menu:
        "\"Ты имеешь в виду сексуальные услуги?\"":
            hide screen hermione_main
            with d3
            $ h_body = "03_hp/13_hermione_main/body_34.png" #Sprite of Hermione's upper body.
            show screen hermione_main
            with d3   
            her "Эм... Я не уверена..."
            her "Те, которые дадут нашему факультету дополнительные очки..."
            hide screen hermione_main
            with d3
            $ h_body = "03_hp/13_hermione_main/body_31.png" #Sprite of Hermione's upper body.
            show screen hermione_main
            with d3   
            her "Я бы могла написать эссе вам или..."
            hide screen hermione_main
            with d3
            $ h_body = "03_hp/13_hermione_main/body_34.png" #Sprite of Hermione's upper body.
            show screen hermione_main
            with d3   
            her "Или может быть почистить вашу башню..?"
            m "{size=-4}(Почистить мою башню? Хех... Эта вероятно грязная шуточка или вроде того...){/size}"
            m "Ну, хорошо. Мы что-нибудь придумаем."
        "\"Ну, если вы настаиваете...\"":
            pass
        "\"Я так не думаю, мисс Грейнджер.\"":
            hide screen hermione_main
            with d3
            $ h_body = "03_hp/13_hermione_main/body_31.png" #Sprite of Hermione's upper body.
            show screen hermione_main
            with d3   
            her "Н-но... Нам нужны очки..."
            her "Профессор, пожалуйста, я в безвыходном положении..."
            m "В безвыходном, вы говорите..?"
            m "Ну, ладно..."
    hide screen hermione_main
    with d3
    $ h_body = "03_hp/13_hermione_main/body_01.png" #Sprite of Hermione's upper body.
    show screen hermione_main
    with d3   
    play music "music/Chipper Doodle v2.mp3" fadein 1 fadeout 1 
    her "Спасибо, профессор..."
    label choose_favor_agagin:
    $ d_flag_01 = False
    $ d_flag_02 = False
    $ d_flag_03 = False
    $ d_flag_04 = False
    her "И так...Что вы хотите?"
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

    
    

    her "Эм, ладно..."
    if d_flag_01: #Show me your tongue.
        hide screen hermione_main
        with d3
        $ h_body = "03_hp/13_hermione_main/body_24.png" #Sprite of Hermione's upper body.
        $ h_xpos=140 #Defines position of the Hermione's full length sprite. (Default 370).
        show screen hermione_main
        with d3
        her "М-мой... язык, сэр?"
        m "Да, девочка, открой свой рот и покажи мне свой язычок."
        hide screen hermione_main
        with d3
        $ h_body = "03_hp/13_hermione_main/body_12.png" #Sprite of Hermione's upper body.
        show screen hermione_main
        with d3
        her "{size=-7}(Что за извращенец...){/size}"
        hide screen hermione_main
        with d3
        $ h_body = "03_hp/13_hermione_main/body_07.png" #Sprite of Hermione's upper body.
        $ h_xpos=140 #Defines position of the Hermione's full length sprite. (Default 370).
        show screen hermione_main
        with d3
        her "Эм...ну, ладно тогда..."
        hide screen hermione_main
        with d3
        $ h_body = "03_hp/13_hermione_main/body_08.png" #Sprite of Hermione's upper body.
        $ h_xpos=140 #Defines position of the Hermione's full length sprite. (Default 370).
        show screen hermione_main
        with d3
        her "Вот..."
        hide screen hermione_main
        with d3
        $ h_body = "03_hp/13_hermione_main/body_35.png" #Sprite of Hermione's upper body.
        $ h_xpos=140 #Defines position of the Hermione's full length sprite. (Default 370).
        show screen hermione_main
        with d3
        her "............."
        her "............."
        hide screen hermione_main
        with d3
        $ h_body = "03_hp/13_hermione_main/body_36.png" #Sprite of Hermione's upper body.
        $ h_xpos=140 #Defines position of the Hermione's full length sprite. (Default 370).
        show screen hermione_main
        with d3
        her "................."
        show screen ctc
        pause
        menu: 
            "\"Очень хорошо. Вот твои очки.\"":
                pass
            "\"Плохо. Ты можешь лучше.\"":
                hide screen hermione_main
                with d3
                $ h_body = "03_hp/13_hermione_main/body_12.png" #Sprite of Hermione's upper body.
                $ h_xpos=140 #Defines position of the Hermione's full length sprite. (Default 370).
                show screen hermione_main
                with d3
                her "..............."
                her "Ладно, я попробую получше, сэр..."
                hide screen hermione_main
                with d3
                $ h_body = "03_hp/13_hermione_main/body_11.png" #Sprite of Hermione's upper body.
                $ h_xpos=140 #Defines position of the Hermione's full length sprite. (Default 370).
                show screen hermione_main
                with d3
                her "Как насчет этого?"
                hide screen hermione_main
                with d3
                $ h_body = "03_hp/13_hermione_main/body_37.png" #Sprite of Hermione's upper body.
                $ h_xpos=140 #Defines position of the Hermione's full length sprite. (Default 370).
                show screen hermione_main
                with d3
                her "А-а-а.................."
                hide screen hermione_main
                with d3
                $ h_body = "03_hp/13_hermione_main/body_38.png" #Sprite of Hermione's upper body.
                $ h_xpos=140 #Defines position of the Hermione's full length sprite. (Default 370).
                show screen hermione_main
                with d3
                "............................"
                hide screen hermione_main
                with d3
                $ h_body = "03_hp/13_hermione_main/body_39.png" #Sprite of Hermione's upper body.
                $ h_xpos=140 #Defines position of the Hermione's full length sprite. (Default 370).
                show screen hermione_main
                with d3
                her "......................................"
                her "..................................................."
                her "...................................................................."
                hide screen hermione_main
                with d3
                $ h_body = "03_hp/13_hermione_main/body_40.png" #Sprite of Hermione's upper body.
                $ h_xpos=140 #Defines position of the Hermione's full length sprite. (Default 370).
                show screen hermione_main
                with d3
                her "......................................................................................................."

    if d_flag_02: #Stand still...
#    if d_flag_01: #STAND STILL.
        hide screen hermione_main
        with d3
        $ h_body = "03_hp/13_hermione_main/body_06.png" #Sprite of Hermione's upper body.
        $ h_xpos=140 #Defines position of the Hermione's full length sprite. (Default 370).
        show screen hermione_main
        with d3
        her "И так, я просто буду стоять здесь...?"
        m "Отлично... Теперь повернись... Медленно."
        her "Ух... Ладно..."
        hide screen hermione_main
        hide screen bld1
        with d3
        pause.5
        show screen hermione_01_f #Hermione stands still.
        with Dissolve(.7)

        her_02 "................................."
        menu:
            m "Hm..."
            "\"Униформа очень идет вам, мисс Грейнджер...\"":
                her_01 "............"
                her_05 "Спасибо, Профессор Дамблдор..."
            "\"У вас отличное тело, мисс Грейнджер...\"":
                her_03 "!?"
                her_04 ".............."
                her_04 "Спасибо, профессор..."
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
        show screen hermione_main
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
        hide screen hermione_main
        with d3
        $ h_body = "03_hp/13_hermione_main/body_24.png" #Sprite of Hermione's upper body.
        $ h_xpos=140 #Defines position of the Hermione's full length sprite. (Default 370).
        show screen hermione_main
        with d3
        
        her "Скорчить глупую рожицу, значит..."
        her "Посмотрим..."
        label stupid_faces:
        hide screen hermione_main
        with d3
        $ h_body = "03_hp/13_hermione_main/body_41.png" #Sprite of Hermione's upper body.
        $ h_xpos=140 #Defines position of the Hermione's full length sprite. (Default 370).
        show screen hermione_main
        with d3
        her "Как насчет этого?"
        menu:
            "\"Отлично! очень тупо! Я имею в виду, глупо.\"":
                jump stupid_enogh
            "\"Не совсем глупая.\"":
                pass
        hide screen hermione_main
        with d3
        $ h_body = "03_hp/13_hermione_main/body_12.png" #Sprite of Hermione's upper body.
        $ h_xpos=140 #Defines position of the Hermione's full length sprite. (Default 370).
        show screen hermione_main
        with d3
        her "........."
        hide screen hermione_main
        with d3
        $ h_body = "03_hp/13_hermione_main/body_43.png" #Sprite of Hermione's upper body.
        $ h_xpos=140 #Defines position of the Hermione's full length sprite. (Default 370).
        show screen hermione_main
        with d3
        her "Как насчет этого?"
        menu:
            "\"Ха-ха! Ты похожа на идиота!\"":
                jump stupid_enogh
            "\"Не достаточно глупо.\"":
                pass
        hide screen hermione_main
        with d3
        $ h_body = "03_hp/13_hermione_main/body_12.png" #Sprite of Hermione's upper body.
        $ h_xpos=140 #Defines position of the Hermione's full length sprite. (Default 370).
        show screen hermione_main
        with d3
        her "........."
        hide screen hermione_main
        with d3
        $ h_body = "03_hp/13_hermione_main/body_42.png" #Sprite of Hermione's upper body.
        $ h_xpos=140 #Defines position of the Hermione's full length sprite. (Default 370).
        show screen hermione_main
        with d3
        her "Что если я сделаю так?"
        menu:
            "\"Отлично! Очень смешно!\"":
                jump stupid_enogh
            "\"Не достаточно глупо.\"":
                jump stupid_faces
    
    if d_flag_04: #BAD GIRL
        hide screen hermione_main
        with d3
        $ h_body = "03_hp/13_hermione_main/body_07.png" #Sprite of Hermione's upper body.
        $ h_xpos=140 #Defines position of the Hermione's full length sprite. (Default 370).
        show screen hermione_main
        with d3
        her "Я..."
        her "Я была очень плохой девочкой..."
        g9 "Ты была очень, очень, очень плохой девочкой?"
        her "Да, сэр..."
        her "Я была очень, очень, очень, очень плохой девочкой..."
        label to_early_for_sucking_cocks:
        menu:
            g9 "..."
            "\"Тебя нужно наказать?\"":
                hide screen hermione_main
                with d3
                $ h_body = "03_hp/13_hermione_main/body_11.png" #Sprite of Hermione's upper body.
                show screen hermione_main
                with d3
                her "Нужно ли меня... наказать?"
                hide screen hermione_main
                with d3
                $ h_body = "03_hp/13_hermione_main/body_13.png" #Sprite of Hermione's upper body.
                show screen hermione_main
                with d3
                her "Эм..."
                her "....................."
                hide screen hermione_main
                with d3
                $ h_body = "03_hp/13_hermione_main/body_12.png" #Sprite of Hermione's upper body.
                show screen hermione_main
                with d3
                her "Ну, я не идеальная, если вы об этом, сэр..."
                hide screen hermione_main
                with d3
                $ h_body = "03_hp/13_hermione_main/body_13.png" #Sprite of Hermione's upper body.
                show screen hermione_main
                with d3
                her "Но нужно ли меня наказывать... Хм?"
                hide screen hermione_main
                with d3
                $ h_body = "03_hp/13_hermione_main/body_07.png" #Sprite of Hermione's upper body.
                show screen hermione_main
                with d3
                her "На самом ли деле это мне решать...? Я имею в виду..."
                her "Какое это имеет значение?"
                m "Ты слишком самокритичная, девочка."
                m "Просто скажи, что тебя нужно наказать!"
                hide screen hermione_main
                with d3
                $ h_body = "03_hp/13_hermione_main/body_05.png" #Sprite of Hermione's upper body.
                show screen hermione_main
                with d3
                her "Ладно. Меня следует наказать!"
                hide screen hermione_main
                with d3
                $ h_body = "03_hp/13_hermione_main/body_33.png" #Sprite of Hermione's upper body.
                show screen hermione_main
                with d3
                her "{size=-5}(И я действительно так думаю иногда...){/size}"
                m "Хорошая девочка."
                hide screen hermione_main
                with d3
                $ h_body = "03_hp/13_hermione_main/body_44.png" #Sprite of Hermione's upper body.
                show screen hermione_main
                with d3
                her "................??"
                m "Это было так трудно?"
                hide screen hermione_main
                with d3
                $ h_body = "03_hp/13_hermione_main/body_29.png" #Sprite of Hermione's upper body.
                show screen hermione_main
                with d3
                her "Н-нет , сэр..."
                m "Ладно, значит..."
            "\"Хочешь чтобы тебя отшлепали?\"":
                hide screen hermione_main
                with d3
                $ h_body = "03_hp/13_hermione_main/body_11.png" #Sprite of Hermione's upper body.
                show screen hermione_main
                with d3
                her "Хочу ли я..."
                hide screen hermione_main
                with d3
                $ h_body = "03_hp/13_hermione_main/body_18.png" #Sprite of Hermione's upper body.
                show screen hermione_main
                with d3
                her "Чтобы меня отшлепали??"
                hide screen hermione_main
                with d3
                $ h_body = "03_hp/13_hermione_main/body_05.png" #Sprite of Hermione's upper body.
                show screen hermione_main
                with d3
                her "?!"
                hide screen hermione_main
                with d3
                $ h_body = "03_hp/13_hermione_main/body_04.png" #Sprite of Hermione's upper body.
                show screen hermione_main
                with d3
                her "Профессор, мне не очень уютно от таких вопросах- -"
                m "Извиняюсь, позволь мне перефразировать вопрос..."
                m "Как сильно тебе нужны эти очки?"
                hide screen hermione_main
                with d3
                $ h_body = "03_hp/13_hermione_main/body_09.png" #Sprite of Hermione's upper body.
                show screen hermione_main
                with d3
                her ".................."
                hide screen hermione_main
                with d3
                $ h_body = "03_hp/13_hermione_main/body_04.png" #Sprite of Hermione's upper body.
                show screen hermione_main
                with d3
                her "Да, сэр. Я хочу, чтобы меня ошлпепали"
                m "Отлично. Думаю достаточно на сегодня..."
                hide screen hermione_main
                with d3
                $ h_body = "03_hp/13_hermione_main/body_07.png" #Sprite of Hermione's upper body.
                show screen hermione_main
                with d3
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
    
    
    hide screen hermione_main
    with d3
    $ h_body = "03_hp/13_hermione_main/body_24.png" #Sprite of Hermione's upper body.
    $ h_xpos=140 #Defines position of the Hermione's full length sprite. (Default 370).
    show screen hermione_main
    with d3
    her "Да!.............."
    her "Это было довольно легко..."
    her "Вы думаете я могла бы покупать еще очки за подобные услуги в будущем, профессор?"
    menu:
        "\"Я не думаю, что это хорошая идея.\"":
            hide screen hermione_main
            with d3
            $ h_body = "03_hp/13_hermione_main/body_28.png" #Sprite of Hermione's upper body.
            $ h_xpos=140 #Defines position of the Hermione's full length sprite. (Default 370).
            show screen hermione_main
            with d3
            her "Пожалуйста, профессор..."
            her "Нам действительно нужны эти очки..."
            m "......."
            hide screen hermione_main
            with d3
            $ h_body = "03_hp/13_hermione_main/body_29.png" #Sprite of Hermione's upper body.
            $ h_xpos=140 #Defines position of the Hermione's full length sprite. (Default 370).
            show screen hermione_main
            with d3
            her "Вы очень уважаемый мастер честно говоря..."
            her "Единственный человек в этой школе, у которого я могу попросить такое..."
            m "Ну, если ты настаиваешь..."
        "\"Возможно...\"":
            pass
            
    hide screen hermione_main
    with d3
    $ h_body = "03_hp/13_hermione_main/body_06.png" #Sprite of Hermione's upper body.
    $ h_xpos=140 #Defines position of the Hermione's full length sprite. (Default 370).
    show screen hermione_main
    with d3
    her "Спасибо, профессор. Огромное спасибо."
    hide screen hermione_main
    with d3
    $ h_body = "03_hp/13_hermione_main/body_01.png" #Sprite of Hermione's upper body.
    $ h_xpos=140 #Defines position of the Hermione's full length sprite. (Default 370).
    show screen hermione_main
    with d3
    her "Ну, я думаю мне стоит идти..."
    m "............"

    hide screen bld1
    hide screen hermione_main
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
        her "{size=-4}(Но нет ничего плохо в том, что я сделал сегодня...){/size}"
        her "{size=-4}(Я получила свои очки для факультета...){/size}"
        
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
        her "{size=-4}(Я плохая девченка...){/size}"
        her "{size=-4}(Я очень плохая девченка...){/size}"
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
    ">Теперь вы можете продавать очки для факультета за сексуальные услуги Гермионы."
    hide screen blktone
    with d3
    $ buying_favors_from_hermione_unlocked = True 
    $ days_without_an_event = 0 #Resets the counter. This counts how many days have passed since this event happened.
    $ event15_happened = True #Turns TRUE after event_15
    jump day_start








    
