label main_ex_CharacterExItem_constants:
    # main zOrders
    define G_Z_UNDERLEGS = 0
    define G_Z_LEGS = 20
    define G_Z_PANTIES = 40
    define G_Z_SKIRT = 60
    define G_Z_HANDS = 80
    define G_Z_BODY = 100
    define G_Z_TITS = 120
    define G_Z_DRESS = 140
    define G_Z_FACE = 300
    
    # additional zOrders
    define G_Z_HEADWEAR = 160
    define G_Z_POSE = 180

    # here is the keys for additional items
    define G_N_SKIRT = 'skirt'
    define G_N_BADGE = 'badge'
    define G_N_NETS = 'nets'
    
    return

init -999 python:
    
    class CharacterExItem:

        # create hermione item's description
        def __init__( self, aFolder, aName, aOrder, aParent = None, aPos = None ):
            self.mName = aName
            self.mFileFolder = aFolder
            self.mImage = aFolder + aName
            self.mZOrder = aOrder
            self.mIsVisible = True

            self.mIsAdditional = False            
            self.mItemPos = Transform( pos = ( 0, 0 ) )            
            if aPos is not None:
                self.mItemPos = aPos
                self.mIsAdditional = True
            # here we'll store all items, which affects visibility of this item
            # items, stored here change the visibility to FALSE
            self.mDirectors = set()
            # parent of item, should be string key or None. When parent item is hiden, this item also hide, and the same with showing parent
            self.mParent = aParent

            # here is the list of keys to hide with this item
            self.mHideList = []
            self._fillHideList()
            
            # set with transforms
            self.mTransforms = set()

        ##########################################################
        # modify image methods
        ##########################################################
        
        def updateImage( self, aImage ):
            # here we can change image ( for example, make im.Flip action to the image, and save it here )
            self.mImage = aImage
        
        def getImage( self ):
            return self.mImage
            
        ##########################################################
        # show/hide methods
        ##########################################################

        def hide( self, aSource, aKey, aCharacterEx ):
            prevVis = self.mIsVisible
            self._hideInner( aSource )
            if prevVis != self.mIsVisible:
                aCharacterEx._onItemHiden( aKey )
                for inKey in self.mHideList:
                    aCharacterEx.showItem( inKey, self.__class__.__name__ )
                
        def show( self, aSource, aKey, aCharacterEx ):
            prevVis = self.mIsVisible            
            self._showInner( aSource )
            if prevVis != self.mIsVisible:
                aCharacterEx._onItemShown( aKey )
                for inKey in self.mHideList:
                    aCharacterEx.hideItem( inKey, self.__class__.__name__ )    

        ##########################################################
        # methods for proper transform work
        ##########################################################

        def addTransform( self, aName ):
            self.mTransforms.add( aName )
                
        def delTransform( self, aName ):
            self.mTransforms.discard( aName )

        def getTransform( self, aName ):
            if aName in self.mTransforms:
                return True
            else:
                return False
            
        ##########################################################
        # inner callbacks, do not use them directly
        ##########################################################            

        def onSelfAdded( self, aItems, aCharacterEx ):
            self.innerOnSelfAdded( aItems, aCharacterEx )

        def onSelfRemoved( self, aItems, aCharacterEx ):
            self.innerOnSelfRemoved( aItems, aCharacterEx )
        
        def onItemAdded( self, aItemKey, aItem, aCharacterEx ):
            self.innerOnItemAdded( aItemKey, aItem, aCharacterEx )
            
        def onItemRemoved( self, aItemKey, aItem, aCharacterEx ):
            if aItemKey == self.mParent:
                self._showInner( 'parent' )
            self.innerOnItemRemoved( aItemKey, aItem, aCharacterEx )
            
        def onItemHidden( self, aKey ):
            if aKey == self.mParent:
                self._hideInner( 'parent' )
            self.innerOnItemHidden( aKey )
            
        def onItemShown( self, aKey ):
            if aKey == self.mParent:
                self._showInner( 'parent' )
            self.innerOnItemShown( aKey )

        ##########################################################
        # methods to forget about them :D
        ##########################################################
        def _hideInner( self, aSource ):
            self.mIsVisible = False
            self.mDirectors.add( aSource )
                
        def _showInner( self, aSource ):
            self.mDirectors.discard( aSource )
            if not self.mDirectors:
                self.mIsVisible = True

        ##########################################################
        # methods to override
        ##########################################################

        def _fillHideList( self ):
            # the easiest way to hide other items by this one - add their keys to the self.mHideList in a way:
            # self.mHideList.append( 'name' )
            None
        
        def innerOnSelfAdded( self, aItems, aCharacterEx ):
            # this called when THIS item is added to Hermione
            # we can add additional items, needed for this item, to HermioneView
            for key in self.mHideList:
                aCharacterEx.hideItem( key, self.__class__.__name__ )                  
            
        def innerOnSelfRemoved( self, aItems, aCharacterEx ):
            # this called just after deleting SELF from Hermione
            for key in self.mHideList:
                aCharacterEx.showItem( key, self.__class__.__name__ )                  
        
        def innerOnItemAdded( self, aItemKey, aItem, aCharacterEx ):
            # this called when other new item added to Hermione, and THIS item is existed before it
            # we can add additional items, needed for this item, to HermioneView
            if aItemKey in self.mHideList:
                aCharacterEx.hideItem( aItemKey, self.__class__.__name__ )
            
        def innerOnItemRemoved( self, aItemKey, aItem, aCharacterEx ):
            # this called when other new item added to Hermione, and THIS item is existed before it
            # we can add additional items, needed for this item, to HermioneView
            # item is removed... fuck all!
            #if aItemKey in self.mHideList:
            #    aCharacterEx.showItem( aItemKey, self.__class__.__name__ )
            None

        def innerOnItemHidden( self, aKey ):
            # this called when other item is hidden
            None
            
        def innerOnItemShown( self, aKey ):
            # this called when other item is shown
            None
           