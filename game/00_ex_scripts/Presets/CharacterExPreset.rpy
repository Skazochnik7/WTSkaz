init -999 python:
    import xml.etree.ElementTree as ET

    class CharacterExPreset:
         # constructor
        def __init__( self ):
            self.mItems = []
            self.mIsSimple = True
            self.mTemplateList = []

        @classmethod
        def clone( cls, aCopyObj ):
            result = cls()
            result.mIsSimple = aCopyObj.mIsSimple
            result.mItems = list( aCopyObj.mItems )
            result.mTemplateList = list( aCopyObj.mTemplateList )
            return result

        def read( self, aElementRoot ):
            for item in aElementRoot:
                if item.tag == 'templates':
                    self.mIsSimple = False
                    self.mTemplateList = item.text.split( ',' )
                elif item.tag == 'item':
                    presetItem = CharacterExPresetItem()
                    presetItem.read( item )
                    self.mItems.append( presetItem )

        # return array of items in preset
        def getItems( self, aParamsList = None ):
            if self.mIsSimple:
                return self.mItems
            else:
                if len( aParamsList ) != len( self.mTemplateList ):
                    # debug
                    CharacterExDebuger.LogE( 'CharacterExPreset::getItems: diferent size of aParamsList and mTemplateList lists!' )
                    return None

                result = []
                for item in self.mItems:
                    newOne = item.applyTemplates( self.mTemplateList, aParamsList )
                    result.append( newOne )
                return result