init -998 python:
    __EData_Add = 0
    __EData_Remove = 1
    __EData_Show = 2
    __EData_Hide = 3
    __EData_Style = 4

    import re
    from copy import deepcopy

    class CharacterExData(store.object):
        # constructor - memorizing Character object
        def __init__( self, aLinkerKey ):
            self.mLinkerKey = aLinkerKey    #special key to ask XmlLinker for apropriate objects
            # currenlty dressed things
            self.mItems = {}
            # dictionary with transforms
            self.mTransforms = {}
            # here we'll save all items and global transforms on character
            self.mSavedItems = {}
            self.mSavedTransforms = {}
            # list of all attached views
            self.mViews = []
            # object to create items from description in xml files
            #self.mCreator = aItemCreator
           
        ##########################################################
        # methods to save/delete attached views
        ##########################################################

        def getView( self, aIndex = 0 ):
            if aIndex < len( self.mViews ):
                return self.mViews[ aIndex ]
            else:
                return None

        def attachedToView( self, aView ):
            self.mViews.append( aView )

        def detachedFromView( self, aView ):
            if aView in self.mViews:
                self.mViews.remove( aView )

        ##########################################################
        # methods to work with global character transforms
        ##########################################################

        def addTransform( self, aTransform, aKey = 'default' ):
            self.delTransform( aKey )
            #apply transform for all items (even hidden)
            for val in self.mItems.values():
                val.addTransform( aKey, aTransform )
            self.mTransforms[ aKey ] = aTransform
            
        def delTransform( self, aKey = 'default' ):
            # discard transform for all items
            if aKey in self.mTransforms.keys():
                del self.mTransforms[ aKey ]
                for val in self.mItems.values():
                    val.delTransform( aKey )
        
        # remove all transforms
        def clearTransforms( self ):
            keys = self.mTransforms.keys()
            for key in keys:
                self.delTransform( key )
            self.mTransforms.clear()

        ##########################################################
        # methods to manipulate items of character
        ##########################################################            
        
        # return Item if Hermione get the item with given key, otherwise - None
        def getItemKey( self, aKey ):
            if aKey in self.mItems.keys():
                return self.mItems[ aKey ]
            else:
                return None

        # return Item if Hermione get the item with given name, otherwise - None
        def getItem( self, aItemName ):
            key = self._getItemKeyByName( aItemName )
            if key in self.mItems.keys():
                item = self.mItems[ key ]
                if item.mName == aItemName:
                    return item
            return None

        #===================================================#
        # add additional stuff on hermione ( permanent )
        def addItemDirect( self, aKey, aCharacterExItem ):
            # debug
            CharacterExDebuger.Log( 'CharacterExData::addItemDirect: aKey = ' + aKey )
            if not aCharacterExItem:
                CharacterExDebuger.LogE( 'CharacterExData::addItemDirect: aCharacterExItem = None' )
            self._addItem( aKey, aCharacterExItem )

        # add item to character with specific key
        def addItemKey( self, aKey, aName, aStyle = 'default' ):
            # debug
            CharacterExDebuger.Log( 'CharacterExData::addItemKey: aKey = ' + aKey + ', aName = ' + aName + ', aStyle = ' + aStyle )
            newItem = WTXmlLinker.c( self.mLinkerKey ).create( aName, aStyle )
            if newItem[0] != None:
                self.addItemDirect( aKey, newItem[0] )

        # add item to character, key info is get from item's data
        def addItem( self, aName, aStyle = 'default' ):
            # debug
            CharacterExDebuger.Log( 'CharacterExData::addItem: aName = ' + aName + ', aStyle = ' + aStyle )            
            newItem = WTXmlLinker.c( self.mLinkerKey ).create( aName, aStyle )
            if newItem[0] != None:
                self.addItemDirect( newItem[0].mKey, newItem[0] )

        def addItemSet( self, aSetName, aStyle = 'default' ):
            # debug
            CharacterExDebuger.Log( 'CharacterExData::addItemSet: aSetName = ' + aSetName + ', aStyle = ' + aStyle )
            self._applyToSet( aSetName, __EData_Add, aStyle )

        #===================================================#
        # delete item by key
        def delItemKey( self, aKey ):
            self._delItem( aKey )

        # delete item by it's name
        def delItem( self, aItemName ):
            key = self._getItemKeyByName( aItemName )
            self._delItem( key, aItemName )

        def delItemSet( self, aSetName ):
            self._applyToSet( aSetName, __EData_Remove )

        #===================================================#
        # show item by key
        def showItemKey( self, aKey, aSource = 'game' ):
            self._showItem( aKey, aSource )

        # show item by it's name
        def showItem( self, aItemName, aSource = 'game' ):
            key = self._getItemKeyByName( aItemName )
            self._showItem( key, aSource, aItemName )

        # show item set on character
        def showItemSet( self, aSetName, aSource = 'game' ):
            self._applyToSet( aSetName, __EData_Show, aSource )

        #===================================================#
        # hide item by key
        def hideItemKey( self, aKey, aSource = 'game' ):
            self._hideItem( aKey, aSource )

        def hideItem( self, aItemName, aSource = 'game' ):
            key = self._getItemKeyByName( aItemName )
            self._hideItem( key, aSource, aItemName )

        # hide item set on character
        def hideItemSet( self, aSetName, aSource = 'game' ):
            self._applyToSet( aSetName, __EData_Hide, aSource )

        #===================================================#
        # try to apply the style to all items. Only items which has such style will be affected
        def setStyleAll( self, aStyleName ):
            for item in self.mItems.values():
                item.setStyle( aStyleName )

        # set style to item by key
        def setStyleKey( self, aKey, aStyleName ):
            self._setStyle( aKey, aStyleName )

        # set style to item
        def setStyleItem( self, aItemName, aStyleName ):
            key = self._getItemKeyByName( aItemName )
            self._setStyle( key, aStyleName, aItemName )

        # set style to all items in set
        def setStyleSet( self, aSetName, aStyleName ):
            self._applyToSet( aSetName, __EData_Style, aStyleName )

        #===================================================#
        # return True, if the item with such name exists in items on given position
        def checkItemKeyName( self, aKey, aName ):
            if aKey in self.mItems.keys():
                item = self.mItems[ aKey ]
                if item.mName == aName:
                    return True
            return False

        # return True, if the item with such style name exists in items on given position
        def checkItemKeyStyle( self, aKey, aStyleName ):
            if aKey in self.mItems.keys():
                item = self.mItems[ aKey ]
                if item.getStyle() == aStyleName:
                    return True
            return False

        # return True, if the item with such style name  and such style exists in items
        def checkItemNameStyle( self, aItemName, aStyleName ):
            key = self._getItemKeyByName( aItemName )
            return self.checkItemKeyStyle( key, aStyleName )

        #===================================================#
        # calling this will change the frame of the item
        # will be acted like we removed the item and added a new one (for actions of items)
        def updateItemFrameKey( self, aKey, aNewFrameName, aNewFrameFolder = None ):
            if aKey in self.mItems.keys(): 
                item = self.mItems[ aKey ]
                frameFolder = aNewFrameFolder
                if frameFolder == None:
                    frameFolder = item.mFileFolder
                item.changeImage( frameFolder, aNewFrameName, True )

        # as previous, but instead key of item - the name of item is used to find the necessary item
        def updateItemFrameName( self, aItemName, aNewFrameName, aNewFrameFolder = None ):
            key = self._getItemKeyByName( aItemName )
            self.updateItemFrameKey( key, aNewFrameName, aNewFrameFolder )

        #===================================================#
        # call this to apply preset for current items
        def applyPreset( self, aPresetName, aActualTemplateParams = None ):
            preset = WTXmlLinker.p( self.mLinkerKey ).get( aPresetName )
            if preset:
                actualsArray = aActualTemplateParams
                # if the actual params variable is string - split it into string array
                if isinstance( aActualTemplateParams, basestring ):
                    actualsArray = re.split( ',|\.| ', aActualTemplateParams )
                presetItems = preset.getItems( actualsArray )
                for item in presetItems:
                    self._applyPresetItem( item )

        #===================================================#
        # call this to remove all items from character mItems
        def clear( self ):
            self.mItems.clear()

        # special stuff for actions - return all current items in data
        def getAllItems( self ):
            return self.mItems
            
        ##########################################################
        # save/load/clear/copy current item sets
        ##########################################################        
        
        # save current state to variable
        def saveState( self ):
            self.mSavedItems = {}# deepcopy( self.mItems )
            for key in self.mItems.keys():
                self.mSavedItems[ key ] = CharacterExItem.fromItem( self.mItems[ key ] )
            self.mSavedTransforms = {}
            for key in self.mTransforms.keys():
                self.mSavedTransforms[ key ] = deepcopy( self.mTransforms[ key ] )
    
        # load saved state
        def loadState( self ):
            self.mItems.clear()
            for key in self.mSavedItems.keys():
                self.mItems[ key ] = CharacterExItem.fromItem( self.mSavedItems[ key ] )
            self.mTransforms.clear()
            for key in self.mSavedTransforms.keys():
                self.mTransforms[ key ] = deepcopy( self.mSavedTransforms[ key ] )              

        # clears the state
        def clearState( self ):
            self.mSavedItems = {}
            self.mSavedTransforms = {}

        # call this to copy all items from the other CharacteEx object
        def copyState( self, aCharacterEx ):
            self.mItems.clear()
            for key in aCharacterEx.mItems.keys():
                self.mItems[ key ] = deepcopy( aCharacterEx.mItems[ key ] )
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
        
        def addFace( self, aData ):
            self._addItem( 'face', aData )
        def delFace( self ):
            self._delItem( 'face' )

        # function imitate adding of item, when it just changed self values
        def updateItemSpecial( self, aItem ):
            self._addItem( aItem.mKey, aItem, False )
        
        ##########################################################
        # DO NOT CALL CALL THESE METHODS FROM THE OUTER CODE! ONLY FROM THE CLASS, THEY'RE INNER!
        ##########################################################        

        def _addItem( self, aKey, aData, aIsDeletePrevious = True ):
            if aIsDeletePrevious:
                self._delItem( aKey )
            self.mItems[ aKey ] = aData
            aData.onSelfAdded( aKey, self.mItems, self )

            if not aData.getIsSubitem():
                for item in self.mItems.values():
                    if item != aData:
                        item.onItemAdded( aData )
            # apply current transforms
            for key,val in self.mTransforms.iteritems():
                aData.addTransform( key, val )

        def _delItem( self, aKey, aItemName = None ):
            if aKey in self.mItems.keys():
                data = self.mItems[ aKey ]
                # if we got item name - compare it with found item's name, and return if the names are different
                if aItemName != None:
                    if data.mName != aItemName:
                        return

                if not data.getIsSubitem():
                    for item in self.mItems.values():
                        if item != data:
                            item.onItemRemoved( data )

                del self.mItems[ aKey ]
                data.onSelfRemoved( self.mItems, self )

        def _showItem( self, aKey, aSource, aItemName = None ):
            if aKey in self.mItems.keys():
                item = self.mItems[ aKey ]
                # if we got item name - compare it with found item's name, and return if the names are different
                if aItemName != None:
                    if item.mName != aItemName:
                        return
                item.show( aSource )

        def _hideItem( self, aKey, aSource, aItemName = None ):
            if aKey in self.mItems.keys():
                item = self.mItems[ aKey ]
                # if we got item name - compare it with found item's name, and return if the names are different
                if aItemName != None:
                    if item.mName != aItemName:
                        return
                item.hide( aSource )

        def _setStyle( self, aKey, aStyleName, aItemName = None ):
            if aKey in self.mItems.keys():
                item = self.mItems[ aKey ]
                # if we got item name - compare it with found item's name, and return if the names are different
                if aItemName != None:
                    if item.mName != aItemName:
                        return
                item.setStyle( aStyleName )
        
        ##########################################################
        def _onItemHidden( self, aItem ):
            for item in self.mItems.values():
                item.onItemHidden( aItem )
            
        def _onItemShown( self, aItem ):
            for item in self.mItems.values():
                item.onItemShown( aItem )

        def _onItemStyleBeforeChange( self, aItem ):
            for item in self.mItems.values():
                item.onItemStyleBeforeChange( aItem )
            
        def _onItemStyleAfterChange( self, aItem ):
            for item in self.mItems.values():
                item.onItemStyleAfterChange( aItem )

        ##########################################################  
        # __EData_Add = 0
        # __EData_Remove = 1
        # __EData_Show = 2
        # __EData_Hide = 3
        # __EData_Style = 4
        def _applyToSet( self, aSetName, aWhatToDo, aStringParam = None ):
            if aSetName[0] != '*':
                aSetName = '*' + aSetName
            setDesc = WTXmlLinker.c( self.mLinkerKey ).mSetBase.getInfo( aSetName )
            if setDesc == None:
                return
            if aWhatToDo == __EData_Add:
                setItems = WTXmlLinker.c( self.mLinkerKey ).create( aSetName, aStringParam )
                for item in setItems:
                    if item != None:
                        self.addItemDirect( item.mKey, item )
            elif aWhatToDo == __EData_Remove:
                for key,name in zip( setDesc.mKeys, setDesc.mNames ):
                    if key != None:
                        self.delItem( name )
            elif aWhatToDo == __EData_Show:
                for key,name in zip( setDesc.mKeys, setDesc.mNames ):
                    if key != None:
                        self.showItem( name, aStringParam )
            elif aWhatToDo == __EData_Hide:
                for key,name in zip( setDesc.mKeys, setDesc.mNames ):
                    if key != None:
                        self.hideItem( name, aStringParam )
            elif aWhatToDo == __EData_Style:
                for key,name in zip( setDesc.mKeys, setDesc.mNames ):
                    if key != None:
                        self.setStyleItem( name, aStringParam )
                                
        ##########################################################  
        # return key of item by it's name
        def _getItemKeyByName( self, aItemName ):
            return WTXmlLinker.i( self.mLinkerKey ).getItemKey( aItemName )

        ##########################################################  
        # apply one item from preset
        def _applyPresetItem( self, aPresetItem ):
            key = None
            if aPresetItem.mKey != None:
                key = aPresetItem.mKey
            elif aPresetItem.mName != None:
                key = self._getItemKeyByName( aPresetItem.mName )

            if key != None:
                if key in self.mItems.keys():
                    item = self.mItems[ key ]

                    if aPresetItem.mFrame != None:
                        self.updateItemFrameKey( key, aPresetItem.mFrame )
                    elif aPresetItem.mStyle != None:
                        self.setStyleKey( key, aPresetItem.mStyle )
