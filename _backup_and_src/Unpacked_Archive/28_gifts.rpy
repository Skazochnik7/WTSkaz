label giving_skirt:
    $ dress_code = True # Turns TRUE when you gift the miniskirt. Unlocks the "dress code" button.
    $ gifted = True #Prevents you from giving Hermione a several gifts in a row. Turns back to False every night and every morning.
    $ have_miniskirt = False # Turns TRUE when you have the skirt in your possession.
    $ gave_miniskirt = True #Turns True when Hermione has the miniskirt.
    $ days_without_an_event = 0
    hide screen hermione_main                                                                                                                                                                                   #HERMIONE
    with d5
    
    
    $ mad = 0
    m "Вот... Это тебе..."
    $ the_gift = "03_hp/18_store/07.png" # Miniskirt.
    show screen gift
    with d3
    $ renpy.play('sounds/win2.mp3')
    ">Вы дали школьную мини-юбку Гермионе..."
    hide screen gift
    with d3
    hide screen hermione_main                                                                                                                                                                                   #HERMIONE
    with d3                                                                                                                                                                                                                        #HERMIONE
    $ h_xpos=140 #Defines position of the Hermione's full length sprite. (Default 370). (Center: 140)                                                       #HERMIONE
    $ h_body = "03_hp/13_hermione_main/body_01.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
    show screen hermione_main                                                                                                                                                                                 #HERMIONE
    with d3                                                                                                                                                                                                                        #HERMIONE
    her "Хм...? Что это?"
    hide screen hermione_main                                                                                                                                                                                   #HERMIONE
    with d3                                                                                                                                                                                                                        #HERMIONE
    $ h_body = "03_hp/13_hermione_main/body_11.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
    show screen hermione_main                                                                                                                                                                                 #HERMIONE
    with d3                                                                                                                                                                                                                        #HERMIONE
    her "Юбка?"
    hide screen hermione_main                                                                                                                                                                                   #HERMIONE
    with d3                                                                                                                                                                                                                        #HERMIONE
    $ h_body = "03_hp/13_hermione_main/body_06.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
    show screen hermione_main                                                                                                                                                                                 #HERMIONE
    with d3                                                                                                                                                                                                                        #HERMIONE
    her "Спасибо, профессор."
    m "Не стоит благодарности."
    hide screen hermione_main                                                                                                                                                                                 #HERMIONE
    with d3  
    $ renpy.play('sounds/win_04.mp3')   #Not loud.
    show screen notes
    #">\"Dresscode\" option unlocked. From now on you can affect Hermione's attire choices."
    $ h_xpos=370 #Defines position of the Hermione's full length sprite. (Default 370). (Center: 140)                                                       #HERMIONE
    $ h_body = "03_hp/13_hermione_main/body_01.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
    show screen hermione_main                                                                                                                                                                                 #HERMIONE
    jump day_time_requests
    
    
    
### DRESS CODE ###
label mini_on:
    
    
    if whoring >= 0 and whoring <= 5: # Lv 1-2.
        hide screen hermione_main                                                                                                                                                                                   #HERMIONE
        with d3                                                                                                                                                                                                                        #HERMIONE
        $ h_body = "03_hp/13_hermione_main/body_04.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
        show screen hermione_main                                                                                                                                                                                 #HERMIONE
        with d3                                                                                                                                                                                                                        #HERMIONE
        her "Вы вероятно не в серьез, сэр!"
        her "Эта мини юбка?!"
        hide screen hermione_main                                                                                                                                                                                   #HERMIONE
        with d3                                                                                                                                                                                                                        #HERMIONE
        $ h_body = "03_hp/13_hermione_main/body_79.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
        show screen hermione_main                                                                                                                                                                                 #HERMIONE
        with d3                                                                                                                                                                                                                        #HERMIONE
        her "...Она едва прикрывает мои прелести."
        menu:
            m "..."
            "\"Ладно. Забудь.\"":
                hide screen hermione_main                                                                                                                                                                                   #HERMIONE
                with d3                                                                                                                                                                                                                        #HERMIONE
                $ h_body = "03_hp/13_hermione_main/body_66.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
                show screen hermione_main                                                                                                                                                                                 #HERMIONE
                with d3                                                                                                                                                                                                                        #HERMIONE
                her "С удовольствем..."
                hide screen hermione_main                                                                                                                                                                                   #HERMIONE
                with d3                                                                                                                                                                                                                        #HERMIONE
                show screen hermione_main                                                                                                                                                                                 #HERMIONE
                with d3            
                jump day_time_requests
            "\"Я дам тебе 15 очков.\"":
                $ gryffindor +=15
                her "........................"
                her "..............................."
                hide screen hermione_main                                                                                                                                                                                   #HERMIONE
                with d3                                                                                                                                                                                                                        #HERMIONE
                $ h_body = "03_hp/13_hermione_main/body_66.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
                show screen hermione_main                                                                                                                                                                                 #HERMIONE
                with d3                                                                                                                                                                                                                        #HERMIONE
                her "Ну, ладно..."
                hide screen hermione_main                                                                                                                                                                                   #HERMIONE
                with d3                                                                                                                                                                                                                        #HERMIONE
                $ mad += 10
                call upset
        
        

    if whoring >= 6 and whoring <= 11: # Lv 3-4.
        hide screen hermione_main                                                                                                                                                                                   #HERMIONE
        with d3                                                                                                                                                                                                                        #HERMIONE
        $ h_body = "03_hp/13_hermione_main/body_15.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
        show screen hermione_main                                                                                                                                                                                 #HERMIONE
        with d3                                                                                                                                                                                                                        #HERMIONE
        her "Хм...?"
        hide screen hermione_main                                                                                                                                                                                   #HERMIONE
        with d3                                                                                                                                                                                                                        #HERMIONE
        $ h_body = "03_hp/13_hermione_main/body_17.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
        show screen hermione_main                                                                                                                                                                                 #HERMIONE
        with d3                                                                                                                                                                                                                        #HERMIONE
        her "Но она очень короткая..."
        menu:
            m "..."
            "\"Просто надень её!\"":
                hide screen hermione_main                                                                                                                                                                                   #HERMIONE
                with d3                                                                                                                                                                                                                        #HERMIONE
                $ h_body = "03_hp/13_hermione_main/body_07.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
                show screen hermione_main                                                                                                                                                                                 #HERMIONE
                with d3                                                                                                                                                                                                                        #HERMIONE
                her "Сэр, врядли это соответствует форме учеников Хогвартса."
                hide screen hermione_main                                                                                                                                                                                   #HERMIONE
                with d3                                                                                                                                                                                                                        #HERMIONE
                $ h_body = "03_hp/13_hermione_main/body_09.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
                show screen hermione_main                                                                                                                                                                                 #HERMIONE
                with d3                                                                                                                                                                                                                        #HERMIONE
                her "Я отказываюсь!"
                hide screen hermione_main                                                                                                                                                                                   #HERMIONE
                with d3  
                $ mad += 5
                call upset                                                                                                                                                                                                                #HERMIONE
                show screen hermione_main                                                                                                                                                                                 #HERMIONE
                with d3            
                jump day_time_requests
            "\"Я дам тебе 15 очков.\"":
                $ gryffindor +=15
                hide screen hermione_main                                                                                                                                                                                   #HERMIONE
                with d3                                                                                                                                                                                                                        #HERMIONE
                $ h_body = "03_hp/13_hermione_main/body_07.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
                show screen hermione_main                                                                                                                                                                                 #HERMIONE
                with d3                                                                                                                                                                                                                        #HERMIONE
                her "Хм..."
                hide screen hermione_main                                                                                                                                                                                   #HERMIONE
                with d3                                                                                                                                                                                                                        #HERMIONE
                $ h_body = "03_hp/13_hermione_main/body_08.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
                show screen hermione_main                                                                                                                                                                                 #HERMIONE
                with d3                                                                                                                                                                                                                        #HERMIONE
                her "Ну, в таком случае..."
                hide screen hermione_main                                                                                                                                                                                   #HERMIONE
                with d3                                                                                                                                                                                                                        #HERMIONE
                $ h_body = "03_hp/13_hermione_main/body_29.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
                show screen hermione_main                                                                                                                                                                                 #HERMIONE
                with d3                                                                                                                                                                                                                        #HERMIONE
                her "Пока это приносит пользу моему факультету..."
            "\"Ладно. Забудь.\"":
                hide screen hermione_main                                                                                                                                                                                   #HERMIONE
                with d3                                                                                                                                                                                                                        #HERMIONE
                $ h_body = "03_hp/13_hermione_main/body_01.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
                show screen hermione_main                                                                                                                                                                                 #HERMIONE
                with d3                                                                                                                                                                                                                        #HERMIONE
                her "Ладно..."
                hide screen hermione_main                                                                                                                                                                                   #HERMIONE
                with d3                                                                                                                                                                                                                        #HERMIONE
                show screen hermione_main                                                                                                                                                                                 #HERMIONE
                with d3            
                jump day_time_requests

    if whoring >= 12 and whoring <= 17: # Lv 5-6.
        hide screen hermione_main                                                                                                                                                                                   #HERMIONE
        with d3                                                                                                                                                                                                                        #HERMIONE
        $ h_body = "03_hp/13_hermione_main/body_15.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
        show screen hermione_main                                                                                                                                                                                 #HERMIONE
        with d3                                                                                                                                                                                                                        #HERMIONE
        her "Хм...?"
        hide screen hermione_main                                                                                                                                                                                   #HERMIONE
        with d3                                                                                                                                                                                                                        #HERMIONE
        $ h_body = "03_hp/13_hermione_main/body_17.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
        show screen hermione_main                                                                                                                                                                                 #HERMIONE
        with d3                                                                                                                                                                                                                        #HERMIONE
        her "Но она очень короткая..."
        menu:
            m "..."
            "\"Просто надень ее!\"":
                hide screen hermione_main                                                                                                                                                                                   #HERMIONE
                with d3                                                                                                                                                                                                                        #HERMIONE
                $ h_body = "03_hp/13_hermione_main/body_69.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
                show screen hermione_main                                                                                                                                                                                 #HERMIONE
                with d3                                                                                                                                                                                                                        #HERMIONE
                her "Ладно, ладно..."
            "\"Я дам тебе 15 очков.\"":
                $ gryffindor +=15
                hide screen hermione_main                                                                                                                                                                                   #HERMIONE
                with d3                                                                                                                                                                                                                        #HERMIONE
                $ h_body = "03_hp/13_hermione_main/body_07.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
                show screen hermione_main                                                                                                                                                                                 #HERMIONE
                with d3                                                                                                                                                                                                                        #HERMIONE
                her "Хм..."
                hide screen hermione_main                                                                                                                                                                                   #HERMIONE
                with d3                                                                                                                                                                                                                        #HERMIONE
                $ h_body = "03_hp/13_hermione_main/body_68.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
                show screen hermione_main                                                                                                                                                                                 #HERMIONE
                with d3                                                                                                                                                                                                                        #HERMIONE
                her "Ладно, я не против."
            "\"Ладно. Забудь\"":
                hide screen hermione_main                                                                                                                                                                                   #HERMIONE
                with d3                                                                                                                                                                                                                        #HERMIONE
                $ h_body = "03_hp/13_hermione_main/body_13.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
                show screen hermione_main                                                                                                                                                                                 #HERMIONE
                with d3                                                                                                                                                                                                                        #HERMIONE
                her "Ох..."
                hide screen hermione_main                                                                                                                                                                                   #HERMIONE
                with d3                                                                                                                                                                                                                        #HERMIONE
                show screen hermione_main                                                                                                                                                                                 #HERMIONE
                with d3            
                jump day_time_requests
        


    
    if whoring >= 18: # Lv 7+
        hide screen hermione_main                                                                                                                                                                                   #HERMIONE
        with d3                                                                                                                                                                                                                        #HERMIONE
        $ h_body = "03_hp/13_hermione_main/body_118.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
        show screen hermione_main                                                                                                                                                                                 #HERMIONE
        with d3                                                                                                                                                                                                                        #HERMIONE
        her "Слушаюсь, сэр..."
        hide screen hermione_main                                                                                                                                                                                   #HERMIONE
        with d3                                                                                                                                                                                                                        #HERMIONE
        $ h_body = "03_hp/13_hermione_main/body_78.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
                                                                                                                                                                                                                          #HERMIONE
    
    
    $ legs_02 = True
    
    show screen blkfade
    with d3
    $ renpy.play('sounds/door.mp3') #Sound of a door opening.
    pause 2
    $ renpy.play('sounds/door.mp3') #Sound of a door opening.
    pause.3
    hide screen blkfade
    with d3
    show screen hermione_main                                                                                                                                                                                 #HERMIONE
    with d3                                                                                                                                                                                                                        #HERMIONE
    jump day_time_requests
    
    
label mini_off:
    if whoring >= 0 and whoring <= 5: # Lv 1-2.
        hide screen hermione_main                                                                                                                                                                                   #HERMIONE
        with d3                                                                                                                                                                                                                        #HERMIONE
        $ h_body = "03_hp/13_hermione_main/body_04.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
        show screen hermione_main                                                                                                                                                                                 #HERMIONE
        with d3                                                                                                                                                                                                                        #HERMIONE
        her "Я рада, что вы попросили меня об этом. "
        hide screen hermione_main                                                                                                                                                                                   #HERMIONE
        with d3                                                                                                                                                                                                                        #HERMIONE
        $ h_body = "03_hp/13_hermione_main/body_03.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE 
        
    if whoring >= 6 and whoring <= 11: # Lv 3-4.
        hide screen hermione_main                                                                                                                                                                                   #HERMIONE
        with d3                                                                                                                                                                                                                        #HERMIONE
        $ h_body = "03_hp/13_hermione_main/body_01.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
        show screen hermione_main                                                                                                                                                                                 #HERMIONE
        with d3                                                                                                                                                                                                                        #HERMIONE
        her "С удовольствем, сэр."

    if whoring >= 12 and whoring <= 17: # Lv 5-6.
        hide screen hermione_main                                                                                                                                                                                   #HERMIONE
        with d3                                                                                                                                                                                                                        #HERMIONE
        $ h_body = "03_hp/13_hermione_main/body_13.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
        show screen hermione_main                                                                                                                                                                                 #HERMIONE
        with d3                                                                                                                                                                                                                        #HERMIONE
        her "Хорошо..."
    
    if whoring >= 18: # Lv 7+
        hide screen hermione_main                                                                                                                                                                                   #HERMIONE
        with d3                                                                                                                                                                                                                        #HERMIONE
        $ h_body = "03_hp/13_hermione_main/body_28.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
        show screen hermione_main                                                                                                                                                                                 #HERMIONE
        with d3                                                                                                                                                                                                                        #HERMIONE
        her "Опять эта скукотища?"
    
    
    $ legs_02 = False
    
    show screen blkfade
    with d3
    $ renpy.play('sounds/door.mp3') #Sound of a door opening.
    pause 2
    $ renpy.play('sounds/door.mp3') #Sound of a door opening.
    pause.3
    hide screen blkfade
    with d3
    jump day_time_requests
   
    
    
label badge_put:
    hide screen hermione_main                                                                                                                                                                                   #HERMIONE
    with d3                                                                                                                                                                                                                        #HERMIONE
    $ h_body = "03_hp/13_hermione_main/body_01.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
    show screen hermione_main                                                                                                                                                                                 #HERMIONE
    with d3                                                                                                                                                                                                                        #HERMIONE
    her "Конечно, сэр..."
    
    $ badges = True
    $ ba_01 = True
    
    show screen blkfade
    with d3
    $ renpy.play('sounds/door.mp3') #Sound of a door opening.
    pause 2
    $ renpy.play('sounds/door.mp3') #Sound of a door opening.
    pause.3
    hide screen blkfade
    with d3
    jump day_time_requests
    
    
label badge_take:
    hide screen hermione_main                                                                                                                                                                                   #HERMIONE
    with d3                                                                                                                                                                                                                        #HERMIONE
    $ h_body = "03_hp/13_hermione_main/body_01.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
    show screen hermione_main                                                                                                                                                                                 #HERMIONE
    with d3                                                                                                                                                                                                                        #HERMIONE
    her "Как пожелаете, сэр..."
    $ badges = False
    $ ba_01 = False
    
    show screen blkfade
    with d3
    $ renpy.play('sounds/door.mp3') #Sound of a door opening.
    pause 2
    $ renpy.play('sounds/door.mp3') #Sound of a door opening.
    pause.3
    hide screen blkfade
    with d3
    jump day_time_requests
    
    
