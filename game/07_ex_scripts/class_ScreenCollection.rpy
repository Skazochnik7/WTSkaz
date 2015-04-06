init -998 python:
  
# Класс - 
    class ScreenCollection(store.object):
        def __init__( self): # ELog:
            self.Name="screens"
            return 

        def __Action(self, name, isshow, transition=None, position=None):
            if isinstance( name, basestring ):
                name=[name]
            for o in name:
                if isshow:
                    if position==None:
                        renpy.show_screen( o )
                    else:    
                        renpy.show_screen( o , position) 
                else:
                    renpy.hide_screen( o ) 
                if transition is not None:
                    renpy.with_statement( transition, None, True )
                
        def Show(self, names, transition=None, position=None):
            self.__Action(names, True, transition, position)
            return

        def ShowAndHide(self, name, lag, transition=None, position=None):
            self.ScreensShow([name], transition)
            renpy.pause(lag)
            self.ScreensHide([name], transition)

        def Hide(self, names, transition=None, position=None):
            self.__Action(names, False, transition, position)
            return
