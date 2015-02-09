label points_changes: # SLYTHERIN POINTS AWARDING
    if generating_points == 1: # NO POINTS FOR SLYTHERIN ON THIS DAY.
            pass
    elif generating_points == 2: # POINTS WILL BE AWARDED

        $li=["02", "05", "07", "09", "11", "13", "15", "17", 
            "19", "21", "23", "25", "27", "29", "31", "40"]

        $ slytherin +=int(li[snapes_support]) * turbo
        if turbo==1:
            hide screen s_p_u
        else: 
            hide screen s_p_u2
        $ s_p_u_pic = "what_"+li[snapes_support]+"_points"
        if turbo==1:
            show screen s_p_u
        else: 
            show screen s_p_u2


    return
                
