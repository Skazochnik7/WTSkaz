label new_personal_request:
    $ pos = POS_410
    if slytherin > gryffindor or slytherin == gryffindor:
        $ herView.showQ( None, pos )
        
        $ menu_x = 0.2 #Default: 0.5
        
        label not_now:
        menu:
            "- Личные услуги -":
                label not_now2:
                ### LEVEL 01 ###
                menu:
#                    "Услуга: \"Поговори со мной\" {image=heart_00.png}" if not new_request_01_01 and not new_request_01_02 and not new_request_01_03:
#                        jump new_request_01
#                    "Услуга: \"Поговори со мной\" {image=heart_01.png}" if new_request_01_01 and not new_request_01_02 and not new_request_01_03:
#                        jump new_request_01
#                    "Услуга: \"Поговори со мной\" {image=heart_02.png}" if new_request_01_02 and not new_request_01_03:
#                        jump new_request_01
#                    "Услуга: \"Поговори со мной\" {image=heart_03.png}" if new_request_01_03:
#                        jump new_request_01
                    "Услуга: [this.new_request_01._caption] {image=heart_4[this.new_request_01._heartCount].png}":
                        jump new_request_01

#                    "Услуга: \"Отличные трусики!\" {image=heart_00.png}" if not new_request_02_01 and not new_request_02_02 and not new_request_02_03: # LEVEL 1
#                        jump new_request_02
#                    "Услуга: \"Отличные трусики!\" {image=heart_01.png}" if new_request_02_01 and not new_request_02_02 and not new_request_02_03: # LEVEL 1
#                        jump new_request_02
#                    "Услуга: \"Отличные трусики!\" {image=heart_02.png}" if new_request_02_02 and not new_request_02_03: # LEVEL 1
#                        jump new_request_02
#                    "Услуга: \"Отличные трусики!\" {image=heart_03.png}" if new_request_02_03: # LEVEL 1
#                        jump new_request_02
                    "Услуга: [this.new_request_02._caption] {image=heart_4[this.new_request_02._heartCount].png}":
                        jump new_request_02
                  
                    ### LEVEL 02 ###
                    "{color=#858585}--Не открытое действие-{/color} -" if imagination == 1:
                        call vague_idea
                        jump not_now2
#                    "Услуга: \"Вор трусиков\" {image=heart_00.png}" if not new_request_03_01 and not new_request_03_02 and not new_request_03_03 and daytime and imagination >= 2:
#                        jump new_request_03
#                    "Услуга: \"Вор трусиков\" {image=heart_01.png}" if new_request_03_01 and not new_request_03_02 and not new_request_03_03 and daytime and imagination >= 2:
#                        jump new_request_03
#                    "Услуга: \"Вор трусиков\" {image=heart_02.png}" if new_request_03_02 and not new_request_03_03 and daytime and imagination >= 2:
#                        jump new_request_03
#                    "Услуга: \"Вор трусиков\" {image=heart_03.png}" if new_request_03_03 and daytime and imagination >= 2:
#                        jump new_request_03
                    "Услуга: [this.new_request_03._caption] {image=heart_4[this.new_request_03._heartCount].png}" if daytime and imagination >= 2:
                        jump new_request_03


                    
                    "{color=#858585}--Не открытое действие-{/color} -" if imagination == 1:
                        call vague_idea
                        jump not_now2
#                    "Услуга: \"Полапать грудь!\" {image=heart_00.png}" if not new_request_04_01 and not new_request_04_02 and not new_request_04_03 and imagination >= 2: 
#                        jump new_request_04
#                    "Услуга: \"Полапать грудь!\" {image=heart_01.png}" if new_request_04_01 and not new_request_04_02 and not new_request_04_03 and imagination >= 2: 
#                        jump new_request_04
#                    "Услуга: \"Полапать грудь!\" {image=heart_02.png}" if new_request_04_02 and not new_request_04_03 and imagination >= 2: 
#                        jump new_request_04
#                    "Услуга: \"Полапать грудь!\" {image=heart_03.png}" if new_request_04_03 and imagination >= 2: 
#                        jump new_request_04
                    "Услуга: [this.new_request_04._caption] {image=heart_4[this.new_request_04._heartCount].png}" if imagination >= 2:
                        jump new_request_04
                        
                    "{color=#858585}--Не открытое действие-{/color} -" if imagination == 1:
                        call vague_idea
                        jump not_now2