### FISHNETS ###
label nets_put:
    if whoring >= 0 and whoring <= 5: # Lv 1-2.
        hide screen hermione_main                                                                                                                                                                                   #HERMIONE
        with d3                                                                                                                                                                                                                        #HERMIONE
        $ h_body = "03_hp/13_hermione_main/body_11.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
        show screen hermione_main                                                                                                                                                                                 #HERMIONE
        with d3                                                                                                                                                                                                                        #HERMIONE
        her "Ажурные чулки...?"
        hide screen hermione_main                                                                                                                                                                                   #HERMIONE
        with d3                                                                                                                                                                                                                        #HERMIONE
        $ h_body = "03_hp/13_hermione_main/body_31.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
        show screen hermione_main                                                                                                                                                                                 #HERMIONE
        with d3                                                                                                                                                                                                                        #HERMIONE
        her "Вы должно быть не серьезно, сэр!"
        menu:
            m "..."
            "\"Ладно. Забудь.\"":
                hide screen hermione_main                                                                                                                                                                                   #HERMIONE
                with d3                                                                                                                                                                                                                        #HERMIONE
                $ h_body = "03_hp/13_hermione_main/body_69.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
                show screen hermione_main                                                                                                                                                                                 #HERMIONE
                with d3                                                                                                                                                                                                                        #HERMIONE
                her "С радостью..."
                hide screen hermione_main                                                                                                                                                                                   #HERMIONE
                with d3                                                                                                                                                                                                                        #HERMIONE
                show screen hermione_main                                                                                                                                                                                 #HERMIONE
                with d3            
                jump day_time_requests
            "\"Я дам тебе 15 очков.\"":
                $ gryffindor +=15
                her "........................"
                her "..............................."
                hide screen hermione_main                                                                                                                                                                                   #HERMIONE
                with d3                                                                                                                                                                                                                        #HERMIONE
                $ h_body = "03_hp/13_hermione_main/body_66.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
                show screen hermione_main                                                                                                                                                                                 #HERMIONE
                with d3                                                                                                                                                                                                                        #HERMIONE
                her "Ну, хорошо..."
                hide screen hermione_main                                                                                                                                                                                   #HERMIONE
                with d3                                                                                                                                                                                                                        #HERMIONE
                $ mad += 5
                call upset
        
    if whoring >= 6 and whoring <= 11: # Lv 3-4.
        hide screen hermione_main                                                                                                                                                                                   #HERMIONE
        with d3                                                                                                                                                                                                                        #HERMIONE
        $ h_body = "03_hp/13_hermione_main/body_15.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
        show screen hermione_main                                                                                                                                                                                 #HERMIONE
        with d3                                                                                                                                                                                                                        #HERMIONE
        her "Хм...?"
        hide screen hermione_main                                                                                                                                                                                   #HERMIONE
        with d3                                                                                                                                                                                                                        #HERMIONE
        $ h_body = "03_hp/13_hermione_main/body_17.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
        show screen hermione_main                                                                                                                                                                                 #HERMIONE
        with d3                                                                                                                                                                                                                        #HERMIONE
        her "Я не из таких девушек, сэр..."
        her "Попытайте удачу с одной из \"Слизеринских\" шлюх..."
        menu:
            m "..."
            "\"Просто надень это!\"":
                hide screen hermione_main                                                                                                                                                                                   #HERMIONE
                with d3                                                                                                                                                                                                                        #HERMIONE
                $ h_body = "03_hp/13_hermione_main/body_07.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
                show screen hermione_main                                                                                                                                                                                 #HERMIONE
                with d3                                                                                                                                                                                                                        #HERMIONE
                her "Сэр, это врядли соответствует форме студента Хогвартса."
                hide screen hermione_main                                                                                                                                                                                   #HERMIONE
                with d3                                                                                                                                                                                                                        #HERMIONE
                $ h_body = "03_hp/13_hermione_main/body_09.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
                show screen hermione_main                                                                                                                                                                                 #HERMIONE
                with d3                                                                                                                                                                                                                        #HERMIONE
                her "Я отказываюсь!"
                hide screen hermione_main                                                                                                                                                                                   #HERMIONE
                with d3  
                $ mad += 5
                call upset                                                                                                                                                                                                                #HERMIONE
                show screen hermione_main                                                                                                                                                                                 #HERMIONE
                with d3            
                jump day_time_requests
            "\"Я дам тебе 15 очков.\"":
                $ gryffindor +=15
                hide screen hermione_main                                                                                                                                                                                   #HERMIONE
                with d3                                                                                                                                                                                                                        #HERMIONE
                $ h_body = "03_hp/13_hermione_main/body_07.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
                show screen hermione_main                                                                                                                                                                                 #HERMIONE
                with d3                                                                                                                                                                                                                        #HERMIONE
                her "Хм..."
                hide screen hermione_main                                                                                                                                                                                   #HERMIONE
                with d3                                                                                                                                                                                                                        #HERMIONE
                $ h_body = "03_hp/13_hermione_main/body_08.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
                show screen hermione_main                                                                                                                                                                                 #HERMIONE
                with d3                                                                                                                                                                                                                        #HERMIONE
                her "Ну, раз так..."
                hide screen hermione_main                                                                                                                                                                                   #HERMIONE
                with d3                                                                                                                                                                                                                        #HERMIONE
                $ h_body = "03_hp/13_hermione_main/body_29.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
                show screen hermione_main                                                                                                                                                                                 #HERMIONE
                with d3                                                                                                                                                                                                                        #HERMIONE
                her "Пока это приносит пользу моему факультету..."
            "\"Ладно. Забудь\"":
                hide screen hermione_main                                                                                                                                                                                   #HERMIONE
                with d3                                                                                                                                                                                                                        #HERMIONE
                $ h_body = "03_hp/13_hermione_main/body_01.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
                show screen hermione_main                                                                                                                                                                                 #HERMIONE
                with d3                                                                                                                                                                                                                        #HERMIONE
                her "Ладно..."
                hide screen hermione_main                                                                                                                                                                                   #HERMIONE
                with d3                                                                                                                                                                                                                        #HERMIONE
                show screen hermione_main                                                                                                                                                                                 #HERMIONE
                with d3            
                jump day_time_requests

    if whoring >= 12 and whoring <= 17: # Lv 5-6.
        hide screen hermione_main                                                                                                                                                                                   #HERMIONE
        with d3                                                                                                                                                                                                                        #HERMIONE
        $ h_body = "03_hp/13_hermione_main/body_15.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
        show screen hermione_main                                                                                                                                                                                 #HERMIONE
        with d3                                                                                                                                                                                                                        #HERMIONE
        her "Хм...?"
        hide screen hermione_main                                                                                                                                                                                   #HERMIONE
        with d3                                                                                                                                                                                                                        #HERMIONE
        $ h_body = "03_hp/13_hermione_main/body_17.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
        show screen hermione_main                                                                                                                                                                                 #HERMIONE
        with d3                                                                                                                                                                                                                        #HERMIONE
        her "Ажурные чулки?"
        hide screen hermione_main                                                                                                                                                                                   #HERMIONE
        with d3                                                                                                                                                                                                                        #HERMIONE
        $ h_body = "03_hp/13_hermione_main/body_29.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
        show screen hermione_main                                                                                                                                                                                 #HERMIONE
        with d3                                                                                                                                                                                                                        #HERMIONE
        her "Я не уверена насчет этого, сэр..."
        menu:
            m "..."
            "\"Просто надень их!\"":
                hide screen hermione_main                                                                                                                                                                                   #HERMIONE
                with d3                                                                                                                                                                                                                        #HERMIONE
                $ h_body = "03_hp/13_hermione_main/body_69.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
                show screen hermione_main                                                                                                                                                                                 #HERMIONE
                with d3                                                                                                                                                                                                                        #HERMIONE
                her "Ладно, Ладно..."
            "\"Я дам тебе 15 очков.\"":
                $ gryffindor +=15
                hide screen hermione_main                                                                                                                                                                                   #HERMIONE
                with d3                                                                                                                                                                                                                        #HERMIONE
                $ h_body = "03_hp/13_hermione_main/body_07.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
                show screen hermione_main                                                                                                                                                                                 #HERMIONE
                with d3                                                                                                                                                                                                                        #HERMIONE
                her "Хм..."
                hide screen hermione_main                                                                                                                                                                                   #HERMIONE
                with d3                                                                                                                                                                                                                        #HERMIONE
                $ h_body = "03_hp/13_hermione_main/body_68.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
                show screen hermione_main                                                                                                                                                                                 #HERMIONE
                with d3                                                                                                                                                                                                                        #HERMIONE
                her "Ладно, я не против."
            "\"Ладно. Забудь\"":
                hide screen hermione_main                                                                                                                                                                                   #HERMIONE
                with d3                                                                                                                                                                                                                        #HERMIONE
                $ h_body = "03_hp/13_hermione_main/body_13.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
                show screen hermione_main                                                                                                                                                                                 #HERMIONE
                with d3                                                                                                                                                                                                                        #HERMIONE
                her "Ох..."
                hide screen hermione_main                                                                                                                                                                                   #HERMIONE
                with d3                                                                                                                                                                                                                        #HERMIONE
                show screen hermione_main                                                                                                                                                                                 #HERMIONE
                with d3            
                jump day_time_requests
        

    
    if whoring >= 18: # Lv 7+
        hide screen hermione_main                                                                                                                                                                                   #HERMIONE
        with d3                                                                                                                                                                                                                        #HERMIONE
        $ h_body = "03_hp/13_hermione_main/body_118.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
        show screen hermione_main                                                                                                                                                                                 #HERMIONE
        with d3                                                                                                                                                                                                                        #HERMIONE
        her "Если вы настаиваете, сэр..."
        hide screen hermione_main                                                                                                                                                                                   #HERMIONE
        with d3                                                                                                                                                                                                                        #HERMIONE
        $ h_body = "03_hp/13_hermione_main/body_78.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
                                                                                                                                                                                                                          #HERMIONE
    
     
    $ ne = True # Shows fishnets layer.
    $ ne_01 = True # Shows the fishnets.
    
    #$ legs_02 = True
    
    show screen blkfade
    with d3
    $ renpy.play('sounds/door.mp3') #Sound of a door opening.
    pause 2
    $ renpy.play('sounds/door.mp3') #Sound of a door opening.
    pause.3
    hide screen blkfade
    with d3
    pause.1
    show screen hermione_main                                                                                                                                                                                 #HERMIONE
    with d3                                                                                                                                                                                                                        #HERMIONE
    jump day_time_requests
    
    
label nets_take:
    if whoring >= 0 and whoring <= 5: # Lv 1-2.
        hide screen hermione_main                                                                                                                                                                                   #HERMIONE
        with d3                                                                                                                                                                                                                        #HERMIONE
        $ h_body = "03_hp/13_hermione_main/body_04.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
        show screen hermione_main                                                                                                                                                                                 #HERMIONE
        with d3                                                                                                                                                                                                                        #HERMIONE
        her "Я рада, что вы приняли это решение, сэр."
        hide screen hermione_main                                                                                                                                                                                   #HERMIONE
        with d3                                                                                                                                                                                                                        #HERMIONE
        $ h_body = "03_hp/13_hermione_main/body_03.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE 
        
    if whoring >= 6 and whoring <= 11: # Lv 3-4.
        hide screen hermione_main                                                                                                                                                                                   #HERMIONE
        with d3                                                                                                                                                                                                                        #HERMIONE
        $ h_body = "03_hp/13_hermione_main/body_01.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
        show screen hermione_main                                                                                                                                                                                 #HERMIONE
        with d3                                                                                                                                                                                                                        #HERMIONE
        her "С удовольствием, сэр."

    if whoring >= 12 and whoring <= 17: # Lv 5-6.
        hide screen hermione_main                                                                                                                                                                                   #HERMIONE
        with d3                                                                                                                                                                                                                        #HERMIONE
        $ h_body = "03_hp/13_hermione_main/body_12.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
        show screen hermione_main                                                                                                                                                                                 #HERMIONE
        with d3                                                                                                                                                                                                                        #HERMIONE
        her "Как пожелаете, сэр."
    
    if whoring >= 18: # Lv 7+
        hide screen hermione_main                                                                                                                                                                                   #HERMIONE
        with d3                                                                                                                                                                                                                        #HERMIONE
        $ h_body = "03_hp/13_hermione_main/body_28.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
        show screen hermione_main                                                                                                                                                                                 #HERMIONE
        with d3                                                                                                                                                                                                                        #HERMIONE
        her "Правда? Ой..."
    
    
    $ ne = False # Shows fishnets layer.
    $ ne_01 = False # Shows the fishnets.
    #$ legs_02 = False
    
    show screen blkfade
    with d3
    $ renpy.play('sounds/door.mp3') #Sound of a door opening.
    pause 2
    $ renpy.play('sounds/door.mp3') #Sound of a door opening.
    pause.3
    hide screen blkfade
    with d3
    show screen hermione_main
    with d3
    jump day_time_requests
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
       
label giving_lube: # JAR OF Анальный лубрикант.
    hide screen hermione_main                                                                                                                                                                                   #HERMIONE
    with d5                                                                                                                                                                                                                        #HERMIONE
    $ h_xpos=140 #Defines position of the Hermione's full length sprite. (Default 370). (Center: 140)                                                       #HERMIONE
    
    if whoring >= 0 and whoring <= 5: # Lv 1-2.
        $ mad += 6
        $ h_body = "03_hp/13_hermione_main/body_02.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
        show screen hermione_main                                                                                                                                                                                 #HERMIONE
        with d5                                                                                                                                                                                                                        #HERMIONE
        her "Я не знаю, что это..."
        hide screen hermione_main                                                                                                                                                                                   #HERMIONE
        with d3                                                                                                                                                                                                                        #HERMIONE
        $ h_body = "03_hp/13_hermione_main/body_05.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
        show screen hermione_main                                                                                                                                                                                 #HERMIONE
        with d3                                                                                                                                                                                                                        #HERMIONE
        her "Но мне кажется, что эта банка полна чего-то мерзкого и противного..."
        her "Нет, спасибо, сэр."
        hide screen hermione_main                                                                                                                                                                                   #HERMIONE
        with d3                                                                                                                                                                                                                        #HERMIONE
        call upset #Message saying that Hermione became upset with you.
        $ h_body = "03_hp/13_hermione_main/body_03.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
       
        
        
    if whoring >= 6 and whoring <= 11: # Lv 3-4.
        $ mad += 2
        $ h_body = "03_hp/13_hermione_main/body_73.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
        show screen hermione_main                                                                                                                                                                                 #HERMIONE
        with d5                                                                                                                                                                                                                        #HERMIONE
        her "Хм..."
        hide screen hermione_main                                                                                                                                                                                   #HERMIONE
        with d3                                                                                                                                                                                                                        #HERMIONE
        $ h_body = "03_hp/13_hermione_main/body_66.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
        show screen hermione_main                                                                                                                                                                                 #HERMIONE
        with d3                                                                                                                                                                                                                        #HERMIONE
        her "Мне кажется, я знаю, что это такое..."
        her "Но почему бы вам дать что-то вроде этого одному из ваших учеников, сэр?"
        hide screen hermione_main                                                                                                                                                                                   #HERMIONE
        with d3                                                                                                                                                                                                                        #HERMIONE
        $ h_body = "03_hp/13_hermione_main/body_69.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
        show screen hermione_main                                                                                                                                                                                 #HERMIONE
        with d3                                                                                                                                                                                                                        #HERMIONE
        her "Нет, спасибо."
        hide screen hermione_main                                                                                                                                                                                   #HERMIONE
        with d3                                                                                                                                                                                                                        #HERMIONE
        call upset #Message saying that Hermione became upset with you.
   
        
    if whoring >= 12 and whoring <= 17: # Lv 5-6.
        $ anal_lube -= 1
        $ h_body = "03_hp/13_hermione_main/body_118.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
        show screen hermione_main                                                                                                                                                                                 #HERMIONE
        with d5                                                                                                                                                                                                                        #HERMIONE
        her "Анальный лубрикант?"
        hide screen hermione_main                                                                                                                                                                                   #HERMIONE
        with d3                                                                                                                                                                                                                        #HERMIONE
        $ h_body = "03_hp/13_hermione_main/body_189.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
        show screen hermione_main                                                                                                                                                                                 #HERMIONE
        with d3                                                                                                                                                                                                                        #HERMIONE
        her "Эм...ну...я знаю девочку..."
        her "То есть не знаю, она подруга моей подруги..."
        her "Да, я передам это ей..."
        hide screen hermione_main                                                                                                                                                                                   #HERMIONE
        with d3                                                                                                                                                                                                                        #HERMIONE
        $ the_gift = "03_hp/18_store/09.png" # Анальный лубрикант
        show screen gift
        with d3
        ">Вы даете банку Гермионе..."
        hide screen gift
        with d3
        hide screen hermione_main                                                                                                                                                                                   #HERMIONE
        with d3                                                                                                                                                                                                                        #HERMIONE
        $ h_body = "03_hp/13_hermione_main/body_186.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
        show screen hermione_main                                                                                                                                                                                 #HERMIONE
        with d3                                                                                                                                                                                                                        #HERMIONE
        her "Тем не менее, я думаю, вы не должны дарить такие подарки, вроде этого, вашим ученикам, сэр."
        hide screen hermione_main                                                                                                                                                                                   #HERMIONE
        with d3                                                                                                                                                                                                                        #HERMIONE
        call no_change #Message: Hermione's mood did not change.
        $ h_body = "03_hp/13_hermione_main/body_79.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
        
    if whoring >= 18: # Lv 7+  
        $ anal_lube -= 1
        $ mad -=5
        $ h_body = "03_hp/13_hermione_main/body_124.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
        show screen hermione_main                                                                                                                                                                                 #HERMIONE
        with d5    
        her "Анальный лубрикант, сэр?"
        hide screen hermione_main                                                                                                                                                                                   #HERMIONE
        with d3                                                                                                                                                                                                                        #HERMIONE
        $ h_body = "03_hp/13_hermione_main/body_186.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
        show screen hermione_main                                                                                                                                                                                 #HERMIONE
        with d3                                                                                                                                                                                                                        #HERMIONE
        her "Я знаю пару девушек, которые могли бы сделать что-нибудь с этим."
        hide screen hermione_main                                                                                                                                                                                   #HERMIONE
        with d3                                                                                                                                                                                                                        #HERMIONE
        $ h_body = "03_hp/13_hermione_main/body_128.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
        show screen hermione_main                                                                                                                                                                                 #HERMIONE
        with d3                                                                                                                                                                                                                        #HERMIONE
        her "Спасибо, что присматриваете за нами, сэр."
        hide screen hermione_main                                                                                                                                                                                   #HERMIONE
        with d3    
        call happy #Message that says that Hermione's mood has improved.
 
    $ h_xpos=370 #Defines position of the Hermione's full length sprite. (Default 370). (Center: 140)                                                       #HERMIONE
    show screen hermione_main                                                                                                                                                                                 #HERMIONE
    with d3                                                                                                                                                                                                                        #HERMIONE
    jump day_time_requests
        
        
        
        
label giving_condoms: # A PACK OF CONDOMS
    hide screen hermione_main                                                                                                                                                                                   #HERMIONE
    with d5                                                                                                                                                                                                                        #HERMIONE
    $ h_xpos=140 #Defines position of the Hermione's full length sprite. (Default 370). (Center: 140)                                                       #HERMIONE
    
    if whoring >= 0 and whoring <= 5: # Lv 1-2.
        $ mad += 6
        $ h_body = "03_hp/13_hermione_main/body_18.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
        show screen hermione_main                                                                                                                                                                                 #HERMIONE
        with d5                                                                                                                                                                                                                        #HERMIONE
        her "Презервативы?!"
        hide screen hermione_main                                                                                                                                                                                   #HERMIONE
        with d3                                                                                                                                                                                                                        #HERMIONE
        $ h_body = "03_hp/13_hermione_main/body_30.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
        show screen hermione_main                                                                                                                                                                                 #HERMIONE
        with d3                                                                                                                                                                                                                        #HERMIONE
        her "Сэр, я даже не знаю, что с этим делать..."
        hide screen hermione_main                                                                                                                                                                                   #HERMIONE
        with d3                                                                                                                                                                                                                        #HERMIONE
        call upset #Message saying that Hermione became upset with you.
        $ h_body = "03_hp/13_hermione_main/body_03.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
       
        
        
    if whoring >= 6 and whoring <= 11: # Lv 3-4.
        $ h_body = "03_hp/13_hermione_main/body_07.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
        show screen hermione_main                                                                                                                                                                                 #HERMIONE
        with d5                                                                                                                                                                                                                        #HERMIONE
        her "...Презервативы?"
        hide screen hermione_main                                                                                                                                                                                   #HERMIONE
        with d3                                                                                                                                                                                                                        #HERMIONE
        $ h_body = "03_hp/13_hermione_main/body_04.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
        show screen hermione_main                                                                                                                                                                                 #HERMIONE
        with d3                                                                                                                                                                                                                        #HERMIONE
        her "Эм... Является ли это частью какой-то новой обучающей программы Хогвартса? Вроде сексуальное развитие или вроде того?"
        hide screen hermione_main                                                                                                                                                                                   #HERMIONE
        with d3                                                                                                                                                                                                                        #HERMIONE
        $ h_body = "03_hp/13_hermione_main/body_189.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
        show screen hermione_main                                                                                                                                                                                 #HERMIONE
        with d3                                                                                                                                                                                                                        #HERMIONE
        her "Нет, сэр ... Мне кажется, что неправильно принимать этот подарок от вас..."
        hide screen hermione_main                                                                                                                                                                                   #HERMIONE
        with d3                                                                                                                                                                                                                        #HERMIONE
        call no_change 
   
        
    if whoring >= 12 and whoring <= 17: # Lv 5-6.
        $ condoms -= 1
        $ mad -= 3
        $ h_body = "03_hp/13_hermione_main/body_03.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
        show screen hermione_main                                                                                                                                                                                 #HERMIONE
        with d5                                                                                                                                                                                                                        #HERMIONE
        her "Пачка презервативов?"
        her "Сэр, как мне использовать их?"
        hide screen hermione_main                                                                                                                                                                                   #HERMIONE
        with d3                                                                                                                                                                                                                        #HERMIONE
        $ h_body = "03_hp/13_hermione_main/body_04.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
        show screen hermione_main                                                                                                                                                                                 #HERMIONE
        with d3                                                                                                                                                                                                                        #HERMIONE
        her "Ну, я приму их, только потому, что невежливо отказываться от подарка..."
        hide screen hermione_main                                                                                                                                                                                   #HERMIONE
        with d3    
        $ the_gift = "03_hp/18_store/10.png" # CONDOMS
        show screen gift
        with d3
        ">Вы даете Гермионе пачку презервативов..."
        hide screen gift
        with d3
        call happy #Message that says that Hermione's mood has improved.
        $ h_body = "03_hp/13_hermione_main/body_29.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
        

        
    if whoring >= 18: # Lv 7+  
        $ anal_lube -= 1
        $ mad -=4
        $ h_body = "03_hp/13_hermione_main/body_08.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
        show screen hermione_main                                                                                                                                                                                 #HERMIONE
        with d5    
        her "Пачка презервативов?"
        hide screen hermione_main                                                                                                                                                                                   #HERMIONE
        with d3                                                                                                                                                                                                                        #HERMIONE
        $ h_body = "03_hp/13_hermione_main/body_128.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
        show screen hermione_main                                                                                                                                                                                 #HERMIONE
        with d3                                                                                                                                                                                                                        #HERMIONE
        her "Я ценю вашу заботу, сэр. Спасибо."
        hide screen hermione_main                                                                                                                                                                                   #HERMIONE
        with d3    
        $ the_gift = "03_hp/18_store/10.png" # CONDOMS
        show screen gift
        with d3
        ">Вы даете пачку презервативов Гермионе..."
        hide screen gift
        with d3
        call happy #Message that says that Hermione's mood has improved.
        $ h_body = "03_hp/13_hermione_main/body_45.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
 
    $ h_xpos=370 #Defines position of the Hermione's full length sprite. (Default 370). (Center: 140)                                                       #HERMIONE
    show screen hermione_main                                                                                                                                                                                 #HERMIONE
    with d3                                                                                                                                                                                                                        #HERMIONE
    jump day_time_requests
        
        
     
     
     
