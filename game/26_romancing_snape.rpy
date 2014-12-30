label date_with_snape_01:
    show screen bld1
    with d3
    m "Хорошо. Теперь научи меня магии с этой палочкой."
    $ s_head_xpos = 330 # x = 330,                                                                              # SNAPE
    $ s_head_ypos = 380 #Right bottom corner: y = 340. y = 380 - no hand.       # SNAPE
    $ s_sprite = "03_hp/10_snape_main/23.png"                                        # SNAPE
    show screen s_head2                                                                                                 # SNAPE
    sna "Хорошо, модно попробовать..."
    $ s_head_xpos = 330 # x = 330,                                                                              # SNAPE
    $ s_sprite = "03_hp/10_snape_main/snape_02.png"                                        # SNAPE
    show screen s_head2                                                                                                 # SNAPE
    sna2 "Или я мог бы рассказать тебе кое-что о этих \"слизеринских\" шлюхах..."
    hide screen s_head2              
    g9 "Последнее, будь добр."
    $ s_head_xpos = 330 # x = 330,                                                                              # SNAPE
    $ s_sprite = "03_hp/10_snape_main/snape_13.png"                                        # SNAPE
    show screen s_head2                                                                                                 # SNAPE
    sna "Великолепно... Слушай сюда..."
    hide screen s_head2  
    pause.1
    show screen blktone
    with d3
    ">Вы проводите вечер, обсуждая с профессором Снейпом всяческие похабные вещи об этих девках."
    $ renpy.play('sounds/win_04.mp3')   #Not loud.
    hide screen notes
    show screen notes
    ">Вы чувствуете тонкую связь между вами..."
    call sly_plus
    hide screen blktone
    hide screen bld1
    with d3

    $ snapes_support += 1 #Controls how much points is awarded to SLYTHERIN daily.
    $ snape_events += 1 #Makes sure this event will happen only once. Also triggers next event with Snape.
    
    return
    
    
label date_with_snape_02:
    show screen bld1
    with d3
    m "Чтобы добиться успеха в нашем деле..."
    m "Тебе нужно быть более щедрым с этими очками для факультета..."
    $ s_head_xpos = 330 # x = 330,                                                                              # SNAPE
    $ s_head_ypos = 380 #Right bottom corner: y = 340. y = 380 - no hand.       # SNAPE
    $ s_sprite = "03_hp/10_snape_main/snape_09.png"                                                      # SNAPE
    show screen s_head2                                                                                                 # SNAPE
    sna "Верно, конечно..."
    sna "Мисс Грейнджер требуется хороший стимул..."
    sna "Поэтому следует вывести мой факультет в лидеры..."
    $ s_sprite = "03_hp/10_snape_main/snape_06.png"                                        # SNAPE
    show screen s_head2                                                                                                 # SNAPE
    sna "Это может занять какое-то время..."
    hide screen s_head2 
    m "Занять время?"
    m "Почему бы нам просто не присудить несколько сотен очков \"Слизерину\" и покончить с этим?"
    $ s_sprite = "03_hp/10_snape_main/24.png"                                        # SNAPE
    show screen s_head2                                                                                                 # SNAPE
    sna "Нет, мы должны быть осторожны..."
    $ s_sprite = "03_hp/10_snape_main/snape_05.png"                                        # SNAPE
    show screen s_head2                                                                                                 # SNAPE
    sna2 "Награждение моего факультета большим количеством очков может привлечь лишнее внимание..."
    hide screen s_head2 
    m "Хм... Я понял твою позицию..."
    show screen blktone
    with d3
    ">Вы проводите вечер с Северусом, обдумывая заговор против Гермионы..."
    ">Узы дружбы между вами несколько укрепляются."
    call sly_plus
    hide screen blktone
    hide screen bld1
    with d3
    
    $ snapes_support += 1 #Controls how much points is awarded to SLYTHERIN daily.
    $ snape_events += 1 #Makes sure this event will happen only once. Also triggers next event with Snape.
    
    return
    
label date_with_snape_03:
    show screen bld1
    with d3
    $ s_head_xpos = 330 # x = 330,                                                                              # SNAPE
    $ s_head_ypos = 380 #Right bottom corner: y = 340. y = 380 - no hand.       # SNAPE
    $ s_sprite = "03_hp/10_snape_main/snape_01.png"                                         # SNAPE
    show screen s_head2                                                                                                 # SNAPE
    sna2 "Ты слышал уже об этом \"движении за права мужчин\"?"
    $ s_sprite = "03_hp/10_snape_main/snape_03.png"                                         # SNAPE
    show screen s_head2                                                                                                 # SNAPE
    sna2 "Эта девка сплошная неприятность..."
    sna2 "Она умна, популярная и обладает железной волей..."
    $ s_sprite = "03_hp/10_snape_main/snape_06.png"                                         # SNAPE
    show screen s_head2                                                                                                 # SNAPE
    sna2 "Иногда я начинаю сомневаться в успешности нашего плана..."
    hide screen s_head2 
    m "Тебе не следует..."
    $ s_sprite = "03_hp/10_snape_main/snape_26.png"                                         # SNAPE
    show screen s_head2                                                                                                 # SNAPE
    sna "Все потому..."
    hide screen s_head2 
    m "Это может занять время, но я {size=+5}сломаю{/size} ее."
    m "Просто доверься мне."
    $ s_sprite = "03_hp/10_snape_main/snape_26.png"                                         # SNAPE
    show screen s_head2                                                                                                 # SNAPE
    sna "Ладно..."
    $ s_sprite = "03_hp/10_snape_main/snape_06.png"                                         # SNAPE
    show screen s_head2                                                                                                 # SNAPE
    sna2 "У меня нет выбора, но я надеюсь на лучшее...?"
    hide screen s_head2 
    show screen blktone
    with d3
    ">Вы проводите вечер с профессором Снейпом, опасаясь неопределенного будущего."
    ">Теперь вы чуть больше доверяете друг другу."
    call sly_plus
    hide screen blktone
    hide screen bld1
    with d3
    
    

    $ snapes_support += 1 #Controls how many points is awarded to SLYTHERIN daily.
    $ snape_events += 1 #Makes sure this event will happen only once. Also triggers next event with Snape.
  
    return
    
