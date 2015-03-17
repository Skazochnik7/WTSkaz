init -999 python:
    import xml.etree.ElementTree as ET
    import re

    ###########################################################
    class CharacterExDescriptionItem(store.object):
        #
        def __init__( self, aXmlRoot, aFolderBase, aOrderBase ):
            self.mKey = ""
            self.mName = ""
            self.mIsSubitem = False
            self.mSubitems = []
            self.mStyles = {}
            self._read( aXmlRoot, aFolderBase, aOrderBase )


        # read self from xml
        def _read( self, aXmlRoot, aFolderBase, aOrderBase ):
            # first of all we should read this two items
            for child in aXmlRoot:
                if child.tag == 'key':
                    self.mKey = child.text
                elif child.tag == 'name':
                    self.mName = child.text
                elif child.tag == 'isSubitem':
                    self.mIsSubitem = wtxml_parseBool( child.text )  #from WTXmlAssitantFunctions
                elif child.tag == 'subitems':
                    wtxml_readList( child, self.mSubitems ) # from WTXmlAssistantFunctions

            # and only then - styles
            for child in aXmlRoot:
                if child.tag == 'style':
                    styleKey = child.get('name', 'default')
                    self.mStyles[ styleKey ] = CharacterExDescriptionStyle( child, styleKey, self.mName,
                        self.mIsSubitem, aFolderBase, aOrderBase )
