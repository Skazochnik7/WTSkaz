init -999 python:
    class CharacterExDebuger:

        @staticmethod
        def Log( aDebugMessage ):
            if 'debug' in globals():
                #debug variable is defined
                debug.SaveString( aDebugMessage, 0 )
            else:
                None

        @staticmethod
        def LogE( aDebugMessage ):
            if 'debug' in globals():
                #debug variable is defined
                debug.SaveString( 'ERROR: ' + aDebugMessage, 0 )
            else:
                None