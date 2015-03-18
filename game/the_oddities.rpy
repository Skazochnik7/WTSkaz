label menu_dahr_book:
    if choose==None:
        $ choose = RunMenu()
    else:
        $choose.Clear()
    python:
        for e in this.List:
            if e.GetValue("block")==_block: # Нужно ставить GetValue("block")  а не _block - у ивента такого объекта может не быть
                choose.AddItem("- Книга: "+e._caption+" - "+("{image=check_08.png}" if e._status>-2 else "{image=check_07.png}"), 
                    "menu_dahre_book_2", True, e.Name)
        choose.AddItem("- Ничего -", "the_oddities", True, "")

    $ choose.Show()

    label menu_dahre_book_2:
        $ the_gift = event._img     # "03_hp/18_store/08.png" # Copper book of spirit.
        show screen gift
        with d3
        dahr "\"[event._caption]\". [event._description]\n"
        if event._status>-2: 
            call do_have_book
            jump the_oddities
        menu:
            "- Купить книгу за [event._price] золота -":
                if gold >= event._price:
                    $ gold -= event._price
                    $ order_placed = True
                    $ event.IncValue("status",1)
#                            $ bought_book_01 = True
                    call thx_4_shoping #Massage that says "Thank you for shopping here!".
                    jump desk
                else:
                    call no_gold #Massage: m "I don't have enough gold".
                    jump expression _label
            "- Ничего -":
                hide screen gift
                jump expression _label #education_menu


label menu_dahr_gift_order:
    $item=itsDAHR(choose.choice)
    $ the_gift = item._img # CANDY.
    show screen gift
    with d3
    $itemCount=0
    if item.Name=="miniskirt":
        menu:
            "- Купить юбку (---) -":
                if vouchers >= 1: #Shows the amount of DAHR's vouchers in your possession.
                    $ vouchers -= 1 #Shows the amount of DAHR's vouchers in your possession.
                    $ order_placed = True
                    $itsOWL.AddItem(item.Name)
                    $itsDAHR.AddItem(item.Name,-1)
                    call thx_4_shoping #Massage that says "Thank you for shopping here!".
                    jump desk
                else:
                    dahr "Эту вещь можно купить только за \"Ваучер Дахра\"."
                    dahr "Что-то не так..."
                    dahr "Чертовы переводчики..."
                    dahr "Я..."
                    translators "Так-то лучше. Этот момент показался всем достаточно сложным. Я о юбке. Дальше будет подсказка, как ее получить."
                    menu:
                        "- Глянуть подсказку -":
                            translators "{size=14}Подсказка от переводчика:\nНайти его можно {b}правильно{/b} прочитав книгу {b}[book07]{/b}{/size}."
                            translators "{size=14}Более подробно {a=http://wtrus.ixbb.ru/viewtopic.php?id=3#p4}здесь{/a}{/size}."
                        
                        "- Не нужно -":
                            translators "Как угодно."
                    hide screen gift
                    with d3
                    jump app
            "- Ничего -":
                hide screen gift
                with d3
                jump app

    if item._block=="gears":
        menu:
            dahr "[item._description]"
            "- Купить ([item._price] галеонов) -":
                $itemCount=1
            "- Ничего -":
                hide screen gift
                jump gifts_menu
    else:
        $_price2=item._price*2
        $_price3=item._price*3
        menu:
            dahr "[item._description]"
            "- Купить 1 ([item._price] галеонов) -":
                $itemCount=1
            "- Купить 2 ([_price2] галеонов) -":
                $itemCount=2
            "- Купить 3 ([_price3] галеонов) -":
                $itemCount=3
            "- Ничего -":
                hide screen gift
                jump gifts_menu


    if gold >= item._price*itemCount:
        hide screen points
        $ gold -=item._price*itemCount
        show screen points
        $ order_placed = True
        $itsOWL.AddItem(item.Name,itemCount)
#        $ bought_candy = True #Affects 15_mail.rpy
        call thx_4_shoping #Massage that says "Thank you for shopping here!".
        jump desk
    else:
        call no_gold #Massage: m "I don't have enough gold".
        jump gifts_menu





