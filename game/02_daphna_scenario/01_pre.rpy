################
### LEVEL 01 ###                
###################REQUEST_01 JUST STAND THERE.
label daphne_pre_01: #Снейп обещает, что пришлет шлюху

    $snape.State(pos2=gMakePos( 340, 420 )).Visibility("head", transition=None)
    $hero("Послушай, Северус. Ты уже давно обещал прислать мне парочку слизеринских шлюх.")
    $snape("~29// Гхм...")
    $hero("Что значит твое «гхм»?... Я точно знаю, у тебя есть шлюхи!// Ты сам мне недавно хвалился, что делаешь что угодно с кем захочешь.")
    $snape("~03// Понимаешь, мой друг, все не так просто.//~04// Эти девки... Они уверены, что ты,... то есть, директор, не в курсе наших маленьких шалостей.")
    $hero("И?")
    $snape("~03// И если окажется, что директору тоже не чуждо стремление к потас...\n к прекрасному, то это разрушит все их мировоззрение...")
    $hero("Послушай, дружище. Мне нет дела до мировоззрения шлюх, в них меня интересуют совсем другие детали.") 
    $snape("~06// Да, но если они узнают о твоем интересе, они могут не захотеть больше этого делать.//~16// #(Надеюсь он проглотит эту хрень)//"
        "~29// #На самом деле я не собираюсь присылать ему шлюх -//"
        " #Он же, мать его, джинн, обладающий крутой космической силой и все такое!//~26// #Кто знает насколько он хорош в ЭТОМ.")
    $hero("Ты думаешь, я проглочу эту хрень?")
    $snape("~05//Хрень?//~04// Мой друг! Я о тебе забочусь! Они реально могут перестать давать!")
    $hero("Давать кому, дружище?// Не тебе ли?// Я думаю, тебе просто нравится быть единственным петухом в курятнике.//"
        "Я тут не досыпаю ночей, тружусь, чтобы выдрессировать тебе девчонку,...// а ты катаешься, как сыр в масле и не хочешь помочь мне с маленьким развлечением.")
    $snape("~01// Да что тебя не устраивает?!// ~02//Я слышал у вас очень хорошо продвигается с мисс Грейнджер.")
    $hero("Ты хочешь поменяться? Я готов уступить тебе воспитание этой девчонки всего за пару шлюх.") 
    $snape("~29// Эм...")
    $hero("Я тебя предупреждаю, Северус, если ты будешь и дальше утаивать от меня девок,...// директор может перестать скрываться в башне и выйдет сам на поиски!")
    $snape("~01// Но ты не можешь!..")
    $hero("Продолжай в том же духе и увидишь могу я или нет...")
    $snape("~06//......")
    $hero("......")
    $snape("~02//............")
    $hero("............")
    $snape("~23// Ладно-ладно...// Ты меня убедил. Я пришлю тебе шлюху.")
    $hero("Двух шлюх, Северус.")
    $snape("~28// Я уверен, ЭТА тебе заменит двух сразу.")
    $hero("Смотри, если это окажется какая-то уродка...")
    $snape("~01// За кого ты меня принимаешь!// Чистая кровь в Мерлин знает каком поколении, была на обложке \"Ведьмополитен\"...//"
        "~02// #(стоит крайняя в пятом ряду)// ~01// ...чирлидерша, слизеринка, наконец!//"
        "~23// Девица - пальчики оближешь!")
    $hero("Ну, это ее забота... облизывать...// Так в чем подвох?")
    $snape("~05// Подвох?")
    $hero("Ты слишком быстро согласился. Вот я и спрашиваю: в чем подвох? ")
    $snape("~23// Никакого подвоха, мой друг!// ~02//Ты сам убедишься. Потерпи пару дней. Всего пару дней!")
    $snape.Visibility()
    "> Вы решаете довериться Снейпу и подождать два дня."
    "> Остаток вечера вы слушаете стенания Северуса\n о нелегкой доле преподавателя и\n фантазируете об обещанной шлюхе."

    $event.Finalize()
    jump day_start


label daphne_pre_02: #LV.1 (Whoring = 0 - 2)
    $ renpy.play('sounds/knocking.mp3') #Sound someone knocking on the door.
    "*Тук-тук-тук!*"
    $daphne.Visibility()
    menu:
        "\"Кто это?\"":
            $daphne(who, "Сэр, меня прислал профессор Снейп...")
            $hero("#(Превосходно! Шлюха прибыла!)// #(Надеюсь, она ничего. Впрочем, после стольких дней воздержания я не очень переборчив.)")
        "\"Да, входи...\"":
            pass

