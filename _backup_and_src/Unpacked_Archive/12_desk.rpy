label desk:
    menu:
        "- Осмотреть -" if not desk_examined:
            $ desk_examined = True
            m "Обычный стол..."
            jump day_main_menu
        "- Делать бумажную работу -" if finished_report < 6 and not got_paycheck and not day == 1 and work_unlock2:
            jump paperwork
        "{color=#858585}- Делать бумажную работу -{/color}" if finished_report >= 6 and not got_paycheck:
            m "Я уже завершил шесть отчетов на этой неделе."
            jump desk
        "{color=#858585}- Делать бумажную работу -{/color}" if got_paycheck: # When TRUE paycheck is in the mail.
            m "Сначала мне нужно получить оплату."
            jump desk
         
        #"- Book collection- {image=book.png}" if not day == 1 and cataloug_found: 
        "- Книжная коллекция -" if not day == 1 and cataloug_found: 
            label books_list:
                menu:
                    "- Обучающие книги -":
                        label books_on_improvement:
                        menu:
                            #"\"Copper book of spirit\""
                            "- Книга: [book01] -" if "book_01" in books and book_01_units <= 9:
                                $ the_gift = "03_hp/18_store/08.png" # Copper book of spirit.
                                show screen gift
                                with d3
                                "\"[book01]\"" "Эта книга содержит различные советы о том, как улучшить свою эффективность. Вы хотите прочитать ее сегодня?"
                                menu:
                                    "- Читать книгу -":
                                        jump reading_book_01
                                    "- Ничего -":
                                        hide screen gift
                                        jump books_on_improvement
                            "- Книга [book01] -{image=check_08.png}" if "book_01" in books and book_01_units == 10:
                                $ the_gift = "03_hp/18_store/08.png" # Copper book of spirit.
                                show screen gift
                                with d3
                                "\"[book01]\"" "Эта книга содержит различные советы о том, как улучшить свою эффективность. Вы хотите прочитать ее сейчас?"
                                m "Я уже закончил ее."
                                m "Она дала мне новый навык: шанс 1 к 6, что я завершу дополнительную главу, во время работы с отчетом. "
                                hide screen gift
                                jump books_on_improvement
                                
                            #"\"Bronze book of spirit\""   
                            "- Книга [book02] -" if "book_02" in books and book_02_units <= 9:
                                $ the_gift = "03_hp/18_store/08.png" # Copper book of spirit.
                                show screen gift
                                with d3
                                ">Эта книга содержит различные советы о том, как улучшить свою эффективность. Вы хотите прочитать ее сейчас?"
                                menu:
                                    "- Читать книгу -":
                                        if "book_01" in books and book_01_units == 10:
                                            jump reading_book_02
                                        else:
                                            call gal_proper
                                            jump books_on_improvement
                                    "- Ничего -":
                                        hide screen gift
                                        jump books_on_improvement
                            "- Книга [book02] -{image=check_08.png}" if "book_02" in books and book_02_units == 10:
                                $ the_gift = "03_hp/18_store/08.png" # Copper book of spirit.
                                show screen gift
                                with d3
                                ">Эта книга содержит различные советы о том, как улучшить свою эффективность."
                                m "Я уже закончил ее."
                                m "Она дала мне новый навык: шанс 1 к 4, что я завершу дополнительную главу, во время работы с отчетом. "
                                hide screen gift
                                jump books_on_improvement
                            
                            #"\"Silver book of spirit\""  
                            "- Книга [book03] -" if "book_03" in books and book_03_units <= 9:
                                $ the_gift = "03_hp/18_store/08.png" # Copper book of spirit.
                                show screen gift
                                with d3
                                ">Эта книга содержит различные советы о том, как улучшить свою эффективность. Вы хотите прочитать ее сегодня?"
                                menu:
                                    "- Читать книгу -":
                                        if "book_02" in books and book_02_units == 10:
                                            jump reading_book_03
                                        else:
                                            call gal_proper
                                            jump books_on_improvement
                                    "- Ничего -":
                                        hide screen gift
                                        jump books_on_improvement
                            "- Книга [book03] -{image=check_08.png}" if "book_03" in books and book_03_units == 10:
                                $ the_gift = "03_hp/18_store/08.png" # Copper book of spirit.
                                show screen gift
                                with d3
                                ">Эта книга содержит различные советы о том, как улучшить свою эффективность."
                                m "Я уже закончил ее."
                                m "Она дала мне новый навык: шанс 1 к 2, что я завершу дополнительную главу, во время работы с отчетом. "
                                hide screen gift
                                jump books_on_improvement
                                
                            #"\"Golden book of spirit\"" 
                            "- Книга [book04] -" if "book_04" in books and book_04_units <= 9:
                                $ the_gift = "03_hp/18_store/08.png" # Copper book of spirit.
                                show screen gift
                                with d3
                                ">Эта книга содержит различные советы о том, как улучшить свою эффективность."
                                menu:
                                    "- Читать книгу -":
                                        if "book_03" in books and book_03_units == 10:
                                            jump reading_book_04
                                        else:
                                            call gal_proper
                                            jump books_on_improvement
                                    "- Ничего -":
                                        hide screen gift
                                        jump books_on_improvement
                            "- Книга [book04] -{image=check_08.png}" if "book_04" in books and book_04_units == 10:
                                $ the_gift = "03_hp/18_store/08.png" # Copper book of spirit.
                                show screen gift
                                with d3
                                ">Эта книга содержит различные советы о том, как улучшить свою эффективность."
                                m "Я уже закончил ее."
                                g4 "Я обуздал свой дух!"
                                g9 "Мой дух - моя сучка!"
                                #m "It taught me a new skill: a decent chance of completing an additional chapter when doing paperwork."
                                hide screen gift
                                jump books_on_improvement
                            
                            #"\"Platinum book of spirit\""
                            "- Книга [book10] -" if "book_10" in books and book_10_units <= 9:
                                $ the_gift = "03_hp/18_store/08.png" # Copper book of spirit.
                                show screen gift
                                with d3
                                ">Эта книга содержит различные советы о том, как улучшить свою эффективность."
                                menu:
                                    "- Читать книгу -":
                                        if "book_04" in books and book_04_units == 10:
                                            jump reading_book_10
                                        else:
                                            call gal_proper
                                            jump books_on_improvement
                                    "- Ничего -":
                                        hide screen gift
                                        jump books_on_improvement
                            "- Книга [book10] -{image=check_08.png}" if "book_10" in books and book_10_units == 10:
                                $ the_gift = "03_hp/18_store/08.png" # Copper book of spirit.
                                show screen gift
                                with d3
                                ">Эта книга содержит различные советы о том, как улучшить свою эффективность."
                                m "Я уже закончил ее."
                                m "Она дала мне новый навык: большой шанс, что я завершу дополнительную главу, во время работы с отчетом. "
                                hide screen gift
                                jump books_on_improvement
                                
                            #"\"Adamantium book of spirit\""
                            "- Книга [book11] -" if "book_11" in books and book_11_units <= 9:
                                $ the_gift = "03_hp/18_store/08.png" # Copper book of spirit.
                                show screen gift
                                with d3
                                ">Эта книга содержит различные советы о том, как улучшить свою эффективность."
                                menu:
                                    "- Читать книгу -":
                                        if "book_10" in books and book_10_units == 10:
                                            jump reading_book_11
                                        else:
                                            call gal_proper
                                            jump books_on_improvement
                                    "- Ничего -":
                                        hide screen gift
                                        jump books_on_improvement
                            "- Книга [book11] -{image=check_08.png}" if "book_11" in books and book_11_units == 10:
                                $ the_gift = "03_hp/18_store/08.png" # Copper book of spirit.
                                show screen gift
                                with d3
                                ">Эта книга содержит различные советы о том, как улучшить свою эффективность."
                                m "Я уже закончил ее."
                                m "Я полностью контролирую свой дух. Отныне я буду всегда делать дополнительную главу."
                                g9 "Мой дух - моя сучка."
                                hide screen gift
                                jump books_on_improvement
                            
                            #"\"Speedwriting for dummies\""
                            "- Книга [book12] -" if "book_12" in books and book_12_units <= 9:
                                $ the_gift = "03_hp/18_store/08.png" # Copper book of spirit.
                                show screen gift
                                with d3
                                ">Эта книга содержит несколько элементарных принципов, позволяющих улучшить скорость моего умение писать."
                                menu:
                                    "- Читать книгу -":
                                        jump reading_book_12
                                    "- Ничего -":
                                        hide screen gift
                                        jump books_on_improvement
                            "- Книга [book12] -{image=check_08.png}" if "book_12" in books and book_12_units == 10:
                                $ the_gift = "03_hp/18_store/08.png" # Copper book of spirit.
                                show screen gift
                                with d3
                                ">Эта книга содержит различные советы о том, как улучшить свою эффективность."
                                m "Я уже закончил ее."
                                m "Она дала мне новый навык: шанс 1 к 6, что я завершу дополнительную главу, во время работы с отчетом. "
                                hide screen gift
                                jump books_on_improvement
                                
                            #"\"Speedwriting for beginners\""
                            "- Книга [book13] -" if "book_13" in books and book_13_units <= 9:
                                $ the_gift = "03_hp/18_store/08.png" # Copper book of spirit.
                                show screen gift
                                with d3
                                ">Эта книга содержит несколько элементарных принципов, позволяющих улучшить скорость моего умение писать."
                                menu:
                                    "- Читать книгу -":
                                         if "book_12" in books and book_12_units == 10:
                                            jump reading_book_13
                                         else:
                                            call gal_proper
                                            jump books_on_improvement
                                    "- Ничего -":
                                        hide screen gift
                                        jump books_on_improvement
                            "- Книга [book13] -{image=check_08.png}" if "book_13" in books and book_13_units == 10:
                                $ the_gift = "03_hp/18_store/08.png" # Copper book of spirit.
                                show screen gift
                                with d3
                                ">Эта книга содержит различные советы о том, как улучшить свою эффективность."
                                m "Я уже закончил ее."
                                m "Она дала мне новый навык: шанс 1 к 4, что я завершу дополнительную главу, во время работы с отчетом. "
                                hide screen gift
                                jump books_on_improvement
                        
                            #"\"Speedwriting for amateurs\""
                            "- Книга [book14] -" if "book_14" in books and book_14_units <= 9:
                                $ the_gift = "03_hp/18_store/08.png" # Copper book of spirit.
                                show screen gift
                                with d3
                                ">Эта книга содержит несколько любительских методов, позволяющих улучшить скорость моего умение писать."
                                menu:
                                    "- Читать книгу -":
                                        if "book_13" in books and book_13_units == 10:
                                            jump reading_book_14
                                        else:
                                            call gal_proper
                                            jump books_on_improvement
                                    "- Ничего -":
                                        hide screen gift
                                        jump books_on_improvement
                            "- Книга [book14] -{image=check_08.png}" if "book_14" in books and book_14_units == 10:
                                $ the_gift = "03_hp/18_store/08.png" # Copper book of spirit.
                                show screen gift
                                with d3
                                ">Эта книга содержит различные советы о том, как улучшить свою эффективность."
                                m "Я уже закончил ее."
                                m "Она дала мне новый навык: шанс 1 к 2, что я завершу дополнительную главу, во время работы с отчетом."
                                hide screen gift
                                jump books_on_improvement
                                
                            #"\"Speedwriting for advanced writers\""
                            "- Книга [book15] -" if "book_15" in books and book_15_units <= 9:
                                $ the_gift = "03_hp/18_store/08.png" # Copper book of spirit.
                                show screen gift
                                with d3
                                ">Эта книга содержит несколько расширенных методов, позволяющих улучшить скорость моего умение писать."
                                menu:
                                    "- Читать книгу -":
                                        if "book_14" in books and book_14_units == 10:
                                            jump reading_book_15
                                        else:
                                            call gal_proper
                                            jump books_on_improvement
                                    "- Ничего -":
                                        hide screen gift
                                        jump books_on_improvement
                            "- Книга [book15] -{image=check_08.png}" if "book_15" in books and book_15_units == 10:
                                $ the_gift = "03_hp/18_store/08.png" # Copper book of spirit.
                                show screen gift
                                with d3
                                ">Эта книга содержит различные советы о том, как улучшить свою эффективность."
                                m "Я уже закончил ее."
                                m "Теперь я настоящий мастер скорописания..."

                                
                                #m "It taught me a new skill: a decent chance of completing an additional chapter when doing paperwork."
                                hide screen gift
                                jump books_on_improvement
                                
                            #"\"Speedwriting for experts.\""
                            "- Книга [book16] -" if "book_16" in books and book_16_units <= 9:
                                $ the_gift = "03_hp/18_store/08.png" # Copper book of spirit.
                                show screen gift
                                with d3
                                ">Эта книга содержит несколько продвинутых принципов, позволяющих улучшить скорость моего умение писать."
                                menu:
                                    "- Читать книгу -":
                                        if "book_15" in books and book_15_units == 10:
                                            jump reading_book_16
                                        else:
                                            call gal_proper
                                            jump books_on_improvement
                                    "- Ничего -":
                                        hide screen gift
                                        jump books_on_improvement
                            "- Книга [book16] -{image=check_08.png}" if "book_16" in books and book_16_units == 10:
                                $ the_gift = "03_hp/18_store/08.png" # Copper book of spirit.
                                show screen gift
                                with d3
                                ">Эта книга содержит различные советы о том, как улучшить свою эффективность."
                                m "Я уже закончил ее."
                                m "Она дала мне новый навык: большой шанс, что я завершу дополнительную главу, во время работы с отчетом."
                                hide screen gift
                                jump books_on_improvement
                            
                            #"\"Speedwriting for maniacs.\""
                            "- Книга [book17] -" if "book_17" in books and book_17_units <= 9:
                                $ the_gift = "03_hp/18_store/08.png" # Copper book of spirit.
                                show screen gift
                                with d3
                                ">Эта книга содержит методы, которые позволяют вам полностью овладеть искусством скорописания."
                                #">This book contains techniques for those obsessed with writing quickly."
                                menu:
                                    "- Читать книгу -":
                                        if "book_16" in books and book_16_units == 10:
                                            jump reading_book_17
                                        else:
                                            call gal_proper
                                            jump books_on_improvement
                                    "- Ничего -":
                                        hide screen gift
                                        jump books_on_improvement
                            "- Книга [book17] -{image=check_08.png}" if "book_17" in books and book_17_units == 10:
                                $ the_gift = "03_hp/18_store/08.png" # Copper book of spirit.
                                show screen gift
                                with d3
                                ">Эта книга содержит различные советы о том, как улучшить свою эффективность."
                                m "Я уже закончил ее."
                                m "Я стал настоящим мастером скорописания и теперь всегда буду делать дополнительную главу, когда пишу отчет."
                                hide screen gift
                                jump books_on_improvement
                                
                                
                            ###08 "SPEED READING FOR DUMMIES" #1/4 chance to complete an extra chapter during reading.   
                            "- Книга [book08] -" if "book_08" in books and book_08_units <= 9:
                                $ the_gift = "03_hp/18_store/08.png" # Copper book of spirit.
                                show screen gift
                                with d3
                                "\"[book08]\"" ">Эта книга содержит начальные методы, используемые для улучшения способностей к скорочтению."
                                menu:
                                    "- Читать книгу -":
                                        jump reading_book_08
                                    "- Ничего -":
                                        hide screen gift
                                        jump books_on_improvement
                            "- Книга [book08] -{image=check_08.png}" if "book_08" in books and book_08_units == 10:
                                $ the_gift = "03_hp/18_store/08.png" # Copper book of spirit.
                                show screen gift
                                with d3
                                "\"[book08]\"" ">Эта книга содержит начальные методы, используемые для улучшения способностей к скорочтению."
                                m "Я уже завершил ее."
                                m "Она дала мне способность: большой шанс прочесть дополнительную главу, во время чтения."
                                hide screen gift
                                jump books_on_improvement
                                
                            ###09 "SPEED READING FOR EXPERTS" #1/2 chance to complete an extra chapter during reading.   
                            "- Книга [book09] -" if "book_09" in books and book_09_units <= 9:
                                $ the_gift = "03_hp/18_store/08.png" # Copper book of spirit.
                                show screen gift
                                with d3
                                "\"[book09]\"" "Эта книга содержит продвинутые методы, используемые для улучшения способности  к скорочтению."
                                menu:
                                    "- Читать книгу -":
                                        if "book_08" in books and book_08_units == 10:
                                            jump reading_book_09
                                        else:
                                            call gal_proper
                                            jump books_on_improvement
                                    "- Ничего -":
                                        hide screen gift
                                        jump books_on_improvement
                            "- Книга [book09] -{image=check_08.png}" if "book_09" in books and book_09_units == 10:
                                $ the_gift = "03_hp/18_store/08.png" # Copper book of spirit.
                                show screen gift
                                with d3
                                "\"[book09]\"" "Эта книга содержит продвинутые методы, используемые для улучшения способности  к скорочтению."
                                m "Я уже закончил ее."
                                m "Она дала мне способность: большой шанс освоить дополнительную главу, во время чтения."
                                hide screen gift
                                jump books_on_improvement
                            "- Ничего -":
                                jump books_list
                    "- Фантастика -":#FICTION==============================================================================
                        label fiction_books:
                        menu:
                            ###05"\"The Tale of Galadriel\""    
                            "- Книга [book05] -" if "book_05" in books and book_05_units <= 19:
                                $ the_gift = "03_hp/18_store/04.png" # THE TALE OF GALADRIEL. BOOK ONE.
                                show screen gift
                                ">Эта книга содержит довольно длинную историю, описывающую в мельчайших подробностях жизнь и приключения молодой эльфийки по имени Галадриэль."
                                with d3
                                menu:
                                    "- Читать книгу -":
                                        hide screen gift
                                        jump reading_book_05
                                    "- Ничего -":
                                        hide screen gift
                                        jump  fiction_books
                            "- Книга [book05] -{image=check_08.png}" if "book_05" in books and book_05_units == 20:
                                $ the_gift = "03_hp/18_store/04.png" # THE TALE OF GALADRIEL. BOOK ONE.
                                show screen gift
                                ">Эта книга содержит довольно длинную историю, описывающую в мельчайших подробностях жизнь и приключения молодой эльфийки по имени Галадриэль."
                                ">Вы уже закончили эту книгу."
                                hide screen gift
                                jump  fiction_books
                            
                            ###05_b"\"The Tale of Galadriel. BOOK TWO.\""    
                            "- Книга [book05b] -" if "book_05_b" in books and book_05_b_units <= 19:
                                $ the_gift = "03_hp/18_store/05.png" # THE TALE OF GALADRIEL. BOOK TWO.
                                show screen gift
                                ">Эта книга содержит довольно длинную историю, описывающую в мельчайших подробностях жизнь и приключения молодой эльфийки по имени Галадриэль."
                                with d3
                                menu:
                                    "- Читать книгу -":
                                        if "book_05" in books and book_05_units == 20: # MAKES SURE YOU DON'T READ PART II BEFORE PART I.
                                            hide screen gift
                                            jump reading_book_05_b      
                                        else:
                                            call gal_proper
                                            jump  fiction_books
                                            
                                    "- Ничего -":
                                        hide screen gift
                                        jump  fiction_books
                            "- Книга [book05b] -{image=check_08.png}" if "book_05_b" in books and book_05_b_units == 20:
                                $ the_gift = "03_hp/18_store/05.png" # THE TALE OF GALADRIEL. BOOK TWO.
                                show screen gift
                                ">Эта книга содержит довольно длинную историю, описывающую в мельчайших подробностях жизнь и приключения молодой эльфийки по имени Галадриэль."
                                ">Вы уже закончили эту книгу."
                                hide screen gift
                                jump  fiction_books
                                
                            ###06"\"The game of chairs\""    
                            "- Книга [book06] -" if "book_06" in books and book_06_units <= 19:
                                $ the_gift = "03_hp/18_store/02.png" # GAME OF THRONES.
                                show screen gift
                                with d3
                                "[book06]\nЭпический рассказ о предательстве, убийствах и изнасилованиях, а затем еще несколько убийств, немного больше предательства и еще больше изнасилований."
                                menu:
                                    "- Читать книгу -":
                                        hide screen gift
                                        jump reading_book_06
                                    "- Ничего -":
                                        hide screen gift
                                        jump fiction_books
                            "- Книга [book06] -{image=check_08.png}" if "book_06" in books and book_06_units == 20:
                                "[book06]\nЭпический рассказ о предательстве, убийствах и изнасилованиях, а затем еще несколько убийств, немного больше предательства и еще больше изнасилований."
                                m "Почему мне нужно снова читать это?"
                                jump fiction_books
                                
                            ###07"\"My dear waifu\""
                            "- Книга [book07] -" if "book_07" in books and book_07_units <= 19 and not waifu_book_completed:
                                $ the_gift = "03_hp/18_store/03.png" # MY DEAR WAIFU.
                                show screen gift
                                with d3
                                "\"[book07]\" {size=-4}От Акабура{/size}" "Переживите славные дни в вашей школе. Ваша сводная сестра Ши, учитель Мисс Стивенс или таинственная девушка из библиотеки? Кто станет вашей окончательной \"вайфу\"?"
                                menu:
                                    "- Читать книгу -":
                                        if dear_waifu_completed_once and book_07_units == 0:
                                            m "Я не думаю, что повторное чтение этой книги даст мне хоть что-то. Прочесть ее просто ради удовольствия?"
                                            menu:
                                                "- Читать книгу again -":
                                                    hide screen gift
                                                    jump reading_book_07
                                                "- Ничего -":
                                                    hide screen gift
                                                    jump fiction_books
                                        else:
                                            hide screen gift
                                            jump reading_book_07
                                    "- Ничего -":
                                        hide screen gift
                                        jump fiction_books
                            "- Книга [book07] -{image=check_08.png}" if "book_07" in books and waifu_book_completed:
                                $ the_gift = "03_hp/18_store/03.png" # MY DEAR WAIFU.
                                show screen gift
                                with d3
                                "\"[book07]\" {size=-4}От Акабура{/size}" "Переживите славные дни в вашей школе. Ваша сводная сестра Ши, учитель Мисс Стивенс или таинственная девушка из библиотеки? Кто станет вашей окончательной \"вайфу\"?"
                                menu:
                                    "- Читать книгу -":
                                        if dear_waifu_completed_once and book_07_units == 0:
                                            m "Я не думаю, что повторное чтение этой книги даст мне хоть что-то."
                                            hide screen gift
                                            jump fiction_books
                                    "- Ничего -":
                                        hide screen gift
                                        jump fiction_books
                                
                            "- Ничего -":
                                jump books_list
                    "- Ничего -":
                        jump desk
            
          
                    
                        
                    
        
                    
                    
                    
        #"- The muggle oddities -" if have_catalogue: #Real thing
        "- Приблуды Дахра -" if cataloug_found: 
            if order_placed or package_is_here:
                show screen bld1
                with d3
                dahr "Пожалуйста, потерпи чуть-чуть. Сова уже в пути."
                hide screen bld1
                with d3
                jump desk
            else:
                 jump the_oddities
        
        
        

        "- Подрочить на трусики Гермионы -" if request_03: #True when Hermione has no panties on.
            jump jerk_off
        "- Состояние Гермионы -" if summoning_hermione_unlocked and buying_favors_from_hermione_unlocked: 
            "> Распутство: {color=#B40000}{size=+4}{b}[whoring]{/b}{/size}{/color}-я степень."
            "> Злость: {color=#B40000}{size=+4}{b}[mad]{/b}{/size}{/color}-я степень"
            if mad >=1 and mad < 3:
                "> Гермиона по-прежнему {b}немного расстроена{/b} вами..."
            elif mad >=3 and mad < 10:
                "> Вы {b}расстроили{/b} Гермиону."
            elif mad >=10 and mad < 20:
                "> Гермиона {b}очень расстроена{/b} вами."
            elif mad >=20 and mad < 40:
                "> Гермиона {b}злится{/b} на вас."
            elif mad >=40 and mad < 50:
                "> Гермиона {b}очень злится{/b} на вас."
            elif mad >=50 and mad < 60:
                "> Гермиона {b}в гневе{/b} на вас."
            elif mad >=60:
                "> Гермиона {b}ненавидит{/b} вас."
            else:
                "> Гермиона {b}не злится{/b} на вас"
            jump desk
        "- Дремать -" if daytime and not day == 1:
            jump night_start
        "- Спать -" if not daytime and not day == 1:
            jump day_start
            

        "- Ничего -":
            call screen main_menu_01
            
            

        
  
            
            


    
