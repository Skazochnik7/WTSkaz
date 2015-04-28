################
### LEVEL 01 ###                
###################REQUEST_01 JUST STAND THERE.
label dap_request_01: #LV.1 (Whoring = 0 - 2)

    play music "music/Chipper Doodle v2.mp3" fadein 1 fadeout 1 

    if IsRunNumber(1):
#    if daphne.whoring<3:
        $hero("Хорошо, мисс, тогда просто расскажите о тех, кто вас окружает. Мы должны понимать с кем имеем дело.")
        $daphne("Ну, мне они, в общем-то, неинтересны, буду я еще обращать внимание на всяких недоволшебников.")
        $hero("Но мисс, чтобы вы заняли на факультете подобающее положение, кто-то должен занять неподобающее. Количество положений довольно ограничено. Вы меня понимаете?")
        $daphne("Ну, понимаю,... кажется.")
        $hero("Поэтому я дам вам задание, вы должны интересоваться другими студентками.// Находить их слабые места, всякого рода недостатки и может быть даже скелеты в шкафу...")
        $daphne("Вы предлагаете мне стучать, сэр? Это недопустимо!")
        $hero("Странно, что мне об этом говорит студентка Слизерина.// Вы не ошиблись факультетом, дорогая? Может, вам дорога в  прямой, как доска, Гриффиндор?")
        $daphne("Хм... Но я...")
        $hero("Я не предлагаю вам \"стучать\", как вы выразились.// Просто изучите своих конкуренток, напомню, многие из них будут выступать на конкурсе.//"
            "Вам нужно заботиться не только о том, как красиво подать себя на сцене, мисс, но и о вашем месте на факультете.//"
            "Чем выше оно будет, тем больше вероятности, что за вас проголосуют – голоса студентов тоже учитываются. Понимаете меня?")
        $hero("Если вы будете успешны, вас ожидает приз.")
    elif IsRunNumberOrMore(2):
        $hero("Так, мисс Гринграсс. Давайте-ка вы сегодня снова займетесь изучением ваших конкуренток.")
        $daphne("Опять, сэр?")
        $hero("Ну, если вы уже все о них знаете…")
        $daphne("Пока не все, сэр.")
        $hero("Тогда вперед, жду вас вечером с отчетом.")

    return



label dap_request_01_complete:
    $daphne.Visibility()
    $daphne.chibi.State("door", speed="go").Trans(d4, "blink").Trans("go center", "blink") # Если делать dissolve в движении, то сбивается счетчик времени. Лучше выполнить появление чибика стоя, затем уже двигать его 
    pause.5
    $screens.ShowD3("bld1")

    $daphne.State(pos="door").Visibility("body+")("~55 00 1 smi// Добрый вечер, профессор Дамблдор.") 


    if IsRunNumber(1):
        $hero("Итак, какой результат.")
        $daphne("Ну я смотрела за Джесси. Похоже, она не слишком прилежно учится.")
        $hero("И?")
        $daphne("И это пока все, сэр.")
        $hero("И как это поможет вам подняться выше Джесси, мисс? Ее плохая учеба влияет на ее популярность?")
        $daphne("Ну, в общем-то, нет.")
        $hero("Значит задание вы сегодня не выполнили, мисс.")
        $daphne("Похоже, что так.")
        $hero("И тем не менее, я готов вас простимулировать. Уверен, это поможет вам в следующий раз.")
    elif IsRunNumber(2):
        $daphne("Сегодня, сэр. Я решила подойти к вопросу системно.")
        $hero("Вот как?")
        $daphne("Да, сэр. Мне кажется, я начала понимать, почему одни девчонки популярнее, чем другие.")
        $hero("(Тоже мне бином Ньютона)")
        $hero("Слушаю вас, мисс.")
        $daphne("Мне надо еще кое-что проверить, сэр, в следующий раз я смогу рассказать вам.")
        $daphne("А сегодня я присматривалась к Мелиссе, она заигрывала с парнями.")
        $hero("И как вам это?")
        $daphne("Отвратительно, сэр. Как может она это делать – среди них были не только полукровки, но и мугродье.")
        $hero("Не может быть!")
        $daphne("Да, сэр, представьте себе.")
        $hero("И что же?")
        $daphne("Парни вились вокруг нее, сэр. И знаете, мне показалось, что некоторые не прочь были с ней зайти дальше заигрываний.")
        $hero("Вот это неожиданность!")
        $daphne("Я тоже была шокирована, сэр. Я никогда не смотрела на это так. Я была уверена, что чистая кровь откроет любые двери и всякие заигрывания никому не нужны. Но почему-то сегодня вокруг меня не было ни одного парня, а к этой девице они летели, как мухи на…")
        $hero("На мед?")
        $daphne("Я хотела употребить более сильное слово, сэр. Но пусть будет «мед».")
        $hero("И что же теперь, мисс?")
        $daphne("Мне надо время, чтобы во всем этом разобраться, сэр.")
        $hero("Ну что ж, мисс Гринграсс, похоже, работа идет. Я хочу вас наградить.")
    elif IsRunNumber(3):
        $daphne("Мне кажется, я поняла, сэр.")
        $hero("Да?")
        $daphne("Популярность может определять учебой и популярностью у парней, и чистотой крови.")
        $hero("Я гляжу, вы серьезно копали, мисс, я не ошибся в вас.")
        $daphne("Спасибо, сэр.")
        $hero("Ну, с чистотой крови у вас все в порядке.")
        $daphne("Да, это так сэр! Такой чистой крови нет ни у кого ни в Хогвартсе, но и в Дурмшанге.")
        $hero("Что насчет учебы?")
        $daphne("Ну, не думаю, что чистокровные волшебницы должны сильно напрягаться, чтобы зарабатывать оценки у каких-то преподавателей с сомнительной родословной. Пусть для этого тужится всякое мугродье типа Грейнджер. Я и так знаю, что я лучшая.")
        $hero("Хм. Тогда этот путь к популярности вычеркиваем. Но одной чистоты крови, маловато, мисс.")
        $daphne("Я тоже думала об этом, сэр.")
        $hero("Остаются, мужчины?")
        $daphne("Мужчины, сэр?")
        $hero("Ну вы назвали три пути получения популярности. Насколько я понимаю: плюс кровь, минус учеба - остаются мужчины.")
        $daphne("Эм…")
        $daphne("Но, сэр, я не думаю, что я должна выпрыгивать из трусиков, чтобы добиться благосклонности каких-то парней.")
        $hero("(Хе-хе, «выпрыгивать из трусиков» - славная метафора. Думаю, вскоре ты будешь из них выпрыгивать, девушка).")
        $hero("Ну что ж, мисс. Тогда с популярностью у нас пока проблемы. Возможно, вам придут в голову другие мысли, потому что дата первого этапа конкурса приближается. А пока хочу дать вам подарок.")

    $screens.HideD3("bld1")
    $daphne.Visibility(transition=d3).chibi.Trans("goout door").Hide(d3)    
    $ renpy.play('sounds/door.mp3') #Sound of a door opening.
    pause.5

    $hero("...................................")
    return event.Finalize()