### CANDY ###
label giving_candy: # CANDY.
    hide screen hermione_main                                                                                                                                                                                   #HERMIONE
    with d5                                                                                                                                                                                                                        #HERMIONE
    $ h_xpos=140 #Defines position of the Hermione's full length sprite. (Default 370). (Center: 140)                                                       #HERMIONE
    
    if whoring >= 0 and whoring <= 5: # Lv 1-2.
        $ mad -= 5
        $ candy -= 1
        $ h_body = "03_hp/13_hermione_main/body_01.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
        show screen hermione_main                                                                                                                                                                                 #HERMIONE
        with d5                                                                                                                                                                                                                        #HERMIONE
        her "Конфета?"
        hide screen hermione_main                                                                                                                                                                                   #HERMIONE
        with d3    
        $ the_gift = "03_hp/18_store/11.png" # CANDY
        show screen gift
        with d3
        ">Вы даете конфету Гермионе..."
        hide screen gift
        with d3
        $ h_body = "03_hp/13_hermione_main/body_06.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
        show screen hermione_main                                                                                                                                                                                 #HERMIONE
        with d3                                                                                                                                                                                                                        #HERMIONE
        her "Спасибо, сэр."
        call happy #Message that says that Hermione's mood has improved.

    if whoring >= 6 and whoring <= 11: # Lv 3-4.
        $ mad -= 5
        $ candy -= 1
        $ h_body = "03_hp/13_hermione_main/body_03.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
        show screen hermione_main                                                                                                                                                                                 #HERMIONE
        with d5                                                                                                                                                                                                                        #HERMIONE
        her "Конфета?"
        hide screen hermione_main                                                                                                                                                                                   #HERMIONE
        with d3                                                                                                                                                                                                                        #HERMIONE
        $ h_body = "03_hp/13_hermione_main/body_02.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
        show screen hermione_main                                                                                                                                                                                 #HERMIONE
        with d3                                                                                                                                                                                                                        #HERMIONE
        her "Конфеты для детей, сэр."
        hide screen hermione_main                                                                                                                                                                                   #HERMIONE
        with d3    
        $ the_gift = "03_hp/18_store/11.png" # CANDY
        show screen gift
        with d3
        ">Вы даете конфету Гермионе..."
        hide screen gift
        with d3
        $ h_body = "03_hp/13_hermione_main/body_29.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
        show screen hermione_main                                                                                                                                                                                 #HERMIONE
        with d3                                                                                                                                                                                                                        #HERMIONE
        her "Спасибо вам..."
        call happy #Message that says that Hermione's mood has improved.
        $ h_body = "03_hp/13_hermione_main/body_06.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
        

        
    if whoring >= 12 and whoring <= 17: # Lv 5-6.
        $ mad -= 5
        $ candy -= 1
        $ h_body = "03_hp/13_hermione_main/body_03.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
        show screen hermione_main                                                                                                                                                                                 #HERMIONE
        with d5                                                                                                                                                                                                                        #HERMIONE
        her "Конфета?"
        hide screen hermione_main                                                                                                                                                                                   #HERMIONE
        with d3    
        $ the_gift = "03_hp/18_store/11.png" # CANDY
        show screen gift
        with d3
        ">Вы даете конфету Гермионе..."
        hide screen gift
        with d3
        $ h_body = "03_hp/13_hermione_main/body_08.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
        show screen hermione_main                                                                                                                                                                                 #HERMIONE
        with d3                                                                                                                                                                                                                        #HERMIONE
        her "Eм... Конечно, спасибо..."
        call happy #Message that says that Hermione's mood has improved.
        $ h_body = "03_hp/13_hermione_main/body_06.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
 
        
    if whoring >= 18: # Lv 7+  
        $ candy -= 1
        $ mad -=5
        $ h_body = "03_hp/13_hermione_main/body_06.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
        show screen hermione_main                                                                                                                                                                                 #HERMIONE
        with d5    
        her "Конфета?"
        hide screen hermione_main                                                                                                                                                                                   #HERMIONE
        with d3                                                                                                                                                                                                                        #HERMIONE
        $ h_body = "03_hp/13_hermione_main/body_46.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
        show screen hermione_main                                                                                                                                                                                 #HERMIONE
        with d3                                                                                                                                                                                                                        #HERMIONE
        her "Умные девушки используют конфеты как \"орудие\"."
        hide screen hermione_main                                                                                                                                                                                   #HERMIONE
        with d3    
        $ the_gift = "03_hp/18_store/11.png" # CANDY
        show screen gift
        with d3
        ">Вы даете конфету Гермионе..."
        hide screen gift
        with d3
        $ h_body = "03_hp/13_hermione_main/body_74.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
        show screen hermione_main                                                                                                                                                                                 #HERMIONE
        with d3                                                                                                                                                                                                                        #HERMIONE  
        her "Спасибо, сэр."
        call happy #Message that says that Hermione's mood has improved.
        $ h_body = "03_hp/13_hermione_main/body_128.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
 
    $ h_xpos=370 #Defines position of the Hermione's full length sprite. (Default 370). (Center: 140)                                                       #HERMIONE
    show screen hermione_main                                                                                                                                                                                 #HERMIONE
    with d3                                                                                                                                                                                                                        #HERMIONE
    jump day_time_requests
    
        
        
        

### CHOCOLATE ###
label giving_chocolate: # CHOCOLATE.
    hide screen hermione_main                                                                                                                                                                                   #HERMIONE
    with d5                                                                                                                                                                                                                        #HERMIONE
    $ h_xpos=140 #Defines position of the Hermione's full length sprite. (Default 370). (Center: 140)                                                       #HERMIONE
    
    if whoring >= 0 and whoring <= 5: # Lv 1-2.
        $ mad -= 10
        $ chocolate -= 1
        $ h_body = "03_hp/13_hermione_main/body_01.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
        show screen hermione_main                                                                                                                                                                                 #HERMIONE
        with d5                                                                                                                                                                                                                        #HERMIONE
        her "Плитка шоколада?"
        hide screen hermione_main                                                                                                                                                                                   #HERMIONE
        with d3    
        $ the_gift = "03_hp/18_store/12.png" # CHOCOLATE
        show screen gift
        with d3
        ">Вы даете Гермионе плитку шоколада..."
        hide screen gift
        with d3
        $ h_body = "03_hp/13_hermione_main/body_06.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
        show screen hermione_main                                                                                                                                                                                 #HERMIONE
        with d3                                                                                                                                                                                                                        #HERMIONE
        her "Спасибо, сэр."
        call happy #Message that says that Hermione's mood has improved.

    if whoring >= 6 and whoring <= 11: # Lv 3-4.
        $ mad -= 10
        $ chocolate -= 1
        $ h_body = "03_hp/13_hermione_main/body_03.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
        show screen hermione_main                                                                                                                                                                                 #HERMIONE
        with d5                                                                                                                                                                                                                        #HERMIONE
        her "Плитка шоколада?"
        hide screen hermione_main                                                                                                                                                                                   #HERMIONE
        with d3                                                                                                                                                                                                                        #HERMIONE
        $ h_body = "03_hp/13_hermione_main/body_09.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
        show screen hermione_main                                                                                                                                                                                 #HERMIONE
        with d3                                                                                                                                                                                                                        #HERMIONE
        her "Хм..."
        her "Тут что-то о феях..."
        hide screen hermione_main                                                                                                                                                                                   #HERMIONE
        with d3                                                                                                                                                                                                                        #HERMIONE
        $ h_body = "03_hp/13_hermione_main/body_11.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
        show screen hermione_main                                                                                                                                                                                 #HERMIONE
        with d3                                                                                                                                                                                                                        #HERMIONE
        her "Это шутка какая-то, не так ли?"
        hide screen hermione_main                                                                                                                                                                                   #HERMIONE
        with d3    
        $ the_gift = "03_hp/18_store/12.png" # CHOCOLATE
        show screen gift
        with d3
        ">Вы даете Гермионе плитку шоколада..."
        hide screen gift
        with d3
        $ h_body = "03_hp/13_hermione_main/body_15.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
        show screen hermione_main                                                                                                                                                                                 #HERMIONE
        with d3                                                                                                                                                                                                                        #HERMIONE
        her "Спасибо вам..."
        call happy #Message that says that Hermione's mood has improved.
        

        
    if whoring >= 12 and whoring <= 17: # Lv 5-6.
        $ mad -= 10
        $ chocolate -= 1
        $ h_body = "03_hp/13_hermione_main/body_03.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
        show screen hermione_main                                                                                                                                                                                 #HERMIONE
        with d5                                                                                                                                                                                                                        #HERMIONE
        her "Плитка шоколада?"
        hide screen hermione_main                                                                                                                                                                                   #HERMIONE
        with d3                                                                                                                                                                                                                        #HERMIONE
        $ h_body = "03_hp/13_hermione_main/body_24.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
        show screen hermione_main                                                                                                                                                                                 #HERMIONE
        with d3                                                                                                                                                                                                                        #HERMIONE
        her "Мне просто нравится как она хрустит, сэр! Н-не вкус..."
        hide screen hermione_main                                                                                                                                                                                   #HERMIONE
        with d3    
        $ the_gift = "03_hp/18_store/12.png" # CHOCOLATE
        show screen gift
        with d3
        ">Вы даете Гермионе плитку шоколада..."
        hide screen gift
        with d3
        $ h_body = "03_hp/13_hermione_main/body_01.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
        show screen hermione_main                                                                                                                                                                                 #HERMIONE
        with d3                                                                                                                                                                                                                        #HERMIONE
        her "Эм... Конечно, спасибо..."
        call happy #Message that says that Hermione's mood has improved.
       
 
        
    if whoring >= 18: # Lv 7+  
        $ chocolate -= 1
        $ mad -= 10
        $ h_body = "03_hp/13_hermione_main/body_06.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
        show screen hermione_main                                                                                                                                                                                 #HERMIONE
        with d5    
        her "Плитка шоколада?"
        hide screen hermione_main                                                                                                                                                                                   #HERMIONE
        with d3                                                                                                                                                                                                                        #HERMIONE
        $ h_body = "03_hp/13_hermione_main/body_111.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
        show screen hermione_main                                                                                                                                                                                 #HERMIONE
        with d3                                                                                                                                                                                                                        #HERMIONE
        her "Вы балуете меня, сэр."
        hide screen hermione_main                                                                                                                                                                                   #HERMIONE
        with d3    
        $ the_gift = "03_hp/18_store/12.png" # CHOCOLATE
        show screen gift
        with d3
        ">Вы даете Гермионе плитку шоколада..."
        hide screen gift
        with d3
        $ h_body = "03_hp/13_hermione_main/body_129.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
        show screen hermione_main                                                                                                                                                                                 #HERMIONE
        with d3                                                                                                                                                                                                                        #HERMIONE  
        her "Спасибо вам."
        call happy #Message that says that Hermione's mood has improved.
        
 
    $ h_xpos=370 #Defines position of the Hermione's full length sprite. (Default 370). (Center: 140)                                                       #HERMIONE
    show screen hermione_main                                                                                                                                                                                 #HERMIONE
    with d3                                                                                                                                                                                                                        #HERMIONE
    jump day_time_requests
        

    ### VIBRATOR ###
label giving_vibrator: # VIBRATOR.
    hide screen hermione_main                                                                                                                                                                                   #HERMIONE
    with d5                                                                                                                                                                                                                        #HERMIONE
    $ h_xpos=140 #Defines position of the Hermione's full length sprite. (Default 370). (Center: 140)                                                       #HERMIONE
    
    if whoring >= 0 and whoring <= 5: # Lv 1-2.
        $ mad+= 10
        $ h_body = "03_hp/13_hermione_main/body_01.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
        show screen hermione_main                                                                                                                                                                                 #HERMIONE
        with d5                                                                                                                                                                                                                        #HERMIONE
        her "Магическая палочка?"
        hide screen hermione_main                                                                                                                                                                                   #HERMIONE
        with d3                                                                                                                                                                                                                        #HERMIONE
        $ h_body = "03_hp/13_hermione_main/body_15.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
        show screen hermione_main                                                                                                                                                                                 #HERMIONE
        with d3                                                                                                                                                                                                                        #HERMIONE
        her "Нет, выглядит как--"
        her ".........?"
        hide screen hermione_main                                                                                                                                                                                   #HERMIONE
        with d3                                                                                                                                                                                                                        #HERMIONE
        $ h_body = "03_hp/13_hermione_main/body_18.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
        show screen hermione_main                                                                                                                                                                                 #HERMIONE
        with d3                                                                                                                                                                                                                        #HERMIONE
        her "!!!"
        hide screen hermione_main                                                                                                                                                                                   #HERMIONE
        with d3                                                                                                                                                                                                                        #HERMIONE
        $ h_body = "03_hp/13_hermione_main/body_187.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
        show screen hermione_main                                                                                                                                                                                 #HERMIONE
        with d3                                                                                                                                                                                                                        #HERMIONE
        her "Профессор Дамблдор!"
        hide screen hermione_main                                                                                                                                                                                   #HERMIONE
        with d3                                                                                                                                                                                                                        #HERMIONE
        $ h_body = "03_hp/13_hermione_main/body_30.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
        show screen hermione_main                                                                                                                                                                                 #HERMIONE
        with d3                                                                                                                                                                                                                        #HERMIONE
        her "Это неуместно!"
        call upset
        $ h_body = "03_hp/13_hermione_main/body_120.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
    
    if whoring >= 6 and whoring <= 11: # Lv 3-4.
        $ mad += 10
        $ h_body = "03_hp/13_hermione_main/body_118.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
        show screen hermione_main                                                                                                                                                                                 #HERMIONE
        with d5                                                                                                                                                                                                                        #HERMIONE
        her "Это то, что я думаю?"
        hide screen hermione_main                                                                                                                                                                                   #HERMIONE
        with d3                                                                                                                                                                                                                        #HERMIONE
        $ h_body = "03_hp/13_hermione_main/body_186.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
        show screen hermione_main                                                                                                                                                                                 #HERMIONE
        with d3                                                                                                                                                                                                                        #HERMIONE
        her "Сэр, позвольте напомнить вам о том, что я принадлежу факультету \"Гриффиндор\"."
        hide screen hermione_main                                                                                                                                                                                   #HERMIONE
        with d3                                                                                                                                                                                                                        #HERMIONE
        $ h_body = "03_hp/13_hermione_main/body_120.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
        show screen hermione_main                                                                                                                                                                                 #HERMIONE
        with d3                                                                                                                                                                                                                        #HERMIONE
        her "Этот подарок подходит для \"Слизеринских\" шлюх, сэр."
        call upset

    if whoring >= 12 and whoring <= 17: # Lv 5-6.
        $ vibrator -= 1
        $ h_body = "03_hp/13_hermione_main/body_118.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
        show screen hermione_main                                                                                                                                                                                 #HERMIONE
        with d5                                                                                                                                                                                                                        #HERMIONE
        her "Это...вибратор?"
        her "Дизайн..."
        her "Он напоминает мне мою палочку..."
        hide screen hermione_main                                                                                                                                                                                   #HERMIONE
        with d3                                                                                                                                                                                                                        #HERMIONE
        $ h_body = "03_hp/13_hermione_main/body_118.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
        show screen hermione_main                                                                                                                                                                                 #HERMIONE
        with d3                                                                                                                                                                                                                        #HERMIONE
        her "Это сделано на заказ для меня?"
        hide screen hermione_main                                                                                                                                                                                   #HERMIONE
        with d3                                                                                                                                                                                                                        #HERMIONE
        $ h_body = "03_hp/13_hermione_main/body_30.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
        show screen hermione_main                                                                                                                                                                                 #HERMIONE
        with d3                                                                                                                                                                                                                        #HERMIONE
        her "Это неуместно."
        hide screen hermione_main                                                                                                                                                                                   #HERMIONE
        with d3                                                                                                                                                                                                                              #HERMIONE
        $ h_body = "03_hp/13_hermione_main/body_29.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
        show screen hermione_main                                                                                                                                                                                 #HERMIONE
        with d3                                                                                                                                                                                                                        #HERMIONE
        her "Но тем не менее..."
        hide screen hermione_main                                                                                                                                                                                   #HERMIONE
        with d3    
        $ the_gift = "03_hp/18_store/13.png" # VIBRATOR
        show screen gift
        with d3
        ">Вы даете вибратор Гермионе..."
        hide screen gift
        with d3
        call no_change
        

    if whoring >= 18: # Lv 7+  
        $ vibrator -= 1
        $ mad -= 10
        $ h_body = "03_hp/13_hermione_main/body_11.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
        show screen hermione_main                                                                                                                                                                                 #HERMIONE
        with d5    
        her "Это вибратор..."
        hide screen hermione_main                                                                                                                                                                                   #HERMIONE
        with d3                                                                                                                                                                                                                        #HERMIONE
        $ h_body = "03_hp/13_hermione_main/body_10.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
        show screen hermione_main                                                                                                                                                                                 #HERMIONE
        with d3                                                                                                                                                                                                                        #HERMIONE
        her "Это... вызывает во мне..."
        hide screen hermione_main                                                                                                                                                                                   #HERMIONE
        with d3                                                                                                                                                                                                                        #HERMIONE
        $ h_body = "03_hp/13_hermione_main/body_66.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
        show screen hermione_main                                                                                                                                                                                 #HERMIONE
        with d3                                                                                                                                                                                                                        #HERMIONE
        her "Грязные мысли, сэр"
        hide screen hermione_main                                                                                                                                                                                   #HERMIONE
        with d3    
        $ the_gift = "03_hp/18_store/13.png" # VIBRATOR
        show screen gift
        with d3
        ">Вы даете вибратор Гермионе..."
        hide screen gift
        with d3
        $ h_body = "03_hp/13_hermione_main/body_124.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
        show screen hermione_main                                                                                                                                                                                 #HERMIONE
        with d3                                                                                                                                                                                                                        #HERMIONE
        her "Спасибо, сэр."
        hide screen hermione_main                                                                                                                                                                                   #HERMIONE
        with d3  
        call happy #Message that says that Hermione's mood has improved.
        
 
    $ h_xpos=370 #Defines position of the Hermione's full length sprite. (Default 370). (Center: 140)                                                       #HERMIONE
    show screen hermione_main                                                                                                                                                                                 #HERMIONE
    with d3                                                                                                                                                                                                                        #HERMIONE
    jump day_time_requests
        
        
        
        
        
        
        
        
        
        
            
            
            
            
            
        ### STRAP-ON ###