### READING ###

######################################
### BOOK 01 ########################## "\"Copper book of spirit\"" #1/8 (small) chance of it to pop up. Completes extra chapter during work.
######################################
label reading_book_01:
    
    call reading_block
    
    hide screen gift
    with d3
    if fire_in_fireplace:
        call fire_in #Shows Genie reading a book near the fireplace.
    else:
        call fire_out #Shows Genie reading a book near the window.

    if raining:
        ">Вы читаете книгу под названием [book01], в тоже время слушая дождь, заливающий крышу вашей башни."
    else:
        ">Вы читаете книгу под названием [book01]."
   
    call chap_finished
    
    call chapter_check_book_01 #Checks if the chapter just finished was the last one.
            
    ">Осталось еще несколько глав."
    
#===### SPEED READING FOR DUMMIES BONUS CHECK ###
    if s_reading_lvl == 1: #First book (book_08) on speed reading completed.
        $ speed_dummies = renpy.random.randint(1, 6) 
        #$ speed_dummies = 1 #Here for testing porpoise only.
        if speed_dummies == 1: #Success.
            call yes_book_08 #Message you see that says you are completed one more chapter because of the "Speed reading for dummies" book.
            call chap_finished
            call chapter_check_book_01 #Checks if the chapter just finished was the last one.
            ">Осталось еще несколько глав."
            
    if s_reading_lvl == 2: #Second book(book_09) on speed reading completed.
        $ speed_dummies = renpy.random.randint(1, 3) 
        #$ speed_dummies = 1 #Here for testing porpoise only.
        if speed_dummies == 1: #Success.
            call yes_book_09 #Message you see that says you are completed one more chapter because of the "Speed reading for dummies" book.
            call chap_finished
            call chapter_check_book_01 #Checks if the chapter just finished was the last one.
            ">Осталось еще несколько глав."

