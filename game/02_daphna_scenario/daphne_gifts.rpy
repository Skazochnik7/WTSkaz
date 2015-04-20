label daphne_giving(item):
    if item.Name=="wine":
        pass

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

        
        


