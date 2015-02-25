label door:

    menu:
        "- Исследовать дверь -" if not door_examined:
            $ door_examined = True
            hide screen genie
            $ tt_xpos=550
            $ tt_ypos=110
            show screen genie_stands
            show screen chair_02 #Empty chair near the desk.
            show screen desk
            with Dissolve(0.5)
            m "Выглядит надежно..."
            m "Интересно, что за ней."
            label examining_the_door:
            menu:
                "- Постучать в дверь -":
                    show screen blktone8
                    with d3
                    $ renpy.play('sounds/knocking.mp3')
                    "*Тук-тук-тук*"
                    "..................."
                    hide screen blktone8
                    with d3
                    m "Не отвечают..."
                    jump examining_the_door
                "- Прислонить к ней ухо -":
                    show screen blktone8
                    with d3
                    ">Вы прикладываете ухо и внимательно слушаете..."
                    m "Я ничего не слышу."
                    hide screen blktone8
                    with d3
                    jump examining_the_door
                "- Ударить дверь -":
                    show screen blktone8
                    with d3
                    $ renpy.play('sounds/kick.ogg')
                    pause.2
                    with hpunch
                    "*Удар!*"
                    ".............................."
                    hide screen blktone8
                    with d3
                    m "Эта дверь выдержит тысячу ударов и не сломается..." 
                    m "Xотя и не выглядит запертой..."
                    jump examining_the_door
                "- Оставить в покое -":
                    m "Кто знает, какие опасности могут скрываться за этой дверью?"
                    m "Я думаю не стоит ничего с ней делать..."
                    pass
            show screen genie
            hide screen genie_stands
            hide screen chair_02 #Empty chair near the desk.
            hide screen desk
            with Dissolve(0.2)
            jump day_main_menu
            
            
       
            
        "{color=#858585}- Позвать Гермиону -{/color}" if this.Has("her_summon")  and hermione_takes_classes or hermione_sleeping:#summoning_hermione_unlocked
            if hermione_takes_classes:
                show screen bld1
                with d3
                ">Гермиона сейчас на уроке."
                hide screen bld1
                with d3
                jump day_main_menu
            elif hermione_sleeping:
                show screen bld1
                with d3
                ">Гермиона уже спит."
                hide screen bld1
                with d3
                jump night_main_menu
        
        "- Позвать Гермиону -" if this.Has("her_summon") and not hermione_takes_classes and not hermione_sleeping: #summoning_hermione_unlocked 
     
            if hermione_takes_classes:
                show screen bld1
                with d3
                ">Гермиона сейчас на уроке."
                hide screen bld1
                with d3
                jump day_main_menu
            elif hermione_sleeping:
                show screen bld1
                with d3
                ">Гермиона уже спит."
                hide screen bld1
                with d3
                jump night_main_menu
                
            else:
                #play music "music/Chipper Doodle v2.mp3" fadein 1 fadeout 1 
                #stop music fadeout 2.0
                
                $ menu_x = 0.2 #Menu is moved to the left side.
                $ pos = POS_410
                
                $ renpy.play('sounds/door.mp3') #Sound of a door opening.
                $ hermione_chibi_xpos = 400 #Near the desk.
                show screen hermione_02 #Hermione stands still.
                show screen bld1
                with d3
                if mad >=1 and mad < 3:
                    $herView.showQQ( "body_03.png", pos )
                    her ">Похоже, Гермиона по-прежнему немного расстроена вами..."
                elif mad >=3 and mad < 10:
                    $herView.showQQ( "body_03.png", pos )
                    ">Вы расстроили Гермиону."
                elif mad >=10 and mad < 20:
                    $herView.showQQ( "body_09.png", pos )
                    ">Гермиона очень расстроена вами."
                elif mad >=20 and mad < 40:
                    $herView.showQQ( "body_05.png", pos )
                    ">Гермиона злится на вас."
                elif mad >=40 and mad < 50:
                    $herView.showQQ( "body_47.png", pos )
                    ">Гермиона очень злится на вас."
                elif mad >=50 and mad < 60:
                    $herView.showQQ( "body_47.png", pos )
                    ">Гермиона в гневе на вас."
                elif mad >=60:
                    $herView.showQQ( "body_47.png", pos )
                    ">Гермиона ненавидит вас."
                else:
                    $herView.showQQ( "body_01.png", pos )
                    her "Да, профессор?"
                
                label day_time_requests:
                menu:
                    "- Поговорить -" if not chitchated_with_her:
                        $ chitchated_with_her = True #Prevents you from chitchatting with Hermione more then once per time of day. Turns back to False every night. (And every day).
                        if mad <= 7:
                            jump chit_chat
                        else:
                            her "Мне нечего сказать вам..."    
                            jump day_time_requests
                    "- Обучение -" if not daytime and not tut_happened and whoring <= 12:
                        if mad >=1 and mad < 3:
                            her "Извините, возможно завтра..."
                            jump day_time_requests
                        elif mad >=3 and mad < 10:
                            her "Сегодня я не в настроении..."
                            jump day_time_requests
                        elif mad >=20:
                            her "После того, что вы сделали?"
                            her "Я думаю нет..."
                            jump day_time_requests
                        else:
                            jump tutoring
                    "- Купить \"сексуальный\" рейтинг -" if this.Has("her_wants_buy"):#buying_favors_from_hermione_unlocked:
                        if mad >=1 and mad < 3:
                            her "Мне жаль, профессор, может быть в другой раз..."
                        elif mad >=3 and mad < 10:
                            her "Мне не хочется сегодня..."
                            her "Может быть через пару дней..."
                        elif mad >=10 and mad < 20:
                            her "Нет, спасибо...."
                        elif mad >=20 and mad < 30:
                            her "После того, что вы сделали?"
                            her "Я так не думаю..."
                        elif mad >=30 and mad < 40:
                            her "Вы серьезно!?"
                        elif mad >=40:
                            her "Это какая-то ваша пошлая шутка?!"
                            her "После того, что вы сделали, я не хочу повторять это!"
                        if mad==0:
                            jump new_personal_request
                        else:
                            jump day_time_requests
                   
                    
                    
                    
                    "- Дать ей подарок -" if not gifted:
                        menu:
                            "- Чупа-чупс -([candy])" if candy >= 1:
                                $ gifted = True 
                                jump giving_candy #28_gifts.rpy
                                
                            "- Шоколад -([chocolate])" if chocolate >= 1:
                                $ gifted = True 
                                jump giving_chocolate #28_gifts.rpy
                            
                            "- Чучело совы -([owl])" if owl >= 1:
                                $ gifted = True 
                                jump giving_owl #28_gifts.rpy
                                
                            "- Сливочное пиво -([beer])" if beer >= 1:
                                $ gifted = True 
                                jump giving_beer #28_gifts.rpy
                                
                            "- Обучающий журнал -([mag1])" if mag1 >= 1:
                                $ gifted = True 
                                jump giving_mag1 #28_gifts.rpy
                                
                            "- Женский журнал -([mag2])" if mag2 >= 1:
                                $ gifted = True 
                                jump giving_mag2 #28_gifts.rpy
                                
                            "- Журнал для взрослых -([mag3])" if mag3 >= 1:
                                $ gifted = True 
                                jump giving_mag3 #28_gifts.rpy
                                
                            "- Порно журнал -([mag4])" if mag4 >= 1:
                                $ gifted = True 
                                jump giving_mag4 #28_gifts.rpy
                            
                            "- Постер Виктора Крама -([krum])" if krum >= 1:
                                $ gifted = True 
                                jump giving_krum #28_gifts.rpy
                            
                            "- Сексуальное нижнее белье -([lingerie])" if lingerie >= 1:
                                $ gifted = True 
                                jump giving_lingerie #28_gifts.rpy
                            
                            "- Упаковка презервативов -([condoms])" if condoms >= 1:
                                $ gifted = True 
                                jump giving_condoms #28_gifts.rpy
                                
                            "- Банка анальной смазки -([anal_lube])" if anal_lube >= 1:
                                $ gifted = True 
                                jump giving_lube #28_gifts.rpy
                            
                            "- Вибратор -([vibrator])" if vibrator >= 1:
                                $ gifted = True 
                                jump giving_vibrator #28_gifts.rpy
                            
                            "- Кляп и наручники  -([ballgag])" if ballgag >= 1:
                                $ gifted = True 
                                jump giving_ballgag #28_gifts.rpy
                                
                            "- Анальная пробка  -([plug])" if plug >= 1:
                                $ gifted = True 
                                jump giving_plug #28_gifts.rpy
                                
                            "- Страпон \"Фестрал\"  -([strapon])" if strapon >= 1:
                                $ gifted = True 
                                jump giving_strapon #28_gifts.rpy
                            
                            "- Леди Спид Стик-2000  -([broom])" if broom >= 1:
                                $ gifted = True 
                                jump giving_broom #28_gifts.rpy
                                
                            "- Секс-кукла \"Джуанна\"  -([sexdoll])" if sexdoll >= 1:
                                $ gifted = True 
                                jump giving_sexdoll #28_gifts.rpy
                            
                            "- Школьная мини-юбка -" if have_miniskirt: # Turns TRUE when you have the skirt in your possession.
                                $ gifted = True
                                jump giving_skirt #28_gifts.rpy
                            
                            "- \"А.В.Н.Э.\" значок -" if badge_01 == 1:
                                $ gifted = True
                                jump giving_badge_01 #28_gifts.rpy
                            
                            "- Ажурные чулки -" if nets == 1:
                                $ gifted = True
                                jump giving_nets #28_gifts.rpy
                                
                                
                                
                                
                            "- Бальное платье -" if "ball_dress" in gifts12 and not gave_the_dress:
                                show screen  blktone
                                with d3
                                m "(Я чувствую, что не будет обратного пути, после того как я дам ей это платье...)"
                                m "(Я готов сделать это?)"
                                hide screen blktone
                                menu:
                                    "\"Да, вполне...\"":
                                        jump giving_thre_dress #27_final_events.rpy
                                    "\"Нет, не готов...\"":
                                        jump day_time_requests
                            "- Ничего -":
                                jump day_time_requests
                
                    
                    # "- Ending \"Your whore\"- ":
                        #jump your_whore
                        
                    # "- Ending \"Public whore\"- ":
                        # $ public_whore_ending = True #If TRUE the game will end with "Public Whore Ending".
                        # jump your_whore
                        
                    "- Гардероб -" if dress_code:
                        if mad >=1 and mad < 3:
                            her "Мне очень жаль, профессор. Может быть, в другой раз..."
                            jump day_time_requests
                        elif mad >=3 and mad < 10:
                            her "Что не так с моей одеждой?"
                            jump day_time_requests
                        elif mad >=10 and mad < 20:
                            her "Нет, спасибо...."
                            jump day_time_requests
                        elif mad >=20 and mad < 30:
                            her "Я так не думаю..."
                            jump day_time_requests
                        elif mad >=30 and mad < 40:
                            her "Нет!"
                            jump day_time_requests
                        elif mad >=40:
                            her "Я никогда не позволю вам снова решать, что мне носить!"
                            jump day_time_requests
                        else:
                            pass
                        menu:
                            
                            "- Надеть значок -" if (herView.data().getItem( G_N_BADGE )==None) and  badge_01 == 7: #not ba_01 and badge_01 == 7:
                                jump badge_put
                            
                            "- Снять значок -" if (herView.data().getItem( G_N_BADGE )!=None) and  badge_01 == 7: #ba_01 and badge_01 == 7:
                                jump badge_take
                            
                            "- Надеть колготки -" if (herView.data().getItem( G_N_NETS )==None) and  nets == 7: #not ne_01 and nets == 7: # Не перевел
                                jump nets_put
                            
                            "- Снять колготки -" if (herView.data().getItem( G_N_NETS )!=None) and  nets == 7: #ne_01 and nets == 7:
                                jump nets_take
                            
                            "- Надеть мини-юбку -" if herView.data().checkItem( G_N_SKIRT, 'skirt_normal.png' ) and gave_miniskirt: #not legs_02 and gave_miniskirt: #Turns True when Hermione has the miniskirt.:
                                jump mini_on #28_gifts.rpy

                            "- Надеть длинную юбку -" if herView.data().checkItem( G_N_SKIRT, 'skirt_short.png' ) and gave_miniskirt: #legs_02 and gave_miniskirt: #Turns True when Hermione has the miniskirt.
                                jump mini_off #28_gifts.rpy
                            
                           
  
                            "- Ничего -":
                                jump day_time_requests
                    
                        
