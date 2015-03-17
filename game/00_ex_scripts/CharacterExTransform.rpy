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
        def __init__( self, aTransformName, aNamedParameters, aId = "" ):
            self.mId = aId   # unique key for transform
            self.mName = aTransformName
            self.mParams = aNamedParameters # map with (string-value)
            self._initVariables()
           
        # static constructor to create from description
        @classmethod
        def create( cls, aDescription ):
            item = cls( aDescription.mName, aDescription.mParams, aDescription.mId )
            return item

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
                    self.mHor = wtxml_parseBool( self.mParams[ param ] ) #from WTXmlAssitantFunctions
                param = 'vertical'
                if param in self.mParams.keys():
                    self.mVer = wtxml_parseBool( self.mParams[ param ] ) #from WTXmlAssitantFunctions
            