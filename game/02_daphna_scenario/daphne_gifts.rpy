#label daphne_giving_pre():
#    $item=itsDAHR(choose.choice)
#    $daphne_giving_return="daphne_pre_finish_menu"
#    jump daphne_giving

label daphne_giving: #Переходит через меню, значит можно в меню добавить адрес ухода в ничего и не использовать вспомогательную, а сразу заходить по этой метке и разбирать переменные менею
    $item=itsDAHR(choose.choice)
    $daphne_giving_return=choose.escLabel

    $daphne.Items.Receive(hero.Items, item.Name)
    if item.Name=="wine":
        pass
    if item.Name=="candy":
        python:
            if daphne.whoring<=0:
                daphne("~55 00 1 def// Не думаю, что это хорошая идея, сэр.// Вы даете пиво своему студенту? Пиво запрещено в Хогвартсе."),
                hero("Мисс, Гринграсс, ОБЫЧНОМУ студенту, я конечно не дал бы пива. Но ВАМ... Вы - совсем другое дело."), 
                daphne("О!...//.....// Вы, конечно, правы, сэр.")
            elif daphne.whoring<=3:
                daphne("~55 00 1 def// Пиво запрещено в Хогвартсе, сэр.// Но из уважения к вам я возьму")
        pass
        
    jump expression daphne_giving_return

label daphne_item_on(item):
    if item.Name=="skirt":
        pass

label daphne_item_off(item):
    if item.Name=="skirt":
        pass

    
    
        
        
label daphne_changeliking(__liking):
    $daphne.liking+=__liking
    $daphne.Visibility()
    if __liking<0:
        ">Настроение Дафны ухудшилось...\n>Дафна {size=+5}злится{/size} на вас..."
    elif __liking==0:
        ">Настроение Дафны не изменилось..."
    else:
        if daphne.liking < 0:
            ">Настроение Дафны улучшено...\n>Дафна {size=+5}огорчена вами{/size}..." 
        elif daphne.liking == 0:
            ">Настроение Дафны улучшено...\n>Дафна {size=+5}не злится{/size} на вас..."
        else:
            ">Настроение Дафны улучшено...\n>Дафне {size=+5}приятно ваше общество{/size}..."        
    return

        



