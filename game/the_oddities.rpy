label the_oddities:
    menu:
        dahr "Добро пожаловать в \"каталог Приблуд Дахра\". Ваши предпочтения не покажутся нам странными!"
        "-Образовательные книги-":
            label education_menu:
            menu:
                ###01"\"Copper book of spirit\""   
                "-Книга: [book01]-" if not "book_01" in books:
                    $ the_gift = "03_hp/18_store/08.png" # Copper book of spirit.
                    show screen gift
                    with d3
                    dahr "\"[book01]\". \nЭта книга содержит различные советы о том, как улучшить свою эффективность."
                    menu:
                        "-Купить книгу за 40 золота -":
                            if gold >= 40:
                                $ gold -= 40
                                $ order_placed = True
                                $ bought_book_01 = True
                                call thx_4_shoping #Massage that says "Thank you for shopping here!".
                                jump desk
                            else:
                                call no_gold #Massage: m "I don't have enough gold".
                                jump education_menu
                        "-Ничего-":
                            hide screen gift
                            jump education_menu
#                "-Книга: [book01] (own)-" if "book_01" in books:
#                    call do_have_book #Message that says that you already bought this book.
#                    jump the_oddities 
                
                
                ###02"\"Bronze book of spirit\""   
                "-Книга: [book02]-" if not "book_02" in books:
                    $ the_gift = "03_hp/18_store/08.png" # Copper book of spirit.
                    show screen gift
                    with d3
                    dahr "\"[book02]\". \nЭта книга содержит различные советы о том, как улучшить свою эффективность."
                    menu:
                        "-Купить книгу за 80 золота -":
                            if gold >= 80:
                                $ gold -= 80
                                $ order_placed = True
                                $ bought_book_02 = True
                                call thx_4_shoping #Massage that says "Thank you for shopping here!".
                                jump desk
                            else:
                                call no_gold #Massage: m "I don't have enough gold".
                                jump education_menu    
                        "-Ничего-":
                            hide screen gift
                            jump education_menu
#                "-Книга: [book02] (own)-" if "book_02" in books:
#                    call do_have_book #Message that says that you already bought this book.
#                    jump the_oddities 
                
                ###03#"\"Silver book of spirit\""  
                "-Книга: [book03]-" if not "book_03" in books:
                    $ the_gift = "03_hp/18_store/08.png" # Copper book of spirit.
                    show screen gift
                    with d3
                    dahr "\"[book03]\". \nЭта книга содержит различные советы о том, как улучшить свою эффективность."
                    menu:
                        "-Купить книгу за 90 золота -":
                            if gold >= 90:
                                $ gold -=90
                                $ order_placed = True
                                $ bought_book_03 = True
                                call thx_4_shoping #Massage that says "Thank you for shopping here!".
                                jump desk
                            else:
                                call no_gold #Massage: m "I don't have enough gold".
                                hide screen gift
                                jump education_menu    
                        "-Ничего-":
                            hide screen gift
                            jump education_menu
#                "-Книга: [book03] (own)-" if "book_03" in books:
#                    call do_have_book #Message that says that you already bought this book.
#                    jump the_oddities 
                    
                ###04"\"Golden book of spirit\"" 
                "-Книга: [book04]-" if not "book_04" in books:
                    $ the_gift = "03_hp/18_store/08.png" # Copper book of spirit.
                    show screen gift
                    with d3
                    dahr "\"[book04]\".\nЭта книга содержит различные советы о том, как улучшить свою эффективность."
                    menu:
                        "-Купить книгу за 100 золота -":
                            if gold >= 100:
                                $ gold -= 100
                                $ order_placed = True
                                $ bought_book_04 = True
                                call thx_4_shoping #Massage that says "Thank you for shopping here!".
                                jump desk
                            else:
                                call no_gold #Massage: m "I don't have enough gold".
                                jump education_menu    
                        "-Ничего-":
                            hide screen gift
                            jump education_menu
#                "-Книга: [book04] (own)-" if "book_04" in books:
#                    call do_have_book #Message that says that you already bought this book.
#                    jump the_oddities 
                    
#                ###10"\"Platinum book of spirit\""
#                "-Книга: [book10]-" if not "book_10" in books:
#                    $ the_gift = "03_hp/18_store/08.png" # Copper book of spirit.
#                    show screen gift
#                    with d3
#                    dahr "\"[book10]\".\nThis book contains various tips on how to improve one's efficiency."
#                    menu:
#                        "-Купить книгу за 120 золота -":
#                            if gold >= 120:
#                                $ gold -=120
#                                $ order_placed = True
#                                $ bought_book_10 = True
#                                call thx_4_shoping #Massage that says "Thank you for shopping here!".
#                                jump desk
#                            else:
#                                call no_gold #Massage: m "I don't have enough gold".
#                                jump education_menu    
#                        "-Ничего-":
#                            hide screen gift
#                            jump education_menu
##                "-Книга: [book10] (own)-" if "book_10" in books:
##                    call do_have_book #Message that says that you already bought this book.
##                    jump the_oddities 
                
#                ###11#"\"Adamantium book of spirit\""
#                "-Книга: [book11]-" if not "book_11" in books:
#                    $ the_gift = "03_hp/18_store/08.png" # Copper book of spirit.
#                    show screen gift
#                    with d3
#                    dahr "\"[book11]\".\nThis book contains various tips on how to improve one's efficiency."
#                    menu:
#                        "-Купить книгу за 150 золота -":
#                            if gold >= 150:
#                                $ gold -= 150
#                                $ order_placed = True
#                                $ bought_book_11 = True
#                                call thx_4_shoping #Massage that says "Thank you for shopping here!".
#                                jump desk
#                            else:
#                                call no_gold #Massage: m "I don't have enough gold".
#                                jump education_menu    
#                        "-Ничего-":
#                            hide screen gift
#                            jump education_menu
##                "-Книга: [book11] (own)-" if "book_11" in books:
##                    call do_have_book #Message that says that you already bought this book.
##                    jump the_oddities 
                
                ###12"\"Speedwriting for dummies.\""
                "-Книга: [book12]-" if not "book_12" in books:
                    $ the_gift = "03_hp/18_store/08.png" # Copper book of spirit.
                    show screen gift
                    with d3
                    dahr "\"[book12]\".\nЭта книга содержит несколько элементарных методов, используемых для улучшения своего навыка скорописания."
                    menu:
                        "-Купить книгу за 30 золота -":
                            if gold >= 30:
                                $ gold -=30
                                $ order_placed = True
                                $ bought_book_12 = True
                                call thx_4_shoping #Massage that says "Thank you for shopping here!".
                                jump desk
                            else:
                                call no_gold #Massage: m "I don't have enough gold".
                                jump education_menu    
                        "-Ничего-":
                            hide screen gift
                            jump education_menu
#                "-Книга: [book12] (own)-" if "book_12" in books:
#                    call do_have_book #Message that says that you already bought this book.
#                    jump the_oddities 
                
                #"\"Speedwriting for beginners.\""
                "-Книга: [book13]-" if not "book_13" in books:
                    $ the_gift = "03_hp/18_store/08.png" # Copper book of spirit.
                    show screen gift
                    with d3
                    dahr "\"[book13]\".\nЭта книга содержит несколько базовых методов, используемых для улучшения своего навыка скорописания."
                    menu:
                        "-Купить книгу за 90 золота -":
                            if gold >= 90:
                                $ gold -=90
                                $ order_placed = True
                                $ bought_book_13 = True
                                call thx_4_shoping #Massage that says "Thank you for shopping here!".
                                jump desk
                            else:
                                call no_gold #Massage: m "I don't have enough gold".
                                jump education_menu    
                        "-Ничего-":
                            hide screen gift
                            jump education_menu
