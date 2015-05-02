###################REQUEST_02 (Level 01)
label new_request_02: #SHOW ME YOUR Трусики
    $herView.hideQQ()
    $ pos = POS_370
    m "{size=-4}(Я хочу попросить ее показать мне трусики. Просто и понятно.){/size}"
    $ menu_x = 0.5 #Default menu position restored.
    menu:
        "\"(Да, давай попробуем!)\"":
            pass
        "\"(Не сейчас)\"":
            $event.NotFinished()
            jump new_personal_request
    $herView.showQQ( "body_01.png", pos )
    her "Так, что же мне нужно сделать?"
    m "Ничего такого, на самом деле..."
    m "Я просто хочу, чтобы ты показала мне свои трусики."             

    if IsFirstRun() and hermi.whoring <= 5: #First time this event taking place. and LEVEL 02.  
#    if request_02 == 0 and whoring <= 5: #First time this event taking place. and LEVEL 02.  
#        $ new_request_02_01 =  True #Hearts.
        $SetHearts(1)

        $herView.hideshowQQ( "body_14.png", pos )
        her "Мои... трусики?.."
        $herView.hideshowQQ( "body_47.png", pos )
        her  "Профессор Дамблдор!"
        m "Я знаю, знаю, это немного странно..."
        $herView.hideshowQQ( "body_48.png", pos )
        her  " {size=+7}Немного!?{/size}"
        her "Это абсолютно неуместно!"
        m "Слушай, нам ведь предстоит это пройти, чтобы пойти дальше, верно?"
        $herView.hideshowQQ( "body_31.png", pos )
        her  "\"Пойти дальше\"? Профессор, я не понимаю..."
        m "Что вы не понимаете, мисс Грейнджер?"
        m "Вам нужны эти очки или нет?"
        $herView.hideshowQQ( "body_31.png", pos )
        her  "Нужны..."
        m "Значит, приподнимайте свою юбку..."
        $herView.hideshowQQ( "body_47.png", pos )
        her "............."
    else:
        if IsNextRun(): #First time this event taking place. and LEVEL 02.  
#        if request_02 >= 1: #Not the first time
            $herView.hideshowQQ( "body_29.png", pos )
            her "Ох... снова?"
            m "Просто сделай это..."
        $herView.hideshowQQ( "body_29.png", pos )
        her ".................."
        
        
    $ current_payout = 5 #Used when haggling about price of th favor.

    hide screen bld1
    $herView.hideQ( d5 )
    $ menu_x = 0.5 #Default menu position restored.
    if hermi.whoring <= 2:    #angry with pants
        show screen hermione_lift_skirt_angry
        with d3
    elif hermi.whoring <= 5:
        show screen hermione_lift_skirt_normal #Hermione lifts her skirt WITH pants
        with d3
    elif hermi.whoring >=6 and hermi.whoring<13:  # no panties
        show screen hermione_lift_skirt_no_panties
        with d3
    else: 
        pass
        
        
    #play music "music/Under-the-Radar by PhobyAk.mp3" fadein 1 fadeout 1 
    play music "music/(Orchestral) Playful Tension by Shadow16nh.mp3" fadein 1 fadeout 1 

    if hermi.whoring >= 0 and hermi.whoring <= 2: #LEVEL 01
        $her_head_state = 8
        her_head_main "........................"
    elif hermi.whoring >= 3 and hermi.whoring <= 5: #LEVEL 02
        $her_head_state = 14
        her_head_main "....................."
    elif hermi.whoring >= 6 and hermi.whoring<13: #LEVEL 03 and up.
        $her_head_state = 18
        her_head_main ".........................."
        g4 "!!?"

        
        

    # save previous state and add pose
    # add pose with lifted skirt
    if hermi.whoring<13:
        $herView.data().saveState()
        #$herView.data().addPose( CharacterExItemSkirtLifted( herView.mPoseFolder, 'pose_skirt_up.png', G_Z_POSE ) )
        $herView.data().addItem( 'item_pose_lifted_skirt' )
        $ pos = POS_120
    
    if hermi.whoring >= 0 and hermi.whoring <= 2: #LEVEL 01   <============================= Fist event.
#        $ new_request_02_01 =  True #Hearts.
#        SetHearts(1)

        show screen bld1
        with d3
        show screen blktone
        with d3
        $herView.showQ( "body_49.png", pos )
        show screen ctc
        with d3
        pause
        
        her "....................."
        menu:
            "- Смотреть на ее лицо -":
                ">Вы внимательно смотрите на лицо Гермионы..."
                pause
                ">Вы задаетесь вопросом, что сейчас происходит у нее в голове."
                $herView.hideshowQQ( "body_51.png", pos )
                her "......................."
                pause
            "- Смотреть на ее трусики -":
                ">Просто женское белье..."
                pause
                $herView.hideshowQQ( "body_51.png", pos )
                her "......................."
               

    elif hermi.whoring >= 3 and hermi.whoring <= 5: #LEVEL 02  <====================================================================== SECOND EVENT!