#===#############################################


    if raining:
        if not fire_in_fireplace:
            call no_fire #Message you see that says you are reading a book during rain.
        else:
            call yes_fire #Message you see that says you are reading a book during rain near fireplace.
            call chap_finished
            call chapter_check_book_01 #Checks if the chapter just finished was the last one.
            ">Осталось еще несколько глав."

    if fire_in_fireplace:
        hide screen reading_near_fire
    else:
        hide screen reading

    if daytime:
        jump night_start
    else: 
        jump day_start
        
######    
label chap_finished: 
    $ book_01_units +=1 
    $ renpy.play('sounds/win_04.mp3')   #Not loud.
    hide screen notes
    show screen notes
    ">Вы закончили \"главу [book_01_units]\" этой книги."
    return
###
label no_fire: #Message you see that says you are reading a book during rain.
    ">Дождь за окном успокаивает вас и вы отлично себя чувствуете за чтением этой книги..."
    ">Вы пытаетесь продолжить читать, но через некоторое время понимаете, что воздух в комнате слишком влажный."
    return
###
label yes_fire: #Message you see that says you are reading a book during rain near fireplace.
    ">Дождь за окном успокаивает вас и вы отлично себя чувствуете за чтением этой книги..."
    return

###
label yes_book_08:
    ">Используя некоторые хитрости при чтении [book08] вы более рационально используете время и продолжаете читать."
    return
label yes_book_09:
    ">Используя некоторые методы скорочтения вы экономите время при чтении книги."
    return
###
label fire_in: #Shows Genie reading a book near the fireplace.
    hide screen chair
    hide screen genie
    show screen reading_near_fire
    with Dissolve(0.3)
    return
###
label fire_out: #Shows Genie reading a book near the window.
    hide screen chair
    hide screen genie
    show screen reading
    with Dissolve(0.3)
    return

###
label chapter_check_book_01: #Checks if the chapter just finished was the last one.
    if book_01_units == 10:
        if fire_in_fireplace:
            show screen done_reading_02  
            hide screen reading_near_fire
        else:
            show screen done_reading  
            hide screen reading

       
        $ renpy.play('sounds/win_04.mp3')   #Not loud.
        hide screen notes
        show screen notes
        ">Это была последняя глава, вы закончили книгу."
        ">Новое умение разблокировано: шанс 1 к 6 завершить дополнительную главу, когда пишите отчет..."

        $ concentration += 1
        $ book_01_complete = True
        
        if fire_in_fireplace:
            hide screen reading_near_fire
        else:
            hide screen reading
        
        if daytime:
            jump night_start
        else: 
            jump day_start
    else:
        return
    
    
######################################
### BOOK 02 ########################## "\"Bronze book of spirit\""
######################################
label reading_book_02:
    
    call reading_block
    
    hide screen gift
    with d3
    if fire_in_fireplace:
        call fire_in #Shows Genie reading a book near the fireplace.
    else:
        call fire_out #Shows Genie reading a book near the window.

    if raining:
        ">Вы читаете книгу под названием [book02], в тоже время слушая дождь, заливающий крышу вашей башни."
    else:
        ">Вы читаете книгу под названием [book02]..."
   
    call chap_finished_02
    
    call chapter_check_book_02 #Checks if the chapter just finished was the last one.
            
    ">Осталось еще несколько глав."
    
#===### SPEED READING FOR DUMMIES BONUS CHECK ###
    if s_reading_lvl == 1: #First book (book_08) on speed reading completed.
        $ speed_dummies = renpy.random.randint(1, 6) 
        #$ speed_dummies = 1 #Here for testing porpoise only.
        if speed_dummies == 1: #Success.
            call yes_book_08 #Message you see that says you are completed one more chapter because of the "Speed reading for dummies" book.
            call chap_finished_02
            call chapter_check_book_02 #Checks if the chapter just finished was the last one.
            ">Осталось еще несколько глав."
    
    if s_reading_lvl == 2: #Second book(book_09) on speed reading completed.
        $ speed_dummies = renpy.random.randint(1, 3) 
        #$ speed_dummies = 1 #Here for testing porpoise only.
        if speed_dummies == 1: #Success.
            call yes_book_09 #Message you see that says you are completed one more chapter because of the "Speed reading for dummies" book.
            call chap_finished_02
            call chapter_check_book_02 #Checks if the chapter just finished was the last one.
            ">Осталось еще несколько глав."
#===#############################################

    if raining:
        if not fire_in_fireplace:
            call no_fire #Message you see that says you are reading a book during rain.
        else:
            call yes_fire #Message you see that says you are reading a book during rain near fireplace.
            call chap_finished_02
            call chapter_check_book_02 #Checks if the chapter just finished was the last one.
            ">Осталось еще несколько глав."
    

    if fire_in_fireplace:
        hide screen reading_near_fire
    else:
        hide screen reading

    if daytime:
        jump night_start
    else: 
        jump day_start
        
######    
label chap_finished_02: 
    $ book_02_units +=1 
    $ renpy.play('sounds/win_04.mp3')   #Not loud.
    show screen notes
    ">Вы закончили \"главу [book_02_units]\" этой книги."
    return
    
###
label chapter_check_book_02: #Checks if the chapter just finished was the last one.
    if book_02_units == 10:
        if fire_in_fireplace:
            show screen done_reading_02  
            hide screen reading_near_fire
        else:
            show screen done_reading  
            hide screen reading

        $ renpy.play('sounds/win_04.mp3')   #Not loud.
        hide screen notes
        show screen notes
        ">Это была последняя глава. Вы закончили эту книгу."
        ">Новое умение разблокировано: шанс 1 к 4 завершить дополнительную главу, когда пишите отчет..."

        $ concentration += 1
        $ book_02_complete = True
        
        if fire_in_fireplace:
            hide screen reading_near_fire
        else:
            hide screen reading
        
        if daytime:
            jump night_start
        else: 
            jump day_start
    else:
        return    
    
    
######################################
### BOOK 03 ########################## "\"Silver book of spirit\""
######################################
label reading_book_03:
    
    call reading_block
    
    hide screen gift
    
    if fire_in_fireplace:
        call fire_in #Shows Genie reading a book near the fireplace.
    else:
        call fire_out #Shows Genie reading a book near the window.

    if raining:
        ">Вы читаете книгу под названием [book03], в тоже время слушая дождь, заливающий крышу вашей башни."
    else:
        ">Вы читаете книгу под названием [book03]..."
   
    call chap_finished_03
    
    call chapter_check_book_03 #Checks if the chapter just finished was the last one.
            
    ">Осталось еще несколько глав."
    
#===### SPEED READING FOR DUMMIES BONUS CHECK ###
    if s_reading_lvl == 1: #First book (book_08) on speed reading completed.
        $ speed_dummies = renpy.random.randint(1, 6) 
        #$ speed_dummies = 1 #Here for testing porpoise only.
        if speed_dummies == 1: #Success.
            call yes_book_08 #DON'T CHANGE! KEEP IT 08. Message you see that says you are completed one more chapter because of the "Speed reading for dummies" book.
            call chap_finished_03
            call chapter_check_book_03 #Checks if the chapter just finished was the last one.
            ">Осталось еще несколько глав."
    
    if s_reading_lvl == 2: #Second book(book_09) on speed reading completed.
        $ speed_dummies = renpy.random.randint(1, 3) 
        #$ speed_dummies = 1 #Here for testing porpoise only.
        if speed_dummies == 1: #Success.
            call yes_book_09 #DON'T CHANGE! KEEP IT 09 Message you see that says you are completed one more chapter because of the "Speed reading for dummies" book.
            call chap_finished_03
            call chapter_check_book_03 #Checks if the chapter just finished was the last one.
            ">Осталось еще несколько глав."
#===#############################################

    if raining:
        if not fire_in_fireplace:
            call no_fire #Message you see that says you are reading a book during rain.
        else:
            call yes_fire #Message you see that says you are reading a book during rain near fireplace.
            call chap_finished_03
            call chapter_check_book_03 #Checks if the chapter just finished was the last one.
            ">Осталось еще несколько глав."
    

    if fire_in_fireplace:
        hide screen reading_near_fire
    else:
        hide screen reading

    if daytime:
        jump night_start
    else: 
        jump day_start
        
######    
label chap_finished_03: 
    $ book_03_units +=1 
    $ renpy.play('sounds/win_04.mp3')   #Not loud.
    show screen notes
    ">Вы закончили \"главу [book_03_units]\" этой книги."
    return
    
###
label chapter_check_book_03: #Checks if the chapter just finished was the last one.
    if book_03_units == 10:
        if fire_in_fireplace:
            show screen done_reading_02
            hide screen reading_near_fire
        else:
            show screen done_reading  
            hide screen reading

        $ renpy.play('sounds/win_04.mp3')   #Not loud.
        hide screen notes
        show screen notes
        ">Это была последняя глава. Вы закончили эту книгу."
        ">Новое умение разблокировано: шанс 1 к 2 завершить дополнительную главу, когда пишите отчет..."

        $ concentration += 1
        $ book_03_complete = True
        
        if fire_in_fireplace:
            hide screen reading_near_fire
        else:
            hide screen reading
        
        if daytime:
            jump night_start
        else: 
            jump day_start
    else:
        return    
 
######################################
### BOOK 04 ########################## "\"Golden book of spirit\""
######################################
label reading_book_04:
    
    call reading_block
    
    hide screen gift
    if fire_in_fireplace:
        call fire_in #Shows Genie reading a book near the fireplace.
    else:
        call fire_out #Shows Genie reading a book near the window.

    if raining:
        ">Вы читаете книгу под названием [book03], в тоже время слушая дождь, заливающий крышу вашей башни."
    else:
        ">Вы читаете книгу под названием [book03]..."
   
    call chap_finished_04
    
    call chapter_check_book_04 #Checks if the chapter just finished was the last one.
            
    ">Осталось еще несколько глав."
    
#===### SPEED READING FOR DUMMIES BONUS CHECK ###
    if s_reading_lvl == 1: #First book (book_08) on speed reading completed.
        $ speed_dummies = renpy.random.randint(1, 6) 
        #$ speed_dummies = 1 #Here for testing porpoise only.
        if speed_dummies == 1: #Success.
            call yes_book_08 #DON'T CHANGE! KEEP IT 08. Message you see that says you are completed one more chapter because of the "Speed reading for dummies" book.
            call chap_finished_04
            call chapter_check_book_04 #Checks if the chapter just finished was the last one.
            ">Осталось еще несколько глав."
    
    if s_reading_lvl == 2: #Second book(book_09) on speed reading completed.
        $ speed_dummies = renpy.random.randint(1, 3) 
        #$ speed_dummies = 1 #Here for testing porpoise only.
        if speed_dummies == 1: #Success.
            call yes_book_09 #DON'T CHANGE! KEEP IT 09 Message you see that says you are completed one more chapter because of the "Speed reading for dummies" book.
            call chap_finished_04
            call chapter_check_book_04 #Checks if the chapter just finished was the last one.
            ">Осталось еще несколько глав."
#===#############################################

    if raining:
        if not fire_in_fireplace:
            call no_fire #Message you see that says you are reading a book during rain.
        else:
            call yes_fire #Message you see that says you are reading a book during rain near fireplace.
            call chap_finished_04
            call chapter_check_book_04 #Checks if the chapter just finished was the last one.
            ">Осталось еще несколько глав."
    

    if fire_in_fireplace:
        hide screen reading_near_fire
    else:
        hide screen reading

    if daytime:
        jump night_start
    else: 
        jump day_start
        
######    
label chap_finished_04: 
    $ book_04_units +=1 
    $ renpy.play('sounds/win_04.mp3')   #Not loud.
    show screen notes
    ">Вы закончили \"главу [book_04_units]\" этой книги."
    return
    
###
label chapter_check_book_04: #Checks if the chapter just finished was the last one.
    if book_04_units == 10:
        if fire_in_fireplace:
            show screen done_reading_02
            hide screen reading_near_fire
        else:
            show screen done_reading  
            hide screen reading

        $ renpy.play('sounds/win_04.mp3')   #Not loud.
        hide screen notes
        show screen notes
        ">Это была последняя глава. Вы закончили книгу."
        #">New skill unlocked: a sure chance of completing an additional chapter when doing paperwork."
        ">Вы полностью контролируете свой дух и отныне всегда завершаете дополнительную главу, во время написания отчета."


        $ concentration += 1
        $ book_04_complete = True
        
        if fire_in_fireplace:
            hide screen reading_near_fire
        else:
            hide screen reading
        
        if daytime:
            jump night_start
        else: 
            jump day_start
    else:
        return    
        
    
 
 
    
