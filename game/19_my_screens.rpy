    
### SCREENS ###
screen main_menu_01:
    imagebutton: # DOOR
        xpos 758 
        ypos 315
        focus_mask True
        xanchor "center"
        yanchor "center"
        idle "03_hp/05_props/01_door.png"
        hover "03_hp/05_props/01_door_02.png"
        action [Hide("main_menu_01"), Hide("animation_feather"), Jump("door")]
        
 
        
    imagebutton: # CUPBOARD
        xpos 120 
        ypos 280
        focus_mask True
        xanchor "center"
        yanchor "center"
        idle "03_hp/05_props/02_cupboard.png"
        hover "03_hp/05_props/02_cupboard_02.png"
        action [Hide("main_menu_01"), Hide("animation_feather"), Jump("cupboard")]
        
    if package_is_here:
        imagebutton: # THE PACKAGE
                xpos 260 
                ypos 235
                xanchor "center"
                yanchor "center"
                idle "03_hp/05_props/owl_06.png" 
                hover "03_hp/05_props/owl_06_2.png"
                #hovered [Show("gui_tooltip", my_picture="hoot", my_tt_xpos=250, my_tt_ypos=180) ] 
                #unhovered [Hide("gui_tooltip")]
                action [Hide("main_menu_01"), Hide("package"), Jump("mail_02")]


    imagebutton: # GENIE
        xpos 230
        ypos 336
        focus_mask True
        xanchor "center"
        yanchor "center"
        idle "newanimation"
        hover "03_hp/05_props/11_genie_02.png"
        hovered [Show("gui_tooltip", my_picture="exclaim_01", my_tt_xpos=195, my_tt_ypos=210) ] 
        #hovered [Show("config_afterchoices_skip_idle.png", xpos=46, ypos=518) ]
        unhovered [Hide("gui_tooltip")]
        action [Hide("main_menu_01"), Hide("animation_feather"), Jump("desk")]
    
    imagebutton: # PHOENIX
        xpos 400 
        ypos 225
        #focus_mask True
        xanchor "center"
        yanchor "center"
        idle "pho_01" 
        hover "03_hp/05_props/06_phoenix_02.png"
        #hovered [Show("gui_tooltip", my_picture="exclaim_01", my_tt_xpos=195, my_tt_ypos=210) ] 
        #hovered [Show("config_afterchoices_skip_idle.png", xpos=46, ypos=518) ]
        #unhovered [Show("gui_tooltip", my_picture="feather", my_tt_xpos=360, my_tt_ypos=140, xanchor="center", yanchor="center") ]
        action [Hide("main_menu_01"), Hide("animation_feather"), Jump("phoenix")]
        
    imagebutton: # FIREPLACE
        xpos 553 
        ypos 277
        #focus_mask True
        xanchor "center"
        yanchor "center"
        idle "03_hp/05_props/03_fireplace_02.png" 
        hover "03_hp/05_props/03_fireplace_03.png"
        action [Hide("main_menu_01"), Jump("fireplace")]
     
    if letters >= 1: #Adds one letter in waiting list to be read. Displays owl with envelope.:
        imagebutton: # OWL
            xpos 315 
            ypos 270
            focus_mask True
            xanchor "center"
            yanchor "center"
            idle "owl_01" 
            hover "03_hp/05_props/owl_04.png"
            #hovered [Show("gui_tooltip", my_picture="hoot", my_tt_xpos=250, my_tt_ypos=180) ] 
            #unhovered [Hide("gui_tooltip")]
            action [Hide("main_menu_01"), Jump("mail")]
    



        
screen gui_tooltip:
    add my_picture xpos my_tt_xpos ypos my_tt_ypos
    
screen animation_feather: #Falling feather animation
    add "feather" xpos 360 ypos 140
    zorder 4
    