label date_with_snape_04:
    show screen bld1
    with d3
    $ s_head_xpos = 330 # x = 330,                                                                              # SNAPE
    $ s_head_ypos = 380 #Right bottom corner: y = 340. y = 380 - no hand.       # SNAPE
    $ s_sprite = "03_hp/10_snape_main/24.png"                                         # SNAPE
    show screen s_head2                                                                                                 # SNAPE
    sna "Скажи мне что-нибудь, Джинн..."
    hide screen s_head2            
    m "Да?"
    $ s_sprite = "03_hp/10_snape_main/snape_25.png"                                         # SNAPE
    show screen s_head2                                                                                                 # SNAPE
    sna "Ты веришь в теорию о параллельных мирах?"
    hide screen s_head2    
    m "Ну, это очень сложно. Учитывая все обстоятельства."
    $ s_sprite = "03_hp/10_snape_main/23.png"                                         # SNAPE
    show screen s_head2                                                                                                 # SNAPE
    sna "Верно..."
    $ s_sprite = "03_hp/10_snape_main/snape_05.png"                                         # SNAPE
    show screen s_head2                                                                                                 # SNAPE
    sna2 "Ты думаешь где-то есть альтернативная версия меня?"
    hide screen s_head2    
    m "Вероятно..."
    $ s_sprite = "03_hp/10_snape_main/23.png"                                         # SNAPE
    show screen s_head2                                                                                                 # SNAPE
    sna "Хм..."
    sna "Северус Снейп - очень веселый белый маг..."
    hide screen s_head2    
    m "Конечно, почему нет?"
    $ s_sprite = "03_hp/10_snape_main/snape_03.png"                                         # SNAPE
    show screen s_head2                                                                                                 # SNAPE
    sna "Эти образы будоражат мое воображение..."
    hide screen s_head2    
    m "Что насчет альтернативной версии девченки Грейнджер?"
    $ s_sprite = "03_hp/10_snape_main/snape_02.png"                                         # SNAPE
    show screen s_head2                                                                                                 # SNAPE
    sna2 "Да! Гермиона Грейнджер - мерзкая шлюха без достоинства! Да, мне это нравится!"
    hide screen s_head2    
    m "А что если в другом мире есть такая же команда веселого Северуса и такого же причудливого меня?"
    m "И мы вместе обучаем шлюху Гермиону быть хорошим студентом и нормальной девушкой?"
    $ s_sprite = "03_hp/10_snape_main/snape_28.png"                                         # SNAPE
    show screen s_head2                                                                                                 # SNAPE
    sna "Ха-ха-ха! Это очень весело!"
    hide screen s_head2
    pause.1
    show screen blktone
    with d3
    ">Вы проводите остаток вечера обсуждая науку, метафизику и шлюх."
    ">Узы дружбы между вами с профессором Снейпом укрепляются."
    call sly_plus
    hide screen blktone
    hide screen bld1
    with d3
    
    $ snapes_support += 1 #Controls how much points is awarded to SLYTHERIN daily.
    $ snape_events += 1 #Makes sure this event will happen only once. Also triggers next event with Snape.
    
    return

    
    
label date_with_snape_05:
    show screen bld1
    with d3
    $ s_head_xpos = 330 # x = 330,                                                                              # SNAPE
    $ s_head_ypos = 380 #Right bottom corner: y = 340. y = 380 - no hand.       # SNAPE
    $ s_sprite = "03_hp/10_snape_main/snape_05.png"                                         # SNAPE
    show screen s_head2                                                                                                 # SNAPE
    sna2 "И так...какой план на этот вечер?"
    sna2 "Эта девка досаждает тебе?"
    hide screen s_head2    
    menu:
        "\"Да уж. Она упряма.\"":
            $ s_sprite = "03_hp/10_snape_main/snape_06.png"                                         # SNAPE
            show screen s_head2                                                                                                 # SNAPE
            sna "Не удивительно..."
        "\"Нет, не очень...\"":
            $ s_sprite = "03_hp/10_snape_main/snape_05.png"                                         # SNAPE
            show screen s_head2                                                                                                 # SNAPE
            sna "Серьезно?"
            sna "Интересно..."
    $ s_sprite = "03_hp/10_snape_main/snape_01.png"                                         # SNAPE
    show screen s_head2                                                                                                 # SNAPE
    sna2 "Но ты уверен, что в состаянии сломить ее волю??"
    hide screen s_head2    
    m "О, абсолютно."
    m "Хотя это и займет некоторое время..."
    $ s_sprite = "03_hp/10_snape_main/snape_06.png"                                         # SNAPE
    show screen s_head2                                                                                                 # SNAPE
    sna "Ну, время у нас есть..."
    $ s_sprite = "03_hp/10_snape_main/snape_05.png"                                         # SNAPE
    show screen s_head2                                                                                                 # SNAPE
    sna2 "Я имею в виду, ты все еще бессилен, так?"
    hide screen s_head2    
    m "Да, не то слово..."
    $ s_sprite = "03_hp/10_snape_main/snape_02.png"                                         # SNAPE
    show screen s_head2                                                                                                 # SNAPE
    sna "Великолепно!"
    hide screen s_head2    
    m "......................."
    $ s_sprite = "03_hp/10_snape_main/snape_29.png"                                         # SNAPE
    show screen s_head2                                                                                                 # SNAPE
    sna2 "Я хотел сказать, это плохо {size=+5}для тебя{/size}, но просто отлично {size=+5}для меня{/size}, верно?"
    hide screen s_head2    
    m "Верно..."
    show screen blktone
    with d3
    ">Профессор Снейп, кажется, чувствует неловкую выгоду из вашего несчастья..."
    ">Узы дружбы между вами немного укрепились..."
    call sly_plus
    hide screen blktone
    hide screen bld1
    with d3
    
    $ snapes_support += 1 #Controls how much points is awarded to SLYTHERIN daily.
    $ snape_events += 1 #Makes sure this event will happen only once. Also triggers next event with Snape.
    return
    