#                    "- Personal requests (lv.1)":
#                        if slytherin > gryffindor or slytherin == gryffindor:
#                            menu:
#                                "Stand there. (I touch myself.)(5pt.)": #Request_01 (Level 01)
#                                    jump request_01
#                                "Lift your skirt.(5pt.)": #Request_02 (Level 01)
#                                    jump request_02
#                                "Flirt with 3 classmates.(5pt.)" if daytime: #Request_02_b (Level 01)
#                                    jump request_02_b
#                                "Flirt with a teacher.(5pt.)" if daytime:  #Request_02_c (Level 01)
#                                    jump request_02_c
#                                "Cancel.":
#                                    jump day_time_requests
#                        else:
#                            her "The Gryffindors are in the lead. I don't need to do this."
#                            jump day_time_requests
#                    ###LEVEL 02###    
#                    "- Personal requests (lv.2)":
#                        if slytherin > gryffindor or slytherin == gryffindor:
#                            menu:
#                                "Take her panties.(15pt.)" if daytime: #Request_03 (Level 02)
#                                    jump request_03
#                                "Touch her tits through her clothes. (15pt)": #Request_04 (Level 02)
#                                    jump request_04
#                                "Touch her butt though her clothes.(15pt)": #Request_05 (Level 02)
#                                    jump request_05
#                                "Flash panties to a classmate. (15pt)" if daytime: #Request_06 (Level 02)
#                                    jump request_06
#                                "Flash panties to a teacher.(15pt)" if daytime: #Request_07 (Level 02)
#                                    jump request_07
#                                "Cancel.":
#                                    jump day_time_requests
#                        else:
#                            her "The Gryffindors are in the lead. I don't need to do this."
#                            jump day_time_requests
#                    ###LEVEL 03###
#                    "- Personal requests (lv.3)":
#                        if slytherin > gryffindor or slytherin == gryffindor:
#                            menu:
#                                "Show me your tits. (25pt)":#Request_08 (Level 03)
#                                    jump request_08
#                                "Show me your pussy.(25pt)":#Request_09 (Level 03):
#                                    jump request_09
#                                "Flash a nipple to a classmate. (25pt)." if daytime:#Request_10 (Level 03)
#                                    jump request_10
#                                "Cancel.":
#                                    jump day_time_requests
#                        else:
#                            her "The Gryffindors are in the lead. I don't need to do this."
#                            jump day_time_requests
                                    
