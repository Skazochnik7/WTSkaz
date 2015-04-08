init -998 python:
  
# Класс - 
    class ScreenCollection(store.object):
        def __init__( self): # ELog:
            self.Name="screens"
            return 

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
                
        def Show(self, arg1, arg2=None, arg3=None, arg4=None, arg5=None):
            return self.__Action([arg1, arg2, arg3, arg4, arg5], True, None)

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

        def Hide(self, arg1, arg2=None, arg3=None, arg4=None, arg5=None):
            return self.__Action([arg1, arg2, arg3, arg4, arg5], False, None)

        def ShowD3(self, arg1, arg2=None, arg3=None, arg4=None, arg5=None):
            return self.__Action([Dissolve(.3), arg1, arg2, arg3, arg4, arg5], True, None)

        def HideD3(self, arg1, arg2=None, arg3=None, arg4=None, arg5=None):
            return self.__Action([Dissolve(.3), arg1, arg2, arg3, arg4, arg5], False, None)

        def Pause(self, lag=None):
            renpy.pause(lag)
            return self

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