label date_with_snape_06:
    show screen bld1
    with d3
    m "И так, расскажи мне еще о \"слизеринских\" шлюхах!"
    $ s_head_xpos = 330 # x = 330,                                                                              # SNAPE
    $ s_head_ypos = 380 #Right bottom corner: y = 340. y = 380 - no hand.       # SNAPE
    $ s_sprite = "03_hp/10_snape_main/23.png"                                         # SNAPE
    show screen s_head2                                                                                                 # SNAPE
    sna2 "Что я могу сказать? Для меня жизнь, в последнее время, просто великолепна."
    $ s_sprite = "03_hp/10_snape_main/snape_22.png"                                         # SNAPE
    show screen s_head2                                                                                                 # SNAPE
    sna2 "В последние дни у меня целый гарем из студенток - выбирай что душе угодно."
    hide screen s_head2  
    g9 "Круто!"
    $ s_sprite = "03_hp/10_snape_main/snape_02.png"                                         # SNAPE
    show screen s_head2                                                                                                 # SNAPE
    sna2 "Да. Благодаря тебе, я могу, черт возьми, делать что душе угодно!"
    sna2 "И что более важно..."
    $ s_sprite = "03_hp/10_snape_main/snape_13.png"                                         # SNAPE
    show screen s_head2                                                                                                 # SNAPE
    sna "С кем, мать его, захочу!"
    hide screen s_head2  
    m "Серьезно?"
    $ s_sprite = "03_hp/10_snape_main/snape_09.png"                                         # SNAPE
    show screen s_head2                                                                                                 # SNAPE
    sna "Ну, вроде того..."
    sna2 "На самом деле что-то вроде \"кого захочу\", почти так..."
    $ s_sprite = "03_hp/10_snape_main/snape_13.png"                                         # SNAPE
    show screen s_head2                                                                                                 # SNAPE
    sna2 "Ты не представляешь, что некоторые из девок готовы сделать за очки для факультета!"
    $ s_sprite = "03_hp/10_snape_main/snape_22.png"                                         # SNAPE
    show screen s_head2                                                                                                 # SNAPE
    sna "Или даже просто обещание о хорошей оценке..."
    hide screen s_head2  
    pause.1
    show screen blktone
    with d3
    ">Холодный темперамент профессора Снейпа улетучивается на глазах..."
    ">Ваша дружба укрепляется..."
    call sly_plus
    hide screen blktone
    hide screen bld1
    with d3
    
    
    $ snapes_support += 1 #Controls how much points is awarded to SLYTHERIN daily.
    $ snape_events += 1 #Makes sure this event will happen only once. Also triggers next event with Snape.
    return
    
    
label date_with_snape_07:
    show screen bld1
    with d3
    $ s_head_xpos = 330 # x = 330,                                                                              # SNAPE
    $ s_head_ypos = 380 #Right bottom corner: y = 340. y = 380 - no hand.       # SNAPE
    $ s_sprite = "03_hp/10_snape_main/snape_05.png"                                         # SNAPE
    show screen s_head2                                                                                                 # SNAPE
    sna2 "В твоем мире ты одно из сильнейших существ?"
    hide screen s_head2  
    m "Да, вроде того..."
    $ s_sprite = "03_hp/10_snape_main/snape_05.png"                                         # SNAPE
    show screen s_head2                                                                                                 # SNAPE
    sna2 "Тогда почему ты просто не продашь эту женщину, Жасмин?"
    hide screen s_head2  
    m "Ох... Ну..."
    m "...Она принцесса."
    $ s_sprite = "03_hp/10_snape_main/snape_05.png"                                         # SNAPE
    show screen s_head2                                                                                                 # SNAPE
    sna "И?"
    sna "Она твоя принцесса? Ты ведь даже не человек."
    sna "Ты клялся ей в своей верности?"
    hide screen s_head2  
    m "Не совсем..."
    $ s_sprite = "03_hp/10_snape_main/snape_06.png"                                         # SNAPE
    show screen s_head2                                                                                                 # SNAPE
    sna "Почему тебя тогда это волнует?"
    $ s_sprite = "03_hp/10_snape_main/snape_09.png"                                         # SNAPE
    show screen s_head2                                                                                                 # SNAPE
    sna2 "Я так понимаю, что она всего своего рода магл ..."
    hide screen s_head2  
    m "Она кто?"
    $ s_sprite = "03_hp/10_snape_main/snape_25.png"                                         # SNAPE
    show screen s_head2                                                                                                 # SNAPE
    sna "Человек... Она просто человек..."
    $ s_sprite = "03_hp/10_snape_main/snape_05.png"                                         # SNAPE
    show screen s_head2                                                                                                 # SNAPE
    sna "Так зачем ты хочешь угодить ей?"
    hide screen s_head2  
    m "Ну, это сложно..."
    $ s_sprite = "03_hp/10_snape_main/snape_05.png"                                         # SNAPE
    show screen s_head2                                                                                                 # SNAPE
    sna ".............."
    hide screen s_head2  
    m ".................."
    $ s_sprite = "03_hp/10_snape_main/snape_02.png"                                         # SNAPE
    show screen s_head2                                                                                                 # SNAPE
    sna "Она горяченькая, не так ли?"
    hide screen s_head2  
    m "Просто огонь..."
    $ s_sprite = "03_hp/10_snape_main/23.png"                                         # SNAPE
    show screen s_head2                                                                                                 # SNAPE
    sna "Тото же."
    hide screen s_head2  
    pause.1
    show screen blktone
    with d3
    ">Вы делитесь с профессором Снейпом горькими моментами полными мужской солидарности."
    ">Ваша дружба крепнет."
    call sly_plus
    hide screen blktone
    hide screen bld1
    with d3
    $ snapes_support += 1 #Controls how much points is awarded to SLYTHERIN daily.
    $ snape_events += 1 #Makes sure this event will happen only once. Also triggers next event with Snape.
    return
    
    