#                    ###LEVEL 04###
#                    "- Personal requests (lv.4)":
#                        if slytherin > gryffindor or slytherin == gryffindor:
#                            menu:
#                                "Strip completely.(35pt)":#Request_11 (Level 04)
#                                    jump request_11
#                                "Play with her tits.(35pt)":#Request_12 (Level 04):
#                                    jump request_12   
#                                "Wear a see-through shirt.(35pt)" if daytime:#Request_13 (Level 04):
#                                    jump request_13   
#                                "wear Cum-soaked panties": #Request_14 (Level 04) #To be added later when ability to jerk off and cum on panties added.
#                                    pass
#                                "Flash a nipple to a teacher.(35pt)" if daytime:#Request_15 (Level 04):
#                                    jump request_15   
#                                "Cancel.":
#                                    jump day_time_requests                    
#                        else:
#                            her "The Gryffindors are in the lead. I don't need to do this."
#                            jump day_time_requests
#                    ###LEVEL 05###
#                    "- Personal requests (lv.5)":
#                        if slytherin > gryffindor or slytherin == gryffindor:
#                            menu:
#                                "Finger her pussy.(45pt)":#Request_16 (Level 05)
#                                    jump request_16
#                                "Finger her butthole.(45pt)":#Request_17 (Level 05)
#                                    jump request_17
#                                "Handjob.(45pt)":#Request_18 (Level 05)
#                                    jump request_18
#                                "Rub your dick against her cheeks.(45pt)": #Request_19 (Level 05)
#                                    jump request_19
#                                "Grab a classmate's cock.(45pt)" if daytime: #Request_20 (Level 05)
#                                    jump request_20
#                                "Cancel.":
#                                    jump day_time_requests
#                        else:
#                            her "The Gryffindors are in the lead. I don't need to do this."
#                            jump day_time_requests
                     
#                    ###LEVEL 06###
#                    "- Personal requests (lv.6)":
#                        if slytherin > gryffindor or slytherin == gryffindor:
#                            menu:
#                                "Cum on tits.(55pt)":#Request_21 (Level 06)
#                                    jump request_21
#                                "Blowjob.(55pt)":#Request_22 (Level 06)
#                                    jump request_22
#                                "Give a handjob to a classmate.(55pt)" if daytime:#Request_23 (Level 06)
#                                    jump request_23
#                                "Flash your tits to a teacher.(55pt)" if daytime:#Request_24 (Level 06)
#                                    jump request_24
#                                "Cancel.":
#                                    jump day_time_requests
#                        else:
#                            her "The Gryffindors are in the lead. I don't need to do this."
#                            jump day_time_requests 
                    