screen rum_screen: #Rummaging through the cumpboard.
    add "03_hp/05_props/02_cupboard_03.png" at Position(xpos=120, ypos=280, xanchor="center", yanchor="center")
    add "03_hp/05_props/04_chair_02.png" at Position(xpos=192, ypos=300, xanchor="center", yanchor="center")
    add "03_hp/05_props/09_table.png" at Position(xpos=220, ypos=330, xanchor="center", yanchor="center") 
    add "rum" xpos 20 ypos 110
    zorder 1
    
screen feeding: #FEEDING THE PHOENIX.
    add "03_hp/05_props/04_chair_02.png" at Position(xpos=180, ypos=300, xanchor="center", yanchor="center")
    add "03_hp/05_props/09_table.png" at Position(xpos=220, ypos=330, xanchor="center", yanchor="center") 
    add "feeding" xpos 270 ypos 75
    zorder 1
    
screen petting: #PETTING THE PHOENIX.
    add "03_hp/05_props/04_chair_02.png" at Position(xpos=180, ypos=300, xanchor="center", yanchor="center")
    add "03_hp/05_props/09_table.png" at Position(xpos=220, ypos=330, xanchor="center", yanchor="center") 
    add "petting" xpos 250 ypos 65
    zorder 1

screen sad_phoenix: #SAD SMILEY THAT SHOWS WHEN YOU PET THE BIRD.
    add "sad_01" xpos 423 ypos 130
    zorder 1
    
screen notes: #A bunch of notes poping out with a "win" sound effect.
    add "notes" xpos 320 ypos 330
    zorder 1
    
screen paperwork: #GENIE DOING PAPERWORK BEHIND HIS DESK.
    add "paperwork_02" xpos 84 ypos 205
    
screen reading_near_fire: #GENIE READING A BOOK BY THE FIRE.
    add "03_hp/05_props/04_chair_02.png" at Position(xpos=180, ypos=300, xanchor="center", yanchor="center")
    add "03_hp/05_props/09_table.png" at Position(xpos=220, ypos=330, xanchor="center", yanchor="center") 
    add "reading_near_fire" xpos 290 ypos 205
    zorder 4 #Because otherwise the bird food would be on top.

screen reading: #GENIE READING A BOOK.
    add "03_hp/05_props/04_chair_02.png" at Position(xpos=180, ypos=300, xanchor="center", yanchor="center")
    add "03_hp/05_props/09_table.png" at Position(xpos=220, ypos=330, xanchor="center", yanchor="center") 
    add "reading" xpos 290 ypos 205
    zorder 4 #Because otherwise the bird food would be on top.

screen done_reading: #DONE READING THE BOOK.
    add "03_hp/05_props/04_chair_02.png" at Position(xpos=180, ypos=300, xanchor="center", yanchor="center")
    add "03_hp/05_props/09_table.png" at Position(xpos=220, ypos=330, xanchor="center", yanchor="center") 
    add im.Flip("03_hp/animation/reading_07.png", horizontal=True) xpos 290 ypos 205
    zorder 4 #Because otherwise the bird food would be on top.
    
screen done_reading_02: #DONE READING THE BOOK BY THE FIRE.
    add "03_hp/05_props/04_chair_02.png" at Position(xpos=180, ypos=300, xanchor="center", yanchor="center")
    add "03_hp/05_props/09_table.png" at Position(xpos=220, ypos=330, xanchor="center", yanchor="center") 
    add "03_hp/animation/reading_07.png" xpos 290 ypos 205

    zorder 4 #Because otherwise the bird food would be on top.
    
screen genie_jerking_off: #Genie sitting behind his desk and jerking off...
    add "genie_jerking_off" xpos 78 ypos 205
    zorder 2 
    tag chibi_genie
    
screen genie_jerking_sperm: #Genie cumming under the desk.
    add "genie_jerking_sperm_ani" xpos 78 ypos 205
    tag after_jerk
    zorder 2 
    
screen genie_jerking_sperm_02 :
    add "03_hp/animation/jerking_sperm_11.png" xpos 78 ypos 205
    tag after_jerk
    zorder 2 


    
screen candlefire_01:
    add "candle_fire" xpos 100 ypos 43
    zorder 2