label date_with_snape_08:
    show screen bld1
    with d3
    $ s_head_xpos = 330 # x = 330,                                                                              # SNAPE
    $ s_head_ypos = 380 #Right bottom corner: y = 340. y = 380 - no hand.       # SNAPE
    $ s_sprite = "03_hp/10_snape_main/snape_05.png"                                         # SNAPE
    show screen s_head2                                                                                                 # SNAPE
    sna "Как ты думаешь, нам можно.."
    sna "Вернуть публичную порку?"
    hide screen s_head2  
    m "Что ты имеешь в виду?"
    $ s_sprite = "03_hp/10_snape_main/snape_06.png"                                         # SNAPE
    show screen s_head2                                                                                                 # SNAPE
    sna2 "Ну много лет назад порка была приемлимой мерой наказания для студентов."
    sna "*Вздыхает* Было время..."
    $ s_sprite = "03_hp/10_snape_main/snape_16.png"                                         # SNAPE
    show screen s_head2                                                                                                 # SNAPE
    sna "В эти дни у студентов просто отсутствует дисциплина..."
    sna2 "Мне было бы достаточно даже этого..."
    $ s_sprite = "03_hp/10_snape_main/snape_22.png"                                         # SNAPE
    show screen s_head2                                                                                                 # SNAPE
    sna "Особенно девушек..."
    hide screen s_head2  
    m "Хм... Мне это нравится..."
    m "Но это разве не привлечет к нам ненужное внимание?"
    $ s_sprite = "03_hp/10_snape_main/snape_29.png"                                         # SNAPE
    show screen s_head2                                                                                                 # SNAPE
    sna "Да. Ты как обычно прав."
    sna "Я становлюсь очень жадным..."
    $ s_sprite = "03_hp/10_snape_main/snape_28.png"                                         # SNAPE
    show screen s_head2                                                                                                 # SNAPE
    sna "Я упиваюсь властью, мой друг!"
    sna2 "И это вино совсем не влияет на мое сознание!"
    hide screen s_head2  
    pause.1
    show screen blktone
    with d3
    ">Профессор Снейп ведет себя вполне не принужденно с вами."
    ">Важа дружба укрепляется еще больше.\n>\"Слизерин\" получает довольно много очков..."
    call sly_plus
    hide screen blktone
    hide screen bld1
    with d3
    $ snapes_support += 1 #Controls how much points is awarded to SLYTHERIN daily.
    $ snape_events += 1 #Makes sure this event will happen only once. Also triggers next event with Snape.
    return


label date_with_snape_09:
    show screen bld1
    with d3
    $ s_head_xpos = 330 # x = 330,                                                                              # SNAPE
    $ s_head_ypos = 380 #Right bottom corner: y = 340. y = 380 - no hand.       # SNAPE
    $ s_sprite = "03_hp/10_snape_main/24.png"                                                     # SNAPE
    show screen s_head2                                                                                                 # SNAPE
    sna "...и так, после этого я вернусь в Россию"
    hide screen s_head2  
    g4 "В Россию?"
    $ s_sprite = "03_hp/10_snape_main/snape_01.png"                                         # SNAPE
    show screen s_head2                                                                                                 # SNAPE
    sna "Но постой, это еше хуже."
    $ s_sprite = "03_hp/10_snape_main/snape_05.png"                                         # SNAPE
    show screen s_head2                                                                                                 # SNAPE
    sna "Очевидно, сейчас я говорю по русски."
    hide screen s_head2 
    g4 "Что, что?"
    $ s_sprite = "03_hp/10_snape_main/snape_06.png"                                         # SNAPE
    show screen s_head2                                                                                                 # SNAPE
    sna2 "И я этот обычный парень, который живет в самой жопе России, полном старых, полуразрушенных зданий."
    sna2 "И я пытаюсь заработать себе на жизнь, рисуя комиксы и делая игры на \"Ren'Py\"..."
    $ s_sprite = "03_hp/10_snape_main/24.png"                                         # SNAPE
    show screen s_head2                                                                                                 # SNAPE
    sna2 "И это так странно, потому что я даже не знаю, что такое \"Ren'Py\"!"
    hide screen s_head2  
    m "Хм...и что теперь?"
    $ s_sprite = "03_hp/10_snape_main/snape_05.png"                                         # SNAPE
    show screen s_head2                                                                                                 # SNAPE
    sna2 "Мда уж...месяцами сидеть на заднице."
    sna2 "Тогда может и получится создать относительно хорошую и завершенную игру..."
    $ s_sprite = "03_hp/10_snape_main/24.png"                                         # SNAPE
    show screen s_head2                                                                                                 # SNAPE
    sna2 "В конце концов я начал делать неплохие деньги..."
    $ s_sprite = "03_hp/10_snape_main/snape_06.png"                                         # SNAPE
    show screen s_head2                                                                                                 # SNAPE
    sna2 "И потом, когда уже начал ощущать надежду на будущее..."
    $ s_sprite = "03_hp/10_snape_main/snape_04.png"                                         # SNAPE
    show screen s_head2                                                                                                 # SNAPE
    sna "Я проснулся..."
    $ s_sprite = "03_hp/10_snape_main/snape_09.png"                                         # SNAPE
    show screen s_head2                                                                                                 # SNAPE
    sna "...................."
    hide screen s_head2  
    m "......................"
    $ s_sprite = "03_hp/10_snape_main/snape_05.png"                                         # SNAPE
    show screen s_head2                                                                                                 # SNAPE
    sna "Как ты думаешь, что это означает?"
    hide screen s_head2  
    m "Похоже на еще одну вставку Акабура."
    $ s_sprite = "03_hp/10_snape_main/snape_05.png"                                         # SNAPE
    show screen s_head2                                                                                                 # SNAPE
    sna "Что?"
    hide screen s_head2  
    m "Just ignore the whole thing."
    m "Глупости, замечтался, не более."
    $ s_sprite = "03_hp/10_snape_main/snape_29.png"                                         # SNAPE
    show screen s_head2                                                                                                 # SNAPE
    sna "Как будто в кошмаре..."
    hide screen s_head2  
    pause.1
    show screen blktone
    with d3
    ">Профессор Снейп теперь больше доверяет вам..."
    ">(До определенного момента он не думал делиться с вами этими странными снами)."
    call sly_plus
    hide screen blktone
    hide screen bld1
    with d3
    
    $ snapes_support += 1 #Controls how much points is awarded to SLYTHERIN daily.
    $ snape_events += 1 #Makes sure this event will happen only once. Also triggers next event with Snape.
    return
    
    
