init -996 python:
  
# 
    class Chibi(Entry):
        # constructor - Chibi initializing
        def __init__( self, Name, defVals=None):
            super(Chibi, self).__init__(Name=Name, Type="Chibi", defVals=defVals )

#            self.Items=RegEntry(ItemCollection("items"+self.Name))  
            return


        def Show(self, images):
            for o in images:
#                if o=="daph walk":
#                    chibitrans(700, 200, 10.0)
                renpy.show_screen("chibiscreen", [o], None)
                renpy.pause()
            return

        def Hide(self):
            renpy.hide_screen("chibiscreen")
            return

        def emo(self, s):
            _temp=s.split(" ")
            for i in range(4):
                daphne.view.data().setStyleKey( ['brows', 'eyes', 'blush', 'mouth'][i], _temp[i] )
            return


screen chibiscreen( aImgs, aTrans=None ):   
    python:
#        data = aData.values()
#        data.sort( key = lambda item: item.zorder )
        #for element in data:
#            element._x_x_x_screen_pos = gSumPos( aPos, element.position )
        data=[
#        '03_hp/animation/h_walk_01.png', 
#        '03_hp/animation/h_walk_02.png', 
#        '03_hp/animation/h_walk_03.png',
        "daph walk2"
        ]
        data=aImgs
    for element in data:
        add element at chibitrans(700, 200, 10.0) # Transform( pos = ( 500, 500 ) )  #at gSumPos( aPos, element.position )


transform chibitrans(x=0, x2=0, v=1.0): 
    xpos x #координата X, из которой начинаем движение
    ypos 0 #высота, на которой проводим движение
    linear v xpos x2 # опреация передвижения (скорость линейна )



image daph blink:
    choice 12.0:
        "03_hp/animation/h_walk_01.png"
        pause.4
    choice:
        "03_hp/animation/h_walk_06.png"
        pause.08
    repeat



image daph walk2:
    "03_hp/24_daphna/daf_walk_a1.png"
    pause.08
    "03_hp/24_daphna/daf_walk_a2.png"
    pause.08
    "03_hp/24_daphna/daf_walk_a3.png"
    pause.08
    "03_hp/24_daphna/daf_walk_a35.png"
    pause.08
    "03_hp/24_daphna/daf_walk_a3.png"
    pause.08
    "03_hp/24_daphna/daf_walk_a2.png"
    pause.08
    "03_hp/24_daphna/daf_walk_a1.png"
    pause.08
    "03_hp/24_daphna/daf_walk_a4.png"
    pause.08
    "03_hp/24_daphna/daf_walk_a5.png"
    pause.08
    "03_hp/24_daphna/daf_walk_a4.png"
    pause.08
    repeat

image daph walk:
    "03_hp/24_daphna/daf_walk_a1.png"
    pause.08
    "03_hp/24_daphna/daf_walk_a2.png"
    pause.08
    "03_hp/24_daphna/daf_walk_a3.png"
    pause.08
    "03_hp/24_daphna/daf_walk_a2.png"
    pause.08
    "03_hp/24_daphna/daf_walk_a1.png"
    pause.08
    "03_hp/24_daphna/daf_walk_a4.png"
    pause.08
    "03_hp/24_daphna/daf_walk_a5.png"
    pause.08
    "03_hp/24_daphna/daf_walk_a4.png"
    pause.08
    repeat