screen candlefire_02:
    add "candle_fire_02" xpos 583 ypos 108
    zorder 2
   
    
    
   
    
    
    
    
    
    
    
    
    
    
    
    
screen phoenix_food: #Phoenix's food.
    add "03_hp/05_props/06_phoenix_food.png" xpos 350 ypos 49 
    zorder 3
    
screen fireplace_fire: #FIREPLACE FIRE.
    add "fireplace_fire" xpos 436 ypos 141
    zorder 1
    
    
    
screen room: #MAIN ROOM BG. #ну, тут все просто. Кстати, здесь zorder по умолчанию равен 0
    #zorder -2
    add "03_hp/01_bg/01_main_room.png"
screen room_night: #MAIN ROOM NIGHT BG. 
    add "03_hp/01_bg/01_main_room_02.png"
    
screen door:    
    add "03_hp/05_props/01_door.png" at Position(xpos=758, ypos=315, xanchor="center", yanchor="center")
screen cupboard:
    add "03_hp/05_props/02_cupboard_00.png" at Position(xpos=120, ypos=280, xanchor="center", yanchor="center")
screen chair:
    add "03_hp/05_props/04_chair.png" at Position(xpos=653, ypos=300, xanchor="center", yanchor="center")
screen chair_02:
    add "03_hp/05_props/04_chair_02.png" at Position(xpos=192, ypos=300, xanchor="center", yanchor="center")
screen fireplace:
    add "03_hp/05_props/03_fireplace.png" at Position(xpos=553, ypos=277, xanchor="center", yanchor="center")
screen phoenix:
    add "03_hp/05_props/06_phoenix.png" at Position(xpos=400, ypos=225, xanchor="center", yanchor="center")
screen candle_01:
    add "03_hp/05_props/07_candle.png" at Position(xpos=693, ypos=225, xanchor="center", yanchor="center")
screen candle_02:
    add "03_hp/05_props/08_candle.png" at Position(xpos=210, ypos=160, xanchor="center", yanchor="center")
screen genie:
    tag chibi_genie
    add "03_hp/05_props/11_genie_00.png" at Position(xpos=230, ypos=336, xanchor="center", yanchor="center")
    #add "03_hp/05_props/09_table.png" at Position(xpos=220, ypos=330, xanchor="center", yanchor="center")
screen owl: #DEFAULT OWL WITH ENVELOPE IN IT'S MOUTH.   
    add "03_hp/05_props/owl_01.png" at Position(xpos=315, ypos=270, xanchor="center", yanchor="center")
screen owl_02: #OWL. No Envelope.   
    add "03_hp/05_props/owl_05.png" at Position(xpos=315, ypos=270, xanchor="center", yanchor="center")
screen package: #PACKAGE.   
    add "03_hp/05_props/owl_06.png" at Position(xpos=260, ypos=235, xanchor="center", yanchor="center")
screen owl_03: #OWL SITTING ON A PACKAGE.
    add "03_hp/05_props/owl_05.png" at Position(xpos=310, ypos=235, xanchor="center", yanchor="center")
    
screen dumbledore: # DUMBLEDORE AND HIS DESK.
    tag chibi_genie
    add "03_hp/05_props/dum.png" at Position(xpos=230, ypos=336, xanchor="center", yanchor="center")

### EMO
screen thought: #Thinking emotion over a chibi.
    tag emo
    add "thought" xpos tt_xpos ypos tt_ypos
    zorder 2

### SNAPE CHIBI
screen snape_01: #Snape stands still near the door.
    tag snape
    add "03_hp/09_snape_ani/snape_0130.png" at Position(xpos=610, ypos=210)
    
screen snape_01_f: #Snape stands still near the door. (Mirrored).
    tag snape
    add im.Flip("03_hp/09_snape_ani/snape_0130.png", horizontal=True) at Position(xpos=610, ypos=210)
    
screen snape_02: #Snape stands still near the desk.
    tag snape
    add "03_hp/09_snape_ani/snape_0130.png" at Position(xpos=360, ypos=210) 
    zorder 3



    
    
