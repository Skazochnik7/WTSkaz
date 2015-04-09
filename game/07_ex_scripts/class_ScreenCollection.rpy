init -998 python:
  
# Класс - 
    class ScreenCollection(store.object):
        def __init__( self): # ELog:
            self.Name="screens"
            return 

# Внутренняя - не вызывается
        def __Action(self, name, isshow, position=None):
            self.__transition=None
            for o in name:
                if isinstance( o, basestring ):
                    if isshow:
                        if position==None:
                            renpy.show_screen( o )
                        else:    
                            renpy.show_screen( o , position) 
                    else:
                        renpy.hide_screen( o ) 
                    if self.__transition is not None:
                        renpy.with_statement( self.__transition, None, True )
                else:
                    self.__transition=o
            return self

# Показать набор экранов и транзишинов. Внимание! Транзишин в строке запоминается и используется при показе последющих экранов. 
# Он идет впереди названия экрана  например screens.Show(d3, "bld1")              
        def Show(self, arg1, arg2=None, arg3=None, arg4=None, arg5=None):
            return self.__Action([arg1, arg2, arg3, arg4, arg5], True, None)

# Показать экран, выдержать паузу и спрятать
        def ShowHide(self, arg1, arg2, arg3=None):
            if arg3==None:
                self.__transition=None
                self.__name=arg1
                self.__lag=arg2
            else:
                self.__transition=arg1
                self.__name=arg2
                self.__lag=arg3

            self.Show(self.__transition, self.__name )
            renpy.pause(self.__lag)
            self.Hide(self.__transition, self.__name )
            return self

# Скрыть экран
        def Hide(self, arg1, arg2=None, arg3=None, arg4=None, arg5=None):
            return self.__Action([arg1, arg2, arg3, arg4, arg5], False, None)

# Show, начиная с d3
        def ShowD3(self, arg1, arg2=None, arg3=None, arg4=None, arg5=None):
            return self.__Action([Dissolve(.3), arg1, arg2, arg3, arg4, arg5], True, None)

# Hide, начиная с d3
        def HideD3(self, arg1, arg2=None, arg3=None, arg4=None, arg5=None):
            return self.__Action([Dissolve(.3), arg1, arg2, arg3, arg4, arg5], False, None)

# Пауза (для построения цепочек)
        def Pause(self, lag=None):
            renpy.pause(lag)
            return self

#  Показать персонажа в позиции
        def ShowPos(self, arg1, arg2, arg3=None):
            if arg3==None:
                self.__transition=None
                self.__name=arg1
                self.__pos=arg2
            else:
                self.__transition=arg1
                self.__name=arg2
                self.__pos=arg3
            return self.__Action([self.__transition, self.__name], True, self.__pos)

# Реплика без персонажа, чтобы можно было строить строки типа screens.Hide("myscreen").Say("Бла-бла-бла").Show("myscreen")
        def Say(self, arg1, arg2=None, arg3=None, arg4=None, arg5=None, arg6=None, arg7=None, arg8=None, arg9=None, arg10=None):
            self.__args=[]
            for o in [arg1, arg2, arg3, arg4, arg5, arg6, arg7, arg8, arg9, arg10]:
                if o==None:
                    break
                else:
                    for p in o.split("//"):
                        if p!=None:
                            if p.strip()!=None:
                                self.__args.append(p.strip(" "))

            for o in self.__args:
                if o==None:
                    break
                else:
                    renpy.say("", StringFormat(o))
            return self
