label tutoring:

    $ tut_happened = True # Turns TRUE after you click the tutoring button and see th message that tutoring is not a part of this game. Make sure the tutoring button will not be visible after that.
    
    #__#hide screen hermione_main                                                                                                                                                                                   #HERMIONE
    #__#with d3                                                                                                                                                                                                                        #HERMIONE
    $herView.hideQ( d3 )
    $ h_xpos=370 #Defines position of the Hermione's full length sprite. (Default 370). (Center: 140)                                                       #HERMIONE
    $pos = POS_370
    #__#$ h_body = "03_hp/13_hermione_main/body_14.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
    #__#show screen hermione_main                                                                                                                                                                                 #HERMIONE
    #__#with d3                                                                                                                                                                                                                        #HERMIONE
    $herView.showQ( "body_14.png", pos, d3 )
    
    herView "Конечно, сэр."
    herView "Тогда я возьму свои книги."
    
    
    #__#hide screen hermione_main                                                                                                                                                                                   #HERMIONE
    $herView.hideQ( d3 )

    show screen blkfade
    with d3
    $ renpy.play('sounds/door.mp3') #Sound of a door opening.
    pause 2
    $ renpy.play('sounds/door.mp3') #Sound of a door opening.
    pause.3
    

    $ only_upper = True
    $ ne = False # Desplays a fishnets in hermione_main screen.

    #__## memorize current state, because we're switching to pose with book
    #__#$ herView.saveState()
    $ herView.addPose( CharacterExItemPoseBook( herView.mPoseFolder, "pose_with_book.png", G_Z_POSE ) )
    #__#$ herView.delHands()
    
    $ h_xpos=140 #Defines position of the Hermione's full length sprite. (Default 370). (Center: 140)                                                       #HERMIONE
    $ pos = POS_140
    #__#$ h_body = "03_hp/13_hermione_main/body_199.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
    #__#$ herView.addAdditional( "full", HermioneItem( "03_hp/13_hermione_main/body_199.png", 0 ) )
    
    #__#show screen hermione_main                                                                                                                                                                                 #HERMIONE
    #__#with d3                                                                                                                                                                                                                        #HERMIONE
    $ herView.showQ( "body_199.png", pos, d3 )
    
    hide screen blkfade
    with d3
    
    show screen ctc
    pause
    hide screen ctc
    
    #__#hide screen hermione_main                                                                                                                                                                                   #HERMIONE
    #__#with d3                                                                                                                                                                                                                        #HERMIONE
    $ herView.hideQ( d3 )
    #__#$ h_body = "03_hp/13_hermione_main/body_198.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
    #__#$ herView.addAdditional( "full", HermioneItem( "03_hp/13_hermione_main/body_198.png", 0 ) )

    $ herView.showQ( "body_198.png", pos, d3 )
    #__#show screen hermione_main                                                                                                                                                                                 #HERMIONE
    #__#with d3                                                                                                                                                                                                                        #HERMIONE
    
    herView "Еще раз спасибо, за то, что делаете это для меня, сэр..."
    m "..........."
    #__#hide screen hermione_main                                                                                                                                                                                   #HERMIONE
    #__#with d3                                                                                                                                                                                                                        #HERMIONE
    $ herView.hideQ( d3 )
    
    #__#$ h_body = "03_hp/13_hermione_main/body_200.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
    #__#$ herView.addAdditional( "full", HermioneItem( "03_hp/13_hermione_main/body_200.png", 0 ) )
    #__#show screen hermione_main                                                                                                                                                                                 #HERMIONE
    #__#with d3                                                                                                                                                                                                                        #HERMIONE
    $ herView.showQ( "body_200.png", pos, d3 )
    herView "Сэр?"
    m "...................."
    stop music fadeout 1.0
    g4 "Я не могу сделать этого."
    #__#hide screen hermione_main                                                                                                                                                                                   #HERMIONE
    #__#with d3                                                                                                                                                                                                                        #HERMIONE
    $ herView.hideQ( d3 )
    #__#$ h_body = "03_hp/13_hermione_main/body_198.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
    #__#$ herView.addAdditional( "full", HermioneItem( "03_hp/13_hermione_main/body_198.png", 0 ) )
    #__#show screen hermione_main                                                                                                                                                                                 #HERMIONE
    #__#with d3                                                                                                                                                                                                                        #HERMIONE
    $ herView.showQ( "body_198.png", pos, d3 )
    herView "А?"
    m "Я не могу учить вас, мисс Грейнджер..."
    #__#hide screen hermione_main                                                                                                                                                                                   #HERMIONE
    #__#with d3                                                                                                                                                                                                                        #HERMIONE
    $ herView.hideQ( d3 )
    #__#$ h_body = "03_hp/13_hermione_main/body_198.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
    #__#$ herView.addAdditional( "full", HermioneItem( "03_hp/13_hermione_main/body_198.png", 0 ) )
    #__#show screen hermione_main                                                                                                                                                                                 #HERMIONE
    #__#with d3                                                                                                                                                                                                                        #HERMIONE
    $ herView.showQ( "body_198.png", pos, d3 )
    play music "music/Music for Manatees.mp3" fadein 1 fadeout 1
    herView "Н-но..."
    #__#hide screen hermione_main                                                                                                                                                                                   #HERMIONE
    #__#with d3                                                                                                                                                                                                                        #HERMIONE
    $ herView.hideQ( d3 )
    #__#$ h_body = "03_hp/13_hermione_main/body_201.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
    #__#$ herView.addAdditional( "full", HermioneItem( "03_hp/13_hermione_main/body_201.png", 0 ) )
    #__#show screen hermione_main                                                                                                                                                                                 #HERMIONE
    #__#with d3                                                                                                                                                                                                                        #HERMIONE
    herView "Но сэр, вы обещали!"
    m "Нет, ты не поняла..."
    m "Я фактически {size=+7}не могу{/size} делать этого."
    m "Акабур не доделал эту часть игры..."
    #__#hide screen hermione_main                                                                                                                                                                                   #HERMIONE
    #__#with d3                                                                                                                                                                                                                        #HERMIONE
    $ herView.hideQ( d3 )
    #__#$ h_body = "03_hp/13_hermione_main/body_202.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
    #__#show screen hermione_main                                                                                                                                                                                 #HERMIONE
    #__#with d3                                                                                                                                                                                                                        #HERMIONE
    $ herView.showQ( "body_202.png", pos, d3 )
    herView "???"
    m "Да, согласен..."
    m "Все, что сделано для обучения выглядит неуместно..."
    m "И я надеялся, что смогу контролировать твой уровень интеллекта или вроде того..."
    #__#hide screen hermione_main                                                                                                                                                                                   #HERMIONE
    #__#with d3                                                                                                                                                                                                                        #HERMIONE
    $ herView.hideQ( d3 )
    #__#$ h_body = "03_hp/13_hermione_main/body_203.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
    #__#show screen hermione_main                                                                                                                                                                                 #HERMIONE
    #__#with d3                                                                                                                                                                                                                        #HERMIONE
    $ herView.showQ( "body_203.png", pos, d3 )
    herView "(Уровень моего интеллекта?)"
    m "Может быть приставать к тебе, пока ты учишься..."
    #__#hide screen hermione_main                                                                                                                                                                                   #HERMIONE
    #__#with d3                                                                                                                                                                                                                        #HERMIONE
    $ herView.hideQ( d3 )
    #__#$ h_body = "03_hp/13_hermione_main/body_204.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
    #__#show screen hermione_main                                                                                                                                                                                 #HERMIONE
    #__#with d3                                                                                                                                                                                                                        #HERMIONE
    $ herView.showQ( "body_204.png", pos, d3 )
    herView "(Что?!)"
    m "Может быть, трахать тебя в то время как ты читаешь книгу..."
    #__#hide screen hermione_main                                                                                                                                                                                   #HERMIONE
    #__#with d3                                                                                                                                                                                                                        #HERMIONE
    $ herView.hideQ( d3 )
    #__#$ h_body = "03_hp/13_hermione_main/body_205.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
    #__#show screen hermione_main                                                                                                                                                                                 #HERMIONE
    #__#with d3                                                                                                                                                                                                                        #HERMIONE
    $ herView.showQ( "body_205.png", pos, d3 )
    stop music
    herView "{size=+7}ЧТО?!{/size}"
    show screen blktone8
    with d3
    ">Гермиона огорчена из-за вас."
    hide screen blktone8
    with d3
    $ mad = +10
    m "*Вздох* Я очень много прошу...?"
    #__#hide screen hermione_main                                                                                                                                                                                   #HERMIONE
    #__#with d3                                                                                                                                                                                                                        #HERMIONE
    $ herView.hideQ( d3 )
    #__#$ h_body = "03_hp/13_hermione_main/body_206.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
    #__#show screen hermione_main                                                                                                                                                                                 #HERMIONE
    #__#with d3                                                                                                                                                                                                                        #HERMIONE
    $ herView.showQ( "body_206.png", pos, d3 )
    herView "Сэр, я думаю мне стоит уйти..."
    show screen blkfade
    #__#hide screen hermione_main
    #__#with d3
    $ herView.hideQ( d3 )
    m "Я сказал что-то не то?"
  
    $ only_upper = False
    $ ne = True # Desplays a fishnets in hermione_main screen.
    
    #__## now we'll restore saved state
    #__#$ herView.loadState()
    $ herView.delPose();
    
    
    
    
    
    
    #"You spend the evening tutoring Hermione. Hermione become a bit smarter."
    