screen snape_walk_01: #Default Snape walk animation. 
    tag snape
    add "snape_walk_01" at custom_walk(walk_xpos, walk_xpos2)
    #at Position(xpos=680, ypos=345, xanchor="center", yanchor="center")

screen snape_walk_01_f: #Default Snape walk animation. (Mirrored).
    tag snape
    add "snape_walk_01_f" at custom_walk(walk_xpos, walk_xpos2)

### HERMIONE CHIBI ###
screen hermione_01: #Hermione stands still.
    tag hermione
    add "03_hp/animation/h_walk_01.png" at Position(xpos=hermione_chibi_xpos, ypos=hermione_chibi_ypos)

screen hermione_01_f: #Hermione stands still. (MIRRORED)
    tag hermione
    add im.Flip("03_hp/animation/h_walk_01.png", horizontal=True) at Position(xpos=hermione_chibi_xpos, ypos=hermione_chibi_ypos) # 610 - Stands near the door.




screen hermione_02: #Hermione stands still and blinks.
    tag hermione
    add "ch_hem blink" at Position(xpos=hermione_chibi_xpos, ypos=hermione_chibi_ypos)

screen hermione_02_b: #Hermione stands still wearing a robe.
    tag hermione
    add "03_hp/animation/01.png" at Position(xpos=hermione_chibi_xpos, ypos=hermione_chibi_ypos)



# second event - hermione lifts her skirt to show panties
screen hermione_lift_skirt_angry: #Hermione lifts her skirt
    tag hermione
    add "03_hp/16_hermione_chibi/panties_00.png" at Position(xpos=350, ypos=190)

screen hermione_lift_skirt_normal: #Hermione lifts her skirt
    tag hermione
    add "03_hp/16_hermione_chibi/panties_01.png" at Position(xpos=350, ypos=190)
    
screen hermione_lift_skirt_no_panties: #Hermione lifts her skirt
    tag hermione
    add "03_hp/16_hermione_chibi/panties_02.png" at Position(xpos=350, ypos=190)

screen hermione_lift_skirt_shift_panties: #Hermione lifts her skirt
    tag hermione
    add "03_hp/16_hermione_chibi/panties_02_s.png" at Position(xpos=350, ypos=190)

 

screen hermione_04: #Hermione lifts her shirt. Showing tits.
    tag hermione
    add "03_hp/16_hermione_chibi/tits_00.png" at Position(xpos=350, ypos=190)

screen hermione_04_b: #Hermione lifts her shirt. Showing tits. CLOSER TO THE DESK
    tag hermione
    add "03_hp/16_hermione_chibi/tits_00.png" at Position(xpos=250, ypos=190)


    
screen hermione_walk_01:
    tag hermione
    add "ch_hem walk_01" at custom_walk_02(walk_xpos, walk_xpos2)

screen hermione_chibi_robe: #Hermione. Chibi. Walking. Wearing a robe.
    tag hermione
    add "ch_hem robe" at custom_walk_02(walk_xpos, walk_xpos2)

screen hermione_chibi_robe_f: #Hermione. Chibi. Walking. Wearing a robe.
    tag hermione
    add "ch_hem robe_f" at custom_walk_02(walk_xpos, walk_xpos2)

    
screen hermione_walk_01_f: #Hermione walking animation. facing right. (Leaving tower).
    tag hermione
    add "ch_hem walk_01_f" at custom_walk_02(walk_xpos, walk_xpos2)
    
screen hermione_run: #Hermione running. facing right. (Leaving tower).
    tag hermione
    add "ch_hem run_f" at custom_walk_02(walk_xpos, walk_xpos2)
    
### GENIE CHIBI ###

screen genie_walk: #Default Genie walk animation. 
    tag chibi_genie
    add "genie_walk_ani" at genie_walk(walk_xpos, walk_xpos2)
  

### SNAPE FULL
screen snape_main: #Snape. Full size.
    tag big_snape
    add "03_hp/10_snape_main/snape_main.png" xpos tt_xpos ypos tt_ypos
    add s_sprite xpos tt_xpos + 299 ypos tt_ypos
    #zorder hermione_main_zorder #(5) Otherwise candle light is shown on top.
    zorder 3 #Otherwise candle light is shown on top.
    