#                    ###LEVEL 07###
#                    "- Personal requests (lv.7)":
#                        if slytherin > gryffindor or slytherin == gryffindor:
#                            menu:
#                                "Cum on face.(65pt)":#Request_25 (Level 07)
#                                    jump request_25
#                                "Cum in her mouth before class.(65pt)" if daytime:#Request_26 (Level 07)
#                                    jump request_26
#                                "Blow two classmates.(65pt)" if daytime:#Request_27 (Level 07)
#                                    jump request_27
#                                "Give a handjob to a teacher.(65pt)" if daytime:#Request_28 (Level 07)
#                                    jump request_28
#                                "Cancel.":
#                                    jump day_time_requests
#                        else:
#                            her "The Gryffindors are in the lead. I don't need to do this."
#                            jump day_time_requests  
                            
#                    ###LEVEL 08###
#                    "- Personal requests (lv.8)":
#                        if slytherin > gryffindor or slytherin == gryffindor:
#                            menu:
#                                "Sex.(75pt)":#Request_29 (Level 08)
#                                    jump request_29
#                                "Blow a teacher.(75pt)" if daytime: #Request_30 (Level 08)
#                                    jump request_30
#                                "Cancel.":
#                                    jump day_time_requests
#                        else:
#                            her "The Gryffindors are in the lead. I don't need to do this."
#                            jump day_time_requests 
                    
#                    ###LEVEL 09###
#                    "- Personal requests (lv.9)":
#                        if slytherin > gryffindor or slytherin == gryffindor:
#                            menu:
#                                "Anal sex.(85pt)" if not daytime:#Request_31 (Level 09)
#                                    jump request_31
#                                "Cancel.":
#                                    jump day_time_requests
#                        else:
#                            her "The Gryffindors are in the lead. I don't need to do this."
#                            jump day_time_requests 
                    
#                    ###LEVEL 10###
#                    "- Personal requests (lv.10)":
#                        if slytherin > gryffindor or slytherin == gryffindor:
#                            menu:
#                                "Wear a revealing outfit to class.(100pt)" if daytime:#Request_32 (Level 10)
#                                    jump request_32
#                                "Cum covered face.(100pt)" if daytime:#Request_33 (Level 10)
#                                    jump request_33
#                                "Cancel.":
#                                    jump day_time_requests
#                        else:
#                            her "The Gryffindors are in the lead. I don't need to do this."
#                            jump day_time_requests 
                    
                    
                    
                    "- Попросить уйти -":
#                        if daytime:
#                            play music "music/Brittle Rille.mp3" fadein 1 fadeout 1
#                        else:
#                            play music "music/Music for Manatees.mp3" fadein 1 fadeout 1
                        $ menu_x = 0.5 #Menu position is back to default. (Center).
                        if daytime:
                            $ hermione_takes_classes = True
                            if mad >=3 and mad <= 6:
                                her "..............................."
                            elif mad >=7:
                                her "*Гм!*..."
                            else:
                                her "О, хорошо! Тогда я пойду на уроки."
                            hide screen bld1
                            $herView.hideQ() 
                            hide screen blktone 
                            hide screen hermione_02
                            hide screen ctc
                            with d3
                            jump day_main_menu
                        else:
                            if mad >=3 and mad <= 6:
                                her "..............................."
                            elif mad >=7:
                                her "Пф..."
                            else:
                                her "О, хорошо! Тогда я пойду спать."
                            hide screen bld1
                            $herView.hideQ()
                            hide screen blktone 
                            hide screen hermione_02
                            hide screen ctc
                            with d3
                            $ hermione_sleeping = True
                            jump night_main_menu
                            
                            
            
        "{color=#858585}- Позвать Снейпа -{/color}" if this.Has("snape_summon") and snape_busy:#hanging_with_snape
            ">Профессор Снейп недоступен."
            if daytime:
                jump day_main_menu
            else: 
                jump night_main_menu
            
        "- Позвать Снейпа -" if this.Has("snape_summon") and not snape_busy:#hanging_with_snape
            play music "music/Dark Fog.mp3" fadein 1 fadeout 1 # SNAPE'S THEME
            jump summon_snape
        "- Ничего -":
            jump day_main_menu
    
    
                
################
### LEVEL 01 ###                
###################REQUEST_01
label request_01: #LV.1 (Whoring = 0 - 2)
    "Гермиона смотрит на вас с интересом и краснеет."
    "Вы провожаете Гермиону."
    if whoring <= 2:
        $ whoring +=1
    $ gryffindor +=5
    "Гриффиндор получает 5 очков."
    if daytime:
        $ hermione_takes_classes = True
        jump day_main_menu
    else:
        $ hermione_sleeping = True
        jump night_main_menu

    
###################REQUEST_02 (Level 01)
label request_02:
    "Сильно краснея и неохотно Гермиона поднимает юбку и показывает вам свои трусики."
    "Вы провожаете Гермиону."
    if whoring <= 2:
        $ whoring +=1
    $ gryffindor +=5
    "Гриффиндор получает 5 очков."
    if daytime:
        $ hermione_takes_classes = True
        jump day_main_menu
    else:
        $ hermione_sleeping = True
        jump night_main_menu
        

###################REQUEST_02_b (Level 01)
label request_02_b:
    "Гермиона соглашается попытаться заигрывать с 3 одноклассниками."
    "Вы провожаете Гермиону."
    $ request_02_b = True
    if whoring <= 2:
        $ whoring +=1
    $ gryffindor +=5
    "Гриффиндор получает 5 очков."
    if daytime:
        $ hermione_takes_classes = True
        jump day_main_menu
    else:
        $ hermione_sleeping = True
        jump night_main_menu
        
label request_02_b_complete:
    "Гермиона возвращается с занятий. Она рассказывает вам о парнях с которыми флиртовала."
    $ request_02_b = False 
    $ hermione_sleeping = True
    her "О, хорошо! Значит я пойду в кровать."
    return
    