label giving_strapon: # STRAP-ON.
    hide screen hermione_main                                                                                                                                                                                   #HERMIONE
    with d5                                                                                                                                                                                                                        #HERMIONE
    $ h_xpos=140 #Defines position of the Hermione's full length sprite. (Default 370). (Center: 140)                                                       #HERMIONE
    
    if whoring >= 0 and whoring <= 5: # Lv 1-2.
        $ mad -= 20
        $ strapon -= 1
        $ h_body = "03_hp/13_hermione_main/body_18.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
        show screen hermione_main                                                                                                                                                                                 #HERMIONE
        with d5                                                                                                                                                                                                                        #HERMIONE
        her "Что это?"
        hide screen hermione_main                                                                                                                                                                                   #HERMIONE
        with d3                                                                                                                                                                                                                        #HERMIONE
        $ h_body = "03_hp/13_hermione_main/body_14.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
        show screen hermione_main                                                                                                                                                                                 #HERMIONE
        with d3                                                                                                                                                                                                                        #HERMIONE
        her "Какой-то артефакт?"
        hide screen hermione_main                                                                                                                                                                                   #HERMIONE
        with d3                                                                                                                                                                                                                        #HERMIONE
        $ h_body = "03_hp/13_hermione_main/body_01.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
        show screen hermione_main                                                                                                                                                                                 #HERMIONE
        with d3                                                                                                                                                                                                                        #HERMIONE
        her "Так хорошо продуман..."
        hide screen hermione_main                                                                                                                                                                                   #HERMIONE
        with d3                                                                                                                                                                                                                        #HERMIONE
        $ h_body = "03_hp/13_hermione_main/body_06.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
        show screen hermione_main                                                                                                                                                                                 #HERMIONE
        with d3                                                                                                                                                                                                                        #HERMIONE
        her "Вы уверены, что мне стоит обладать этим?"
        hide screen hermione_main                                                                                                                                                                                   #HERMIONE
        with d3    
        $ the_gift = "03_hp/18_store/14.png" # STRAP-ON
        show screen gift
        with d3
        ">Вы даете страпон Гермионе..."
        hide screen gift
        with d3
        $ h_body = "03_hp/13_hermione_main/body_16.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
        show screen hermione_main                                                                                                                                                                                 #HERMIONE
        with d3                                                                                                                                                                                                                        #HERMIONE
        her "Огромное спасибо, сэр. Я обещаю хорошо обращаться с ним."
        hide screen hermione_main                                                                                                                                                                                   #HERMIONE
        with d3                                                                                                                                                                                                                        #HERMIONE
        call happy
        $ h_body = "03_hp/13_hermione_main/body_15.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
    
    
    
    if whoring >= 6 and whoring <= 11: # Lv 3-4.
        $ mad += 15
        $ h_body = "03_hp/13_hermione_main/body_18.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
        show screen hermione_main                                                                                                                                                                                 #HERMIONE
        with d5                                                                                                                                                                                                                        #HERMIONE
        her "!!!"
        hide screen hermione_main                                                                                                                                                                                   #HERMIONE
        with d3                                                                                                                                                                                                                        #HERMIONE
        $ h_body = "03_hp/13_hermione_main/body_118.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
        show screen hermione_main                                                                                                                                                                                 #HERMIONE
        with d3                                                                                                                                                                                                                        #HERMIONE
        her "Это..."
        her "Оно не выглядит... по человечески..."
        hide screen hermione_main                                                                                                                                                                                   #HERMIONE
        with d3                                                                                                                                                                                                                        #HERMIONE
        $ h_body = "03_hp/13_hermione_main/body_69.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
        show screen hermione_main                                                                                                                                                                                 #HERMIONE
        with d3                                                                                                                                                                                                                        #HERMIONE
        her "То есть..."
        hide screen hermione_main                                                                                                                                                                                   #HERMIONE
        with d3                                                                                                                                                                                                                        #HERMIONE
        $ h_body = "03_hp/13_hermione_main/body_86.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
        show screen hermione_main                                                                                                                                                                                 #HERMIONE
        with d3                                                                                                                                                                                                                        #HERMIONE
        her "Сэр, вам не стыдно?!"
        her "Дарить что-то вроде этого ученику?!"
        hide screen hermione_main                                                                                                                                                                                   #HERMIONE
        with d3                                                                                                                                                                                                                        #HERMIONE
        $ h_body = "03_hp/13_hermione_main/body_87.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
        show screen hermione_main                                                                                                                                                                                 #HERMIONE
        with d3                                                                                                                                                                                                                        #HERMIONE
        her ".................."
        hide screen hermione_main                                                                                                                                                                                   #HERMIONE
        with d3                                                                                                                                                                                                                        #HERMIONE
        $ h_body = "03_hp/13_hermione_main/body_47.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
        show screen hermione_main                                                                                                                                                                                 #HERMIONE
        with d3                                                                                                                                                                                                                        #HERMIONE
        her "Пожалуйста, уберите это."
        hide screen hermione_main                                                                                                                                                                                 #HERMIONE
        with d3                                                                                                                                                                                                                        #HERMIONE
        call upset

    if whoring >= 12 and whoring <= 17: # Lv 5-6.
        $ strapon -= 1
        $ mad -= 10
        $ h_body = "03_hp/13_hermione_main/body_118.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
        show screen hermione_main                                                                                                                                                                                 #HERMIONE
        with d5                                                                                                                                                                                                                        #HERMIONE
        her "Эта штука..."
        hide screen hermione_main                                                                                                                                                                                   #HERMIONE
        with d3                                                                                                                                                                                                                        #HERMIONE
        $ h_body = "03_hp/13_hermione_main/body_117.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
        show screen hermione_main                                                                                                                                                                                 #HERMIONE
        with d3                                                                                                                                                                                                                        #HERMIONE
        her "Это нормальный размер...для \"этого\"?"
        hide screen hermione_main                                                                                                                                                                                   #HERMIONE
        with d3                                                                                                                                                                                                                        #HERMIONE
        $ h_body = "03_hp/13_hermione_main/body_189.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
        show screen hermione_main                                                                                                                                                                                 #HERMIONE
        with d3                                                                                                                                                                                                                        #HERMIONE
        her "Я имею в виду..."
        hide screen hermione_main                                                                                                                                                                                   #HERMIONE
        with d3                                                                                                                                                                                                                        #HERMIONE
        $ h_body = "03_hp/13_hermione_main/body_118.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
        show screen hermione_main                                                                                                                                                                                 #HERMIONE
        with d3                                                                                                                                                                                                                        #HERMIONE
        her "......................."
        hide screen hermione_main                                                                                                                                                                                   #HERMIONE
        with d3                                                                                                                                                                                                                        #HERMIONE
        $ h_body = "03_hp/13_hermione_main/body_117.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
        show screen hermione_main                                                                                                                                                                                 #HERMIONE
        with d3                                                                                                                                                                                                                        #HERMIONE
        her "Это реквизит для какого-то розыгрыша?"
        hide screen hermione_main                                                                                                                                                                                  #HERMIONE
        with d3                                                                                                                                                                                                                        #HERMIONE
        $ h_body = "03_hp/13_hermione_main/body_118.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
        show screen hermione_main                                                                                                                                                                                 #HERMIONE
        with d3                                                                                                                                                                                                                        #HERMIONE
        her "Оно неплохо сделано "
        hide screen hermione_main                                                                                                                                                                                   #HERMIONE
        with d3                                                                                                                                                                                                                        #HERMIONE
        $ h_body = "03_hp/13_hermione_main/body_33.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
        show screen hermione_main                                                                                                                                                                                 #HERMIONE
        with d3                                                                                                                                                                                                                        #HERMIONE
        her "Я возьму его..."
        hide screen hermione_main                                                                                                                                                                                   #HERMIONE
        with d3    
        $ the_gift = "03_hp/18_store/14.png" # STRAP-ON
        show screen gift
        with d3
        ">Вы даете страпон Гермионе..."
        hide screen gift
        with d3
        call happy


    if whoring >= 18: # Lv 7+  
        $ strapon -= 1
        $ mad -= 30
        $ h_body = "03_hp/13_hermione_main/body_48.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
        show screen hermione_main                                                                                                                                                                                 #HERMIONE
        with d5    
        her "Это... Это великолепно, сэр..."
        hide screen hermione_main                                                                                                                                                                                   #HERMIONE
        with d3                                                                                                                                                                                                                        #HERMIONE
        $ h_body = "03_hp/13_hermione_main/body_189.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
        show screen hermione_main                                                                                                                                                                                 #HERMIONE
        with d3                                                                                                                                                                                                                        #HERMIONE
        her "Он смоделирован по тому самому Фестралу?"
        hide screen hermione_main                                                                                                                                                                                   #HERMIONE
        with d3                                                                                                                                                                                                                        #HERMIONE
        $ h_body = "03_hp/13_hermione_main/body_190.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
        show screen hermione_main                                                                                                                                                                                 #HERMIONE
        with d3                                                                                                                                                                                                                        #HERMIONE
        her "Но эти существа невидимы..."
        hide screen hermione_main                                                                                                                                                                                   #HERMIONE
        with d3                                                                                                                                                                                                                        #HERMIONE
        $ h_body = "03_hp/13_hermione_main/body_118.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
        show screen hermione_main                                                                                                                                                                                 #HERMIONE
        with d3                                                                                                                                                                                                                        #HERMIONE
        her ".................."
        hide screen hermione_main                                                                                                                                                                                   #HERMIONE
        with d3                                                                                                                                                                                                                        #HERMIONE
        $ h_body = "03_hp/13_hermione_main/body_123.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
        show screen hermione_main                                                                                                                                                                                 #HERMIONE
        with d3                                                                                                                                                                                                                        #HERMIONE
        her "Захватывающе..."
        hide screen hermione_main                                                                                                                                                                                   #HERMIONE
        with d3                                                                                                                                                                                                                        #HERMIONE
        $ h_body = "03_hp/13_hermione_main/body_120.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
        show screen hermione_main                                                                                                                                                                                 #HERMIONE
        with d3                                                                                                                                                                                                                        #HERMIONE
        her "Не так, как вы думаете, сэр..."
        hide screen hermione_main                                                                                                                                                                                   #HERMIONE
        with d3                                                                                                                                                                                                                        #HERMIONE
        $ h_body = "03_hp/13_hermione_main/body_127.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
        show screen hermione_main                                                                                                                                                                                 #HERMIONE
        with d3                                                                                                                                                                                                                        #HERMIONE
        her "Я просто любуюсь мастерством..."
        hide screen hermione_main                                                                                                                                                                                   #HERMIONE
        with d3    
        $ the_gift = "03_hp/18_store/14.png" # STRAP-ON
        show screen gift
        with d3
        ">Вы даете страпон Гермионе..."
        hide screen gift
        with d3
        $ h_body = "03_hp/13_hermione_main/body_129.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
        show screen hermione_main                                                                                                                                                                                 #HERMIONE
        with d3                                                                                                                                                                                                                        #HERMIONE
        her "Спасибо вам за подарок, сэр."
        hide screen hermione_main                                                                                                                                                                                   #HERMIONE
        with d3                                                                                                                                                                                                                        #HERMIONE
        call happy

 
    $ h_xpos=370 #Defines position of the Hermione's full length sprite. (Default 370). (Center: 140)                                                       #HERMIONE
    show screen hermione_main                                                                                                                                                                                 #HERMIONE
    with d3                                                                                                                                                                                                                        #HERMIONE
    jump day_time_requests
        
        
        
        
        
   
        ### BALL GAG ###
label giving_ballgag: # BALL GAG.
    hide screen hermione_main                                                                                                                                                                                   #HERMIONE
    with d5                                                                                                                                                                                                                        #HERMIONE
    $ h_xpos=140 #Defines position of the Hermione's full length sprite. (Default 370). (Center: 140)                                                       #HERMIONE
    
    if whoring >= 0 and whoring <= 5: # Lv 1-2.
        $ mad += 10
        $ h_body = "03_hp/13_hermione_main/body_118.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
        show screen hermione_main                                                                                                                                                                                 #HERMIONE
        with d5                                                                                                                                                                                                                        #HERMIONE
        her "Что это?"
        hide screen hermione_main                                                                                                                                                                                   #HERMIONE
        with d3                                                                                                                                                                                                                        #HERMIONE
        $ h_body = "03_hp/13_hermione_main/body_141.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
        show screen hermione_main                                                                                                                                                                                 #HERMIONE
        with d3                                                                                                                                                                                                                        #HERMIONE
        her "Выглядит как одна из игрушек для взрослых?"
        hide screen hermione_main                                                                                                                                                                                   #HERMIONE
        with d3                                                                                                                                                                                                                        #HERMIONE
        $ h_body = "03_hp/13_hermione_main/body_30.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
        show screen hermione_main                                                                                                                                                                                 #HERMIONE
        with d3                                                                                                                                                                                                                        #HERMIONE
        her "Какая женщина в здравом уме будет подвергать себя такому унижению?"
        hide screen hermione_main                                                                                                                                                                                   #HERMIONE
        with d3                                                                                                                                                                                                                        #HERMIONE
        $ h_body = "03_hp/13_hermione_main/body_186.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
        show screen hermione_main                                                                                                                                                                                 #HERMIONE
        with d3                                                                                                                                                                                                                        #HERMIONE
        her "И что мне с этим сделать?"
        hide screen hermione_main                                                                                                                                                                                   #HERMIONE
        with d3                                                                                                                                                                                                                        #HERMIONE
        $ h_body = "03_hp/13_hermione_main/body_187.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
        show screen hermione_main                                                                                                                                                                                 #HERMIONE
        with d3                                                                                                                                                                                                                        #HERMIONE
        her "Это очень обидно, сэр..."                                                                                                                                                                                                              
        call upset

    if whoring >= 6 and whoring <= 11: # Lv 3-4.
        $ mad += 5
        $ h_body = "03_hp/13_hermione_main/body_186.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
        show screen hermione_main                                                                                                                                                                                 #HERMIONE
        with d5                                                                                                                                                                                                                        #HERMIONE
        her "Сэр, вы не понимаете, насколько неправильно было бы для меня, принять от вас такой подарок?"
        hide screen hermione_main                                                                                                                                                                                   #HERMIONE
        with d3                                                                                                                                                                                                                        #HERMIONE
        $ h_body = "03_hp/13_hermione_main/body_189.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
        show screen hermione_main                                                                                                                                                                                 #HERMIONE
        with d3                                                                                                                                                                                                                        #HERMIONE
        her "И ведь я даже не представляю, что с этим делать..."
        hide screen hermione_main                                                                                                                                                                                   #HERMIONE
        with d3                                                                                                                                                                                                                        #HERMIONE
        $ h_body = "03_hp/13_hermione_main/body_118.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
        show screen hermione_main                                                                                                                                                                                 #HERMIONE
        with d3                                                                                                                                                                                                                        #HERMIONE
        her "То есть эти пушистые наручники, это просто..."
        her "И этот круглый кляп... Эм..."
        hide screen hermione_main                                                                                                                                                                                   #HERMIONE
        with d3                                                                                                                                                                                                                        #HERMIONE
        $ h_body = "03_hp/13_hermione_main/body_120.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
        show screen hermione_main                                                                                                                                                                                 #HERMIONE
        with d3                                                                                                                                                                                                                        #HERMIONE
        her "Сэр, пожалуйста..."
        her "Просто уберите это."
        call upset


    if whoring >= 12 and whoring <= 17: # Lv 5-6.
        $ ballgag -= 1
        $ mad -= 9
        $ h_body = "03_hp/13_hermione_main/body_120.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
        show screen hermione_main                                                                                                                                                                                 #HERMIONE
        with d5                                                                                                                                                                                                                        #HERMIONE
        her "Месяц назад я бы чувствовала себя оскорбленной, если бы получила такой подарок..."
        hide screen hermione_main                                                                                                                                                                                   #HERMIONE
        with d3                                                                                                                                                                                                                        #HERMIONE
        $ h_body = "03_hp/13_hermione_main/body_118.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
        show screen hermione_main                                                                                                                                                                                 #HERMIONE
        with d3                                                                                                                                                                                                                        #HERMIONE
        her "Но теперь я знаю, что некоторые девушки получают удовольствие от такого..."
        hide screen hermione_main                                                                                                                                                                                   #HERMIONE
        with d3                                                                                                                                                                                                                        #HERMIONE
        $ h_body = "03_hp/13_hermione_main/body_117.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
        show screen hermione_main                                                                                                                                                                                 #HERMIONE
        with d3                                                                                                                                                                                                                        #HERMIONE
        hide screen hermione_main                                                                                                                                                                                   #HERMIONE
        with d3                                                                                                                                                                                                                        #HERMIONE
        $ h_body = "03_hp/13_hermione_main/body_120.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
        show screen hermione_main                                                                                                                                                                                 #HERMIONE
        with d3                                                                                                                                                                                                                        #HERMIONE
        her "Уверяю вас, я не одна из таких, сэр."
        hide screen hermione_main                                                                                                                                                                                   #HERMIONE
        with d3                                                                                                                                                                                                                        #HERMIONE
        $ h_body = "03_hp/13_hermione_main/body_189.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
        show screen hermione_main                                                                                                                                                                                 #HERMIONE
        with d3                                                                                                                                                                                                                        #HERMIONE
        her "Но я знаю девушку, которая знает девушку, которая в таких вещах, как ..."
        hide screen hermione_main                                                                                                                                                                                   #HERMIONE
        with d3                                                                                                                                                                                                                        #HERMIONE
        $ h_body = "03_hp/13_hermione_main/body_188.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
        show screen hermione_main                                                                                                                                                                                 #HERMIONE
        with d3                                                                                                                                                                                                                        #HERMIONE
        her "Да, я возьму это и отдам ей..."
        hide screen hermione_main                                                                                                                                                                                   #HERMIONE
        with d3    
        $ the_gift = "03_hp/18_store/15.png" # BALL GAG.
        show screen gift
        with d3
        ">Вы даете кляп и наручники Гермионе..."
        hide screen gift
        with d3
        call happy

    if whoring >= 18: # Lv 7+  
        $ ballgag -= 1
        $ mad -= 15
        $ h_body = "03_hp/13_hermione_main/body_190.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
        show screen hermione_main                                                                                                                                                                                 #HERMIONE
        with d5    
        her "Кляп и наручники?"
        hide screen hermione_main                                                                                                                                                                                   #HERMIONE
        with d3                                                                                                                                                                                                                        #HERMIONE
        $ h_body = "03_hp/13_hermione_main/body_122.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
        show screen hermione_main                                                                                                                                                                                 #HERMIONE
        with d3                                                                                                                                                                                                                        #HERMIONE
        her "Это совершенно неуместно, сэр." # :)
        hide screen hermione_main                                                                                                                                                                                   #HERMIONE
        with d3                                                                                                                                                                                                                        #HERMIONE
        $ h_body = "03_hp/13_hermione_main/body_129.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
        show screen hermione_main                                                                                                                                                                                 #HERMIONE
        with d3                                                                                                                                                                                                                        #HERMIONE
        her "Но, подарок это подарок, так?"
        hide screen hermione_main                                                                                                                                                                                   #HERMIONE
        with d3    
        $ the_gift = "03_hp/18_store/15.png" # BALL GAG.
        show screen gift
        with d3
        ">Вы даете кляп и наручники Гермионе..."
        hide screen gift
        with d3
        call happy
        

 
    $ h_xpos=370 #Defines position of the Hermione's full length sprite. (Default 370). (Center: 140)                                                       #HERMIONE
    show screen hermione_main                                                                                                                                                                                 #HERMIONE
    with d3                                                                                                                                                                                                                        #HERMIONE
    jump day_time_requests
        
        
        
        
        
        
        
        
        
        
        
        
        
  
      ### ANAL PLUGS ###