#                "-Книга: [book13] (own)-" if "book_13" in books:
#                    call do_have_book #Message that says that you already bought this book.
#                    jump the_oddities 
                
                #"\"Speedwriting for intermediates.\""
                "-Книга: [book14]-" if not "book_14" in books:
                    $ the_gift = "03_hp/18_store/08.png" # Copper book of spirit.
                    show screen gift
                    with d3
                    dahr "\"[book14]\".\nЭта книга содержит несколько начальных методов, используемых для улучшения своего навыка скорописания."
                    menu:
                        "-Купить книгу за 100 золота -":
                            if gold >= 100:
                                $ gold -= 100
                                $ order_placed = True
                                $ bought_book_14 = True
                                call thx_4_shoping #Massage that says "Thank you for shopping here!".
                                jump desk
                            else:
                                call no_gold #Massage: m "I don't have enough gold".
                                jump education_menu    
                        "-Ничего-":
                            hide screen gift
                            jump education_menu
#                "-Книга: [book14] (own)-" if "book_14" in books:
#                    call do_have_book #Message that says that you already bought this book.
#                    jump the_oddities 
                
                #"\"Speedwriting for the advanced.\""
                "-Книга: [book15]-" if not "book_15" in books:
                    $ the_gift = "03_hp/18_store/08.png" # Copper book of spirit.
                    show screen gift
                    with d3
                    dahr "\"[book15]\".\nЭта книга содержит несколько продвинутых методов, используемых для улучшения своего навыка скорописания."
                    menu:
                        "-Купить книгу за 130 золота -":
                            if gold >= 130:
                                $ gold -= 130
                                $ order_placed = True
                                $ bought_book_15 = True
                                call thx_4_shoping #Massage that says "Thank you for shopping here!".
                                jump desk
                            else:
                                call no_gold #Massage: m "I don't have enough gold".
                                jump education_menu    
                        "-Ничего-":
                            hide screen gift
                            jump education_menu
#                "-Книга: [book15] (own)-" if "book_15" in books:
#                    call do_have_book #Message that says that you already bought this book.
#                    jump the_oddities  
                    
#                #"\"Speedwriting for experts.\""
#                "-Книга: [book16]-" if not "book_16" in books:
#                    $ the_gift = "03_hp/18_store/08.png" # Copper book of spirit.
#                    show screen gift
#                    with d3
#                    dahr "\"[book16]\".\nThis book contains expert techniques used to improve one's ability to write quickly."
#                    menu:
#                        "-Купить книгу за 150 золота -":
#                            if gold >= 150:
#                                $ gold -=150
#                                $ order_placed = True
#                                $ bought_book_16 = True
#                                call thx_4_shoping #Massage that says "Thank you for shopping here!".
#                                jump desk
#                            else:
#                                call no_gold #Massage: m "I don't have enough gold".
#                                jump education_menu    
#                        "-Ничего-":
#                            hide screen gift
#                            jump education_menu
##                "-Книга: [book16] (own)-" if "book_16" in books:
##                    call do_have_book #Message that says that you already bought this book.
##                    jump the_oddities  
                
#                #"\"Speedwriting for maniacs.\""
#                "-Книга: [book17]-" if not "book_17" in books:
#                    $ the_gift = "03_hp/18_store/08.png" # Copper book of spirit.
#                    show screen gift
#                    with d3
#                    #dahr "\"[book17]\"\nThis book contains maniacal level techniques used to improve one's ability to write quickly."
#                    dahr "\"[book17]\"\nThis book contains techniques which let one master the art of speedwriting completely."
#                    menu:
#                        "-Купить книгу за 170 золота -":
#                            if gold >= 170:
#                                $ gold -= 170
#                                $ order_placed = True
#                                $ bought_book_17 = True
#                                call thx_4_shoping #Massage that says "Thank you for shopping here!".
#                                jump desk
#                            else:
#                                call no_gold #Massage: m "I don't have enough gold".
#                                jump education_menu    
#                        "-Ничего-":
#                            hide screen gift
#                            jump education_menu
#                "-Книга: [book17] (own)-" if "book_17" in books:
#                    call do_have_book #Message that says that you already bought this book.
#                    jump the_oddities  
                
                ###08 "SPEED READING FOR DUMMIES" #
                "-Книга: [book08]-" if not "book_08" in books:
                    $ the_gift = "03_hp/18_store/08.png" # Copper book of spirit.
                    show screen gift
                    with d3
                    dahr "\"[book08]\"\nЭта книга содержит несколько базовых методов, используемых для улучшения своего навыка скорочтения."
                    menu:
                        "-Купить книгу за 50 золота -":
                            if gold >= 50:
                                $ gold -=50
                                $ order_placed = True
                                $ bought_book_08 = True
                                call thx_4_shoping #Massage that says "Thank you for shopping here!".
                                jump desk
                            else:
                                call no_gold #Massage: m "I don't have enough gold".
                                jump education_menu    
                        "-Ничего-":
                            hide screen gift
                            jump education_menu
#                "-Книга: [book08] (own)-" if "book_08" in books:
#                    call do_have_book #Message that says that you already bought this book.
#                    jump the_oddities  
            
                ###09 "SPEED READING FOR EXPERTS" #
                "-Книга: [book09]-" if not "book_09" in books:
                    $ the_gift = "03_hp/18_store/08.png" # Copper book of spirit.
                    show screen gift
                    with d3
                    dahr "\"[book08]\"\nЭта книга содержит несколько экспертных методов, используемых для улучшения своего навыка скорочтения."
                    menu:
                        "-Купить книгу за 90 золота -":
                            if gold >= 90:
                                $ gold -=90
                                $ order_placed = True
                                $ bought_book_09 = True
                                call thx_4_shoping #Massage that says "Thank you for shopping here!".
                                jump desk
                            else:
                                call no_gold #Massage: m "I don't have enough gold".
                                jump education_menu    
                        "-Ничего-":
                            hide screen gift
                            jump education_menu