#                    "Услуга: \"Полапать попку!\" {image=heart_00.png}" if not new_request_05_01 and not new_request_05_02 and not new_request_05_03 and imagination >= 2:
#                        jump new_request_05
#                    "Услуга: \"Полапать попку!\" {image=heart_01.png}" if new_request_05_01 and not new_request_05_02 and not new_request_05_03 and imagination >= 2: 
#                        jump new_request_05
#                    "Услуга: \"Полапать попку!\" {image=heart_02.png}" if new_request_05_02 and not new_request_05_03 and imagination >= 2: 
#                        jump new_request_05
#                    "Услуга: \"Полапать попку!\" {image=heart_03.png}" if new_request_05_03 and imagination >= 2: 
#                        jump new_request_05
                    "Услуга: [this.new_request_05._caption] {image=heart_0[this.new_request_05._heartCount].png}" if imagination >= 2:
                        jump new_request_05
                        
                    ### LEVEL 03 ### IMAGINATION == 3
                    "{color=#858585}--Не открытое действие-{/color} -" if imagination < 3:
                        call vague_idea
                        jump not_now2
#                    "Услуга: \"Покажи их мне!\" {image=heart_00.png}" if not new_request_08_01 and not new_request_08_02 and not new_request_08_03 and imagination >= 3:
#                        jump new_request_08
#                    "Услуга: \"Покажи их мне!\" {image=heart_01.png}" if new_request_08_01 and not new_request_08_02 and not new_request_08_03 and imagination >= 3: 
#                        jump new_request_08
#                    "Услуга: \"Покажи их мне!\" {image=heart_02.png}" if new_request_08_02 and not new_request_08_03 and imagination >= 3: 
#                        jump new_request_08
#                    "Услуга: \"Покажи их мне!\" {image=heart_03.png}" if new_request_08_03 and imagination >= 3: 
#                        jump new_request_08 
                    "Услуга: [this.new_request_08._caption] {image=heart_4[this.new_request_08._heartCount].png}" if imagination >= 3:
                        jump new_request_08
 

#                    "Услуга: \"Show {size=+5}it{/size} to me! (NOT FINISHED YET)":
#                        jump new_request_09
                    
                    ### LEVEL 04 ### IMAGINATION == 3
                    "{color=#858585}--Не открытое действие-{/color} -" if imagination < 3:
                        call vague_idea
                        jump not_now2
#                    "Услуга: \"Станцуй для меня!\" {image=heart_00.png}" if not new_request_11_01 and not new_request_11_02 and not new_request_11_03 and imagination >= 3:
#                        jump new_request_11
#                    "Услуга: \"Станцуй для меня!\" {image=heart_01.png}" if new_request_11_01 and not new_request_11_02 and not new_request_11_03 and imagination >= 3: 
#                        jump new_request_11
#                    "Услуга: \"Станцуй для меня!\" {image=heart_02.png}" if new_request_11_02 and not new_request_11_03 and imagination >= 3:
#                        jump new_request_11
#                    "Услуга: \"Станцуй для меня!\" {image=heart_03.png}" if new_request_11_03 and imagination >= 3: 
#                        jump new_request_11
                    "Услуга: [this.new_request_11._caption] {image=heart_0[this.new_request_11._heartCount].png}" if imagination >= 3:
                        jump new_request_11

                    
                    "{color=#858585}--Не открытое действие-{/color} -" if imagination < 3:
                        call vague_idea
                        jump not_now2
#                    "Услуга: \"Дай мне потрогать их!\" {image=heart_00.png}" if not new_request_12_01 and not new_request_12_02 and not new_request_12_03 and daytime and imagination >= 3: # LEVEL 4
#                        jump new_request_12
#                    "Услуга: \"Дай мне потрогать их!\" {image=heart_01.png}" if new_request_12_01 and not new_request_12_02 and not new_request_12_03 and daytime and imagination >= 3: # LEVEL 4
#                        jump new_request_12
#                    "Услуга: \"Дай мне потрогать их!\" {image=heart_02.png}" if new_request_12_02 and not new_request_12_03 and daytime and imagination >= 3: # LEVEL 4
#                        jump new_request_12
#                    "Услуга: \"Дай мне потрогать их!\" {image=heart_03.png}" if new_request_12_03 and daytime and imagination >= 3: # LEVEL 4
#                        jump new_request_12
                    "Услуга: [this.new_request_12._caption] {image=heart_0[this.new_request_12._heartCount].png}" if imagination >= 3:
                        jump new_request_12

                    
                    ### LEVEL 05 ### IMAGINATION == 4
                    "{color=#858585}--Не открытое действие-{/color} -" if imagination < 4:
                        call vague_idea
                        jump not_now2
