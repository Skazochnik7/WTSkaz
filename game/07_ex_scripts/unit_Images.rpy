label daphne_images_init:
    python:
        __path="03_hp/24_daphne/dap_walk_"
#        __path="03_hp/animation/h_walk_"
        # GO
        for s in {"a", "b", "c", "d", "e", "f"}:  
            __s=s
#            if not s in {"a", "b"}: # Это заглушка пока нет чибиков от художника, потом просто убрать ее
#                s="a"

            renpy.image("chibidaphne "+__s+" go", Animation(__path+s+"1.png", .08,
                                        __path+s+"2.png", .08,
                                        __path+s+"3.png", .08,
                                        __path+s+"2.png", .08,
                                        __path+s+"1.png", .08,
                                        __path+s+"4.png", .08,
                                        __path+s+"5.png", .08,
                                        __path+s+"4.png", .08
                                        ))
            renpy.image("chibidaphne "+__s+" goout", Animation(im.Flip(__path+s+"1.png", horizontal=True), .08,
                                        im.Flip(__path+s+"2.png", horizontal=True), .08,
                                        im.Flip(__path+s+"3.png", horizontal=True), .08,
                                        im.Flip(__path+s+"2.png", horizontal=True), .08,
                                        im.Flip(__path+s+"1.png", horizontal=True), .08,
                                        im.Flip(__path+s+"4.png", horizontal=True), .08,
                                        im.Flip(__path+s+"5.png", horizontal=True), .08,
                                        im.Flip(__path+s+"4.png", horizontal=True), .08
                                        ))



# Здесь есть вероятность (choice), а в renpy нет функции, которая при анимации вероятность задает, пока для каждого чибика отдельный экран 
    image chibidaphne a blink:
        choice 12.0:
            "03_hp/24_daphne/dap_walk_a1.png"
            pause.4
        choice:
            "03_hp/24_daphne/dap_blink_a2.png"
            pause.08
        repeat

    image chibidaphne b blink:
        choice 12.0:
            "03_hp/24_daphne/dap_blink_b1.png"
            pause.4
        choice:
            "03_hp/24_daphne/dap_blink_b2.png"
            pause.08
        repeat

    image chibidaphne c blink:
        choice 12.0:
            "03_hp/24_daphne/dap_walk_a1.png"
            pause.4
        choice:
            "03_hp/24_daphne/dap_blink_a2.png"
            pause.08
        repeat

    image chibidaphne d blink:
        choice 12.0:
            "03_hp/24_daphne/dap_walk_a1.png"
            pause.4
        choice:
            "03_hp/24_daphne/dap_blink_a2.png"
            pause.08
        repeat



    return