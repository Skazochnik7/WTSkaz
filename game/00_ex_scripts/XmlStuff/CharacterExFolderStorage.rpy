init -999 python:
    import xml.etree.ElementTree as ET

    class CharacterExFolderStorage:
        # constructor
        def __init__( self ):
           self.mSynonyms = {}
           self.mDataPath = ""   # here we save the path, from where we've loaded data last time

        # call this to clear all loaded info
        def CLEAR( self ):
            self.mSynonyms.clear()
            
        # this should be called at the beginning of the game, path is the location of folders.xml file
        def read( self, aFolderFilePath ):
            self.mDataPath = aFolderFilePath
            opened = ET.parse( renpy.loader.transfn( aFolderFilePath ) )
            root = opened.getroot()
            
            for child in root:
                key = child.get('name')
                path = child.text
                if not path.endswith( '/' ):
                    path += '/'
                self.mSynonyms[ key ] = path

        # aValue should be string
        def get( self, aValue ):
            if aValue in self.mSynonyms.keys():
                return self.mSynonyms[ aValue ]
            else:
                return aValue