### SNAPE EMOTIONS
screen s_emo_01: #Closed eyes and closed mouth.
    tag semo
    add "03_hp/10_snape_main/s_emo_01.png" xpos tt_xpos ypos tt_ypos
    zorder 2 #Otherwise candle light is shown on top.
















### MISC SCREENS
screen bld1:
    add "03_hp/11_misc/bld.png"
    zorder 3
screen ctc:
    zorder 7
    add "ctc4"
screen points: #House points screen.
    add "03_hp/11_misc/points_02.png" at Position(xpos=0, ypos=1)  
    hbox: #горизонтальный «контейнер», где будет изображение золота и его количество
        spacing 10 xpos 146 ypos 11#отступ для текста, если надо прямо в левом углу — убираем его        
        text "{size=-5}[slytherin]{/size}" #сумма текстом
    hbox: #горизонтальный «контейнер», где будет изображение золота и его количество
        spacing 10 xpos 252 ypos 11#отступ для текста, если надо прямо в левом углу — убираем его        
        text "{size=-5}[gryffindor]{/size}" #сумма текстом
    hbox: 
        spacing 10 xpos 365 ypos 11
        text "{size=-5}[hufflepuff]{/size}" 
    hbox: 
        spacing 10 xpos 37 ypos 11
        text "{size=-5}[ravenclaw]{/size}" 
    
    hbox: ### DAYS COUNTER ###
        spacing 10 xpos 630 ypos 10
        text "{size=-3}[day]{/size}" 
    
    hbox: ### DGOLD COUNTER ###
        spacing 10 xpos 734 ypos 10
        text "{size=-4}[gold]{/size}" 


screen gift:
    zorder 5
    add "03_hp/18_store/00.png" 
    add the_gift
    




    











screen letter:
    zorder 4
    add "03_hp/11_misc/letter.png" at Position(xpos=200, ypos=30)  
    hbox: #горизонтальный «контейнер», где будет изображение золота и его количество
        spacing 40 xpos 270 ypos 80 xmaximum 250#отступ для текста, если надо прямо в левом углу — убираем его        
        text letter_text
screen blkfade:
    zorder 5
    add "blackfade.png"
 
screen jerkingimage:
    zorder jerk_zorder
    add jerk_image
    # variant "small"
    # modal True
    
screen blktone:
    zorder 5 #Otherwise bird's food will be on top.
    add im.Alpha("blackfade.png", 0.5)

screen blktone8:
    zorder 5 #Otherwise bird's food will be on top.
    add im.Alpha("blackfade.png", 0.8)

screen whitetone8:
    zorder 5 #Otherwise bird's food will be on top.
    add im.Alpha("white.jpg", 0.8)
    
screen white:
    zorder 3
    add "white.jpg"
    
screen emo: #Character talking off screen.
    #zorder 3 
    add "emo8" at Position(xpos=700, ypos=100, xanchor=0, yanchor=0) 



        ### ADDING HOUSE POINTS ###
screen adding_03_points:
    add "what_03_points" at Position(xpos=131, ypos=0)

        ### GRYFFINDOR POINTS ###
screen gryffindor_03_points:
    add "what_03_points" at Position(xpos=238, ypos=0)
screen gryffindor_01_points:
    add "what_01_points" at Position(xpos=238, ypos=0)
screen gryffindor_02_points:
    add "what_02_points" at Position(xpos=238, ypos=0)
screen gryffindor_05_points:
    add "what_05_points" at Position(xpos=238, ypos=0)
screen gryffindor_15_points:
    add "what_15_points" at Position(xpos=238, ypos=0)
    
    
### Hufflepuff POINTS ###
screen hufflepuff_03_points:
    add "what_03_points" at Position(xpos=348, ypos=0)
screen hufflepuff_01_points:
    add "what_01_points" at Position(xpos=348, ypos=0)
screen hufflepuff_02_points:
    add "what_02_points" at Position(xpos=348, ypos=0)