#                "-Книга: [book09] (own)-" if "book_09" in books:
#                    call do_have_book #Message that says that you already bought this book.
#                    jump the_oddities  
                
                "-Ничего-":
                    jump the_oddities
         
         
        "-Фантастика-":
            label fiction_menu:
            menu:
                ###06"\"The game of chairs\""
                "-Книга: [book06]- {image=check_07.png}" if not "book_06" in books:
                    $ the_gift = "03_hp/18_store/02.png" # GAME OF THRONES.
                    show screen gift
                    with d3
                    "\"[book06]\"" "Эпический рассказ о предательстве, убийствах и изнасилованиях, а затем еще несколько убийств, немного больше предательства и еще больше изнасилований."
                    menu:
                        "-Купить книгу за 100 золота -":
                            if gold >= 100:
                                $ gold -=100
                                $ order_placed = True
                                $ bought_book_06 = True #Affects 15_mail.rpy
                                call thx_4_shoping #Massage that says "Thank you for shopping here!".
                                jump desk
                            else:
                                hide screen gift
                                call no_gold #Massage: m "I don't have enough gold".
                                jump fiction_menu
                         
                        "-Ничего-":
                            hide screen gift
                            jump fiction_menu
                "-Книга: [book06] {image=check_08.png}-" if "book_06" in books:
                    call do_have_book #Message that says that you already bought this book.
                    jump fiction_menu
                
            
            
            
            
            
            
            
            
            
            
                ###05"\"The Tale of Galadriel\""    
                "-Книга: [book05]- {image=check_07.png}" if not "book_05" in books:
                    $ the_gift = "03_hp/18_store/04.png" # ADVENTURE OF GALADRIEL. BOOK ONE.
                    show screen gift
                    with d3
                    ">Эта книга рассказывает историю эльфийской принцессы, которая бросает вызов традициям своего народа и выбирает оковы для ее сосбтвенной судьбы. Или все не так?"
                    #">This book contains a rather lengthy tale describing in great detail life and adventures of young elven female by the name of Galadriel."
                    menu:
                        "-Купить книгу за 200 золота -":
                            if gold >= 200:
                                $ gold -=200
                                $ order_placed = True
                                $ bought_book_05 = True
                                call thx_4_shoping #Massage that says "Thank you for shopping here!".
                                jump desk
                            else:
                                call no_gold #Massage: m "I don't have enough gold".
                                jump fiction_menu
                                
                        "-Ничего-":
                            hide screen gift
                            jump fiction_menu
                "-Книга: [book05] {image=check_08.png}-" if "book_05" in books:
                    call do_have_book #Message that says that you already bought this book.
                    jump fiction_menu
                
        
                ###05_b"\"The Tale of Galadriel. BOOK TWO\""    
                "-Книга: [book05b]- {image=check_07.png}" if not "book_05_b" in books:
                    $ the_gift = "03_hp/18_store/05.png" # ADVENTURE OF GALADRIEL. BOOK TWO.
                    show screen gift
                    with d3
                    ">Эта книга рассказывает историю эльфийской принцессы, которая бросает вызов традициям своего народа и выбирает оковы для ее сосбтвенной судьбы. Или все не так? "
                    #">This book contains a rather lengthy tale describing in great detail life and adventures of young elven female by the name of Galadriel."
                    menu:
                        "-Купить книгу за 250 золота -":
                            if gold >= 250:
                                $ gold -=250
                                $ order_placed = True
                                $ bought_book_05_b = True
                                call thx_4_shoping #Massage that says "Thank you for shopping here!".
                                jump desk
                            else:
                                call no_gold #Massage: m "I don't have enough gold".
                                jump fiction_menu
                                
                        "-Ничего-":
                            hide screen gift
                            jump fiction_menu
                "-Книга: [book05b]- {image=check_08.png}" if "book_05_b" in books:
                    call do_have_book #Message that says that you already bought this book.
                    jump fiction_menu
                
                
               
                ###07"\"My dear waifu\""
                "-Книга: [book07] {image=check_07.png}-" if not "book_07" in books:
                    $ the_gift = "03_hp/18_store/03.png" # MY DEAR WAIFU.
                    show screen gift
                    with d3
                    "\"[book07]\" {size=-4}BY AKABUR{/size}" "Переживите славные дни в вашей школе. Ваша сводная сестра Ши, учитель Мисс Стивенс или таинственная девушка из библиотеки? Кто станет ваша окончательной \"вайфу\"?"
                    menu:
                        "-Купить книгу за 300 золота -":
                            if gold >= 300:
                                $ gold -=300
                                $ order_placed = True
                                $ bought_book_07 = True #Affects 15_mail.rpy
                                call thx_4_shoping #Massage that says "Thank you for shopping here!".
                                jump desk
                            else:
                                call no_gold #Massage: m "I don't have enough gold".
                                jump fiction_menu
                        "-Ничего-":
                            hide screen gift
                            jump fiction_menu
                "-Книга: [book07]- {image=check_08.png}" if "book_07" in books:
                    call do_have_book #Message that says that you already bought this book.
                    jump fiction_menu
                

                "-Ничего-":
                    jump the_oddities
                
         



















        "-Подарки-":
            label gifts_menu:
            menu:
                #dahr "Gifts that you can gift to that special someone."
                
                "-Чупа-чупс- (20 з.)":
                    $ the_gift = "03_hp/18_store/11.png" # CANDY.
                    show screen gift
                    with d3
                    dahr "Чупа-чупс. Взрослая конфета для детей или детская конфета для взрослых?"
                    menu:
                        "-Купить это (20 золота)-":
                            if gold >= 20:
                                $ gold -=20
                                $ order_placed = True
                                $ bought_candy = True #Affects 15_mail.rpy
                                call thx_4_shoping #Massage that says "Thank you for shopping here!".
                                jump desk
                            else:
                                call no_gold #Massage: m "I don't have enough gold".
                                jump gifts_menu
                        "-Ничего-":
                            hide screen gift
                            jump gifts_menu
                            
                "-Шоколад- (40 з.)":
                    $ the_gift = "03_hp/18_store/12.png" # CHOCOLATE.
                    show screen gift
                    with d3
                    call choco_text
                    menu:
                        "-Купить это (40 золота)-":
                            if gold >= 40:
                                $ gold -= 40
                                $ order_placed = True
                                $ bought_chocolate = True #Affects 15_mail.rpy
                                call thx_4_shoping #Massage that says "Thank you for shopping here!".
                                jump desk
                            else:
                                call no_gold #Massage: m "I don't have enough gold".
                                jump gifts_menu
                        "-Ничего-":
                            hide screen gift
                            jump gifts_menu
                            
                "-Плюшевая сова- (35 з.)":
                    $ the_gift = "03_hp/18_store/22.png" # PLUSH OWL
                    show screen gift
                    with d3
                    call owl_text
                    menu:
                        "-Купить это (35 золота)-":
                            if gold >= 35:
                                $ gold -= 35
                                $ order_placed = True
                                $ bought_owl = True #Affects 15_mail.rpy
                                call thx_4_shoping #Massage that says "Thank you for shopping here!".
                                jump desk
                            else:
                                call no_gold #Massage: m "I don't have enough gold".
                                jump gifts_menu
                        "-Ничего-":
                            hide screen gift
                            jump gifts_menu
                            
                
                "{color=#858585}-Товар закончился-{/color}" if whoring < 3: # BUTTERBEER.
                    show screen bld1
                    with d3
                    call out # Message "Item us out of stock".
                    hide screen bld1
                    with d3
                    jump gifts_menu
                "-Сливочное пиво- (50 з.)" if whoring >= 3: # LEVEL 02.
                    $ the_gift = "03_hp/18_store/21.png" # BUTTERBEER
                    show screen gift
                    with d3
                    call beer_text
                    menu:
                        "-Купить это (50 золота)-":
                            if gold >= 50:
                                $ gold -= 50
                                $ order_placed = True
                                $ bought_beer = True #Affects 15_mail.rpy
                                call thx_4_shoping #Massage that says "Thank you for shopping here!".
                                jump desk
                            else:
                                call no_gold #Massage: m "I don't have enough gold".
                                jump gifts_menu
                        "-Ничего-":
                            hide screen gift
                            jump gifts_menu

                    
                    
                "-Обучающий журнал- (30 з.)":
                    $ the_gift = "03_hp/18_store/17.png" # MAGAZINE # 1
                    show screen gift
                    with d3
                    call mag1_text
                    menu:
                        "-Купить это (30 золота)-":
                            if gold >= 30:
                                $ gold -= 30
                                $ order_placed = True
                                $ bought_mag1 = True #Affects 15_mail.rpy
                                call thx_4_shoping #Massage that says "Thank you for shopping here!".
                                jump desk
                            else:
                                call no_gold #Massage: m "I don't have enough gold".
                                jump gifts_menu
                        "-Ничего-":
                            hide screen gift
                            jump gifts_menu
                
                "-Женский журнал- (45 з.)":
                    $ the_gift = "03_hp/18_store/18.png" # MAGAZINE # 2
                    show screen gift
                    with d3
                    call mag2_text
                    menu:
                        "-Купить это (45 золота)-":
                            if gold >= 45:
                                $ gold -= 45
                                $ order_placed = True
                                $ bought_mag2 = True #Affects 15_mail.rpy
                                call thx_4_shoping #Massage that says "Thank you for shopping here!".
                                jump desk
                            else:
                                call no_gold #Massage: m "I don't have enough gold".
                                jump gifts_menu
                        "-Ничего-":
                            hide screen gift
                            jump gifts_menu


                "-Журнал для взрослых- (60 з.)":
                    $ the_gift = "03_hp/18_store/19.png" # MAGAZINE # 3
                    show screen gift
                    with d3
                    call mag3_text
                    menu:
                        "-Купить это (60 золота)-":
                            if gold >= 60:
                                $ gold -= 60
                                $ order_placed = True
                                $ bought_mag3 = True #Affects 15_mail.rpy
                                call thx_4_shoping #Massage that says "Thank you for shopping here!".
                                jump desk
                            else:
                                call no_gold #Massage: m "I don't have enough gold".
                                jump gifts_menu
                        "-Ничего-":
                            hide screen gift
                            jump gifts_menu
                            
                
                "{color=#858585}-Этот товар закончился на складе-{/color}" if whoring < 3: # PORN MAGAZINES.
                    show screen bld1
                    with d3
                    call out # Message "Item us out of stock".
                    hide screen bld1
                    with d3
                    jump gifts_menu
                "-Порно журнал- (80 з.)" if whoring >= 3: # LEVEL 02.
                    $ the_gift = "03_hp/18_store/20.png" # MAGAZINE # 4
                    show screen gift
                    with d3
                    call mag4_text
                    menu:
                        "-Купить это (80 золота)-":
                            if gold >= 80:
                                $ gold -= 80
                                $ order_placed = True
                                $ bought_mag4 = True #Affects 15_mail.rpy
                                call thx_4_shoping #Massage that says "Thank you for shopping here!".
                                jump desk
                            else:
                                call no_gold #Massage: m "I don't have enough gold".
                                jump gifts_menu
                        "-Ничего-":
                            hide screen gift
                            jump gifts_menu


                "{color=#858585}-Этот товар закончился на складе-{/color}" if whoring < 3: # CONDOMS.
                    show screen bld1
                    with d3
                    call out # Message "Item us out of stock".
                    hide screen bld1
                    with d3
                    jump gifts_menu
                "-Упаковка презервативов- (50 з.)" if whoring >= 3: # LEVEL 02.
                    $ the_gift = "03_hp/18_store/10.png" # CONDOMS
                    show screen gift
                    with d3
                    call con_text
                    menu:
                        "-Купить это (50 золота)-":
                            if gold >= 50:
                                $ gold -= 50
                                $ order_placed = True
                                $ bought_condoms = True #Affects 15_mail.rpy
                                call thx_4_shoping #Massage that says "Thank you for shopping here!".
                                jump desk
                            else:
                                call no_gold #Massage: m "I don't have enough gold".
                                jump gifts_menu
                        "-Ничего-":
                            hide screen gift
                            jump gifts_menu
                
                "{color=#858585}-Этот товар закончился на складе-{/color}" if whoring < 3: # VIBRATOR
                    show screen bld1
                    with d3
                    call out # Message "Item us out of stock".
                    hide screen bld1
                    with d3
                    jump gifts_menu
                "-Вибратор- (55 з.)" if whoring >= 3: # LEVEL 02.
                    $ the_gift = "03_hp/18_store/13.png" # VIBRATOR.
                    show screen gift
                    with d3
                    call vib_text
                    menu:
                        "-Купить это (55 золота)-":
                            if gold >= 55:
                                $ gold -=55
                                $ order_placed = True
                                $ bought_vibrator = True #Affects 15_mail.rpy
                                call thx_4_shoping #Massage that says "Thank you for shopping here!".
                                jump desk
                            else:
                                call no_gold #Massage: m "I don't have enough gold".
                                jump gifts_menu
                        "-Ничего-":
                            hide screen gift
                            jump gifts_menu
                
                "-Банка лубриканта (60 з.)":
                    $ the_gift = "03_hp/18_store/09.png" # ANAL LUBRICANT
                    show screen gift
                    with d3
                    call lub_text
                    menu:
                        "-Купить это (60 золота)-":
                            if gold >= 60:
                                $ gold -= 60
                                $ order_placed = True
                                $ bought_anal_lube = True #Affects 15_mail.rpy
                                call thx_4_shoping #Massage that says "Thank you for shopping here!".
                                jump desk
                            else:
                                call no_gold #Massage: m "I don't have enough gold".
                                jump gifts_menu
                        "-Ничего-":
                            hide screen gift
                            jump gifts_menu
                

                "-Кляп и наручники- (70 з.)":
                    $ the_gift = "03_hp/18_store/15.png" # BALL GAG.
                    show screen gift
                    with d3
                    call ball_text
                    menu:
                        "-Купить это (70 золота)-":
                            if gold >= 70:
                                $ gold -= 70
                                $ order_placed = True
                                $ bought_ballgag = True #Affects 15_mail.rpy
                                call thx_4_shoping #Massage that says "Thank you for shopping here!".
                                jump desk
                            else:
                                call no_gold #Massage: m "I don't have enough gold".
                                jump gifts_menu
                        "-Ничего-":
                            hide screen gift
                            jump gifts_menu
                
                "{color=#858585}-Этот товар закончился на складе-{/color}" if whoring < 3: # VIBRATOR
                    show screen bld1
                    with d3
                    call out # Message "Item us out of stock".
                    hide screen bld1
                    with d3
                    jump gifts_menu
                "-Анальная пробка- (85 з.)" if whoring >= 3: # LEVEL 02.
                    $ the_gift = "03_hp/18_store/16.png" # ANAL PLUGS.
                    show screen gift
                    with d3
                    call anal_text
                    menu:
                        "-Купить это (85 золота)-":
                            if gold >= 85:
                                $ gold -= 85
                                $ order_placed = True
                                $ bought_plug = True #Affects 15_mail.rpy
                                call thx_4_shoping #Massage that says "Thank you for shopping here!".
                                jump desk
                            else:
                                call no_gold #Massage: m "I don't have enough gold".
                                jump gifts_menu
                        "-Ничего-":
                            hide screen gift
                            jump gifts_menu
                
                "{color=#858585}-Этот товар закончился на складе-{/color}" if whoring < 3: # VIBRATOR
                    show screen bld1
                    with d3
                    call out # Message "Item us out of stock".
                    hide screen bld1
                    with d3
                    jump gifts_menu
                "- Страпон \"Thestral\" - (200 з.)" if whoring >= 3: # LEVEL 02.
                    $ the_gift = "03_hp/18_store/14.png" # STRAP-ON.
                    show screen gift
                    with d3
                    call str_text
                    menu:
                        "-Купить это (200 золота)-":
                            if gold >= 200:
                                $ gold -=200
                                $ order_placed = True
                                $ bought_strapon = True #Affects 15_mail.rpy
                                call thx_4_shoping #Massage that says "Thank you for shopping here!".
                                jump desk
                            else:
                                call no_gold #Massage: m "I don't have enough gold".
                                jump gifts_menu
                        "-Ничего-":
                            hide screen gift
                            jump gifts_menu
                
                
                
                
                "-Ничего-":
                            hide screen gift
                            with d3
                            jump the_oddities
                
                
                
                
                            
                            
        "-Одежда-":
            label app:
                pass
            menu:

                    
           
