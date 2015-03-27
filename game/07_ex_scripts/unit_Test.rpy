label test_daphna:
# Метка - зерезервированная RenPy. На нее программа переходит после загрузки.
# Код ниже инициализирует переменные хранилища, если они не были инициализированы (например, написан новый шаг сценария)
# Этот же код вызываем из блока start для начальной инициализации переменных
#show ch_hem blink at Position(xpos=300, ypos=350, xanchor="center", yanchor="center") with Dissolve(.1)
#pause 
    $chibi=Chibi("daphna")
    $ posHead = gMakePos( 390, -100 )
    $ posHead2 = gMakePos( 190, -100 )

    label test_daphna_menu:
        menu:
            "Дафна 5 картинок":
    #            renpy.show_screen("chibiscreen")
    #            renpy.pause()
                $chibi.Show(["daph walk"])
            "Дафна 6 картинок":
                $chibi.Show(["daph walk2"])
            "По умолчанию":
                $daphne.view.data().setStyleKey( 'mouth', 'default' )
                $daphne.view.data().setStyleKey( 'eyes', 'default' )
                $daphne.view.showQ("body_01.png", posHead)
                $daphne.head.showQ("body_01.png", posHead2)
            "Действие":
#                $daphne.view.showQ("body_01.png", posHead)
                $daphne.view.data().setStyleKey( 'mouth', 'wo' )
                $daphne.view.data().setStyleKey( 'eyes', 'narrow_lower' )
            "Тест (55 00 3 opT)":
                $daphne.Face("55 00 3 opT")
                "..."
            "Тест (36 n2 1 dis)":
                $daphne.Face("36 n2 1 dis")
                "..."

#                $daphne.view.showQ("body_47.png", posHead)

        $chibi.Hide()
        jump test_daphna_menu

#python:
#    def emo(s):
#        _temp=s.split(" ")
#        for i in range(4):
#            daphne.view.setStyleKey( ['brows', 'eyes', 'cheeks', 'mouth'][i], _temp[i] )
#        return

#            renpy.show_screen("chibiscreen")
#            renpy.pause()
    

#    python:

#        renpy.show_screen("hermione_02")
#        renpy.say("","Теперь не видно? но видно другое!")
#    "Теперь не видно"



    #    def hlebo(**kwargs):
    #        ui.frame()
    #        ui.image('03_hp/animation/h_walk_03.png')
    #        ui.close()
    #        renpy.pause(2)
    #        ui.image('03_hp/animation/h_walk_02.png')
    #        ui.close()
    #        renpy.pause(2)
#            return
    #        ui.vbox()
    #        ui.text("Test")
    #        ui.close()

    #    renpy.define_screen("hlebo", hlebo, "False", "2", tag=None, variant=None)
    # Можно в функйии создающей экран добавлять картинки, но что если нужно создать последовательность картинок (через пауззу)?

    #    renpy.show_screen("hleboscreen")

    #    renpy.show("hermione_02", at_list=[Position(xalign=300,yalign=300)], zorder=2, tag="hermiona")