screen hufflepuff_05_points:
    add "what_05_points" at Position(xpos=348, ypos=0)
screen hufflepuff_15_points:
    add "what_15_points" at Position(xpos=348, ypos=0)
    
### Ravenclaw POINTS ###
screen ravenclaw_03_points:
    add "what_03_points" at Position(xpos=22, ypos=0)
screen ravenclaw_01_points:
    add "what_01_points" at Position(xpos=22, ypos=0)
screen ravenclaw_02_points:
    add "what_02_points" at Position(xpos=22, ypos=0)
screen ravenclaw_05_points:
    add "what_05_points" at Position(xpos=22, ypos=0)
screen ravenclaw_15_points:
    add "what_15_points" at Position(xpos=22, ypos=0)
    
    
### UNIVERSAL POINTS AWARDING SCREEN FOR EVERY HOUSE ###

screen s_p_u: # SLYTHERIN
    add s_p_u_pic at Position(xpos=131, ypos=0)
    
screen g_p_u: # GRYFFINDOR
    add g_p_u_pic at Position(xpos=238, ypos=0)
    
screen h_p_u: # HUFFLEPUFF 
    add h_p_u_pic at Position(xpos=348, ypos=0)
    
screen r_p_u: # RAVENCLAW
    add r_p_u_pic at Position(xpos=22, ypos=0)
    
### MAIN SCREEN FOR ADDING POINTS ###


    

### EVENT 01 ###
screen genie_stands:
    add "03_hp/animation/feeding_01.png" xpos tt_xpos ypos tt_ypos
    
screen genie_stands_f: #Genie stands. Facing left.
    add im.Flip("03_hp/animation/feeding_01.png", horizontal=True) xpos tt_xpos ypos tt_ypos  

screen desk: #Genie's desk.
    add "03_hp/05_props/09_table.png" at Position(xpos=220, ypos=330, xanchor="center", yanchor="center") 
    
screen desk_02: #Genie's desk.
    add "03_hp/05_props/09_table.png" at Position(xpos=220, ypos=330, xanchor="center", yanchor="center") 


### DUEL ###

screen snape_defends:
    add "ch_sna defend" at Position(xpos=-90, ypos=-5)
    zorder 7

### DAMAGE ###
screen minus_100:
    add "minus_100" at Position(xpos=640, ypos=120)

screen minus_300:
    add "minus_300" at Position(xpos=640, ypos=120)
    
    
screen minus_500:
    add "minus_500" at Position(xpos=640, ypos=120)
    
screen minus_0:
    add "minus_0" at Position(xpos=640, ypos=120)

screen minus_0_genie:
    add "minus_0" at Position(xpos=310, ypos=120)
screen minus_400_genie:
    add "minus_400" at Position(xpos=310, ypos=120)
screen minus_50_genie:
    add "minus_50" at Position(xpos=310, ypos=120)

screen plus_300:
    add "plus_300" at Position(xpos=310, ypos=120)



### HANGING WITH SNAPE ###

screen with_snape:
    add "03_hp/05_props/with_snape.png"
    tag hanging_with_snape
    zorder 3
screen with_snape_animated:
    add "genie_jerking_sperm"
    tag hanging_with_snape
    zorder 3
    
    
screen s_head: #Snape. Head.
    tag head
    add "03_hp/10_snape_main/snape_main.png" xpos tt_xpos ypos tt_ypos # x = 330, Right bottom corner: y = 340
    add s_sprite xpos tt_xpos + 299 ypos tt_ypos # x = 330, Right bottom corner: y = 340
    zorder 8
   
screen s_head2: #Snape. Head.
    tag head
    add "03_hp/10_snape_main/snape_main.png" xpos s_head_xpos ypos s_head_ypos # x = 330, Right bottom corner: y = 340
    add s_sprite xpos s_head_xpos + 299 ypos s_head_ypos # x = 330, Right bottom corner: y = 340
    zorder 8
    
    
    
    
    
    
    
    
    
    
    

### GROPING ###

