    
##################################################################################################################################
### LEVEL 04 #####################################################################################################################
###################REQUEST_11 (Level 04) (DANCE FOR ME AND SNAPE) (Day/Night) ################################################################
label new_request_11: #LV.4 (Whoring = 9 - 11)
    $herView.hideQQ()
   
    m "{size=-4}(Попросить её станцевать для вас?){/size}"

    $ menu_x = 0.5 #Default position of the menu (0.5). Version B is $ menu_x = 0.2
    menu:
        "\"(Да, давай попробуем!)\"":
            show screen blktone
            with d3
            pass
        "\"(Не сейчас.)\"":
            jump new_personal_request

    $ current_payout = 35 #Because will have option to pay extra.

    $ herView.data().saveState()
    $ herView.data().addItem( 'sweat', CharacterExItemSweat( herView.mMiscFolder, "sweat.png", G_Z_POSE - 1 ) )

    if request_11_points == 0: #<==============================EVENT 01
        
        m "Мисс Грейнджер, не могли бы вы станцевать для меня."
        $herView.hideQQ()
        $ pos = POS_140
        $herView.showQQ( "body_11.png", pos )
        her "Вы хотите, чтобы я..."
        $herView.hideshowQQ( "body_10.png", pos )
        her "...танцевала для вас, сэр?"
        if whoring <= 8:
            jump too_much
        $ new_request_11_01 = True # HEARTS
        m "Да... как вы думаете, вы сможете справиться с этим?"
        her "Эм... Я попробую..."
        $herView.hideshowQQ( "body_11.png", pos )
        her "Это ваше официальное предложение, сэр?"
        with hpunch
        g4 "Что ты сказала!?"
        stop music fadeout 1.0
        $herView.hideshowQQ( "body_12.png", pos )
        her "Я имею в виду, пользу. Это в пользу школы, сэр?"
        show screen whitetone8
        hide screen blktone
        with Dissolve(1)
        $herView.hideQ( Dissolve( 1 ) )
        g4 "(\"Это ваше официальное желание, мастер....?\")"
        m "(О, это вызывает воспоминания...)"
        m "(Аграба и Джини...)"
        m "(Пре-акабурная эра моей жизни...)"
        m "(Неплохие времена...)"
        g4 "(Сволочь, испортил мне жизнь!)"
        her "Eм... Профессор?"
        hide screen whitetone8
        with Dissolve(1)
        $herView.showQQ( None, pos )
        call music_block
        her "сэр..?"
        m "Так, Гермиона..."
        m "Я предался воспоминаниям..."
        her "Я получу за это награду?"
        m "Конечно, девочка!"
        $herView.hideshowQQ( "body_29.png", pos )
        her "Так... я просто немного потанцую..."
        m "Начинай, когда будешь готова..."
        her "................."
        $herView.hideQQ()
        ">Гермиона начинает танцевать..."
        stop music fadeout 1.0
        hide screen blktone
        $ hermione_chibi_xpos = 400 #Near the desk.
        #$ hermione_chibi_ypos = 240 #Default: 250
        show screen clothed_dance #Hermione stands still.
        with fade
        m "Хм..."
        $her_head_state = 12
        her_head_main "{size=-5}(...........................................){/size}"
        $her_head_state = 4
        her_head_main "{size=-5}(Это глупо...){/size}"
        ">Гермиона выглядит растерянной, но она продолжает \"танцы\"..."
        m "..................."
        her_head_main "{size=-5}(...........................................){/size}"
        m "Отлично, теперь можешь начинать раздеваться."
        show screen hermione_02 #Hermione stands still.
        with hpunch
        $her_head_state = 7
        her_head_main "??!"
        $her_head_state = 8
        her_head_main "Мы же договаривались только о танце?"
        play music "music/(Orchestral) Playful Tension by Shadow16nh.mp3" fadein 1 fadeout 1 # SEX THEME.
        m "В самом деле? Вот обидно."
        m "Теперь начинай снимать свою одежду."
        $her_head_state = 12
        her_head_main "Вы хотите, чтобы я станцевала вам стриптиз...?"
        m "Да. И я ожидаю, что ты сделаешь это сегодня, девочка."
        $her_head_state = 19
        her_head_main "Профессор Дамблдор!"
        m "Не повышай на меня голос, девочка!"
        $her_head_state = 7
        her_head_main ".....!!?"
        m "Никто не заставляет тебя делать это."
        m "Я делаю тебе одолжение!"
        m "Если тебе не нужны очки, пожалуйста, не задерживайся в кабинете."
        $her_head_state = 8
        her_head_main "....................."
        $her_head_state = 12
        her_head_main "......................................."
        ">Гермиона начинает танцевать снова..."
        show screen clothed_dance #Hermione stands still.
        with fade
        $her_head_state = 15
        her_head_main "{size=-5}(...........................................){/size}"
        m "И чего же мы теперь ждем?"
        m "Начните с жилета."
        $her_head_state = 12
        her_head_main "............................................................."
        ">Гермиона сконфуженно смотрит на вас и снимает с жилет..."
        show screen ctc
        pause
        show screen no_vest_dance
        with d3
        pause
        $her_head_state = 19
        her_head_main "{size=-5}(Я действительно собираюсь сделать это?){/size}"
        menu:
            m "......................."
            "\"Теперь избавься от юбки!\"":
                her_head_main "................................."
                show screen blktone
                with d3
                ">Гермиона начинает расстегивать юбку..."
                ">Она очень смущена, поэтому у нее это сразу не получается..."
                ">Наконец, молния расстегнута и Гермионе остается только снять юбку..."
                hide screen blktone
                with d3
                her_head_main "{size=-5}(Ох, мне придется это сделать...){/size}"
                $her_head_state = 24
                her_head_main "{size=-5}(За честь \"Гриффиндора\"....){/size}"
                ">Гермиона сняла юбку и положила ее на пол..."
                show screen ctc
                pause
                show screen no_skirt_dance
                with d3
                pause
                m "..............."
                $her_head_state = 19
                her_head_main "{size=-5}(.........................................){/size}"
                ">Гермиона продолжает танцевать..."
                m "Ладно, рубашка следующая!"
                $her_head_state = 20
                her_head_main "Моя рубашка....?"
                show screen blktone
                with d3
                ">Гермиона ужасно сконфужена..."
                ">Она неуклюже копошится с пуговицами рубашки..."
                hide screen blktone
                with d3
                m "В чем проблема, девочка?"
                $her_head_state = 19
                her_head_main "Извините, сэр..."
                her_head_main "Пуговица застряла..."
                her_head_main "И не хочет расстегиваться..."
                $her_head_state = 28
                her_head_main "Почему она не расстегивается?! *хлюп*"
                her_head_main "Нет, я не могу сделать этого, сэр! *хлюп*"
                m "Что?"
                her_head_main "Я думала, я смогу, но..."
                her_head_main "Станцевать стриптиз, сэр?"
                her_head_main "Люди равняются на меня в этой школе!"
                her_head_main "У меня репутация...*хлюп*"
                $her_head_state = 29
                her_head_main "И если я сделаю это..."
            "\"Сейчас же сними рубашку!\"":
                $her_head_state = 19
                her_head_main "................................."
                show screen blktone
                with d3
                ">Гермиона начинает расстегивать свою рубашку..."
                ">Она кажется очень нерешителной и тянет время..."
                ">Наконец, последняя пуговица снята, и у нее нет выбора, кроме как снять рубашку..."
                hide screen blktone
                with d3
                her_head_main "{size=-5}(Ладно, снимаю...){/size}"
                her_head_main "{size=-5}(За честь \"Гриффиндора\"!){/size}"
                show screen blktone
                with d3
                ">Гермиона сняла с себя рубашку..."
                hide screen blktone
                with d3
                show screen ctc
                pause
                show screen no_shirt_dance
                with d3
                pause
                $her_head_state = 40
                her_head_main "{size=-5}(Я сделала это...){/size}"
                her_head_main "{size=-5}(Профессор Дамблдор видит мою грудь, пока я танцую...){/size}"
                her_head_main "{size=-5}(Это так унизительно...){/size}"
                her_head_main "{size=-5}(Но я делаю это для моего факультета...){/size}"
                m "Неплохо...."
                her_head_main "{size=-5}(.........................................){/size}"
                show screen blktone
                with d3
                ">Гермиона топлес..."
                ">Она продолжает танцевать, но, кажется, она очень стеснена в движениях. Даже больше, чем раньше..."
                ">Похоже, она отчаянно пытается предотвратить покачивания и подпрыгивания её груди.."
                hide screen blktone
                with d3
                m "Ладно, юбка следующая!"
                her_head_main "...................."
                show screen blktone
                with d3
                ">Гермиона выглядит крайне растерянной..."
                show screen blktone8
                with d3
                ">Она пытается расстегнуть молнию на юбке..."
                m "Какие-то проблемы, девочка?"
                her_head_main "Мне жаль, сэр..."
                her_head_main "Она застряла..."
                her_head_main "Не двигается..."
                her_head_main "Почему она не двигается? *всхлип*"
                $her_head_state = 41
                her_head_main "Нет, я не могу, сэр! *всхлип*"
                m "Что?"
                her_head_main "Я думала, что смогу, но..."
                her_head_main "Стриптиз за очки, сэр?"
                her_head_main "Люди равняются на меня в этой школе!"
                her_head_main "У меня есть репутация...*всхлип*"
                $her_head_state = 42
                her_head_main "И если я это сделаю..."
                
        menu:
            "\"Кого волнует твоя репутация?\"":
                m "Кого волнует твоя репутация? Продолжай раздеваться!"
                $ end.SetEndingValue(const_ENDING_STRONG_GIRL,1)
            "Тут никого нет":
                m "Ну, тут никого нет и твоей репутации ничего не угрожает."        


        show screen blkfade 
        with d3
        hide screen blktone8    
        ">Гермиона быстро одевает свою форму..."
        stop music fadeout 1.0
        show screen hermione_02 #Hermione stands still.
        hide screen blkfade
        with d3
        $her_head_state = 31
        her_head_main "Сэр, я думаю мне стоит уйти... *всхлип!*"
        menu:
            "\"Ладно. Мне было весело. Вот твои очки.\"":
                $herView.setZOrder( 8 )
                $ pos = gMakePos( 390, 340 )
                $herView.showQ( "body_13.png", pos )
                her2 "Правда? Я ничего не испортила?"
                $herView.hideQ()
                pause.2 #Otherwise a bug occurs. 
                $herView.setZOrder( 5 )
                $ pos = gMakePos( 390, 0 )
            "\"Конечно. И ты не получишь очки.\"":
                play music "music/Chipper Doodle v2.mp3" fadein 1 fadeout 1 # HERMIONE'S THEME.
                $herView.setZOrder( 8 )
                $ pos = gMakePos( 390, 340 )
                $herView.showQ( "body_02.png", pos )
                her2 "сэр... Мне кажется, я не очень хороша в этом..."
                her2 "НО я сделала все, что смогла... Я думаю, я заслужила--"
                $herView.hideQ()
                m "Просто в следующий раз постарайтесь лучше, Мисс Грейнджер."
                $herView.showQ( "body_31.png", pos )
                her2 "Следующий раз?!"
                $herView.hideQ()
                $herView.showQ( "body_47.png", pos )
                her2 "Уверяю вас, сэр, следующего раза не будет..."
                $herView.hideQ()
                m "Посмотрим..."
                $herView.showQ( "body_66.png", pos )
                her2 "Арх!"
                $herView.hideQ()
                pause.2 #Otherwise a bug occurs. 
                $herView.setZOrder( 5 )
                $ pos = gMakePos( 390, 0 )
                $ mad += 35
                call music_block
                jump restore_state_could_not_flirt

    # SECOND PART #

    if request_11_points == 1: #<====================================================================================================================EVENT 02 
        $ new_request_11_02 = True # HEARTS
        m "Мисс Грейнджер, я хочу, чтобы вы станцевали для меня."
        $herView.hideQQ()
        $ pos = POS_140
        $herView.showQQ( "body_66.png", pos )
        her "Снова, сэр...?"
        m "Все будет оплачено, конечно же..."
        $herView.hideshowQQ( "body_69.png", pos )
        her "............................"
        $herView.hideshowQQ( "body_69.png", pos )
        her "И вы ожидаете от меня... Эм..."
        m "Стриптиз, конечно же."
        $herView.hideshowQQ( "body_69.png", pos )
        stop music fadeout 1.0
        her "......................"
        $herView.hideshowQQ( "body_66.png", pos )
        play music "music/Chipper Doodle v2.mp3" fadein 1 fadeout 1 # HERMIONE'S THEME.
        her "Ну, почему бы и нет?"
        $herView.hideshowQQ( "body_86.png", pos )
        her "Да, и правда, почему бы и нет!"
        m "Хм...? {size=-4}(Посмотрите на нее. Такая энергичная...){/size}"
        $herView.hideshowQQ( "body_30.png", pos )
        her "В конце концов, как ученица, я должна подчиняться любому вашему приказу, не так ли, сэр?!"
        m "...................."
        $herView.hideshowQQ( "body_30.png", pos )
        her "Если директор говорит мне раздеться, то, значит, я должна раздеться!!!"
        $herView.hideshowQQ( "body_47.png", pos )
        her "Считать это неуместным, позорным и унизительным?"
        $herView.hideshowQQ( "body_30.png", pos )
        her "Конечно же, нет! Какой вздор!"
        m ".............."
        $herView.hideshowQQ( "body_47.png", pos )
        her "Ха! Все ведь так, как и должно быть!"
        $herView.hideQQ()
        hide screen blktone 
        with d3
        m "??!"
        hide screen bld1
        with d3
        $ walk_xpos=400 #Animation of walking chibi. (From)
        $ walk_xpos2=280 #Coordinates of it's movement. (To)
        $ hermione_speed = 03.0 #The speed of moving the walking animation across the screen.
        show screen hermione_walk_01 
        pause 1
        show screen blkfade
        with Dissolve(1)
        $ renpy.play('sounds/08_hop_on_desk.mp3') #Sound of the desk squeaking. 
        pause 5
        g4 "!!!!!!"
        ">К вашему удивлению, Гермиона взбирается на ваш стол и начинает безумно танцевать..."
        hide screen blkfade
        $ hermione_chibi_xpos = 210 #Near the desk: 400.
        $ hermione_chibi_ypos = 180 #Default: 250
        show screen clothed_dance #Hermione stands still.
        show screen ctc
        with fade
        pause
        show screen bld1
        show screen blktone
        with d3
        $herView.setZOrder( 8 )
        $ pos = gMakePos( 390, 340 )
        $herView.showQ( "body_30.png", pos )
        her2 "Если я должна немного опуститься, чтобы защитить честь своего факультета..."
        $herView.hideQ()
        ">Гермиона начинает снимать свой жилет..."
        $herView.showQ( "body_86.png", pos )
        her "Пусть так и будет!"
        $herView.hideQ()
        $herView.showQ( "body_87.png", pos )
        her "Просто..."
        $herView.hideQ()
        $herView.showQ( "body_88.png", pos )
        her "*стон*"
        $herView.hideQ()
        show screen blktone8
        hide screen blktone
        with d3
        ">Ее жилет, кажется, застрял. Но она рьяно пытается сорвать его с себя..."
        $herView.showQ( None, pos )
        her "Почему он не....?!"
        $herView.addFaceName( "body_81.png" )
        her "Вот!"
        $herView.hideQ()
        ">Гермионе наконец удается стянуть жилет и она швыряет его в противоположную часть комнаты..."
        hide screen blktone8
        with d3
        hide screen bld1
        with d3
        show screen ctc
        pause
        show screen no_vest_dance
        with d3
        pause
        show screen bld1
        with d3
        $herView.showQ( "body_30.png", pos )
        hide screen ctc
        her "Юбка следующая, да?"
        $herView.hideQ()
       
        menu:
            m "..."
            "\"Да, именно. Снимай ее!\"":
                $herView.showQ( None, pos )
                her "Конечно!"
                $herView.addFaceName( "body_87.png" )
                her "А вот и она!"
                $herView.hideQ()
                pause.1
                show screen blktone8
                with d3
                ">Гермиона бросает свою юбку через всю комнату, как сделала это с жилетом ранее..."
            "\"Успокойся, девочка. \"":
                $herView.showQ( None, pos )
                her2 "Ну, {size=+7}ПРОСТИТЕ МЕНЯ{/size}, профессор!"
                her2 "Вы попросили меня станцевать стриптиз для вас, но не предупреждали, насколько громкой я должна быть!"
                $herView.hideQ()
                m "Ну, я говорю это сейчас!"
                $herView.showQ( None, pos )
                her2 "Слишком поздно!"
                $herView.hideQ()
                pause.1
                show screen blktone8
                with d3
                ">И она бросает свою юбку через всю комнату, как сделала это с жилетом ранее..."
        hide screen blktone8
        with d3
        hide screen bld1
        with d3
        show screen ctc
        show screen no_skirt_dance
        with d3
        pause
        show screen bld1
        with d3
        hide screen ctc
        m "{size=-4}(Вау, она и правда поработала над этим...){/size}"
        m "{size=-4}(Может быть, еще рано для-{/size}"
        $herView.showQ( "body_66.png", pos )
        her "Моя рубашка?!!"
        $herView.addFaceName( "body_86.png" )
        her "{size=+9}Мне она не нужна!{/size}"
        $herView.hideQ()
        pause.1
        show screen blktone8
        with d5
        ">Ее рубашка внезапно спадает на пол."
        g4 "{size=-4}(Когда она успела??!){/size}"
        hide screen blktone8
        with d3
        hide screen bld1
        with d3
        show screen ctc
        pause
        show screen no_shirt_no_skirt_dance
        with d3
        pause
        show screen bld1
        with d3
        $herView.showQ( None, pos )
        hide screen ctc
        her "Вам нравится, сэр?"
        $herView.addFaceName( "body_30.png" )
        her2 "Мне стоит потрясти сиськами, как одна из тех шлюх?"
        $herView.hideQ()
        m "Ну---"
        $herView.showQ( "body_30.png", pos )
        her2 "Конечно! Почему бы мне не опуститься для вашего удовольствия?!"
        $herView.addFaceName( "body_86.png" )
        her2 "Это совершенно {size=+7}приемлемо!{/size}"
        $herView.hideQ()
        pause.1
        show screen blktone
        with d3
        ">Гермиона начинает неуклюже трясти своими сиськами..."
        ">Пока вы смотрите, как сиськи этой девочки расскачиваются влево-вправо перед вашим лицом, вам приходится бороться с сильным желанием..."
        menu:
            m "..."
            "- Схватить их! -":
                g9 "{size=-4}(Да, просто положить свои руки на эти милые сиськи, именно!){/size}"
                g9 "{size=-4}(Может, чуть подергать их...){/size}"
            "- Шлепнуть! -":
                m "{size=-4}(О да, хочу шлепнуть их.){/size}"
                g9 "{size=-4}(Да, просто немного шлепнуть...){/size}"
            "- Укусить!":
                m "{size=-4}(Это странно, что я хочу впиться в них зубами?){/size}"
                m "{size=-4}(Нет, это не странно!){/size}"
                m "{size=-4}(Просто пара нежных укусов с любовью!){/size}"
                g9 "{size=-4}(Да... Может быть, больше чем пара...){/size}"
            "- Зарыться в них лицом! -":
                m "{size=-4}(Я просто хочу залезть лицом между ними!){/size}"
                g9 "{size=-4}(Да, зарыться в них лицом это лучшее, что можно сделать!){/size}"
        ">Пока вы думаете, Гермиона продолжает танцевать..."
        
        call req11_undress
        $ pos = gMakePos( 390, 235 )
        $herView.showQ( "body_89.png", pos )
        her2 "(Танцую голой перед директором...)"
        her2 "(Если бы мои родители узнали об этом, они бы просто сошли с ума...)"
        $herView.addFaceName( "body_90.png" )
        her2 "(Особенно отец...)"
        $herView.hideQ()
        ">Гермиона снова трясет своими грудками..."
        $herView.showQ( "body_90.png", pos )
        her "(Гермиона Грейнджер - стриптизерша...)"
        $herView.addFaceName( "body_91.png" )
        her2 "(Прости меня, папочка...)"
        $herView.hideQ()
        pause.1
        show screen blktone8
        hide screen blktone
        with d3
        ">Гермиона кладет свои руки на грудь и начинает сжимать ее..."
        ">Вы можете только предполагать, что у нее на уме, но выглядит она очень подавленно и смущенно."
        $herView.showQ( "body_91.png", pos )
        her2 "(Я лучший студент... Я являюсь примером для других...)"
        $herView.hideQ()
        ">Гермиона сильнее хватается за сиськи и скручивает их пару раз..."
        ">Выглядит так, будто она зла на них и пытается наказать..."
        ">Это выглядит станным, но возбуждающим..."
        $herView.showQ( "body_92.png", pos )
        $ h_c_u_pic = "03_hp/08_animation_02/05_panties_01.png"
        show screen h_c_u
        her "Ну, я думаю, вам это нравится, сэр!"
        $herView.hideQ()
        m "Что?"
        $herView.showQ( "body_93.png", pos )
        her "Я хотела бы получить оплату..."
        $herView.hideQ()
        m "Вы ничего не забыли, Мисс Грейнджер?"
        $herView.showQ( "body_92.png", pos )
        her2 "сэр...?"
        $herView.hideQ()
        m "Ваши трусики...?"
        $herView.showQ( "body_94.png", pos )
        her "Мои трусики?"
        her "Но, они всегда остаются!"
        $herView.hideQ()
        m "Когда это \"всегда\"?"
        m "Стриптиз в детских мультиках?"
        m "Стриптиз это стриптиз, девочка!"
        m "Теперь, снимай свои трусики!"
        $herView.showQ( "body_95.png", pos )
        her "................"
        $herView.hideQ()
        ">Гермиона выглядит испуганно. Вся ее злоба ушла..."
        $herView.showQ( "body_90.png", pos )
        her "................."
        $herView.hideQ()
        ">Не говоря ни слова..."
        ">Она начинает снимать свои трусики..."
        g9 "......................................."
        $ renpy.play('sounds/door.mp3') #Sound of a door opening.
        $ snapes_speed = 02.0 #The speed of moving the walking animation across the screen.
        $ walk_xpos=470 #Animation of walking chibi. (From)
        $ walk_xpos2=360 #Coordinates of it's movement. (To)
        hide screen blktone8
        hide screen bld1
        show screen snape_walk_01 
        with d3
        pause 1.5
        stop music 
        $ renpy.play('sounds/scratch.wav')
        show screen snape_02 #Snape stands still.
        
        $ posHead = gMakePos( pos.xpos, pos.ypos )
        
        $ tt_xpos=330 #Defines position of the Snape's full length sprite. (Default 300). 140 - center.
        $ tt_ypos=340#(Default 0). Right bottom corner: 340
        $ s_sprite = "03_hp/10_snape_main/snape_01.png"
        show screen s_head
        $ h_c_u_pic = "03_hp/08_animation_02/05_panties_01.png"
        show screen h_c_u
               
        sna2 "Послушай, Джинни. Я тут подумал--"
        $ s_sprite = "03_hp/10_snape_main/snape_11.png"
        with hpunch
        sna2 "................................................................................................................................................................................"
        
        # add black-white hermione as a pose, higher then face
        $herViewHead.data().addPose( CharacterExItem( herViewHead.mPoseFolder, 'hermione_bw_strip.png', G_Z_FACE + 1 ) )
        $herViewHead.showQ( "body_96.png", posHead )
        with hpunch
        her "(Профессор Снейп???????!)"
        $ s_sprite = "03_hp/10_snape_main/snape_12.png"
        show screen s_head
        sna2 "Мисс Грейнджер?"
        hide screen s_head
        $herViewHead.showQ( "body_96.png", posHead )
        her "(Нет, нет... Этого не может быть... Пожалуйста...)"
        $herViewHead.hideQ()
        $herViewHead.data().delPose()
        play music "music/(Orchestral) Playful Tension by Shadow16nh.mp3" fadein 1 fadeout 1 # SEX THEME.
        m "...................................."
        show screen bld1
        with d3
        menu:
            m "..."
            "\"Северус, Я сейчас занят.\"":
                $ s_sprite = "03_hp/10_snape_main/snape_13.png"
                show screen s_head
                sna "Да... Я вижу..."
                $herViewHead.showQ( "body_97.png", posHead )
                her "{size=-7}(Я хочу сдохнуть!){/size}"
                $ s_sprite = "03_hp/10_snape_main/snape_12.png"
                show screen s_head
                sna2 "Отложим наш разговор на потом, Джинн-- *Кхм!* Альбус."
                $ s_sprite = "03_hp/10_snape_main/snape_13.png"
                sna "Мисс Грейнджер..."
                $herViewHead.showQ( "body_97.png", posHead )
                her ".........................................."
                $herViewHead.hideQ()
            "\"Северус! Пожалуйста, присоединяйся.\"":
                $ mad += 37
                $ snape_invated_to_watch = True #Turns TRUE when Hermione is stripping and Snape walks in on you. Allows to invite him to watch her strip next time.
                $ s_sprite = "03_hp/10_snape_main/snape_14.png"
                show screen s_head
                sna "Серьезно?"
                $herViewHead.showQ( "body_97.png", posHead )
                her "(Профессор, нет, пожалуйста.............................)"
                $ s_sprite = "03_hp/10_snape_main/snape_13.png"
                show screen s_head
                sna "Действительно, заманчивое предложение..."
                $herViewHead.showQ( "body_95.png", posHead )
                her "!!!!!!......."
                $ s_sprite = "03_hp/10_snape_main/snape_13.png"
                show screen s_head
                sna2 "Но я откажусь... Может, в другой раз..."
                $herViewHead.showQ( "body_99.png", posHead )
                her "{size=-5}(Другого раза не будет!){/size}"
                her "{size=-5}(Клянусь, я перестану продавать себя за эти гребаные очки!){/size}"
                $ s_sprite = "03_hp/10_snape_main/snape_12.png"
                show screen s_head
                sna2 "Отложим наш разговор, Джинн-- *Кхм!* Альбус."
                $ s_sprite = "03_hp/10_snape_main/snape_13.png"
                sna2 "Мисс Грейнджер..."
                $herViewHead.showQ( "body_97.png", posHead )
                her "................................."
                $herViewHead.hideQ()
        show screen blkfade 
        with d3
        hide screen snape_walk_01 
        $ renpy.play('sounds/door.mp3') #Sound of a door opening.
        pause 1.5

        
        ">Снейп уходит..."
        ">Гермиона спешно спрыгивает с вашего стола."
        ">Она отчаянно пытается натянуть на себя одежду..."
        $herViewHead.showQ( "body_98.png", posHead )
        her "Моя рубашка! Где моя рубашка?!"
        $herViewHead.hideQ()
        m "Там, у камина..."
        pause 1

        call req11_dress
        $herViewHead.data().addPose( CharacterExItemPoseShowTits( herViewHead.mPoseFolder, 'pose_dress_up.png', G_Z_POSE ) )
        $herViewHead.showQ( "body_85.png", posHead )
        her2 "................................"
        $herViewHead.hideQ()
        pause 2
        $herViewHead.data().delPose()
        $herViewHead.showQ( "body_33.png", posHead )
        
        
        her "........................"
        stop music fadeout 2.0
        her "Могу я получить свои очки, пожалуйста?"
        $herViewHead.hideQ()
        hide screen snape_02 #Snape stands still.
        pause.1
        $herView.setZOrder( 5 )
        
        $ pos = gMakePos( pos.xpos, 0 )
        $ hermione_chibi_xpos = 400 #Near the desk.
        show screen hermione_02 #Hermione stands still.
        $ hermione_chibi_ypos = 250 #Default: 250. Another number is 180
            
            
    # THIRD PART #
            
    if request_11_points >= 2: #<====================================================================================================================EVENT 03
        $ new_request_11_03 = True # HEARTS
        if snape_invated_to_watch: #Turns TRUE when Hermione is stripping and Snape walks in on you. Allows to invite him to watch her strip next time.
            m "(Хм... могу ли я позвать Снейпа тоже посмотреть на это?)"
            menu:
                "\"Да! Гермионе нужна аудитория!\"":
                    if not invited_snape_once_already:
                        $ invited_snape_once_already = True #Makes sure this event takes place only once.
                        hide screen blktone
                        with d3
                        m "Мисс Грейнджер, я хочу от вас еще одну услугу сегодня."
                        $herView.hideQQ()
                        $ pos = POS_140
                        $herView.showQQ( "body_16.png", pos )
                        her "Конечно, сэр."
                        m "Но для начала, вы не могли бы пойти и позвать профессора Снейпа сюда?"
                        $herView.hideshowQQ( "body_17.png", pos )
                        her "...Профессора Снейпа?"
                        her "Могу я спросить, зачем, сэр?"
                        m "Ох, я думаю, вам нужна аудитория побольше для подобных танцев."
                        $herView.hideshowQQ( "body_48.png", pos )
                        her "Подобных танцев...?!!"
                        $herView.hideshowQQ( "body_47.png", pos )
                        her "Со всем уважением, сэр..."
                        $herView.hideshowQQ( "body_07.png", pos )
                        her "{size=-5}(Которого уже и так мало...){/size}"
                        $herView.hideshowQQ( "body_30.png", pos )
                        her "Я отказываюсь унижаться перед профессором Снейпом!"
                        m "Нет, нет. Ты все не так поняла."
                        $herView.hideshowQQ( "body_15.png", pos )
                        her "Хм..?"
                        m "Я хочу проверить профессора Снейпа на причастность к \"грязным\" делишкам с помощью тебя."
                        $herView.hideshowQQ( "body_48.png", pos )
                        her "!!!"
                        m "Да, хочу поймать его на месте преступления!"
                        $herView.hideshowQQ( "body_11.png", pos )
                        her "Профессор, Я не понимаю..."
                        $herView.hideshowQQ( "body_06.png", pos )
                        her "Хм... хотя.... теперь ясно..."
                        her "Я извиняюсь, что засомневалась в вас, сэр..."
                        m "Ничего. Теперь найди профессор Снейпа и приведи его сюда."
                        $herView.hideshowQQ( "body_111.png", pos )
                        her "Как скажете, сэр!"
                        label fetching_snape:
                        $herView.hideQQ()
                        hide screen bld1
                        with d3
                        hide screen hermione_02 #Hermione stands still.
                        $ walk_xpos=400 #Animation of walking chibi. (From)
                        $ walk_xpos2=610 #Coordinates of it's movement. (To)
                        $ hermione_speed = 02.0 #The speed of moving the walking animation across the screen.
                        show screen hermione_walk_01_f 
                        pause 2
                        hide screen hermione_walk_01_f 
                        $ renpy.play('sounds/door.mp3') #Sound of a door opening.
                        with Dissolve(.3)
                        pause.2
                        show screen blkfade
                        with d5
                        stop music fadeout 1.0
                        ">...................{w}...................{w}...................{w}..................."
                        hide screen blkfade
                        with d5
                        $ walk_xpos=610 #Animation of walking chibi. (From)
                        $ walk_xpos2=360 #Coordinates of it's movement. (To)
                        $ snapes_speed = 04.0 #The speed of moving the walking animation across the screen.
                        show screen snape_walk_01 
                        
                        pause 4
                        show screen snape_02 #Snape stands still.

                        $ renpy.play('sounds/door.mp3') #Sound of a door opening.
                        $ hermione_chibi_xpos = 610
                        $ hermione_chibi_ypos = 250
                        show screen hermione_02 #Hermione stands still.
                        with Dissolve(.5)
                        pause.3
                        
                        $ walk_xpos=610 #Animation of walking chibi. (From)
                        $ walk_xpos2=500 #Coordinates of it's movement. (To) 400 - near desk.
                        $ hermione_speed = 03.0 #The speed of moving the walking animation across the screen.
                        show screen hermione_walk_01 
                        pause 3
                        $ hermione_chibi_xpos = 500 #Near the desk - 400
                        show screen hermione_02 #Hermione stands still.
                        pause.5
                        show screen ctc
                        pause
                        show screen bld1
                        with Dissolve(.3)
                        $ tt_xpos=180 #Defines position of the Snape's full length sprite. Default - 300
                        $ tt_ypos=0
                        $ s_sprite = "03_hp/10_snape_main/snape_01.png"
                        show screen snape_main
                        show screen ctc
                        with Dissolve(.3)
                        
                    else:
                        hide screen blktone
                        with d3
                        m "Мисс Грейнджер, Я хочу от вас еще одну услугу сегодня."
                        $herView.hideQQ()
                        $ pos = POS_140
                        $herView.showQQ( "body_16.png", pos )
                        her "Конечно, сэр."
                        m "Но, для начала, вы не могли бы пойти и позвать профессора Снейпа сюда?"
                        $herView.hideshowQQ( "body_17.png", pos )
                        her "...Профессор Снейп?"
                        her "Могу я спросить, зачем, сэр?"
                        m "Ох, я просто хочу, чтобы ты станцевала для нас."
                        $herView.hideshowQQ( "body_14.png", pos )
                        her "!!!"
                        m "Я хочу проверить профессора Снейпа на причастность к \"грязным\" делишкам и ты должна мне помочь."
                        $herView.hideshowQQ( "body_29.png", pos )
                        her "Но разве мы не договаривались, что я делаю это в последний раз?"
                        m "Ну, эм... конечно..."
                        m "Но мне нужны доказательства, если я хочу отправить это в министерство магии!"
                        $herView.hideshowQQ( "body_47.png", pos )
                        her "....."
                        m "Ну, что ты скажешь, девочка?"
                        m "Один танец для большей справедливости?"
                        $herView.hideshowQQ( "body_66.png", pos )
                        her "Ну, ладно..."
                        m "Отлично. Тогда пойди и найди профессора Снейпа."
                        jump fetching_snape
                    
                    play music "music/Dark Fog.mp3" fadein 1 fadeout 1 # SNAPE'S THEME
                    sna "Джинни... э-э, то есть Альбус, ты хотел меня видеть?"
                    m "Да. Не желаешь немного стриптиза?"
                    hide screen snape_main
                    with d3
                    $ s_sprite = "03_hp/10_snape_main/snape_05.png"
                    show screen snape_main
                    with d3
                    sna "Оу...?"
                    sna "Мисс Грейнджер будет выступать, не так ли?"
                    $ pos.xpos = 380
                    $herView.showQQ( "body_34.png", pos )
                    her ".............."
                    m "Да, наша маленькая потаскуха будет более чем довольна снять одежду для нас."
                    $herView.hideshowQQ( "body_34.png", pos )
                    her "............"
                    m "Не так ли, девочка?"
                    $herView.hideshowQQ( "body_34.png", pos )
                    her "Да, сэр."
                    m "В таком случае, приступай!"
                    $herView.hideQ()
                    hide screen snape_main
                    with d3
                    pause
                    
                    show screen blkfade
                    with Dissolve(1)
                    $ renpy.play('sounds/08_hop_on_desk.mp3') #Sound of the desk squeaking. 
                    pause 1
                    $ posHead = gMakePos( 390, 340 )
                    $herViewHead.showQ( "body_16.png", posHead )
                    her2 "............."

                    
                    
                    $ s_head_xpos = 330 # x = 330,
                    $ s_head_ypos = 380 #Right bottom corner: y = 340. y = 380 - no hand.
                    $ s_sprite = "03_hp/10_snape_main/snape_05.png"
                    show screen s_head2
                    sna "......................"
                    hide screen s_head2
                    m ".........................."
                    hide screen blkfade
                    hide screen bld1
                    $ hermione_chibi_xpos = 210 #Near the desk: 400.
                    $ hermione_chibi_ypos = 180 #Default: 250
                    show screen clothed_dance #Hermione stands still.
                    show screen ctc
                    show screen s_c_u
                    $ s_c_u_pic = "03_hp/09_snape_ani/snape_0130.png"
                    $ snape_chibi_xpos = 290 #Default 360.
                    $ snape_chibi_ypos = 210
                    with fade
                    pause
                    show screen bld1
                    with d3
                    m "И так... Северус... Как жизнь?"
                    $ s_sprite = "03_hp/10_snape_main/snape_09.png"
                    show screen s_head2
                    sna "Ну, вы знаете... все по старому, все по старому..."
                    $ s_sprite = "03_hp/10_snape_main/snape_06.png"
                    sna " Студенты вызывают одно разочарование..."
                    $ s_sprite = "03_hp/10_snape_main/snape_03.png"
                    sna2 "На самом деле, мисс Грейнджер удалось достать меня больше остальных..."
                    $herViewHead.showQ( "body_68.png", posHead )
                    her "..............................."
                    $herViewHead.hideQ()
                    m "Я уверен, она очень сожалеет об этом..."
                    $herViewHead.showQ( "body_74.png", posHead )
                    her "{size=-4}(Ни капельки!){/size}"
                    $herViewHead.hideQ()
                    m "И сделает что угодно для тебя сегодня. Да, девочка?"
                    $herViewHead.showQ( "body_53.png", posHead )
                    her "Э-эм... Да, профессор."
                    $herViewHead.hideQ()
                    hide screen ctc
                    pause.2
                    show screen blktone
                    with d3
                    ">Гермиона снимает свой жилет и начинает покачивать бедрами."
                    hide screen blktone
                    with d3

                    show screen ctc
                    hide screen bld1
                    with d3
                    pause
                    show screen no_vest_dance
                    with d3
                    pause
                    show screen bld1
                    hide screen ctc
                    with d3
                    $herViewHead.showQ( "body_87.png", posHead )
                    her "..................."
                    $ s_sprite = "03_hp/10_snape_main/snape_05.png"
                    show screen s_head2
                    sna "Хм... В последнее время ты очень тихая."
                    $herViewHead.showQ( "body_48.png", posHead )
                    her "{size=-4}(О нет! Он дейстивтельно так считает?){/size}"
                    $herViewHead.showQ( "body_57.png", posHead )
                    her2 "Я просто делаю то, что мне сказал профессор..."
                    $ s_sprite = "03_hp/10_snape_main/snape_03.png"
                    show screen s_head2
                    sna2 "Сегодня вы не собираетесь читать мне лекции о \"коррупции в Хогвартсе\"?"
                    hide screen s_head2
                    m "Северус..."
                    $ s_sprite = "03_hp/10_snape_main/snape_03.png"
                    show screen s_head2
                    sna2 "Нет, Альбус, я хочу услышать ответ от нашей маленькой мисс совершенство."
                    $herViewHead.showQ( "body_57.png", posHead )
                    her2 "Я просто хочу, чтобы вы отлично провели время, сэр..."
                    $ s_sprite = "03_hp/10_snape_main/snape_03.png"
                    show screen s_head2
                    sna2 "Ох! Этот \"сэр\", это ведь не ко мне ты обращаешься?"
                    $ s_sprite = "03_hp/10_snape_main/snape_10.png"
                    sna2 "Что стало с  \"Снейпо-каракулем\" и профессором \"Сопливикусом\"!??"
                    hide screen s_head2
                    g9 "{size=-5}( \"Сопливикус\", хех... это забавно.){/size}"
                    $herViewHead.showQ( "body_57.png", posHead )
                    her "............."
                    $ s_sprite = "03_hp/10_snape_main/snape_08.png"
                    show screen s_head2
                    sna2 "Да, я знаю, как ты зовешь меня за спиной, девочка!"
                    $herViewHead.showQ( "body_86.png", posHead )
                    her2 "Может быть это потому что вы заслужили это... сэр."
                    $ s_sprite = "03_hp/10_snape_main/snape_10.png" #SNAPE
                    show screen s_head2 #SNAPE
                    sna "Что?!"
                    sna "Да как ты смеешь....?"
                    $ s_sprite = "03_hp/10_snape_main/snape_15.png" #SNAPE
                    show screen s_head2 #SNAPE
                    sna "Кем ты себя возомнила? Ты грязно--"
                    $herViewHead.showQ( "body_62.png", posHead )
                    her2 "Профессор, один из ваших сотрудников собирается оскорбить меня!"
                    her2 "Вы это допустите?"
                    $ s_sprite = "03_hp/10_snape_main/snape_08.png" #SNAPE
                    show screen s_head2 #SNAPE
                    sna "Оскорблять...?! Ты очень нервируешь меня, девочка!"
                    $ s_sprite = "03_hp/10_snape_main/snape_10.png" #SNAPE
                    show screen s_head2 #SNAPE
                    sna2 "Альбус, ты позволишь ей так разговаривать с учителем?"
                    $herViewHead.showQ( "body_62.png", posHead )
                    her "Профессор Дамблдор!"
                    $ s_sprite = "03_hp/10_snape_main/snape_10.png" #SNAPE
                    show screen s_head2 #SNAPE
                    sna "Альбус!"
                    hide screen s_head2
                    menu:
                        m "..."
                        "\"Мисс Грейнджер, проявите уважение!\"":
                            $ mad += 9
                            $herViewHead.showQ( "body_61.png", posHead )
                            her "Что?"
                            her "Но профессор!"
                            $herViewHead.hideQ()
                            m "Юная леди, вам {size=+4}следует{/size} успокоиться."
                            $herViewHead.showQ( "body_66.png", posHead )
                            her "Арх!"
                            $herViewHead.hideQ()
                            m "И снимай свою юбку, хорошо?"
                            $herViewHead.showQ( "body_69.png", posHead )
                            her "......."
                            $ s_sprite = "03_hp/10_snape_main/snape_13.png" #SNAPE
                            show screen s_head2                                                          #SNAPE
                            sna "..........."
                            hide screen s_head2  
                        "\"Северус, ты первый начал.\"":
                            $ s_sprite = "03_hp/10_snape_main/snape_10.png" #SNAPE
                            show screen s_head2  
                            sna "Что? Я?!"
                            $herViewHead.showQ( "body_52.png", posHead )
                            her "Спасибо, профессор."
                            $ s_sprite = "03_hp/10_snape_main/snape_08.png" #SNAPE
                            show screen s_head2                                                          #SNAPE
                            sna2 "Альбус, ты портишь девочку! Ей нужно преподать урок!"
                            hide screen s_head2 
                            m "...............Северус."
                            g4 "Ты головой ударился?!"
                            $ s_sprite = "03_hp/10_snape_main/snape_03.png" #SNAPE
                            show screen s_head2                                                          #SNAPE
                            sna "Простите?"
                            hide screen s_head2 
                            g4 "Она танцует стриптиз для тебя!"
                            g4 "О каком наказании идет речь?"
                            $ s_sprite = "03_hp/10_snape_main/snape_16.png" #SNAPE
                            show screen s_head2  
                            sna "Арх... Как насчет порки?" 
                            hide screen s_head2
                            g4 "Северус!"
                            $ s_sprite = "03_hp/10_snape_main/snape_17.png" #SNAPE
                            show screen s_head2                                                          #SNAPE
                            sna "Ладно, ладно, я понял тебя..."
                            hide screen s_head2
                            m "Мисс Грейнджер, вы собиретесь раздеваться дальше, или нам нужно заглядывать вам под юбку?"
                            $herViewHead.showQ( "body_87.png", posHead )
                            her "Эм..."
                            $herViewHead.hideQ()
                            m "Снимай свою юбку, девочка!"
                            $herViewHead.showQ( "body_55.png", posHead )
                            her "Да, сэр..."
                            $herViewHead.hideQ()
                        "\"Вы оба, заткнитесь нахер.\"":
                            m "Ты, высокий-темный-парень, успокойся, ага?"
                            $ s_sprite = "03_hp/10_snape_main/snape_03.png" #SNAPE
                            show screen s_head2                                                          #SNAPE
                            sna "Простите?"
                            $herViewHead.showQ( "body_69.png", posHead )
                            her "Да! Вы должны сказать ему--"
                            $herViewHead.hideQ()
                            m "И ты тоже, извращенка!"
                            m "Успокойся и снимай уже с себя юбку!"
                            $herViewHead.showQ( "body_79.png", posHead )
                            her "Я не извращенка..."
                            $herViewHead.hideQ()
                            m "Юбка, девочка!"
                            $herViewHead.showQ( "body_69.png", posHead )
                            her "......"
                            $ s_sprite = "03_hp/10_snape_main/snape_13.png" #SNAPE
                            show screen s_head2  
                            sna "............."
                            hide screen s_head2     
                    
                    show screen blktone
                    with d3
                    ">Гермиона быстро снимает юбку \"Хогвартса\"..."
                    hide screen blktone
                    with d3
                   
                    show screen ctc
                    hide screen bld1
                    with d3
                    pause
                    show screen no_skirt_dance
                    with d3
                    pause
                    show screen bld1
                    hide screen ctc
                    with d3
                    show screen s_head2
                    sna "Хм..."
                    $herViewHead.showQ( "body_87.png", posHead )
                    her "........................"
                    $herViewHead.hideQ()
                    m "Да, так-то лучше!"
                    show screen blktone
                    with d3
                    ">Гермиона продолжает танцевать. На ней уже не осталось ничего, кроме рубашки и трусиков..."
                    menu:
                        m "..."
                        "\"Северус, что насчет Поттера?\"":
                            $herViewHead.showQ( "body_55.png", posHead )
                            her "(.....?)"
                            $ s_sprite = "03_hp/10_snape_main/snape_09.png" #SNAPE
                            show screen s_head2
                            sna "Что с ним?"
                            hide screen s_head2
                            m "Ты все еще из за него расстраиваешься?"
                            $ s_sprite = "03_hp/10_snape_main/snape_09.png" #SNAPE
                            show screen s_head2                                                          #SNAPE
                            sna "О..."
                            sna "На самом деле - нет."
                            $ s_sprite = "03_hp/10_snape_main/snape_06.png" #SNAPE
                            show screen s_head2                                                          #SNAPE
                            sna2 "Честно говоря, у меня никогда не было с ним особых проблем..."
                            sna2 "Хотя я планировал сделать его жизнь невыносимой из-за его отца..."
                            $ s_sprite = "03_hp/10_snape_main/snape_02.png" #SNAPE
                            show screen s_head2    
                            sna2 "Но в последнее время у меня есть много интересных проектов, чтобы занять себя..."
                            $herViewHead.showQ( "body_55.png", posHead )
                            her "..................."  
                            $herViewHead.hideQ()
                        "\"Северус, что насчет семьи Уизли?\"":
                            $ s_sprite = "03_hp/10_snape_main/snape_09.png" #SNAPE
                            show screen s_head2                                                          #SNAPE
                            sna "Что с ними?"
                            hide screen s_head2   
                            m "Они все еще являются проблемой?"
                            $ s_sprite = "03_hp/10_snape_main/snape_09.png" #SNAPE
                            show screen s_head2                                                          #SNAPE
                            sna "Да... Даже большей, чем раньше."
                            hide screen s_head2
                            m "Хм...?"
                            m "Ты кажешься удивительно равнодушным по этому поводу..."
                            $ s_sprite = "03_hp/10_snape_main/snape_05.png" #SNAPE
                            show screen s_head2                                                          #SNAPE
                            sna2 "Это только потому, что я знаю, что в конце концов они получат то, что заслуживают..."
                            hide screen s_head2
                            m "Месть? Отлично! Что у тебя на уме?"
                            $herViewHead.showQ( "body_55.png", posHead )
                            her "!!!"
                            $ s_sprite = "03_hp/10_snape_main/snape_06.png" #SNAPE
                            show screen s_head2                                                          #SNAPE
                            sna "Хм... немогу обсуждать это, пока \"враг\" рядом."
                            $herViewHead.showQ( "body_69.png", posHead )
                            her "Арх!"
                            $ s_sprite = "03_hp/10_snape_main/snape_13.png" #SNAPE
                            show screen s_head2                                                          #SNAPE
                            sna2 "Все, что я могу сказать - это то, что это включает в себя их любимую маленькую сестренку Джинни..."
                            hide screen s_head2  
                            m "Джинни? Хм... Что за странное имя для девочки..."
                            m "............."
                            m "Так ты планируешь ее трахнуть?"
                            $ s_sprite = "03_hp/10_snape_main/snape_08.png" #SNAPE
                            show screen s_head2                                                          #SNAPE
                            sna "!!?"
                            $ s_sprite = "03_hp/10_snape_main/snape_17.png" #SNAPE
                            show screen s_head2                                                          #SNAPE
                            sna2 "Альбус, пожалуйста, не перед девочкой же!"
                            hide screen s_head2  
                            m "Хорошо, хорошо..."
                            $herViewHead.showQ( "body_87.png", posHead )
                            her "{size=-5}(Джинни...){/size}"
                            $herViewHead.hideQ()
                        "\"Как ты оцениваешь попку Гермионы?\"":
                            $ s_sprite = "03_hp/10_snape_main/snape_05.png" #SNAPE
                            show screen s_head2                                                          #SNAPE
                            sna "Оценить ягодицы мисс Грейнджер?" 
                            $herViewHead.showQ( "body_69.png", posHead )
                            her "!!!............"
                            $herViewHead.hideQ()
                            m "Конечно! Так же, как ты оцениваешь бумагу."
                            $ s_sprite = "03_hp/10_snape_main/snape_13.png" #SNAPE
                            show screen s_head2                                                          #SNAPE
                            sna "Хм..."
                            hide screen s_head2  
                            pause.1
                            ">Профессор Снейп оценивающе смотрит на попку Гермионы..."
                            $herViewHead.showQ( "body_44.png", posHead )
                            her ".........?"
                            $ s_sprite = "03_hp/10_snape_main/snape_13.png" #SNAPE
                            show screen s_head2                                                          #SNAPE
                            sna "Я бы сказал..."
                            $herViewHead.showQ( "body_59.png", posHead )
                            her "............?!"
                            $ s_sprite = "03_hp/10_snape_main/snape_09.png" #SNAPE
                            show screen s_head2                                                          #SNAPE
                            sna "Да... \"{size=+5}2-{/size}\"."
                            $herViewHead.showQ( "body_48.png", posHead )
                            her "(Что?!)"
                            $ s_sprite = "03_hp/10_snape_main/snape_09.png" #SNAPE
                            show screen s_head2                                                          #SNAPE
                            sna "Неудовлетворительно..."
                            sna2 "Посмотрите на нее. Маленькая и тощая... Да это задница мальчика."
                            $herViewHead.showQ( "body_51.png", posHead )
                            her "!!!!!!!!!!"
                            $herViewHead.hideQ()
                            
                    show screen blktone
                    with d3
                    ">Одну за другой, Гермиона расстегивает пуговицы своей блузки и снимает ее..."
                    hide screen blktone
                    with d3
                   
                    show screen ctc
                    hide screen bld1
                    with d3
                    pause
                    show screen no_shirt_no_skirt_dance
                    with d3
                    pause
                    show screen bld1
                    hide screen ctc
                    with d3
                    m "Неплохо! Мы наконец-то добрались до сладкого!"
                    $ s_sprite = "03_hp/10_snape_main/snape_13.png" #SNAPE
                    show screen s_head2       
                    sna "Хм..."
                    
                    call req11_undress
                    
                    $ posHead = gMakePos( 390, 235 )
                    $herViewHead.showQ( "body_90.png", posHead )
                    her "........"
                    $herViewHead.hideQ()
                    menu:
                        m "..."
                        "- Начать дрочить -":
                            play music "music/(Orchestral) Playful Tension by Shadow16nh.mp3" fadein 1 fadeout 1 # SEX THEME.
                            
                            hide screen bld1
                            show screen ctc
                            with d3
                            pause
                            show screen blkfade
                            with d6
                            $herViewHead.showQ( "body_94.png", posHead )
                            her "Профессор Дамблдор?!"
                            $herViewHead.hideQ()
                            m "Все в порядке, девочка. Не возражай мне..."
                            $ s_sprite = "03_hp/10_snape_main/snape_12.png" #SNAPE
                            show screen s_head2                                                          #SNAPE
                            sna "О, мы будем теперь вести себя так?"
                            sna "Что же, не возражаешь, если я тоже присоединюсь?.."
                            $ posHead.ypos = 380
                            $herViewHead.showQ( "body_94.png", posHead )
                            
                            her "!!!"
                            $herViewHead.hideQ()
                            
                            
                            hide screen genie
                            hide screen no_shirt_no_skirt_dance
                            $ genie_chibi_xpos = -185
                            $ genie_chibi_ypos = 10
                            $ g_c_u_pic = "jerking_off_02_ani"
                            $ snape_chibi_xpos = -185
                            $ snape_chibi_ypos = 10
                            $ s_c_u_pic = "jerking_off_03_ani" #Snape.
                            show screen chair_02
                            show screen g_c_u
                            show screen desk_02
                            show screen no_shirt_no_skirt_dance
                            hide screen blkfade
                            with fade
                            pause
                            show screen bld1
                            with d3
                            $herViewHead.showQ( "body_95.png", posHead )
  
                            her2 "Нет, ребята... эмм, я имею в виду, сэры... Эм, профессоры!"
                            $herViewHead.hideQ()
                            m "Не обращай на нас внимания, девочка, просто продолжай."
                            $herViewHead.showQ( None, posHead )
                            her "Но..."
                            $herViewHead.showQ( "body_99.png", posHead )
                            her2 "Нет! Я отказываюсь танцевать, пока эти штуки нацелены на меня!"
                            her2 "Вы должны убрать их, или танца не будет!"
                            $herViewHead.hideQ()
                            m "Ты не в том положении, чтобы что-то требовать, девочка."
                            $herViewHead.showQ( "body_110.png", posHead )
                            her2 "Это было не требование, сэр. Это был ультиматум."
                            $herViewHead.hideQ()
                            menu:
                                m "..."
                                "\"Что же Северус, давай будем цивилизованными...\"":
                                    $ s_sprite = "03_hp/10_snape_main/snape_03.png" #SNAPE
                                    show screen s_head2                                                          #SNAPE
                                    sna2 "Я вижу, Мисс Грейнджер может упорствовать в любой ситуации..."
                                    hide screen s_head2  
                                    show screen blkfade
                                    with d3
                                    hide screen no_shirt_no_skirt_dance
                                    show screen genie
                                    hide screen chair_02
                                    hide screen g_c_u
                                    hide screen desk_02
                                    show screen no_shirt_no_skirt_dance
                                    show screen s_c_u
                                    $ s_c_u_pic = "03_hp/09_snape_ani/snape_0130.png"
                                    $ snape_chibi_xpos = 290 #Default 360.
                                    $ snape_chibi_ypos = 210
                                    pause.3
                                    hide screen blkfade 
                                    with d3
                                    jump civil_with_snape
                                    
                                "\"(Пст! Напомни мне, зачем мы это делаем?!)\"":
                                    if whoring >= 15: #LEVEL 06. You jerk off your cock and Hermione is OK with it.
                                        $herViewHead.showQ( "body_104.png", posHead )
                                        her "О, точно..."
                                        $ s_sprite = "03_hp/10_snape_main/snape_05.png" #SNAPE
                                        show screen s_head2                                                          #SNAPE
                                        sna "Что это было?"
                                        $herViewHead.showQ( "body_108.png", posHead )
                                        her "Пожалуйста, не слушайте меня..."
                                        $ s_sprite = "03_hp/10_snape_main/snape_05.png" #SNAPE
                                        show screen s_head2                                                          #SNAPE
                                        sna "Хм...?"
                                        $herViewHead.showQ( "body_108.png", posHead )
                                        her2 "Я не против того, что вы трогаете себя передо мной..."
                                        her2 "Да, я не против всего этого..."
                                        her "Я просто продолжу танцевать..."
                                        $herViewHead.hideQ()
                                        hide screen ctc
                                        pause.1
                                        show screen blktone
                                        with d3
                                        show screen blktone8
                                        with d3
                                        ">Вы продолжаете дрочить, смотря на танец Гермионы..."
                                        ">Гермиона сжимает свою грудь и немного покачивает бедрами..."
                                        hide screen blktone8
                                        with d3
                                        m "Да, ммм. Очень хорошо."
                                        $ s_sprite = "03_hp/10_snape_main/snape_12.png" #SNAPE
                                        show screen s_head2                                                          #SNAPE
                                        sna "*Кхм!* Неплохое выступление, Мисс Грейнджер."
                                        $herViewHead.showQ( "body_97.png", posHead )
                                        her "...................."
                                        $herViewHead.hideQ()
                                        m "Хех, профессор Снейп..."
                                        $herViewHead.hideQ()
                                        m "Как вы оцените ее грудь?"
                                        $herViewHead.showQ( "body_94.png", posHead )
                                        her "......"
                                        $ s_sprite = "03_hp/10_snape_main/snape_13.png" #SNAPE
                                        show screen s_head2                                                          #SNAPE
                                        sna "Хм......"
                                        $herViewHead.showQ( "body_103.png", posHead )
                                        her "........"
                                        $ s_sprite = "03_hp/10_snape_main/snape_12.png" #SNAPE
                                        show screen s_head2                                                          #SNAPE
                                        sna "\"4+\"!"
                                        $herViewHead.showQ( "body_94.png", posHead )
                                        her "!!!"
                                        $herViewHead.hideQ()
                                        m "Правда?"
                                        $ s_sprite = "03_hp/10_snape_main/snape_12.png" #SNAPE
                                        show screen s_head2                                                          #SNAPE
                                        sna2 "Да. Я всегда отдаю должное хорошей груди."
                                        $herViewHead.showQ( "body_90.png", posHead )
                                        her "(Профессор...)"
                                        $herViewHead.showQ( "body_102.png", posHead )
                                        her "(Время завершающего акта!)"
                                        $herViewHead.hideQ()
                                        pause.1
                                        show screen blktone8
                                        with d3
                                        ">Гермиона нагибается и ее трусики соскальзывают вниз."
                                        ">Ее движения лишены грации..."
                                        ">Но ее хорошенькая киска, тем не менее, вам нравится..."
                                        ">Вы показываете свое одобрение, начиная дрочить быстрее..."
                                        
                                       
                                        hide screen blktone8 
                                        hide screen blktone
                                        with d3
                                        hide screen bld1
                                        with d3
                                        show screen ctc
                                        pause
                                        $ h_c_u_pic = "no_panties_dance_ani"
                                        hide screen no_shirt_no_skirt_dance
                                        show screen h_c_u
                                        with d3
                                        pause
                                        show screen bld1
                                        with d3
                                        show screen blktone
                                        with d3
                                        
                                        $ s_sprite = "03_hp/10_snape_main/snape_18.png" #SNAPE
                                        show screen s_head2                                                          #SNAPE
                                        sna "Да... Да!!!"
                                        sna2 "Теперь потряси этими сиськами для меня, ты, шлюха!"
                                        $herViewHead.showQ( "body_99.png", posHead )
                                        her "......."
                                        $herViewHead.hideQ()
                                        hide screen ctc
                                        pause.1
                                        show screen blktone8
                                        with d3
                                        ">Гермиона неожиданно прерывается на серию довольно сложных пируэтов."
                                        $ s_sprite = "03_hp/10_snape_main/snape_19.png" #SNAPE
                                        show screen s_head2                                                          #SNAPE
                                        sna "Да, такая грация..."
                                        $ s_sprite = "03_hp/10_snape_main/snape_20.png" #SNAPE
                                        show screen s_head2                                                          #SNAPE
                                        sna "Это гибкое молодое тело!"
                                        $herViewHead.showQ( "body_106.png", posHead )
                                        her "........."
                                        $ s_sprite = "03_hp/10_snape_main/snape_20.png" #SNAPE
                                        show screen s_head2                                                          #SNAPE
                                        sna "О, да!"
                                        $herViewHead.showQ( "body_106.png", posHead )
                                        her "{size=-5}(Три-два-раз... Три-два-раз... И шаг!){/size}"
                                        $herViewHead.hideQ()
                                        pause.1
                                        show screen blktone8
                                        with d3
                                        ">Гермиона выглядит очень сосредоточенной на своем танце..."
                                        hide screen blktone8
                                        with d3
                                        $ s_sprite = "03_hp/10_snape_main/snape_19.png" #SNAPE
                                        show screen s_head2                                                          #SNAPE
                                        sna "Да, и еще один пируэт!"
                                        sna "Великолепно!"
                                        $ s_sprite = "03_hp/10_snape_main/snape_13.png" #SNAPE
                                        show screen s_head2                                                          #SNAPE
                                        sna2 "Я бы тебе поаплодировал, но одна моя рука занята."
                                        hide screen s_head2  
                                        m "{size=-4}(Это была попытка пошутить?){/size}"
                                        m "{size=-4}(Черт, возбужденный Снейп такой странный...){/size}"
                                        show screen blktone8
                                        with d3
                                        ">Гермиона начинает еще одну серию движений и пируэтов..."
                                        ">Делает реверанс воображаемой публике..."
                                        show screen blkfade
                                        with d3
                                        $ hermione_chibi_xpos = -210 #400 = Near the desk.
                                        $ hermione_chibi_ypos = 10
                                        $ h_c_u_pic = "03_hp/08_animation_02/08_sits.png"
                                        ">И после этого измученно падает на задницу."
                                        
                                        hide screen blktone
                                        with d3
                                        hide screen blktone8
                                        with d3
                                        hide screen blkfade
                                        with d3
                                        hide screen bld1 
                                        with d3
                                        show screen ctc
                                        pause
                                        $herViewHead.showQ( "body_102.png", posHead )
                                        her "Фью... Это было--"
                                        $herViewHead.hideQ()
                                        with hpunch
                                        g4 "АРГХ! ТЫ ЕБАНАЯ ШЛЮХА!"
                                        $herView.hideQQ()
                                        show screen white 
                                        pause.1
                                        hide screen white
                                        pause.2
                                        show screen white 
                                        pause .1
                                        hide screen white
                                        with hpunch
                                        $ genie_chibi_xpos = -210
                                        $ genie_chibi_ypos = 10
                                        $ genie_cum_chibi_xpos =  -210
                                        $ genie_cum_chibi_ypos  = 10
                                        $ g_c_c_u_pic = "genie_cum_03"
                                        $ h_c_u_pic = "03_hp/08_animation_02/08_sits_02.png"
                                        show screen g_c_c_u
                                        pause
                                        
                                        $herViewHead.data().addItem( 'sperm', CharacterExItem( herViewHead.mMiscFolder, 'sperm_01.png', G_Z_FACE + 1 ) )
                                        $herViewHead.showQ( "body_104.png", posHead )
                                        her "??!!!"
                                        $herViewHead.hideQ()
                                        $herViewHead.showQ( "body_97.png", posHead )
                                        
                                        $ s_sprite = "03_hp/10_snape_main/snape_18.png" #SNAPE
                                        show screen s_head2                                                          #SNAPE
                                        sna "Хорошая работа, ты, шлюшка!"
                                        $ s_sprite = "03_hp/10_snape_main/snape_21.png" #SNAPE
                                        show screen s_head2                                                          #SNAPE
                                        sna "Вот твоя награда!"
                                        hide screen s_head2     
                                        show screen white 
                                        pause.1
                                        hide screen white
                                        pause.2
                                        show screen white 
                                        pause .1
                                        hide screen white
                                        with hpunch
                                        $ snape_chibi_xpos = -210
                                        $ snape_chibi_ypos = 10
                                        $ snape_cum_chibi_xpos =  -210
                                        $ snape_cum_chibi_ypos  = 10
                                        $ s_c_c_u_pic = "snape_cum_01"
                                        show screen s_c_c_u
                                        pause
                                        $herViewHead.showQ( "body_104.png", posHead )
                                        $herViewHead.data().addItem( 'sperm', CharacterExItem( herViewHead.mMiscFolder, 'sperm_02.png', G_Z_FACE + 1 ) )
                                        her "!!!!!!!!!!!"
                                        $ s_sprite = "03_hp/10_snape_main/snape_21.png" #SNAPE
                                        show screen s_head2                                                          #SNAPE
                                        sna2 "О... Да..."
                                        hide screen s_head2 
                                        g4 "Маленькая блядь!"
                                        $herViewHead.showQ( "body_106.png", posHead )
                                        her "..............................."
                                
                                        $ s_c_c_u_pic = "03_hp/08_animation_02/11_cum_18.png"
                                        $ g_c_c_u_pic = "03_hp/08_animation_02/09_cum_18.png"
                                        $ s_sprite = "03_hp/10_snape_main/snape_21.png" #SNAPE
                                        show screen s_head2                                                          #SNAPE
                                        sna "Ха-ха-ха! Это было превосходно!"
                                        hide screen s_head2
                                        g9 "Я знаю!"
                                        show screen bld1
                                        with d3
                                        $ g_c_u_pic = "03_hp/08_animation_02/06_jerking_01.png" # Genie stands still with his dick in hand.
                                        $ s_c_u_pic = "03_hp/08_animation_02/10_jerking_01.png" # Snape stands still with his dick in hand.
                                        $ s_sprite = "03_hp/10_snape_main/snape_22.png" #SNAPE
                                        show screen s_head2                                                          #SNAPE
                                        sna "Да... Нам стоит делать это почаще..."
                                        $herViewHead.showQ( "body_106.png", posHead )
                                        her "................."
                                        $ s_sprite = "03_hp/10_snape_main/snape_20.png" #SNAPE
                                        show screen s_head2                                                          #SNAPE
                                        sna "Ваше выступление было неплохим, Мисс Грейнджер..."
                                        $herViewHead.showQ( "body_91.png", posHead )
                                        her "Спасибо................"
                                        $ s_sprite = "03_hp/10_snape_main/snape_19.png" #SNAPE
                                        show screen s_head2                                                          #SNAPE
                                        sna "Но если я здесь, чтобы оценить это..."
                                        $herViewHead.showQ( "body_91.png", posHead )
                                        her "..........."
                                        $ s_sprite = "03_hp/10_snape_main/snape_22.png" #SNAPE
                                        show screen s_head2                                                          #SNAPE
                                        sna "Хм...."
                                        $herViewHead.showQ( "body_91.png", posHead )
                                        her "............"
                                        $ s_sprite = "03_hp/10_snape_main/snape_10.png" #SNAPE
                                        show screen s_head2                                                          #SNAPE
                                        sna "\"{size=+5}2+{/size}\"!"
                                        $herViewHead.showQ( "body_112.png", posHead )
                                        stop music
                                        her "{size=+5}ЧТО?!!!{/size}"
                                        $ s_sprite = "03_hp/10_snape_main/snape_09.png" #SNAPE
                                        show screen s_head2                                                          #SNAPE
                                        sna2 "Да... Думаю кое-что можно было бы и улучшить."
                                        $herViewHead.showQ( "body_110.png", posHead )
                                        play music "music/Chipper Doodle v2.mp3" fadein 1 fadeout 1 # HERMIONE'S THEME.
                                        her "Не могу поверить!"
                                        $herViewHead.hideQ()
                                        pause
                                        show screen blkfade 
                                        with d3
                                        hide screen h_c_u 
                                        hide screen s_c_c_u
                                        hide screen g_c_c_u
                                        show screen genie
                                        $ snape_chibi_xpos = -60
                                        $ snape_chibi_ypos = 10
                                        $ s_c_u_pic = "jerking_off_03_ani" #Snape.
                                        hide screen chair_02
                                        hide screen g_c_u
                                        hide screen desk_02
                                        $ hermione_chibi_xpos = 300 #Near the desk: 400. (210 - standing on desk.)
                                        $ hermione_chibi_ypos = 260#Default: 250. (180- standing on desk.)
                                        show screen h_c_u 
                                        $ h_c_u_pic = im.Flip("03_hp/08_animation_02/07_dance_03.png", horizontal=True)
                                        ">Гермиона в ярости спрыгивает со стола."
                                        hide screen blkfade
                                        with d3
                                        hide screen bld1
                                        with d3
                                        pause
                                        
                                        
                                        
                                        $ pos = POS_140
                                        show screen bld1
                                        with d5
                                        
                                        
                                        $herView.data().addTransform( gTrEx( 'flip', horizontal = True ) )
                                        $herView.showQQ( "body_101.png", pos )
                                        pause
                                        hide screen ctc
                                        her "Я требую более высокую оценку за это!"
                                        $ s_sprite = "03_hp/10_snape_main/snape_09.png" #SNAPE
                                        show screen s_head2      
                                        sna2 "Не требуйте оценку Мисс Грейнджер, вы заработали ее."
                                        hide screen s_head2     
                                        $herView.hideQQ()
                                        $ herView.showQQ( "body_107.png", pos )
                                        her "Я заслужила ее!"
                                        $herView.hideQQ()
                                        $ herView.showQQ( "body_103.png", pos )
                                        her "И не могли бы вы, хотя бы для порядочности, перестать трогать себя, сэр?!"
                                        $ s_sprite = "03_hp/10_snape_main/snape_12.png" #SNAPE
                                        show screen s_head2     
                                        sna2 "Тс..."
                                        hide screen s_head2   
                                        $herView.hideQQ()
                                        m "(Она это вправду?..)"
                                        show screen ctc
                                        pause
                                        show screen blkfade
                                        with d7
                                        hide screen ctc
                                        hide screen s_c_u
                                        hide screen h_c_u
                                        $ hermione_chibi_xpos = 400 #Near the desk.
                                        $ hermione_chibi_ypos = 250 #Default: 250
                                        show screen hermione_02 #Hermione stands still.
                                        ">Вы видите как Снейп, со все еще стоящим членом и полностью покрытая спермой Гермиона громко спорят о воображаемой оценке."
                                        ">Наконец, профессор Снейп соглашается изменить ее оценку с \"2+\" на \"3-\"."
                                        ">После этого он поспешно уходит, до того, как Гермиона сможет найти еще один аргумент..."
                                        hide screen blkfade
                                        with d5
                                        $herView.data().delTransform()
                                        $herView.data().delItem( 'sperm' )
                                        $herView.data().addItem( 'sperm_after', CharacterExItem( herView.mMiscFolder, 'sperm_00_after.png', G_Z_FACE + 1 ) )
                                        $herView.hideQQ()
                                        $ pos = POS_140
                                        call req11_dress
                                        $herView.showQQ( "body_29.png", pos )
                                        her "Что ж..."
                                        her "Наша миссия была успешной, сэр?"
                                        menu:
                                            m "..."
                                            "\"А? Какая миссия?\"":
                                                $ mad += 7
                                                $herView.hideshowQQ( "body_32.png", pos )
                                                her "Я согласилась на это только ради того, чтобы вы увидели профессора Снейпа в действии, сэр!"
                                                $herView.hideshowQQ( "body_33.png", pos )
                                                her "Так что у нас есть неопровержимое доказательство того, что он \"грязный\"!"
                                                m "О, эта миссия..."
                                                m "Да. Миссия выполнена!"
                                            "\"Да! Спасибо вам!\"":
                                                pass
                                        m "Хорошая работа, мисс Грейнджер."
                                        $herView.hideshowQQ( "body_33.png", pos )
                                        her "Я была рада помочь, сэр!"
                                        $herView.hideshowQQ( "body_34.png", pos )
                                        her "...могу ли я теперь получить оплату?"
                                        

                                    else:
                                        $herViewHead.showQ( "body_94.png", posHead )
                                        her "О..."
                                        $herViewHead.showQ( "body_97.png", posHead )
                                        her "Нет, я не могу! Это того не стоит!"
                                        hide screen ctc
                                        $herViewHead.hideQ()
                                        pause.1
                                        show screen blkfade
                                        with d5
                                        ">Гермиона спрыгивает со стола и начинает одеваться."
                                        $ s_sprite = "03_hp/10_snape_main/snape_03.png" #SNAPE
                                        show screen s_head2                                                          #SNAPE
                                        sna "Это ужасно разочаровывает..."
                                        hide screen s_head2  
                                        g4 "И не говори..."
                                        $ s_sprite = "03_hp/10_snape_main/snape_03.png" #SNAPE
                                        show screen s_head2                                                          #SNAPE
                                        sna2 "Пожалуй, я вас покину. Поговорим позже, Альбус."
                                        hide screen s_head2  
                                        m "Да, попозже, Северус."
                                        $ s_sprite = "03_hp/10_snape_main/snape_04.png" #SNAPE
                                        show screen s_head2                                                          #SNAPE
                                        sna "Мисс Грейнджер..."
                                        $herViewHead.showQ( "body_99.png", posHead )
                                        her "Профессор..."
                                        $herViewHead.hideQ()
                                        her "Я хочу получить свои очки."
                                        show screen ctc
                                        pause.4
                                        hide screen s_c_u
                                        hide screen ctc
                                        ">Профессор Снейп уходит..."
                                        $herViewHead.showQ( "body_91.png", posHead )
                                        stop music fadeout 1.0
                                        her "...................."
                                        $herViewHead.hideQ()
                                        pause.5
                                        ">.................{w}.................{w}.................{w}................."
                                        call req11_dress
                                        $herViewHead.showQ( "body_33.png", posHead )
                                        
                                        
                                        her "...Могу ли я получить оплату... сэр...?"
                                        $herViewHead.hideQ()

                        "- Продолжать смотреть -":
                            label civil_with_snape:
                            play music "music/Dark Fog.mp3" fadein 1 fadeout 1 # SNAPE'S THEME
                            # JUST WATCHING.
                            $herViewHead.showQ( "body_102.png", posHead )
                            her "Я просто продолжу танцевать..."
                            $herViewHead.hideQ()
                            hide screen ctc
                            pause.1
                            show screen blktone8
                            with d3
                            ">Гермиона сжимает свою грудь и немного покачивает бедрами..."
                            hide screen blktone8
                            with d3
                            m "Да, девочка. Очень хорошо."
                            $ s_sprite = "03_hp/10_snape_main/snape_12.png" #SNAPE
                            show screen s_head2                                                          #SNAPE
                            sna "*Кхм!* Неплохое выступление, Мисс Грейнджер."
                            $herViewHead.showQ( "body_102.png", posHead )
                            her "...."
                            $herViewHead.hideQ()
                            m "Хех, профессор Снейп..."
                            m "Как вы оцените ее грудь?"
                            $herViewHead.showQ( "body_90.png", posHead )
                            her "......"
                            $ s_sprite = "03_hp/10_snape_main/snape_20.png" #SNAPE
                            show screen s_head2                                                          #SNAPE
                            sna "Хм......"
                            $herViewHead.showQ( "body_90.png", posHead )
                            her "........"
                            $ s_sprite = "03_hp/10_snape_main/snape_12.png" #SNAPE
                            show screen s_head2                                                          #SNAPE
                            sna "\"4+\"!"
                            $herViewHead.showQ( "body_94.png", posHead )
                            her "!!!"
                            $herViewHead.hideQ()
                            m "Правда?"
                            $ s_sprite = "03_hp/10_snape_main/snape_12.png" #SNAPE
                            show screen s_head2                                                          #SNAPE
                            sna "Да. Я всегда отдаю должное хорошей груди."
                            $herViewHead.showQ( "body_95.png", posHead )
                            her "(Профессор...)"
                            $herViewHead.showQ( "body_102.png", posHead )
                            her "(Время для завершающего акта!)"
                            $herViewHead.hideQ()
                            pause.1
                            show screen blktone8
                            with d3
                            ">Гермиона нагибается и ее трусики соскальзывают вниз."
                            ">Ее движения лишены грации..."
                            ">Но ее хорошенькая киска, тем не менее, вам нравится..."
                            hide screen blktone
                            with d3
                            $ s_sprite = "03_hp/10_snape_main/snape_20.png" #SNAPE
                            show screen s_head2                                                          #SNAPE
                            sna "Да...Да..."
                            sna2 "Теперь потряси этими сиськами для меня, шлюха!"
                            $herViewHead.showQ( "body_99.png", posHead )
                            her "......."
                            $herViewHead.hideQ()
                            show screen blktone8
                            with d3
                            ">Гермиона неожиданно прерывается на серию довольно сложных пируэтов."
                            $ s_sprite = "03_hp/10_snape_main/snape_19.png" #SNAPE
                            show screen s_head2                                                          #SNAPE
                            sna "Да, такая грация..."
                            $ s_sprite = "03_hp/10_snape_main/snape_20.png" #SNAPE
                            show screen s_head2                                                          #SNAPE
                            sna "Это гибкое, молодое тело!"
                            $herViewHead.showQ( "body_102.png", posHead )
                            her "{size=-5}(Три-два-раз... Три-два-раз... И шаг!){/size}"
                            $herViewHead.hideQ()
                            ">Гермиона выглядит очень сосредоточенной на своем танце..."
                            $ s_sprite = "03_hp/10_snape_main/snape_19.png" #SNAPE
                            show screen s_head2
                            sna "Да, и еще один пируэт!"
                            sna "Великолепно!"
                            hide screen s_head2
                            show screen blkfade
                            with d3
                            ">Гермиона начинает еще одну серию движений и пируэтов..."
                            ">Делает реверанс воображаемой публике..."
                            ">И после этого измученно падает на задницу"
                            $ hermione_chibi_xpos = -210 #400 = Near the desk.
                            $ hermione_chibi_ypos = 10
                            $ h_c_u_pic = "03_hp/08_animation_02/08_sits.png"
                            show screen h_c_u
                            hide screen blkfade
                            with d3
                            hide screen blktone8
                            with d3
                            $ s_sprite = "03_hp/10_snape_main/snape_22.png" #SNAPE
                            show screen s_head2                                                          #SNAPE
                            sna "Хорошая работа, ты, шлюха!"
                            $herViewHead.showQ( "body_105.png", posHead )
                            her "............."
                            if daytime:
                                $ s_sprite = "03_hp/10_snape_main/snape_22.png" #SNAPE
                                show screen s_head2                                                          #SNAPE
                                sna2 "Что ж, мой урок скоро должен начаться, поэтому я вас покину."
                                sna2 "У вас же сегодня мой урок зельеварения, верно, Мисс Грейнджер?"
                                $herViewHead.showQ( "body_91.png", posHead )
                                her2 "Да, сэр..."
                                $ s_sprite = "03_hp/10_snape_main/snape_22.png" #SNAPE
                                show screen s_head2                                                          #SNAPE
                                sna2 "Тогда не опаздывай, девочка..."
                                hide screen s_head2      
                            else:
                                $ s_sprite = "03_hp/10_snape_main/snape_22.png" #SNAPE
                                show screen s_head2    
                                sna2 "Что ж, уже довольно поздно. Я покину вас."
                                sna2 "Доброй ночи, Альбус."
                                hide screen s_head2    
                                m "Северус."
                                $ s_sprite = "03_hp/10_snape_main/snape_22.png" #SNAPE
                                show screen s_head2    
                                sna2 "Шлюха."
                                $herViewHead.showQ( "body_91.png", posHead )
                                her2 "Профессор..."
                                $herViewHead.hideQ()


                            show screen ctc
                            pause
                            show screen blkfade
                            hide screen s_c_u
                            hide screen ctc
                            with d5
                            ">Профессор Снейп уходит..."
                            $herViewHead.showQ( "body_91.png", posHead )
                            stop music fadeout 1.0
                            her "...................."
                            $herViewHead.hideQ()
                            pause.5
                            ">.................{w}.................{w}.................{w}................."
                            call req11_dress
                            $herViewHead.showQ( "body_33.png", posHead )
                            her "Могу я... получить оплату... сэр...?"
                            $herViewHead.hideQ()


                "\"Мм... Это плохая идея...\"":
                    label no_snape_watching:  
                    hide screen blktone
                    with d3
                    m "Мисс Грейнджер, как насчет еще одного стриптиза?"     
                    $ pos = POS_140
                    $herView.showQQ( "body_66.png", pos )
                    her ".............."
                    her "Я скорее откажусь, профессор..."
                    m "Почему? Ты становишься довольно хороша в этом."
                    $herView.hideshowQQ( "body_79.png", pos )
                    her "........................."
                    $herView.hideshowQQ( "body_87.png", pos )
                    her "Тридцать пять очков?"
                    m "Конечно! Обычная цена."
                    $herView.hideshowQQ( "body_69.png", pos )
                    her "..................."
                    $herView.hideQQ()
                    hide screen bld1
                    with d3
                    pause
                    #Walks to the door
                    
                    $ walk_xpos=400 #Animation of walking chibi. (From) 400 = desk.
                    $ walk_xpos2=650 #Coordinates of it's movement. (To) 610 = door.
                    $ hermione_speed = 02.0 #The speed of moving the walking animation across the screen.
                    show screen hermione_walk_01_f 
                    pause 2
                    hide screen hermione_walk_01_f 
                    $ hermione_chibi_xpos = 650 # Position of the chibi (Near the door).
                    $ h_c_u_pic = im.Flip("03_hp/animation/h_walk_01.png", horizontal=True)
                    show screen h_c_u
                    pause.5
                   
                    $ tt_xpos=670
                    $ tt_ypos=200
                    show screen thought 
                    with Dissolve(.3)
                    pause.5
                    hide screen thought
                    pause.5
                   
                    $ h_c_u_pic = im.Flip("03_hp/animation/h_walk_03.png", horizontal=True)
                    $ renpy.play('sounds/09_lock.wav') #Sound of a door opening.
                    pause.4
                    $ h_c_u_pic = im.Flip("03_hp/animation/h_walk_01.png", horizontal=True)
                    show screen ctc
                    pause
                    m "??!"
                    hide screen h_c_u
                    hide screen ctc
                    $ walk_xpos=650 #Animation of walking chibi. (From)
                    $ walk_xpos2=400 #Coordinates of it's movement. (To)
                    $ hermione_speed = 03.0 #The speed of moving the walking animation across the screen.
                    show screen hermione_walk_01 
                    pause 3
                    $ hermione_chibi_xpos = 400 #Near the desk.
                    show screen hermione_02 #Hermione stands still.
                    show screen bld1
                    with Dissolve(.3)
                    $herView.showQQ( "body_69.png", pos )
                    her "Просто на всякий случай..."
                    stop music fadeout 1.0
                    $herView.hideQ( d5 )

                    show screen blkfade
                    with Dissolve(1)
                    $ renpy.play('sounds/08_hop_on_desk.mp3') #Sound of the desk squeaking. 
                    pause 5
                    $ posHead = gMakePos( 390, 340 )

                    $herViewHead.showQ( "body_16.png", posHead )
                    her2 "Просто для протокола..."
                    her2 "Я все еще считаю, что это совершенно недопустимо, покупать одну из своих студенток, сэр."
                    $herViewHead.hideQ()
                    m "Правильно. И еще более неуместно продавать себя своему директору. Согласна?"
                    $herViewHead.showQ( "body_69.png", posHead )
                    her ".........."
                    $herViewHead.hideQ()
                    hide screen blkfade
                    hide screen bld1
                    $ hermione_chibi_xpos = 210 #Near the desk: 400.
                    $ hermione_chibi_ypos = 180 #Default: 250
                    show screen clothed_dance #Hermione stands still.
                    show screen ctc
                    with fade
                    pause
                    show screen no_vest_dance
                    with d3
                    pause
                    show screen bld1
                    hide screen ctc
                    with d3
                    $herViewHead.showQ( "body_87.png", posHead )
                    play music "music/(Orchestral) Playful Tension by Shadow16nh.mp3" fadein 1 fadeout 1 # SEX THEME.
                    her ".............."
                    $herViewHead.addFaceName( "body_85.png" )
                    her2 "Что, если мои родители узнают об этом, сэр?"
                    her2 "Мама никогда не поймет..."
                    $herViewHead.addFaceName( "body_44.png" )
                    her "А насчет моего отца..."
                    $herViewHead.hideQ()
                    menu:
                        m "..."
                        "{size=-3}\"Твой отец гордился бы тобой!\"{/size}":
                            $herViewHead.showQ( "body_44.png", posHead )
                            her "Я сомневаюсь..."
                            her "Да, я делаю это в благих целях, но..."
                            $herViewHead.showQ( "body_61.png", posHead )
                            her "Он никогда не видел меня такой..."
                            her "Он никогда не должен узнать об этом..."
                            $herViewHead.hideQ()
                        "{size=-3}\"Твой папочка отшлепал бы тебя!\"{/size}":
                            $herViewHead.showQ( "body_48.png", posHead )
                            her "Он бы не посмел!"
                            $herViewHead.addFaceName( "body_44.png" )
                            her "И, в любом случае, я уже взрослая для такого..."
                            $herViewHead.hideQ()
                            g9 "Я бы сказал, что ты в идеальном возрасте для такого..."
                            $herViewHead.showQ( "body_57.png", posHead )
                            her "А?"
                            her "Я не понимаю о чем вы, сэр."
                            $herViewHead.hideQ()
                        "{size=-3}\"Твой папочка отрекся бы от тебя!\"{/size}":
                            $herViewHead.showQ( "body_34.png", posHead )
                            her "Вы, вероятно, правы, сэр..."
                            $herViewHead.addFaceName( "body_22.png" )
                            her "(Ох, папочка, мне очень жаль...)"
                            $herViewHead.addFaceName( "body_21.png" )
                            her "Он никогда не должен узнать..."
                            $herViewHead.hideQ()
                        "{size=-3}\"Твой отец хотел бы посмотреть на это!\"{/size}":
                            $herViewHead.showQ( "body_33.png", posHead )
                            her "Нет! Ему было бы стыдно за меня!"
                            $herViewHead.hideQ()
                            m "Ты в этом уверена?"
                            $herViewHead.showQ( "body_32.png", posHead )
                            her "Абсолютно! Мой папа - культурный человек!"
                            $herViewHead.hideQ()
                            m "Но {size=+4}он{/size} {size=+4}мужчина{/size}, верно?"
                            $herViewHead.showQ( "body_50.png", posHead )
                            her "....................."
                            $herViewHead.addFaceName( "body_29.png" )
                            her "Папа никога не должен узнать об этом..."
                            $herViewHead.hideQ()
                    show screen blktone
                    with d3
                    ">Гермиона начнает соблазнительно качать бедрами, пока ее юбка соскальзывает с ее тела..."
                    hide screen blktone
                    with d3
                    hide screen bld1
                    with d3
                    show screen ctc
                    pause
                    show screen no_skirt_dance
                    with d3
                    pause
                    hide screen ctc
                    show screen bld1
                    with d3
                    
                    $herViewHead.showQ( "body_31.png", posHead )
                    her "Профессор?"
                    $herViewHead.hideQ()
                    m "А?"
                    $herViewHead.showQ( "body_44.png", posHead )
                    her "Могу я задать вопрос?"
                    $herViewHead.hideQ()
                    m "Попробуй..."
                    $herViewHead.showQ( "body_33.png", posHead )
                    her "..............."
                    $herViewHead.addFaceName( "body_57.png" )
                    her "Вы когда-нибудь любили...?"
                    $herViewHead.hideQ()
                    menu:
                        m "..."
                        "\"Это смешно! Любовь - это ложь!\"":
                            $herViewHead.showQ( "body_29.png", posHead )
                            her "Очень жаль, что вы так считаете, сэр!"
                            $herViewHead.addFaceName( "body_50.png" )
                            her "Но вы можете очень сильно ошибаться!"
                            $herViewHead.addFaceName( "body_54.png" )
                            her2 "Я считаю, что настоящая любовь вращает Землю!"
                            $herViewHead.hideQ()
                            m "На самом деле, момент сохранения импульса отвечает за это."
                            $herViewHead.showQ( "body_44.png", posHead )
                            her "А?"
                            $herViewHead.hideQ()
                            m "Забудь. Готова снять рубашку?"
                            $herViewHead.showQ( "body_50.png", posHead )
                            her "............"      
                            $herViewHead.hideQ()
                        "\"Молчи и продолжай танцевать\"":
                            $herViewHead.showQ( "body_50.png", posHead )
                            her "Но вы сказали, что я могу задать вопрос..."
                            $herViewHead.hideQ()
                            m "И ты это сделала, не так ли?"
                            $herViewHead.showQ( "body_31.png", posHead )
                            her "!!!............"
                            $herViewHead.addFaceName( "body_50.png" )
                            her2 "...................................."
                            $herViewHead.hideQ()
                            m "Теперь, снимай свою рубашку."
                            $herViewHead.showQ( "body_69.png", posHead )
                            her "........"
                            $herViewHead.hideQ()
                        "\"Да... очень и очень давно...\"":
                            $herViewHead.hideQ()
                            m "Да... очень и очень давно..."
                            $herViewHead.showQ( "body_31.png", posHead )
                            her2 "!!!!!??.............................."
                            $herViewHead.hideQ()
                            m "Ее имя было Эден..."
                            $herViewHead.showQ( "body_45.png", posHead )
                            her "Она была красива?"
                            $herViewHead.hideQ()
                            m "Более чем..."
                            m "Она была умна, зелена и совершенна..."
                            $herViewHead.showQ( "body_87.png", posHead )
                            her "Она была...{w} \"зелена\"...?"
                            $herViewHead.addFaceName( "body_47.png" )
                            her2 "Вы издеваетесь, сэр?"
                            $herViewHead.hideQ()
                            m "Ох, вы, люди, ничего не знаете о настоящей любви..."
                            $herViewHead.showQ( "body_55.png", posHead )
                            her ".....................................?"
                            $herViewHead.hideQ()
                            m "Э-э...то есть, снимай рубашку, девочка!"
                            $herViewHead.showQ( "body_69.png", posHead )
                            her "................."
                            $herViewHead.hideQ()
                        "\"Мне кажется, я влюбляюсь прямо сейчас!\"":
                            $herViewHead.showQ( "body_69.png", posHead )
                            her "Не нужно быть таким вульгарным, сэр."
                            $herViewHead.hideQ()
                            m "Ох, но мне кажется, что это так!"
                            $herViewHead.showQ( "body_66.png", posHead )
                            her "Сэр, Пожалуйста!"
                            $herViewHead.addFaceName( "body_55.png" )
                            her "Я одна из ваших студенток!"
                            $herViewHead.addFaceName( "body_57.png" )
                            her "И вы старше моего отца!"
                            $herViewHead.hideQ()
                            m "{size=-4}(Даже не представляешь насколько, девочка.){/size}"
                            $herViewHead.showQ( "body_55.png", posHead )
                            her2 "Некоторые ученые считают, что \"любовь\" это не что иное, как химическая реакция..."
                            $herViewHead.addFaceName( "body_16.png" )
                            her2 "И, когда человек испытывает сексуальное влечение, тот же тип гормонов--"
                            $herViewHead.hideQ()
                            m "Мисс Грейнджер!"
                            $herViewHead.showQ( "body_15.png", posHead )
                            her "Да, сэр?"
                            $herViewHead.hideQ()
                            m "Вы забыли чем мы занимаемся?"
                            $herViewHead.showQ( "body_24.png", posHead )
                            her "Ох, мои извинения, сэр... Иногда я отвлекаюсь."
                            $herViewHead.hideQ()
                            m "Давай ты уже снимешь свою рубашку?!"
                            $herViewHead.showQ( "body_29.png", posHead )
                            her "Верно..."
                            $herViewHead.hideQ()
                    show screen blktone
                    with d3
                    ">Гермиона расстегивает последнюю пуговицу на рубашке и изящно скидывает ее..."
                    hide screen blktone
                    with d3
                    hide screen bld1
                    with d3
                    show screen ctc
                    pause
                    show screen no_shirt_no_skirt_dance
                    with d3
                    pause
                    hide screen ctc
                    show screen bld1
                    with d3
                    g9 "Да! Сиськи!"
                    
                    
                    
                    $ posHead = gMakePos( 390, 235 )
                    $herViewHead.data().hideItem('dress')
                    $herViewHead.showQ( "body_90.png", posHead )
                    her "Вам обязательно быть настолько пошлым, сэр?"
                    $herViewHead.hideQ()
                    menu: 
                        "- Достать член и начать дрочить -":
                            hide screen bld1
                            show screen ctc
                            with d3
                            pause
                            show screen blkfade
                            with d6
                            $herViewHead.showQ( "body_94.png", posHead )
                            her "Профессор Дамблдор?!"
                            $herViewHead.hideQ()
                            m "Все в порядке, девочка. Доверься мне..."
                            
                            
                            hide screen genie
                            hide screen no_shirt_no_skirt_dance
                            $ genie_chibi_xpos = -185
                            $ genie_chibi_ypos = 10
                            $ g_c_u_pic = "jerking_off_02_ani"
                            show screen chair_02
                            show screen g_c_u
                            show screen desk_02
                            show screen no_shirt_no_skirt_dance
                            hide screen blkfade
                            with fade
                            pause
                            show screen bld1
                            with d3
                            $herViewHead.showQ( "body_95.png", posHead )
                            her "Н-но..."
                            her "Ваш..."
                            $herViewHead.hideQ()
                            m "Да... Ах, да, это великолепно..."
                            $herViewHead.showQ( "body_98.png", posHead )
                            her "Профессор!!!"
                            her "Я хочу, чтобы вы убрали эту..."
                            $herViewHead.addFaceName( "body_99.png" )
                            her "...штуку."
                            $herViewHead.hideQ()
                            menu:
                                m "..."
                                "\"Я сказал, продолжай танцевать, девочка!\"":
                                    if whoring >= 15: #LEVEL 06. You jerk off your cock and Hermione is OK with it.
                                        $herViewHead.showQ( "body_99.png", posHead )
                                        her "Но..."
                                        her "............................."
                                        $herViewHead.addFaceName( "body_101.png" )
                                        her2 "Ну, ладно, но только если вы пообешаете мне на кончать, сэр."
                                        $herViewHead.hideQ()
                                        menu:
                                            m "..."
                                            "- Пообещать сдержаться -":
                                                    $ d_flag_07 = True #Promised to hold it.
                                                    $herViewHead.showQ( "body_102.png", posHead )
                                                    her "Ну, тогда ладно..."
                                                    $herViewHead.hideQ()
                                            "- Не давать такого обещания -":
                                                $ d_flag_07 = False #Did not promise to hold it.
                                                m "\"Не кончать\"? Это похоже на пытку!"
                                                m "Пожалуйста, сдержите свои садистские наклонности, Мисс Грейнджер."
                                                $herViewHead.showQ( "body_103.png", posHead )
                                                her2 "У меня нет никаких... садистcких наклонностей, сэр!"
                                                her "Я просто хочу, чтобы..."
                                                $herViewHead.hideQ()
                                                g9 "Да... У тебя такие отличные сиськи..."
                                                $herViewHead.showQ( "body_97.png", posHead )
                                                her "............"
                                                $herViewHead.hideQ()
                                                g9 "А-ах... Да..."
                                                $herViewHead.showQ( "body_97.png", posHead )
                                                her ".........."
                                                $herViewHead.addFaceName( "body_99.png" )
                                                her "Ладно! Будь по вашему, сэр!"
                                                $herViewHead.addFaceName( "body_103.png" )
                                                her "{size=-5}(Как обычно...){/size}"
                                                $herViewHead.hideQ()
                                        show screen blktone
                                        with d3
                                        ">Вы продолжаете дрочить, наблюдая за Гермионой..."
                                        $herViewHead.showQ( "body_90.png", posHead )
                                        her "Время кончать, я полагаю..."
                                        $herViewHead.hideQ()
                                        m "Да, девочка! Снимай свои трусики!"
                                        $herViewHead.showQ( "body_91.png", posHead )
                                        her "........"
                                        $herViewHead.hideQ()
                                        show screen blktone8
                                        with d3
                                        ">Гермиона слегка наклоняется и стягивает с себя трусики..."
                                        ">Вы видите, что она делает все возможное, чтобы это выглядело изящно..."
                                        ">Но ее попытки выглядеть, как настоящая стриптизерша, довольно смешны..."
                                        hide screen blktone8 
                                        hide screen blktone
                                        with d3
                                        hide screen bld1
                                        with d3
                                        pause
                                        $ h_c_u_pic = "no_panties_dance_ani"
                                        hide screen no_shirt_no_skirt_dance
                                        show screen h_c_u
                                        with d3
                                        pause
                                        show screen bld1
                                        with d3
                                        show screen blktone
                                        with d3
                                        ">Тем не менее, вы показываете ей, что у нее получается весьма неплохо..."
                                        ">Начиная дрочить еще быстрее!"
                                        $herViewHead.showQ( "body_91.png", posHead )
                                        her ".........."
                                        $herViewHead.hideQ()
                                        show screen blktone8
                                        with d3
                                        ">Внезапно, Гермиона начинает выдавать целые сложные пируэты..."
                                        m "{size=-4}(Это выглядит очень даже не дурно...){/size}"
                                        ">Гермиона хватает и слегка скручивает свои сиськи, после чего снова делает серию сложны пируэтов (иногда нелепых)..."
                                        m "{size=-4}(Она практиковалась?){/size}"
                                        g9 "Ох, какое мне дело?"
                                        ">Вы начинаете еще сильнее надрачивать ваш твердый как алмаз член."
                                        $herViewHead.showQ( "body_102.png", posHead )
                                        her "{size=-5}(Три-два-раз... Три-два-раз... И шаг!){/size}"
                                        $herViewHead.hideQ()
                                        ">Гермиона выполняет другую партию движений, которые выглядет весьма стильно..."
                                        ">Ее упругие сиськи подпрыгивают в такт танцу..."
                                        g9 "Да, да, маленькая шлюха!"
                                        ">Еще несколько движений, пара жестов и небольшой реверанс-поклон воображаемой публике..."
                                        show screen blkfade
                                        with d3
                                        $ hermione_chibi_xpos = -210 #400 = Near the desk.
                                        $ hermione_chibi_ypos = 10
                                        $ h_c_u_pic = "03_hp/08_animation_02/08_sits.png"
                                        ">И под конец она падает на свою попку."
                                        hide screen blktone
                                        with d3
                                        hide screen blktone8
                                        with d3
                                        hide screen blkfade
                                        with d3
                                        hide screen bld1 
                                        with d3
                                        pause
                                        $herViewHead.showQ( "body_102.png", posHead )
                                        her "Фиу... Это было--"
                                        $herViewHead.hideQ()
                                        with hpunch
                                        g4 "АРГХ! ЕБАНАЯ ДЫРКА!"
                                        $herView.hideQQ()
                                        show screen white 
                                        pause.1
                                        hide screen white
                                        pause.2
                                        show screen white 
                                        pause .1
                                        hide screen white
                                        with hpunch
                                        $ genie_chibi_xpos = -210
                                        $ genie_chibi_ypos = 10
                                        $ genie_cum_chibi_xpos =  -210
                                        $ genie_cum_chibi_ypos  = 10
                                        $ g_c_c_u_pic = "genie_cum_03"
                                        $ h_c_u_pic = "03_hp/08_animation_02/08_sits_02.png"
                                        show screen g_c_c_u
                                        pause
                                        
                                        $herViewHead.data().addItem( 'sperm', CharacterExItem( herViewHead.mMiscFolder, 'sperm_01.png', G_Z_FACE + 1 ) )
                                        $herViewHead.showQ( "body_104.png", posHead )
                                        her "??!!!"
                                        $herViewHead.hideQ()
                                        show screen bld1
                                        with d3
                                        $herViewHead.showQ( "body_97.png", posHead )
                                        her "Профессор!!!"
                                        $ g_c_c_u_pic = "03_hp/08_animation_02/09_cum_18.png"
                                        $herViewHead.hideQ()
                                        if d_flag_07: #Promised to hold it.
                                            $herViewHead.showQ( "body_97.png", posHead )
                                            her "Нет, профессор! Вы же обещали!"
                                            $herViewHead.hideQ()
                                            g4 "Ох, детка... Это было довольно круто..."
                                            $herViewHead.showQ( "body_98.png", posHead )
                                            her "ВЫ не сдержали слово, сэр!"
                                            $herViewHead.hideQ()
                                            m "А? О чем ты говоришь?"
                                            $herViewHead.showQ( "body_113.png", posHead )
                                            her "Как вы могли так со мной поступить, сэр?"
                                            $herViewHead.hideQ()
                                            m "Ох, успокойся, девочка."
                                            m "Сегодня ты заслужила свои очки."
                                            m "Теперь, просто оденься и уходи, пока кто-нибудь не застукал нас тут."
                                            $herViewHead.showQ( "body_114.png", posHead )
                                            her "*всхлип!*........................"
                                            $herViewHead.hideQ()
                                            $ mad += 50
                                            show screen blkfade 
                                            with d3
                                            
                                            $herViewHead.data().delItem( 'sperm' )
                                            $herViewHead.data().addItem( 'sperm_after', CharacterExItem( herView.mMiscFolder, 'sperm_00_after.png', G_Z_FACE + 1 ) )
                                            stop music fadeout 5.0
                                            ">.................{w}.................{w}.................{w}................."
                                            call req11_dress
                                            $herViewHead.showQ( "body_12.png", posHead )
                                            her "...Могу я получить оплату, сэр... пожалуйста?"
                                            $herViewHead.hideQ()
                                            jump done_with_dancing
                                        else:
                                            $herViewHead.showQ( "body_97.png", posHead )
                                            her "Было жарко..."
                                            $herViewHead.hideQ()
                                            $ g_c_u_pic = "03_hp/08_animation_02/06_jerking_01.png" # Genie stands still with his dick in hand.
                                            m "Аха... Даа... Это просто безумие..."
                                            $herViewHead.showQ( "body_105.png", posHead )
                                            her "Вы всю меня обкончали..."
                                            her "Я же ваш ученик..."
                                            $herViewHead.showQ( "body_106.png", posHead )
                                            her "Вы просто кончили на меня..."
                                            $herViewHead.hideQ()
                                            g9 "Я знаю! Довольно круто, да?!"
                                            $herViewHead.showQ( "body_107.png", posHead )
                                            her "Ничего подобного!"
                                            #her "You should not have done this, сэр!"
                                            her2 "Вы должны вести себя, как подобает директору!"
                                            $herViewHead.hideQ()
                                            m "Правда? Что же ты хотела от меня?"
                                            m "Направить его в сторону стены или обратно в трусы и просто кончить?"
                                            $herViewHead.showQ( "body_105.png", posHead )
                                            her "........"
                                            $herViewHead.showQ( "body_101.png", posHead )
                                            her "Тем не менее, вы не должны были..."
                                            $herViewHead.showQ( "body_102.png", posHead )
                                            her "Я согласилась танцевать для вас..."
                                            her2 "Но я не соглашалась быть оскверненной вашей спермой."
                                            $herViewHead.hideQ()
                                            m "Ну, это уже произошло..."
                                            $herViewHead.showQ( "body_100.png", posHead )
                                            her "Я требую дополнительные очки за это!"
                                            $herViewHead.hideQ()
                                            m "Конечно, как иначе..."
                                            menu:
                                                m "..."
                                                "\"Ты получишь 1 дополнительное очко.\"":
                                                    play music "music/Chipper Doodle v2.mp3" fadein 1 fadeout 1 # HERMIONE'S THEME.
                                                    $herViewHead.showQ( "body_101.png", posHead )
                                                    her "Одно дополнительное очко?"
                                                    $herViewHead.addFaceName( "body_98.png" )
                                                    her2 "Одно жалкое очко за все, что вы со мной сделали?"
                                                    $herViewHead.addFaceName( "body_101.png" )
                                                    her "Это просто оскорбительно, сэр!"
                                                    $herViewHead.hideQ()
                                                    m "Одно очко, Мисс Грейнджер. Забирайте или уходите."
                                                    $herViewHead.showQ( "body_103.png", posHead )
                                                    her "............."
                                                    $herViewHead.addFaceName( "body_101.png" )
                                                    her "Я беру его."
                                                    $herViewHead.hideQ()
                                                    $ mad += 30
                                                    $ current_payout = 36
                                                    hide screen bld1
                                                    with d3
                                                    pause
                                                    show screen blkfade
                                                    with d7
                                                    pause.5
                                                    
                                                    $herView.data().addItem( 'sperm_after', CharacterExItem( herView.mMiscFolder, 'sperm_00_after.png', G_Z_FACE + 1 ) )
                                                    jump done_with_dancing
                                                "\"Десять дополнительных очков.\"":
                                                    $ current_payout = 45
                                                    $herViewHead.showQ( "body_101.png", posHead )
                                                    her "Десять дополнительных очков, сэр?"
                                                    her "Но это слишком мало!"
                                                    $herViewHead.hideQ()
                                                    m "Десять очков. Берите или уходите, Мисс Грейнджер."
                                                    $herViewHead.showQ( "body_103.png", posHead )
                                                    her "..............."
                                                    $herViewHead.showQ( "body_101.png", posHead )
                                                    her "Ну ладно... Лучше, чем ничего..."
                                                    $herViewHead.hideQ()
                                                    $ mad += 11
                                                    hide screen bld1
                                                    with d3
                                                    pause
                                                    show screen blkfade
                                                    with d7
                                                    pause.5
                                                    
                                                    $herView.data().addItem( 'sperm_after', CharacterExItem( herView.mMiscFolder, 'sperm_00_after.png', G_Z_FACE + 1 ) )
                                                    jump done_with_dancing
                                                "\"Вы получите 25 дополнительных очков.\"":
                                                    $ current_payout = 60
                                                    $herViewHead.showQ( "body_102.png", posHead )
                                                    her2 "Да, думаю, этого хватит."
                                                    $herViewHead.hideQ()
                                                    m "Теперь вы счастливы?"
                                                    $herViewHead.showQ( "body_102.png", posHead )
                                                    her "Да, сэр. Спасибо сэр."
                                                    $herViewHead.hideQ()
                                                    $ h_c_u_pic = "03_hp/08_animation_02/08_sits.png"
                                                    hide screen bld1
                                                    with d3
                                                    pause
                                                    show screen blkfade
                                                    with d7
                                                    pause.5
                                                    
                                                    $herView.data().addItem( 'sperm_after', CharacterExItem( herView.mMiscFolder, 'sperm_00_after.png', G_Z_FACE + 1 ) )
                                                    jump done_with_dancing
                                                "\"Вы получаете 50 дополнительных очков.\"":
                                                    $ current_payout = 85
                                                    $herViewHead.showQ( "body_95.png", posHead )
                                                    her "Серьезно?!"
                                                    $herViewHead.addFaceName( "body_94.png" )
                                                    her "Ох, не знаю что сказать..."
                                                    $herViewHead.hideQ()
                                                    m "Мне понравилось, Мисс Грейнджер."
                                                    $herViewHead.showQ( "body_109.png", posHead )
                                                    her "Спасибо, сэр..."
                                                    $herViewHead.hideQ()
                                                    m "Так же, мне понравилось заливать твое гибкое тельце своей спермой..."
                                                    $herViewHead.showQ( "body_108.png", posHead )
                                                    her "Сэр......"
                                                    $herViewHead.hideQ()
                                                    m "И так, просто позвольте мне показать свою признательность."
                                                    m "Пятьдесяц очков, заслуженно, Мисс Грейнджер."
                                                    $herViewHead.showQ( "body_108.png", posHead )
                                                    her "Огромное спасибо, сэр."
                                                    $herViewHead.hideQ()
                                                    $ h_c_u_pic = "03_hp/08_animation_02/08_sits.png"
                                                    hide screen bld1
                                                    with d3
                                                    pause
                                                    show screen blkfade
                                                    with d7
                                                    pause.5
                                                    
                                                    $herView.data().addItem( 'sperm_after', CharacterExItem( herView.mMiscFolder, 'sperm_00_after.png', G_Z_FACE + 1 ) )
                                                    jump done_with_dancing
                                                "\"Ты ни черта не получишь!\"":
                                                    stop music fadeout 1.0
                                                    $herViewHead.showQ( "body_104.png", posHead )
                                                    her "Что? Даже обычной платы?"
                                                    $herViewHead.hideQ()
                                                    menu:
                                                        m "..."
                                                        "\"Ох, нет, их ты получишь.\"":
                                                            $ mad += 30
                                                            $herViewHead.showQ( "body_101.png", posHead )
                                                            her "Как великодушно с вашей стороны, сэр." 
                                                            $herViewHead.hideQ()
                                                            hide screen bld1
                                                            with d3
                                                            pause
                                                            show screen blkfade
                                                            with d7
                                                            pause.5
                                                            
                                                            $herView.data().addItem( 'sperm_after', CharacterExItem( herView.mMiscFolder, 'sperm_00_after.png', G_Z_FACE + 1 ) )
                                                            jump done_with_dancing
                                                        "\"Нет, их тоже не получишь!\"":
                                                            play music "music/Chipper Doodle v2.mp3" fadein 1 fadeout 1 # HERMIONE'S THEME.
                                                            $herViewHead.showQ( "body_104.png", posHead )
                                                            her "!!!?"
                                                            her "Я танцевала для вас, сэр..."
                                                            $herViewHead.addFaceName( "body_105.png" )
                                                            her "Я унижалась для вашего веселья..."
                                                            $herViewHead.addFaceName( "body_107.png" )
                                                            her "Позволила кончить на себя..."
                                                            $herViewHead.addFaceName( "body_110.png" )
                                                            with hpunch
                                                            her "И не получу ничего?!"
                                                            $herViewHead.hideQ()
                                                            m "Вы провалились, Мисс Грейнджер!"
                                                            $herViewHead.showQ( "body_101.png", posHead )
                                                            her "Ох, это низко даже для вас, сэр!"
                                                            $herViewHead.hideQ()
                                                            m "Я сказал: вы провалились."
                                                            $herViewHead.showQ( "body_110.png", posHead )
                                                            her "*Тяжелый вздох!*"
                                                            $ mad += 90
                                                            $herViewHead.hideQ()
                                                            hide screen bld1
                                                            with d3
                                                            pause
                                                            show screen blkfade
                                                            with d7
                                                            pause.5
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
                                                            call music_block
                                                            jump restore_state_could_not_flirt #Leaves without getting any очков.
                                                        

                                    else: # You jerk off your cock and Hermione is NOT OK with it.
                                        $herViewHead.showQ( "body_103.png", posHead )
                                        stop music fadeout 1.0
                                        her "Нет, сэр!"
                                        $herViewHead.hideQ()
                                        m "А?"
                                        show screen blkfade
                                        with d7
                                        ">Гермиона спрыгивает со стола и начинает спешно одеваться, посматривая на вас..."
                                        m "Ох, да ладно! Не оставляй меня так!"
                                        $ posHead = gMakePos( 390, 340 )
                                        $herViewHead.showQ( "body_101.png", posHead )
                                        her "Танец окончен, сэр!"
                                        $herViewHead.hideQ()
                                        pause 1
                                        call req11_dress
                                        $herViewHead.showQ( "body_79.png", posHead )
                                        her "Я хотела бы получить очки!"
                                        $herViewHead.hideQ()
                                        m "Упрямая девчонка..."
                                        ">Вы неохотно убрали свой член..."
                                        $herViewHead.showQ( "body_79.png", posHead )
                                        her "Полагаю, я могу получить сейчас свою оплату."
                                        $herViewHead.hideQ()
                                        jump done_with_dancing
                                "\"Ладно. Не драматизируй ты так!\"": 
                                    $herViewHead.showQ( "body_103.png", posHead )
                                    her2 "......................"
                                    $herViewHead.hideQ()
                                    pause.1
                                    hide screen no_shirt_no_skirt_dance
                                    show screen genie
                                    hide screen chair_02
                                    hide screen g_c_u
                                    hide screen desk_02
                                    show screen no_shirt_no_skirt_dance
                                    hide screen blkfade
                                    with fade
                                    pause
                                    show screen bld1
                                    with d3
                                    pass

                        "- Показать хорошие манеры и просто смотреть -":
                            pass
                    # JUST WATCHING.
                    show screen blktone
                    with d3
                    ">Вы смотрите танец Гермионы..."
                    $herViewHead.showQ( "body_97.png", posHead )
                    her "(Время заканчивать, я полагаю...)"
                    $herViewHead.hideQ()
                    m "Да! Снимай их!"
                    $herViewHead.showQ( "body_90.png", posHead )
                    her "........"
                    $herViewHead.hideQ()
                    show screen blktone8
                    with d3
                    ">Гермиона нагибается и стягивает свои трусики..."
                    ">Она делает все возможное, чтобы это выглядело изящно..."
                    ">Но ее попытки выглядеть как настоящая стриптизерша выглядят довольно смешно..."
                    $herViewHead.showQ( "body_109.png", posHead )
                    her ".........."
                    $herViewHead.hideQ()
                    ">Внезапно, она начинает выдавать целые пируэты..."
                    $herViewHead.hideQ()
                    m "{size=-4}(Это довольно неплохо...){/size}"
                    ">Гермиона хватает и слегка скручивает свои сиськи, после чего снова делает серию сложны пируэтов (иногда нелепых)..."
                    m "{size=-4}(Она практиковалась?){/size}"
                    g9 "Ох, какое мне дело?"
                    $herViewHead.showQ( "body_102.png", posHead )
                    her "{size=-5}(Три-два-раз... Три-два-раз... и шаг!){/size}"
                    $herViewHead.hideQ()
                    ">Гермиона выполняет довольно сложные движения, которые были бы весьма стильными, если бы не ее прыгающие в разные стороны сиськи..."
                    g9 "Да, да, маленькая потаскушка!"
                    
                    show screen blkfade
                    with d3
                    $ hermione_chibi_xpos = -210 #400 = Near the desk.
                    $ hermione_chibi_ypos = 10
                    $ h_c_u_pic = "03_hp/08_animation_02/08_sits.png"
                    ">Еще несколько движений, пара жестов, поклон воображаемой аудитории и Гермиона мягко шлепается на свою замучанную попку."
                    show screen h_c_u
                    hide screen blktone
                    with d3
                    hide screen blktone8
                    with d3
                    hide screen blkfade
                    with d3
                    hide screen bld1 
                    with d3
                    pause
                    $herViewHead.showQ( "body_108.png", posHead )
                    show screen bld1
                    with d3
                    her "Фиу... Было весьма захватывающе..."
                    $herViewHead.hideQ()
                    menu:
                        m "..."
                        "{size=-3}\"Отличная работа, девочка! Ты правда знаешь в этом толк!\"{/size}":
                            m "Отличная работа, девочка!"
                            $herViewHead.showQ( "body_109.png", posHead )
                            her "Правда?"
                            $herViewHead.hideQ()
                            m "Да! У тебя есть талант!"
                            $herViewHead.showQ( "body_108.png", posHead )
                            her "Спасибо, сэр."
                            $herViewHead.hideQ()
                        "{size=-3}\"Хм... Это было ужасно...\"{/size}":
                            $herViewHead.showQ( "body_105.png", posHead )
                            her "Ох... Мне жаль..."
                            $herViewHead.hideQ()
                            m "Ничего... Тебе просто нужно практиковаться..."
                            $herViewHead.showQ( "body_107.png", posHead )
                            her "Эм... Буду иметь в виду, сэр..."
                            $herViewHead.hideQ()
                        "{size=-3}\".................................................\"{/size}":
                            $herViewHead.showQ( "body_108.png", posHead )
                            her "......................."
                            $herViewHead.hideQ()

                    
                    $ h_c_u_pic = "03_hp/08_animation_02/08_sits.png"
                    hide screen bld1
                    show screen ctc
                    with d3
                    pause
                    show screen blkfade
                    with d7
                    pause.5

                            
        else: #Stripping only for Genie.
            jump no_snape_watching 

        
        

    label done_with_dancing:
    call req11_dress
    $herView.data().delItem( 'sperm' )
    
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
    $herViewHead.hideQ()
    $herView.hideQ()
    hide screen blkfade
    with d3
    
    
    m "Да, Мисс Грейнджер. [current_payout] очков \"Гриффиндору\"." 
    $ pos = POS_140
    $herView.showQ( "body_13.png", pos )
    hide screen hermione_01_f #Hermione stands still.
    with d3
    
    her "Спасибо, сэр..."

    if whoring <= 11:
        $ whoring +=1

    $ request_11_points += 1
    



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

    $herView.data().loadState()
    call music_block
    if daytime:
        $ hermione_takes_classes = True
        jump night_main_menu
    else:
        $ hermione_sleeping = True
        jump day_main_menu       


label restore_state_could_not_flirt:
    $herView.data().loadState()
    jump could_not_flirt

label req11_undress:
    $herView.data().hideItem( 'dress' )
    $herView.data().hideItem( 'skirt' )
    $herView.data().hideItem( 'panties' )
    return
    
label req11_dress:
    $herView.data().showItem( 'dress' )
    $herView.data().showItem( 'skirt' )
    $herView.data().showItem( 'panties' )
    return