label giving_plug: 
    hide screen hermione_main                                                                                                                                                                                   #HERMIONE
    with d5                                                                                                                                                                                                                        #HERMIONE
    $ h_xpos=140 #Defines position of the Hermione's full length sprite. (Default 370). (Center: 140)                                                       #HERMIONE
    
    if whoring >= 0 and whoring <= 5: # Lv 1-2.
        $ mad -= 8
        $ plug -= 1
        $ h_body = "03_hp/13_hermione_main/body_01.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
        show screen hermione_main                                                                                                                                                                                 #HERMIONE
        with d5                                                                                                                                                                                                                        #HERMIONE
        her "Хм...?"
        hide screen hermione_main                                                                                                                                                                                   #HERMIONE
        with d3                                                                                                                                                                                                                        #HERMIONE
        $ h_body = "03_hp/13_hermione_main/body_15.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
        show screen hermione_main                                                                                                                                                                                 #HERMIONE
        with d3                                                                                                                                                                                                                        #HERMIONE
        her "Это что-то вроде затычек?"
        hide screen hermione_main                                                                                                                                                                                   #HERMIONE
        with d3    
        $ the_gift = "03_hp/18_store/16.png" # ANAL PLUG.
        show screen gift
        with d3
        ">Вы даете Гермионе анальную пробку..."
        hide screen gift
        with d3
        hide screen hermione_main                                                                                                                                                                                   #HERMIONE
        with d3                                                                                                                                                                                                                        #HERMIONE
        $ h_body = "03_hp/13_hermione_main/body_185.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
        show screen hermione_main                                                                                                                                                                                 #HERMIONE
        with d3                                                                                                                                                                                                                        #HERMIONE
        her "Спасибо, сэр."
        call happy


    if whoring >= 6 and whoring <= 11: # Lv 3-4.
        $ mad -= 15
        $ h_body = "03_hp/13_hermione_main/body_186.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
        show screen hermione_main                                                                                                                                                                                 #HERMIONE
        with d5                                                                                                                                                                                                                        #HERMIONE
        her "Сэр, это какие-то игрушки для взрослых?"
        hide screen hermione_main                                                                                                                                                                                   #HERMIONE
        with d3                                                                                                                                                                                                                        #HERMIONE
        $ h_body = "03_hp/13_hermione_main/body_187.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
        show screen hermione_main                                                                                                                                                                                 #HERMIONE
        with d3                                                                                                                                                                                                                        #HERMIONE
        her "Это что-то из штук для анального секса?"
        her "Сэр, я считаю, что это одно из оружий для угнетения и унижения женщин!"
        hide screen hermione_main                                                                                                                                                                                   #HERMIONE
        with d3                                                                                                                                                                                                                        #HERMIONE
        $ h_body = "03_hp/13_hermione_main/body_120.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
        show screen hermione_main                                                                                                                                                                                 #HERMIONE
        with d3                                                                                                                                                                                                                        #HERMIONE
        her "Козел!"
        call upset

        
    if whoring >= 12 and whoring <= 17: # Lv 5-6.
        $ h_body = "03_hp/13_hermione_main/body_120.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
        show screen hermione_main                                                                                                                                                                                 #HERMIONE
        with d5                                                                                                                                                                                                                        #HERMIONE
        her "Да, я знаю девочку, которая..."
        hide screen hermione_main                                                                                                                                                                                   #HERMIONE
        with d3                                                                                                                                                                                                                        #HERMIONE
        $ h_body = "03_hp/13_hermione_main/body_186.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
        show screen hermione_main                                                                                                                                                                                 #HERMIONE
        with d3                                                                                                                                                                                                                        #HERMIONE
        her "Пользуется чем-то подобным..."
        her "Но не я, сэр."
        hide screen hermione_main                                                                                                                                                                                   #HERMIONE
        with d3                                                                                                                                                                                                                        #HERMIONE
        $ h_body = "03_hp/13_hermione_main/body_120.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
        show screen hermione_main                                                                                                                                                                                 #HERMIONE
        with d3                                                                                                                                                                                                                        #HERMIONE
        her "Нет. Спасибо."
        call no_change

    if whoring >= 18: # Lv 7+  
        $ plug -= 1
        $ mad -= 10
        $ h_body = "03_hp/13_hermione_main/body_118.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
        show screen hermione_main                                                                                                                                                                                 #HERMIONE
        with d5    
        her "Анальная пробка?"
        hide screen hermione_main                                                                                                                                                                                   #HERMIONE
        with d3                                                                                                                                                                                                                        #HERMIONE
        $ h_body = "03_hp/13_hermione_main/body_117.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
        show screen hermione_main                                                                                                                                                                                 #HERMIONE
        with d3                                                                                                                                                                                                                        #HERMIONE
        her "Я не пользуюсь таким..."
        hide screen hermione_main                                                                                                                                                                                   #HERMIONE
        with d3                                                                                                                                                                                                                        #HERMIONE
        $ h_body = "03_hp/13_hermione_main/body_122.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
        show screen hermione_main                                                                                                                                                                                 #HERMIONE
        with d3                                                                                                                                                                                                                        #HERMIONE
        her "Хотя оно очень красиво..."
        hide screen hermione_main                                                                                                                                                                                   #HERMIONE
        with d3                                                                                                                                                                                                                        #HERMIONE
        $ h_body = "03_hp/13_hermione_main/body_118.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
        show screen hermione_main                                                                                                                                                                                 #HERMIONE
        with d3                                                                                                                                                                                                                        #HERMIONE
        her "....................."
        hide screen hermione_main                                                                                                                                                                                   #HERMIONE
        with d3                                                                                                                                                                                                                        #HERMIONE
        $ h_body = "03_hp/13_hermione_main/body_121.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
        show screen hermione_main                                                                                                                                                                                 #HERMIONE
        with d3                                                                                                                                                                                                                        #HERMIONE
        her "Ну, ладно. Я возьму, если вы настаиваете."
        hide screen hermione_main                                                                                                                                                                                   #HERMIONE
        with d3    
        $ the_gift = "03_hp/18_store/16.png" # ANAL PLUGS.
        show screen gift
        with d3
        ">Вы даете Гермионе анальную пробку..."
        hide screen gift
        with d3
        $ h_body = "03_hp/13_hermione_main/body_127.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
        show screen hermione_main                                                                                                                                                                                 #HERMIONE
        with d3                                                                                                                                                                                                                        #HERMIONE
        her "Но конечно же никогда не воспользуюсь..."
        hide screen hermione_main                                                                                                                                                                                   #HERMIONE
        with d3                                                                                                                                                                                                                        #HERMIONE
        $ h_body = "03_hp/13_hermione_main/body_124.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
        show screen hermione_main                                                                                                                                                                                 #HERMIONE
        with d3                                                                                                                                                                                                                        #HERMIONE
        her "................"
        call happy
        

 
    $ h_xpos=370 #Defines position of the Hermione's full length sprite. (Default 370). (Center: 140)                                                       #HERMIONE
    show screen hermione_main                                                                                                                                                                                 #HERMIONE
    with d3                                                                                                                                                                                                                        #HERMIONE
    jump day_time_requests
        
        
        
        
        
        
        
          ### EDUCATIONAL MAGAZINES ###
label giving_mag1: 
    hide screen hermione_main                                                                                                                                                                                   #HERMIONE
    with d5                                                                                                                                                                                                                        #HERMIONE
    $ h_xpos=140 #Defines position of the Hermione's full length sprite. (Default 370). (Center: 140)                                                       #HERMIONE
    
    if whoring >= 0 and whoring <= 5: # Lv 1-2.
        $ mad -= 15
        $ mag1 -= 1
        $ h_body = "03_hp/13_hermione_main/body_01.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
        show screen hermione_main                                                                                                                                                                                 #HERMIONE
        with d5                                                                                                                                                                                                                        #HERMIONE
        her "\"Популярные магические\" журналы?"
        hide screen hermione_main                                                                                                                                                                                   #HERMIONE
        with d3    
        $ the_gift = "03_hp/18_store/17.png" # EDUCATIONAL MAGAZIES.
        show screen gift
        with d3
        ">Вы даете несколько обучающих журналов Гермионе..."
        hide screen gift
        with d3
        $ h_body = "03_hp/13_hermione_main/body_06.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
        show screen hermione_main                                                                                                                                                                                 #HERMIONE
        with d3                                                                                                                                                                                                                        #HERMIONE
        her "Спасибо, сэр!"
        her "Я использую их для своих исследований!"
        call happy

    if whoring >= 6 and whoring <= 11: # Lv 3-4.
        $ mad -= 10
        $ mag1 -= 1
        $ h_body = "03_hp/13_hermione_main/body_01.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
        show screen hermione_main                                                                                                                                                                                 #HERMIONE
        with d5                                                                                                                                                                                                                        #HERMIONE
        her "Временами я ищу в журналах информацию, которую не могу найти в книгах..."
        hide screen hermione_main                                                                                                                                                                                   #HERMIONE
        with d3    
        $ the_gift = "03_hp/18_store/17.png" # EDUCATIONAL MAGAZIES.
        show screen gift
        with d3
        ">Вы даете несколько обучающих журналов Гермионе..."
        hide screen gift
        with d3
        $ h_body = "03_hp/13_hermione_main/body_06.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
        show screen hermione_main                                                                                                                                                                                 #HERMIONE
        with d3                                                                                                                                                                                                                        #HERMIONE
        her "Спасибо, сэр!"
        her "Я использую их для своих исследований!"
        call happy

    if whoring >= 12 and whoring <= 17: # Lv 5-6.
        $ mad -= 3 
        $ mag1 -= 1
        $ h_body = "03_hp/13_hermione_main/body_02.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
        show screen hermione_main                                                                                                                                                                                 #HERMIONE
        with d5                                                                                                                                                                                                                        #HERMIONE
        her "Ох..."
        hide screen hermione_main                                                                                                                                                                                   #HERMIONE
        with d3                                                                                                                                                                                                                        #HERMIONE
        $ h_body = "03_hp/13_hermione_main/body_06.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
        show screen hermione_main                                                                                                                                                                                 #HERMIONE
        with d3                                                                                                                                                                                                                        #HERMIONE
        her "Да, я читаю как можно больше журналов..."
        hide screen hermione_main                                                                                                                                                                                   #HERMIONE
        with d3                                                                                                                                                                                                                        #HERMIONE
        $ h_body = "03_hp/13_hermione_main/body_10.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
        show screen hermione_main                                                                                                                                                                                 #HERMIONE
        with d3                                                                                                                                                                                                                        #HERMIONE
        her "Особенно много в последнее время..."
        hide screen hermione_main                                                                                                                                                                                   #HERMIONE
        with d3    
        $ the_gift = "03_hp/18_store/17.png" # EDUCATIONAL MAGAZIES.
        show screen gift
        with d3
        ">Вы даете несколько обучающих журналов Гермионе..."
        hide screen gift
        with d3
        $ h_body = "03_hp/13_hermione_main/body_06.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
        show screen hermione_main                                                                                                                                                                                 #HERMIONE
        with d3                                                                                                                                                                                                                        #HERMIONE
        her "Спасибо, сэр!"
        call happy
     

    if whoring >= 18: # Lv 7+  
        $ mag1 -= 1
        $ h_body = "03_hp/13_hermione_main/body_10.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
        show screen hermione_main                                                                                                                                                                                 #HERMIONE
        with d5    
        her "Эм..."
        hide screen hermione_main                                                                                                                                                                                   #HERMIONE
        with d3                                                                                                                                                                                                                        #HERMIONE
        $ h_body = "03_hp/13_hermione_main/body_08.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
        show screen hermione_main                                                                                                                                                                                 #HERMIONE
        with d3                                                                                                                                                                                                                        #HERMIONE
        her "Если быть честной, журналы уже не особо привлекают меня..."
        hide screen hermione_main                                                                                                                                                                                   #HERMIONE
        with d3                                                                                                                                                                                                                        #HERMIONE
        $ h_body = "03_hp/13_hermione_main/body_11.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
        show screen hermione_main                                                                                                                                                                                 #HERMIONE
        with d3                                                                                                                                                                                                                        #HERMIONE
        her "Но я не против принять их от вас."
        hide screen hermione_main                                                                                                                                                                                   #HERMIONE
        with d3    
        $ the_gift = "03_hp/18_store/17.png" # EDUCATIONAL MAGAZIES.
        show screen gift
        with d3
        ">Вы даете несколько обучающих журналов Гермионе..."
        hide screen gift
        with d3
        $ h_body = "03_hp/13_hermione_main/body_13.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
        show screen hermione_main                                                                                                                                                                                 #HERMIONE
        with d3                                                                                                                                                                                                                        #HERMIONE
        her "Спасибо вам."
        call no_change 

 
    $ h_xpos=370 #Defines position of the Hermione's full length sprite. (Default 370). (Center: 140)                                                       #HERMIONE
    show screen hermione_main                                                                                                                                                                                 #HERMIONE
    with d3                                                                                                                                                                                                                        #HERMIONE
    jump day_time_requests    
        
        
        
        
        
              ### GIRLY MAGAZINES ###
label giving_mag2: 
    hide screen hermione_main                                                                                                                                                                                   #HERMIONE
    with d5                                                                                                                                                                                                                        #HERMIONE
    $ h_xpos=140 #Defines position of the Hermione's full length sprite. (Default 370). (Center: 140)                                                       #HERMIONE
    
    if whoring >= 0 and whoring <= 5: # Lv 1-2.
        $ h_body = "03_hp/13_hermione_main/body_15.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
        show screen hermione_main                                                                                                                                                                                 #HERMIONE
        with d5                                                                                                                                                                                                                        #HERMIONE
        her "Хм?"
        hide screen hermione_main                                                                                                                                                                                   #HERMIONE
        with d3                                                                                                                                                                                                                        #HERMIONE
        $ h_body = "03_hp/13_hermione_main/body_17.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
        show screen hermione_main                                                                                                                                                                                 #HERMIONE
        with d3                                                                                                                                                                                                                        #HERMIONE
        her "Это какие-то журналы для \"слизеринских\" девок, я полагаю."
        hide screen hermione_main                                                                                                                                                                                   #HERMIONE
        with d3                                                                                                                                                                                                                        #HERMIONE
        $ h_body = "03_hp/13_hermione_main/body_16.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
        show screen hermione_main                                                                                                                                                                                 #HERMIONE
        with d3                                                                                                                                                                                                                        #HERMIONE
        her "Я выше, этих глупых журналов, сэр."
        call no_change
        $ h_body = "03_hp/13_hermione_main/body_01.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
        
        
        
      
    if whoring >= 6 and whoring <= 11: # Lv 3-4.
        $ mad -= 5
        $ mag2 -= 1
        $ h_body = "03_hp/13_hermione_main/body_04.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
        show screen hermione_main                                                                                                                                                                                 #HERMIONE
        with d5                                                                                                                                                                                                                        #HERMIONE
        her "Я не читаю журналы такого рода..."
        hide screen hermione_main                                                                                                                                                                                   #HERMIONE
        with d3                                                                                                                                                                                                                        #HERMIONE
        $ h_body = "03_hp/13_hermione_main/body_13.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
        show screen hermione_main                                                                                                                                                                                 #HERMIONE
        with d3                                                                                                                                                                                                                        #HERMIONE
        her "................"
        hide screen hermione_main                                                                                                                                                                                   #HERMIONE
        with d3                                                                                                                                                                                                                        #HERMIONE
        $ h_body = "03_hp/13_hermione_main/body_04.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
        show screen hermione_main                                                                                                                                                                                 #HERMIONE
        with d3                                                                                                                                                                                                                        #HERMIONE
        her "Но я могу попробовать, просто смеха ради..."
        hide screen hermione_main                                                                                                                                                                                   #HERMIONE
        with d3    
        $ the_gift = "03_hp/18_store/18.png" # GIRLY MAGAZIES.
        show screen gift
        with d3
        ">Вы даете женские журналы Гермионе..."
        hide screen gift
        with d3
        $ h_body = "03_hp/13_hermione_main/body_08.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
        show screen hermione_main                                                                                                                                                                                 #HERMIONE
        with d3                                                                                                                                                                                                                        #HERMIONE
        her "Спасибо, сэр!"
        call happy
        $ h_body = "03_hp/13_hermione_main/body_06.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE

    if whoring >= 12 and whoring <= 17: # Lv 5-6.
        $ mad -= 15 
        $ mag2 -= 1
        $ h_body = "03_hp/13_hermione_main/body_10.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
        show screen hermione_main                                                                                                                                                                                 #HERMIONE
        with d5                                                                                                                                                                                                                        #HERMIONE
        her "Мне стыдно признаваться, но..."
        hide screen hermione_main                                                                                                                                                                                   #HERMIONE
        with d3                                                                                                                                                                                                                        #HERMIONE
        $ h_body = "03_hp/13_hermione_main/body_24.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
        show screen hermione_main                                                                                                                                                                                 #HERMIONE
        with d3                                                                                                                                                                                                                        #HERMIONE
        her "Последнее время мне действительно нравится читать подобное..."
        hide screen hermione_main                                                                                                                                                                                   #HERMIONE
        with d3    
        $ the_gift = "03_hp/18_store/18.png" # GIRLY MAGAZIES.
        show screen gift
        with d3
        ">Вы даете женские журналы Гермионе..."
        hide screen gift
        with d3
        $ h_body = "03_hp/13_hermione_main/body_08.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
        show screen hermione_main                                                                                                                                                                                 #HERMIONE
        with d3                                                                                                                                                                                                                        #HERMIONE
        her "Спасибо, сэр."
        call happy
        $ h_body = "03_hp/13_hermione_main/body_06.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
        

    if whoring >= 18: # Lv 7+  
        $ mag2 -= 1
        $ mad -= 15
        $ h_body = "03_hp/13_hermione_main/body_18.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
        show screen hermione_main                                                                                                                                                                                 #HERMIONE
        with d5    
        her "Последний выпуск \"Девченок\"?!"
        hide screen hermione_main                                                                                                                                                                                   #HERMIONE
        with d3                                                                                                                                                                                                                        #HERMIONE
        $ h_body = "03_hp/13_hermione_main/body_24.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
        show screen hermione_main                                                                                                                                                                                 #HERMIONE
        with d3                                                                                                                                                                                                                        #HERMIONE
        her "Нет ничего лучше этого журнала!"
        hide screen hermione_main                                                                                                                                                                                   #HERMIONE
        with d3    
        $ the_gift = "03_hp/18_store/18.png" # GIRLY MAGAZIES.
        show screen gift
        with d3
        ">Вы даете женские журналы Гермионе..."
        hide screen gift
        with d3
        $ h_body = "03_hp/13_hermione_main/body_08.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
        show screen hermione_main                                                                                                                                                                                 #HERMIONE
        with d3                                                                                                                                                                                                                        #HERMIONE
        her "Спасибо, сэр."
        call happy
        $ h_body = "03_hp/13_hermione_main/body_06.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE

 
    $ h_xpos=370 #Defines position of the Hermione's full length sprite. (Default 370). (Center: 140)                                                       #HERMIONE
    show screen hermione_main                                                                                                                                                                                 #HERMIONE
    with d3                                                                                                                                                                                                                        #HERMIONE
    jump day_time_requests        
        
        
        
                  ### Журналы для взрослых ###
