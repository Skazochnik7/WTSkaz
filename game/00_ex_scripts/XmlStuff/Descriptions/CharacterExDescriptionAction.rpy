init -999 python:
    import xml.etree.ElementTree as ET
    import re

    ###########################################################
    class CharacterExDescriptionAction(store.object):
        #
        def __init__( self, aElementRoot, aFolderBase, aOrderBase ):
            self.mEvent = ""    # type of events ( selfAdded, selfRemoved, itemAdded, itemRemoved, itemShown, itemHidden )
            self.mBlocks = []   # array of block descriptions
            self.mResults = []  # array of result descriptions
            self.mBadResults = []   # array of bad result descriptions
            self._read( aElementRoot, aFolderBase, aOrderBase )

        #
        def _read( self, aElementRoot, aFolderBase, aOrderBase ):
            self.mEvent = aElementRoot.get('event')
            for child in aElementRoot:
                if child.tag == 'body':
                    for block in child:
                        self.mBlocks.append( CharacterExDescriptionActionBlock( block, aFolderBase, aOrderBase ) )
                if child.tag == 'result':
                    self.mResults.append( CharacterExDescriptionActionResultFactory.create( child, aFolderBase, aOrderBase ) )
                if child.tag == 'badresult':
                    self.mBadResults.append( CharacterExDescriptionActionResultFactory.create( child, aFolderBase, aOrderBase ) )