###################REQUEST_02_c (Level 01)
label request_02_c:
    "Гермиона соглашается попробовать флиртовать с учителем."
    "Вы провожаете Гермиону."
    $ request_02_c = True
    if whoring <= 2:
        $ whoring +=1
    $ gryffindor +=5
    "Гриффиндор получает 5 очков."
    if daytime:
        $ hermione_takes_classes = True
        jump day_main_menu
    else:
        $ hermione_sleeping = True
        jump night_main_menu
        
label request_02_c_complete:
    "Гермиона возвращается с занятий. Она рассказывает вам о флирте с ее учителем."
    $ request_02_c = False 
    $ hermione_sleeping = True
    her "О, хорошо! Значит я пойду спать."
    return    
    
    
################
### LEVEL 02 ###    
###################REQUEST_03 (Level 02) (Available during daytime only).
label request_03: #(Whoring = 3 - 5)
    if whoring <=2:
        jump too_much
        
    if whoring >= 3: #Level 02
        "Гермиона нерешительно стягивает свои трусики и дает их вам."
        "Вы провожаете Гермиону."
        $ request_03 = True #True when Hermione has no panties on.
        if whoring <= 5:
            $ whoring +=1
        $ gryffindor +=15
        $ hermione_takes_classes = True
        "Гриффиндор получает 15 очков."
        jump day_main_menu
        
label request_03_complete:
    "Гермиона возвращается с занятий. Вы отдаете ей трусики обратно."
    $ request_03 = False #When False - you gave her her panties back.
    $ hermione_sleeping = True
    her "О, хорошо! Значит я пойду спать."
    return


###################REQUEST_04 (Level 02) (Touch tits's through fabric.)
label request_04:
    if whoring <=2:
        jump too_much
    if whoring >= 3: #Level 02
        "Гермиона позволяет поласкать ее грудь."
        "Вы провожаете Гермиону."
        if whoring <= 5:
            $ whoring +=1
        $ gryffindor +=15
        "Гриффиндор получает 15 очков."
        if daytime:
            $ hermione_takes_classes = True
            jump day_main_menu
        else:
            $ hermione_sleeping = True
            jump night_main_menu
            
###################REQUEST_05 (Level 02) (Touch butt through fabric.)
label request_05:
    if whoring <=2:
        jump too_much
    if whoring >= 3: #Level 02
        "Гермиона позволяет поласкать ее попку."
        "Вы провожаете Гермиону."
        if whoring <= 5:
            $ whoring +=1
        $ gryffindor +=15
        "Гриффиндор получает 15 очков."
        if daytime:
            $ hermione_takes_classes = True
            jump day_main_menu
        else:
            $ hermione_sleeping = True
            jump night_main_menu

###################REQUEST_06 (Level 02) (Flash panties to classmate.)
label request_06:
    if whoring <=2:
        jump too_much
    if whoring >= 3: #Level 02
        "Гермиона соглашается попробовать \"посветить\" своими трусиками перед одноклассником."
        "Вы провожаете Гермиону."
        $ request_05 = True
        if whoring <= 5:
            $ whoring +=1
        $ gryffindor +=15
        "Гриффиндор получает 15 очков."
        $ hermione_takes_classes = True
        jump day_main_menu
       
label request_05_complete:
    "Гермиона возвращается с занятий. Она рассказывает вам о своих попытках \"посветить\" своими трусиками перед одноклассником."
    $ request_05 = False 
    $ hermione_sleeping = True
    her "О, хорошо! Значит я пойду спать."
    return
    

###################REQUEST_07 (Level 02) (Flash panties to a teacher).(Daytime only).
label request_07:
    if whoring <=2:
        jump too_much
    if whoring >= 3: #Level 02
        "Гермиона соглашается попробовать \"посветить\" своими трусиками перед учителем."
        "Вы провожаете Гермиону."
        $ request_06 = True
        if whoring <= 5:
            $ whoring +=1
        $ gryffindor +=15
        "Гриффиндор получает 15 очков."
        $ hermione_takes_classes = True
        jump day_main_menu
        

label request_06_complete:
    "Гермиона возвращается с занятий и рассказывает о своих попытках \"посветить\" своими трусиками перед учителем."
    $ request_06 = False 
    $ hermione_sleeping = True
    her "О, хорошо! Значит я пойду спать."
    return
    
################
### LEVEL 03 ###
###################REQUEST_08 (Level 03) (Show me tits).
label request_08: #LV.3 (Whoring = 6 - 8)
    if whoring <=5:
        jump too_much
    "Гермиона показывает вам свою грудь."
    "Вы провожаете Гермиону."
    if whoring <= 8:
        $ whoring +=1
    $ gryffindor +=25
    "Гриффиндор получает 25 очков."
    if daytime:
        $ hermione_takes_classes = True
        jump day_main_menu
    else:
        $ hermione_sleeping = True
        jump night_main_menu

###################REQUEST_09 (Level 03) (Show me pussy).
label request_09: #LV.3 (Whoring = 6 - 8)
    if whoring <=5:
        jump too_much
    "Гермиона показывает вам свою киску."
    "Вы провожаете Гермиону."
    if whoring <= 8:
        $ whoring +=1
    $ gryffindor +=25
    "Гриффиндор получает 25 очков."
    if daytime:
        $ hermione_takes_classes = True
        jump day_main_menu
    else:
        $ hermione_sleeping = True
        jump night_main_menu

###################REQUEST_10 (Level 03) (25 pt.) (Flash nipple to a classmate). (Available during daytime only).
label request_10:
    if whoring <=5:
        jump too_much
    "Гермиона соглашается попробовать показать свои соски однокласснику."
    "Вы провожаете Гермиону."
    $ request_10 = True 
    if whoring <= 8:
        $ whoring +=1
    $ gryffindor +=25
    $ hermione_takes_classes = True
    "Гриффиндор получает 25 очков."
    jump day_main_menu
        
label request_10_complete:
    "Гермиона возвращается с занятий. Она рассказывает вам, как она мелькнула своими сосками перед одноклассником."
    $ request_10 = False 
    $ hermione_sleeping = True
    her "О, хорошо! Значит я пойду спать."
    return

