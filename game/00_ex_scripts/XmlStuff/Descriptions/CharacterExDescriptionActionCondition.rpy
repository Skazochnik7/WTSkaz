init -999 python:
    import xml.etree.ElementTree as ET
    import re

    ###########################################################
    class CharacterExDescriptionActionCondition(store.object):
        #
        def __init__( self, aElementRoot, aFolderBase, aOrderBase ):
            self.mType = ""
            self.mParams = {}   # map (string-tupple(value,compare_method))
            # compare methods:
            # e - equal (default)
            # ne - not equal
            # le - lower or equal
            # ge - greater or equal
            # l - lower
            # g - greater
            # ne - not equal
            self._read( aElementRoot, aFolderBase, aOrderBase )

        #
        def _read( self, aElementRoot, aFolderBase, aOrderBase ):
            self.mType = aElementRoot.get('type', 'hasItem')
            compPossible = [ 'e', 'ne', 'ge', 'le', 'g', 'l' ]
            for param in aElementRoot:
                compareMeth = param.get('comp', 'e')
                if compareMeth not in compPossible:
                    compareMeth = 'e'
                # we need additional checking for folder and zorder params
                val = param.text
                if param.tag == 'folder':
                    val = aFolderBase.get( val )
                elif param.tag == 'zorder':
                    val = wtxml_readZOrder( val, aOrderBase )   # from WTXmlAssistantFunctions
                self.mParams[ param.tag ] = ( val, compareMeth )
