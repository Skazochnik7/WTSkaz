init -999 python:
    import xml.etree.ElementTree as ET

    class CharacterExPresetData:
         # constructor
        def __init__( self ):
            self.mKey = None
            self.mName = None
            self.mFrame = None
            self.mStyle = None

        def read( self, aElementRoot ):
            for item in aElementRoot:
                if item.tag == 'key':
                    self.mKey = item.text
                elif item.tag == 'name':
                    self.mName = item.text
                elif item.tag == 'frame':
                    self.mFrame = item.text
                elif item.tag == 'style':
                    self.mStyle = item.text

    class CharacterExPresetStorage:
        # constructor
        def __init__( self ):
           self.mPresets = {}  # map with ( string, array of CharacterExPresetData )
           self.mDataPath = ""   # here we save the path, from where we've loaded data last time

        # call this to clear all loaded info
        def CLEAR( self ):
            self.mPresets.clear()

        # this should be called at the beginning of the game, start path is the directory where presets kept
        def read( self, aStartPath ):
            self.mDataPath = aStartPath
            fileList = renpy.list_files()
            for item in fileList:
                if item.endswith( '.hxml' ):
                    if item.startswith( aStartPath ):
                        # we found needed item!
                        self._readFile( item )

        def _readFile( self, aFilePath ):
            f = renpy.file( aFilePath )
            opened = ET.parse( f )
            root = opened.getroot()
            for item in root:
                if item.tag == 'preset':
                    presetName = item.get( 'name' )
                    if not presetName:
                        presetName = wtxml_getFileNameFromPath( aFilePath )  #from WTXmlAssistansFunctions
                    arr = []
                    for elem in item:
                        data = CharacterExPresetData()
                        data.read( elem )
                        arr.append( data )
                    self.mPresets[ presetName ] = arr

        # return None or array of CharacterExPresetData
        def get( self, aPresetName ):
            if aPresetName in self.mPresets.keys():
                return self.mPresets[ aPresetName ] # this is an array
            else:
                return None