######################################
### BOOK 05 ##########################
######################################
label reading_book_05:
    stop music fadeout 2.0
    if fire_in_fireplace:
        play bg_sounds "sounds/fire02.mp3" fadeout 1.0 fadein 1.0 #Quiet...
        call fire_in #Shows Genie reading a book near the fireplace.
    else:
        call fire_out #Shows Genie reading a book near the window.

    if daytime and not raining and not fire_in_fireplace:
        play bg_sounds "sounds/day.mp3" fadeout 1.0 fadein 1.0 #Quiet...
    
    if not daytime and not raining and not fire_in_fireplace:
        play bg_sounds "sounds/night.mp3" fadeout 1.0 fadein 1.0 #Quiet...


    if raining:
        play weather "sounds/rain.mp3" fadeout 1.0 fadein 1.0 #Quiet...
        ">Вы читаете книгу под названием [book05], в тоже время слушая дождь, заливающий крышу вашей башни."
    else:
        ">Вы читаете книгу под названием [book05]..."
   
    call chap_finished_05
    
    call chapter_check_book_05 #Checks if the chapter just finished was the last one.
    
    ">Осталось еще несколько глав."
    
#===### SPEED READING FOR DUMMIES BONUS CHECK ###
    if s_reading_lvl == 1: #First book (book_08) on speed reading completed.
        $ speed_dummies = renpy.random.randint(1, 3) 
        #$ speed_dummies = 1 #Here for testing porpoise only.
        if speed_dummies == 1: #Success.
            call yes_book_08 #Message you see that says you are completed one more chapter because of the "Speed reading for dummies" book.
            call chap_finished_05
            call chapter_check_book_05 #Checks if the chapter just finished was the last one.
            ">Осталось еще несколько глав."
    if s_reading_lvl == 2: #Second book(book_09) on speed reading completed.
        $ speed_dummies = renpy.random.randint(1, 2) 
        #$ speed_dummies = 1 #Here for testing porpoise only.
        if speed_dummies == 1: #Success.
            call yes_book_09 #Message you see that says you are completed both speed reading books.
            call chap_finished_05
            call chapter_check_book_05 #Checks if the chapter just finished was the last one.
            ">Осталось еще несколько глав."
#===#############################################    
    
    if raining:
        if not fire_in_fireplace:
            call no_fire #Message you see that says you are reading a book during rain.
        else:
            call yes_fire #Message you see that says you are reading a book during rain near fireplace.
            call chap_finished_05
            call chapter_check_book_05 #Checks if the chapter just finished was the last one.
            ">Осталось еще несколько глав."

    if fire_in_fireplace:
        hide screen reading_near_fire
        stop bg_sounds #"sounds/fire02.mp3" fadeout 1.0 fadein 1.0 #Quiet...
    else:
        hide screen reading

    if daytime:
        jump night_start
    else: 
        jump day_start
        
######    
label chap_finished_05: 
    
    $ book_05_units +=1
    
    if book_05_units == 1:
        "Глава [book_05_units]" "Галадриэль - нежная и добрая эльфийская принцесса."
    if book_05_units == 2:
        "Глава [book_05_units]" "Отец Галадриэль - Король Метис и его друг детства Мофоселис."
    if book_05_units == 3:
        "Глава [book_05_units]" "Король Метис объявляет о помолвке его дочери, принцессы Галадриэль и канцлера Мофоселиса."
    if book_05_units == 4:
        "Глава [book_05_units]" "Галадриэль отказывается выйти замуж за человека, который в три раза старше ее и кого, до этой поры, она считала своим дядей."
    if book_05_units == 5:
        "Глава [book_05_units]" "Король Метис не слушает \"глупые\" жалобы дочери. Галадриэль решает бежать."
    if book_05_units == 6:
        "Глава [book_05_units]" "Галадриэль удается покинуть королевские покои ночью ..."
    if book_05_units == 7:
        "Глава [book_05_units]" "Король Метис в ярости из-за побега дочери. Он решает лично возглавить поисковую группу."
    if book_05_units == 8:
        "Глава [book_05_units]" "Галадриэль уезжает на личком коне \"белом голубе\" через лес. Принцесса наслаждается своей свободой... Через время она встречает красивого человеческого дворянина на лошади..."
    if book_05_units == 9:
        "Глава [book_05_units]" "Галадриэль едет вместе с дворянином. Они обмениваются бессмысленными шутками. Он очень веселит ее. Вдруг дворянин нападает на принцессу и вырубает ее!..."
    if book_05_units == 10:
        "Глава [book_05_units]" "Галадриэль приходит в себя. К своему ужасу, она понимает, что дворянин, насилует ее. Галадриэль кричит о помощи, но красавчик сдерживает ее жестоко насилуя."
    if book_05_units == 11:
        "Глава [book_05_units]" "Галадриэль пытается бороться с мужчиной. Но не тут-то было. Вдруг она замечает, что ее окружают десятки мужчин, которые злобно ухмыляются."
    if book_05_units == 12:
        "Глава [book_05_units]" "После того, как дворянин заканчивает с Галадриэль, его люди пускают ее по кругу и насилуют эльфийскую принцессу. Галадриэль плачет и умоляет их прекратить."
    if book_05_units == 13:
        "Глава [book_05_units]" "Галадриэль приходит в себя в клетке на каком-то рынке. Ее руки связаны, ее благородные одежды разорваны в клочья, а ее волосы полны веток и сухой спермы."
    if book_05_units == 14:
        "Глава [book_05_units]" "Жирный, богатый мужчина покупает Галадриэль и приводит ее в свой дом. Принцесса больше не плачет. Она счастлива выбраться из клетки."
    if book_05_units == 15:
        "Глава [book_05_units]" "Галадриэль позволили принять ванну, после чего раб приносит ей чистую одежду и еду."
    if book_05_units == 16:
        "Глава [book_05_units]" "Галадриэль начинает чувствовать надежду, но это не так. Вскоре она понимает, что это за место: бордель."
    if book_05_units == 17:
        "Глава [book_05_units]" "Эльфийская принцесса вынуждена работать шлюхой. Она ненавидит свою новую жизнь, но у нее не остается выбора."
    if book_05_units == 18:
        "Глава [book_05_units]" "Галадриэль быстро набирает популярность. Люди, Темные Эльфы и даже карлики, она раздвигает ноги для всех."
    if book_05_units == 19:
        "Глава [book_05_units]" "Слава о молодой и красивой эльфийской шлюхе распространяется. Галадриэль принимает ее новую жизнь в борделе."
    if book_05_units == 20:
        "Глава [book_05_units]" "Вдруг все резко меняется. Галадриэль узнает, что она беременна. - Конец первой книги -"


     
    $ renpy.play('sounds/win_04.mp3')   #Not loud.
    show screen notes
    ">Вы закончили \"главу [book_05_units]\" этой книги."
    return
    
###
label chapter_check_book_05: #Checks if the chapter just finished was the last one.
    if book_05_units == 20:
        if fire_in_fireplace:
            show screen done_reading_02 
            hide screen reading_near_fire
        else:
            show screen done_reading  
            hide screen reading

        $ renpy.play('sounds/win_04.mp3')   #Not loud.
        show screen notes
        ">Это была последняя глава. Вы закончили книгу."
        $ book_05_complete = True
        $ renpy.play('sounds/win_04.mp3')   #Not loud.
        hide screen notes
        show screen notes
        ">Выше воображение улучшилось."
        $ imagination +=1
        
        if fire_in_fireplace:
            hide screen reading_near_fire
        else:
            hide screen reading
        
        if daytime:
            jump night_start
        else: 
            jump day_start
    else:
        return    
    
    
    
######################################
### BOOK 05_b ##########################
######################################
label reading_book_05_b: ### TALE OF GALADRIEL. BOOK TWO.
    
    ### SOUNDS BLOCK ###
    stop music fadeout 1.0
    if raining:
        play weather "sounds/rain.mp3" fadeout 1.0 fadein 1.0 #Quiet...
    if fire_in_fireplace:
        play bg_sounds "sounds/fire02.mp3" fadeout 1.0 fadein 1.0 #Quiet...
    if daytime and not raining and not fire_in_fireplace:
        play bg_sounds "sounds/day.mp3" fadeout 1.0 fadein 1.0 #Quiet...
    if not daytime and not raining and not fire_in_fireplace:
        play bg_sounds "sounds/night.mp3" fadeout 1.0 fadein 1.0 #Quiet...
    ### END OF BLOCK ###

    if fire_in_fireplace:
        call fire_in #Shows Genie reading a book near the fireplace.
    else:
        call fire_out #Shows Genie reading a book near the window.

    if raining:
        ">Вы читаете книгу под названием [book05b], в тоже время слушая дождь, заливающий крышу вашей башни."
    else:
        ">Вы читаете книгу под названием [book05b]"
   
    call chap_finished_05_b
    
    call chapter_check_book_05_b #Checks if the chapter just finished was the last one.
    
    ">Осталось еще несколько глав."
    
#===### SPEED READING FOR DUMMIES BONUS CHECK ###
    if s_reading_lvl == 1: #First book (book_08) on speed reading completed.
        $ speed_dummies = renpy.random.randint(1, 3) 
        if speed_dummies == 1: #Success.
            call yes_book_08 #Message you see that says you are completed one more chapter because of the "Speed reading for dummies" book.
            call chap_finished_05_b
            call chapter_check_book_05_b #Checks if the chapter just finished was the last one.
            ">Осталось еще несколько глав."
    if s_reading_lvl == 2: #Second book(book_09) on speed reading completed.
        $ speed_dummies = renpy.random.randint(1, 2) 
        if speed_dummies == 1: #Success.
            call yes_book_09 #Message you see that says you are completed both speed reading books.
            call chap_finished_05_b
            call chapter_check_book_05_b #Checks if the chapter just finished was the last one.
            ">Осталось еще несколько глав."
#===#############################################    
    
    if raining:
        if not fire_in_fireplace:
            call no_fire #Message you see that says you are reading a book during rain.
        else:
            call yes_fire #Message you see that says you are reading a book during rain near fireplace.
            call chap_finished_05_b
            call chapter_check_book_05_b #Checks if the chapter just finished was the last one.
            ">Осталось еще несколько глав."

    if fire_in_fireplace:
        hide screen reading_near_fire
    else:
        hide screen reading

    if daytime:
        jump night_start
    else: 
        jump day_start
        
######    
label chap_finished_05_b: 
    
    $ book_05_b_units +=1
    
    if book_05_b_units == 1:
        "Глава [book_05_b_units]" "Галадриэль уже беременна в течение нескольких месяцев. У принцессы, к ее удивлению, популярность растет, казалось бы, в прямой зависимости от размера ее живота."
    if book_05_b_units == 2:
        "Глава [book_05_b_units]" "Хотя Галадриэль и выглядит как послушная шлюха, по правде, она продумывает побег из борделя."
    if book_05_b_units == 3:
        "Глава [book_05_b_units]" "Эльфийская принцесса шлюха ничего не знает о жизни за пределами стен борделя. Но это не влияет на ее решимость спастись."
    if book_05_b_units == 4:
        "Глава [book_05_b_units]" "Это занимает много времени и тщательного планирования, но Галадриэль удается успешно сбежать из борделя."
    if book_05_b_units == 5:
        "Глава [book_05_b_units]" "Галадриэль теряется в огромном городе и вынуждена провести ночь на улице."
    if book_05_b_units == 6:
        "Глава [book_05_b_units]" "На улицах трудно найти еду. Галадриэль борется со стаей бродячих собак, и одна из них кусает Галадриэль за руку."
    if book_05_b_units == 7:
        "Глава [book_05_b_units]" "Беременная Галадриэль предлагает составить компанию  паре грязных бездомных мужчин в обмен на продовольствие. С ними она и ночует."
    if book_05_b_units == 8:
        "Глава [book_05_b_units]" "Галадриэль понимает, что ее жизнь в борделе была раем по сравнению с тем, что она имеет теперь. Она решает вернуться обратно."
    if book_05_b_units == 9:
        "Глава [book_05_b_units]" "Владелец Галадриэль - жирный, богатый человек не наказывает Галадриэль за побег. Наоборот, он счастлив, что одна из его самых популярных девушек вернулась обратно."
    if book_05_b_units == 10:
        "Глава [book_05_b_units]" "Галадриэль снова тепло, чисто и хорошо кормят. Она рада вернуться и популярна, как никогда."
    if book_05_b_units == 11:
        "Глава [book_05_b_units]" "Галадриэль обслуживает клиентов на протяжении всей беременности.Ребенок вот-вот родится..."
    if book_05_b_units == 12:
        "Глава [book_05_b_units]" "Богатый человек в маске заказал Галадриэль на весь день. Галадриэль задается вопросом, о том, кто это на самом деле, лениво ублажая его."
    if book_05_b_units == 13:
        "Глава [book_05_b_units]" "Таинственный человек целый день развлекается, трахая беременную Галадриэль. Из ее наполненных грудей капает молоко, в то время как человек трахает ее."
    if book_05_b_units == 14:
        "Глава [book_05_b_units]" "Человек в маске кончает на лицо Галадриэль во второй раз за сегодня. Затем он решает снять свою маску, чтобы показать лицо."
    if book_05_b_units == 15:
        "Глава [book_05_b_units]" "Галадриэль понимает, что этот человек - ее отец, король Метис. Теперь он понимает, что беременна шлюха, которую он трахал в течение нескольких часов его дочь."
    # Only now he realizes that the pregnant whore he fucked for hours is his daughter.
    if book_05_b_units == 16:
        "Глава [book_05_b_units]" "Он обнимает его лишенного речи ребенка. Глаза Галадриэль опустошены. Сперма ее отца капает с лица..."
    if book_05_b_units == 17:
        "Глава [book_05_b_units]" "Галадриэль в ужасе кричит. К ее удивлению, она приходит в себя в королевских покоях, в своей постели."
    if book_05_b_units == 18:
        "Глава [book_05_b_units]" "Она приходит в себя несколько минут, до того, как понять, что она никогда не была беременна.Все приключения, это лишь сон."
    if book_05_b_units == 19:
        "Глава [book_05_b_units]" "Галадриэль бросается к отцу и обнимает его. Девушка пережила слишком многое в \"прошлой жизни\". Она счастлива и соглашается выйти замуж за канцлера Мофоселиса."
    if book_05_b_units == 20:
        "Глава [book_05_b_units]" "{size=-1}Галадриэль находится у алтаря. Она довольна и счастлива. Вдруг она замечает то, что наполняет ее сердце ужасом. Она обнаружила шрам на руке. Место укуса собаки. - Конец -{/size}"
    
     
    $ renpy.play('sounds/win_04.mp3')   #Not loud.
    show screen notes
    ">Вы закончили \"главу [book_05_b_units]\" этой книги."
    
    return
    
