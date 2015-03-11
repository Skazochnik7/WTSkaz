label mail:
    if finished_report >= 1:
        $ letters -= 1 #Adds one letter in waiting list to be read. Displays owl with envelope.
        $ got_paycheck = False #When TRUE the paycheck is in the mail. Can't do paper work.
        hide screen owl
        show screen owl_02
        ">Вы читаете свои сообщения."
        play sound "sounds/money.mp3"  #Quiet...

        $dgold=([40, 70, 90, 110, 150, 200][finished_report-1])*turbo
        $ letter_text = "{size=-7}ОТ:Министерства Магии\nКому: Профессору Дамблдору\n\n\n{/size}{size=-2}Благодарим Вас за отчеты, присланные на этой неделе.\n Ваша оплата:{/size} \n{size=+4}[dgold] золотых монет.{/size}\n\n\n{size=-3}-С уважением-{/size}"    
        $ gold += dgold

        
        show screen bld1
        show screen letter
        show screen ctc
        pause
        hide screen letter
        hide screen bld1
        hide screen ctc
            
        $ finished_report = 0

        call screen main_menu_01
    
    
### MAIL FROM HERMIONE ###
if day == 1:
    #$ letter_text = "{size=-4}-Для профессора Дамблдора-\n\nЯ пишу Вам, что бы довести до Вашего внимания текущию ситуацию в нашей школе .\n Я боюсь мне будет нужна Ваша помощь, чтобы разобраться в этом.\n\n\n-С уважениям Ваша Гермиона Грейнджер-{/size}"
    $ letter_text = "{size=-7}От: Гермионы Грейнджер\nКому: Профессору Дамблдору\n\n{/size}{size=-4}Я уверена, вы помните причину, по которой я написала вам последнее письмо, сэр.\n\nЯ прошу вас, пожалуйста, услышьте меня на этот раз. Эта несправедливость не может продолжаться...\nТолько не в наши дни и не в нашей школе.\n\nПожалуйста, примите меры.\n\n{size=-3}С уважением,\nГермиона Грейнджер{/size}"    
    hide screen owl
    show screen owl_02
    #$ mail_from_her = False #Comented out because replaced with $ letters += 1
    $ letters -= 1
    label letter01_agagin:
    show screen letter
    show screen ctc
    show screen bld1
    with Dissolve(.3)
    pause
    menu:
        "- Закончить чтение -":
            pass    
        "- Продолжить чтение -":
            jump letter01_agagin
    hide screen letter
    hide screen ctc
    hide screen bld1
    with Dissolve(.3)
    show screen bld1
    with d3
    m "Эмм..............................."
    m "Что?"
    m "................................."
    hide screen bld1
    with d3
    jump event_00
    #call screen main_menu_01
    


if letter_from_hermione_02: #Letter from Hermione #02.
    $ letter_from_hermione_02 = False
    #$ letter_text = "{size=-4}-Для профессора Дамблдора-\n\nЯ пишу Вам, что бы довести до Вашего внимания текущию ситуацию в нашей школе.\n Я боюсь мне будет нужна Ваша помощь, чтобы разобраться в этом.\n\n\n-С уважениям Ваша Гермиона Грейнджер--{/size}"
    $ letter_text = "{size=-7}От: Гермионы Грейнджер\nКому: Профессору Дамблдору\n\n{/size}{size=-4}Прошу прощения, что беспокою Вас снова профессор. Я просто хочу убедиться, что Вы отнесётесь к этой проблеме серьезно.\n\nПрошлой ночью еще одна однокурсница призналась мне... Я пообещала держать это в секрете, поэтому не могу вдаваться в подробности.\n\nВсе, что я могу сказать, это то, что вовлечен один из профессоров.\n\nПожалуйста примите меры в ближайшее время.\n\n{size=-3}С уважением,\nГермиона Грейнджер.{/size}"
    hide screen owl
    show screen owl_02
    #$ mail_from_her = False #Comented out because replaced with $ letters += 1
    $ letters -= 1
    label letter02_agagin:
    show screen letter
    show screen ctc
    show screen bld1
    with Dissolve(.3)
    pause
    menu:
        "- Закончить чтение -":
            pass    
        "- Продолжить чтение -":
            jump letter02_agagin
    hide screen letter
    hide screen ctc
    hide screen bld1
    with Dissolve(.3)
    call screen main_menu_01