label giving_mag3: 
    hide screen hermione_main                                                                                                                                                                                   #HERMIONE
    with d5                                                                                                                                                                                                                        #HERMIONE
    $ h_xpos=140 #Defines position of the Hermione's full length sprite. (Default 370). (Center: 140)                                                       #HERMIONE
    
    if whoring >= 0 and whoring <= 5: # Lv 1-2.
        $ mad += 7
        $ h_body = "03_hp/13_hermione_main/body_02.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
        show screen hermione_main                                                                                                                                                                                 #HERMIONE
        with d5                                                                                                                                                                                                                        #HERMIONE
        her "Это...?"
        hide screen hermione_main                                                                                                                                                                                   #HERMIONE
        with d3                                                                                                                                                                                                                        #HERMIONE
        $ h_body = "03_hp/13_hermione_main/body_31.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
        show screen hermione_main                                                                                                                                                                                 #HERMIONE
        with d3                                                                                                                                                                                                                        #HERMIONE
        her "Журналы для взрослых, сэр?"
        hide screen hermione_main                                                                                                                                                                                   #HERMIONE
        with d3                                                                                                                                                                                                                        #HERMIONE
        $ h_body = "03_hp/13_hermione_main/body_69.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
        show screen hermione_main                                                                                                                                                                                 #HERMIONE
        with d3                                                                                                                                                                                                                        #HERMIONE
        her "Учитывая ваш высокий статус?"
        hide screen hermione_main                                                                                                                                                                                   #HERMIONE
        with d3                                                                                                                                                                                                                        #HERMIONE
        $ h_body = "03_hp/13_hermione_main/body_66.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
        show screen hermione_main                                                                                                                                                                                 #HERMIONE
        with d3                                                                                                                                                                                                                        #HERMIONE
        her "Сэр, неужели вы не нашли более продуктивный способ провести свое время?"
        hide screen hermione_main                                                                                                                                                                                   #HERMIONE
        with d3                                                                                                                                                                                                                        #HERMIONE
        $ h_body = "03_hp/13_hermione_main/body_47.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
        show screen hermione_main                                                                                                                                                                                 #HERMIONE
        with d3                                                                                                                                                                                                                        #HERMIONE
        her "Я определенно не стану брать их..."
        call upset
        

    if whoring >= 6 and whoring <= 11: # Lv 3-4.
        $ mad += 3
        $ h_body = "03_hp/13_hermione_main/body_05.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
        show screen hermione_main                                                                                                                                                                                 #HERMIONE
        with d5                                                                                                                                                                                                                        #HERMIONE
        her "Журналы для взрослых?"
        hide screen hermione_main                                                                                                                                                                                   #HERMIONE
        with d3                                                                                                                                                                                                                        #HERMIONE
        $ h_body = "03_hp/13_hermione_main/body_69.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
        show screen hermione_main                                                                                                                                                                                 #HERMIONE
        with d3                                                                                                                                                                                                                        #HERMIONE
        her "Сэр, мне не интересно подобное."
        hide screen hermione_main                                                                                                                                                                                   #HERMIONE
        with d3                                                                                                                                                                                                                        #HERMIONE
        $ h_body = "03_hp/13_hermione_main/body_47.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
        show screen hermione_main                                                                                                                                                                                 #HERMIONE
        with d3                                                                                                                                                                                                                        #HERMIONE
        her "И это не очень уместный подарок для одного из ваших студентов."
        call upset
        $ h_body = "03_hp/13_hermione_main/body_29.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
        


    if whoring >= 12 and whoring <= 17: # Lv 5-6.
        $ mad -= 8 
        $ mag3 -= 1
        $ h_body = "03_hp/13_hermione_main/body_31.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
        show screen hermione_main                                                                                                                                                                                 #HERMIONE
        with d5     
        her "Журналы для взрослых?"
        hide screen hermione_main                                                                                                                                                                                   #HERMIONE
        with d3                                                                                                                                                                                                                        #HERMIONE
        $ h_body = "03_hp/13_hermione_main/body_34.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
        show screen hermione_main                                                                                                                                                                                 #HERMIONE
        with d3                                                                                                                                                                                                                        #HERMIONE
        her "Сэр, мне кажется это не подходящий подарок для девушки моего возраста..."
        hide screen hermione_main                                                                                                                                                                                   #HERMIONE
        with d3    
        $ the_gift = "03_hp/18_store/19.png" # ADULT MAGAZIES.
        show screen gift
        with d3
        ">Вы даете Гермионе несколько журналов для взрослых..."
        hide screen gift
        with d3
        $ h_body = "03_hp/13_hermione_main/body_79.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
        show screen hermione_main                                                                                                                                                                                 #HERMIONE
        with d3                                                                                                                                                                                                                        #HERMIONE
        her "Я уберу их подальше..."
        call happy
        $ h_body = "03_hp/13_hermione_main/body_120.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE


    if whoring >= 18: # Lv 7+  
        $ mag3 -= 1
        $ mad -= 15
        $ h_body = "03_hp/13_hermione_main/body_75.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
        show screen hermione_main                                                                                                                                                                                 #HERMIONE
        with d5  
        her "Новый выпуск \"Л.ю.б.в.и.\"!!!"
        hide screen hermione_main                                                                                                                                                                                   #HERMIONE
        with d3                                                                                                                                                                                                                        #HERMIONE
        $ h_body = "03_hp/13_hermione_main/body_122.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
        show screen hermione_main                                                                                                                                                                                 #HERMIONE
        with d3                                                                                                                                                                                                                        #HERMIONE
        her "Э-э...я имела в виду журналы для взрослых?"
        her "Это слегка опрометчиво..."
        hide screen hermione_main                                                                                                                                                                                   #HERMIONE
        with d3                                                                                                                                                                                                                        #HERMIONE
        $ h_body = "03_hp/13_hermione_main/body_74.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
        show screen hermione_main                                                                                                                                                                                 #HERMIONE
        with d3                                                                                                                                                                                                                        #HERMIONE
        her "Но я возьму их..."
        hide screen hermione_main                                                                                                                                                                                   #HERMIONE
        with d3    
        $ the_gift = "03_hp/18_store/19.png" # ADULT MAGAZIES.
        show screen gift
        with d3
        ">Вы даете Гермионе несколько журналов для взрослых..."
        hide screen gift
        with d3
        $ h_body = "03_hp/13_hermione_main/body_74.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
        show screen hermione_main                                                                                                                                                                                 #HERMIONE
        with d3                                                                                                                                                                                                                        #HERMIONE
        her "Спасибо, сэр."
        call happy
       

 
    $ h_xpos=370 #Defines position of the Hermione's full length sprite. (Default 370). (Center: 140)                                                       #HERMIONE
    show screen hermione_main                                                                                                                                                                                 #HERMIONE
    with d3                                                                                                                                                                                                                        #HERMIONE
    jump day_time_requests            
        
        
        
        
        
                      ### PORN MAGAZINES ###
label giving_mag4: 
    hide screen hermione_main                                                                                                                                                                                   #HERMIONE
    with d5                                                                                                                                                                                                                        #HERMIONE
    $ h_xpos=140 #Defines position of the Hermione's full length sprite. (Default 370). (Center: 140)                                                       #HERMIONE
    
    if whoring >= 0 and whoring <= 5: # Lv 1-2.
        $ mad += 15
        $ h_body = "03_hp/13_hermione_main/body_01.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
        show screen hermione_main                                                                                                                                                                                 #HERMIONE
        with d5                                                                                                                                                                                                                        #HERMIONE
        her "Хм... Что это?"
        hide screen hermione_main                                                                                                                                                                                   #HERMIONE
        with d3                                                                                                                                                                                                                        #HERMIONE
        $ h_body = "03_hp/13_hermione_main/body_130.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
        show screen hermione_main                                                                                                                                                                                 #HERMIONE
        with d3                                                                                                                                                                                                                        #HERMIONE
        her "Сэр, это порно журналы!"
        hide screen hermione_main                                                                                                                                                                                   #HERMIONE
        with d3                                                                                                                                                                                                                        #HERMIONE
        $ h_body = "03_hp/13_hermione_main/body_187.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
        show screen hermione_main                                                                                                                                                                                 #HERMIONE
        with d3                                                                                                                                                                                                                        #HERMIONE
        her "Вам должно быть стыдно!"
        call upset
        


    if whoring >= 6 and whoring <= 11: # Lv 3-4.
        $ mad += 8
        $ h_body = "03_hp/13_hermione_main/body_48.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
        show screen hermione_main                                                                                                                                                                                 #HERMIONE
        with d5                                                                                                                                                                                                                        #HERMIONE
        her "Порно журналы?"
        hide screen hermione_main                                                                                                                                                                                   #HERMIONE
        with d3                                                                                                                                                                                                                        #HERMIONE
        $ h_body = "03_hp/13_hermione_main/body_87.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
        show screen hermione_main                                                                                                                                                                                 #HERMIONE
        with d3                                                                                                                                                                                                                        #HERMIONE
        her "Сэр, что мне с ними делать?"
        hide screen hermione_main                                                                                                                                                                                   #HERMIONE
        with d3                                                                                                                                                                                                                        #HERMIONE
        $ h_body = "03_hp/13_hermione_main/body_79.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
        show screen hermione_main                                                                                                                                                                                 #HERMIONE
        with d3                                                                                                                                                                                                                        #HERMIONE
        her "Исследовать их?"
        hide screen hermione_main                                                                                                                                                                                   #HERMIONE
        with d3                                                                                                                                                                                                                        #HERMIONE
        $ h_body = "03_hp/13_hermione_main/body_86.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
        show screen hermione_main                                                                                                                                                                                 #HERMIONE
        with d3                                                                                                                                                                                                                        #HERMIONE
        her "Козел!"
        call upset
        $ h_body = "03_hp/13_hermione_main/body_120.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
        

    if whoring >= 12 and whoring <= 17: # Lv 5-6.
        $ mag4 -= 1
        $ h_body = "03_hp/13_hermione_main/body_31.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
        show screen hermione_main                                                                                                                                                                                 #HERMIONE
        with d5     
        her "Это жесткое порно."
        hide screen hermione_main                                                                                                                                                                                   #HERMIONE
        with d3                                                                                                                                                                                                                        #HERMIONE
        $ h_body = "03_hp/13_hermione_main/body_34.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
        show screen hermione_main                                                                                                                                                                                 #HERMIONE
        with d3                                                                                                                                                                                                                        #HERMIONE
        her "Не очень подходящий подарок для девушки моих лет!"
        hide screen hermione_main                                                                                                                                                                                   #HERMIONE
        with d3                                                                                                                                                                                                                        #HERMIONE
        $ h_body = "03_hp/13_hermione_main/body_118.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
        show screen hermione_main                                                                                                                                                                                 #HERMIONE
        with d3                                                                                                                                                                                                                        #HERMIONE
        her ".............."
        hide screen hermione_main                                                                                                                                                                                   #HERMIONE
        with d3                                                                                                                                                                                                                        #HERMIONE
        $ h_body = "03_hp/13_hermione_main/body_117.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
        show screen hermione_main                                                                                                                                                                                 #HERMIONE
        with d3                                                                                                                                                                                                                        #HERMIONE
        her "Но я возьму..."
        hide screen hermione_main                                                                                                                                                                                   #HERMIONE
        with d3    
        $ the_gift = "03_hp/18_store/20.png" # PORN MAGAZIES.
        show screen gift
        with d3
        ">Вы даете Гермионе несколько порно-журналов..."
        hide screen gift
        with d3
        $ h_body = "03_hp/13_hermione_main/body_79.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
        show screen hermione_main                                                                                                                                                                                 #HERMIONE
        with d3                                                                                                                                                                                                                        #HERMIONE
        her "И я выброшу их в мусорное ведро, где они и...девушки, которые любят такие вещи..."
        call no_change
        $ h_body = "03_hp/13_hermione_main/body_120.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
        

    if whoring >= 18: # Lv 7+  
        $ mag4 -= 1
        $ mad -= 15
        $ h_body = "03_hp/13_hermione_main/body_48.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
        show screen hermione_main                                                                                                                                                                                 #HERMIONE
        with d5  
        her "Порнография?"
        hide screen hermione_main                                                                                                                                                                                   #HERMIONE
        with d3                                                                                                                                                                                                                        #HERMIONE
        $ h_body = "03_hp/13_hermione_main/body_118.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
        show screen hermione_main                                                                                                                                                                                 #HERMIONE
        with d3                                                                                                                                                                                                                        #HERMIONE
        her "................"
        hide screen hermione_main                                                                                                                                                                                   #HERMIONE
        with d3                                                                                                                                                                                                                        #HERMIONE
        $ h_body = "03_hp/13_hermione_main/body_117.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
        show screen hermione_main                                                                                                                                                                                 #HERMIONE
        with d3                                                                                                                                                                                                                        #HERMIONE
        her "Как женщины вообще могут такое делать?"
        hide screen hermione_main                                                                                                                                                                                   #HERMIONE
        with d3                                                                                                                                                                                                                        #HERMIONE
        $ h_body = "03_hp/13_hermione_main/body_118.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
        show screen hermione_main                                                                                                                                                                                 #HERMIONE
        with d3                                                                                                                                                                                                                        #HERMIONE
        her "................."
        hide screen hermione_main                                                                                                                                                                                   #HERMIONE
        with d3                                                                                                                                                                                                                        #HERMIONE
        $ h_body = "03_hp/13_hermione_main/body_120.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
        show screen hermione_main                                                                                                                                                                                 #HERMIONE
        with d3                                                                                                                                                                                                                        #HERMIONE
        her "Ладно, я возьму их..."
        hide screen hermione_main                                                                                                                                                                                   #HERMIONE
        with d3                                                                                                                                                                                                                        #HERMIONE
        $ h_body = "03_hp/13_hermione_main/body_189.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
        show screen hermione_main                                                                                                                                                                                 #HERMIONE
        with d3                                                                                                                                                                                                                        #HERMIONE
        her "Исключительно для научных целей, конечно же..."
        hide screen hermione_main                                                                                                                                                                                   #HERMIONE
        with d3    
        $ the_gift = "03_hp/18_store/20.png" # PORN MAGAZIES.
        show screen gift
        with d3
        ">Вы даете Гермионе несколько порно-журналов..."
        hide screen gift
        with d3
        call happy
        $ h_body = "03_hp/13_hermione_main/body_45.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE

 
    $ h_xpos=370 #Defines position of the Hermione's full length sprite. (Default 370). (Center: 140)                                                       #HERMIONE
    show screen hermione_main                                                                                                                                                                                 #HERMIONE
    with d3                                                                                                                                                                                                                        #HERMIONE
    jump day_time_requests                
        
        
        
        
           
                      ### BUTTERBEER ###
label giving_beer: 
    hide screen hermione_main                                                                                                                                                                                   #HERMIONE
    with d5                                                                                                                                                                                                                        #HERMIONE
    $ h_xpos=140 #Defines position of the Hermione's full length sprite. (Default 370). (Center: 140)                                                       #HERMIONE
    
    if whoring >= 0 and whoring <= 5: # Lv 1-2.
        $ beer -= 1
        $ mad -= 3
        $ h_body = "03_hp/13_hermione_main/body_01.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
        show screen hermione_main                                                                                                                                                                                 #HERMIONE
        with d5                                                                                                                                                                                                                        #HERMIONE
        her "Сливочное пиво?"
        hide screen hermione_main                                                                                                                                                                                   #HERMIONE
        with d3                                                                                                                                                                                                                        #HERMIONE
        $ h_body = "03_hp/13_hermione_main/body_08.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
        show screen hermione_main                                                                                                                                                                                 #HERMIONE
        with d3                                                                                                                                                                                                                        #HERMIONE
        her "Вы уверены насчет этого?"
        hide screen hermione_main                                                                                                                                                                                   #HERMIONE
        with d3                                                                                                                                                                                                                        #HERMIONE
        $ h_body = "03_hp/13_hermione_main/body_06.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
        show screen hermione_main                                                                                                                                                                                 #HERMIONE
        with d3                                                                                                                                                                                                                        #HERMIONE
        her "Оно содержит алкоголь..."
        hide screen hermione_main                                                                                                                                                                                   #HERMIONE
        with d3    
        $ the_gift = "03_hp/18_store/21.png" # BUTTERBEER.
        show screen gift
        with d3
        ">Вы даете бутылку Гермионе..."
        hide screen gift
        with d3
        $ h_body = "03_hp/13_hermione_main/body_01.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
        show screen hermione_main                                                                                                                                                                                 #HERMIONE
        with d3                                                                                                                                                                                                                        #HERMIONE
        her "Спасибо вам."
        call happy
        


    if whoring >= 6 and whoring <= 11: # Lv 3-4.
        $ mad -= 10
        $ beer -= 1
        $ h_body = "03_hp/13_hermione_main/body_11.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
        show screen hermione_main                                                                                                                                                                                 #HERMIONE
        with d5                                                                                                                                                                                                                        #HERMIONE
        her "Сливочное пиво, сэр?"
        hide  screenhermione_main                                                                                                                                                                                   #HERMIONE
        with d3                                                                                                                                                                                                                        #HERMIONE
        $ h_body = "03_hp/13_hermione_main/body_14.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
        show screen hermione_main                                                                                                                                                                                 #HERMIONE
        with d3                                                                                                                                                                                                                        #HERMIONE
        her "Это будет наш маленький секрет..."
        hide screen hermione_main                                                                                                                                                                                   #HERMIONE
        with d3                                                                                                                                                                                                                        #HERMIONE
        $ h_body = "03_hp/13_hermione_main/body_06.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
        show screen hermione_main                                                                                                                                                                                 #HERMIONE
        with d3                                                                                                                                                                                                                        #HERMIONE
        her "Я большая поклонница этого безвредного напитка."
        hide screen hermione_main                                                                                                                                                                                   #HERMIONE
        with d3    
        $ the_gift = "03_hp/18_store/21.png" # BUTTERBEER.
        show screen gift
        with d3
        ">Вы даете бутылку Гермионе..."
        hide screen gift
        with d3
        $ h_body = "03_hp/13_hermione_main/body_01.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
        show screen hermione_main                                                                                                                                                                                 #HERMIONE
        with d3                                                                                                                                                                                                                        #HERMIONE
        her "Спасибо, сэр."
        call happy
        

        

    if whoring >= 12 and whoring <= 17: # Lv 5-6.
        $ mad -= 15
        $ beer -= 1
        $ h_body = "03_hp/13_hermione_main/body_01.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
        show screen hermione_main                                                                                                                                                                                 #HERMIONE
        with d5     
        her "Сливочное пиво?"
        hide screen hermione_main                                                                                                                                                                                   #HERMIONE
        with d3                                                                                                                                                                                                                        #HERMIONE
        $ h_body = "03_hp/13_hermione_main/body_24.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
        show screen hermione_main                                                                                                                                                                                 #HERMIONE
        with d3                                                                                                                                                                                                                        #HERMIONE
        her "Спасибо, сэр."
        hide screen hermione_main                                                                                                                                                                                   #HERMIONE
        with d3    
        $ the_gift = "03_hp/18_store/21.png" # BUTTERBEER.
        show screen gift
        with d3
        ">Вы даете бутылку Гермионе..."
        hide screen gift
        with d3
        $ h_body = "03_hp/13_hermione_main/body_06.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
        show screen hermione_main                                                                                                                                                                                 #HERMIONE
        with d3                                                                                                                                                                                                                        #HERMIONE
        her "Я выпью ее с девочками несколько позднее."
        call happy
        

    if whoring >= 18: # Lv 7+  
        $ mad -= 20
        $ beer -= 1
        $ h_body = "03_hp/13_hermione_main/body_06.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
        show screen hermione_main                                                                                                                                                                                 #HERMIONE
        with d5  
        her "Сливочное пиво...?"
        hide screen hermione_main                                                                                                                                                                                   #HERMIONE
        with d3                                                                                                                                                                                                                        #HERMIONE
        $ h_body = "03_hp/13_hermione_main/body_01.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
        show screen hermione_main                                                                                                                                                                                 #HERMIONE
        with d3                                                                                                                                                                                                                        #HERMIONE
        her "Спасибо, сэр."
        hide screen hermione_main                                                                                                                                                                                   #HERMIONE
        with d3    
        $ the_gift = "03_hp/18_store/21.png" # BUTTERBEER.
        show screen gift
        with d3
        ">Вы даете бутылку Гермионе..."
        hide screen gift
        with d3
        $ h_body = "03_hp/13_hermione_main/body_06.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
        show screen hermione_main                                                                                                                                                                                 #HERMIONE
        with d3                                                                                                                                                                                                                        #HERMIONE
        her "Я выпью ее с мальчишками несколько позднее."
        hide screen hermione_main                                                                                                                                                                                   #HERMIONE
        with d3                                                                                                                                                                                                                        #HERMIONE
        $ h_body = "03_hp/13_hermione_main/body_189.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
        show screen hermione_main                                                                                                                                                                                 #HERMIONE
        with d3                                                                                                                                                                                                                        #HERMIONE
        her "Э-э... Я хотела сказать с девочками, да."
        call happy
        $ h_body = "03_hp/13_hermione_main/body_01.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE

 
    $ h_xpos=370 #Defines position of the Hermione's full length sprite. (Default 370). (Center: 140)                                                       #HERMIONE
    show screen hermione_main                                                                                                                                                                                 #HERMIONE
    with d3                                                                                                                                                                                                                        #HERMIONE
    jump day_time_requests                
            
        
        
        
        
        
                   ### PLUSH OWL ###
