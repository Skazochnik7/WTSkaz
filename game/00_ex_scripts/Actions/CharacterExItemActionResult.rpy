init -999 python:
    import itertools

    ###########################################################
    # factory for creating results
    ###########################################################
    class CharacterExItemActionResultFactory:
        @staticmethod
        def create( aDescription ):
            basicTypes = [ 'addItem', 'removeItem', 'showItem', 'hideItem', 'setStyle' ]
            if aDescription.mType in basicTypes:
                return CharacterExItemActionResultBasic.create( aDescription )
            elif aDescription.mType == 'setParams':
                return CharacterExItemActionResultSetParams.create( aDescription )
            # default value
            return None

    ###########################################################
    # interface to work with results
    ###########################################################
    class ICharacterExItemActionResult:
        def __init__( self ):
            self.mType = ""     # type of result
           
        def apply( self, aCharacterEx, aParentItem ):
            None

    ###########################################################
    # for basic actions ( addItem, removeItem, showItem, hideItem )
    class CharacterExItemActionResultBasic( store.object, ICharacterExItemActionResult ):
        def __init__( self ):
            super( CharacterExItemActionResultBasic, self ).__init__()
            self.mKeys = []   # array of strings ( keys where to add/remove etc. )
            self.mNames = []   # array of strings ( names of items/styles )
            self.mSets = []    # array of strings ( names of sets )
            self.mItems = []   # array of strings ( names of items )

        @classmethod
        def create( cls, aResultDescription ):
            desc = aResultDescription
            res = cls()
            res.mType = desc.mType
            for key in desc.mKeys:
                res.mKeys.append( key )
            for name in desc.mNames:
                res.mNames.append( name )
            for theSet in desc.mSets:
                res.mSets.append( theSet )
            for item in desc.mItems:
                res.mItems.append( item )
            return res

        @staticmethod
        def getItemKeyByName( aParentItem, aSearchedItemName ):
            if aParentItem.mOwner != None:
                itemBase = WTXmlLinker.i( aParentItem.mOwner.mLinkerKey )
                return itemBase.getItemKey( aSearchedItemName )
            else:
                return ""

        # overridden parent method
        def apply( self, aCharacterEx, aParentItem ):
            if self.mKeys and self.mNames:
                for key,name in itertools.izip_longest( self.mKeys, self.mNames ):   
                    if key != "":
                        self._applyKeyResults( aParentItem, aCharacterEx, key, name )
                    else:
                        key = CharacterExItemActionResult.getItemKeyByName( aParentItem, name )
                        if key == "":
                            continue
                        self._applyKeyResults( aParentItem, aCharacterEx, key, name )
            elif self.mSets:
                for theSet,name in itertools.izip_longest( self.mSets, self.mNames ):   
                    theSet = "*" + theSet
                    self._applySetResults( aParentItem, aCharacterEx, theSet, name )
            elif self.mItems:
                for item,name in itertools.izip_longest( self.mItems, self.mNames ):   
                    self._applyItemResults( aParentItem, aCharacterEx, item, name )

        def _applySetResults( self, aParentItem, aCharacterEx, aSetName, aName ):
            if self.mType == 'addItem':
                aCharacterEx.addItemSet( aSetName )
            elif self.mType == 'removeItem':
                aCharacterEx.delItemSet( aSetName )
            elif self.mType == 'showItem':
                aCharacterEx.showItemSet( aSetName, aParentItem.mName )
            elif self.mType == 'hideItem':
                aCharacterEx.hideItemSet( aSetName, aParentItem.mName )
            elif self.mType == 'setStyle':
                aCharacterEx.setStyleSet( aSetName, aName )

        def _applyItemResults( self, aParentItem, aCharacterEx, aItemName, aName ):
            if self.mType == 'addItem':
                aCharacterEx.addItem( aItemName )
            elif self.mType == 'removeItem':
                aCharacterEx.delItem( aItemName )
            elif self.mType == 'showItem':
                aCharacterEx.showItem( aItemName, aParentItem.mName )
            elif self.mType == 'hideItem':
                aCharacterEx.hideItem( aItemName, aParentItem.mName )
            elif self.mType == 'setStyle':
                aCharacterEx.setStyleItem( aItemName, aName )

        def _applyKeyResults( self, aParentItem, aCharacterEx, aKey, aName ):
            if self.mType == 'addItem':
                aCharacterEx.addItemKey( aKey, aName )
            elif self.mType == 'removeItem':
                aCharacterEx.delItemKey( aKey )
            elif self.mType == 'showItem':
                aCharacterEx.showItemKey( aKey, aParentItem.mName )
            elif self.mType == 'hideItem':
                aCharacterEx.hideItemKey( aKey, aParentItem.mName )
            elif self.mType == 'setStyle':
                aCharacterEx.setStyleKey( aKey, aName )

    ###########################################################
    # for action 'setParams'
    class CharacterExItemActionResultSetParams( store.object, ICharacterExItemActionResult ):
        #
        def _operSet( self, aCurValue, aValue, aCap ):
            # cap is unused
            return aValue

        #
        def _operInc( self, aCurValue, aValue, aCap ):
            newVal = aCurValue + aValue
            if aCap != None:
                if newVal > aCap:
                    newVal = aCap
            return newVal

        #
        def _operDec( self, aCurValue, aValue, aCap ):
            newVal = aCurValue - val
            if aCap != None:
                if newVal < aCap:
                    newVal = aCap
            return newVal

        def __init__( self ):
            super( CharacterExItemActionResultSetParams, self ).__init__()
            self.mTarget = ""
            self.mConditionBlock = None # can be None or CharacterExItemActionBlock
            self.mParamKey = None   # can be ( string, oper, cap )
            self.mParamFileName = None  # can be ( string, oper, cap )
            self.mParamFileFolder = None    # can be ( string, oper, cap )
            self.mParamIsVisible = None # can be ( 1 or 0 (True or False), oper, cap )
            self.mParamZOrder = None   # can be ( int, oper, cap )

        @classmethod
        def create( cls, aResultDescription ):
            desc = aResultDescription
            res = cls()
            mapOper = { 'set': res._operSet, 'inc' : res._operInc, 'dec' : res._operDec }

            res.mType = desc.mType
            res.mTarget = desc.mTarget
            if desc.mConditionBlock != None:
                res.mConditionBlock = CharacterExItemActionBlock.create( desc.mConditionBlock )
            for name,tup in desc.mParams.iteritems():
                ( val, oper, cap ) = tup
                operFunc = res._operSet
                if oper in mapOper.keys():
                    operFunc = mapOper[ oper ]

                resTupple = ( val, operFunc, cap )
                if name == 'key':
                    res.mParamKey = resTupple
                elif name == 'frame':
                    res.mParamFileName = resTupple
                elif name == 'folder':
                    res.mParamFileFolder = resTupple
                elif name == 'visible':
                    res.mParamIsVisible = resTupple
                elif name == 'zorder':
                    res.mParamZOrder = resTupple
            return res

        # overridden parent method
        def isNeedPassedItems( self ):
            if self.mTarget == 'self':
                return False
            else:
                return True

        # overridden parent method
        def apply( self, aCharacterEx, aParentItem ):
            itemsToApply = []
            if self.mTarget == 'self':
                itemsToApply.append( aParentItem )
            elif self.mTarget == 'custom' or self.mTarget == 'customUnion':
                if self.mConditionBlock != None:
                    needUnion = self.mTarget == 'customUnion'
                    res = self.mConditionBlock.check( aCharacterEx.getAllItems().values(), aParentItem, True, needUnion )
                    if res.isPassed and res.passedItems != None:
                        if aParentItem.mKey in res.passedItems.keys():
                            del res.passedItems[ aParentItem.mKey ]
                        itemsToApply = res.passedItems.values()

            for item in itemsToApply:
                item.mKey = self._setParam( self.mParamKey, item.mKey, str )
                item.mFileName = self._setParam( self.mParamFileName, item.mFileName, str )
                item.mFileFolder = self._setParam( self.mParamFileFolder, item.mFileFolder, str )
                item.setIsVisible( bool(self._setParam( self.mParamIsVisible, item.mIsVisible, int )) )
                item.zorder = self._setParam( self.mParamZOrder, item.zorder, int )

        def _setParam( self, aTupple, aCurrentValue, aConvertFunc ):
            if aTupple != None:
                ( val, oper, cap ) = aTupple
                if cap != None:
                    cap = aConvertFunc( cap )
                return oper( aCurrentValue, aConvertFunc( val ), cap )
            else:
                return aCurrentValue