screen groping_01: #Facing Genie.
    tag favor
    add "groping_01" at Position(xpos=-200, ypos=10)
    add "groping_01_blinking" at Position(xpos=-200, ypos=10)
    
screen groping_02: #Facing Genie.
    tag favor
    add "groping_02" at Position(xpos=-200, ypos=10)
    add "groping_02_blinking" at Position(xpos=-200, ypos=10)
    
screen no_groping_01: #Facing Genie.
    tag favor
    add "03_hp/animation/grope_05.png" at Position(xpos=-200, ypos=10)
    add "groping_01_blinking" at Position(xpos=-200, ypos=10)
    
screen no_groping_02: #Facing Genie.
    tag favor
    add "03_hp/animation/grope_b_05.png" at Position(xpos=-200, ypos=10)
    add "groping_02_blinking" at Position(xpos=-200, ypos=10)
    
### MOLESTING TITS FULLY CLOTHED ###

screen groping_03: #Facing Genie.
    tag favor
    add "groping_03_ani" at Position(xpos=-200, ypos=10)
    add "groping_01_blinking" at Position(xpos=-200, ypos=10)
    
### MOLESTING NAKED TITS ###

screen groping_naked_tits: 
    tag favor
    add "groping_naked_tits_ani" at Position(xpos=-200, ypos=10)
    add "groping_01_blinking" at Position(xpos=-200, ypos=10)
    zorder 1 #Otherwise chair is on top.
    
### JERKING OFF ###

screen jerking_off_01: 
    tag favor
    add "jerking_off_ani" at Position(xpos=-200, ypos=10)
    if not no_blinking: #When True - blinking animation is not displayed. 
        add "groping_01_blinking" at Position(xpos=-200, ypos=10)
    zorder 1 #Otherwise chair is on top.

### SPERM ###
screen jerking_off_cum: 
    add "jerking_off_cum_ani" at Position(xpos=-200, ypos=10)
    #add "groping_01_blinking" at Position(xpos=-200, ypos=10)
    zorder 2 #Otherwise there is a bug with blinking.

### ADMIRING TITS ###
screen genie_and_tits_01: #Genie sitting, looking ar naked tits. Hermione stands right in front of him. (Behind the desk even).
    tag favor
    add "03_hp/05_props/admire_tits_00.png" at Position(xpos=-200, ypos=10)

### HERMIONE DANCING FULLY CLOTHED ###
screen clothed_dance: #Hermione stands still.
    tag hermione
    add "clothed_dance_ani" at Position(xpos=hermione_chibi_xpos, ypos=hermione_chibi_ypos)

### HERMIONE DANCING NO VEST ###
screen no_vest_dance: #Hermione stands still.
    tag hermione
    add "no_vest_dance_ani" at Position(xpos=hermione_chibi_xpos, ypos=hermione_chibi_ypos)
    
### HERMIONE DANCING NO VEST ###
screen no_skirt_dance: #Hermione stands still.
    tag hermione
    add "no_skirt_dance_ani" at Position(xpos=hermione_chibi_xpos, ypos=hermione_chibi_ypos)
    
### HERMIONE DANCING NO VEST ###
screen no_shirt_dance: #Hermione stands still.
    tag hermione
    add "no_shirt_dance_ani" at Position(xpos=hermione_chibi_xpos, ypos=hermione_chibi_ypos)
    
### HERMIONE DANCING NO SKIRT NO SHIRT ###
screen no_shirt_no_skirt_dance: #Hermione stands still.
    tag hermione
    add "no_shirt_no_skirt_dance_ani" at Position(xpos=hermione_chibi_xpos, ypos=hermione_chibi_ypos)
    
### HERMIONE CHIBI UNIVERSAL SCREEN ###
screen h_c_u: 
    tag hermione
    add h_c_u_pic at Position(xpos=hermione_chibi_xpos, ypos=hermione_chibi_ypos)

###  GENIE CHIBI UNIVERSAL SCREEN ###
screen g_c_u: 
    tag genie
    add g_c_u_pic at Position(xpos=genie_chibi_xpos, ypos=genie_chibi_ypos)
    