label the_oddities:
    $choose=None
    menu:
        dahr "Добро пожаловать в \"каталог Приблуд Дахра\". Ваши предпочтения не покажутся нам странными!"
        "- Образовательные книги -":
            label education_menu:
                $_label="education_menu"
                $_block="books_edu"
                jump menu_dahr_book
        "- Фантастика -":
            label fiction_menu:
                $_label="fiction_menu"
                $_block="books_fict"
                jump menu_dahr_book



        "- Подарки -":
            label gifts_menu:
            $ choose = RunMenu()
            python:
                for o in itsDAHR():
                    if o._block=="gifts": 
                        _temp={"candy": fn0, "chocolate": fn0, "owl": fn0, "beer": fn3, "mag1": fn0, "mag2": fn0, "mag3": fn0, "mag4": fn3,
                     "condoms": fn3, "vibrator": fn3, "lubricant": fn0,"ballgag": fn0, "plug": fn3, "strapon": fn3}[o.Name](o)
                        choose.AddItem("- "+o._caption+" - ("+str(o._price)+" гал.) -" if _temp else "{color=#858585}- Товар временно отсутствует -{/color}", 
                            "menu_dahr_gift_order" if _temp else "out" , True, o.Name)
                choose.AddItem("- Ничего -", "the_oddities", True, "")

            $ choose.Show() 
                
                            
                            
        "- Одежда -":
            label app:
                pass

                $ choose = RunMenu()
                python:
                    for o in itsDAHR():
                        if o._block=="gears": 
                            _temp={"ball_dress": lambda e: sorry_for_hesterics and not bought_dress_already, "badge_01": fn0, "nets": fn0, "miniskirt": lambda e: not bought_skirt_already and not gave_miniskirt and whoring >= 3}[o.Name](o)
                            choose.AddItem("- "+o._caption+" - ("+str(o._price)+" гал.) -" if _temp else "{color=#858585}- Товар временно отсутствует  -{/color}", 
                                "menu_dahr_gift_order" if _temp else "out" , True, o.Name)
                    choose.AddItem("- Ничего -", "the_oddities", True, "")

                $ choose.Show()



                        
        "- Священные свитки. Часть I -":
            label sscrolls:
            menu:

                "- С.01: [scroll_01_name] -" if not sscroll_01:
                    $ the_gift = "03_hp/18_store/31.png" # SACRED SCROLL.
                    show screen gift
                    with d3
                    call sscroll
                    menu:
                        "- Купить свиток (30 золота) -":
                            if gold >= 30:
                                $ gold -=30
                                $ sscroll_01 = True # Turns TRUE if the scroll had been bought.
                                $ renpy.play('sounds/win_04.mp3')   #Not loud.
                                call sscroll_bought
                                call thx_4_shoping2 #Massage that says "Thank you for shopping here!".
                                jump desk
                            else:
                                call no_gold #Massage: m "I don't have enough gold".
                                hide screen gift
                                jump sscrolls
                        "- Ничего -":
                            hide screen gift
                            jump sscrolls
                
                "- С.02: [scroll_02_name] -" if not sscroll_02:
                    $ the_gift = "03_hp/18_store/31.png" # SACRED SCROLL.
                    show screen gift
                    with d3
                    call sscroll
                    menu:
                        "- Купить свиток (30 золота) -":
                            if gold >= 30:
                                $ gold -=30
                                $ sscroll_02 = True # Turns TRUE if the scroll had been bought.
                                $ renpy.play('sounds/win_04.mp3')   #Not loud.
                                call sscroll_bought
                                call thx_4_shoping2 #Massage that says "Thank you for shopping here!".
                                jump desk
                            else:
                                call no_gold #Massage: m "I don't have enough gold".
                                hide screen gift
                                jump sscrolls
                        "- Ничего -":
                            hide screen gift
                            jump sscrolls
                
                "- С.03: [scroll_03_name] -" if not sscroll_03:
                    $ the_gift = "03_hp/18_store/31.png" # SACRED SCROLL.
                    show screen gift
                    with d3
                    call sscroll
                    menu:
                        "- Купить свиток (30 золота) -":
                            if gold >= 30:
                                $ gold -=30
                                $ sscroll_03 = True # Turns TRUE if the scroll had been bought.
                                $ renpy.play('sounds/win_04.mp3')   #Not loud.
                                call sscroll_bought
                                call thx_4_shoping2 #Massage that says "Thank you for shopping here!".
                                jump desk
                            else:
                                call no_gold #Massage: m "I don't have enough gold".
                                hide screen gift
                                jump sscrolls
                        "- Ничего -":
                            hide screen gift
                            jump sscrolls
                            
                "- С.04: [scroll_04_name] -" if not sscroll_04:
                    $ the_gift = "03_hp/18_store/31.png" # SACRED SCROLL.
                    show screen gift
                    with d3
                    call sscroll
                    menu:
                        "- Купить свиток (30 золота) -":
                            if gold >= 30:
                                $ gold -=30
                                $ sscroll_04 = True # Turns TRUE if the scroll had been bought.
                                $ renpy.play('sounds/win_04.mp3')   #Not loud.
                                call sscroll_bought
                                call thx_4_shoping2 #Massage that says "Thank you for shopping here!".
                                jump desk
                            else:
                                call no_gold #Massage: m "I don't have enough gold".
                                hide screen gift
                                jump sscrolls
                        "- Ничего -":
                            hide screen gift
                            jump sscrolls
                            
                "- С.05: [scroll_05_name] -" if not sscroll_05:
                    $ the_gift = "03_hp/18_store/31.png" # SACRED SCROLL.
                    show screen gift
                    with d3
                    call sscroll
                    menu:
                        "- Купить свиток (30 золота) -":
                            if gold >= 30:
                                $ gold -=30
                                $ sscroll_05 = True # Turns TRUE if the scroll had been bought.
                                $ renpy.play('sounds/win_04.mp3')   #Not loud.
                                call sscroll_bought
                                call thx_4_shoping2 #Massage that says "Thank you for shopping here!".
                                jump desk
                            else:
                                call no_gold #Massage: m "I don't have enough gold".
                                hide screen gift
                                jump sscrolls
                        "- Ничего -":
                            hide screen gift
                            jump sscrolls
                            
                "- С.06: [scroll_06_name] -" if not sscroll_06:
                    $ the_gift = "03_hp/18_store/31.png" # SACRED SCROLL.
                    show screen gift
                    with d3
                    call sscroll
                    menu:
                        "- Купить свиток (30 золота) -":
                            if gold >= 30:
                                $ gold -=30
                                $ sscroll_06 = True # Turns TRUE if the scroll had been bought.
                                $ renpy.play('sounds/win_04.mp3')   #Not loud.
                                call sscroll_bought
                                call thx_4_shoping2 #Massage that says "Thank you for shopping here!".
                                jump desk
                            else:
                                call no_gold #Massage: m "I don't have enough gold".
                                hide screen gift
                                jump sscrolls
                        "- Ничего -":
                            hide screen gift
                            jump sscrolls
                            
                "- С.07: [scroll_07_name] -" if not sscroll_07:
                    $ the_gift = "03_hp/18_store/31.png" # SACRED SCROLL.
                    show screen gift
                    with d3
                    call sscroll
                    menu:
                        "- Купить свиток (30 золота) -":
                            if gold >= 30:
                                $ gold -=30
                                $ sscroll_07 = True # Turns TRUE if the scroll had been bought.
                                $ renpy.play('sounds/win_04.mp3')   #Not loud.
                                call sscroll_bought
                                call thx_4_shoping2 #Massage that says "Thank you for shopping here!".
                                jump desk
                            else:
                                call no_gold #Massage: m "I don't have enough gold".
                                hide screen gift
                                jump sscrolls
                        "- Ничего -":
                            hide screen gift
                            jump sscrolls
                            
                "- С.08: [scroll_08_name] -" if not sscroll_08:
                    $ the_gift = "03_hp/18_store/31.png" # SACRED SCROLL.
                    show screen gift
                    with d3
                    call sscroll
                    menu:
                        "- Купить свиток (30 золота) -":
                            if gold >= 30:
                                $ gold -=30
                                $ sscroll_08 = True # Turns TRUE if the scroll had been bought.
                                $ renpy.play('sounds/win_04.mp3')   #Not loud.
                                call sscroll_bought
                                call thx_4_shoping2 #Massage that says "Thank you for shopping here!".
                                jump desk
                            else:
                                call no_gold #Massage: m "I don't have enough gold".
                                hide screen gift
                                jump sscrolls
                        "- Ничего -":
                            hide screen gift
                            jump sscrolls
                            
                "- С.09: [scroll_09_name] -" if not sscroll_09:
                    $ the_gift = "03_hp/18_store/31.png" # SACRED SCROLL.
                    show screen gift
                    with d3
                    call sscroll
                    menu:
                        "- Купить свиток (30 золота) -":
                            if gold >= 30:
                                $ gold -=30
                                $ sscroll_09 = True # Turns TRUE if the scroll had been bought.
                                $ renpy.play('sounds/win_04.mp3')   #Not loud.
                                call sscroll_bought
                                call thx_4_shoping2 #Massage that says "Thank you for shopping here!".
                                jump desk
                            else:
                                call no_gold #Massage: m "I don't have enough gold".
                                hide screen gift
                                jump sscrolls
                        "- Ничего -":
                            hide screen gift
                            jump sscrolls
                            
                "- С.10: [scroll_10_name] -" if not sscroll_10:
                    $ the_gift = "03_hp/18_store/31.png" # SACRED SCROLL.
                    show screen gift
                    with d3
                    call sscroll
                    menu:
                        "- Купить свиток (30 золота) -":
                            if gold >= 30:
                                $ gold -=30
                                $ sscroll_10 = True # Turns TRUE if the scroll had been bought.
                                $ renpy.play('sounds/win_04.mp3')   #Not loud.
                                call sscroll_bought
                                call thx_4_shoping2 #Massage that says "Thank you for shopping here!".
                                jump desk
                            else:
                                call no_gold #Massage: m "I don't have enough gold".
                                hide screen gift
                                jump sscrolls
                                
                "- С.11: [scroll_11_name] -" if not sscroll_11:
                    $ the_gift = "03_hp/18_store/31.png" # SACRED SCROLL.
                    show screen gift
                    with d3
                    call sscroll
                    menu:
                        "- Купить свиток (30 золота) -":
                            if gold >= 30:
                                $ gold -=30
                                $ sscroll_11 = True # Turns TRUE if the scroll had been bought.
                                $ renpy.play('sounds/win_04.mp3')   #Not loud.
                                call sscroll_bought
                                call thx_4_shoping2 #Massage that says "Thank you for shopping here!".
                                jump desk
                            else:
                                call no_gold #Massage: m "I don't have enough gold".
                                hide screen gift
                                jump sscrolls
                        "- Ничего -":
                            hide screen gift
                            jump sscrolls
                
                "- С.12: [scroll_12_name] -" if not sscroll_12:
                    $ the_gift = "03_hp/18_store/31.png" # SACRED SCROLL.
                    show screen gift
                    with d3
                    call sscroll
                    menu:
                        "- Купить свиток (30 золота) -":
                            if gold >= 30:
                                $ gold -=30
                                $ sscroll_12 = True # Turns TRUE if the scroll had been bought.
                                $ renpy.play('sounds/win_04.mp3')   #Not loud.
                                call sscroll_bought
                                call thx_4_shoping2 #Massage that says "Thank you for shopping here!".
                                jump desk
                            else:
                                call no_gold #Massage: m "I don't have enough gold".
                                hide screen gift
                                jump sscrolls
                        "- Ничего -":
                            hide screen gift
                            jump sscrolls
                
                "- С.13: [scroll_13_name] -" if not sscroll_13:
                    $ the_gift = "03_hp/18_store/31.png" # SACRED SCROLL.
                    show screen gift
                    with d3
                    call sscroll
                    menu:
                        "- Купить свиток (30 золота) -":
                            if gold >= 30:
                                $ gold -=30
                                $ sscroll_13 = True # Turns TRUE if the scroll had been bought.
                                $ renpy.play('sounds/win_04.mp3')   #Not loud.
                                call sscroll_bought
                                call thx_4_shoping2 #Massage that says "Thank you for shopping here!".
                                jump desk
                            else:
                                call no_gold #Massage: m "I don't have enough gold".
                                hide screen gift
                                jump sscrolls
                        "- Ничего -":
                            hide screen gift
                            jump sscrolls
        
                "- С.14: [scroll_14_name] -" if not sscroll_14:
                    $ the_gift = "03_hp/18_store/31.png" # SACRED SCROLL.
                    show screen gift
                    with d3
                    call sscroll
                    menu:
                        "- Купить свиток (30 золота) -":
                            if gold >= 30:
                                $ gold -=30
                                $ sscroll_14 = True # Turns TRUE if the scroll had been bought.
                                $ renpy.play('sounds/win_04.mp3')   #Not loud.
                                call sscroll_bought
                                call thx_4_shoping2 #Massage that says "Thank you for shopping here!".
                                jump desk
                            else:
                                call no_gold #Massage: m "I don't have enough gold".
                                hide screen gift
                                jump sscrolls
                        "- Ничего -":
                            hide screen gift
                            jump sscrolls
                
                "- С.15: [scroll_15_name] -" if not sscroll_15:
                    $ the_gift = "03_hp/18_store/31.png" # SACRED SCROLL.
                    show screen gift
                    with d3
                    call sscroll
                    menu:
                        "- Купить свиток (30 золота) -":
                            if gold >= 30:
                                $ gold -=30
                                $ sscroll_15 = True # Turns TRUE if the scroll had been bought.
                                $ renpy.play('sounds/win_04.mp3')   #Not loud.
                                call sscroll_bought
                                call thx_4_shoping2 #Massage that says "Thank you for shopping here!".
                                jump desk
                            else:
                                call no_gold #Massage: m "I don't have enough gold".
                                hide screen gift
                                jump sscrolls
                        "- Ничего -":
                            hide screen gift
                            jump sscrolls
                
                
                "- Ничего -":
                    jump the_oddities
                    
        "- Священные свитки. Часть II -":
            label sscrolls2:
            menu:

                "- С.16: [scroll_16_name] -" if not sscroll_16:
                    $ the_gift = "03_hp/18_store/31.png" # SACRED SCROLL.
                    show screen gift
                    with d3
                    call sscroll
                    menu:
                        "- Купить свиток (30 золота) -":
                            if gold >= 30:
                                $ gold -=30
                                $ sscroll_16 = True # Turns TRUE if the scroll had been bought.
                                $ renpy.play('sounds/win_04.mp3')   #Not loud.
                                call sscroll_bought
                                call thx_4_shoping2 #Massage that says "Thank you for shopping here!".
                                jump desk
                            else:
                                call no_gold #Massage: m "I don't have enough gold".
                                hide screen gift
                                jump sscrolls2
                        "- Ничего -":
                            hide screen gift
                            jump sscrolls2
                
                "- С.17: [scroll_17_name] -" if not sscroll_17:
                    $ the_gift = "03_hp/18_store/31.png" # SACRED SCROLL.
                    show screen gift
                    with d3
                    call sscroll
                    menu:
                        "- Купить свиток (30 золота) -":
                            if gold >= 30:
                                $ gold -=30
                                $ sscroll_17 = True # Turns TRUE if the scroll had been bought.
                                $ renpy.play('sounds/win_04.mp3')   #Not loud.
                                call sscroll_bought
                                call thx_4_shoping2 #Massage that says "Thank you for shopping here!".
                                jump desk
                            else:
                                call no_gold #Massage: m "I don't have enough gold".
                                hide screen gift
                                jump sscrolls2
                        "- Ничего -":
                            hide screen gift
                            jump sscrolls2
                
                "- С.18: [scroll_18_name] -" if not sscroll_18:
                    $ the_gift = "03_hp/18_store/31.png" # SACRED SCROLL.
                    show screen gift
                    with d3
                    call sscroll
                    menu:
                        "- Купить свиток (30 золота) -":
                            if gold >= 30:
                                $ gold -=30
                                $ sscroll_18 = True # Turns TRUE if the scroll had been bought.
                                $ renpy.play('sounds/win_04.mp3')   #Not loud.
                                call sscroll_bought
                                call thx_4_shoping2 #Massage that says "Thank you for shopping here!".
                                jump desk
                            else:
                                call no_gold #Massage: m "I don't have enough gold".
                                hide screen gift
                                jump sscrolls2
                        "- Ничего -":
                            hide screen gift
                            jump sscrolls2
                            
                "- С.19: [scroll_19_name] -" if not sscroll_19:
                    $ the_gift = "03_hp/18_store/31.png" # SACRED SCROLL.
                    show screen gift
                    with d3
                    call sscroll
                    menu:
                        "- Купить свиток (30 золота) -":
                            if gold >= 30:
                                $ gold -=30
                                $ sscroll_19 = True # Turns TRUE if the scroll had been bought.
                                $ renpy.play('sounds/win_04.mp3')   #Not loud.
                                call sscroll_bought
                                call thx_4_shoping2 #Massage that says "Thank you for shopping here!".
                                jump desk
                            else:
                                call no_gold #Massage: m "I don't have enough gold".
                                hide screen gift
                                jump sscrolls2
                        "- Ничего -":
                            hide screen gift
                            jump sscrolls2
                            
                "- С.20: [scroll_20_name] -" if not sscroll_20:
                    $ the_gift = "03_hp/18_store/31.png" # SACRED SCROLL.
                    show screen gift
                    with d3
                    call sscroll
                    menu:
                        "- Купить свиток (30 золота) -":
                            if gold >= 30:
                                $ gold -=30
                                $ sscroll_20 = True # Turns TRUE if the scroll had been bought.
                                $ renpy.play('sounds/win_04.mp3')   #Not loud.
                                call sscroll_bought
                                call thx_4_shoping2 #Massage that says "Thank you for shopping here!".
                                jump desk
                            else:
                                call no_gold #Massage: m "I don't have enough gold".
                                hide screen gift
                                jump sscrolls2
                        "- Ничего -":
                            hide screen gift
                            jump sscrolls2
                            
                "- С.21: [scroll_21_name] -" if not sscroll_21:
                    $ the_gift = "03_hp/18_store/31.png" # SACRED SCROLL.
                    show screen gift
                    with d3
                    call sscroll
                    menu:
                        "- Купить свиток (30 золота) -":
                            if gold >= 30:
                                $ gold -=30
                                $ sscroll_21 = True # Turns TRUE if the scroll had been bought.
                                $ renpy.play('sounds/win_04.mp3')   #Not loud.
                                call sscroll_bought
                                call thx_4_shoping2 #Massage that says "Thank you for shopping here!".
                                jump desk
                            else:
                                call no_gold #Massage: m "I don't have enough gold".
                                hide screen gift
                                jump sscrolls2
                        "- Ничего -":
                            hide screen gift
                            jump sscrolls2
                            
                "- С.22: [scroll_22_name] -" if not sscroll_22:
                    $ the_gift = "03_hp/18_store/31.png" # SACRED SCROLL.
                    show screen gift
                    with d3
                    call sscroll
                    menu:
                        "- Купить свиток (30 золота) -":
                            if gold >= 30:
                                $ gold -=30
                                $ sscroll_22 = True # Turns TRUE if the scroll had been bought.
                                $ renpy.play('sounds/win_04.mp3')   #Not loud.
                                call sscroll_bought
                                call thx_4_shoping2 #Massage that says "Thank you for shopping here!".
                                jump desk
                            else:
                                call no_gold #Massage: m "I don't have enough gold".
                                hide screen gift
                                jump sscrolls2
                        "- Ничего -":
                            hide screen gift
                            jump sscrolls2
                            
                "- С.23: [scroll_23_name] -" if not sscroll_23:
                    $ the_gift = "03_hp/18_store/31.png" # SACRED SCROLL.
                    show screen gift
                    with d3
                    call sscroll
                    menu:
                        "- Купить свиток (30 золота) -":
                            if gold >= 30:
                                $ gold -=30
                                $ sscroll_23 = True # Turns TRUE if the scroll had been bought.
                                $ renpy.play('sounds/win_04.mp3')   #Not loud.
                                call sscroll_bought
                                call thx_4_shoping2 #Massage that says "Thank you for shopping here!".
                                jump desk
                            else:
                                call no_gold #Massage: m "I don't have enough gold".
                                hide screen gift
                                jump sscrolls2
                        "- Ничего -":
                            hide screen gift
                            jump sscrolls2
                            
                "- С.24: [scroll_24_name] -" if not sscroll_24:
                    $ the_gift = "03_hp/18_store/31.png" # SACRED SCROLL.
                    show screen gift
                    with d3
                    call sscroll
                    menu:
                        "- Купить свиток (30 золота) -":
                            if gold >= 30:
                                $ gold -=30
                                $ sscroll_24 = True # Turns TRUE if the scroll had been bought.
                                $ renpy.play('sounds/win_04.mp3')   #Not loud.
                                call sscroll_bought
                                call thx_4_shoping2 #Massage that says "Thank you for shopping here!".
                                jump desk
                            else:
                                call no_gold #Massage: m "I don't have enough gold".
                                hide screen gift
                                jump sscrolls2
                        "- Ничего -":
                            hide screen gift
                            jump sscrolls2
                            
                "- С.25: [scroll_25_name] -" if not sscroll_25:
                    $ the_gift = "03_hp/18_store/31.png" # SACRED SCROLL.
                    show screen gift
                    with d3
                    call sscroll
                    menu:
                        "- Купить свиток (30 золота) -":
                            if gold >= 30:
                                $ gold -=30
                                $ sscroll_25 = True # Turns TRUE if the scroll had been bought.
                                $ renpy.play('sounds/win_04.mp3')   #Not loud.
                                call sscroll_bought
                                call thx_4_shoping2 #Massage that says "Thank you for shopping here!".
                                jump desk
                            else:
                                call no_gold #Massage: m "I don't have enough gold".
                                hide screen gift
                                jump sscrolls2
                        "- Ничего -":
                            hide screen gift
                            jump sscrolls2
                                
                "- С.26: [scroll_26_name] -" if not sscroll_26:
                    $ the_gift = "03_hp/18_store/31.png" # SACRED SCROLL.
                    show screen gift
                    with d3
                    call sscroll
                    menu:
                        "- Купить свиток (30 золота) -":
                            if gold >= 30:
                                $ gold -=30
                                $ sscroll_26 = True # Turns TRUE if the scroll had been bought.
                                $ renpy.play('sounds/win_04.mp3')   #Not loud.
                                call sscroll_bought
                                call thx_4_shoping2 #Massage that says "Thank you for shopping here!".
                                jump desk
                            else:
                                call no_gold #Massage: m "I don't have enough gold".
                                hide screen gift
                                jump sscrolls2
                        "- Ничего -":
                            hide screen gift
                            jump sscrolls2
                
                "- С.27: [scroll_27_name] -" if not sscroll_27:
                    $ the_gift = "03_hp/18_store/31.png" # SACRED SCROLL.
                    show screen gift
                    with d3
                    call sscroll
                    menu:
                        "- Купить свиток (30 золота) -":
                            if gold >= 30:
                                $ gold -=30
                                $ sscroll_27 = True # Turns TRUE if the scroll had been bought.
                                $ renpy.play('sounds/win_04.mp3')   #Not loud.
                                call sscroll_bought
                                call thx_4_shoping2 #Massage that says "Thank you for shopping here!".
                                jump desk
                            else:
                                call no_gold #Massage: m "I don't have enough gold".
                                hide screen gift
                                jump sscrolls2
                        "- Ничего -":
                            hide screen gift
                            jump sscrolls2
                
                "- С.28: [scroll_28_name] -" if not sscroll_28:
                    $ the_gift = "03_hp/18_store/31.png" # SACRED SCROLL.
                    show screen gift
                    with d3
                    call sscroll
                    menu:
                        "- Купить свиток (30 золота) -":
                            if gold >= 30:
                                $ gold -=30
                                $ sscroll_28 = True # Turns TRUE if the scroll had been bought.
                                $ renpy.play('sounds/win_04.mp3')   #Not loud.
                                call sscroll_bought
                                call thx_4_shoping2 #Massage that says "Thank you for shopping here!".
                                jump desk
                            else:
                                call no_gold #Massage: m "I don't have enough gold".
                                hide screen gift
                                jump sscrolls2
                        "- Ничего -":
                            hide screen gift
                            jump sscrolls2
        
                "- С.29: [scroll_29_name] -" if not sscroll_29:
                    $ the_gift = "03_hp/18_store/31.png" # SACRED SCROLL.
                    show screen gift
                    with d3
                    call sscroll
                    menu:
                        "- Купить свиток (30 золота) -":
                            if gold >= 30:
                                $ gold -=30
                                $ sscroll_29 = True # Turns TRUE if the scroll had been bought.
                                $ renpy.play('sounds/win_04.mp3')   #Not loud.
                                call sscroll_bought
                                call thx_4_shoping2 #Massage that says "Thank you for shopping here!".
                                jump desk
                            else:
                                call no_gold #Massage: m "I don't have enough gold".
                                hide screen gift
                                jump sscrolls2
                        "- Ничего -":
                            hide screen gift
                            jump sscrolls2
                
                "- С.30: [scroll_30_name] -" if not sscroll_30:
                    $ the_gift = "03_hp/18_store/31.png" # SACRED SCROLL.
                    show screen gift
                    with d3
                    call sscroll
                    menu:
                        "- Купить свиток (30 золота) -":
                            if gold >= 30:
                                $ gold -=30
                                $ sscroll_30 = True # Turns TRUE if the scroll had been bought.
                                $ renpy.play('sounds/win_04.mp3')   #Not loud.
                                call sscroll_bought
                                call thx_4_shoping2 #Massage that says "Thank you for shopping here!".
                                jump desk
                            else:
                                call no_gold #Massage: m "I don't have enough gold".
                                hide screen gift
                                jump sscrolls2
                        "- Ничего -":
                            hide screen gift
                            jump sscrolls2





                "- Ничего -":
                    jump the_oddities

        "- Ничего -":
            jump desk
        
        