################
### LEVEL 04 ###
###################REQUEST_11 (Level 04) (Get naked.) (Day/Night)
label request_11: #LV.4 (Whoring = 9 - 11)
    if whoring <=8:
        jump too_much
    "Гермиона раздевается перед вами, а затем откладывает одежду назад."
    "Вы провожаете Гермиону."
    if whoring <= 11:
        $ whoring +=1
    $ gryffindor +=35
    "Гриффиндор получает 35 очков."
    if daytime:
        $ hermione_takes_classes = True
        jump day_main_menu
    else:
        $ hermione_sleeping = True
        jump night_main_menu

###################REQUEST_12 (Level 04) (Play with her tits.) (Day/Night)
label request_12: #LV.4 (Whoring = 9 - 11)
    if whoring <=8:
        jump too_much
    "Гермиона обнажает свою грудь. Вы немного играете с ними."
    "Вы провожаете Гермиону."
    if whoring <= 11:
        $ whoring +=1
    $ gryffindor +=35
    "Гриффиндор получает 35 очков."
    if daytime:
        $ hermione_takes_classes = True
        jump day_main_menu
    else:
        $ hermione_sleeping = True
        jump night_main_menu

###################REQUEST_13 (Level 04) (35 pt.) (Wear see-though shirt to classes). (Available during daytime only).
label request_13: #LV.4 (Whoring = 9 - 11)
    if whoring <=8:
        jump too_much
    "Гермиона соглашается надеть прозрачную рубашку и пойти в класс."
    "Вы провожаете Гермиону."
    $ request_13 = True 
    if whoring <= 11:
        $ whoring +=1
    $ gryffindor +=35
    $ hermione_takes_classes = True
    "Гриффиндор получает 35 очков."
    jump day_main_menu
        
label request_13_complete:
    "Гермиона возвращается с занятий и рассказывает вам, как все пялились на ее грудь."
    $ request_13 = False 
    $ hermione_sleeping = True
    her "О, хорошо! Значит я пойду спать."
    return

###################REQUEST_15 (Level 04) (35 pt.) (Flash a nipple to a teacher). (Available during daytime only).
label request_15: #LV.4 (Whoring = 9 - 11)
    if whoring <=8:
        jump too_much
    "Гермиона соглашается попробовать \"посветить\" сосками перед учителем."
    "Вы провожаете Гермиону."
    $ request_15 = True 
    if whoring <= 11:
        $ whoring +=1
    $ gryffindor +=35
    $ hermione_takes_classes = True
    "Гриффиндор получает 35 очков."
    jump day_main_menu
        
label request_15_complete:
    "Гермиона возвращается с занятий. Она рассказывает вам, как она \"светила\" сосками перед учителем.."
    $ request_15 = False 
    $ hermione_sleeping = True
    her "О, хорошо! Значит я пойду спать."
    return

################
### LEVEL 05 ###   
###################REQUEST_16 (Level 05) (Finger her pussy) (Day/Night)
label request_16: #LV.5 (Whoring = 12 - 14)
    if whoring <=11:
        jump too_much
    "Гермиона позволяет пощупать ее киску."
    "Вы провожаете Гермиону."
    if whoring <= 14:
        $ whoring +=1
    $ gryffindor +=45
    "Гриффиндор получает 45 очков."
    if daytime:
        $ hermione_takes_classes = True
        jump day_main_menu
    else:
        $ hermione_sleeping = True
        jump night_main_menu
        
###################REQUEST_17 (Level 05) (Stick a finger up her but thole.) (Day/Night)
label request_17: #LV.5 (Whoring = 12 - 14)
    if whoring <=11:
        jump too_much
    "Гермиона позволяет поводить палецем у входа в ее попку."
    "Вы провожаете Гермиону."
    if whoring <= 14:
        $ whoring +=1
    $ gryffindor +=45
    "Гриффиндор получает 45 очков."
    if daytime:
        $ hermione_takes_classes = True
        jump day_main_menu
    else:
        $ hermione_sleeping = True
        jump night_main_menu


###################REQUEST_18 (Level 05) (Handjob) (Day/Night)
label request_18: #LV.5 (Whoring = 12 - 14)
    if whoring <=11:
        jump too_much
    "Гермиона дрочит вам."
    "Вы провожаете Гермиону."
    if whoring <= 14:
        $ whoring +=1
    $ gryffindor +=45
    "Гриффиндор получает 45 очков."
    if daytime:
        $ hermione_takes_classes = True
        jump day_main_menu
    else:
        $ hermione_sleeping = True
        jump night_main_menu

###################REQUEST_19 (Level 05) (Rub your dick against her cheeks.) (Day/Night)
label request_19: #LV.5 (Whoring = 12 - 14)
    if whoring <=11:
        jump too_much
    "Гермиона сидит на месте, пока вы трете свой член о ее личико."
    "Вы провожаете Гермиону."
    if whoring <= 14:
        $ whoring +=1
    $ gryffindor +=45
    "Гриффиндор получает 45 очков."
    if daytime:
        $ hermione_takes_classes = True
        jump day_main_menu
    else:
        $ hermione_sleeping = True
        jump night_main_menu

###################REQUEST_20 (Level 05) (45 pt.) (Grab a classmate's cock). (Available during daytime only).
label request_20: #LV.5 (Whoring = 12 - 14)
    if whoring <=11:
        jump too_much
    "Гермиона соглашается попробовать cхватить одноклассника за член."
    "Вы провожаете Гермиону."
    $ request_20 = True 
    if whoring <= 14:
        $ whoring +=1
    $ gryffindor +=45
    $ hermione_takes_classes = True
    "Гриффиндор получает 45 очков."
    jump day_main_menu
        
label request_20_complete:
    "Гермиона возвращается с занятий и рассказывает вам, как она схватила член одного из своих одноклассников."
    $ request_20 = False 
    $ hermione_sleeping = True
    her "О, хорошо! Значит я пойду спать."
    return
    
