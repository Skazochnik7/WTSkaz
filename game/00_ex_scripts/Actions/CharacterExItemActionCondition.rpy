init -999 python:
    import itertools

    ###########################################################
    # class for condition check result
    ###########################################################    
    class CharacterExItemActionConditionResult:
        def __init__( self, aIsPassed = False, aPassedItems = None ):
            self.isPassed = aIsPassed
            self.passedItems = aPassedItems # dictionary with passed items, can be None. ( Key == item.mKey, Value == item )

    ###########################################################
    # factory for creating conditions
    ###########################################################
    class CharacterExItemActionConditionFactory:
        @staticmethod
        def create( aDescription ):
            if aDescription.mType == 'hasItem' or aDescription.mType == 'missItem':
                return CharacterExItemActionConditionHasMiss.create( aDescription )
            # default value
            return None

    ###########################################################
    # interface to work with conditions
    ###########################################################
    class ICharacterExItemActionCondition:
        # aItems - items to check
        # aEventSenderItem - item, who intitate current event
        # aIsNeedPassedItems - flag to determine whether condition should return passed items or not
        # @return - function should return the CharacterExItemActionConditionResult object, with result.isPassed param set to True,
        #           if condition is passed, and False otherwise. In addition, if aIsNeedPassedItems is set to True,
        #           function should return all items which passed the condition 
        #           ( as dictionary, result.passedItems field of CharacterExItemActionConditionResult )
        def check( self, aItems, aEventSenderItem, aIsNeedPassedItems = False ):
            return CharacterExItemActionConditionResult( False )

    ###########################################################
    class CharacterExItemActionConditionParams( store.object ):
        def _compE( self, valCond, valCheck ):
            return valCheck == valCond

        def _compNE( self, valCond, valCheck ):
            return valCheck != valCond

        def _compG( self, valCond, valCheck ):
            return valCheck > valCond

        def _compL( self, valCond, valCheck ):
            return valCheck < valCond

        def _compGE( self, valCond, valCheck ):
            return valCheck >= valCond

        def _compLE( self, valCond, valCheck ):
            return valCheck <= valCond

        def __init__( self ):
            #self.mType = ""     # type of condition. Can be 'hasItem' or 'missItem'
            self.mParamKey = None   # can be ( string, comp )
            self.mParamName = None   # can be ( string, comp )
            self.mParamFileName = None  # can be ( string, comp )
            self.mParamFileFolder = None    # can be ( string, comp )
            self.mParamIsVisible = None # can be ( 1 or 0 (True or False), comp )
            self.mParamZOrder = None   # can be ( int, comp )
            self.mParamStyle = None     # can be ( string, comp )
            # boolean - is this item is the sender of action or not, can be 1 or 0 (True or False)
            # IT'S NOT A TUPPLE!
            self.mParamActionItem = None

        @classmethod
        def create( cls, aConditionDescription ):
            desc = aConditionDescription
            cond = cls()
            mapMeth = { 'e': cond._compE, 'ne' : cond._compNE, 'l' : cond._compL, 'g': cond._compG,
                 'ge' : cond._compGE, 'le' : cond._compLE }

            # we won't read type in params - move it to child create method
            #cond.mType = desc.mType
            for name,tup in desc.mParams.iteritems():
                ( val, meth ) = tup

                methFunc = cond._compE
                if meth in mapMeth.keys():
                    methFunc = mapMeth[ meth ]

                if name == 'key':
                    cond.mParamKey = ( val, methFunc, str )
                if name == 'name':
                    cond.mParamName = ( val, methFunc, str )
                elif name == 'frame':
                    cond.mParamFileName = ( val, methFunc, str )
                elif name == 'folder':
                    cond.mParamFileFolder = ( val, methFunc, str )
                elif name == 'visible':
                    cond.mParamIsVisible = ( val, methFunc, wtxml_parseBool )    #_parseBool is from WTXmlAssitantFunctions
                elif name == 'zorder':
                    cond.mParamZOrder = ( val, methFunc, int )
                elif name == 'style':
                    cond.mParamStyle = ( val, methFunc, str )
                elif name == 'actionItem':
                    cond.mParamActionItem = wtxml_parseBool( val ) # IT'S NOT A TUPPLE!  #_parseBool is from WTXmlAssitantFunctions

            return cond

        def checkConditionParam( self, aTupple, aCheckedValue ):
            if aTupple == None:
                return True
            ( val, comp, conv ) = aTupple
            return comp( conv(val), aCheckedValue )

    ###########################################################
    class CharacterExItemActionConditionHasMiss( CharacterExItemActionConditionParams, ICharacterExItemActionCondition ):

        def _missItemFunc( self, aResult ):
            return not aResult

        def _hasItemFunc( self, aResult ):
            return aResult

        def __init__( self ):
            super( CharacterExItemActionConditionHasMiss, self ).__init__()
            self.mType = ""     # type of condition. Can be 'hasItem' or 'missItem'

        # overridden parent method
        @classmethod
        def create( cls, aConditionDescription ):
            desc = aConditionDescription
            cond = super( CharacterExItemActionConditionHasMiss, cls ).create( aConditionDescription )
            cond.mType = desc.mType
            return cond

        # overridden parent method
        def check( self, aItems, aEventSenderItem, aIsNeedPassedItems = False ):
            # select result function
            resFunc = None
            if self.mType == 'hasItem':
                resFunc = self._hasItemFunc
            elif self.mType == 'missItem':
                resFunc = self._missItemFunc

            # fail condition if the type is incorrect
            if resFunc == None:
                return False

            if aIsNeedPassedItems:
                passedItems = {}
                isPassed = False
                for item in aItems:
                    isCurPassed = self._checkOne( item, aEventSenderItem )
                    if isCurPassed:
                        passedItems[ item.mKey ] = item
                    isPassed = isPassed or isCurPassed
                if not passedItems:
                    passedItems = None
                return CharacterExItemActionConditionResult( resFunc( isPassed ), passedItems )
            else:
                for item in aItems:
                    if self._checkOne( item, aEventSenderItem ):
                        return CharacterExItemActionConditionResult( resFunc( True ) )
                return CharacterExItemActionConditionResult( resFunc( False ) )
                

        def _checkOne( self, aItem, aEventSenderItem ):
            #check action item - ignore all compare methods
            if self.mParamActionItem != None:
                val = self.mParamActionItem
                compareRes = ( aItem.mName == aEventSenderItem.mName )
                if compareRes != val:
                    return False

            desired = [ self.mParamKey, self.mParamName, self.mParamStyle, self.mParamFileName,
                         self.mParamFileFolder, self.mParamIsVisible, self.mParamZOrder  ]
            real = [ aItem.mKey, aItem.mName, aItem.mActiveStyle, aItem.mFileName,
                         aItem.mFileFolder, aItem.mIsVisible, aItem.zorder ]
            for cond,val in zip( desired, real ):
                if not self.checkConditionParam( cond, val ):
                    return False
            return True