init -999 python:
    import xml.etree.ElementTree as ET

    class CharacterExItemStorage:
        # constructor
        def __init__( self ):
           self.mItems = {} # map of ( name, item_description )
           self.mDataPath = ""   # here we save the path, from where we've loaded data last time

        # call this to clear all loaded info
        def CLEAR( self ):
            self.mItems.clear()

        # this should be called at the beginning of the game, path is the location of zorders.xml file
        def read( self, aStartPath, aFolderBase, aZOrderBase ):
            self.mDataPath = aStartPath
            fileList = renpy.list_files()
            for item in fileList:
                if item.endswith( '.hxml' ):
                    if item.startswith( aStartPath ):
                        # we found needed item!
                        self._readFile( item, aFolderBase, aZOrderBase )

        def _readFile( self, aFilePath, aFolderBase, aZOrderBase ):
            f = renpy.file( aFilePath )
            opened = ET.parse( f )
            root = opened.getroot()
            itemDesc = CharacterExDescriptionItem( root, aFolderBase, aZOrderBase )
            if not itemDesc.mName:
                itemDesc.mName = wtxml_getFileNameFromPath( aFilePath )  #from WTXmlAssistansFunctions
            self.mItems[ itemDesc.mName ] = itemDesc

        # return ItemDescription or None
        # remember to NOT CHANGE the obtained descriptions
        def get( self, aItemName ):
            if aItemName in self.mItems.keys():
                return self.mItems[ aItemName ]
            else:
                return None

        # return ItemStyleDescription or None
        # remember to NOT CHANGE the obtained descriptions
        def getItemStyle( self, aItemName, aStyleName ):
            if aItemName in self.mItems.keys():
                item = self.mItems[ aItemName ]
                if aStyleName in item.mStyles.keys():
                    return item.mStyles[ aStyleName ]
                else:
                    return None
            else:
                return None

        # return the key where the item should be added
        def getItemKey( self, aItemName ):
            if aItemName in self.mItems.keys():
                item = self.mItems[ aItemName ]
                return item.mKey
            else:
                return ""

