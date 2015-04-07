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

        def ShowHide(self, name, lag, transition=None):
            self.Show(transition, name )
            renpy.pause(lag)
            self.Hide(transition, name )
            return self

        def Hide(self, arg1, arg2=None, arg3=None, arg4=None, arg5=None):
            return self.__Action([arg1, arg2, arg3, arg4, arg5], False, None)

        def ShowD3(self, arg1, arg2=None, arg3=None, arg4=None, arg5=None):
            return self.__Action([d3, НЕ будет работать, наждо найти аналог d3 arg1, arg2, arg3, arg4, arg5], True, None)

        def HideD3(self, arg1, arg2=None, arg3=None, arg4=None, arg5=None):


        def ShowPos(self, name, position, transition=None):
            return self.__Action([transition, name], True, position)