#                "{color=#858585}-Этот товар закончился на складе-{/color}"
#                    show screen bld1
#                    with d3
#                    call out # Message "Item us out of stock".
#                    hide screen bld1
#                    with d3
#                    jump app
                "-\"А.В.Н.Э.\" знак (100 золота)-" if not badge_01 == 7:
                    $ the_gift = "03_hp/18_store/29.png" # SPEW BADGE.
                    show screen gift
                    with d3
                    dahr "Значок \"А.В.Н.Э.\". Симулируй заботу..."
                    menu:
                        "-Купить это (100 золота)-":
                            if badge_01 == 7 or badge_01 == 1: # == 7 means "gifted already" # badge_01 == 1 because otherwise you could still buy it in the shop, even if you have 1 already.
                                call do_have_book # "I already own this one."
                                jump app
                            else:
                                if gold >= 100:
                                    $ gold -=100
                                    $ order_placed = True
                                    $ bought_badge_01 = True #Affects 15_mail.rpy
                                    call thx_4_shoping #Massage that says "Thank you for shopping here!".
                                    jump desk
                                else:
                                    call no_gold #Massage: m "I don't have enough gold".
                                    hide screen gift
                                    with d3
                                    jump app
                        "-Ничего-":
                            hide screen gift
                            with d3
                            jump app
                            
                
                
#                "{color=#858585}-Этот товар закончился на складе-{/color}" if whoring < 3: # $ level = "02":
#                    show screen bld1
#                    with d3
#                    call out # Message "Item us out of stock".
#                    hide screen bld1
#                    with d3
#                    jump app
                "-Ажурные чулки (800 золота)-" if not nets == 7:
                    $ the_gift = "03_hp/18_store/30.png" # FISHNETS.
                    show screen gift
                    with d3
                    call nets_text
                    menu:
                        "-Купить это (800 золота)-":
                            if nets == 7 or nets == 1: # == 7 means "gifted already"
                                call do_have_book # "I already own this one."
                                jump app
                            else:
                                if gold >= 800:
                                    $ gold -= 800
                                    $ order_placed = True
                                    $ bought_nets = True #Affects 15_mail.rpy
                                    call thx_4_shoping #Massage that says "Thank you for shopping here!".
                                    jump desk
                                else:
                                    call no_gold #Massage: m "I don't have enough gold".
                                    hide screen gift
                                    with d3
                                    jump app
                        "-Ничего-":
                            hide screen gift
                            with d3
                            jump app





