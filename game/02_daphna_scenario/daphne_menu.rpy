#play music "music/Chipper Doodle v2.mp3" fadein 1 fadeout 1 
#stop music fadeout 2.0
label daphne_approaching(isKnocking=False):   

#    $ menu_x = 0.2 #Menu is moved to the left side.
#    $ pos = POS_410
                
    $ renpy.play('sounds/door.mp3') #Sound of a door opening.
#    $ hermione_chibi_xpos = 400 #Near the desk.
#    show screen hermione_02 #Hermione stands still.
#    show screen bld1
#    with d3
#    $daphne.LoadDefItemSets()
    $daphne.Visibility("body", False)

    python:
        for t in [
            (0, ["daphne:>// ~55 00 1 def// Да, профессор?"]),
            (-2, [">Похоже, Дафна по-прежнему немного расстроена вами..."]),
            (-9, [">Вы расстроили Дафну."]),
            (-19, [">Дафна очень расстроена вами."]),
            (-39, [">Дафна злится на вас."]),
            (-49, [">Дафна очень злится на вас."]),
            (-59, [">Дафна гневается на вас."]),
            (-100, [">Дафна ненавидит вас."])
            ]:
            (_val, _texts)=t
            if daphne.liking>=_val:
                for s in _texts:
                    Say(s)
                break


    $ this.RunStep("DAPHENTER")      

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
            if daphne.liking<0:
                python:
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
                                daphne(_text)
                                break
            else:
                label daphne_main_menu_requests:
                    $choose = RunMenu()
                    python:
                        for o in this.List:
                            if o._points!=None:
                                if (("daphne_public" in o._points and daytime) or "daphne_private" in  o._points):
                                    choose.AddItem(str(o._caption), None, o.Name)        
                        choose.Show("daphne_main_menu")

                    $daphne.Visibility("body+")
                    $hero(m,this(choose.choice)._eventPlan)
                    menu:
                        "\"(Да, сделаем это.)\"":
                            call expression this(choose.choice).Name
                        "\"(Не сейчас.)\"":
                            jump daphne_main_menu_requests 
                    
                    
                    call daphne_pre_menu(_return) # Вызов меню подарков

# Завершение ивента, который исполнялся 
                    if event._scenario==None: 
                        $event.Finalize("day_main_menu" if daytime else "night_main_menu")    
                    else:
                        $event.Finalize("night_start" if daytime else "day_start")    

                     
        
        
        "- Дать ей подарок -" if not daphne.IsGift():
            $ choose = RunMenu()
            python:
                for o in hero.Items():
                    if not o.Name in {"scroll", "ball_dress"}:
                        choose.AddItem("- "+o._caption+" -", 
                            "daphne_giving" , o.Name)

            $ choose.Show("daphne_main_menu")


                    
        

# Пока комментировать? сделать в следующих версиях
#        "- Гардероб -" if dress_code:
#            python:
#                if daphne.liking<0:
#                    for t in [
#                    (-2, "Мне жаль, профессор, может быть в другой раз..."),
#                    (-9, "Мне не хочется сегодня...\nМожет быть через пару дней..."),
#                    (-19, "Нет, спасибо...."),
#                    (-29, "После того, что вы сделали?\nЯ так не думаю..."),
#                    (-39, "Вы серьезно!?"),
#                    (-100, "Это какая-то ваша пошлая шутка?!\nПосле того, что вы сделали, я не хочу повторять это!")
#                    ]:
#                        (_val, _text)=t
#                        if daphne.liking>=_val:
#                            renpy.say(her, _text)
#                            break
#                else:
#                    choose = RunMenu()
#                    for o in daphne.Items():
#                        if o.Name in {"badge_01", "nets", "miniskirt"}:
#                            choose.AddItem("- "+("Надеть" if o._status==0 else "Снять")+" "+o._caption+" -", 
#                                "daphne_item_"+("on" if o._status==0 else "off"), True, o.Name)

#                    choose.Show("daphne_main_menu")                            
#            jump daphne_main_menu            




       
        
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

       

        
### CHITCHAT WITH DAPHNE ###
label daphne_chat:
    if this.IsStep("DAPHNECHAT"):
        $ this.RunStep("DAPHNECHAT")
    else:
        if daphne.whoring in {0,1,2}:
            $daphne([
            "Мугродью - бой!// Вот что должно быть заповедью каждого настоящего волшебника!",
            "Сегодня грязнокровка Грейнджер опять получила высший балл. Куда смотрит министерство?!//"
                "Так скоро среди волшебников не останется ни одного чистокровного.",
            "\"Чистокровные вести\" опубликовали список чистокровных волшебников Англии. Вы там тоже есть - на предпоследней строчке.",
            "Мама говорит, что я смогу раскрыть свои настоящие таланты, только если займу правильную позицию. Вы тоже так думаете?",
            "Моя сова Пухля опять обожралась птичьим кормом и теперь не может никуда лететь.//"
                "Но я ее ни за что не променяю на другую.//"
                "Она тоже очень чистокровная!"
            ][Rand(5)-1])
        elif daphne.whoring in {3,4,5}:
            $daphne([
            "Конкурс приближается и я места себе не нахожу. Иногда мне хочется выпить как следует...//"
                "Ой, простите, профессор, сорвалось. Я совсем не это имела в виду!",
            "Сегодня какой-то полукровка заговорил со мной. Мне даже показалось, что он пытался меня клеить. Просто смешно.",
            "Этот призрак - Пивз, ну, знаете его, сегодня по секрету рассказал мне что тоже из какого-то древнего рода.//"
                "И представляете, он был очень убедителен. Странно - обычно он так себя не ведет.",
            "Я надеюсь, что с вашей помощью профессор, я утру нос всем этим худородным, полукровкам и конечно же, мугродью.",
            "Сегодня был матч и я исполняла танец чирлидера со всем присущим мне изяществом.//"
                "Некоторые парни так пялились на меня...// Но мне это совсем не нужно, сэр!"
            ][Rand(5)-1])


    jump daphne_main_menu