label giving_owl: 
    hide screen hermione_main                                                                                                                                                                                   #HERMIONE
    with d5                                                                                                                                                                                                                        #HERMIONE
    $ h_xpos=140 #Defines position of the Hermione's full length sprite. (Default 370). (Center: 140)                                                       #HERMIONE
    
    if whoring >= 0 and whoring <= 5: # Lv 1-2.
        $ owl -= 1
        $ mad -= 7
        $ h_body = "03_hp/13_hermione_main/body_01.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
        show screen hermione_main                                                                                                                                                                                 #HERMIONE
        with d5                                                                                                                                                                                                                        #HERMIONE
        her "Плюшевая сова?"
        hide screen hermione_main                                                                                                                                                                                   #HERMIONE
        with d3                                                                                                                                                                                                                        #HERMIONE
        $ h_body = "03_hp/13_hermione_main/body_06.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
        show screen hermione_main                                                                                                                                                                                 #HERMIONE
        with d3                                                                                                                                                                                                                        #HERMIONE
        her "Это мило..."
        hide screen hermione_main                                                                                                                                                                                   #HERMIONE
        with d3    
        $ the_gift = "03_hp/18_store/22.png" # PLUSH OWL.
        show screen gift
        with d3
        ">Вы даете Гермионе плюшевую сову..."
        hide screen gift
        with d3
        $ h_body = "03_hp/13_hermione_main/body_01.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
        show screen hermione_main                                                                                                                                                                                 #HERMIONE
        with d3                                                                                                                                                                                                                        #HERMIONE
        her "Спасибо, сэр."
        call happy
        
      

    if whoring >= 6 and whoring <= 11: # Lv 3-4.
        $ mad -= 10
        $ owl -= 1
        $ h_body = "03_hp/13_hermione_main/body_11.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
        show screen hermione_main                                                                                                                                                                                 #HERMIONE
        with d5                                                                                                                                                                                                                        #HERMIONE
        her "Плюшевая сова?"
        hide screen hermione_main                                                                                                                                                                                   #HERMIONE
        with d3                                                                                                                                                                                                                        #HERMIONE
        $ h_body = "03_hp/13_hermione_main/body_06.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
        show screen hermione_main                                                                                                                                                                                 #HERMIONE
        with d3                                                                                                                                                                                                                        #HERMIONE
        her "Мне нравится!"
        hide screen hermione_main                                                                                                                                                                                   #HERMIONE
        with d3    
        $ the_gift = "03_hp/18_store/22.png" # PLUSH OWL.
        show screen gift
        with d3
        ">Вы даете Гермионе плюшевую сову..."
        hide screen gift
        with d3
        $ h_body = "03_hp/13_hermione_main/body_01.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
        show screen hermione_main                                                                                                                                                                                 #HERMIONE
        with d3                                                                                                                                                                                                                        #HERMIONE
        her "Спасибо, сэр."
        call happy

    if whoring >= 12 and whoring <= 17: # Lv 5-6.
        $ mad -= 15
        $ owl -= 1
        $ h_body = "03_hp/13_hermione_main/body_01.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
        show screen hermione_main                                                                                                                                                                                 #HERMIONE
        with d5     
        her "Игрушка?"
        hide screen hermione_main                                                                                                                                                                                   #HERMIONE
        with d3                                                                                                                                                                                                                        #HERMIONE
        $ h_body = "03_hp/13_hermione_main/body_02.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
        show screen hermione_main                                                                                                                                                                                 #HERMIONE
        with d3                                                                                                                                                                                                                        #HERMIONE
        her "Игрушки для детей, сэр."
        hide screen hermione_main                                                                                                                                                                                   #HERMIONE
        with d3                                                                                                                                                                                                                        #HERMIONE
        $ h_body = "03_hp/13_hermione_main/body_29.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
        show screen hermione_main                                                                                                                                                                                 #HERMIONE
        with d3                                                                                                                                                                                                                        #HERMIONE
        her "Но я возьму..."
        hide screen hermione_main                                                                                                                                                                                   #HERMIONE
        with d3    
        $ the_gift = "03_hp/18_store/22.png" # PLUSH OWL.
        show screen gift
        with d3
        ">Вы даете Гермионе плюшевую сову..."
        hide screen gift
        with d3
        $ h_body = "03_hp/13_hermione_main/body_01.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
        show screen hermione_main                                                                                                                                                                                 #HERMIONE
        with d3                                                                                                                                                                                                                        #HERMIONE
        her "Спасибо, сэр."
        call happy
        
        
        
      
    if whoring >= 18: # Lv 7+  
        $ mad -= 4
        $ owl -= 1
        $ h_body = "03_hp/13_hermione_main/body_66.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
        show screen hermione_main                                                                                                                                                                                 #HERMIONE
        with d5  
        her "Это что-то из игрушек для взрослых?"
        hide screen hermione_main                                                                                                                                                                                   #HERMIONE
        with d3                                                                                                                                                                                                                        #HERMIONE
        $ h_body = "03_hp/13_hermione_main/body_87.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
        show screen hermione_main                                                                                                                                                                                 #HERMIONE
        with d3                                                                                                                                                                                                                        #HERMIONE
        her "Где-то есть переключатель или кнопка..."
        hide screen hermione_main                                                                                                                                                                                   #HERMIONE
        with d3                                                                                                                                                                                                                        #HERMIONE
        $ h_body = "03_hp/13_hermione_main/body_124.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
        show screen hermione_main                                                                                                                                                                                 #HERMIONE
        with d3                                                                                                                                                                                                                        #HERMIONE
        her "И так...оно вибрирует или как?"
        hide screen hermione_main                                                                                                                                                                                   #HERMIONE
        with d3                                                                                                                                                                                                                        #HERMIONE
        $ h_body = "03_hp/13_hermione_main/body_190.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
        show screen hermione_main                                                                                                                                                                                 #HERMIONE
        with d3                                                                                                                                                                                                                        #HERMIONE
        her "Ох...?"
        her "Так это действительно просто плюшевая сова?"
        hide screen hermione_main                                                                                                                                                                                   #HERMIONE
        with d3                                                                                                                                                                                                                        #HERMIONE
        $ h_body = "03_hp/13_hermione_main/body_118.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
        show screen hermione_main                                                                                                                                                                                 #HERMIONE
        with d3                                                                                                                                                                                                                        #HERMIONE
        her "Стыдно..."
        hide screen hermione_main                                                                                                                                                                                   #HERMIONE
        with d3                                                                                                                                                                                                                        #HERMIONE
        $ h_body = "03_hp/13_hermione_main/body_34.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
        show screen hermione_main                                                                                                                                                                                 #HERMIONE
        with d3                                                                                                                                                                                                                        #HERMIONE
        her "То есть, Спасибо, сэр."
        hide screen hermione_main                                                                                                                                                                                   #HERMIONE
        with d3    
        $ the_gift = "03_hp/18_store/22.png" # PLUSH OWL.
        show screen gift
        with d3
        ">Вы даете Гермионе плюшевую сову..."
        hide screen gift
        with d3
        $ h_body = "03_hp/13_hermione_main/body_01.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
        call happy

    $ h_xpos=370 #Defines position of the Hermione's full length sprite. (Default 370). (Center: 140)                                                       #HERMIONE
    show screen hermione_main                                                                                                                                                                                 #HERMIONE
    with d3                                                                                                                                                                                                                        #HERMIONE
    jump day_time_requests                
    
    
    
        
     ### SEX DOLL ###
label giving_sexdoll: 
    hide screen hermione_main                                                                                                                                                                                   #HERMIONE
    with d5                                                                                                                                                                                                                        #HERMIONE
    $ h_xpos=140 #Defines position of the Hermione's full length sprite. (Default 370). (Center: 140)                                                       #HERMIONE
    
    if whoring >= 0 and whoring <= 5: # Lv 1-2.
        $ mad += 20
        $ h_body = "03_hp/13_hermione_main/body_48.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
        show screen hermione_main                                                                                                                                                                                 #HERMIONE
        with d5                                                                                                                                                                                                                        #HERMIONE
        her "Это..."
        hide screen hermione_main                                                                                                                                                                                   #HERMIONE
        with d3                                                                                                                                                                                                                        #HERMIONE
        $ h_body = "03_hp/13_hermione_main/body_34.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
        show screen hermione_main                                                                                                                                                                                 #HERMIONE
        with d3                                                                                                                                                                                                                        #HERMIONE
        her "Секс-кукла?!"
        hide screen hermione_main                                                                                                                                                                                   #HERMIONE
        with d3                                                                                                                                                                                                                        #HERMIONE
        $ h_body = "03_hp/13_hermione_main/body_32.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
        show screen hermione_main                                                                                                                                                                                 #HERMIONE
        with d3                                                                                                                                                                                                                        #HERMIONE
        her "Профессор Дамблдор!!!"
        call upset
        $ h_body = "03_hp/13_hermione_main/body_33.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
      

    if whoring >= 6 and whoring <= 11: # Lv 3-4.
        $ mad += 20
        $ h_body = "03_hp/13_hermione_main/body_48.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
        show screen hermione_main                                                                                                                                                                                 #HERMIONE
        with d5                                                                                                                                                                                                                        #HERMIONE
        her "Секс-кукла?"
        hide screen hermione_main                                                                                                                                                                                   #HERMIONE
        with d3                                                                                                                                                                                                                        #HERMIONE
        $ h_body = "03_hp/13_hermione_main/body_120.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
        show screen hermione_main                                                                                                                                                                                 #HERMIONE
        with d3                                                                                                                                                                                                                        #HERMIONE
        her "Это очень неприлично, для такого как вы..."
        call upset

    if whoring >= 12 and whoring <= 17: # Lv 5-6.
        $ mad -= 10
        $ sexdoll -= 1
        $ h_body = "03_hp/13_hermione_main/body_118.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
        show screen hermione_main                                                                                                                                                                                 #HERMIONE
        with d5     
        her "Секс-кукла..."
        hide screen hermione_main                                                                                                                                                                                   #HERMIONE
        with d3                                                                                                                                                                                                                        #HERMIONE
        $ h_body = "03_hp/13_hermione_main/body_120.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
        show screen hermione_main                                                                                                                                                                                 #HERMIONE
        with d3                                                                                                                                                                                                                        #HERMIONE
        her "Это немного неуместно..."
        hide screen hermione_main                                                                                                                                                                                   #HERMIONE
        with d3                                                                                                                                                                                                                        #HERMIONE
        $ h_body = "03_hp/13_hermione_main/body_124.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
        show screen hermione_main                                                                                                                                                                                 #HERMIONE
        with d3                                                                                                                                                                                                                        #HERMIONE
        her "Но может мы сможешь использовать ее для розыгрышей или вроде того..."
        hide screen hermione_main                                                                                                                                                                                   #HERMIONE
        with d3    
        $ the_gift = "03_hp/18_store/23.png" # SEX DOLL.
        show screen gift
        with d3
        ">Вы даете Гермионе секс-куклу..."
        hide screen gift
        with d3
        $ h_body = "03_hp/13_hermione_main/body_124.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
        show screen hermione_main                                                                                                                                                                                 #HERMIONE
        with d3                                                                                                                                                                                                                        #HERMIONE
        her "Спасибо, сэр."
        call happy
        
    if whoring >= 18: # Lv 7+  
        $ mad -= 30
        $ sexdoll -= 1
        $ h_body = "03_hp/13_hermione_main/body_73.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
        show screen hermione_main                                                                                                                                                                                 #HERMIONE
        with d5  
        her "Секс-кукла Джуанна?"
        hide screen hermione_main                                                                                                                                                                                   #HERMIONE
        with d3                                                                                                                                                                                                                        #HERMIONE
        $ h_body = "03_hp/13_hermione_main/body_189.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
        show screen hermione_main                                                                                                                                                                                 #HERMIONE
        with d3                                                                                                                                                                                                                        #HERMIONE
        her "Я не сказал бы, что одобряю подобное..."
        hide screen hermione_main                                                                                                                                                                                   #HERMIONE
        with d3                                                                                                                                                                                                                        #HERMIONE
        $ h_body = "03_hp/13_hermione_main/body_124.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
        show screen hermione_main                                                                                                                                                                                 #HERMIONE
        with d3                                                                                                                                                                                                                        #HERMIONE
        her "Но знаю, что Гарри хотел бы такую..."
        hide screen hermione_main                                                                                                                                                                                   #HERMIONE
        with d3    
        $ the_gift = "03_hp/18_store/23.png" # SEX DOLL.
        show screen gift
        with d3
        ">Вы даете Гермионе секс-куклу..."
        hide screen gift
        with d3
        $ h_body = "03_hp/13_hermione_main/body_188.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
        show screen hermione_main                                                                                                                                                                                 #HERMIONE
        with d3                                                                                                                                                                                                                        #HERMIONE
        her "Спасибо, сэр."
        call happy
        

        
    $ h_xpos=370 #Defines position of the Hermione's full length sprite. (Default 370). (Center: 140)                                                       #HERMIONE
    show screen hermione_main                                                                                                                                                                                 #HERMIONE
    with d3                                                                                                                                                                                                                        #HERMIONE
    jump day_time_requests                
        
        
      ### SEXY LINGERIE ###
label giving_lingerie: 
    hide screen hermione_main                                                                                                                                                                                   #HERMIONE
    with d5                                                                                                                                                                                                                        #HERMIONE
    $ h_xpos=140 #Defines position of the Hermione's full length sprite. (Default 370). (Center: 140)                                                       #HERMIONE
    
    if whoring >= 0 and whoring <= 5: # Lv 1-2.
        $ mad += 10
        $ h_body = "03_hp/13_hermione_main/body_118.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
        show screen hermione_main                                                                                                                                                                                 #HERMIONE
        with d5                                                                                                                                                                                                                        #HERMIONE
        her "Нижнее белье?"
        hide screen hermione_main                                                                                                                                                                                   #HERMIONE
        with d3                                                                                                                                                                                                                        #HERMIONE
        $ h_body = "03_hp/13_hermione_main/body_120.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
        show screen hermione_main                                                                                                                                                                                 #HERMIONE
        with d3                                                                                                                                                                                                                        #HERMIONE
        her "Сэр, я не могу принять от вас такой подарок.."
        call upset
       
      

    if whoring >= 6 and whoring <= 11: # Lv 3-4.
        $ h_body = "03_hp/13_hermione_main/body_118.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
        show screen hermione_main                                                                                                                                                                                 #HERMIONE
        with d5                                                                                                                                                                                                                        #HERMIONE
        her "Сексуальное нижнее белье?"
        hide screen hermione_main                                                                                                                                                                                   #HERMIONE
        with d3                                                                                                                                                                                                                        #HERMIONE
        $ h_body = "03_hp/13_hermione_main/body_117.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
        show screen hermione_main                                                                                                                                                                                 #HERMIONE
        with d3                                                                                                                                                                                                                        #HERMIONE
        her "Вы ведь знаете, что я не могу принять этот подарок."
        hide screen hermione_main                                                                                                                                                                                   #HERMIONE
        with d3                                                                                                                                                                                                                        #HERMIONE
        $ h_body = "03_hp/13_hermione_main/body_118.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
        show screen hermione_main                                                                                                                                                                                 #HERMIONE
        with d3                                                                                                                                                                                                                        #HERMIONE
        her "(Хотя оно довольно милое)........."
        call no_change

    if whoring >= 12 and whoring <= 17: # Lv 5-6.
        $ mad -= 7
        $ lingerie -= 1
        $ h_body = "03_hp/13_hermione_main/body_124.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
        show screen hermione_main                                                                                                                                                                                 #HERMIONE
        with d5     
        her "Сексуальное нижнее белье?"
        hide screen hermione_main                                                                                                                                                                                   #HERMIONE
        with d3                                                                                                                                                                                                                        #HERMIONE
        $ h_body = "03_hp/13_hermione_main/body_122.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
        show screen hermione_main                                                                                                                                                                                 #HERMIONE
        with d3                                                                                                                                                                                                                        #HERMIONE
        her "Сэр, это несколько неуместно..."
        hide screen hermione_main                                                                                                                                                                                   #HERMIONE
        with d3    
        $ the_gift = "03_hp/18_store/24.png" # SEXY LINGERIE.
        show screen gift
        with d3
        ">Вы даете Гермионе сексуальное нижнее белье..."
        hide screen gift
        with d3
        $ h_body = "03_hp/13_hermione_main/body_188.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
        show screen hermione_main                                                                                                                                                                                 #HERMIONE
        with d3                                                                                                                                                                                                                        #HERMIONE
        her "Спасибо, сэр."
        call happy

        
    if whoring >= 18: # Lv 7+  
        $ mad -= 15
        $ lingerie -= 1
        $ h_body = "03_hp/13_hermione_main/body_124.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
        show screen hermione_main                                                                                                                                                                                 #HERMIONE
        with d5  
        her "Сексуальное нижнее белье?"
        hide screen hermione_main                                                                                                                                                                                   #HERMIONE
        with d3                                                                                                                                                                                                                        #HERMIONE
        $ h_body = "03_hp/13_hermione_main/body_123.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
        show screen hermione_main                                                                                                                                                                                 #HERMIONE
        with d3                                                                                                                                                                                                                        #HERMIONE
        her "Как вам кажется, я могу стать похожей на одну из ведьм из тех журналов для взрослых?"
        hide screen hermione_main                                                                                                                                                                                   #HERMIONE
        with d3                                                                                                                                                                                                                        #HERMIONE
        $ h_body = "03_hp/13_hermione_main/body_122.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
        show screen hermione_main                                                                                                                                                                                 #HERMIONE
        with d3                                                                                                                                                                                                                        #HERMIONE
        her "Ох... То есть, спасибо, сэр."
        hide screen hermione_main                                                                                                                                                                                   #HERMIONE
        with d3    
        $ the_gift = "03_hp/18_store/24.png" # SEXY LINGERIE.
        show screen gift
        with d3
        ">Вы даете Гермионе сексуальное нижнее белье..."
        hide screen gift
        with d3
        call happy
        

    $ h_xpos=370 #Defines position of the Hermione's full length sprite. (Default 370). (Center: 140)                                                       #HERMIONE
    show screen hermione_main                                                                                                                                                                                 #HERMIONE
    with d3                                                                                                                                                                                                                        #HERMIONE
    jump day_time_requests                
        
    ### BROOM ###