#                "{color=#858585}-Этот товар закончился на складе-{/color}" if whoring < 3: # $ level = "02": MINI SKIRT.
#                    show screen bld1
#                    with d3
#                    call out # Message "Item us out of stock".
#                    hide screen bld1
#                    with d3
#                    jump app
                "-Школьная мини-юбка- (---)" if not bought_skirt_already and not gave_miniskirt and whoring >= 3:
                    $ the_gift = "03_hp/18_store/07.png" # MINISKIRT
                    show screen gift
                    with d3
                    dahr "Школьная мини-юбка. Резко улучшает оценки."
                    menu:
                        "-Купить юбку- (---)":
                            if vouchers >= 1: #Shows the amount of DAHR's vouchers in your possession.
                                $ vouchers -= 1 #Shows the amount of DAHR's vouchers in your possession.
                                $ order_placed = True
                                $ bought_miniskirt = True #Affects 15_mail.rpy
                                call thx_4_shoping #Massage that says "Thank you for shopping here!".
                                jump desk
                            else:
                                dahr "Эту вещь можно купить только за \"Ваучер Дахра\"."
                                dahr "Что-то не так..."
                                dahr "Чертовы переводчики..."
                                dahr "Я..."
                                translators "Так-то лучше. Этот момент показался всем достаточно сложным. Я о юбке. Дальше будет подсказка, как ее получить."
                                menu:
                                    "-Глянуть подсказку-":
                                        translators "{size=14}Подсказка от переводчика:\nНайти его можно {b}правильно{/b} прочитав книгу {b}[book07]{/b}{/size}."
                                        translators "{size=14}Более подробно {a=http://pornolab.net/forum/viewtopic.php?t=1930734}здесь{/a} в F.A.Q{/size}."
                                    
                                    "-Не нужно-":
                                        translators "Как угодно."
                                hide screen gift
                                with d3
                                jump app
                        "-Ничего-":
                            hide screen gift
                            with d3
                            jump app
