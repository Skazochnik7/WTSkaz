#play music "music/Chipper Doodle v2.mp3" fadein 1 fadeout 1 
#stop music fadeout 2.0
label daphne_approaching(isKnocking=False):     
         
    $ menu_x = 0.2 #Menu is moved to the left side.
#    $ pos = POS_410
                
    $ renpy.play('sounds/door.mp3') #Sound of a door opening.
#    $ hermione_chibi_xpos = 400 #Near the desk.
#    show screen hermione_02 #Hermione stands still.
#    show screen bld1
#    with d3

    python:
        for t in [
            (0, "body_01.png", her, "Да, профессор?"),
            (-2, "body_03.png", "", ">Похоже, Гермиона по-прежнему немного расстроена вами..."),
            (-9, "body_03.png", "", ">Вы расстроили Гермиону."),
            (-19, "body_09.png", "", ">Гермиона очень расстроена вами."),
            (-39, "body_05.png", "", ">Гермиона злится на вас."),
            (-49, "body_47.png", "", ">Гермиона очень злится на вас."),
            (-59, "body_47.png", "", ">Гермиона гневается на вас."),
            (-100, "body_47.png", "", ">Гермиона ненавидит вас.")
            ]:
            (_val, _img, _char, _text)=t
            if hermi.liking>=_val:
                herView.showQQ( _img, pos )
                renpy.say(_char, _text)
                break



    label daphne_main_menu:
    menu:
        "- Поговорить -" if not daphne.IsTalk():
            $daphne.CommitTalk() #Prevents you from chitchatting with Hermione more then once per time of day. Turns back to False every night. (And every day).
            if daphne.liking >= -7:
                jump daphne_chat
            else:
                $daphne("Мне нечего сказать вам...")    
                jump daphne_main_menu

        "- Тренировка -" if this.daphne_pre_finish.IsFinished():#buying_favors_from_hermione_unlocked:
            python:
                if daphne.liking<0:
                        for t in [
                        (-2, "Мне жаль, профессор, может быть в другой раз..."),
                        (-9, "Мне не хочется сегодня...\nМожет быть через пару дней..."),
                        (-19, "Нет, спасибо...."),
                        (-29, "После того, что вы сделали?\nЯ так не думаю..."),
                        (-39, "Вы серьезно!?"),
                        (-100, "Это какая-то ваша пошлая шутка?!\nПосле того, что вы сделали, я не хочу повторять это!")
                        ]:
                            (_val, _text)=t
                            if daphne.liking>=_val:
                                renpy.say(her, _text)
                                break
                else:
                    choose = RunMenu()
                    choose.AddItem("- Сокурсницы", True, "имя ивента")
                    choose.AddItem("- Покажись!", True, "имя ивента")
                    choose.Show("daphne_main_menu") 
       
        
        
        "- Дать ей подарок -" if not gifted:
            $ choose = RunMenu()
            python:
                for o in hero.Items():
                    if not o.Name in {"scroll"}:
                        choose.AddItem("- "+o._caption+" -", 
                            "daphne_giving" , True, o.Name)

            $ choose.Show("daphne_main_menu")


                    
        

            
        "- Гардероб -" if dress_code:
            python:
                if daphne.liking<0:
                    for t in [
                    (-2, "Мне жаль, профессор, может быть в другой раз..."),
                    (-9, "Мне не хочется сегодня...\nМожет быть через пару дней..."),
                    (-19, "Нет, спасибо...."),
                    (-29, "После того, что вы сделали?\nЯ так не думаю..."),
                    (-39, "Вы серьезно!?"),
                    (-100, "Это какая-то ваша пошлая шутка?!\nПосле того, что вы сделали, я не хочу повторять это!")
                    ]:
                        (_val, _text)=t
                        if daphne.liking>=_val:
                            renpy.say(her, _text)
                            break
                else:
                    choose = RunMenu()
                    for o in daphne.Items():
                        if o.Name in {"badge_01", "nets", "miniskirt"}:
                            choose.AddItem("- "+("Надеть" if o._status==0 else "Снять")+" "+o._caption+" -", 
                                "daphne_item_"+("on" if o._status==0 else "off"), True, o.Name)

                    choose.Show("daphne_main_menu")                            
            jump daphne_main_menu            




       
        
        "- Попросить уйти -":
#                        if daytime:
#                            play music "music/Brittle Rille.mp3" fadein 1 fadeout 1
#                        else:
#                            play music "music/Music for Manatees.mp3" fadein 1 fadeout 1
            $ menu_x = 0.5 #Menu position is back to default. (Center).

            if daphne.liking>=-2:
                $daphne(["О, хорошо! Тогда я пойду на уроки.", "О, хорошо! Тогда я пойду спать."][0 if daytime else 1])
            elif daphne.liking >= -6:
                $daphne("...............................")
            else: 
                $daphne(["*Гм!*...", "Пф!..."][0 if daytime else 1])


            label daphne_goout:
#            hide screen bld1
#            $herView.hideQ() 
#            hide screen blktone 
#            hide screen hermione_02
#            hide screen ctc
#            with d3

            $daphne.Visibility()
            $screens.Hide("bld1", "blktone", d3, "ctc")

            if daytime:
#                $ hermione_takes_classes = True
                jump day_main_menu
            else:
#                $ hermione_sleeping = True
                jump night_main_menu

       

        
### CHITCHAT WITH HERMIONE ###
label daphne_chat:
    $ this.RunStep("DAPHNECHAT")

    jump daphne_main_menu

