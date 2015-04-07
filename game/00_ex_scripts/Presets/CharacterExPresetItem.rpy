init -999 python:
    import xml.etree.ElementTree as ET

    class CharacterExPresetItem:
         # constructor
        def __init__( self ):
            self.mKey = None
            self.mName = None
            self.mFrame = None
            self.mStyle = None

        @classmethod
        def clone( cls, aCopyObj ):
            result = cls()
            result.mKey = aCopyObj.mKey
            result.mName = aCopyObj.mName
            result.mFrame = aCopyObj.mFrame
            result.mStyle = aCopyObj.mStyle
            return result

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

        def applyTemplates( self, aTemplates, aActuals ):
            result = CharacterExPresetItem.clone( self )
            for template, value in zip( aTemplates, aActuals ):
                if result.mKey:
                    result.mKey = result.mKey.replace( template, value )
                if result.mName:
                    result.mName = result.mName.replace( template, value )
                if result.mFrame:
                    result.mFrame = result.mFrame.replace( template, value )
                if result.mStyle:
                    result.mStyle = result.mStyle.replace( template, value )
            return result