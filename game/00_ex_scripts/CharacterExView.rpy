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
    class CharacterEx:
        # constructor - memorizing Character object
        def __init__( self, zOrder, aCharacter, aUniqName = 'default' ):
            self.mCh = aCharacter
            self.mUniqName = aUniqName
            # currenlty dressed things
            self.mStuff = {}
            # here we'll save all items on Hermione
            self.mSavedItems = {}
            
            # memorize default pathes
            self.mBodyFolder = "00_ex/00_hermione/body/"
            self.mClothesFolder = "00_ex/00_hermione/clothes/"
            self.mFaceFolder = "00_ex/00_hermione/face/"
            self.mPoseFolder = "00_ex/00_hermione/pose/"
            # z odrder of called screen
            self.mZOrderScreen = zOrder
            self.mTagScreen = self.__class__.__name__ + '_' + self.mUniqName;
            
        # need for using as simple character dialogue
        def __call__( self, what, interact = True ):
            return self.mCh( what, interact = interact )

        # need for using as simple character dialogue
        def predict( self, what ):
            return self.mCh.predict( what )
        
        #-----------------------------#
        
        # sets/get zOrder of called screen
        def setZOrder( self, zOrder ):
            self.mZOrderScreen = zOrder
            
        def getZOrder( self ):
            return self.mZOrderScreen
       
        #-----------------------------#
        
        ## show hermione screen with data parameters
        #def showSelf( self, aData, aPos, aTransition = None ):
        #    #renpy.show_screen( "CharacterExViewScreen", aData, aPos )
        #    self._showView( aData, aPos )
        #    if aTransition is not None:
        #        renpy.with_statement( aTransition )            
        
        ## hide hermione screen
        #def hideSelf( self, aTransition = None ):
        #    #renpy.hide_screen( self.mTagScreen )
        #    self._hideView()
        #    if aTransition is not None:
        #        renpy.with_statement( aTransition )            
        #    
        #-----------------------------#
        
        # show hermione screen with saved parameters
        def showQ( self, aFace, aPos, aTransition = None ):
            if aFace is not None:
                self.addFace( CharacterExItem( self.mFaceFolder, aFace, G_Z_FACE ) )
            #renpy.show_screen( "CharacterExViewScreen", self.mStuff, aPos )
            self._showView( self.mStuff, aPos )
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

        #------------------------------#
        
        # call this to remove all items from hermione mStuff
        def clear():
            self.mStuff = {}
        
        #------------------------------#
            
        # return Item if Hermione get the item with given key, otherwise - None
        def getItem( self, aKey ):
            if aKey in self.mStuff.keys():
                return self.mStuff[ aKey ]
            else:
                return None
                
        # add additional stuff on hermione ( permanent )
        def addItem( self, aKey, aCharacterExItem ):
            self._addItem( aKey, aCharacterExItem )
        
        # del additional stuff on hermione ( permanent )
        def delItem( self, aKey ):
            self._delItem( aKey )

        # show item on hermione ( make it visible )
        def showItem( self, aKey, aSource = 'game' ):
            if aKey in self.mStuff.keys():
                item = self.mStuff[ aKey ]
                item.show( aSource, aKey, self )

        # hide item on hermione ( make it invisible )
        def hideItem( self, aKey, aSource = 'game' ):
            if aKey in self.mStuff.keys():
                item = self.mStuff[ aKey ]
                item.hide( aSource, aKey, self )
            
        #------------------------------#
        
        # save/load/clear current items set
        def saveState( self ):
            self.mSavedItems = deepcopy( self.mStuff )
    
        def loadState( self ):
            self.mStuff.clear()
            for key in self.mSavedItems:
                self.mStuff[ key ] = deepcopy( self.mSavedItems[ key ] )
            
        def clearState( self ):
            self.mSavedItems = {}
            
        #------------------------------#

        # methods to add/del important parts of clothes, but you still can use addItem/delItem methods
        
        def addLegs( self, aData ):
            self._addItem( 'legs', aData )
        def delLegs( self ):
            self._delItem( 'legs' )
            
        def addHands( self, aData ):
            self._addItem( 'hands', aData )
        def delHands( self ):
            self._delItem( 'hands' )
            
        def addPanties( self, aData ):
            self._addItem( 'panties', aData )
        def delPanties( self ):
            self._delItem( 'panties' )

        def addSkirt( self, aData ):
            self._addItem( 'skirt', aData )
        def delSkirt( self ):
            self._delItem( 'skirt' )
            
        def addBody( self, aData ):
            self._addItem( 'body', aData )
        def delBody( self ):
            self._delItem( 'body' )
            
        def addDress( self, aData ):
            self._addItem( 'dress', aData )
        def delDress( self ):
            self._delItem( 'dress' )
            
        def addTits( self, aData ):
            self._addItem( 'tits', aData )
        def delTits( self ):
            self._delItem( 'tits' )
            
        def addPose( self, aData ):
            self._addItem( 'pose', aData )
        def delPose( self ):
            self._delItem( 'pose' )
            
        #additional function for face to pass only file name
        def addFaceName( self, aFace ):
            self._addItem( 'face', CharacterExItem( self.mFaceFolder, aFace, G_Z_FACE ) )
        
        def addFace( self, aData ):
            self._addItem( 'face', aData )
        def delFace( self ):
            self._delItem( 'face' )

        #------------------------------#
        
        #DO NOT CALL CALL THESE METHODS FROM THE OUTER CODE! ONLY FROM THE CLASS, THEY'RE INNER!
        def _addItem( self, aName, aData ):
            aData.onSelfAdded( self.mStuff, self )
            for item in self.mStuff.values():
                item.onItemAdded( aName, aData, self )
            self.mStuff[ aName ] = aData

        def _delItem( self, aName ):
            if aName in self.mStuff.keys():
                data = self.mStuff[ aName ]
                data.onSelfRemoved( self.mStuff, self )
                del self.mStuff[ aName ]
                for item in self.mStuff.values():
                    item.onItemRemoved( aName, data, self )        
    
        def _showView( self, aData, aPos ):
            oldOrder = store._CharacterExViewScreenZOrder
            store._CharacterExViewScreenZOrder = self.mZOrderScreen
            renpy.show_screen( "CharacterExViewScreen", aData, aPos, _tag = self.mTagScreen )
            
        def _hideView( self ):
            renpy.hide_screen( self.mTagScreen )
            
        def _onItemHiden( self, aKey ):
            for item in self.mStuff.values():
                item.onItemHidden( aKey )  
            
        def _onItemShown( self, aKey ):
            for item in self.mStuff.values():
                item.onItemShown( aKey )  