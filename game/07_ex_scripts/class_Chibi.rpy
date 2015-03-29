init -996 python:
  
# 
    class Chibi(Entry):
        # constructor - Chibi initializing
        def __init__( self, Name, defVals=None):
            super(Chibi, self).__init__(Name=Name, Type="Chibi", defVals={"x0":0, "y0":0} )
            return

        def TransPos(self, image, x=None, y=None, lag=0.0):
            if y==None:
                y=self.y0
            if x==None:
                x=self.x0
            self.Hide()
            renpy.show_screen(Name+"screen", self.Name+" "+image, self.x0, x, y, lag)
            renpy.pause(lag)

            self.x0=x
            self.y0=y
            return

        def Trans(self, images):
            self.__y=None
            self.__x=None
            self.__lag=None
            for o in images:
                self.__pars=o.split(" ")
                if len(self.__pars)>=2:
                    self.__x={"door":600,"center":400,"neardesk":200}[self.__pars[1]] 

                if len(self.__pars)>=3:
                    self.__lag={"walk":abs(self.__x-self.x0)/20.0}[self.__pars[2]]

                self.TransPos(self.__pars[0], self.__x, self.__y, self.__lag)

            return

#        def Show(self, images):
#            for o in images:
#                renpy.show_screen("chibiscreen", [o], None)
#                renpy.pause()
#            return

        def Hide(self):
            renpy.hide_screen(Name+"screen")
            return


        @property
        def x0(self):
            return self.GetValue("x0")
        @x0.setter
        def x0(self, value):
            self.SetValue("x0", value)

        @property
        def y0(self):
            return self.GetValue("y0")
        @y0.setter
        def y0(self, value):
            self.SetValue("y0", value)




screen chibidaphnescreen( aImgs, x1=0, x2=0, y=0, lag=1.0 ):   
    add aImgs at chibitrans(x1, x2, y, lag) #chibitrans(700, 200, 10.0) # Transform( pos = ( 500, 500 ) )  #at gSumPos( aPos, element.position )

transform chibitrans(x1=0, x2=0, y=0, lag=1.0): 
    xpos x1 #координата X, из которой начинаем движение
    ypos y #высота, на которой проводим движение
    linear lag xpos x2 # опреация передвижения (скорость линейна )


image chibidaphne blink:
    choice 12.0:
        "03_hp/animation/h_walk_01.png"
        pause.4
    choice:
        "03_hp/animation/h_walk_06.png"
        pause.08
    repeat

image chibidaphne walk:
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

        