###################REQUEST_21 (Level 06) (55 pt.) (Cum on tits). 
#As this request levels up, there are an option appears to offer some extra points if Hermione will put her clothes
#on top of her sperm covered tits and go to classes like that.
label request_21: #LV.6 (Whoring = 15 - 17)
    if whoring <=14:
        jump too_much
    "Гермиона обнажает свою грудь. Вы дрочите и кончая, заливаете спермой ее прелестные сиськи."
    "Вы провожаете Гермиону."
    if whoring <= 17:
        $ whoring +=1
    $ gryffindor +=55
    $ hermione_takes_classes = True
    "Гриффиндор получает 55 очков."
    if daytime:
        $ hermione_takes_classes = True
        jump day_main_menu
    else:
        $ hermione_sleeping = True
        jump night_main_menu
        
###################REQUEST_22 (Level 06) (55 pt.) (Blowjob). 
label request_22: #LV.6 (Whoring = 15 - 17)
    if whoring <=14:
        jump too_much
    "Гермиона делает вам минет."
    "Вы провожаете Гермиону."
    if whoring <= 17:
        $ whoring +=1
    $ gryffindor +=55
    $ hermione_takes_classes = True
    "Гриффиндор получает 55 очков."
    if daytime:
        $ hermione_takes_classes = True
        jump day_main_menu
    else:
        $ hermione_sleeping = True
        jump night_main_menu
        
###################REQUEST_23 (Level 06) (55 pt.) (Give handjob to a classmate). (Available during daytime only).
label request_23: #LV.6 (Whoring = 15 - 17)
    if whoring <=14:
        jump too_much
    "Гермиона соглашается попробовать подрочить однокласснику."
    "Вы провожаете Гермиону."
    $ request_23 = True 
    if whoring <= 17:
        $ whoring +=1
    $ gryffindor +=55
    $ hermione_takes_classes = True
    "Гриффиндор получает 55 очков."
    jump day_main_menu
        
label request_23_complete:
    "Гермиона возвращается с занятий и рассказывает вам, как дрочила одному из своих одноклассников во время урока."
    $ request_23 = False 
    $ hermione_sleeping = True
    her "О, хорошо. Тогда я пойду спать."
    return

###################REQUEST_24 (Level 06) (55 pt.) (Flash your tits to a teacher). (Available during daytime only).
label request_24: #LV.6 (Whoring = 15 - 17)
    if whoring <=14:
        jump too_much
    "Гермиона соглашается попробовать и \"посветить\" грудью перед учителем."
    "Вы провожаете Гермиону."
    $ request_24 = True 
    if whoring <= 17:
        $ whoring +=1
    $ gryffindor +=55
    $ hermione_takes_classes = True
    "Гриффиндор получает 55 очков."
    jump day_main_menu
        
label request_24_complete:
    "Гермиона возвращается с занятий. Она рассказывает вам, как она \"светила\" сиськами перед учителем."
    $ request_24 = False 
    $ hermione_sleeping = True
    her "О, хорошо. Тогда я пойду спать."
    return
    
###################REQUEST_25 (Level 07) (65 pt.) (Cum on face). 
label request_25: #LV.7 (Whoring = 18 - 20)
    if whoring <=17:
        jump too_much
    "Гермиона сидит на месте, пока вы дрочите на ее лицо."
    "Вы провожаете Гермиону."
    if whoring <= 20:
        $ whoring +=1
    $ gryffindor +=65
    $ hermione_takes_classes = True
    "Гриффиндор получает 65 очков."
    if daytime:
        $ hermione_takes_classes = True
        jump day_main_menu
    else:
        $ hermione_sleeping = True
        jump night_main_menu
        
###################REQUEST_26 (Level 07) (65 pt.) (Cum in open mouth before class). (Available during daytime only).
label request_26: #LV.7 (Whoring = 18 - 20)
    if whoring <=17:
        jump too_much
    
    "Гермиона сидит с открытым ртом, пока вы дрочите и кончаете в него. Вы запретили ей глотать, до того, как она попадет в класс."
    "Вы провожаете Гермиону с полным ртом своей спермы."
    
    $ request_26 = True 
    if whoring <= 20:
        $ whoring +=1
    $ gryffindor +=65
    $ hermione_takes_classes = True
    "Гриффиндор получает 65 очков."
    jump day_main_menu
        
label request_26_complete:
    "Гермиона возвращается с занятий и рассказывает вам, что не могла говорить с одноклассниками, потому что ее рот был заполнен вашей спермой."
    $ request_26 = False 
    $ hermione_sleeping = True
    her "О, хорошо. Тогда я пойду спать."
    return

###################REQUEST_27 (Level 07) (65 pt.) (Blow two classmates). (Available during daytime only).
label request_27: #LV.7 (Whoring = 18 - 20)
    if whoring <=17:
        jump too_much
    "Гермиона соглашается попробовать отсосать двум одноклассникам во время занятий."
    "Вы провожаете Гермиону."
    $ request_27 = True 
    if whoring <= 20:
        $ whoring +=1
    $ gryffindor +=65
    $ hermione_takes_classes = True
    "Гриффиндор получает 65 очков."
    jump day_main_menu
        
label request_27_complete:
    "Гермиона возвращается с занятий. Она рассказывает вам, как она сосала двум одноклассникам во время занятий."
    $ request_27 = False 
    $ hermione_sleeping = True
    her "О, хорошо. Тогда я пойду спать."
    return

###################REQUEST_28 (Level 07) (65 pt.) (Give handjob to a teacher). (Available during daytime only).
label request_28: #LV.7 (Whoring = 18 - 20)
    if whoring <=17:
        jump too_much
    "Гермиона соглашается попробовать и подрочить учителю во время занятий."
    "Вы провожаете Гермиону."
    $ request_28 = True 
    if whoring <= 20:
        $ whoring +=1
    $ gryffindor +=65
    $ hermione_takes_classes = True
    "Гриффиндор получает 65 очков."
    jump day_main_menu
        