### MAIL THAT UNLOCKS ABILITY TO WORK ###
if work_unlock: # Send a letter that will unlock an ability to write reports
    $ work_unlock = False # Send a letter that will unlock an ability to write reports
    $ letters -= 1
    $ work_unlock2 = True # Unlocks the "Paperwork" button.
    hide screen owl
    show screen owl_02
    $ letter_text = "{size=-7}От: Министерства Магии\nКому: Профессору Альбусу Дамблдору\n\n{/size}{size=-4}Дорогой профессор Дамблдор.\nМы напоминаем Вам, что только при предоставлении нам выполненого отчета, мы можем перечислить оплату на Ваше имя.\n\n{size=-3}С уважением,\nМинистерство Магии.{/size}"
    label letter_work:
    show screen letter
    show screen ctc
    show screen bld1
    with Dissolve(.3)
    pause
    menu:
        "- Закончить чтение -":
            pass    
        "- Продолжить чтение -":
            jump letter_work
    hide screen letter
    hide screen ctc
    hide screen bld1
    with Dissolve(.3)
    m "Оплата? Хм..."
    show screen blktone8
    with d3
    $ renpy.play('sounds/win2.mp3')   #Not loud.
    ">Теперь вы можете писать отчеты в Министерство магии, чтобы заработать золото..."
    hide screen blktone8
    with d3
    call screen main_menu_01


    
label mail_02: #Packages only. <=====================================================================### PACKAGES ###=================================================== 

    $evn=None
    python:
        for e in this.List:
            if "book_" in e.Name and e._status==-1:
                e.SetValue("status", 0)
                evn=e 

    if evn!=None:
        $ package_is_here = False # Turns True when days_in_delivery >= 5. Package is displayed.
        $ days_in_delivery = 0 #Count's +1 every day when order_placed = True
        $ the_gift = evn._img #"03_hp/18_store/08.png" # Copper book of spirit.
        show screen gift
        with d3
        ">Книга [evn._caption] была добавлена в Вашу коллекцию."
        hide screen gift
        with d3
        call screen main_menu_01  


    
    
    
    
    
