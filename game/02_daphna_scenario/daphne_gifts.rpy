label daphne_giving(item=itsDAHR(choose.choice)):
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
        
    return

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

        