###
label chapter_check_book_05_b: #Checks if the chapter just finished was the last one.
    if book_05_b_units == 20:
        if fire_in_fireplace:
            show screen done_reading_02 
            hide screen reading_near_fire
        else:
            show screen done_reading  
            hide screen reading

        $ renpy.play('sounds/win_04.mp3')   #Not loud.
        show screen notes
        ">Это была последняя глава. Вы закончили книгу."
        $ book_05_b_complete = True
        $ renpy.play('sounds/win_04.mp3')   #Not loud.
        hide screen notes
        show screen notes
        ">Ваше воображение улучшилось."
        $ imagination +=1
        
        if fire_in_fireplace:
            hide screen reading_near_fire
        else:
            hide screen reading
        
        if daytime:
            jump night_start
        else: 
            jump day_start
    else:
        return    
        
        
        
######################################
### BOOK 06 ##########################
######################################
label reading_book_06:
    
    call reading_block
 
    if fire_in_fireplace:
        call fire_in #Shows Genie reading a book near the fireplace.
    else:
        call fire_out #Shows Genie reading a book near the window.

    if raining:
        ">Вы читаете книгу под названием [book06], в тоже время слушая дождь, заливающий крышу вашей башни."
    else:
        ">Вы читаете книгу под названием [book06]..."
   
    call chap_finished_06
    
    call chapter_check_book_06 #Checks if the chapter just finished was the last one.
    ">Осталось еще несколько глав."

#===### SPEED READING FOR DUMMIES BONUS CHECK ###
    if s_reading_lvl == 1: #First book (book_08) on speed reading completed.
        $ speed_dummies = renpy.random.randint(1, 3) 
        #$ speed_dummies = 1 #Here for testing porpoise only.
        if speed_dummies == 1: #Success.
            call yes_book_08 #Message you see that says you are completed one more chapter because of the "Speed reading for dummies" book.
            call chap_finished_06
            call chapter_check_book_06 #Checks if the chapter just finished was the last one.
            ">Осталось еще несколько глав."
    if s_reading_lvl == 2: #Second book(book_09) on speed reading completed.
        $ speed_dummies = renpy.random.randint(1, 2) 
        #$ speed_dummies = 1 #Here for testing porpoise only.
        if speed_dummies == 1: #Success.
            call yes_book_09 #Message you see that says you are completed one more chapter because of the "Speed reading for dummies" book.
            call chap_finished_06
            call chapter_check_book_06 #Checks if the chapter just finished was the last one.
            ">Осталось еще несколько глав."
#===#############################################       
    
    
    if raining:
        if not fire_in_fireplace:
            call no_fire #Message you see that says you are reading a book during rain.
        else:
            call yes_fire #Message you see that says you are reading a book during rain near fireplace.
            call chap_finished_06
            call chapter_check_book_06 #Checks if the chapter just finished was the last one.
            ">Осталось еще несколько глав."

    if fire_in_fireplace:
        hide screen reading_near_fire
    else:
        hide screen reading

    if daytime:
        jump night_start
    else: 
        jump day_start
        
######    
label chap_finished_06: 
    
    $ book_06_units +=1
    
    if book_06_units == 1:
        "\"Глава [book_06_units]\"\nСемейство благородных северян."
    if book_06_units == 2:
        "\"Глава [book_06_units]\"\nКоролевская семья и царь."
    if book_06_units == 3:
        "\"Глава [book_06_units]\"\nДругое семейство."
    if book_06_units == 4:
        "\"Глава [book_06_units]\"\nИнцест между братом и сестрой королевой."
    if book_06_units == 5:
        "\"Глава [book_06_units]\"\nПокушение на ребенка. Он выживает, но находится в коме."
    if book_06_units == 6:
        "\"Глава [book_06_units]\"\nДругие персонажи."
    if book_06_units == 7:
        "\"Глава [book_06_units]\"\nНекоторые персонажи показывают себя с плохой стороны."
    if book_06_units == 8:
        "\"Глава [book_06_units]\"\nКороля отравили и он умирает. Инцест между братом и сестрой."
    if book_06_units == 9:
        "\"Глава [book_06_units]\"\nКазнили некоторых персонажей, за которых вы болели." # НЕ ПЕРЕВЕДЕНо
    if book_06_units == 10:
        "\"Глава [book_06_units]\"\nПоявилось несколько персонажей."
    if book_06_units == 11:
        "\"Глава [book_06_units]\"\nНекоторые женщины были изнасилованы и жестоко убиты."
    if book_06_units == 12:
        "\"Глава [book_06_units]\"\nЕще несколько членов дворянской семьи северян померли."
    if book_06_units == 13:   
        "\"Глава [book_06_units]\"\nНекоторых женщин насилуют еще больше. Некоторым из них удается выжить. (Конечно, их изнасилуют чуть позже)." 
    if book_06_units == 14:
        "\"Глава [book_06_units]\"\nПерсонажи, которых вы ненавидите сталкиваются в эпической битве против персонажей за которых вы болели."
    if book_06_units == 15:
        "\"Глава [book_06_units]\"\nБольшинство персонажей, которых вы ненавидите пережили сражение. Все, за кого вы болели мертвы."
    if book_06_units == 16:
        "\"Глава [book_06_units]\"\nЕще несколько изнасилований и убийств... (Вас это уже не задевает...)" 
    if book_06_units == 17:
        "\"Глава [book_06_units]\"\nНовые персонажи появляются в истории. Вы вроде начинаете болеть за одного из них."
    if book_06_units == 18:
        "\"Глава [book_06_units]\"\nПерсонаж за которого вы не болели, влюбляется в милую девушку."
    if book_06_units == 19:
        "\"Глава [book_06_units]\"\nПерсонаж, за которого вы болели, жестоко убит. Его девушку насилуют, а затем убивают."
    if book_06_units == 20:
        "\"Глава [book_06_units]\"\nНовая раса наполовину замороженной нежити включается в историю. Продолжение следует..."
        
    
        
    
     
    $ renpy.play('sounds/win_04.mp3')   #Not loud.
    show screen notes
    ">Вы закончили \"главу [book_06_units]\" этой книги."
    return
    
###
label chapter_check_book_06: #Checks if the chapter just finished was the last one.
    if book_06_units == 20:
        if fire_in_fireplace:
            show screen done_reading_02  
            hide screen reading_near_fire
        else:
            show screen done_reading  
            hide screen reading

      
        ">Это была последняя глава. Вы закончили эту книгу."
        g4 "Что за херня! Я ненавижу человека, который это написал!"
        m "Хотя все эти изнасилования подтолкнули меня на пару идей..."
        $ renpy.play('sounds/win_04.mp3')   #Not loud.
        hide screen notes
        show screen notes
        ">Ваше воображение улучшилось."
        $ imagination +=1
        $ book_06_complete = True
        
        if fire_in_fireplace:
            hide screen reading_near_fire
        else:
            hide screen reading
        
        if daytime:
            jump night_start
        else: 
            jump day_start
    else:
        return    
    
    
    
######################################
### BOOK 07 ########################## MY DEAR WAIFU ###
######################################
label reading_book_07:
    
    call reading_block
    
    if fire_in_fireplace:
        call fire_in #Shows Genie reading a book near the fireplace.
    else:
        call fire_out #Shows Genie reading a book near the window.

    if raining:
        ">Вы читаете книгу под названием [book07], в тоже время слушая дождь, заливающий крышу вашей башни."
    else:
        ">Вы читаете книгу под названием [book07]..."
   
    call chap_finished_07
    
    call chapter_check_book_07 #Checks if the chapter just finished was the last one.
    
    ">Осталось еще несколько глав."

#===### SPEED READING FOR DUMMIES BONUS CHECK ###
    if s_reading_lvl == 1: #First book (book_08) on speed reading completed.
        $ speed_dummies = renpy.random.randint(1, 2) 
        #$ speed_dummies = 1 #Here for testing porpoise only.
        if speed_dummies == 1: #Success.
            call yes_book_08 #Message you see that says you are completed one more chapter because of the "Speed reading for dummies" book.
            call chap_finished_07
            call chapter_check_book_07 #Checks if the chapter just finished was the last one.
            ">Осталось еще несколько глав."
    if s_reading_lvl == 2: #Second book(book_09) on speed reading completed.
#        $ speed_dummies = renpy.random.randint(1, 2) 
#        #$ speed_dummies = 1 #Here for testing porpoise only.
#        if speed_dummies == 1: #Success.
        call yes_book_09 #Message you see that says you are completed one more chapter because of the "Speed reading for dummies" book.
        call chap_finished_07
        call chapter_check_book_07 #Checks if the chapter just finished was the last one.
        ">Осталось еще несколько глав."
#===#############################################
    
    if raining:
        if not fire_in_fireplace:
            call no_fire #Message you see that says you are reading a book during rain.
        else:
            call yes_fire #Message you see that says you are reading a book during rain near fireplace.
            call chap_finished_07
            call chapter_check_book_07 #Checks if the chapter just finished was the last one.
            ">Осталось еще несколько глав."

    if fire_in_fireplace:
        hide screen reading_near_fire
    else:
        hide screen reading

    if daytime:
        jump night_start
    else: 
        jump day_start
        
######    
label chap_finished_07: 
    
    $ book_07_units +=1
    
    call waifu
    
    $ renpy.play('sounds/win_04.mp3')   #Not loud.
    show screen notes
    ">Вы закончили \"главу [book_07_units]\" этой книги."
    return
    
###
label chapter_check_book_07: #Checks if the chapter just finished was the last one.
    if book_07_units == 20:
        if fire_in_fireplace:
            show screen done_reading_02  
            hide screen reading_near_fire
        else:
            show screen done_reading  
            hide screen reading

      
        ">Это была последняя глава. Вы закончили эту книгу."
        if complited_leena_already and complited_shea_already and complited_stevens_already and victoria >= 1 and shea >= 1 and leena >= 1: #Harem ending. The DAHR's ticket.
            m "Вау! Отличная книга! Это было неплохо!"
            
            #m "No, I mean it! What a great peace of fiction! That Akabur dude must be a genius!"
            if not found_dahrs_ticket_once:
                m "Хм...?"
                m "Что это...? Закладка?"
                $ the_gift = "03_hp/18_store/06.png" # The DAHR's ticket.
                show screen gift
                with d3
                $ renpy.play('sounds/win2.mp3') #Sound of finding an item.
                ">Вы нашли ваучер Дахра."
                hide screen gift
                with d3
                m "Хм..."
                $ vouchers += 1 #Shows the amount of DAHR's vouchers in your possession.
                $ found_dahrs_ticket_once = True # Turns TRUE after you complete "My Dear Waifu" with the harem ending and "Dahr's voucher" fall out.
                $ waifu_book_completed = True
        elif shea_waifu and shea >= 8: 
            if not complited_shea_already: #Finished with Shea for the first time.
                m "Неплохо. Я действительно готов заботиться о Ши ..."
                g9 "Ну, о ней и ее анальной девственности..."
                $ complited_shea_already = True
            else: #Finished with Shea for the second time.
                m "Значит в конце я снова с Ши?"
                m "Хм... Может быть, я должен попробовать и выбирать другие варианты в следующий раз...?"
        elif victoria_waifu and victoria >= 7:
            if not complited_stevens_already: #Finished with Ms.Stevens for the first time.
                m "Неплохо, неплохо. Госпожа Стивенс оказалась той еще шлюхой..."
                $ complited_stevens_already = True
            else: #Finished with Shea for the second time.
                m "Значит в конце я снова с госпожой Стивенс?"
                m "Хм... Может быть, я должен попробовать и выбирать другие варианты в следующий раз...?"
        elif leena_waifu and leena >= 8:
            if not complited_leena_already: #Finished with Leena for the first time.
                g9 "Славненько! Обожаю хэппи энды!"
                $ complited_leena_already = True
            else: #Finished with Shea for the second time.
                m "Значит в конце я снова со светленькой девахой?"
                m "Hm... Может быть, я должен попробовать и выбирать другие варианты в следующий раз...?"

        else:
            m "Хм ... Конец очень разочаровал..."
            #m "Maybe I should read it again sometime."
        
        if not dear_waifu_completed_once:
            $ dear_waifu_completed_once = True # Turns TRUE when complete the book for the first time with any ending. Makes sure you get +1 imagination only once.
            $ renpy.play('sounds/win_04.mp3')   #Not loud.
            hide screen notes
            show screen notes
            ">Ваше воображение улучшилось."
            $ imagination +=1
        $ book_07_units = 0 #RESTING THE BOOK FOR ANOTHER PLAYTHORUGH.
        $ shea = 0 #RESETING SHEA'S POINTS FOR THE NEXT PLAYTHOURGH.
        $ victoria = 0
        $ leena = 0
        if fire_in_fireplace:
            hide screen reading_near_fire
        else:
            hide screen reading
        
        if daytime:
            jump night_start
        else: 
            jump day_start
    else:
        return    
    
    
        