### ALREADY HAVE THIS BOOK
label do_have_book:
    show screen bld1
    m "Я уже это покупал и мне больше не нужно."
    hide screen bld1
    hide screen gift
    with d3
    return
### THANK YOU FOR shopping here.
label thx_4_shoping:
    $item=itsOWL()[0]
    $itemCount=itsOWL.Count(item.Name)
    $ days_in_delivery2 = one_of_five  #Generating one number out of three for various porpoises.
    if days_in_delivery2==1:
        $days_in_delivery2+=1 # Назавтра только экспресс
        $days_in_delivery2+=itemCount-1  # Удлинняется, если несколько предметов

    if gold >= item._price*itemCount//2:
        menu:
            dahr "Вы заказали [itemCount] шт. предметов \"[item._caption]\". Оплатите экспресс-доставку?"
            "Экспресс-доставка (1/2 стоимости заказа)":
                $days_in_delivery2=1
                $gold -= item._price*itemCount//2
            "Обычная доставка":
                pass

    if days_in_delivery2 ==  1:
        dahr "Спасибо за покупку в \"Приблудах Дахра\". Ваш заказ будет доставлен завтра."
        hide screen gift
        with d3
        return
    else:
        dahr "Спасибо за покупку в \"Приблудах Дахра\". Доставка вашего заказа займет около [days_in_delivery2] дней."
        hide screen gift
        with d3
        return
    
