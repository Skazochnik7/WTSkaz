init -999 python:
    import xml.etree.ElementTree as ET
    import re

    ###########################################################
    class CharacterExDescriptionStyle(store.object):
        #
        def _fillValuesForDefault( self ):
            self.mFrame = ""
            self.mFileFolder = ""
            self.mZOrder = 0
            self.mParent = None
            self.mParentStyles = []
            self.mIsVisible = True
            self.mShift = Transform( pos = ( 0, 0 ) )
            self.mTransforms = {} # map of transform descriptions
            self.mHideList = [] # array of strings
            self.mActions = []  # array of actions descriptions

        def __init__( self, aElementRoot, aStyleName, aItemName, aIsSubitem, aFolderBase, aOrderBase ):
            self.mName = aItemName
            self.mFrame = None
            self.mFileFolder = None
            self.mZOrder = None
            self.mParent = None
            self.mParentStyles = None
            self.mIsVisible = True
            self.mShift = None
            self.mTransforms = None # map of transform descriptions
            self.mHideList = None # array of strings
            self.mActions = None  # array of actions descriptions
            
            if aStyleName == 'default':
                self._fillValuesForDefault()

            self._read( aElementRoot, aIsSubitem, aFolderBase, aOrderBase )

        # read self from xml
        def _read( self, aElementRoot, aIsSubitem, aFolderBase, aOrderBase ):
            for child in aElementRoot:
                if child.tag == 'frame':
                    self.mFrame = child.text
                elif child.tag == 'folder':
                    self.mFileFolder = aFolderBase.get( child.text )
                elif child.tag == 'zorder':
                    self._readOrder( child, aOrderBase )
                elif child.tag == 'visible':
                    self.mIsVisible = wtxml_parseBool( child.text )  #from WTXmlAssitantFunctions
                elif child.tag == 'parent':
                    if not aIsSubitem:
                        self.mParent = child.text
                elif child.tag == 'parentStyles':
                    self._readParentStyles( child )
                elif child.tag == 'shift':
                    self._readShift( child )
                elif child.tag == 'transforms':
                    if self.mTransforms == None:
                        self.mTransforms = {}
                    for trSingle in child:
                        trId = trSingle.get('id')
                        self.mTransforms[ trId ] = CharacterExDescriptionTransform( trSingle, trId )

                elif child.tag == 'hidelist':
                    if not aIsSubitem:
                        self._readHideList( child )

                elif child.tag == 'actions':
                    if not aIsSubitem:
                        if self.mActions == None:
                                self.mActions = []
                        for actSingle in child:
                            self.mActions.append( CharacterExDescriptionAction( actSingle, aFolderBase, aOrderBase ) )

        def _readParentStyles( self, child ):
            if self.mParentStyles == None:
                self.mParentStyles = []
            wtxml_readList( child, self.mParentStyles ) # from WTXmlAssistantFunctions

        def _readHideList( self, child ):
            if self.mHideList == None:
                self.mHideList = []
            wtxml_readList( child, self.mHideList ) # from WTXmlAssistantFunctions

        def _readShift( self, child ):
            if child.text != '':
                posText = child.text
                if posText != None:
                    positions = []
                    for pos in child.text.split( ',' ):
                        positions.append( int( pos ) )
                    self.mShift = Transform( pos = ( positions[0], positions[1] ) )

        def _readOrder( self, child, aOrderBase ):
            self.mZOrder = wtxml_readZOrder( child.text, aOrderBase )   # from WTXmlAssistantFunctions
