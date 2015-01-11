init -999 python:

    # to simplify creating ex transforms
    # gExTr( 'flip', vertical = True )
    def gTrEx( aName, **kwargs ):
        dict = {}
        for key,val in kwargs.iteritems():
            dict[ key ] = val
        return CharacterExTransform( aName, dict )


    class CharacterExTransform(store.object):
        
        # aTransformName - code string, aNamedParameters - dictionary with parameters
        #
        # EXAMPLE OF PARAMETERS FOR im.Flip:
        # aTransformName = 'flip'
        # aNamedParameters = { 'vertical' : True, 'horizontal': False }
        # all paramters can be ommited
        #
        def __init__( self, aTransformName, aNamedParameters ):
            self.mName = aTransformName
            self.mParams = aNamedParameters
            self._initVariables()
            
        def apply( self, aImage ):
            # for now, as there are only flip - use if block
            result = aImage
            
            if self.mName == 'flip':
                result = im.Flip( aImage, self.mHor, self.mVer )
                
            return result
            
        def discard( self, aImage ):
            # for now, as there are only flip - use if block
            result = aImage
            
            if self.mName == 'flip':
                result = im.Flip( aImage, self.mHor, self.mVer )
            
            return result
            
        def _initVariables( self ):
            # for now, as there are only flip - use if block
            if self.mName == 'flip':
                self.mHor = False
                self.mVer = False
                param = 'horizontal'
                if param in self.mParams.keys():
                    self.mHor = self.mParams[ param ]
                param = 'vertical'
                if param in self.mParams.keys():
                    self.mVer = self.mParams[ param ]
            