#    if knowledge >= 5 and tutoring_events == 0 and whoring >= 1:
#        $ tutoring_events += 1
#        "Event 01"
        
#    if knowledge >= 10 and tutoring_events == 1 and whoring >= 2: #LEVEL 02
#        $ tutoring_events += 1
#        "Event 02"
        
#    if knowledge >= 15 and tutoring_events == 2 and whoring >= 3: #LEVEL 03
#        $ tutoring_events += 1
#        "Event 03"
        
#    if knowledge >= 20 and tutoring_events == 3 and whoring >= 4: #LEVEL 04
#        $ tutoring_events += 1
#        "Event 04"
        
#    if knowledge >= 25 and tutoring_events == 4 and whoring >= 5: #LEVEL 05
#        $ tutoring_events += 1
#        "Event 05"
        
#    if knowledge >= 30 and tutoring_events == 5 and whoring >= 7: #LEVEL 06
#        $ tutoring_events += 1
#        "Event 06"
        
#    if knowledge >= 35 and tutoring_events == 6 and whoring >= 8: #LEVEL 07
#        $ tutoring_events += 1
#        "Event 07"
         
#    if knowledge >= 40 and tutoring_events == 7 and whoring >= 9: #LEVEL 08
#        $ tutoring_events += 1
#        "Event 08"
        
#    if knowledge >= 45 and tutoring_events == 8 and whoring >= 11: #LEVEL 09
#        $ tutoring_events += 1
#        "Event 09"
        
#    if knowledge >= 50 and tutoring_events == 9 and whoring >= 13: #EVENT 10
#        $ tutoring_events += 1
#        "Event 10"
        
#    if knowledge >= 55 and tutoring_events == 10 and whoring >= 14: #EVENT 10
#        $ tutoring_events += 1
#        "Event 11"
        
#    if knowledge >= 60 and tutoring_events == 11 and whoring >= 16: #EVENT 11
#        $ tutoring_events += 1
#        "Event 12"
         
#    if knowledge >= 65 and tutoring_events == 12 and whoring >= 18: #EVENT 12
#        $ tutoring_events += 1
#        "Event 13"
        
#    if knowledge >= 70 and tutoring_events == 13 and whoring >= 20: #EVENT 13
#        $ tutoring_events += 1
#        "Event 14"
        
#    if knowledge >= 75 and tutoring_events == 14 and whoring >= 21: #EVENT 14
#        $ tutoring_events += 1
#        "Event 15"
        
 
    
   
#    $ knowledge +=1
#    "You dismiss Hermione."
    jump day_start