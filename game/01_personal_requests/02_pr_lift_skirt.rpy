###################REQUEST_02 (Level 01)
label new_request_02: #SHOW ME YOUR Трусики
    $herView.hideQQ()
    $ pos = POS_370
    m "{size=-4}(Я хочу попросить ее показать мне трусики. Просто и понятно.){/size}"
    $ menu_x = 0.5 #Default menu position restored.
    menu:
        "\"(Да, давай попробуем!)\"":
            pass
        "\"(Не сейчас.)\"":
            jump new_personal_request
    $herView.showQQ( "body_01.png", pos )
    her "Так, что же мне нужно сделать?"
    m "Ничего такого, на самом деле..."
    m "Я просто хочу, чтобы ты показа мне свои трусики."             
    if request_02 == 0 and whoring <= 5: #First time this event taking place. and LEVEL 02.  
        $ new_request_02_01 =  True #Hearts.
        $herView.hideQQ()
        $herView.showQQ( "body_14.png", pos )
        her "Мои... трусики...?"
        $herView.hideQQ()
        $herView.showQQ( "body_47.png", pos )
        her  "Профессор Дамблдор!"
        m "Я знаю, знаю, это немного странно..."
        $herView.hideQQ()
        $herView.showQQ( "body_48.png", pos )
        her  " {size=+7}Немного !?{/size}"
        her "Это абсолютно неуместно!"
        m "Слушай, нам ведь предстоит это пройти, чтобы пойти дальше, верно?"
        $herView.hideQQ()
        $herView.showQQ( "body_31.png", pos )
        her  "\"Пойти дальше\"? Профессор, я не понимаю..."
        m "Что вы не понимаете, мисс Грейнджер?"
        m "Вам нужны эти очки или нет?"
        $herView.hideQQ()
        $herView.showQQ( "body_31.png", pos )
        her  "Нужны..."
        m "Значит приподнимайте свою юбку..."
        $herView.hideQQ()
        $herView.showQQ( "body_47.png", pos )
        her "............."
    else:
        if request_02 >= 1: #Not the first time
            $herView.hideQQ()
            $herView.showQQ( "body_29.png", pos )
            her "Ох... снова?"
            m "Просто сделай это..."
        $herView.hideQQ()
        $herView.showQQ( "body_29.png", pos )
        her ".................."
        
        

    hide screen bld1
    $herView.hideQ( d5 )
    $ menu_x = 0.5 #Default menu position restored.
    if whoring <= 2:    #angry with pants
        show screen hermione_lift_skirt_angry
        with d3
    elif whoring <= 5:
        show screen hermione_lift_skirt_normal #Hermione lifts her skirt WITH pants
        with d3
    else: #whoring >= 6: # no panties
        show screen hermione_lift_skirt_no_panties
        with d3
        
        
    #play music "music/Under-the-Radar by PhobyAk.mp3" fadein 1 fadeout 1 
    play music "music/(Orchestral) Playful Tension by Shadow16nh.mp3" fadein 1 fadeout 1 

    if whoring >= 0 and whoring <= 2: #LEVEL 01
        $her_head_state = 8
        her_head_main "........................"
    elif whoring >= 3 and whoring <= 5: #LEVEL 02
        $her_head_state = 14
        her_head_main "....................."
    elif whoring >= 6: #LEVEL 03 and up.
        $her_head_state = 18
        her_head_main ".........................."
        g4 "!!?"
        
        

    # save previous state and add pose
    # add pose with lifted skirt
    $herView.data().saveState()
    $herView.data().addPose( CharacterExItemSkirtLifted( herView.mPoseFolder, 'pose_skirt_up.png', G_Z_POSE ) )
    $ pos = POS_120
    
    if whoring >= 0 and whoring <= 2: #LEVEL 01   <============================= Fist event.
        $ new_request_02_01 =  True #Hearts.
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
                ">Вы задаетесь вопрос о том, что происходит у нее в голове сейчас."
                $herView.hideQQ()
                $herView.showQQ( "body_51.png", pos )
                her "......................."
                pause
            "- Смотреть на ее трусики -":
                ">Просто женское белье..."
                pause
                $herView.hideQQ()
                $herView.showQQ( "body_51.png", pos )
                her "......................."
               

    elif whoring >= 3 and whoring <= 5: #LEVEL 02  <====================================================================== SECOND EVENT!
        $ new_request_02_02 =  True #Hearts.
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
            "\"Вы не выглядите смущенно...\"":
                $herView.hideQQ()
                $herView.showQQ( "body_53.png", pos )
                her "Это не так..."
                $herView.hideQQ()
                $herView.showQQ( "body_54.png", pos )
                her "Это сравнительно небольшая плата, если \"Гриффиндор\" получит кубок в этом году."
                her "Я знаю, что все будут счастливы..."
                pause
            "\"Мне нравятся ваши трусики...\"":
                $herView.hideQQ()
                $herView.showQQ( "body_53.png", pos )
                her "Спасибо, профессор..."
            "- Продолжать смотреть в ее глаза -":
                $herView.hideQQ()
                $herView.showQQ( "body_55.png", pos )
                her ".............................."
                her "...........................?"
                $herView.hideQQ()
                $herView.showQQ( "body_56.png", pos )
                her "................................"
                $herView.hideQQ()
                $herView.showQQ( "body_57.png", pos )
                her "Профессор, пожалуйста... Вы смущаете меня."
                

    elif whoring >= 6: #LEVEL 04 and up. <====================================================================== FINAL EVENT! (No Трусики).
        $ new_request_02_03 =  True #Hearts.
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
        $herView.hideQQ()
        $herView.showQQ( "body_59.png", pos )
        her "Ох, в последнее время я не очень хочу носить их..."
        menu:
            "\"Ах ты маленькая шлюха!\"":
                her "Хм..."
                $herView.hideQQ()
                $herView.showQQ( "body_58.png", pos )
                her "Вероятно это так..."
                her "Могу я получить чуть больше очков за это?"
                menu:
                    "\"Конечно!\"":
                        m "Конечно!"
                        $ gryffindor +=10
                        m "Десять очков \"Гриффиндору\"!" 
                        $herView.hideQQ()
                        $herView.showQQ( "body_60.png", pos )
                        her "Спасибо вам, сэр!"
                    "\"Категорически нет!\"":
                        $ mad +=15
                        $herView.hideQQ()
                        $herView.showQQ( "body_61.png", pos )
                        her ".............................."
                        $herView.hideQQ()
                        $herView.showQQ( "body_62.png", pos )
                        her "Не будьте так скупы, профессор."   
            "\"Отлично. Пять очков Гриффиндору!\"":
                pass           
    
    
    
    stop music fadeout 4.0
    
    label request_02_done:
    $ gryffindor +=5
    m "Пять очков  \"Гриффиндору\", мисс Грейнджер. Отличная работа." 
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

    if request_02 == 0: #First time.
        $herView.hideQQ()
        $ pos.xpos = 300
        $herView.showQQ( "body_13.png", pos )
        her "Еще пять очков..."
        her "Не дождусь рассказать ребятам!"
        $herView.hideQQ()
        $herView.showQQ( "body_12.png", pos )
        her "Только я не могу рассказать о всем, что пришлось сделать для этого..."
    
    if daytime:
        her "Ну, мои занятия вот-вот начнутся..."
    else:
        her "Уже довольно поздно, сэр... Мне нужно идти..."

    
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



    if whoring <= 2:
        $ whoring +=1
    $ request_02 += 1
    if daytime:
        $ hermione_takes_classes = True
        jump day_main_menu
    else:
        $ hermione_sleeping = True
        jump night_main_menu