label date_with_snape_10:
    show screen bld1
    with d3
    $ s_head_xpos = 330 # x = 330,                                                                              # SNAPE
    $ s_head_ypos = 380 #Right bottom corner: y = 340. y = 380 - no hand.       # SNAPE
    $ s_sprite = "03_hp/10_snape_main/snape_29.png"                                         # SNAPE
    show screen s_head2                                                                                                 # SNAPE
    sna "В чем смысл жизни, Джинни"
    hide screen s_head2  
    g4 "Что?"
    $ s_sprite = "03_hp/10_snape_main/snape_05.png"                                         # SNAPE
    show screen s_head2                                                                                                 # SNAPE
    sna2 "Ведь ты такое могущественное существо, вероятно ты должен знать что-то такое?"
    hide screen s_head2  
    m "Возможно..."
    $ s_sprite = "03_hp/10_snape_main/snape_06.png"                                         # SNAPE
    show screen s_head2                                                                                                 # SNAPE
    sna "Отлично. Тогда расскажи мне."
    hide screen s_head2  
    m "Хм...Ты уверен, что готов услышать это?"
    $ s_sprite = "03_hp/10_snape_main/snape_05.png"                                         # SNAPE
    show screen s_head2                                                                                                 # SNAPE
    sna "Да. Приступай, мой друг."
    hide screen s_head2  
    m "Ну, ладно..."
    $ s_sprite = "03_hp/10_snape_main/snape_01.png"                                         # SNAPE
    show screen s_head2                                                                                                 # SNAPE
    sna "................!"
    hide screen s_head2  
    m "Это пластик..."
    $ s_sprite = "03_hp/10_snape_main/snape_05.png"                                         # SNAPE
    show screen s_head2                                                                                                 # SNAPE
    sna "Извини, что?"
    hide screen s_head2  
    m "Это пластик..."
    $ s_sprite = "03_hp/10_snape_main/snape_25.png"                                         # SNAPE
    show screen s_head2                                                                                                 # SNAPE
    sna "Я не понимаю..."
    hide screen s_head2  
    m "Эта планета будет развиваться в нечто другое в течении следующих миллионов лет..."
    m "Для этого нужен особый материал, который планета не может производить сама."
    m "Поэтому она порадила новую форму жизни - людей."
    $ s_sprite = "03_hp/10_snape_main/snape_11.png"                                         # SNAPE
    show screen s_head2                                                                                                 # SNAPE
    sna ".............."
    hide screen s_head2 
    m "Ты хотел знать цель своего существования?"
    m "Просто для производства пластика. Вот так просто."
    $ s_sprite = "03_hp/10_snape_main/snape_30.png"                                         # SNAPE
    show screen s_head2                                                                                                 # SNAPE
    sna "Да ты, блять, издеваешься?!"
    $ s_sprite = "03_hp/10_snape_main/snape_26.png"                                         # SNAPE
    show screen s_head2                                                                                                 # SNAPE
    sna "Нет, нет... Этого не может быть..."
    hide screen s_head2  
    g9 "Хе-хе..."
    $ s_sprite = "03_hp/10_snape_main/snape_25.png"                                         # SNAPE
    show screen s_head2                                                                                                 # SNAPE
    sna "Ты подколол меня?"
    hide screen s_head2  
    g9 "Видел бы ты свое лицо."
    $ s_sprite = "03_hp/10_snape_main/snape_15.png"                                         # SNAPE
    show screen s_head2                                                                                                 # SNAPE
    sna2 "Ты реально подколо меня, чертов нечеловеческий ублюдок!"
    hide screen s_head2  
    g9 "Я знаю! Было очень трудно устоять..."
    show screen blktone
    with d3
    ">вы проводите вечер ловко избегая подобные вопросы."
    ">Несмотря на ваши подколы, дружба между вами все таки крепнет."
    call sly_plus
    hide screen blktone
    hide screen bld1
    with d3

    $ snapes_support += 1 #Controls how much points is awarded to SLYTHERIN daily.
    $ snape_events += 1 #Makes sure this event will happen only once. Also triggers next event with Snape.
    return

