init -997 python:


  
# Класс - обертка для словаря ивентов
    class Person(Entry):
        # constructor - Event initializing
        def __init__( self, Name, caption, viewInfo=None, defVals=None):
            SetArrayValue(Name, "caption", caption) 

            if defVals==None:
                defVals={"liking":0, "whoring":0}

            if viewInfo!=None:
                viewInfo["vData"].clearState()
                viewInfo["view"].attach( viewInfo["vData"] )
                viewInfo["head"].pushScreenTag( 'head' )
                viewInfo["head"].attach( viewInfo["vData"] )


                viewInfo["view"].data().addItemSet( viewInfo["view"].mUniqName+'_body' )
                viewInfo["view"].data().addItemSet( viewInfo["view"].mUniqName+'_start_clothes' )
                

                defVals.update({"vData": viewInfo["vData"], "view": viewInfo["view"], "head": viewInfo["head"]})


            super(Person, self).__init__(Name=Name, Type="Person", defVals=defVals )

            self.Items=RegEntry(ItemCollection("items"+self.Name))        # Это словарь сохраняемых аргументов
            self.chibi=RegEntry(Chibi("chibi"+Name))

            return

        def SetFace(self, s):
            _temp=s.split(" ")
            for i in range(4):
                daphne.view.data().setStyleKey( ['brows', 'eyes', 'blush', 'mouth'][i], _temp[i] )
            return

        def ChibiShow(self, images):
            for o in images:
#                if chibiTranses[o]
                renpy.show_screen(Name+"screen", chibiTranses[o]["image"], None)
                renpy.pause()
            return

        def ChibiTrans(self, image, trans=None):
            renpy.show_screen(self.Name+"screen", image, trans)
            renpy.pause()
            return


        @property
        def liking(self):
            return self.GetValue("liking")
        @liking.setter
        def liking(self, value):
            self.SetValue("liking", value, minim=-100, maxim=0)

        @property
        def whoring(self):
            return self.GetValue("whoring")
        @whoring.setter
        def whoring(self, value):
            self.SetValue("whoring", value, minim=0)

        @property
        def view(self):
            return self.GetValue("view")

        @property
        def head(self):
            return self.GetValue("head")





# При таком описании проперти объект корретно сохранялся/читался
#        @property
#        def liking(self):
#            return self.GetValue("test")
#        @liking.setter
#        def liking(self, value):
#            if renpy.store.whoring>0:
#                renpy.store.whoring+=1
#            self.SetValue("test", value)

