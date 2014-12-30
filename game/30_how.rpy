label howtoplay:
    $ end_u_1_pic =  "title3.jpg" #<---- SCREEN
    show screen end_u_1                                             #<---- SCREEN
    play music "music/silly_fun_loop.mp3" fadein 1 fadeout 1 # LOLA'S THEME.
    if not persistent.tut: #Turns TRUE after tutorial happened once already. EVENT_01
        
        
        
        
        $ lola_face = "03_hp/22_lola/01.png"
        $ lola_body = "03_hp/22_lola/body_01.png"
        
        $ l_things = True
        #$ l_blush = True
        $ lx = 490
        $ ly = 190
        show screen l_head
        l "Привет интернет-извращугам!"
        hide screen l_head
        a5 "Следи за языком, сука!"
        $ l_things = False
        $ lola_face = "03_hp/22_lola/02.png"
        show screen l_head
        l "Хах...?"
        hide screen l_head
        a6 "Что я тебе говорил о слове на букву \"и\"?"
        $ l_question = True
        $ lola_face = "03_hp/22_lola/03.png"
        show screen l_head
        l "Эм... Использовать его как можно чаще..?"
        hide screen l_head
        pause.01
        with hpunch
        a7 "{size=+7}Нет!{/size}"
        $ l_question = False
        $ l_drop = True
        $ lola_face = "03_hp/22_lola/04.png"
        show screen l_head
        l "гх!"
        hide screen l_head
        pause.01
        with hpunch
        a7 "{size=+7}Мы не используем его! Никогда!{/size}"
        $ lola_face = "03_hp/22_lola/01.png"
        $ l_drop = False
        show screen l_head
        l "Потому что самый самый большой здесь папочка?"
        hide screen l_head
        a6 "Гх!"
        a6 "Тебе понравилось сниматься в \"Тренер Принцессы\"?"
        $ l_hearts = True
        $ lola_face = "03_hp/22_lola/01.png"
        show screen l_head
        l "Лучшее событие в моей жизни!"
        hide screen l_head
        a1 "Хочешь попасть в \"золотое издание\"?"
        $ l_hearts = False
        $ lola_face = "03_hp/22_lola/05.png"
        show screen l_head
        l "!!!"
        $ lola_face = "03_hp/22_lola/06.png"
        show screen l_head
        l "Дамы и гопода, добро пожаловать в обучающий режим \"Тренера Гермионы\"."
        hide screen l_head
        a1 "Умница, девочка."
        $ l_drop = True
    else: # EVENT_02
        $ lx = 490
        $ ly = 190
        $ lola_body = "03_hp/22_lola/body_01.png"
        $ lola_face = "03_hp/22_lola/05.png"
        show screen l_head
        l "Хм...?"
        l "Ты хочешь прослушать обучение снова?"
        $ lola_face = "03_hp/22_lola/09.png"
        l "Хм...."
        $ lola_face = "03_hp/22_lola/11.png"
        l "You are not very bright, are you?"
        $ lola_face = "03_hp/22_lola/10.png"
        l "Хм..."
        $ l_things = True
        $ lola_face = "03_hp/22_lola/08.png"
        l "*Хихикает!*"
        $ l_things = False
        $ lola_face = "03_hp/22_lola/01.png"
        l "Ты хочешь, чтобы я учила тебя топлесс?"
        hide screen l_head
        $ d_flag_01 = False
        menu:
            "\"Еще бы!\"":
                $ lola_face = "03_hp/22_lola/01.png"
                show screen l_head
                
                $ d_flag_01 = True
                l "Океюшки!"
                hide screen l_head
                pause.1
                show screen blkfade 
                with d3
                $ lola_body = "03_hp/22_lola/body_02.png"
                $ l_blush = True
                pause.5
                hide screen blkfade
                with d7
                
                
            "\"Не интересно.\"":
                $ lola_face = "03_hp/22_lola/12.png"
                show screen l_head
                l "Ты скучный..."
                $ lola_face = "03_hp/22_lola/09.png"
                l "Ладно, пофиг..."

                   
    ### THE TUTORIAL ###
    play music "music/Under-the-Radar by PhobyAk.mp3" fadein 1 fadeout 1 
    $ lola_face = "03_hp/22_lola/06.png"
    show screen l_head
    l "Вот краткий перечень вещей, которые стоит помнить..."
    with hpunch
    $ end_u_1_pic =  "03_hp/22_lola/tut_02.png" #<---- SCREEN
    $ renpy.play('sounds/boing02.mp3')   

    l "Гермиона захочет продавать сексуальные услуги в обмен на очки факультета, когда Гриффиндор отстает."
    
    with hpunch
    $ end_u_1_pic =  "03_hp/22_lola/tut_01.png" #<---- SCREEN
    $ renpy.play('sounds/boing02.mp3')   
    l "Дружба с профессором Снейпом  увеличит количество очков, зарабатываемых Слизереном."
    with hpunch
    $ end_u_1_pic =  "03_hp/22_lola/tut_03.png" #<---- SCREEN
    $ renpy.play('sounds/boing02.mp3') 
    if d_flag_01: # TOPLESS.
        $ lola_face = "03_hp/22_lola/07.png"
    l "Чтение образовательных книг позволит тебе зарабатыва, но это по желанию."

    with hpunch
    $ end_u_1_pic =  "03_hp/22_lola/tut_04.png" #<---- SCREEN
    $ renpy.play('sounds/boing02.mp3') 
    l "Покупка одной и той же сексуальной услуги может привести к разным последствиям, в зависимости от того, как далеко Гермиона зашла в своих тренировках."
    $ lola_face = "03_hp/22_lola/06.png"

    with hpunch
    $ end_u_1_pic =  "03_hp/22_lola/tut_07.png" #<---- SCREEN
    l "Все услуги разделены на две группы: \"приватные услуги\" и\"публичные услуги\"."
    l "Приватные услуги оказываются в кабинете и не сильно влияют на репутацию Гермионы."
    l "Публичные услуги оказываются во время уроков за пределами экрана."
    l "Каждая публичная услуга, не считая последней, имеет девять концовок."
    l "Кстати, несмотря на то, что покупка приватных услуг - необходима для тренировки Гермионы, публичные услуги не обязательны."

    with hpunch
    $ end_u_1_pic =  "03_hp/22_lola/tut_05.png" #<---- SCREEN

    $ renpy.play('sounds/boing02.mp3') 
    l "Если обрщаться с ней плохо, то настроение Гермиона может обидеться и стать очень неподатливой..."
    l "Она остынет со временем, но ты можешь ускорить процесс, если купишб ей что-нибудь..."
    
    with hpunch
    $ end_u_1_pic =  "03_hp/22_lola/tut_06.png" #<---- SCREEN
    $ renpy.play('sounds/boing02.mp3') 
    l "Здесь нет временных ограничений. Так что можешь играть в нее столько дней, сколько захочешь."
 
    
    
    
    $ end_u_1_pic =  "03_hp/22_lola/tut_00.png" #<---- SCREEN
    $ l_drop = False
    
    if not persistent.tut: # FIRST TIME TUTORIAL. Turns TRUE after tutorial happened once already. EVENT_01
        $ persistent.tut = True #Turns TRUE after tutorial happened once already.
        hide screen l_head
        a1 "Ладно, этого хватит..."
        $ l_question = True
        $ lola_face = "03_hp/22_lola/05.png"
        show screen l_head
        l "Как я справилась?"
        hide screen l_head
        a1 "Ты хорошо поработала. Хорошая девочка."
        $ l_question = False
        $ l_things = True
        $ lola_face = "03_hp/22_lola/08.png"
        show screen l_head
        l "Ме-хе-хе. Лола хорошая девочка!"
        $ l_things = False
        $ lola_face = "03_hp/22_lola/01.png"
        show screen l_head
        l "А что я получу?"
        hide screen l_head
        a1 "А что ты хочешь?"
        $ lola_face = "03_hp/22_lola/10.png"
        show screen l_head
        l "Хм..."
        $ l_exclamation = True
        $ lola_face = "03_hp/22_lola/01.png"
        l "Мы можем сделать сцену изнасилования со мной в \"Золотом издании\"?"
        hide screen l_head
        a6 "Не испытывай мое терпения, девочка."
        $ l_exclamation = False
        $ l_drop = True
        $ lola_face = "03_hp/22_lola/04.png"
        show screen l_head
        l "Извини, папочка."
        $ l_drop = False
        hide screen l_head
        a5 "............"

    else: ### NOT FIRST TUTORIAL. EVENT_02
        if d_flag_01: #TOPLESS.
            hide screen l_head
            stop music fadeout 1.0
            a1 "Что здесь происходит?"
            $ lola_face = "03_hp/22_lola/14.png"
            $ l_drop = True
            show screen l_head
            l "Упс!"
            hide screen l_head
            a1 "Что я говорил тебе о раздевании перед незнакомцами?"
            $ lola_face = "03_hp/22_lola/04.png"
            show screen l_head
            l "Это важная часть взросления?"
            hide screen l_head
            a6 "Нет!"
            $ l_drop = False
            $ l_tears = True
            $ lola_body = "03_hp/22_lola/body_01.png"
            $ lola_face = "03_hp/22_lola/04.png"
            show screen l_head
            l "Папочка, мне так жаль!"
            l "Этот случайный чувак из интернета заставил меня, я клянусь!"
            hide screen l_head
            a1 "Обучение закончено."
            $ l_blush = False
            $ l_tears = False
            $ lola_face = "03_hp/22_lola/15.png"
            show screen l_head
            l "Хе-хе! Ты попался!"
        else:
            $ lola_face = "03_hp/22_lola/09.png"
            l "And that's that..."
            $ lola_face = "03_hp/22_lola/13.png"
            l "Did you get it this time?"
            
        