#        $ new_request_02_02 =  True #Hearts.
        $SetHearts(2)

        show screen bld1
        with d3
        show screen blktone
        with d3
        $herView.showQ( "body_52.png", pos )
        show screen ctc
        with d3
        pause
        her "Вот, профессор..."
        menu:
            "\"Вы не выглядите смущенной...\"":
                $herView.hideshowQQ( "body_53.png", pos )
                her "Это не так..."
                $herView.hideshowQQ( "body_54.png", pos )
                her "Это сравнительно небольшая плата, если \"Гриффиндор\" получит кубок в этом году."
                her "Я знаю, что все будут счастливы..."
                pause
            "\"Мне нравятся ваши трусики...\"":
                $herView.hideshowQQ( "body_53.png", pos )
                her "Спасибо, профессор..."
            "- Продолжать смотреть в ее глаза -":
                $herView.hideshowQQ( "body_55.png", pos )
                her ".............................."
                her "...........................?"
                $herView.hideshowQQ( "body_56.png", pos )
                her "................................"
                $herView.hideshowQQ( "body_57.png", pos )
                her "Профессор, пожалуйста... Вы смущаете меня."
                

    elif hermi.whoring >= 6 and hermi.whoring<13: #LEVEL 04 and up. <====================================================================== FINAL EVENT! (No Трусики).
#        $ new_request_02_03 =  True #Hearts.
        $SetHearts(3)

        show screen bld1
        with d3
        show screen blktone
        with d3
        
        # we should remove panties from hermi in this event
        $herView.data().delPanties()
        
        $herView.showQ( "body_58.png", pos )
        show screen ctc
        with d3
        pause
        g4 "Где ваши трусики, мисс Грейнджер?"
        $herView.hideshowQQ( "body_59.png", pos )
        her "Ох, в последнее время я не очень хочу носить их..."
        menu:
            "\"Ах ты, маленькая шлюха!\"":
                her "Хм..."
                $herView.hideshowQQ( "body_58.png", pos )
                her "Вероятно, это так..."
                her "Могу я получить чуть больше очков за это?"
                menu:
                    "\"Конечно!\"":
                        m "Конечно!"
                        $ current_payout +=10
                        m "Десять очков \"Гриффиндору\"!" 
                        $herView.hideshowQQ( "body_60.png", pos )
                        her "Спасибо вам, сэр!"
                    "\"Категорически нет!\"":
                        $ hermi.liking -=15
                        $herView.hideshowQQ( "body_61.png", pos )
                        her ".............................."
                        $herView.hideshowQQ( "body_62.png", pos )
                        her "Не будьте так скупы, профессор."   
            "\"Отлично. Пять очков Гриффиндору!\"":
                pass           
    elif hermi.whoring >= 13: #Хотя бы один раз дрочила
        $herView.hideshowQQ( "body_12.png", pos )
        her "Сэр, вы действительно позвали меня сюда из-за этих несчастных 5 очков?"
        her "Мне жалко тратить время на такую  услугу. Это для первокурок, сэр!"
        m "Неужели?"
        her "\"Показать трусики за 5 очков\". Просто смешно!"
        $herView.hideshowQQ( "body_10.png", pos )
        her "Может, мы займемся чем-нибудь ....м-м... поинтереснее?"
        her "В смысле, дающим больше очков?"
        menu: 
            "\"И чем же вы хотите заняться?\"":
                m "И чем же вы хотите заняться, мисс Грейнджер?"
                $herView.hideshowQQ( "body_68.png", pos )
                her "Ну, не знаю, сэр. Есть разные варианты!"
                jump new_personal_request
            "\"C каких это пор вы стали выбирать себе задания, мисс Грейнджер?":
                $ SetHearts(4)
                m "C каких это пор вы стали выбирать себе задания, мисс Грейнджер?"
                m "Кажется, это я здесь решаю, какая услуга оплачивается."
                m "Так вот, сегодня оплачивается показ ваших трусов!"
                $herView.hideshowQQ( "body_202.png", pos )
                her "Простите, сэр! Конечно."
                m "Итак?"
                her "Вот, профессор."
                $herView.hideshowQQ( "body_111.png", pos )
                "> Гермиона достает из кармана трусики и показывает их вам."
                g4 "Что это за?!.."
                her "Мои трусики, сэр. Показываю их вам, как вы просили."
                m "Вы прикидываетесь, мисс?"
                $herView.hideshowQQ( "body_53.png", pos )
                her "Сэр?"
                m "Я рассчитываю увидеть нижнее белье, которое {size=+4}НА ВАС!{/size}"
                $herView.hideshowQQ( "body_68.png", pos )
                her "А-а! Так его нет, сэр. Я сегодня хожу без трусов."
                m "Ну так и покажите мне это!"
                $herView.hideshowQQ( "body_31.png", pos )
                her "При всем уважении, сэр, это получается почти стриптиз. А значит, стоит гораздо больше, чем пять очков!"
                $herView.hideshowQQ( "body_128.png", pos )
                her "Так, посчитаем..."
                her "Парни хотят увидеть киску девчонки гораздо больше, чем все остальное..."
                her "Пусть киска - 2/3 от всего стриптиза..."
                $herView.hideshowQQ( "body_101.png", pos )
                her "2/3 от 35 очков это... 23 и 3 в периоде, сэр."
                her "Только из уважения к вам округляем в меньшую сторону."
                $herView.hideshowQQ( "body_53.png", pos )
                her "Получается 20 очков! Вот, это будет справедливо."
                menu: 
                    "\"Нет!\"":
                        m "Вы свободны, мисс Грейнджер!"
                        $herView.hideshowQQ( "body_58.png", pos )
                        her "Как скажете, сэр. В таком случае, я хотела бы получить свою оплату."
                    "\"Хорошо, 20 очков. Показывайте!":
                        $current_payout+=20
                        m "Ладно, я заплачу вам 20 очков. Показывайте!"
                        $herView.hideshowQQ( "body_186.png", pos )
                        her "25 очков, сэр."
                        g4 "?!"
                        her "20 за киску и 5 за трусики, которые я уже показала, сэр. Всего 25."
                        m "Мисс Грейнджер, вы торгуетесь, как на рынке, вы потеряли всякий стыд!"
                        $herView.hideshowQQ( "body_64.png", pos )
                        her "Не потеряла, сэр. Вы же видите, как я краснею."
                        m "Действительно... Кхм!"
                        m "Ну и чего вы ждете? За 25 очков я хочу увидеть что-то особенное."
                        $herView.hideQQ()