#    skaz "Жаль прерываться на самом интересном месте? "
#    skaz "Нам тоже. Но данная сюжетная линия пока дописана только до этой точки..."
#    skaz "(впрочем, вам доступны другие сюжетные линии)."
#    skaz "Оставьте ваши вопросы, благодарности и пожелания на нашем {a=http://wtrus.ixbb.ru/viewtopic.php?id=9}ФОРУМЕ{/a}. \nТак вы простимулируете нас и продолжение появится быстрее. :)"
    $daphne.LoadDefItemSets()
    $daphne.chibi.State("door", speed="go").Trans(d4, "blink").Trans("go center", "blink") # Если делать dissolve в движении, то сбивается счетчик времени. Лучше выполнить появление чибика стоя, затем уже двигать его 
    pause.5
    $screens.ShowD3("bld1")



    $daphne.State(pos="door").Visibility("body+")("~55 00 1 smi// Добрый день, профессор Дамблдор.") 
#    $hermi.Visibility("body+")(".....")

    $screens.Show("ctc").Pause()

    $hero  (m, "#(О-о, вот это шлюшка! Обожаю длинноногих блондинок!...)//#(...а также брюнеток, шатенок и рыжих. Я могу кончить от одного их вида!)// #(Вот только сиськи маловаты. Может, их подрастить заклинанием?..)", 
        g4, "#(Нет, джинни, умерь свои фантазии. Вспомни, что случилось, когда ты растил сиськи принцессе... мда)", 
        m, "Здравствуйте, мисс э-э... \n#(Великие пески, почему он не сказал как ее зовут?).") 
    $daphne("~55 00 1 def// Профессор Снейп сообщил, что вы хотели меня видеть.") 
    $hero  ("Эм, да. Несомненно хотел... видеть.// Но, он же сказал, зачем он тебя прислал?") 
    $daphne("~55 00 1 smi", "Нет, сэр. Он не сказал.") 
    $hero  ("#(Думаю, нужно с ней немного поболтать. Просто для разогрева.)") 

    menu: 
        "Поговорить насчет учебы": 
            $hero  ("Что ж, мисс, я хотел поговорить насчет вашей учебы.") 
            $daphne("Учеба не то, что меня волнует, сэр.// ~46 n0 1 def// Меня гораздо больше волнует, почему в Хогвартсе обучается грязнокровое мугродье.//" 
                "Вы же чистокровный волшебник, сэр?") 
            $hero  (g4, "Кто? Я?.. А, ну да. Вроде того.") 
            $daphne("~55 00 1 pur",  "Хм. Вы по делу смущаетесь.// По древности рода с Гринграссами никто не сравнится, так что вы и должны чувствовать себя неловко.") 
            $hero  (m,"(Гринграссы? Что это еще за хрень?)") 
            $daphne("~46 00 1 pur",  "Но как бы то ни было, сэр. Вы должны были проследить, чтобы  мугродье не чувствовало себя здесь вольготно.", 
                "А вы вместо этого каждый год принимаете новых.// ~46 03 1 smi// И чистокровные девочки должны испытывать сложности.") 
            $hero  ("Чистокровные девочки?") 
            $daphne("~46 n0 1 pur",  "Да, сэр! Почему эту грязнокровку называют лучшей на курсе?//"
                "Почему мугродью разрешается дышать одним воздухом с истинными волшебниками?//" 
                "~64 n0 1 pur// Я могу еще быть рядом со всякими Малфоями или Паркинсон.//" 
                "Семейки так себе, второй сорт. Но какие-никакие чистокровки, а эта девица!!!") 
        "Поговорить насчет факультета": 
            $hero  ("Что ж, мисс, я хотел поговорить об обстановке на факультете.") 
            $daphne("~46 n0 1 def",  "Обстановка на факультете, сэр? Она отвратительна!// Грязнокровое мугродье заполонило Хогвартс.") 
            $hero  ("#(Что это за?..)") 
            $daphne("~55 n0 1 ope",  "И вы делаете вид, что этого не замечаете. Хотя ваш отец...// Вот он был истинным чистокровным волшебником и не побоялся прикончить троих маглов. За что его и упрятали в Азкабан.") 
            $hero  ("Правда, что ли? #(Ну и висельники в родстве с местным директором)") 
            $daphne("~55 00 1 dis",  "Не притворяйтесь, что вы этого не помните, сэр!// А если позабыли, это не делает вам чести!", 
                "~55 00 1 pou// Гринграссы всегда стояли за чистоту крови и когда видишь волшебника, который предает наши идеалы...") 

    $hero  ("#(Хм, какая экспрессия! Интересно, трахается она так же энергично?)// Постойте, мисс, это все очень увлекательно, но, может, уже завершим прелюдию и приступим?") 
    $daphne("~64 00 1 smi// Приступим к чему, сэр?") 
    $hero  ("Ну, к этому самому... чпоки-чпоки, тити-мити, а?") 
    $daphne("~64 w0 1 pur",  "\"Чпоки-чпоки\", сэр?") 
    $hero  ("Ну я не знаю, как это у вас, девушек, называется.// В общем, то, что вы постоянно делаете с профессором и зачем он вас сюда прислал.") 
    $daphne("~64 w0 1 pou// Я не понимаю, сэр.") 
    $hero  ("О, великие пески пустыни!// #(Она небыстро шевелит мозгами. Надеюсь, что бедрами шевелит быстрее.)//" 
        "Я говорю, заняться тем, чем обычно занимаются шлю... девчонки вроде вас.") 
    $daphne("~55 n0 1 dis// На что это вы намекаете?!") 
    $hero  ("Я намекаю? Да я прямо говорю!...") 
    $daphne("~55 n0 1 ang",  "Если вы смеете намекать на то, чем занимаются некоторые особы с преподавателями, то это омерзительно!") 
    $hero  ("#(Э-э, Снейп, это что, шутка?)") 
    $daphne("~55 n0 1 ope",  "Я сегодня же пошлю сову родителям и сообщу о грязных предложениях, которые вы мне тут делаете.", 
        "А уж они донесут об этом в министерство, будьте уверены.") 
    $hero  (g4, "#(Не могу поверить!... Чертов Снейп!!!)// Эм, постойте, мисс, вы неправильно поняли!") 
    $daphne("~46 n0 1 ope// Я все правильно поняла! Вам недолго осталось сидеть в этом кресле!") 

    $screens.HideD3("bld1")
    $daphne.Visibility(transition=d3).chibi.Trans("goout door").Hide(d3)    
    $ renpy.play('sounds/door.mp3') #Sound of a door opening.
    pause.5

    $hero("...................................")


    $event.Finalize()
    return
