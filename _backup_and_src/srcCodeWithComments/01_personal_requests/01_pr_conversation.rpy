################
### LEVEL 01 ###                
###################REQUEST_01 JUST STAND THERE.
label new_request_01: #LV.1 (Whoring = 0 - 2)
    #__#hide screen hermione_main
    #__#with d3
    $herView.hideQQ()
    m "{size=-4}(Я просто поговорю с ней...){/size}"
    menu:
        "\"(Да, сделаем это.)\"":
            pass
        "\"(Не сейчас.)\"":
            jump new_personal_request
    play music "music/Chipper Doodle v2.mp3" fadein 1 fadeout 1 
    m "Ладно..."
    m "Просто расскажи что нового у тебя."
    #__#hide screen hermione_main
    #__#with d3
    $herView.hideQQ()
    #__#$ h_xpos=140 #Defines position of the Hermione's full length sprite. (Default 370).
    $ pos = POS_140
    #__#$ h_body = "03_hp/13_hermione_main/body_08.png" #Sprite of Hermione's upper body.
    #__#show screen hermione_main
    #__#with d3
    $herView.showQQ( "body_08.png", pos )
    
    if request_01 == 0: #First time this event taking place.
        her "Эм... Ладно..."
        her "Мне просто стоять здесь и говорить...? Как сейчас?"
    else:
        her "В центре, верно? Я помню..."
    #__#hide screen hermione_main
    #__#with d3
    $herView.hideQQ()
    $ menu_x = 0.5 #Menu is moved to the left side.
    #__#$ h_xpos=120 #Defines position of the Hermione's full length sprite.
    #__#$ h_ypos=0
    #__#$ pos = POS_120
    #__#$ h_body = "03_hp/13_hermione_main/body_01.png" #Sprite of Hermione's upper body.
    
    show screen blktone 
    with d3
    show screen ctc
    #__#show screen hermione_main
    $herView.showQ( "body_01.png", pos )
    with Dissolve(.3)
    pause
    
    $pos = POS_140
    m "Ну?"
    if request_01 == 0 and whoring <=5: #First time this event taking place.
        $  new_request_01_01 = True #Hearts on menu buttons.
        #__#hide screen hermione_main
        #__#with d3
        $herView.hideQQ()
        #__#$ h_xpos=140 #Defines position of the Hermione's full length sprite. (Default 370).
        #__#$ pos = POS_140
        #__#$ h_body = "03_hp/13_hermione_main/body_11.png" #Sprite of Hermione's upper body.
        #__#show screen hermione_main
        #__#with d3
        $herView.showQQ( "body_11.png", pos )
        her "Эм... Ну чтож..."
        ">Гермиона чувствует смущение..."
        #__#hide screen hermione_main
        #__#with d3
        $herView.hideQQ()
        #__#$ h_body = "03_hp/13_hermione_main/body_12.png" #Sprite of Hermione's upper body.
        #__#$ h_xpos=140 #Defines position of the Hermione's full length sprite. (Default 370).
        #__#show screen hermione_main
        #__#with d3
        $herView.showQQ( "body_12.png", pos )
        her "..................."
    if whoring >= 0 and  whoring <= 5: #LEVEL 01 and LEVEL 02
        if whoring >= 3 and whoring <= 5:
            $ level = "02"
            $ new_request_01_02 = True #Hearts on menu buttons.
        #__#hide screen hermione_main
        #__#with d3
        $herView.hideQQ()
        #__#$ h_body = "03_hp/13_hermione_main/body_12.png" #Sprite of Hermione's upper body.
        #__#$ h_xpos=140 #Defines position of the Hermione's full length sprite. (Default 370).
        #__#$ pos = POS_140
        #__#show screen hermione_main
        #__#with d3
        $herView.showQQ( "body_12.png", pos )
        her "Последнее время все относительно спокойно, ничего такого..."
        her "Кроме того дня, когда я завалила тест..."
        her "Все еще не могу поверить в это..."
        menu: 
            "- Дрочить пока она говорит -":
                $ d_flag_01 = True #If TRUE genie jerks off under the desk.    
                #__#hide screen hermione_main
                $herView.hideQ() #"WARNING_Z"
                hide screen blktone
                with d3
                ">Вы опускаете руки под стол и обхватываете свой член..."
                hide screen blktone8
                with d3
                hide screen genie
                show screen genie_jerking_off
                with d3
                pause
                #__#hide screen hermione_main
                #__#with d3
                $herView.hideQQ()
                #__#$ h_body = "03_hp/13_hermione_main/body_14.png" #Sprite of Hermione's upper body.
                #__#$ h_xpos=370 #Defines position of the Hermione's full length sprite. (Default 370). (Center: 140)
                $ pos = POS_370
                #__#show screen hermione_main
                #__#with d3
                $herView.showQQ( "body_14.png", pos )
                her "Профессор, что вы делаете?"
                m "Что, ничего. Просто чешу свою ногу."
                m "Так о чем ты говорила?"
                #__#hide screen hermione_main
                #__#with d3
                $herView.hideQQ()
                #__#$ h_body = "03_hp/13_hermione_main/body_14.png" #Sprite of Hermione's upper body.
                #__#$ h_xpos=370 #Defines position of the Hermione's full length sprite. (Default 370). (Center: 140)
                #__#show screen hermione_main
                #__#with d3
                $herView.showQQ( "body_14.png", pos )
                her "Да... Ну, тот тест я провалила..."
            "- Слушать ее -":
                $ d_flag_01 = False #NOT JERKING OFF.
                m "Да, это такая трагедия..."
                her "Именно! я рада, что вы понимаете меня, профессор."
                pass
        her "Подумайте об этом, мне больше не о чем говорить..."
        m "Хорошо, что еще произошло за последнее время?"
        her "Эм... Ну, у меня очень хорошо идут дела с биологией..."
        her "Я имею в виду, у меня всегда хорошие оценки, но я все равно учусь усерднее..."
        her "Иногда мне кажется, что я знаю намного больше чем профессор Стебль..."
        if d_flag_01:
            m "{size=-4}(Да... ах...){/size}"
        else:
            # translators "(Sprout - росток, отросток. В книгах/фильмах ее зовут Памона Спраут/Памона Стебль.  Еще одна игра слов.)"
            m "(Профессор Стебль... Хе-хе, забавное имя...)"
        
        #__#hide screen hermione_main                                                                                                                                                                                   #HERMIONE
        #__#with d3                                                                                                                                                                                                                        #HERMIONE
        $herView.hideQQ()
        #__#$ h_body = "03_hp/13_hermione_main/body_07.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
        #__#show screen hermione_main                                                                                                                                                                                 #HERMIONE
        #__#with d3                                                                                                                                                                                                                        #HERMION
        $herView.showQQ( "body_07.png", pos )
        her "Вы что-то сказали?"
        m "Ничего, продолжай..."
        #__#hide screen hermione_main                                                                                                                                                                                   #HERMIONE
        #__#with d3                                                                                                                                                                                                                        #HERMIONE
        $herView.hideQQ()
        #__#$ h_body = "03_hp/13_hermione_main/body_14.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
        #__#show screen hermione_main                                                                                                                                                                                 #HERMIONE
        #__#with d3                                                                                                                                                                                                                        #HERMIONE
        $herView.showQQ( "body_14.png", pos )
        her "Ну, некоторые студенты смеются над профессором Квирреллом..."
        her "Конечно же я не одобряю такое поведение."
        if d_flag_01:
            m "{size=-4}(Давай же! Скажи что-нибудь грязное!){/size}"
        else:
            m ".................."
        her "О, мое \"Общество по защите мужских прав\" набирает популярность..."
        her "И я очень рада..."
        #__#hide screen hermione_main                                                                                                                                                                                   #HERMIONE
        #__#with d3                                                                                                                                                                                                                        #HERMIONE
        $herView.hideQQ()
        #__#$ h_body = "03_hp/13_hermione_main/body_16.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
        #__#show screen hermione_main                                                                                                                                                                                 #HERMIONE
        #__#with d3                                                                                                                                                                                                                        #HERMIONE
        $herView.showQQ( "body_16.png", pos )
        her "Я думаю, с учетом всего времени, мы действительно сможем что-нибудь изменить..."
        #__#hide screen hermione_main                                                                                                                                                                                   #HERMIONE
        #__#with d3                                                                                                                                                                                                                        #HERMIONE
        $herView.hideQQ()
        #__#$ h_body = "03_hp/13_hermione_main/body_06.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
        #__#show screen hermione_main                                                                                                                                                                                 #HERMIONE
        #__#with d3                                                                                                                                                                                                                        #HERMIONE
        $herView.showQQ( "body_06.png", pos )
        her "Да, то, что вы делаете это, очень ободряет нас."
        her "Разве вы не согласны?"
        if d_flag_01:
            m "{size=-4}(Черт. Теперь она полностью убила все желание...){/size}"
            show screen genie
            with d3
            $ d_flag_01 = False #NOT JERKING OFF ANY MORE.
            pass
        else:
            m "*Зевает*........"
            
        #__#hide screen hermione_main                                                                                                                                                                                   #HERMIONE
        #__#with d3                                                                                                                                                                                                                        #HERMIONE
        $herView.hideQQ()
        #__#$ h_body = "03_hp/13_hermione_main/body_05.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
        #__#show screen hermione_main                                                                                                                                                                                 #HERMIONE
        #__#with d3                                                                                                                                                                                                                        #HERMIONE
        $herView.showQQ( "body_05.png", pos )
        her "Профессор?"
        m "Да, да, я внимательно слушаю..."
        m "Это все очень самооправданно, э-э..."
        m "То есть, очень помогает нам и поддерживает..."
        #__#hide screen hermione_main                                                                                                                                                                                   #HERMIONE
        #__#with d3                                                                                                                                                                                                                        #HERMIONE
        $herView.hideQQ()
        #__#$ h_body = "03_hp/13_hermione_main/body_07.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
        #__#show screen hermione_main                                                                                                                                                                                 #HERMIONE
        #__#with d3                                                                                                                                                                                                                        #HERMIONE
        $herView.showQQ( "body_07.png", pos )
        her ".........................."
  
    elif whoring >= 6: #LEVEL 03
        $  new_request_01_03 = True #Hearts on menu buttons.
        #__#hide screen hermione_main
        #__#with d3
        $herView.hideQQ()
        #__#$ h_body = "03_hp/13_hermione_main/body_12.png" #Sprite of Hermione's upper body.
        #__#$ h_xpos=140 #Defines position of the Hermione's full length sprite. (Default 370).
        #__#$ pos = POS_140
        #__#show screen hermione_main
        #__#with d3
        $herView.showQQ( "body_12.png", pos )
        her "У меня в последнее время все вроде-как в порядке..."
        her "Хм..."
        her "Сейчас факультеты \"Слизерина\" и \"Гриффиндора\" очень сильно соперничают."
        her "Если честно, то этого не должно быть..."
        her "\"Гриффиндор\" был бы в лидерах, если бы не \"Слизеринские\" шлюхи..."
        her "Я только и слышу, что они получают свои очки за \"услуги\"..."
        #__#hide screen hermione_main
        #__#with d3
        $herView.hideQQ()
        #__#$ h_body = "03_hp/13_hermione_main/body_04.png" #Sprite of Hermione's upper body.
        #__#$ h_xpos=140 #Defines position of the Hermione's full length sprite. (Default 370).
        #__#show screen hermione_main
        #__#with d3
        $herView.showQQ( "body_04.png", pos )
        her "Очень подло!"
        m "И что же вы теперь будете делать, мисс Грейнджер?"
        #__#hide screen hermione_main
        #__#with d3
        $herView.hideQQ()
        #__#$ h_body = "03_hp/13_hermione_main/body_03.png" #Sprite of Hermione's upper body.
        #__#$ h_xpos=140 #Defines position of the Hermione's full length sprite. (Default 370).
        #__#show screen hermione_main
        #__#with d3
        $herView.showQQ( "body_03.png", pos )
        her "Точно!"
        m "А?"
        #__#hide screen hermione_main
        #__#with d3
        $herView.hideQQ()
        #__#$ h_body = "03_hp/13_hermione_main/body_04.png" #Sprite of Hermione's upper body.
        #__#$ h_xpos=140 #Defines position of the Hermione's full length sprite. (Default 370).
        #__#show screen hermione_main
        #__#with d3
        $herView.showQQ( "body_04.png", pos )
        her "Я должна трудится еще лучше, чтобы выровнять шансы, неравные из-за этих грязных девок..."
        #__#hide screen hermione_main
        #__#with d3
        $herView.hideQQ()
        #__#$ h_body = "03_hp/13_hermione_main/body_03.png" #Sprite of Hermione's upper body.
        #__#$ h_xpos=140 #Defines position of the Hermione's full length sprite. (Default 370).
        #__#show screen hermione_main
        #__#with d3
        $herView.showQQ( "body_03.png", pos )
        her "Спасибо мне за помощь, профессор."
        menu: 
            "- Начать дрочить -":
                $ d_flag_01 = True #If TRUE genie jerks off under the desk.    
                #__#hide screen hermione_main
                $herView.hideQ() #"WARNING_Z"
                hide screen blktone
                with d3
                ">Вы опускаете руки под стол и обхватываете свой член..."
                hide screen blktone8
                with d3
                hide screen genie
                show screen genie_jerking_off
                with d3
                pause
                #__#hide screen hermione_main
                #__#with d3
                $herView.hideQQ()
                #__#$ h_body = "03_hp/13_hermione_main/body_14.png" #Sprite of Hermione's upper body.
                #__#$ h_xpos=370 #Defines position of the Hermione's full length sprite. (Default 370). (Center: 140)
                $ pos = POS_370
                #__#show screen hermione_main
                #__#with d3
                $herView.showQQ( "body_14.png", pos )
                her "Профессор, что вы делаете?"
                her "Вы же не.....?"
                #__#hide screen hermione_main
                #__#with d3
                $herView.hideQQ()
                #__#$ h_body = "03_hp/13_hermione_main/body_29.png" #Sprite of Hermione's upper body.
                #__#$ h_xpos=370 #Defines position of the Hermione's full length sprite. (Default 370). (Center: 140)
                #__#show screen hermione_main
                #__#with d3
                $herView.showQQ( "body_29.png", pos )
                her "Вы...?"
                m "Ничего. Просто продолжай."
                #__#hide screen hermione_main
                #__#with d3
                $herView.hideQQ()
                #__#$ h_body = "03_hp/13_hermione_main/body_07.png" #Sprite of Hermione's upper body.
                #__#$ h_xpos=370 #Defines position of the Hermione's full length sprite. (Default 370). (Center: 140)
                #__#show screen hermione_main
                #__#with d3
                $herView.showQQ( "body_07.png", pos )
                her "Хм..."
                m "{size=-4}(Он что-то заподозрила? Да не...){/size}"
            "- Внимательно выслушать ее -":
                $ d_flag_01 = False #NOT JERKING OFF.
                m "Не стоит благодарности."
                pass
        #__#hide screen hermione_main
        #__#with d3
        $herView.hideQQ()
        #__#$ h_body = "03_hp/13_hermione_main/body_16.png" #Sprite of Hermione's upper body.
        #__#$ h_xpos=370 #Defines position of the Hermione's full length sprite. (Default 370). (Center: 140)
        #__#$ pos = POS_370
        #__#show screen hermione_main
        #__#with d3
        $herView.showQQ( "body_16.png", pos )
        her "Ну, как я и сказала..."
        her "Я слышала, девочки меняют свои пикантные фотографии в обмен на очки для факультета..."
        if d_flag_01:
            m "{size=-4}(Ну и шлюха... ах... Да...){/size}"
        else:
            m "Десять очков, да?"
        her "Да..."
        if d_flag_01:
            #__#hide screen hermione_main
            #__#with d3
            $herView.hideQQ()
            #__#$ h_body = "03_hp/13_hermione_main/body_29.png" #Sprite of Hermione's upper body.
            #__#$ h_xpos=370 #Defines position of the Hermione's full length sprite. (Default 370). (Center: 140)
            #__#show screen hermione_main
            #__#with d3
            $herView.showQQ( "body_29.png", pos )
            her "И эти две девушки..."
            her "Ходит слух, что они даже спят с профессором Снейпом..."
            m "{size=-4}(Да... Ты маленькая, мерзка, \"слизеринская\" шлюха!){/size}"
            #__#hide screen hermione_main
            #__#with d3
            $herView.hideQQ()
            #__#$ h_body = "03_hp/13_hermione_main/body_45.png" #Sprite of Hermione's upper body.
            #__#$ h_xpos=370 #Defines position of the Hermione's full length sprite. (Default 370). (Center: 140)
            #__#show screen hermione_main
            #__#with d3
            $herView.showQQ( "body_45.png", pos )
            her "То же был случай, я слышала, что ученица дрочила учителю прямо на занятии..."
            m "{size=-4}(Да... Это очень круто, продолжай!){/size}"
            #__#hide screen hermione_main
            #__#with d3
            $herView.hideQQ()
            #__#$ h_body = "03_hp/13_hermione_main/body_29.png" #Sprite of Hermione's upper body.
            #__#$ h_xpos=370 #Defines position of the Hermione's full length sprite. (Default 370). (Center: 140)
            #__#show screen hermione_main
            #__#with d3
            $herView.showQQ( "body_29.png", pos )
            her "И другая девочка, она сосала учителю!"
            m "{size=-4}(Да! Да!){/size}"
            #__#hide screen hermione_main
            #__#with d3
            $herView.hideQQ()
            #__#$ h_body = "03_hp/13_hermione_main/body_46.png" #Sprite of Hermione's upper body.
            #__#$ h_xpos=370 #Defines position of the Hermione's full length sprite. (Default 370). (Center: 140)
            #__#show screen hermione_main
            #__#with d3
            $herView.showQQ( "body_46.png", pos )
            her "А еще одна девочка позволила кончить себе в рот..."
            her "И ведь она все это проглатила и ей понравилось!"
            m "{size=-4}(Стоп... Она правда это делает?){/size}"
            #__#hide screen hermione_main
            #__#with d3
            $herView.hideQQ()
            #__#$ h_body = "03_hp/13_hermione_main/body_64.png" #Sprite of Hermione's upper body.
            #__#$ h_xpos=370 #Defines position of the Hermione's full length sprite. (Default 370). (Center: 140)
            #__#show screen hermione_main
            #__#with d3
            $herView.showQQ( "body_64.png", pos )
            her "Я ведь тоже очень грязная девченка..."
            g4 "Что?!"
            #__#hide screen hermione_main
            #__#with d3
            $herView.hideQQ()
            #__#$ h_body = "03_hp/13_hermione_main/body_65.png" #Sprite of Hermione's upper body.
            #__#$ h_xpos=370 #Defines position of the Hermione's full length sprite. (Default 370). (Center: 140)
            #__#show screen hermione_main
            #__#with d3
            $herView.showQQ( "body_65.png", pos )
            her "Я просто обожаю сосать члены..."
            her "Я хочу чтобы мужчина кончил мне на лицо, как в тех фильмах, которые я смотрю!"
            g4 "{size=-4}(Ах ты маленькая шлюха! Ты реально делаешь это!) *Argh!*{/size}"
            #__#hide screen hermione_main
            #__#with d3
            $herView.hideQQ()
            show screen white 
            pause.1
            hide screen white
            pause.2
            show screen white 
            pause .1
            hide screen white
            with hpunch
            g4 "Аргх! ДА!"
            #__#hide screen hermione_main
            #__#with d3
            $herView.hideQQ()
            hide screen bld1
            with d3
            show screen genie_jerking_sperm
            with d3
            #pause 3
            pause
            
            $ mad = +7
            
            #__#$ h_body = "03_hp/13_hermione_main/body_47.png" #Sprite of Hermione's upper body.
            show screen bld1
            with d3
            #__#show screen hermione_main
            #__#with d3
            $herView.showQQ( "body_47.png", pos )
            her "Я знала! Вы трогаете себя, профессор!"
            show screen genie_jerking_sperm_02
            with d3
            g4 "Что? Нет, я просто... ах, дерьмо, это просто охуенно..."
            show screen genie
            #show screen genie_jerking_off
            with d3
            #__#hide screen hermione_main
            #__#with d3
            $herView.hideQQ()
            #__#$ h_body = "03_hp/13_hermione_main/body_32.png" #Sprite of Hermione's upper body.
            #__#$ h_xpos=370 #Defines position of the Hermione's full length sprite. (Default 370). (Center: 140)
            #__#show screen hermione_main
            #__#with d3
            $herView.showQQ( "body_32.png", pos )
            her "Это отвратительно! Как вы могли!?"
            her "Сэр, вы ведь директор! Вы должны подавать хороший пример!"
            m "Эй, маленькая Мисси, ты так и будешь судить меня или тебе нужны очки?"
            #__#hide screen hermione_main
            #__#with d3
            $herView.hideQQ()
            #__#$ h_body = "03_hp/13_hermione_main/body_34.png" #Sprite of Hermione's upper body.
            #__#$ h_xpos=370 #Defines position of the Hermione's full length sprite. (Default 370). (Center: 140)
            #__#show screen hermione_main
            #__#with d3
            $herView.showQQ( "body_34.png", pos )
            her "Мои очки, пожалуйста. Я думаю, я заслужила их."
            m "Да, даже очень."
            #__#hide screen hermione_main
            #__#with d3
            $herView.hideQQ()
            #__#$ h_body = "03_hp/13_hermione_main/body_47.png" #Sprite of Hermione's upper body.
            #__#$ h_xpos=370 #Defines position of the Hermione's full length sprite. (Default 370). (Center: 140)
            #__#show screen hermione_main
            #__#with d3
            $herView.showQQ( "body_47.png", pos )
            her "Фу... Теперь я чувствую себя такой грязной..."
            hide screen genie_jerking_sperm_02
            with d3
        else:
            her "Мы должны прекратить это, профессор!"
            m "Да, конечно..."
            her "Так вы согласны со мной?"
            her "Я думаю, следует ввести систему штрафов, чтобы наказать девушек которые поступают таким нечестным образом..."
            m "(Все, что я слышу это - \"нужно наказать девочек\"...)"
            her "Так же это поможет мальчикам, так они не будут дискриминироваться!"
            m "Мальчики?"
            m "О, точно...Никому не нужны их услуги... Ублюдки."
            $herView.hideQQ()
            $herView.showQ( "body_03.png", pos, d3 )
            her "Я так рада, что вы понимаете меня, сэр."
            m "Да, да, конечно..."


    stop music fadeout 2.0
    
    $ gryffindor +=5
    
    $herView.hideQQ()
    $herView.showQ( None, pos, d3 )
    m "Пять очков \"Гриффиндору\" мисс Грейнджер. Отличная работа." 
    
    #__#show screen hermione_main
    #$herView.showQ( "body_07.png", pos, d3 )
    hide screen hermione_01_f #Hermione stands still.
    with d3
    her "Это все?"
    if whoring >= 0 and whoring <= 2: #LEVEL 01
        her "*Вздох облегчения*"
    m "Да, можете идти."
    if request_01 == 0:
        #__#hide screen hermione_main                                                                                                                                                                                   #HERMIONE
        #__#with d3                                                                                                                                                                                                                        #HERMIONE
        $herView.hideQQ()
        #__#$ h_body = "03_hp/13_hermione_main/body_01.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
        #__#show screen hermione_main                                                                                                                                                                                 #HERMIONE
        #__#with d3                                                                                                                                                                                                                        #HERMIONE
        $herView.showQQ( "body_01.png", pos )
        her "Еще пять очков... Ребята будут счастливы."
        her "Спасибо, профессор."

    label request_01_done:
    if whoring <= 2:
            $ whoring +=1
 
    $ request_01 += 1
    
    hide screen bld1
    #__#hide screen hermione_main
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
    
    
    ### MUSIC BLOCK ###
    if daytime:
        play music "music/Brittle Rille.mp3" fadein 1 fadeout 1 # DAY MUSIC
    else:
        play music "music/Music for Manatees.mp3" fadein 1 fadeout 1 # NIGHT MUSIC
    ### END OF BLOCK ###
    
    if daytime:
        $ hermione_takes_classes = True
        jump day_main_menu
    else:
        $ hermione_sleeping = True
        jump night_main_menu
        