#                "-Item Sold Out-" if bought_skirt_already:
#                    "This item has been sold out."
#                    jump app
                            
                            
                            
                "-Предмет уже распродан-" if bought_dress_already:
                    "Этот товар уже продан."
                    jump app
                "{color=#858585}-Этот товар закончился на складе-{/color}" if not sorry_for_hesterics: # NIGHT DRESS.
                    show screen bld1
                    with d3
                    call out # Message "Item us out of stock".
                    hide screen bld1
                    with d3
                    jump app
                "-Бальное платье- (1500 золота)" if sorry_for_hesterics and not bought_dress_already:
                    $ the_gift = "03_hp/18_store/01.png" # DRESS.
                    show screen gift
                    with d3
                    dahr "Ночное платье для особых случаев."
                    menu:
                        "-Купить платье (1500 золота)-":
                            if gold >= 1500:
                                $ gold -=1500
                                $ order_placed = True
                                $ bought_ball_dress = True #Affects 15_mail.rpy
                                call thx_4_shoping #Massage that says "Thank you for shopping here!".
                                jump desk
                            else:
                                call no_gold #Massage: m "I don't have enough gold".
                                hide screen gift
                                with d3
                                jump app
                        "-Ничего-":
                            hide screen gift
                            with d3
                            jump app
                            
                "-Ничего-":
                        jump the_oddities
                        
        "-Священные свитки. Часть I-":
            label sscrolls:
            menu:

                "-С.01: [scroll_01_name]-" if not sscroll_01:
                    $ the_gift = "03_hp/18_store/31.png" # SACRED SCROLL.
                    show screen gift
                    with d3
                    call sscroll
                    menu:
                        "-Купить свиток (30 золота)-":
                            if gold >= 30:
                                $ gold -=30
                                $ sscroll_01 = True # Turns TRUE if the scroll had been bought.
                                $ renpy.play('sounds/win_04.mp3')   #Not loud.
                                call sscroll_bought
                                call thx_4_shoping2 #Massage that says "Thank you for shopping here!".
                                jump desk
                            else:
                                call no_gold #Massage: m "I don't have enough gold".
                                hide screen gift
                                jump sscrolls
                        "-Ничего-":
                            hide screen gift
                            jump sscrolls
                
                "-С.02: [scroll_02_name]-" if not sscroll_02:
                    $ the_gift = "03_hp/18_store/31.png" # SACRED SCROLL.
                    show screen gift
                    with d3
                    call sscroll
                    menu:
                        "-Купить свиток (30 золота)-":
                            if gold >= 30:
                                $ gold -=30
                                $ sscroll_02 = True # Turns TRUE if the scroll had been bought.
                                $ renpy.play('sounds/win_04.mp3')   #Not loud.
                                call sscroll_bought
                                call thx_4_shoping2 #Massage that says "Thank you for shopping here!".
                                jump desk
                            else:
                                call no_gold #Massage: m "I don't have enough gold".
                                hide screen gift
                                jump sscrolls
                        "-Ничего-":
                            hide screen gift
                            jump sscrolls
                
                "-С.03: [scroll_03_name]-" if not sscroll_03:
                    $ the_gift = "03_hp/18_store/31.png" # SACRED SCROLL.
                    show screen gift
                    with d3
                    call sscroll
                    menu:
                        "-Купить свиток (30 золота)-":
                            if gold >= 30:
                                $ gold -=30
                                $ sscroll_03 = True # Turns TRUE if the scroll had been bought.
                                $ renpy.play('sounds/win_04.mp3')   #Not loud.
                                call sscroll_bought
                                call thx_4_shoping2 #Massage that says "Thank you for shopping here!".
                                jump desk
                            else:
                                call no_gold #Massage: m "I don't have enough gold".
                                hide screen gift
                                jump sscrolls
                        "-Ничего-":
                            hide screen gift
                            jump sscrolls
                            
                "-С.04: [scroll_04_name]-" if not sscroll_04:
                    $ the_gift = "03_hp/18_store/31.png" # SACRED SCROLL.
                    show screen gift
                    with d3
                    call sscroll
                    menu:
                        "-Купить свиток (30 золота)-":
                            if gold >= 30:
                                $ gold -=30
                                $ sscroll_04 = True # Turns TRUE if the scroll had been bought.
                                $ renpy.play('sounds/win_04.mp3')   #Not loud.
                                call sscroll_bought
                                call thx_4_shoping2 #Massage that says "Thank you for shopping here!".
                                jump desk
                            else:
                                call no_gold #Massage: m "I don't have enough gold".
                                hide screen gift
                                jump sscrolls
                        "-Ничего-":
                            hide screen gift
                            jump sscrolls
                            
                "-С.05: [scroll_05_name]-" if not sscroll_05:
                    $ the_gift = "03_hp/18_store/31.png" # SACRED SCROLL.
                    show screen gift
                    with d3
                    call sscroll
                    menu:
                        "-Купить свиток (30 золота)-":
                            if gold >= 30:
                                $ gold -=30
                                $ sscroll_05 = True # Turns TRUE if the scroll had been bought.
                                $ renpy.play('sounds/win_04.mp3')   #Not loud.
                                call sscroll_bought
                                call thx_4_shoping2 #Massage that says "Thank you for shopping here!".
                                jump desk
                            else:
                                call no_gold #Massage: m "I don't have enough gold".
                                hide screen gift
                                jump sscrolls
                        "-Ничего-":
                            hide screen gift
                            jump sscrolls
                            
                "-С.06: [scroll_06_name]-" if not sscroll_06:
                    $ the_gift = "03_hp/18_store/31.png" # SACRED SCROLL.
                    show screen gift
                    with d3
                    call sscroll
                    menu:
                        "-Купить свиток (30 золота)-":
                            if gold >= 30:
                                $ gold -=30
                                $ sscroll_06 = True # Turns TRUE if the scroll had been bought.
                                $ renpy.play('sounds/win_04.mp3')   #Not loud.
                                call sscroll_bought
                                call thx_4_shoping2 #Massage that says "Thank you for shopping here!".
                                jump desk
                            else:
                                call no_gold #Massage: m "I don't have enough gold".
                                hide screen gift
                                jump sscrolls
                        "-Ничего-":
                            hide screen gift
                            jump sscrolls
                            
                "-С.07: [scroll_07_name]-" if not sscroll_07:
                    $ the_gift = "03_hp/18_store/31.png" # SACRED SCROLL.
                    show screen gift
                    with d3
                    call sscroll
                    menu:
                        "-Купить свиток (30 золота)-":
                            if gold >= 30:
                                $ gold -=30
                                $ sscroll_07 = True # Turns TRUE if the scroll had been bought.
                                $ renpy.play('sounds/win_04.mp3')   #Not loud.
                                call sscroll_bought
                                call thx_4_shoping2 #Massage that says "Thank you for shopping here!".
                                jump desk
                            else:
                                call no_gold #Massage: m "I don't have enough gold".
                                hide screen gift
                                jump sscrolls
                        "-Ничего-":
                            hide screen gift
                            jump sscrolls
                            
                "-С.08: [scroll_08_name]-" if not sscroll_08:
                    $ the_gift = "03_hp/18_store/31.png" # SACRED SCROLL.
                    show screen gift
                    with d3
                    call sscroll
                    menu:
                        "-Купить свиток (30 золота)-":
                            if gold >= 30:
                                $ gold -=30
                                $ sscroll_08 = True # Turns TRUE if the scroll had been bought.
                                $ renpy.play('sounds/win_04.mp3')   #Not loud.
                                call sscroll_bought
                                call thx_4_shoping2 #Massage that says "Thank you for shopping here!".
                                jump desk
                            else:
                                call no_gold #Massage: m "I don't have enough gold".
                                hide screen gift
                                jump sscrolls
                        "-Ничего-":
                            hide screen gift
                            jump sscrolls
                            
                "-С.09: [scroll_09_name]-" if not sscroll_09:
                    $ the_gift = "03_hp/18_store/31.png" # SACRED SCROLL.
                    show screen gift
                    with d3
                    call sscroll
                    menu:
                        "-Купить свиток (30 золота)-":
                            if gold >= 30:
                                $ gold -=30
                                $ sscroll_09 = True # Turns TRUE if the scroll had been bought.
                                $ renpy.play('sounds/win_04.mp3')   #Not loud.
                                call sscroll_bought
                                call thx_4_shoping2 #Massage that says "Thank you for shopping here!".
                                jump desk
                            else:
                                call no_gold #Massage: m "I don't have enough gold".
                                hide screen gift
                                jump sscrolls
                        "-Ничего-":
                            hide screen gift
                            jump sscrolls
                            
                "-С.10: [scroll_10_name]-" if not sscroll_10:
                    $ the_gift = "03_hp/18_store/31.png" # SACRED SCROLL.
                    show screen gift
                    with d3
                    call sscroll
                    menu:
                        "-Купить свиток (30 золота)-":
                            if gold >= 30:
                                $ gold -=30
                                $ sscroll_10 = True # Turns TRUE if the scroll had been bought.
                                $ renpy.play('sounds/win_04.mp3')   #Not loud.
                                call sscroll_bought
                                call thx_4_shoping2 #Massage that says "Thank you for shopping here!".
                                jump desk
                            else:
                                call no_gold #Massage: m "I don't have enough gold".
                                hide screen gift
                                jump sscrolls
                                
                "-С.11: [scroll_11_name]-" if not sscroll_11:
                    $ the_gift = "03_hp/18_store/31.png" # SACRED SCROLL.
                    show screen gift
                    with d3
                    call sscroll
                    menu:
                        "-Купить свиток (30 золота)-":
                            if gold >= 30:
                                $ gold -=30
                                $ sscroll_11 = True # Turns TRUE if the scroll had been bought.
                                $ renpy.play('sounds/win_04.mp3')   #Not loud.
                                call sscroll_bought
                                call thx_4_shoping2 #Massage that says "Thank you for shopping here!".
                                jump desk
                            else:
                                call no_gold #Massage: m "I don't have enough gold".
                                hide screen gift
                                jump sscrolls
                        "-Ничего-":
                            hide screen gift
                            jump sscrolls
                
                "-С.12: [scroll_12_name]-" if not sscroll_12:
                    $ the_gift = "03_hp/18_store/31.png" # SACRED SCROLL.
                    show screen gift
                    with d3
                    call sscroll
                    menu:
                        "-Купить свиток (30 золота)-":
                            if gold >= 30:
                                $ gold -=30
                                $ sscroll_12 = True # Turns TRUE if the scroll had been bought.
                                $ renpy.play('sounds/win_04.mp3')   #Not loud.
                                call sscroll_bought
                                call thx_4_shoping2 #Massage that says "Thank you for shopping here!".
                                jump desk
                            else:
                                call no_gold #Massage: m "I don't have enough gold".
                                hide screen gift
                                jump sscrolls
                        "-Ничего-":
                            hide screen gift
                            jump sscrolls
                
                "-С.13: [scroll_13_name]-" if not sscroll_13:
                    $ the_gift = "03_hp/18_store/31.png" # SACRED SCROLL.
                    show screen gift
                    with d3
                    call sscroll
                    menu:
                        "-Купить свиток (30 золота)-":
                            if gold >= 30:
                                $ gold -=30
                                $ sscroll_13 = True # Turns TRUE if the scroll had been bought.
                                $ renpy.play('sounds/win_04.mp3')   #Not loud.
                                call sscroll_bought
                                call thx_4_shoping2 #Massage that says "Thank you for shopping here!".
                                jump desk
                            else:
                                call no_gold #Massage: m "I don't have enough gold".
                                hide screen gift
                                jump sscrolls
                        "-Ничего-":
                            hide screen gift
                            jump sscrolls
        
                "-С.14: [scroll_14_name]-" if not sscroll_14:
                    $ the_gift = "03_hp/18_store/31.png" # SACRED SCROLL.
                    show screen gift
                    with d3
                    call sscroll
                    menu:
                        "-Купить свиток (30 золота)-":
                            if gold >= 30:
                                $ gold -=30
                                $ sscroll_14 = True # Turns TRUE if the scroll had been bought.
                                $ renpy.play('sounds/win_04.mp3')   #Not loud.
                                call sscroll_bought
                                call thx_4_shoping2 #Massage that says "Thank you for shopping here!".
                                jump desk
                            else:
                                call no_gold #Massage: m "I don't have enough gold".
                                hide screen gift
                                jump sscrolls
                        "-Ничего-":
                            hide screen gift
                            jump sscrolls
                
                "-С.15: [scroll_15_name]-" if not sscroll_15:
                    $ the_gift = "03_hp/18_store/31.png" # SACRED SCROLL.
                    show screen gift
                    with d3
                    call sscroll
                    menu:
                        "-Купить свиток (30 золота)-":
                            if gold >= 30:
                                $ gold -=30
                                $ sscroll_15 = True # Turns TRUE if the scroll had been bought.
                                $ renpy.play('sounds/win_04.mp3')   #Not loud.
                                call sscroll_bought
                                call thx_4_shoping2 #Massage that says "Thank you for shopping here!".
                                jump desk
                            else:
                                call no_gold #Massage: m "I don't have enough gold".
                                hide screen gift
                                jump sscrolls
                        "-Ничего-":
                            hide screen gift
                            jump sscrolls
                
                
                "-Ничего-":
                    jump the_oddities
                    
        "-Священные свитки. Часть II-":
            label sscrolls2:
            menu:

                "-С.16: [scroll_16_name]-" if not sscroll_16:
                    $ the_gift = "03_hp/18_store/31.png" # SACRED SCROLL.
                    show screen gift
                    with d3
                    call sscroll
                    menu:
                        "-Купить свиток (30 золота)-":
                            if gold >= 30:
                                $ gold -=30
                                $ sscroll_16 = True # Turns TRUE if the scroll had been bought.
                                $ renpy.play('sounds/win_04.mp3')   #Not loud.
                                call sscroll_bought
                                call thx_4_shoping2 #Massage that says "Thank you for shopping here!".
                                jump desk
                            else:
                                call no_gold #Massage: m "I don't have enough gold".
                                hide screen gift
                                jump sscrolls2
                        "-Ничего-":
                            hide screen gift
                            jump sscrolls2
                
                "-С.17: [scroll_17_name]-" if not sscroll_17:
                    $ the_gift = "03_hp/18_store/31.png" # SACRED SCROLL.
                    show screen gift
                    with d3
                    call sscroll
                    menu:
                        "-Купить свиток (30 золота)-":
                            if gold >= 30:
                                $ gold -=30
                                $ sscroll_17 = True # Turns TRUE if the scroll had been bought.
                                $ renpy.play('sounds/win_04.mp3')   #Not loud.
                                call sscroll_bought
                                call thx_4_shoping2 #Massage that says "Thank you for shopping here!".
                                jump desk
                            else:
                                call no_gold #Massage: m "I don't have enough gold".
                                hide screen gift
                                jump sscrolls2
                        "-Ничего-":
                            hide screen gift
                            jump sscrolls2
                
                "-С.18: [scroll_18_name]-" if not sscroll_18:
                    $ the_gift = "03_hp/18_store/31.png" # SACRED SCROLL.
                    show screen gift
                    with d3
                    call sscroll
                    menu:
                        "-Купить свиток (30 золота)-":
                            if gold >= 30:
                                $ gold -=30
                                $ sscroll_18 = True # Turns TRUE if the scroll had been bought.
                                $ renpy.play('sounds/win_04.mp3')   #Not loud.
                                call sscroll_bought
                                call thx_4_shoping2 #Massage that says "Thank you for shopping here!".
                                jump desk
                            else:
                                call no_gold #Massage: m "I don't have enough gold".
                                hide screen gift
                                jump sscrolls2
                        "-Ничего-":
                            hide screen gift
                            jump sscrolls2
                            
                "-С.19: [scroll_19_name]-" if not sscroll_19:
                    $ the_gift = "03_hp/18_store/31.png" # SACRED SCROLL.
                    show screen gift
                    with d3
                    call sscroll
                    menu:
                        "-Купить свиток (30 золота)-":
                            if gold >= 30:
                                $ gold -=30
                                $ sscroll_19 = True # Turns TRUE if the scroll had been bought.
                                $ renpy.play('sounds/win_04.mp3')   #Not loud.
                                call sscroll_bought
                                call thx_4_shoping2 #Massage that says "Thank you for shopping here!".
                                jump desk
                            else:
                                call no_gold #Massage: m "I don't have enough gold".
                                hide screen gift
                                jump sscrolls2
                        "-Ничего-":
                            hide screen gift
                            jump sscrolls2
                            
                "-С.20: [scroll_20_name]-" if not sscroll_20:
                    $ the_gift = "03_hp/18_store/31.png" # SACRED SCROLL.
                    show screen gift
                    with d3
                    call sscroll
                    menu:
                        "-Купить свиток (30 золота)-":
                            if gold >= 30:
                                $ gold -=30
                                $ sscroll_20 = True # Turns TRUE if the scroll had been bought.
                                $ renpy.play('sounds/win_04.mp3')   #Not loud.
                                call sscroll_bought
                                call thx_4_shoping2 #Massage that says "Thank you for shopping here!".
                                jump desk
                            else:
                                call no_gold #Massage: m "I don't have enough gold".
                                hide screen gift
                                jump sscrolls2
                        "-Ничего-":
                            hide screen gift
                            jump sscrolls2
                            
                "-С.21: [scroll_21_name]-" if not sscroll_21:
                    $ the_gift = "03_hp/18_store/31.png" # SACRED SCROLL.
                    show screen gift
                    with d3
                    call sscroll
                    menu:
                        "-Купить свиток (30 золота)-":
                            if gold >= 30:
                                $ gold -=30
                                $ sscroll_21 = True # Turns TRUE if the scroll had been bought.
                                $ renpy.play('sounds/win_04.mp3')   #Not loud.
                                call sscroll_bought
                                call thx_4_shoping2 #Massage that says "Thank you for shopping here!".
                                jump desk
                            else:
                                call no_gold #Massage: m "I don't have enough gold".
                                hide screen gift
                                jump sscrolls2
                        "-Ничего-":
                            hide screen gift
                            jump sscrolls2
                            
                "-С.22: [scroll_22_name]-" if not sscroll_22:
                    $ the_gift = "03_hp/18_store/31.png" # SACRED SCROLL.
                    show screen gift
                    with d3
                    call sscroll
                    menu:
                        "-Купить свиток (30 золота)-":
                            if gold >= 30:
                                $ gold -=30
                                $ sscroll_22 = True # Turns TRUE if the scroll had been bought.
                                $ renpy.play('sounds/win_04.mp3')   #Not loud.
                                call sscroll_bought
                                call thx_4_shoping2 #Massage that says "Thank you for shopping here!".
                                jump desk
                            else:
                                call no_gold #Massage: m "I don't have enough gold".
                                hide screen gift
                                jump sscrolls2
                        "-Ничего-":
                            hide screen gift
                            jump sscrolls2
                            
                "-С.23: [scroll_23_name]-" if not sscroll_23:
                    $ the_gift = "03_hp/18_store/31.png" # SACRED SCROLL.
                    show screen gift
                    with d3
                    call sscroll
                    menu:
                        "-Купить свиток (30 золота)-":
                            if gold >= 30:
                                $ gold -=30
                                $ sscroll_23 = True # Turns TRUE if the scroll had been bought.
                                $ renpy.play('sounds/win_04.mp3')   #Not loud.
                                call sscroll_bought
                                call thx_4_shoping2 #Massage that says "Thank you for shopping here!".
                                jump desk
                            else:
                                call no_gold #Massage: m "I don't have enough gold".
                                hide screen gift
                                jump sscrolls2
                        "-Ничего-":
                            hide screen gift
                            jump sscrolls2
                            
                "-С.24: [scroll_24_name]-" if not sscroll_24:
                    $ the_gift = "03_hp/18_store/31.png" # SACRED SCROLL.
                    show screen gift
                    with d3
                    call sscroll
                    menu:
                        "-Купить свиток (30 золота)-":
                            if gold >= 30:
                                $ gold -=30
                                $ sscroll_24 = True # Turns TRUE if the scroll had been bought.
                                $ renpy.play('sounds/win_04.mp3')   #Not loud.
                                call sscroll_bought
                                call thx_4_shoping2 #Massage that says "Thank you for shopping here!".
                                jump desk
                            else:
                                call no_gold #Massage: m "I don't have enough gold".
                                hide screen gift
                                jump sscrolls2
                        "-Ничего-":
                            hide screen gift
                            jump sscrolls2
                            
                "-С.25: [scroll_25_name]-" if not sscroll_25:
                    $ the_gift = "03_hp/18_store/31.png" # SACRED SCROLL.
                    show screen gift
                    with d3
                    call sscroll
                    menu:
                        "-Купить свиток (30 золота)-":
                            if gold >= 30:
                                $ gold -=30
                                $ sscroll_25 = True # Turns TRUE if the scroll had been bought.
                                $ renpy.play('sounds/win_04.mp3')   #Not loud.
                                call sscroll_bought
                                call thx_4_shoping2 #Massage that says "Thank you for shopping here!".
                                jump desk
                            else:
                                call no_gold #Massage: m "I don't have enough gold".
                                hide screen gift
                                jump sscrolls2
                        "-Ничего-":
                            hide screen gift
                            jump sscrolls2
                                
                "-С.26: [scroll_26_name]-" if not sscroll_26:
                    $ the_gift = "03_hp/18_store/31.png" # SACRED SCROLL.
                    show screen gift
                    with d3
                    call sscroll
                    menu:
                        "-Купить свиток (30 золота)-":
                            if gold >= 30:
                                $ gold -=30
                                $ sscroll_26 = True # Turns TRUE if the scroll had been bought.
                                $ renpy.play('sounds/win_04.mp3')   #Not loud.
                                call sscroll_bought
                                call thx_4_shoping2 #Massage that says "Thank you for shopping here!".
                                jump desk
                            else:
                                call no_gold #Massage: m "I don't have enough gold".
                                hide screen gift
                                jump sscrolls2
                        "-Ничего-":
                            hide screen gift
                            jump sscrolls2
                
                "-С.27: [scroll_27_name]-" if not sscroll_27:
                    $ the_gift = "03_hp/18_store/31.png" # SACRED SCROLL.
                    show screen gift
                    with d3
                    call sscroll
                    menu:
                        "-Купить свиток (30 золота)-":
                            if gold >= 30:
                                $ gold -=30
                                $ sscroll_27 = True # Turns TRUE if the scroll had been bought.
                                $ renpy.play('sounds/win_04.mp3')   #Not loud.
                                call sscroll_bought
                                call thx_4_shoping2 #Massage that says "Thank you for shopping here!".
                                jump desk
                            else:
                                call no_gold #Massage: m "I don't have enough gold".
                                hide screen gift
                                jump sscrolls2
                        "-Ничего-":
                            hide screen gift
                            jump sscrolls2
                
                "-С.28: [scroll_28_name]-" if not sscroll_28:
                    $ the_gift = "03_hp/18_store/31.png" # SACRED SCROLL.
                    show screen gift
                    with d3
                    call sscroll
                    menu:
                        "-Купить свиток (30 золота)-":
                            if gold >= 30:
                                $ gold -=30
                                $ sscroll_28 = True # Turns TRUE if the scroll had been bought.
                                $ renpy.play('sounds/win_04.mp3')   #Not loud.
                                call sscroll_bought
                                call thx_4_shoping2 #Massage that says "Thank you for shopping here!".
                                jump desk
                            else:
                                call no_gold #Massage: m "I don't have enough gold".
                                hide screen gift
                                jump sscrolls2
                        "-Ничего-":
                            hide screen gift
                            jump sscrolls2
        
                "-С.29: [scroll_29_name]-" if not sscroll_29:
                    $ the_gift = "03_hp/18_store/31.png" # SACRED SCROLL.
                    show screen gift
                    with d3
                    call sscroll
                    menu:
                        "-Купить свиток (30 золота)-":
                            if gold >= 30:
                                $ gold -=30
                                $ sscroll_29 = True # Turns TRUE if the scroll had been bought.
                                $ renpy.play('sounds/win_04.mp3')   #Not loud.
                                call sscroll_bought
                                call thx_4_shoping2 #Massage that says "Thank you for shopping here!".
                                jump desk
                            else:
                                call no_gold #Massage: m "I don't have enough gold".
                                hide screen gift
                                jump sscrolls2
                        "-Ничего-":
                            hide screen gift
                            jump sscrolls2
                
                "-С.30: [scroll_30_name]-" if not sscroll_30:
                    $ the_gift = "03_hp/18_store/31.png" # SACRED SCROLL.
                    show screen gift
                    with d3
                    call sscroll
                    menu:
                        "-Купить свиток (30 золота)-":
                            if gold >= 30:
                                $ gold -=30
                                $ sscroll_30 = True # Turns TRUE if the scroll had been bought.
                                $ renpy.play('sounds/win_04.mp3')   #Not loud.
                                call sscroll_bought
                                call thx_4_shoping2 #Massage that says "Thank you for shopping here!".
                                jump desk
                            else:
                                call no_gold #Massage: m "I don't have enough gold".
                                hide screen gift
                                jump sscrolls2
                        "-Ничего-":
                            hide screen gift
                            jump sscrolls2





                "-Ничего-":
                    jump the_oddities

        "-Ничего-":
            jump desk
        
        
