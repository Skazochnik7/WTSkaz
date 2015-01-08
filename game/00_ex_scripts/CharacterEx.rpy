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
            # dictionary with transforms
            self.mTransforms = {}
            # here we'll save all items on Hermione and transforms
            self.mSavedItems = {}
            self.mSavedTransforms = {}
            
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
            
            # varaible, to which this is binded
            self.mBinded = None

            
        # need for using as simple character dialogue
        def __call__( self, what, interact = True ):
            return self.mCh( what, interact = interact )

        # need for using as simple character dialogue
        def predict( self, what ):
            return self.mCh.predict( what )
        
        ##########################################################
        # these methods allow you to bind/unbind current object to another
        # binded object will use mStuff and mTransform from the target one,
        # all other stuff will be unique
        # WARNING operations with state will call methods from binded object, so don't mess the things
        ##########################################################
        
        def bindTo( self, aTarget ):
            self.saveState( True )
            self.mBinded = aTarget
            
        def unbind( self ):
            self.mBinded = None
            self.loadState( True )

        ##########################################################
        # methods to work with global character transforms
        ##########################################################

        def addTransform( self, aTransform, aKey = 'default' ):
            self.delTransform( aKey )            
            self.mTransforms[ aKey ] = aTransform
            
            #apply transform for all items (even hiden)
            for val in self.mStuff.values():
                self._applyTr( aTransform, val, aKey )
            
        def delTransform( self, aKey = 'default' ):
            # discard transform for all items
            if aKey in self.mTransforms.keys():
                for val in self.mStuff.values():
                    self._discardTr( self.mTransforms[ aKey ], val, aKey )
                del self.mTransforms[ aKey ]
        
        # remov all trasnforms
        def clearTransforms( self ):
            if aKey in self.mTransforms.keys():
                self.delTransform( aKey )

        ##########################################################
        # methods to manipulate screen zOrder
        ##########################################################
        #-----------------------------#
        
        # sets/get zOrder of called screen
        def setZOrder( self, zOrder ):
            self.mZOrderScreen = zOrder
            
        def getZOrder( self ):
            return self.mZOrderScreen
       
        #-----------------------------#
        
        ##########################################################
        # methods to manipulate with screen tags
        ##########################################################

        def pushScreenTag( self, aNewScreenTag ):
            self.mTagsStack.append( self.mTagScreen )
            self.mTagScreen = aNewScreenTag
        
        def pullScreenTag( self ):
            if self.mTagsStack:
                self.mTagScreen = self.mTagsStack.pop()
        
        #-----------------------------#
        ##########################################################
        # show/hide screens
        ##########################################################              
        
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

        ##########################################################
        # methods to manipulate items of character
        ##########################################################            
        
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

        # call this to remove all items from character mStuff
        def clear( self ):
            self.mStuff = {}
            
        ##########################################################
        # save/load/clear/copy current item sets
        ##########################################################        
        
        # save current state to variable
        def saveState( self, aKeepLinks = False ):
            if self.mBinded != None:
                self.mBinded.saveState()
                return

            if aKeepLinks:
                self.mSavedItems = self.mStuff
                self.mSavedTransforms = self.mTransforms
            else:
                self.mSavedItems = {}# deepcopy( self.mStuff )
                for key in self.mStuff.keys():
                    self.mSavedItems[ key ] = deepcopy( self.mStuff[ key ] )
                self.mSavedTransforms = {}
                for key in self.mTransforms.keys():
                    self.mSavedTransforms[ key ] = deepcopy( self.mTransforms[ key ] )
    
        # load saved statet
        def loadState( self, aKeepLinks = False ):
            if self.mBinded != None:
                self.mBinded.loadState()
                return
                
            if aKeepLinks:
                self.mStuff = self.mSavedItems
                self.mTransforms = self.mSavedTransforms
            else:
                self.mStuff.clear()
                for key in self.mSavedItems.keys():
                    self.mStuff[ key ] = deepcopy( self.mSavedItems[ key ] )
                self.mTransforms.clear()
                for key in self.mSavedTransforms.keys():
                    self.mTransforms[ key ] = deepcopy( self.mSavedTransforms[ key ] )            
            
        # clears the state
        def clearState( self ):
            if self.mBinded != None:
                self.mBinded.clearState()
                return

            self.mSavedItems = {}
            self.mSavedTransforms = {}

        # call this to copy all items from the other CharacteEx object
        def copyState( self, aCharacterEx ):
            if self.mBinded != None:
                self.mBinded.copyState( aCharacterEx )
                return
            
            self.mStuff.clear()
            for key in aCharacterEx.mStuff.keys():
                self.mStuff[ key ] = deepcopy( aCharacterEx.mStuff[ key ] )
            self.mTransforms.clear()
            for key in aCharacterEx.mTransforms.keys():
                self.mTransforms[ key ] = deepcopy( aCharacterEx.mTransforms[ key ] )
            
        ##########################################################
        # methods to add/del important parts of clothes, but you still can use addItem/delItem methods
        ##########################################################
        
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
            
        # additional function for face to pass only file name
        def addFaceName( self, aFace ):
            self._addItem( 'face', CharacterExItem( self.mFaceFolder, aFace, G_Z_FACE ) )
        
        def addFace( self, aData ):
            self._addItem( 'face', aData )
        def delFace( self ):
            self._delItem( 'face' )
        
        ##########################################################
        # DO NOT CALL CALL THESE METHODS FROM THE OUTER CODE! ONLY FROM THE CLASS, THEY'RE INNER!
        ##########################################################        

        def _addItem( self, aName, aData ):
            aData.onSelfAdded( self.mStuff, self )
            for item in self.mStuff.values():
                item.onItemAdded( aName, aData, self )
            self.mStuff[ aName ] = aData
            # apply current transforms
            for key,val in self.mTransforms.iteritems():
                self._applyTr( val, aData, key )

        def _delItem( self, aName ):
            if aName in self.mStuff.keys():
                data = self.mStuff[ aName ]
                del self.mStuff[ aName ]
                data.onSelfRemoved( self.mStuff, self )
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

        def _applyTr( self, aTransform, aItem, aKey ):
            aItem.addTransform( aKey )
            aItem.updateImage( aTransform.apply( aItem.getImage() ) )
            
        def _discardTr( self, aTransform, aItem, aKey ):
            if aItem.getTransform( aKey ):
                aItem.delTransform( aKey )
                aItem.updateImage( aTransform.discard( aItem.getImage() ) ) 