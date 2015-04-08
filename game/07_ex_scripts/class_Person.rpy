init -997 python:


  
# Класс - персона
    class Person(Entry):
        # constructor 
        def __init__( self, Name, caption, charData=None, defVals=None, constVals=None):
            SetArrayValue(Name, "caption", caption)

            if defVals==None:
                defVals={"liking":0, "whoring":0}
            else:
                defVals.update({"liking":0, "whoring":0})

            if charData!=None:
                charData.clearState()
                defVals.update({"vData": charData, 
                    "body": CharacterExView( 5, 
                        Character(caption, color="#402313", show_two_window=True, ctc="ctc3", ctc_position="fixed"), "body"+Name ), 
                    "head": CharacterExView( 8, 
                        Character(caption, color="#402313", window_right_padding=220, show_two_window=True, ctc="ctc3", ctc_position="fixed"), "head"+Name )
                    })

                defVals["body"].attach( charData )
                defVals["head"].pushScreenTag( 'head' )
                defVals["head"].attach( charData )
                defVals["body"].data().addItemSet( Name+'_body' )
                defVals["body"].data().addItemSet( Name+'_start_clothes' )

            defVals.update({"curchar": None, "talkingView": "body", "Visible": False})

            super(Person, self).__init__(Name=Name, Type="Person", defVals=defVals, constVals=constVals )

#            self.LoadDefItemSets()

            self.Items=RegEntry(ItemCollection("items"+Name))        # Это словарь сохраняемых аргументов
            self.chibi=RegEntry(Chibi("chibi"+Name))

            return


        def __call__( self, arg1, arg2=None, arg3=None, arg4=None, arg5=None, arg6=None, arg7=None, arg8=None, arg9=None, arg10=None, 
                        arg11=None, arg12=None, arg13=None, arg14=None, arg15=None, arg16=None, arg17=None, arg18=None, arg19=None, 
                        arg20=None, arg21=None, arg22=None, arg23=None, arg24=None):
#            self.__argstemp=[arg1, arg2, arg3, arg4, arg5, arg6, arg7, arg8, arg9, arg10, arg11, arg12, arg13, arg14, arg15, arg16, arg17, arg18, arg19, arg20, arg21, arg22, arg23, arg24]
            self.__args=[]
            for o in [arg1, arg2, arg3, arg4, arg5, arg6, arg7, arg8, arg9, arg10, arg11, arg12, arg13, arg14, arg15, arg16, arg17, arg18, arg19, arg20, arg21, arg22, arg23, arg24]:
                if o==None:
                    break
                if isinstance( o, ADVCharacter ): # Если ADVCharacter, то добавляем в массив
                    self.__args.append(o)
                else: # Иначе - разбираем на подстроки
                    debug.SaveString("o: "+str(o), 3)
                    for p in o.split("//"):
                        debug.SaveString("p: "+str(p), 3)
                        if p!=None:
                            if p.strip()!=None:
                                self.__args.append(p.strip(" "))
                                debug.SaveString("p.strip: "+str(p.strip(" ")), 3)

            self.__trans=d3
            if not self.GetValue("Visible"):
                self.Visibility(self._talkingView, True, self.__trans)
            for o in self.__args:
                if o==None:
                    break
                if not isinstance( o, basestring ): # если не строка, значит Character
                    self.curchar=o
                else: # теперь столько строки
                    if o[0]=="~": # если это фейс, то показать его
                        debug.SaveString("face: "+str(o), 3)
                        self.Face(o.replace("~",""))    
#                        self.Visibility(self._talkingView, True, self.__trans)


#                        self.__trans=None

#                        self.Visibility(self._talkingView)

#                        if self.Name!="hero":
#                            if self.viewMode in {1, 3}:
#                                self.curchar=self.char2
#                            else:
#                                self.curchar=self.char

