label sexy_tutoring:
    $ dates += 1
    if dates == 3:
        jump date_01
       
        
#    if dates >=3:
#        menu:
#            "Touch her thigh."
#            "Touch yourself."
#            "Touch her tits."
            
        
        
        
    "Вы обучаете Гермиону."
    jump day_start 
    
###DATE - 1#######
label date_01:
    "Вы трогаете ее ножку."
    her "Профессор? Что вы делаете?"
    her "Хорошо, я дам вам потрогать мою ногу, но только если вы пообещаете мне взамен 5 очков."
    "Вы обещаете Гермионе 5 баллов, чтобы потрогать ее бедра."
    "На сегодня репетиторство закончено."
    jump day_start 

###DATE - 2#######
label date_02:
    menu:
        "Тронуть ее ногу свой ногой.":
            if whoring < 3:
                "Гермиона вообще не обращает внимания на ваши прикосновения..."
            elif whoring >= 3 and whoring < 6:
                "Гермиона понимает, что вы делаете, но ничего не говорит."
            elif whoring >= 6:
                "Гермиона подсаживается чуть ближе к вам. Она отвечает на ваши прикосновения."
            "Обучения законечно. Гермиона уходит."
            $ whoring +=1
            jump day_start 
        "Touch her leg with your hand." if whoring >= 7:
            pass
        "{color=#858585}...(ЗАБЛОКИРОВАНО)...{/color}" if whoring <=7:
            jump locked
        "Положить ее руки на член." if whoring >= 14:
            pass
        "{color=#858585}...(ЗАБЛОКИРОВАНО)...{/color}" if whoring <=14:
            jump locked
        "Подроить." if whoring >= 21:
            pass
        "{color=#858585}...(ЗАБЛОКИРОВАНО)...{/color}" if whoring <=21:
            jump locked
        "Заставить ее дрочить вам." if whoring >= 28:
            pass
        "{color=#858585}...(ЗАБЛОКИРОВАНО)...{/color}" if whoring <=28:
            jump locked
        "Засунуть в нее свой палец." if whoring >= 35:
            pass
        "{color=#858585}...(ЗАБЛОКИРОВАНО)...{/color}" if whoring <=35:
            jump locked
        "Заставить ее сосать член." if whoring >= 42:
            pass
        "{color=#858585}...(ЗАБЛОКИРОВАНО)...{/color}" if whoring <=42:
            jump locked
        "Трахнуть ее во время чтения." if whoring >= 49:
            pass
        "{color=#858585}...(ЗАБЛОКИРОВАНО)...{/color}" if whoring <=49:
            jump locked
        "Трахнуть ее в попку." if whoring >= 56:
            pass
        "{color=#858585}...(ЗАБЛОКИРОВАНО)...{/color}" if whoring <=56:
            jump locked
        "-Отмена-":
            jump home_assignment
            
            
###LOCKED MASSAGE###
label locked:
    "Не хватает порочности."
    jump sexy_tutoring