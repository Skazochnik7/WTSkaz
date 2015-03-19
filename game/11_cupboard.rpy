label cupboard:
    menu:
        "- Осмотреть шкаф -" if not cupboard_examined:
            $ cupboard_examined = True
            show screen chair_02 #Empty chair near the desk.
            hide screen genie
            $ tt_xpos=-20
            $ tt_ypos=100
            show screen genie_stands_f
            show screen desk
            with Dissolve(0.5)
            m "Хм....."
            m "Шкаф..."
            m "Может порыться в нем чуть позже..."
            show screen genie
            hide screen genie_stands_f
            hide screen chair_02 #Empty chair near the desk.
            hide screen desk
            with Dissolve(0.5)
            jump day_main_menu
            
            
            
        "- Рыться в шкафу -" if not searched and not day == 1:
            jump rummaging
        "{color=#858585}- Рыться в шкафу -{/color}" if searched and not day == 1:
            call already_did #Message that says that you have searched the cupboard today already.
            jump cupboard
        "- Ваши вещи -" if not day == 1:
            label possessions:
                $ choose = RunMenu()
                python:
                    for o in hero.Items():
                            choose.AddItem("- "+o._caption+" -", 
                                "menu_cupboard_description" , True, o.Name)
                    if  day>1: 
                        choose.AddItem("Помощь", "cheat_help", True, "")
                    choose.AddItem("- Ничего -", "cupboard", True, "")

                $ choose.Show()

            label menu_cupboard_description:
                $item=itsDAHR(choose.choice)
                $ the_gift = item._img
                show screen gift
                with d3
                ">[item._description]"
                hide screen gift
                with d3
                jump possessions                

                   
                label cheat_help:
                menu:
                    "Включить ТУРБО-режим" if turbo==1: 
                        $turbo=2
                        "ТУРБО-режим включен. Теперь ваши действия будут приносить вам вдвое больше денег и очков факультету Слизерина.\n Шанс на прочтение дополнительной главы вдвое больше."                    
                    "Выключить ТУРБО-режим" if turbo==2: 
                        $turbo=1
                        "ТУРБО-режим выключен. Теперь ваши действия будут приносить вам обычное количество денег и очков факультету Слизерина.\n Шанс на прочтение дополнительной главы стандартный."                    
                    "ЧИТ: +100 очков Слизерину":
                        hide screen points
                        $slytherin+=100
                        show screen points
                    "ЧИТ: Гермиона больше не злиться на вас":
                        hide screen points
                        $mad=0
                        show screen points
                        "Готово можете проверить"
                    "ЧИТ: +100 золотых":
                        hide screen points
                        $gold+=100
                        show screen points
                    "Прохождение":
                        "Прохождение и ответы часто встречающиеся вопросы можно найти {a=http://wtrus.ixbb.ru/viewtopic.php?id=3}ЗДЕСЬ{/a}. "

                    "- Ничего -":
                        jump cupboard
                jump cheat_help


        "- Священные свитки. Часть I -" if not day == 1 and cataloug_found:
            label sc_col_men_1:
                $ choose = RunMenu()
                python:
                    for i in range(1, 15):
                        choose.AddItem("- C.[i]: Священный свиток #[i] -", 
                            "menu_cupboard_scroll_show" , True, i)
                    choose.AddItem("- Ничего -", "cupboard", True, "")
                $ choose.Show()


        "- Священные свитки. Часть II -" if not day == 1 and cataloug_found:
            label sc_col_men_2:
                $ choose = RunMenu()
                python:
                    for i in range(16, 30):
                        choose.AddItem("- C.[i]: Священный свиток #[i] -", 
                            "menu_cupboard_scroll_show" , True, i)
                    choose.AddItem("- Ничего -", "cupboard", True, "")
                $ choose.Show()


                label menu_cupboard_scroll_show:

                    $ the_gift = "03_hp/19_extras/"+str(choose.choice).zfill(2)+".png"
 # SACRED SCROLL 01.
                    show screen gift
                    show screen ctc
                    with d3
                    pause
                    hide screen gift
                    hide screen ctc
                    with d3
                    jump sc_col_men_1
            
        "- Ничего -":
            jump day_main_menu
 
label rummaging:  
    
    $ searched = True #Turns true after you search the cupboard. Turns back to False every day. Makes sure you can only search the cupboard once a day.
    
    $ rum_times += 1 # Counts how many times have you rummaged the cupboard. +1 every time you do that. Needed to make to grand 2 potions before the fight.
    
    hide screen cupboard
    hide screen genie
    show screen rum_screen
    with Dissolve(0.3)
    show screen bld1
    with d3
    ">Вы роетесь в шкафу..." 
    
    if day <= 4:
        if rum_times == 2 or rum_times == 3:
            $ renpy.play('sounds/win2.mp3')   #Not loud.
            $ potions += 1
            $ the_gift = "03_hp/18_store/32.png" # CANDY.
            show screen gift
            with d3
            ">Вы нашли какое-то зелье..." 
            hide screen gift
            with d3
            show screen cupboard
            show screen genie
            hide screen rum_screen
            
            hide screen bld1
            with d3
            
            if daytime:
                jump night_start
            else: 
                jump day_start

    if rum_times == 15 and not cataloug_found:
        $ renpy.play('sounds/win2.mp3')   #Not loud.
        $ cataloug_found = True # Turns TRUE after you found the Dahr's oddities catalog in the cupboard.
        $ the_gift = "03_hp/18_store/dahr2.png" # DAHR's oddities catalog. 
        show screen gift
        with d3
        ">Вы нашли каталог \"Приблуды Дахра\"... \n>Теперь вы можете использовать каталог для заказа товаров с помощью совы."
        hide screen gift
        with d3
        show screen cupboard
        show screen genie
        hide screen rum_screen
        
        hide screen bld1
        with d3
        
        if daytime:
            jump night_start
        else: 
            jump day_start
        
    
    if i_of_iv == 4: # Found something.
        $arrProb={"candy":[2,2,2,0], "wine": [7,5,4,0], "chocolate":[1,1,0,4], "lingere":[1,1,0,1], "sexdoll":[1,1,1,1],
        "krum":[0,1,1,1],"owl":[0,0,4,4], "broom":[0,0,0,1]} #"gold":[8, 9, 8, 8]

        $_level=GetStage(whoring, 0, 6, 4)-1
        $_randValue=one_of_tw
        $_name="gold"
        python:
            for o in arrProb:
                _randValue-=arrProb[o][_level]
                if _randValue<=0:
                    _name=o

        $ renpy.play('sounds/win2.mp3')   #Not loud.
        $item=hero.Items.AddItem(_name)
        if item.Name=="gold":
            $gold=[gold1,gold2,gold3,gold4][_level]
        $ the_gift = item._img
        show screen gift
        with d3
        ">Вы нашли предмет: [item._caption]!" 
        hide screen gift
        with d3



    else: #Didn't find anything.
        ">...Вы не нашли ничего ценного." 
    

    
    show screen cupboard
    show screen genie
    hide screen rum_screen
    
    hide screen bld1
    with d3
    
    if daytime:
        jump day_main_menu
    else: 
        jump night_main_menu
        
        
        
        
        
        
        
######################
label already_did:
    show screen bld1
    with d3
    m "Я сегодня уже рылся в шкафу..."
    hide screen bld1
    with d3
    return