return

### ABOUT GAME ####
label abouttrainer:
    $ end_u_1_pic =  "title3.jpg" #<---- SCREEN
    show screen end_u_1                                             #<---- SCREEN
    play music "music/GrapeSodaIsFuckingRawbyjrayteam6.mp3" fadein 1 fadeout 1 
    
    a1 "Хм... Посмотрим..."
    a1 "Я начал работу над \"Тренером Гермионы\" сразу после релиза \"Тренера Принцессы\"."
    a1 "У меня была идея создать маленькую милую игру, на разработку которой уйдет не больше, чем пара месяцев."
    a1 "Как мы все знаем, это заняло у меня больше полугода..." 
    a1 "И несмотря на бесконечные компромиссы, мне пришлось просто-напросто закончить разработку, чтобы эта чертовщина не убила у меня еще больше времени."
    a1 "Порой работать над игрой было весело..."
    a1 "Но также были и трудности..."
    a1 "Иногда мне приходилось бороться с некотрыми идеями и игровыми механиками, которые не хотели работать правильно..."
    a1 "Также работа над этой игрой рассказала мне много о моих способностях как разработчик игр и моих слабостях."
    a2 "Мне почти кажется, что я должен получить медаль или грамоту за это."
    a1 "Ладно, я сваливаю в мой следующий проект. {size=-4}(\"Тренер Принцессы Золотое Издание\"){/size}"
    a1 "Спасибо за поддержку, парни. И я надеюсь, что эта игра сделала ваши будни хоть чуточку светлее."
    a2 "До следующего раза..."

    return

