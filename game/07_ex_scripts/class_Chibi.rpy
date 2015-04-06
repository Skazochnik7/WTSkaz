init -996 python:
  
# 
    class Chibi(Entry):
        # constructor - Chibi initializing
        def __init__( self, Name, defVals=None):
            super(Chibi, self).__init__(Name=Name, Type="Chibi", defVals={"x0":0, "y0":0, "speed":0.0} )
            return

        def TransPos(self, image, x=None, y=None, lag=0.0):
            if y==None:
                y=self.y0
            if x==None:
                x=self.x0
            self.Hide()
            renpy.show_screen(self.Name+"screen", self.Name+" "+image, self.x0, x, y, lag)
#            if transition is not None:
            renpy.with_statement( d3, None, True )
            renpy.pause(lag)

            self.x0=x
            self.y0=y
            return self

        def Trans(self, arg1, arg2=None, arg3=None, arg4=None, arg5=None):
            self.__args=[arg1, arg2, arg3, arg4, arg5]

            for o in self.__args:
                if o==None:
                    break
                self.__pars=o.split(" ")
                if len(self.__pars)>=2:
                    self.__State(self.__pars[1])

                self.TransPos(self.__pars[0], self.__x, self.__y, 0.0 if self.speed==0.0 else abs(self.__x-self.x0)/self.speed)
            return self

        def Hide(self):
            renpy.hide_screen(self.Name+"screen")
#            if transition is not None:
            renpy.with_statement( d3, None, True )
            return

        def State(self, x=None, y=None, speed=None):
            self.__State(x, y, speed)
            self.x0=self.__x
            self.y0=self.__y
            self.speed=self.__speed
            return self

        def __State(self, x=None, y=None, speed=None):
            self.__speed=self.speed
            self.__x=self.x0
            self.__y=self.y0
            if isinstance( x, basestring ):
                self.__x={"door":610,"center":360,"neardesk":200}[x]
                self.__y={"door":210,"center":210,"neardesk":0}[x]
            else:
                if x!=None:
                    self.__x=x
                if y!=None:
                    self.__y=y
            if isinstance( speed, basestring ):
                self.__speed={"go":20.0}[speed]
            else:
                if speed!=None:
                    self.__speed=speed
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

        @property
        def speed(self):
            return self.GetValue("speed")
        @speed.setter
        def speed(self, value):
            self.SetValue("speed", value)




screen chibidaphnescreen( aImgs, x1=0, x2=0, y=0, lag=1.0 ):   
    add aImgs at chibitrans(x1, x2, y, lag) #chibitrans(700, 200, 10.0) # Transform( pos = ( 500, 500 ) )  #at gSumPos( aPos, element.position )

transform chibitrans(x1=0, x2=0, y=0, lag=1.0): 
    xpos x1 #координата X, из которой начинаем движение
    ypos y #высота, на которой проводим движение
    linear lag xpos x2 # опреация передвижения (скорость линейна )


image chibidaphne blink:
    choice 12.0:
        "03_hp/24_daphne/dap_walk_a1.png"
        pause.4
    choice:
        "03_hp/24_daphne/dap_blink_a2.png"
        pause.08
    repeat

image chibidaphne go:
    "03_hp/24_daphne/dap_walk_a1.png"
    pause.08
    "03_hp/24_daphne/dap_walk_a2.png"
    pause.08
    "03_hp/24_daphne/dap_walk_a3.png"
    pause.08
    "03_hp/24_daphne/dap_walk_a2.png"
    pause.08
    "03_hp/24_daphne/dap_walk_a1.png"
    pause.08
    "03_hp/24_daphne/dap_walk_a4.png"
    pause.08
    "03_hp/24_daphne/dap_walk_a5.png"
    pause.08
    "03_hp/24_daphne/dap_walk_a4.png"
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


# СНЕЙП
screen chibisnapescreen( aImgs, x1=0, x2=0, y=0, lag=1.0 ):   
    add aImgs at chibitrans(x1, x2, y, lag) #chibitrans(700, 200, 10.0) # Transform( pos = ( 500, 500 ) )  #at gSumPos( aPos, element.position )

image chibisnape go: #Default Snape walk animation. 
    "03_hp/09_snape_ani/snape_02.png"
    pause.18
    "03_hp/09_snape_ani/snape_03.png"
    pause.18
    "03_hp/09_snape_ani/snape_02.png"
    pause.18
    "03_hp/09_snape_ani/snape_05.png"
    pause.18
    repeat
        
image chibisnape goout: #Default Snape walk animation. 
    im.Flip("03_hp/09_snape_ani/snape_02.png", horizontal=True)     
    pause.18
    im.Flip("03_hp/09_snape_ani/snape_03.png", horizontal=True)     
    pause.18
    im.Flip("03_hp/09_snape_ani/snape_02.png", horizontal=True)     
    pause.18
    im.Flip("03_hp/09_snape_ani/snape_05.png", horizontal=True)     
    pause.18
    repeat

image chibisnape blink: #Snape stands still near the door.
    "03_hp/09_snape_ani/snape_0130.png" #at Position(xpos=610, ypos=210)