### ITEMS ###    
    
    if bought_ball_dress:
        $ bought_ball_dress = False
        $ package_is_here = False # Turns True when days_in_delivery >= 5. Package is displayed.
        $ days_in_delivery = 0 #Count's +1 every day when order_placed = True
        
        #$ gifts12 += ["ball_dress"]
        $ bought_dress_already = True #Makes sure that you won't buy the dress twice.
        
        $ gifts12.append("ball_dress")
        $ the_gift = "03_hp/18_store/01.png" # THE NIGHT DRESS.
        show screen gift
        with d3
        ">Роскошное вечернее платье было добавлено в вашу собственность."
        hide screen gift
        with d3
        call screen main_menu_01
        
        
        
    if bought_miniskirt:
        $ bought_miniskirt = False #Affects 15_mail.rpy
        $ package_is_here = False # Turns True when days_in_delivery >= 5. Package is displayed.
        $ days_in_delivery = 0 #Count's +1 every day when order_placed = True
        
        #$ gifts12 += ["ball_dress"]
        $ bought_skirt_already = True #Makes sure that you won't buy the skirt twice.
        $ have_miniskirt = True # Turns TRUE when you have the skirt in your possession.
        $ the_gift = "03_hp/18_store/07.png" # MINISKIRT.
        show screen gift
        with d3
        ">Школьная миниюбка была добавлена в вашу собственность."
        hide screen gift
        with d3
        call screen main_menu_01

    
    if bought_anal_lube:
        $ bought_anal_lube = False #Affects 15_mail.rpy
        $ package_is_here = False # Turns True when days_in_delivery >= 5. Package is displayed.
        $ days_in_delivery = 0 #Count's +1 every day when order_placed = True
        
        $ anal_lube += 1 #Amount of anal lubricant in possesion. 

        $ the_gift = "03_hp/18_store/09.png" # ANAL LUBRICANT.
        show screen gift
        with d3
        ">Банка анального лубриканта была добавлена в вашу собственность."
        hide screen gift
        with d3
        call screen main_menu_01

    if bought_anal_lube2:
        define bought_anal_lube2 = False #Fix Error
        $ bought_anal_lube2 = False #Affects 15_mail.rpy
        $ package_is_here = False # Turns True when days_in_delivery >= 5. Package is displayed.
        $ days_in_delivery = 0 #Count's +1 every day when order_placed = True
        
        $ anal_lube += 2 #Amount of anal lubricant in possesion. 

        $ the_gift = "03_hp/18_store/09.png" # ANAL LUBRICANT.
        show screen gift
        with d3
        ">2 Банки анального лубриканта была добавлена в вашу собственность."
        hide screen gift
        with d3
        call screen main_menu_01

    if bought_anal_lube3:
        define bought_anal_lube3 = False #Fix Error
        $ bought_anal_lube3 = False #Affects 15_mail.rpy
        $ package_is_here = False # Turns True when days_in_delivery >= 5. Package is displayed.
        $ days_in_delivery = 0 #Count's +1 every day when order_placed = True
        
        $ anal_lube += 3 #Amount of anal lubricant in possesion. 

        $ the_gift = "03_hp/18_store/09.png" # ANAL LUBRICANT.
        show screen gift
        with d3
        ">3 Банки анального лубриканта была добавлена в вашу собственность."
        hide screen gift
        with d3
        call screen main_menu_01
        
    
    if bought_condoms:
        $ bought_condoms = False #Affects 15_mail.rpy
        $ package_is_here = False # Turns True when days_in_delivery >= 5. Package is displayed.
        $ days_in_delivery = 0 #Count's +1 every day when order_placed = True
        
        $ condoms += 1 #Amount of anal lubricant in possesion. 

        $ the_gift = "03_hp/18_store/10.png" # CONDOMS.
        show screen gift
        with d3
        ">Упаковка презервативов была добавлена в вашу собственность."
        hide screen gift
        with d3
        call screen main_menu_01

    if bought_condoms2:
        define bought_condoms2 = False #Fix Error
        $ bought_condoms2 = False #Affects 15_mail.rpy
        $ package_is_here = False # Turns True when days_in_delivery >= 5. Package is displayed.
        $ days_in_delivery = 0 #Count's +1 every day when order_placed = True
        
        $ condoms += 2 #Amount of anal lubricant in possesion. 

        $ the_gift = "03_hp/18_store/10.png" # CONDOMS.
        show screen gift
        with d3
        ">2 Упаковки презервативов была добавлена в вашу собственность."
        hide screen gift
        with d3
        call screen main_menu_01

    if bought_condoms3:
        define bought_condoms3 = False #Fix Error
        $ bought_condoms3 = False #Affects 15_mail.rpy
        $ package_is_here = False # Turns True when days_in_delivery >= 5. Package is displayed.
        $ days_in_delivery = 0 #Count's +1 every day when order_placed = True
        
        $ condoms += 3 #Amount of anal lubricant in possesion. 

        $ the_gift = "03_hp/18_store/10.png" # CONDOMS.
        show screen gift
        with d3
        ">3 Упаковки презервативов была добавлена в вашу собственность."
        hide screen gift
        with d3
        call screen main_menu_01
    
    
    if bought_candy:
        $ bought_candy = False #Affects 15_mail.rpy
        $ package_is_here = False # Turns True when days_in_delivery >= 5. Package is displayed.
        $ days_in_delivery = 0 #Count's +1 every day when order_placed = True
        
        $ candy += 1 #Amount of anal lubricant in possesion. 

        $ the_gift = "03_hp/18_store/11.png" # CANDY.
        show screen gift
        with d3
        ">Леденец был добавлен в вашу собственность."
        hide screen gift
        with d3
        call screen main_menu_01

    if bought_candy2:
        define bought_candy2 = False #Fix Error
        $ bought_candy2 = False #Affects 15_mail.rpy
        $ package_is_here = False # Turns True when days_in_delivery >= 5. Package is displayed.
        $ days_in_delivery = 0 #Count's +1 every day when order_placed = True
        
        $ candy += 2 #Amount of anal lubricant in possesion. 

        $ the_gift = "03_hp/18_store/11.png" # CANDY.
        show screen gift
        with d3
        ">2 Леденца были добавлены в вашу собственность."
        hide screen gift
        with d3
        call screen main_menu_01    

    if bought_candy3:
        define bought_candy3 = False #Fix Error
        $ bought_candy3 = False #Affects 15_mail.rpy
        $ package_is_here = False # Turns True when days_in_delivery >= 5. Package is displayed.
        $ days_in_delivery = 0 #Count's +1 every day when order_placed = True
        
        $ candy += 3 #Amount of anal lubricant in possesion. 

        $ the_gift = "03_hp/18_store/11.png" # CANDY.
        show screen gift
        with d3
        ">3 Леденца были добавлены в вашу собственность."
        hide screen gift
        with d3
        call screen main_menu_01   
        
        
    if bought_chocolate:
        $ bought_chocolate = False #Affects 15_mail.rpy
        $ package_is_here = False # Turns True when days_in_delivery >= 5. Package is displayed.
        $ days_in_delivery = 0 #Count's +1 every day when order_placed = True
        
        $ chocolate += 1 #Amount of anal lubricant in possesion. 

        $ the_gift = "03_hp/18_store/12.png" # CHOCOLATE.
        show screen gift
        with d3
        ">Плитка шоколада была добавлена в вашу собственность."
        hide screen gift
        with d3
        call screen main_menu_01

    if bought_chocolate2:
        define bought_chocolate2 = False #Fix Error
        $ bought_chocolate = False #Affects 15_mail.rpy
        $ package_is_here = False # Turns True when days_in_delivery >= 5. Package is displayed.
        $ days_in_delivery = 0 #Count's +1 every day when order_placed = True
        
        $ chocolate += 2 #Amount of anal lubricant in possesion. 

        $ the_gift = "03_hp/18_store/12.png" # CHOCOLATE.
        show screen gift
        with d3
        ">2 Плитки шоколада была добавлена в вашу собственность."
        hide screen gift
        with d3
        call screen main_menu_01

    if bought_chocolate3:
        define bought_chocolate3 = False #Fix Error
        $ bought_chocolate = False #Affects 15_mail.rpy
        $ package_is_here = False # Turns True when days_in_delivery >= 5. Package is displayed.
        $ days_in_delivery = 0 #Count's +1 every day when order_placed = True
        
        $ chocolate += 3 #Amount of anal lubricant in possesion. 

        $ the_gift = "03_hp/18_store/12.png" # CHOCOLATE.
        show screen gift
        with d3
        ">3 Плитки шоколада была добавлена в вашу собственность."
        hide screen gift
        with d3
        call screen main_menu_01
        
    if bought_vibrator:
        $ bought_vibrator = False #Affects 15_mail.rpy
        $ package_is_here = False # Turns True when days_in_delivery >= 5. Package is displayed.
        $ days_in_delivery = 0 #Count's +1 every day when order_placed = True
        
        $ vibrator += 1 #Amount of anal lubricant in possesion. 

        $ the_gift = "03_hp/18_store/13.png" # VIBRATOR.
        show screen gift
        with d3
        ">Вибратор был добавлен в вашу собственность."
        hide screen gift
        with d3
        call screen main_menu_01
        
    if bought_vibrator2:
        define bought_vibrator2 = False #Fix Error
        $ bought_vibrator2 = False #Affects 15_mail.rpy
        $ package_is_here = False # Turns True when days_in_delivery >= 5. Package is displayed.
        $ days_in_delivery = 0 #Count's +1 every day when order_placed = True
        
        $ vibrator += 2 #Amount of anal lubricant in possesion. 

        $ the_gift = "03_hp/18_store/13.png" # VIBRATOR.
        show screen gift
        with d3
        ">2 Вибратора был добавлен в вашу собственность."
        hide screen gift
        with d3
        call screen main_menu_01

    if bought_vibrator3:
        define bought_vibrator3 = False #Fix Error
        $ bought_vibrator3 = False #Affects 15_mail.rpy
        $ package_is_here = False # Turns True when days_in_delivery >= 5. Package is displayed.
        $ days_in_delivery = 0 #Count's +1 every day when order_placed = True
        
        $ vibrator += 3 #Amount of anal lubricant in possesion. 

        $ the_gift = "03_hp/18_store/13.png" # VIBRATOR.
        show screen gift
        with d3
        ">3 Вибратора был добавлен в вашу собственность."
        hide screen gift
        with d3
        call screen main_menu_01

        
    if bought_strapon:
        $ bought_strapon = False #Affects 15_mail.rpy
        $ package_is_here = False # Turns True when days_in_delivery >= 5. Package is displayed.
        $ days_in_delivery = 0 #Count's +1 every day when order_placed = True
        
        $ strapon += 1 #Amount of anal lubricant in possesion. 

        $ the_gift = "03_hp/18_store/14.png" # STRAP-ON.
        show screen gift
        with d3
        "> Страпон \"Фестрал\" был добавлен в вашу собственность."
        hide screen gift
        with d3
        call screen main_menu_01

    if bought_strapon2:
        define bought_strapon2 = False #Fix Error
        $ bought_strapon2 = False #Affects 15_mail.rpy
        $ package_is_here = False # Turns True when days_in_delivery >= 5. Package is displayed.
        $ days_in_delivery = 0 #Count's +1 every day when order_placed = True
        
        $ strapon += 2 #Amount of anal lubricant in possesion. 

        $ the_gift = "03_hp/18_store/14.png" # STRAP-ON.
        show screen gift
        with d3
        ">2 Страпон \"Фестрал\" был добавлен в вашу собственность."
        hide screen gift
        with d3
        call screen main_menu_01

    if bought_strapon3:
        define bought_strapon3 = False #Fix Error
        $ bought_strapon3 = False #Affects 15_mail.rpy
        $ package_is_here = False # Turns True when days_in_delivery >= 5. Package is displayed.
        $ days_in_delivery = 0 #Count's +1 every day when order_placed = True
        
        $ strapon += 3 #Amount of anal lubricant in possesion. 

        $ the_gift = "03_hp/18_store/14.png" # STRAP-ON.
        show screen gift
        with d3
        ">3 Страпон \"Фестрал\" был добавлен в вашу собственность."
        hide screen gift
        with d3
        call screen main_menu_01
        
        
        
    if bought_ballgag:
        $ bought_ballgag = False #Affects 15_mail.rpy
        $ package_is_here = False # Turns True when days_in_delivery >= 5. Package is displayed.
        $ days_in_delivery = 0 #Count's +1 every day when order_placed = True
        
        $ ballgag += 1 #Amount of anal lubricant in possesion. 

        $ the_gift = "03_hp/18_store/15.png" # BALL GAG.
        show screen gift
        with d3
        ">Кляп и наручники были добавлены в вашу собственность."
        hide screen gift
        with d3
        call screen main_menu_01

    if bought_ballgag2:
        define bought_ballgag2 = False #Fix Error
        $ bought_ballgag2 = False #Affects 15_mail.rpy
        $ package_is_here = False # Turns True when days_in_delivery >= 5. Package is displayed.
        $ days_in_delivery = 0 #Count's +1 every day when order_placed = True
        
        $ ballgag += 2 #Amount of anal lubricant in possesion. 

        $ the_gift = "03_hp/18_store/15.png" # BALL GAG.
        show screen gift
        with d3
        ">2 Кляпа и наручники были добавлены в вашу собственность."
        hide screen gift
        with d3
        call screen main_menu_01

    if bought_ballgag3:
        define bought_ballgag3 = False #Fix Error
        $ bought_ballgag3 = False #Affects 15_mail.rpy
        $ package_is_here = False # Turns True when days_in_delivery >= 5. Package is displayed.
        $ days_in_delivery = 0 #Count's +1 every day when order_placed = True
        
        $ ballgag += 3 #Amount of anal lubricant in possesion. 

        $ the_gift = "03_hp/18_store/15.png" # BALL GAG.
        show screen gift
        with d3
        ">3 Кляпа и наручники были добавлены в вашу собственность."
        hide screen gift
        with d3
        call screen main_menu_01
        
    if bought_plug:
        $ bought_plug = False #Affects 15_mail.rpy
        $ package_is_here = False # Turns True when days_in_delivery >= 5. Package is displayed.
        $ days_in_delivery = 0 #Count's +1 every day when order_placed = True
        
        $ plug += 1 #Amount of anal lubricant in possesion. 

        $ the_gift = "03_hp/18_store/16.png" # ANAL PLUG.
        show screen gift
        with d3
        ">Ассортимент анальных пробок был добавлен в вашу собственность."
        hide screen gift
        with d3
        call screen main_menu_01

    if bought_plug2:
        define bought_plug2 = False #Fix Error
        $ bought_plug2 = False #Affects 15_mail.rpy
        $ package_is_here = False # Turns True when days_in_delivery >= 5. Package is displayed.
        $ days_in_delivery = 0 #Count's +1 every day when order_placed = True
        
        $ plug += 2 #Amount of anal lubricant in possesion. 

        $ the_gift = "03_hp/18_store/16.png" # ANAL PLUG.
        show screen gift
        with d3
        ">2 Ассортимента анальных пробок был добавлен в вашу собственность."
        hide screen gift
        with d3
        call screen main_menu_01

    if bought_plug3:
        define bought_plug3 = False #Fix Error
        $ bought_plug3 = False #Affects 15_mail.rpy
        $ package_is_here = False # Turns True when days_in_delivery >= 5. Package is displayed.
        $ days_in_delivery = 0 #Count's +1 every day when order_placed = True
        
        $ plug += 3 #Amount of anal lubricant in possesion. 

        $ the_gift = "03_hp/18_store/16.png" # ANAL PLUG.
        show screen gift
        with d3
        ">3 Ассортимента анальных пробок был добавлен в вашу собственность."
        hide screen gift
        with d3
        call screen main_menu_01
        
    if bought_mag1:
        $ bought_mag1 = False #Affects 15_mail.rpy
        $ package_is_here = False # Turns True when days_in_delivery >= 5. Package is displayed.
        $ days_in_delivery = 0 #Count's +1 every day when order_placed = True
        
        $ mag1 += 1 #Amount of anal lubricant in possesion. 

        $ the_gift = "03_hp/18_store/17.png" # MAGAZINE # 1
        show screen gift
        with d3
        ">Ассортимент образовательных журналов был добавлен в вашу собственность."
        hide screen gift
        with d3
        call screen main_menu_01

    if bought_mag12:
        define bought_mag12 = False #Fix Error
        $ bought_mag12 = False #Affects 15_mail.rpy
        $ package_is_here = False # Turns True when days_in_delivery >= 5. Package is displayed.
        $ days_in_delivery = 0 #Count's +1 every day when order_placed = True
        
        $ mag1 += 2 #Amount of anal lubricant in possesion. 

        $ the_gift = "03_hp/18_store/17.png" # MAGAZINE # 1
        show screen gift
        with d3
        ">2 Ассортимента образовательных журналов был добавлен в вашу собственность."
        hide screen gift
        with d3
        call screen main_menu_01

    if bought_mag13:
        define bought_mag13 = False #Fix Error
        $ bought_mag13 = False #Affects 15_mail.rpy
        $ package_is_here = False # Turns True when days_in_delivery >= 5. Package is displayed.
        $ days_in_delivery = 0 #Count's +1 every day when order_placed = True
        
        $ mag1 += 3 #Amount of anal lubricant in possesion. 

        $ the_gift = "03_hp/18_store/17.png" # MAGAZINE # 1
        show screen gift
        with d3
        ">3 Ассортимента образовательных журналов был добавлен в вашу собственность."
        hide screen gift
        with d3
        call screen main_menu_01
        
    if bought_mag2:
        $ bought_mag2 = False #Affects 15_mail.rpy
        $ package_is_here = False # Turns True when days_in_delivery >= 5. Package is displayed.
        $ days_in_delivery = 0 #Count's +1 every day when order_placed = True
        
        $ mag2 += 1 #Amount of anal lubricant in possesion. 

        $ the_gift = "03_hp/18_store/18.png" # MAGAZINE # 2
        show screen gift
        with d3
        ">Ассортимент женских журналов был добавлен в вашу собственность."
        hide screen gift
        with d3
        call screen main_menu_01

    if bought_mag22:
        define bought_mag22 = False #Fix Error
        $ bought_mag22 = False #Affects 15_mail.rpy
        $ package_is_here = False # Turns True when days_in_delivery >= 5. Package is displayed.
        $ days_in_delivery = 0 #Count's +1 every day when order_placed = True
        
        $ mag2 += 2 #Amount of anal lubricant in possesion. 

        $ the_gift = "03_hp/18_store/18.png" # MAGAZINE # 2
        show screen gift
        with d3
        ">2 Ассортимента женских журналов был добавлен в вашу собственность."
        hide screen gift
        with d3
        call screen main_menu_01

    if bought_mag23:
        define bought_mag23 = False #Fix Error
        $ bought_mag23 = False #Affects 15_mail.rpy
        $ package_is_here = False # Turns True when days_in_delivery >= 5. Package is displayed.
        $ days_in_delivery = 0 #Count's +1 every day when order_placed = True
        
        $ mag2 += 3 #Amount of anal lubricant in possesion. 

        $ the_gift = "03_hp/18_store/18.png" # MAGAZINE # 2
        show screen gift
        with d3
        ">3 Ассортимента женских журналов был добавлен в вашу собственность."
        hide screen gift
        with d3
        call screen main_menu_01
        
    if bought_mag3:
        $ bought_mag3 = False #Affects 15_mail.rpy
        $ package_is_here = False # Turns True when days_in_delivery >= 5. Package is displayed.
        $ days_in_delivery = 0 #Count's +1 every day when order_placed = True
        
        $ mag3 += 1 #Amount of anal lubricant in possesion. 

        $ the_gift = "03_hp/18_store/19.png" # MAGAZINE # 3
        show screen gift
        with d3
        ">Ассортимент журналов для взрослых был добавлен в вашу собственность."
        hide screen gift
        with d3
        call screen main_menu_01

    if bought_mag32:
        define bought_mag32 = False #Fix Error
        $ bought_mag32 = False #Affects 15_mail.rpy
        $ package_is_here = False # Turns True when days_in_delivery >= 5. Package is displayed.
        $ days_in_delivery = 0 #Count's +1 every day when order_placed = True
        
        $ mag3 += 2 #Amount of anal lubricant in possesion. 

        $ the_gift = "03_hp/18_store/19.png" # MAGAZINE # 3
        show screen gift
        with d3
        ">2 Ассортимента журналов для взрослых был добавлен в вашу собственность."
        hide screen gift
        with d3
        call screen main_menu_01

    if bought_mag33:
        define bought_mag33 = False #Fix Error
        $ bought_mag33 = False #Affects 15_mail.rpy
        $ package_is_here = False # Turns True when days_in_delivery >= 5. Package is displayed.
        $ days_in_delivery = 0 #Count's +1 every day when order_placed = True
        
        $ mag3 += 3 #Amount of anal lubricant in possesion. 

        $ the_gift = "03_hp/18_store/19.png" # MAGAZINE # 3
        show screen gift
        with d3
        ">3 Ассортимента журналов для взрослых был добавлен в вашу собственность."
        hide screen gift
        with d3
        call screen main_menu_01
        
    if bought_mag4:
        $ bought_mag4 = False #Affects 15_mail.rpy
        $ package_is_here = False # Turns True when days_in_delivery >= 5. Package is displayed.
        $ days_in_delivery = 0 #Count's +1 every day when order_placed = True
        
        $ mag4 += 1 #Amount of anal lubricant in possesion. 

        $ the_gift = "03_hp/18_store/20.png" # MAGAZINE # 4
        show screen gift
        with d3
        ">Ассортимент порно журналов был добавлен в вашу собственность."
        hide screen gift
        with d3
        call screen main_menu_01
        
    if bought_mag42:
        define bought_mag42 = False #Fix Error
        $ bought_mag42 = False #Affects 15_mail.rpy
        $ package_is_here = False # Turns True when days_in_delivery >= 5. Package is displayed.
        $ days_in_delivery = 0 #Count's +1 every day when order_placed = True
        
        $ mag4 += 2 #Amount of anal lubricant in possesion. 

        $ the_gift = "03_hp/18_store/20.png" # MAGAZINE # 4
        show screen gift
        with d3
        ">2 Ассортимента порно журналов был добавлен в вашу собственность."
        hide screen gift
        with d3
        call screen main_menu_01

    if bought_mag43:
        define bought_mag43 = False #Fix Error
        $ bought_mag43 = False #Affects 15_mail.rpy
        $ package_is_here = False # Turns True when days_in_delivery >= 5. Package is displayed.
        $ days_in_delivery = 0 #Count's +1 every day when order_placed = True
        
        $ mag4 += 3 #Amount of anal lubricant in possesion. 

        $ the_gift = "03_hp/18_store/20.png" # MAGAZINE # 4
        show screen gift
        with d3
        ">3 Ассортимента порно журналов был добавлен в вашу собственность."
        hide screen gift
        with d3
        call screen main_menu_01

    if bought_beer:
        $ bought_beer = False #Affects 15_mail.rpy
        $ package_is_here = False # Turns True when days_in_delivery >= 5. Package is displayed.
        $ days_in_delivery = 0 #Count's +1 every day when order_placed = True
        
        $ beer += 1 

        $ the_gift = "03_hp/18_store/21.png" # BUTTERBEER.
        show screen gift
        with d3
        ">Бутылка сливочного пива была добавлена в вашу собственность."
        hide screen gift
        with d3
        call screen main_menu_01

    if bought_beer2:
        define bought_beer2 = False #Fix Error
        $ bought_beer3 = False #Affects 15_mail.rpy
        $ package_is_here = False # Turns True when days_in_delivery >= 5. Package is displayed.
        $ days_in_delivery = 0 #Count's +1 every day when order_placed = True
        
        $ beer += 2 

        $ the_gift = "03_hp/18_store/21.png" # BUTTERBEER.
        show screen gift
        with d3
        ">2 Бутылки сливочного пива была добавлена в вашу собственность."
        hide screen gift
        with d3
        call screen main_menu_01

    if bought_beer3:
        define bought_beer3 = False #Fix Error
        $ bought_beer3 = False #Affects 15_mail.rpy
        $ package_is_here = False # Turns True when days_in_delivery >= 5. Package is displayed.
        $ days_in_delivery = 0 #Count's +1 every day when order_placed = True
        
        $ beer += 3 

        $ the_gift = "03_hp/18_store/21.png" # BUTTERBEER.
        show screen gift
        with d3
        ">3 Бутылки сливочного пива была добавлена в вашу собственность."
        hide screen gift
        with d3
        call screen main_menu_01
        
    if bought_owl:
        $ bought_owl = False #Affects 15_mail.rpy
        $ package_is_here = False # Turns True when days_in_delivery >= 5. Package is displayed.
        $ days_in_delivery = 0 #Count's +1 every day when order_placed = True
        
        $ owl += 1 

        $ the_gift = "03_hp/18_store/22.png" # PLUSH OWL.
        show screen gift
        with d3
        ">Плюшевая сова была добавлена в вашу собственность."
        hide screen gift
        with d3
        call screen main_menu_01
        
    if bought_owl2:
        define bought_owl2 = False #Fix Error
        $ bought_owl = False #Affects 15_mail.rpy
        $ package_is_here = False # Turns True when days_in_delivery >= 5. Package is displayed.
        $ days_in_delivery = 0 #Count's +1 every day when order_placed = True
        
        $ owl += 2 

        $ the_gift = "03_hp/18_store/22.png" # PLUSH OWL.
        show screen gift
        with d3
        ">2 Плюшевая сова была добавлена в вашу собственность."
        hide screen gift
        with d3
        call screen main_menu_01

    if bought_owl3:
        define bought_owl3 = False #Fix Error
        $ bought_owl = False #Affects 15_mail.rpy
        $ package_is_here = False # Turns True when days_in_delivery >= 5. Package is displayed.
        $ days_in_delivery = 0 #Count's +1 every day when order_placed = True
        
        $ owl += 3 

        $ the_gift = "03_hp/18_store/22.png" # PLUSH OWL.
        show screen gift
        with d3
        ">3 Плюшевые сова была добавлена в вашу собственность."
        hide screen gift
        with d3
        call screen main_menu_01

    if bought_badge_01:
        $ bought_badge_01 = False #Affects 15_mail.rpy
        $ package_is_here = False # Turns True when days_in_delivery >= 5. Package is displayed.
        $ days_in_delivery = 0 #Count's +1 every day when order_placed = True
        
        $ badge_01 = 1 

        $ the_gift = "03_hp/18_store/29.png" # S.P.E.W. Badge.
        show screen gift
        with d3
        ">Значок \"А.В.Н.Э.\" был добавлен в вашу собственность."
        hide screen gift
        with d3
        call screen main_menu_01
    
    
    if bought_nets:
        $ bought_nets = False #Affects 15_mail.rpy
        $ package_is_here = False # Turns True when days_in_delivery >= 5. Package is displayed.
        $ days_in_delivery = 0 #Count's +1 every day when order_placed = True
        
        $ nets = 1 

        $ the_gift = "03_hp/18_store/30.png" # FISHNETS.
        show screen gift
        with d3
        ">Пара ажурных чулков была добавлена в вашу собственность."
        hide screen gift
        with d3
        call screen main_menu_01