#                        show screen bld1
#                        with d3
#                        show screen blktone
#                        with d3
                        
                        # we should remove panties from hermi in this event
                        show screen hermione_lift_skirt_no_panties
                        with d3
#                        $her_head_state = 18
#                        her_head_main ".........................."
#                        g4 "!!?"
                        hide screen bld1

                        $herView.data().delPanties()
#                        $herView.data().saveState()
                        #$herView.data().addPose( CharacterExItemSkirtLifted( herView.mPoseFolder, 'pose_skirt_up.png', G_Z_POSE ) )
                        $herView.data().addItem( 'item_pose_lifted_skirt' )
                        $ pos = POS_120

#                        her "test"
                        
                        show screen bld1
                        with d3
                        show screen blktone
                        with d3
                        
                        # we should remove panties from hermi in this event
                        
                        $herView.showQ( "body_58.png", pos )
                        show screen ctc
                        with d3
                        pause






                        her "Это достаточно особенное, сэр? Я как раз сегодня подбрилась."
                        m "Завораживающие подробности."
                        menu:
                            "\"Вы не слишком смущаетесь, мисс...\"":
                                $herView.hideshowQQ( "body_53.png", pos )
                                m "Вы не слишком смущены, мисс Грейнджер."
                                her "Ну, если мой директор хочет получше меня рассмотреть, должна ли я возражать?..."
                                $herView.hideshowQQ( "body_54.png", pos )
                                her "Тем более, что Гиффиндор получит еще [current_payout] очков."
                            "- Продолжать смотреть ей в глаза -":
                                $herView.hideshowQQ( "body_55.png", pos )
                                her ".............................."
                                her "...........................?"
                                $herView.hideshowQQ( "body_56.png", pos )
                                her "................................"
                                if not end.IsEnding(const_ENDING_STRONG_GIRL) and hermi.whoring<14:
                                    her "Сэр, мне пора идти. У меня сейчас зельеварение, а профессор Снейп очень строг к опаздывающим..."               
                                    her "...если они из Гриффиндора."               
                                    m "Хорошо, мисс Грейнджер."
                                else:
                                    $music.Start("Supergirl")
                                    $herView.hideshowQQ( "body_64.png", pos )
                                    "> Гермиона нахально смотрит вам в глаза, и вы чувствуете, что начинаете возбуждаться."
                                    "> Девушка, как бы невзначай, облизывает губы."
                                    her "Сэр, уже скоро уроки. Может, я вас по-быстрому подою и уйду заниматься?"
                                    menu:
                                        "\"Нет! Хватит на сегодня.\"":
                                            $herView.hideshowQQ( "body_55.png", pos )
                                            m "Достаточно, мисс Грейнджер."
                                        "\"Что ты сделаешь?!...\"":
                                            $herView.hideshowQQ( "body_53.png", pos )
                                            g4 "Что ты сделаешь?!"
                                            her "Подою вас. Только не говорите, что не знаете, как девчонки называют {size=+4}ЭТО{/size}."
                                            m "Я знаю, как они называют. Но откуда это знаете {size=+4}ВЫ{/size}, мисс Грейнждер?!"
                                            m "Вы ведь не интересуетесь {size=+4}ТАКИМИ{/size} вещами?"
                                            $herView.hideshowQQ( "body_84.png", pos )
                                            her "Ну, сэр, поскольку вы уже просили меня об этой услуге, мне пришлось подготовиться и провести небольшое исследование."
                                            m "Научное, разумеется?"
                                            her "Разумеется, сэр. И теперь я знаю много подходящих выражений: играть в руку, дурака валять, трясти мошной..."
                                            m "Мисс Грейнджер, избавьте меня от ваших лингвистических упражнений."
                                            $herView.hideshowQQ( "body_75.png", pos )
                                            her "Конечно, сэр... "
                                            $herView.hideshowQQ( "body_46.png", pos )
                                            her "Так мы будем сегодня драконить тузика или как?"
                                            menu:
                                                "\"Нет!...\"":
                                                    $herView.hideshowQQ( "body_53.png", pos )
                                                    m "Мисс Грейнджер, подите прочь с этим вашим Тузиком!"
                                                    her "Не могу с тузиком, сэр, потому что..."
                                                    m "Неважно, мисс Грейнджер, просто достаточно на сегодня."
                                                    her ".............................."
                                                "Хорошо, мисс Грейнджер...":
                                                    $herView.hideshowQQ( "body_56.png", pos )
                                                    m "Хорошо, мисс Грейнджер, приступайте. Надеюсь, ваши ручки так же искусны, как ваш язык."
                                                    $herView.hideshowQQ( "body_53.png", pos )
                                                    her "Да, сэр. Плюс 45 очков?"
                                                    m "Да, девочка, да. Плюс 45."
                                                    $current_payout+=45
                                                    $music()
                                                    $ hermione_chibi_xpos = 400 #Near the desk.
                                                    $ pos = POS_120
                                                    hide screen ctc
                                                    $herView.hideQQ()
                                                      
                                                    # load state before doing mess
                                                    $herView.data().loadState()

                                                    jump new_request_16_jerkonly

    stop music fadeout 4.0
    
    label request_02_done:
    $ gryffindor +=current_payout
    m "[current_payout] очков \"Гриффиндору\", мисс Грейнджер. Отличная работа." 
    pause
    
    $ hermione_chibi_xpos = 400 #Near the desk.
    $ pos = POS_120
    hide screen ctc
    $herView.hideQQ()
      
    # load state before doing mess
    $herView.data().loadState()

    show screen hermione_02 #Hermione stands still.
    $herView.showQ( "body_31.png", pos )
    with fade
    
    stop music fadeout 4.0

    her "Это все?"
    m "Да, можешь идти."

    if IsFirstRun():
