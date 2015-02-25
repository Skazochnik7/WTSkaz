
###################REQUEST_12 (Level 04) (Play with her tits.) (Day/Night) ############################################################################
label new_request_12: #LV.4 (Whoring = 9 - 11)
    $herView.hideQQ()
    if request_12_points == 0:
        m "{size=-4}(Кажется, пора поиграть с её сиськами.){/size}"
    else:
        m "{size=-4}(Пора ещё раз поразвлечься с её сиськами.){/size}"
    $ menu_x = 0.5 #Default position of the menu (0.5). Version B is $ menu_x = 0.2
    menu:
        "\"(Да, давай попробую!)\"":
            show screen blktone
            with d3
            pass
        "\"(Нет, не сейчас.)\"":
            $event.NotFinished()
            jump new_personal_request
    
    if whoring <=8:
        jump too_much

    $ pos = POS_140
    $ herView.data().saveState()
        
    if request_12_points == 0 and whoring <= 14: # LEVEL 05 (one level higher then level at which it unlocks - 04) # FIRST TIME.
        m "Мисс Грейнджер."
        $herView.hideshowQQ( "body_01.png", pos )
        her "Да, сэр?"
        m "Как насчет еще одной услуги?"
        $herView.hideshowQQ( "body_02.png", pos )
        her "Эм... Ладно..."
        her "Какой, сэр?"
        m "Ну, как на счет того, чтобы ты подошла ко мне поближе и дала бы мне полапать твою грудь...?"
        $herView.hideshowQQ( "body_31.png", pos )
        her "!!!"
        m "Я бы хотел её потрогать."
        $herView.hideshowQQ( "body_66.png", pos )
        her "Профессор Дамбалдор! Вам не кажется, что это перебор?"
        m "Ты думаешь?"
        her "Я не такая распутная, как эти девчонки из \"Слизерина\", ну вы знаете..."
        m "Я знаю... Ты из \"Гриффундор\"... или как там..." #<- GRYFFINDOR MISSPELLED ON PERPOUSE   I KNOW
        $herView.hideshowQQ( "body_29.png", pos )
        her "И, раз я не такая, то я не буду продавать ещё одну услугу, сэр!"
        m "Конечно..."
        $herView.hideshowQQ( "body_69.png", pos )
        her "..................."
        m "Я дам тебе за это 35 очков."
        $herView.hideshowQQ( "body_66.png", pos )
        her "......................."
        her "Вы ведь будете только смотреть, сэр?"
        m "Вообще-то, я бы хотел потрогать и помять..."
        her "...................................."


    else: # Intro. Not first time.
        if whoring >= 9 and whoring <= 14: # LEVEL 04 AND LEVEL 05 # NOT A WHORE YET.
            m "Мисс Грейнджер..."
            $herView.hideshowQQ( "body_01.png", pos )
            her "Сэр?"
            m "Я бы хотел поиграть немного с вашей грудью..."
            $herView.hideshowQQ( "body_79.png", pos )
            her "Сэр... Лучше бы вы не делали мне таких предложения..."
            m "А что? Тяжело отказаться?"
            her "Ничего подобного, сэр."
            m "Я дам тебе 35 очков за это..."
            $herView.hideshowQQ( "body_69.png", pos )
            her ".................."
            her "Ладно... Вы можете потрогать их немного..."
        elif whoring >= 15: # LEVEL 06 and higher # NASTY WHORE.
            m "Мисс Грейнджер..."
            
            $herView.hideshowQQ( "body_01.png", pos )
            her "Сэр?"
            m "Я могу поиграть с вашей грудью немного?"
            $herView.hideshowQQ( "body_78.png", pos )
            her "Конечно, сэр..."
    
    $herView.hideQQ()
    hide screen blktone
    with d3
    hide screen bld1
    with d3
    $ walk_xpos=400 #Animation of walking chibi. (From)
    $ walk_xpos2=280 #Coordinates of it's movement. (To)
    $ hermione_speed = 03.0 #The speed of moving the walking animation across the screen.
    show screen hermione_walk_01 
    pause 1
    show screen blkfade
    with Dissolve(1)
    pause.5


    hide screen hermione_walk_01
    hide screen genie
    show screen ctc
    #show screen chair_02 #Genie's chair.
    hide screen genie
    show screen genie_and_tits_01
    with d1
    hide screen blkfade
    with d5
    stop music fadeout 1.0
    pause
    play music "music/(Orchestral) Playful Tension by Shadow16nh.mp3" fadein 1 fadeout 1 # SEX THEME.
    show screen blktone 
    with d3
    $herView.hideQQ()
    #$ only_upper = True #No lower body displayed. 
    $herView.data().addPose( CharacterExItemPoseShowTits( herView.mPoseFolder, 'pose_dress_up.png', G_Z_POSE ) )
    $herView.showQQ( "body_82.png", pos )
    pause
    her "...................................."
    
    
    
    $ posHead = gMakePos( 390, 340 )
    
    menu:
        m "..."
        "- Схватить грудь -":
            label no_smacking_tits:
                pass
            $herView.hideQQ()
            $herView.data().delPose()
            show screen blkfade
            with d5
            hide screen hermione_04 #Stands with tits out.
            hide screen genie
            show screen groping_naked_tits
            with d1
            hide screen blkfade
            hide screen blktone
            with d5
            pause
            show screen bld1
            with d3
            

            
            if whoring >= 9 and whoring <= 14: # LEVEL 04 AND LEVEL 05 # <=================================================================================== FIRST EVENT. (HERMIONE IS UNWILLING).

                $herViewHead.showQ( "body_118.png", posHead )
                her ".............................."
                $herViewHead.hideQ()
                m "У вас прекрасная грудь, мисс Грейнджер..."
                $herViewHead.showQ( "body_118.png", posHead )
                her "...................................."
                $herViewHead.hideQ()
                m "Вам нравится, когда я сжимаю их так?"
                $herViewHead.showQ( "body_120.png", posHead )
                her2 "Извините, сэр, но вы меня путаете с пошлыми развратными девчонками, я не такая..."
                her2 "Я позволила вам трогать мою грудь лишь потому, что вы заплатите мне за это..."
                her "Не потому, что мне нравится это..."
                $herViewHead.hideQ()
                m "Ясно..."
                m "Тогда ты больше похожа на проститутку..."
                $herViewHead.showQ( "body_119.png", posHead )
                her "Профессор Дамблдор!"
                her "Проституткам платят за секс..."
                $herViewHead.showQ( "body_120.png", posHead )
                her "Я никогда не опущусь до такого!"
                $herViewHead.hideQ()
                show screen blktone
                with d3
                ">Вы сжали одну грудь девочки и начали жадно сосать её."
                hide screen blktone
                with d3
                $herViewHead.showQ( "body_131.png", posHead )
                her "Ааах..."
                $herViewHead.hideQ()
                m "Наслаждаетесь, мисс Грейнджер?"
                if whoring >= 9 and whoring <= 11: # LEVEL 04 #  <=================================================================================== FIRST EVENT.
                    $herViewHead.showQ( "body_120.png", posHead )
                    her "Сэр, я всего лишь делаю это--"
                    $herViewHead.hideQ()
                    show screen blktone
                    with d3
                    ">Вы начали сильнее сжимать грудь..."
                    hide screen blktone
                    with d3
                    $herViewHead.showQ( "body_132.png", posHead )
                    her "Ах..."
                    $herViewHead.hideQ()
                    m "Скажи мне, что тебе нравится, девчонка!"
                    $herViewHead.showQ( "body_131.png", posHead )
                    her "Сэр, я позволила вам делать так, только потому--"
                    $herViewHead.hideQ()
                    m "Знаю, знаю...."
                    m "Ты начинаешь говорить как сломанный магнитофон."
                    $herViewHead.showQ( "body_79.png", posHead )
                    her "...."
                    $herViewHead.hideQ()
                    show screen blktone
                    with d3
                    show screen blkfade
                    with d7

                    show screen genie
                    hide screen groping_naked_tits
                    hide screen ctc

            
                    ">Вы отпускаете грудь девочки..."
                else:  # LEVEL 05 # <=================================================================================== SECOND EVENT.
                    $herViewHead.showQ( "body_87.png", posHead )
                    her "Ах..."
                    $herViewHead.hideQ()
                    show screen blktone
                    with d3
                    ">Вы ещё пару раз сжимаете её грудь, а потом снова начинаете жадно посасывать её..."
                    hide screen blktone
                    with d3
                    $herViewHead.showQ( "body_31.png", posHead )
                    her "Ах... Сэр..."
                    $herViewHead.hideQ()
                    m "Что? Тебе нравится это, правда?"
                    $herViewHead.showQ( "body_31.png", posHead )
                    her "Нет... Я..."
                    $herViewHead.hideQ()
                    m "Не ври своему директору, девчонка!"
                    show screen blktone
                    with d3
                    ">Вы снова сжимаете её грудь..."
                    hide screen blktone 
                    with d3
                    $herViewHead.showQ( "body_87.png", posHead )
                    her "Ах..."
                    her "Я не вру, сэр..."
                    $herViewHead.showQ( "body_31.png", posHead )
                    her "С чего бы мне наслаждаться этим?"
                    $herViewHead.hideQ()
                    m "Я не знаю, это ты мне расскажи."
                    show screen blktone
                    with d3
                    ">Вы продолжаете играть с её грудью..."
                    hide screen blktone
                    with d3
                    $herViewHead.showQ( "body_31.png", posHead )
                    her "Ах... Я..."
                    $herViewHead.hideQ()
                    m "Да, что такое?"
                    $herViewHead.showQ( "body_117.png", posHead )
                    her "Нич... ничего, сэр..."
                    $herViewHead.hideQ()
                    m "А я думаю, как раз кое что...."
                    m "Я думаю, тебе нравится, когда я сжимаю твои сиськи и играю с ними."      
                    $herViewHead.showQ( "body_118.png", posHead )
                    her "Сэр, пожалуйста..."
                    if daytime:
                        her "Скоро начнутся уроки..."
                    else: 
                        her "Уже поздно..."
                    $herViewHead.showQ( "body_117.png", posHead )
                    her "Я могу идти, сэр? Пожалуйста?"
                    $herViewHead.hideQ()
                    show screen blkfade 
                    with d3
                    m "Конечно, ступай..."
                    $herViewHead.showQ( "body_118.png", posHead )
                    her "..............."
                    $herViewHead.showQ( "body_117.png", posHead )
                    her "Сэр, вы продолжаете... держать меня..."
                    $herViewHead.hideQ()
                    m "О, правда... моя вина...."
                    ">Вы отпускаете грудь Гермионы..."
                    
                    show screen genie
                    hide screen groping_naked_tits
                    hide screen ctc

            elif whoring >= 15: # LEVEL 06 and higher # <=================================================================================== THIRD EVENT. 
               
                $herViewHead.showQ( "body_121.png", posHead )
                her "Ах..."
                $herViewHead.hideQ()
                m "Ты сегодня более чувствительная, да?"
                $herViewHead.showQ( "body_128.png", posHead )
                her "Наверное..."
                $herViewHead.showQ( "body_131.png", posHead )
                her "Ах..."
                $herViewHead.hideQ()
                m "Тебе нравится, когда я играю с твоими сиськами?"
                $herViewHead.showQ( "body_128.png", posHead )
                her "Да, сэр... Ах..."
                $herViewHead.hideQ()
                m "Хех..."
                m "Что, если я ущипну твой сосок?"
                show screen blktone
                with d5
                $herViewHead.showQ( "body_117.png", posHead )
                her "!!!"
                $herViewHead.showQ( "body_131.png", posHead )
                her "Ах! Сэр..."
                $herViewHead.hideQ()
                m "Или сделаю вот так?"
                show screen blktone8
                with d3
                ">Вы схватили грудь девочки сильнее и начали массировать стоячие соски..."
                hide screen blktone8
                with d3
                $herViewHead.showQ( "body_132.png", posHead )
                her "Ах... ааа... аааааа... Сэр..."
                $herViewHead.hideQ()
                m "А если я поиграю с ними жестче?"
                $herViewHead.showQ( "body_130.png", posHead )
                her "Ааа... Сэр, пожалуйста..."
                $herViewHead.hideQ()
                show screen blktone8
                with d3
                ">Гермиона схватилась за стол, чтобы не сделать случайный шаг к вам..."
                hide screen blktone8
                with d3
                m "Умница..."
                $herViewHead.showQ( "body_123.png", posHead )
                her "*Тяжело дышит*"
                $herViewHead.hideQ()
                m "Тебе нравится это?"
                $herViewHead.showQ( "body_139.png", posHead )
                her "Вы делаете мне больно, сэр..."
                $herViewHead.hideQ()
                m "Но тебе это нравится?"
                $herViewHead.showQ( "body_140.png", posHead )
                her "Ах... Да, сэр... Не знаю почему, но мне нравится..."
                $herViewHead.hideQ()
                m "Хорошая девочка..."
                show screen blktone8
                with d3
                ">Вы отпустили её сосочки..."
                hide screen blktone8
                with d3
                $herViewHead.showQ( "body_138.png", posHead )
                her "Ах..."
                $herViewHead.hideQ()
                show screen blkfade
                with d5
                m "На сегодня всё, мисс Грейнджер..."
                $herViewHead.showQ( "body_139.png", posHead )
                her "Ооо...?"
                $herViewHead.hideQ()
                m "Что такое? У вас разочарованный вид."
                m "Я заплачу вам, конечно же..."
                $herViewHead.showQ( "body_141.png", posHead )
                her "Не в этом дело..."
                her "А..."
                $herViewHead.showQ( "body_139.png", posHead )
                if daytime:
                    her2 "У меня всё ещё есть время перед уроками и..."
                else:
                    her "Сейчас ещё ведь не поздно?"
                her "ммм..."
                her "..................."
                $herViewHead.hideQ()
                m "Вы хотите, чтобы я продолжил, да?"
                $herViewHead.showQ( "body_139.png", posHead )
                her "Я... не то, чтобы \"хочу\"... "
                $herViewHead.showQ( "body_138.png", posHead )
                her "Но, если вы настаиваете...."
                $herViewHead.hideQ()
                m "Конечно, я настаиваю... видимо."
                $herViewHead.showQ( "body_138.png", posHead )
                her "Ах..."
                $herViewHead.hideQ()
                hide screen blkfade
                with d5
                
                show screen ctc
                pause
                hide screen ctc
                
                #BLACK FADE
                show screen blkfade
                with d7
                ">Вы Еще немного играетесь с грудью Гермионы..."
                
                show screen genie
                hide screen groping_naked_tits
                hide screen ctc

        "- Шлепнуть по ней -":
            $herView.hideQ()
            with d5
            ">Вы громко и мощно шлепнули грудь Гермионы!"
            $ renpy.play('sounds/slap.mp3') #SLAP!
            show screen white
            with hpunch
            pause.08
            hide screen white
            show screen bld1
            if whoring >= 9 and whoring <= 11: # LEVEL 04 # <=================================================================================== FIRST EVENT. (HERMIONE IS UNWILLING).
                $herView.hideQQ()
                $herView.showQ( "182.png", pos )
                her "!!!"
                $herView.hideQQ()
                $herView.showQ( "183.png", pos )
                her "Ау! Это больно! *Хнык!*"
                m "Но тебе это всё равно нравится?"
                $herView.hideQQ()
                $herView.showQ( "body_81.png", pos )
                her "Мне правда... должно \"нравится\" это, сэр..?"
                her "Какой же девушке в здравом уме понравится это?"
                $herView.hideQQ()
                $herView.showQQ( "184.png", pos )
                stop music fadeout 1.0
                her "Вы чокнутый и сумасшедший старик!"
                $herView.hideQQ()
                show screen blkfade
                with d3
                # RUNS OFF
                $ mad += 20
                m "............"
                m "Ну, тогда никаких очков \"Гриффиндору\"..."
                
                show screen genie
                hide screen groping_naked_tits
                hide screen ctc
                hide screen genie_and_tits_01
                call music_block

                # restore state before leaving
                $herView.data().loadState()
                jump could_not_flirt #Sent here when choose "Favor failed! No points for you!" (Hermione is leaving without getting any points).
                
                    
            elif whoring >= 12 and whoring <= 14: # LEVEL 05 # <=================================================================================== SECOND EVENT.
                $herView.hideQQ()
                $herView.showQ( "182.png", pos )
                her "!!!"
                $herView.hideQQ()
                $herView.showQ( "183.png", pos )
                her "Ау!"
                her "Зачем вы так делаете, сэр?"
                m "Хммм... мне показалось это хорошей идеей..."
                m "Тебе нравится?"
                $herView.hideQQ()
                $herView.showQ( "body_83.png", pos )
                her "...Конечно нет, сэр."
                m "Тогда давай попробуем ещё раз."
                $herView.hideQQ()
                $herView.showQ( "body_82.png", pos )
                her "Что?"
                $herView.hideQQ()
                $ renpy.play('sounds/slap.mp3') #SLAP!
                show screen white
                with hpunch
                pause.08
                hide screen white
                $herView.hideQQ()
                $herView.showQ( "182.png", pos )
                her "!!!"
                her "Ау! Прекратите, мне больно!"
                m "Мне показалось, что тебе понравилось."
                $herView.hideQQ()
                $herView.showQ( "body_85.png", pos )
                her "Но это не так..."
                her "И если вы собираетесь продолжить, сэр..."
                $herView.hideQQ()
                $herView.showQ( "body_81.png", pos )
                her "...тогда я собираюсь уйти."
                m "Ладно, ладно..."
                $herView.hideQQ()
                jump no_smacking_tits #Jumps to usual tits molesting scene.

            elif whoring >= 15: # LEVEL 06 and higher # <=================================================================================== THIRD EVENT. 
                $herView.hideQQ()
                $herView.showQ( "182.png", pos )
                her "Ах!!!"
                $herView.hideQQ()
                $herView.showQ( "185.png", pos )
                her "Сэр, зачем вы сделали это?"
                m "Хм... Мне показалось это хорошей идеей..."
                m "Тебе понравилось?"
                $herView.hideQQ()
                $herView.showQ( "body_82.png", pos )
                her ".........."
                her "Я не извращенка..."
                $herView.hideQQ()
                show screen blktone8
                with d3
                ">Вы ещё раз смачно шлепнули грудь Гермионы!"
                hide screen blktone8
                with d3
                $ renpy.play('sounds/slap.mp3') #SLAP!
                show screen white
                with hpunch
                pause.08
                hide screen white
                $herView.hideQQ()
                $herView.showQ( "186.png", pos )
                her "Аа!!!"
                m "Скажи, что тебе это нравится!"
                her "Сэр... Я..."
                $herView.hideQQ()
                show screen blktone8
                with d5
                ">Вы ещё несколько раз шлепнули по груди!"
                $ renpy.play('sounds/slap.mp3') #SLAP!
                show screen white
                with hpunch
                pause.05
                hide screen white
                pause.3
                $ renpy.play('sounds/slap.mp3') #SLAP!
                show screen white
                with hpunch
                pause.05
                hide screen white
                pause.3
                $ renpy.play('sounds/slap.mp3') #SLAP!
                show screen white
                with hpunch
                pause.05
                hide screen white
                pause.3
                ">Сиськи Гермионы прыгают как шарики..."
                hide screen blktone8
                with d5
                $herView.hideQQ()
                $herView.showQ( "187.png", pos )
                her "А-аах!!! АА!!! А-ах-ааах!!!"
                m "Тебе нравится это, признайся."
                $herView.hideQQ()
                $herView.showQ( "188.png", pos )
                her "..........."
                $herView.hideQ()
                hide screen ctc
                with d3
                ">Вы шлепнули по груди ещё раз."
                $ renpy.play('sounds/slap.mp3') #SLAP!
                show screen white
                with hpunch
                pause.05
                hide screen white
                pause.3
                $ renpy.play('sounds/slap.mp3') #SLAP!
                show screen white
                with hpunch
                pause.05
                hide screen white
                pause.3
                $ renpy.play('sounds/slap.mp3') #SLAP!
                show screen white
                with hpunch
                pause.05
                hide screen white
                pause.3
                $herView.hideQQ()
                $herView.showQQ( "187.png", pos )
                her "А-а! Да! Мне нравится, мне нравится это! А-а..."
                $herView.hideQQ()
                $herView.showQQ( "184.png", pos )
                her "...получается, я извращенка, сэр?"
                m "Что?"
                m "Не глупи, девчонка."
                m "Это вполне естественно для девочки, наслаждаться тем, что с её грудью играют."
                her "......"
                her "Вы уверены, сэр?"
                m "Да. Поверь мне, я знаю."
                $herView.hideQQ()
                ">Вы начали снова шлепать её грудь!"
                $ renpy.play('sounds/slap.mp3') #SLAP!
                show screen white
                with hpunch
                pause.05
                hide screen white
                pause.3
                $herView.hideQQ()
                $herView.showQQ( "187.png", pos )
                her "Да-да... да... Спасибо, сэр."
                $herView.hideQQ()
                m "Ну что-ж... Достаточно со шлепками на сегодня..."
                jump no_smacking_tits #Jumps to usual tits molesting scene.

    
    $ gryffindor += current_payout #35
    hide screen h_c_u
    hide screen g_c_u
    hide screen g_c_c_u # Genie's sperm. Universal.
    hide screen ctc
    hide screen chair_02
    hide screen desk_02
    show screen genie
    show screen bld1
    $ hermione_chibi_xpos = 400 #Near the desk.
    $ hermione_chibi_ypos = 250 #Default: 250
    show screen hermione_02 #Hermione stands still.
    pause.1
    hide screen blkfade
    with d3
    
    stop music fadeout 1.0
    m "Да, мисс Грейнджер. 35 очков \"Гриффиндору\"." 
    $ gryffindor +=35
    $herView.showQ( "body_13.png", pos )
    hide screen hermione_01_f #Hermione stands still.
    with d3
    her "Спасибо, Сэр..."

    if whoring <= 11: # If still of level of unlocking - 04
        $ whoring +=1

    $ request_12_points += 1

    if whoring >= 9 and whoring <= 11:
        $ level = "04"
        $ new_request_12_01 = True # HEARTS.
    if whoring >= 12 and whoring <= 14:
        $ level = "05"
        $ new_request_12_02 = True # HEARTS.
    if whoring >= 15:
        $ level = "06"
        $ new_request_12_03 = True # HEARTS.


    hide screen bld1
    $herView.hideQ()
    hide screen blktone 
    hide screen ctc
    with Dissolve(.3)
    
    $ walk_xpos=400 #Animation of walking chibi. (From)
    $ walk_xpos2=610 #Coordinates of it's movement. (To)
    $ hermione_speed = 02.0 #The speed of moving the walking animation across the screen.
    show screen hermione_walk_01_f 
    pause 2
    hide screen hermione_walk_01_f 
    $ renpy.play('sounds/door.mp3') #Sound of a door opening.
    with Dissolve(.3)

    $ herView.data().loadState()
    call music_block
    if daytime:
        $ hermione_takes_classes = True
        jump night_main_menu
    else:
        $ hermione_sleeping = True
        jump day_main_menu            
   
    




