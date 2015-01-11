screen CharacterExViewScreen( aData, aPos ):   
    python:
        dataToSort = aData.values()
        sorted_data = sorted( dataToSort, key = lambda item: item.mZOrder )
    for element in sorted_data:
        if element.mIsVisible == True:
            if element.mIsAdditional == False:
                add element.getImage() at aPos
            else:
                add element.getImage() at gSumPos( aPos, element.mItemPos )
    
    #this variable is defined below, it's changed from the CharacterEx class
    zorder _CharacterExViewScreenZOrder

init -999 python:
    _CharacterExViewScreenZOrder = 0

init -998 python:
    from copy import deepcopy 
    class CharacterExView(store.object):
        # constructor - memorizing Character object
        def __init__( self, zOrder, aCharacter, aUniqName = 'default' ):
            self.mCh = aCharacter
            self.mUniqName = aUniqName
            
            # memorize default pathes
            self.mBodyFolder = "00_ex/00_hermione/body/"
            self.mClothesFolder = "00_ex/00_hermione/clothes/"
            self.mFaceFolder = "00_ex/00_hermione/face/"
            self.mPoseFolder = "00_ex/00_hermione/pose/"
            self.mMiscFolder = "00_ex/00_hermione/misc/"

            # z odrder of called screen
            self.mZOrderScreen = zOrder
            self.mTagScreen = self.__class__.__name__ + '_' + self.mUniqName;
            
            # stack for view tags
            self.mTagsStack = []

            # attached data
            self.mData = None

            
        # need for using as simple character dialogue
        def __call__( self, what, interact = True ):
            return self.mCh( what, interact = interact )

        # need for using as simple character dialogue
        def predict( self, what ):
            return self.mCh.predict( what )
        
        ##########################################################
        # methods operate with CharacterExData
        ##########################################################
        
        def attach( self, aData ):
            self.mData = aData
            aData.attachedToView( self )
            
        def detach( self ):
            self.mData = None
            aData.detachedFromView( self )
            
        def data( self ):
            return self.mData

        ##########################################################
        # methods to manipulate screen zOrder
        ##########################################################
        
        # sets/get zOrder of called screen
        def setZOrder( self, zOrder ):
            self.mZOrderScreen = zOrder
            
        def getZOrder( self ):
            return self.mZOrderScreen
       
        ##########################################################
        # methods to manipulate with screen tags
        ##########################################################

        def pushScreenTag( self, aNewScreenTag ):
            self.mTagsStack.append( self.mTagScreen )
            self.mTagScreen = aNewScreenTag
        
        def popScreenTag( self ):
            if self.mTagsStack:
                self.mTagScreen = self.mTagsStack.pop()
        
        ##########################################################
        # show/hide screens
        ##########################################################              
        
        # show hermione screen with saved parameters
        def showQ( self, aFace, aPos, aTransition = None ):
            if aFace is not None:
                self.mData.addFace( CharacterExItem( self.mFaceFolder, aFace, G_Z_FACE ) )
            #renpy.show_screen( "CharacterExViewScreen", self.mStuff, aPos )
            self._showView( self.mData.mStuff, aPos )
            if aTransition is not None:
                renpy.with_statement( aTransition, None, True )
        
        # hide hermione screen
        def hideQ( self, aTransition = None ):
            self._hideView()
            if aTransition is not None:
                renpy.with_statement( aTransition )
                
        # below is two methods to simplifying typing
        def showQQ( self, aFace, aPos ):
            self.showQ( aFace, aPos, d3 )

        def hideQQ( self ):
            self.hideQ( d3 )
            
        ##########################################################
        # helper methods
        ##########################################################     
        
        
        # additional function for face to pass only file name
        def addFaceName( self, aFace ):
            self.mData.addItem( 'face', CharacterExItem( self.mFaceFolder, aFace, G_Z_FACE ) )

        ##########################################################
        # DO NOT CALL CALL THESE METHODS FROM THE OUTER CODE! ONLY FROM THE CLASS, THEY'RE INNER!
        ##########################################################
    
        def _showView( self, aData, aPos ):
            oldOrder = store._CharacterExViewScreenZOrder
            store._CharacterExViewScreenZOrder = self.mZOrderScreen
            renpy.show_screen( "CharacterExViewScreen", aData, aPos, _tag = self.mTagScreen )
            
        def _hideView( self ):
            renpy.hide_screen( self.mTagScreen )
