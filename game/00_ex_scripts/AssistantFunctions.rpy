init -999 python:
    # assistant functions
    
    def gMakePos( aXPos, aYPos ):
        return Transform( pos = ( aXPos, aYPos ) )
        
    def gSumPos( aPos1, aPos2 ):
        return Transform( pos = ( aPos1.xpos + aPos2.xpos, aPos1.ypos + aPos2.ypos ) )
