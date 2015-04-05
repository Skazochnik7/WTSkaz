init -997 python:


  
# Класс - персона
    class Person(Entry):
        # constructor 
        def __init__( self, Name, caption, charData=None, defVals=None, constVals=None):
            SetArrayValue(Name, "caption", caption)

            if defVals==None:
                defVals={"liking":0, "whoring":0}

            if charData!=None:
                charData.clearState()
#                viewInfo["view"].attach( viewInfo["vData"] )
#                viewInfo["head"].pushScreenTag( 'head' )
#                viewInfo["head"].attach( viewInfo["vData"] )

                defVals.update({"vData": charData, 
                    "body": CharacterExView( 5, 
                        Character(caption, color="#402313", show_two_window=True, ctc="ctc3", ctc_position="fixed"), "body"+Name ), 
                    "head": CharacterExView( 8, 
                        Character(caption, color="#402313", window_right_padding=220, show_two_window=True, ctc="ctc3", ctc_position="fixed"), "head"+Name ),
                    "pos": constVals["pos_def"], "pos2": constVals["pos2_def"]
                    })

                defVals["body"].attach( charData )
                defVals["head"].pushScreenTag( 'head' )
                defVals["head"].attach( charData )
                defVals["body"].data().addItemSet( Name+'_body' )
                defVals["body"].data().addItemSet( Name+'_start_clothes' )

            defVals.update({"curchar": None, "viewMode": 0})

            super(Person, self).__init__(Name=Name, Type="Person", defVals=defVals, constVals=constVals )

            self.Items=RegEntry(ItemCollection("items"+Name))        # Это словарь сохраняемых аргументов
            self.chibi=RegEntry(Chibi("chibi"+Name))

            return


        def __call__( self, arg1, arg2=None, arg3=None, arg4=None, arg5=None, arg6=None, arg7=None, arg8=None, arg9=None, arg10=None, arg11=None, arg12=None, arg13=None, arg14=None, arg15=None, arg16=None):
            self.__args=[arg1, arg2, arg3, arg4, arg5, arg6, arg7, arg8, arg9, arg10, arg11, arg12, arg13, arg14, arg15, arg16]
            for o in self.__args:
                if o==None:
                    break
                if not isinstance( o, basestring ): # если не строка, значит Character
                    self.curchar=o
                else: # теперь столько строки
                    if o[0]=="~": # если это фейс, то показать его
                        self.Face(o.replace("~",""))    

                        if self.Name!="hero":
                            if self.viewMode in {1, 3}:
                                self.curchar=self.char2
                            else:
                                self.curchar=self.char

                        else:
                            if viewMode==0:
                                for o in GetEntriesByType("Person"):
                                    if o.Name not in {"hero"}:
                                        o.head.hideQ()

                    else:
                        renpy.say(self.curchar, self.__Format(o))
                
            return


        def Face(self, s):
# При подключении Гермионы, поставить условие - если есть точка в параметре - значит это имя файла и нужно не стили менять, а грузить сразу файл лица
            if not " " in s:
                self.body.data().setStyleKey( "face", "face_"+s )
            else:

                self.__temp=s.split(" ")
                for i in range(4):
                    self.body.data().setStyleKey( ['brows', 'eyes', 'blush', 'mouth'][i], self.__temp[i] )

            return


        def __Format(self, s):
            self.__pars=s.split(" ")
            debug.SaveString("Format: "+s, 3)


            s=""
            for o in self.__pars:
                self.__count=0
                if len(o)>=2 and not o.isdigit():
                    for h in o:
                        if h.isalpha() and h.isupper():
                           self.__count+=1
                        if self.__count>=2:
                            o="{size=+4}"+o+"{/size}"
                            break
#                    if o.isupper():
#                        debug.SaveString("isupper: "+o, 3)
                        
                s+=o+" "
            s=s.rstrip(" ")

            if "#(" in s:
                s=s.replace("#(","{size=-4}(") 
                s=s.replace(")","){/size}") 
            return s


        @property
        def pos(self):
            return self.GetValue("pos")
        @pos.setter
        def pos(self, value):
            self.SetValue("pos", value)
            self.body.showQ("", GetValue(value))

        @property
        def pos2(self):
            return self.GetValue("pos2")
        @pos2.setter
        def pos2(self, value):
            self.SetValue("pos2", value)
            self.head.showQ("", GetValue(value))


        @property
        def char(self):
            return self.body.mCh

        @property
        def char2(self):
            return self.head.mCh

        @property
        def curchar(self):
            return self.GetValue("curchar")
        @curchar.setter
        def curchar(self, value):
            self.SetValue("curchar", value)

        @property
        def viewMode(self):
            return self.GetValue("viewMode")
        @viewMode.setter
        def viewMode(self, value):
            self.SetValue("viewMode", value)
            if self.Name!="hero":
                self.body.hideQ()
                self.head.hideQ()
                if self.viewMode in {1, 3}:
                    self.head.showQ("", self.pos2)
                if self.viewMode in {2, 3}:
                    self.body.showQ("", self.pos)  




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
        def body(self):
            return self.GetValue("body")

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