### THANK YOU FOR shopping here. IMMEDIATE DELIVERY.
label thx_4_shoping2:
    dahr "Спасибо за покупку в \"Приблудах Дахра\"."
    hide screen gift
    with d3
    return
### NOT ENOUGH GOLD ###
label no_gold:
    m "У меня нет столько золота... Это удручает..."
    hide screen gift
    with d3
    return
    
### Этот товар закончился на складе ###

label out:
    dahr "Этот товар закончился на складе"
    return

### SACRED SCROLL MASSAGE ###
label sscroll:
    dahr "Свиток священных знаний.\n(Может содержать спойлеры)."
    return
    
### BOUGHT SACRED SCROLL MESSAGE ###
label sscroll_bought:
    ">Новый свиток был добавлен в вашу коллекцию."
    hide screen gift
    with d3
    return
    
### CHOCOLATE BAR DESCRIPTION ###
label choco_text:
    dahr "Рецепт этого восхитительного молочного шоколада держится в секрете. (По слухам, он содержит сушеных фей)."
    return

### TOY OWL ###
label owl_text:
    dahr "Игрушечная сова, набитая перьями настоящей совы. Она такая мягкая!"
    return
    
### BUTTERBEER ###
label beer_text:
    dahr "Девушки не могут устоять перед этим вкусом. Поэтому всегда пользуются большим спросом среди мальчиков. \n {size=-4}. Предупреждение: употребление алкоголя не допускается несовершеннолетними, без присмотра взрослых {/size}"
    return
          