######################################
### BOOK 08 ##########################
######################################
label reading_book_08:
    
    call reading_block
    
    hide screen gift
    if fire_in_fireplace:
        call fire_in #Shows Genie reading a book near the fireplace.
    else:
        call fire_out #Shows Genie reading a book near the window.

    if raining:
        ">Вы читаете книгу под названием [book08], в тоже время слушая дождь, заливающий крышу вашей башни."
    else:
        ">Вы читаете книгу под названием [book08]..."
   
    call chap_finished_08
    
    call chapter_check_book_08 #Checks if the chapter just finished was the last one.
            
   
    


    if raining:
        if not fire_in_fireplace:
            call no_fire #Message you see that says you are reading a book during rain.
        else:
            call yes_fire #Message you see that says you are reading a book during rain near fireplace.
            call chap_finished_08
            call chapter_check_book_08 #Checks if the chapter just finished was the last one.
      
    ">Осталось еще несколько глав."
    if fire_in_fireplace:
        hide screen reading_near_fire
    else:
        hide screen reading

    if daytime:
        jump night_start
    else: 
        jump day_start
        
######    
label chap_finished_08: 
    $ book_08_units +=1 
    $ renpy.play('sounds/win_04.mp3')   #Not loud.
    show screen notes
    ">Вы закончили \"главу [book_08_units]\" этой книги."
    return
    
###
label chapter_check_book_08: #Checks if the chapter just finished was the last one.
    if book_08_units == 10:
        if fire_in_fireplace:
            show screen done_reading_02  
            hide screen reading_near_fire
        else:
            show screen done_reading  
            hide screen reading

        $ renpy.play('sounds/win_04.mp3')   #Not loud.
        hide screen notes
        show screen notes
        ">Это была последняя глава. Вы закончили книгу."
        $ renpy.play('sounds/win_04.mp3')   #Not loud.
        hide screen notes
        show screen notes
        ">Новая способность: большой шанс закончить дополнительную главу во время чтения."
        $ book_08_complete = True
        $ s_reading_lvl +=1
        
        if fire_in_fireplace:
            hide screen reading_near_fire
        else:
            hide screen reading
        
        if daytime:
            jump night_start
        else: 
            jump day_start
    else:
        return        
    
    
    
######################################
### BOOK 09 ########################## Speed reading for experts
######################################
label reading_book_09:
    
    call reading_block ### Plays sound effects appropriate for reading. 

    hide screen gift
    if fire_in_fireplace:
        call fire_in #Shows Genie reading a book near the fireplace.
    else:
        call fire_out #Shows Genie reading a book near the window.

    if raining:
        ">Вы читаете книгу под названием [book09], в тоже время слушая дождь, заливающий крышу вашей башни."
    else:
        ">Вы читаете книгу под названием [book09]..."
   
    call chap_finished_09
    
    call chapter_check_book_09 #Checks if the chapter just finished was the last one.
            
    
#===### SPEED READING FOR DUMMIES BONUS CHECK ###
    if s_reading_lvl == 1: #First book (book_08) on speed reading completed.
        $ speed_dummies = renpy.random.randint(1, 6) 
        #$ speed_dummies = 1 #Here for testing porpoise only.
        if speed_dummies == 1: #Success.
            call yes_book_08 #Message you see that says you are completed one more chapter because of the "Speed reading for dummies" book.
            call chap_finished_09
            call chapter_check_book_09 #Checks if the chapter just finished was the last one.
            ">Осталось еще несколько глав."
#===#############################################       

    if raining:
        if not fire_in_fireplace:
            call no_fire #Message you see that says you are reading a book during rain.
        else:
            call yes_fire #Message you see that says you are reading a book during rain near fireplace.
            call chap_finished_09
            call chapter_check_book_09 #Checks if the chapter just finished was the last one.

    
    ">Осталось еще несколько глав."
    if fire_in_fireplace:
        hide screen reading_near_fire
    else:
        hide screen reading

    if daytime:
        jump night_start
    else: 
        jump day_start
        
######    
label chap_finished_09: 
    $ book_09_units +=1 
    $ renpy.play('sounds/win_04.mp3')   #Not loud.
    hide screen notes
    show screen notes
    ">Вы закончили \"главу [book_09_units]\" этой книги."
    return
    
###
label chapter_check_book_09: #Checks if the chapter just finished was the last one.
    if book_09_units == 10:
        if fire_in_fireplace:
            show screen done_reading_02  
            hide screen reading_near_fire
        else:
            show screen done_reading  
            hide screen reading

        $ renpy.play('sounds/win_04.mp3')   #Not loud.
        hide screen notes
        show screen notes
        ">Это была последняя глава. Вы закончили эту книгу."
        $ renpy.play('sounds/win_04.mp3')   #Not loud.
        hide screen notes
        show screen notes
        ">Новая способность: большой шанс закончить дополнительную главу во время чтения."


        $ book_09_complete = True
        $ s_reading_lvl +=1
        
        if fire_in_fireplace:
            hide screen reading_near_fire
        else:
            hide screen reading
        
        if daytime:
            jump night_start
        else: 
            jump day_start
    else:
        return        
    
    
######################################
### BOOK 10 ########################## "\"Platinum book of spirit\""
######################################
label reading_book_10:
    hide screen gift
    call reading_block
    
    if fire_in_fireplace:
        call fire_in #Shows Genie reading a book near the fireplace.
    else:
        call fire_out #Shows Genie reading a book near the window.

    if raining:
        ">Вы читаете книгу под названием [book10], в тоже время слушая дождь, заливающий крышу вашей башни."
    else:
        ">Вы читаете книгу под названием [book10]..."
   
    call chap_finished_10 #Basicly $ book_04_units +=1 and "Chapter completed" message.
    
    call chapter_check_book_10 #Checks if the chapter just finished was the last one.
            
    ">Осталось еще несколько глав."
    
#===### SPEED READING FOR DUMMIES BONUS CHECK ###
    if s_reading_lvl == 1: #First book (book_08) on speed reading completed.
        $ speed_dummies = renpy.random.randint(1, 3) 
        #$ speed_dummies = 1 #Here for testing porpoise only.
        if speed_dummies == 1: #Success.
            call yes_book_08 #DON'T CHANGE! KEEP IT 08. Message you see that says you are completed one more chapter because of the "Speed reading for dummies" book.
            call chap_finished_10
            call chapter_check_book_10 #Checks if the chapter just finished was the last one.
            ">Осталось еще несколько глав."
    
    if s_reading_lvl == 2: #Second book(book_09) on speed reading completed.
        $ speed_dummies = renpy.random.randint(1, 2) 
        #$ speed_dummies = 1 #Here for testing porpoise only.
        if speed_dummies == 1: #Success.
            call yes_book_09 #DON'T CHANGE! KEEP IT 09 Message you see that says you are completed one more chapter because of the "Speed reading for dummies" book.
            call chap_finished_10
            call chapter_check_book_10 #Checks if the chapter just finished was the last one.
            ">Осталось еще несколько глав."
#===#############################################

    if raining:
        if not fire_in_fireplace:
            call no_fire #Message you see that says you are reading a book during rain.
        else:
            call yes_fire #Message you see that says you are reading a book during rain near fireplace.
            call chap_finished_10
            call chapter_check_book_10 #Checks if the chapter just finished was the last one.
            ">Осталось еще несколько глав."
    

    if fire_in_fireplace:
        hide screen reading_near_fire
    else:
        hide screen reading

    if daytime:
        jump night_start
    else: 
        jump day_start
        
######    
label chap_finished_10: 
    $ book_10_units +=1 
    $ renpy.play('sounds/win_04.mp3')   #Not loud.
    show screen notes
    ">Вы закончили \"главу [book_10_units]\" этой книги."
    return
    
###
label chapter_check_book_10: #Checks if the chapter just finished was the last one.
    if book_10_units == 10:
        if fire_in_fireplace:
            show screen done_reading_02
            hide screen reading_near_fire
        else:
            show screen done_reading  
            hide screen reading

        $ renpy.play('sounds/win_04.mp3')   #Not loud.
        hide screen notes
        show screen notes
        ">Это была последняя глава. Вы закончили эту книгу."
        $ renpy.play('sounds/win_04.mp3')   #Not loud.
        hide screen notes
        show screen notes

        ">Новая способность: большой шанс закончить дополнительную главу во время написания отчета."

        $ concentration += 1
        $ book_10_complete = True
        
        if fire_in_fireplace:
            hide screen reading_near_fire
        else:
            hide screen reading
        
        if daytime:
            jump night_start
        else: 
            jump day_start
    else:
        return    
        
######################################
### BOOK 11 ########################## "\"Adamantium book of spirit\""
######################################
label reading_book_11:
    
    call reading_block
    
    hide screen gift
    if fire_in_fireplace:
        call fire_in #Shows Genie reading a book near the fireplace.
    else:
        call fire_out #Shows Genie reading a book near the window.

    if raining:
        ">Вы читаете книгу под названием [book11], в тоже время слушая дождь, заливающий крышу вашей башни."
    else:
        ">Вы читаете книгу под названием [book11]..."
   
    call chap_finished_11 #Basicly $ book_04_units +=1 and "Chapter completed" message.
    
    call chapter_check_book_11 #Checks if the chapter just finished was the last one.
            
    ">Осталось еще несколько глав."
    
#===### SPEED READING FOR DUMMIES BONUS CHECK ###
    if s_reading_lvl == 1: #First book (book_08) on speed reading completed.
        $ speed_dummies = renpy.random.randint(1, 6) 
        #$ speed_dummies = 1 #Here for testing porpoise only.
        if speed_dummies == 1: #Success.
            call yes_book_08 #DON'T CHANGE! KEEP IT 08. Message you see that says you are completed one more chapter because of the "Speed reading for dummies" book.
            call chap_finished_11
            call chapter_check_book_11 #Checks if the chapter just finished was the last one.
            ">Осталось еще несколько глав."
    
    if s_reading_lvl == 2: #Second book(book_09) on speed reading completed.
        $ speed_dummies = renpy.random.randint(1, 3) 
        #$ speed_dummies = 1 #Here for testing porpoise only.
        if speed_dummies == 1: #Success.
            call yes_book_09 #DON'T CHANGE! KEEP IT 09 Message you see that says you are completed one more chapter because of the "Speed reading for dummies" book.
            call chap_finished_11
            call chapter_check_book_11 #Checks if the chapter just finished was the last one.
            ">Осталось еще несколько глав."
#===#############################################

    if raining:
        if not fire_in_fireplace:
            call no_fire #Message you see that says you are reading a book during rain.
        else:
            call yes_fire #Message you see that says you are reading a book during rain near fireplace.
            call chap_finished_11
            call chapter_check_book_11 #Checks if the chapter just finished was the last one.
            ">Осталось еще несколько глав."
    

    if fire_in_fireplace:
        hide screen reading_near_fire
    else:
        hide screen reading

    if daytime:
        jump night_start
    else: 
        jump day_start
        
######    
label chap_finished_11: 
    $ book_11_units +=1 
    $ renpy.play('sounds/win_04.mp3')   #Not loud.
    show screen notes
    ">Вы закончили \"главу [book_11_units]\" этой книги."
    return
    
###
label chapter_check_book_11: #Checks if the chapter just finished was the last one.
    if book_11_units == 10:
        if fire_in_fireplace:
            show screen done_reading_02
            hide screen reading_near_fire
        else:
            show screen done_reading  
            hide screen reading

        $ renpy.play('sounds/win_04.mp3')   #Not loud.
        hide screen notes
        show screen notes
        ">Это была последняя глава. Вы закончили эту книгу."
        $ renpy.play('sounds/win_04.mp3')   #Not loud.
        hide screen notes
        show screen notes
        ">Вы полностью контролируете свой дух и отныне всегда завершаете дополнительную главу, во время написания отчета."

        $ concentration += 1
        $ book_11_complete = True
        
        if fire_in_fireplace:
            hide screen reading_near_fire
        else:
            hide screen reading
        
        if daytime:
            jump night_start
        else: 
            jump day_start
    else:
        return    
        
    
 