### ALREADY HAVE THIS BOOK
label do_have_book:
    show screen bld1
    m "У меня уже есть эта книга."
    hide screen bld1
    hide screen gift
    with d3
    return
### THANK YOU FOR shopping here.
label thx_4_shoping:
    $ days_in_delivery2 = one_of_five  #Generating one number out of three for various porpoises.

    if one_of_five ==  1:
        dahr "Спасибо за покупки в \"Приблудах Дахра\". Ваш заказ будет доставлен завтра."
        hide screen gift
        with d3
        return
    else:
        dahr "Спасибо за покупки в \"Приблудах Дахра\". Ваш заказ будет доставлен в течении 1 - [one_of_five] дней."
        hide screen gift
        with d3
        return
    
### THANK YOU FOR shopping here. IMMEDIATE DELIVERY.
label thx_4_shoping2:
    dahr "Спасибо за покупки в \"Приблудах Дахра\"."
    hide screen gift
    with d3
    return
### NOT ENOUGH GOLD ###
label no_gold:
    m "У меня нет столько золота...Это удручает..."
    hide screen gift
    with d3
    return
    
### Этот товар закончился на складе ###

label out:
    dahr "Этот товар закончился на складе"
    return

### SACRED SCROLL MASSAGE ###
label sscroll:
    dahr "Свиток священных знаний.\n(Может содержать спойлеры)."
    return
    