label date_with_snape_11:
    show screen bld1
    with d3
    $ s_head_xpos = 330 # x = 330,                                                                              # SNAPE
    $ s_head_ypos = 380 #Right bottom corner: y = 340. y = 380 - no hand.       # SNAPE
    $ s_sprite = "03_hp/10_snape_main/snape_05.png"                                         # SNAPE
    show screen s_head2                                                                                                 # SNAPE
    sna2 "И так... Возвращаясь к вашему миру, у вас есть страна под названием Англия?"
    hide screen s_head2  
    m "Мы привыкли..."
    $ s_sprite = "03_hp/10_snape_main/snape_26.png"                                         # SNAPE
    show screen s_head2                                                                                                 # SNAPE
    sna "Что происходит?"
    hide screen s_head2  
    m "\"Великая катастрофа\"..."
    m "Она выжигает большую часть населения в течении нескольких часов..."
    $ s_sprite = "03_hp/10_snape_main/snape_26.png"                                         # SNAPE
    show screen s_head2                                                                                                 # SNAPE
    sna "................"
    hide screen s_head2  
    m "Превращает 80 процентов поверхности земли в горячую пустыню..."
    m "А остальные двадцать процентов в ледяную пустыню..."
    m "............."
    $ s_sprite = "03_hp/10_snape_main/snape_26.png"                                         # SNAPE
    show screen s_head2                                                                                                 # SNAPE
    sna "Это..."
    $ s_sprite = "03_hp/10_snape_main/snape_06.png"                                         # SNAPE
    show screen s_head2                                                                                                 # SNAPE
    sna "Ужасно..."
    $ s_sprite = "03_hp/10_snape_main/snape_25.png"                                         # SNAPE
    show screen s_head2                                                                                                 # SNAPE
    sna2 "Вы уверены, что хотите вернуться туда?"
    hide screen s_head2  
    m "Конечно."
    m "Там  все немного варварское...но это мой дом."
    show screen blktone 
    with d3
    ">Вы с профессором Снейпом переходите на следующий уровень дружбы..."
    ">Дружба между вами очень крепка."
    call sly_plus
    hide screen blktone
    hide screen bld1
    with d3
    
    $ snapes_support += 1 #Controls how much points is awarded to SLYTHERIN daily.
    $ snape_events += 1 #Makes sure this event will happen only once. Also triggers next event with Snape.
    return
    
label date_with_snape_12:
    show screen bld1
    with d3
    $ s_head_xpos = 330 # x = 330,                                                                              # SNAPE
    $ s_head_ypos = 380 #Right bottom corner: y = 340. y = 380 - no hand.       # SNAPE
    $ s_sprite = "03_hp/10_snape_main/snape_09.png"                                         # SNAPE
    show screen s_head2                                                                                                 # SNAPE
    sna2 "Я думал о том, что вы сказали на днях..."
    sna2 "О том, что ваш мир это огромная пустыня..."
    hide screen s_head2
    m "Да?"
    $ s_sprite = "03_hp/10_snape_main/snape_06.png"                                         # SNAPE
    show screen s_head2                                                                                                 # SNAPE
    sna "Вы думаете Альбус там в порядке?"
    hide screen s_head2
    m "Ох, конечно!"
    m "Я ведь буквально заменил его на посту..."
    m "И конечно же он заменил меня там, в Аграбе."
    $ s_sprite = "03_hp/10_snape_main/snape_05.png"                                         # SNAPE
    show screen s_head2                                                                                                 # SNAPE
    sna "Аграба?"
    hide screen s_head2
    m "Да... Очень большой город."
    m "Один из, которые появились после катастрофы."
    m "Вероятно, самый большой..."
    m "Сердце человеческой цивилизации, если вам угодно."
    $ s_sprite = "03_hp/10_snape_main/23.png"                                         # SNAPE
    show screen s_head2                                                                                                 # SNAPE
    sna "Это успокаивает..."
    hide screen s_head2
    m "Конечно..."
    m "Хотя, если ваш друг Альбус появится там же, откуда я телепортировался, читая заклинание..."
    m "Я полагаю, принцесса могла отрубить ему голову..."
    $ s_sprite = "03_hp/10_snape_main/snape_01.png"                                         # SNAPE
    show screen s_head2                                                                                                 # SNAPE
    sna "ЧТО?!"
    hide screen s_head2
    m "Но это очень маловероятно..."
    m "Около пяти процентов...может быть десять...максимум двадцать."
    $ s_sprite = "03_hp/10_snape_main/snape_03.png"                                         # SNAPE
    show screen s_head2                                                                                                 # SNAPE
    sna "......................................................."
    hide screen s_head2
    pause.1
    show screen blktone
    with d3
    ">Профессор Снейп благодарен вам (что-то вроде) за опасения по поводу Альбуса..."
    ">Ваша дружба крепнет..."
    call sly_plus
    hide screen blktone
    hide screen bld1
    with d3

    $ snapes_support += 1 #Controls how much points is awarded to SLYTHERIN daily.
    $ snape_events += 1 #Makes sure this event will happen only once. Also triggers next event with Snape.
    return
    