#    jump day_start

label daphne_pre_03: #Разборки со Снейпом после того, как шлюха оказалась не шлюхой

    $screens.Hide("snape_main")
    $snape.State("doorleft").Visibility("body", transition=Dissolve(.5))

    $hero("Что это было?!.. Отвечай мне, во имя гребаных песков пустыни!")
    $snape("~29// Ты о чем, мой друг?")
    $hero("Не прикидывайся овечкой! Я просил у тебя шлюху, мать твою, а ты кого мне прислал?")
    $snape("~29// Ну, технически она шлюха.")
    $hero("Что это вообще значит «технически она шлюха»?")
    $snape("~29// Ну у нее есть все необходимое для шлюхи. Все нужные хм, детали. И какая экспрессия!")
    $hero("Да уж, экспрессию было трудно не заметить.")
    $snape("~29// Я бы ее с удовольствием разложил на полу.")
    $hero("Я бы тоже ее с удовольствием... Постой, так ты сам ни разу ее не трахал?!")
    $snape("~29// За кого ты меня принимаешь, мой друг? Разве стал бы я предлагать тебе пользованный товар?// Чистокровная...")
    $hero("Про чистокровную я уже наслушался, твою мать!")
    $snape("~29// Чистокровная нетронутая юная волшебница, которая только и ждет, чтобы кто-нибудь ее объездил.")
    $hero("И ты решил, что я лучше всех подхожу на эту роль.")
    $snape("~29// Ну, у тебя неплохо получается с мисс Грейнджер. Я был уверен, что ты не спасуешь и перед мисс Гринграсс.")
    $hero("Если бы ты, дружище, хотя бы предупредил меня, я бы может что-то и придумал.//"
        " Но теперь эта юная сука настучит родителям и министерская проверка – самое меньшее, что нас ждет.//"
        "Предупреждаю, если меня вынесут из этого кабинета, то тебя вынесут следом #(если я не найду способа смыться раньше)")
    $snape("~29// Не все так трагично, мой друг. Я поговорил с мисс Гринграсс, и она готова не сообщать ничего родителям.// Пока.")
    $hero("Слово «пока» особенно обнадеживает, гребаные пески.//"
        "Я не спрашиваю как тебе это удалось. И все же, прости мое любопытство,...//"
        "...если ты так замечательно ладишь с этой сучкой, почему ты до сих пор не трахнул ее?!")
    $snape("~29// Мой друг. Одно дело убедить заносчивую дрянь в том, что шум вокруг такого деликатного предмета, как ее невинность, не в ее интересах.//"
        " И совсем другое - залезть к ней в трусики.// Я хочу предоставить эту честь тебе.")
    $hero("Не собираюсь я с ней больше встречаться!")
    $snape("~29// Боюсь, у тебя нет выбора.")
    $hero("Та-ак... Чего я еще не знаю?")
    $snape("~29// Не хочу на тебя давить, мой друг.// Поэтому давай просто предоставим событиям идти своим чередом, может все и обойдется.//"
        "Но на твоем месте я бы уже начал задумываться как расположить к себе очаровательную девушку из древнего и благородного рода.//"
        "А теперь извини, мне пора идти.")

#    $snape.Visibility()

    $event.Finalize()
    jump snape_nothing
#    if daytime:
#        jump night_start
#    else: 
#        jump day_start

