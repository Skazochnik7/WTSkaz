init -999 python:
    import xml.etree.ElementTree as ET

    class CharacterExSetInfo:
        def __init__( self, aItemsList, aItemBase ):
            self.mNames = aItemsList
            self.mKeys = []
            self._createInfo( aItemBase )

        def _createInfo( self, aItemBase ):
            for item in self.mNames:
                desc = aItemBase.get( item )
                if desc != None:
                    self.mKeys.append( desc.mKey )
                else:
                    self.mKeys.append( None )

    class CharacterExSetStorage:
        # constructor
        def __init__( self ):
           self.mSets = {}  # map with ( string, array of strings )
           self.mSetInfos = {}  # map with ( string, setInfo )
           self.mDataPath = ""   # here we save the path, from where we've loaded data last time

        # call this to clear all loaded info
        def CLEAR( self ):
            self.mSets.clear()
            self.mSetInfos.clear()

        # this should be called at the beginning of the game, path is the location of zorders.xml file
        def read( self, aStartPath, aItemBase ):
            self.mDataPath = aStartPath
            fileList = renpy.list_files()
            for item in fileList:
                if item.endswith( '.hxml' ):
                    if item.startswith( aStartPath ):
                        # we found needed item!
                        self._readFile( item, aItemBase )

        def _readFile( self, aFilePath, aItemBase ):
            opened = ET.parse( renpy.loader.transfn( aFilePath ) )
            root = opened.getroot()
            for item in root:
                if item.tag == 'set':
                    setKey = item.get( 'name' )
                    if not setKey:
                        setKey = wtxml_getFileNameFromPath( aFilePath )  #from WTXmlAssistansFunctions
                    setItems = []
                    for setIt in item:
                        setItems.append( setIt.text )
                    self.mSetInfos[ setKey ] = CharacterExSetInfo( setItems, aItemBase )
                    self.mSets[ setKey ] = setItems


        # return None or list of set items
        def get( self, aSetName ):
            if aSetName[0] == '*':
                aSetName = aSetName[1:]
            if aSetName in self.mSets.keys():
                return self.mSets[ aSetName ]
            else:
                return None

        # return None or setinfo
        def getInfo( self, aSetName ):
            if aSetName[0] == '*':
                aSetName = aSetName[1:]
            if aSetName in self.mSetInfos.keys():
                return self.mSetInfos[ aSetName ]
            else:
                return None