######################################
### BOOK 12 ########################## "\"Speedwriting for dummies.\""
######################################
label reading_book_12:
    
    call reading_block
    
    hide screen gift
    if fire_in_fireplace:
        call fire_in #Shows Genie reading a book near the fireplace.
    else:
        call fire_out #Shows Genie reading a book near the window.

    if raining:
        ">Вы читаете книгу под названием [book12], в тоже время слушая дождь, заливающий крышу вашей башни."
    else:
        ">Вы читаете книгу под названием [book12]..."
   
    call chap_finished_12 #Basicly $ book_04_units +=1 and "Chapter completed" message.
    
    call chapter_check_book_12 #Checks if the chapter just finished was the last one.
            
    ">Осталось еще несколько глав."
    
#===### SPEED READING FOR DUMMIES BONUS CHECK ###
    if s_reading_lvl == 1: #First book (book_08) on speed reading completed.
        $ speed_dummies = renpy.random.randint(1, 6) 
        #$ speed_dummies = 1 #Here for testing porpoise only.
        if speed_dummies == 1: #Success.
            call yes_book_08 #DON'T CHANGE! KEEP IT 08. Message you see that says you are completed one more chapter because of the "Speed reading for dummies" book.
            call chap_finished_12
            call chapter_check_book_12 #Checks if the chapter just finished was the last one.
            ">Осталось еще несколько глав."
    
    if s_reading_lvl == 2: #Second book(book_09) on speed reading completed.
        $ speed_dummies = renpy.random.randint(1, 3) 
        if speed_dummies == 1: #Success.
            call yes_book_09 #DON'T CHANGE! KEEP IT 09 Message you see that says you are completed one more chapter because of the "Speed reading for dummies" book.
            call chap_finished_12
            call chapter_check_book_12 #Checks if the chapter just finished was the last one.
            ">Осталось еще несколько глав."
#===#############################################

    if raining:
        if not fire_in_fireplace:
            call no_fire #Message you see that says you are reading a book during rain.
        else:
            call yes_fire #Message you see that says you are reading a book during rain near fireplace.
            call chap_finished_12
            call chapter_check_book_12 #Checks if the chapter just finished was the last one.
            ">Осталось еще несколько глав."
    

    if fire_in_fireplace:
        hide screen reading_near_fire
    else:
        hide screen reading

    if daytime:
        jump night_start
    else: 
        jump day_start
        
######    
label chap_finished_12: 
    $ book_12_units +=1 
    $ renpy.play('sounds/win_04.mp3')   #Not loud.
    hide screen notes
    show screen notes
    ">Вы закончили \"главу [book_12_units]\" этой книги."
    return
    
###
label chapter_check_book_12: #Checks if the chapter just finished was the last one.
    if book_12_units == 10:
        if fire_in_fireplace:
            show screen done_reading_02
            hide screen reading_near_fire
        else:
            show screen done_reading  
            hide screen reading

        $ renpy.play('sounds/win_04.mp3')   #Not loud.
        hide screen notes
        show screen notes
        ">Это была последняя глава. Вы закончили книгу."
        $ renpy.play('sounds/win_04.mp3')   #Not loud.
        hide screen notes
        show screen notes
        ">Новая способность: шанс 1 к 6 закончить дополнительную главу во время написания отчета."

        $ speedwriting += 1
        $ book_12_complete = True
        
        if fire_in_fireplace:
            hide screen reading_near_fire
        else:
            hide screen reading
        
        if daytime:
            jump night_start
        else: 
            jump day_start
    else:
        return    
        
######################################
### BOOK 13 ########################## "\"Speedwriting for beginners.\""
######################################
label reading_book_13:
    
    call reading_block
    
    hide screen gift
    if fire_in_fireplace:
        call fire_in #Shows Genie reading a book near the fireplace.
    else:
        call fire_out #Shows Genie reading a book near the window.

    if raining:
        ">Вы читаете книгу под названием [book13], в тоже время слушая дождь, заливающий крышу вашей башни."
    else:
        ">Вы читаете книгу под названием [book13]."
   
    call chap_finished_13 #Basicly $ book_04_units +=1 and "Chapter completed" message.
    
    call chapter_check_book_13 #Checks if the chapter just finished was the last one.
            

    
#===### SPEED READING FOR DUMMIES BONUS CHECK ###
    if s_reading_lvl == 1: #First book (book_08) on speed reading completed.
        $ speed_dummies = renpy.random.randint(1, 6) 
        #$ speed_dummies = 1 #Here for testing porpoise only.
        if speed_dummies == 1: #Success.
            call yes_book_08 #DON'T CHANGE! KEEP IT 08. Message you see that says you are completed one more chapter because of the "Speed reading for dummies" book.
            call chap_finished_13
            
    if s_reading_lvl == 2: #Second book(book_09) on speed reading completed.
        $ speed_dummies = renpy.random.randint(1, 3) 
        if speed_dummies == 1: #Success.
            call yes_book_09 #DON'T CHANGE! KEEP IT 09 Message you see that says you are completed one more chapter because of the "Speed reading for dummies" book.
            call chap_finished_13
            
#===#############################################
    
    call chapter_check_book_13 #Checks if the chapter just finished was the last one.
    ">Осталось еще несколько глав."
   
    if raining:
        if not fire_in_fireplace:
            call no_fire #Message you see that says you are reading a book during rain.
        else:
            call yes_fire #Message you see that says you are reading a book during rain near fireplace.
            call chap_finished_13
            call chapter_check_book_13 #Checks if the chapter just finished was the last one.
            ">Осталось еще несколько глав."
    

    if fire_in_fireplace:
        hide screen reading_near_fire
    else:
        hide screen reading

    if daytime:
        jump night_start
    else: 
        jump day_start
        
######    
label chap_finished_13: 
    $ book_13_units +=1 
    $ renpy.play('sounds/win_04.mp3')   #Not loud.
    show screen notes
    ">Вы закончили \"главу [book_13_units]\" этой книги."
    return
    
###
label chapter_check_book_13: #Checks if the chapter just finished was the last one.
    if book_13_units == 10:
        if fire_in_fireplace:
            show screen done_reading_02
            hide screen reading_near_fire
        else:
            show screen done_reading  
            hide screen reading

        $ renpy.play('sounds/win_04.mp3')   #Not loud.
        hide screen notes
        show screen notes
        ">Это была последняя глава. Вы закончили книгу."
        $ renpy.play('sounds/win_04.mp3')   #Not loud.
        hide screen notes
        show screen notes
        ">Новая способность: шанс 1 к 4 закончить дополнительную главу во время написания отчета."

        $ speedwriting += 1
        $ book_13_complete = True
        
        if fire_in_fireplace:
            hide screen reading_near_fire
        else:
            hide screen reading
        
        if daytime:
            jump night_start
        else: 
            jump day_start
    else:
        return             
    
    
######################################
### BOOK 14 ########################## "\"Speedwriting for intermediate.\"" # 1/6 chance of it to pop up. Completes extra chapter during work.
######################################
label reading_book_14:
    
    call reading_block
    
    hide screen gift
    if fire_in_fireplace:
        call fire_in #Shows Genie reading a book near the fireplace.
    else:
        call fire_out #Shows Genie reading a book near the window.

    if raining:
        ">Вы читаете книгу под названием [book14], в тоже время слушая дождь, заливающий крышу вашей башни."
    else:
        ">Вы читаете книгу под названием [book14]..."
   
    call chap_finished_14 #Basicly $ book_04_units +=1 and "Chapter completed" message.
    
    call chapter_check_book_14 #Checks if the chapter just finished was the last one.
            
    #">Осталось еще несколько глав."
    
#===### SPEED READING FOR DUMMIES BONUS CHECK ###
    if s_reading_lvl == 1: #First book (book_08) on speed reading completed.
        $ speed_dummies = renpy.random.randint(1, 6) 
        #$ speed_dummies = 1 #Here for testing porpoise only.
        if speed_dummies == 1: #Success.
            call yes_book_08 #DON'T CHANGE! KEEP IT 08. Message you see that says you are completed one more chapter because of the "Speed reading for dummies" book.
            call chap_finished_14
            
    if s_reading_lvl == 2: #Second book(book_09) on speed reading completed.
        $ speed_dummies = renpy.random.randint(1, 3) 
        if speed_dummies == 1: #Success.
            call yes_book_09 #DON'T CHANGE! KEEP IT 09 Message you see that says you are completed one more chapter because of the "Speed reading for dummies" book.
            call chap_finished_14
            
#===#############################################
    
    call chapter_check_book_14 #Checks if the chapter just finished was the last one.

   
    if raining:
        if not fire_in_fireplace:
            call no_fire #Message you see that says you are reading a book during rain.
        else:
            call yes_fire #Message you see that says you are reading a book during rain near fireplace.
            call chap_finished_14
            call chapter_check_book_14 #Checks if the chapter just finished was the last one.
            
    
    ">Осталось еще несколько глав."
    if fire_in_fireplace:
        hide screen reading_near_fire
    else:
        hide screen reading

    if daytime:
        jump night_start
    else: 
        jump day_start
        
######    
label chap_finished_14: 
    $ book_14_units +=1 
    $ renpy.play('sounds/win_04.mp3')   #Not loud.
    show screen notes
    ">Вы закончили \"главу [book_14_units]\" этой книги."
    return
    
###
label chapter_check_book_14: #Checks if the chapter just finished was the last one.
    if book_14_units == 10:
        if fire_in_fireplace:
            show screen done_reading_02
            hide screen reading_near_fire
        else:
            show screen done_reading  
            hide screen reading

        $ renpy.play('sounds/win_04.mp3')   #Not loud.
        hide screen notes
        show screen notes
        ">Это была последняя глава. Вы закончили книгу."
        $ renpy.play('sounds/win_04.mp3')   #Not loud.
        hide screen notes
        show screen notes
        ">Новое умение разблокировано: шанс 1 к 2 завершить дополнительную главу, когда пишите отчет..."

        $ speedwriting += 1
        $ book_14_complete = True
        
        if fire_in_fireplace:
            hide screen reading_near_fire
        else:
            hide screen reading
        
        if daytime:
            jump night_start
        else: 
            jump day_start
    else:
        return                 
            
    
######################################
### BOOK 15 ########################## "\"Speedwriting for advanced.\"" # 1/4 chance of it to pop up. Completes extra chapter during work.
######################################
label reading_book_15:
    
    call reading_block
    
    hide screen gift
    if fire_in_fireplace:
        call fire_in #Shows Genie reading a book near the fireplace.
    else:
        call fire_out #Shows Genie reading a book near the window.

    if raining:
        ">Вы читаете книгу под названием [book15], в тоже время слушая дождь, заливающий крышу вашей башни."
    else:
        ">Вы читаете книгу под названием [book15]..."
   
    call chap_finished_15 #Basicly $ book_04_units +=1 and "Chapter completed" message.
    
    call chapter_check_book_15 #Checks if the chapter just finished was the last one.
            
  
    
#===### SPEED READING FOR DUMMIES BONUS CHECK ###
    if s_reading_lvl == 1: #First book (book_08) on speed reading completed.
        $ speed_dummies = renpy.random.randint(1, 6) 
        #$ speed_dummies = 1 #Here for testing porpoise only.
        if speed_dummies == 1: #Success.
            call yes_book_08 #DON'T CHANGE! KEEP IT 08. Message you see that says you are completed one more chapter because of the "Speed reading for dummies" book.
            call chap_finished_15
            
    if s_reading_lvl == 2: #Second book(book_09) on speed reading completed.
        $ speed_dummies = renpy.random.randint(1, 3) 
        if speed_dummies == 1: #Success.
            call yes_book_09 #DON'T CHANGE! KEEP IT 09 Message you see that says you are completed one more chapter because of the "Speed reading for dummies" book.
            call chap_finished_15
            
#===#############################################
    
    call chapter_check_book_15 #Checks if the chapter just finished was the last one.
   
   
    if raining:
        if not fire_in_fireplace:
            call no_fire #Message you see that says you are reading a book during rain.
        else:
            call yes_fire #Message you see that says you are reading a book during rain near fireplace.
            call chap_finished_15
            call chapter_check_book_15 #Checks if the chapter just finished was the last one.

    
    ">Осталось еще несколько глав."
    if fire_in_fireplace:
        hide screen reading_near_fire
    else:
        hide screen reading

    if daytime:
        jump night_start
    else: 
        jump day_start
        
######    
label chap_finished_15: 
    $ book_15_units +=1 
    $ renpy.play('sounds/win_04.mp3')   #Not loud.
    show screen notes
    ">Вы закончили \"главу [book_15_units]\" этой книги."
    return
    