#                    "Услуга: \"Потрогай меня!\" {image=heart_00.png}" if not new_request_16_01 and not new_request_16_02 and not new_request_16_03 and imagination >= 4: # LEVEL 5
#                        jump new_request_16
#                    "Услуга: \"Потрогай меня!\" {image=heart_01.png}" if new_request_16_01 and not new_request_16_02 and not new_request_16_03 and imagination >= 4: # LEVEL 5
#                        jump new_request_16
#                    "Услуга: \"Потрогай меня!\" {image=heart_02.png}" if new_request_16_02 and not new_request_16_03 and imagination >= 4: # LEVEL 5
#                        jump new_request_16
#                    "Услуга: \"Потрогай меня!\" {image=heart_03.png}" if new_request_16_03 and imagination >= 4:  # LEVEL 5
#                        jump new_request_16
                    "Услуга: [this.new_request_16._caption] {image=heart_0[this.new_request_16._heartCount].png}" if imagination >= 4:
                        jump new_request_16

                       
                    ### LEVEL 06 ### IMAGINATION == 4
                    "{color=#858585}--Не открытое действие-{/color} -" if imagination < 4:
                        call vague_idea
                        jump not_now2
#                    "Услуга: \"Соси его!\" {image=heart_00.png}" if not new_request_22_01 and not new_request_22_02 and not new_request_22_03 and imagination >= 4: # LEVEL 6
#                        jump new_request_22
#                    "Услуга: \"Соси его!\" {image=heart_01.png}" if new_request_22_01 and not new_request_22_02 and not new_request_22_03 and imagination >= 4: # LEVEL 6
#                        jump new_request_22
#                    "Услуга: \"Соси его!\" {image=heart_02.png}" if new_request_22_02 and not new_request_22_03 and imagination >= 4: # LEVEL 6
#                        jump new_request_22
#                    "Услуга: \"Соси его!\" {image=heart_03.png}" if new_request_22_03 and imagination >= 4: # LEVEL 6
#                        jump new_request_22
                    "Услуга: [this.new_request_22._caption] {image=heart_0[this.new_request_22._heartCount].png}" if imagination >= 4:
                        jump new_request_22

                    
                    ### LEVEL 07 ### IMAGINATION == 5
                    "{color=#858585}--Не открытое действие-{/color} -" if imagination < 5:
                        call vague_idea
                        jump not_now2
#                    "Услуга: \"Давай займемся сексом!\" {image=heart_00.png}" if not new_request_29_01 and not new_request_29_02 and not new_request_29_03 and imagination >= 5: # LEVEL 7
#                        jump new_request_29
#                    "Услуга: \"Давай займемся сексом!\" {image=heart_01.png}" if new_request_29_01 and not new_request_29_02 and not new_request_29_03 and imagination >= 5: # LEVEL 7
#                        jump new_request_29
#                    "Услуга: \"Давай займемся сексом!\" {image=heart_02.png}" if new_request_29_02 and not new_request_29_03 and imagination >= 5: # LEVEL 7
#                        jump new_request_29
#                    "Услуга: \"Давай займемся сексом!\" {image=heart_03.png}" if new_request_29_03 and imagination >= 5: # LEVEL 7
#                        jump new_request_29
                    "Услуга: [this.new_request_29._caption] {image=heart_0[this.new_request_29._heartCount].png}" if imagination >= 5:
                        jump new_request_29
                        
                    ### LEVEL 08 ###
                    "{color=#858585}--Не открытое действие-{/color} -" if imagination < 5:
                        call vague_idea
                        jump not_now2
