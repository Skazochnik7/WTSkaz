init -999 python:
    import xml.etree.ElementTree as ET
    import re

    ###########################################################
    class CharacterExDescriptionTransform(store.object):
        #
        def __init__( self, aElementRoot, aId ):
            self.mId = aId
            self.mName = ""
            self.mParams = {}
            self._read( aElementRoot )

        #
        def _read( self, aElementRoot ):
            for child in aElementRoot:
                if child.tag == 'name':
                    self.mName = child.text
                elif child.tag == 'params':
                    for param in child:
                        self.mParams[ param.tag ] = param.text