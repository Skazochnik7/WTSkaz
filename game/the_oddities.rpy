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


label menu_dahr_gifts_and_gears:
    $ choose = RunMenu()
    python:
        for o in itsDAHR():
            if _block=="gifts" and o._block=="gifts": 
                _temp={"candy": fn0, "chocolate": fn0, "owl": fn0, "beer": fn3, "mag1": fn0, "mag2": fn0, "mag3": fn0, "mag4": fn3,
             "condoms": fn3, "vibrator": fn3, "lubricant": fn0,"ballgag": fn0, "plug": fn3, "strapon": fn3}[o.Name](o)

            if _block=="gears" and o._block=="gears": 
                _temp={"ball_dress": lambda e: sorry_for_hesterics and not bought_dress_already, "badge_01": fn0, "nets": fn0, 
                    "miniskirt": lambda e: whoring >= 3 and (hero.Items.Count("miniskirt")+hermi.Items.Count("miniskirt")+itsOWL.Count("miniskirt")==0) }[o.Name](o)

                choose.AddItem("- "+o._caption+" - ("+str(o._price)+" гал.) -" if _temp else "{color=#858585}- Товар временно отсутствует -{/color}", 
                    "menu_dahr_gift_order" if _temp else "out" , True, o.Name)
        choose.AddItem("- Ничего -", "the_oddities", True, "")

    $ choose.Show() 



label menu_dahr_gift_order:
    $item=itsDAHR(choose.choice)
    label menu_dahr_scroll_order:
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

    if itsDAHR.Count(item.Name)>0:
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
            if itsDAHR.Count(item.Name)>0:
                menu:
                    dahr "[item._description]"
                    "- Купить 1 ([item._price] галеонов) -":
                        $itemCount=1
                    "- Купить 2 ([_price2] галеонов) -" if itsDAHR.Count(item.Name)>1:
                        $itemCount=2
                    "- Купить 3 ([_price3] галеонов) -" if itsDAHR.Count(item.Name)>2:
                        $itemCount=3
                    "- Ничего -":
                        hide screen gift
                        jump gifts_menu
    else:
        ">Извините, товар закончился"


    if gold >= item._price*itemCount:
        hide screen points
        $ gold -=item._price*itemCount
        show screen points
        $ order_placed = True
        $itsOWL.AddItem(item.Name,itemCount)
        if item.Name in {"scroll"}:
            $itsDAHR.AddItem(item.Name,-itemCount)
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
                $_block="gifts"
                jump menu_dahr_gifts_and_gears
                
                            
                            
        "- Одежда -":
            label app:
                pass
                $_block="gears"
                jump menu_dahr_gifts_and_gears



        "- Священные свитки -":
            label sscrolls:
                $item=itsDAHR.Items("scroll")
                jump menu_dahr_gift_order

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
            dahr "Вы заказали [itemCount] шт. предметов \"[item._caption]\". Вы оплатите экспресс-доставку?"
            "Экспресс-доставка (50%% стоимости заказа)":
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