#                    "Услуга:  \"Время для анала!\" {image=heart_00.png}" if not new_request_31_01 and not new_request_31_02 and not new_request_31_03 and imagination >= 5: # LEVEL 8
#                        jump new_request_31
#                    "Услуга:  \"Время для анала!\" {image=heart_01.png}" if new_request_31_01 and not new_request_31_02 and not new_request_31_03 and imagination >= 5: # LEVEL 8
#                        jump new_request_31
#                    "Услуга:  \"Время для анала!\" {image=heart_02.png}" if new_request_31_02 and not new_request_31_03 and imagination >= 5: # LEVEL 8
#                        jump new_request_31
#                    "Услуга:  \"Время для анала!\" {image=heart_03.png}" if new_request_31_03 and imagination >= 5: # LEVEL 8
#                        jump new_request_31
                    "Услуга: [this.new_request_31._caption] {image=heart_0[this.new_request_31._heartCount].png}" if imagination >= 5:
                        jump new_request_31

                            
                    "- Отмена -":
                        jump new_personal_request
                
            "{color=#858585}-Публичные услуги-{/color}" if not daytime:
                show screen blktone
                $herView.hideQQ()
                ">Публичные услуги недоступны в это время суток."
                hide screen blktone
                $herView.showQ( None, pos )
                with d3
                jump not_now
            "- Публичные услуги -" if daytime:
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
                        "{color=#858585}--Не открытое действие-{/color} -" if imagination < 2:
                            call vague_idea
                            jump not_now3
                        "Услуга: \"Флиртуй с учителем\"" if daytime  and imagination >= 2:
                            jump new_request_02_c
                        
                        ### LEVEL 03 ### IMAGINATION == 3
                        "{color=#858585}--Не открытое действие-{/color} -" if imagination < 3:
                            call vague_idea
                            jump not_now3
                        "Услуга: \"Дай однокласснику поприставать к тебе.\"" if imagination >= 3: # LEVEL 3
                            jump new_request_10
                        
                        ### LEVEL 04 ### IMAGINATION == 3
                        "{color=#858585}--Не открытое действие-{/color} -" if imagination < 3:
                            call vague_idea
                            jump not_now3
                        "Услуга: \"Посвети сиськами перед одноклассниками.\"" if imagination >= 3: # LEVEL 4
                            jump new_request_15
                        
                        
                        ### LEVEL 05 ### IMAGINATION == 4
                        "{color=#858585}--Не открытое действие-{/color} -" if imagination < 4:
                            call vague_idea
                            jump not_now3
                        "Услуга: \"Поцелуй девченку.\"" if imagination >= 4: # LEVEL 5
                            jump new_request_20
                            
                        ### LEVEL 06 ### IMAGINATION == 4
                        "{color=#858585}--Не открытое действие-{/color} -" if imagination < 4:
                            call vague_idea
                            jump not_now3
                        "Услуга: \"Вздрочни однокласснику.\"" if imagination >= 4: # LEVEL 6
                            jump new_request_23
                            
                        ### LEVEL 07 ### IMAGINATION == 5
                        "{color=#858585}--Не открытое действие-{/color} -" if imagination < 5:
                            call vague_idea
                            jump not_now3
                        "Услуга: \"Отсоси однокласснику\"" if imagination >= 5:# LEVEL 7
                            jump new_request_24
                                
                         ### LEVEL 08 ### IMAGINATION == 5
                        "{color=#858585}--Не открытое действие-{/color} -" if imagination < 5:
                            call vague_idea
                            jump not_now3
                        "Услуга: \"Трахнись с одноклассником\"" if imagination >= 5:# LEVEL 8
                            jump new_request_30
                        
                        "- Отмена -":
                            jump new_personal_request
                
                
            "- Ничего -":
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
      
###################REQUEST_09 (Level 03) (Show me pussy).###############################################################################################
label new_request_09: #LV.3 (Whoring = 6 - 8)
    $herView.hideQQ()
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
        $herView.hideQQ()
        $ pos = POS_370
        $herView.showQQ( "body_03.png", pos )
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
        ">Гермиона резво соглашается."
        
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
        ">Гермиона резво соглашается."
        
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
                    "- Дать дополнительные баллы -":
                        m "Хорошо..."
                        her "Тогда ладно..."
                        ">Гермиона застегивает свою блузку."
                        $ gryffindor +=10
                        "Гриффиндор получает 10 очков."
                        $ request_21 = True
                    "- Забудь -":
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
        her "В классе я сидела и чувствовала как мои сиськи полностью покрыты спермой. Это просто улет."
             

    
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
                    "- Дать дополнительные баллы -":
                        m "Хорошо..."
                        her "Тогда ладно..."
                        ">Гермиона не трогает свое обкончанное лицо."
                        $ gryffindor +=30
                        "Гриффиндор получает 30 очков."
                        $ request_25 = True
                    "- Забудь -":
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


label could_not_flirt: #Sent here when choose "Задание провалено! Ты не получишь очки!" (Hermione is leaving without getting any points).
    hide screen blkfade
    hide screen bld1
    $herView.hideQ()
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

    if daytime:
        $ hermione_takes_classes = True
    else:
        $ hermione_sleeping = True
    return

label finish_daytime_event:
    call music_block
    
    if daytime:
        $ hermione_takes_classes = True
        jump day_main_menu
    else:
        $ hermione_sleeping = True
        jump night_main_menu
