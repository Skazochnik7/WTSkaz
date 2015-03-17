init -999 python:
    import xml.etree.ElementTree as ET
    import re

    ###########################################################
    # factory for creating results
    ###########################################################
    class CharacterExDescriptionActionResultFactory:
        @staticmethod
        def create( aElementRoot, aFolderBase, aOrderBase ):
            resObj = None
            resType = aElementRoot.get( 'type' )
            basicTypes = [ 'addItem', 'removeItem', 'showItem', 'hideItem', 'setStyle' ]
            if resType in basicTypes:
                resObj = CharacterExDescriptionActionResultBasic()
            elif resType == 'setParams':
                resObj = CharacterExDescriptionActionResultSetParams()
            if resObj != None:
                resObj.read( aElementRoot, aFolderBase, aOrderBase )
            return resObj

    ###########################################################
    class CharacterExDescriptionActionResultBase(store.object):
        def __init__( self ):
            self.mType = ""     # type of actions

        def read( self, aElementRoot, aFolderBase, aOrderBase ):
            self.mType = aElementRoot.get('type')

    ###########################################################
    # for basic actions ( addItem, removeItem, showItem, hideItem )
    class CharacterExDescriptionActionResultBasic( CharacterExDescriptionActionResultBase ):
        #
        def __init__( self ):
            super( CharacterExDescriptionActionResultBasic, self ).__init__()
            self.mKeys = []   # array of strings ( keys where to add/remove etc. )
            self.mNames = []   # array of strings ( names of items/styles )
            self.mSets = []    # array of strings ( names of sets )
            self.mItems = []   # array of strings ( names of items ) 

        # overridden parent method
        def read( self, aElementRoot, aFolderBase, aOrderBase ):
            super( CharacterExDescriptionActionResultBasic, self ).read( aElementRoot, aFolderBase, aOrderBase )
            for child in aElementRoot:
                if child.tag == 'key':
                    if child.text:
                        for key in child.text.split(','):
                            self.mKeys.append( key )
                elif child.tag == 'name':
                    if child.text:
                        for name in child.text.split(','):
                            self.mNames.append( name )
                elif child.tag == 'set':
                    if child.text:
                        for name in child.text.split(','):
                            self.mSets.append( name )
                elif child.tag == 'item':
                    if child.text:
                        for name in child.text.split(','):
                            self.mItems.append( name )

    ###########################################################
    # for basic actions ( addItem, removeItem, showItem, hideItem )
    class CharacterExDescriptionActionResultSetParams( CharacterExDescriptionActionResultBase ):
        #
        def __init__( self ):
            super( CharacterExDescriptionActionResultSetParams, self ).__init__()
            # target can be 'self',,'matched', and 'unmatched'
            # self - means change the values of current item ( where this result is declared )
            # mathced - means change the values of all items, matched be one passed condition of the action
            # unmatched - means change the values of all items, not matched by one passed condition of the action
            self.mTarget = ""
            # oper can be 'set', 'inc', 'dec'
            # set - set value of item to value from result param
            # inc - increase value of item by value from result param
            # dec - decrease value of item by value from result param

            #addition param - 'cap' - if item param goes lower (in case of 'dec') or higher (in case of 'inc') the 'cap' value,
            # item value will be set to 'cap'
            self.mParams = {}

            # custom conditions for setParams result - filter all items to get that ones, to which result will be applied
            # !!! if <filter></filter> block is missed, result will be applied to ALL ITEMS IN THE CharacterData, excluding self !!!
            self.mConditionBlock = None

        # overridden parent method
        def read( self, aElementRoot, aFolderBase, aOrderBase ):
            super( CharacterExDescriptionActionResultSetParams, self ).read( aElementRoot, aFolderBase, aOrderBase )
            self.mTarget = aElementRoot.get('target', 'self')
            if self.mTarget not in [ 'self', 'custom' ]:
                self.mTarget = 'self'

            operPossible = [ 'set', 'inc', 'dec' ]
            for child in aElementRoot:
                if child.tag == 'filter':
                    # read filter
                    self.mConditionBlock = CharacterExDescriptionActionBlock( child, aFolderBase, aOrderBase )
                else:
                    # read parameters
                    param = child
                    operMeth = param.get('oper', 'set')
                    if operMeth not in operPossible:
                        operMeth = 'set'
                    # can be None
                    valueCap = param.get('cap')
                    # we need additional checking for folder and zorder params
                    val = param.text
                    if param.tag == 'folder':
                        val = aFolderBase.get( val )
                    elif param.tag == 'zorder':
                        val = wtxml_readZOrder( val, aOrderBase )   # from WTXmlAssistantFuctions
                        valueCap = wtxml_readZOrder( valueCap, aOrderBase ) # from WTXmlAssistantFunctions
                    self.mParams[ param.tag ] = ( val, operMeth, valueCap )