#    if request_02 == 0: #First time.
        $herView.hideQQ()
        $ pos.xpos = 300
        $herView.showQQ( "body_13.png", pos )
        her "Еще [current_payout] очков..."
        her "Не могу дождаться, чтобы рассказать ребятам!"
        $herView.hideshowQQ( "body_12.png", pos )
        her "Только я не могу рассказать обо всем, что пришлось сделать для этого..."
    
    if daytime:
        her "Мои занятия вот-вот начнутся..."
    else:
        her "Уже довольно поздно, сэр... Мне пора..."

    label new_request_16_jerkonly_to_02:
        hide screen hermione_02 #Hermione stands still.
        $herView.data().loadState()

    
    $herView.hideQQ()
    hide screen bld1
    hide screen blktone 
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
    
    

    ### MUSIC BLOCK ###
    if daytime:
        play music "music/Brittle Rille.mp3" fadein 1 fadeout 1 # DAY MUSIC
    else:
        play music "music/Music for Manatees.mp3" fadein 1 fadeout 1 # NIGHT MUSIC
    ### END OF BLOCK ###



    if hermi.whoring <= 2:
        $ hermi.whoring +=1
#    $ request_02 += 1

    $event.Finalize()    
    if daytime:
        $ hermione_takes_classes = True
        jump day_main_menu
    else:
        $ hermione_sleeping = True
        jump night_main_menu

