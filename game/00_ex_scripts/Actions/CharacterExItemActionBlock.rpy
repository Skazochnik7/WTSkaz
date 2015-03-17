init -999 python:
    import itertools

    ###########################################################
    class CharacterExItemActionBlock(store.object):
       
        def __init__( self ):
            self.mConditions = []    # array of ICharacterExItemActionCondition

        @classmethod
        def create( cls, aBlockDescription ):
            desc = aBlockDescription
            block = cls()
            for cond in desc.mConditions:
                condition = CharacterExItemActionConditionFactory.create( cond )
                block.mConditions.append( condition )
            return block

        # call this method to check all conditions in the block for result
        # return CharacterExItemActionConditionResult
        # params:
        #   @ aItems - array of items to check
        #   @ aEventSenderItem - item which own current condition block element
        #   @ aIsNeedPassedItems - wheter this block should return items, which passed its conditions
        #   @ aIsNeedPassedUnion - relevant only if aIsNeedPassedItems set to True
        #                           determine whether block should return items, which passed ALL conditions (intersection),
        #                           or items, which passed at least one condition (union)
        def check( self, aItems, aEventSenderItem, aIsNeedPassedItems = False, aIsNeedPassedUnion = False ):
            if aIsNeedPassedItems:
                passedDic = None
                for cond in self.mConditions:
                    res = cond.check( aItems, aEventSenderItem, aIsNeedPassedItems )
                    if not res.isPassed:
                        return CharacterExItemActionConditionResult( False )
                    else:
                        if not aIsNeedPassedUnion:
                            # collect items which passed ALL conditions (intersection)
                            if passedDic == None:
                                # first iteration
                                passedDic = res.passedItems
                            else:
                                # second and greater iteration
                                tmpDic = {}
                                for key in passedDic.keys():
                                    if key in res.passedItems.keys():
                                        tmpDic[ key ] = passedDic[ key ]
                                passedDic = tmpDic
                        else:
                            # collect items which passed at least one condition (union)
                            if key in res.passedItems.keys():
                                passedDic[ key ] = res.passedItems[ key ]
                # passedDic can't be None, because in this case we would have been finished the function in previous False branch
                return CharacterExItemActionConditionResult( True, passedDic )
            else:
                for cond in self.mConditions:
                    res = cond.check( aItems, aEventSenderItem, aIsNeedPassedItems )
                    if not res.isPassed:
                        return CharacterExItemActionConditionResult( False )
                return CharacterExItemActionConditionResult( True )