#                        else:
#                            if self.viewMode==0:
#                                for o in GetEntriesByType("Person"):
#                                    if o.Name not in {"hero"}:
#                                        o.head.hideQ()

                    else:
                        if self.Name=="hero": 
                            for p in GetEntriesByType("Person"):
                                if p.Name not in {"hero"}:
                                    if "body+" not in p._talkingView:
                                        p.body.hideQ()
                                        p.SetValue("Visible", False)
                                    if "head+" not in p._talkingView:
                                        p.head.hideQ()
#                                        p.SetValue("Visible", False)
                        renpy.say(self.curchar, self.__Format(o))

                
            return


        def Face(self, s):
# При подключении Гермионы, поставить условие - если есть точка в параметре - значит это имя файла и нужно не стили менять, а грузить сразу файл лица
            if not " " in s:
                if "." in s:
                    self.body.addFaceName( s )
                else:
                    self.body.data().setStyleKey( "face", "face_"+s )
            else:

                self.__temp=s.split(" ")
                for i in range(4):
                    self.body.data().setStyleKey( ['brows', 'eyes', 'blush', 'mouth'][i], self.__temp[i] )

            return



        def LoadDefItemSets(self):
            self.body.data().addItemSet( self.Name+'_body' )
            self.body.data().addItemSet( self.Name+'_start_clothes' )
            return


        def __Format(self, s):
            self.__pars=s.split(" ")
#            debug.SaveString("Format: "+s, 3)


            s=""
            for o in self.__pars:
                self.__count=0
                if len(o)>=2 and not o.isdigit():
                    for h in o:
                        if h.isalpha() and h.isupper():
                           self.__count+=1
                        if self.__count>=2:
                            o="{size=+5}"+o+"{/size}"
                            break
#                    if o.isupper():
#                        debug.SaveString("isupper: "+o, 3)
                        
                s+=o+" "
            if s!=None:
                s=s.strip(" ")

            if "#(" in s: #  "Бла бла #(тралала) бла бла" => "Бла бла {size=-3}(тралала){/size} бла бла"
                s=s.replace("#(","{size=-3}(") 
                s=s.replace(")","){/size}") 
            else:
                if len(s)>1:
                    if s[0]=="#": #  "#Бла бла (тралала) бла бла" => "{size=-3}Бла бла (тралала) бла бла{/size}"
                        s="{size=-3}"+s[1:]+"{/size}"
                if len(s)>3:
                    debug.SaveString("format.s[:2]: "+str(s[:2]), 3)
                    if s[:2] in {"{-", "{+"}: #  "{-5}Бла бла (тралала) бла бла" => "{size=-5}Бла бла (тралала) бла бла{/size}"
                        s="{size="+s[1:3]+s[3:]+"{/size}"

            debug.SaveString("format: "+str(s), 3)

            return s


        def Visibility(self, talkingView=" ", isTalking=True, transition=None):
            self.SetValue("talkingView", talkingView)
            if self.Name!="hero":
                if (isTalking and ('head' in self._talkingView)) or ('head+' in self._talkingView): 
                    self.head.showQ(None, self.pos2, transition)
#                    self.SetValue("Visible", True)
                else:
                    self.head.hideQ(transition)
#                    self.SetValue("Visible", False)
                    self.curchar=self.char
                if (isTalking and ('body' in self._talkingView)) or ('body+' in self._talkingView):  
                    self.body.showQ(None, self.pos, transition)
                    self.SetValue("Visible", True)
                else:
                    self.body.hideQ(transition)
                    self.SetValue("Visible", False)
                    self.curchar=self.char2
            return self



        @property
        def pos(self):
            return self.GetValue("pos")
        @pos.setter
        def pos(self, value):
            self.SetValue("pos", value)
            self.body.showQ(None, GetValue(value))

        @property
        def pos2(self):
            return self.GetValue("pos2")
        @pos2.setter
        def pos2(self, value):
            self.SetValue("pos2", value)
            self.head.showQ(None, GetValue(value))


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

