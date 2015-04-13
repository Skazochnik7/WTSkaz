
label lrm_stats_00:
    $screens.ShowD3("lrm_stats_00", 
    par1="{size=-3}Гермиона{/size}      {size=-6}Развращенность:{/size}"
    "{size=-4} [hermi.whoring]{/size}\n                    {size=-6}Злость:{/size}"
    "{size=-4} "+str(-hermi.liking)+"{/size}\n                    {size=-6}{/size}",
    par2="{size=-3}Дафна   {/size}      {size=-6}Развращенность:{/size}"
    "{size=-4} [daphne.whoring]{/size}\n                    {size=-6}Злость:{/size}"
    "{size=-4} "+str(-daphne.liking)+"{/size}\n                    {size=-6}{/size}",
        )
# Если этого не делать, то при включенной ускоренной прокрутке окно появляется и тут же исчезает. 
# Если ставить, то при ускоренной прокрутке чтобы окно исчезло нужно щелкать дважды. 
# Пока непонятно почему так, но это намного предпочтительнее мелькания
    $config.allow_skipping = False 
    pause
    $config.allow_skipping = True # 
    $screens.HideD3("lrm_stats_00")


    call screen main_menu_01



screen lrm_stats_00(par1, par2):
    zorder 4

    add "03_hp/11_misc/lrm_stats.png" at Position(xpos=200, ypos=30)

    hbox: #                								Гермиона
        spacing 40 xpos 260 ypos 100 xmaximum 350  #       
        text par1 #lrm_stats_text_01

    hbox: #                								Дафна
        spacing 40 xpos 260 ypos 200 xmaximum 350  #       
        text par2 #lrm_stats_text_02



screen lrm_hat:                                                                                                               # LRM
    add "03_hp/05_props/00_lrm_hat.png" at Position(xpos=120, ypos=280, xanchor="center", yanchor="center")                   # LRM  