### MAGAZINES ###
label mag1_text:
    dahr "Образовательный журнал. \nВерный спутник каждого изгоя."
    return
          
label mag2_text:
    dahr "Женский журнал. \nВсе крутые девчонки читают их."
    return
    
label mag3_text:
    dahr "Ваш парень превращается в хорошего мальчика? \nВаш муж больше не использует вас по назначению?\nВсе, что вы ждали о отношениях, любви и сексе. В основном о сексе."
    return
    
label mag4_text:
    dahr "Дайте их своей девушке, чтобы проверить ее, своей жене, чтобы постыдить ее и вашей дочери, чтобы избежать \"разговоров\"."
    return
    
### CONDOMS ###
label con_text:
    dahr "\"Презервативы Розовый единорог\". \nПокажите всем однорогое существо!\n{size=-4}Может содержать слюну реального единорога.{/size}"
    return
    
### VIBRATOR ###
label vib_text:
    dahr "Великолепный, волшебный усиленный вибратор изготовлен из лозы дерева, с ядром жилы дракона."
    return
    
### ANAL LUBRICANT ###
label lub_text:
    dahr "Банка анальной смазки. Купите это любимому человеку - покажите, что вы заботитесь о нем/ней."
    return

### BALL GAG AND CUFFS ###
label ball_text:
    dahr "Кляп и манжеты, превратите свою вторую половинку в вашего сокамерника."
    return
          
### ANAL PLUGS ###
label anal_text:
    dahr "Анальные пробки украшены настоящими хвостами. \n Разные размеры, чтобы удовлетворить экспертов, практиков и начинающих."
    return
          
### STRAP-ON ###
label str_text:
    dahr "Cтрапон \"Фестрал\".\nКогда вы его увидите - потеряете дар речи."
    return

### FISHNETS ###
label nets_text:
    dahr "Ажурные чулки. Вопреки распространенному мнению, они не были изобретены рыбаком."
    return
