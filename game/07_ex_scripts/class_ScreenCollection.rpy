init -998 python:
  
# Класс - 
    class ScreenCollection(store.object):
        def __init__( self): # ELog:
            self.Name="screens"
            return 

                
        def Show(self, names, transition=None):
            for o in names:
                renpy.show_screen( o )    
                if transition is not None:
                    renpy.with_statement( transition, None, True )
            return

        def ShowAndHide(self, name, lag, transition=None):
            self.ScreensShow([name], transition)
            renpy.pause(lag)
            self.ScreensHide([name], transition)

        def Hide(self, names, transition=None):
            for o in names:
                renpy.hide_screen( o )    
                if aTransition is not None:
                    renpy.with_statement( aTransition, None, True )
            return