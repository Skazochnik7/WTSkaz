label mail:

    $ this.RunStep("MAIL")    

    if finished_report >= 1:
        $ letters -= 1 #Adds one letter in waiting list to be read. Displays owl with envelope.
        $ got_paycheck = False #When TRUE the paycheck is in the mail. Can't do paper work.
        hide screen owl
        show screen owl_02
        ">Вы читаете свои сообщения."
        play sound "sounds/money.mp3"  #Quiet...

        $dgold=([40, 70, 90, 110, 150, 200][finished_report-1])*turbo
        $ letter_text = "{size=-7}ОТ:Министерства Магии\nКому: Профессору Дамблдору\n\n\n{/size}{size=-2}Благодарим Вас за отчеты, присланные на этой неделе.\n Ваша оплата:{/size} \n{size=+4}[dgold] галеонов.{/size}\n\n\n{size=-3}-С уважением-{/size}"    
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

        $screens.ShowD3("gift", par1=evn._img).Say(">Книга [evn._caption] была добавлена в Вашу коллекцию.").HideD3("gift")

#        $ the_gift = evn._img #"03_hp/18_store/08.png" # Copper book of spirit.
#        show screen gift
#        with d3
#        ">Книга [evn._caption] была добавлена в Вашу коллекцию."
#        hide screen gift
#        with d3
        call screen main_menu_01  


    
    
    
    
    
### ITEMS ###  
    if itsOWL.Any():
        $item=itsOWL()[0]
        $_count=itsOWL.Count(item.Name)
        $hero.Items.AddItem(item.Name, _count)  
        $itsOWL.Clear()
        $ package_is_here = False # Turns True when days_in_delivery >= 5. Package is displayed.

        $screens.ShowD3("gift", par1=item._img).Say(">Добавлено к вашим вещам: [item._caption], [_count] шт. ").HideD3("gift")

#        $ the_gift = item._img 
#        show screen gift
#        with d3
#        ">Добавлено к вашим вещам: [item._caption], [_count] шт. "
#        hide screen gift
#        with d3
        call screen main_menu_01



label bigletter(__pages): #Письмо родителей Дафны Дамблдору
    $screens.Hide("owl").Show("owl_02")
    $ letters -= 1

    $__pageIndex=0
    label letterbig_newpage:
    $screens.Show("letterbig", par1=__pages[__pageIndex])
    $screens.Show("ctc", d3, "bld1").Pause()

    menu:
        "<<< Вернуться " if __pageIndex>0:
            $__pageIndex-=1                
            jump letterbig_newpage
        " Продолжить >>>" if __pageIndex<len(__pages)-1:
            $__pageIndex+=1
            jump letterbig_newpage
        "- Завершить -":
            pass    
    $screens.Hide("letterbig", "ctc", d3, "bld1")
    return





label daphne_pre_04: #Письмо родителей Дафны Дамблдору
    call bigletter(["{size=-7}От: Оливии Гринграсс\nКому: Профессору Дамблдору\n\n{/size}"
    "{size=-4}Профессор Дамблдор!\n\nМы с мужем серьезно обеспокоены тем, что наша дочь не получает достаточно внимания в Хогвартсе и до сих пор не заняла в нем подобающего положения.\n\n "
    "Профессор Северус Снейп проинформировал нас, что вы, наконец-то, спохватились и вызвались давать ей частные уроки.\n\n Вы непозволительно долго шли к этому, профессор!\n\n "
    "Надеемся, что ваши запоздалые действия возымеют хоть какой-то эффект...{/size}\n\n ",
    "{size=-4}...Как вы знаете, в министерстве намечено очередное заседание по вопросам выделения фондов магическим учебным заведениям.\n\n "
    "Информируем вас, что если вами не будет достигнут достаточный прогресс, Дафна будет переведена в Дурмштанг - в академию, где умеют ценить настоящих чистокровных магов.\n\n "
    "Мы же в этом случае приложим все усилия, чтобы Хогвартс получил самое минимальное финансирование.{/size}\n\n "
    "{size=-3}Без особой надежды на ваш успех,\nОливия Гринграсс.{/size}"])

    $hero(g4, "{size=+5}Гре - {/size}{size=+3}ба - {/size}{size=+1}ны - {/size}{size=-1}е     {/size}{size=-3}пес - {/size}{size=-5}ки-и-и.......{/size}",
        m,"Чувствуется почерк дружищи Снейпа, и я не уверен, что мне это нравится.//"
        "Подобающее положение?! Если она у меня займет подобающее ЕЙ положение, оно не слишком понравится ее мамочке!//"
        "Великие пески, придется все время трястись, чтобы не сболтнуть лишнего, и она не настучала родителям...//"
        "Но чему ее учить, если я вообще ничего о ней не знаю?!")

    $event.Finalize()

    call screen main_menu_01


label daphne_pre_07: #Выписка из личного дела Дафны, присланная Снейпом
    call bigletter(["{size=-7}От: Северуса Снейпа\nКому: Профессору Дамблдору\n\n{/size}"
    "{size=+2}Выписка из досье на Дафну Гринграсс\n\n{/size}"
    "{size=-4}Рост: 5' 8\", Вес: 53 kg, Размер груди: 34В\n\n"
    "Ориентация: Предположительно гетеро.\n\n"
    "Девственница: Нет доказательств обратного.\n\n"
    "Мастурбация: Да? (доказательства косвенные: однокурсница, случайно оказавшаяся рядом, слышала стоны, раздающиеся из кабинки в душе)\n\n"
    "Просмотр порно: Да? (доказательства косвенные: случайно оставленный диск с порно исчез, в гостиную кроме Гринграсс никто не входил)\n\n"
    "Подглядывание: Да? (доказательства косвенные: была застигнута около отверстия, которое однокурсницы проделали в мужскую душевую, но поймана за подглядыванием не была){/size}",
    "{size=-4}Сексуальные страхи и установки:\n\n" 
    "* считает, что ее грудь слишком мала\n"
    "* считает, что спать можно только с чистокровным высоким, мужественным\n"
    "* боится, что не сможет удовлетворить чистокровного высокого, мужественного...\n"
    "* комплексует по поводу своего маленького (отсутствующего?) сексуального опыта\n\n"
    "Девиации: Не обнаружены{/size}\n\n "
    "{size=-3}Успехов, мой друг!\nСеверус Снейп.{/size}"
    "P.S. Мисс Гринграсс получила напутственное письмо от родителей. Думаю, будет правильно, мой друг, если не ты будешь вызывать ее, а она сама придет к тебе на первое занятие."])

    $hero(m,"Ну и досье. Он что диссертацию по ней собирался писать? И почти ничего ценного: Нет доказательств, не обнаржено, доказательства косвенные...//"
        "Неудивительно, что у него ничего с ней не вышло...// Хм, значит она должна прийти сама. Нужно бы подготовиться. Но как?")

    $event.Finalize()

    call screen main_menu_01