###
label chapter_check_book_15: #Checks if the chapter just finished was the last one.
    if book_15_units == 10:
        if fire_in_fireplace:
            show screen done_reading_02
            hide screen reading_near_fire
        else:
            show screen done_reading  
            hide screen reading

        $ renpy.play('sounds/win_04.mp3')   #Not loud.
        hide screen notes
        show screen notes
        ">Это была последняя глава. Вы закончили книгу."
        $ renpy.play('sounds/win_04.mp3')   #Not loud.
        hide screen notes
        show screen notes
        ">Вы стали настоящим мастером скорописания и с этого момента вы всегда выполняете дополнительную главу, когда составляете отчет."
        #">New skill unlocked: a decent chance of completing an additional chapter when doing paperwork."

        $ speedwriting += 1
        $ book_15_complete = True
        
        if fire_in_fireplace:
            hide screen reading_near_fire
        else:
            hide screen reading
        
        if daytime:
            jump night_start
        else: 
            jump day_start
    else:
        return                 
                
######################################
### BOOK 16 ########################## "\"Speedwriting for experts.\"" # 1/2 chance of it to pop up. Completes extra chapter during work.
######################################
label reading_book_16:
    
    call reading_block
    
    hide screen gift
    if fire_in_fireplace:
        call fire_in #Shows Genie reading a book near the fireplace.
    else:
        call fire_out #Shows Genie reading a book near the window.

    if raining:
        ">Вы читаете книгу под названием [book16], в тоже время слушая дождь, заливающий крышу вашей башни."
    else:
        ">Вы читаете книгу под названием [book16]..."
   
    call chap_finished_16 #Basicly $ book_04_units +=1 and "Chapter completed" message.
    
    call chapter_check_book_16 #Checks if the chapter just finished was the last one.
            
    
    
#===### SPEED READING FOR DUMMIES BONUS CHECK ###
    if s_reading_lvl == 1: #First book (book_08) on speed reading completed.
        $ speed_dummies = renpy.random.randint(1, 6) 
        #$ speed_dummies = 1 #Here for testing porpoise only.
        if speed_dummies == 1: #Success.
            call yes_book_08 #DON'T CHANGE! KEEP IT 08. Message you see that says you are completed one more chapter because of the "Speed reading for dummies" book.
            call chap_finished_16
            
    if s_reading_lvl == 2: #Second book(book_09) on speed reading completed.
        $ speed_dummies = renpy.random.randint(1, 3) 
        if speed_dummies == 1: #Success.
            call yes_book_09 #DON'T CHANGE! KEEP IT 09 Message you see that says you are completed one more chapter because of the "Speed reading for dummies" book.
            call chap_finished_16
            
#===#############################################
    
    call chapter_check_book_16 #Checks if the chapter just finished was the last one.

   
    if raining:
        if not fire_in_fireplace:
            call no_fire #Message you see that says you are reading a book during rain.
        else:
            call yes_fire #Message you see that says you are reading a book during rain near fireplace.
            call chap_finished_16
            call chapter_check_book_16 #Checks if the chapter just finished was the last one.
       
    
    ">Осталось еще несколько глав."
    if fire_in_fireplace:
        hide screen reading_near_fire
    else:
        hide screen reading

    if daytime:
        jump night_start
    else: 
        jump day_start
        
######    
label chap_finished_16: 
    $ book_16_units +=1 
    $ renpy.play('sounds/win_04.mp3')   #Not loud.
    show screen notes
    ">Вы закончили \"главу [book_16_units]\" этой книги."
    return
    
###
label chapter_check_book_16: #Checks if the chapter just finished was the last one.
    if book_16_units == 10:
        if fire_in_fireplace:
            show screen done_reading_02
            hide screen reading_near_fire
        else:
            show screen done_reading  
            hide screen reading

        $ renpy.play('sounds/win_04.mp3')   #Not loud.
        hide screen notes
        show screen notes
        ">Это была последняя глава. Вы закончили эту книгу."
        ">Новая способность: большой шанс закончить дополнительную главу во время написания отчета."
       
        $ speedwriting += 1
        $ book_16_complete = True
        
        if fire_in_fireplace:
            hide screen reading_near_fire
        else:
            hide screen reading
        
        if daytime:
            jump night_start
        else: 
            jump day_start
    else:
        return                 
                
                
######################################
### BOOK 17 ########################## "\"Speedwriting for maniacs.\"" # 1 (sure) chance of it to pop up. Completes extra chapter during work.
######################################
label reading_book_17:
    
    call reading_block
    
    hide screen gift
    if fire_in_fireplace:
        call fire_in #Shows Genie reading a book near the fireplace.
    else:
        call fire_out #Shows Genie reading a book near the window.

    if raining:
        ">Вы читаете книгу под названием [book17], в тоже время слушая дождь, заливающий крышу вашей башни."
    else:
        ">Вы читаете книгу под названием [book17]..."
   
    call chap_finished_17 #Basicly $ book_04_units +=1 and "Chapter completed" message.
    
    call chapter_check_book_17 #Checks if the chapter just finished was the last one.
            
 
    
#===### SPEED READING FOR DUMMIES BONUS CHECK ###
    if s_reading_lvl == 1: #First book (book_08) on speed reading completed.
        $ speed_dummies = renpy.random.randint(1, 6) 
        #$ speed_dummies = 1 #Here for testing porpoise only.
        if speed_dummies == 1: #Success.
            call yes_book_08 #DON'T CHANGE! KEEP IT 08. Message you see that says you are completed one more chapter because of the "Speed reading for dummies" book.
            call chap_finished_17
            
    if s_reading_lvl == 2: #Second book(book_09) on speed reading completed.
        $ speed_dummies = renpy.random.randint(1, 3) 
        if speed_dummies == 1: #Success.
            call yes_book_09 #DON'T CHANGE! KEEP IT 09 Message you see that says you are completed one more chapter because of the "Speed reading for dummies" book.
            call chap_finished_17
            
#===#############################################
    
    call chapter_check_book_17 #Checks if the chapter just finished was the last one.
    
   
    if raining:
        if not fire_in_fireplace:
            call no_fire #Message you see that says you are reading a book during rain.
        else:
            call yes_fire #Message you see that says you are reading a book during rain near fireplace.
            call chap_finished_17
            call chapter_check_book_17 #Checks if the chapter just finished was the last one.
        
    
    ">Осталось еще несколько глав."
    if fire_in_fireplace:
        hide screen reading_near_fire
    else:
        hide screen reading

    if daytime:
        jump night_start
    else: 
        jump day_start
        
######    
label chap_finished_17: 
    $ book_17_units +=1 
    $ renpy.play('sounds/win_04.mp3')   #Not loud.
    show screen notes
    ">Вы закончили \"главу [book_17_units]\" этой книги."
    return
    
###
label chapter_check_book_17: #Checks if the chapter just finished was the last one.
    if book_17_units == 10:
        if fire_in_fireplace:
            show screen done_reading_02
            hide screen reading_near_fire
        else:
            show screen done_reading  
            hide screen reading

        $ renpy.play('sounds/win_04.mp3')   #Not loud.
        hide screen notes
        show screen notes
        ">Это была последняя глава. Вы закончили книгу."
        $ renpy.play('sounds/win_04.mp3')   #Not loud.
        hide screen notes
        show screen notes
        ">Вы стали настоящим мастером скорописания и с этого момента вы всегда выполняете дополнительную главу, когда пишите отчет."

        $ speedwriting += 1
        $ book_17_complete = True
        
        if fire_in_fireplace:
            hide screen reading_near_fire
        else:
            hide screen reading
        
        if daytime:
            jump night_start
        else: 
            jump day_start
    else:
        return                     
    
    
    
### PAPERWORK ###
label paperwork:
    stop music fadeout 1.0
    if daytime:
        play bg_sounds "sounds/day.mp3" fadeout 1.0 fadein 1.0 #Quiet...
    else: 
        play bg_sounds "sounds/night.mp3" fadeout 1.0 fadein 1.0 #Quiet...
    
    if raining:
        play weather "sounds/rain.mp3" fadeout 1.0 fadein 1.0 #Quiet...
        stop bg_sounds 
    
    
    hide screen genie
    show screen paperwork
    with Dissolve(0.3)
    ">Вы делаете отчет."
    
    call finished_working_chapter #Chapter finished. $ report_chapters += 1
    
    call report_chapters_check #Checks whether or not the completed chapter was the final one.
        
    if daytime: # Makes sure that check happens only at nighttime. 
        pass
    else:
        if wather_generator >= 31 and wather_generator <= 40: # FULL MOON
            call f_moon_bonus
        if wather_generator >= 51 and wather_generator <= 60: # FULL MOON
            call f_moon_bonus
           
    call report_chapters_check #Checks whether or not the completed chapter was the final one.
    
    ### CONCENTRATION CHECK ###========================================================================
    if concentration == 1:
        $ concentraton_check = renpy.random.randint(1, 6) #Copper book.
        if concentraton_check == 1:
            call concentration_label
    if concentration == 2:
        $ concentraton_check = renpy.random.randint(1, 4) #Bronze book.
        if concentraton_check == 1:
            call concentration_label
    if concentration == 3:
        $ concentraton_check = renpy.random.randint(1, 2) #Silver book.
        if concentraton_check == 1:
            call concentration_label
    if concentration == 4:                                                               #Golden book.
        call concentration_label
#    if concentration == 5:
#        $ concentraton_check = renpy.random.randint(1, 2) #Platinum book.
#        if concentraton_check == 1:
#            call concentration_label
#    if concentration == 6:
#            call concentration_label
    ###==============================================================================================
    
    call report_chapters_check #Checks whether or not the completed chapter was the final one.
    
    ### SPEEDWRITING CHECK ###========================================================================
    if speedwriting == 1:
        $ speedwriting_check = renpy.random.randint(1, 6) #"\"Speedwriting for dummies.\"" # 1/10 chance
        if speedwriting_check == 1:
            call speedwriting_label
    if speedwriting == 2:
        $ speedwriting_check = renpy.random.randint(1, 4) #"\"Speedwriting for beginners.\"" # 1/8 chance of it to pop up.
        if speedwriting_check == 1:
            call speedwriting_label
    if speedwriting == 3:
        $ speedwriting_check = renpy.random.randint(1, 2) #"\"Speedwriting for intermediate.\"" # 1/6 chance of it to pop up.
        if speedwriting_check == 1:
            call speedwriting_label
    if speedwriting == 4:
            call speedwriting_label
#    if speedwriting == 5:
#        $ speedwriting_check = renpy.random.randint(1, 2) #"\"Speedwriting for experts.\"" # 1/2 chance of it to pop up.
#        if speedwriting_check == 1:
#            call speedwriting_label
#    if speedwriting == 6:
#        call speedwriting_label #""\"Speedwriting for maniacs.\"" # 1 (sure) chance of it to pop up.
    
    call report_chapters_check #Checks whether or not the completed chapter was the final one.
            

    show screen genie
    hide screen paperwork
    
    
    
    if daytime:
        jump night_start
    else: 
        jump day_start    
    
### 
label report_chapters_check:
    if report_chapters >= 7:
        ">Вы закончили отчет."
        $ report_chapters = 0
        $ finished_report += 1
    return
### FULL MOON BONUS ###
label f_moon_bonus:
    $ renpy.play('sounds/win_04.mp3')   #Not loud.
    hide screen notes
    show screen notes
    $ report_chapters += 1
    ">Полнолуние сделало вас более продуктивным.\n>Вы закончили [report_chapters] глав."
    return
###
label finished_working_chapter:
    $ report_chapters += 1
    $ renpy.play('sounds/win_04.mp3')   #Not loud.
    hide screen notes
    show screen notes
    ">Вы закончили [report_chapters] глав."
    return
### CONCENTRATION
label concentration_label:
    $ renpy.play('sounds/win_04.mp3')   #Not loud.
    hide screen notes
    show screen notes
    $ report_chapters += 1
    ">Во время работы вы идеально сконцентрированы.\n>И заканчиваете дополнительную главу.\n>Вы закончили [report_chapters] глав."
    return
### SPEEDWRITING
label speedwriting_label:
    $ renpy.play('sounds/win_04.mp3')   #Not loud.
    hide screen notes
    show screen notes
    $ report_chapters += 1
    ">Вы используете свой навык скорописания.\n>И заканчиваете дополнительную главу.\n>Вы закончили [report_chapters] глав."
    return
    
    
### READING GALADRIEL BOOKS IN PROPER ORDER ###
label gal_proper:
    m "Чтение книг не дает мне ничего."
    hide screen gift
    return
    
    
    
### READING A BOOK BLOCK ### Sends here to make sure that proper SFX is played during reading a book.
label reading_block:
    stop music fadeout 2.0
    if fire_in_fireplace:
        play bg_sounds "sounds/fire02.mp3" fadeout 1.0 fadein 1.0 #Quiet...
    else:
        call fire_out #Shows Genie reading a book near the window.

    if daytime and not raining:
        #play bg_sounds "sounds/day.mp3" fadeout 1.0 fadein 1.0 #Quiet...
        play weather "sounds/day.mp3" fadeout 1.0 fadein 1.0 #Quiet...

    
    if not daytime and not raining:
        play weather "sounds/night.mp3" fadeout 1.0 fadein 1.0 #Quiet...


    if raining:
        play weather "sounds/rain.mp3" fadeout 1.0 fadein 1.0 #Quiet...
    
    return