### F.A.Q. ###
label faq:
    $ end_u_1_pic =  "title3.jpg" #<---- SCREEN
    show screen end_u_1 
    with flashbb#<---- SCREEN
    play music "music/(Orchestral) Playful Tension by Shadow16nh.mp3" fadein 1 fadeout 1 
    
    a1 "Привет. Меня зовут Акабур. Я создатель игры и я здесь, чтобы ответить на твои вопросы." 
label faq2:    
    menu:
        "Как я могу поддержать тебя?":
            a1 "Ну, есть несколько способов..."  
            a1 "Самый простой способов написать мне (akaburfake2@yahoo.com) и дать мне знать, что тебе понравилась игра."
            a1 "Также ты можешь поддержать меня лично на {a=http://www.patreon.com/akabur}www.patreon.com/akabur{/a}"
            a1 "Еще один способ поддержать меня это перейти по этой ссылке: {a=http://akabur.hentaiunited.com}akabur.hentaiunited.com{/a}."
            a1 "У таких независимых художников как я каждый бакс на счету..."
            a6 "Серьезно. Из-за моего стиля жизни гребанный банк все еще не может выдать мне кредитную карту..."
#            label payments:
#            menu:
#                "-WebMoney info-":
#                    a1 "My RUBLES WebMoney purse: R133931000745"
#                    a1 "My USD WebMoney purse: Z319925489258"
#                    a1 "My EURO WebMoney purse: E800599783938"
#                    jump payments
#                "-YandexMoney Info-":
#                    a1 "My Yandex Purse Number: 41001849167270"
#                    jump payments
#                "-PayPal Info-":
#                    a1 "Contact me via email and i will give you my PayPal."
#                    jump payments
#                "-Credit Card-":
#                    a1 "Here: {a=http://www.test.akabur.com/donate}how to donate with Credit Card.{/a}"
#                    jump payments
#                "-Cancel-":
#                    jump faq2
            jump faq2
            
        "Как оставаться в курсе?":
            a1 "Ну, перейти по этой ссылке: {a=http://akabur.hentaiunited.com}akabur.hentaiunited.com{/a} и подписаться. Или посетить мой сайт: {a=http://akabur.com}akabur.com{/a}."
            a1 "Еще, конечно есть Patreon {a=http://www.patreon.com/akabur}www.patreon.com/akabur{/a}.\nи {a=https://twitter.com/AKABUR}мой twitter{/a}." 
            jump faq2
        "У меня есть другой вопрос.":
            a1 "Если у тебя есть вопрос, что не входит в это\"F.A.Q.\", не стесняйся и пиши: akaburfake2@yahoo.com"
            a1 "Или оставь вопрос здесь: {a=http://ask.fm/AKABUR}ask.fm/AKABUR{/a}"
            jump faq2
        "Я хочу сообщить о баге/ошибке.":
            a1 "Эта игра тестировалась много много много раз, но лучшими тестерами всегда были и остаются игроки."
            a1 "Так что, если вы встретили баг - пишите мне (akaburfake2@yahoo.com) и я исправлю проблеиу в следущей версии игры."
            jump faq2
        "Кто помог тебе создавать игру?":
            a1 "Никто не помогал мне! Я сделал все сам!"
            a1 "Я сам написал все скрипты, нарисовал все арты, и сыграл всю музыку!"
            a7 "Я! {size=+3}Я! {size=+3}Я создал все! {size=+3}me!{/size}"
            a2 "Хех..."
            a1 "Ну, по правде, я сделал большую часть работу. Но мне много помогали."
            a1 "Мой друг и коллега Dahr беспечил меня благородно (и бесплатно) разными художествами (помимо всего прочего)."
            a1 "Не бойтись кинуть парню монетки или две на {a=http://www.patreon.com/DAHR}www.patreon.com/DAHR{/a}"
            a1 "Xaljio всегда был рядом, когда у меня были проблемы с коддингом. (частенько). Посетите его страничку - {a=http://www.patreon.com/xaljio}www.patreon.com/xaljio{/a}"
            a1 "И, конечно, сообщества на patreon и hentaiunited. Парни, вы шикарны."
            a1 "Спасибо вам за моральную и финансовую поддержку разработки этой игры. Вы, ребята, делаете этот мир чуточку лучше."
            jump faq2
        "Можно взломать и перевести эту игру?":
            a1 "..."
            a1 "..."
            a5 "Нет."
            define nyor = Character('Nyarkohotep', color="#9F42AB")
            nyor "Странный вопрос, не находишь?"
            nyor "И это после того, как я полтора гребанных часа возился, чтобы перевести никому не нужные FAQ и обучалки!"
            nyor "Агрх!"
            nyor "А вообще, молодец, что заглянул."
            nyor "Минута славы."
            nyor "Перевод для вас пилили \
            {a=http://pornolab.net/forum/profile.php?mode=viewprofile&u=14141420}Ave_Fletch{/a}, \
            {a=http://pornolab.net/forum/profile.php?mode=viewprofile&u=15155170}Discordnk90{/a}, \
            {a=http://pornolab.net/forum/profile.php?mode=viewprofile&u=8041771}maniac4a{/a}, \
            {a=http://pornolab.net/forum/profile.php?mode=viewprofile&u=4472572}Rio-Violente{/a}, \
            {a=http://pornolab.net/forum/profile.php?mode=viewprofile&u=16957111}MrFrost1991{/a}, \
            {a=http://pornolab.net/forum/profile.php?mode=viewprofile&u=18304384}babaylolxz{/a}, \
            {a=http://pornolab.net/forum/profile.php?mode=viewprofile&u=15179745}qcerb1880{/a}, \
            {a=http://pornolab.net/forum/profile.php?mode=viewprofile&u=11908608}sn0rk95{/a}, \
            и любимец публики {a=http://pornolab.net/forum/profile.php?mode=viewprofile&u=16733487}Nyarkohotep{/a}."
            nyor "Извините, если кого-то забыли :3!"
            nyor "Не забывайте пользоваться салфетками, ребята, пока-пока!"
            a1 "..."
            jump faq2

        "Неважно. Выпусти меня отсюда!":
            return

    
    return