label day_01:
    "*Тук-тук-тук!*"
    her "Здравствуйте, профессор. Вы хотели видеть меня?"
    m "Уходи!"
    jump day_main_menu
    
    
label day_02_2:    
    her "Сегодня профессор Снейп поставил мне плохую оценку!" # Professor Snape gave me a bad grade for no good reason today
    menu:
        "Это не проблема.":
            $ teachers_pet +=1
            
        "Я поговорю с ним.":
            $ genies_slut = 0
            her "Спасибо!"
            
        "Ты должна проявлять больше уважения к учителям!":
            pass
            
label day_07:
    her "Я немного волнуюсь по поводу сегодняшнего экзамена."
    m "Не волнуйся, все будет в порядке!"
    "Гермиона уходит."
    jump day_main_menu
    
label day_07_02:
    if knowledge >= 5:
        $ test_aced = True
    elif knowledge >= 3:
        $ test_passed = True
    else:
        $ test_failed = True
    her "Я удивляюсь, как я сдала тест..."
    jump home_assignment #Moment after all cutscenes, before you sent Hermione home.
    
label day_09:
    her "Сегодня я узнаю результаты тестов. Я очень волнуюсь!"
    "Гермиона уходит."
    jump day_main_menu
    
label day_09_02:
    if test_aced:
        her "Я получила \"отлично\" за тест!!!"
    elif test_passed:
        her "Ну, я не провалила..."
    elif test_failed:
        her "Я провалила тест! Это ужасно!"
    $ test_aced = False
    $ test_passed = False
    $ test_failed = False
    jump home_assignment