label request_28_complete:
    "Гермиона возвращается с занятий и рассказывает вам, как она мастурбировала учителю во время занятий."
    $ request_28 = False 
    $ hermione_sleeping = True
    her "О, хорошо. Тогда я пойду спать."
    return
    
################
### LEVEL 08 ###
###################REQUEST_29 (Level 08) (75 pt.) (Sex). 
label request_29: #LV.8 (Whoring = 21 - 23)
    if whoring <=20:
        jump too_much
    if daytime:
        "Вы занимаетесь сексом с Гермионой, после чего отправляете ее на занятия."
    else:
        "Вы занимаетесь сексом с Гермионой."
        "Вы провожаете Гермиону."
    if whoring <= 23:
        $ whoring +=1
    $ gryffindor +=75
    "Гриффиндор получает 75 очков."
    if daytime:
        $ hermione_takes_classes = True
        jump day_main_menu
    else:
        $ hermione_sleeping = True
        jump night_main_menu

###################REQUEST_30 (Level 08) (75 pt.) (Blow a teacher). (Available during daytime only).
label request_30: #LV.8 (Whoring = 21 - 23)
    if whoring <=20:
        jump too_much
    "Гермиона соглашается попробовать и сосет у учителя."
    "Вы провожаете Гермиону."
    $ request_30 = True 
    if whoring <= 23:
        $ whoring +=1
    $ gryffindor +=75
    $ hermione_takes_classes = True
    "Гриффиндор получает 75 очков."
    jump day_main_menu
        
label request_30_complete:
    "Гермиона возвращается с занятий. Она рассказывает вам, как она делала минет учителю во время занятий."
    $ request_30 = False 
    $ hermione_sleeping = True
    her "О, хорошо. Тогда я пойду спать."
    return

################
### LEVEL 09 ###
###################REQUEST_31 (Level 09) (85 pt.) (Anal sex). (Nighttime)
label request_31: #LV.9 (Whoring = 24 - 26)
    if whoring <=23:
        jump too_much
    "Вы занимаетесь анальным сексом с Гермионой"
    "Вы провожаете Гермиону."
    if whoring <= 26:
        $ whoring +=1
    $ gryffindor +=85
    "Гриффиндор получает 85 очков."
    $ hermione_sleeping = True
    jump day_start


################
### LEVEL 10 ###
###################REQUEST_32 (Level 10) (100 pt.) (Wear a very revealing outfit to class). (Daytime only)
label request_32: #LV.10 (Whoring = 27 - 29)
    if whoring <=26:
        jump too_much
    "Гермиона надевает очень распутный наряд и идет на занятия."
    $ request_32 = True
    if whoring <= 29:
        $ whoring +=1
    $ gryffindor +=100
    $ hermione_takes_classes = True
    "Гриффиндор получает 100 очков."
    jump day_main_menu

label request_32_complete:
    "Гермиона возвращается с занятий и говорит, что люди относились к ней как к шлюхе."
    $ request_32 = False 
    $ hermione_sleeping = True
    her "О, хорошо. Тогда я пойду спать."
    return

###################REQUEST_33 (Level 10) (100 pt.) THIS REQUEST IS NOW CAN ONLY BE ACCESSED THROUGH REQUEST_25 (CUM ON FACE) when whoring > 26. (Go to class with cum on your face). (Daytime only)
label request_33: #LV.10 (Whoring = 27 - 29)
    if whoring <=26:
        jump too_much
    "Вы кончаете на лицо Гермионы и отправляете ее на занятия."
    $ request_33 = True
    if whoring <= 29:
        $ whoring +=1
    $ gryffindor +=100
    $ hermione_takes_classes = True
    "Гриффиндор получает 100 очков."
    jump day_main_menu

label request_33_complete:
    "Гермиона возвращается с занятий и говорит, что люди относились к ней, как потаскухе и смеялись над ней."
    $ request_33 = False 
    $ hermione_sleeping = True
    her "О, хорошо. Тогда я пойду спать."
    return





#############This massage shows when you make a request, and Hermione refuses because she is not slutty enough yet.
label too_much:
    if IsEventOnlyAfter("new_personal_request"): # Если попали сюда после ивента, запущенного через меню "new_personal_request", значит ивент не завершен
        $event.NotFinished()
    stop music fadeout 2.0
    $herView.hideQQ()
    $ pos = POS_120
    $herView.showQQ( "body_48.png", pos )
    her "Профессор Дамблдор??!"
    her "Как вы можете просить меня о таком!?"
    $herView.hideQQ()
    $herView.showQQ( "body_34.png", pos )
    her "По-моему, мне лучше уйти."

    hide screen blktone
    hide screen bld1
    $herView.hideQ()
    with Dissolve(.3)
    $ walk_xpos=400 #Animation of walking chibi. (From)
    $ walk_xpos2=610 #Coordinates of it's movement. (To)
    $ hermione_speed = 02.0 #The speed of moving the walking animation across the screen.
    show screen hermione_walk_01_f 
    pause 2
    hide screen hermione_walk_01_f 
    $ hermione_chibi_xpos = 610 #Near the desk.
    with Dissolve(.3)    
    
    hide screen hermione_01_f #Hermione stands still.
    with Dissolve(.3)
    $ renpy.play('sounds/door.mp3') #Sound of a door opening.
    with Dissolve(.3)
    pause.5
    
    $ mad += 7
    
    ### MUSIC BLOCK ###
    if daytime:
        play music "music/Brittle Rille.mp3" fadein 1 fadeout 1 # DAY MUSIC
    else:
        play music "music/Music for Manatees.mp3" fadein 1 fadeout 1 # NIGHT MUSIC
    ### END OF BLOCK ###
    
    if daytime:
        $ hermione_takes_classes = True
        jump day_main_menu
    else:
        $ hermione_sleeping = True
        jump night_main_menu