### BOUGHT SACRED SCROLL MESSAGE ###
label sscroll_bought:
    ">Новый свиток был добавлен в вашу коллекцию."
    hide screen gift
    with d3
    return
    
### CHOCOLATE BAR DESCRIPTION ###
label choco_text:
    dahr "Рецепт этого восхитительного молочного шоколада держится в секрете. (По слухам, он содержит сушеных фей)."
    return

### TOY OWL ###
label owl_text:
    dahr "Игрушечная сова, набитая перьями настоящей совы. Она такая мягкая!"
    return
    
### BUTTERBEER ###
label beer_text:
    dahr "Девушки не могут устоять перед этим вкусом. Поэтому всегда пользуются большим спросом среди мальчиков. \n {size=-4}. Предупреждение: употребление алкоголя не допускается несовершеннолетними, без присмотра взрослыми {/size}"
    return
          
### MAGAZINES ###
label mag1_text:
    dahr "Образовательный журнал. \nВерный спутник каждого изгоя."
    return
          
label mag2_text:
    dahr "Женский журнал. \nВсе крутые девченки читают их."
    return
    
label mag3_text:
    dahr "Ваш парень превращается в хорошего мальчика? \nВаш муж больше не использует вас по назначению?\nВсе, что вы ждали об отношениях, любви и сексе. В основном о сексе."
    return
    
label mag4_text:
    dahr "Дайте их к своей девушке, чтобы проверить ее, своей жене, чтобы постыдить ее и вашей дочери, чтобы избежать \"разговоров\"."
    return
    
### CONDOMS ###
label con_text:
    dahr "\"Презервативы Розовый единорог\". \nПокажите всем однорогое существо!\n{size=-4}Может содержать слюну реального единорога.{/size}"
    return
    
### VIBRATOR ###
label vib_text:
    dahr "Великолепный, волшебным усиленный вибратор изготовлен из лозы дерева, с ядром сердечной жилы дракона."
    return
    
### ANAL LUBRICANT ###
label lub_text:
    dahr "Банка анальной смазки. Купите это любимому человеку - покажите, что вы заботитесь о нем/ней."
    return

### BALL GAG AND CUFFS ###
label ball_text:
    dahr "Кляп и манжеты, превратите свою вторую половинку в вашего сокамерника."
    return
          
### ANAL PLUGS ###
label anal_text:
    dahr "Анальные пробки украшены настоящими хвостами. \n Разные размеры, чтобы удовлетворить экспертов, практиков и начинающих."
    return
          
### STRAP-ON ###
label str_text:
    dahr "Cтрапон \"Фестрал\".\nКогда вы его увидите -- потеряете дар речи."
    return

### FISHNETS ###
label nets_text:
    dahr "Ажурные чулки. Вопреки распространенному мнению, они не были изобретены рыбаком."
    return