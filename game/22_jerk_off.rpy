label jerk_off:
   $ cum_on_desk = False
   $ cum_on_the_floor = False
   $ jerk_zorder = 5
   $ cum_on_panties = False #True when choose to cum on Hermione's panties.
   m "Хм...кем же мы займемся сегодня?"
   menu:
       "- Принцесса Жасмин -":
           m "Да, принцесса... Эта грязная шлюха!"
           $ jerking_off_to_jasmine = True #Princess Jasmine has been chosen as a target for a jerk-off session
           pass
       "- Лара Крофт -":
           $ jerking_off_to_lara = True
           pass
       "- Передумал -":
           jump desk

   m "Куда бы кончить?"   
   label how_to_finish:
       menu:
           "- На пол -":
               $ cum_on_the_floor = True #TRUE when chosen to cum on the floor.
               pass
           "- На стол -":
               $ cum_on_desk = True
               pass
           "{color=#858585}- (ЗАБЛОКИРОВАННО) -{/color}" if not request_03: #True when Hermione has no panties on.:
               ">Вам не доступен этот выбор."
               jump how_to_finish
           "- Трусики Гермионы -" if request_03: #True when Hermione has no panties on.
               $ cum_on_panties = True #True when choose to cum on Hermione's panties.
               pass
           "- Отмена -":
               jump jerk_off


   ### JERKING OFF ###
   with d5
   ">Вы решили вздрочнуть, вспоминая былые времена..."
   show screen genie_jerking_off
   with d8
   if jerking_off_to_jasmine:
       ">Вы фантазируете о принцессе Жасмин..."
       $ checked = 'jas'
       g9 "Ух...да, та еще шлюшка..."
       jump random_pics
   if jerking_off_to_lara:
       ">Вы фантазируете о Ларе Крофт..."
       $ checked = 'lara'
       g9 "О да... эта соска была великолепна..."
       # show image "03_hp/22_dreams/lara/1.png" onlayer overlay at Transform(zoom=0.9)# CLEAR WEATHER.
       with d8
       jump random_pics
       
   label finish_cum:
       ">Вы вот-вот кончите..."
       if one_out_of_three == 1:
           g4 "Архг! Шлюха!"
       elif one_out_of_three == 2:
           g4 "ДА! ПОЛУЧАЙ ПОТАСКУХА! АРХ"
       elif one_out_of_three == 2:
           g4 "О да! Вау... Давненько такого не было."
       # hide screen genie_jerking_off
       show screen genie_jerking_sperm
       if cum_on_desk:
           ">Вы обильно кончаете на стол."
           g4 "Придется здесь прибраться..."
       if cum_on_the_floor:
           ">Вы кончили на пол."
       if cum_on_panties:
           $ have_cum_soaced_panties = True #TRUE when you have the panties in your possession (before you return them to Hermione).
           ">Вы кончили на трусики Гермионы, а затем протерли ими пол..."
           ">Вы получили предмет: \"Трусики пропитанные спермой\"."
       hide screen genie_jerking_sperm
       g7 "Да уж, было время. Интересно, получится ли повторить все, что было?"
       g7 "Был бы не против снова натянуть эту потаскуху... как ее там... Лара..."
       g4 "Да и принцесса еще та соска. Как вспомню ее влажный ротик. Ух..."
       g4 "Ладно, стоит вернуться к текущим делам."
   ### SETTING ALL THE FLAGS BACK TO DEFAULT ###
   $ jerking_off_to_jasmine = False #Turns TRUE when Princess Jasmine has been chosen as a target for a jerk-off session.
   $ jerking_off_to_lara = False 
   $ cum_on_the_floor = False #TRUE when chosen to cum on the floor.
   $ cum_on_panties = False #True when choose to cum on Hermione's panties.
   
   if daytime:
       jump night_start
   else: 
       jump day_start
   
   label random_pics:
           $ list_of_files_jas = 10
           $ list_of_files_lara = 103
           
           if checked == 'jas':
               $ directory_of_images = '03_hp/22_dreams/jas'
               $ list_of_files = list_of_files_jas
           elif checked == 'lara':
               $ list_of_files = list_of_files_lara
               $ directory_of_images = '03_hp/22_dreams/lara'
           else:
               $ list_of_files = list_of_files_jas
               $ directory_of_images = '03_hp/22_dreams/jas'

           # About python code
           python:
                x = 0
                list_of_numbers = []
                while x < 10:
                    random_int = renpy.random.randint(1, list_of_files)
                    list_of_numbers.append(random_int)
                    x = x+1
                list_of_numbers = set(list_of_numbers)
            
                for i in list_of_numbers:
                    jerk_image = directory_of_images + '/%s.png' % i
                    renpy.show_screen("jerkingimage")
                    renpy.pause()
                    renpy.hide_screen("jerkingimage")
           # /About python code
           
           $ directory_of_images = False;
           $ list_of_files = False;
           jump finish_cum