label giving_broom: 
    hide screen hermione_main                                                                                                                                                                                   #HERMIONE
    with d5                                                                                                                                                                                                                        #HERMIONE
    $ h_xpos=140 #Defines position of the Hermione's full length sprite. (Default 370). (Center: 140)                                                       #HERMIONE
    
    if whoring >= 0 and whoring <= 5: # Lv 1-2.
        $ mad -= 20
        $ broom -= 1
        $ h_body = "03_hp/13_hermione_main/body_01.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
        show screen hermione_main                                                                                                                                                                                 #HERMIONE
        with d5                                                                                                                                                                                                                        #HERMIONE
        her "Метла...?"
        hide screen hermione_main                                                                                                                                                                                   #HERMIONE
        with d3                                                                                                                                                                                                                        #HERMIONE
        $ h_body = "03_hp/13_hermione_main/body_03.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
        show screen hermione_main                                                                                                                                                                                 #HERMIONE
        with d3                                                                                                                                                                                                                        #HERMIONE
        her "Хм..."
        hide screen hermione_main                                                                                                                                                                                   #HERMIONE
        with d3                                                                                                                                                                                                                        #HERMIONE
        $ h_body = "03_hp/13_hermione_main/body_07.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
        show screen hermione_main                                                                                                                                                                                 #HERMIONE
        with d3                                                                                                                                                                                                                        #HERMIONE
        her "Что это за странные штуки на ней?"
        hide screen hermione_main                                                                                                                                                                                   #HERMIONE
        with d3                                                                                                                                                                                                                        #HERMIONE
        $ h_body = "03_hp/13_hermione_main/body_08.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
        show screen hermione_main                                                                                                                                                                                 #HERMIONE
        with d3                                                                                                                                                                                                                        #HERMIONE
        her "Выглядит как седло...?"
        hide screen hermione_main                                                                                                                                                                                   #HERMIONE
        with d3    
        $ the_gift = "03_hp/18_store/25.png" # BROOM
        show screen gift
        with d3
        ">Вы даете метлу Гермионе..."
        hide screen gift
        with d3
        $ h_body = "03_hp/13_hermione_main/body_11.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
        show screen hermione_main                                                                                                                                                                                 #HERMIONE
        with d3                                                                                                                                                                                                                        #HERMIONE
        her "Спасибо вам за подарок, сэр."
        $ h_body = "03_hp/13_hermione_main/body_06.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
        call happy
       
      

    if whoring >= 6 and whoring <= 11: # Lv 3-4.
        $ mad -= 20
        $ broom -= 1
        $ h_body = "03_hp/13_hermione_main/body_01.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
        show screen hermione_main                                                                                                                                                                                 #HERMIONE
        with d5                                                                                                                                                                                                                        #HERMIONE
        her "Метла...?"
        hide screen hermione_main                                                                                                                                                                                   #HERMIONE
        with d3                                                                                                                                                                                                                        #HERMIONE
        $ h_body = "03_hp/13_hermione_main/body_07.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
        show screen hermione_main                                                                                                                                                                                 #HERMIONE
        with d3                                                                                                                                                                                                                        #HERMIONE
        her "Хм..."
        hide screen hermione_main                                                                                                                                                                                   #HERMIONE
        with d3                                                                                                                                                                                                                        #HERMIONE
        $ h_body = "03_hp/13_hermione_main/body_05.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
        show screen hermione_main                                                                                                                                                                                 #HERMIONE
        with d3                                                                                                                                                                                                                        #HERMIONE
        her "Это какая-то секс-игрушка, не так ли?"
        hide screen hermione_main                                                                                                                                                                                   #HERMIONE
        with d3                                                                                                                                                                                                                        #HERMIONE
        $ h_body = "03_hp/13_hermione_main/body_87.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
        show screen hermione_main                                                                                                                                                                                 #HERMIONE
        with d3                                                                                                                                                                                                                        #HERMIONE
        her "Ну, неплохо сделано..."
        hide screen hermione_main                                                                                                                                                                                   #HERMIONE
        with d3    
        $ the_gift = "03_hp/18_store/25.png" # BROOM
        show screen gift
        with d3
        ">Вы даете метлу Гермионе..."
        hide screen gift
        with d3
        $ h_body = "03_hp/13_hermione_main/body_120.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
        show screen hermione_main                                                                                                                                                                                 #HERMIONE
        with d3                                                                                                                                                                                                                        #HERMIONE
        her "Спасибо, сэр."
        call happy
        
        
    if whoring >= 12 and whoring <= 17: # Lv 5-6.
        $ mad -= 30
        $ broom -= 1
        $ h_body = "03_hp/13_hermione_main/body_118.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
        show screen hermione_main                                                                                                                                                                                 #HERMIONE
        with d5     
        her "Метла...?"
        her "Хм..."
        hide screen hermione_main                                                                                                                                                                                   #HERMIONE
        with d3                                                                                                                                                                                                                        #HERMIONE
        $ h_body = "03_hp/13_hermione_main/body_66.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
        show screen hermione_main                                                                                                                                                                                 #HERMIONE
        with d3                                                                                                                                                                                                                        #HERMIONE
        her "Что это за седло...?"
        hide screen hermione_main                                                                                                                                                                                   #HERMIONE
        with d3                                                                                                                                                                                                                        #HERMIONE
        $ h_body = "03_hp/13_hermione_main/body_127.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
        show screen hermione_main                                                                                                                                                                                 #HERMIONE
        with d3                                                                                                                                                                                                                        #HERMIONE
        her "Ну, не важно."
        her "Отказываться от дорогого подарка было бы глупо..."
        hide screen hermione_main                                                                                                                                                                                   #HERMIONE
        with d3    
        $ the_gift = "03_hp/18_store/25.png" # BROOM
        show screen gift
        with d3
        ">Вы даете метлу Гермионе..."
        hide screen gift
        with d3
        $ h_body = "03_hp/13_hermione_main/body_120.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
        show screen hermione_main                                                                                                                                                                                 #HERMIONE
        with d3                                                                                                                                                                                                                        #HERMIONE
        her "Спасибо, сэр."
        call happy

    if whoring >= 18: # Lv 7+  
        $ mad -= 30
        $ broom -= 1
        $ h_body = "03_hp/13_hermione_main/body_124.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
        show screen hermione_main                                                                                                                                                                                 #HERMIONE
        with d5  
        her "Метла..."
        her "Хм..."
        hide screen hermione_main                                                                                                                                                                                   #HERMIONE
        with d3                                                                                                                                                                                                                        #HERMIONE
        $ h_body = "03_hp/13_hermione_main/body_189.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
        show screen hermione_main                                                                                                                                                                                 #HERMIONE
        with d3                                                                                                                                                                                                                        #HERMIONE
        her "Это седло, сэр..."
        hide screen hermione_main                                                                                                                                                                                   #HERMIONE
        with d3                                                                                                                                                                                                                        #HERMIONE
        $ h_body = "03_hp/13_hermione_main/body_190.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
        show screen hermione_main                                                                                                                                                                                 #HERMIONE
        with d3                                                                                                                                                                                                                        #HERMIONE
        her "Оно было разработано специально для меня, не так ли?"
        hide screen hermione_main                                                                                                                                                                                   #HERMIONE
        with d3                                                                                                                                                                                                                        #HERMIONE
        $ h_body = "03_hp/13_hermione_main/body_185.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
        show screen hermione_main                                                                                                                                                                                 #HERMIONE
        with d3                                                                                                                                                                                                                        #HERMIONE
        her "Я не уверена, неуместно это или разумно..."
        hide screen hermione_main                                                                                                                                                                                   #HERMIONE
        with d3                                                                                                                                                                                                                        #HERMIONE
        $ h_body = "03_hp/13_hermione_main/body_129.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
        show screen hermione_main                                                                                                                                                                                 #HERMIONE
        with d3                                                                                                                                                                                                                        #HERMIONE
        her "Но это идеальное инженерное решение..."
        hide screen hermione_main                                                                                                                                                                                   #HERMIONE
        with d3    
        $ the_gift = "03_hp/18_store/25.png" # BROOM
        show screen gift
        with d3
        ">Вы даете метлу Гермионе..."
        hide screen gift
        with d3
        $ h_body = "03_hp/13_hermione_main/body_128.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
        show screen hermione_main                                                                                                                                                                                 #HERMIONE
        with d3                                                                                                                                                                                                                        #HERMIONE
        her "Спасибо, сэр."
        call happy


    $ h_xpos=370 #Defines position of the Hermione's full length sprite. (Default 370). (Center: 140)                                                       #HERMIONE
    show screen hermione_main                                                                                                                                                                                 #HERMIONE
    with d3                                                                                                                                                                                                                        #HERMIONE
    jump day_time_requests                
        
    ### KRUM POSTER ###
label giving_krum: 
    hide screen hermione_main                                                                                                                                                                                   #HERMIONE
    with d5                                                                                                                                                                                                                        #HERMIONE
    $ h_xpos=140 #Defines position of the Hermione's full length sprite. (Default 370). (Center: 140)                                                       #HERMIONE
    
    if whoring >= 0 and whoring <= 5: # Lv 1-2.
        $ h_body = "03_hp/13_hermione_main/body_73.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
        show screen hermione_main                                                                                                                                                                                 #HERMIONE
        with d5                                                                                                                                                                                                                        #HERMIONE
        her "Постер Квиддича?"
        hide screen hermione_main                                                                                                                                                                                   #HERMIONE
        with d3                                                                                                                                                                                                                        #HERMIONE
        $ h_body = "03_hp/13_hermione_main/body_185.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
        show screen hermione_main                                                                                                                                                                                 #HERMIONE
        with d3                                                                                                                                                                                                                        #HERMIONE
        her "Что мне с этим делать, сэр?"
        hide screen hermione_main                                                                                                                                                                                   #HERMIONE
        with d3                                                                                                                                                                                                                        #HERMIONE
        $ h_body = "03_hp/13_hermione_main/body_184.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
        show screen hermione_main                                                                                                                                                                                 #HERMIONE
        with d3                                                                                                                                                                                                                        #HERMIONE
        her "Нет, Спасибо."
        call no_change
        $ h_body = "03_hp/13_hermione_main/body_71.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
       


    if whoring >= 6 and whoring <= 11: # Lv 3-4.
        $ mad -= 1
        $ krum -= 1
        $ h_body = "03_hp/13_hermione_main/body_73.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
        show screen hermione_main                                                                                                                                                                                 #HERMIONE
        with d5                                                                                                                                                                                                                        #HERMIONE
        her "Постер по Квиддичу?"
        hide screen hermione_main                                                                                                                                                                                   #HERMIONE
        with d3                                                                                                                                                                                                                        #HERMIONE
        $ h_body = "03_hp/13_hermione_main/body_185.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
        show screen hermione_main                                                                                                                                                                                 #HERMIONE
        with d3                                                                                                                                                                                                                        #HERMIONE
        her "Хм..."
        hide screen hermione_main                                                                                                                                                                                   #HERMIONE
        with d3                                                                                                                                                                                                                        #HERMIONE
        $ h_body = "03_hp/13_hermione_main/body_71.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
        show screen hermione_main                                                                                                                                                                                 #HERMIONE
        with d3                                                                                                                                                                                                                        #HERMIONE
        her "Мне кажется, я видела этого игрока пару раз..."
        hide screen hermione_main                                                                                                                                                                                   #HERMIONE
        with d3                                                                                                                                                                                                                        #HERMIONE
        $ h_body = "03_hp/13_hermione_main/body_06.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
        show screen hermione_main                                                                                                                                                                                 #HERMIONE
        with d3                                                                                                                                                                                                                        #HERMIONE
        her "Это тот студент из Дурмштранга?"
        hide screen hermione_main                                                                                                                                                                                   #HERMIONE
        with d3    
        $ the_gift = "03_hp/18_store/26.png" # KRUM POSTER.
        show screen gift
        with d3
        ">Вы даете постер Гермионе..."
        hide screen gift
        with d3
        call happy
        

        
    if whoring >= 12 and whoring <= 17: # Lv 5-6.
        $ mad -= 15
        $ krum -= 1
        $ h_body = "03_hp/13_hermione_main/body_73.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
        show screen hermione_main                                                                                                                                                                                 #HERMIONE
        with d5     
        her "Постер Виктора Крама, сэр?"
        hide screen hermione_main                                                                                                                                                                                   #HERMIONE
        with d3                                                                                                                                                                                                                        #HERMIONE
        $ h_body = "03_hp/13_hermione_main/body_08.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
        show screen hermione_main                                                                                                                                                                                 #HERMIONE
        with d3                                                                                                                                                                                                                        #HERMIONE
        her "Ну, я немного интересуюсь квиддичем..."
        hide screen hermione_main                                                                                                                                                                                   #HERMIONE
        with d3                                                                                                                                                                                                                        #HERMIONE
        $ h_body = "03_hp/13_hermione_main/body_87.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
        show screen hermione_main                                                                                                                                                                                 #HERMIONE
        with d3                                                                                                                                                                                                                        #HERMIONE
        her "Я могу понять, что девушки находят в этих перекачаных парнях..."
        hide screen hermione_main                                                                                                                                                                                   #HERMIONE
        with d3    
        $ the_gift = "03_hp/18_store/26.png" # KRUM POSTER.
        show screen gift
        with d3
        ">Вы даете постер Гермионе..."
        hide screen gift
        with d3
        call happy
        
        
       
    if whoring >= 18: # Lv 7+  
        $ mad -= 25
        $ krum -= 1
        $ h_body = "03_hp/13_hermione_main/body_72.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
        show screen hermione_main                                                                                                                                                                                 #HERMIONE
        with d5  
        her "Постер Виктора Крама?!"
        hide screen hermione_main                                                                                                                                                                                   #HERMIONE
        with d3                                                                                                                                                                                                                        #HERMIONE
        $ h_body = "03_hp/13_hermione_main/body_24.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
        show screen hermione_main                                                                                                                                                                                 #HERMIONE
        with d3                                                                                                                                                                                                                        #HERMIONE
        her "Спасибо, сэр!"
        hide screen hermione_main                                                                                                                                                                                   #HERMIONE
        with d3    
        $ the_gift = "03_hp/18_store/26.png" # KRUM POSTER.
        show screen gift
        with d3
        ">Вы даете постер Гермионе..."
        hide screen gift
        with d3
        $ h_body = "03_hp/13_hermione_main/body_46.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
        show screen hermione_main                                                                                                                                                                                 #HERMIONE
        with d3                                                                                                                                                                                                                        #HERMIONE
        her "Не могу дождаться, чтобы повесить его над своей кроватью!"
        hide screen hermione_main                                                                                                                                                                                   #HERMIONE
        with d3                                                                                                                                                                                                                        #HERMIONE
        $ h_body = "03_hp/13_hermione_main/body_64.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
        show screen hermione_main                                                                                                                                                                                 #HERMIONE
        with d3                                                                                                                                                                                                                        #HERMIONE
        her "Девченки обзавидуются..."
        call happy


    $ h_xpos=370 #Defines position of the Hermione's full length sprite. (Default 370). (Center: 140)                                                       #HERMIONE
    show screen hermione_main                                                                                                                                                                                 #HERMIONE
    with d3                                                                                                                                                                                                                        #HERMIONE
    jump day_time_requests                    
        
        
        
        
        
     ### S.P.E.W. BADGE ###
label giving_badge_01: 
    hide screen hermione_main                                                                                                                                                                                   #HERMIONE
    with d5                                                                                                                                                                                                                        #HERMIONE
    $ h_xpos=140 #Defines position of the Hermione's full length sprite. (Default 370). (Center: 140)                                                       #HERMIONE
    

    $ mad -= 30
    $ badge_01 = 7 # Means already gifted.
    $ h_body = "03_hp/13_hermione_main/body_01.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
    show screen hermione_main                                                                                                                                                                                 #HERMIONE
    with d5                                                                                                                                                                                                                        #HERMIONE
    her "Значок?"
    hide screen hermione_main                                                                                                                                                                                   #HERMIONE
    with d3                                                                                                                                                                                                                        #HERMIONE
    $ the_gift = "03_hp/18_store/29.png" # S.P.E.W. BADGE.
    show screen gift
    with d3
    ">Вы даете значок Гермионе...\n>Значок \"А.В.Н.Э.\" был добавлен в гардероб Гермионы."
    hide screen gift

    $ dress_code = True

    $ h_body = "03_hp/13_hermione_main/body_06.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
    show screen hermione_main                                                                                                                                                                                 #HERMIONE
    with d3                                                                                                                                                                                                                        #HERMIONE
    her "Спасибо, сэр."
    call happy


    $ h_xpos=370 #Defines position of the Hermione's full length sprite. (Default 370). (Center: 140)                                                       #HERMIONE
    show screen hermione_main                                                                                                                                                                                 #HERMIONE
    with d3                                                                                                                                                                                                                        #HERMIONE
    jump day_time_requests                    
            
        
        
        
    ### Ажурные чулки ###
label giving_nets: 
    hide screen hermione_main                                                                                                                                                                                   #HERMIONE
    with d5                                                                                                                                                                                                                        #HERMIONE
    $ h_xpos=140 #Defines position of the Hermione's full length sprite. (Default 370). (Center: 140)                                                       #HERMIONE
    

    $ mad -= 30
    $ nets = 7 # Means already gifted.
    $ h_body = "03_hp/13_hermione_main/body_03.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
    show screen hermione_main                                                                                                                                                                                 #HERMIONE
    with d5                                                                                                                                                                                                                        #HERMIONE
    her "Пара чулков?"
    hide screen hermione_main                                                                                                                                                                                   #HERMIONE
    with d3                                                                                                                                                                                                                        #HERMIONE
    $ the_gift = "03_hp/18_store/30.png" # FISHNETS.
    show screen gift
    with d3
    ">Вы даете Гермионе пару чулков...\n>Ажурные чулки добавлены в ее гардероб."
    hide screen gift

    $ dress_code = True

    $ h_body = "03_hp/13_hermione_main/body_04.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
    show screen hermione_main                                                                                                                                                                                 #HERMIONE
    with d3                                                                                                                                                                                                                        #HERMIONE
    her "Спасибо, сэр."
    call happy
    $ h_body = "03_hp/13_hermione_main/body_03.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE

    $ h_xpos=370 #Defines position of the Hermione's full length sprite. (Default 370). (Center: 140)                                                       #HERMIONE
    show screen hermione_main                                                                                                                                                                                 #HERMIONE
    with d3                                                                                                                                                                                                                        #HERMIONE
    jump day_time_requests                    
            
   
    
    
    
    
    
    
    
    
    
    
    
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
    label happy:
        hide screen hermione_main                                                                                                                                                                                 #HERMIONE
        with d3  
        if mad <= 0:
            $ mad = 0
        if mad == 0:
            ">Настроение Гермионы улучшено...\n>Гермиона {size=+5}не злится{/size} на вас..."
        else:
            ">Настроение Гермионы улучшено...\n>Гермиона {size=+5}огорчена вами{/size}..."
        return



    label no_change:
        hide screen hermione_main                                                                                                                                                                                 #HERMIONE
        with d3  
        ">Настроение Гермионы не изменилось..."
        return
        
    label upset:
        hide screen hermione_main                                                                                                                                                                                 #HERMIONE
        with d3  
        ">Настроение Гермионы ухудшилось...\n>Гермиона {size=+5}злится{/size} на вас..."
        return
        
        