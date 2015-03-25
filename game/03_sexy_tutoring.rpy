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
    "Вы обещаете Гермионе 5 баллов за то, чтобы потрогать ее бедра."
    "На сегодня репетиторство закончено."
    jump day_start 

###DATE - 2#######
label date_02:
    menu:
        "Дотронуться своей ногой до ее ноги.":
            if hermi.whoring < 3:
                "Гермиона не обратила внимания на ваши прикосновения..."
            elif hermi.whoring >= 3 and hermi.whoring < 6:
                "Гермиона понимает, что вы делаете, но ничего не говорит."
            elif hermi.whoring >= 6:
                "Гермиона подсаживается чуть ближе к вам. Она отвечает на ваши прикосновения."
            "Обучения законечно. Гермиона уходит."
            $ hermi.whoring +=1
            jump day_start 
        "Коснуться ее ноги рукой." if hermi.whoring >= 7:
            pass
        "{color=#858585}...(ЗАБЛОКИРОВАНО)...{/color}" if hermi.whoring <=7:
            jump locked
        "Положить ее руки на член." if hermi.whoring >= 14:
            pass
        "{color=#858585}...(ЗАБЛОКИРОВАНО)...{/color}" if hermi.whoring <=14:
            jump locked
        "Подрочить." if hermi.whoring >= 21:
            pass
        "{color=#858585}...(ЗАБЛОКИРОВАНО)...{/color}" if hermi.whoring <=21:
            jump locked
        "Заставить ее дрочить вам." if hermi.whoring >= 28:
            pass
        "{color=#858585}...(ЗАБЛОКИРОВАНО)...{/color}" if hermi.whoring <=28:
            jump locked
        "Засунуть в нее свой палец." if hermi.whoring >= 35:
            pass
        "{color=#858585}...(ЗАБЛОКИРОВАНО)...{/color}" if hermi.whoring <=35:
            jump locked
        "Заставить ее сосать член." if hermi.whoring >= 42:
            pass
        "{color=#858585}...(ЗАБЛОКИРОВАНО)...{/color}" if hermi.whoring <=42:
            jump locked
        "Трахнуть ее во время чтения." if hermi.whoring >= 49:
            pass
        "{color=#858585}...(ЗАБЛОКИРОВАНО)...{/color}" if hermi.whoring <=49:
            jump locked
        "Трахнуть ее в попку." if hermi.whoring >= 56:
            pass
        "{color=#858585}...(ЗАБЛОКИРОВАНО)...{/color}" if hermi.whoring <=56:
            jump locked
        "- Отмена -":
            jump home_assignment
            
            
###LOCKED MASSAGE###
label locked:
    "Не хватает распутства."
    jump sexy_tutoring
