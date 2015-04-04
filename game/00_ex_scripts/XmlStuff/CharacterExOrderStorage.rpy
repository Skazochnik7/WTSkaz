init -999 python:
    import xml.etree.ElementTree as ET

    class CharacterExOrderStorage:
        # constructor
        def __init__( self ):
           self.mSynonyms = {}
           self.mDataPath = ""   # here we save the path, from where we've loaded data last time

        # call this to clear all loaded info
        def CLEAR( self ):
            self.mSynonyms.clear()

        # this should be called at the beginning of the game, path is the location of zorders.xml file
        def read( self, aOrderFilePath ):
            self.mDataPath = aOrderFilePath
            f = renpy.file( aOrderFilePath )
            opened = ET.parse( f )
            root = opened.getroot()
            
            for child in root:
                key = child.get('name')
                self.mSynonyms[ key ] = int( child.text )

        # aValue should be string-key or int-value
        def get( self, aValue ):
            if aValue in self.mSynonyms.keys():
                return self.mSynonyms[ aValue ]
            else:
                return int( aValue )