label date_with_snape_13:
    show screen bld1
    with d3
    $ s_head_xpos = 330 # x = 330,                                                                              # SNAPE
    $ s_head_ypos = 380 #Right bottom corner: y = 340. y = 380 - no hand.       # SNAPE
    $ s_sprite = "03_hp/10_snape_main/snape_01.png"                                         # SNAPE
    show screen s_head2                                                                                                 # SNAPE
    sna "Знаешь что?"
    hide screen s_head2
    m "Что?"
    $ s_sprite = "03_hp/10_snape_main/snape_01.png"                                         # SNAPE
    show screen s_head2                                                                                                 # SNAPE
    sna "Впервые за долго время..."
    $ s_sprite = "03_hp/10_snape_main/snape_03.png"                                         # SNAPE
    show screen s_head2                                                                                                 # SNAPE
    sna "Я думаю..."
    $ s_sprite = "03_hp/10_snape_main/snape_25.png"                                         # SNAPE
    show screen s_head2                                                                                                 # SNAPE
    sna2 "Я на самом деле доволен ходом своей жизни." # 0_0
    $ s_sprite = "03_hp/10_snape_main/snape_26.png"                                         # SNAPE
    show screen s_head2                                                                                                 # SNAPE
    sna "И это беспокоит..."
    hide screen s_head2
    m "Ты уверен, что это не эйфория после всего секса, который у тебя был?"
    $ s_sprite = "03_hp/10_snape_main/snape_22.png"                                         # SNAPE
    show screen s_head2                                                                                                 # SNAPE
    sna "Может быть."
    $ s_sprite = "03_hp/10_snape_main/snape_09.png"                                         # SNAPE
    show screen s_head2                                                                                                 # SNAPE
    sna2 "Тем не менее, ты можешь заниматься только с одной девочкой..."
    $ s_sprite = "03_hp/10_snape_main/24.png"                                         # SNAPE
    show screen s_head2                                                                                                 # SNAPE
    sna "Но она очень меня беспокоит..."
    sna "И даже эта школа..."
    hide screen s_head2
    m "Иначе говоря, ты все менее задумчив и все меньше винишь себя."
    $ s_sprite = "03_hp/10_snape_main/23.png"                                         # SNAPE
    show screen s_head2                                                                                                 # SNAPE
    sna "Что-то вроде того..."
    $ s_sprite = "03_hp/10_snape_main/snape_28.png"                                         # SNAPE
    show screen s_head2                                                                                                 # SNAPE
    sna "Я растерял свою темную сторону, чувак." # :)
    hide screen s_head2
    pause.1
    show screen blktone
    with d3
    ">Профессор Снейп действительно стал немного веселее в последнее время..."
    ">Даже выглядит моложе, чем при вашей первой встрече..."
    ">Чувство благосклонности профессора Снейпа  укрепляет узы вашей дружбы."
    call sly_plus
    hide screen blktone
    hide screen bld1
    with d3

    $ snapes_support += 1 #Controls how much points is awarded to SLYTHERIN daily.
    $ snape_events += 1 #Makes sure this event will happen only once. Also triggers next event with Snape.
    return
    
label date_with_snape_14:
    $ s_head_xpos = 330 # x = 330,                                                                              # SNAPE
    $ s_head_ypos = 380 #Right bottom corner: y = 340. y = 380 - no hand.       # SNAPE
    $ s_sprite = "03_hp/10_snape_main/snape_02.png"                                         # SNAPE
    show screen s_head2                                                                                                 # SNAPE
    sna2 "...и тут она сказала: \"Сэр, не могли бы вы немного придушить меня!\"."
    $ s_sprite = "03_hp/10_snape_main/snape_13.png"                                         # SNAPE
    show screen s_head2                                                                                                 # SNAPE
    sna "И я был счастлив сделать это!"
    $ s_sprite = "03_hp/10_snape_main/snape_19.png"                                         # SNAPE
    show screen s_head2                                                                                                 # SNAPE
    sna2 "Значит, душу я эту суку, в то время как мой член скользит в ее узкой киске, ага?"
    sna2 "И тут она настолько сильно закатила глаза, что я даже не видел ее зрачков!"
    sna2 "Ее миленькое личико наливается светло фиолетовым оттенком и она едва дышит."
    $ s_sprite = "03_hp/10_snape_main/snape_14.png"                                         # SNAPE
    show screen s_head2                                                                                                 # SNAPE
    sna2 "И тут я думаю, что стоит ослабить хватку..."
    $ s_sprite = "03_hp/10_snape_main/snape_21.png"                                         # SNAPE
    show screen s_head2                                                                                                 # SNAPE
    sna "И вот, эта сука начинает кончать!"
    hide screen s_head2
    m "Мило! И тут ты проснулся?"
    $ s_sprite = "03_hp/10_snape_main/snape_05.png"                                         # SNAPE
    show screen s_head2                                                                                                 # SNAPE
    sna "Что? Это произошло на самом деле."
    $ s_sprite = "03_hp/10_snape_main/snape_13.png"                                         # SNAPE
    show screen s_head2                                                                                                 # SNAPE
    sna "Я наконец-то добил эту ведьму из \"Слизерина\"."
    hide screen s_head2
    g9 "Круто!"
    $ s_sprite = "03_hp/10_snape_main/snape_13.png"                                         # SNAPE
    show screen s_head2                                                                                                 # SNAPE
    sna "Я знаю."
    $ s_sprite = "03_hp/10_snape_main/snape_25.png"                                         # SNAPE
    show screen s_head2                                                                                                 # SNAPE
    sna "Она довольно мило извивалась..."
    $ s_sprite = "03_hp/10_snape_main/snape_26.png"                                         # SNAPE
    show screen s_head2                                                                                                 # SNAPE
    sna "И я хочу сказать, это было действительно круто."
    hide screen s_head2
    g9 "Что за девка!"
    $ s_sprite = "03_hp/10_snape_main/snape_22.png"                                         # SNAPE
    show screen s_head2                                                                                                 # SNAPE
    sna "Именно!"
    hide screen s_head2
    pause.1
    show screen blktone
    with d3
    ">Вы находите ваши вкусы к женщинам в чем-то похожими."
    ">Ваша дружба еще никогда не была настолько сильной."
    call sly_plus
    hide screen blktone
    hide screen bld1
    with d3

    $ snapes_support += 1 #Controls how much points is awarded to SLYTHERIN daily.
    $ snape_events += 1 #Makes sure this event will happen only once. Also triggers next event with Snape.
    return
    