###  SNAPE CHIBI UNIVERSAL SCREEN ###
screen s_c_u: 
    tag snape
    add s_c_u_pic at Position(xpos=snape_chibi_xpos, ypos=snape_chibi_ypos) # (xpos=360, ypos=210) 
    zorder 3
      
 

    
    
    

###  GENIE'S CUM UNIVERSAL SCREEN ###
screen g_c_c_u: 
    add g_c_c_u_pic at Position(xpos=genie_cum_chibi_xpos, ypos=genie_cum_chibi_ypos)

###  SNAPE'S CUM UNIVERSAL SCREEN ###
screen s_c_c_u: 
    add s_c_c_u_pic at Position(xpos=snape_cum_chibi_xpos, ypos=snape_cum_chibi_ypos)



### ENDING UNIVERSAL 01 ###
screen end_u_1: 
    add end_u_1_pic #at Position(xpos=snape_cum_chibi_xpos, ypos=snape_cum_chibi_ypos)
    tag ending
    zorder 2
    
### ENDING UNIVERSAL 02 ###
screen end_u_2: 
    add end_u_2_pic #at Position(xpos=snape_cum_chibi_xpos, ypos=snape_cum_chibi_ypos)
    tag ending
    zorder 2
    
### ENDING UNIVERSAL 03 ###
screen end_u_3: 
    add end_u_3_pic #at Position(xpos=snape_cum_chibi_xpos, ypos=snape_cum_chibi_ypos)
    zorder 2

### ENDING UNIVERSAL 04 ###
screen end_u_4: 
    add end_u_4_pic #at Position(xpos=snape_cum_chibi_xpos, ypos=snape_cum_chibi_ypos)
    zorder 2


screen new_window: #WEATHER BG. CLEAR SKY. #тут тоже просто — делаем zorder -2, чтобы заглушка была ниже остальных скринов — ведь облако должно плыть между ней и комнатой 
    zorder -2
    add "03_hp/01_bg/03_weather.png"
    
screen cloud: # zorder -1, т.к. должно быть выше заглушки, но ниже комнаты
    zorder -1
    add "03_hp/07_weather/cloud_small.png" at cloud_move # это значит, что изображение подчиняется методу движения cloud_move, который прописан дальше

screen cloud_night_01: 
    #zorder -1
    add "03_hp/07_weather/night_cloud_02.png" at cloud_night_move_01
    
screen cloud_night_02: 
    #zorder -1
    add "03_hp/07_weather/night_cloud_01.png" at cloud_night_move_02
    
screen cloud_night_03: 
    #zorder -1
    add "03_hp/07_weather/night_cloud_03.png" at cloud_night_move_03
    
    
    
screen credits_chibi: # ONE CHIBI
    zorder 5   
    add dermo at Position(xpos=280, ypos=140)
    
    
screen credits_chibi2: # TWO CHIBIs
    zorder 5   
    add dermo at Position(xpos=150, ypos=140)
    
screen uni_cr: # UNIVERSAL CREDITS CHIBI
    zorder 5
    add dermo at Position(xpos=xder, ypos=yder)
    
    
    
    
    
### LOLA ###

screen l_head: #Screen that shows a full sprite of HERMIONE.
    tag head
    zorder 8
    add lola_body xpos lx ypos ly
    add lola_face xpos lx ypos ly
    if l_blush:
        add "03_hp/22_lola/blush.png" xpos lx ypos ly
    if l_things:
        add "03_hp/22_lola/things.png" xpos lx ypos ly
    if l_question:
        add "03_hp/22_lola/question.png" xpos lx ypos ly
    if l_drop:
        add "03_hp/22_lola/drop.png" xpos lx ypos ly
    if l_hearts:
        add "03_hp/22_lola/hearts.png" xpos lx ypos ly
    if l_exclamation:
        add "03_hp/22_lola/exclamation.png" xpos lx ypos ly
    if l_tears:
        add "03_hp/22_lola/tears.png" xpos lx ypos ly
    
    
    
    

