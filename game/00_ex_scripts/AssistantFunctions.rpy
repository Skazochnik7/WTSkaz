init -999 python:
    # assistant functions
     
    def gMakePos( aXPos, aYPos ):
        return Transform( pos = ( aXPos, aYPos ) )
        
    def gSumPos( aPos1, aPos2 ):
        return Transform( pos = ( aPos1.xpos + aPos2.xpos, aPos1.ypos + aPos2.ypos ) )
        
init -998 python:
    # most used positions of hermione sprite
    POS_410 = gMakePos( 410, 0 )
    POS_370 = gMakePos( 370, 0 )
    POS_120 = gMakePos( 120, 0 )
    POS_140 = gMakePos( 140, 0 )