label date_with_snape_15:
    $ s_head_xpos = 330 # x = 330,                                                                              # SNAPE
    $ s_head_ypos = 380 #Right bottom corner: y = 340. y = 380 - no hand.       # SNAPE
    $ s_sprite = "03_hp/10_snape_main/snape_05.png"                                         # SNAPE
    show screen s_head2                                                                                                 # SNAPE
    sna "Это было относительно недавно..."
    hide screen s_head2
    m "Что ты имешь в виду?"
    $ s_sprite = "03_hp/10_snape_main/24.png"                                         # SNAPE
    show screen s_head2                                                                                                 # SNAPE
    sna "Заклинание, которое привело меня сюда..."
    sna "Ты сказал, что оно рассеится со временем..."
    $ s_sprite = "03_hp/10_snape_main/snape_05.png"                                         # SNAPE
    show screen s_head2                                                                                                 # SNAPE
    sna "Есть какая-то разница?"
    hide screen s_head2
    m "Нет...не совсем..."
    m "Может быть нужно больше времени?"
    $ s_sprite = "03_hp/10_snape_main/snape_01.png"                                         # SNAPE
    show screen s_head2                                                                                                 # SNAPE
    sna "Возможно..."
    sna "Или что-то вроде того..."
    hide screen s_head2
    m "Например?"
    $ s_sprite = "03_hp/10_snape_main/snape_09.png"                                         # SNAPE
    show screen s_head2                                                                                                 # SNAPE
    sna "Даже не знаю..."
    sna "Но, мне стоит еще подумать..."
    $ s_sprite = "03_hp/10_snape_main/24.png"                                         # SNAPE
    show screen s_head2                                                                                                 # SNAPE
    sna "Да и еще кое-что..."
    hide screen s_head2
    m "Хм...?"
    $ s_sprite = "03_hp/10_snape_main/24.png"                                         # SNAPE
    show screen s_head2                                                                                                 # SNAPE
    sna "В это время года обычно я очень занят делами..."
    sna2 "Особенно сейчас, когда мне приходится прикрывать отстутствие Альбуса."
    hide screen s_head2
    m "..................."
    $ s_sprite = "03_hp/10_snape_main/snape_06.png"                                         # SNAPE
    show screen s_head2                                                                                                 # SNAPE
    sna2 "Я не уверен, что смогу проводить свои вечера вот таким образом..."
    hide screen s_head2
    m "Действительно?"
    $ s_sprite = "03_hp/10_snape_main/snape_06.png"                                         # SNAPE
    show screen s_head2                                                                                                 # SNAPE
    sna "Да..."
    sna2 "Будут небольшие разговоры, время от времени, но на это все."
    hide screen s_head2
    m "Понятно..."
    m "Мне придется как-то иначе проводить свои вечера..."
    $ s_sprite = "03_hp/10_snape_main/snape_02.png"                                         # SNAPE
    show screen s_head2                                                                                                 # SNAPE
    sna "Я уверен, что мисс Грейнджер будет рада мне помочь."
    hide screen s_head2
    m "Да, до тех пор пока \"Злизерин\" лидирует."
    $ s_sprite = "03_hp/10_snape_main/snape_05.png"                                         # SNAPE
    show screen s_head2                                                                                                 # SNAPE
    sna "Серьезно? Ее до сих пор это волнует?"
    hide screen s_head2
    m "Очень."
    $ s_sprite = "03_hp/10_snape_main/23.png"                                         # SNAPE
    show screen s_head2                                                                                                 # SNAPE
    sna2 "Ну, значит я буду лично контролировать распределение очков, в частности для \"Слизерина\"."
    hide screen s_head2
    pause.1
    show screen blktone
    with d3
    ">Уровень вашей дружбы с прфессором Снейпом достиг максимума."
    ">Поздравляем. Если бы это был симулятор знакомств, то вы получили бы от Северуса Снейпа \"что-нибудь\"."
    ">\"Слизерину\" начисленно огромное количество очков.\"Слизерин\" получил максимальное количество очков."
    call sly_plus
    hide screen blktone
    hide screen bld1
    with d3

    $ snapes_support += 1 #Controls how much points is awarded to SLYTHERIN daily.
    $ snape_events += 1 #Makes sure this event will happen only once. Also triggers next event with Snape.
    
    $ sfmax = True # Turns TRUE when friendship with Snape been maxed out.
    return


    
    
    
    
    
    
    
    
    
    
    
    
#    show screen bld1
#    with d3
#    $ renpy.play('sounds/win_04.mp3')   #Not loud.
#    hide screen notes
#    show screen notes
#    ">You spend the evening by hanging out with Professor Snape.\n>Your relationship with him has improved."
#    $ snape_friendship +=1
#    hide screen bld1
#    with d3

#    return
    
    
    
    
    
    
    
label sly_plus:
    $ renpy.play('sounds/win_04.mp3')   #Not loud.
    hide screen notes
    show screen notes
    ">\"Слизерин\" получает несколько очков..."
    return