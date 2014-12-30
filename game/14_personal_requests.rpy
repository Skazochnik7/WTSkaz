label new_personal_request:
    if slytherin > gryffindor or slytherin == gryffindor:
        show screen hermione_main
        $ menu_x = 0.2 #Default: 0.5
        
        label not_now:
        menu:
            "-Личные услуги-":
                label not_now2:

                # define first choice format
                $hearts_count = 0
                if not new_request_01_01 and not new_request_01_02 and not new_request_01_03:
                    $hearts_count = 0
                elif new_request_01_01 and not new_request_01_02 and not new_request_01_03:
                    $hearts_count = 1
                elif new_request_01_02 and not new_request_01_03:
                    $hearts_count = 2
                else:
                    $hearts_count = 3
                
                ##example of list
                #python:
                #    heartsVar = [2,3,1]
                ## and usage of list
                ## "Услуга: \"Поговори со мной\" {image=heart_0[heartsVar[2]].png}":

                ##example of map
                #$heartsDict = {'first_act' : 2, 'second_act' : 1 }
                #$heartsDict['first_act'] = 3
                #$valReal = heartsDict['first_act']
                ## and usage of list
                ##"Услуга: \"Поговори со мной\" {image=heart_0[valReal].png}":
                
                ### LEVEL 01 ###
                menu:
                    
                    "Услуга: \"Поговори со мной\" {image=heart_0[hearts_count].png}":
                        jump new_request_01
 
#                    "Услуга: \"Поговори со мной\" {image=heart_00.png}" if not new_request_01_01 and not new_request_01_02 and not new_request_01_03:
#                        jump new_request_01
#                    "Услуга: \"Поговори со мной\" {image=heart_01.png}" if new_request_01_01 and not new_request_01_02 and not new_request_01_03:
#                        jump new_request_01
#                    "Услуга: \"Поговори со мной\" {image=heart_02.png}" if new_request_01_02 and not new_request_01_03:
#                        jump new_request_01
#                    "Услуга: \"Поговори со мной\" {image=heart_03.png}" if new_request_01_03:
#                        jump new_request_01
                        

                    "Услуга: \"Отличные трусики!\" {image=heart_00.png}" if not new_request_02_01 and not new_request_02_02 and not new_request_02_03: # LEVEL 1
                        jump new_request_02
                    "Услуга: \"Отличные трусики!\" {image=heart_01.png}" if new_request_02_01 and not new_request_02_02 and not new_request_02_03: # LEVEL 1
                        jump new_request_02
                    "Услуга: \"Отличные трусики!\" {image=heart_02.png}" if new_request_02_02 and not new_request_02_03: # LEVEL 1
                        jump new_request_02
                    "Услуга: \"Отличные трусики!\" {image=heart_03.png}" if new_request_02_03: # LEVEL 1
                        jump new_request_02
                  
                    ### LEVEL 02 ###
                    "{color=#858585}--Не открытое действие-{/color}-" if imagination == 1:
                        call vague_idea
                        jump not_now2
                    "Услуга: \"Вор трусиков\" {image=heart_00.png}" if not new_request_03_01 and not new_request_03_02 and not new_request_03_03 and daytime and imagination >= 2:
                        jump new_request_03
                    "Услуга: \"Вор трусиков\" {image=heart_01.png}" if new_request_03_01 and not new_request_03_02 and not new_request_03_03 and daytime and imagination >= 2:
                        jump new_request_03
                    "Услуга: \"Вор трусиков\" {image=heart_02.png}" if new_request_03_02 and not new_request_03_03 and daytime and imagination >= 2:
                        jump new_request_03
                    "Услуга: \"Вор трусиков\" {image=heart_03.png}" if new_request_03_03 and daytime and imagination >= 2:
                        jump new_request_03
                    
                    "{color=#858585}--Не открытое действие-{/color}-" if imagination == 1:
                        call vague_idea
                        jump not_now2
                    "Услуга: \"Полапать грудь!\" {image=heart_00.png}" if not new_request_04_01 and not new_request_04_02 and not new_request_04_03 and imagination >= 2: 
                        jump new_request_04
                    "Услуга: \"Полапать грудь!\" {image=heart_01.png}" if new_request_04_01 and not new_request_04_02 and not new_request_04_03 and imagination >= 2: 
                        jump new_request_04
                    "Услуга: \"Полапать грудь!\" {image=heart_02.png}" if new_request_04_02 and not new_request_04_03 and imagination >= 2: 
                        jump new_request_04
                    "Услуга: \"Полапать грудь!\" {image=heart_03.png}" if new_request_04_03 and imagination >= 2: 
                        jump new_request_04
                        
                    "{color=#858585}--Не открытое действие-{/color}-" if imagination == 1:
                        call vague_idea
                        jump not_now2
                    "Услуга: \"Полапать попку!\" {image=heart_00.png}" if not new_request_05_01 and not new_request_05_02 and not new_request_05_03 and imagination >= 2:
                        jump new_request_05
                    "Услуга: \"Полапать попку!\" {image=heart_01.png}" if new_request_05_01 and not new_request_05_02 and not new_request_05_03 and imagination >= 2: 
                        jump new_request_05
                    "Услуга: \"Полапать попку!\" {image=heart_02.png}" if new_request_05_02 and not new_request_05_03 and imagination >= 2: 
                        jump new_request_05
                    "Услуга: \"Полапать попку!\" {image=heart_03.png}" if new_request_05_03 and imagination >= 2: 
                        jump new_request_05
                        
                    ### LEVEL 03 ### IMAGINATION == 3
                    "{color=#858585}--Не открытое действие-{/color}-" if imagination < 3:
                        call vague_idea
                        jump not_now2
                    "Услуга: \"Покажи их мне!\" {image=heart_00.png}" if not new_request_08_01 and not new_request_08_02 and not new_request_08_03 and imagination >= 3:
                        jump new_request_08
                    "Услуга: \"Покажи их мне!\" {image=heart_01.png}" if new_request_08_01 and not new_request_08_02 and not new_request_08_03 and imagination >= 3: 
                        jump new_request_08
                    "Услуга: \"Покажи их мне!\" {image=heart_02.png}" if new_request_08_02 and not new_request_08_03 and imagination >= 3: 
                        jump new_request_08
                    "Услуга: \"Покажи их мне!\" {image=heart_03.png}" if new_request_08_03 and imagination >= 3: 
                        jump new_request_08 
                    
#                    "Услуга: \"Show {size=+5}it{/size} to me! (NOT FINISHED YET)":
#                        jump new_request_09
                    
                    ### LEVEL 04 ### IMAGINATION == 3
                    "{color=#858585}--Не открытое действие-{/color}-" if imagination < 3:
                        call vague_idea
                        jump not_now2
                    "Услуга: \"Станцуй для меня!\" {image=heart_00.png}" if not new_request_11_01 and not new_request_11_02 and not new_request_11_03 and imagination >= 3:
                        jump new_request_11
                    "Услуга: \"Станцуй для меня!\" {image=heart_01.png}" if new_request_11_01 and not new_request_11_02 and not new_request_11_03 and imagination >= 3: 
                        jump new_request_11
                    "Услуга: \"Станцуй для меня!\" {image=heart_02.png}" if new_request_11_02 and not new_request_11_03 and imagination >= 3:
                        jump new_request_11
                    "Услуга: \"Станцуй для меня!\" {image=heart_03.png}" if new_request_11_03 and imagination >= 3: 
                        jump new_request_11
                    
                    "{color=#858585}--Не открытое действие-{/color}-" if imagination < 3:
                        call vague_idea
                        jump not_now2
                    "Услуга: \"Дай мне потрогать их!\" {image=heart_00.png}" if not new_request_12_01 and not new_request_12_02 and not new_request_12_03 and daytime and imagination >= 3: # LEVEL 4
                        jump new_request_12
                    "Услуга: \"Дай мне потрогать их!\" {image=heart_01.png}" if new_request_12_01 and not new_request_12_02 and not new_request_12_03 and daytime and imagination >= 3: # LEVEL 4
                        jump new_request_12
                    "Услуга: \"Дай мне потрогать их!\" {image=heart_02.png}" if new_request_12_02 and not new_request_12_03 and daytime and imagination >= 3: # LEVEL 4
                        jump new_request_12
                    "Услуга: \"Дай мне потрогать их!\" {image=heart_03.png}" if new_request_12_03 and daytime and imagination >= 3: # LEVEL 4
                        jump new_request_12
                    
                    ### LEVEL 05 ### IMAGINATION == 4
                    "{color=#858585}--Не открытое действие-{/color}-" if imagination < 4:
                        call vague_idea
                        jump not_now2
                    "Услуга: \"Потрогай меня!\" {image=heart_00.png}" if not new_request_16_01 and not new_request_16_02 and not new_request_16_03 and imagination >= 4: # LEVEL 5
                        jump new_request_16
                    "Услуга: \"Потрогай меня!\" {image=heart_01.png}" if new_request_16_01 and not new_request_16_02 and not new_request_16_03 and imagination >= 4: # LEVEL 5
                        jump new_request_16
                    "Услуга: \"Потрогай меня!\" {image=heart_02.png}" if new_request_16_02 and not new_request_16_03 and imagination >= 4: # LEVEL 5
                        jump new_request_16
                    "Услуга: \"Потрогай меня!\" {image=heart_03.png}" if new_request_16_03 and imagination >= 4:  # LEVEL 5
                        jump new_request_16
                       
                    ### LEVEL 06 ### IMAGINATION == 4
                    "{color=#858585}--Не открытое действие-{/color}-" if imagination < 4:
                        call vague_idea
                        jump not_now2
                    "Услуга: \"Соси его!\" {image=heart_00.png}" if not new_request_22_01 and not new_request_22_02 and not new_request_22_03 and imagination >= 4: # LEVEL 6
                        jump new_request_22
                    "Услуга: \"Соси его!\" {image=heart_01.png}" if new_request_22_01 and not new_request_22_02 and not new_request_22_03 and imagination >= 4: # LEVEL 6
                        jump new_request_22
                    "Услуга: \"Соси его!\" {image=heart_02.png}" if new_request_22_02 and not new_request_22_03 and imagination >= 4: # LEVEL 6
                        jump new_request_22
                    "Услуга: \"Соси его!\" {image=heart_03.png}" if new_request_22_03 and imagination >= 4: # LEVEL 6
                        jump new_request_22
                    
                    ### LEVEL 07 ### IMAGINATION == 5
                    "{color=#858585}--Не открытое действие-{/color}-" if imagination < 5:
                        call vague_idea
                        jump not_now2
                    "Услуга: \"Давай займемся сексом!\" {image=heart_00.png}" if not new_request_29_01 and not new_request_29_02 and not new_request_29_03 and imagination >= 5: # LEVEL 7
                        jump new_request_29
                    "Услуга: \"Давай займемся сексом!\" {image=heart_01.png}" if new_request_29_01 and not new_request_29_02 and not new_request_29_03 and imagination >= 5: # LEVEL 7
                        jump new_request_29
                    "Услуга: \"Давай займемся сексом!\" {image=heart_02.png}" if new_request_29_02 and not new_request_29_03 and imagination >= 5: # LEVEL 7
                        jump new_request_29
                    "Услуга: \"Давай займемся сексом!\" {image=heart_03.png}" if new_request_29_03 and imagination >= 5: # LEVEL 7
                        jump new_request_29
                        
                    ### LEVEL 08 ###
                    "{color=#858585}--Не открытое действие-{/color}-" if imagination < 5:
                        call vague_idea
                        jump not_now2
                    "Услуга:  \"Время для анала!\" {image=heart_00.png}" if not new_request_31_01 and not new_request_31_02 and not new_request_31_03 and imagination >= 5: # LEVEL 8
                        jump new_request_31
                    "Услуга:  \"Время для анала!\" {image=heart_01.png}" if new_request_31_01 and not new_request_31_02 and not new_request_31_03 and imagination >= 5: # LEVEL 8
                        jump new_request_31
                    "Услуга:  \"Время для анала!\" {image=heart_02.png}" if new_request_31_02 and not new_request_31_03 and imagination >= 5: # LEVEL 8
                        jump new_request_31
                    "Услуга:  \"Время для анала!\" {image=heart_03.png}" if new_request_31_03 and imagination >= 5: # LEVEL 8
                        jump new_request_31
                            
                    "-Отмена-":
                        jump new_personal_request
                
            "{color=#858585}-Публичные услуги-{/color}" if not daytime:
                show screen blktone
                hide screen hermione_main
                with d3
                ">Публичные услуги недоступны в это время суток."
                hide screen blktone
                show screen hermione_main
                with d3
                jump not_now
            "-Публичные услуги-" if daytime:
                if lock_public_favors:
                    her "Эм... Сэр..."
                    her "Я согласна обменивать очки за всякие услуги..."
                    her "Но только до тех пор, пока все это между нами, а не на публику..."
                    jump new_personal_request
                else:
                    label not_now3:
                    menu:
                        ### LEVEL 01 ### 
                        "Услуга: \"Флиртуй с учеником\"" if daytime:
                            jump new_request_02_b
                            
                        ### LEVEL 02 ### IMAGINATION == 2
                        "{color=#858585}--Не открытое действие-{/color}-" if imagination < 2:
                            call vague_idea
                            jump not_now3
                        "Услуга: \"Флиртуй с учителем\"" if daytime  and imagination >= 2:
                            jump new_request_02_c
                        
                        ### LEVEL 03 ### IMAGINATION == 3
                        "{color=#858585}--Не открытое действие-{/color}-" if imagination < 3:
                            call vague_idea
                            jump not_now3
                        "Услуга: \"Дай однокласснику поприставать к тебе.\"" if imagination >= 3: # LEVEL 3
                            jump new_request_10
                        
                        ### LEVEL 04 ### IMAGINATION == 3
                        "{color=#858585}--Не открытое действие-{/color}-" if imagination < 3:
                            call vague_idea
                            jump not_now3
                        "Услуга: \"Посвети сиськами перед одноклассниками.\"" if imagination >= 3: # LEVEL 4
                            jump new_request_15
                        
                        
                        ### LEVEL 05 ### IMAGINATION == 4
                        "{color=#858585}--Не открытое действие-{/color}-" if imagination < 4:
                            call vague_idea
                            jump not_now3
                        "Услуга: \"Поцелуй девченку.\"" if imagination >= 4: # LEVEL 5
                            jump new_request_20
                            
                        ### LEVEL 06 ### IMAGINATION == 4
                        "{color=#858585}--Не открытое действие-{/color}-" if imagination < 4:
                            call vague_idea
                            jump not_now3
                        "Услуга: \"Вздрочни однокласснику.\"" if imagination >= 4: # LEVEL 6
                            jump new_request_23
                            
                        ### LEVEL 07 ### IMAGINATION == 5
                        "{color=#858585}--Не открытое действие-{/color}-" if imagination < 5:
                            call vague_idea
                            jump not_now3
                        "Услуга: \"Отсоси однокласснику\"" if imagination >= 5:# LEVEL 7
                            jump new_request_24
                                
                         ### LEVEL 08 ### IMAGINATION == 5
                        "{color=#858585}--Не открытое действие-{/color}-" if imagination < 5:
                            call vague_idea
                            jump not_now3
                        "Услуга: \"Трахнись с одноклассником\"" if imagination >= 5:# LEVEL 8
                            jump new_request_30
                        
                        "-Отмена-":
                            jump new_personal_request
                
                
            "-Ничего-":
                jump day_time_requests
    
        
        
        
        
                   
                    
                    
                        
                 
                     
                    
                   
                        
#                    "...flash your Трусики to a teacher.{image=3_stars_00.png}" if request_07_points == 0:
#                        jump new_request_07
#                    "...flash your Трусики to a teacher.{image=3_stars_01.png}" if request_07_points == 1:
#                        jump new_request_07
#                    "...flash your Трусики to a teacher.{image=3_stars_02.png}" if request_07_points == 2:
#                        jump new_request_07
#                    "...flash your Трусики to a teacher.{image=3_stars.png}" if request_07_points >= 3:
#                        jump new_request_07
                        
                    

#                    "\"Let me stick a finger up your butt.\"{image=3_stars_00.png}" if request_17_points == 0:
#                        jump new_request_17
#                    "\"Let me stick a finger up your butt.\"{image=3_stars_01.png}" if request_17_points == 1:
#                        jump new_request_17
#                    "\"Let me stick a finger up your butt.\"{image=3_stars_02.png}" if request_17_points == 2:
#                        jump new_request_17
#                    "\"Let me stick a finger up your butt.\"{image=3_stars.png}" if request_17_points >= 3:
#                        jump new_request_17
                        
#                    "\"Touch my cock a little.\"{image=3_stars_00.png}" if request_18_points == 0:
#                        jump new_request_18
#                    "\"Touch my cock a little.\"{image=3_stars_01.png}" if request_18_points == 1:
#                        jump new_request_18
#                    "\"Touch my cock a little.\"{image=3_stars_02.png}" if request_18_points == 2:
#                        jump new_request_18
#                    "\"Touch my cock a little.\"{image=3_stars.png}" if request_18_points >= 3:
#                        jump new_request_18
                    
#                    "\"Rub my cock against your cheeks.\"{image=3_stars_00.png}" if request_19_points == 0:
#                        jump new_request_19
#                    "\"Rub my cock against your cheeks.\"{image=3_stars_01.png}" if request_19_points == 1:
#                        jump new_request_19
#                    "\"Rub my cock against your cheeks.\"{image=3_stars_02.png}" if request_19_points == 2:
#                        jump new_request_19
#                    "\"Rub my cock against your cheeks.\"{image=3_stars.png}" if request_19_points >= 3:
#                        jump new_request_19
                        
                    
                   
#                    "\"Let me cum on your tits\"{image=3_stars_00.png}" if request_21_points == 0: # LEVEL 6
#                        jump new_request_21
#                    "\"Let me cum on your tits\"{image=3_stars_01.png}" if request_21_points == 1:
#                        jump new_request_21
#                    "\"Let me cum on your tits\"{image=3_stars_02.png}" if request_21_points == 2:
#                        jump new_request_21
#                    "\"Let me cum on your tits\"{image=3_stars.png}" if request_21_points >= 3:
#                        jump new_request_21
                            
                    


            
            

    else:
        her "Гриффиндор лидирует. Мне это не нужно сейчас."
        jump day_time_requests
                
################
### LEVEL 01 ###                
###################REQUEST_01 JUST STAND THERE.
label new_request_01: #LV.1 (Whoring = 0 - 2)
    hide screen hermione_main
    with d3
    m "{size=-4}(Я просто поговорю с ней...){/size}"
    menu:
        "\"(Да, сделаем это.)\"":
            pass
        "\"(Не сейчас.)\"":
            jump new_personal_request
    play music "music/Chipper Doodle v2.mp3" fadein 1 fadeout 1 
    m "Ладно..."
    m "Просто расскажи что нового у тебя."
    hide screen hermione_main
    with d3
    $ h_body = "03_hp/13_hermione_main/body_08.png" #Sprite of Hermione's upper body.
    $ h_xpos=140 #Defines position of the Hermione's full length sprite. (Default 370).
    show screen hermione_main
    with d3
    if request_01 == 0: #First time this event taking place.
        her "Эм... Ладно..."
        her "Мне просто стоять здесь и говорить...? Как сейчас?"
    else:
        her "В центре, верно? Я помню..."
    hide screen hermione_main
    with d3
    $ menu_x = 0.5 #Menu is moved to the left side.
    $ h_xpos=120 #Defines position of the Hermione's full length sprite.
    $ h_ypos=0
    $ h_body = "03_hp/13_hermione_main/body_01.png" #Sprite of Hermione's upper body.
    show screen blktone 
    with d3
    show screen ctc
    show screen hermione_main
    with Dissolve(.3)
    pause
    
    m "Ну?"
    if request_01 == 0 and whoring <=5: #First time this event taking place.
        $  new_request_01_01 = True #Hearts on menu buttons.
        hide screen hermione_main
        with d3
        $ h_body = "03_hp/13_hermione_main/body_11.png" #Sprite of Hermione's upper body.
        $ h_xpos=140 #Defines position of the Hermione's full length sprite. (Default 370).
        show screen hermione_main
        with d3
        her "Эм... Ну чтож..."
        ">Гермиона чувствует смущение..."
        hide screen hermione_main
        with d3
        $ h_body = "03_hp/13_hermione_main/body_12.png" #Sprite of Hermione's upper body.
        $ h_xpos=140 #Defines position of the Hermione's full length sprite. (Default 370).
        show screen hermione_main
        with d3
        her "..................."
    if whoring >= 0 and  whoring <= 5: #LEVEL 01 and LEVEL 02
        if whoring >= 3 and whoring <= 5:
            $ level = "02"
            $  new_request_01_02 =True #Hearts on menu buttons.
        hide screen hermione_main
        with d3
        $ h_body = "03_hp/13_hermione_main/body_12.png" #Sprite of Hermione's upper body.
        $ h_xpos=140 #Defines position of the Hermione's full length sprite. (Default 370).
        show screen hermione_main
        with d3
        her "Последнее время все относительно спокойно, ничего такого..."
        her "Кроме того дня, когда я завалила тест..."
        her "Все еще не могу поверить в это..."
        menu: 
            "-Дрочить пока она говорит-":
                $ d_flag_01 = True #If TRUE genie jerks off under the desk.    
                hide screen hermione_main
                hide screen blktone
                with d3
                ">Вы опускаете руки под стол и обхватываете свой член..."
                hide screen blktone8
                with d3
                hide screen genie
                show screen genie_jerking_off
                with d3
                pause
                hide screen hermione_main
                with d3
                $ h_body = "03_hp/13_hermione_main/body_14.png" #Sprite of Hermione's upper body.
                $ h_xpos=370 #Defines position of the Hermione's full length sprite. (Default 370). (Center: 140)
                show screen hermione_main
                with d3
                her "Профессор, что вы делаете?"
                m "Что, ничего. Просто чешу свою ногу."
                m "Так о чем ты говорила?"
                hide screen hermione_main
                with d3
                $ h_body = "03_hp/13_hermione_main/body_14.png" #Sprite of Hermione's upper body.
                $ h_xpos=370 #Defines position of the Hermione's full length sprite. (Default 370). (Center: 140)
                show screen hermione_main
                with d3
                her "Да... Ну, тот тест я провалила..."
            "-Слушать ее-":
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
        
        hide screen hermione_main                                                                                                                                                                                   #HERMIONE
        with d3                                                                                                                                                                                                                        #HERMIONE
        $ h_body = "03_hp/13_hermione_main/body_07.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
        show screen hermione_main                                                                                                                                                                                 #HERMIONE
        with d3                                                                                                                                                                                                                        #HERMION
        her "Вы что-то сказали?"
        m "Ничего, продолжай..."
        hide screen hermione_main                                                                                                                                                                                   #HERMIONE
        with d3                                                                                                                                                                                                                        #HERMIONE
        $ h_body = "03_hp/13_hermione_main/body_14.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
        show screen hermione_main                                                                                                                                                                                 #HERMIONE
        with d3                                                                                                                                                                                                                        #HERMIONE
        her "Ну, некоторые студенты смеются над профессором Квирреллом..."
        her "Конечно же я не одобряю такое поведение."
        if d_flag_01:
            m "{size=-4}(Давай же! Скажи что-нибудь грязное!){/size}"
        else:
            m ".................."
        her "О, мое \"Общество по защите мужских прав\" набирает популярность..."
        her "И я очень рада..."
        hide screen hermione_main                                                                                                                                                                                   #HERMIONE
        with d3                                                                                                                                                                                                                        #HERMIONE
        $ h_body = "03_hp/13_hermione_main/body_16.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
        show screen hermione_main                                                                                                                                                                                 #HERMIONE
        with d3                                                                                                                                                                                                                        #HERMIONE
        her "Я думаю, с учетом всего времени, мы действительно сможем что-нибудь изменить..."
        hide screen hermione_main                                                                                                                                                                                   #HERMIONE
        with d3                                                                                                                                                                                                                        #HERMIONE
        $ h_body = "03_hp/13_hermione_main/body_06.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
        show screen hermione_main                                                                                                                                                                                 #HERMIONE
        with d3                                                                                                                                                                                                                        #HERMIONE
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
            
        hide screen hermione_main                                                                                                                                                                                   #HERMIONE
        with d3                                                                                                                                                                                                                        #HERMIONE
        $ h_body = "03_hp/13_hermione_main/body_05.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
        show screen hermione_main                                                                                                                                                                                 #HERMIONE
        with d3                                                                                                                                                                                                                        #HERMIONE
        her "Профессор?"
        m "Да, да, я внимательно слушаю..."
        m "Это все очень самооправданно, э-э..."
        m "То есть, очень помогает нам и поддерживает..."
        hide screen hermione_main                                                                                                                                                                                   #HERMIONE
        with d3                                                                                                                                                                                                                        #HERMIONE
        $ h_body = "03_hp/13_hermione_main/body_07.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
        show screen hermione_main                                                                                                                                                                                 #HERMIONE
        with d3                                                                                                                                                                                                                        #HERMIONE
        her ".........................."
  
    elif whoring >= 6: #LEVEL 03
        $  new_request_01_03 = True #Hearts on menu buttons.
        hide screen hermione_main
        with d3
        $ h_body = "03_hp/13_hermione_main/body_12.png" #Sprite of Hermione's upper body.
        $ h_xpos=140 #Defines position of the Hermione's full length sprite. (Default 370).
        show screen hermione_main
        with d3
        her "У меня в последнее время все вроде-как в порядке..."
        her "Хм..."
        her "Сейчас факультеты \"Слизерина\" и \"Гриффиндора\" очень сильно соперничают."
        her "Если честно, то этого не должно быть..."
        her "\"Гриффиндор\" был бы в лидерах, если бы не \"Слизеринские\" шлюхи..."
        her "Я только и слышу, что они получают свои очки за \"услуги\"..."
        hide screen hermione_main
        with d3
        $ h_body = "03_hp/13_hermione_main/body_04.png" #Sprite of Hermione's upper body.
        $ h_xpos=140 #Defines position of the Hermione's full length sprite. (Default 370).
        show screen hermione_main
        with d3
        her "Очень подло!"
        m "И что же вы теперь будете делать, мисс Грейнджер?"
        hide screen hermione_main
        with d3
        $ h_body = "03_hp/13_hermione_main/body_03.png" #Sprite of Hermione's upper body.
        $ h_xpos=140 #Defines position of the Hermione's full length sprite. (Default 370).
        show screen hermione_main
        with d3
        her "Точно!"
        m "А?"
        hide screen hermione_main
        with d3
        $ h_body = "03_hp/13_hermione_main/body_04.png" #Sprite of Hermione's upper body.
        $ h_xpos=140 #Defines position of the Hermione's full length sprite. (Default 370).
        show screen hermione_main
        with d3
        her "Я должна трудится еще лучше, чтобы выровнять шансы, неравные из-за этих грязных девок..."
        hide screen hermione_main
        with d3
        $ h_body = "03_hp/13_hermione_main/body_03.png" #Sprite of Hermione's upper body.
        $ h_xpos=140 #Defines position of the Hermione's full length sprite. (Default 370).
        show screen hermione_main
        with d3
        her "Спасибо мне за помощь, профессор."
        menu: 
            "-Начать дрочить-":
                $ d_flag_01 = True #If TRUE genie jerks off under the desk.    
                hide screen hermione_main
                hide screen blktone
                with d3
                ">Вы опускаете руки под стол и обхватываете свой член..."
                hide screen blktone8
                with d3
                hide screen genie
                show screen genie_jerking_off
                with d3
                pause
                hide screen hermione_main
                with d3
                $ h_body = "03_hp/13_hermione_main/body_14.png" #Sprite of Hermione's upper body.
                $ h_xpos=370 #Defines position of the Hermione's full length sprite. (Default 370). (Center: 140)
                show screen hermione_main
                with d3
                her "Профессор, что вы делаете?"
                her "Вы же не.....?"
                hide screen hermione_main
                with d3
                $ h_body = "03_hp/13_hermione_main/body_29.png" #Sprite of Hermione's upper body.
                $ h_xpos=370 #Defines position of the Hermione's full length sprite. (Default 370). (Center: 140)
                show screen hermione_main
                with d3
                her "Вы...?"
                m "Ничего. Просто продолжай."
                hide screen hermione_main
                with d3
                $ h_body = "03_hp/13_hermione_main/body_07.png" #Sprite of Hermione's upper body.
                $ h_xpos=370 #Defines position of the Hermione's full length sprite. (Default 370). (Center: 140)
                show screen hermione_main
                with d3
                her "Хм..."
                m "{size=-4}(Он что-то заподозрила? Да не...){/size}"
            "-Внимательно выслушать ее-":
                $ d_flag_01 = False #NOT JERKING OFF.
                m "Не стоит благодарности."
                pass
        hide screen hermione_main
        with d3
        $ h_body = "03_hp/13_hermione_main/body_16.png" #Sprite of Hermione's upper body.
        $ h_xpos=370 #Defines position of the Hermione's full length sprite. (Default 370). (Center: 140)
        show screen hermione_main
        with d3
        her "Ну, как я и сказала..."
        her "Я слышала, девочки меняют свои пикантные фотографии в обмен на очки для факультета..."
        if d_flag_01:
            m "{size=-4}(Ну и шлюха... ах... Да...){/size}"
        else:
            m "Десять очков, да?"
        her "Да..."
        if d_flag_01:
            hide screen hermione_main
            with d3
            $ h_body = "03_hp/13_hermione_main/body_29.png" #Sprite of Hermione's upper body.
            $ h_xpos=370 #Defines position of the Hermione's full length sprite. (Default 370). (Center: 140)
            show screen hermione_main
            with d3
            her "И эти две девушки..."
            her "Ходит слух, что они даже спят с профессором Снейпом..."
            m "{size=-4}(Да... Ты маленькая, мерзка, \"слизеринская\" шлюха!){/size}"
            hide screen hermione_main
            with d3
            $ h_body = "03_hp/13_hermione_main/body_45.png" #Sprite of Hermione's upper body.
            $ h_xpos=370 #Defines position of the Hermione's full length sprite. (Default 370). (Center: 140)
            show screen hermione_main
            with d3
            her "То же был случай, я слышала, что ученица дрочила учителю прямо на занятии..."
            m "{size=-4}(Да... Это очень круто, продолжай!){/size}"
            hide screen hermione_main
            with d3
            $ h_body = "03_hp/13_hermione_main/body_29.png" #Sprite of Hermione's upper body.
            $ h_xpos=370 #Defines position of the Hermione's full length sprite. (Default 370). (Center: 140)
            show screen hermione_main
            with d3
            her "И другая девочка, она сосала учителю!"
            m "{size=-4}(Да! Да!){/size}"
            hide screen hermione_main
            with d3
            $ h_body = "03_hp/13_hermione_main/body_46.png" #Sprite of Hermione's upper body.
            $ h_xpos=370 #Defines position of the Hermione's full length sprite. (Default 370). (Center: 140)
            show screen hermione_main
            with d3
            her "А еще одна девочка позволила кончить себе в рот..."
            her "И ведь она все это проглатила и ей понравилось!"
            m "{size=-4}(Стоп... Она правда это делает?){/size}"
            hide screen hermione_main
            with d3
            $ h_body = "03_hp/13_hermione_main/body_64.png" #Sprite of Hermione's upper body.
            $ h_xpos=370 #Defines position of the Hermione's full length sprite. (Default 370). (Center: 140)
            show screen hermione_main
            with d3
            her "Я ведь тоже очень грязная девченка..."
            g4 "Что?!"
            hide screen hermione_main
            with d3
            $ h_body = "03_hp/13_hermione_main/body_65.png" #Sprite of Hermione's upper body.
            $ h_xpos=370 #Defines position of the Hermione's full length sprite. (Default 370). (Center: 140)
            show screen hermione_main
            with d3
            her "Я просто обожаю сосать члены..."
            her "Я хочу чтобы мужчина кончил мне на лицо, как в тех фильмах, которые я смотрю!"
            g4 "{size=-4}(Ах ты маленькая шлюха! Ты реально делаешь это!) *Argh!*{/size}"
            hide screen hermione_main
            with d3
            show screen white 
            pause.1
            hide screen white
            pause.2
            show screen white 
            pause .1
            hide screen white
            with hpunch
            g4 "Аргх! ДА!"
            hide screen hermione_main
            with d3
            hide screen bld1
            with d3
            show screen genie_jerking_sperm
            with d3
            #pause 3
            pause
            
            $ mad = +7
            
            $ h_body = "03_hp/13_hermione_main/body_47.png" #Sprite of Hermione's upper body.
            show screen bld1
            with d3
            show screen hermione_main
            with d3
            her "Я знала! Вы трогаете себя, профессор!"
            show screen genie_jerking_sperm_02
            with d3
            g4 "Что? Нет, я просто... ах, дерьмо, это просто охуенно..."
            show screen genie
            #show screen genie_jerking_off
            with d3
            hide screen hermione_main
            with d3
            $ h_body = "03_hp/13_hermione_main/body_32.png" #Sprite of Hermione's upper body.
            $ h_xpos=370 #Defines position of the Hermione's full length sprite. (Default 370). (Center: 140)
            show screen hermione_main
            with d3
            her "Это отвратительно! Как вы могли!?"
            her "Сэр, вы ведь директор! Вы должны подавать хороший пример!"
            m "Эй, маленькая Мисси, ты так и будешь судить меня или тебе нужны очки?"
            hide screen hermione_main
            with d3
            $ h_body = "03_hp/13_hermione_main/body_34.png" #Sprite of Hermione's upper body.
            $ h_xpos=370 #Defines position of the Hermione's full length sprite. (Default 370). (Center: 140)
            show screen hermione_main
            with d3
            her "Мои очки, пожалуйста. Я думаю, я заслужила их."
            m "Да, даже очень."
            hide screen hermione_main
            with d3
            $ h_body = "03_hp/13_hermione_main/body_47.png" #Sprite of Hermione's upper body.
            $ h_xpos=370 #Defines position of the Hermione's full length sprite. (Default 370). (Center: 140)
            show screen hermione_main
            with d3
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
            her "Я так рада, что вы понимаете меня, сэр."
            m "Да, да, конечно..."
        
        
                
                
        

    stop music fadeout 2.0
    
    $ gryffindor +=5
    m "Пять очков \"Гриффиндору\" мисс Грейнджер. Отличная работа." 
    show screen hermione_main
    hide screen hermione_01_f #Hermione stands still.
    with d3
    her "Это все?"
    if whoring >= 0 and whoring <= 2: #LEVEL 01
        her "*Вздох облегчения*"
    m "Да, можете идти."
    if request_01 == 0:
        hide screen hermione_main                                                                                                                                                                                   #HERMIONE
        with d3                                                                                                                                                                                                                        #HERMIONE
        $ h_body = "03_hp/13_hermione_main/body_01.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
        show screen hermione_main                                                                                                                                                                                 #HERMIONE
        with d3                                                                                                                                                                                                                        #HERMIONE
        her "Еще пять очков... Ребята будут счастливы."
        her "Спасибо, профессор."

    label request_01_done:
    if whoring <= 2:
            $ whoring +=1
 
    $ request_01 += 1
    
 
    
    
    hide screen bld1
    hide screen hermione_main
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
        
        
###################REQUEST_02 (Level 01)
label new_request_02: #SHOW ME YOUR Трусики
    hide screen hermione_main
    with d3
    m "{size=-4}(Я хочу попросить ее показать мне трусики. Просто и понятно.){/size}"
    $ menu_x = 0.5 #Default menu position restored.
    menu:
        "\"(Да, давай попробуем!)\"":
            pass
        "\"(Не сейчас.)\"":
            jump new_personal_request
    show screen hermione_main
    her "Так, что же мне нужно сделать?"
    m "Ничего такого, на самом деле..."
    m "Я просто хочу, чтобы ты показа мне свои трусики."             
    if request_02 == 0 and whoring <= 5: #First time this event taking place. and LEVEL 02.  
        $ new_request_02_01 =  True #Hearts.
        hide screen hermione_main
        with d3
        $ h_body = "03_hp/13_hermione_main/body_14.png" #Sprite of Hermione's upper body.
        show screen hermione_main
        with d3
        her "Мои... трусики...?"
        hide screen hermione_main
        with d3
        $ h_body = "03_hp/13_hermione_main/body_47.png" #Sprite of Hermione's upper body.
        show screen hermione_main
        with d3
        her  "Профессор Дамблдор!"
        m "Я знаю, знаю, это немного странно..."
        hide screen hermione_main
        with d3
        $ h_body = "03_hp/13_hermione_main/body_48.png" #Sprite of Hermione's upper body.
        show screen hermione_main
        with d3
        her  " {size=+7}Немного !?{/size}"
        her "Это абсолютно неуместно!"
        m "Слушай, нам ведь предстоит это пройти, чтобы пойти дальше, верно?"
        hide screen hermione_main
        with d3
        $ h_body = "03_hp/13_hermione_main/body_31.png" #Sprite of Hermione's upper body.
        show screen hermione_main
        with d3
        her  "\"Пойти дальше\"? Профессор, я не понимаю..."
        m "Что вы не понимаете, мисс Грейнджер?"
        m "Вам нужны эти очки или нет?"
        hide screen hermione_main
        with d3
        $ h_body = "03_hp/13_hermione_main/body_31.png" #Sprite of Hermione's upper body.
        show screen hermione_main
        with d3
        her  "Нужны..."
        m "Значит приподнимайте свою юбку..."
        hide screen hermione_main
        with d3
        $ h_body = "03_hp/13_hermione_main/body_47.png" #Sprite of Hermione's upper body.
        show screen hermione_main
        with d3
        her "............."
    else:
        if request_02 >= 1: #Not the first time
            hide screen hermione_main
            with d3
            $ h_body = "03_hp/13_hermione_main/body_29.png" #Sprite of Hermione's upper body.
            show screen hermione_main
            with d3
            her "Ох... снова?"
            m "Просто сделай это..."
        hide screen hermione_main
        with d3
        $ h_body = "03_hp/13_hermione_main/body_29.png" #Sprite of Hermione's upper body.
        show screen hermione_main
        with d3
        her ".................."
        
        

    hide screen bld1
    hide screen hermione_main
    with d5
    $ menu_x = 0.5 #Default menu position restored.
    if whoring >= 6: # NO Трусики
        show screen hermione_03_b
        with d3
    else:
        show screen hermione_03 #Hermione lifts her skirt
        with d3
        
    #play music "music/Under-the-Radar by PhobyAk.mp3" fadein 1 fadeout 1 
    play music "music/(Orchestral) Playful Tension by Shadow16nh.mp3" fadein 1 fadeout 1 

    if whoring >= 0 and whoring <= 2: #LEVEL 01
        her_08 "........................"
    elif whoring >= 3 and whoring <= 5: #LEVEL 02
        her_14 "....................."
    elif whoring >= 6: #LEVEL 03 and up.
        her_18 ".........................."
        g4 "!!?"
        
        
    

    


    if whoring >= 0 and whoring <= 2: #LEVEL 01   <============================= Fist event.
        $ new_request_02_01 =  True #Hearts.
        show screen bld1
        with d3
        show screen blktone
        with d3
        $ h_xpos=120 #Defines position of the Hermione's full length sprite.
        $ only_upper = True #When False legs are displayed in the hermione_main acreen.
        $ h_body = "03_hp/13_hermione_main/body_49.png" #Flashing Трусики
        show screen hermione_main
        show screen ctc
        with d3
        pause
        
        her "....................."
        menu:
            "-Смотреть на ее лицо-":
                ">Вы внимательно смотрите на лицо Гермионы..."
                pause
                ">Вы задаетесь вопрос о том, что происходит у нее в голове сейчас."
                hide screen hermione_main
                with d3
                $ h_body = "03_hp/13_hermione_main/body_51.png" #Flashing Трусики
                show screen hermione_main
                with d3
                her "......................."
                pause
            "-Смотреть на ее трусики-":
                ">Просто женское белье..."
                pause
                hide screen hermione_main
                with d3
                $ h_body = "03_hp/13_hermione_main/body_51.png" #Flashing Трусики
                show screen hermione_main
                with d3
                her "......................."
               

    elif whoring >= 3 and whoring <= 5: #LEVEL 02  <====================================================================== SECOND EVENT!
        $ new_request_02_02 =  True #Hearts.
        show screen bld1
        with d3
        show screen blktone
        with d3
        $ h_xpos=120 #Defines position of the Hermione's full length sprite.
        $ only_upper = True #When False legs are displayed in the hermione_main acreen.
        $ h_body = "03_hp/13_hermione_main/body_52.png" #Flashing Трусики
        show screen hermione_main
        show screen ctc
        with d3
        pause
        her "Вот, профессор..."
        menu:
            "\"Вы не выглядите смущенно...\"":
                hide screen hermione_main
                with d3
                $ h_body = "03_hp/13_hermione_main/body_53.png" #Flashing Трусики
                show screen hermione_main
                with d3
                her "Это не так..."
                hide screen hermione_main
                with d3
                $ h_body = "03_hp/13_hermione_main/body_54.png" #Flashing Трусики
                show screen hermione_main
                with d3
                her "Это сравнительно небольшая плата, если \"Гриффиндор\" получит кубок в этом году."
                her "Я знаю, что все будут счастливы..."
                pause
            "\"Мне нравятся ваши трусики...\"":
                hide screen hermione_main
                with d3
                $ h_body = "03_hp/13_hermione_main/body_53.png" #Flashing Трусики
                show screen hermione_main
                with d3
                her "Спасибо, профессор..."
            "-Продолжать смотреть в ее глаза-":
                hide screen hermione_main
                with d3
                $ h_body = "03_hp/13_hermione_main/body_55.png" #Flashing Трусики
                show screen hermione_main
                with d3
                her ".............................."
                her "...........................?"
                hide screen hermione_main
                with d3
                $ h_body = "03_hp/13_hermione_main/body_56.png" #Flashing Трусики
                show screen hermione_main
                with d3
                her "................................"
                hide screen hermione_main
                with d3
                $ h_body = "03_hp/13_hermione_main/body_57.png" #Flashing Трусики
                show screen hermione_main
                with d3
                her "Профессор, пожалуйста... Вы смущаете меня."
                

    elif whoring >= 9: #LEVEL 04 and up. <====================================================================== FINAL EVENT! (No Трусики).
        $ new_request_02_03 =  True #Hearts.
        show screen bld1
        with d3
        show screen blktone
        with d3
        $ h_xpos=120 #Defines position of the Hermione's full length sprite.
        $ only_upper = True #When False legs are displayed in the hermione_main acreen.
        $ h_body = "03_hp/13_hermione_main/body_58.png" #Flashing Трусики
        show screen hermione_main
        show screen ctc
        with d3
        pause
        g4 "Где ваши трусики, мисс Грейнджер?"
        hide screen hermione_main
        with d3
        $ h_body = "03_hp/13_hermione_main/body_59.png" #Flashing Трусики
        show screen hermione_main
        with d3
        her "Ох, в последнее время я не очень хочу носить их..."
        menu:
            "\"Ах ты маленькая шлюха!\"":
                her "Хм..."
                hide screen hermione_main
                with d3
                $ h_body = "03_hp/13_hermione_main/body_58.png" #Flashing Трусики
                show screen hermione_main
                with d3
                her "Вероятно это так..."
                her "Могу я получить чуть больше очков за это?"
                menu:
                    "\"Конечно!\"":
                        m "Конечно!"
                        $ gryffindor +=10
                        m "Десять очков \"Гриффиндору\"!" 
                        hide screen hermione_main
                        with d3
                        $ h_body = "03_hp/13_hermione_main/body_60.png" #Flashing Трусики
                        show screen hermione_main
                        with d3
                        her "Спасибо вам, сэр!"
                    "\"Категорически нет!\"":
                        $ mad +=15
                        hide screen hermione_main
                        with d3
                        $ h_body = "03_hp/13_hermione_main/body_61.png" #Flashing Трусики
                        show screen hermione_main
                        with d3
                        her ".............................."
                        hide screen hermione_main
                        with d3
                        $ h_body = "03_hp/13_hermione_main/body_62.png" #Flashing Трусики
                        show screen hermione_main
                        with d3
                        her "Не будьте так скупы, профессор."   
            "\"Отлично. Пять очков Гриффиндору!\"":
                pass
    
    
    
    
    stop music fadeout 4.0
    
    label request_02_done:
    $ gryffindor +=5
    m "Пять очков  \"Гриффиндору\", мисс Грейнджер. Отличная работа." 
    pause
    
    $ hermione_chibi_xpos = 400 #Near the desk.
    $ h_xpos=120 #Defines position of the Hermione's full length sprite.
    hide screen ctc
    hide screen hermione_main
    with d3
    $ h_body = "03_hp/13_hermione_main/body_31.png" #Flashing Трусики
    $ only_upper = False #When False legs are displayed in the hermione_main acreen.
    show screen hermione_02 #Hermione stands still.
    show screen hermione_main
    with fade
    
    stop music fadeout 4.0
    
    her "Это все?"
    m "Да, можешь идти."

    if request_02 == 0: #First time.
        hide screen hermione_main
        with d3
        $ h_xpos=300 #Defines position of the Hermione's full length sprite.
        $ h_body = "03_hp/13_hermione_main/body_13.png" #Flashing Трусики
        show screen hermione_main
        with d3
        her "Еще пять очков..."
        her "Не дождусь рассказать ребятам!"
        hide screen hermione_main
        with d3
        $ h_xpos=300 #Defines position of the Hermione's full length sprite.
        $ h_body = "03_hp/13_hermione_main/body_12.png" #Flashing Трусики
        show screen hermione_main
        with d3
        her "Только я не могу рассказать о всем, что пришлось сделать для этого..."
    
    if daytime:
        her "Ну, мои занятия вот-вот начнутся..."
    else:
        her "Уже довольно поздно, сэр... Мне нужно идти..."

    
    hide screen hermione_main
    with d3
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

###################REQUEST_02_b (LEVEL 01) ### FLIRT WITH CLASSMATES ###
label new_request_02_b:
    hide screen hermione_main
    with d3
    m "{size=-4}(Попросить ее флиртовать с парнями из \"Слизерина\"?){/size}"
    $ menu_x = 0.5 #Default menu position restored.
    menu:
        "\"(Да, давай попробуем!)\"":
            pass
        "\"(Не сейчас.)\"":
            jump new_personal_request
    
    m "Мисс Грейнджер?"
    $ h_xpos=140 #Defines position of the Hermione's full length sprite. (Default 370). 140 - center.
    $ h_body = "03_hp/13_hermione_main/body_13.png" #Flashing Трусики
    show screen hermione_main
    with d3
    her "Да?"
    
    if request_02_b_points == 0 and whoring <= 5: ### LEVEL 01 and LEVEL 02
        ### LEVEL 01 ### <===============================================================FIRST EVENT!
        play music "music/Chipper Doodle v2.mp3" fadein 1 fadeout 1 # HERMIONE'S THEME.
        m "Что вы думаете насчет мальчиков из \"Слизерина\"?"
        hide screen hermione_main
        with d3
        $ h_xpos=140 #Defines position of the Hermione's full length sprite. (Default 370). 140 - center.
        $ h_body = "03_hp/13_hermione_main/body_05.png" #Flashing Трусики
        show screen hermione_main
        with d3
        her "Я терпеть их не могу, сэр."
        m "Ну, очень плохо. Потому что я хочу, чтобы ты подружилась с несколькими из них."
        hide screen hermione_main
        with d3
        $ h_xpos=140 #Defines position of the Hermione's full length sprite. (Default 370). 140 - center.
        $ h_body = "03_hp/13_hermione_main/body_13.png" #Flashing Трусики
        show screen hermione_main
        with d3
        her "Если я должна..."
        her "Да, думаю я могу быть вежлива с парой из них."
        m "Да, и я сказал \"подружиться с ними...\""
        m "Вообще я имел в виду заигрывания с ними..."
        hide screen hermione_main
        with d3
        $ h_xpos=140 #Defines position of the Hermione's full length sprite. (Default 370). 140 - center.
        $ h_body = "03_hp/13_hermione_main/body_48.png" #Flashing Трусики
        show screen hermione_main
        with d3
        her "Заигрывать?!"
        hide screen hermione_main
        with d3
        $ h_xpos=140 #Defines position of the Hermione's full length sprite. (Default 370). 140 - center.
        $ h_body = "03_hp/13_hermione_main/body_47.png" #Flashing Трусики
        show screen hermione_main
        with d3
        her "Профессор Дамблдор!"
        hide screen hermione_main
        with d3
        $ h_xpos=140 #Defines position of the Hermione's full length sprite. (Default 370). 140 - center.
        $ h_body = "03_hp/13_hermione_main/body_17.png" #Flashing Трусики
        show screen hermione_main
        with d3
        her "Я даже не буду спрашивать, почему вам это интересно..."
        hide screen hermione_main
        with d3
        $ h_xpos=140 #Defines position of the Hermione's full length sprite. (Default 370). 140 - center.
        $ h_body = "03_hp/13_hermione_main/body_11.png" #Flashing Трусики
        show screen hermione_main
        with d3
        her "Но почему \"Слизерин\"?"
        her "Если вам нужно, чтобы я кокетничала сегодня, то я могу..."
        her "Но, пожалуйста, может быть другой факультет?"
        hide screen hermione_main
        with d3
        $ h_xpos=140 #Defines position of the Hermione's full length sprite. (Default 370). 140 - center.
        $ h_body = "03_hp/13_hermione_main/body_44.png" #Flashing Трусики
        show screen hermione_main
        with d3
        her "Может \"Гриффиндор\"?"
        m "Я просто стараюсь защитить вашу репутацию, Мисс Грейнджер."
        hide screen hermione_main
        with d3
        $ h_xpos=140 #Defines position of the Hermione's full length sprite. (Default 370). 140 - center.
        $ h_body = "03_hp/13_hermione_main/body_15.png" #Flashing Трусики
        show screen hermione_main
        with d3
        her "Сэр?"
        m "Вам важно мнение \"Слизеринских\" учеников о себе?"
        hide screen hermione_main
        with d3
        $ h_xpos=140 #Defines position of the Hermione's full length sprite. (Default 370). 140 - center.
        $ h_body = "03_hp/13_hermione_main/body_30.png" #Flashing Трусики
        show screen hermione_main
        with d3
        her "Вообще мне плевать на мнение этих дикарей."
        m "Что насчет студентов из \"Гриффиндора\"?"
        hide screen hermione_main
        with d3
        $ h_xpos=140 #Defines position of the Hermione's full length sprite. (Default 370). 140 - center.
        $ h_body = "03_hp/13_hermione_main/body_29.png" #Flashing Трусики
        show screen hermione_main
        with d3
        her "Их мнение очень важно для меня--"
        hide screen hermione_main
        with d3
        $ h_xpos=140 #Defines position of the Hermione's full length sprite. (Default 370). 140 - center.
        $ h_body = "03_hp/13_hermione_main/body_06.png" #Flashing Трусики
        show screen hermione_main
        with d3
        her "Ох, понятно..."
        m "Точно... Просто идеально для вас, Мисс Грейнджер."
        her "Эм... Спасибо, профессор..."
        call music_block
    
    else:
        if whoring <= 2: ### LEVEL 01
            m "Мне нужно, чтобы ты завела пару друзей в \"Слизерине\"."
            her "То есть снова заигрывать со \"слизеринскими\" парнями?"
            m "Именно то, что я хочу от вас сегодня, Мисс Грейнджер."
            hide screen hermione_main
            with d3
            $ h_xpos=140 #Defines position of the Hermione's full length sprite. (Default 370). 140 - center.
            $ h_body = "03_hp/13_hermione_main/body_02.png" #Flashing Трусики
            show screen hermione_main
            with d3
            her "Мне действительно это нужно делать?"
            m "Мы уже проходили через это, девочка."
            m "В твоих же интересах заводить себе друзей в \"Слизерине\"."
            hide screen hermione_main
            with d3
            $ h_xpos=140 #Defines position of the Hermione's full length sprite. (Default 370). 140 - center.
            $ h_body = "03_hp/13_hermione_main/body_04.png" #Flashing Трусики
            show screen hermione_main
            with d3
            her "Да, я знаю, сэр."
            her "Но почему именно я?"
            m "Никто вас не заставляет, Мисс Грейнджер..."
            hide screen hermione_main
            with d3
            $ h_xpos=140 #Defines position of the Hermione's full length sprite. (Default 370). 140 - center.
            $ h_body = "03_hp/13_hermione_main/body_05.png" #Flashing Трусики
            show screen hermione_main
            with d3
            her "Вам не нужно напоминать мне это, сэр..."
            hide screen hermione_main
            with d3
            $ h_xpos=140 #Defines position of the Hermione's full length sprite. (Default 370). 140 - center.
            $ h_body = "03_hp/13_hermione_main/body_07.png" #Flashing Трусики
            show screen hermione_main
            with d3
            her "Ладно, я поняла... Сэр..."


        else: #if whoring >= 3 and whoring >= 6: ### LEVEL 02 and higher ## <=========================================================== SECOND EVENT!
            m "Ты должна кокетничать с парнями из \"Слизерина\"."
            her "Я посмотрю, что можно сделать."
            m "Отлично. Буду ждать вас после занятий."

    
    her "Ну, мне стоит идти. Занятия вот-вот начнутся..."
    $ request_02_b = True

    hide screen bld1
    hide screen hermione_main
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
    jump day_main_menu
   
        
        
label new_request_02_b_complete:
    $ walk_xpos=520 #Animation of walking chibi. (From)
    $ walk_xpos2=400 #Coordinates of it's movement. (To)
    $ hermione_speed = 02.0 #The speed of moving the walking animation across the screen.
    $ renpy.play('sounds/door.mp3') #Sound of a door opening.
    show screen hermione_walk_01 
    with d4
    pause 1.7 
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
    her "Добрый вечер, сэр."
    m "Мисс Грейнджер..."
    m "Вы завершили задание?"
    her "Я сделала все как вы просили..."
    menu:
        "\"Отлично. Вот твои очки.\"":
            pass
        "\"Расскажи поподробнее.\"":
            hide screen hermione_main
            with d3
            m "Со сколькими мальчиками вы успели позаигрывать, Мисс Грейнджер?"
            m "Раскажите мне."
            show screen blktone
            with d3
            if whoring >= 0 and whoring <= 2: ### LEVEL 01
                if one_out_of_three == 1: ### EVENT (A)
                    
                    stop music fadeout 1.0
                    hide screen hermione_main
                    with d3
                    $ h_xpos=370 #Defines position of the Hermione's full length sprite. (Default 370). 140 - center.
                    $ h_body = "03_hp/13_hermione_main/body_10.png" #Flashing Трусики
                    show screen hermione_main
                    with d3
                    her "Ну..."
                    her "Был этот первокурсик..."
                    her "........."
                    m "Я слушаю..."
                    her "Эм... Я подошла к нему и сказа \"Эй, красавчик!\"."
                    m "И?"
                    play music "music/Chipper Doodle v2.mp3" fadein 1 fadeout 1 # HERMIONE'S THEME.
                    hide screen hermione_main
                    with d3
                    $ h_xpos=370 #Defines position of the Hermione's full length sprite. (Default 370). 140 - center.
                    $ h_body = "03_hp/13_hermione_main/body_07.png" #Flashing Трусики
                    show screen hermione_main
                    with d3
                    her "Он показал мне язык и убежал, сэр."
                    m "Ты пробовала заманить его обратно конфеткой?"
                    hide screen hermione_main
                    with d3
                    $ h_xpos=370 #Defines position of the Hermione's full length sprite. (Default 370). 140 - center.
                    $ h_body = "03_hp/13_hermione_main/body_10.png" #Flashing Трусики
                    show screen hermione_main
                    with d3
                    her "Нет, сэр..."
                    her "Это не приходило мне в голову--"
                    m "Я шучу, Мисс Грейнджер."
                    hide screen hermione_main
                    with d3
                    $ h_xpos=370 #Defines position of the Hermione's full length sprite. (Default 370). 140 - center.
                    $ h_body = "03_hp/13_hermione_main/body_07.png" #Flashing Трусики
                    show screen hermione_main
                    with d3
                    her "Сэр?"
                    m "Я не посылал тебя приставать к маленьким детям!"
                    hide screen hermione_main
                    with d3
                    $ h_xpos=370 #Defines position of the Hermione's full length sprite. (Default 370). 140 - center.
                    $ h_body = "03_hp/13_hermione_main/body_09.png" #Flashing Трусики
                    show screen hermione_main
                    with d3
                    her "............."
                    m "Я попросил тебя флиртовать с мальчиками {size=+5}твоего{/size} возраста!"
                    hide screen hermione_main
                    with d3
                    $ h_xpos=370 #Defines position of the Hermione's full length sprite. (Default 370). 140 - center.
                    $ h_body = "03_hp/13_hermione_main/body_07.png" #Flashing Трусики
                    show screen hermione_main
                    with d3
                    her "Сначала я хотела, но..."
                    hide screen hermione_main
                    with d3
                    $ h_xpos=370 #Defines position of the Hermione's full length sprite. (Default 370). 140 - center.
                    $ h_body = "03_hp/13_hermione_main/body_12.png" #Flashing Трусики
                    show screen hermione_main
                    with d3
                    her "Я просто испугалась..."
                    her "То есть я презираю  \"Слизеринцев\" слишком сильно, чтобы флиртовать с ними, сэр!"
                    hide screen hermione_main
                    with d3
                    $ h_xpos=370 #Defines position of the Hermione's full length sprite. (Default 370). 140 - center.
                    $ h_body = "03_hp/13_hermione_main/body_05.png" #Flashing Трусики
                    show screen hermione_main
                    with d3
                    her "Мне приходится бороться с рвотным рефлексом при их виде!"
                    menu:
                        "\"Ладно. Попробуй в следующий раз.\"":
                            hide screen hermione_main
                            with d3
                            $ h_xpos=370 #Defines position of the Hermione's full length sprite. (Default 370). 140 - center.
                            $ h_body = "03_hp/13_hermione_main/body_06.png" #Flashing Трусики
                            show screen hermione_main
                            with d3
                            her "Спасибо, сэр."
                            her "Я попробую, обещаю!"
                        "\"Ты провалилась! Никаких очков ты не получишь!\"":
                            stop music fadeout 1.0
                            hide screen hermione_main
                            with d3
                            $ h_xpos=370 #Defines position of the Hermione's full length sprite. (Default 370). 140 - center.
                            $ h_body = "03_hp/13_hermione_main/body_07.png" #Flashing Трусики
                            show screen hermione_main
                            with d3
                            her "Я понимаю..."
                            m "Убирайся с глаз моих..."
                            hide screen hermione_main
                            with d3
                            $ h_xpos=370 #Defines position of the Hermione's full length sprite. (Default 370). 140 - center.
                            $ h_body = "03_hp/13_hermione_main/body_09.png" #Flashing Трусики
                            show screen hermione_main
                            with d3
                            her "Да, сэр...Простите, сэр..."
                            jump could_not_flirt
                    
                elif one_out_of_three == 2: ### EVENT (B)
                    play music "music/Chipper Doodle v2.mp3" fadein 1 fadeout 1 # HERMIONE'S THEME.
                    hide screen hermione_main
                    with d3
                    $ h_xpos=370 #Defines position of the Hermione's full length sprite. (Default 370). 140 - center.
                    $ h_body = "03_hp/13_hermione_main/body_10.png" #Flashing Трусики
                    show screen hermione_main
                    with d3
                    her "Ну, я пыталась подкатить к старшекласснику..."
                    m "Он повелся?"
                    hide screen hermione_main
                    with d3
                    $ h_xpos=370 #Defines position of the Hermione's full length sprite. (Default 370). 140 - center.
                    $ h_body = "03_hp/13_hermione_main/body_76.png" #Flashing Трусики
                    show screen hermione_main
                    with d3
                    her "Он назвал меня \"Гриффиндорской шлюхой\", сэр!"
                    m "Понятно..."
                    m "И что ты сделал?"
                    hide screen hermione_main
                    with d3
                    $ h_xpos=370 #Defines position of the Hermione's full length sprite. (Default 370). 140 - center.
                    $ h_body = "03_hp/13_hermione_main/body_04.png" #Flashing Трусики
                    show screen hermione_main
                    with d3
                    her "Ну, это было неправильно для ученика \"Хогвартса\"..."
                    her "И я сказала ему, что настучу на него."
                    m "Действительно захватывающая история..."
                    m "Что-то еще?"
                    hide screen hermione_main
                    with d3
                    $ h_xpos=370 #Defines position of the Hermione's full length sprite. (Default 370). 140 - center.
                    $ h_body = "03_hp/13_hermione_main/body_09.png" #Flashing Трусики
                    show screen hermione_main
                    with d3
                    her "Да, был еще мальчик в библиотеке..."
                    her "Он, очевидно, был чем-то занят..."
                    her "Ну я и предложила свою помощь..."
                    m "И?"
                    hide screen hermione_main
                    with d3
                    $ h_xpos=370 #Defines position of the Hermione's full length sprite. (Default 370). 140 - center.
                    $ h_body = "03_hp/13_hermione_main/body_76.png" #Flashing Трусики
                    show screen hermione_main
                    with d3
                    her "Он назвал меня \"Главной шлюхой Гриффиндора\"..."
                    m "И ты угрожала настучать на него за это?"
                    hide screen hermione_main
                    with d3
                    $ h_xpos=370 #Defines position of the Hermione's full length sprite. (Default 370). 140 - center.
                    $ h_body = "03_hp/13_hermione_main/body_04.png" #Flashing Трусики
                    show screen hermione_main
                    with d3
                    her "Конечно, сэр."
                    m "*Вздох*"
                    m "Что-то еще?"
                    hide screen hermione_main
                    with d3
                    $ h_xpos=370 #Defines position of the Hermione's full length sprite. (Default 370). 140 - center.
                    $ h_body = "03_hp/13_hermione_main/body_09.png" #Flashing Трусики
                    show screen hermione_main
                    with d3
                    her "Ну, был еще один момент, похожий на предыдущие..."
                    m "\"Гриффиндорская шлюха\"?"
                    hide screen hermione_main
                    with d3
                    $ h_xpos=370 #Defines position of the Hermione's full length sprite. (Default 370). 140 - center.
                    $ h_body = "03_hp/13_hermione_main/body_66.png" #Flashing Трусики
                    show screen hermione_main
                    with d3
                    her ".........да, сэр."
                    m "Вы делаете все неправильно, Мисс Грейнджер."
                    hide screen hermione_main
                    with d3
                    $ h_xpos=370 #Defines position of the Hermione's full length sprite. (Default 370). 140 - center.
                    $ h_body = "03_hp/13_hermione_main/body_69.png" #Flashing Трусики
                    show screen hermione_main
                    with d3
                    her "Простите, профессор. Я думала, что будет легко..."
                    menu:
                        "\"Ну, ты хотя бы попыталась.\"":
                            hide screen hermione_main
                            with d3
                            $ h_xpos=370 #Defines position of the Hermione's full length sprite. (Default 370). 140 - center.
                            $ h_body = "03_hp/13_hermione_main/body_34.png" #Flashing Трусики
                            show screen hermione_main
                            with d3
                            her "Видимо флирт не одна из моих сильных сторон..."
                        "\"Задание провалено. Ты не получишь очки!\"":
                            stop music fadeout 1.0
                            hide screen hermione_main
                            with d3
                            $ h_xpos=370 #Defines position of the Hermione's full length sprite. (Default 370). 140 - center.
                            $ h_body = "03_hp/13_hermione_main/body_11.png" #Flashing Трусики
                            show screen hermione_main
                            with d3
                            $ mad +=15
                            her "Вы не заплатите мне, сэр?"
                            hide screen hermione_main
                            with d3
                            $ h_xpos=370 #Defines position of the Hermione's full length sprite. (Default 370). 140 - center.
                            $ h_body = "03_hp/13_hermione_main/body_21.png" #Flashing Трусики
                            show screen hermione_main
                            with d3
                            her "Но, вы обещали!"
                            hide screen hermione_main
                            with d3
                            $ h_xpos=370 #Defines position of the Hermione's full length sprite. (Default 370). 140 - center.
                            $ h_body = "03_hp/13_hermione_main/body_20.png" #Flashing Трусики
                            show screen hermione_main
                            with d3
                            her "................"
                            call music_block
                            jump could_not_flirt
                    
                elif one_out_of_three == 3: ### EVENT (C)
                    stop music fadeout 1.0
                    hide screen hermione_main
                    with d3
                    $ h_xpos=370 #Defines position of the Hermione's full length sprite. (Default 370). 140 - center.
                    $ h_body = "03_hp/13_hermione_main/body_10.png" #Flashing Трусики
                    show screen hermione_main
                    with d3
                    her "Ну, команда \"Слизерина\" по квиддичу занималась сегодня на стадионе..."
                    her "Я подумала, что смогу проникнуть на трибуны и болеть за них..."
                    hide screen hermione_main
                    with d3
                    $ h_xpos=370 #Defines position of the Hermione's full length sprite. (Default 370). 140 - center.
                    $ h_body = "03_hp/13_hermione_main/body_12.png" #Flashing Трусики
                    show screen hermione_main
                    with d3
                    her "Но..."
                    m "Да?"
                    play music "music/Chipper Doodle v2.mp3" fadein 1 fadeout 1 # HERMIONE'S THEME.
                    hide screen hermione_main
                    with d3
                    $ h_xpos=370 #Defines position of the Hermione's full length sprite. (Default 370). 140 - center.
                    $ h_body = "03_hp/13_hermione_main/body_77.png" #Flashing Трусики
                    show screen hermione_main
                    with d3
                    her "Все эти \"Слизеринские\" шлюхи уже были там."
                    her "У них были кричалки и все такое..."
                    hide screen hermione_main
                    with d3
                    $ h_xpos=370 #Defines position of the Hermione's full length sprite. (Default 370). 140 - center.
                    $ h_body = "03_hp/13_hermione_main/body_47.png" #Flashing Трусики
                    show screen hermione_main
                    with d3
                    her "И некоторые из них даже показывали себя неподобающим образом, сэр..."
                    her "Я не могу поверить, что таких допустили к обучению в нашей школе..."
                    m "И так...что же было в конце этого всего?"
                    hide screen hermione_main
                    with d3
                    $ h_xpos=370 #Defines position of the Hermione's full length sprite. (Default 370). 140 - center.
                    $ h_body = "03_hp/13_hermione_main/body_69.png" #Flashing Трусики
                    show screen hermione_main
                    with d3
                    her "Я просто ушла, сэр..."
                    menu:
                        m "Хм..."
                        "\"Но все же, вот твои очки.\"":
                            hide screen hermione_main
                            with d3
                            $ h_xpos=370 #Defines position of the Hermione's full length sprite. (Default 370). 140 - center.
                            $ h_body = "03_hp/13_hermione_main/body_16.png" #Flashing Трусики
                            show screen hermione_main
                            with d3
                            her "Спасибо, сэр..."               
                            
                        "\"Задание провалено! Ты не получишь очки!\"":
                            stop music fadeout 1.0
                            hide screen hermione_main
                            with d3
                            $ h_xpos=370 #Defines position of the Hermione's full length sprite. (Default 370). 140 - center.
                            $ h_body = "03_hp/13_hermione_main/body_12.png" #Flashing Трусики
                            show screen hermione_main
                            with d3
                            her "Все равно я чувствую, что не заслужила ничего за это..."
                            call music_block
                            jump could_not_flirt
                    
                    
                    
                    
            elif whoring >= 3 and whoring <= 5: ### LEVEL 02
                if one_out_of_three == 1: ### EVENT (A)
                    stop music fadeout 1.0
                    hide screen hermione_main
                    with d3
                    $ h_xpos=140 #Defines position of the Hermione's full length sprite. (Default 370). 140 - center.
                    $ h_body = "03_hp/13_hermione_main/body_10.png" #Flashing Трусики
                    show screen hermione_main
                    with d3
                    her "Ну, был один парень в библиотеке..."
                    her "Он был чем-то озадачен и я предложила помощь..."
                    m "И?"
                    play music "music/Chipper Doodle v2.mp3" fadein 1 fadeout 1 # HERMIONE'S THEME.
                    hide screen hermione_main
                    with d3
                    $ h_xpos=140 #Defines position of the Hermione's full length sprite. (Default 370). 140 - center.
                    $ h_body = "03_hp/13_hermione_main/body_75.png" #Flashing Трусики
                    show screen hermione_main
                    with d3
                    her "Ну, к моему удивению, он принял помощь..."
                    her "Он позволил закончить для него задание..."
                    hide screen hermione_main
                    with d3
                    $ h_xpos=140 #Defines position of the Hermione's full length sprite. (Default 370). 140 - center.
                    $ h_body = "03_hp/13_hermione_main/body_34.png" #Flashing Трусики
                    show screen hermione_main
                    with d3
                    her "Пока я работала, он сделал пару неуместных замечаний, но я просто улыбалась в ответ..."
                    m "Кажется он сам флиртовал с тобой..."
                    hide screen hermione_main
                    with d3
                    $ h_xpos=140 #Defines position of the Hermione's full length sprite. (Default 370). 140 - center.
                    $ h_body = "03_hp/13_hermione_main/body_24.png" #Flashing Трусики
                    show screen hermione_main
                    with d3
                    her "Ну... думаю да."
                    hide screen hermione_main
                    with d3
                    $ h_xpos=140 #Defines position of the Hermione's full length sprite. (Default 370). 140 - center.
                    $ h_body = "03_hp/13_hermione_main/body_45.png" #Flashing Трусики
                    show screen hermione_main
                    with d3
                    her "Но, несмотря на его недостойное поведение, я подыгрывала ему..."
                    m "Осторожно?"
                    her "Да, сэр..."
                    her "То есть, он чего-то хотел, верно?"
                    m "Э-эм..."
                    m "Что у тебя еще есть?"
                    hide screen hermione_main
                    with d3
                    $ h_xpos=140 #Defines position of the Hermione's full length sprite. (Default 370). 140 - center.
                    $ h_body = "03_hp/13_hermione_main/body_69.png" #Flashing Трусики
                    show screen hermione_main
                    with d3
                    her "Верно..."
                    her "Потом в коридоре я встретила ребят, которые оценили мою внешность в весьма вульгарной манере..."
                    hide screen hermione_main
                    with d3
                    $ h_xpos=140 #Defines position of the Hermione's full length sprite. (Default 370). 140 - center.
                    $ h_body = "03_hp/13_hermione_main/body_34.png" #Flashing Трусики
                    show screen hermione_main
                    with d3
                    her "Но я просто улыбнулась им..."
                    m "И снова ты почти ничего не сделала..."
                    m "Это не то, что я просил, Мисс Грейнджер."
                    hide screen hermione_main
                    with d3
                    $ h_xpos=140 #Defines position of the Hermione's full length sprite. (Default 370). 140 - center.
                    $ h_body = "03_hp/13_hermione_main/body_34.png" #Flashing Трусики
                    show screen hermione_main
                    with d3
                    her "Я знаю, сэр!"
                    hide screen hermione_main
                    with d3
                    $ h_xpos=140 #Defines position of the Hermione's full length sprite. (Default 370). 140 - center.
                    $ h_body = "03_hp/13_hermione_main/body_69.png" #Flashing Трусики
                    show screen hermione_main
                    with d3
                    her "Но я очень занята. У меня встречи \"ОЗМП\" и еще занятия..."
                    her "Мне едва хватает времени--"
                    m "Это все, что ты хотела мне сказать сегодня?"
                    hide screen hermione_main
                    with d3
                    $ h_xpos=140 #Defines position of the Hermione's full length sprite. (Default 370). 140 - center.
                    $ h_body = "03_hp/13_hermione_main/body_69.png" #Flashing Трусики
                    show screen hermione_main
                    with d3
                    her "Нет, сэр."
                    her "Около часа назад я столкнулась с Драко Малфоем."
                    m "Не может быть!!! (Понятия не имею кто это...)"
                    her "Я пыталась быть дружелюбной с ним..."
                    hide screen hermione_main
                    with d3
                    $ h_xpos=140 #Defines position of the Hermione's full length sprite. (Default 370). 140 - center.
                    $ h_body = "03_hp/13_hermione_main/body_74.png" #Flashing Трусики
                    show screen hermione_main
                    with d3
                    her "В итоге мы закончили не очень приличной беседой." 
                    translators "Drako - Драко Малфой.\nDark-Ох - темный..."
                    m "Понятно... Это \"Темный\" парень..."
                    m "Он вообще смотрел на твои ножки?"
                    hide screen hermione_main
                    with d3
                    $ h_xpos=140 #Defines position of the Hermione's full length sprite. (Default 370). 140 - center.
                    $ h_body = "03_hp/13_hermione_main/body_02.png" #Flashing Трусики
                    show screen hermione_main
                    with d3
                    her "Что?"
                    m "Он смотрел на твои ноги или нет??"
                    hide screen hermione_main
                    with d3
                    $ h_xpos=140 #Defines position of the Hermione's full length sprite. (Default 370). 140 - center.
                    $ h_body = "03_hp/13_hermione_main/body_44.png" #Flashing Трусики
                    show screen hermione_main
                    with d3
                    her "Эм...возможно так и было..."
                    m "Что насчет сисек?"
                    hide screen hermione_main
                    with d3
                    $ h_xpos=140 #Defines position of the Hermione's full length sprite. (Default 370). 140 - center.
                    $ h_body = "03_hp/13_hermione_main/body_47.png" #Flashing Трусики
                    show screen hermione_main
                    with d3
                    her "Профессор!!!"
                    m "Ладно. Получай свои очки. Ты хорошо постаралась."
                    hide screen hermione_main
                    with d3
                    $ h_xpos=140 #Defines position of the Hermione's full length sprite. (Default 370). 140 - center.
                    $ h_body = "03_hp/13_hermione_main/body_29.png" #Flashing Трусики
                    show screen hermione_main
                    with d3
 
                elif one_out_of_three == 2: ### EVENT (B)
                    stop music fadeout 1.0
                    hide screen hermione_main
                    with d3
                    $ h_xpos=370 #Defines position of the Hermione's full length sprite. (Default 370). 140 - center.
                    $ h_body = "03_hp/13_hermione_main/body_10.png" #Flashing Трусики
                    show screen hermione_main
                    with d3
                    her "Ну..."
                    her "Сегодня утром я заигрывала с одним парнем..."
                    hide screen hermione_main
                    with d3
                    $ h_xpos=370 #Defines position of the Hermione's full length sprite. (Default 370). 140 - center.
                    $ h_body = "03_hp/13_hermione_main/body_13.png" #Flashing Трусики
                    show screen hermione_main
                    with d3
                    her "Через секунду уже с другим..."
                    hide screen hermione_main
                    with d3
                    $ h_xpos=370 #Defines position of the Hermione's full length sprite. (Default 370). 140 - center.
                    $ h_body = "03_hp/13_hermione_main/body_28.png" #Flashing Трусики
                    show screen hermione_main
                    with d3
                    her "А потом случилось что-то странное..."
                    play music "music/(Orchestral) Playful Tension by Shadow16nh.mp3" fadein 1 fadeout 1 # SEX THEME.
                    her "Этот злобно-выгядящий парень из \"Слизерина\" подошел и пригласил меня на свидание..."
                    hide screen hermione_main
                    with d3
                    $ h_xpos=370 #Defines position of the Hermione's full length sprite. (Default 370). 140 - center.
                    $ h_body = "03_hp/13_hermione_main/body_13.png" #Flashing Трусики
                    show screen hermione_main
                    with d3
                    her "Я ему отказала, но все таки он шел со мной вместе."
                    m "Вам это понравилось, Мисс Грейнджер?"
                    hide screen hermione_main
                    with d3
                    $ h_xpos=370 #Defines position of the Hermione's full length sprite. (Default 370). 140 - center.
                    $ h_body = "03_hp/13_hermione_main/body_31.png" #Flashing Трусики
                    show screen hermione_main
                    with d3
                    her "Я думаю да... К моему собственному удивлению..."
                    hide screen hermione_main
                    with d3
                    $ h_xpos=370 #Defines position of the Hermione's full length sprite. (Default 370). 140 - center.
                    $ h_body = "03_hp/13_hermione_main/body_45.png" #Flashing Трусики
                    show screen hermione_main
                    with d3
                    her "Мне вроде и было безразлично, но..."
                    hide screen hermione_main
                    with d3
                    $ h_xpos=370 #Defines position of the Hermione's full length sprite. (Default 370). 140 - center.
                    $ h_body = "03_hp/13_hermione_main/body_74.png" #Flashing Трусики
                    show screen hermione_main
                    with d3
                    her "Он был так уверен и спокоен..."
                    hide screen hermione_main
                    with d3
                    $ h_xpos=370 #Defines position of the Hermione's full length sprite. (Default 370). 140 - center.
                    $ h_body = "03_hp/13_hermione_main/body_34.png" #Flashing Трусики
                    show screen hermione_main
                    with d3
                    her "Я конечно же до сих пор ненавижу \"Слизерин\"!"
                    hide screen hermione_main
                    with d3
                    $ h_xpos=370 #Defines position of the Hermione's full length sprite. (Default 370). 140 - center.
                    $ h_body = "03_hp/13_hermione_main/body_73.png" #Flashing Трусики
                    show screen hermione_main
                    with d3
                    her "Но..."
                    her "Может быть некоторые ученики там по ошибке?"
                    hide screen hermione_main
                    with d3
                    $ h_xpos=370 #Defines position of the Hermione's full length sprite. (Default 370). 140 - center.
                    $ h_body = "03_hp/13_hermione_main/body_10.png" #Flashing Трусики
                    show screen hermione_main
                    with d3
                    her "Может быть \"Шляпа\"... спутала?"
                    menu:
                        "\"Просто забирай свои очки и иди!\"":
                            hide screen hermione_main
                            with d3
                            $ h_xpos=370 #Defines position of the Hermione's full length sprite. (Default 370). 140 - center.
                            $ h_body = "03_hp/13_hermione_main/body_07.png" #Flashing Трусики
                            show screen hermione_main
                            with d3
                            her "................"
                        "\"Она никогда не ошибается!\"":
                            hide screen hermione_main
                            with d3
                            $ h_xpos=370 #Defines position of the Hermione's full length sprite. (Default 370). 140 - center.
                            $ h_body = "03_hp/13_hermione_main/body_13.png" #Flashing Трусики
                            show screen hermione_main
                            with d3
                            her "Д, конечно... Все это знают..."
                        "\"Ты думаешь это так?\"":
                            hide screen hermione_main
                            with d3
                            $ h_xpos=370 #Defines position of the Hermione's full length sprite. (Default 370). 140 - center.
                            $ h_body = "03_hp/13_hermione_main/body_13.png" #Flashing Трусики
                            show screen hermione_main
                            with d3
                            her "Ох, не обращайте на меня внимания."
                            her "Все знают, что \"Шляпа\" никогда не ошибается."
                    
                    
                elif one_out_of_three == 3: ### EVENT (C)
                    play music "music/Chipper Doodle v2.mp3" fadein 1 fadeout 1 # HERMIONE'S THEME.
                    hide screen hermione_main
                    with d3
                    $ h_xpos=370 #Defines position of the Hermione's full length sprite. (Default 370). 140 - center.
                    $ h_body = "03_hp/13_hermione_main/body_75.png" #Flashing Трусики
                    show screen hermione_main
                    with d3
                    her "Пять парней, сэр!"
                    m "Действительно?"
                    hide screen hermione_main
                    with d3
                    $ h_xpos=370 #Defines position of the Hermione's full length sprite. (Default 370). 140 - center.
                    $ h_body = "03_hp/13_hermione_main/body_74.png" #Flashing Трусики
                    show screen hermione_main
                    with d3
                    her "Да!"
                    hide screen hermione_main
                    with d3
                    $ h_xpos=370 #Defines position of the Hermione's full length sprite. (Default 370). 140 - center.
                    $ h_body = "03_hp/13_hermione_main/body_74.png" #Flashing Трусики
                    show screen hermione_main
                    with d3
                    her "Один сегодня утром."
                    her "Потом сразу же двое мальчиков во второй раз."
                    her "И еще один в третий раз."
                    hide screen hermione_main
                    with d3
                    $ h_xpos=370 #Defines position of the Hermione's full length sprite. (Default 370). 140 - center.
                    $ h_body = "03_hp/13_hermione_main/body_68.png" #Flashing Трусики
                    show screen hermione_main
                    with d3
                    her "И после этого у меня был довольно приятный разгвор с одним мальчиком."
                    hide screen hermione_main
                    with d3
                    $ h_xpos=370 #Defines position of the Hermione's full length sprite. (Default 370). 140 - center.
                    $ h_body = "03_hp/13_hermione_main/body_74.png" #Flashing Трусики
                    show screen hermione_main
                    with d3
                    her "Последний был даже довольно умен и неплохо воспитан."
                    her "............................"
                    her "................"
                    hide screen hermione_main
                    with d3
                    $ h_xpos=370 #Defines position of the Hermione's full length sprite. (Default 370). 140 - center.
                    $ h_body = "03_hp/13_hermione_main/body_34.png" #Flashing Трусики
                    show screen hermione_main
                    with d3
                    her "Но это не поменяет моего мнения насчет \"Слизерина\", сэр."
                    m "Мне это и не нужно, Мисс Грейнджер."
                    her "Я делаю это для своего факультета!"
                    hide screen hermione_main
                    with d3
                    $ h_xpos=370 #Defines position of the Hermione's full length sprite. (Default 370). 140 - center.
                    $ h_body = "03_hp/13_hermione_main/body_32.png" #Flashing Трусики
                    show screen hermione_main
                    with d3
                    her "Для гордого \"Гриффиндора\"!"
                    m "Ладно, ладно, успокойся, девочка."
                    hide screen hermione_main
                    with d3
                    $ h_xpos=370 #Defines position of the Hermione's full length sprite. (Default 370). 140 - center.
                    $ h_body = "03_hp/13_hermione_main/body_74.png" #Flashing Трусики
                    show screen hermione_main
                    with d3

            elif whoring >= 6: # LEVEL 03 and higher.
                if one_out_of_three == 1: ### EVENT (A)
                    play music "music/Chipper Doodle v2.mp3" fadein 1 fadeout 1 # HERMIONE'S THEME.
                    hide screen hermione_main
                    with d3
                    $ h_xpos=370 #Defines position of the Hermione's full length sprite. (Default 370). 140 - center.
                    $ h_body = "03_hp/13_hermione_main/body_75.png" #Flashing Трусики
                    show screen hermione_main
                    with d3
                    her "Одиннадцать мальчиков, сэр!"
                    m "Одиннадцать? Really? Ваш личный рекдорд, Мисс Грейнджер."
                    hide screen hermione_main
                    with d3
                    $ h_xpos=370 #Defines position of the Hermione's full length sprite. (Default 370). 140 - center.
                    $ h_body = "03_hp/13_hermione_main/body_74.png" #Flashing Трусики
                    show screen hermione_main
                    with d3
                    her "Да."
                    hide screen hermione_main
                    with d3
                    $ h_xpos=370 #Defines position of the Hermione's full length sprite. (Default 370). 140 - center.
                    $ h_body = "03_hp/13_hermione_main/body_68.png" #Flashing Трусики
                    show screen hermione_main
                    with d3
                    her "Так, посмотрим..."
                    her "Сначала эти два красавчика..."
                    hide screen hermione_main
                    with d3
                    $ h_xpos=370 #Defines position of the Hermione's full length sprite. (Default 370). 140 - center.
                    $ h_body = "03_hp/13_hermione_main/body_64.png" #Flashing Трусики
                    show screen hermione_main
                    with d3
                    her "Потом несколько неловких слов с еще одним парнем."
                    hide screen hermione_main
                    with d3
                    $ h_xpos=370 #Defines position of the Hermione's full length sprite. (Default 370). 140 - center.
                    $ h_body = "03_hp/13_hermione_main/body_68.png" #Flashing Трусики
                    show screen hermione_main
                    with d3
                    her "После этого был еще один парень..."
                    hide screen hermione_main
                    with d3
                    $ h_xpos=370 #Defines position of the Hermione's full length sprite. (Default 370). 140 - center.
                    $ h_body = "03_hp/13_hermione_main/body_73.png" #Flashing Трусики
                    show screen hermione_main
                    with d3
                    her "Потом еще три парня..."
                    hide screen hermione_main
                    with d3
                    $ h_xpos=370 #Defines position of the Hermione's full length sprite. (Default 370). 140 - center.
                    $ h_body = "03_hp/13_hermione_main/body_74.png" #Flashing Трусики
                    show screen hermione_main
                    with d3
                    her "Потом еще один, по моему..."
                    hide screen hermione_main
                    with d3
                    $ h_xpos=370 #Defines position of the Hermione's full length sprite. (Default 370). 140 - center.
                    $ h_body = "03_hp/13_hermione_main/body_75.png" #Flashing Трусики
                    show screen hermione_main
                    with d3
                    her "И последний мальчик проводил меня до вашей башни, сэр..."
                    m "Так, одиннадцать?"
                    m "Вы действительно начинаете нравится этим \"Слизеринским\" парням, ага?"
                    hide screen hermione_main
                    with d3
                    $ h_xpos=370 #Defines position of the Hermione's full length sprite. (Default 370). 140 - center.
                    $ h_body = "03_hp/13_hermione_main/body_74.png" #Flashing Трусики
                    show screen hermione_main
                    with d3
                    her "Похоже на то..."
                    hide screen hermione_main
                    with d3
                    $ h_xpos=370 #Defines position of the Hermione's full length sprite. (Default 370). 140 - center.
                    $ h_body = "03_hp/13_hermione_main/body_73.png" #Flashing Трусики
                    show screen hermione_main
                    with d3
                    her "Ну, не все из них были обходительны со мной по началу..."
                    hide screen hermione_main
                    with d3
                    $ h_xpos=370 #Defines position of the Hermione's full length sprite. (Default 370). 140 - center.
                    $ h_body = "03_hp/13_hermione_main/body_64.png" #Flashing Трусики
                    show screen hermione_main
                    with d3
                    her "Но я пытаюсь их немного \"приручить\"."
                    m "Приручить?"
                    hide screen hermione_main
                    with d3
                    $ h_xpos=370 #Defines position of the Hermione's full length sprite. (Default 370). 140 - center.
                    $ h_body = "03_hp/13_hermione_main/body_74.png" #Flashing Трусики
                    show screen hermione_main
                    with d3
                    her "Да... Каждый раз, когда кто-то из них произносит мое имя..."
                    her "Я просто пытаюсь проглотить свою гордость и улыбнуться в ответ."
                    m "Хм..."
                    m "Например, если кто-то назовет тебя \"шлюхой\" ты просто улыбнешься в ответ?"
                    hide screen hermione_main
                    with d3
                    $ h_xpos=370 #Defines position of the Hermione's full length sprite. (Default 370). 140 - center.
                    $ h_body = "03_hp/13_hermione_main/body_34.png" #Flashing Трусики
                    show screen hermione_main
                    with d3
                    her "Ну, да..."
                    m "Отлично, уверен, что вы отлично справились."
                    m "Прекрасная работа, Мисс Грейнджер."
                    hide screen hermione_main
                    with d3
                    $ h_xpos=370 #Defines position of the Hermione's full length sprite. (Default 370). 140 - center.
                    $ h_body = "03_hp/13_hermione_main/body_68.png" #Flashing Трусики
                    show screen hermione_main
                    with d3
                    
                elif one_out_of_three == 2: ### EVENT (B)
                    play music "music/Chipper Doodle v2.mp3" fadein 1 fadeout 1 # HERMIONE'S THEME.
                    hide screen hermione_main
                    with d3
                    $ h_xpos=370 #Defines position of the Hermione's full length sprite. (Default 370). 140 - center.
                    $ h_body = "03_hp/13_hermione_main/body_75.png" #Flashing Трусики
                    show screen hermione_main
                    with d3
                    her "Два свидания, семь очень приятных разговоров..."
                    hide screen hermione_main
                    with d3
                    $ h_xpos=370 #Defines position of the Hermione's full length sprite. (Default 370). 140 - center.
                    $ h_body = "03_hp/13_hermione_main/body_68.png" #Flashing Трусики
                    show screen hermione_main
                    with d3
                    her "И один даже поцеловал меня..."
                    m "Впечатляет, Мисс Грейнджер."
                    hide screen hermione_main
                    with d3
                    $ h_xpos=370 #Defines position of the Hermione's full length sprite. (Default 370). 140 - center.
                    $ h_body = "03_hp/13_hermione_main/body_74.png" #Flashing Трусики
                    show screen hermione_main
                    with d3
                    her "Я тоже так думаю, сэр. Спасибо."
                    hide screen hermione_main
                    with d3
                    $ h_xpos=370 #Defines position of the Hermione's full length sprite. (Default 370). 140 - center.
                    $ h_body = "03_hp/13_hermione_main/body_75.png" #Flashing Трусики
                    show screen hermione_main
                    with d3
                    her "Ох, еще этот первокурсник..."
                    her "Я пыталась заигрывать с ним, но все закончилось простым разговором..."
                    her "Он называл меня \"Мисс Гермиона\"..."
                    her "Это так очаровательно..."
                    m "Ну, я не посылал вас приставать к детям, Мисс Грейнджер."
                    hide screen hermione_main
                    with d3
                    $ h_xpos=370 #Defines position of the Hermione's full length sprite. (Default 370). 140 - center.
                    $ h_body = "03_hp/13_hermione_main/body_66.png" #Flashing Трусики
                    show screen hermione_main
                    with d3
                    her "I didn't haras--"
                    hide screen hermione_main
                    with d3
                    $ h_xpos=370 #Defines position of the Hermione's full length sprite. (Default 370). 140 - center.
                    $ h_body = "03_hp/13_hermione_main/body_34.png" #Flashing Трусики
                    show screen hermione_main
                    with d3
                    her "Сэр! Семь подкатов и два свидания ведь неплохо, не так ли?"
                    m "Ох, конечно."
                    hide screen hermione_main
                    with d3
                    $ h_xpos=370 #Defines position of the Hermione's full length sprite. (Default 370). 140 - center.
                    $ h_body = "03_hp/13_hermione_main/body_30.png" #Flashing Трусики
                    show screen hermione_main
                    with d3
                    her "Теперь я хотела бы получить свою плату..."
                    hide screen hermione_main
                    with d3
                    $ h_xpos=370 #Defines position of the Hermione's full length sprite. (Default 370). 140 - center.
                    $ h_body = "03_hp/13_hermione_main/body_33.png" #Flashing Трусики
                    show screen hermione_main
                    with d3
                    
                elif one_out_of_three == 3: ### EVENT (C)
                    stop music fadeout 1.0
                    hide screen hermione_main
                    with d3
                    $ h_xpos=370 #Defines position of the Hermione's full length sprite. (Default 370). 140 - center.
                    $ h_body = "03_hp/13_hermione_main/body_33.png" #Flashing Трусики
                    show screen hermione_main
                    with d3
                    her "Сэр, простите, но..."
                    play music "music/Chipper Doodle v2.mp3" fadein 1 fadeout 1 # HERMIONE'S THEME.
                    hide screen hermione_main
                    with d3
                    $ h_xpos=370 #Defines position of the Hermione's full length sprite. (Default 370). 140 - center.
                    $ h_body = "03_hp/13_hermione_main/body_47.png" #Flashing Трусики
                    show screen hermione_main
                    with d3
                    her "Я ненавижу этих \"Слизеринских\" ублюдков, сэр!"
                    m "Расскажи, что произошло."
                    hide screen hermione_main
                    with d3
                    $ h_xpos=370 #Defines position of the Hermione's full length sprite. (Default 370). 140 - center.
                    $ h_body = "03_hp/13_hermione_main/body_69.png" #Flashing Трусики
                    show screen hermione_main
                    with d3
                    her "я не хочу говорить об этом..."
                    m "Расскажи мне что произошло, девочка!"
                    hide screen hermione_main
                    with d3
                    $ h_xpos=370 #Defines position of the Hermione's full length sprite. (Default 370). 140 - center.
                    $ h_body = "03_hp/13_hermione_main/body_76.png" #Flashing Трусики
                    show screen hermione_main
                    with d3
                    her "Я не хочу говорить об этом, сэр."
                    hide screen hermione_main
                    with d3
                    $ h_xpos=370 #Defines position of the Hermione's full length sprite. (Default 370). 140 - center.
                    $ h_body = "03_hp/13_hermione_main/body_69.png" #Flashing Трусики
                    show screen hermione_main
                    with d3
                    her "Пожалуйста, не заставляйте меня..."
                    menu:
                        "\"Ладно. На сегодня достаточно.\"":
                            hide screen hermione_main
                            with d3
                            $ h_xpos=370 #Defines position of the Hermione's full length sprite. (Default 370). 140 - center.
                            $ h_body = "03_hp/13_hermione_main/body_33.png" #Flashing Трусики
                            show screen hermione_main
                            with d3
                            her "Спасибо, сэр."
                            m "Значит сегодня ты провалила задание?"
                            hide screen hermione_main
                            with d3
                            $ h_xpos=370 #Defines position of the Hermione's full length sprite. (Default 370). 140 - center.
                            $ h_body = "03_hp/13_hermione_main/body_34.png" #Flashing Трусики
                            show screen hermione_main
                            with d3
                            her "О, совсем напротив, сэр."
                            play music "music/(Orchestral) Playful Tension by Shadow16nh.mp3" fadein 1 fadeout 1 # SEX THEME.
                            her "Один из мальчиков \"Слизерина\" взял меня в общую комнату..."
                            hide screen hermione_main
                            with d3
                            $ h_xpos=370 #Defines position of the Hermione's full length sprite. (Default 370). 140 - center.
                            $ h_body = "03_hp/13_hermione_main/body_03.png" #Flashing Трусики
                            show screen hermione_main
                            with d3
                            her "Там была как минимум дужина парней..."
                            hide screen hermione_main
                            with d3
                            $ h_xpos=370 #Defines position of the Hermione's full length sprite. (Default 370). 140 - center.
                            $ h_body = "03_hp/13_hermione_main/body_04.png" #Flashing Трусики
                            show screen hermione_main
                            with d3
                            her "Все они знали, кто я ..."
                            her "Я была в центре внимания..."
                            hide screen hermione_main
                            with d3
                            $ h_xpos=370 #Defines position of the Hermione's full length sprite. (Default 370). 140 - center.
                            $ h_body = "03_hp/13_hermione_main/body_78.png" #Flashing Трусики
                            show screen hermione_main
                            with d3
                            her "И я чувствовала себя превосходно..."
                            play music "music/Chipper Doodle v2.mp3" fadein 1 fadeout 1 # HERMIONE'S THEME.
                            hide screen hermione_main
                            with d3
                            $ h_xpos=370 #Defines position of the Hermione's full length sprite. (Default 370). 140 - center.
                            $ h_body = "03_hp/13_hermione_main/body_66.png" #Flashing Трусики
                            show screen hermione_main
                            with d3
                            her "И накинулись на кучку этих \"Слизеринских\" шлюх..."
                            m "И?"
                            hide screen hermione_main
                            with d3
                            $ h_xpos=370 #Defines position of the Hermione's full length sprite. (Default 370). 140 - center.
                            $ h_body = "03_hp/13_hermione_main/body_69.png" #Flashing Трусики
                            show screen hermione_main
                            with d3
                            her "Ну, они делали и говорили всякое такое..."
                            her "Не важно, я все равно ушла..."
                            m "Понятно..."
                            m "Ну, думаю вы заслужили свои очки, Мисс Грейнджер."
                            hide screen hermione_main
                            with d3
                            $ h_xpos=370 #Defines position of the Hermione's full length sprite. (Default 370). 140 - center.
                            $ h_body = "03_hp/13_hermione_main/body_74.png" #Flashing Трусики
                            show screen hermione_main
                            with d3

                        "\"Рассказывай или потеряешь свои очки!\"":
                            $ mad +=10
                            hide screen hermione_main
                            with d3
                            $ h_xpos=370 #Defines position of the Hermione's full length sprite. (Default 370). 140 - center.
                            $ h_body = "03_hp/13_hermione_main/body_66.png" #Flashing Трусики
                            show screen hermione_main
                            with d3
                            her "Сэр, пожалуйста, я не хочу об этом говорить."
                            m "Никто не заставляет вас, Мисс Грейнджер."
                            m "Ты можешь уйти."
                            hide screen hermione_main
                            with d3
                            $ h_xpos=370 #Defines position of the Hermione's full length sprite. (Default 370). 140 - center.
                            $ h_body = "03_hp/13_hermione_main/body_47.png" #Flashing Трусики
                            show screen hermione_main
                            with d3
                            her "{size=-4}(Упрямый старик!){/size}"
                            jump could_not_flirt
                            
                            
    
    $ gryffindor +=5
    m "\"Гриффиндор\" получает 5 очков."
    her "Спасибо, сэр."
    
    hide screen bld1
    hide screen hermione_main
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




    $ request_02_b_points += 1
    $ request_02_b = False 
    $ hermione_sleeping = True
    
    $ p_level_02_active = True #When turns TRUE public favors of level 02 become available. 
    
    if whoring <= 2:
        $ whoring +=1
        
    call music_block
    
    return        
    
label could_not_flirt: #Sent here when choose "Задание провалено! Ты не получишь очки!" (Hermione is leaving without getting any points).
    hide screen blkfade
    hide screen bld1
    hide screen hermione_main
    hide screen blktone 
    hide screen chair_02
    hide screen hermione_02
    hide screen jerking_off_01 #Hermione topless. Genie jerking off.
    hide screen ctc
    show screen genie
    with d3

    $ walk_xpos=400 #Animation of walking chibi. (From)
    $ walk_xpos2=610 #Coordinates of it's movement. (To)
    $ hermione_speed = 02.0 #The speed of moving the walking animation across the screen.
    show screen hermione_walk_01_f 
    pause 2
    hide screen hermione_walk_01_f 
    $ renpy.play('sounds/door.mp3') #Sound of a door opening.
    with Dissolve(.3)
    
    $ request_02_b_points += 1
    $ request_02_b = False 
    
    call music_block
    
    if daytime:
        $ hermione_takes_classes = True
    else:
        $ hermione_sleeping = True
    return
    

#################################################################################################################################
### LEVEL 02 ####################################################################################################################    
###################REQUEST_02_c (LEVEL02) ### FLIRT WITH TEACHERS ###
label new_request_02_c:
    
    hide screen hermione_main 
    with d3
    m "{size=-4}(Заставить ее флиртовать с учителем?){/size}"
    $ menu_x = 0.5 #Default position of the menu (0.5). Version B is $ menu_x = 0.2
    menu:
        "\"(Да, давай попробуем!)\"":
            pass
        "\"(Не сейчас.)\"":
            jump new_personal_request

    m "Мисс Грейнджер, я хочу, чтобы вы флиртовали с учителем."
    if whoring <=2 or request_02_b_points <= 1: # request_02_b_points - counts how many times Hermione was sent to flirt with boys. 
        jump too_much
   

    if request_02_c_points == 0 and whoring <= 8: ### up to LEVEL 03
    ### LEVEL 03 ### <===============================================================FIRST EVENT!
        $ h_xpos=140 #Defines position of the Hermione's full length sprite. (Default 370). 140 - center.
        $ h_body = "03_hp/13_hermione_main/body_01.png" #Flashing Трусики
        show screen hermione_main
        with d3
        her "Я постараюсь, сэр!"
        hide screen hermione_main
        with d3
        $ h_xpos=140 #Defines position of the Hermione's full length sprite. (Default 370). 140 - center.
        $ h_body = "03_hp/13_hermione_main/body_02.png" #Flashing Трусики
        show screen hermione_main
        with d3
        her "Я рада, что вы наконец предложили это мне!"
        m "Да?"
        hide screen hermione_main
        with d3
        $ h_xpos=140 #Defines position of the Hermione's full length sprite. (Default 370). 140 - center.
        $ h_body = "03_hp/13_hermione_main/body_07.png" #Flashing Трусики
        show screen hermione_main
        with d3
        her "Вы наконец-то решили устроить проверку учителям, которые обменивают очки на услуги, не так ли?" 
        hide screen hermione_main
        with d3
        $ h_xpos=140 #Defines position of the Hermione's full length sprite. (Default 370). 140 - center.
        $ h_body = "03_hp/13_hermione_main/body_16.png" #Flashing Трусики
        show screen hermione_main
        with d3
        her "Для меня большая честь выступить в качестве приманки."
        m "Эм... Да, именно этим мы и займемся."
        hide screen hermione_main
        with d3
        $ h_xpos=140 #Defines position of the Hermione's full length sprite. (Default 370). 140 - center.
        $ h_body = "03_hp/13_hermione_main/body_07.png" #Flashing Трусики
        show screen hermione_main
        with d3
        her "Отлично! Вы можете расчитывать на меня!"
    else:
        hide screen hermione_main
        with d3
        $ h_xpos=140 #Defines position of the Hermione's full length sprite. (Default 370). 140 - center.
        $ h_body = "03_hp/13_hermione_main/body_07.png" #Flashing Трусики
        show screen hermione_main
        with d3
        her "Я зайду к вам с подробностями вечером."
        m "Буду ждать..."
    

    
    her "Ну, мне следует идти. Занятия вот-вот начнутся..."
    $ request_02_c = True

    hide screen bld1
    hide screen hermione_main
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
    jump day_main_menu


    
    
label new_request_02_c_complete:  ### FLIRTING WITH TEACHERS COMPLETE ###
    $ walk_xpos=520 #Animation of walking chibi. (From)
    $ walk_xpos2=400 #Coordinates of it's movement. (To)
    $ hermione_speed = 02.0 #The speed of moving the walking animation across the screen.
    $ renpy.play('sounds/door.mp3') #Sound of a door opening.
    show screen hermione_walk_01 
    with d4
    pause 1.7 
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
    her "Добрый вечер, сэр."
    m "Мисс Грейнджер..."
    m "Вы справились с заданием?"
    her "Я сделала, что вы просили, сэр..."
    menu:
        "\"Отлично. Вот твои очки.\"":
            pass
        "\"Теперь поподробнее.\"":
            hide screen hermione_main
            with d3
            m "Скажите, со сколькими учителями вы заигрывали, Мисс Грейнджер?"
            m "Мне нужны подробности."
            show screen blktone
            with d3
    
            if  whoring >= 3 and whoring <= 5: ### LEVEL 02 <===================================================================== EVENT LEVEL 01
                if one_out_of_three == 1: ### EVENT (A)
                    play music "music/Chipper Doodle v2.mp3" fadein 1 fadeout 1 # HERMIONE'S THEME.
                    hide screen hermione_main
                    with d3
                    $ h_xpos=370 #Defines position of the Hermione's full length sprite. (Default 370). 140 - center.
                    $ h_body = "03_hp/13_hermione_main/body_10.png" #Flashing Трусики
                    show screen hermione_main
                    with d3
                    her "Ну, я попыталась заигрывать с профессором Флитвиком..."
                    hide screen hermione_main
                    with d3
                    $ h_xpos=370 #Defines position of the Hermione's full length sprite. (Default 370). 140 - center.
                    $ h_body = "03_hp/13_hermione_main/body_09.png" #Flashing Трусики
                    show screen hermione_main
                    with d3
                    her "Но это не сработало..."
                    hide screen hermione_main
                    with d3
                    $ h_xpos=370 #Defines position of the Hermione's full length sprite. (Default 370). 140 - center.
                    $ h_body = "03_hp/13_hermione_main/body_12.png" #Flashing Трусики
                    show screen hermione_main
                    with d3
                    her ".............................."
                    m "Как замечательно..."
                    m "Это все, что вы сделали сегодня, Мисс Грейнджер?"
                    hide screen hermione_main
                    with d3
                    $ h_xpos=370 #Defines position of the Hermione's full length sprite. (Default 370). 140 - center.
                    $ h_body = "03_hp/13_hermione_main/body_11.png" #Flashing Трусики
                    show screen hermione_main
                    with d3
                    her "Д-да..."
                    her "Но сэр, я знаю \"грязные\" факты о профессоре Флитвике!"
                    her "Всем известно, что из-за его роста..."
                    hide screen hermione_main
                    with d3
                    $ h_xpos=370 #Defines position of the Hermione's full length sprite. (Default 370). 140 - center.
                    $ h_body = "03_hp/13_hermione_main/body_13.png" #Flashing Трусики
                    show screen hermione_main
                    with d3
                    her "Он иногда... Эм..."
                    hide screen hermione_main
                    with d3
                    $ h_xpos=370 #Defines position of the Hermione's full length sprite. (Default 370). 140 - center.
                    $ h_body = "03_hp/13_hermione_main/body_29.png" #Flashing Трусики
                    show screen hermione_main
                    with d3
                    her "Он любит заглядывать под юбки учениц, сэр!"
                    m "Это еще не все?"
                    hide screen hermione_main
                    with d3
                    $ h_xpos=370 #Defines position of the Hermione's full length sprite. (Default 370). 140 - center.
                    $ h_body = "03_hp/13_hermione_main/body_31.png" #Flashing Трусики
                    show screen hermione_main
                    with d3
                    her "Что?"
                    m "Я имею в виду, он нам всем нравится и мы возмущены таким поведением профессора Флик-флика."
                    hide screen hermione_main
                    with d3
                    $ h_xpos=370 #Defines position of the Hermione's full length sprite. (Default 370). 140 - center.
                    $ h_body = "03_hp/13_hermione_main/body_07.png" #Flashing Трусики
                    show screen hermione_main
                    with d3
                    her "Э-э... \"Профессор Флитвик\", сэр."
                    m "Верно. Внесем его в мой \"список непослушных мальчиков\" как я и говорил."
                    hide screen hermione_main
                    with d3
                    $ h_xpos=370 #Defines position of the Hermione's full length sprite. (Default 370). 140 - center.
                    $ h_body = "03_hp/13_hermione_main/body_17.png" #Flashing Трусики
                    show screen hermione_main
                    with d3
                    her "......................"
                    m "Ну, не люблю это признавать, но вы очень плохо выполнили свою работу, Мисс Грейнджер."
                    hide screen hermione_main
                    with d3
                    $ h_xpos=370 #Defines position of the Hermione's full length sprite. (Default 370). 140 - center.
                    $ h_body = "03_hp/13_hermione_main/body_12.png" #Flashing Трусики
                    show screen hermione_main
                    with d3
                    her "................................"
                    menu:
                        "\"Остаетесь без очков!\"":

                            hide screen hermione_main
                            with d3
                            $ h_xpos=140 #Defines position of the Hermione's full length sprite. (Default 370). 140 - center.
                            $ h_body = "03_hp/13_hermione_main/body_28.png" #Flashing Трусики
                            show screen hermione_main
                            with d3
                            her "но профессор, я сделала все что смогла!"
                            hide screen hermione_main
                            with d3
                            $ h_xpos=140 #Defines position of the Hermione's full length sprite. (Default 370). 140 - center.
                            $ h_body = "03_hp/13_hermione_main/body_67.png" #Flashing Трусики
                            show screen hermione_main
                            with d3
                            her "Вы не можете отказаться от своего обещания!"
                            m "......................."
                            hide screen hermione_main
                            with d3
                            $ h_xpos=140 #Defines position of the Hermione's full length sprite. (Default 370). 140 - center.
                            $ h_body = "03_hp/13_hermione_main/body_32.png" #Flashing Трусики
                            show screen hermione_main
                            with d3
                            stop music fadeout 1.0
                            her "Это не подобает директору школы!"
                            m "Вы провалились, Мисс Грейнджер."
                            hide screen hermione_main
                            with d3
                            $ h_xpos=140 #Defines position of the Hermione's full length sprite. (Default 370). 140 - center.
                            $ h_body = "03_hp/13_hermione_main/body_76.png" #Flashing Трусики
                            show screen hermione_main
                            with d3
                            her "Арх!"
                            $ mad += 18
                            call music_block
                            jump could_not_flirt_02
                        "\"Хотя, вы заслужили эти очки.\"":
                            hide screen hermione_main
                            with d3
                            $ h_xpos=140 #Defines position of the Hermione's full length sprite. (Default 370). 140 - center.
                            $ h_body = "03_hp/13_hermione_main/body_28.png" #Flashing Трусики
                            show screen hermione_main
                            with d3
                            her "Правда?"
                            hide screen hermione_main
                            with d3
                            $ h_xpos=140 #Defines position of the Hermione's full length sprite. (Default 370). 140 - center.
                            $ h_body = "03_hp/13_hermione_main/body_75.png" #Flashing Трусики
                            show screen hermione_main
                            with d3
                            her "Огромное спасибо, профессор!"
                           
                elif one_out_of_three == 2: ### EVENT (B)
                    hide screen hermione_main
                    with d3
                    $ h_xpos=140 #Defines position of the Hermione's full length sprite. (Default 370). 140 - center.
                    $ h_body = "03_hp/13_hermione_main/body_13.png" #Flashing Трусики
                    show screen hermione_main
                    with d3
                    her ".................."
                    her "............................"
                    m "Мисс Грейнджер?"
                    hide screen hermione_main
                    with d3
                    $ h_xpos=140 #Defines position of the Hermione's full length sprite. (Default 370). 140 - center.
                    $ h_body = "03_hp/13_hermione_main/body_11.png" #Flashing Трусики
                    show screen hermione_main
                    with d3
                    her "Да, профессор... Мне жаль... Просто я..."
                    hide screen hermione_main
                    with d3
                    $ h_xpos=140 #Defines position of the Hermione's full length sprite. (Default 370). 140 - center.
                    $ h_body = "03_hp/13_hermione_main/body_13.png" #Flashing Трусики
                    show screen hermione_main
                    with d3
                    her "............"
                    m "Ты сделала то, что я просил?"
                    hide screen hermione_main
                    with d3
                    $ h_xpos=140 #Defines position of the Hermione's full length sprite. (Default 370). 140 - center.
                    $ h_body = "03_hp/13_hermione_main/body_14.png" #Flashing Трусики
                    show screen hermione_main
                    with d3
                    her "Я пыталась, сэр. Правда..."
                    m "С кем ты пыталась заигрывать?"
                    hide screen hermione_main
                    with d3
                    $ h_xpos=140 #Defines position of the Hermione's full length sprite. (Default 370). 140 - center.
                    $ h_body = "03_hp/13_hermione_main/body_13.png" #Flashing Трусики
                    show screen hermione_main
                    with d3
                    her "........."
                    hide screen hermione_main
                    with d3
                    $ h_xpos=140 #Defines position of the Hermione's full length sprite. (Default 370). 140 - center.
                    $ h_body = "03_hp/13_hermione_main/body_12.png" #Flashing Трусики
                    show screen hermione_main
                    with d3
                    her "Профессор Снейп, сэр."
                    play music "music/Chipper Doodle v2.mp3" fadein 1 fadeout 1 # HERMIONE'S THEME.
                    m "Северус? Интересно..."
                    m "Как прошло?"
                    hide screen hermione_main
                    with d3
                    $ h_xpos=140 #Defines position of the Hermione's full length sprite. (Default 370). 140 - center.
                    $ h_body = "03_hp/13_hermione_main/body_07.png" #Flashing Трусики
                    show screen hermione_main
                    with d3
                    her "Ужасно сэр..."
                    her "Простите, но я правда ненавижу Профессора Снейпа, сэр!"
                    m "И конечно же я уверен, что это взаимно..."
                    m "Расскажи, что произошло."
                    hide screen hermione_main
                    with d3
                    $ h_xpos=140 #Defines position of the Hermione's full length sprite. (Default 370). 140 - center.
                    $ h_body = "03_hp/13_hermione_main/body_09.png" #Flashing Трусики
                    show screen hermione_main
                    with d3
                    her "Ничего не произошло, сэр. Он просто рассмеялся мне в лицо..."
                    hide screen hermione_main
                    with d3
                    $ h_xpos=140 #Defines position of the Hermione's full length sprite. (Default 370). 140 - center.
                    $ h_body = "03_hp/13_hermione_main/body_29.png" #Flashing Трусики
                    show screen hermione_main
                    with d3
                    her "У меня не так уж много женского очарования, но я пыталась быть милой..."
                    hide screen hermione_main
                    with d3
                    $ h_xpos=140 #Defines position of the Hermione's full length sprite. (Default 370). 140 - center.
                    $ h_body = "03_hp/13_hermione_main/body_30.png" #Flashing Трусики
                    show screen hermione_main
                    with d3
                    her "И он просто начал смеяться прямо мне в лицо!"
                    hide screen hermione_main
                    with d3
                    $ h_xpos=140 #Defines position of the Hermione's full length sprite. (Default 370). 140 - center.
                    $ h_body = "03_hp/13_hermione_main/body_34.png" #Flashing Трусики
                    show screen hermione_main
                    with d3
                    her "...действительно страшно видеть как Профессор Снейп смеется..."
                    her "........"
                    her "Я ужасно заигрываю, простите, сэр..."
                    hide screen hermione_main
                    with d3
                    $ h_xpos=140 #Defines position of the Hermione's full length sprite. (Default 370). 140 - center.
                    $ h_body = "03_hp/13_hermione_main/body_47.png" #Flashing Трусики
                    show screen hermione_main
                    with d3
                    her "Но я знаю, что Профессор Снейп тоже проворачивает \"грязные\" делишки!"
                    her "Если бы вы отправили кого-то другого к нему, то все было бы иначе!"
                    m "Кого-то другого?"
                    hide screen hermione_main
                    with d3
                    $ h_xpos=140 #Defines position of the Hermione's full length sprite. (Default 370). 140 - center.
                    $ h_body = "03_hp/13_hermione_main/body_44.png" #Flashing Трусики
                    show screen hermione_main
                    with d3
                    her "Да! Кого-то опытного..."
                    her "Кого-то..."
                    her "Кого-то, хм..."
                    m "Распущенного?"
                    hide screen hermione_main
                    with d3
                    $ h_xpos=140 #Defines position of the Hermione's full length sprite. (Default 370). 140 - center.
                    $ h_body = "03_hp/13_hermione_main/body_66.png" #Flashing Трусики
                    show screen hermione_main
                    with d3
                    her "Да, я полагаю..."
                    m "Не сдавайтесь, Мисс Грейнджер. Мы сделаем из тебя шлюху э-э--"
                    m "То есть женщину!"
                    hide screen hermione_main
                    with d3
                    $ h_xpos=140 #Defines position of the Hermione's full length sprite. (Default 370). 140 - center.
                    $ h_body = "03_hp/13_hermione_main/body_79.png" #Flashing Трусики
                    show screen hermione_main
                    with d3
                    her "..................."
                    menu:
                        "\"...Но ты не получишь очки в этот раз\"":
                            hide screen hermione_main
                            with d3
                            $ h_xpos=140 #Defines position of the Hermione's full length sprite. (Default 370). 140 - center.
                            $ h_body = "03_hp/13_hermione_main/body_12.png" #Flashing Трусики
                            show screen hermione_main
                            with d3
                            her "Но я старалась..."
                            hide screen hermione_main
                            with d3
                            $ h_xpos=140 #Defines position of the Hermione's full length sprite. (Default 370). 140 - center.
                            $ h_body = "03_hp/13_hermione_main/body_34.png" #Flashing Трусики
                            show screen hermione_main
                            with d3
                            her "И чувствую себя очень униженно..."
                            hide screen hermione_main
                            with d3
                            $ h_xpos=140 #Defines position of the Hermione's full length sprite. (Default 370). 140 - center.
                            $ h_body = "03_hp/13_hermione_main/body_33.png" #Flashing Трусики
                            show screen hermione_main
                            with d3
                            her "Но я понимаю и не буду с вами спорить..."
                            call music_block
                            jump could_not_flirt_02
                        "\"Ты заслужила очки, девочка.\"":
                            pass
                elif one_out_of_three == 3: ### EVENT (C)
                    stop music fadeout 1.0
                    hide screen hermione_main
                    with d3
                    $ h_xpos=370 #Defines position of the Hermione's full length sprite. (Default 370). 140 - center.
                    $ h_body = "03_hp/13_hermione_main/body_10.png" #Flashing Трусики
                    show screen hermione_main
                    with d3
                    her "Я пыталась флиртовать с профессором Филчем, сэр..."
                    m "Понятно. {size=-5}(Понятия не имею кто это.){/size}"
                    hide screen hermione_main
                    with d3
                    $ h_xpos=140 #Defines position of the Hermione's full length sprite. (Default 370). 140 - center.
                    $ h_body = "03_hp/13_hermione_main/body_11.png" #Flashing Трусики
                    show screen hermione_main
                    with d3
                    play music "music/Chipper Doodle v2.mp3" fadein 1 fadeout 1 # HERMIONE'S THEME.
                    her "Да, знаю, технически он не учитель..."
                    m "А?"
                    hide screen hermione_main
                    with d3
                    $ h_xpos=140 #Defines position of the Hermione's full length sprite. (Default 370). 140 - center.
                    $ h_body = "03_hp/13_hermione_main/body_01.png" #Flashing Трусики
                    show screen hermione_main
                    with d3
                    her "Но он является частью персонала школы..."
                    her "И мы нашли общий язык с ним!"
                    her "Он на удивление милый."
                    her "Но я не знаю ничего о его \"грязных\" делах, сэр."
                    translators "Filtch - мистер Филч. Filth - грязь."
                    m "Ага... Мистер Гряз{size=+7}ик{/size} исключен из списка."
                    hide screen hermione_main
                    with d3
                    $ h_xpos=140 #Defines position of the Hermione's full length sprite. (Default 370). 140 - center.
                    $ h_body = "03_hp/13_hermione_main/body_07.png" #Flashing Трусики
                    show screen hermione_main
                    with d3
                    her "\"Мистер Филч\", сэр..."
                    m "А я что сказал?"
                    
                    
            elif whoring >= 6 and whoring <= 8: ### LEVEL 03 <=======================================================================================EVENT LEVEL 02
                if one_out_of_three == 1: ### EVENT (A)
                    stop music fadeout 1.0
                    hide screen hermione_main
                    with d3
                    $ h_xpos=140 #Defines position of the Hermione's full length sprite. (Default 370). 140 - center.
                    $ h_body = "03_hp/13_hermione_main/body_10.png" #Flashing Трусики
                    show screen hermione_main
                    with d3
                    her "Ну, профессор Слагхорн пригласил меня к себе..."
                    her "Профессор просто пригласил меня на чашечку чая..."
                    hide screen hermione_main
                    with d3
                    $ h_xpos=140 #Defines position of the Hermione's full length sprite. (Default 370). 140 - center.
                    $ h_body = "03_hp/13_hermione_main/body_16.png" #Flashing Трусики
                    show screen hermione_main
                    with d3
                    play music "music/Chipper Doodle v2.mp3" fadein 1 fadeout 1 # HERMIONE'S THEME.
                    her "Там было несколько девочек..."
                    her "Но все из них были сильно младше меня..."
                    hide screen hermione_main
                    with d3
                    $ h_xpos=140 #Defines position of the Hermione's full length sprite. (Default 370). 140 - center.
                    $ h_body = "03_hp/13_hermione_main/body_17.png" #Flashing Трусики
                    show screen hermione_main
                    with d3
                    her "Почти каждая из них была первокурсницей..."
                    hide screen hermione_main
                    with d3
                    $ h_xpos=140 #Defines position of the Hermione's full length sprite. (Default 370). 140 - center.
                    $ h_body = "03_hp/13_hermione_main/body_16.png" #Flashing Трусики
                    show screen hermione_main
                    with d3
                    her "Пы пили чай и ели печеньки..."
                    her "Все было довольно безобидно..."
                    m "Ты флиртовала с кем-то или нет?"
                    her "Флиртовала..."
                    hide screen hermione_main
                    with d3
                    $ h_xpos=140 #Defines position of the Hermione's full length sprite. (Default 370). 140 - center.
                    $ h_body = "03_hp/13_hermione_main/body_17.png" #Flashing Трусики
                    show screen hermione_main
                    with d3
                    her "Ну, то есть, я пытался..."
                    her "Профессор Слагхорн, кажется, более заинтересован в молодых девочках..."
                    m "Вы будто ревнуете его, Мисс Грейнджер."
                    hide screen hermione_main
                    with d3
                    $ h_xpos=140 #Defines position of the Hermione's full length sprite. (Default 370). 140 - center.
                    $ h_body = "03_hp/13_hermione_main/body_18.png" #Flashing Трусики
                    show screen hermione_main
                    with d3
                    her "Что?!"
                    hide screen hermione_main
                    with d3
                    $ h_xpos=140 #Defines position of the Hermione's full length sprite. (Default 370). 140 - center.
                    $ h_body = "03_hp/13_hermione_main/body_69.png" #Flashing Трусики
                    show screen hermione_main
                    with d3
                    her "Это нелепо!"
                    m "Вот ваши очки..."
                    her "...................."
          
                elif one_out_of_three == 2: ### EVENT (B)
                    play music "music/Chipper Doodle v2.mp3" fadein 1 fadeout 1 # HERMIONE'S THEME.
                    hide screen hermione_main
                    with d3
                    $ h_xpos=140 #Defines position of the Hermione's full length sprite. (Default 370). 140 - center.
                    $ h_body = "03_hp/13_hermione_main/body_80.png" #Flashing Трусики
                    show screen hermione_main
                    with d3
                    her "Это был удивительный день, сэр!"
                    m "Ну же, расскажите, Мисс Грейнджер..."
                    hide screen hermione_main
                    with d3
                    $ h_xpos=140 #Defines position of the Hermione's full length sprite. (Default 370). 140 - center.
                    $ h_body = "03_hp/13_hermione_main/body_68.png" #Flashing Трусики
                    show screen hermione_main
                    with d3
                    her "У меня были занятия у профессора Локонса..."
                    her "сэр Локонс он такой милый и умный..."
                    hide screen hermione_main
                    with d3
                    $ h_xpos=140 #Defines position of the Hermione's full length sprite. (Default 370). 140 - center.
                    $ h_body = "03_hp/13_hermione_main/body_78.png" #Flashing Трусики
                    show screen hermione_main
                    with d3
                    her "И идеальный..."
                    m "Избавьте меня от вашей школьной влюбленности, Мисс Грейнджер."
                    hide screen hermione_main
                    with d3
                    $ h_xpos=140 #Defines position of the Hermione's full length sprite. (Default 370). 140 - center.
                    $ h_body = "03_hp/13_hermione_main/body_80.png" #Flashing Трусики
                    show screen hermione_main
                    with d3
                    her "сэр Lockhart такой любезный, что дал мне свой автограф..."
                    m "Как мило с его стороны."
                    hide screen hermione_main
                    with d3
                    $ h_xpos=140 #Defines position of the Hermione's full length sprite. (Default 370). 140 - center.
                    $ h_body = "03_hp/13_hermione_main/body_68.png" #Flashing Трусики
                    show screen hermione_main
                    with d3
                    her "Да, не могу дождаться, как покажу его девочкам!"
                    m "Хм.. Могу я увидеть его?"
                    hide screen hermione_main
                    with d3
                    $ h_xpos=140 #Defines position of the Hermione's full length sprite. (Default 370). 140 - center.
                    $ h_body = "03_hp/13_hermione_main/body_45.png" #Flashing Трусики
                    show screen hermione_main
                    with d3
                    her "Сэр?"
                    m "Автограф, девочка. Могу я его увидеть?"
                    hide screen hermione_main
                    with d3
                    $ h_xpos=140 #Defines position of the Hermione's full length sprite. (Default 370). 140 - center.
                    $ h_body = "03_hp/13_hermione_main/body_44.png" #Flashing Трусики
                    show screen hermione_main
                    with d3
                    her "Ну... Эм... Он в весьма тайной зоне, сэр."
                    m "Что? Ну, следовательно у профессора Локоноса есть какие-то \"грязные\" делишки!"
                    hide screen hermione_main
                    with d3
                    $ h_xpos=140 #Defines position of the Hermione's full length sprite. (Default 370). 140 - center.
                    $ h_body = "03_hp/13_hermione_main/body_69.png" #Flashing Трусики
                    show screen hermione_main
                    with d3
                    her "Это профессор Локонос, сэр..."
                    her "И... Эм..."
                    her "Ну, это не {size=+5}настолько{/size} укромное место..."
                    m "Покажи это мне!"
                    hide screen hermione_main
                    with d3
                    $ h_xpos=140 #Defines position of the Hermione's full length sprite. (Default 370). 140 - center.
                    $ h_body = "03_hp/13_hermione_main/body_66.png" #Flashing Трусики
                    show screen hermione_main
                    with d3
                    her "Нет, сэр! Это было бы неуместно!"
                    menu: 
                        "{size=-3}\"Профессор Локонос вылетит из школы в ближайшее время!\"{/size}":
                            hide screen hermione_main
                            with d3
                            $ h_xpos=140 #Defines position of the Hermione's full length sprite. (Default 370). 140 - center.
                            $ h_body = "03_hp/13_hermione_main/body_72.png" #Flashing Трусики
                            show screen hermione_main
                            with d3
                            her "Из-за меня?"
                            hide screen hermione_main
                            with d3
                            $ h_xpos=140 #Defines position of the Hermione's full length sprite. (Default 370). 140 - center.
                            $ h_body = "03_hp/13_hermione_main/body_67.png" #Flashing Трусики
                            show screen hermione_main
                            with d3
                            her "Сэр, пожалуйста!"
                            m "Покажи мне!"
                            hide screen hermione_main
                            with d3
                            $ h_xpos=140 #Defines position of the Hermione's full length sprite. (Default 370). 140 - center.
                            $ h_body = "03_hp/13_hermione_main/body_32.png" #Flashing Трусики
                            show screen hermione_main
                            with d3
                            her "Нет, мне стыдно!"
                            menu:
                                "\"Ладно. Вот твои очки.\"":
                                    hide screen hermione_main
                                    with d3
                                    $ h_xpos=140 #Defines position of the Hermione's full length sprite. (Default 370). 140 - center.
                                    $ h_body = "03_hp/13_hermione_main/body_74.png" #Flashing Трусики
                                    show screen hermione_main
                                    with d3
                                    her "Спасибо за понимание, сэр."
                                "\"Покажи мне или я не получишь ничего!\"":
                                    hide screen hermione_main
                                    with d3
                                    $ h_xpos=140 #Defines position of the Hermione's full length sprite. (Default 370). 140 - center.
                                    $ h_body = "03_hp/13_hermione_main/body_72.png" #Flashing Трусики
                                    show screen hermione_main
                                    with d3
                                    her "Что?!"
                                    hide screen hermione_main
                                    with d3
                                    $ h_xpos=140 #Defines position of the Hermione's full length sprite. (Default 370). 140 - center.
                                    $ h_body = "03_hp/13_hermione_main/body_73.png" #Flashing Трусики
                                    show screen hermione_main
                                    with d3
                                    her "..............."
                                    hide screen hermione_main
                                    with d3
                                    $ h_xpos=140 #Defines position of the Hermione's full length sprite. (Default 370). 140 - center.
                                    $ h_body = "03_hp/13_hermione_main/body_29.png" #Flashing Трусики
                                    show screen hermione_main
                                    with d3
                                    her ".................."
                                    hide screen hermione_main
                                    with d3
                                    $ h_xpos=140 #Defines position of the Hermione's full length sprite. (Default 370). 140 - center.
                                    $ h_body = "03_hp/13_hermione_main/body_47.png" #Flashing Трусики
                                    show screen hermione_main
                                    with d3
                                    her "Ну, ладно, но только, чтобы очистить имя моего кумира..."
                                    hide screen hermione_main
                                    with d3
                                    show screen blktone8
                                    with d5
                                    her_12 "Вот...."
                                    m "Хм..."
                                    hide screen blktone8 
                                    with d5
                                    $ only_upper = True #Skirt lifted.
                                    $ autograph = True #Autograph shown.
                                    $ h_xpos=140 #Defines position of the Hermione's full length sprite. (Default 370). 140 - center.
                                    $ h_body = "03_hp/13_hermione_main/body_51.png" #Flashing Трусики
                                    show screen hermione_main
                                    hide screen ctc
                                    show screen ctc
                                    with d3
                                    pause
                                    hide screen hermione_main
                                    with d3
                                    $ h_body = "03_hp/13_hermione_main/body_50.png" #Flashing Трусики
                                    show screen hermione_main
                                    with d3
                                    her "Как вы понимаете, профессор Локонос очень смелый и воплощает в себе все чистое."
                                    pause
                                    m "Что мне теперь делать?"
                                    her "Можете не беспокоиться об этом, сэр."
                                    her "Он не один из \"пошлых\" учителей."
                                    m "Ах, да какое мне дело..."
                                    hide screen hermione_main
                                    with d3     
                                    $ h_body = "03_hp/13_hermione_main/body_51.png" #Flashing Трусики
                                    show screen hermione_main
                                    with d3
                                    her "............?"
                                    hide screen hermione_main 
                                    with d3
                                    $ only_upper = False #Skirt lifted.
                                    $ autograph = False #Autograph shown.
                                    $ h_xpos=140 #Defines position of the Hermione's full length sprite. (Default 370). 140 - center.
                                    $ h_body = "03_hp/13_hermione_main/body_47.png" #Flashing Трусики
                                    show screen hermione_main
                                    with fade
                                    pause
                                    hide screen ctc
                                    $ mad += 18
                        "\"Ладно... Вот твои очки.\"":
                            hide screen hermione_main
                            with d3
                            $ h_xpos=140 #Defines position of the Hermione's full length sprite. (Default 370). 140 - center.
                            $ h_body = "03_hp/13_hermione_main/body_74.png" #Flashing Трусики
                            show screen hermione_main
                            with d3
                            her "Спасибо за понимание, профессор."
                            
                elif one_out_of_three == 3: ### EVENT (C)
                    play music "music/Chipper Doodle v2.mp3" fadein 1 fadeout 1 # HERMIONE'S THEME.
                    hide screen hermione_main
                    with d3
                    $ h_xpos=370 #Defines position of the Hermione's full length sprite. (Default 370). 140 - center.
                    $ h_body = "03_hp/13_hermione_main/body_15.png" #Flashing Трусики
                    show screen hermione_main
                    with d3
                    her "Ну, сегодня я некоторое время заигрывала с мистером Филчем."
                    hide screen hermione_main
                    with d3
                    $ h_xpos=370 #Defines position of the Hermione's full length sprite. (Default 370). 140 - center.
                    $ h_body = "03_hp/13_hermione_main/body_16.png" #Flashing Трусики
                    show screen hermione_main
                    with d3
                    her "Ну, мистел Филч очень начитанный и обладает манерами."
                    m "........"
                    hide screen hermione_main
                    with d3
                    $ h_xpos=370 #Defines position of the Hermione's full length sprite. (Default 370). 140 - center.
                    $ h_body = "03_hp/13_hermione_main/body_13.png" #Flashing Трусики
                    show screen hermione_main
                    with d3
                    her "Не думаю, что кто-то знает его таким..."
                    her "Не думаю, что кто-то знает мистера Филча так, как я."
                    hide screen hermione_main
                    with d3
                    $ h_xpos=370 #Defines position of the Hermione's full length sprite. (Default 370). 140 - center.
                    $ h_body = "03_hp/13_hermione_main/body_06.png" #Flashing Трусики
                    show screen hermione_main
                    with d3
                    her "Я чувствую, что со мной он очень открыт, сэр."
                    m "Ладно..."
                    m "Этот, мистер Фли{size=+7}нт{/size}--"
                    hide screen hermione_main
                    with d3
                    $ h_xpos=370 #Defines position of the Hermione's full length sprite. (Default 370). 140 - center.
                    $ h_body = "03_hp/13_hermione_main/body_04.png" #Flashing Трусики
                    show screen hermione_main
                    with d3
                    her "Мистер Филч, сэр."
                    m "Да, не важно... Он учитель?"
                    her "Мистер Филч? Учитель? Нет, сэр..."
                    hide screen hermione_main
                    with d3
                    $ h_xpos=370 #Defines position of the Hermione's full length sprite. (Default 370). 140 - center.
                    $ h_body = "03_hp/13_hermione_main/body_06.png" #Flashing Трусики
                    show screen hermione_main
                    with d3
                    her "Он смотритель..."
                    m "Смотритель...?"
                    m "Ты имеешь в виду дворник?"
                    hide screen hermione_main
                    with d3
                    $ h_xpos=370 #Defines position of the Hermione's full length sprite. (Default 370). 140 - center.
                    $ h_body = "03_hp/13_hermione_main/body_10.png" #Flashing Трусики
                    show screen hermione_main
                    with d3
                    her "Ну..."
                    m "Мисс Грейнджер, я не посылал вас очаровывать дворников!"
                    hide screen hermione_main
                    with d3
                    $ h_xpos=370 #Defines position of the Hermione's full length sprite. (Default 370). 140 - center.
                    $ h_body = "03_hp/13_hermione_main/body_14.png" #Flashing Трусики
                    show screen hermione_main
                    with d3
                    her "Но мистер Филч является частью школьного персонала, сэр!"
                    menu:
                        "\"Просто бери свои очки и уходи!\"":
                            hide screen hermione_main
                            with d3
                            $ h_xpos=370 #Defines position of the Hermione's full length sprite. (Default 370). 140 - center.
                            $ h_body = "03_hp/13_hermione_main/body_03.png" #Flashing Трусики
                            show screen hermione_main
                            with d3
                            her "........................."
                        "\"Задание провалено! Ты не получишь очки!\"":
                            $ mad +=15
                            hide screen hermione_main
                            with d3
                            $ h_xpos=370 #Defines position of the Hermione's full length sprite. (Default 370). 140 - center.
                            $ h_body = "03_hp/13_hermione_main/body_07.png" #Flashing Трусики
                            show screen hermione_main
                            with d3
                            her "Но профессор?"
                            m "Вы провалились, Мисс Грейнджер."
                            hide screen hermione_main
                            with d3
                            $ h_xpos=370 #Defines position of the Hermione's full length sprite. (Default 370). 140 - center.
                            $ h_body = "03_hp/13_hermione_main/body_05.png" #Flashing Трусики
                            show screen hermione_main
                            with d3
                            her "........................................."
                            jump could_not_flirt_02


            elif whoring >= 9: # LEVEL 04 and higher.
                if one_out_of_three == 1: ### EVENT (A) LEVEL04 <============================================================================
                    stop music fadeout 1.0
                    hide screen hermione_main
                    with d3
                    $ h_xpos=370 #Defines position of the Hermione's full length sprite. (Default 370). 140 - center.
                    $ h_body = "03_hp/13_hermione_main/body_33.png" #Flashing Трусики
                    show screen hermione_main
                    with d3
                    her "............................."
                    her "....................................."
                    m "Мисс Грейнджер?"
                    hide screen hermione_main
                    with d3
                    $ h_xpos=370 #Defines position of the Hermione's full length sprite. (Default 370). 140 - center.
                    $ h_body = "03_hp/13_hermione_main/body_34.png" #Flashing Трусики
                    show screen hermione_main
                    with d3
                    her "Профессор, Я....."
                    m "Что такое? Что произошло?"
                    hide screen hermione_main
                    with d3
                    $ h_xpos=370 #Defines position of the Hermione's full length sprite. (Default 370). 140 - center.
                    $ h_body = "03_hp/13_hermione_main/body_29.png" #Flashing Трусики
                    show screen hermione_main
                    with d3
                    her "Ну..."
                    her "Мистер Филч, сэр..."
                    m "Дворник?"
                    hide screen hermione_main
                    with d3
                    $ h_xpos=370 #Defines position of the Hermione's full length sprite. (Default 370). 140 - center.
                    $ h_body = "03_hp/13_hermione_main/body_31.png" #Flashing Трусики
                    show screen hermione_main
                    with d3
                    her "Я с ним немного флиртовала..."
                    her "И все было отлично сначала..."
                    hide screen hermione_main
                    with d3
                    $ h_xpos=370 #Defines position of the Hermione's full length sprite. (Default 370). 140 - center.
                    $ h_body = "03_hp/13_hermione_main/body_29.png" #Flashing Трусики
                    show screen hermione_main
                    with d3
                    her "......................."
                    m "................?"
                    hide screen hermione_main
                    with d3
                    $ h_xpos=370 #Defines position of the Hermione's full length sprite. (Default 370). 140 - center.
                    $ h_body = "03_hp/13_hermione_main/body_31.png" #Flashing Трусики
                    show screen hermione_main
                    with d3
                    her "И потом..."
                    hide screen hermione_main
                    with d3
                    $ h_xpos=370 #Defines position of the Hermione's full length sprite. (Default 370). 140 - center.
                    $ h_body = "03_hp/13_hermione_main/body_29.png" #Flashing Трусики
                    show screen hermione_main
                    with d3
                    her "Не уверена, должна ли я..."
                    m "Мисс Грейнджер, если вы не хотите говорить, можете уйти."
                    hide screen hermione_main
                    with d3
                    $ h_xpos=370 #Defines position of the Hermione's full length sprite. (Default 370). 140 - center.
                    $ h_body = "03_hp/13_hermione_main/body_32.png" #Flashing Трусики
                    show screen hermione_main
                    with d3
                    play music "music/Chipper Doodle v2.mp3" fadein 1 fadeout 1 # HERMIONE'S THEME.
                    her "Он показал мне свою \"штучку\", сэр!"
                    m "Его что?"
                    hide screen hermione_main
                    with d3
                    $ h_xpos=370 #Defines position of the Hermione's full length sprite. (Default 370). 140 - center.
                    $ h_body = "03_hp/13_hermione_main/body_34.png" #Flashing Трусики
                    show screen hermione_main
                    with d3
                    her "Его... мужское начало, сэр."
                    g9 "Так держать, парень-дворник!"
                    hide screen hermione_main
                    with d3
                    $ h_xpos=370 #Defines position of the Hermione's full length sprite. (Default 370). 140 - center.
                    $ h_body = "03_hp/13_hermione_main/body_72.png" #Flashing Трусики
                    show screen hermione_main
                    with d3
                    her "Что?!"
                    m "*Кхм* То есть это возмутимо!"
                    hide screen hermione_main
                    with d3
                    $ h_xpos=370 #Defines position of the Hermione's full length sprite. (Default 370). 140 - center.
                    $ h_body = "03_hp/13_hermione_main/body_21.png" #Flashing Трусики
                    show screen hermione_main
                    with d3
                    her "Да... Мерзкий, кривой, весь в венах..."
                    m "Избавьте меня от ужасных подробностей, девушка."
                    hide screen hermione_main
                    with d3
                    $ h_xpos=370 #Defines position of the Hermione's full length sprite. (Default 370). 140 - center.
                    $ h_body = "03_hp/13_hermione_main/body_20.png" #Flashing Трусики
                    show screen hermione_main
                    with d3
                    her "Зачем он вообще сделал это?"
                    her "Только что мы говорили, как вдруг..."
                    m "Ну, ваша благородная жертва не должна остаться незамеченной, Мисс Грейнджер!"
                    m "Пятнадцать очков \"Грифф--"
                    hide screen hermione_main
                    with d3
                    $ h_xpos=370 #Defines position of the Hermione's full length sprite. (Default 370). 140 - center.
                    $ h_body = "03_hp/13_hermione_main/body_19.png" #Flashing Трусики
                    show screen hermione_main
                    with d3
                    her "Профессор Дамблдор, пожалуйста подождите."
                    m "А?"
                    hide screen hermione_main
                    with d3
                    $ h_xpos=370 #Defines position of the Hermione's full length sprite. (Default 370). 140 - center.
                    $ h_body = "03_hp/13_hermione_main/body_31.png" #Flashing Трусики
                    show screen hermione_main
                    with d3
                    her "Ну, вы не собираетесь что-то с этим сделать?"
                    m "Ну..."
                    hide screen hermione_main
                    with d3
                    $ h_xpos=370 #Defines position of the Hermione's full length sprite. (Default 370). 140 - center.
                    $ h_body = "03_hp/13_hermione_main/body_47.png" #Flashing Трусики
                    show screen hermione_main
                    with d3
                    her "Что если я не первая жертва..?"
                    her "Какой-нибудь первокур может получить травму на всю жизнь!"
                    m "Действительно может?"
                    hide screen hermione_main
                    with d3
                    $ h_xpos=370 #Defines position of the Hermione's full length sprite. (Default 370). 140 - center.
                    $ h_body = "03_hp/13_hermione_main/body_31.png" #Flashing Трусики
                    show screen hermione_main
                    with d3
                    her "Это значит, что вы примете меры, сэр?"
                    m "Эм... Да, конечно..."
                    m "Занесу его в свой \"список\"..."
                    m "\"Позаботиться о дворнике и его жутко кривом члене.\"..."
                    m "Да, завтра же в первую очередь."
                    hide screen hermione_main
                    with d3
                    $ h_xpos=370 #Defines position of the Hermione's full length sprite. (Default 370). 140 - center.
                    $ h_body = "03_hp/13_hermione_main/body_16.png" #Flashing Трусики
                    show screen hermione_main
                    with d3
                    her "Спасибо сэр."
                    hide screen hermione_main
                    with d3
                    $ h_xpos=370 #Defines position of the Hermione's full length sprite. (Default 370). 140 - center.
                    $ h_body = "03_hp/13_hermione_main/body_75.png" #Flashing Трусики
                    show screen hermione_main
                    with d3
                    her "Могу я получить свои очки?"
    
                elif one_out_of_three == 2: ### EVENT (B)
                    play music "music/Chipper Doodle v2.mp3" fadein 1 fadeout 1 # HERMIONE'S THEME.
                    hide screen hermione_main
                    with d3
                    $ h_xpos=370 #Defines position of the Hermione's full length sprite. (Default 370). 140 - center.
                    $ h_body = "03_hp/13_hermione_main/body_76.png" #Flashing Трусики
                    show screen hermione_main
                    with d3
                    her "Профессор Снейп!"
                    m "Эм... Ага, Я вообще-то Дамблдор вроде как..."
                    hide screen hermione_main
                    with d3
                    
                    g4 "{size=-5}(Стоп, может {size=+7}он{/size} сменил мою маскировку?){/size}"
                    g4 "{size=-5}(Значит, теперь я выгляжу как Профессор Снейп?){/size}"
                    g4 "{size=-5}(Во имя великих песков пустыни! Акабур, тебе следует сдерживать себя!){/size}"
                    a5 "{size=-5}(Нужно было сначала послушать девочку. Блин...){/size}"
                    hide screen hermione_main
                    with d3
                    $ h_xpos=370 #Defines position of the Hermione's full length sprite. (Default 370). 140 - center.
                    $ h_body = "03_hp/13_hermione_main/body_02.png" #Flashing Трусики
                    show screen hermione_main
                    with d3
                    her "Профессор? С кем вы говорили?"
                    m "Эм... Я связался с духами из другого измерения..."
                    hide screen hermione_main
                    with d3
                    $ h_xpos=370 #Defines position of the Hermione's full length sprite. (Default 370). 140 - center.
                    $ h_body = "03_hp/13_hermione_main/body_17.png" #Flashing Трусики
                    show screen hermione_main
                    with d3
                    her ".....??!"
                    hide screen hermione_main
                    with d3
                    a6 "{size=-5}(Придерживайся сценария, придурок!){/size}"
                    g4 "Да, очень раздражительный дух ... Раздражительный и немой!"
                    a6 "{size=-5}(Ты......!){/size}"
                    hide screen hermione_main
                    with d3
                    $ h_xpos=370 #Defines position of the Hermione's full length sprite. (Default 370). 140 - center.
                    $ h_body = "03_hp/13_hermione_main/body_02.png" #Flashing Трусики
                    show screen hermione_main
                    with d3
                    her "Профессор Дамблдор, пожалуйста, выслушайте меня!"
                    m "Да, да, девочка. Я слушаю."
                    hide screen hermione_main
                    with d3
                    $ h_xpos=370 #Defines position of the Hermione's full length sprite. (Default 370). 140 - center.
                    $ h_body = "03_hp/13_hermione_main/body_04.png" #Flashing Трусики
                    show screen hermione_main
                    with d3
                    her "Я только нашла подтверждение тому, что профессор Снейп коррумпирован и имеет \"грязные\" дела, сэр!"
                    m "Расскажи, что произошло."
                    hide screen hermione_main
                    with d3
                    $ h_xpos=370 #Defines position of the Hermione's full length sprite. (Default 370). 140 - center.
                    $ h_body = "03_hp/13_hermione_main/body_02.png" #Flashing Трусики
                    show screen hermione_main
                    with d3
                    her "ну, сегодня во время занятий..."
                    her "Я делала все возможное, чтобы привлечь внимание профессора Снейпа..."
                    her "Я \"мечтательно\" пялилась на него..."
                    her "И следила за его членом..."
                    m "Ты..."
                    m "Смотрела в сторону его члена?"
                    hide screen hermione_main
                    with d3
                    $ h_xpos=370 #Defines position of the Hermione's full length sprite. (Default 370). 140 - center.
                    $ h_body = "03_hp/13_hermione_main/body_04.png" #Flashing Трусики
                    show screen hermione_main
                    with d3
                    her "Да... Имею в виду, когда вы смотрите туда и хотите кое-что от него..."
                    m "Откуда ты знаешь о таком?"
                    hide screen hermione_main
                    with d3
                    $ h_xpos=370 #Defines position of the Hermione's full length sprite. (Default 370). 140 - center.
                    $ h_body = "03_hp/13_hermione_main/body_10.png" #Flashing Трусики
                    show screen hermione_main
                    with d3
                    her "Женские журналы..."
                    hide screen hermione_main
                    with d3
                    $ h_xpos=370 #Defines position of the Hermione's full length sprite. (Default 370). 140 - center.
                    $ h_body = "03_hp/13_hermione_main/body_07.png" #Flashing Трусики
                    show screen hermione_main
                    with d3
                    her "Ну, не важно, это сработало, сэр."
                    hide screen hermione_main
                    with d3
                    $ h_xpos=370 #Defines position of the Hermione's full length sprite. (Default 370). 140 - center.
                    $ h_body = "03_hp/13_hermione_main/body_47.png" #Flashing Трусики
                    show screen hermione_main
                    with d3
                    her "Когда занятия закончились, Профессор Снейп схватил меня за попку, сэр!"
                    m "Дьявол!"
                    m "Тебе понравилось, не так ли?"
                    hide screen hermione_main
                    with d3
                    $ h_xpos=370 #Defines position of the Hermione's full length sprite. (Default 370). 140 - center.
                    $ h_body = "03_hp/13_hermione_main/body_30.png" #Flashing Трусики
                    show screen hermione_main
                    with d3
                    her "Сэр, я делаю это только для--"
                    m "Только во имя чести \"Гриффиндора\"! и все такое. Да, помню."
                    m "Вот твои очки."
                    hide screen hermione_main
                    with d3
                    $ h_xpos=370 #Defines position of the Hermione's full length sprite. (Default 370). 140 - center.
                    $ h_body = "03_hp/13_hermione_main/body_66.png" #Flashing Трусики
                    show screen hermione_main
                    with d3
  
                elif one_out_of_three == 3: ### EVENT (C)
                    stop music fadeout 1.0
                    hide screen hermione_main
                    with d3
                    $ h_xpos=370 #Defines position of the Hermione's full length sprite. (Default 370). 140 - center.
                    $ h_body = "03_hp/13_hermione_main/body_09.png" #Flashing Трусики
                    show screen hermione_main
                    with d3
                    her "Профессор Локонос!"
                    m "Ага! Добавим его в \"список непослушных\"!"
                    hide screen hermione_main
                    with d3
                    $ h_xpos=370 #Defines position of the Hermione's full length sprite. (Default 370). 140 - center.
                    $ h_body = "03_hp/13_hermione_main/body_11.png" #Flashing Трусики
                    show screen hermione_main
                    with d3
                    her "Нет, сэр, это не то..."
                    hide screen hermione_main
                    with d3
                    $ h_xpos=370 #Defines position of the Hermione's full length sprite. (Default 370). 140 - center.
                    $ h_body = "03_hp/13_hermione_main/body_12.png" #Flashing Трусики
                    show screen hermione_main
                    with d3
                    her "Или..."
                    her "Я не уверена..."
                    hide screen hermione_main
                    with d3
                    $ h_xpos=370 #Defines position of the Hermione's full length sprite. (Default 370). 140 - center.
                    $ h_body = "03_hp/13_hermione_main/body_11.png" #Flashing Трусики
                    show screen hermione_main
                    with d3
                    her "Раньше я его обожала..."
                    hide screen hermione_main
                    with d3
                    $ h_xpos=370 #Defines position of the Hermione's full length sprite. (Default 370). 140 - center.
                    $ h_body = "03_hp/13_hermione_main/body_13.png" #Flashing Трусики
                    show screen hermione_main
                    with d3
                    her "Но он..."
                    her "Он просто..."
                    hide screen hermione_main
                    with d3
                    $ h_xpos=370 #Defines position of the Hermione's full length sprite. (Default 370). 140 - center.
                    $ h_body = "03_hp/13_hermione_main/body_20.png" #Flashing Трусики
                    show screen hermione_main
                    with d3
                    her "Как это возможно?"
                    her "Я не могу поверить в это..."
                    hide screen hermione_main
                    with d3
                    play music "music/(Orchestral) Playful Tension by Shadow16nh.mp3" fadein 1 fadeout 1 # SEX THEME.
                    m "{size=-4}(Арх! Ожидание убивает меня!){/size}" 
                    m "{size=-4}(Может он заставил ее сосать?){/size}"
                    m "{size=-4}(Или может изнасилова?){/size}"
                    g4 "Что такое, девочка? Говори!"
                    hide screen hermione_main
                    with d3
                    $ h_xpos=370 #Defines position of the Hermione's full length sprite. (Default 370). 140 - center.
                    $ h_body = "03_hp/13_hermione_main/body_14.png" #Flashing Трусики
                    show screen hermione_main
                    with d3
                    her "А?"
                    m "Что профессор Локонос сделал с тобой?"
                    hide screen hermione_main
                    with d3
                    $ h_xpos=370 #Defines position of the Hermione's full length sprite. (Default 370). 140 - center.
                    $ h_body = "03_hp/13_hermione_main/body_13.png" #Flashing Трусики
                    show screen hermione_main
                    with d3
                    her "Эм... Ничего, сэр..."
                    m "Ничего?!"
                    hide screen hermione_main
                    with d3
                    $ h_xpos=370 #Defines position of the Hermione's full length sprite. (Default 370). 140 - center.
                    $ h_body = "03_hp/13_hermione_main/body_11.png" #Flashing Трусики
                    show screen hermione_main
                    with d3
                    her "Да, я конечно загнала его в угол сегодня..."
                    hide screen hermione_main
                    with d3
                    $ h_xpos=370 #Defines position of the Hermione's full length sprite. (Default 370). 140 - center.
                    $ h_body = "03_hp/13_hermione_main/body_31.png" #Flashing Трусики
                    show screen hermione_main
                    with d3
                    her "И еще могла выглядеть доступной для него..."
                    m "Серьезно?"
                    hide screen hermione_main
                    with d3
                    $ h_xpos=370 #Defines position of the Hermione's full length sprite. (Default 370). 140 - center.
                    $ h_body = "03_hp/13_hermione_main/body_34.png" #Flashing Трусики
                    show screen hermione_main
                    with d3
                    her "Да... Не уверена, что он хотел от меня, сэр..."
                    m "Ну же, Мисс Грейнджер!"
                    hide screen hermione_main
                    with d3
                    $ h_xpos=370 #Defines position of the Hermione's full length sprite. (Default 370). 140 - center.
                    $ h_body = "03_hp/13_hermione_main/body_32.png" #Flashing Трусики
                    show screen hermione_main
                    with d3
                    her "Выслушайте меня сначала, пожалуйста!"
                    m "Мои извенения. Продолжай."
                    hide screen hermione_main
                    with d3
                    $ h_xpos=370 #Defines position of the Hermione's full length sprite. (Default 370). 140 - center.
                    $ h_body = "03_hp/13_hermione_main/body_14.png" #Flashing Трусики
                    show screen hermione_main
                    with d3
                    her "Ну, обычно профессор Локонос ведет себя как джентельмен..."
                    her "И... и я просто хотела очистить его имя от всех этих подозрений раз и навсегда..."
                    hide screen hermione_main
                    with d3
                    $ h_xpos=370 #Defines position of the Hermione's full length sprite. (Default 370). 140 - center.
                    $ h_body = "03_hp/13_hermione_main/body_29.png" #Flashing Трусики
                    show screen hermione_main
                    with d3
                    her "..............."
                    her "Ну, профессор Локонос не отверг меня..."
                    m "Ты меня убиваешь, девочка!"
                    m "Он не отверг тебя, он не изнасиловал тебя..."
                    m "Тогда что произошло?"
                    hide screen hermione_main
                    with d3
                    $ h_xpos=370 #Defines position of the Hermione's full length sprite. (Default 370). 140 - center.
                    $ h_body = "03_hp/13_hermione_main/body_33.png" #Flashing Трусики
                    show screen hermione_main
                    with d3
                    her "............."
                    hide screen hermione_main
                    with d3
                    $ h_xpos=370 #Defines position of the Hermione's full length sprite. (Default 370). 140 - center.
                    $ h_body = "03_hp/13_hermione_main/body_34.png" #Flashing Трусики
                    show screen hermione_main
                    with d3
                    play music "music/Chipper Doodle v2.mp3" fadein 1 fadeout 1 # HERMIONE'S THEME.
                    her "Я заставила его плакать, сэр..."
                    m "..............стоп.......что?"
                    hide screen hermione_main
                    with d3
                    $ h_xpos=370 #Defines position of the Hermione's full length sprite. (Default 370). 140 - center.
                    $ h_body = "03_hp/13_hermione_main/body_28.png" #Flashing Трусики
                    show screen hermione_main
                    with d3
                    her "Он озадаченно посмотрел и затем начал рыдать..."
                    her "Он смотрел на меня так, как будто боится, сэр."
                    hide screen hermione_main
                    with d3
                    $ h_xpos=370 #Defines position of the Hermione's full length sprite. (Default 370). 140 - center.
                    $ h_body = "03_hp/13_hermione_main/body_29.png" #Flashing Трусики
                    show screen hermione_main
                    with d3
                    her "Я думаю..."
                    her "Я думаю, мистер Локонос боится женщин..."
                    m "Боится женщин?"
                    m "Что это может значить?"
                    hide screen hermione_main
                    with d3
                    $ h_xpos=370 #Defines position of the Hermione's full length sprite. (Default 370). 140 - center.
                    $ h_body = "03_hp/13_hermione_main/body_34.png" #Flashing Трусики
                    show screen hermione_main
                    with d3
                    her "То, что ему нравятся мальчики, сэр?"
                    m "Ох..."
                    hide screen hermione_main
                    with d3
                    $ h_xpos=370 #Defines position of the Hermione's full length sprite. (Default 370). 140 - center.
                    $ h_body = "03_hp/13_hermione_main/body_44.png" #Flashing Трусики
                    show screen hermione_main
                    with d3
                    her "............"
                    m "..........."
                    m "Ну, почти уверен, что этот опыт нанес вам травму, Мисс Грейнджер."
                    hide screen hermione_main
                    with d3
                    $ h_xpos=370 #Defines position of the Hermione's full length sprite. (Default 370). 140 - center.
                    $ h_body = "03_hp/13_hermione_main/body_31.png" #Flashing Трусики
                    show screen hermione_main
                    with d3
                    her "Вроде, сэр..."
                    m "Ну, надеюсь эти очки поднимут тебе настроение.."
                    
                            
    
    $ gryffindor +=15
    m "\"Гриффиндор\" получает 15 очков!"
    her "Спасибо, сэр."
    
    hide screen bld1
    hide screen hermione_main
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

    call music_block

    $ p_level_03_active = True #When turns TRUE public favors of level 03 become available. 

    
    if whoring <= 5:  # (if whoring >= 3 and whoring <= 5) - LEVEL 02
        $ whoring +=1

    $ request_02_c_points += 1 #Leveling up the event.
    $ request_02_c = False 
    $ hermione_sleeping = True

    return    
    
label could_not_flirt_02: #Sent here when chose "Задание провалено! Ты не получишь очки!"
    hide screen bld1
    hide screen hermione_main
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
    
    $ request_02_b_points += 1
    $ request_02_b = False 
    $ hermione_sleeping = True
    
    return   
    
    
    
    
    
    
    
    
    
    
    
    
    
################### REQUEST_03 (Level 02) (Available during daytime only). "Give me your Трусики" ###############################
label new_request_03: #(Whoring = 3 - 5)
    if whoring <=2:
        jump too_much
    hide screen hermione_main
    with d3
    m "{size=-4}(Попросить ее отдать мне трусики и пойти на занятия?){/size}"
    $ menu_x = 0.5 #Default position of the menu. Version B is $ menu_x = 0.2
    menu:
        "\"(Да, давай попробуем!)\"":
            pass
        "\"(Не сейчас.)\"":
            jump new_personal_request
    m "Мисс Грейнджер?"
    show screen hermione_main
    with d3
    her "Я слушаю, сэр."
    m "Мне нужны ваши трусики..."   
    hide screen hermione_main
    with d3
    $ menu_x = 0.5 #Menu is moved to the left side.
    $ h_xpos=120 #Defines position of the Hermione's full length sprite. Left: 370 Center: 120
    $ h_ypos=0
    $ h_body = "03_hp/13_hermione_main/body_01.png" #Sprite of Hermione's upper body.
    show screen blktone 
    show screen ctc
    show screen hermione_main
    with Dissolve(.3)
    pause
    
    
    
    if request_03 == 0 and whoring <= 5: #First time this event taking place. and LEVEL 02.   <===================================== ONE TIME EVENT.
        stop music fadeout 10.0
        $ new_request_03_01 = True # HEARTS.
        $ request_03 += 1
        hide screen hermione_main
        with d3
        $ h_xpos=120 #Defines position of the Hermione's full length sprite.
        $ h_body = "03_hp/13_hermione_main/body_11.png" #Flashing Трусики
        show screen hermione_main
        with d3
        her "Ч-что?"
        her "Мои... Трусики...?"
        her "Профессор Дамблдор, это..."
        m "Это моя сегодняшняя просьба, Мисс Грейнджер..."
        m "Если вам не интересно, можете уходить."
        her "Нет, мне интересно. Да... просто это..."
        her "Вам нужны мои...."
        play music "music/Chipper Doodle v2.mp3" fadein 1 fadeout 1 # HERMIONE'S THEME.
        hide screen hermione_main
        with d3
        $ h_xpos=120 #Defines position of the Hermione's full length sprite.
        $ h_body = "03_hp/13_hermione_main/body_47.png" #Flashing Трусики
        show screen hermione_main
        with d3
        her "...Трусики, сэр?"
        m "Именно..."
        hide screen hermione_main
        with d3
        $ h_xpos=120 #Defines position of the Hermione's full length sprite.
        $ h_body = "03_hp/13_hermione_main/body_66.png" #Flashing Трусики
        show screen hermione_main
        with d3
        her "Могу ли я узнать, что вы планируете с ними делать...?"
        m "Эм...Я провожу исследования..."
        her "Но это немного странно, не находите?"
        m "Но вам ведь не нравится, что девушки из \"Слизерина\"..."
        m "Оказывают услуги за очки для факультета, не так ли, Мисс Грейнджер?"
        hide screen hermione_main
        with d3
        $ h_xpos=120 #Defines position of the Hermione's full length sprite.
        $ h_body = "03_hp/13_hermione_main/body_47.png" #Flashing Трусики
        show screen hermione_main
        with d3
        her "Верно!"
        hide screen hermione_main
        with d3
        $ h_xpos=120 #Defines position of the Hermione's full length sprite.
        $ h_body = "03_hp/13_hermione_main/body_12.png" #Flashing Трусики
        show screen hermione_main
        with d3
        her "(Эти \"Слизеринские\" шлюхи потеряли все достоинство.)"
        hide screen hermione_main
        with d3
        m "Ну, тогда давайте!"
        hide screen hermione_main
        with d3
        $ h_xpos=120 #Defines position of the Hermione's full length sprite.
        $ h_body = "03_hp/13_hermione_main/body_66.png" #Flashing Трусики
        show screen hermione_main
        with d3
        her "А?"
        m "Победите их в их собственной игре!"
        hide screen hermione_main
        with d3
        $ h_xpos=120 #Defines position of the Hermione's full length sprite.
        $ h_body = "03_hp/13_hermione_main/body_14.png" #Flashing Трусики
        show screen hermione_main
        with d3
        her "Что?"
        m "Да! Не дайте \"Слизерину\" вырваться в лидеры..."
        m "Но я не могу сделать этого, даже, чтобы победить в игре!"
        hide screen hermione_main
        with d3
        $ h_xpos=120 #Defines position of the Hermione's full length sprite.
        $ h_body = "03_hp/13_hermione_main/body_11.png" #Flashing Трусики
        show screen hermione_main
        with d3
        her "Профессор..."
        m "Директор не может иметь любимчиков, но вы знаете, что я думаю о \"Гриффиндоре\"..."
        m "Я могу просто дать вам очков, но это разрушит всю систему..."
        show screen blktone8
        hide screen hermione_main
        with d3
        ">Внезапно Гермиона протягивает вам руку..."
        ">Вы замечаете, что она сжимает какую-то ткань в кулаке..."
        #">Her Трусики? You can't help but wonder when she managed to take them off..."
        m "??!"
        ">Вы получили трусики Гермионы..."
        hide screen blktone8
        with d3
        hide screen hermione_main
        with d3
        $ h_xpos=120 #Defines position of the Hermione's full length sprite.
        $ h_body = "03_hp/13_hermione_main/body_67.png" #Flashing Трусики
        show screen hermione_main
        with d3
        
        her "Просто возьмите из, сэр..."
        m "Что? Как ты успела?"
        her "Ваша речь была такой трогательной..."
        her "Вы совершенно правы, сэр! Я должна победить их в этой игре."
        her "Мои занятия вот-вот начнутся. Мне лучше пойти..."
        hide screen hermione_main
        with d3
        $ h_xpos=370 #Right: 370 Center: 120
        $ h_body = "03_hp/13_hermione_main/body_23.png" #Flashing Трусики
        show screen hermione_main
        with d3
        her "..........."
        hide screen hermione_main
        with d3
        $ h_xpos=370 #Right: 370 Center: 120
        $ h_body = "03_hp/13_hermione_main/body_29.png" #Flashing Трусики
        show screen hermione_main
        with d3
        her "...Я надеюсь, что никто не заметит, что у меня нет белья..."
        hide screen hermione_main
        with d3
        $ h_xpos=370 #Right: 370 Center: 120
        $ h_body = "03_hp/13_hermione_main/body_31.png" #Flashing Трусики
        show screen hermione_main
        with d3
        her "Ох, я вернусь за ними вечером, сэр."
        m "Конечно. Твои трусики будут лежать на моем столе и ждать тебя..."
        hide screen hermione_main
        with d3
        $ h_xpos=370 #Right: 370 Center: 120
        $ h_body = "03_hp/13_hermione_main/body_34.png" #Flashing Трусики
        show screen hermione_main
        with d3
        her "............."
        jump request_03_ends

    else: #<========================================================================================== FIRST EVENT!
        if request_03 >= 1:
            her "Снова, сэр?"
            m "Да, снова..."
        her "Вот..."
        if whoring >= 12: #LEVEL 05
            hide screen hermione_main
            with d3
            ">Гермиона достает свои трусики из кармана..."
            m "Что?"
            hide screen hermione_main
            with d3
            $ h_xpos=120 #Defines position of the Hermione's full length sprite.
            $ h_body = "03_hp/13_hermione_main/body_45.png" #Flashing Трусики
            show screen hermione_main
            with d3
            her "Да, у меня было ощущение, что вы их попросите сегодня, сэр."
            m "Было ощущение?"
            hide screen hermione_main
            with d3
            $ h_xpos=120 #Defines position of the Hermione's full length sprite.
            $ h_body = "03_hp/13_hermione_main/body_68.png" #Flashing Трусики
            show screen hermione_main
            with d3
            her "Ну, если быть честной, то я теперь не всегда их надеваю..."
        else:
            hide screen hermione_main
            with d3
            ">Гермиона снимает трусики и отдает их вам..."
        hide screen hermione_main
        with d3
        ">Получены трусики Гермионы."
        $ h_body = "03_hp/13_hermione_main/body_15.png" #Flashing Трусики
        show screen hermione_main
        with d3
        her "Ну, мне стоит идти на занятия. Они вот-вот начнутся..."

 
        
    label request_03_ends:
    $ request_03 = True #True when Hermione has no Трусики on.
    if whoring <= 5:
        $ whoring +=1
        
    hide screen bld1
    hide screen hermione_main
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
    
    $ h_xpos=370 #Defines position of the Hermione's full length sprite.
    $ h_ypos=0
    $ h_body = "03_hp/13_hermione_main/body_01.png" #Sprite of Hermione's upper body.
    show screen hermione_main
    show screen hermione_02
    with Dissolve(.3)
    
    "Добрый вечер, сэр..."
    play music "music/Chipper Doodle v2.mp3" fadein 1 fadeout 1 # HERMIONE'S THEME.
    menu:
        "\"Вот твои трусики.\"":
            if have_cum_soaced_panties:
                jump Трусики_soaked_in_cum
            else:
                her "Спасибо, сэр."
                her "И моя оплата?"
                m "Конечно."
        "\"Как прошел ваш день, Мисс Грейнджер?\"":
            if  whoring <= 5: #LEVEL 02. EVENT LEVEL: 01
                $ new_request_03_01 = True # HEARTS.
                hide screen hermione_main
                with d3
                $ h_xpos=120 #Defines position of the Hermione's full length sprite. center: 120. Right: 370.
                $ h_body = "03_hp/13_hermione_main/body_15.png" #Flashing Трусики
                show screen hermione_main
                with d3
                her "Ох..."
                her "Довольно обычно..."
                hide screen hermione_main
                with d3
                $ h_xpos=120 #Defines position of the Hermione's full length sprite.
                $ h_body = "03_hp/13_hermione_main/body_13.png" #Flashing Трусики
                show screen hermione_main
                with d3
                her "Хотя я не уверена, возможно кто-то мог заметить, что я..."
                hide screen hermione_main
                with d3
                $ h_xpos=120 #Defines position of the Hermione's full length sprite. center: 120. Right: 370.
                $ h_body = "03_hp/13_hermione_main/body_29.png" #Flashing Трусики
                show screen hermione_main
                with d3
                her "....."
                hide screen hermione_main
                with d3
                $ h_xpos=120 #Defines position of the Hermione's full length sprite. center: 120. Right: 370.
                $ h_body = "03_hp/13_hermione_main/body_31.png" #Flashing Трусики
                show screen hermione_main
                with d3
                her "Могу я получить свои трусики назад?"
                m "Конечно..."
                hide screen hermione_main
                with d3
                ">Вы отдаете Гермионее ее трусики..."
                if have_cum_soaced_panties:
                    jump Трусики_soaked_in_cum
                else:
                    hide screen hermione_main
                    with d3
                    $ h_xpos=120 #Defines position of the Hermione's full length sprite. center: 120. Right: 370.
                    $ h_body = "03_hp/13_hermione_main/body_31.png" #Flashing Трусики
                    show screen hermione_main
                    with d3
                    her "И мои очки?"
                    m "Да, да..."
            elif whoring >= 6 and whoring <= 8: #LEVEL 03. EVENT LEVEL 02.
                $ new_request_03_02 = True # HEARTS.
                hide screen hermione_main
                with d3
                $ h_xpos=120 #Defines position of the Hermione's full length sprite. center: 120. Right: 370.
                $ h_body = "03_hp/13_hermione_main/body_15.png" #Flashing Трусики
                show screen hermione_main
                with d3
                her "Ох..."
                her "Все как всегда..."
                her "Я провела некоторое время с одноклассниками..."
                her "И у нас было недолго собрание \"ОЗМП\"..."
                translators "Напоминание.\nОЗМП - Общество по Защите Мужских Прав."
                hide screen hermione_main
                with d3
                $ h_xpos=120 #Defines position of the Hermione's full length sprite. center: 120. Right: 370.
                $ h_body = "03_hp/13_hermione_main/body_16.png" #Flashing Трусики
                show screen hermione_main
                with d3
                her "Я произносила небольшую речь на тему \"Почему обменивать очки для факультета за сексуальные услуги это плохо\"..."
                hide screen hermione_main
                with d3
                $ h_xpos=120 #Defines position of the Hermione's full length sprite. center: 120. Right: 370.
                $ h_body = "03_hp/13_hermione_main/body_12.png" #Flashing Трусики
                show screen hermione_main
                with d3
                her "Я чувствовала себя не очень, так как была без белья..."
                menu:
                    "\"Ах ты маленькая лицемерка!\"":
                        $ mad +=5
                        hide screen hermione_main
                        with d3
                        $ h_xpos=120 #Defines position of the Hermione's full length sprite. center: 120. Right: 370.
                        $ h_body = "03_hp/13_hermione_main/body_14.png" #Flashing Трусики
                        show screen hermione_main
                        with d3
                        her "Профессор?"
                        m "Только этим утром ты обменяла свои труски..."
                        m "И несколькими часами позднее произносила речь, осуждая подобное..."
                        #m "What would you call this?"
                        hide screen hermione_main
                        with d3
                        $ h_xpos=120 #Defines position of the Hermione's full length sprite. center: 120. Right: 370.
                        $ h_body = "03_hp/13_hermione_main/body_69.png" #Flashing Трусики
                        show screen hermione_main
                        with d3
                        #her "I know you are right, профессор..."
                        her "(Но нам нужны эти очки...)"
                        hide screen hermione_main
                        with d3
                        $ h_xpos=120 #Defines position of the Hermione's full length sprite. center: 120. Right: 370.
                        $ h_body = "03_hp/13_hermione_main/body_66.png" #Flashing Трусики
                        show screen hermione_main
                        with d3
                        her "Могу я получить свои очки?"
                        m "Что насчет трусиков?"
                        hide screen hermione_main
                        with d3
                        $ h_xpos=120 #Defines position of the Hermione's full length sprite. center: 120. Right: 370.
                        $ h_body = "03_hp/13_hermione_main/body_34.png" #Flashing Трусики
                        show screen hermione_main
                        with d3
                        her "Ох, их, конечно же тоже..." 
                        if have_cum_soaced_panties:
                            jump Трусики_soaked_in_cum
                        else:
                            pass
                    "\"Это для блага...\"":
                        her "Именно!"
                        her "Нам очень нужны эти очки..."
                        her "Это не моя ошибка, это дыры в системе образования..."
                        hide screen hermione_main
                        with d3
                        $ h_xpos=120 #Defines position of the Hermione's full length sprite. center: 120. Right: 370.
                        $ h_body = "03_hp/13_hermione_main/body_16.png" #Flashing Трусики
                        show screen hermione_main
                        with d3
                        her "Я не перестану быть символом праведности для моих сверстников!"
                        hide screen hermione_main
                        with d3
                        $ h_xpos=120 #Defines position of the Hermione's full length sprite. center: 120. Right: 370.
                        $ h_body = "03_hp/13_hermione_main/body_31.png" #Flashing Трусики
                        show screen hermione_main
                        with d3
                        her "Могу я получить свои трусики обратно, пожалуйста?"
                        if have_cum_soaced_panties:
                            jump Трусики_soaked_in_cum
                        else:
                            her "И мои очки."
            elif whoring >= 9: #LEVEL 04. EVENT LEVEL 03.
                $ new_request_03_03 = True # HEARTS.
                hide screen hermione_main
                with d3
                $ h_xpos=120 #Defines position of the Hermione's full length sprite. center: 120. Right: 370.
                $ h_body = "03_hp/13_hermione_main/body_16.png" #Flashing Трусики
                show screen hermione_main
                with d3
                her "Еще один обычный день в Хогвартсе..."
                her "Ничего примечательного..."
                hide screen hermione_main
                with d3
                $ h_xpos=120 #Defines position of the Hermione's full length sprite. center: 120. Right: 370.
                $ h_body = "03_hp/13_hermione_main/body_29.png" #Flashing Трусики
                show screen hermione_main
                with d3
                her "Хотя, должна признаться..."
                her "Я была по странному свободна без белья..."
                her "Хм..."
                hide screen hermione_main
                with d3
                $ h_xpos=120 #Defines position of the Hermione's full length sprite. center: 120. Right: 370.
                $ h_body = "03_hp/13_hermione_main/body_45.png" #Flashing Трусики
                show screen hermione_main
                with d3
                her "Я могу получить свои трусики назад?"
                m "Конечно..."
                hide screen hermione_main
                with d3
                ">Вы отдаете Гермионее ее трусики..."
                if have_cum_soaced_panties:
                    jump Трусики_soaked_in_cum
                else:
                    hide screen hermione_main
                    with d3
                    $ h_xpos=120 #Defines position of the Hermione's full length sprite. center: 120. Right: 370.
                    $ h_body = "03_hp/13_hermione_main/body_45.png" #Flashing Трусики
                    show screen hermione_main
                    with d3
                    her "И мои очки?"
                    m "Да, да..."
    label back_from_panties:
    $ gryffindor +=15
    m "Пятнадцать очков \"Гриффиндору\", мисс Грейнджер. Вы заслужили." 
    her "Спасибо, сэр..."
    m "Можешь идти."
    her "Доброй ночи, сэр."
    #m "Да, доброй ночи..."

    hide screen bld1
    hide screen hermione_main
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



    $ request_03_points += 1 #Leveling up the event.
    $ request_03 = False #When False - you gave her her Трусики back.
    $ hermione_sleeping = True


    play music "music/Music for Manatees.mp3" fadein 1 fadeout 1 # NIGHT MUSIC

    return    
### Трусики SOAKED IN CUM ###
label Трусики_soaked_in_cum:
    $ have_cum_soaced_panties = False #TRUE when you have the Трусики in your possession (before you return them to Hermione).
    
    if whoring >= 3 and whoring <= 5: # LEVEL 02
        hide screen hermione_main
        with d3
        $ h_xpos=120 #Defines position of the Hermione's full length sprite. center: 120. Right: 370.
        $ h_body = "03_hp/13_hermione_main/body_71.png" #Flashing Трусики
        show screen hermione_main
        with d3
        her "Хм....?"
        hide screen hermione_main
        with d3
        $ h_xpos=120 #Defines position of the Hermione's full length sprite. center: 120. Right: 370.
        $ h_body = "03_hp/13_hermione_main/body_05.png" #Flashing Трусики
        show screen hermione_main
        with d3
        her "Сэр? Что это такое?"
        her "Что вы с ними сделали?"
        hide screen hermione_main
        with d3
        $ h_xpos=120 #Defines position of the Hermione's full length sprite. center: 120. Right: 370.
        $ h_body = "03_hp/13_hermione_main/body_07.png" #Flashing Трусики
        show screen hermione_main
        with d3
        her "Они в чем-то скользком..."
        menu:
            "\"Эксперимент провалился.\"":
                hide screen hermione_main
                with d3
                $ h_xpos=120 #Defines position of the Hermione's full length sprite. center: 120. Right: 370.
                $ h_body = "03_hp/13_hermione_main/body_02.png" #Flashing Трусики
                show screen hermione_main
                with d3
                her "Эсперимент прошел плохо, сэр?"
                m "Да...Или, лучше сказать..."
                g9 "\"Эксперимент прошел очень хорошо\"? Хе-хе..."
                hide screen hermione_main
                with d3
                $ h_xpos=120 #Defines position of the Hermione's full length sprite. center: 120. Right: 370.
                $ h_body = "03_hp/13_hermione_main/body_07.png" #Flashing Трусики
                show screen hermione_main
                with d3
                her ".....................?"
                her "Что это был за эксперимент?"
                m "Что? Ох..."
                m "Я провожу пару сверх-секретных исследований."
                m "Я не могу обсуждать его со студентами."
                hide screen hermione_main
                with d3
                $ h_xpos=120 #Defines position of the Hermione's full length sprite. center: 120. Right: 370.
                $ h_body = "03_hp/13_hermione_main/body_05.png" #Flashing Трусики
                show screen hermione_main
                with d3
                her "................................"
            "\"Вы мне дали их такими!\"":
                her "Я уверена, что это не так, сэр!"
                her ".........................."
        hide screen hermione_main
        with d3
        $ h_xpos=120 #Defines position of the Hermione's full length sprite. center: 120. Right: 370.
        $ h_body = "03_hp/13_hermione_main/body_71.png" #Flashing Трусики
        show screen hermione_main
        with d3
        her "Ну, мне потребуется сперва очистить их от всего этого..."
        m "Или ты можешь их надеть прямо сейчас."
        hide screen hermione_main
        with d3
        $ h_xpos=120 #Defines position of the Hermione's full length sprite. center: 120. Right: 370.
        $ h_body = "03_hp/13_hermione_main/body_14.png" #Flashing Трусики
        show screen hermione_main
        with d3
        her "Что?"
        hide screen hermione_main
        with d3
        $ h_xpos=120 #Defines position of the Hermione's full length sprite. center: 120. Right: 370.
        $ h_body = "03_hp/13_hermione_main/body_13.png" #Flashing Трусики
        show screen hermione_main
        with d3
        her "Мне бы этого правда не хотелось, сэр..."
        menu:
            "\"Надень их или потеряешь очки!\"":
                $ mad +=7
                hide screen hermione_main
                with d3
                $ h_xpos=120 #Defines position of the Hermione's full length sprite. center: 120. Right: 370.
                $ h_body = "03_hp/13_hermione_main/body_72.png" #Flashing Трусики
                show screen hermione_main
                with d3
                her "Что?"
                her "Профессор, вы шутите, так?"
                m "Вообще-то нет..."
                hide screen hermione_main
                with d3
                $ h_xpos=120 #Defines position of the Hermione's full length sprite. center: 120. Right: 370.
                $ h_body = "03_hp/13_hermione_main/body_31.png" #Flashing Трусики
                show screen hermione_main
                with d3
                her "Н-но..."
                hide screen hermione_main
                with d3
                $ h_xpos=120 #Defines position of the Hermione's full length sprite. center: 120. Right: 370.
                $ h_body = "03_hp/13_hermione_main/body_33.png" #Flashing Трусики
                show screen hermione_main
                with d3
                her "........................................"
                hide screen hermione_main
                with d3
                $ h_xpos=120 #Defines position of the Hermione's full length sprite. center: 120. Right: 370.
                $ h_body = "03_hp/13_hermione_main/body_47.png" #Flashing Трусики
                show screen hermione_main
                with d3
                her "(ВЫ всегда настаиваете на своем, сэр?)"
                m "Что такое, Мисс Грейнджер?"
                hide screen hermione_main
                with d3
                $ h_xpos=120 #Defines position of the Hermione's full length sprite. center: 120. Right: 370.
                $ h_body = "03_hp/13_hermione_main/body_30.png" #Flashing Трусики
                show screen hermione_main
                with d3
                her "Ничего, сэр."
                her "Верните мне трусики!"
                hide screen hermione_main
                with d3
                show screen blktone8
                with d3
                ">Гермиона нерешительно надевает трусики..."
                ">Несколько капель спермы стекают по ее ноге..."
                ">Гермионе, видимо, очень неудобно..."
                hide screen blktone8
                with d3
                hide screen hermione_main
                with d3
                $ h_xpos=120 #Defines position of the Hermione's full length sprite. center: 120. Right: 370.
                $ h_body = "03_hp/13_hermione_main/body_34.png" #Flashing Трусики
                show screen hermione_main
                with d3
                her "......................"
            "\"Ну, надень их...\"":
                pass
    if whoring >= 6 and whoring <= 8: # LEVEL 03 (SECOND EVENT)
        hide screen hermione_main
        with d3
        $ h_xpos=120 #Defines position of the Hermione's full length sprite. center: 120. Right: 370.
        $ h_body = "03_hp/13_hermione_main/body_71.png" #Flashing Трусики
        show screen hermione_main
        with d3
        her "Мои трусики..."
        hide screen hermione_main
        with d3
        $ h_xpos=120 #Defines position of the Hermione's full length sprite. center: 120. Right: 370.
        $ h_body = "03_hp/13_hermione_main/body_73.png" #Flashing Трусики
        show screen hermione_main
        with d3
        her "Что произошло с ними, сэр?"
        menu: 
            "\"Эксперимент не увенчался успехом.\"":
                her "Хм..."
                her "Понятно..."
            "\"Вы мне дали их такими!\"":
                her "Да? Ох, ясно..."
        hide screen hermione_main
        with d3
        ">Гермиона усмехаясь берет свои пропитаные спермой трусики..."
        hide screen hermione_main
        with d3
        $ h_xpos=120 #Defines position of the Hermione's full length sprite. center: 120. Right: 370.
        $ h_body = "03_hp/13_hermione_main/body_71.png" #Flashing Трусики
        show screen hermione_main
        with d3
        her "Вероятно их стоит очистить, прежде чем надевать..."
        m "Почему бы не надеть их прямо сейчас?"
        hide screen hermione_main
        with d3
        $ h_xpos=120 #Defines position of the Hermione's full length sprite. center: 120. Right: 370.
        $ h_body = "03_hp/13_hermione_main/body_17.png" #Flashing Трусики
        show screen hermione_main
        with d3
        her "Хм....?"
        hide screen hermione_main
        with d3
        $ h_xpos=120 #Defines position of the Hermione's full length sprite. center: 120. Right: 370.
        $ h_body = "03_hp/13_hermione_main/body_71.png" #Flashing Трусики
        show screen hermione_main
        with d3
        her "Ну, думаю можно их надеть еще раз, прежде чем постирать..."
        hide screen hermione_main
        with d3
        show screen blktone8
        with d3
        ">Гермиона надевает свои трусики..."
        hide screen blktone8
        with d3
        hide screen hermione_main
        with d3
        $ h_xpos=120 #Defines position of the Hermione's full length sprite. center: 120. Right: 370.
        $ h_body = "03_hp/13_hermione_main/body_34.png" #Flashing Трусики
        show screen hermione_main
        with d3
        her "(Выглядит забавно...)"
        hide screen hermione_main
        with d3
        $ h_xpos=120 #Defines position of the Hermione's full length sprite. center: 120. Right: 370.
        $ h_body = "03_hp/13_hermione_main/body_44.png" #Flashing Трусики
        show screen hermione_main
        with d3
        her "Это все, сэр?"
    if whoring >= 9: #LEVEL 04+ (THIRD EVENT)
        hide screen hermione_main
        with d3
        $ h_xpos=120 #Defines position of the Hermione's full length sprite. center: 120. Right: 370.
        $ h_body = "03_hp/13_hermione_main/body_71.png" #Flashing Трусики
        show screen hermione_main
        with d3
        her "Мои трусики..."
        if request_03 >= 1:
            her "Они снова в чем-то скользком..."
        else:
            her "Они покрыты чем-то скользким..."
        her "И забавно пахнут..."
        hide screen hermione_main
        with d3
        $ h_xpos=120 #Defines position of the Hermione's full length sprite. center: 120. Right: 370.
        $ h_body = "03_hp/13_hermione_main/body_29.png" #Flashing Трусики
        show screen hermione_main
        with d3
        her "Хм... Этот запах..."
        her "Какой-то знакомый..."
        hide screen hermione_main
        with d3
        $ h_xpos=120 #Defines position of the Hermione's full length sprite. center: 120. Right: 370.
        $ h_body = "03_hp/13_hermione_main/body_45.png" #Flashing Трусики
        show screen hermione_main
        with d3
        her "Что вы с ними делали, сэр?"
        menu:
            "\"Эксперимент не увенчался успехом\"":
                her "Эксперимент, да?"
                her "Какого рода?"
                hide screen hermione_main
                with d3
                $ h_xpos=120 #Defines position of the Hermione's full length sprite. center: 120. Right: 370.
                $ h_body = "03_hp/13_hermione_main/body_46.png" #Flashing Трусики
                show screen hermione_main
                with d3
                her "Нет, не отвечайте...Мне кажется я знаю..."
            "\"Вы мне дали их такими!\"":
                her "Я так не думаю, сэр."
                her "Но ладно, если вы не хотите говорить, сэр..."
                her "Я уверена, что знаю что с ними произошло..."
            "\"Я кончил на них!\"":
                hide screen hermione_main
                with d3
                $ h_xpos=120 #Defines position of the Hermione's full length sprite. center: 120. Right: 370.
                $ h_body = "03_hp/13_hermione_main/body_64.png" #Flashing Трусики
                show screen hermione_main
                with d3
                her "Я знала это..."
                her "Они пахнут спермой!"
        hide screen hermione_main
        with d3
        $ h_xpos=120 #Defines position of the Hermione's full length sprite. center: 120. Right: 370.
        $ h_body = "03_hp/13_hermione_main/body_68.png" #Flashing Трусики
        show screen hermione_main
        with d3
        her "Хм..."
        her "Похоже стоит их постирать, прежде чем надевать..."
        hide screen hermione_main
        with d3
        $ h_xpos=120 #Defines position of the Hermione's full length sprite. center: 120. Right: 370.
        $ h_body = "03_hp/13_hermione_main/body_64.png" #Flashing Трусики
        show screen hermione_main
        with d3
        her "Или вы хотите, чтобы я надела их сейчас, сэр...?"
        menu: 
            "\"Да! Надень их сейчас, девочка!\"":
                her "Ну, если так надо..."
            "\"Мне плевать. Делай что хочешь.\"":
                her "Почему бы не недеть их еще раз?"
        
        hide screen hermione_main
        with d3
        $ h_xpos=120 #Defines position of the Hermione's full length sprite. center: 120. Right: 370.
        $ h_body = "03_hp/13_hermione_main/body_74.png" #Flashing Трусики
        show screen hermione_main
        with d3
        her "Я делаю это только для того, чтобы выиграть кубок в этом году..."
        m "Верно..."
        hide screen hermion_main
        with d3
        show screen blktone8
        with d3
        ">Гермиона быстро проскальзывает в свои влажные трусики..."
        hide screen blktone8
        with d3

    jump back_from_panties
    
###################REQUEST_04 (Level 02) (Touch tits's through fabric.)###############################
label new_request_04:
    hide screen hermione_main 
    with d3
    m "{size=-4}(Я хочу немного потискать ее грудки. Даже не буду просить оголить их. Очень безобидно){/size}"
    $ menu_x = 0.5 #Default position of the menu (0.5). Version B is $ menu_x = 0.2
    menu:
        "\"(Да, давай попробуем!)\"":
            pass
        "\"(Не сейчас.)\"":
            jump new_personal_request
    
    
    
    if whoring <=2: # LEVEL 01 # Hermione refuses.
        jump too_much
        
    elif whoring >= 3 and whoring <= 5: # LEVEL 02 # Hermione is hesitant. 
        $ new_request_04_01 = True # Hearts.
        hide bld1
        with d3
        m "Подойди, девочка..."
        her_02 "Эм... Ладно..."
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

        her_02 "сэр.....?"
        menu: 
            m "..."
            "\"Я хочу потискать твои грудки.\"":
                her_03 "Что? Что вы имеете в виду, профессор--?"
                ">Гермиона чуть отходит назад..."
                ">Вы притягиваете ее и хватаетесь за грудки..."
                "-Просто протягиваете руку и хватаетесь за них.-"
                ">Вы протягиваете вторую и руку и вот уже держите обе сиськи!"
        stop music fadeout 1.0
        with hpunch
        her_07 "!!!?"
        her_08 "Профессор Дамблдор?!"
        ">Гермиона пытается оттолкнуть вас, но вы крепко схватили ее за бюст..."
        play music "music/(Orchestral) Playful Tension by Shadow16nh.mp3" fadein 1 fadeout 1 # SEX THEME.
        her_09 "Профессор, что вы--?"
        ">Она снова пытается оттолкнуть вас."
        ">Вы сжимаете ее сиськи как тисками."
        her_10 "Профессор, вы делаете мне больно!"
        g4 "Просто стой на месте, девочка!"
        her_11 "Н-но..."
        m "Я просто хочу немного потискать твою грудь, за что ты получишь очки!"
        her_12 "Н-но... это..."
        m "Просто стой..."
        m "Представь что ты в любимом месте или вроде того..."
        her_11 "М-моем любимом месте...?"
        ">Вы ощущаете насколько упруги грудки этой девчушки..."
        hide screen hermione_walk_01
        hide screen genie
        show screen ctc
        show screen bld1
        show screen chair_02 #Genie's chair.
        show screen groping_03
        with d1
        hide screen blkfade
        with d5
        pause
        her_13 "............................"
        menu:
            "-Сжать ее груди со всей силой-":
                show screen blktone
                with d5
                ">Вы собираетесь с силами..."
                her_12 "Мои..........."
                ">Вы сжимаете ее груди сильнее..."
                her_13 "Профессор, вы делаете мне больно..."
                m "Тише, девочка..."
                her_12 "Ау.............."
                ">Вы сжимаете ее большие груди еще сильнее."
                her_10"Ах! Это больно!"
                her_10 "Они сейчас лопнут! Пожалуйста, прекратите!"
                m "Они не могут лопнуть, глупышка..."
                ">Вы ослабляете напор..."
                her_13 "Это больно..."
                m "Ты будешь в порядке..."
                her_04 "........."

            "-Массировать грудь-":
                show screen blktone
                with d5
                ">Вы начинаете массировать грудь Гермионы..."
                her_13 "Профессор...?"
                m "Очки, девочка... Тебе нужны очки. Сконцентрируйся на этом."
                her_04 "Да..."
                her_15 "Да, честь \"Гриффиндора\"..."
                "*Жим-жим!*"
                ">Вы продолжаете массировать сисечки..."
                ">Вы слегка щипаете одну из грудок..."
                her_13 "Профессор... Вы ущепнули меня...?"
                ">Ваши попытки оказались напрасны. Ткань униформы слишком толстая..."
                her_15 "\"Гриффиндор\" ............"

            "-Отпустить ее и дать очки-":
                show screen blktone
                with d5
                m "Ну, если ты собираешься так драматизировать, то можешь просто уйти..."
                show screen blkfade
                with d5
                ">Вы отпускаете ее грудь..."
                her_14 "Правда?"
                m "Да, да... Я все равно дам тебе очки..."
                her_14 "Э-э... Спасибо, профессор..."
                m "Но сегодня вы их не заработали..."
                her_12 "Оу........."

    if whoring >= 6: # LEVEL 03 and higher # Hermione doesn't mind. <============================================================================EVENT LEVEL: 03
        if whoring >= 6 and whoring <= 8: # LEVEL 03.
            $ new_request_04_02 = True # Hearts.
        else:
            $ new_request_04_03 = True # Hearts.
        stop music fadeout 2.0
        m "Подойди ближе, девочка... Я хочу сделать тебе массаж груди..."
        her_14 "Как скажете, профессор..."
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
        play music "music/(Orchestral) Playful Tension by Shadow16nh.mp3" fadein 1 fadeout 1 # SEX THEME.
        ">Гермиона начинает стягивать свою униформу..."
        m "Нет, не стоит. Я хочу делать это пока ты полностью одета..."
        her_14 "Ох, хорошо..."
        ">Гермиона стоит перед вами в ожидании..."
        ">Вы хватаете ее больший сиськи..."
        ">И усиленно начинаете их массировать..."

        hide screen hermione_walk_01
        hide screen genie
        show screen ctc
        show screen bld1
        show screen chair_02 #Genie's chair.
        show screen groping_03
        with d1
        hide screen blkfade
        with d5
        pause

        "*Жмак-жмак-жмак*"
        her_16 "................"
        menu:
            "\"Тебе нравится это, девочка?\"":
                her_14 "Что...?"
                her_14 "Ох, Я не против этого..."
                "*Жмак-жмак-жмак*"
                ">Вы продолжаете мягко мять ее грудь..."
                her_16 "То есть, это не такая большая плата за то, что я получу в конце..."
                ">Вы продолжаете мять ее грудки через униформу..."
                her_01 "Небольшая цена для чести моего факультета......{image=textheart.png}"
            "-Резко потянуть их с силой-":
                show screen blktone8
                with d3
                ">Внезапно вы сильно оттягиваете ее сиськи..."
                with vpunch
                her_09 "Ауч...."
                ">ВЫ снова оттягиваете ее сиськи. На этот раз чуть сильнее."
                with vpunch
                her_09 "Ой! Профессор, что вы пытаетесь сделать...?"
                ">Вы оттягиваете их вниз со всей силы..."
                with vpunch
                with vpunch
                ">Гермиона теряет равновесие..."
                her_17 "*Задыхаясь* Что вы делаете, сэр...?"
                her_18 "Вам не стоит быть таким грубым со мной....{image=textheart.png}"
        
        
        

    


    if whoring <= 5:
        $ whoring +=1
        
    show screen blkfade 
    with d3
    hide screen bld1
    hide screen hermione_main
    hide screen blktone 
    hide screen hermione_02
    hide screen ctc
    hide screen bld1
    hide screen chair_02 #Genie's chair.
    hide screen groping_03
    hide screen blktone8
    show screen genie
    show screen hermione_01 #Hermione stands still.


    stop music fadeout 1.0
    ">Вы отпускаете грудь Гермионы..."
    m "На этом все."
    her_04 "................"
    
    hide screen blkfade 
    with d3
    
    $ gryffindor +=15
    m "\"Гриффиндор\" получает 15 очков!"
    
    $ request_04_points += 1
   
   
    $ hermione_chibi_xpos = 400 #Near the desk.
    show screen hermione_02 #Hermione stands still.
    show screen bld1
    hide screen blkfade
    with Dissolve(1)
    
    $ h_xpos=370 #Defines position of the Hermione's full length sprite.
    $ h_ypos=0
    $ h_body = "03_hp/13_hermione_main/body_29.png" #Sprite of Hermione's upper body.
    show screen hermione_main
    with d3
    her ".................."
    her "Спасибо сэр..."
    if daytime:
        her "Теперь, мне лучше идти. Занятия вот-вот начнутся."
    else:
        her "Мне лучше пойти. Уже поздно..."
    
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

###################REQUEST_05 (Level 02) (BUTT MOLESTER).
label new_request_05:
    hide screen hermione_main 
    with d3
    m "{size=-4}(Я просто хочу немного помять ее попку.){/size}"
    $ menu_x = 0.5 #Default position of the menu (0.5). Version B is $ menu_x = 0.2
    menu:
        "\"(Да, давай попробуем!)\"":
            pass
        "\"(Не сейчас.)\"":
            jump new_personal_request

    
    if whoring <=2:
        jump too_much
        
    if whoring >= 3 and whoring <= 5:
        $ level = "02"
        $ new_request_05_01 = True # HEARTS.
    elif whoring >= 6 and whoring <= 8:
        $ level = "03"
        $ new_request_05_02 = True # HEARTS.
    elif whoring >= 9:
        $ level = "04"
        $ new_request_05_03 = True # HEARTS.
        
        
    if whoring >= 3 and whoring <= 5: # LEVEL 02 # Hermione is hesitant. <=================================================================================== FIRST EVENT.
        
        hide bld1
        with d3
        m "Подойди ближе, дитя. Давайка разомнем твою сочную попку."
        if request_05_points == 0 and whoring <= 5: #First time
            stop music fadeout 5.0
            her_07 "Профессор Дамблдор!?"
            m "Расслабься. Это будет самая простая услуга за эти 15 очков, я обещаю."
            her_08 "Но...."
            m "Все, что я хочу, это несколько раз сжать твою милую попку..."
            her_04 "Это неуместно, профессор................"
            m "Всем не обязательно знать, как ты получила эти очки..."
            her_12 "(Эти 15 очков действительно вытолкнут нас вперед...)"
            her_19 "(Черт.....!)"
        else:
            her_04 "Снова.....?"
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
        her_04 ".................."
        her_04 "Вы хотите, чтобы я развернулась, сэр?"
        play music "music/(Orchestral) Playful Tension by Shadow16nh.mp3" fadein 1 fadeout 1 # SEX THEME.
        menu:
            m "Хм..."
            "\"Да, развернитесь, пожалуйста, Мисс Грейнджер.\"":
                her_04 "Как вы скажите, сэр..."
                hide screen hermione_walk_01
                hide screen genie
                show screen ctc
                show screen no_groping_02
                with d1
                hide screen blkfade
                with d5
                pause
                her_04 "............."
                her_04 "..........................."
                her_25 "Сэр, я бы хотела покончить с этим как можно раньше..."
                m "Не торопи меня, девочка...Дай мне насладиться моментом..."
                her_04 "............................."
                menu:
                    m "Хм..."
                    "-Сжать ее булочки-":
                        pass
                    "-Шлепнуть по попке-":
                        $ renpy.play('sounds/slap_02.mp3') #SLAP!
                        show screen white
                        with hpunch
                        pause.08
                        hide screen white
                        show screen bld1
                        her_22 "!!!!!!!!!!!!!"
                        her_22 "Профессор!!?"
                        menu:
                            "\"Ладно, ладно... Я просто не смогу устоять....\"":
                                her_25 "......................."
                                pass
                            "-Шлепнуть еще раз-":
                                $ renpy.play('sounds/slap_02.mp3') #SLAP!
                                show screen white
                                with hpunch
                                pause.08
                                hide screen white
                                show screen bld1
                                her_21 "!!!!!!!!!!!!!"
                                her_15 "Профессор, что вы делаете!?"
                                her_15 "Вы сказали, что будете просто щупать!"
                                menu:
                                    "\"Ладно, ладно... Я просто не смог устоять....\"":
                                        her_25 "......................."
                                        pass
                                    "-Шлепнуть еще раз-":
                                        $ renpy.play('sounds/slap_02.mp3') #SLAP!
                                        show screen white
                                        with hpunch
                                        pause.08
                                        hide screen white
                                        show screen bld1
                                        her_15 "Ой! Это больно!"
                                        her_20 "Это так унизительно!"
                                        her_20 "Вы сказали, что будете просто щупать!..."
                                        #her_20 "Why are you doing this, профессор?"
                                        g4 "Просто стойте, Мисс Грейнджер!"
                                        her_19 "Я так не думаю, сэр!"
                                        her_24 "Никакие очки не стоят такого!"
                                        her_23 "Вы злоупотребляете свой властью, сэр!"
                                        g4 "Что?"
                                        her_19 "Я ухожу!"
                                        menu:
                                            g4 "Арх..."
                                            "\"Мои... Я прошу прощения...\"":
                                                her_25 "Просто больше не делаете этого, сэр..."
                                                pass
                                            "\"Ты не получишь очков за это!\"":
                                                $ mad += 30
                                                her_20 "Ха! See if I care, сэр!"
                                                ### Takes place aftre you refuse to pay her the очков.
                                                $ walk_xpos=300 #Animation of walking chibi. (From)
                                                $ walk_xpos2=610 #Coordinates of it's movement. (To)
                                                $ hermione_speed = 03.0 #The speed of moving the walking animation across the screen.
                                                hide screen no_groping_02
                                                hide screen bld1
                                                show screen genie
                                                show screen hermione_walk_01_f 
                                                with fade
                                                pause 2
                                                hide screen hermione_walk_01_f 
                                                $ renpy.play('sounds/door.mp3') #Sound of a door opening.
                                                with Dissolve(.3)
                                                pause.5
                                                g4 "Арх! (You little brat!)"
                                                $ request_05_points += 1
                                                if daytime:
                                                    $ hermione_takes_classes = True
                                                    jump day_main_menu
                                                else:
                                                    $ hermione_sleeping = True
                                                    jump night_main_menu
                                            "\"Я вычитаю очки за это!\"":
                                                $ mad += 20
                                                her_22 "Вы серьезно!?"
                                                $ gryffindor -=10
                                                g4 " \"Гриффиндор\" , минус 10 очков!"
                                                g4 "Все! Именно так!"
                                                her_24 "Грр..........."
                                                her_24 "........................"
                                                her_27 "Это не справедливо..."
                                                m "Что? Эй, подожди, не начинай плакаться мне..."
                                                her_29 "Я ненавижу вас, проф! Я ненавижу вас!"
                                                
                                                $ walk_xpos=300 #Animation of walking chibi. (From)
                                                $ walk_xpos2=610 #Coordinates of it's movement. (To)
                                                $ hermione_speed = 02.0 #The speed of moving the walking animation across the screen.
                                                hide screen no_groping_02
                                                hide screen bld1
                                                show screen genie
                                                show screen hermione_run
                                                with fade
                                                pause.9
                                                hide screen hermione_run
                                                with Dissolve(.3)
                                                $ renpy.play('sounds/door.mp3') #Sound of a door opening.
                                                m ".............."
                                                menu:
                                                    "\"Черт. Чувствую себя хреново...\"":
                                                        $ mad -= 5
                                                        m "Черт... Чувствую себя хреново..."
                                                        m "But who could resist slapping that little behind of her's?"
                                                    "\"She made me do this, that brat!\"":
                                                        $ mad += 9
                                                        m "She made me do this, that brat!"
                                                        m "Acting all wounded now..."
                                                        m "I bet she actually enjoyed the slapping and just won't admit it..."
                                                $ request_05_points += 1
                                                if daytime:
                                                    $ hermione_takes_classes = True
                                                    jump day_main_menu
                                                else:
                                                    $ hermione_sleeping = True
                                                    jump night_main_menu     
        
                pause
                show screen groping_02
                with d7
                her_07 "!!!!!!?"
                m "Что такое, Мисс Грейнджер?"
                her_15 "ничего профессор ..."
                her_15 "Просто... "
                her_15 "Я просто не могу поверить что это случилось..."
                her_15 "Это... неправльно..."
                m "Расслабься, девочка. It's not like you are enjoying this..."
                her_19 "Что? Конечно нет! Это непристойно..."
                her_19 "Я сделаю эту жертву для чести моего факультета..."
                m "Да,сосредоточся на этом..."
                her_20 "...................."
                show screen bld1
                with d3
                pause
                her_17 "Но, профессор..."
                her_05 "Почему  {size=+7}вы{/size} делаете это?"
                menu: 
                    m "Хм..."
                    "\"У меня есть свои причины...\"":
                        her_12 "Oх..."
                        her_25 "Хм..."
                    "\"Это для науки, конечно!\"":
                        her_03 "Правда?!"
                        her_03 "Это одно из исследований?"
                        m "Да, точно, я исследую Эм... э..."
                        m "Ну, тебе не понять, это некоторые довольно продвинутые магические штуки..."
                        her_03 "Понятно..."
                        her_02 "Ну, если это для науки, то я рада помочь..."
                    "-Сжать её ягодицы жестче-":
                        ">Вы мнете ягодицы Гермионы с удвоеной силой."
                        her_05 "...................."
                        her_12 "(Должна ли я промолчать.....?)"
                show screen blktone8
                with d3
                ">Вы продолжаете играть с ягодицами Гермионы..."
                ">Вы проводите руками вниз..."
                her_15 "................"
                label connection_of_rapes:
                menu:
                    "-Залесть к ней в трусики-":
                        ">Вы медленно запускаете свою руку в  ее трусики..."
                        her_07 "Профессор... Что вы...?"
                        m "Это нормально, просто подумай о тех 15 баллах, которые ты можешь получить..."
                        her_12 "............."
                        menu:
                            "-Поласкать её киску пальцем-":
                                show screen blkfade
                                with d3
                                ">Вы проникаете пальцами вниз и засовываете в ее маленькую щель..."
                                her_07 "Про? Нет! Что вы...?"
                                ">Гермиона пытается вырваться..."
                                menu:
                                    "-Засунуть пальцы силой!-":
                                        ">Вы силой суете палец ей в киску..."
                                        ">Там очень тепло и узко..."
                                        ">Но там очень суха... Не похоже, что Гермиона получила от этого удоволствие..."
                                        jump screams_of_rapings
                                    "-Продолжить...-":
                                        pass
                            "-Поласкать пальцем ее попку-":
                                show screen blkfade
                                with d3
                                ">Вы всовывайте свой палец в её узенькую дырочку..."
                                her_07 "Профессор? Нет! Что вы делаете!?"
                                ">Гермиона пытается вырваться..."
                                menu:
                                    "-Силой засунуть палец-":
                                        ">Вы силой всовывайте палец в её дырочку..."
                                        with hpunch
                                        her_30 "!!?"
                                        ">Там очень узко и тепло..."
                                        jump screams_of_rapings
                                    "-Умерить пыл...-":
                                        pass
                            "- Перестать испытовать удачу.-":
                                pass
                    "-Нет. На сегодня хватит. Отпустить её-":
                        pass
            "\"Нет. Просто стойте, Мисс Грейнджер.\"":
                her_04 "Как вы скажите, сэр..."
                hide screen hermione_walk_01
                hide screen genie
                show screen ctc
                show screen no_groping_01
                with d1
                hide screen blkfade
                with d5
                pause
                her_01 "Сэр,пожалуйста поторопитесь, прежде чем кто-нибудь узнает..."
                m "В чем проблема, Мисс Грейнджер?"
                m "Вы знаете вы делаете это для факультета."
                her_04 "Я знаю."
                her_04 "Но никто не знает каким образом..."
                her_04 "Так, что давайте сделаем это как можно быстрее..."
                her_05 "Пожалуйста..."
                m "Ну, если ты не против..."
                show screen groping_01
                with d7
                her_07 "!!!"
                m "Что случилось?"
                her_05 "Ничего, сэр. У вас руки холодные вот и все..."
                show screen bld1 
                with d3
                show screen blktone8
                with d3
                ">Вы растираете руки об ноги Гермионы..."
                her_04 "........................."
                ">Вы хорошенько сжимаете её ягодицы..."
                her_19 "................."
                m "Не смотри по сторонам, девочка. Я хочу чтобы ты смотрела мне в глаза."
                her_19 "Я бы предпочла не смотреть, сэр..."
                menu:
                    m "..."
                    "\"Ладно.Тогда просто продолжай стоять.\"":
                        her_15 "Спасибо сэр..."
                        ">Вы делаете легкий массаж её ягодицам..."
                        her_15 "...................."
                        ">И вы наслаждаете её формами..."
                        her_19 "....................."
                        ">Затем вы в последний раз сжиматете её попку."
                        her_19 "....................."
                    "\"Открой глаза, или лишишься очков очков!\"":
                        $ mad += 7
                        her_19 "Арх! {size=-5}(Ах ты старый--{/size}"
                        m "Что нибудь скажите, Мисс Грейнджер?"
                        her_08 "Ничего, сэр."
                        ">Вы делаете легкий массаж её ягодицам..."
                        ">Гермиона смотрит вам в глаза, как она и сказала..."
                        her_08 "...................."
                        her_04 "..............................."
                        m "Что я тебе говорил об отводе глаз?"
                        her_19 "Да, я помню..."
                        her_08 "................................."
                        her_25 "..................................."
                        her_25 ".................................................."
                        ">Вы продолжаете наслаждаться её упругой попкой..."
                        her_08 "....................."
                        jump connection_of_rapes
    
        
    elif whoring >= 6: # LEVEL 04 # Hermione is hesitant. <=================================================================================== SECOND EVENT.
        $ new_request_05_02 = True # HEARTS.
        hide screen bld1
        with d3
        m "Подойди ближе, девочка. Позволь потрогать твою попу."
        her_17 "Как скажете..."
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
        her_18 "Вы хотите чтобы я повернулась, сэр?"
        play music "music/(Orchestral) Playful Tension by Shadow16nh.mp3" fadein 1 fadeout 1 # SEX THEME.
        menu:
            m "Хм..."
            "\"Да. Повернитесь, Мисс Грейнджер.\"":
                her_18 "Как вы скажите, сэр..."
                hide screen hermione_walk_01
                hide screen genie
                show screen ctc
                show screen no_groping_02
                with d1
                hide screen blkfade
                with d5
                pause
                her_35 "............."
                menu:
                    m "Хм..."
                    "-Сжать ее булочки-":
                        pass
                    "-Шлепнуть по попке-":
                        $ renpy.play('sounds/slap_02.mp3') #SLAP!
                        show screen white
                        with hpunch
                        pause.08
                        hide screen white
                        show screen bld1
                        her_22 "!!!!!!!!!!!!!"
                        her_18 "Профессор....?"
                        menu:
                            "\"Ладно,ладно... Я просто не смог удержаться....\"":
                                her_18 "Хорошо..."
                                pass
                            "-Шлепнуть еще раз-":
                                $ renpy.play('sounds/slap_02.mp3') #SLAP!
                                show screen white
                                with hpunch
                                pause.08
                                hide screen white
                                show screen bld1
                                her_21 "!!!!!!!!!!!!!"
                                her_18 "Профессор, что вы делаете!?"
                                her_18 "Вы сказали,что только потрогаете!"
                                menu:
                                    "\"Ладно,ладно... Я просто не смог удержаться....\"":
                                        her_18 "Это ведь не так трудно..."
                                        pass
                                    "-Шлепнуть еще раз-":
                                        $ renpy.play('sounds/slap_02.mp3') #SLAP!
                                        show screen white
                                        with hpunch
                                        pause.08
                                        hide screen white
                                        show screen bld1
                                        her_34 "Пр, не так громко, пожалуйста..."
                                        her_34 "Нас ведь могут услышать?"
                                        m "Хорошо,хорошо... продолжу щупать..."
                                        her_18 "................"

                pause
                show screen groping_02
                with d7
                her_18 "..................."
                m "Ты сегодня тихая, Мисс Грейнджер."
                her_18 "Я...?"
                her_35 "Ну, вы знаете меня, сэр..."
                her_35 "Я просто рада быть частью факультета \"Гриффиндора\"...."
                her_35 "Не обращайте внимание и продолжайте..."
                her_18 "(...Щупать меня...)"
                show screen blktone8
                with d3
                ">Вы продолжаете играть с попкой Гермионы..."
                ">And continue sliding your hands up and down her inner tighs..."
                her_18 "................"
                label connection_of_rapes_02:
                menu:
                    "-Залесть к ней в трусики-":
                        ">Вы медленно запускаете свою руку в  девочкины трусики... "
                        her_17"Профессор... Что вы...?"
                        m "Это нормально, просто подумай о тех 15 баллов которые ты можешь получить.."
                        her_17 "Как вы скажите..."
                        menu:
                            "-Поласкать её киску пальцем-":
                                show screen blkfade
                                with d3
                                ">Вы проникаете пальцами вниз и засовываете в ее маленькую щель..."
                                her_18 "Профессор?" 
                                menu:
                                    "-Засунуть палец силой в её киску!-":
                                        ">-Вы силой всовывайте свой палец в её маленькую щель-..."
                                        ">Там очень тепло и узко...."
                                        ">Там немного влажно, похоже она получает немного удовольствия от этого..."
                                        jump screams_of_pleasure
                                    "-Продолжить...-":
                                        pass
                            "-Prod her butt-hole instead-":
                                show screen blkfade
                                with d3
                                ">Вы всовывайте свой палец в её узенькую дырочку..."
                                her_18 "Профессор? Что вы пытаетесь сделать?"
                                menu:
                                    "-Силой заусунуть палец в её узкую попку-":
                                        ">Вы всовывайте свой палец в её узенькую дырочку..."
                                        with hpunch
                                        her_36 "aх... ваш палец в моей ..."
                                        ">Там тепло и узко..."
                                        jump screams_of_pleasure
                                    "-Продожить...-":
                                        pass
                            "-Перестать испытовать удачу.Отпустить девочку-":
                                pass
                    "-Нет. На сегодня хватит. Отпустить девочку-":
                        pass
            "\"Нет. Просто стойте, Мисс Грейнджер.\"":
                her_04 "Как вы скажите, сэр..."
                hide screen hermione_walk_01
                hide screen genie
                show screen ctc
                show screen no_groping_01
                with d1
                hide screen blkfade
                with d5
                pause
                her_01 "сэр,поторопитесь,пока никто не узнал про это..."
                m "В чем проблема, Мисс Грейнджер?"
                m "Вы знаете , что вы делаете это для своего факультета."
                her_04 "Знаю."
                her_04 "Но никто не видет каким образом..."
                her_04 "Так ,что давайте покончим с этим как можно быстрее..."
                her_05 "Пожалуйста..."
                m "Ну,если ты настаиваешь..."
                show screen groping_01
                with d7
                her_07 "!!!"
                m "Что случилось?"
                her_05 "Ничего, сэр. Ничего, сэр. У вас руки холодные вот и все..."
                show screen bld1 
                with d3
                show screen blktone8
                with d3
                ">Вы растираете руки об ноги Гермионы..."
                her_04 "........................."
                ">И хорошенько жамкайте ягодицы..."
                her_19 "................."
                m "Не смотри по сторонам, девочка. Я хочу чтобы ты смотрела мне в глаза."
                her_19 "Я бы предпочла не смотреть,, сэр..."
                menu:
                    m "..."
                    "\"Ладно.Тогда просто продолжай стоять..\"":
                        her_15 "Спасибо сэр..."
                        ">Вы делаете легкий массаж её ягодицам..."
                        her_15 "...................."
                        ">Вы продолжаете наслаждаться её упругой попкой..."
                        her_19 "....................."
                        ">Затем вы последний раз сжимаете их."
                        her_19 "....................."
                    "\"Открой свои глаза или не получишь очков!\"":
                        $ mad += 20
                        her_19 "Арх! {size=-5}(Старый козел--{/size}"
                        m "Вы что-то сказали, Мисс Грейнджер?"
                        her_08 "Ничего, сэр."
                        ">Вы делаете легкий массаж её ягодицам...."
                        ">Гермиона смотрит вам в глаза, как она и сказала..."
                        her_08 "...................."
                        her_04 "..............................."
                        m "Что я тебе говорил об отводе глаз?"
                        her_19 "Да, я помню...."
                        her_08 "................................."
                        her_25 "..................................."
                        her_25 ".................................................."
                        ">Вы продолжаете наслаждаться её упругой попкой..."
                        her_08 "....................."
                        jump connection_of_rapes_02  
        
        
        
        
        
        
        
  
  
  
  
  
  
  
  
    
        
    label ending_of_screams_of_pleasure:
    if whoring <= 5:
        $ whoring +=1
    show screen blkfade 
    with d5
    
    stop music fadeout 1.0
    ">Вы отпускаете ее попку..."
    m "На этом закончим."
    
    hide screen blktone8
    hide screen ctc
    hide screen bld1
    hide screen groping_01
    hide screen groping_02
    show screen hermione_02
    show screen genie
    with d1
    
    hide screen blkfade
    with d3

    $ gryffindor +=15
    m " \"Гриффиндор\" получает 15 очков!"
    
    $ request_05_points += 1
   
   
    $ hermione_chibi_xpos = 400 #Near the desk.
    show screen hermione_02 #Hermione stands still.
    show screen bld1
    hide screen blkfade
    with Dissolve(1)
    
    $ h_xpos=370 #Defines position of the Hermione's full length sprite.
    $ h_ypos=0
    $ h_body = "03_hp/13_hermione_main/body_29.png" #Sprite of Hermione's upper body.
    show screen hermione_main
    with d3
    her ".................."
    her "Спасибо сэр..."
    if daytime:
        her "Теперь, мне лучше идти. Занятия вот-вот начнутся."
    else:
        her "Я лучше пойду. Уже очень поздно..."
    

    hide screen bld1
    hide screen hermione_main
    with Dissolve(.3)
    $ walk_xpos=400 #Animation of walking chibi. (From)
    $ walk_xpos2=610 #Coordinates of it's movement. (To)
    $ hermione_speed = 02.0 #The speed of moving the walking animation across the screen.
    show screen hermione_walk_01_f 
    pause 2
    hide screen hermione_walk_01_f 
    $ hermione_chibi_xpos = 610 #Near the desk.
    show screen hermione_01_f #Hermione stands still.
    with Dissolve(.3)
    
    if whoring >= 3 and whoring <= 5: #First level. Not happy.
        her_12 "..........................."
        
        
    hide screen hermione_01_f #Hermione stands still.
    with Dissolve(.3)
    $ renpy.play('sounds/door.mp3') #Sound of a door opening.
    with Dissolve(.3)
    pause.5

    call music_block # Lunches apropriete BGM day/night.

    if daytime:
        $ hermione_takes_classes = True
        jump day_main_menu
    else:
        $ hermione_sleeping = True
        jump night_main_menu

### ALL THE SCREAMS ABOUT RAPE ###
label screams_of_rapings:
her_10 "НЕТ! Что вы наделали!!?"
">Гермиона сильно толкает вас..."
with hpunch
her_10 "Почему вы это делаете со мной, сэр...?"
her_27 "Я не согласна делать это... для..."
her_27 "Для... вас..."
with hpunch
her_29 "{size=+7}ВЫ ИЗНАСИЛОВАЛИ МЕНЯ!{/size}"
g4 "Что? Не смеши, девочка! Я не далал этого!"
her_29 "Да, изнасиловали! Изнасиловали!"
g4 "Я уверен, что это не так!"
her_29 "Нет,вы сделали это профессор!"
her_31 "Теперь дайте мне 20 очков--"
her_31 "Нет, 100 очков или я пожалуйюсь на вас в гильдию магии!!"
menu:
    m "(Ах, черт...)"
    "\"Ладно, ладно... 100 очков...\"":
        $ gryffindor +=100
        m "100 очков \"Гриффиндору\" !"
        m "Все,сделано..."
        m "Теперь вы успокоились, Мисс Грейнджер?"
        her_29 "Нет,еще нет!"
        her_29 "Я была изнасилована!"
        g4 "Ох, успокойся  девочка, я не насиловал тебя! Все что я сделал это--"
        with hpunch
        her_29 "{size=+7}Вы изнасиловали меня!!!{/size}"
        g4 "Великие пески пустыни, потише говори об изнасиловании!?"
        g4  "Кто-нибудь может услышать тебя!"
        her_29 "Отлично! Я хочу чтобы они услышали!"
        m "Почему ты досих пор недовольна? Я уже заплатил тебе!"
        her_32 "Oх... ладно..."
        her_33 "Но я тебя ненавижу!Я ненавижу вас профессор!"
        $ mad +=30

    "\"Ты блефуешь, девочка!\"":
        her_29 "Нет!Я сделаю это"
        g4 "By all means, go ahead..."
        g4 "There was no rape!"
        her_29 "Я ненавижу вас,профессор!"
        $ mad +=50


hide screen bld1
hide screen ctc
hide screen hermione_main
show screen genie
hide screen groping_01
hide screen groping_02
hide screen blkfade
hide screen blktone8
with Dissolve(.3)
$ walk_xpos=400 #Animation of walking chibi. (From)
$ walk_xpos2=610 #Coordinates of it's movement. (To)
$ hermione_speed = 02.0 #The speed of moving the walking animation across the screen.
show screen hermione_walk_01_f 
pause 2
hide screen hermione_walk_01_f 
$ hermione_chibi_xpos = 610 #Near the desk.
show screen hermione_01_f #Hermione stands still.
with Dissolve(.3)

if whoring >= 3 and whoring <= 5: #First level. Not happy.
    her_12 "..........................."
    
    
hide screen hermione_01_f #Hermione stands still.
with Dissolve(.3)
$ renpy.play('sounds/door.mp3') #Sound of a door opening.
with Dissolve(.3)
pause.5

if daytime:
    $ hermione_takes_classes = True
    jump day_main_menu
else:
    $ hermione_sleeping = True
    jump night_main_menu        
    
########### SCREAM OF PLEASURES ###        
label screams_of_pleasure:
    her_34 "Aх...."
    her_34 "Он внутри меня..."
    her_18 "Нет, профессор, вы должны остановиться..."
    m "Почему?Тебе не нравиться?"
    her_18 "Не имеет значение нравиться мне или нет, сэр."
    her_18 "Вы знаете почему я делаю это..."
    her_18 "И это неправильно,что вы даете всего 15 очков..."
    ">Гермиона отталкивает вас..."
    m "Хех... Я вижу..."
    m "Ну, в таком случае..."
    jump ending_of_screams_of_pleasure

    

###################REQUEST_06 (Level 02) (Flash Трусики to classmate.) #################################################################################
label new_request_06:
    if whoring <=2:
        jump too_much
    if whoring >= 3: #Level 02
        m "Я хочу чтобы ты сегодня кое-что сделала в своем классе: покажи трусики одному из своих однокласников."
        if request_06_points == 0: #One star.
            her "Oх..."
            "Гермиона неохотно соглашается."
        elif request_06_points == 1: #Two stars.
            her "Если только..."
            "Гермиона согласна."
            
        elif request_06_points == 2: #Three stars.
            her "Конечно..."
            "Гермиона согласна. Очень охотно."
            
        elif request_06_points >= 3: #Master.
            her "Конечно, профессор."
            ">Гермиона с радостью согласна."
        

        "Вы отправляете Гермиону."
        $ request_05 = True
        $ hermione_takes_classes = True
        
        if whoring <= 5:
            $ whoring +=1
            
        if request_05_points <= 2:
            $ gryffindor +=15
            "Гриффиндору +15 очков."
        else:
            $ gryffindor +=5
            "Гриффиндору  +5 очков."

        jump day_main_menu
       
label new_request_05_complete:
    "Гермиона возвращается с занятий."
    m "Как прошел день, Мисс Грейнджер?"
    if request_06_points == 0: #One star.
        her "Хм... Я пытался показать свои трусики, чтобы один из моих одноклассников увидел, но вместо этого я думаю, что пять или шесть из них мельком. Так стыдно..."
    elif request_06_points == 1: #Two stars.
        her "Я показала свои трусики одному из одноклассников."
    elif request_06_points == 2: #Three stars.
        her "Я долго показала свои трусики одному из одноклассников ."
    elif request_06_points >= 3: #Three stars.
        her "Мне удалось показать свои трусики так чтобы один из однокласснников глазел на них."
        her "Это было супер!"
    
    "Вы отпускаете Гермиону."
    $ request_06_points += 1 #Leveling up the event.
    $ request_05 = False 
    $ hermione_sleeping = True
    her "Ну, ладно. Я пойду спать тогда."     
    return


###################REQUEST_07 (Level 02) (Flash Трусики to a teacher).(Daytime only). #######################################################################
label new_request_07:
    if whoring <=2:
        jump too_much
    if whoring >= 3: #Level 02
        m "Я хочу чтобы ты сегодня кое-что сделала в своем классе: покажи трусики одному из своих учителей."
        if request_07_points == 0: #One star.
            her "Oх..."
            "Гермиона неохотно соглашается."
            
        elif request_07_points == 1: #Two stars.
            her "Если только..."
            "Гермиона согласна."
            
        elif request_07_points == 2: #Three stars.
            her "Конечно..."
            "Гермиона согласна. Очень охотно."
            
        elif request_07_points >= 3: #Master.
            her "Конечно, профессор."
            ">Гермиона с радостью согласна."
        

        "Вы отпускаете Гермиону."
        $ request_06 = True
        if whoring <= 5:
            $ whoring +=1
        
        if request_05_points <= 2:
            $ gryffindor +=15
            "Гриффиндор получает +15 очков."
        else:
            $ gryffindor +=5
            "Гриффиндор получает +5 очков."
        $ hermione_takes_classes = True
        jump day_main_menu
        

label new_request_06_complete:
    "Гермиона возвращается с занятий."
    m "Как прошел день, Мисс Грейнджер?"
    if request_07_points == 0: #One star.
        her "Хм... Я пыталась показать свои трусики учителю, чтобы он увидел их, но вместо этого я думаю, что пять или шесть одноклассников из них  увидели мельком. Так стыдно..."
    elif request_07_points == 1: #Two stars.
        her "Я показала свои трусики одному из учителей."
    elif request_07_points == 2: #Three stars.
        her "Я долго показала свои трусики одному из учителей."
    elif request_07_points >= 3: #Three stars.
        her "Я долго показала свои трусики одному из учителей."
        her "Это было супер!"
    
    $ request_07_points += 1 
    $ request_06 = False 
    $ hermione_sleeping = True
    her "Ну, ладно. Я пойду спать тогда."
    return

#####################################################################################################################################################################
### LEVEL 03 ###########################################################################################################################################################
###################REQUEST_08 (Level 03) (Show me tits). #####################################################################################################################
label new_request_08: #LV.3 (Whoring = 6 - 8)
    hide screen hermione_main 
    with d3
    if request_08_points == 0:
        m "{size=-4}(Я хочу посмотреть на эти сиськи?){/size}"
    else:
        m "{size=-4}(Я хочу посмотреть на эти сиськи снова?){/size}"
    $ menu_x = 0.5 #Default position of the menu (0.5). Version B is $ menu_x = 0.2
    menu:
        "\"(Да, давай попробуем!)\"":
            show screen blktone
            with d3
            pass
        "\"(Не сейчас.)\"":
            jump new_personal_request
    
    if whoring <=5:
        jump too_much
        
    
        
    $ current_payout = 25 #Used when haggling about price of th favor.
        
    if request_08_points == 0 and whoring <= 11: # LEVEL 04 # FIRST TIME.
        m "Мисс Грейнджер?"
        hide screen hermione_main
        with d3
        $ h_body = "03_hp/13_hermione_main/body_03.png" #Sprite of Hermione's upper body.
        $ h_xpos=370 #Defines position of the Hermione's full length sprite. (Default 370). (Center: 140)
        show screen hermione_main
        with d3
        her "Да, сэр..."
        m "Сколько очков будет стоить посмотреть на твои сиськи?"
        hide screen hermione_main
        with d3
        $ h_body = "03_hp/13_hermione_main/body_14.png" #Sprite of Hermione's upper body.
        $ h_xpos=370 #Defines position of the Hermione's full length sprite. (Default 370). (Center: 140)
        show screen hermione_main
        with d3
        stop music fadeout 1.0
        her "Сколько вы можете предложить...?"
        play music "music/Chipper Doodle v2.mp3" fadein 1 fadeout 1 # HERMIONE'S THEME.
        hide screen hermione_main
        with d3
        $ h_body = "03_hp/13_hermione_main/body_30.png" #Sprite of Hermione's upper body.
        $ h_xpos=370 #Defines position of the Hermione's full length sprite. (Default 370). (Center: 140)
        show screen hermione_main
        with d3
        her "Профессор Дамблдор!"
        m "Хм... Я думал ваш факультет может получить дополнительные очки..."
        m "Но я думаю, я был неправ..."
        hide screen hermione_main
        with d3
        $ h_body = "03_hp/13_hermione_main/body_31.png" #Sprite of Hermione's upper body.
        $ h_xpos=370 #Defines position of the Hermione's full length sprite. (Default 370). (Center: 140)
        show screen hermione_main
        with d3
        her ".........?"
        m "Пожалуйста не противься мне..."
        m "Все что я хочу это помочь тебе..."
        hide screen hermione_main
        with d3
        $ h_body = "03_hp/13_hermione_main/body_29.png" #Sprite of Hermione's upper body.
        $ h_xpos=370 #Defines position of the Hermione's full length sprite. (Default 370). (Center: 140)
        show screen hermione_main
        with d3
        her "............."
        hide screen hermione_main
        with d3
        $ h_body = "03_hp/13_hermione_main/body_33.png" #Sprite of Hermione's upper body.
        $ h_xpos=370 #Defines position of the Hermione's full length sprite. (Default 370). (Center: 140)
        show screen hermione_main
        with d3
        her "200 очков, сэр."
        m "Если я дам вам 200 очков, Мисс Грейнджер..."
        m "Вы оголите свою грудь и покажите свои дыньки?"
        hide screen hermione_main
        with d3
        $ h_body = "03_hp/13_hermione_main/body_47.png" #Sprite of Hermione's upper body.
        $ h_xpos=370 #Defines position of the Hermione's full length sprite. (Default 370). (Center: 140)
        show screen hermione_main
        with d3
        her "Профессор Дамблдор! Не надо так выражаться!"
        her "Я думаю я лучше пойду..."
        menu:
            "\"Стой. 200 очков твои. Показывай!\"":
                $ current_payout = 200 #Used when haggling about price of th favor.
                hide screen hermione_main
                with d3
                $ h_body = "03_hp/13_hermione_main/body_14.png" #Sprite of Hermione's upper body.
                $ h_xpos=370 #Defines position of the Hermione's full length sprite. (Default 370). (Center: 140)
                show screen hermione_main
                with d3
                her "Серьезно?"
                m "Да"
                hide screen hermione_main
                with d3
                $ h_body = "03_hp/13_hermione_main/body_29.png" #Sprite of Hermione's upper body.
                $ h_xpos=370 #Defines position of the Hermione's full length sprite. (Default 370). (Center: 140)
                show screen hermione_main
                with d3
                her "......................................"
                her "Вы обещаете,что не будете трогать их, сэр."
                m "Конечно,конечно..."
                hide screen hermione_main
                with d3
                $ h_body = "03_hp/13_hermione_main/body_32.png" #Sprite of Hermione's upper body.
                $ h_xpos=370 #Defines position of the Hermione's full length sprite. (Default 370). (Center: 140)
                show screen hermione_main
                with d3
                her "Я делаю это только ради моего факультета, сэр!"

            "\"Я дам тебе 5 очков если ты покажешь сиськи.\"":
                hide screen hermione_main
                with d3
                $ h_body = "03_hp/13_hermione_main/body_72.png" #Sprite of Hermione's upper body.
                $ h_xpos=370 #Defines position of the Hermione's full length sprite. (Default 370). (Center: 140)
                show screen hermione_main
                with d3
                her "Пять?!"
                hide screen hermione_main
                with d3
                $ h_body = "03_hp/13_hermione_main/body_76.png" #Sprite of Hermione's upper body.
                $ h_xpos=370 #Defines position of the Hermione's full length sprite. (Default 370). (Center: 140)
                show screen hermione_main
                with d3
                her "Профессор, я не собираюсь показывать их за скромные пять очков!"
                m "Ну, твои сиськи конечно не стоят 200, девочка!"
                hide screen hermione_main
                with d3
                $ h_body = "03_hp/13_hermione_main/body_73.png" #Sprite of Hermione's upper body.
                $ h_xpos=370 #Defines position of the Hermione's full length sprite. (Default 370). (Center: 140)
                show screen hermione_main
                with d3
                her "(Неужели они так плохи?)"
                hide screen hermione_main
                with d3
                $ h_body = "03_hp/13_hermione_main/body_69.png" #Sprite of Hermione's upper body.
                $ h_xpos=370 #Defines position of the Hermione's full length sprite. (Default 370). (Center: 140)
                show screen hermione_main
                with d3
                her "Может быть за сто очков?"
                menu:
                    "\"Хорошо. 100 очков твои! Показывай!":
                        $ current_payout = 100 #Used when haggling about price of th favor.
                        her "................."
                        her "Так и быть... за сто баллов..."
                    "\"25 очков моё финальное предложение!\"":
                        her "..............."
                        her "Ну,так и быть..."
            "\"Отлично, вали.Мне пофиг..\"":
                $mad = +12
                her "Арх!"
                call music_block
                jump could_not_flirt
                
                
        hide screen blktone
        with d3
        hide screen bld1
        with d3
        hide screen hermione_main
        with d5
        $ menu_x = 0.5 #Default menu position restored.
        show screen ctc
        play music "music/(Orchestral) Playful Tension by Shadow16nh.mp3" fadein 1 fadeout 1 # SEX THEME.
        pause
        show screen hermione_04
        with fade
        pause
        show screen bld1
        with d3
        m "Хм..."
        her_12 "{size=-5}(Мои сисечки сейчас взорвуться...){/size}"
        m "Подойди ближе, девочка, дай мне лучше рассмотреть..."
        her_04 "............"
        
        hide screen bld1
        with d3

        show screen blkfade #Completely black screen.
        with Dissolve(1)
        pause.5
        ">Гермиона медленно подходит к вам."
        ">С каждым шагом её сиськи покачиваются..."
       
        hide screen hermione_04 #Stands with tits out.
        hide screen genie
        show screen ctc
        show screen genie_and_tits_01
        with d1
        hide screen blkfade
        with d5
        pause
        show screen bld1
        with d3
        her_01 "............"
        m "Очень хорошо..."
        her_04 "....."

        $ badges = False # Hides any badges from hermione_main screen.


        show screen blktone 
        with d3
        hide screen hermione_main
        with d3
        $ h_body = "03_hp/13_hermione_main/body_81.png" #Sprite of Hermione's upper body.
        $ h_xpos=140 #Defines position of the Hermione's full length sprite. (Default 370). (Center: 140)
        #$ only_upper = True #No lower body displayed. 
        show screen hermione_main
        with d3
        pause
        her "...................................."
        
        
        
    else:
        if whoring >= 6 and whoring <= 8: # LEVEL 03 # <=================================================================================== FIRST EVENT. (HERMIONE IS UNWILLING).
            m "Мисс Грейнджер?"
            her_02 "Да, профессор?"
            m "Я хочу посмортреть на твои сиськи."
            her_04 "............"
            her_04 "Вы обещаете не трогать их, сэр?"
            m "Конечно."
            hide screen blktone
            with d3
            hide screen bld1
            with d3
            hide screen hermione_main
            with d5
            $ menu_x = 0.5 #Default menu position restored.
            show screen ctc
            pause
            show screen hermione_04
            with fade
            pause
            show screen bld1
            with d3
            m "Хм..."
            m "Подойди ближе, девочка, дай лучше рассмотреть их..."
            hide screen bld1
            with d3
            show screen blkfade #Completely black screen.
            with Dissolve(1)
            pause.5
            ">Гермиона медленно подходит к доске."
            hide screen hermione_04 #Stands with tits out.
            hide screen genie
            show screen ctc
            show screen genie_and_tits_01
            with d1
            hide screen blkfade
            with d5
            pause
            show screen bld1
            with d3
            m "Очень хорошо..."
            play music "music/(Orchestral) Playful Tension by Shadow16nh.mp3" fadein 1 fadeout 1 # SEX THEME.
            show screen blktone 
            with d3
            hide screen hermione_main
            with d3
            $ h_body = "03_hp/13_hermione_main/body_81.png" #Sprite of Hermione's upper body.
            $ h_xpos=140 #Defines position of the Hermione's full length sprite. (Default 370). (Center: 140)
            #$ only_upper = True #No lower body displayed. 
            $ badges = False # Hides any badges from hermione_main screen.

            show screen hermione_main
            with d3
            pause
            her "...................................."
            
            
            
            
            
            
        elif whoring >= 9: # LEVEL 04 and higher# <=================================================================================== SECOND EVENT and THIRD EVENT. (HERMIONE IS INDIFFERENT) 
            m "Я хочу увидеть твои сиськи, Мисс Грейнджер."
            her_15 "Вы будете только смотреть, сэр?"
            m "Конечно..."
            hide screen blktone
            with d3
            hide screen bld1
            with d3
            hide screen hermione_main
            with d5
            $ menu_x = 0.5 #Default menu position restored.
            show screen ctc
            pause
            show screen hermione_04
            with fade
            pause
            show screen bld1
            with d3
            m "Хм..."
            m "Подойди ближе, девочка, дай лучше рассмотреть их..."
            hide screen bld1
            with d3
            show screen blkfade #Completely black screen.
            with Dissolve(1)
            pause.5
            ">Гермиона медленно подходит к доске."
            hide screen hermione_04 #Stands with tits out.
            hide screen genie
            show screen ctc
            show screen genie_and_tits_01
            with d1
            hide screen blkfade
            with d5
            pause
            show screen bld1
            with d3
            m "Очень хорошо..."
            show screen blktone 
            with d3
            hide screen hermione_main
            with d3
            
            $ badges = False # Hides the layer with badges.
            
            $ h_body = "03_hp/13_hermione_main/body_84.png" #Sprite of Hermione's upper body.
            $ h_xpos=140 #Defines position of the Hermione's full length sprite. (Default 370). (Center: 140)
            #$ only_upper = True #No lower body displayed. 
            show screen hermione_main
            with d3
            pause
            her "...................................."
            play music "music/(Orchestral) Playful Tension by Shadow16nh.mp3" fadein 1 fadeout 1 # SEX THEME.
    menu:
        "\"Солгать. Схватить за сиськи!\"":
            if whoring >= 6 and whoring <= 8: # LEVEL 03 # <=================================================================================== FIRST EVENT. HERMIONE OUTRAGED.
                hide screen hermione_main
                $ only_upper = False #No lower body displayed. 
                with d3
                show screen blkfade
                with d3
                ">Вы протягиваете руку и вставляете свой палец в Гермиону..."
                her_07 "Профессор, что вы делаете?"
                hide screen blkfade
                hide screen blktone8
                hide screen blktone
                show screen chair_02 #Genie's chair.
                hide screen bld1
                show screen groping_naked_tits
                with fade
                pause
                show screen bld1
                with d3
                
                m "Расслабься, девочка. Просто стой!"
                m "Oх... Какие же у тебя классные сиськи..."
                play music "music/Chipper Doodle v2.mp3" fadein 1 fadeout 1 # HERMIONE'S THEME.
                her_13 "Нет, сэр, пожалуйста! Вы не должны..."
                m "Это не займет много времени, Просто стойте."
                her_24 "Сэр, Я не соглашалась на это!"
                with hpunch
                her_23 "Вы должны отпустите меня сейчас же!!!"
                show screen blkfade
                with d5
                ">Гермиона отторгает  от вас и спешно прикрывается."
                her_19 "Думаю я лучше пойду..."
                hide screen blkfade
                hide screen chair_02 #Genie's chair.
                hide screen groping_naked_tits
                hide screen bld1
                show screen genie
                $ hermione_chibi_xpos = 400 #Near the desk.
                show screen hermione_02 #Hermione stands still.
                with d5
                pause
                show screen bld1
                m "Вали, девочка. Ты не получишь свою оплтау..."
                her_19 "Но я показала свои..."
                her_24 "И вы трогали меня..."
                her_23 "И я ничего не получу?"
                m "Вы провалились, Мисс Грейнджер..."
                her_19  "Гр.................."
                her_19 "{size=-5}(Burn in hell, you wretched old---{/size}"
                $ mad += 22
                call music_block
                jump could_not_flirt
            elif whoring >= 9 and whoring <= 11: # LEVEL 04 # <=================================================================================== SECOND EVENT. A BIT ANGRY.
                hide screen hermione_main
                with d3
                $ only_upper = False #No lower body displayed. 
                show screen blkfade
                with d3
                ">Вы протягиваете свои руки и вставляете палец в Гермиону..."
                her_07 "Профессор, что вы делаете?"
                hide screen blkfade
                hide screen blktone8
                hide screen blktone
                show screen chair_02 #Genie's chair.
                hide screen bld1
                show screen groping_naked_tits
                with fade
                pause
                show screen bld1
                with d3
                m "Расслабься, девочка. Просто стой!"
                her_04 "Я не соглашалась на это, сэр..."
                her_04 "Я не думаю что вы должны..."
                m "Тебе не нравиться...?"
                her_12 "Что?"
                m "Тебе не нравиться как я играю и сжимаю твои сиськи?"
                her_12 "..............."
                m "Признайтесь, вам это нравится немного..."
                her_12 "{size=-5}(Так странно видеть мои сиськи у кого-то в руках...){/size}"
                her_13 "сэр, Я позволяю вам делать это со мной, чтобы помочь моему факультету, ничего более!"
                play music "music/Chipper Doodle v2.mp3" fadein 1 fadeout 1 # HERMIONE'S THEME.
                her_04 "Пожалуйста,отпустите меня!"
                show screen blkfade
                with d5
                ">Гермиона отторгает вас и спешно прикрывается."
                her_04 "Вы обещали не трогать, профессор..."
                m "Так сложно удержаться..."
                hide screen blkfade
                hide screen chair_02 #Genie's chair.
                hide screen groping_naked_tits
                hide screen bld1
                show screen genie
                $ hermione_chibi_xpos = 400 #Near the desk.
                show screen hermione_02 #Hermione stands still.
                with d5
                pause
                show screen bld1
                her_01 "............."
                her_09 "Могу я получить свою оплату?"
                m "Конечно..."
                $ mad += 9
            elif whoring >= 12: # LEVEL 05 # <=================================================================================== THIRD EVENT. ENJOYS A LITTLE.
                hide screen hermione_main
                with d3
                $ only_upper = False #No lower body displayed. 
                show screen blkfade
                with d3
                ">Вы протягиваете свои руки и вставляете палец в Гермиону..."
                her_07 "Профессор, что вы делаете?"
                hide screen blkfade
                hide screen blktone8
                hide screen blktone
                show screen chair_02 #Genie's chair.
                hide screen bld1
                show screen groping_naked_tits
                with fade
                pause
                show screen bld1
                with d3
                m "Расслабься, девочка. Просто стойте!"
                her_12 "Но..."
                her_13 "ах...{image=textheart.png}"
                her_12 " Я не соглашалась на это..."
                m "Но тебе это нравиться,не так ли?"
                her_13 "Несовсем, сэр!{image=textheart.png}"
                show screen blktone
                with d3
                ">Вы несколько раз сжимаете её сиськи..."
                hide screen blktone
                with d3
                her_15 "сэр,вы обещали не трогать..."
                m "Я знаю, я знаю... Но так трудно удержаться..."
                her_20 "................."
                her_06 "....................aх...{image=textheart.png}"
                her_06 "сэр,вы должны остановиться..."
                m "Еще чуть-чуть..."
                show screen blktone8
                with d3
                ">Вы продолжаете мять её сиськи..."
                hide screen blktone8
                with d3
                her_37 "сэр... остановитесь..."
                m "Почему? Потому что тебе это сильно нравиться?"
                her_18 "Нет,это не так..."
                her_17 "Я считаю..."
                show screen blktone8
                with d3
                ">Вы тянете сиськи в противоположных направлениях, а затем стягиваете их вместе..."
                hide screen blktone8
                with d3
                her_38 "Aх...{image=textheart.png} сэр, я действительно должна идти..."
                if daytime:
                    her_17 "Хорошо... скоро начнуться укроки..."
                else:
                    her_17 "Уже поздно..."
                m "Ну,хорошо..."
                show screen blkfade
                with d5
                ">Вы отпускаете ее грудь..."
                ">Гермиона прикрывается..."
                play music "music/Chipper Doodle v2.mp3" fadein 1 fadeout 1 # HERMIONE'S THEME.
                her_25 "Пожалуйста не думайте,что я забыла ваше обещание, сэр."
                m "Точно..."
                hide screen blkfade
                hide screen chair_02 #Genie's chair.
                hide screen groping_naked_tits
                hide screen bld1
                show screen genie
                $ hermione_chibi_xpos = 400 #Near the desk.
                show screen hermione_02 #Hermione stands still.
                with d5
                pause
                show screen bld1
                her_35 "Могу я получить свои очки?"
                $ mad +=7
   
        "\"Сдержать обещания. Просто смотреть.\"":
            ">Вы долго всматриваетесь в грудь Гермионы..."
            if whoring >= 6 and whoring <= 8: # LEVEL 03 # <=================================================================================== FIRST EVENT.
                pause
                menu:
                    "-Одобрительно кивнуть-":
                        ">Вы смотрите на ее сиськи и киваете в знак одобрения..."
                        her "......................"
                    "-Отрицательно трясти головой-":
                        $ mad += 3
                        ">Вы посмотрите на сиськи девушки, а затем в разочаровании трясете головой..."
                        her ".....................?"
            elif whoring >= 9 and whoring <= 11: # LEVEL 04 # <=================================================================================== SECOND EVENT.
                pause
                menu:
                    "\"У тебя отличный сиськи.\"":
                        hide screen hermione_main
                        with d3
                        $ h_body = "03_hp/13_hermione_main/body_83.png" #Sprite of Hermione's upper body.
                        $ h_xpos=140 #Defines position of the Hermione's full length sprite. (Default 370). (Center: 140)
                        show screen hermione_main
                        with d3
                        pause
                        her "Спасибо--"
                        hide screen hermione_main
                        with d3
                        $ h_body = "03_hp/13_hermione_main/body_82.png" #Sprite of Hermione's upper body.
                        $ h_xpos=140 #Defines position of the Hermione's full length sprite. (Default 370). (Center: 140)
                        show screen hermione_main
                        with d3
                        play music "music/Chipper Doodle v2.mp3" fadein 1 fadeout 1 # HERMIONE'S THEME.
                        her "..........."
                        hide screen hermione_main
                        with d3
                        $ h_body = "03_hp/13_hermione_main/body_81.png" #Sprite of Hermione's upper body.
                        $ h_xpos=140 #Defines position of the Hermione's full length sprite. (Default 370). (Center: 140)
                        show screen hermione_main
                        with d3
                        her "В последнее время вы частенько говорите разные неуместные вещи, профессор."
                        
                    "\"Хм... Видел и лучше.\"":
                        $ mad += 7
                        her "Арх..."
                        her "Теперь мы закончили?"

            elif whoring >= 12: # LEVEL 05 # <=================================================================================== THIRD EVENT.
                pause
                menu:
                    "\"У тебя отличные сиськи, девочка.\"":
                        hide screen hermione_main
                        with d3
                        $ h_body = "03_hp/13_hermione_main/body_82.png" #Sprite of Hermione's upper body.
                        $ h_xpos=140 #Defines position of the Hermione's full length sprite. (Default 370). (Center: 140)
                        show screen hermione_main
                        with d3
                        her "Вы правда так думаете профессор?"
                        hide screen hermione_main
                        with d3
                        $ h_body = "03_hp/13_hermione_main/body_84.png" #Sprite of Hermione's upper body.
                        $ h_xpos=140 #Defines position of the Hermione's full length sprite. (Default 370). (Center: 140)
                        show screen hermione_main
                        with d3
                        her "Мне приятно,что вам они нравятся, сэр..."
                    "\"Your tits are alright I suppose...\"":
                        hide screen hermione_main
                        with d3
                        $ h_body = "03_hp/13_hermione_main/body_82.png" #Sprite of Hermione's upper body.
                        $ h_xpos=140 #Defines position of the Hermione's full length sprite. (Default 370). (Center: 140)
                        show screen hermione_main
                        with d3
                        her "А?"
                        her "Это значит что они вам не нравятся, сэр?"
                        hide screen hermione_main
                        with d3
                        $ h_body = "03_hp/13_hermione_main/body_85.png" #Sprite of Hermione's upper body.
                        $ h_xpos=140 #Defines position of the Hermione's full length sprite. (Default 370). (Center: 140)
                        show screen hermione_main
                        with d3
                        her "Мне жаль..."
            ">Вы смотрите на ее грудь немного подольше..."
            pause
            m "Ладно,ты можешь прикрыться, девочка..."
            her "............."
            hide screen hermione_main
            with d3
            $ only_upper = False #No lower body displayed. 
            show screen blkfade
            with d3
            ">Гермиона прикрылась..."
            $ badges = True # Shows layer with badges.
            hide screen chair_02 #Genie's chair.
            hide screen genie_and_tits_01
            hide screen bld1
            hide screen blktone
            show screen genie
            show screen bld1
            $ hermione_chibi_xpos = 400 #Near the desk.
            show screen hermione_02 #Hermione stands still.
            with d5

        "\"Начать дрочить.\"":
            if whoring >= 6 and whoring <= 8: # LEVEL 03 # <=================================================================================== FIRST EVENT.
                $ mad += 2
                hide screen hermione_main
                with d3
                ">Вы взяли свой член и начали дрочить..."
                show screen blkfade
                hide screen bld1
                with d3
                play music "music/Chipper Doodle v2.mp3" fadein 1 fadeout 1 # HERMIONE'S THEME.
                her_30 "Профессор?!!"
                m "Просто стойте, девочка..."
                hide screen hermione_walk_01
                hide screen genie
                hide screen bld1
                show screen chair_02 #Genie's chair.
                hide screen blkfade
                hide screen blktone
                show screen jerking_off_01
                with d5
                pause
                
                show screen bld1
                with d3
                ">Вы пялитись на сиськи Гермионы голодными глазами..."
                her_13 "Профессор, что вы...?"
                ">Вы продолжаете дрочить свой член..."
                her_12 "Профессор, нет..."
                her_12 "Вы должны... Убрать это..."
                m "Хватит трепетать девочка. Я же не трогаю тебя,?"
                her_19 "Но..."
                her_20 "Но я не соглашалась на это!"
                her_19"Я..."
                her_19 "Я думаю мне лучше уйти!"
                menu:
                    "\"Уйдешь сейчас и не получишь очков!\"":
                        $ only_upper = False
                        her_21 "После {size=+5}этого{/size}? Вы издиваетесь, сэр?"
                        her_21 "Я показала свои..."
                        her_25 ".........."
                        her_24 "Я не собираюсь показывать вам больше, профессор!"
                        show screen blkfade
                        with d3
                        ">Гермиона оттолкнула вас и прикрылась..."
                        g4 "Не смей покидать меня в таком состоянии, девочка!"
                        her_10 "Ноги моей больше не будет в вашем кабинете, сэр!"
                        g4 "Да ладно уже,скажи что нибудь грязное!Я почти кончил!"
                        her_27 "Вы ужасный человек, сэр..."
                        $ mad += 30
                        call music_block
                        jump could_not_flirt
                    "\"Ладно, ладно. На сегодня достаточно.\"":
                        $ mad +=9
                        $ only_upper = False
                        pass
                    "-Дрочить быстрее-":
                        $ mad += 35
                        $ only_upper = False
                        ">Вы начали дрочить очень быстро!"
                        her_23 "Нет,профессор,стойте!"
                        ">Вы дрочите еще быстрее!"
                        her_25 "Профессор, думаю,  я пойду..."
                        g4 "Нет,подожди,я почти кончил!"
                        show screen blkfade
                        with d3
                        her_10 "Иу! Профессор!"
                        her_10 "Я ухожу!"
                        call music_block
                        jump could_not_flirt
            elif whoring >= 9 and whoring <= 11: # LEVEL 04 # <=================================================================================== SECOND EVENT.
                hide screen hermione_main
                with d3
                ">Вы взяли свой член и начали дрочить..."
                show screen blkfade
                hide screen bld1
                with d3
                her_30 "Профессор?"
                ">Вы смотрите на сиськи Гермионы с голодными глазами..."
                hide screen hermione_walk_01
                hide screen genie
                hide screen bld1
                show screen chair_02 #Genie's chair.
                hide screen blkfade
                hide screen blktone
                show screen jerking_off_01
                with d5
                pause
                
                show screen bld1
                with d3
                her_13 "Профессор,я не соглашалась на это..."
                m "Чего ты жалуешься, девочка?"
                m "Я не трогаю тебя..."
                her_13 "Да,но вы трогаете себя, сэр."
                ">Вы подняли темп..."
                m "Просто стой, девочка."
                m "Скоро я закончу."
                her_13 ".................."
                her_12 "(Он такой большой...)"
                m "Да,вот так..."
                m "Да,с твоими голыми сиськами..."
                her_12 ".............."
                her_17 "ну, так и быть..."
                her_17 "Вы можете трогать себя, сэр..."
                her_01 "Но вы должны обещать мне не..."
                her_05 "Не... eм..."
                her_04 "Не закончить на меня..."
                her_08 "Не передо мной, сэр..."
                m "Хорошо..."
                m "Ах, ты, маленькая шлюшка. Ты дикая шлюшка!"
                her_19 "......................."
                "Вы начали дрочить свой член еще быстрее..."
                g4 "Да,ты знаешь что это! Да!"
                her_19 "................"
                show screen blkfade 
                with d3
                ">Вы собираетесь кончить..."
                menu:
                    "-Держите его, как обещали-":
                        g4 "Ох,отлично..."
                        g4 "Я думаю стоит остановиться..."
                        her_15 "..............."
                        ">Гермиона прикрыла груди..."
                    "-Кончить-":
                        #play music "music/Chipper Doodle v2.mp3" fadein 1 fadeout 1 # HERMIONE'S THEME.
                        g4 "Aргх! Ты шлюшка!"
                        her_21 "Профе-- ??"
                        show screen white 
                        pause.1
                        hide screen white
                        pause.2
                        show screen white 
                        pause .1
                        hide screen white
                        with hpunch
                        g4 "Aргх! ДА!"
                        hide screen bld1
                        with d3
                        $ no_blinking = True #When True - blinking animation is not displayed. 
                        show screen jerking_off_cum
                        hide screen blkfade
                        hide screen bld1
                        with d3
                        pause
                        show screen bld1
                        with d3
                        her_23 "Профессор, нет, вы обещали!"
                        g4 "Ох, это здорово, да..."
                        $ no_blinking = False #When True - blinking animation is not displayed. 
                        hide screen jerking_off_cum
                        with d3
                        her_10 "Профессор, как вы могли...?"
                        m "Ох, это было очень классно..."
                        show screen blktone8
                        with d3
                        $ badges = False # Turns off badges from hermione_main screen.
                        $ sperm_on_tits = True
                        $ h_body = "03_hp/13_hermione_main/body_85.png" #Sprite of Hermione's upper body.
                        show screen hermione_main
                        with d3
                        pause
                        her "Моя форма..."
                        her "Испорчена...."
                        m "Не беспокойся, я дам тебе очки факультета, девочка."
                        m "Вы сделала мне  хорошо."
                        her "................"
                        her "Мне нужно очистить себя..."
                        hide screen hermione_main
                        with d3
                        show screen blkfade
                        with d3
                        show screen genie
                        hide screen jerking_off_01
                        hide screen chair_02
                        show screen hermione_02
                        with d3
                        $ sperm_on_tits = False
                        $ only_upper = False
                        $ aftersperm = True
                        $ h_body = "03_hp/13_hermione_main/body_47.png" #Sprite of Hermione's upper body.
                        hide screen blkfade
                        with d5
                        
                        $ badges = True # Turns badges back on from hermione_main screen.
                        
                        show screen hermione_main
                        with d3
                        pause
                        #play music "music/Chipper Doodle v2.mp3" fadein 1 fadeout 1 # HERMIONE'S THEME.
                        her "Как вы могли сделать это, сэр?!"
                        her "Вы дали слово!"
                        hide screen hermione_main
                        with d3
                        $ mad += 45
            elif whoring >= 12: # LEVEL 05 # <=================================================================================== THIRD EVENT.
                hide screen hermione_main
                with d3
                ">Вы берете свой член и начинаете дрочить..."
                show screen blkfade
                hide screen bld1
                with d3
                her_06 "Профессор?"
                ">Вы смотрите на сиськи Гермионы с голодными глазами..."
                hide screen hermione_walk_01
                hide screen genie
                hide screen bld1
                show screen chair_02 #Genie's chair.
                hide screen blkfade
                hide screen blktone
                show screen jerking_off_01
                with d5
                pause
                
                show screen bld1
                with d3
                her_13 "Профессор, я  не соглашалась на это..."
                m "Чего ты жалуешься, девочка?"
                m "Я тебя не трогаю..."
                her_13 "Да, но вы... трогаете себя, сэр."
                #">You pick up the pace..."
                m "Просто стой, сука."
                m "Я скоро кончу."
                her_13 ".................."
                m "Да... да, вот так..."
                m "Да,твои сисечки..."
                her_12 ".............."
                her_17 "ну, так и быть..."
                her_01 "Но вы должны мне пообещать..."
                her_05 "Не... Эм..."
                her_04 "Не кончать..."
                her_04 "Не передо мной, сэр..."
                m "Хорошо..."
                m "Ах, ты, маленькая шлюшка. Ты грязная шлюшка!"
                her_12 "......................."
                ">Вы начинаете дрочить еще быстрее..."
                g4 "Да, я знаю, ты хочешь этого! Да!"
                her_12 "................"
                show screen blkfade 
                with d3
                 # SAME AS PREVIOUS EVENT^^^
                menu:
                    g4 "Aргх! (Я кончаю!)"
                    "-Сдержать обещание-":
                        g4 "Ох,ладно..."
                        g4 "Думаю лучше остановиться..."
                        her_12 "..............."
                        her_12 "Эм... Я читала,что это плохо для мужчин, сэр..."
                        m "А?"
                        her_13 "Это плохо для вашего здоровья сдерживать себя..."
                        her_12 "Eм..."
                        her_14 "Если вы хотите вы можете--"
                        g4 "Aргх! Ты шлюшка!"
                        her_07 "???"
                        show screen white 
                        pause.1
                        hide screen white
                        pause.2
                        show screen white 
                        pause .1
                        hide screen white
                        with hpunch
                        g4 "Aргх! ДА!"
                        hide screen bld1
                        with d3
                        $ no_blinking = True #When True - blinking animation is not displayed. 
                        show screen jerking_off_cum
                        hide screen blkfade
                        hide screen bld1
                        with d3
                        pause
                        show screen bld1
                        with d3
                        her_09 "Профессор, я не имел в виду, что вы можете ... кончить на меня, сэр..."
                        g4 "Ох, это здорово, да..."
                        $ no_blinking = False #When True - blinking animation is not displayed. 
                        hide screen jerking_off_cum
                        with d3
                        her_18 "Ну, что сделано, то сделано, я полагаю..."
                        m "Ох, это было очень классно..."
                        show screen blktone8
                        with d3
                        $ sperm_on_tits = True
                        $ h_body = "03_hp/13_hermione_main/body_85.png" #Sprite of Hermione's upper body.
                        $ badges = False # Hides any badges from hermione_main screen.
                        show screen hermione_main
                        with d3
                        pause
                        her "Моя форма испачкана..."
                        m "Не беспокойся, я дам тебе очки для факультета, девочка."
                        m "Ты сделала мне хорошо."
                        hide screen hermione_main
                        with d3
                        $ h_body = "03_hp/13_hermione_main/body_84.png" #Sprite of Hermione's upper body.
                        show screen hermione_main
                        with d3
                        her "Спасибо сэр."
                        hide screen hermione_main
                        with d3
                        $ h_body = "03_hp/13_hermione_main/body_83.png" #Sprite of Hermione's upper body.
                        show screen hermione_main
                        with d3
                        her "Теперь мне нужно, чтобы очистить себя..."
                        pause
                        hide screen hermione_main
                        with d3
                        show screen blkfade
                        with d3
                        show screen genie
                        hide screen jerking_off_01
                        hide screen chair_02
                        show screen hermione_02
                        $ badges = True # Shows badges on hermione_main screen.
                        $ sperm_on_tits = False
                        $ only_upper = False
                        $ aftersperm = True
                        $ h_body = "03_hp/13_hermione_main/body_45.png" #Sprite of Hermione's upper body.
                        hide screen blkfade
                        with d5
                        show screen hermione_main
                        pause
                        her "Ну, это следует сделать сейчас..."
                        hide screen hermione_main
                        with d3
                    "-Кончить-":
                        g4 "Aргх! Ты шлюшка!"
                        her_07 "???"
                        show screen white 
                        pause.1
                        hide screen white
                        pause.2
                        show screen white 
                        pause .1
                        hide screen white
                        with hpunch
                        g4 "Aргх! Да!"
                        hide screen bld1
                        with d3
                        $ no_blinking = True #When True - blinking animation is not displayed. 
                        show screen jerking_off_cum
                        hide screen blkfade
                        hide screen bld1
                        with d3
                        pause
                        show screen bld1
                        with d3
                        her_13 "aх...{image=textheart.png} Так горячо...{image=textheart.png}"
                        her_09 "Профессор,вы обещали..."
                        g4 "Ох, это здорово, да..."
                        $ no_blinking = False #When True - blinking animation is not displayed. 
                        hide screen jerking_off_cum
                        with d3
                        her_15 "Ну, что сделано, то сделано, я полагаю..."
                        m "Ох, это было довольно классно.."
                        show screen blktone8
                        with d3
                        $ badges = False # Hides any badges from hermione_main screen.
                        $ sperm_on_tits = True
                        $ h_body = "03_hp/13_hermione_main/body_85.png" #Sprite of Hermione's upper body.
                        show screen hermione_main
                        with d3
                        pause
                        her "Моя форма испачкана..."
                        m "Не беспокойся, я дам тебе очки факультета, девочка."
                        m "Ты сделала мне хорошо."
                        hide screen hermione_main
                        with d3
                        $ h_body = "03_hp/13_hermione_main/body_84.png" #Sprite of Hermione's upper body.
                        show screen hermione_main
                        with d3
                        her "Спасибо сэр."
                        hide screen hermione_main
                        with d3
                        $ h_body = "03_hp/13_hermione_main/body_83.png" #Sprite of Hermione's upper body.
                        show screen hermione_main
                        with d3
                        her "Теперь я должна себя очистить..."
                        pause
                        hide screen hermione_main
                        with d3
                        show screen blkfade
                        with d3
                        show screen genie
                        hide screen jerking_off_01
                        hide screen chair_02
                        show screen hermione_02
                        $ badges = True # Turns the badges layer back on.
                        $ sperm_on_tits = False
                        $ only_upper = False
                        $ aftersperm = True
                        $ h_body = "03_hp/13_hermione_main/body_45.png" #Sprite of Hermione's upper body.
                        hide screen blkfade
                        with d5
                        $ badges = True # Hides any badges from hermione_main screen.
                        show screen hermione_main
                        pause
                        her "Ну, это следует сделать сейчас..."
                        hide screen hermione_main
                        with d3
                        

    
    $ badges = True # Hides any badges from hermione_main screen.
    
    hide screen jerking_off_01                   
    hide screen blktone8
    hide screen ctc
    hide screen bld1
    hide screen groping_01
    hide screen groping_02
    show screen hermione_02
    show screen genie
    with fade
    
    hide screen blkfade
    with d3

    $ gryffindor +=current_payout
    m " \"Гриффиндор\" получает [current_payout] очков!"
    stop music fadeout 10.0

   
   
    $ hermione_chibi_xpos = 400 #Near the desk.
    show screen hermione_02 #Hermione stands still.
    show screen bld1
    hide screen blkfade
    with Dissolve(1)
    
    $ h_xpos=370 #Defines position of the Hermione's full length sprite.
    $ h_ypos=0
    $ h_body = "03_hp/13_hermione_main/body_29.png" #Sprite of Hermione's upper body.
    show screen hermione_main
    with d3
    her ".................."
    her "Спасибо сэр..."
    if daytime:
        her "Теперь, если Вы не возражаете, я лучше пойду. Мои занятия начинаются."
    else:
        her" Я лучше пойду сейчас. Пока не слишком поздно..."
    
    if whoring >= 6 and whoring <= 8:
        $ level = "03"
        $ new_request_08_01 = True # HEARTS.
    if whoring >= 9 and whoring <= 11:
        $ level = "04"
        $ new_request_08_02 = True # HEARTS.
    if whoring >= 12:
        $ level = "05"
        $ new_request_08_03 = True # HEARTS.

    hide screen bld1
    hide screen hermione_main
    with Dissolve(.3)
    $ walk_xpos=400 #Animation of walking chibi. (From)
    $ walk_xpos2=610 #Coordinates of it's movement. (To)
    $ hermione_speed = 02.0 #The speed of moving the walking animation across the screen.
    show screen hermione_walk_01_f 
    pause 2
    hide screen hermione_walk_01_f 
    $ hermione_chibi_xpos = 610 #Near the desk.
    show screen hermione_01_f #Hermione stands still.
    with Dissolve(.3)    
        
    if whoring >= 6 and whoring <= 8: # LEVEL 03 # <=================================================================================== FIRST EVENT.    
        her_12 "(Как унизительно... кем я стала...?)"
        $ renpy.play('sounds/door.mp3') #Sound of a door opening.
        hide screen hermione_01_f #Hermione stands still.
        with Dissolve(.3)
    elif whoring >= 9 and whoring <= 11: # LEVEL 04 # <=================================================================================== SECOND EVENT.
        her_12 "........................"
        $ renpy.play('sounds/door.mp3') #Sound of a door opening.
        hide screen hermione_01_f #Hermione stands still.
        with Dissolve(.3)  
    elif whoring >= 12: # LEVEL 05 # <=================================================================================== THIRD EVENT.
        her_06 "{size=-5}(Как унизительно...){/size}"
        her_24 "{size=-5}(Нет, Гермиона, ты глупая девочка!){/size}"
        her_24 "{size=-5}(Мы делаем это, чтобы защитить честь нашего факультета!){/size}"
        her_19 "................................."
        $ renpy.play('sounds/door.mp3') #Sound of a door opening.
        hide screen hermione_01_f #Hermione stands still.
        with Dissolve(.3)  
    else:
        $ renpy.play('sounds/door.mp3') #Sound of a door opening.
        hide screen hermione_01_f #Hermione stands still.
        with Dissolve(.3)  


        
    if whoring <= 8:
        $ whoring +=1
        

    $ request_08_points += 1
        
    $ aftersperm = False #Shows cum stains on Hermione's uniform.
    
    call music_block
    
    if daytime:
        $ hermione_takes_classes = True
        jump day_main_menu
    else:
        $ hermione_sleeping = True
        jump night_main_menu
    
    
###################REQUEST_09 (Level 03) (Show me pussy).###############################################################################################
label new_request_09: #LV.3 (Whoring = 6 - 8)
    hide screen hermione_main 
    with d3
    if request_09_points == 0:
        m "{size=-4}(Попросить девочку, показать мне свою киску?){/size}"
    else:
        m "{size=-4}(Попросить девочку, показать мне свою киску еще раз?){/size}"
    $ menu_x = 0.5 #Default position of the menu (0.5). Version B is $ menu_x = 0.2
    menu:
        "\"(Да, пусть покажет!)\"":
            show screen blktone
            with d3
            pass
        "\"(Не сейчас.)\"":
            jump new_personal_request
    
    
    if request_09_points == 0 and whoring <= 11: # LEVEL 04 # FIRST TIME.
        m "Мисс Грейнджер..."
        m "Сегодняшняя награда для факультета \"Гриффиндора\" 25 очков."
        hide screen hermione_main
        with d3
        $ h_body = "03_hp/13_hermione_main/body_03.png" #Sprite of Hermione's upper body.
        $ h_xpos=370 #Defines position of the Hermione's full length sprite. (Default 370). (Center: 140)
        show screen hermione_main
        with d3
        her "Правда?"
        her "Спасибо,это так много, сэр!"
        m "Да, но мне потребуется ваша помощь..."
        her "Конечно, сэр! Что угодно!"
        m "Поднимите юбку..."
        her "...?"
        m "Спустите трусики..."
        her "?!!"
        m "И покажи свою киску!"
        if whoring <=5:
            jump too_much
        her "Профессор Дамблдор!"
        her "Это совершенно новый уровень неуместным, даже для вас, сэр!"
        her "Как можно просить такие вещи вашей ученицы?"
        m "Так вот, как тыы себя чувствущь? Я вижу..."
        m "Тогда я думаю, наградить другие дома..."
        m "\"Слизерин\" ?"
        her "................"
        m "Но ты знаешь,..."
        her "Профессор..."
        her "Судьба моего факультета для меня очень важна..."
        m "Неужели?"
        m "Почему тогда ты не покажешь её мне?"
        m "Да. Покажите мне, как это для вас важно, Мисс Грейнджер."
        her "Но это не просто..."
        m "У нас нет времени  обсуждать, что уместно, а что нет, Мисс Грейнджер?"
        her ".................."
        m "Я бы сказал, что корабль уплыл..."
        her ".............."
        m "Все, что я хочу сделать, это быстро посмотреть..."
        her "Но почему? Почему я должена делать это, сэр?"
        m "Минуту вашего времени и \"Гриффиндор\" получает 25 очков..."
        m "Очень хорошее сделка, разве вы не согласны?"
        her "Я подумаю..."
    else:
        m "Мисс Грейнджер?"
        her "Да..."
        m "Мне нужно увидеть вашу киску..."
        if whoring >= 6 and whoring <= 8: #LEVEL 03 <=========================================================================================== FIRST EVENT
            her "Aргх... Только не опять, сэр..."
            her "{size=-5}...так стыдно...{/size}"
            m "25 очков, Мисс Грейнджер..."
            her ".............."
        if whoring >= 9 and whoring <= 11: #LEVEL 04 <=========================================================================================== SECOND EVENT
            her "*Вздох*... Если только..."      
        if whoring >= 12 and whoring <= 14: # LEVEL 05 <=========================================================================================== THIRD EVENT
            her "Неужели?"
            her "Ну ладно..."

  
#    if whoring >= 6 and whoring <= 8: #LEVEL 03 <=========================================================================================== FIRST EVENT

#    if whoring >= 9 and whoring <= 11: #LEVEL 04 <=========================================================================================== SECOND EVENT
  
#    if whoring >= 12 and whoring <= 14: # LEVEL 05 <=========================================================================================== THIRD EVENT
    

        
    
    
    
    
    if whoring <=5:
        jump too_much
        

        
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    m "Покажи мне свою киску..."
    if request_09_points == 0: #One star.
        her "Oх... "
        ">Гермиона тянет  вверх ее юбку и тянет вниз трусики. Она покраснела и выглядит сердитой."
    
    elif request_09_points == 1: #Two stars.
        her "...Да, профессор."
        ">Гермиона тянет  вверх ее юбку и тянет вниз трусики. Она выглядит нетерпеливой."
        
    elif request_09_points == 2: #Three stars.
        her "Конечно, сэр..."
        ">Гермиона тянет  вверх ее юбку и тянет вниз трусики.Она выглядит игривой."
        
    elif request_09_points >= 3: #Master.
        her "Here you go, Headmaster."
        ">Гермиона тянет  вверх ее юбку и тянет вниз трусики. Они вам улыбается."
    
    "Вы отпускаете Гермиону."
        
    if whoring <= 8:
        $ whoring +=1

    if request_09_points <= 2:
        $ gryffindor +=25
        "Гриффиндор получил +25 очков."
    else:
        $ gryffindor +=7
        "Гриффиндор получил  +7 очков."
       
    $ request_09_points += 1
    
    if daytime:
        $ hermione_takes_classes = True
        jump day_main_menu
    else:
        $ hermione_sleeping = True
        jump night_main_menu    
    

    
##################################################################################################################################
### LEVEL 04 #####################################################################################################################
###################REQUEST_11 (Level 04) (DANCE FOR ME AND SNAPE) (Day/Night) ################################################################
label new_request_11: #LV.4 (Whoring = 9 - 11)
    hide screen hermione_main 
    with d3
   
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

    if request_11_points == 0: #<==============================EVENT 01
        
        m "Мисс Грейнджер, не могли бы вы станцевать для меня."
        hide screen hermione_main
        with d3
        $ h_body = "03_hp/13_hermione_main/body_11.png" #Sprite of Hermione's upper body.
        $ h_xpos=140 #Defines position of the Hermione's full length sprite. (Default 370). (Center: 140)
        show screen hermione_main
        with d3
        her "Вы хотите, чтобы я..."
        hide screen hermione_main
        with d3
        $ h_body = "03_hp/13_hermione_main/body_10.png" #Sprite of Hermione's upper body.
        $ h_xpos=140 #Defines position of the Hermione's full length sprite. (Default 370). (Center: 140)
        show screen hermione_main
        with d3
        her "...танцевала для вас, сэр?"
        if whoring <=8:
            jump too_much
        $ new_request_11_01 = True # HEARTS
        m "Да... вы думаете, вы могли справиться с этим?"
        her "Эм... Я попробую..."
        hide screen hermione_main
        with d3
        $ h_body = "03_hp/13_hermione_main/body_11.png" #Sprite of Hermione's upper body.
        $ h_xpos=140 #Defines position of the Hermione's full length sprite. (Default 370). (Center: 140)
        show screen hermione_main
        with d3
        her "Это ваш официальное предложение, сэр?"
        with hpunch
        g4 "Что ты сказала!?"
        stop music fadeout 1.0
        hide screen hermione_main
        with d3
        $ h_body = "03_hp/13_hermione_main/body_12.png" #Sprite of Hermione's upper body.
        $ h_xpos=140 #Defines position of the Hermione's full length sprite. (Default 370). (Center: 140)
        show screen hermione_main
        with d3
        her "Я имею в виду, пользу. Это в пользу школы сэр?"
        show screen whitetone8
        hide screen blktone
        with Dissolve(1)
        hide screen hermione_main
        with Dissolve(1)
        g4 "(\"Это вашt официальный желние, мастер....?\")"
        m "(О, это  вызывает воспоминания...)"
        m "(Аграба и Джини...)"
        m "(Пре-акабурная эра моей жизни...)"
        m "(Неплохие времена...)"
        g4 "(Сволочь, испортил мне жизнь!)"
        her "Eм... Профессор?"
        hide screen whitetone8
        with Dissolve(1)
        show screen hermione_main
        with d3
        call music_block
        her "сэр..?"
        m "Так Гермиона..."
        m "Я предался воспоминаниям..."
        her "Я получу за это награду?"
        m "Конечно, девочка!"
        hide screen hermione_main
        with d3
        $ h_body = "03_hp/13_hermione_main/body_29.png" #Sprite of Hermione's upper body.
        $ h_xpos=140 #Defines position of the Hermione's full length sprite. (Default 370). (Center: 140)
        show screen hermione_main
        with d3
        her "Так... я просто немного потанцую..."
        m "Когда будешь готова..."
        her "................."
        hide screen hermione_main
        with d3
        ">Гермиона начинает танцевать..."
        stop music fadeout 1.0
        hide screen blktone
        $ hermione_chibi_xpos = 400 #Near the desk.
        #$ hermione_chibi_ypos = 240 #Default: 250
        show screen clothed_dance #Hermione stands still.
        with fade
        m "Хм..."
        her_12 "{size=-5}(...........................................){/size}"
        her_04 "{size=-5}(Это глупо...){/size}"
        ">Гермиона выглядит растерянным, но она продолжает \"танцы\"..."
        m "..................."
        her_04 "{size=-5}(...........................................){/size}"
        m "Отлично,теперь можешь начинать раздеваться."
        show screen hermione_02 #Hermione stands still.
        with hpunch
        her_07 "??!"
        her_08 "Мы же договаривались только о танце?"
        play music "music/(Orchestral) Playful Tension by Shadow16nh.mp3" fadein 1 fadeout 1 # SEX THEME.
        m "В самом деле? Вот обидно."
        m "Теперь начать снимать свою одежду."
        her_12 "Вы хотете чтобы я станцевала вам стриптиз...?"
        m "Да. И я ожидаю, что ты сделаешь это сегодня, девочка."
        her_19 "Профессор Дамблдор!"
        m "Не повышай свой голос на меня, девочка!"
        her_07 ".....!!?"
        m "Никто не заставляет вас делать это."
        m "Я делаю вам одолжение!"
        m "Если вам не нужны очки, пожалуйста, не задерживайтесь в кабинете."
        her_08 "....................."
        her_12 "......................................."
        ">Гермиона начинает танцевать снова..."
        show screen clothed_dance #Hermione stands still.
        with fade
        her_15 "{size=-5}(...........................................){/size}"
        m "Чего же вы ждете?"
        m "Начнем с жилета."
        her_12 "............................................................."
        ">Гермиона делает растерянный вид, а затем снимает с себя жилет..."
        show screen ctc
        pause
        show screen no_vest_dance
        with d3
        pause
        her_19 "{size=-5}(Я действительно собираюсь сделать это?){/size}"
        menu:
            m "......................."
            "\"Теперь избавиться от юбки!\"":
                her_19 "................................."
                show screen blktone
                with d3
                ">Гермиона начинает растегивать свою юбка..."
                ">Она, кажется очень нерешительной и немного мешкается ..."
                ">Наконец молния внизу и у нее нет выбора,  чтобы не снять юбку..."
                hide screen blktone
                with d3
                her_19 "{size=-5}(Вот и она...){/size}"
                her_24 "{size=-5}(За честь \"Гриффиндора\"....){/size}"
                ">Гермиона сняла свою юбку..."
                show screen ctc
                pause
                show screen no_skirt_dance
                with d3
                pause
                m "..............."
                her_19 "{size=-5}(.........................................){/size}"
                ">Гермиона продолжает танцевать..."
                m "Ладно, рубашка следующая!"
                her_20 "Моя рубашка....?"
                show screen blktone
                with d3
                ">Гермиона выглядит крайне неловко..."
                ">Она неуклюже копошится с пуговицами  рубашки..."
                hide screen blktone
                with d3
                m "В чем проблема, девочка?"
                her_19 "Мне жаль, сэр..."
                her_19 "Оно застряло..."
                her_19 "И не хочет выйти..."
                her_28 "Почему не двигается?! *хлюп*"
                her_28 "Нет,я не могу сделать этого, сэр! *хлюп*"
                m "Что?"
                her_28 "Я думал, я мог бы, но..."
                her_28 "Станцевать стриптиз, сэр?"
                her_28 "Люди смотрят на меня в этой школе!"
                her_28 "У меня репутация...*хлюп*"
                her_29 "And if I do this..."
            "\"Сейчас же сними рубашку!\"":
                her_19 "................................."
                show screen blktone
                with d3
                ">Гермиона начинает расстегивать свою рубашку..."
                ">Она, кажется, очень нерешительой и тянет  время..."
                ">Наконец, последняя пуговица снята, и у нее нет выбора, чтобы не снять рубашку..."
                hide screen blktone
                with d3
                her_19 "{size=-5}(Ладно,показываю...){/size}"
                her_19 "{size=-5}(За честь \"Гриффиндора\"!){/size}"
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
                her_40 "{size=-5}(Я сделала это...){/size}"
                her_40 "{size=-5}(Профессор Дамблдор видит мою грудь пока я танцую...){/size}"
                her_40 "{size=-5}(Это так унизительно...){/size}"
                her_40 "{size=-5}(Но я делаю это для моего факультета...){/size}"
                m "Неплохо...."
                her_40 "{size=-5}(.........................................){/size}"
                show screen blktone
                with d3
                ">Гермиона топлес..."
                ">Она продолжает танцевать, но, кажется, она очень ограничена в движениях. Даже больше, чем раньше..."
                ">Похоже, она отчаянно пытается предотвратить покачивания и подпрыгивания её груди.."
                hide screen blktone
                with d3
                m "Ладно,юбка следующая!"
                her_40 "...................."
                show screen blktone
                with d3
                ">Гермиона выглядит крайне неловко..."
                show screen blktone8
                with d3
                ">Она пытается расстегнуть молнию на юбке..."
                m "Какие-то проблемы, девочка?"
                her_40 "Мне жаль, сэр..."
                her_40 "Она застраляа..."
                her_40 "Не сдвигается..."
                her_40 "Почему она не двигается *плачет*"
                her_41 "Нет, Я не могу, сэр! *плачет*"
                m "Что?"
                her_41 "Я думала, что смогу, но..."
                her_41 "Стриптиз за очки, сэр?"
                her_41 "Люди ровняются на меня в этой школе!"
                her_41 "У меня есть репутация...*плачет*"
                her_42 "И если я это сделаю..."
                
        show screen blkfade 
        with d3
        hide screen blktone8    
        ">Гермиона быстро снимается свою форму..."
        stop music fadeout 1.0
        show screen hermione_02 #Hermione stands still.
        hide screen blkfade
        with d3
        her_31 "сэр, я думаю мне стоит уйти... *плачет!*"
        menu:
            "\"Ладно. Мне было весело. Вот твои очки.\"":
                $ hermione_main_zorder = 8 #Zorder of the screen hermione_main. 5 puts it on top of everything but behind the speech box.
                $ h_xpos=390 #Defines position of the Hermione's full length sprite. (Default 370). 140 - center.
                $ h_ypos=340 #Defines position of the Hermione's full length sprite. (Default 0). Right bottom corner: 340
                $ h_body = "03_hp/13_hermione_main/body_13.png" #Flashing Трусики
                show screen hermione_main
                her "Правда? Я ничего не испортила?"
                hide screen hermione_main
                pause.2 #Otherwise a bug occurs. 
                $ hermione_main_zorder = 5 #Zorder of the screen hermione_main. 5 puts it on top of everything but behind the speech box.
                $ h_ypos=0 #Defines position of the Hermione's full length sprite. (Default 0). Right bottom corner: 340
            "\"Конечно. И ты не получишь очки.\"":
                play music "music/Chipper Doodle v2.mp3" fadein 1 fadeout 1 # HERMIONE'S THEME.
                $ hermione_main_zorder = 8 #Zorder of the screen hermione_main. 5 puts it on top of everything but behind the speech box.
                $ h_xpos=390 #Defines position of the Hermione's full length sprite. (Default 370). 140 - center.
                $ h_ypos=340 #Defines position of the Hermione's full length sprite. (Default 0). Right bottom corner: 340
                $ h_body = "03_hp/13_hermione_main/body_02.png" #Flashing Трусики
                show screen hermione_main
                her "сэр... Мне кажется я не очень хороша в этом..."
                her "НО я сделала все, что смогла... Я думаю, я заслужила--"
                hide screen hermione_main
                m "Просто в следующий раз постарайтесь лучше, Мисс Грейнджер."
                $ h_body = "03_hp/13_hermione_main/body_31.png" #Flashing Трусики
                show screen hermione_main
                her "Следующий раз?!"
                $ h_body = "03_hp/13_hermione_main/body_47.png" #Flashing Трусики
                her2 "Уверяю вас, сэр, следующего раза не будет..."
                hide screen hermione_main
                m "Посмотрим..."
                $ h_body = "03_hp/13_hermione_main/body_66.png" #Flashing Трусики
                show screen hermione_main
                her "Арх!"
                hide screen hermione_main
                pause.2 #Otherwise a bug occurs. 
                $ hermione_main_zorder = 5 #Zorder of the screen hermione_main. 5 puts it on top of everything but behind the speech box.
                $ h_ypos=0 #Defines position of the Hermione's full length sprite. (Default 0). Right bottom corner: 340
                $ mad += 35
                call music_block
                jump could_not_flirt

    if request_11_points == 1: #<====================================================================================================================EVENT 02 
        $ new_request_11_02 = True # HEARTS
        m "Мисс Грейнджер, я хочу, чтобы вы станцевали для меня."
        hide screen hermione_main
        with d3
        $ h_body = "03_hp/13_hermione_main/body_66.png" #Sprite of Hermione's upper body.
        $ h_xpos=140 #Defines position of the Hermione's full length sprite. (Default 370). (Center: 140)
        show screen hermione_main
        with d3
        her "Снова, сэр...?"
        m "Все будет оплачено, конечно же..."
        hide screen hermione_main
        with d3
        $ h_body = "03_hp/13_hermione_main/body_69.png" #Sprite of Hermione's upper body.
        $ h_xpos=140 #Defines position of the Hermione's full length sprite. (Default 370). (Center: 140)
        show screen hermione_main
        with d3
        her "............................"
        hide screen hermione_main
        with d3
        $ h_body = "03_hp/13_hermione_main/body_69.png" #Sprite of Hermione's upper body.
        show screen hermione_main
        with d3
        her "И вы ожидаете от меня... Эм..."
        m "Снимай свою одежду. Конечно же."
        hide screen hermione_main
        with d3
        $ h_body = "03_hp/13_hermione_main/body_69.png" #Sprite of Hermione's upper body.
        $ h_xpos=140 #Defines position of the Hermione's full length sprite. (Default 370). (Center: 140)
        show screen hermione_main
        with d3
        stop music fadeout 1.0
        her "......................"
        hide screen hermione_main
        with d3
        $ h_body = "03_hp/13_hermione_main/body_66.png" #Sprite of Hermione's upper body.
        $ h_xpos=140 #Defines position of the Hermione's full length sprite. (Default 370). (Center: 140)
        show screen hermione_main
        with d3
        play music "music/Chipper Doodle v2.mp3" fadein 1 fadeout 1 # HERMIONE'S THEME.
        her "Ну, почему нет?"
        hide screen hermione_main
        with d3
        $ h_body = "03_hp/13_hermione_main/body_86.png" #Sprite of Hermione's upper body.
        $ h_xpos=140 #Defines position of the Hermione's full length sprite. (Default 370). (Center: 140)
        show screen hermione_main
        with d3
        her "Да, и правда, почему бы и нет!"
        m "Хм...? {size=-4}(Посмотрите на нее. Такая энергичная...){/size}"
        hide screen hermione_main
        with d3
        $ h_body = "03_hp/13_hermione_main/body_30.png" #Sprite of Hermione's upper body.
        $ h_xpos=140 #Defines position of the Hermione's full length sprite. (Default 370). (Center: 140)
        show screen hermione_main
        with d3
        her "В конце концов, как ученица, я должна подчиняться любому вашему приказу, не так ли, сэр?!"
        m "...................."
        hide screen hermione_main
        with d3
        $ h_body = "03_hp/13_hermione_main/body_30.png" #Sprite of Hermione's upper body.
        $ h_xpos=140 #Defines position of the Hermione's full length sprite. (Default 370). (Center: 140)
        show screen hermione_main
        with d3
        her "Если деректор говорит мне раздеться, то значит я сделаю это!!!"
        hide screen hermione_main
        with d3
        $ h_body = "03_hp/13_hermione_main/body_47.png" #Sprite of Hermione's upper body.
        $ h_xpos=140 #Defines position of the Hermione's full length sprite. (Default 370). (Center: 140)
        show screen hermione_main
        with d3
        her "Даже если это неуместно, позорно, и унизительно?"
        hide screen hermione_main
        with d3
        $ h_body = "03_hp/13_hermione_main/body_30.png" #Sprite of Hermione's upper body.
        $ h_xpos=140 #Defines position of the Hermione's full length sprite. (Default 370). (Center: 140)
        show screen hermione_main
        with d3
        her "Конечно нет. Какой вздор!"
        m ".............."
        hide screen hermione_main
        with d3
        $ h_body = "03_hp/13_hermione_main/body_47.png" #Sprite of Hermione's upper body.
        $ h_xpos=140 #Defines position of the Hermione's full length sprite. (Default 370). (Center: 140)
        show screen hermione_main
        with d3
        her "Ха! Все ведь как и должно быть!"
        hide screen hermione_main
        with d3
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
        $ hermione_main_zorder = 8 #Zorder of the screen hermione_main. 5 puts it on top of everything but behind the speech box.
        $ h_xpos=390 #Defines position of the Hermione's full length sprite. (Default 370). 140 - center.
        $ h_ypos=340 #Defines position of the Hermione's full length sprite. (Default 0). Right bottom corner: 340
        $ h_body = "03_hp/13_hermione_main/body_30.png" #Flashing Трусики
        show screen hermione_main
        her2 "Я должна немного опуститься, чтобы защитить честь своего факультета..."
        hide screen hermione_main
        ">Гермиона начинает снимать свой жилет..."
        $ h_body = "03_hp/13_hermione_main/body_86.png" #Flashing Трусики
        show screen hermione_main
        her "Пусть все так и будет!"
        $ h_body = "03_hp/13_hermione_main/body_87.png" #Flashing Трусики
        her "Просто..."
        $ h_body = "03_hp/13_hermione_main/body_88.png" #Flashing Трусики
        her "*стон*"
        hide screen hermione_main
        show screen blktone8
        hide screen blktone
        with d3
        ">Ее жилет, кажется, застрял. Но она продолжает тянуть его с особым усилием..."
        show screen hermione_main
        her "Почему он не....?!"
        $ h_body = "03_hp/13_hermione_main/body_81.png" #Flashing Трусики
        her "Вот!"
        hide screen hermione_main
        ">Гермионе наконец удается стянуть жилет и она кидает его в другую часть комнаты..."
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
        show screen hermione_main
        hide screen ctc
        $ h_body = "03_hp/13_hermione_main/body_30.png" #Flashing Трусики
        her "Юбка следующая, да?"
        hide screen hermione_main
       
        menu:
            m "..."
            "\"Да, именно. Снимай ее!\"":
                show screen hermione_main
                her "Конечно!"
                $ h_body = "03_hp/13_hermione_main/body_87.png" #Flashing Трусики
                her "А вот и она!"
                hide screen hermione_main
                pause.1
                show screen blktone8
                with d3
                ">Гермиона запускает свою юбку через всю комнату, как сделала с жилетом ранее..."
            "\"Тебе следует быть тише, девочка. \"":
                show screen hermione_main
                her2 "Ну, {size=+7}ПРОСТИТЕ МЕНЯ{/size}, профессор!"
                her2 "Вы попросили меня станцевать для вас, но не предупреждали насколько громкой я должна быть!"
                hide screen hermione_main
                m "Ну, я говорю это сейчас!"
                show screen hermione_main
                her2 "Слишком поздно!"
                hide screen hermione_main
                pause.1
                show screen blktone8
                with d3
                ">И конечно же, она запускает свою юбку через всю комнату, как сделала с жилетом ранее..."
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
        m "{size=-4}(Может быть еще рано для-{/size}"
        $ h_body = "03_hp/13_hermione_main/body_66.png" 
        show screen hermione_main
        her "Моя рубашка?!!"
        $ h_body = "03_hp/13_hermione_main/body_86.png" 
        her "{size=+9}Мне она не нужна!{/size}"
        hide screen hermione_main
        pause.1
        show screen blktone8
        with d5
        ">Ее рубашка внезапно падает на пол."
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
        show screen hermione_main
        hide screen ctc
        her "Вам нравится, сэр?"
        $ h_body = "03_hp/13_hermione_main/body_30.png" 
        her2 "Мне стоит потрясти сиськами, как одна из тех шлюх?"
        hide screen hermione_main
        m "Ну---"
        show screen hermione_main
        her2 "Конечно! Почему бы мне не опуститься для вашего же удовольствия?!"
        $ h_body = "03_hp/13_hermione_main/body_86.png" 
        her2 "Это вполне {size=+7}приемлимо!{/size}"
        hide screen hermione_main
        pause.1
        show screen blktone
        with d3
        ">Гермиона начинает неуклюже трясти своими сиськами..."
        ">Пока вы смотрите как сиськи этой девочки расскачиваются то влево, то в право, вам приходится бороться с сильным желанием..."
        menu:
            m "..."
            "-Схватить их!-":
                g9 "{size=-4}(Да, просто положить свои руки на эти милые сиськи, именно!){/size}"
                g9 "{size=-4}(Может чуть подергать их...){/size}"
            "-Шлепнуть!-":
                m "{size=-4}(О да, хочу шлепнуть их.){/size}"
                g9 "{size=-4}(Да, просто немного шлепнуть...){/size}"
            "-Укусить!":
                m "{size=-4}(Это странно, что я хочу впиться в них зубами?){/size}"
                m "{size=-4}(Нет, это не странно!){/size}"
                m "{size=-4}(Просто пара нежных укусов с любовью!){/size}"
                g9 "{size=-4}(Да... Может быть больше чем пара...){/size}"
            "-Забуриться в них лицом!-":
                m "{size=-4}(Я просто хочу залезть лицом между ними!){/size}"
                g9 "{size=-4}(Да, забуриться в них лицом это лучшее, что можно сделать!){/size}"
        ">Пока вы думаете, Гермиона продолжает танцевать..."
        
        $ badges = False # Turns off the badges layer.
        
        $ h_body = "03_hp/13_hermione_main/body_89.png" 
        $ hermione_main_zorder = 8 #Zorder of the screen hermione_main. 5 puts it on top of everything but behind the speech box.
        $ h_xpos=390 #Defines position of the Hermione's full length sprite. (Default 370). 140 - center. Bottom right: 390
        $ h_ypos=235 #Defines position of the Hermione's full length sprite. (Default 0). Right bottom corner: 340
        show screen hermione_main
        her2 "(Танцую голой перед директором...)"
        her2 "(Если бы мои родители узнали об этом, они бы просто сошли с ума...)"
        $ h_body = "03_hp/13_hermione_main/body_90.png"
        her2 "(Особенно отец...)"
        hide screen hermione_main
        ">Гермиона снова трясет своими грудками...)"
        show screen hermione_main
        her "(Гермиона Грейнджер - стриптизершка...)"
        $ h_body = "03_hp/13_hermione_main/body_91.png"
        her2 "(Прости меня, папочка...)"
        hide screen hermione_main
        pause.1
        show screen blktone8
        hide screen blktone
        with d3
        ">Гермиона кладет свои руки на грудь и начинает сжимать их..."
        ">Вы можете только предпологать, что у нее на уме, но выглядит она очень подавленно и стыдливо."
        show screen hermione_main
        her2 "(Я лучший студент... Я являюсь примером для других...)"
        hide screen hermione_main
        ">Гермиона сильнее хватается за сиськи и скручивает их пару раз..."
        ">Выглядит так, будто она зла на них и пытается наказать..."
        ">Вы находите это странным..."
        $ h_body = "03_hp/13_hermione_main/body_92.png"
        show screen hermione_main
        $ h_c_u_pic = "03_hp/08_animation_02/05_panties_01.png"
        show screen h_c_u
        her "Ну, я думаю вам это нравится, сэр!"
        hide screen hermione_main
        m "Что?"
        $ h_body = "03_hp/13_hermione_main/body_93.png"
        show screen hermione_main
        her "Я хотела бы получить оплату..."
        hide screen hermione_main
        m "Вы ничего не забыли, Мисс Грейнджер?"
        $ h_body = "03_hp/13_hermione_main/body_92.png"
        show screen hermione_main
        her2 "сэр...?"
        hide screen hermione_main
        m "Ваши трусики...?"
        $ h_body = "03_hp/13_hermione_main/body_94.png"
        show screen hermione_main
        her "Мои трусики?"
        her "Но, они всегда остаются!"
        hide screen hermione_main
        m "Когда это \"всегда\"?"
        m "Стриптиз в детских мультиках?"
        m "Стриптиз это стриптиз, девочка!"
        m "Теперь снимай свои трусики!"
        $ h_body = "03_hp/13_hermione_main/body_95.png"
        show screen hermione_main
        her "................"
        hide screen hermione_main
        ">Гермиона выглядит испуганно. Вся ее злоба ушла..."
        $ h_body = "03_hp/13_hermione_main/body_90.png"
        show screen hermione_main
        her "................."
        hide screen hermione_main
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
        
        $ tt_xpos=330 #Defines position of the Snape's full length sprite. (Default 300). 140 - center.
        $ tt_ypos=340#(Default 0). Right bottom corner: 340
        $ s_sprite = "03_hp/10_snape_main/snape_01.png"
        $ hermione_main_zorder = 8 #Zorder of the screen hermione_main. 5 puts it on top of everything but behind the speech box. Works for all full size sprites.
        show screen s_head
        $ h_c_u_pic = "03_hp/08_animation_02/05_panties_01.png"
        show screen h_c_u
        
        
        
        sna2 "Послушай, Джинни. Я тут подумал--"
        $ s_sprite = "03_hp/10_snape_main/snape_11.png"
        with hpunch
        sna2 "................................................................................................................................................................................"
        $ h_body = "03_hp/13_hermione_main/body_96.png"
        show screen h_head
        with hpunch
        her "(Профессор Снейп???????!)"
        $ s_sprite = "03_hp/10_snape_main/snape_12.png"
        show screen s_head
        sna2 "Мисс Грейнджер?"
        show screen h_head
        her "(Нет, нет... Этого нельзя допустить. Пожалуйста...)"
        hide screen h_head
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
                $ h_body = "03_hp/13_hermione_main/body_97.png"
                show screen h_head
                her "{size=-7}(Я хочу сдохнуть!){/size}"
                $ s_sprite = "03_hp/10_snape_main/snape_12.png"
                show screen s_head
                sna2 "Отложим наш разговор на потом, Джинн-- *Кхм!* Альбус."
                $ s_sprite = "03_hp/10_snape_main/snape_13.png"
                sna "Мисс Грейнджер..."
                $ h_body = "03_hp/13_hermione_main/body_97.png"
                show screen h_head
                her ".........................................."
                hide screen h_head
            "\"Северус! Пожалуйста, присоеденяйся.\"":
                $ mad += 37
                $ snape_invated_to_watch = True #Turns TRUE when Hermione is stripping and Snape walks in on you. Allows to invite him to watch her strip next time.
                $ s_sprite = "03_hp/10_snape_main/snape_14.png"
                show screen s_head
                sna "Серьезно?"
                $ h_body = "03_hp/13_hermione_main/body_97.png"
                show screen h_head
                her "(Профессор, нет, пожалуйста.............................)"
                $ s_sprite = "03_hp/10_snape_main/snape_13.png"
                show screen s_head
                sna "Действительно, заманчивое предложение..."
                $ h_body = "03_hp/13_hermione_main/body_95.png"
                show screen h_head
                her "!!!!!!......."
                $ s_sprite = "03_hp/10_snape_main/snape_13.png"
                show screen s_head
                sna2 "Ну, может вдругой раз..."
                $ h_body = "03_hp/13_hermione_main/body_99.png"
                show screen h_head
                her "{size=-5}(Другого раза не будет!){/size}"
                her "{size=-5}(Клянусь, я перестану продавать себя за эти гребаные очки!){/size}"
                $ s_sprite = "03_hp/10_snape_main/snape_12.png"
                show screen s_head
                sna2 "Отложим наш разговор, Джинн-- *Кхм!* Альбус."
                $ s_sprite = "03_hp/10_snape_main/snape_13.png"
                sna2 "Мисс Грейнджер..."
                $ h_body = "03_hp/13_hermione_main/body_97.png"
                show screen h_head
                her "................................."
                hide screen h_head
        show screen blkfade 
        with d3
        hide screen snape_walk_01 
        $ renpy.play('sounds/door.mp3') #Sound of a door opening.
        pause 1.5

        
        ">Снейп уходит..."
        ">Гермиона спешно спрыгивает с вашего стола."
        ">Она отчаянно пытается натянуть на себя одежду..."
        $ h_body = "03_hp/13_hermione_main/body_98.png"
        show screen h_head
        her "Моя рубашка! Где моя рубашка?!"
        hide screen h_head
        m "Там, у камина..."
        $ h_body = "03_hp/13_hermione_main/body_85.png"
        show screen h_head
        her2 "................................"
        hide screen h_head
        pause 2
        $ h_body = "03_hp/13_hermione_main/body_33.png"
        show screen h_head
        
        $ badges = True # Turns the badges layer back ON.
        
        her "........................"
        $ h_body = "03_hp/13_hermione_main/body_34.png"
        stop music fadeout 2.0
        her "Могу я получить свои очки, пожалуйста?"
        hide screen h_head
        hide screen snape_02 #Snape stands still.
        pause.1
        $ hermione_main_zorder = 5 #Zorder of the screen hermione_main. 5 puts it on top of everything but behind the speech box. On top of EVERYTHING = 8.
        $ h_ypos=0 #Defines position of the Hermione's full length sprite. (Default 0). Right bottom corner: 340
        $ hermione_chibi_xpos = 400 #Near the desk.
        show screen hermione_02 #Hermione stands still.
        $ hermione_chibi_ypos = 250 #Default: 250. Another number is 180
            
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
                        m "Мисс Грейнджер, Я хочу от вас еще одну услугу сегодня."
                        hide screen hermione_main
                        with d3
                        $ h_body = "03_hp/13_hermione_main/body_16.png" #Sprite of Hermione's upper body.
                        $ h_xpos=140 #Defines position of the Hermione's full length sprite. (Default 370). (Center: 140)
                        show screen hermione_main
                        with d3
                        her "Конечно, сэр."
                        m "Но для начала, вы не могли бы пойти и позвать профессора Снейпа сюда?"
                        hide screen hermione_main
                        with d3
                        $ h_body = "03_hp/13_hermione_main/body_17.png" #Sprite of Hermione's upper body.
                        show screen hermione_main
                        with d3
                        her "...Профессора Снейпа?"
                        her "Могу я спросить, зачем, сэр?"
                        m "Ох, Я думаю, вам нужна большая аудитория для подобных танцев."
                        hide screen hermione_main
                        with d3
                        $ h_body = "03_hp/13_hermione_main/body_48.png" #Sprite of Hermione's upper body.
                        show screen hermione_main
                        with d3
                        her "Подобных танцев...?!!"
                        hide screen hermione_main
                        with d3
                        $ h_body = "03_hp/13_hermione_main/body_47.png" #Sprite of Hermione's upper body.
                        show screen hermione_main
                        with d3
                        her "Со всем уважением, сэр..."
                        hide screen hermione_main
                        with d3
                        $ h_body = "03_hp/13_hermione_main/body_07.png" #Sprite of Hermione's upper body.
                        show screen hermione_main
                        with d3
                        her "{size=-5}(Которого уже и так мало...){/size}"
                        hide screen hermione_main
                        with d3
                        $ h_body = "03_hp/13_hermione_main/body_30.png" #Sprite of Hermione's upper body.
                        show screen hermione_main
                        with d3
                        her "Я отказываюсь унижаться перед профессором Снейпом!"
                        m "Нет, нет. Ты поняла все не так."
                        hide screen hermione_main
                        with d3
                        $ h_body = "03_hp/13_hermione_main/body_15.png" #Sprite of Hermione's upper body.
                        show screen hermione_main
                        with d3
                        her "Хм..?"
                        m "Я хочу проверить профессор Снейпа на причастность к \"грязным\" делишкам с помощью тебя."
                        hide screen hermione_main
                        with d3
                        $ h_body = "03_hp/13_hermione_main/body_48.png" #Sprite of Hermione's upper body.
                        show screen hermione_main
                        with d3
                        her "!!!"
                        m "Да, хочу поймать его на месте преступоления!"
                        hide screen hermione_main
                        with d3
                        $ h_body = "03_hp/13_hermione_main/body_11.png" #Sprite of Hermione's upper body.
                        show screen hermione_main
                        with d3
                        her "Профессор, Я не понимаю..."
                        hide screen hermione_main
                        with d3
                        $ h_body = "03_hp/13_hermione_main/body_06.png" #Sprite of Hermione's upper body.
                        show screen hermione_main
                        with d3
                        her "Теперь ясно..."
                        her "Я извиняюсь, что засомневалась в вас, сэр..."
                        m "Ничего. Теперь найди профессор Снейпа и приведи его сюда."
                        hide screen hermione_main
                        with d3
                        $ h_body = "03_hp/13_hermione_main/body_111.png" #Sprite of Hermione's upper body.
                        show screen hermione_main
                        with d3
                        her "Как скажете, сэр!"
                        label fetching_snape:
                        hide screen hermione_main
                        with d3
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
                        hide screen hermione_main
                        with d3
                        $ h_body = "03_hp/13_hermione_main/body_16.png" #Sprite of Hermione's upper body.
                        $ h_xpos=140 #Defines position of the Hermione's full length sprite. (Default 370). (Center: 140)
                        show screen hermione_main
                        with d3
                        her "Конечно, сэр."
                        m "Но для начала, вы не могли бы пойти и позвать профессора Снейпа сюда?"
                        hide screen hermione_main
                        with d3
                        $ h_body = "03_hp/13_hermione_main/body_17.png" #Sprite of Hermione's upper body.
                        show screen hermione_main
                        with d3
                        her "...Профессор Снейп?"
                        her "Могу я спросить, зачем, сэр?"
                        m "Ох, я просто хочу, чтобы ты станцевала для нас."
                        hide screen hermione_main
                        with d3
                        $ h_body = "03_hp/13_hermione_main/body_14.png" #Sprite of Hermione's upper body.
                        show screen hermione_main
                        with d3
                        her "!!!"
                        m "Я хочу проверить профессора Снейпа на причастность к \"грязным\" делишкам и ты должна мне помочь."
                        hide screen hermione_main
                        with d3
                        $ h_body = "03_hp/13_hermione_main/body_29.png" #Sprite of Hermione's upper body.
                        show screen hermione_main
                        with d3
                        her "Но разве мы не договаривались, что я делаю это в последний раз?"
                        m "Ну, Эм... конечно..."
                        m "Но мне нужны доказательства, если я хочу отправить это в министерство магии!"
                        hide screen hermione_main
                        with d3
                        $ h_body = "03_hp/13_hermione_main/body_47.png" #Sprite of Hermione's upper body.
                        show screen hermione_main
                        with d3
                        her "....."
                        m "Ну, что ты скажешь, девочка?"
                        m "Один танец для большей справедливости?"
                        hide screen hermione_main
                        with d3
                        $ h_body = "03_hp/13_hermione_main/body_66.png" #Sprite of Hermione's upper body.
                        show screen hermione_main
                        with d3
                        her "Ну, ладно..."
                        m "Отлично. Тогдай пойди и найди профессора Снейпа."
                        jump fetching_snape
                    
                    play music "music/Dark Fog.mp3" fadein 1 fadeout 1 # SNAPE'S THEME
                    sna "Джинни... э-э, то есть Альбус, ты хотел видеть меня?"
                    m "Да. Не желаешь немного стриптиза?"
                    hide screen snape_main
                    with d3
                    $ s_sprite = "03_hp/10_snape_main/snape_05.png"
                    show screen snape_main
                    with d3
                    sna "Оу...?"
                    sna "Мисс Гейнджер будет выступать, не так ли?"
                    $ h_body = "03_hp/13_hermione_main/body_34.png" #Sprite of Hermione's upper body.
                    $ h_xpos=380 #Defines position of the Hermione's full length sprite. (Default 370). (Center: 140)
                    show screen hermione_main
                    with d3
                    her ".............."
                    m "Да, наша маленькая потаскуха будет более чем довольна снять одежду для нас."
                    hide screen hermione_main
                    with d3
                    $ h_body = "03_hp/13_hermione_main/body_34.png" #Sprite of Hermione's upper body.
                    $ h_xpos=380 #Defines position of the Hermione's full length sprite. (Default 370). (Center: 140)
                    show screen hermione_main
                    with d3
                    her "............"
                    m "Не так ли, девочка?"
                    hide screen hermione_main
                    with d3
                    $ h_body = "03_hp/13_hermione_main/body_34.png" #Sprite of Hermione's upper body.
                    $ h_xpos=380 #Defines position of the Hermione's full length sprite. (Default 370). (Center: 140)
                    show screen hermione_main
                    with d3
                    her "Да, сэр."
                    m "В таком случае, приступай!"
                    hide screen hermione_main
                    hide screen snape_main
                    
                    pause
                    
                    show screen blkfade
                    with Dissolve(1)
                    $ renpy.play('sounds/08_hop_on_desk.mp3') #Sound of the desk squeaking. 
                    pause 1
                    $ h_body = "03_hp/13_hermione_main/body_16.png"
                    $ her_head_xpos=390 #Defines position of the Hermione's full length sprite. (Default 370). 140 - center. Bottom right: 390
                    $ her_head_ypos=340 #Defines position of the Hermione's full length sprite. (Default 0). Right bottom corner: 340 - head only. 235 - tits.
                    show screen h_head2
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
                    sna "Ну, вы знаете ... все по старому, все по старому..."
                    $ s_sprite = "03_hp/10_snape_main/snape_06.png"
                    sna " Студенты вызывают одно разочарование..."
                    $ s_sprite = "03_hp/10_snape_main/snape_03.png"
                    sna2 "На самом деле, Мисс Грейнджер удалось достать меня больше остальных..."
                    show screen h_head2
                    $ h_body = "03_hp/13_hermione_main/body_68.png"
                    her "..............................."
                    hide screen h_head2
                    m "Я уверен, она очень сожалеет об этом..."
                    show screen h_head2
                    $ h_body = "03_hp/13_hermione_main/body_74.png"
                    her "{size=-4}(Ни капельки!){/size}"
                    hide screen h_head2
                    m "И сделает что угодно для тебя сегодня, да, девочка?"
                    show screen h_head2
                    $ h_body = "03_hp/13_hermione_main/body_53.png"
                    her "Э-эм... Да, профессор."
                    hide screen h_head2
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
                    show screen h_head2
                    $ h_body = "03_hp/13_hermione_main/body_87.png"
                    her "..................."
                    $ s_sprite = "03_hp/10_snape_main/snape_05.png"
                    show screen s_head2
                    sna "Хм... В последнее время ты очень тихая."
                    show screen h_head2
                    $ h_body = "03_hp/13_hermione_main/body_48.png"
                    her "{size=-4}(О нет! Он дейстивтельно так считает?){/size}"
                    $ h_body = "03_hp/13_hermione_main/body_57.png"
                    her2 "Я просто делаю то, что мне сказал профессор..."
                    $ s_sprite = "03_hp/10_snape_main/snape_03.png"
                    show screen s_head2
                    sna2 "Сегодня вы не собираетесь читать мне лекции о \"коррупкции в Хогвартсе\"?"
                    hide screen s_head2
                    m "Северус..."
                    $ s_sprite = "03_hp/10_snape_main/snape_03.png"
                    show screen s_head2
                    sna2 "Неь, Альбус, я хочу услышать ответ от нашей маленькой мисс совершенство."
                    show screen h_head2
                    $ h_body = "03_hp/13_hermione_main/body_57.png"
                    her2 "Я просто хочу, чтобы вы отлично провели время, сэр..."
                    $ s_sprite = "03_hp/10_snape_main/snape_03.png"
                    show screen s_head2
                    sna2 "Ох! Этот \"сэр\", это ведь не ко мне ты обращаешься?"
                    $ s_sprite = "03_hp/10_snape_main/snape_10.png"
                    sna2 "Что стало с  \"Снейпо-каракулем\" и профессором \"Сопливикусом\"!??"
                    hide screen s_head2
                    g9 "{size=-5}( \"Сопливикус\", хех... это забавно.){/size}"
                    show screen h_head2 # HERMIONE
                    $ h_body = "03_hp/13_hermione_main/body_57.png" # HERMIONE
                    her "............."
                    $ s_sprite = "03_hp/10_snape_main/snape_08.png"
                    show screen s_head2
                    sna2 "Да, я знаю, как ты зовешь меня за спиной, девочка!"
                    show screen h_head2
                    $ h_body = "03_hp/13_hermione_main/body_86.png"
                    her2 "Может быть это потому что вы заслужили это... сэр."
                    $ s_sprite = "03_hp/10_snape_main/snape_10.png" #SNAPE
                    show screen s_head2 #SNAPE
                    sna "Что?!"
                    sna "Да как ты смеешь....?"
                    $ s_sprite = "03_hp/10_snape_main/snape_15.png" #SNAPE
                    show screen s_head2 #SNAPE
                    sna "Кем ты себя возомнила? Ты грязно--"
                    show screen h_head2 # HERMIONE
                    $ h_body = "03_hp/13_hermione_main/body_62.png" # HERMIONE
                    her2 "Профессор, один из ваших сотрудников собирается оскорбить меня!"
                    her2 "Вы это допустите?"
                    $ s_sprite = "03_hp/10_snape_main/snape_08.png" #SNAPE
                    show screen s_head2 #SNAPE
                    sna "Оскорблять...?! Ты очень нервируешь меня, девочка!"
                    $ s_sprite = "03_hp/10_snape_main/snape_10.png" #SNAPE
                    show screen s_head2 #SNAPE
                    sna2 "Альбус, ты позволишь ей так разговаривать с учителем?"
                    show screen h_head2                                                             # HERMIONE
                    $ h_body = "03_hp/13_hermione_main/body_62.png" # HERMIONE
                    her "Профессор Дамблдор!"
                    $ s_sprite = "03_hp/10_snape_main/snape_10.png" #SNAPE
                    show screen s_head2 #SNAPE
                    sna "Альбус!"
                    hide screen s_head2
                    menu:
                        m "..."
                        "\"Мисс Грейнджер, проявите уважение!\"":
                            $ mad += 9
                            show screen h_head2                                                             # HERMIONE
                            $ h_body = "03_hp/13_hermione_main/body_61.png" # HERMIONE
                            her "Что?"
                            her "Но профессор!"
                            hide screen h_head2  
                            m "Юная леди, вам {size=+4}следует{/size} успокоиться."
                            show screen h_head2                                                             # HERMIONE
                            $ h_body = "03_hp/13_hermione_main/body_66.png" # HERMIONE
                            her "Арх!"
                            hide screen h_head2      
                            m "И снимай свою юбку, хорошо?"
                            show screen h_head2                                                             # HERMIONE
                            $ h_body = "03_hp/13_hermione_main/body_69.png" # HERMIONE
                            her "......."
                            $ s_sprite = "03_hp/10_snape_main/snape_13.png" #SNAPE
                            show screen s_head2                                                          #SNAPE
                            sna "..........."
                            hide screen s_head2  
                        "\"Северус, ты первый начал.\"":
                            $ s_sprite = "03_hp/10_snape_main/snape_10.png" #SNAPE
                            show screen s_head2  
                            sna "Что? Я?!"
                            show screen h_head2                                                             # HERMIONE
                            $ h_body = "03_hp/13_hermione_main/body_52.png" # HERMIONE
                            her "Спасибо, профессор."
                            $ s_sprite = "03_hp/10_snape_main/snape_08.png" #SNAPE
                            show screen s_head2                                                          #SNAPE
                            sna2 "Albus, ты портишь девочку! Ей нужно преподать урок!"
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
                            m "Мисс Грейнджер, вы собиретесь танцевать для нас или подняться как можно выше, чтобы получить лучший вид сверху?"
                            show screen h_head2                                                             # HERMIONE
                            $ h_body = "03_hp/13_hermione_main/body_87.png" # HERMIONE
                            her "Эм..."
                            hide screen h_head2
                            m "Снимай свою юбку, девочка!"
                            show screen h_head2                                                             # HERMIONE
                            $ h_body = "03_hp/13_hermione_main/body_55.png" # HERMIONE
                            her "Да, сэр..."
                            hide screen h_head2
                        "\"Вы оба, заткнитесь нахер.\"":
                            m "Ты, высокий-темный-парень, успокойся, ага?"
                            $ s_sprite = "03_hp/10_snape_main/snape_03.png" #SNAPE
                            show screen s_head2                                                          #SNAPE
                            sna "Простите?"
                            show screen h_head2                                                             # HERMIONE
                            $ h_body = "03_hp/13_hermione_main/body_69.png" # HERMIONE
                            her "Да! Вы должны сказать ему--"
                            hide screen h_head2     
                            m "И ты тоже, извращенка!"
                            m "Успокойтесь и снимайте с себя уже юбку."
                            show screen h_head2                                                             # HERMIONE
                            $ h_body = "03_hp/13_hermione_main/body_79.png" # HERMIONE
                            her "Я не извращенка..."
                            hide screen h_head2     
                            m "Юбка, девочка!"
                            show screen h_head2                                                             # HERMIONE
                            $ h_body = "03_hp/13_hermione_main/body_69.png" # HERMIONE
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
                    show screen h_head2                                                             # HERMIONE
                    $ h_body = "03_hp/13_hermione_main/body_87.png" # HERMIONE
                    her "........................"
                    hide screen h_head2
                    m "Да, так-то лучше!"
                    show screen blktone
                    with d3
                    ">Гермиона продолжает танцевать. На ней уже не осталось ничего, кроме рубашки..."
                    menu:
                        m "..."
                        "\"Северус, что насчет Поттера?\"":
                            show screen h_head2                                                             # HERMIONE
                            $ h_body = "03_hp/13_hermione_main/body_55.png" # HERMIONE
                            her "(.....?)"
                            $ s_sprite = "03_hp/10_snape_main/snape_09.png" #SNAPE
                            show screen s_head2
                            sna "Что с ним?"
                            hide screen s_head2
                            m "Ты все еще из за него расстраиваешься?"
                            $ s_sprite = "03_hp/10_snape_main/snape_09.png" #SNAPE
                            show screen s_head2                                                          #SNAPE
                            sna "О..."
                            sna "На самом деле нет."
                            $ s_sprite = "03_hp/10_snape_main/snape_06.png" #SNAPE
                            show screen s_head2                                                          #SNAPE
                            sna2 "Честно говоря у меня никогда не было с ним особых проблем..."
                            sna2 "Хотя я планировал сделать его жизнь невыносимой из-за его отца..."
                            $ s_sprite = "03_hp/10_snape_main/snape_02.png" #SNAPE
                            show screen s_head2    
                            sna2 "Но в последнее время у меня есть много интересных проектов, чтобы занять себя..."
                            show screen h_head2                                                             # HERMIONE
                            $ h_body = "03_hp/13_hermione_main/body_55.png" # HERMIONE
                            her "..................."  
                            hide screen h_head2   
                        "\"Северус, что насчет семьи Уизли?\"":
                            $ s_sprite = "03_hp/10_snape_main/snape_09.png" #SNAPE
                            show screen s_head2                                                          #SNAPE
                            sna "Что с ними?"
                            hide screen s_head2   
                            m "Они все еще являются проблемой?"
                            $ s_sprite = "03_hp/10_snape_main/snape_09.png" #SNAPE
                            show screen s_head2                                                          #SNAPE
                            sna "Да... Больше чем раньше."
                            hide screen s_head2
                            m "Хм...?"
                            m "Ты кажешься удивительно равнодушным насчет этого..."
                            $ s_sprite = "03_hp/10_snape_main/snape_05.png" #SNAPE
                            show screen s_head2                                                          #SNAPE
                            sna2 "Это только потому что я знаю что в конце концов они получат то, что заслуживают..."
                            hide screen s_head2
                            m "Месть? Отлично! Что у тебя на уме?"
                            show screen h_head2                                                             # HERMIONE
                            $ h_body = "03_hp/13_hermione_main/body_55.png" # HERMIONE
                            her "!!!"
                            $ s_sprite = "03_hp/10_snape_main/snape_06.png" #SNAPE
                            show screen s_head2                                                          #SNAPE
                            sna "Хм... Can't discuss this with \"the enemy\" present."
                            show screen h_head2                                                             # HERMIONE
                            $ h_body = "03_hp/13_hermione_main/body_69.png" # HERMIONE
                            her "Арх!"
                            $ s_sprite = "03_hp/10_snape_main/snape_13.png" #SNAPE
                            show screen s_head2                                                          #SNAPE
                            sna2 "Все что я могу сказать - это то, что это включает в себя их любимую маленькую сестренку Джинни..."
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
                            show screen h_head2                                                             # HERMIONE
                            $ h_body = "03_hp/13_hermione_main/body_87.png" # HERMIONE
                            her "{size=-5}(Ginny...){/size}"
                            hide screen h_head2 
                        "\"Как ты оцениваешь попку Гермионы?\"":
                            $ s_sprite = "03_hp/10_snape_main/snape_05.png" #SNAPE
                            show screen s_head2                                                          #SNAPE
                            sna "ягодицы мисс Гермионы?" 
                            show screen h_head2                                                             # HERMIONE
                            $ h_body = "03_hp/13_hermione_main/body_69.png" # HERMIONE
                            her "!!!............"
                            hide screen h_head2      
                            m "Конечно! Так же, как ты оцениваешь бумагу."
                            $ s_sprite = "03_hp/10_snape_main/snape_13.png" #SNAPE
                            show screen s_head2                                                          #SNAPE
                            sna "Хм..."
                            hide screen s_head2  
                            pause.1
                            ">Профессор Снейп оценивающе смотрит на ягодицы Гермионы..."
                            show screen h_head2                                                             # HERMIONE
                            $ h_body = "03_hp/13_hermione_main/body_44.png" # HERMIONE
                            her ".........?"
                            $ s_sprite = "03_hp/10_snape_main/snape_13.png" #SNAPE
                            show screen s_head2                                                          #SNAPE
                            sna "Я бы сказал..."
                            show screen h_head2                                                             # HERMIONE
                            $ h_body = "03_hp/13_hermione_main/body_59.png" # HERMIONE
                            her "............?!"
                            $ s_sprite = "03_hp/10_snape_main/snape_09.png" #SNAPE
                            show screen s_head2                                                          #SNAPE
                            sna "Да... \"{size=+5}F-{/size}\"."
                            show screen h_head2                                                             # HERMIONE
                            $ h_body = "03_hp/13_hermione_main/body_48.png" # HERMIONE
                            her "(Что?!)"
                            $ s_sprite = "03_hp/10_snape_main/snape_09.png" #SNAPE
                            show screen s_head2                                                          #SNAPE
                            sna "Неудовлетворительно..."
                            sna2 "Посмотрите на это. Маленькая и тощая... Да это задница мальчика."
                            show screen h_head2                                                             # HERMIONE
                            $ h_body = "03_hp/13_hermione_main/body_51.png" # HERMIONE
                            her "!!!!!!!!!!"
                            hide screen h_head2   
                            
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
                    m "Неплохо! Мы наконец-то добрались до приятного!"
                    $ s_sprite = "03_hp/10_snape_main/snape_13.png" #SNAPE
                    show screen s_head2       
                    sna "Хм..."
                    
                    $ badges = False # Hides the layer with badges.
                    
                    $ her_head_xpos=390 #Defines position of the Hermione's full length sprite. (Default 370). 140 - center. Bottom right: 390
                    $ her_head_ypos=235 #Defines position of the Hermione's full length sprite. (Default 0). Right bottom corner: 340 - head only. 235 - tits.
                    show screen h_head2                                                             # HERMIONE
                    $ h_body = "03_hp/13_hermione_main/body_90.png" # HERMIONE
                    her "........"
                    hide screen h_head2   
                    menu:
                        m "..."
                        "-Начать дрочить-":
                            play music "music/(Orchestral) Playful Tension by Shadow16nh.mp3" fadein 1 fadeout 1 # SEX THEME.
                            
                            hide screen bld1
                            show screen ctc
                            with d3
                            pause
                            show screen blkfade
                            with d6
                            show screen h_head2
                            $ h_body = "03_hp/13_hermione_main/body_94.png"
                            her "Профессор Дамблдор?!"
                            hide screen h_head2
                            m "Все в порядке, девочка. Не возражай мне..."
                            $ s_sprite = "03_hp/10_snape_main/snape_12.png" #SNAPE
                            show screen s_head2                                                          #SNAPE
                            sna "О, мы будем теперь вести себя так?"
                            sna "Что же, не обращай внимания, если я начну..."
                            show screen h_head2                                                             # HERMIONE
                            $ h_body = "03_hp/13_hermione_main/body_94.png" # HERMIONE
                            $ s_head_ypos = 380 #Right bottom corner: y = 340. y = 380 - no hand.
                            her "!!!"
                            hide screen h_head2    
                            
                            
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
                            show screen h_head2
                            $ h_body = "03_hp/13_hermione_main/body_95.png"
  
                            her "Нет, ребята... эмм, я имею в виду сэры... Эм, профессоры!"
                            hide screen h_head2
                            m "Не обращай внимания на нас, девочка, просто продолжай."
                            show screen h_head2
                            her "Но..."
                            show screen h_head2                                                             # HERMIONE
                            $ h_body = "03_hp/13_hermione_main/body_99.png" # HERMIONE
                            her2 "Нет! Я отказываюсь танцевать, пока эти штуки нацелены на меня!"
                            her2 "Вы должны убрать их, или танца не будет!"
                            hide screen h_head2    
                            m "Ты не в том положении, чтобы что-то требовать, девочка."
                            show screen h_head2                                                             # HERMIONE
                            $ h_body = "03_hp/13_hermione_main/body_110.png" # HERMIONE
                            her2 "это было не требование, сэр.Это был ультиматум."
                            hide screen h_head2    
                            menu:
                                m "..."
                                "\"Что же Северус, давай будем цивилизованными...\"":
                                    $ s_sprite = "03_hp/10_snape_main/snape_03.png" #SNAPE
                                    show screen s_head2                                                          #SNAPE
                                    sna2 "Я вижу Мисс Грейнджер может вести себя упорно в любой ситуации..."
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
                                    
                                "\"(Пст! Напомните мне, зачем мы это делаем!)\"":
                                    if whoring >= 15: #LEVEL 06. You jerk off your cock and Hermione is OK with it.
                                        show screen h_head2                                                               # HERMIONE
                                        $ h_body = "03_hp/13_hermione_main/body_104.png" # HERMIONE
                                        her "О, точно..."
                                        $ s_sprite = "03_hp/10_snape_main/snape_05.png" #SNAPE
                                        show screen s_head2                                                          #SNAPE
                                        sna "Что это было?"
                                        show screen h_head2                                                               # HERMIONE
                                        $ h_body = "03_hp/13_hermione_main/body_108.png" # HERMIONE
                                        her "Пожалуйста, не возражайте против меня..."
                                        $ s_sprite = "03_hp/10_snape_main/snape_05.png" #SNAPE
                                        show screen s_head2                                                          #SNAPE
                                        sna "Хм...?"
                                        show screen h_head2                                                               # HERMIONE
                                        $ h_body = "03_hp/13_hermione_main/body_108.png" # HERMIONE
                                        her2 "Я не против, что вы трогаете себя передо мной..."
                                        her2 "Да, я не против всего этого..."
                                        her "Я просто продолжу танцевать..."
                                        hide screen h_head2
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
                                        show screen h_head2                                                             # HERMIONE
                                        $ h_body = "03_hp/13_hermione_main/body_97.png" # HERMIONE
                                        her "...................."
                                        hide screen h_head2
                                        m "Хех..."
                                        hide screen h_head2
                                        m "Как вы оцените ее грудь?"
                                        show screen h_head2                                                             # HERMIONE
                                        $ h_body = "03_hp/13_hermione_main/body_94.png" # HERMIONE
                                        her "......"
                                        $ s_sprite = "03_hp/10_snape_main/snape_13.png" #SNAPE
                                        show screen s_head2                                                          #SNAPE
                                        sna "Хм......"
                                        show screen h_head2                                                             # HERMIONE
                                        $ h_body = "03_hp/13_hermione_main/body_103.png" # HERMIONE
                                        her "........"
                                        $ s_sprite = "03_hp/10_snape_main/snape_12.png" #SNAPE
                                        show screen s_head2                                                          #SNAPE
                                        sna "\"4+\"!"
                                        show screen h_head2                                                             # HERMIONE
                                        $ h_body = "03_hp/13_hermione_main/body_94.png" # HERMIONE
                                        her "!!!"
                                        hide screen h_head2
                                        m "Правда?"
                                        $ s_sprite = "03_hp/10_snape_main/snape_12.png" #SNAPE
                                        show screen s_head2                                                          #SNAPE
                                        sna2 "Да. Я всегда отдаю должное."
                                        show screen h_head2                                                             # HERMIONE
                                        $ h_body = "03_hp/13_hermione_main/body_90.png" # HERMIONE
                                        her "(Профессор...)"
                                        show screen h_head2                                                             # HERMIONE
                                        $ h_body = "03_hp/13_hermione_main/body_102.png" # HERMIONE
                                        her "(Время завершающего акта!)"
                                        hide screen h_head2 
                                        pause.1
                                        show screen blktone8
                                        with d3
                                        ">Гермиона нагибается и ее трусики соскальзывают вниз."
                                        ">Ее движения лишены грации..."
                                        ">Но ее хорошенькая киска тем не менее вам нравится..."
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
                                        show screen h_head2                                                             # HERMIONE
                                        $ h_body = "03_hp/13_hermione_main/body_99.png" # HERMIONE
                                        her "......."
                                        hide screen h_head2       
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
                                        show screen h_head2                                                             # HERMIONE
                                        $ h_body = "03_hp/13_hermione_main/body_106.png" # HERMIONE
                                        her "........."
                                        $ s_sprite = "03_hp/10_snape_main/snape_20.png" #SNAPE
                                        show screen s_head2                                                          #SNAPE
                                        sna "О, да!"
                                        show screen h_head2                                                             # HERMIONE
                                        $ h_body = "03_hp/13_hermione_main/body_106.png" # HERMIONE
                                        her "{size=-5}(Три-два-раз... Три-два-раз... And step!){/size}"
                                        hide screen h_head2     
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
                                        show screen h_head2
                                        $ h_body = "03_hp/13_hermione_main/body_102.png"
                                        her "Фью... Это было--"
                                        hide screen h_head2
                                        with hpunch
                                        g4 "АРГХ! ТЫ ЕБАНАЯ ШЛЮХА!"
                                        hide screen hermione_main
                                        with d3
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
                                        $ uni_sperm = True #Triggers universal sperm to show on hermione_main screen.
                                        $ h_body = "03_hp/13_hermione_main/body_104.png"
                                        $ u_sperm = "03_hp/13_hermione_main/auto_04.png"
                                        show screen h_head2  
                                        her "??!!!"
                                        hide screen h_head2
                                        $ h_body = "03_hp/13_hermione_main/body_97.png"
                                        show screen h_head2  
                                        
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
                                        $ uni_sperm = True #Triggers universal sperm to show on hermione_main screen.
                                        $ h_body = "03_hp/13_hermione_main/body_104.png"
                                        $ u_sperm = "03_hp/13_hermione_main/auto_04.png"
                                        show screen h_head2  
                                        $ u_sperm = "03_hp/13_hermione_main/auto_05.png"
                                        her "!!!!!!!!!!!"
                                        $ s_sprite = "03_hp/10_snape_main/snape_21.png" #SNAPE
                                        show screen s_head2                                                          #SNAPE
                                        sna2 "О... Да..."
                                        hide screen s_head2 
                                        g4 "Маленькая блядь!"
                                        show screen h_head2                                                             # HERMIONE
                                        $ h_body = "03_hp/13_hermione_main/body_106.png" # HERMIONE
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
                                        show screen h_head2                                                             # HERMIONE
                                        $ h_body = "03_hp/13_hermione_main/body_106.png" # HERMIONE
                                        her "................."
                                        $ s_sprite = "03_hp/10_snape_main/snape_20.png" #SNAPE
                                        show screen s_head2                                                          #SNAPE
                                        sna "Ваше выступление было неплохим, Мисс Грейнджер..."
                                        show screen h_head2                                                             # HERMIONE
                                        $ h_body = "03_hp/13_hermione_main/body_91.png" # HERMIONE
                                        her "Спасибо................"
                                        $ s_sprite = "03_hp/10_snape_main/snape_19.png" #SNAPE
                                        show screen s_head2                                                          #SNAPE
                                        sna "Но если я здесь чтобы оценить это..."
                                        show screen h_head2                                                             # HERMIONE
                                        $ h_body = "03_hp/13_hermione_main/body_91.png" # HERMIONE
                                        her "..........."
                                        $ s_sprite = "03_hp/10_snape_main/snape_22.png" #SNAPE
                                        show screen s_head2                                                          #SNAPE
                                        sna "Хм...."
                                        show screen h_head2                                                               # HERMIONE
                                        $ h_body = "03_hp/13_hermione_main/body_91.png" # HERMIONE
                                        her "............"
                                        $ s_sprite = "03_hp/10_snape_main/snape_10.png" #SNAPE
                                        show screen s_head2                                                          #SNAPE
                                        sna "\"{size=+5}2+{/size}\"!"
                                        show screen h_head2                                                               # HERMIONE
                                        $ h_body = "03_hp/13_hermione_main/body_112.png" # HERMIONE
                                        stop music
                                        her "{size=+5}ЧТО?!!!{/size}"
                                        $ s_sprite = "03_hp/10_snape_main/snape_09.png" #SNAPE
                                        show screen s_head2                                                          #SNAPE
                                        sna2 "Да... Думаю кое-что можно было бы и улучшить."
                                        show screen h_head2                                                               # HERMIONE
                                        $ h_body = "03_hp/13_hermione_main/body_110.png" # HERMIONE
                                        play music "music/Chipper Doodle v2.mp3" fadein 1 fadeout 1 # HERMIONE'S THEME.
                                        her "Не могу поверить!"
                                        hide screen h_head2 
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
                                        $ flip = True # Flips hermione_main screen.
                                        $ u_sperm = im.Flip("03_hp/13_hermione_main/auto_05.png", horizontal=True)
                                        $ h_body = im.Flip("03_hp/13_hermione_main/body_101.png", horizontal=True) #Sprite of Hermione's upper body.
                                        $ h_xpos=140 #Defines position of the Hermione's full length sprite. (Default 370). (Center: 140)
                                        $ only_upper = True #No legs shown.
                                        show screen bld1
                                        with d5
                                        show screen hermione_main
                                        with d3
                                        pause
                                        hide screen ctc
                                        her "Я требую более высокую оценку за это!"
                                        $ s_sprite = "03_hp/10_snape_main/snape_09.png" #SNAPE
                                        show screen s_head2      
                                        sna2 "Не требуйте оценку Мисс Грейнджер, вы заработали ее."
                                        hide screen s_head2     
                                        hide screen hermione_main                                                                                                                                                                                   #HERMIONE
                                        with d3                                                                                                                                                                                                                        #HERMIONE
                                        $ h_xpos=140 #Defines position of the Hermione's full length sprite. (Default 370). (Center: 140)                                                        #HERMIONE
                                        $ h_body = im.Flip("03_hp/13_hermione_main/body_107.png", horizontal=True) #Sprite of Hermione's upper body.                    #HERMIONE
                                        show screen hermione_main                                                                                                                                                                                 #HERMIONE
                                        with d3                                                                                                                                                                                                                        #HERMIONE
                                        her "Я заслужила ее!"
                                        hide screen hermione_main                                                                                                                                                                                   #HERMIONE
                                        with d3                                                                                                                                                                                                                        #HERMIONE
                                        $ h_xpos=140 #Defines position of the Hermione's full length sprite. (Default 370). (Center: 140)                                                        #HERMIONE
                                        $ h_body = im.Flip("03_hp/13_hermione_main/body_103.png", horizontal=True) #Sprite of Hermione's upper body.                    #HERMIONE
                                        show screen hermione_main                                                                                                                                                                                 #HERMIONE
                                        with d3                                                                                                                                                                                                                        #HERMIONE
                                        her "И не могли бы вы хотя бы для порядочности перестать трогать себя, сэр?!"
                                        $ s_sprite = "03_hp/10_snape_main/snape_12.png" #SNAPE
                                        show screen s_head2     
                                        sna2 "Тс..."
                                        hide screen s_head2   
                                        hide screen hermione_main                                                                                                                                                                                   #HERMIONE
                                        with d3   
                                        m "(Она это вправду?)"
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
                                        ">Наконец профессор Снейп соглашается изменить ее оценку с \"2+\" на \"3-\"."
                                        ">После этого он поспешно уходит, до того как Гермиона найдет еще один аргумент..."
                                        hide screen blkfade
                                        with d5
                                        $ flip = False # Flips hermione_main
                                        $ only_upper = False #Show legs.
                                        $ aftersperm = True #Show cum stains.
                                        $ uni_sperm = False #Don't show cum.
                                        hide screen hermione_main                                                                                                                                                                                   #HERMIONE
                                        with d3                                                                                                                                                                                                                        #HERMIONE
                                        $ h_xpos=140 #Defines position of the Hermione's full length sprite. (Default 370). (Center: 140)                                                        #HERMIONE
                                        $ h_body = "03_hp/13_hermione_main/body_29.png"#Sprite of Hermione's upper body.                    #HERMIONE
                                        $ badges = True
                                        show screen hermione_main                                                                                                                                                                                 #HERMIONE
                                        with d3                                                                                                                                                                                                                        #HERMIONE
                                        her "Что же..."
                                        her "Наша миссия была успешной, сэр?"
                                        menu:
                                            m "..."
                                            "\"А? Какая миссия?\"":
                                                $ mad += 7
                                                hide screen hermione_main                                                                                                                                                                                   #HERMIONE
                                                with d3                                                                                                                                                                                                                        #HERMIONE
                                                $ h_xpos=140 #Defines position of the Hermione's full length sprite. (Default 370). (Center: 140)                                                        #HERMIONE
                                                $ h_body = "03_hp/13_hermione_main/body_32.png"#Sprite of Hermione's upper body.                                                                   #HERMIONE
                                                show screen hermione_main                                                                                                                                                                                 #HERMIONE
                                                with d3                                                                                                                                                                                                                        #HERMIONE
                                                her "Я согласилась на это только ради того, чтобы вы увидели профессора Снейпа в действии, сэр!"
                                                hide screen hermione_main                                                                                                                                                                                   #HERMIONE
                                                with d3                                                                                                                                                                                                                        #HERMIONE
                                                $ h_xpos=140 #Defines position of the Hermione's full length sprite. (Default 370). (Center: 140)                                                        #HERMIONE
                                                $ h_body = "03_hp/13_hermione_main/body_33.png"#Sprite of Hermione's upper body.                                                                   #HERMIONE
                                                show screen hermione_main                                                                                                                                                                                 #HERMIONE
                                                with d3                                                                                                                                                                                                                        #HERMIONE
                                                her "Так что у нас есть неопровержимое доказательство того, что он \"грязный\"!"
                                                m "О, эта миссия..."
                                                m "Да. Миссия выполнена!"
                                            "\"Да! Спасибо вам!\"":
                                                pass
                                        m "Хорошая работа, мисс Грейнджер."
                                        hide screen hermione_main                                                                                                                                                                                   #HERMIONE
                                        with d3                                                                                                                                                                                                                        #HERMIONE
                                        $ h_xpos=140 #Defines position of the Hermione's full length sprite. (Default 370). (Center: 140)                                                        #HERMIONE
                                        $ h_body = "03_hp/13_hermione_main/body_33.png"#Sprite of Hermione's upper body.                                                                   #HERMIONE
                                        show screen hermione_main                                                                                                                                                                                 #HERMIONE
                                        with d3                                                                                                                                                                                                                        #HERMIONE
                                        her "Я была рада помочь, сэр!"
                                        hide screen hermione_main                                                                                                                                                                                   #HERMIONE
                                        with d3                                                                                                                                                                                                                        #HERMIONE
                                        $ h_xpos=140 #Defines position of the Hermione's full length sprite. (Default 370). (Center: 140)                                                        #HERMIONE
                                        $ h_body = "03_hp/13_hermione_main/body_34.png"#Sprite of Hermione's upper body.                                                                   #HERMIONE
                                        show screen hermione_main                                                                                                                                                                                 #HERMIONE
                                        with d3                                                                                                                                                                                                                        #HERMIONE
                                        her "...Могу ли я теперь получить оплату?"
                                        

                                    else:
                                        show screen h_head2                                                              # HERMIONE
                                        $ h_body = "03_hp/13_hermione_main/body_94.png" # HERMIONE
                                        her "О..."
                                        show screen h_head2                                                              # HERMIONE
                                        $ h_body = "03_hp/13_hermione_main/body_97.png" # HERMIONE
                                        her "Нет, я не могу! Это того не стоит!"
                                        hide screen ctc
                                        hide screen h_head2  
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
                                        sna2 "Пожалуй я могу вас покинуть. Поговорим позже, Альбус."
                                        hide screen s_head2  
                                        m "Да, попозже, Северус."
                                        $ s_sprite = "03_hp/10_snape_main/snape_04.png" #SNAPE
                                        show screen s_head2                                                          #SNAPE
                                        sna "Мисс Грейнджер..."
                                        show screen h_head2                                                              # HERMIONE
                                        $ h_body = "03_hp/13_hermione_main/body_99.png" # HERMIONE
                                        her "Профессор..."
                                        hide screen h_head2          
                                       # her "Я хочу получить свои очки."
                                        show screen ctc
                                        pause.4
                                        hide screen s_c_u
                                        hide screen ctc
                                        ">Профессор Снейп уходит..."
                                        show screen h_head2                                                              # HERMIONE
                                        $ h_body = "03_hp/13_hermione_main/body_91.png" # HERMIONE
                                        stop music fadeout 1.0
                                        her "...................."
                                        hide screen h_head2
                                        pause.5
                                        ">.................{w}.................{w}.................{w}................."
                                        show screen h_head2                                                              # HERMIONE
                                        
                                        $ badges = True # Turns badges back on.
                                        
                                        $ h_body = "03_hp/13_hermione_main/body_33.png" # HERMIONE
                                        her "...Могу ли я получить оплату... сэр...?"
                                        hide screen h_head2   

                        "-Продолжать смотреть-":
                            label civil_with_snape:
                                play music "music/Dark Fog.mp3" fadein 1 fadeout 1 # SNAPE'S THEME
                            # JUST WATCHING.
                            show screen h_head2                                                              # HERMIONE
                            $ h_body = "03_hp/13_hermione_main/body_102.png" # HERMIONE
                            her "Я просто продолжу танцевать..."
                            hide screen h_head2 
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
                            show screen h_head2                                                              # HERMIONE
                            $ h_body = "03_hp/13_hermione_main/body_102.png" # HERMIONE
                            her "...."
                            hide screen h_head2    
                            m "Хех..."
                            m "Как вы оцените ее грудь?"
                            show screen h_head2                                                              # HERMIONE
                            $ h_body = "03_hp/13_hermione_main/body_90.png" # HERMIONE
                            her "......"
                            $ s_sprite = "03_hp/10_snape_main/snape_20.png" #SNAPE
                            show screen s_head2                                                          #SNAPE
                            sna "Хм......"
                            show screen h_head2                                                              # HERMIONE
                            $ h_body = "03_hp/13_hermione_main/body_90.png" # HERMIONE
                            her "........"
                            $ s_sprite = "03_hp/10_snape_main/snape_12.png" #SNAPE
                            show screen s_head2                                                          #SNAPE
                            sna "\"4+\"!"
                            show screen h_head2                                                              # HERMIONE
                            $ h_body = "03_hp/13_hermione_main/body_94.png" # HERMIONE
                            her "!!!"
                            hide screen h_head2
                            m "Правда?"
                            $ s_sprite = "03_hp/10_snape_main/snape_12.png" #SNAPE
                            show screen s_head2                                                          #SNAPE
                            sna "Да. Я всегда отдаю должное."
                            show screen h_head2                                                              # HERMIONE
                            $ h_body = "03_hp/13_hermione_main/body_95.png" # HERMIONE
                            her "(Профессор...)"
                            show screen h_head2                                                              # HERMIONE
                            $ h_body = "03_hp/13_hermione_main/body_102.png" # HERMIONE
                            her "(Время для завершающего акта!)"
                            hide screen h_head2   
                            pause.1
                            show screen blktone8
                            with d3
                            ">Гермиона нагибается и ее трусики соскальзывают вниз."
                            ">Ее движения лишены грации..."
                            ">Но ее хорошенькая киска тем не менее вам нравится..."
                            hide screen blktone
                            with d3
                            $ s_sprite = "03_hp/10_snape_main/snape_20.png" #SNAPE
                            show screen s_head2                                                          #SNAPE
                            sna "Да...Да..."
                            sna2 "Теперь потряси этими сиськами для меня, шлюха!"
                            show screen h_head2                                                              # HERMIONE
                            $ h_body = "03_hp/13_hermione_main/body_99.png" # HERMIONE
                            her "......."
                            hide screen h_head2       
                            show screen blktone8
                            with d3
                            ">Гермиона неожиданно прерывается на серию довольно сложных пируэтов."
                            $ s_sprite = "03_hp/10_snape_main/snape_19.png" #SNAPE
                            show screen s_head2                                                          #SNAPE
                            sna "Да, такая грация..."
                            $ s_sprite = "03_hp/10_snape_main/snape_20.png" #SNAPE
                            show screen s_head2                                                          #SNAPE
                            sna "Это гибкое, молодое тело!"
                            show screen h_head2                                                              # HERMIONE
                            $ h_body = "03_hp/13_hermione_main/body_102.png" # HERMIONE
                            her "{size=-5}(Три-два-раз... Три-два-раз... And step!){/size}"
                            hide screen h_head2 
                            ">HГермиона выглядит очень сосредоточенной на своем танце..."
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
                            sna "Хорошая работа, ты шлюха!"
                            show screen h_head2                                                              # HERMIONE
                            $ h_body = "03_hp/13_hermione_main/body_105.png" # HERMIONE
                            her "............."
                            if daytime:
                                $ s_sprite = "03_hp/10_snape_main/snape_22.png" #SNAPE
                                show screen s_head2                                                          #SNAPE
                                sna2 "Что ж, мой урок скоро должен начаться, поэтому я вас покину."
                                sna2 "Разве у вас нет урока зельеделия со мной сегодня, Мисс Грейнджер?"
                                show screen h_head2                                                              # HERMIONE
                                $ h_body = "03_hp/13_hermione_main/body_91.png" # HERMIONE
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
                                show screen h_head2                                                              # HERMIONE
                                $ h_body = "03_hp/13_hermione_main/body_91.png" # HERMIONE
                                her2 "Профессор..."
                                hide screen h_head2      


                            show screen ctc
                            pause
                            show screen blkfade
                            hide screen s_c_u
                            hide screen ctc
                            with d5
                            ">Профессор Снейп уходит..."
                            show screen h_head2                                                              # HERMIONE
                            $ h_body = "03_hp/13_hermione_main/body_91.png" # HERMIONE
                            stop music fadeout 1.0
                            her "...................."
                            hide screen h_head2
                            pause.5
                            ">.................{w}.................{w}.................{w}................."
                            $ badges = True
                            show screen h_head2                                                              # HERMIONE
                            $ h_body = "03_hp/13_hermione_main/body_33.png" # HERMIONE
                            her "Могу я... получить оплату... сэр...?"
                            hide screen h_head2   


                "\"Мм... Это плохая идея...\"":
                    label no_snape_watching:  
                    hide screen blktone
                    with d3
                    m "Мисс Грейнджер, как насчет еще одного стриптиза?"     
                    $ h_body = "03_hp/13_hermione_main/body_66.png" #Sprite of Hermione's upper body.
                    $ h_xpos=140 #Defines position of the Hermione's full length sprite. (Default 370). (Center: 140)
                    show screen hermione_main
                    with d3
                    her ".............."
                    her "Я скорее откажусь, профессор..."
                    m "Почему? Ты становишься довольно хороша в этом."
                    hide screen hermione_main
                    with d3
                    $ h_body = "03_hp/13_hermione_main/body_79.png" #Sprite of Hermione's upper body.
                    $ h_xpos=140 #Defines position of the Hermione's full length sprite. (Default 370). (Center: 140)
                    show screen hermione_main
                    with d3
                    her "........................."
                    hide screen hermione_main
                    with d3
                    $ h_body = "03_hp/13_hermione_main/body_87.png" #Sprite of Hermione's upper body.
                    $ h_xpos=140 #Defines position of the Hermione's full length sprite. (Default 370). (Center: 140)
                    show screen hermione_main
                    with d3
                    her "Тридцать пять очков?"
                    m "Конечно! Обычная цена."
                    hide screen hermione_main
                    with d3
                    $ h_body = "03_hp/13_hermione_main/body_69.png" #Sprite of Hermione's upper body.
                    $ h_xpos=140 #Defines position of the Hermione's full length sprite. (Default 370). (Center: 140)
                    show screen hermione_main
                    with d3
                    her "..................."
                    hide screen hermione_main
                    with d3
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
                    $ h_xpos=140 #Defines position of the Hermione's full length sprite. (Default 370). (Center: 140)
                    $ h_ypos=0
                    $ h_body = "03_hp/13_hermione_main/body_69.png" #Sprite of Hermione's upper body.
                    show screen hermione_main
                    with d3
                    her "Просто на всякий случай..."
                    stop music fadeout 1.0
                    hide screen hermione_main
                    with d5

                    show screen blkfade
                    with Dissolve(1)
                    $ renpy.play('sounds/08_hop_on_desk.mp3') #Sound of the desk squeaking. 
                    pause 5
                    $ h_body = "03_hp/13_hermione_main/body_16.png"
                    $ her_head_xpos=390 #Defines position of the Hermione's full length sprite. (Default 370). 140 - center. Bottom right: 390
                    $ her_head_ypos=340 #Defines position of the Hermione's full length sprite. (Default 0). Right bottom corner: 340 - head only. 235 - tits.
                    show screen h_head2
                    her2 "Просто для протокола..."
                    $ h_body = "03_hp/13_hermione_main/body_17.png"
                    her2 "Я все еще считаю, что это совершенно недопустимая услуга, покупать одну из своих студенток, сэр."
                    hide screen h_head2
                    m "Правильно. И уж более неуместно продавать себя своему директору. Не согласишься?"
                    show screen h_head2
                    $ h_body = "03_hp/13_hermione_main/body_69.png"
                    her ".........."
                    hide screen h_head2
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
                    show screen h_head2
                    $ h_body = "03_hp/13_hermione_main/body_87.png"
                    play music "music/(Orchestral) Playful Tension by Shadow16nh.mp3" fadein 1 fadeout 1 # SEX THEME.
                    her ".............."
                    $ h_body = "03_hp/13_hermione_main/body_85.png"
                    her2 "Что если мои родители узнают об этом, сэр?"
                    her2 "Мама никогда не поймет..."
                    $ h_body = "03_hp/13_hermione_main/body_44.png"
                    her "А насчет моего отца..."
                    hide screen h_head2
                    menu:
                        m "..."
                        "{size=-3}\"Твой отец гордился бы тобой!\"{/size}":
                            show screen h_head2
                            her "Я сомневаюсь..."
                            her "Да, я делаю это в благих целях, но..."
                            show screen h_head2
                            $ h_body = "03_hp/13_hermione_main/body_61.png"
                            her "Он никогда не видел меня такой..."
                            her "Он никогда не должен узнать об этом..."
                            hide screen h_head2
                        "{size=-3}\"Твой папочка отшлепал бы тебя!\"{/size}":
                            show screen h_head2
                            $ h_body = "03_hp/13_hermione_main/body_48.png"
                            her "Он бы не посмел!"
                            $ h_body = "03_hp/13_hermione_main/body_44.png"
                            her "И в любом случае я уже взрослая для такого..."
                            hide screen h_head2
                            g9 "Я бы сказал, что ты в идеальном возрасте для такого..."
                            show screen h_head2
                            her "А?"
                            $ h_body = "03_hp/13_hermione_main/body_57.png"
                            her "Я не понимаю о чем вы, сэр."
                            hide screen h_head2
                        "{size=-3}\"Твой папочка отрекся бы от тебя!\"{/size}":
                            show screen h_head2
                            $ h_body = "03_hp/13_hermione_main/body_34.png"
                            her "Вы вероятно правы, сэр..."
                            $ h_body = "03_hp/13_hermione_main/body_22.png"
                            her "(Ох папочка, мне очень жаль...)"
                            $ h_body = "03_hp/13_hermione_main/body_21.png"
                            her "Он никогда не должен узнать..."
                            hide screen h_head2
                        "{size=-3}\"Твой отец хотел бы посмотреть на это!\"{/size}":
                            show screen h_head2
                            $ h_body = "03_hp/13_hermione_main/body_33.png"
                            her "Он бы не посмел! Ему было бы стыдно за меня!"
                            hide screen h_head2
                            m "Ты в этом уверена?"
                            show screen h_head2
                            $ h_body = "03_hp/13_hermione_main/body_32.png"
                            her "Абсолютно! Мой папа культурный человек!"
                            hide screen h_head2
                            m "Но {size=+4}он{/size} {size=+4}мужчина{/size}, верно?"
                            show screen h_head2
                            $ h_body = "03_hp/13_hermione_main/body_50.png"
                            her "....................."
                            $ h_body = "03_hp/13_hermione_main/body_29.png"
                            her "Папа никога не должен узнать об этом..."
                            hide screen h_head2
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
                    
                    show screen h_head2
                    $ h_body = "03_hp/13_hermione_main/body_31.png"
                    her "Профессор?"
                    hide screen h_head2
                    m "А?"
                    show screen h_head2
                    $ h_body = "03_hp/13_hermione_main/body_44.png"
                    her "Могу я задать вопрос?"
                    hide screen h_head2
                    m "Попробуй..."
                    show screen h_head2
                    $ h_body = "03_hp/13_hermione_main/body_33.png"
                    her "..............."
                    $ h_body = "03_hp/13_hermione_main/body_57.png"
                    her "Вы когда-нибудь любили...?"
                    hide screen h_head2
                    menu:
                        m "..."
                        "\"Это смешно! Любовь это ложь!\"":
                            show screen h_head2
                            $ h_body = "03_hp/13_hermione_main/body_29.png"
                            her "Очень жаль, что вы так считаете, сэр!"
                            $ h_body = "03_hp/13_hermione_main/body_50.png"
                            her "Но вы можете очень сильно ошибаться!"
                            $ h_body = "03_hp/13_hermione_main/body_54.png"
                            her2 "Я считаю, что настоящая любовь вращает Землю!"
                            hide screen h_head2
                            m "На самом деле момент сохранения импульса отвечает за это."
                            show screen h_head2
                            $ h_body = "03_hp/13_hermione_main/body_44.png"
                            her "А?"
                            hide screen h_head2
                            m "Забудь. Готова снять рубашку?"
                            show screen h_head2
                            $ h_body = "03_hp/13_hermione_main/body_50.png"
                            her "............"      
                            hide screen h_head2
                        "\"Молчи и продолжай танцевать\"":
                            show screen h_head2
                            $ h_body = "03_hp/13_hermione_main/body_50.png"
                            her "Но вы сказали, что я могла задать вопрос..."
                            hide screen h_head2
                            m "И ты это сделала, не так ли?"
                            show screen h_head2
                            $ h_body = "03_hp/13_hermione_main/body_31.png"
                            her "!!!............"
                            $ h_body = "03_hp/13_hermione_main/body_50.png"
                            her2 "...................................."
                            hide screen h_head2
                            m "Теперь снимай свою рубашку."
                            show screen h_head2
                            $ h_body = "03_hp/13_hermione_main/body_69.png"
                            her "........"
                            hide screen h_head2
                        "\"Да...очень и очень давно...\"":
                            hide screen h_head2
                            m "Да... очень и очень давно..."
                            show screen h_head2
                            $ h_body = "03_hp/13_hermione_main/body_31.png"
                            her2 "!!!!!??.............................."
                            hide screen h_head2
                            m "Ее имя было Эден..."
                            show screen h_head2
                            $ h_body = "03_hp/13_hermione_main/body_45.png"
                            her "Она была красива?"
                            hide screen h_head2
                            m "Более чем..."
                            m "Она была умна, зелена и совершенна..."
                            show screen h_head2
                            $ h_body = "03_hp/13_hermione_main/body_87.png"
                            her "Она была... \"зелена\"...?"
                            $ h_body = "03_hp/13_hermione_main/body_47.png"
                            her2 "Вы издеваетесь, сэр?"
                            hide screen h_head2
                            m "Ох, вы люди, ничего не знаете о настоящей любви..."
                            show screen h_head2
                            $ h_body = "03_hp/13_hermione_main/body_55.png"
                            her ".....................................?"
                            hide screen h_head2
                            m "Э-э...то есть, снимай рубашку, девочка!"
                            show screen h_head2
                            $ h_body = "03_hp/13_hermione_main/body_69.png"
                            her "................."
                            hide screen h_head2
                        "\"Мне кажется я влюбляюсь прямо сейчас!\"":
                            show screen h_head2
                            $ h_body = "03_hp/13_hermione_main/body_69.png"
                            her "Не нужно быть таким вульгарным, сэр."
                            hide screen h_head2
                            m "Ох, но мне кажется это так!"
                            show screen h_head2
                            $ h_body = "03_hp/13_hermione_main/body_66.png"
                            her "Сэр, Пожалуйста!"
                            $ h_body = "03_hp/13_hermione_main/body_55.png"
                            her "Я одна из ваших студенток!"
                            $ h_body = "03_hp/13_hermione_main/body_57.png"
                            her "И вы старе моего отца!"
                            hide screen h_head2
                            m "{size=-4}(Не представляешь насколько, девочка.){/size}"
                            show screen h_head2
                            $ h_body = "03_hp/13_hermione_main/body_55.png"
                            her2 "Некоторые ученые считают, что \"любовь\" это ничто иное, как химическая реакция..."
                            $ h_body = "03_hp/13_hermione_main/body_16.png"
                            her2 "И когда человек испытывает сексуальное влечение, тот же тип гормонов--"
                            hide screen h_head2
                            m "Мисс Грейнджер!"
                            show screen h_head2
                            $ h_body = "03_hp/13_hermione_main/body_15.png"
                            her "Да, сэр?"
                            hide screen h_head2
                            m "Вы забыли чем мы занимаемся?"
                            show screen h_head2
                            $ h_body = "03_hp/13_hermione_main/body_24.png"
                            her "Ох, мои извинения, сэр... Иногда я отвлекаюсь."
                            hide screen h_head2
                            m "Давай ты уже снимешь свою рубашку?!"
                            show screen h_head2
                            $ h_body = "03_hp/13_hermione_main/body_29.png"
                            her "Верно..."
                            hide screen h_head2
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
                    g9 "Да! Сисьски!"
                    
                    $ badges = False # Hides any badges from hermione_main screen.
                    
                    show screen h_head2
                    $ her_head_xpos=390 #Defines position of the Hermione's full length sprite. (Default 370). 140 - center. Bottom right: 390
                    $ her_head_ypos=235 #Defines position of the Hermione's full length sprite. (Default 0). Right bottom corner: 340 - head only. 235 - tits.
                    $ h_body = "03_hp/13_hermione_main/body_90.png"
                    her "Вам обязательно быть настолько пошлым, сэр?"
                    hide screen h_head2
                    menu: 
                        "-Достать член и начать дрочить-":
                            hide screen bld1
                            show screen ctc
                            with d3
                            pause
                            show screen blkfade
                            with d6
                            show screen h_head2
                            $ h_body = "03_hp/13_hermione_main/body_94.png"
                            her "Профессор Дамблдор?!"
                            hide screen h_head2
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
                            show screen h_head2
                            $ h_body = "03_hp/13_hermione_main/body_95.png"
                            her "Н-но..."
                            her "Ваш..."
                            hide screen h_head2
                            m "Да... Ах, да, это великолепно..."
                            show screen h_head2
                            $ h_body = "03_hp/13_hermione_main/body_98.png"
                            her "Профессор!!!"
                            her "Я хочу, чтобы вы убрали эту..."
                            $ h_body = "03_hp/13_hermione_main/body_99.png"
                            her "...штуку."
                            hide screen h_head2
                            menu:
                                m "..."
                                "\"Я сказал, продолжай танцевать, девочка!\"":
                                    if whoring >= 15: #LEVEL 06. You jerk off your cock and Hermione is OK with it.
                                        show screen h_head2
                                        $ h_body = "03_hp/13_hermione_main/body_99.png"
                                        her "Но..."
                                        her "............................."
                                        $ h_body = "03_hp/13_hermione_main/body_101.png"
                                        her2 "Ну, ладно, но если только вы пообешаете мне на кончать, сэр."
                                        hide screen h_head2
                                        menu:
                                            m "..."
                                            "-Пообещать сдержаться-":
                                                    $ d_flag_07 = True #Promised to hold it.
                                                    show screen h_head2
                                                    $ h_body = "03_hp/13_hermione_main/body_102.png"
                                                    her "Ну, тогда ладно..."
                                                    hide screen h_head2
                                            "-Не давать такого обещания-":
                                                $ d_flag_07 = False #Did not promise to hold it.
                                                m "\"Не кончать\"? Это похоже на пытку!"
                                                m "Пожалуйста, сдержите свои садистские наклонности, Мисс Грейнджер."
                                                show screen h_head2
                                                $ h_body = "03_hp/13_hermione_main/body_103.png"
                                                her "У меня нет никаких... садистких наклонностей, сэр!"
                                                her "Я просто хочу, чтобы..."
                                                hide screen h_head2
                                                g9 "Да... У тебя такие отличные сиськи..."
                                                show screen h_head2
                                                $ h_body = "03_hp/13_hermione_main/body_97.png"
                                                her "............"
                                                hide screen h_head2
                                                g9 "А-ах... Да..."
                                                show screen h_head2
                                                $ h_body = "03_hp/13_hermione_main/body_97.png"
                                                her ".........."
                                                $ h_body = "03_hp/13_hermione_main/body_99.png"
                                                her "Ладно! Будь по вашему, сэр!"
                                                $ h_body = "03_hp/13_hermione_main/body_103.png"
                                                her "{size=-5}(Как обычно...){/size}"
                                                hide screen h_head2
                                        show screen blktone
                                        with d3
                                        ">Вы продолжаете дрочить, наблюдая за Гермионой..."
                                        show screen h_head2
                                        $ h_body = "03_hp/13_hermione_main/body_90.png"
                                        her "Время кончить, я пологаю..."
                                        hide screen h_head2
                                        m "Да, девочка! Снимай свои трусики!"
                                        show screen h_head2
                                        $ h_body = "03_hp/13_hermione_main/body_91.png"
                                        her "........"
                                        hide screen h_head2
                                        show screen blktone8
                                        with d3
                                        ">Гермиона слегка наклоняется и стягивает с себя трусики..."
                                        ">Вы видите, что она делает все возможное, чтобы это выглядело изящно..."
                                        ">Но ее попытки выглядеть как настоящая стриптизерша, выглядят довольно смешно..."
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
                                        ">Тем не менее вы показываете ей, что у нее получается весьма неплохо..."
                                        ">Начиная дрочить еще быстрее!"
                                        show screen h_head2
                                        $ h_body = "03_hp/13_hermione_main/body_91.png"
                                        her ".........."
                                        hide screen h_head2
                                        show screen blktone8
                                        with d3
                                        ">Внезапно Гермиона начинает выдавать целые сложные пируэты..."
                                        m "{size=-4}(Это выглядит очень даже не дурно...){/size}"
                                        ">Гермиона хватает и слегка скручивает свои сиськи, после чего снова делает серию сложны пируэтов (иногда нелепых)..."
                                        m "{size=-4}(Она практиковалась?){/size}"
                                        g9 "Ох, какое мне дело?"
                                        ">Вы начинаете еще сильнее надрачивать ваш твердый как алмаз член."
                                        show screen h_head2
                                        $ h_body = "03_hp/13_hermione_main/body_102.png"
                                        her "{size=-5}(Три-два-раз... Три-два-раз... И шаг!){/size}"
                                        hide screen h_head2
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
                                        show screen h_head2
                                        $ h_body = "03_hp/13_hermione_main/body_102.png"
                                        her "Фиу... Это было--"
                                        hide screen h_head2
                                        with hpunch
                                        g4 "АРГХ! ЕБАНАЯ ДЫРКА!"
                                        hide screen hermione_main
                                        with d3
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
                                        $ uni_sperm = True #Triggers universal sperm to show on hermione_main screen.
                                        $ h_body = "03_hp/13_hermione_main/body_104.png"
                                        $ u_sperm = "03_hp/13_hermione_main/auto_04.png"
                                        show screen h_head2  
                                        her "??!!!"
                                        hide screen h_head2
                                        show screen bld1
                                        with d3
                                        $ h_body = "03_hp/13_hermione_main/body_97.png"
                                        show screen h_head2  
                                        her "Профессор!!!"
                                        $ g_c_c_u_pic = "03_hp/08_animation_02/09_cum_18.png"
                                        hide screen h_head2
                                        if d_flag_07: #Promised to hold it.
                                            show screen h_head2                                                              # HERMIONE
                                            $ h_body = "03_hp/13_hermione_main/body_97.png" # HERMIONE
                                            her "Нет, профессор! Вы обещали!"
                                            hide screen h_head2
                                            g4 "Ох, детка... Это было довольно круто..."
                                            show screen h_head2                                                              # HERMIONE
                                            $ h_body = "03_hp/13_hermione_main/body_98.png" # HERMIONE
                                            her "ВЫ не сдержали слово, сэр!"
                                            hide screen h_head2
                                            m "А? О чем ты говоришь?"
                                            show screen h_head2                                                              # HERMIONE
                                            $ h_body = "03_hp/13_hermione_main/body_113.png" # HERMIONE
                                            her "Как вы могли так со мной поступить, сэр?"
                                            hide screen h_head2
                                            m "Ох, успокойся, девочка."
                                            m "Сегодня ты заслужила свои очки."
                                            m "Теперь, просто оденься и уходи, пока кто-нибудь не застукал нас тут."
                                            show screen h_head2                                                              # HERMIONE
                                            $ h_body = "03_hp/13_hermione_main/body_114.png" # HERMIONE
                                            her "*плачет!*........................"
                                            hide screen h_head2        
                                            $ mad += 50
                                            show screen blkfade 
                                            with d3
                                            $ uni_sperm = False #Sperm layer is not displayed.
                                            $ aftersperm = True #Aftersperm layer is displayed. 
                                            stop music fadeout 5.0
                                            ">.................{w}.................{w}.................{w}................."
                                            show screen h_head2                                                              # HERMIONE
                                            $ h_body = "03_hp/13_hermione_main/body_12.png" # HERMIONE
                                            her "...Могу я получить оплату, сэр... пожалуйста?"
                                            hide screen h_head2   
                                            jump done_with_dancing
                                        else:
                                            $ h_body = "03_hp/13_hermione_main/body_97.png"
                                            show screen h_head2  
                                            her "Было жарко..."
                                            hide screen h_head2  
                                            $ g_c_u_pic = "03_hp/08_animation_02/06_jerking_01.png" # Genie stands still with his dick in hand.
                                            m "Аха... Даа... Это просто безумие..."
                                            $ h_body = "03_hp/13_hermione_main/body_105.png"
                                            show screen h_head2  
                                            her "Вы всю меня обкончали..."
                                            her "Я вам ученик и ..."
                                            $ h_body = "03_hp/13_hermione_main/body_106.png"
                                            show screen h_head2  
                                            her "Вы просто кончили на меня..."
                                            hide screen h_head2  
                                            g9 "Я знаю! Довольно круто, да?!"
                                            $ h_body = "03_hp/13_hermione_main/body_107.png"
                                            show screen h_head2  
                                            her "Ничего подобного!"
                                            #her "You should not have done this, сэр!"
                                            her2 "Вы должны вести себя как подобает директору!"
                                            hide screen h_head2  
                                            m "Правда? Что ты хочешь от меня?"
                                            m "Направить его в сторону стены или обратно в трусы и просто кончить?"
                                            $ h_body = "03_hp/13_hermione_main/body_105.png"
                                            show screen h_head2
                                            her "........"
                                            $ h_body = "03_hp/13_hermione_main/body_101.png"
                                            show screen h_head2
                                            her "Тем не менее, вы не должны были..."
                                            $ h_body = "03_hp/13_hermione_main/body_102.png"
                                            show screen h_head2
                                            her "Я согласилась танцевать для вас..."
                                            her "Но я не соглашалась быть оскверненной вашей спермой."
                                            hide screen h_head2  
                                            m "Я думаю, это уже произошло..."
                                            $ h_body = "03_hp/13_hermione_main/body_100.png"
                                            show screen h_head2
                                            her "Я требую дополнительные очки за это!"
                                            hide screen h_head2  
                                            m "Конечно, как иначе..."
                                            menu:
                                                m "..."
                                                "\"Ты получишь 1 дополнительное очко.\"":
                                                    play music "music/Chipper Doodle v2.mp3" fadein 1 fadeout 1 # HERMIONE'S THEME.
                                                    $ h_body = "03_hp/13_hermione_main/body_101.png"
                                                    show screen h_head2
                                                    her "Одно дополнительное очко?"
                                                    $ h_body = "03_hp/13_hermione_main/body_98.png"
                                                    her2 "Одно жалкое очко за все, что вы со мной сделали?"
                                                    $ h_body = "03_hp/13_hermione_main/body_101.png"
                                                    her "Это просто оскорбительно, сэр!"
                                                    hide screen h_head2  
                                                    m "Одно очко, Мисс Грейнджер. Забирайте или уходите."
                                                    $ h_body = "03_hp/13_hermione_main/body_103.png"
                                                    show screen h_head2
                                                    her "............."
                                                    $ h_body = "03_hp/13_hermione_main/body_101.png"
                                                    her "Я беру его."
                                                    hide screen h_head2  
                                                    $ mad += 30
                                                    $ current_payout = 36
                                                    hide screen bld1
                                                    with d3
                                                    pause
                                                    show screen blkfade
                                                    with d7
                                                    pause.5
                                                    $ aftersperm = True #Show cum stains on Hermione's uniform.
                                                    jump done_with_dancing
                                                "\"Десять дополнительных очков.\"":
                                                    $ current_payout = 45
                                                    $ h_body = "03_hp/13_hermione_main/body_101.png"
                                                    show screen h_head2
                                                    her "Десять дополнительных очков, сэр?"
                                                    her "Но это слишком мало!"
                                                    hide screen h_head2  
                                                    m "Десять очков. Берите или уходите, Мисс Грейнджер."
                                                    $ h_body = "03_hp/13_hermione_main/body_103.png"
                                                    show screen h_head2
                                                    her "..............."
                                                    $ h_body = "03_hp/13_hermione_main/body_101.png"
                                                    show screen h_head2
                                                    her "Ну, ладно... Лучше чем ничего..."
                                                    hide screen h_head2  
                                                    $ mad += 11
                                                    hide screen bld1
                                                    with d3
                                                    pause
                                                    show screen blkfade
                                                    with d7
                                                    pause.5
                                                    $ aftersperm = True #Show cum stains on Hermione's uniform.
                                                    jump done_with_dancing
                                                "\"Вы получите 25 дополнительных очков.\"":
                                                    $ current_payout = 60
                                                    $ h_body = "03_hp/13_hermione_main/body_102.png"
                                                    show screen h_head2
                                                    her2 "Да, думаю этого хватит."
                                                    hide screen h_head2  
                                                    m "Теперь вы счастливы?"
                                                    $ h_body = "03_hp/13_hermione_main/body_102.png"
                                                    show screen h_head2
                                                    her "Да, сэр. Спасибо сэр."
                                                    hide screen h_head2  
                                                    $ h_c_u_pic = "03_hp/08_animation_02/08_sits.png"
                                                    hide screen bld1
                                                    with d3
                                                    pause
                                                    show screen blkfade
                                                    with d7
                                                    pause.5
                                                    $ aftersperm = True #Show cum stains on Hermione's uniform.
                                                    jump done_with_dancing
                                                "\"Вы получаете 50 дополнительных очков.\"":
                                                    $ current_payout = 85
                                                    $ h_body = "03_hp/13_hermione_main/body_95.png"
                                                    show screen h_head2
                                                    her "Серьезно?!"
                                                    $ h_body = "03_hp/13_hermione_main/body_94.png"
                                                    her "Ох, не знаю что сказать..."
                                                    hide screen h_head2  
                                                    m "Мне понравилось,Мисс Грейнджер."
                                                    show screen h_head2
                                                    $ h_body = "03_hp/13_hermione_main/body_109.png"
                                                    her "Спасибо сэр..."
                                                    hide screen h_head2  
                                                    m "Так же мне понравилось заливать твое гибкое тельце своей спермой..."
                                                    $ h_body = "03_hp/13_hermione_main/body_108.png"
                                                    show screen h_head2
                                                    her "Сэр......"
                                                    hide screen h_head2  
                                                    m "И так, просто позвольте мне показать свою признательность."
                                                    m "Пятьдесяц очков, заслуженно, Мисс Грейнджер."
                                                    $ h_body = "03_hp/13_hermione_main/body_108.png"
                                                    show screen h_head2
                                                    her "Огромное спасибо, сэр."
                                                    hide screen h_head2  
                                                    $ h_c_u_pic = "03_hp/08_animation_02/08_sits.png"
                                                    hide screen bld1
                                                    with d3
                                                    pause
                                                    show screen blkfade
                                                    with d7
                                                    pause.5
                                                    $ aftersperm = True #Show cum stains on Hermione's uniform.
                                                    jump done_with_dancing
                                                "\"Ты ни черта не получишь!\"":
                                                    stop music fadeout 1.0
                                                    $ h_body = "03_hp/13_hermione_main/body_104.png"
                                                    show screen h_head2
                                                    her "Что? Даже обычной платы?"
                                                    hide screen h_head2  
                                                    menu:
                                                        m "..."
                                                        "\"Ох, нет, их ты поучишь.\"":
                                                            $ mad += 30
                                                            $ h_body = "03_hp/13_hermione_main/body_101.png"
                                                            show screen h_head2
                                                            her "Как великодушно с вашей стороны, сэр." 
                                                            hide screen h_head2  
                                                            hide screen bld1
                                                            with d3
                                                            pause
                                                            show screen blkfade
                                                            with d7
                                                            pause.5
                                                            $ aftersperm = True #Show cum stains on Hermione's uniform.
                                                            jump done_with_dancing
                                                        "\"Нет, их тоже не получишь!\"":
                                                            play music "music/Chipper Doodle v2.mp3" fadein 1 fadeout 1 # HERMIONE'S THEME.
                                                            $ h_body = "03_hp/13_hermione_main/body_104.png"
                                                            show screen h_head2
                                                            her "!!!?"
                                                            her "Я танцевала для вас, сэр..."
                                                            $ h_body = "03_hp/13_hermione_main/body_105.png"
                                                            her "Я унижалась для вашего веселья..."
                                                            $ h_body = "03_hp/13_hermione_main/body_107.png"
                                                            her "Позволила кончить на себя..."
                                                            $ h_body = "03_hp/13_hermione_main/body_110.png"
                                                            with hpunch
                                                            her "И не получу ничего?!"
                                                            hide screen h_head2  
                                                            m "Вы провалились, Мисс Грейнджер!"
                                                            $ h_body = "03_hp/13_hermione_main/body_101.png"
                                                            show screen h_head2
                                                            her "Ох, это низко даже для вас, сэр!"
                                                            hide screen h_head2  
                                                            m "Я сказал: вы провалились."
                                                            $ h_body = "03_hp/13_hermione_main/body_110.png"
                                                            show screen h_head2
                                                            her "*Тяжелый вздох!*"
                                                            $ mad += 90
                                                            hide screen h_head2  
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
                                                            jump could_not_flirt #Leaves without getting any очков.
                                                        

                                    else: # You jerk off your cock and Hermione is NOT OK with it.
                                        $ h_body = "03_hp/13_hermione_main/body_103.png"
                                        show screen h_head2
                                        stop music fadeout 1.0
                                        her "Нет, сэр!"
                                        hide screen h_head2  
                                        m "А?"
                                        show screen blkfade
                                        with d7
                                        ">Гермиона спрыгивает со стола и начинает спешно одеваться, посматривая на вас..."
                                        m "Ох, да ладно! Не оставляй меня так!"
                                        $ her_head_xpos=390 #Defines position of the Hermione's full length sprite. (Default 370). 140 - center. Bottom right: 390
                                        $ her_head_ypos=340 #Defines position of the Hermione's full length sprite. (Default 0). Right bottom corner: 340 - head only. 235 - tits.
                                        $ h_body = "03_hp/13_hermione_main/body_101.png"
                                        show screen h_head2
                                        her "Танец окончен, сэр!"
                                        hide screen h_head2
                                        pause 1
                                        show screen h_head2
                                        $ h_body = "03_hp/13_hermione_main/body_79.png"
                                        her "Я хотела бы получить очки!"
                                        hide screen h_head2
                                        m "Упрямая девчонка..."
                                        ">Вы неохотно убрали свой член..."
                                        show screen h_head2
                                        $ h_body = "03_hp/13_hermione_main/body_79.png"
                                        her "Полагаю, я могу получить сейчас свою оплату."
                                        hide screen h_head2
                                        jump done_with_dancing
                                "\"Ладно. Не драматизируй ты так!\"": 
                                    $ h_body = "03_hp/13_hermione_main/body_103.png"
                                    show screen h_head2
                                    her2 "......................"
                                    hide screen h_head2
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

                        "-Показать хорошие манеры и просто смотреть-":
                            pass
                    # JUST WATCHING.
                    show screen blktone
                    with d3
                    ">Вы смотрите танец Гермионы..."
                    $ h_body = "03_hp/13_hermione_main/body_97.png"
                    show screen h_head2
                    her "(Время заканчивать, я полагаю...)"
                    hide screen h_head2
                    m "Да! Снимай их!"
                    show screen h_head2
                    $ h_body = "03_hp/13_hermione_main/body_90.png"
                    her "........"
                    hide screen h_head2
                    show screen blktone8
                    with d3
                    ">Гермиона нагинается и стягивает свои трусики..."
                    ">Она делает все возможное, чтобы это выглядело изящно..."
                    ">Но ее попытки выглядеть как настоящая стриптизерша выглядят довольно смешно..."
                    show screen h_head2
                    $ h_body = "03_hp/13_hermione_main/body_109.png"
                    her ".........."
                    hide screen h_head2
                    ">Внезапно она начинает выдавать целые пируэты..."
                    hide screen h_head2
                    m "{size=-4}(Это выглядит довольно неплохо...){/size}"
                    ">Гермиона хватает и слегка скручивает свои сиськи, после чего снова делает серию сложны пируэтов (иногда нелепых)..."
                    m "{size=-4}(Она практиковалась?){/size}"
                    g9 "Ох, какое мне дело?"
                    show screen h_head2
                    $ h_body = "03_hp/13_hermione_main/body_102.png"
                    her "{size=-5}(Три-два-раз... Три-два-раз... And step!){/size}"
                    hide screen h_head2
                    ">Гермиона выполняет довольно сложные движения, которые могли бы выглядет довольно стильно и круто, если бы не ее прыгающие в разные стороны сиськи..."
                    g9 "Да, да, маленькая потаскушка!"
                    
                    show screen blkfade
                    with d3
                    $ hermione_chibi_xpos = -210 #400 = Near the desk.
                    $ hermione_chibi_ypos = 10
                    $ h_c_u_pic = "03_hp/08_animation_02/08_sits.png"
                    ">Еще несколько движений, пара жестов, поклон воображаемой аудитории и Гермиона резко падает на мягкую, замучанную попку."
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
                    show screen h_head2
                    $ h_body = "03_hp/13_hermione_main/body_108.png"
                    show screen bld1
                    with d3
                    her "Фиу... Было весьма захватывающе..."
                    hide screen h_head2 
                    menu:
                        m "..."
                        "{size=-3}\"Отличная работа, девочка! Ты правда знаешь как это делается!\"{/size}":
                            m "Отличная работа, девочка!"
                            show screen h_head2
                            $ h_body = "03_hp/13_hermione_main/body_109.png"
                            her "Правда?"
                            hide screen h_head2
                            m "Да! У тебя есть талант!"
                            show screen h_head2
                            $ h_body = "03_hp/13_hermione_main/body_108.png"
                            her "Спасибо сэр."
                            hide screen h_head2
                        "{size=-3}\"Хм... Это было ужасно...\"{/size}":
                            show screen h_head2
                            $ h_body = "03_hp/13_hermione_main/body_105.png"
                            her "Ох... Мне жаль..."
                            hide screen h_head2
                            m "Ничего... Тебе просто нужно практиковаться..."
                            show screen h_head2
                            $ h_body = "03_hp/13_hermione_main/body_107.png"
                            her "Эм... Буду иметь в виду, сэр..."
                            hide screen h_head2
                        "{size=-3}\".................................................\"{/size}":
                            show screen h_head2
                            $ h_body = "03_hp/13_hermione_main/body_108.png"
                            her "......................."
                            hide screen h_head2

                    
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
    $ uni_sperm = False #Sperm layer is not displayed in hermione screen.
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
    
    $ badges = True # Shows any badges from hermione_main screen.
    
    m "Да, Мисс Грейнджер. [current_payout] очков \"Гриффиндору\"." 
    $ h_xpos=140 #Defines position of the Hermione's full length sprite. (Default 370). (Center: 140)
    $ h_body = "03_hp/13_hermione_main/body_13.png" #Flashing Трусики
    show screen hermione_main
    hide screen hermione_01_f #Hermione stands still.
    with d3
    
    her "Спасибо, сэр..."

    if whoring <= 11:
        $ whoring +=1

    $ request_11_points += 1

    
    

    $ sperm_on_tits = False
    $ uni_sperm = False


    hide screen bld1
    hide screen hermione_main
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

    $ aftersperm = False #Show cum stains on Hermione's uniform.
    call music_block
    if daytime:
        $ hermione_takes_classes = True
        jump night_main_menu
    else:
        $ hermione_sleeping = True
        jump day_main_menu            


    

        

    
#############################################################################################################################
### LEVEL 05 ################################################################################################################   
###################REQUEST_16 (Level 05) (HANDJOB) (Day/Night) #####################################################
label new_request_16: #LV.5 (Whoring = 12 - 14)
    hide screen hermione_main 
    with d3
    if request_16_points == 0:
        m "{size=-4}(Попросить ее вздрочнуть мне?){/size}"
    else:
        m "{size=-4}(Попросить ее еще раз подрочить мне?){/size}"
    $ menu_x = 0.5 #Default position of the menu (0.5). Version B is $ menu_x = 0.2
    menu:
        "\"(Да, давай попробуем!)\"":
            show screen blktone
            with d3
            pass
        "\"(Не сейчас.)\"":
            jump new_personal_request
            
    $ current_payout = 45 #Used when haggling about price of th favor.  
    if request_16_points == 0: # FIRST EVENT <============================================================== EVENT 01
        m "Мисс Грейнджер."
        hide screen hermione_main                                                                                                                                                                                   #HERMIONE
        with d3                                                                                                                                                                                                                        #HERMIONE
        $ h_xpos=140 #Defines position of the Hermione's full length sprite. (Default 370). (Center: 140)                                                        #HERMIONE
        $ h_body = "03_hp/13_hermione_main/body_01.png" #Sprite of Hermione's upper body.                    #HERMIONE
        show screen hermione_main                                                                                                                                                                                 #HERMIONE
        with d3                                                                                                                                                                                                                        #HERMIONE
        her "Да, профессор?"
        m "Ты знаешь что такое \"работа ручками\"?"
        if whoring <=11:
            jump too_much
        hide screen hermione_main                                                                                                                                                                                   #HERMIONE
        with d3                                                                                                                                                                                                                        #HERMIONE
        $ h_xpos=140 #Defines position of the Hermione's full length sprite. (Default 370). (Center: 140)                                                        #HERMIONE
        $ h_body = "03_hp/13_hermione_main/body_79.png" #Sprite of Hermione's upper body.                    #HERMIONE
        show screen hermione_main                                                                                                                                                                                 #HERMIONE
        with d3                    
        her "А что?"
        m "Я хочу чтобы ты сделала это мне..."
        hide screen hermione_main                                                                                                                                                                                   #HERMIONE
        with d3                                                                                                                                                                                                                        #HERMIONE
        $ h_xpos=140 #Defines position of the Hermione's full length sprite. (Default 370). (Center: 140)                                                        #HERMIONE
        $ h_body = "03_hp/13_hermione_main/body_47.png" #Sprite of Hermione's upper body.                    #HERMIONE
        show screen hermione_main                                                                                                                                                                                 #HERMIONE
        with d3                    
        her "Профессор!"
        m "Просто одна услуга. Ничего страшного, да?"
        hide screen hermione_main                                                                                                                                                                                   #HERMIONE
        with d3                                                                                                                                                                                                                        #HERMIONE
        $ h_xpos=140 #Defines position of the Hermione's full length sprite. (Default 370). (Center: 140)                                                        #HERMIONE
        $ h_body = "03_hp/13_hermione_main/body_66.png" #Sprite of Hermione's upper body.                    #HERMIONE
        show screen hermione_main                                                                                                                                                                                 #HERMIONE
        with d3                    
        her "......"
        hide screen hermione_main                                                                                                                                                                                   #HERMIONE
        with d3                                                                                                                                                                                                                        #HERMIONE
        $ h_xpos=140 #Defines position of the Hermione's full length sprite. (Default 370). (Center: 140)                                                        #HERMIONE
        $ h_body = "03_hp/13_hermione_main/body_34.png" #Sprite of Hermione's upper body.                    #HERMIONE
        show screen hermione_main                                                                                                                                                                                 #HERMIONE
        with d3                    
        her "{size=-7}Я хочу 100 очков за это...{/size}"
        m "А? Что эт было?"
        hide screen hermione_main                                                                                                                                                                                   #HERMIONE
        with d3                                                                                                                                                                                                                        #HERMIONE
        $ h_xpos=140 #Defines position of the Hermione's full length sprite. (Default 370). (Center: 140)                                                        #HERMIONE
        $ h_body = "03_hp/13_hermione_main/body_32.png" #Sprite of Hermione's upper body.                    #HERMIONE
        show screen hermione_main                                                                                                                                                                                 #HERMIONE
        with d3                    
        her "Я хочу 100 очков за это!!!"
        m "100 очков, да?"
        m "И ты подрочишь мне и все такое, да?"
        hide screen hermione_main                                                                                                                                                                                   #HERMIONE
        with d3                                                                                                                                                                                                                        #HERMIONE
        $ h_xpos=140 #Defines position of the Hermione's full length sprite. (Default 370). (Center: 140)                                                        #HERMIONE
        $ h_body = "03_hp/13_hermione_main/body_66.png" #Sprite of Hermione's upper body.                    #HERMIONE
        show screen hermione_main                                                                                                                                                                                 #HERMIONE
        with d3                    
        her "{size=-7}Да...{/size}"
        m "Прости, я не расслышал..."
        hide screen hermione_main                                                                                                                                                                                   #HERMIONE
        with d3                                                                                                                                                                                                                        #HERMIONE
        $ h_xpos=140 #Defines position of the Hermione's full length sprite. (Default 370). (Center: 140)                                                        #HERMIONE
        $ h_body = "03_hp/13_hermione_main/body_32.png" #Sprite of Hermione's upper body.                    #HERMIONE
        show screen hermione_main                                                                                                                                                                                 #HERMIONE
        with d3                 
        her "Да, я сказала да! Я подрочу вам, сэр!"
        label back_to_handjob_choices:
        menu:
            m "..."
            "\"Ты получишь 15 очков.\"":
                $ mad +=7
                hide screen hermione_main                                                                                                                                                                                   #HERMIONE
                with d3                                                                                                                                                                                                                        #HERMIONE
                $ h_xpos=140 #Defines position of the Hermione's full length sprite. (Default 370). (Center: 140)                                                        #HERMIONE
                $ h_body = "03_hp/13_hermione_main/body_69.png" #Sprite of Hermione's upper body.                    #HERMIONE
                show screen hermione_main                                                                                                                                                                                 #HERMIONE
                with d3                 
                her "За 15 очков вы сможете немного поприставать ко мне, но это все, сэр."
                her "Я не продешевлю и не стану дрочить вам за 15 очков."
                her "Это оскорбительн, сэр."
                jump back_to_handjob_choices
            "\"Ты получишь 45 очков.\"":
                hide screen hermione_main                                                                                                                                                                                   #HERMIONE
                with d3                                                                                                                                                                                                                        #HERMIONE
                $ h_xpos=140 #Defines position of the Hermione's full length sprite. (Default 370). (Center: 140)                                                        #HERMIONE
                $ h_body = "03_hp/13_hermione_main/body_69.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
                show screen hermione_main                                                                                                                                                                                 #HERMIONE
                with d3                 
                her "....."
                hide screen hermione_main                                                                                                                                                                                   #HERMIONE
                with d3                                                                                                                                                                                                                        #HERMIONE
                $ h_xpos=140 #Defines position of the Hermione's full length sprite. (Default 370). (Center: 140)                                                        #HERMIONE
                $ h_body = "03_hp/13_hermione_main/body_87.png" #Sprite of Hermione's upper body.                    #HERMIONE
                show screen hermione_main                                                                                                                                                                                 #HERMIONE
                with d3                 
                her "45 очков...?"
                her "Это вернет \"Гриффиндор\" в лидеры..."
                m "Это значит \"Да\"?"
                hide screen hermione_main                                                                                                                                                                                   #HERMIONE
                with d3                                                                                                                                                                                                                        #HERMIONE
                $ h_xpos=140 #Defines position of the Hermione's full length sprite. (Default 370). (Center: 140)                                                        #HERMIONE
                $ h_body = "03_hp/13_hermione_main/body_79.png" #Sprite of Hermione's upper body.                    #HERMIONE
                show screen hermione_main                                                                                                                                                                                 #HERMIONE
                with d3                 
                her "YesДа, это значит да, сэр."
                m "Отлично!"
            "\"Ты получишь 100 очков.\"":
                play music "music/Chipper Doodle v2.mp3" fadein 1 fadeout 1 # HERMIONE'S THEME.
                $ current_payout = 100 #Used when haggling about price of th favor.
                $ mad = 0
                hide screen hermione_main                                                                                                                                                                                   #HERMIONE
                with d3                                                                                                                                                                                                                        #HERMIONE
                $ h_xpos=140 #Defines position of the Hermione's full length sprite. (Default 370). (Center: 140)                                                        #HERMIONE
                $ h_body = "03_hp/13_hermione_main/body_72.png" #Sprite of Hermione's upper body.                    #HERMIONE
                show screen hermione_main                                                                                                                                                                                 #HERMIONE
                with d3                 
                her "100 очков?!"
                her "Это вернет \"Гриффиндор\" в лидеры!"
                m "Is that a \"yes\" then?"
                hide screen hermione_main                                                                                                                                                                                   #HERMIONE
                with d3                                                                                                                                                                                                                        #HERMIONE
                $ h_xpos=140 #Defines position of the Hermione's full length sprite. (Default 370). (Center: 140)                                                        #HERMIONE
                $ h_body = "03_hp/13_hermione_main/body_75.png" #Sprite of Hermione's upper body.                    #HERMIONE
                show screen hermione_main                                                                                                                                                                                 #HERMIONE
                with d3                 
                her "Конечно!"
                hide screen hermione_main                                                                                                                                                                                   #HERMIONE
                with d3                                                                                                                                                                                                                        #HERMIONE
                $ h_xpos=140 #Defines position of the Hermione's full length sprite. (Default 370). (Center: 140)                                                        #HERMIONE
                $ h_body = "03_hp/13_hermione_main/body_80.png" #Sprite of Hermione's upper body.                    #HERMIONE
                show screen hermione_main                                                                                                                                                                                 #HERMIONE
                with d3                 
                her "Если это принесет \"Гриффиндору\" 100 очков, то я согласна прикасаться...к вашей штуке."
        # GENIE STANDS WITH HIS COCK OUT
       
        play music "music/(Orchestral) Playful Tension by Shadow16nh.mp3" fadein 1 fadeout 1 # SEX THEME.
        hide screen hermione_main                                                                                                                                                                                   #HERMIONE
        hide screen genie
        $ genie_chibi_xpos = 5 #-185 behind the desk.
        $ genie_chibi_ypos = 10
        $ g_c_u_pic = "jerking_off_02_ani"
        show screen chair_02
        show screen g_c_u
        show screen desk_02

        hide screen blkfade
        hide screen blktone
        hide screen bld1
        show screen ctc
        with fade
        pause
        show screen bld1
        with d3
        $ her_head_xpos=390 #Defines position of the Hermione's full length sprite. (Default 370). 140 - center. Bottom right: 390
        $ her_head_ypos=235 #Defines position of the Hermione's full length sprite. (Default 0). Right bottom corner: 340 - head only. 235 - tits.
        show screen h_head2                                                             # HERMIONE
        $ h_body = "03_hp/13_hermione_main/body_31.png" # HERMIONE
        her "..........."
        hide screen h_head2
        m "Как будешь готова, девочка."
        show screen h_head2                                                             # HERMIONE
        $ h_body = "03_hp/13_hermione_main/body_34.png" # HERMIONE
        her "Верно..."
        hide screen h_head2
        hide screen bld1
        with d3
        $ walk_xpos=400 #Animation of walking chibi. (From)
        $ walk_xpos2=280 #Coordinates of it's movement. (To)
        $ hermione_speed = 03.0 #The speed of moving the walking animation across the screen.
        show screen hermione_walk_01 
        pause.1
        show screen blkfade
        with Dissolve(1)
        pause.3
        label event_01_round_02:
        ">Гермиона берет своими худыми ручками ваш член..."
        m "Отлично. Теперь дрочи его."
        show screen h_head2                                                             # HERMIONE
        $ h_body = "03_hp/13_hermione_main/body_34.png" # HERMIONE
        her "Верно..."
        hide screen h_head2 
        #Stroking the cock.
        $ genie_chibi_xpos = 60 #-185 behind the desk.
        $ genie_chibi_ypos = 10
        $ g_c_u_pic = "handjob_ani"
        hide screen hermione_walk_01 
        hide screen blkfade
        with d3
        show screen ctc
        pause
        play music "music/(Orchestral) Playful Tension by Shadow16nh.mp3" fadein 1 fadeout 1 # SEX THEME.
        hide screen ctc
        show screen bld1
        with d3
        g9 "Отлично..."
        if request_16_points == 0:
            show screen h_head2                                                             # HERMIONE
            $ h_body = "03_hp/13_hermione_main/body_48.png" # HERMIONE
            her "!!!"
            her "Как насчет кончитьы, сэр?!"
            hide screen h_head2 
            m "Кончить?"
            m "Не будь глупа, мы только начали."
            show screen h_head2                                                             # HERMIONE
            $ h_body = "03_hp/13_hermione_main/body_34.png" # HERMIONE
            her "Ох..."
            her "......"
            show screen h_head2                                                             # HERMIONE
            $ h_body = "03_hp/13_hermione_main/body_44.png" # HERMIONE
            her2 "Вы предупредите меня, сэр?"
            hide screen h_head2 
        else:
            show screen h_head2                                                             # HERMIONE
            $ h_body = "03_hp/13_hermione_main/body_34.png" # HERMIONE
            her "Сэр...?"
            hide screen h_head2    
            m "Что такое?"
            show screen h_head2                                                             # HERMIONE
            $ h_body = "03_hp/13_hermione_main/body_34.png" # HERMIONE
            her "Вы могли бы предупредить меня... э-эм... когда вы..."
            hide screen h_head2    
        $ d_flag_01 = False #If TRUE Genie promised to warn her.
        menu:
            m "..."
            "\"Конечно я скажу тебе, когда буду готов.\"":
                $ d_flag_01 = True #If TRUE Genie promised to warn her.
                show screen h_head2                                                             # HERMIONE
                $ h_body = "03_hp/13_hermione_main/body_33.png" # HERMIONE
                her "Спасибо, сэр."
                hide screen h_head2 
            "\"Я и сам не всегда уверен...\"":
                show screen h_head2                                                             # HERMIONE
                $ h_body = "03_hp/13_hermione_main/body_31.png" # HERMIONE
                her "Правда? Но я думалаы..."
                show screen h_head2                                                             # HERMIONE
                $ h_body = "03_hp/13_hermione_main/body_33.png" # HERMIONE
                her "Ну, тогда ладно..."
                hide screen h_head2 
        show screen h_head2                                                             # HERMIONE
        $ h_body = "03_hp/13_hermione_main/body_31.png" # HERMIONE
        her "........"
        hide screen h_head2 
        m "............."
        show screen h_head2                                                             # HERMIONE
        $ h_body = "03_hp/13_hermione_main/body_33.png" # HERMIONE
        her "............."
        show screen h_head2                                                             # HERMIONE
        $ h_body = "03_hp/13_hermione_main/body_33.png" # HERMIONE
        her "Э-э... сэр?"
        hide screen h_head2 
        m "Да, что такое?"
        show screen h_head2                                                             # HERMIONE
        $ h_body = "03_hp/13_hermione_main/body_31.png" # HERMIONE
        her "Как долго мне придется это делать?"
        hide screen h_head2 
        m "В смысле?"
        if daytime:
            show screen h_head2                                                             # HERMIONE
            $ h_body = "03_hp/13_hermione_main/body_44.png" # HERMIONE
            her2 "Просто, мои занятия вот-вот начнутся..."
        else: 
            show screen h_head2                                                             # HERMIONE
            $ h_body = "03_hp/13_hermione_main/body_44.png" # HERMIONE
            her2 "Ну, мне нужно заниматься, и хотелось бы это закончить побыстрее..."
            her2 "Завтра рано вставать, а уже довольно поздно..."
        hide screen h_head2 
        m "Вам нужны очки или нет?"
        show screen h_head2                                                             # HERMIONE
        $ h_body = "03_hp/13_hermione_main/body_74.png" # HERMIONE
        her "Да, сэр! Мне жаль..."
        her "Просто я никогда не дрочила мужчине..."
        hide screen h_head2 
        m "Ну, есть кое-что, чтобы ускорить процесс..."
        show screen h_head2                                                             # HERMIONE
        $ h_body = "03_hp/13_hermione_main/body_45.png" # HERMIONE
        her "Правда? Что это, сэр?"
        hide screen h_head2 
        menu:
            m "..."
            "\"Скажи мне насколько ты распутная шлюха!\"":
                show screen h_head2                                                             # HERMIONE
                $ h_body = "03_hp/13_hermione_main/body_47.png" # HERMIONE
                her "Что?"
                her "Но я не..."
                hide screen h_head2 
                m "Не нужно быть честной, девочка."
                m "Просто сделай это."
                show screen h_head2                                                             # HERMIONE
                $ h_body = "03_hp/13_hermione_main/body_44.png" # HERMIONE
                her "Правда?"
                hide screen h_head2 
                m "Конечно. Мы немного повеселимся."
                show screen h_head2                                                             # HERMIONE
                $ h_body = "03_hp/13_hermione_main/body_87.png" # HERMIONE
                her "Ну, раз так..."
                her "Я... я шлюха."
                hide screen h_head2 
                m "Хех... великолепно. Продолжай."
                show screen h_head2                                                             # HERMIONE
                $ h_body = "03_hp/13_hermione_main/body_87.png" # HERMIONE
                her "Я самая большая шлюха..."
                hide screen h_head2 
                m "Да, именно."
                show screen h_head2                                                             # HERMIONE
                $ h_body = "03_hp/13_hermione_main/body_79.png" # HERMIONE
                her "Я самая распутная шлюха во всей Англии!"
                her2 "Я пытаюсь казаться невинной, но на самом деле все, о чем я думаю, это члены!"
                hide screen h_head2 
                m "Да, ты малолетняя шлюха!"
                show screen h_head2                                                             # HERMIONE
                $ h_body = "03_hp/13_hermione_main/body_69.png" # HERMIONE
                her "Да! Я шлюха!"
                her "Я жажду о членах постоянно."
                hide screen h_head2 
                m "Очень хорошо!"
                m "Но,как я уже сказал, не нужно быть честной."
                show screen h_head2                                                             # HERMIONE
                $ h_body = "03_hp/13_hermione_main/body_48.png" # HERMIONE
                her "Что?"
                show screen h_head2                                                             # HERMIONE
                $ h_body = "03_hp/13_hermione_main/body_44.png" # HERMIONE
                her "сэр, все это неправда!"
                hide screen h_head2 
                g9 "Хех... Я знаю. Я просто шучу."
                show screen h_head2                                                             # HERMIONE
                $ h_body = "03_hp/13_hermione_main/body_66.png" # HERMIONE
                her "сэр!"
                hide screen h_head2 
                m "Ты все делаешь отлично. Продолжай!"
                show screen h_head2                                                             # HERMIONE
                $ h_body = "03_hp/13_hermione_main/body_87.png" # HERMIONE
                her "....."
                her "Я обожаю члены..."
                show screen h_head2                                                             # HERMIONE
                $ h_body = "03_hp/13_hermione_main/body_88.png" # HERMIONE
                her "И я люблю когда... меня шлепают..."
                her "И сперму..."
                her "Я люблю глотать сперму..."
                show screen h_head2                                                             # HERMIONE
                $ h_body = "03_hp/13_hermione_main/body_65.png" # HERMIONE
                her "Я хочу, чтобы вы меня накормили спермой, сэр!"
                hide screen h_head2 
                g4 "!!!"
                show screen h_head2                                                             # HERMIONE
                $ h_body = "03_hp/13_hermione_main/body_64.png" # HERMIONE
                her2 "Или лучше, наполните меня ею, сэр!"
                hide screen ctc
                hide screen h_head2 
                with hpunch
                g4 "{size=-4}(Я почти! Стоит мне предупредить ее?){/size}"
            
            "\"Высунь свой язык и смотри на меня!\"":
                show screen h_head2                                                             # HERMIONE
                $ h_body = "03_hp/13_hermione_main/body_45.png" # HERMIONE
                her "Что?"
                hide screen h_head2 
                m "Просто сделай это, шлюха."
                show screen h_head2                                                             # HERMIONE
                $ h_body = "03_hp/13_hermione_main/body_38.png" # HERMIONE
                her "Вот так?"
                hide screen h_head2 
                m "Да, отлично. Продолжай смотреть мне в глаза и дрочи."
                show screen h_head2                                                             # HERMIONE
                $ h_body = "03_hp/13_hermione_main/body_115.png" # HERMIONE
                her "....................."
                hide screen h_head2 
                m "Да... Отлично..."
                show screen h_head2                                                             # HERMIONE
                $ h_body = "03_hp/13_hermione_main/body_115.png" # HERMIONE
                her "..........."
                her "..........."
                show screen h_head2                                                             # HERMIONE
                $ h_body = "03_hp/13_hermione_main/body_31.png" # HERMIONE
                her2 "Я не могу так долго сидеть с открытым ртом. У меня потекут слюни..."
                hide screen h_head2 
                m "Но я хочу, чтобы они потекли..."
                show screen h_head2                                                             # HERMIONE
                $ h_body = "03_hp/13_hermione_main/body_31.png" # HERMIONE
                her "Что? Я буду выгядеть глупо!"
                hide screen h_head2 
                m "Именно это мне и нужно, девочка!"
                show screen h_head2                                                             # HERMIONE
                $ h_body = "03_hp/13_hermione_main/body_29.png" # HERMIONE
                her "......."
                hide screen h_head2 
                m "Разве ты не хочешь, чтобы я кончил как можно быстрее?"
                show screen h_head2                                                             # HERMIONE
                $ h_body = "03_hp/13_hermione_main/body_33.png" # HERMIONE
                her "............"
                show screen h_head2                                                             # HERMIONE
                $ h_body = "03_hp/13_hermione_main/body_115.png" # HERMIONE
                her "А-ха....."
                hide screen h_head2 
                m "Отлично."
                show screen h_head2                                                             # HERMIONE
                $ h_body = "03_hp/13_hermione_main/body_115.png" # HERMIONE
                her ".............."
                hide screen h_head2 
                m "Да, продолжай дрочить мой член."
                show screen h_head2                                                             # HERMIONE
                $ h_body = "03_hp/13_hermione_main/body_115.png" # HERMIONE
                her ".................."
                hide screen h_head2
                g4 "Ох... Я хочу проскользнуть своим членом в твой влажный ротик!"
                show screen h_head2                                                             # HERMIONE
                $ h_body = "03_hp/13_hermione_main/body_40.png" # HERMIONE
                her "................."
                hide screen h_head2 
                m "Нет, смотри на меня!"
                show screen h_head2                                                             # HERMIONE
                $ h_body = "03_hp/13_hermione_main/body_115.png" # HERMIONE
                her "....................."
                hide screen h_head2 
                m "Да, маленькая шлюха!"
                show screen h_head2                                                             # HERMIONE
                $ h_body = "03_hp/13_hermione_main/body_116.png" # HERMIONE
                her "......................"
                hide screen h_head2 
                m "Я хочу кончить в этот ротик, да..."
                show screen h_head2                                                             # HERMIONE
                $ h_body = "03_hp/13_hermione_main/body_116.png" # HERMIONE
                her "................"
                hide screen h_head2 
                with hpunch
                g4 "{size=-4}(Я почти! Стоит мне предупредить ее?){/size}"
            "\"Поцелуй мой член!\"":
                show screen h_head2                                                               # HERMIONE
                $ h_body = "03_hp/13_hermione_main/body_47.png" # HERMIONE
                her "Простите?"
                hide screen h_head2 
                m "Ты поняла, просто поцелуй, своими губами."
                show screen h_head2                                                             # HERMIONE
                $ h_body = "03_hp/13_hermione_main/body_47.png" # HERMIONE
                her "............."
                show screen h_head2                                                             # HERMIONE
                $ h_body = "03_hp/13_hermione_main/body_48.png" # HERMIONE
                her "...губами?"
                hide screen h_head2 
                m "Конечно... это очень ускорит приблежение конца."
                show screen h_head2                                                             # HERMIONE
                $ h_body = "03_hp/13_hermione_main/body_87.png" # HERMIONE
                her "*вздох!*.............."
                her "Ну, я бы могла попробовать, наверное..."
                hide screen h_head2 
                ">Гермиона нежно целует вашу головку."
                
                $ g_c_u_pic = "kiss_ani"
                $ renpy.play('sounds/kiss.mp3') 
                with kisсэрis
                pause
                show screen blkfade
                with d3
                $ g_c_u_pic = "handjob_ani"
                hide screen blkfade
                with d3

                show screen h_head2                                                             # HERMIONE
                $ h_body = "03_hp/13_hermione_main/body_87.png" # HERMIONE
                her "Вот так?"
                hide screen h_head2 
                m "Не так уж и плохо, правда?"
                show screen h_head2                                                             # HERMIONE
                $ h_body = "03_hp/13_hermione_main/body_44.png" # HERMIONE
                her "Нет, кажется нет..."
                hide screen h_head2 
                m "Можешь это сделать снова?"
                show screen h_head2                                                             # HERMIONE
                $ h_body = "03_hp/13_hermione_main/body_33.png" # HERMIONE
                her "Вероятно..."
                hide screen h_head2 
                m "Сделай это!"
                show screen h_head2                                                             # HERMIONE
                $ h_body = "03_hp/13_hermione_main/body_31.png" # HERMIONE
                her "Ну, ладно..."
                hide screen h_head2
                ">Гермиона еще раз целует головку вашего члена..."
                $ g_c_u_pic = "kiss_ani"
                $ renpy.play('sounds/kiss.mp3') 
                with kisсэрis
                pause
                ">В этот раз поцелуй длится чуть дольше..."
                show screen blkfade
                with d3
                $ g_c_u_pic = "handjob_ani"
                hide screen blkfade
                with d3

                hide screen h_head2 
                m "Великолепно... Теперь сделай это еще разочек, но еще дольше."
                show screen h_head2                                                             # HERMIONE
                $ h_body = "03_hp/13_hermione_main/body_31.png" # HERMIONE
                her "Вы имеете в виде, поцеловать ваш... член, сэр?"
                show screen h_head2                                                             # HERMIONE
                $ h_body = "03_hp/13_hermione_main/body_29.png" # HERMIONE
                her "Нет, я выгляжу глупо..."
                hide screen h_head2 
                m "Не глупи, девочка. Никто не смотрет."
                show screen h_head2                                                             # HERMIONE
                $ h_body = "03_hp/13_hermione_main/body_87.png" # HERMIONE
                her "Вы, сэр."
                hide screen h_head2 
                m "Но в этом весь смыслс!"
                show screen h_head2                                                             # HERMIONE
                $ h_body = "03_hp/13_hermione_main/body_79.png" # HERMIONE
                her "......"
                hide screen h_head2 
                m "Это поможем мне кончить почти сразу же!"
                show screen h_head2                                                             # HERMIONE
                $ h_body = "03_hp/13_hermione_main/body_69.png" # HERMIONE
                her "..............."
                hide screen h_head2 
                m "И после этого вы сможете просто уйти, не заботясь о наших делах на сегодня."
                show screen h_head2                                                             # HERMIONE
                $ h_body = "03_hp/13_hermione_main/body_66.png" # HERMIONE
                her "............."
                show screen h_head2                                                             # HERMIONE
                $ h_body = "03_hp/13_hermione_main/body_87.png" # HERMIONE
                her "Ну, тогда ладно...."
                hide screen h_head2
                ">Гермиона снова касается вашего члена своими губками..."
                ">Она косается головки вашего члена своими губами и остается в таком положении..."
                $ g_c_u_pic = "kiss_ani"
                $ renpy.play('sounds/kiss.mp3') 
                with kisсэрis
                pause
                hide screen h_head2 
                show screen blktone
                with d3
                m "Очень хорошо..."
                m "Теперь дотронься до него языком."
                her "??!"
                hide screen h_head2 
                m "Это последнее, что я попрошу на сегодня."
                her "............"
                ">Вы чувствуете, как кончик языка Гермионы мягко касается головки вашего члена..."
                hide screen h_head2 
                m "Да, Вот так..."
                ">Гермиона немного шевелит своим язычком...."
                hide screen h_head2 
                m "Да... Отлично..."
                show screen blkfade
                with d3
                $ g_c_u_pic = "handjob_ani"
                hide screen blkfade
                with d3
                show screen h_head2                                                             # HERMIONE
                $ h_body = "03_hp/13_hermione_main/body_87.png" # HERMIONE
                her2 "Ну, сработало? Вы готовы... кончить, профессор?"
                hide screen h_head2 
                g4 "{size=-4}(Удивительно, но да! Я сейчас кончу! Мне стоит предупредить ее?){/size}"
                hide screen blktone
        menu:
            m "..."
            "-Предупредить ее-":
                g4 "Почти кончил! Тебе лучше подготовиться!"
                show screen h_head2                                                             # HERMIONE
                $ h_body = "03_hp/13_hermione_main/body_48.png" # HERMIONE
                her "Что? Так быстро?!"
                hide screen h_head2 
                g4 "{size=+5}Да, отличная работа!!!{/size}"
                g4 "{size=+5}Маленькая шлюха!!!{/size}"
                hide screen bld1
                with d3
                show screen ctc
                pause
                hide screen ctc
                show screen blkfade 
                with d5
                show screen h_head2                                                             # HERMIONE
                $ h_body = "03_hp/13_hermione_main/body_117.png" # HERMIONE
                her "Нет, профессор, подождите, Я--"
                hide screen h_head2 
                g4 "{size=+5}Слишком поздно, шлюха!{/size}"
                show screen h_head2                                                             # HERMIONE
                $ h_body = "03_hp/13_hermione_main/body_118.png" # HERMIONE
                her2 "*хныкает*"
                hide screen h_head2       
                ">Гермиона резко засовывает ваш член себе под рубашку..."
                g4 "?!!"
                ">Ощущение трения вашего члена о ее мягую, теплую кожу переполняет вас и вы люто извергаетесь спермой."
                hide screen h_head2 
                
                show screen white 
                pause.1
                hide screen white
                pause.2
                show screen white 
                pause .1
                hide screen white
                with hpunch
                g4 "{size=+5}АРГХ! ДА!!!{/size}"
              
                
                
                
                
                
                show screen h_head2                                                             # HERMIONE
                $ h_body = "03_hp/13_hermione_main/body_48.png" # HERMIONE
                her "!!!!!!!!!!!"
                hide screen h_head2 
                
                

                $ genie_chibi_xpos = 60 #-185 behind the desk.
                $ genie_chibi_ypos = 10
                $ g_c_u_pic = "undershirt_cum_ani"
                hide screen hermione_walk_01 
                hide screen blkfade
                with d3
                stop music fadeout 1.0
                pause 
                        
                $ aftersperm = True
                $ her_head_xpos=390 #Defines position of the Hermione's full length sprite. (Default 370). 140 - center. Bottom right: 390
                $ her_head_ypos=300 #Defines position of the Hermione's full length sprite. (Default 0). Right bottom corner: 340 - head only. 235 - tits.
                show screen h_head2                                                             # HERMIONE
                $ h_body = "03_hp/13_hermione_main/body_119.png" # HERMIONE
                her2 "......................."
                hide screen h_head2                
                m "..........................."
                show screen h_head2                   
                $ h_body = "03_hp/13_hermione_main/body_119.png" # HERMIONE
                her2 "......................."
                hide screen h_head2    
                m "....................?"
                show screen h_head2                   
                $ h_body = "03_hp/13_hermione_main/body_118.png" # HERMIONE
                her2 "......................."
                hide screen h_head2    
                m "...Что за херня сейчас произошла?"
                show screen bld1
                with d3
                show screen h_head2                                                             # HERMIONE
                $ h_body = "03_hp/13_hermione_main/body_34.png" # HERMIONE
                play music "music/Chipper Doodle v2.mp3" fadein 1 fadeout 1 # HERMIONE'S THEME.
                her "Я не знаю... Я запаниковала..."
                hide screen h_head2    
                if daytime:
                    show screen h_head2                                                             # HERMIONE
                    $ h_body = "03_hp/13_hermione_main/body_34.png" # HERMIONE
                    her2 "Мои занятия вот-вот начнутся и я не хотела, чтобы вы испортили мою форму..."
                    hide screen h_head2 
                    m "И ты пойдешь на занятия вот так?"
                    m "В форме, полной изнутри спермы?"
                    show screen h_head2                                                             # HERMIONE
                    $ h_body = "03_hp/13_hermione_main/body_118.png" # HERMIONE
                    her2 "У меня есть другой выбор?"
                    her2 "Я могу просто пропустить занятия..."
                    hide screen h_head2
                else:
                    show screen h_head2                                                             # HERMIONE
                    $ h_body = "03_hp/13_hermione_main/body_34.png" # HERMIONE
                    her2 "Сейчас общая комната \"Гриффиндора\" будет полна людей..."
                    her2 "И я не хотела бы вернуться туда покрытой вашей спермой, сэр."
                    show screen h_head2                                                             # HERMIONE
                    $ h_body = "03_hp/13_hermione_main/body_117.png" # HERMIONE
                    her2 "Ох, становится поздно..."
                    hide screen h_head2 
                    m "И ты вот так пойдешь?"
                    m "В форме, полной изнутри спермы?"
                    show screen h_head2                                                             # HERMIONE
                    $ h_body = "03_hp/13_hermione_main/body_118.png" # HERMIONE
                    her "У меня есть другой выбор?"
                    hide screen h_head2     
                    
                show screen ctc
                pause
                hide screen ctc
                show screen blkfade
                with d7
                ">Гермиона отпускает ваш все еще пульсирующий член."
                
                show screen hermione_01 
                hide screen chair_02
                hide screen desk_02
                show screen genie
                hide screen g_c_u
                $ her_head_xpos=390 #Defines position of the Hermione's full length sprite. (Default 370). 140 - center. Bottom right: 390
                $ her_head_ypos=235 #Defines position of the Hermione's full length sprite. (Default 0). Right bottom corner: 340 - head only. 235 - tits.
                show screen h_head2                                                             # HERMIONE
                $ h_body = "03_hp/13_hermione_main/body_118.png" # HERMIONE
                her "Фи... Ваша сперма, сэр..."
                show screen h_head2                                                             # HERMIONE
                $ h_body = "03_hp/13_hermione_main/body_117.png" # HERMIONE
                her "Она везде на форме..."
                hide screen h_head2          
                m "Просто вставляй его в рот в следующий раз."
                show screen h_head2                                                             # HERMIONE
                $ h_body = "03_hp/13_hermione_main/body_79.png" # HERMIONE
                her "Я... так не думаю, сэр."
                her "Мне правда нужно идти. Могу я получить свои очки?"
                hide screen h_head2   
                
                
                
                
                
                
#                g4 "You whore! You little nasty wore!"
#                g4 "There! Allover your fucking belly and tits!"
#                her "Ah! It's so hot!"
#                hide screen h_head2 
#                g4 "Ох, yes, this is so good!"
#                her "Ah..."
#                hide screen h_head2 
#                m "..............."
#                her "............"
#                hide screen h_head2 
#                m "I think I'm done..."
#                her "Ох..."
#                ">Hermione releases your still pulsating cock."
#                her "Ew... Your sperm, сэр..."
#                her "It's everywhere under my uniform..."
#                hide screen h_head2 
#                m "What possessed you to put my cock there, м?"
                

            "-Просто начать кончать-":
                hide screen ctc
                with hpunch
                g4 "АРГХ!"
                show screen blkfade
                with d3
                show screen h_head2                                                             # HERMIONE
                $ h_body = "03_hp/13_hermione_main/body_48.png" # HERMIONE
                her "ЧТО?!"
                hide screen h_head2               
                g4 "Так тебе!"

                hide screen h_head2 
                
                show screen white 
                pause.1
                hide screen white
                pause.2
                show screen white 
                pause .1
                hide screen white
                with hpunch
                g4 "{size=+5}АРГХ! ДА!!!{/size}"
                
                
                
                  
                show screen h_head2                                                             # HERMIONE
                $ h_body = "03_hp/13_hermione_main/body_48.png" # HERMIONE
                her "!!!!!!!!!!!"
                hide screen h_head2 
                
                

                $ genie_chibi_xpos = 60 #-185 behind the desk.
                $ genie_chibi_ypos = 10
                $ g_c_u_pic = "on_shirt_cum_ani"
                hide screen hermione_walk_01 
                hide screen blkfade
                with d3
                show screen ctc
                hide screen bld1
                with d3
                pause
                show screen bld1
                with d3
                        
                $ aftersperm = True
                $ her_head_xpos=390 #Defines position of the Hermione's full length sprite. (Default 370). 140 - center. Bottom right: 390
                $ her_head_ypos=300 #Defines position of the Hermione's full length sprite. (Default 0). Right bottom corner: 340 - head only. 235 - tits.
                show screen h_head2                                                             # HERMIONE
                $ h_body = "03_hp/13_hermione_main/body_119.png" # HERMIONE
                her2 "......................."
                hide screen h_head2          
                m "Да... Теперь мне лучше..."
                pause
                $ g_c_u_pic = "03_hp/08_animation_02/15_cum_21.png"
                
                $ u_sperm = "03_hp/13_hermione_main/auto_06.png"
                $ uni_sperm = True
                $ h_xpos=130 #Defines position of the Hermione's full length sprite. (Default 370). (Center: 140)
                $ h_body = "03_hp/13_hermione_main/body_19.png" #Flashing Трусики
                show screen hermione_main
                with d5
                pause
                her ".........."
                m "Ну, я думаю это все..."
                show screen hermione_01 
                hide screen chair_02
                hide screen desk_02
                hide screen g_c_u
                show screen genie
                hide screen hermione_main                                                                                                                                                                                   #HERMIONE
                with fade                                                                                                                                                                                                                      #HERMIONE
                $ h_xpos=140 #Defines position of the Hermione's full length sprite. (Default 370). (Center: 140)                                                        #HERMIONE
                $ h_body = "03_hp/13_hermione_main/body_32.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
                show screen hermione_main                                                                                                                                                                                 #HERMIONE
                with d3                 
                her "Профессор! Что вы наделали?!"
                m "Что?"
                if d_flag_01: #If TRUE Genie promised to warn her.
                    play music "music/Chipper Doodle v2.mp3" fadein 1 fadeout 1 # HERMIONE'S THEME.
                    $ mad += 11
                    hide screen hermione_main                                                                                                                                                                                   #HERMIONE
                    with d3                                                                                                                                                                                                                        #HERMIONE
                    $ h_xpos=140 #Defines position of the Hermione's full length sprite. (Default 370). (Center: 140)                                                        #HERMIONE
                    $ h_body = "03_hp/13_hermione_main/body_47.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
                    show screen hermione_main                                                                                                                                                                                 #HERMIONE
                    with d3                 
                    her "Вы обещали предупредить меня, сэр!"
                    m "Ох, верно... Моя оплошность."
                    hide screen hermione_main                                                                                                                                                                                   #HERMIONE
                    with d3                                                                                                                                                                                                                        #HERMIONE
                    $ h_xpos=140 #Defines position of the Hermione's full length sprite. (Default 370). (Center: 140)                                                        #HERMIONE
                    $ h_body = "03_hp/13_hermione_main/body_69.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
                    show screen hermione_main                                                                                                                                                                                 #HERMIONE
                    her "Моя форма испорчена..."
                    her "...Я хочу получить свои очки."
                    hide screen hermione_main     
                    with d3
                    $ uni_sperm = False
                else:
                    if daytime:
                        hide screen hermione_main                                                                                                                                                                                   #HERMIONE
                        with d3                                                                                                                                                                                                                        #HERMIONE
                        $ h_xpos=140 #Defines position of the Hermione's full length sprite. (Default 370). (Center: 140)                                                        #HERMIONE
                        $ h_body = "03_hp/13_hermione_main/body_69.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
                        show screen hermione_main                                                                                                                                                                                 #HERMIONE
                        her "Моя форма испорчена!"
                        hide screen hermione_main                                                                                                                                                                                   #HERMIONE
                        with d3                                                                                                                                                                                                                        #HERMIONE
                        $ h_xpos=140 #Defines position of the Hermione's full length sprite. (Default 370). (Center: 140)                                                        #HERMIONE
                        $ h_body = "03_hp/13_hermione_main/body_87.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
                        show screen hermione_main                                                                                                                                                                                 #HERMIONE
                        her "Мои занятия вот-вот начнутся и я не могу вот так пойти на них!"
                        m "Конечно можешь, просто протри ее и все..."
                        m "Никто даже не заметит."
                        hide screen hermione_main                                                                                                                                                                                   #HERMIONE
                        with d3                                                                                                                                                                                                                        #HERMIONE
                        $ h_xpos=140 #Defines position of the Hermione's full length sprite. (Default 370). (Center: 140)                                                        #HERMIONE
                        $ h_body = "03_hp/13_hermione_main/body_79.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
                        show screen hermione_main                                                                                                                                                                                 #HERMIONE
                        her "...Я хочу получить свои очки."
                        hide screen hermione_main     
                        with d3
                        $ uni_sperm = False
                    else:
                        hide screen hermione_main                                                                                                                                                                                   #HERMIONE
                        with d3                                                                                                                                                                                                                        #HERMIONE
                        $ h_xpos=140 #Defines position of the Hermione's full length sprite. (Default 370). (Center: 140)                                                        #HERMIONE
                        $ h_body = "03_hp/13_hermione_main/body_69.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
                        show screen hermione_main                                                                                                                                                                                 #HERMIONE
                        her "Моя форма испорчена!"
                        her "И как я вернусь в комнату \"Гриффиндора\" в таком виде?!"
                        m "Почему нет? Ты выглядишь горячо, девочка!"
                        hide screen hermione_main                                                                                                                                                                                   #HERMIONE
                        with d3                                                                                                                                                                                                                        #HERMIONE
                        $ h_xpos=140 #Defines position of the Hermione's full length sprite. (Default 370). (Center: 140)                                                        #HERMIONE
                        $ h_body = "03_hp/13_hermione_main/body_79.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
                        show screen hermione_main                                                                                                                                                                                 #HERMIONE
                        her "Профессор!!!"
                        m "Ладно, хорошо. Просто вытри ее и се."
                        m "Никто и не заметит."
                        hide screen hermione_main                                                                                                                                                                                   #HERMIONE
                        with d3                                                                                                                                                                                                                        #HERMIONE
                        $ h_xpos=140 #Defines position of the Hermione's full length sprite. (Default 370). (Center: 140)                                                        #HERMIONE
                        $ h_body = "03_hp/13_hermione_main/body_79.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
                        show screen hermione_main                                                                                                                                                                                 #HERMIONE
                        her "...Я хочу получить свои очки."
                        hide screen hermione_main     
                        with d3
                        $ uni_sperm = False
        #her "Могу я получить свои очки?"

    elif request_16_points == 1: # SECOND EVENT <============================================================== EVENT 02
        m "Мисс Грейнджер?"
        hide screen hermione_main                                                                                                                                                                                   #HERMIONE
        with d3                                                                                                                                                                                                                        #HERMIONE
        $ h_xpos=140 #Defines position of the Hermione's full length sprite. (Default 370). (Center: 140)                                                        #HERMIONE
        $ h_body = "03_hp/13_hermione_main/body_01.png" #Sprite of Hermione's upper body.                    #HERMIONE
        show screen hermione_main                                                                                                                                                                                 #HERMIONE
        with d3                                                                                                                                                                                                                        #HERMIONE
        her "Да, сэр?"
        m "Что вы знаете о \"работе ручками\"?"
        hide screen hermione_main                                                                                                                                                                                   #HERMIONE
        with d3                                                                                                                                                                                                                        #HERMIONE
        $ h_xpos=140 #Defines position of the Hermione's full length sprite. (Default 370). (Center: 140)                                                        #HERMIONE
        $ h_body = "03_hp/13_hermione_main/body_66.png" #Sprite of Hermione's upper body.                    #HERMIONE
        show screen hermione_main                                                                                                                                                                                 #HERMIONE
        with d3                                                                                                                                                                                                                        #HERMIONE
        her "Вы меня уже спрашивали, сэр."
        m "Ах, верно."
        m "Ну, я хочу, чтобы вы снова поиграли с моим членом."
        hide screen hermione_main                                                                                                                                                                                   #HERMIONE
        with d3                                                                                                                                                                                                                        #HERMIONE
        $ h_xpos=140 #Defines position of the Hermione's full length sprite. (Default 370). (Center: 140)                                                        #HERMIONE
        $ h_body = "03_hp/13_hermione_main/body_120.png" #Sprite of Hermione's upper body.                                                                 #HERMIONE
        show screen hermione_main                                                                                                                                                                                 #HERMIONE
        with d3                                                                                                                                                                                                                        #HERMIONE
        her "сэр, вы опять начинаете пошлить..."
        m "Ладно, ладно."
        m "Мисс Грейнджер, как насчет некоторой услуги на сегодня."
        hide screen hermione_main                                                                                                                                                                                   #HERMIONE
        with d3                                                                                                                                                                                                                        #HERMIONE
        $ h_xpos=140 #Defines position of the Hermione's full length sprite. (Default 370). (Center: 140)                                                        #HERMIONE
        $ h_body = "03_hp/13_hermione_main/body_69.png" #Sprite of Hermione's upper body.                                                                 #HERMIONE
        show screen hermione_main                                                                                                                                                                                 #HERMIONE
        with d3                                                                                                                                                                                                                        #HERMIONE
        her "Конечно, сэр."
        g9 "Услуга в том, что вы должны поиграть с моим членом!"
        hide screen hermione_main                                                                                                                                                                                   #HERMIONE
        with d3                                                                                                                                                                                                                        #HERMIONE
        $ h_xpos=140 #Defines position of the Hermione's full length sprite. (Default 370). (Center: 140)                                                        #HERMIONE
        $ h_body = "03_hp/13_hermione_main/body_66.png" #Sprite of Hermione's upper body.                                                                 #HERMIONE
        show screen hermione_main                                                                                                                                                                                 #HERMIONE
        with d3                                                                                                                                                                                                                        #HERMIONE
        her ".............."
        m "Ох, да ладно. Ради чести \"Гриффиндора\"?"
        hide screen hermione_main                                                                                                                                                                                   #HERMIONE
        with d3                                                                                                                                                                                                                        #HERMIONE
        $ h_xpos=140 #Defines position of the Hermione's full length sprite. (Default 370). (Center: 140)                                                        #HERMIONE
        $ h_body = "03_hp/13_hermione_main/body_47.png" #Sprite of Hermione's upper body.                                                                 #HERMIONE
        show screen hermione_main                                                                                                                                                                                 #HERMIONE
        with d3                                                                                                                                                                                                                        #HERMIONE
        her "............."
        g9 "Поиграй с моим членом  ради чести \"Гриффиндора\"!"
        hide screen hermione_main                                                                                                                                                                                   #HERMIONE
        with d3                                                                                                                                                                                                                        #HERMIONE
        $ h_xpos=140 #Defines position of the Hermione's full length sprite. (Default 370). (Center: 140)                                                        #HERMIONE
        $ h_body = "03_hp/13_hermione_main/body_86.png" #Sprite of Hermione's upper body.                                                                 #HERMIONE
        show screen hermione_main                                                                                                                                                                                 #HERMIONE
        with d3                               
        her "Хватит так говорить, сэр..."
        #Genie with his cock out
        m "Ну же, девочка, я же не прошу тебя сделать это за просто так."
        hide screen hermione_main                                                                                                                                                                                   #HERMIONE
        with d3                                                                                                                                                                                                                        #HERMIONE
        $ h_xpos=140 #Defines position of the Hermione's full length sprite. (Default 370). (Center: 140)                                                        #HERMIONE
        $ h_body = "03_hp/13_hermione_main/body_69.png" #Sprite of Hermione's upper body.                                                                 #HERMIONE
        show screen hermione_main                                                                                                                                                                                 #HERMIONE
        with d3                               
        her "......."
        stop music fadeout 4.0
        

        hide screen hermione_main            
        hide screen bld1
        with d3
        $ walk_xpos=400 #Animation of walking chibi. (From)
        $ walk_xpos2=280 #Coordinates of it's movement. (To)
        $ hermione_speed = 03.0 #The speed of moving the walking animation across the screen.
        show screen hermione_walk_01 
        pause.1
        show screen blkfade
        with Dissolve(1)
        pause.3

        
                                                                                                                                                                               #HERMIONE
        hide screen genie
        $ genie_chibi_xpos = 5 #-185 behind the desk.
        $ genie_chibi_ypos = 10
        $ g_c_u_pic = "jerking_off_02_ani"
        show screen chair_02
        show screen g_c_u
        show screen desk_02
        hide screen blktone

        jump event_01_round_02


    elif request_16_points >= 2: # THIRD EVENT <========================================================================================================= EVENT 03

        $ new_request_16_03 = True #  Hearts
        
        m "Мисс Грейнджер?"
        hide screen hermione_main                                                                                                                                                                                   #HERMIONE
        with d3                                                                                                                                                                                                                        #HERMIONE
        $ h_xpos=140 #Defines position of the Hermione's full length sprite. (Default 370). (Center: 140)                                                        #HERMIONE
        $ h_body = "03_hp/13_hermione_main/body_01.png" #Sprite of Hermione's upper body.                    #HERMIONE
        show screen hermione_main                                                                                                                                                                                 #HERMIONE
        with d3                                                                                                                                                                    
        her "сэр?"
        m "Как насчет дрочки?"
        hide screen hermione_main                                                                                                                                                                                   #HERMIONE
        with d3                                                                                                                                                                                                                        #HERMIONE
        $ h_xpos=140 #Defines position of the Hermione's full length sprite. (Default 370). (Center: 140)                                                        #HERMIONE
        $ h_body = "03_hp/13_hermione_main/body_68.png" #Sprite of Hermione's upper body.                    #HERMIONE
        show screen hermione_main                                                                                                                                                                                 #HERMIONE
        with d3                                                                                                                                                                    
        her "Пока вы даете мне очки..."
        m "Ну, тогда начнем. Заработай пару очков."
        
        
        hide screen hermione_main            
        hide screen bld1
        with d3
        $ walk_xpos=400 #Animation of walking chibi. (From)
        $ walk_xpos2=280 #Coordinates of it's movement. (To)
        $ hermione_speed = 03.0 #The speed of moving the walking animation across the screen.
        show screen hermione_walk_01 
        pause.1
        show screen blkfade
        with Dissolve(1)
        pause.3

        hide screen genie
        $ genie_chibi_xpos = 5 #-185 behind the desk.
        $ genie_chibi_ypos = 10
        $ g_c_u_pic = "jerking_off_02_ani"
        show screen chair_02
        show screen g_c_u
        show screen desk_02
        hide screen blktone
        
        
        
        ">Гермиона хватает ваш член своими худенькими пальчками..."
        $ her_head_xpos=390 #Defines position of the Hermione's full length sprite. (Default 370). 140 - center. Bottom right: 390
        $ her_head_ypos=290 #Defines position of the Hermione's full length sprite. (Default 0). Right bottom corner: 340 - head only. 235 - tits.
        show screen h_head2                                                             # HERMIONE
        $ h_body = "03_hp/13_hermione_main/body_68.png" # HERMIONE
        stop music fadeout 3.0
        her "Вам нравится, когда я делаю вот так, сэр?"
        hide screen h_head2         
        g9 "Конечно, да! Очень хорошо!"
        play music "music/Chipper Doodle v2.mp3" fadein 1 fadeout 1 # HERMIONE'S THEME.
        hide screen h_head2 
        #Stroking the cock.
        $ genie_chibi_xpos = 60 #-185 behind the desk.
        $ genie_chibi_ypos = 10
        $ g_c_u_pic = "handjob_ani"
        hide screen hermione_walk_01 
        hide screen blkfade
        with d7
        show screen ctc
        pause
        hide screen ctc
        show screen bld1
        with d3

        m "Да, да, вот так..."
        m "Хм... Ты, однако,Ты наловчилась."
        show screen h_head2                                                             # HERMIONE
        $ h_body = "03_hp/13_hermione_main/body_74.png" # HERMIONE
        her "Спасибо, сэр."
        her2 "Я поняла, что лучше я буду делать это качественнее и быстрее."
        hide screen h_head2      
        m "Хм..."
        menu:
            m "..."
            "\"Что ты думаешь о моем члене?\"":
                show screen h_head2                                                             # HERMIONE
                $ h_body = "03_hp/13_hermione_main/body_31.png" # HERMIONE
                her "А?"
                her2 "Ох, он неплохой..."
                show screen h_head2                                                             # HERMIONE
                $ h_body = "03_hp/13_hermione_main/body_34.png" # HERMIONE
                her2 "Мне нужно похвалить ваш член! Совсем забыла об этом!"
                hide screen h_head2         
                m "Ну, ты не должна--"
                show screen h_head2                                                             # HERMIONE
                $ h_body = "03_hp/13_hermione_main/body_120.png" # HERMIONE
                her "сэр, позвольте мне быть честной с вами..."
                hide screen h_head2         
                m "Да?"
                show screen h_head2                                                             # HERMIONE
                $ h_body = "03_hp/13_hermione_main/body_111.png" # HERMIONE
                her "У вас самый большой пенис, который я только видела!"
                hide screen h_head2         
                m "Ну, я полагаю--"
                show screen h_head2                                                             # HERMIONE
                $ h_body = "03_hp/13_hermione_main/body_30.png" # HERMIONE
                her "Еще не все!"
                hide screen h_head2         
                m "Извиняюсь."
                show screen h_head2                                                             # HERMIONE
                $ h_body = "03_hp/13_hermione_main/body_118.png" # HERMIONE
                her "Ваш член настоько большой, что пугает меня!"
                hide screen h_head2      
                g9 "Ах ты маленькая потаскуха. Ты знаешь, что нужно говорить..."
                show screen h_head2                                                             # HERMIONE
                $ h_body = "03_hp/13_hermione_main/body_121.png" # HERMIONE
                her "И конечно же я жажду его..."
                her2 "Любая женщина была бы рада, чтобы ощутить его в себе!"
                hide screen h_head2         
                m "...а ты хороша!"
                show screen h_head2                                                             # HERMIONE
                $ h_body = "03_hp/13_hermione_main/body_30.png" # HERMIONE
                her "Есть еще!"
                hide screen h_head2         
                m "Несмотря ни на что..."
                show screen h_head2                                                             # HERMIONE
                $ h_body = "03_hp/13_hermione_main/body_30.png" # HERMIONE
                her2 "Я думаю, что ваш член это благословение для всего мира!"
                hide screen h_head2         
                m "Ну, не стал бы так преувеличивать--"
                show screen h_head2                                                             # HERMIONE
                $ h_body = "03_hp/13_hermione_main/body_30.png" # HERMIONE
                her2 "Послушайте меня, сэр!"
                her2 "Я считаю, что стоит установить статуи в каждом городе на земле, посвященные вашему члену!"
                her2 "Так, чтобы люди всео мира могли поклоняться вашему члену!"
                hide screen h_head2         
                m "Ладно, Я услугыла достаточно."
                show screen h_head2                                                             # HERMIONE
                $ h_body = "03_hp/13_hermione_main/body_122.png" # HERMIONE
                her "Слишком?"
                hide screen h_head2         
                m "Ага, немного."
                show screen h_head2                                                             # HERMIONE
                $ h_body = "03_hp/13_hermione_main/body_34.png" # HERMIONE
                her "Простите..."
                hide screen h_head2         
                m "Ничего. Продолжай дрочить."
                show screen h_head2                                                             # HERMIONE
                $ h_body = "03_hp/13_hermione_main/body_121.png" # HERMIONE
                her2 "................."
                hide screen h_head2  
                show screen blktone
                with d3
                ">Гермиона продолжает дрочить ваш член."
                ">у нее это отлично получается."  
                hide screen blktone
                with d3
                m "Да, да... Вот так."
                
            "\"Назови себя шлюхой!\"":
                show screen h_head2                                                             # HERMIONE
                $ h_body = "03_hp/13_hermione_main/body_31.png" # HERMIONE
                her "Простите?"
                show screen h_head2                                                             # HERMIONE
                $ h_body = "03_hp/13_hermione_main/body_17.png" # HERMIONE
                her2 "Ох, точно! Я должна унижать себя, да?"
                hide screen h_head2  
                m "Ну, не обязательно, но..."
                show screen h_head2                                                             # HERMIONE
                $ h_body = "03_hp/13_hermione_main/body_120.png" # HERMIONE
                her2 "Это отлично, я не возражаю."
                show screen h_head2                                                             # HERMIONE
                $ h_body = "03_hp/13_hermione_main/body_45.png" # HERMIONE
                her "И так. Я шлюха!"
                hide screen h_head2  
                m "Отлично. Рад, что мы выяснили это."
                m "Теперь, я хочу, чтобы ты сказала..."
                menu:
                    m "..."
                    "\"Я дешевая шлюха!\"":
                        show screen h_head2                                                             # HERMIONE
                        $ h_body = "03_hp/13_hermione_main/body_122.png" # HERMIONE
                        her "Конечно."
                        show screen h_head2                                                             # HERMIONE
                        $ h_body = "03_hp/13_hermione_main/body_121.png" # HERMIONE
                        her "Я дешевая шлюха."
                        her "Грязная маленькая шлюшка, вот кто я."
                        hide screen h_head2  
                        m "Да! Отлично!"
                    "\"Я живу, чтобы сосать член!\"":
                        show screen h_head2                                                             # HERMIONE
                        $ h_body = "03_hp/13_hermione_main/body_122.png" # HERMIONE
                        her "Эмм..."
                        show screen h_head2                                                             # HERMIONE
                        $ h_body = "03_hp/13_hermione_main/body_45.png" # HERMIONE
                        her2 "Я живу, чтобы сосать пенис... То есть член..."
                        hide screen h_head2  
                        m "Правда? Почему тогда ты сейчас его не отсасываешь?"
                        show screen h_head2                                                             # HERMIONE
                        $ h_body = "03_hp/13_hermione_main/body_111.png" # HERMIONE
                        her2 "Сэр, Я просто отвечаю вам..."
                        hide screen h_head2  
                        m "Да ну? Может ты меня обманываешь...."
                        show screen h_head2                                                             # HERMIONE
                        $ h_body = "03_hp/13_hermione_main/body_122.png" # HERMIONE
                        her2 "...................."
                        hide screen h_head2
                        m ".................."
                    "\"Я люблю глотать сперму!\"":
                        show screen h_head2                                                             # HERMIONE
                        $ h_body = "03_hp/13_hermione_main/body_122.png" # HERMIONE
                        her "Я люблю... Эм... глотать сперму."
                        hide screen h_head2  
                        m "Вы некоторое время колеблетесь."
                        show screen h_head2                                                             # HERMIONE
                        $ h_body = "03_hp/13_hermione_main/body_122.png" # HERMIONE
                        her "Да, я знаю...."
                        her "Дайте мне начать снова..."
                        show screen h_head2                                                             # HERMIONE
                        $ h_body = "03_hp/13_hermione_main/body_121.png" # HERMIONE
                        her "Я люблю глотать сперму!"
                        her "Глотать сперму - это самое лучшее!"
                        her "Я люблю это!"
                        show screen h_head2                                                             # HERMIONE
                        $ h_body = "03_hp/13_hermione_main/body_123.png" # HERMIONE
                        her2 "..................................."
                        show screen h_head2                                                             # HERMIONE
                        $ h_body = "03_hp/13_hermione_main/body_122.png" # HERMIONE
                        her "Как вам это, сэр?"
                        hide screen h_head2  
                        m "Идеально." 
            "\"Это действительно неплохо. Ты практиковалась?\"":
                show screen h_head2                                                             # HERMIONE
                $ h_body = "03_hp/13_hermione_main/body_74.png" # HERMIONE
                her "Хм?"
                her "Вроде... На самом деле нет..."
                show screen h_head2                                                             # HERMIONE
                $ h_body = "03_hp/13_hermione_main/body_122.png" # HERMIONE
                her "Я говорила с девочками, и..."
                hide screen h_head2    
                m "Про мастурбацию?"
                show screen h_head2                                                             # HERMIONE
                $ h_body = "03_hp/13_hermione_main/body_80.png" # HERMIONE
                her "Помимо других вещей..."
                hide screen h_head2    
                m "Так эти твои подружки, они много об этом знают?"
                show screen h_head2                                                             # HERMIONE
                $ h_body = "03_hp/13_hermione_main/body_48.png" # HERMIONE
                her "На самом деле да. Я была удивлена."
                show screen h_head2                                                             # HERMIONE
                $ h_body = "03_hp/13_hermione_main/body_68.png" # HERMIONE
                her2 "Все странные и изощренные виды секса судя по всему случались в нашей школе..."
                her "Не скажу, что я это одобряю..."
                show screen h_head2                                                             # HERMIONE
                $ h_body = "03_hp/13_hermione_main/body_74.png" # HERMIONE
                her "Но они научили меня некоторым... приемам."
                hide screen h_head2    
                m "Хм? И каким например?"
                show screen h_head2                                                             # HERMIONE
                $ h_body = "03_hp/13_hermione_main/body_124.png" # HERMIONE
                her "Давайте посмотрим..."
                her "Если я положу одну руку сюда..."
                her "А другую сюда..."
                hide screen h_head2    
                m "О, я вижу... Да, это довольно приятно."
                show screen h_head2                                                             # HERMIONE
                $ h_body = "03_hp/13_hermione_main/body_122.png" # HERMIONE
                her "Да?"
                show screen h_head2                                                             # HERMIONE
                $ h_body = "03_hp/13_hermione_main/body_68.png" # HERMIONE
                her "Джинни была права насчет этого..."
                hide screen h_head2
                g4 "Что ты сказала?"
                show screen h_head2                                                             # HERMIONE
                $ h_body = "03_hp/13_hermione_main/body_74.png" # HERMIONE
                her "Джинни Уизли, она научила меня этому."
                hide screen h_head2    
                m "О, ясно..."
                show screen h_head2                                                             # HERMIONE
                $ h_body = "03_hp/13_hermione_main/body_124.png" # HERMIONE
                her2 "Она сказала что любой парень влюбится в меня, если я ему так сделаю..."
                her2 "Еще одна вещь, когда я делаю колечко из моих пальцев..."
                her2 "И потом вставляю палец сюда..."
                hide screen h_head2    
                m "Хм... Я ничего не чувствую..."
                show screen h_head2                                                             # HERMIONE
                $ h_body = "03_hp/13_hermione_main/body_118.png" # HERMIONE
                her "Правда?"
                her "Хм..."
                show screen h_head2                                                             # HERMIONE
                $ h_body = "03_hp/13_hermione_main/body_124.png" # HERMIONE
                her "О! Точно!"
                her "Палец нужно вставит сюда! Какая же я глупая!"
                hide screen h_head2    
                with hpunch
                with kisсэрis
                g4 "О!!! Во имя великих песков пустыни, да!"
                show screen h_head2                                                             # HERMIONE
                $ h_body = "03_hp/13_hermione_main/body_80.png" # HERMIONE
                her "Да? Вам хорошо?"
                show screen h_head2                                                             # HERMIONE
                $ h_body = "03_hp/13_hermione_main/body_124.png" # HERMIONE
                her2 "Что, если я продолжу, но вставлю палец сюда и немного нажму..."
                hide screen h_head2    
                g4 "Девочка, ты меня убиваешь!"
                show screen h_head2                                                             # HERMIONE
                $ h_body = "03_hp/13_hermione_main/body_80.png" # HERMIONE
                her "Правда? Правда?!"
                her "Это действительно довольно весело!"
                show screen h_head2                                                             # HERMIONE
                $ h_body = "03_hp/13_hermione_main/body_122.png" # HERMIONE
                her "Эмм... Я имею в виду..."
                her "Я конечно же делаю это только для моего факультета..."
                hide screen h_head2    
                m "Да, да...  \"Гриффиндор\" гордится этим."
                m "Просто продолжай гладить это место..."
                m "О, да..."
                show screen h_head2                                                             # HERMIONE
                $ h_body = "03_hp/13_hermione_main/body_124.png" # HERMIONE
                her "..............."
                hide screen h_head2
        m "Да... ."
        show screen h_head2                                                             # HERMIONE
        $ h_body = "03_hp/13_hermione_main/body_122.png" # HERMIONE
        her ".............."
        hide screen h_head2
        m "Теперь я хочу чтобы ты кое-что сказала..."
        menu:
            m "..."
            "{size=-4}\"Я мечтаю, чтоб меня изнасиловал отец.\"{/size}":
                $ mad += 11
                show screen h_head2                                                             # HERMIONE
                $ h_body = "03_hp/13_hermione_main/body_77.png" # HERMIONE
                her "Я не мечтаю об этом!"
                hide screen h_head2
                m "Я знаю. Просто скажи это."
                show screen h_head2                                                             # HERMIONE
                $ h_body = "03_hp/13_hermione_main/body_76.png" # HERMIONE
                her "Мой отец? Это отвратительно, сэр!"
                hide screen h_head2
                m "Сделай, что я сказал."
                show screen h_head2                                                             # HERMIONE
                $ h_body = "03_hp/13_hermione_main/body_79.png" # HERMIONE
                her "..........."
                show screen h_head2                                                             # HERMIONE
                $ h_body = "03_hp/13_hermione_main/body_87.png" # HERMIONE
                her "Что же..."
                her "Иногда я мечтаю быть изнасилованной..."
                her "......."
                hide screen h_head2
                m "Я вижу. И в твоих фантазиях..."
                m "Кто тебя насилует?"
                show screen h_head2                                                             # HERMIONE
                $ h_body = "03_hp/13_hermione_main/body_117.png" # HERMIONE
                her "Мой отец...?"
                hide screen h_head2
                m "Тебе это нравится?"
                show screen h_head2                                                             # HERMIONE
                $ h_body = "03_hp/13_hermione_main/body_118.png" # HERMIONE
                her "Нет! Я плачу и умоляю его остановиться!"
                hide screen h_head2
                m "Хех... Неплохо."
                show screen h_head2                                                             # HERMIONE
                $ h_body = "03_hp/13_hermione_main/body_118.png" # HERMIONE
                her "......."
                hide screen h_head2
                m "Разве это было сложно?--"
                show screen h_head2                                                             # HERMIONE
                $ h_body = "03_hp/13_hermione_main/body_67.png" # HERMIONE
                her "Я зову мамочку, но она до сих пор на работе..."
                hide screen h_head2
                m "Хм?"
                show screen h_head2                                                             # HERMIONE
                $ h_body = "03_hp/13_hermione_main/body_33.png" # HERMIONE
                her "Мой папа несет меня в мою комнату..."
                her "И кидает меня на кровать!"
                show screen h_head2                                                             # HERMIONE
                $ h_body = "03_hp/13_hermione_main/body_32.png" # HERMIONE
                her "Я плачу \"Нет, папочка, я еще девственница!\""
                show screen h_head2                                                             # HERMIONE
                $ h_body = "03_hp/13_hermione_main/body_123.png" # HERMIONE
                $ g_c_u_pic= "03_hp/08_animation_02/12_handjob_01.png"
                her "Но он не слушает! Он просто срывает мои трусики!"
                show screen h_head2                                                             # HERMIONE
                $ h_body = "03_hp/13_hermione_main/body_22.png" # HERMIONE
                her "Я умоляю его остановиться! Я все кричу и кричу!"
                hide screen h_head2
                m "Мм, девочка?"
                show screen h_head2                                                             # HERMIONE
                $ h_body = "03_hp/13_hermione_main/body_21.png" # HERMIONE
                her "Да?"
                hide screen h_head2
                m "Ты больше не дрочишь мой член..."
                show screen h_head2                                                             # HERMIONE
                $ h_body = "03_hp/13_hermione_main/body_24.png" # HERMIONE
                her "О, я прошу прощения, сэр."
                her "Я просто задумалась..."
                $ g_c_u_pic = "handjob_ani"
                show screen h_head2                                                             # HERMIONE
                $ h_body = "03_hp/13_hermione_main/body_31.png" # HERMIONE
                her "Но все что я сказала, это конечно же неправда!"
                her "Я никогда о таком не фантазирую!"
                hide screen h_head2
                m "Хорошо."
            "{size=-4}\"Иногда мне становится одиноко и я даю моему псу трахнуть меня.\"{/size}":
                show screen h_head2                                                             # HERMIONE
                $ h_body = "03_hp/13_hermione_main/body_18.png" # HERMIONE
                her "Что?!"
                show screen h_head2                                                             # HERMIONE
                $ h_body = "03_hp/13_hermione_main/body_17.png" # HERMIONE
                her "Это отвратительно."
                show screen h_head2                                                             # HERMIONE
                $ h_body = "03_hp/13_hermione_main/body_16.png" # HERMIONE
                her "Собаки разносчики {size=+5}болезней{/size}, сэр."
                hide screen h_head2
                m "На самом деле человеческие и собачьи {size=+5}болезни{/size} сильно отличаются..."
                m "Что означает, что они не смогут тебя заразить."
                show screen h_head2                                                             # HERMIONE
                $ h_body = "03_hp/13_hermione_main/body_08.png" # HERMIONE
                her "............"
                hide screen h_head2
                m "Я слышал, кстати, что многие женщины любят быть \"связанными\" ."
                show screen h_head2                                                             # HERMIONE
                $ h_body = "03_hp/13_hermione_main/body_07.png" # HERMIONE
                her "В каком смысле \"связанными\"?"
                hide screen h_head2
                m "Эм... Ну..."
                m "Не имеет значения."
                m "Просто скажи это!"
                show screen h_head2                                                             # HERMIONE
                $ h_body = "03_hp/13_hermione_main/body_03.png" # HERMIONE
                her "Хорошо!"
                show screen h_head2                                                             # HERMIONE
                $ h_body = "03_hp/13_hermione_main/body_08.png" # HERMIONE
                her "Иногда мне становится одиноко и я даю моему псу трахнуть меня."
                hide screen h_head2
                m "Звучит не очень..."
                show screen h_head2                                                             # HERMIONE
                $ h_body = "03_hp/13_hermione_main/body_07.png" # HERMIONE
                her "Потому что у нас даже собаки нет!"
                hide screen h_head2
                m "Да все равно, просто продолжай..."
            "{size=-4}\"-Manual user input-\"{/size}":

                # The phrase in the brackets is the text that the game will display to prompt 
                # the player to enter the name they've chosen.

                $ jasname = renpy.input("(Используйте клавиатуру, чтобы ввести предложение.)")

                $ jasname = jasname.strip()
                # The .strip() instruction removes any extra spaces the player may have typed by accident.

                #  If the player can't be bothered to choose a name, then we
                #  choose a suitable one for them:
                if jasname == "":
                    $ jasname="Я шлюха."
                    show screen h_head2                                                             # HERMIONE
                    $ h_body = "03_hp/13_hermione_main/body_29.png" # HERMIONE
                    her2 "Хм...?"
                    her2 "Должна ли я сказать что \"Я шлюха\" как обычно?"
                    hide screen h_head2
                if one_out_of_three == 1:
                    show screen h_head2                                                             # HERMIONE
                    $ h_body = "03_hp/13_hermione_main/body_29.png" # HERMIONE
                    her "Я не хочу этог говорить..."
                    hide screen h_head2
                    m "О, просто сделай это, девочка."
                    show screen h_head2                                                             # HERMIONE
                    $ h_body = "03_hp/13_hermione_main/body_29.png" # HERMIONE
                    her "..........."
                    show screen h_head2                                                             # HERMIONE
                    $ h_body = "03_hp/13_hermione_main/body_30.png" # HERMIONE
                    her2 "[jasname]"
                    hide screen h_head2
                    g9 "Хе-хе..."
                    hide screen h_head2
                elif one_out_of_three == 2:
                    show screen h_head2                                                             # HERMIONE
                    $ h_body = "03_hp/13_hermione_main/body_29.png" # HERMIONE
                    her "А?"
                    her2 "Что это значит?"
                    hide screen h_head2
                    m "Просто скажи это."
                    show screen h_head2                                                             # HERMIONE
                    $ h_body = "03_hp/13_hermione_main/body_29.png" # HERMIONE
                    her "......"
                    hide screen h_head2
                    m "Давай, развлеки меня."
                    show screen h_head2                                                             # HERMIONE
                    $ h_body = "03_hp/13_hermione_main/body_30.png" # HERMIONE
                    her2 "[jasname]"
                    hide screen h_head2
                    g9 "Хе-хе..."
                    hide screen h_head2
                elif one_out_of_three == 3:
                    show screen h_head2                                                             # HERMIONE
                    $ h_body = "03_hp/13_hermione_main/body_29.png" # HERMIONE
                    her "..........."
                    her2 "Я должна сделать это?"
                    hide screen h_head2
                    m "Просто скажиt."
                    show screen h_head2                                                             # HERMIONE
                    $ h_body = "03_hp/13_hermione_main/body_30.png" # HERMIONE
                    her2 "[jasname]"
                    hide screen h_head2
                    g9 "Хе-хе..."
        
        #CUMMING
        m "Хм..."
        m "Мне нравится, то что ты делаешь ладонью!"
        show screen h_head2                                                             # HERMIONE
        $ h_body = "03_hp/13_hermione_main/body_122.png" # HERMIONE
        her2 "Вы заметили...?"
        her2 "Мне продолжить?"
        hide screen h_head2 
        show screen blkfade
        with d3
        ">Гермиона прижимает ладонью ваш член и начинает очень нежно тереть его..."
        m "О да!!!"
        stop music fadeout 1.0
        g4 "{size=-5}(Я думаю что я готов! Нужно ли мне предупредить ее?){/size}"
        menu:
            m "..."
            "\"(Да, лучше сказать ей об этом).\"":
                g4 "Я думаю я близок к--"
                if whoring >= 18: # LEVEL 07
                    jump kiss_suck
                else:
                    pass
                ">Гермиона быстро поднимает свою блузку..."
                ">Она направляет ваш член себе на живот и быстро спускает ее..."
                ">Ощущение ее кожи на вашем разгоряченном члене вызывает у вас легкое головокружение..."
                ">Гермиона направляет ваш член чуть выше, чем вы ожидали..."
                ">Вы чувствуете ее невероятно мягкую грудь, трущуюся о ваш член..."
               
                
                
                show screen white 
                pause.1
                hide screen white
                pause.2
                show screen white 
                pause .1
                hide screen white
                with hpunch
                g4 "{size=+5}АГРХ! ДА!!!{/size}"
              
                
                play music "music/Chipper Doodle v2.mp3" fadein 1 fadeout 1 # HERMIONE'S THEME.
                
                
                
                show screen h_head2                                                             # HERMIONE
                $ h_body = "03_hp/13_hermione_main/body_48.png" # HERMIONE
                her "!!!!!!!!!!!"
                hide screen h_head2 
                
                

                $ genie_chibi_xpos = 60 #-185 behind the desk.
                $ genie_chibi_ypos = 10
                $ g_c_u_pic = "undershirt_cum_ani"
                hide screen hermione_walk_01 
                hide screen blkfade
                with d3
                show screen ctc
                pause 
                        
                $ aftersperm = True
                $ her_head_xpos=390 #Defines position of the Hermione's full length sprite. (Default 370). 140 - center. Bottom right: 390
                $ her_head_ypos=300 #Defines position of the Hermione's full length sprite. (Default 0). Right bottom corner: 340 - head only. 235 - tits.
                

                
                
                g4 "Агрх! Ты шлюха!"
                show screen h_head2                                                             # HERMIONE
                $ h_body = "03_hp/13_hermione_main/body_124.png" # HERMIONE
                her2 "Да, сэр! Просто выпустите ее!"
                hide screen h_head2       
                g4 "Да! Ебаная шлюха!"
                #Cuming.
                show screen h_head2                                                             # HERMIONE
                $ h_body = "03_hp/13_hermione_main/body_64.png" # HERMIONE
                her2 "Ах!! Она такая горячая!"
                show screen h_head2                                                             # HERMIONE
                $ h_body = "03_hp/13_hermione_main/body_121.png" # HERMIONE
                her2 "И она просто везде! Ее так много!"
                her2 "...профессор."
                hide screen h_head2       
                g4 "Агрх!!!"
                m "............"
                m "Я думаю я закончил..."
                show screen h_head2                                                             # HERMIONE
                $ h_body = "03_hp/13_hermione_main/body_122.png" # HERMIONE
                her2 "Ах, хорошо..."
                show screen h_head2                                                             # HERMIONE
                $ h_body = "03_hp/13_hermione_main/body_124.png" # HERMIONE
                her2 ".............."
                show screen h_head2                                                             # HERMIONE
                $ h_body = "03_hp/13_hermione_main/body_121.png" # HERMIONE
                her2 "Вы так много накончали на меня сегодня, сэр..."
                hide screen h_head2    
                show screen ctc
                pause
                hide screen ctc
                show screen blkfade
                with d5
                ">Гермиона отпускает ваш все еще пульсирующий член."
                
                show screen hermione_01 
                hide screen chair_02
                hide screen desk_02
                show screen genie
                hide screen g_c_u
                $ her_head_xpos=390 #Defines position of the Hermione's full length sprite. (Default 370). 140 - center. Bottom right: 390
                $ her_head_ypos=235 #Defines position of the Hermione's full length sprite. (Default 0). Right bottom corner: 340 - head only. 235 - tits.
                hide screen blkfade
                with d5
                
               
                
                
                
                
                if daytime:
                    show screen h_head2                                                             # HERMIONE
                    $ h_body = "03_hp/13_hermione_main/body_45.png" # HERMIONE
                    her2 "Наверное мне лучше уйти... мои уроки скоро должны начаться."
                else:
                    show screen h_head2                                                             # HERMIONE
                    $ h_body = "03_hp/13_hermione_main/body_45.png" # HERMIONE
                    her2 "Наверное мне лучше уйти...  Уже довольно поздно."
                hide screen h_head2       
                m "Тебе нормально в такой одежде?"
                show screen h_head2                                                             # HERMIONE
                $ h_body = "03_hp/13_hermione_main/body_87.png" # HERMIONE
                her "Что?"
                show screen h_head2                                                             # HERMIONE
                $ h_body = "03_hp/13_hermione_main/body_68.png" # HERMIONE
                her "О. Да, со мной будет все в порядке..."
                show screen h_head2                                                             # HERMIONE
                $ h_body = "03_hp/13_hermione_main/body_74.png" # HERMIONE
                her2 "Она может немного впитаться здесь и немного здесь, но я надеюсь что никто не заметит."
                hide screen h_head2    
                m "Хм... Тебе стоит заглотить мой член в следующий раз..."
                show screen h_head2                                                             # HERMIONE
                $ h_body = "03_hp/13_hermione_main/body_122.png" # HERMIONE
                her "И проглотить вашу горячую сперму сэр?"
                hide screen h_head2    
                m "По крайней мере твоя одежда будет чистая."
                show screen h_head2                                                             # HERMIONE
                $ h_body = "03_hp/13_hermione_main/body_120.png" # HERMIONE
                her "Со всем уважением, сэр..."
                show screen h_head2                                                             # HERMIONE
                $ h_body = "03_hp/13_hermione_main/body_122.png" # HERMIONE
                her2 "45 очков за это будет мало..."
                her2 "Кстати об этом. Могу ли я получить оплату?"
                hide screen h_head2    
                

            "\"(А, не нужно!).\"":
                g4 "Вот! Получай, шлюха!"
                if whoring >= 18: # LEVEL 07
                    jump kiss_suck
                else:
                    pass
                with hpunch
                g4 "АГРХ!"
                show screen blkfade
                with d3
                show screen h_head2                                                             # HERMIONE
                $ h_body = "03_hp/13_hermione_main/body_48.png" # HERMIONE
                her "ЧТО?!"
                hide screen h_head2               
                g4 "Получай!"

                hide screen h_head2 
                
                show screen white 
                pause.1
                hide screen white
                pause.2
                show screen white 
                pause .1
                hide screen white
                with hpunch
                g4 "{size=+5}АГРРРХ! ДА!!!{/size}"
                
                
                
                  
                show screen h_head2                                                             # HERMIONE
                $ h_body = "03_hp/13_hermione_main/body_48.png" # HERMIONE
                her "!!!!!!!!!!!"
                hide screen h_head2 
                
                

                $ genie_chibi_xpos = 60 #-185 behind the desk.
                $ genie_chibi_ypos = 10
                $ g_c_u_pic = "on_shirt_cum_ani"
                hide screen hermione_walk_01 
                hide screen blkfade
                with d3
                show screen ctc
                hide screen bld1
                with d3
                pause
                show screen bld1
                with d3
                        
                $ aftersperm = True
                $ her_head_xpos=390 #Defines position of the Hermione's full length sprite. (Default 370). 140 - center. Bottom right: 390
                $ her_head_ypos=300 #Defines position of the Hermione's full length sprite. (Default 0). Right bottom corner: 340 - head only. 235 - tits.
                show screen h_head2                                                             # HERMIONE
                $ h_body = "03_hp/13_hermione_main/body_119.png" # HERMIONE
                her2 "......................."
                hide screen h_head2          
                m "Да... Я чувствую себя намного лучше..."
                pause
                $ g_c_u_pic = "03_hp/08_animation_02/15_cum_21.png"
                
                $ u_sperm = "03_hp/13_hermione_main/auto_06.png"
                $ uni_sperm = True
                $ h_xpos=130 #Defines position of the Hermione's full length sprite. (Default 370). (Center: 140)
                $ h_body = "03_hp/13_hermione_main/body_19.png" #Flashing Трусики
                show screen hermione_main
                with d5
                pause
                her ".........."
                m "Well, I think that's about it..."
                show screen hermione_01 
                hide screen chair_02
                hide screen desk_02
                hide screen g_c_u
                show screen genie
                hide screen hermione_main                                                                                                                                                                                   #HERMIONE
                with fade                                                                                                                                                                                                                      #HERMIONE
                $ h_xpos=140 #Defines position of the Hermione's full length sprite. (Default 370). (Center: 140)                                                        #HERMIONE
                $ h_body = "03_hp/13_hermione_main/body_32.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
                show screen hermione_main                                                                                                                                                                                 #HERMIONE
                with d3                                                                                                                                                                                                                        #HERMIONE          
                her "Профессор! Что вы сделали?"
                play music "music/Chipper Doodle v2.mp3" fadein 1 fadeout 1 # HERMIONE'S THEME.
                m "Что?"
                hide screen hermione_main                                                                                                                                                                                   #HERMIONE
                with d3                                                                                                                                                                                                                  #HERMIONE
                $ h_xpos=140 #Defines position of the Hermione's full length sprite. (Default 370). (Center: 140)                                                        #HERMIONE
                $ h_body = "03_hp/13_hermione_main/body_32.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
                show screen hermione_main                                                                                                                                                                                 #HERMIONE
                with d3                                                                                                                                                                                                                        #HERMIONE      
                her "Вы всю меня обкончали, сэр..."
                hide screen hermione_main                                                                                                                                                                                   #HERMIONE
                with d3                                                                                                                                                                                                                     #HERMIONE
                $ h_xpos=140 #Defines position of the Hermione's full length sprite. (Default 370). (Center: 140)                                                        #HERMIONE
                $ h_body = "03_hp/13_hermione_main/body_118.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
                show screen hermione_main                                                                                                                                                                                 #HERMIONE
                with d3                                                                                                                                                                                                                        #HERMIONE      
                her "Что за ужас..."
                hide screen hermione_main                                                                                                                                                                                   #HERMIONE
                with d3                                                                                                                                                                                                         #HERMIONE
                $ h_xpos=140 #Defines position of the Hermione's full length sprite. (Default 370). (Center: 140)                                                        #HERMIONE
                $ h_body = "03_hp/13_hermione_main/body_120.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
                show screen hermione_main                                                                                                                                                                                 #HERMIONE
                with d3                                                                                                                                                                                                                        #HERMIONE      
                her2 "Профессор, вы должны были предупредить меня."
                m "Это все твоя вина!"
                hide screen hermione_main                                                                                                                                                                                   #HERMIONE
                with d3                                                                                                                                                                                                                     #HERMIONE
                $ h_xpos=140 #Defines position of the Hermione's full length sprite. (Default 370). (Center: 140)                                                        #HERMIONE
                $ h_body = "03_hp/13_hermione_main/body_117.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
                show screen hermione_main                                                                                                                                                                                 #HERMIONE
                with d3                                                                                                                                                                                                                        #HERMIONE      
                her2 "Моя вина?"
                m "Да! Ты делала мне так хорошо..."
                m "Что я позабыл вообще обо всем..."     
                hide screen hermione_main                                                                                                                                                                                   #HERMIONE
                with d3                                                                                                                                                                                                                #HERMIONE
                $ h_xpos=140 #Defines position of the Hermione's full length sprite. (Default 370). (Center: 140)                                                        #HERMIONE
                $ h_body = "03_hp/13_hermione_main/body_122.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
                show screen hermione_main                                                                                                                                                                                 #HERMIONE
                with d3                                                                                                                                                                                                                        #HERMIONE     
                her2 "О..."
                her2 "Ну что сделано, то сделано..."
                hide screen hermione_main                                                                                                                                                                                   #HERMIONE
                with d3                                                                                                                                                                                                            #HERMIONE
                $ h_xpos=140 #Defines position of the Hermione's full length sprite. (Default 370). (Center: 140)                                                        #HERMIONE
                $ h_body = "03_hp/13_hermione_main/body_123.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
                show screen hermione_main                                                                                                                                                                                 #HERMIONE
                with d3                                                                                                                                                                                                                        #HERMIONE      
                her "Я просто вытрусь и буду надеяться, что никто ничего не заметит..."
                hide screen hermione_main                                                                                                                                                                                   #HERMIONE
                with d3                                                                                                                                                                                                                   #HERMIONE
                $ h_xpos=140 #Defines position of the Hermione's full length sprite. (Default 370). (Center: 140)                                                        #HERMIONE
                $ h_body = "03_hp/13_hermione_main/body_122.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
                show screen hermione_main                                                                                                                                                                                 #HERMIONE
                with d3                                                                                                                                                                                                                        #HERMIONE      
                her2 "Могу я получить свою оплату?"
                hide screen hermione_main                                                                                                                                                                                   #HERMIONE
                with fade   
    
    label done_with_handjob:
                
    $ uni_sperm = False #Sperm layer is not displayed in hermione screen.
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
    
    m "Yes, Да, мисс Грейнджер. [current_payout]  \"Гриффиндору\"." 
    $ gryffindor +=current_payout
    $ h_xpos=140 #Defines position of the Hermione's full length sprite. (Default 370). (Center: 140)
    $ h_body = "03_hp/13_hermione_main/body_13.png" #Flashing Трусики
    show screen hermione_main
    hide screen hermione_01_f #Hermione stands still.
    with d3
    her "Спасибо, сэр..."

    if whoring <= 14:
        $ whoring +=1

    
    
    if whoring >= 12 and whoring <= 14:
        $ level = "05"
        $ new_request_16_01 = True #  Hearts
    if whoring >= 15 and whoring <= 17:
        $ level = "06"
        $ new_request_16_02 = True #  Hearts
    

    $ request_16_points += 1

    hide screen bld1
    hide screen hermione_main
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

    $ aftersperm = False #Show cum stains on Hermione's uniform.
    call music_block
    if daytime:
        $ hermione_takes_classes = True
        jump night_main_menu
    else:
        $ hermione_sleeping = True
        jump day_main_menu            
   

        
        
### KISS SUCK! ###

label kiss_suck: #Jumps here after event #03 and if WHORING >= LEVEL 07
    ">Гермиона нежно тянется своими губами к вашему члену и целует его..."
    ">Это простое действие заставило ваш член практически взорваться потоком спермы."
    show screen white 
    pause.1
    hide screen white
    pause.2
    show screen white 
    pause .1
    hide screen white
    with hpunch
    g4 "{size=+5}Агрх! ДА!!!{/size}"
    $ genie_chibi_xpos = 60 #-185 behind the desk.
    $ genie_chibi_ypos = 10
    $ g_c_u_pic = "kiss_cum_ani"
    
    hide screen blkfade
    with d3
    show screen ctc
    hide screen bld1
    with d3
    pause
    
    
    
    show screen bld1
    with d3
                        
   
    her2 "*Глп!-Глп!-Глп!*"
    hide screen h_head2          
    g4 "Аргх! Ты маленькая шлюха!"
    g4 "Да, блядь! Пей мою сперму! Выпей ее всю!"
    her2 "*Глп!-Глп!-Глп!*"
    g4 "Арх... Да!"
    ">Вы замечаете что Гермиона едва справляется с таким потоком спермы в своем рту."
    her2 "*Глп!-Глп!-Глп!*"
    g4 "Ах..."
    g4 "Просто великолепное чувство..."
    her2 "*Глп!-Глп!-Глп!*"
    m "Я думаю это все, девочка..."
    m "Можешь идти..."
    pause
    show screen blkfade
    with d5
    show screen hermione_01 
    hide screen chair_02
    hide screen desk_02
    hide screen g_c_u
    show screen genie
    hide screen hermione_main                                                                                                                                                                                   #HERMIONE
                                                                                                                                                                                                                         #HERMIONE
    $ h_xpos=140 #Defines position of the Hermione's full length sprite. (Default 370). (Center: 140)                                                        #HERMIONE
    $ h_body = "03_hp/13_hermione_main/body_125.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
    show screen hermione_main                                                                                                                                                                                 #HERMIONE
    with d3       
    show screen ctc
    pause
    her2 "........................................."
    hide screen hermione_main                                                                                                                                                                                   #HERMIONE
    with d3                                                                                                                                                                                                                   #HERMIONE
    $ h_xpos=140 #Defines position of the Hermione's full length sprite. (Default 370). (Center: 140)                                                        #HERMIONE
    $ h_body = "03_hp/13_hermione_main/body_126.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
    show screen hermione_main                                                                                                                                                                                 #HERMIONE
    her2 "ГЛП!!!"
    hide screen hermione_main                                                                                                                                                                                   #HERMIONE
    with d3                                                                                                                                                                                                                   #HERMIONE
    $ h_xpos=140 #Defines position of the Hermione's full length sprite. (Default 370). (Center: 140)                                                        #HERMIONE
    $ h_body = "03_hp/13_hermione_main/body_39.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
    show screen hermione_main                                                                                                                                                                                 #HERMIONE
    her2 "Гу-а-а..."
    hide screen blkfade
    with d3
    hide screen hermione_main                                                                                                                                                                                   #HERMIONE
    with d3                                                                                                                                                                                                                   #HERMIONE
    $ h_xpos=140 #Defines position of the Hermione's full length sprite. (Default 370). (Center: 140)                                                        #HERMIONE
    $ h_body = "03_hp/13_hermione_main/body_123.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
    show screen hermione_main                                                                                                                                                                                 #HERMIONE
    her2 "Я проглотила ее всю, сэр!"
    m "Хорошая девочка..."
    hide screen hermione_main                                                                                                                                                                                   #HERMIONE
    with d3                                                                                                                                                                                                                   #HERMIONE
    $ h_xpos=140 #Defines position of the Hermione's full length sprite. (Default 370). (Center: 140)                                                        #HERMIONE
    $ h_body = "03_hp/13_hermione_main/body_123.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
    show screen hermione_main                                                                                                                                                                                 #HERMIONE
    her "В один момент я думала что задохнусь..."
    her2 "Ее было так много..."
    hide screen h_head2
    m "Что же, дело сделано и твоя форма идеально чистая."
    hide screen hermione_main                                                                                                                                                                                   #HERMIONE
    with d3                                                                                                                                                                                                                   #HERMIONE
    $ h_xpos=140 #Defines position of the Hermione's full length sprite. (Default 370). (Center: 140)                                                        #HERMIONE
    $ h_body = "03_hp/13_hermione_main/body_124.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
    show screen hermione_main                                                                                                                                                                                 #HERMIONE
    her2 "Да! Я знаю! Этот вариант намного лушче!"
    if daytime:
        hide screen hermione_main                                                                                                                                                                                   #HERMIONE
        with d3                                                                                                                                                                                                                   #HERMIONE
        $ h_xpos=140 #Defines position of the Hermione's full length sprite. (Default 370). (Center: 140)                                                        #HERMIONE
        $ h_body = "03_hp/13_hermione_main/body_122.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
        show screen hermione_main       
        with d3                                                                                                                                                                                                                                 #HERMIONE
        her "Я лучше просто пойду в класс, как будто ничего и не было."
    else:
        hide screen hermione_main                                                                                                                                                                                   #HERMIONE
        with d3                                                                                                                                                                                                                   #HERMIONE
        $ h_xpos=140 #Defines position of the Hermione's full length sprite. (Default 370). (Center: 140)                                                        #HERMIONE
        $ h_body = "03_hp/13_hermione_main/body_124.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
        show screen hermione_main                  
        with d3 #HERMIONE
        her "Я могу просто пойти и провести время с парнями в Общей Комнате и никто не узнает..."
    hide screen h_head2
    m "Да... С полным животом спермы..."
    hide screen hermione_main                                                                                                                                                                                     #HERMIONE
    with d3                                                                                                                                                                                                                           #HERMIONE
    $ h_xpos=140 #Defines position of the Hermione's full length sprite. (Default 370). (Center: 140)                                                           #HERMIONE
    $ h_body = "03_hp/13_hermione_main/body_117.png" #Sprite of Hermione's upper body.                                                                    #HERMIONE
    show screen hermione_main                                                                                                                                                                                      #HERMIONE
    with d3                                                                                                                                                                                                                             #HERMIONE
    her2 "Профессор!"
    her2 "...Могу ли я получить оплату, сэр?"
    hide screen h_head2
    jump done_with_handjob #^^^ (<-That's to a smiley. That's a arrow up).
    
     
     
     
     
     
     
     
     
     
     
     
     
     
     
     
     
###################REQUEST_17 (Level 05) (Stick a finger up her butthole.) (Day/Night)
label new_request_17: #LV.5 (Whoring = 12 - 14)
    if whoring <=11:
        jump too_much
        
    m "Подойди сюда и дай мне засунуть палец в твою попку."
    if request_17_points == 0: #One star.
        her "Ох... "
        ">Гермиона неохотно соглашается."
    elif request_17_points == 1: #Two stars.
        her "...Да, профессор."
        ">Гермиона соглашается."
    elif request_17_points == 2: #Three stars.
        ">Гермиона беззаботно соглашается."
    elif request_17_points >= 3: #Master.
        her "Вот, профессор."
        ">Гермиона горячо соглашается."
        
    "Вы отпустили Гермиону."
        
    if whoring <= 14:
        $ whoring +=1

    if request_17_points <= 2:
        $ gryffindor +=45
        "Гриффиндор получает 45 очков."
    else:
        $ gryffindor +=11
        "Гриффиндор получает 11 очков."
       
    $ request_17_points += 1
    
    if daytime:
        $ hermione_takes_classes = True
        jump day_main_menu
    else:
        $ hermione_sleeping = True
        jump night_main_menu        
        
        
###################REQUEST_18 (Level 05) (Handjob) (Day/Night)
label new_request_18: #LV.5 (Whoring = 12 - 14)
    if whoring <=11:
        jump too_much
        
    m "Подойди и потрогай мой член."
    if request_18_points == 0: #One star.
        her "Ох... "
        ">Гермиона неохотно соглашается."
    elif request_18_points == 1: #Two stars.
        her "...Да, профессор."
        ">Гермиона соглашается."
    elif request_18_points == 2: #Three stars.
        ">Гермиона беззаботно соглашается."
    elif request_18_points >= 3: #Master.
        her "Вот, профессор."
        ">Гермиона горячо соглашается."
        
    "Вы отпускаете Гермиону."
        
    if whoring <= 14:
        $ whoring +=1

    if request_18_points <= 2:
        $ gryffindor +=45
        "Гриффиндор получает 45 очков."
    else:
        $ gryffindor +=11
        "Гриффиндор получает 11 очков."
       
    $ request_18_points += 1
    
    if daytime:
        $ hermione_takes_classes = True
        jump day_main_menu
    else:
        $ hermione_sleeping = True
        jump night_main_menu        
        
        
    
###################REQUEST_19 (Level 05) (Rub her dick against her cheeks.) (Day/Night)
label new_request_19: #LV.5 (Whoring = 12 - 14)
    if whoring <=11:
        jump too_much
    
    m "Иди сюда и потри мой член о свои милые щечки."
    if request_19_points == 0: #One star.
        her "Ох... "
        ">Гермиона неохотно соглашается."
    elif request_19_points == 1: #Two stars.
        her "...Да, профессор."
        ">Гермиона соглашается."
    elif request_19_points == 2: #Three stars.
        ">Гермиона беззаботно соглашается."
    elif request_19_points >= 3: #Master.
        her "Как скажете, профессор."
        ">Гермиона с нетерпением соглашается."
        
    "Вы прогоняете Гермиону."
        
    if whoring <= 14:
        $ whoring +=1

    if request_19_points <= 2:
        $ gryffindor +=45
        "Гриффиндор получает 45 очков."
    else:
        $ gryffindor +=11
        "Гриффиндор получает 11 очков."
       
    $ request_19_points += 1
    
    if daytime:
        $ hermione_takes_classes = True
        jump day_main_menu
    else:
        $ hermione_sleeping = True
        jump night_main_menu        
        
        

    
    
    
#############################################################################################################################################
### LEVEL 06 ################################################################################################################################       
###################REQUEST_21 (Level 06) (55 pt.) (Cum on tits). ############################################################################ 
#As this request levels up, there are an option appears to offer some extra points if Hermione will put her clothes
#on top of her sperm covered tits and go to classes like that.
label new_request_21: #LV.6 (Whoring = 15 - 17)
    if whoring <=14:
        jump too_much
    
    m "Подойди сюда и дай подрочить на твои сиськи."
    if request_21_points == 0: #One star.
        her "Ох... "
        ">Гермиона неохотно соглашается."
        ">Вы кончаете на ее голую грудь."
    elif request_21_points == 1: #Two stars.
        her "...Да, профессор."
        ">Гермиона соглашается."
        ">Вы кончаете на ее голую грудь."
    elif request_21_points == 2: #Three stars.
        ">Гермиона беззаботно соглашается."
        ">Вы кончаете на ее голую грудь."

    elif request_21_points >= 3: #Master.
        her "Как пожелаете, дире... хозяин."
        ">Гермиона горячо соглашается."
        ">Вы кончаете на ее голую грудь."
    
    her "Можно дать мне полотенце, чтобы я могла вытереться?"
    menu:
        "\"Конечно.\"":
            ">Вы даете Гермионе полотенце и она вытирает вашу сперму."
        "\"Иди так.\"":
            m "Просто застегни блузку и иди так."
            
            if request_21_points <= 1:
                her "Что? Я не могу так, пожалуйста дайте полотенце."
                ">Вы даете Гермионе полотенце и она вытирает вашу сперму."
           
            else:
                her "Что? Но..."
                her "Хорошо, но только если вы дадите мне дополнительные баллы."
                menu:
                    "-Дать дополнительные баллы-":
                        m "Хорошо..."
                        her "Тогда ладно..."
                        ">Гермиона застегивает свою блузку."
                        $ gryffindor +=10
                        "Гриффиндор получает 10 очков."
                        $ request_21 = True
                    "-Забудь-":
                        ">Вы даете Гермионе полотенце и она вытирает вашу сперму."
            
    "Вы отпускаете Гермиону."
        
    if whoring <= 14:
        $ whoring +=1

    if request_21_points <= 2:
        $ gryffindor +=55
        "Гриффиндор получает 55 очков."
    else:
        $ gryffindor +=12
        "Гриффиндор получает 12 очков."
       
    $ request_21_points += 1 
    
    if daytime:
        $ hermione_takes_classes = True
        jump day_main_menu
    else:
        $ hermione_sleeping = True
        jump night_main_menu        
        
        
        
label new_request_21_complete:
    "Гермиона возвращается в свой класс."
    m "Как прошел твой день?"
    if request_21_points == 3: #One star.
        her "Эм... В классе я сидела и чувствовала как мои сиськи полностью покрыты спермой. Это было так неприятно..."
    elif request_21_points >= 4: #Two stars.
        her "В классе я сидела и чувствовала как мои сиськи полностью покрыты спермой. Это просто лучше всего."
             

    
    $ request_21 = False 
    $ hermione_sleeping = True
    her "О, ладно. Я просто вернусь в постель."
    return        
        
        
    

    

#############################################################################################################################################
### LEVEL 07 ################################################################################################################################  
#############################################################################################################################################
    
###################REQUEST_25 (Level 07) (65 pt.) (Cum on face). 
label new_request_25: #LV.7 (Whoring = 18 - 20)
    if whoring <=17:
        jump too_much
    
    m "Подойди сюда и дай мне кончить на твое лицо."
    if request_25_points == 0: #One star.
        her "О... "
        ">Гермиона неохотно соглашается."
        ">Вы кончаете ей на лицо."
    elif request_25_points == 1: #Two stars.
        her "...Да, профессор."
        ">Гермиона соглашается."
        ">Вы кончаете ей на лицо."
    elif request_25_points == 2: #Three stars.
        ">Гермиона беззаботно соглашается."
        ">Вы кончаете ей на лицо."

    elif request_25_points >= 3: #Master.
        her "Конечно, дире...хозяин."
        ">Гермиона горячо соглашается."
        ">Вы кончаете ей на лицо."
    
    her "Могу я взять полотенце, чтобы вытереться?"
    menu:
        "\"Конечно.\"":
            ">Вы даете Гермионе полотенце и она стирает с лица вашу сперму."
        "\"Иди так.\"":
            m "Иди на уроки с покрытым спермой лицом."
            
            if whoring <=26:
                her "Что? Нет, я не могу, пожалуйста дайте мне полотенце!."
                ">Вы даете Гермионе полотенце и она стирает с лица вашу сперму."
           
            else:
                her "Что? Но..."
                her "Хорошо, но только если вы дадите мне дополнительные баллы."
                menu:
                    "-Дать дополнительные баллы-":
                        m "Хорошо..."
                        her "Тогда ладно..."
                        ">Гермиона не трогает свое обкончанное лицо."
                        $ gryffindor +=30
                        "Гриффиндор получает 30 очков."
                        $ request_25 = True
                    "-Забудь-":
                        ">Вы даете Гермионе полотенце и она стирает с лица вашу сперму."
            
    "Вы отпускаете Гермиону."
        
    if whoring <= 20:
        $ whoring +=1

    if request_21_points <= 2:
        $ gryffindor +=65
        "Гриффиндор получает 65 очков."
    else:
        $ gryffindor +=14
        "Гриффиндор получает 14 очков."
       
    $ request_25_points += 1 
    
    if daytime:
        $ hermione_takes_classes = True
        jump day_main_menu
    else:
        $ hermione_sleeping = True
        jump night_main_menu        
        
        
        
label new_request_25_complete:
    "Гермиона возвращается с уроков."
    m "Как прошел ваш день, Мисс Грейнджер?"
    her "Эм... Я провела большую часть дня с покрытым спермой лицом. Мне постоянно задавали вопросы."
    
    
    $ request_25 = False 
    $ hermione_sleeping = True
    her "Хорошо. Тогда я пойду спать."
    return        
        

###################REQUEST_26 (Level 07) (65 pt.) (Cum in open mouth before class). (Available during daytime only).
label new_request_26: #LV.7 (Whoring = 18 - 20)
    if whoring <=17:
        jump too_much
    m "Я хочу кончить тебе в лицо, до того как ты пойдешь в класс."
    if request_26_points == 0: #One star.
        her "О..."
        "Гермиона неохотно соглашается."
    elif request_26_points == 1: #Two stars.
        her "Если я должна..."
        "Гермиона соглашается."
    elif request_26_points == 2: #Three stars.
        her "Конечно... профессор."
        "Гермиона соглашается. По ней видно как она этого хочет."    
    elif request_26_points >= 3: #Master.
        her "Конечно, дире...хозяин"
        ">Гермиона радостно соглашается."
    
    "Вы отпускаете Гермиону."
    
    $ request_26 = True 
    if whoring <= 20:
        $ whoring +=1
        
    if request_26_points <= 2:
        $ gryffindor +=65
        "Гриффиндор получает 65 очков."
    else:
        $ gryffindor +=14
        "Гриффиндор получает 14 очков."

    $ hermione_takes_classes = True
    jump day_main_menu
        

label new_request_26_complete:
    "Гермиона возвращается с занятий."
    m "Как прошел ваш день, Мисс Грейнджер?"
    if request_26_points == 0: #One star.
        her "Эм... Я провела половину урока со спермой во рту"
    elif request_26_points == 1: #Two stars.
        her "Something else about cum. LVL 2"
    elif request_26_points == 2: #Three stars.
        her "LVL3"
    elif request_26_points >= 3: #Three stars.
        her "LVL4"
        her "Это было чудесно!"
    
    $ request_26_points += 1 
    $ request_26 = False 
    $ hermione_sleeping = True
    her "Ох, ладно, тогда я пойду в постель."
    return
    
###################REQUEST_27 (Level 07) (65 pt.) (Blow two classmates). (Available during daytime only).
label new_request_27: #LV.7 (Whoring = 18 - 20)
    if whoring <=17:
        jump too_much
    m "Я хочу, чтобы вы кое-что сделали для меня сегодня: отсосите у двух одноклассников"
    if request_27_points == 0: #One star.
        her "Ох..."
        "Гермиона неохотно соглашается."
    elif request_27_points == 1: #Two stars.
        her "Если я должна..."
        "Гермиона соглашается."
    elif request_27_points == 2: #Three stars.
        her "Конечно, профессор"
        "Гермиона согласна. Она жаждет этого."    
    elif request_27_points >= 3: #Master.
        her "Конечно директор..."
        ">Гермиона с радостью соглашается."
    
    "Вы отпускаете Гермиону."
    
    $ request_27 = True 
    if whoring <= 20:
        $ whoring +=1
        
    if request_27_points <= 2:
        $ gryffindor +=65
        "Гриффиндор получает 65 очков."
    else:
        $ gryffindor +=14
        "Гриффиндор получает 14 очков."

    $ hermione_takes_classes = True
    jump day_main_menu
        

label new_request_27_complete:
    "Гермиона возвращается с занятий."
    m "Как прошел ваш день, Мисс Грейнджер?"
    if request_27_points == 0: #One star.
        her "Эм... Lvl.1."
    elif request_27_points == 1: #Two stars.
        her "Something else about LVL 2"
    elif request_27_points == 2: #Three stars.
        her "LVL3"
    elif request_27_points >= 3: #Three stars.
        her "LVL4"
        her "Это было чудесно!"
    
    $ request_27_points += 1 
    $ request_27 = False 
    $ hermione_sleeping = True
    her "Ох, ладно. Пожалуй я пойду спать."
    return
    
    
###################REQUEST_28 (Level 07) (65 pt.) (Give handjob to a teacher). (Available during daytime only).
label new_request_28: #LV.7 (Whoring = 18 - 20)
    if whoring <=17:
        jump too_much
    m "Я хочу, чтобы ты подрочила своему учителю"
    if request_28_points == 0: #One star.
        her "Ох..."
        "Гермиона неохотно соглашается."
    elif request_28_points == 1: #Two stars.
        her "Если так нужно..."
        "Гермиона соглашается."
    elif request_28_points == 2: #Three stars.
        her "Конечно, профессор."
        "Гермиона соглашается. Она жаждет этого."    
    elif request_28_points >= 3: #Master.
        her "Конечно директор..."
        ">Гермиона с радостью соглашается."
    
    "Вы отпускаете Гермиону."
    
    $ request_28 = True 
    if whoring <= 20:
        $ whoring +=1
        
    if request_28_points <= 2:
        $ gryffindor +=65
        "Гриффиндор получает 65 очков."
    else:
        $ gryffindor +=14
        "Гриффиндор получает 14 очков."

    $ hermione_takes_classes = True
    jump day_main_menu

        
label new_request_28_complete:
    "Гермиона возвращается с занятий."
    m "Как прошел ваш день, Мисс Грейнджер?"
    if request_28_points == 0: #One star.
        her "Em... Lvl.1."
    elif request_28_points == 1: #Two stars.
        her "Something else about LVL 2"
    elif request_28_points == 2: #Three stars.
        her "LVL3"
    elif request_28_points >= 3: #Three stars.
        her "LVL4"
        her "Это было чудесно!"
    
    $ request_28_points += 1 
    $ request_28 = False 
    $ hermione_sleeping = True
    her "Ох, ладно. Я тогда пойду спать."
    return
    


   
    
    


    
###############################################################################################################################################
### LEVEL 10 ##################################################################################################################################
###################REQUEST_32 (Level 10) (100 pt.) (Wear a very revealing outfit to class). (Daytime only) ####################################
label new_request_32: #LV.10 (Whoring = 27 - 29)
    if whoring <=26:
        jump too_much
    m "Я хочу, чтобы ты надела это."
    if request_32_points == 0: #One star.
        her "Ох..."
        "Гермиона неохотно соглашается."
    elif request_32_points == 1: #Two stars.
        her "Если так нужно..."
        "Гермиона соглашается."
    elif request_32_points == 2: #Three stars.
        her "Конечно, профессор."
        "Гермиона соглашается. Она жаждет этого."    
    elif request_32_points >= 3: #Master.
        her "Конечно, директор..."
        ">Гермиона с радостью соглашается."
    
    "Гермиона надевает очень распутный наряд и идет на занятия."
    
    $ request_32 = True 
    if whoring <= 29:
        $ whoring +=1
        
    if request_32_points <= 2:
        $ gryffindor +=100
        "Гриффиндор получает 100 очков."
    else:
        $ gryffindor +=23
        "Гриффиндор получает 23 очков."

    $ hermione_takes_classes = True
    jump day_main_menu


label new_request_32_complete:
    "Гермиона возвращается с занятий."
    m "Как прошел ваш день, Мисс Грейнджер?"
    if request_32_points == 0: #One star.
        her "Em... Lvl.1. She tells you how people treated her like a whore today."
    elif request_32_points == 1: #Two stars.
        her "Something else about LVL 2. She tells you how people treated her like a whore today."
    elif request_32_points == 2: #Three stars.
        her "LVL3. She tells you how people treated her like a whore today."
    elif request_32_points >= 3: #Three stars.
        her "LVL4. She tells you how people treated her like a whore today."
        her "Это было чудесно!"
    
    $ request_32_points += 1
    $ request_32 = False 
    $ hermione_sleeping = True
    her "Ох, ладно. Я тогда пойду спать."
    return
    
    
    

    
    
    
    
    
### MUSIC BLOCK ###
label music_block:
    if daytime:
        play music "music/Brittle Rille.mp3" fadein 1 fadeout 1 # DAY MUSIC
    else:
        play music "music/Music for Manatees.mp3" fadein 1 fadeout 1 # NIGHT MUSIC
    return
    ### END OF BLOCK ###    
    
    


### YOU LUCK IMAGINATION ###
label vague_idea:
    show screen blktone8
    ">Вам не хватает воображения для такого."
    hide screen blktone8
    return