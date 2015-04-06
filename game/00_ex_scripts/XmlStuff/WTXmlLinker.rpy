init -999 python:
    
    class WTXmlLinker:
        _indF = 0
        _indO = 1
        _indI = 2
        _indS = 3
        _indC = 4
        _indP = 5
        # this is the dictionary with the pairs: <string, array of objects >
        _mLinkerDictionary = {}

        #####################
        #old style initing:
        #####################
        #_lkHermione = 'hermione'
        
        # # declare variables
        # global Hermione_FB
        # global Hermione_OB
        # global Hermione_IB
        # global Hermione_SB

        # # initing variables
        # Hermione_FB = CharacterExFolderStorage()
        # Hermione_OB = CharacterExOrderStorage()
        # Hermione_IB = CharacterExItemStorage()
        # Hermione_SB = CharacterExSetStorage()

        # # initing creator
        # global Hermione_ItemCreator
        # Hermione_ItemCreator = CharacterExItemCreator( Hermione_IB, Hermione_SB, WTXmlLinker.getHermioneLinkerKey() )

        # # fill variables
        # Hermione_FB.read( '00_ex/hxml_items/00_hermione/folders.hxml' )
        # Hermione_OB.read( '00_ex/hxml_items/zorders.hxml' )
        # Hermione_IB.read( '00_ex/hxml_items/00_hermione/items/', Hermione_FB, Hermione_OB )
        # Hermione_SB.read( '00_ex/hxml_items/00_hermione/sets/', Hermione_IB )

        #####################
        #a bit latest style
        #####################
#        execString = """
# # declare variables
# #global {0}_OB
# #global {0}_FB
# #global {0}_IB
# #global {0}_SB

# # initing variables
# {0}_OS = CharacterExOrderStorage()
# {0}_FS = CharacterExFolderStorage()
# {0}_IS = CharacterExItemStorage()
# {0}_SS = CharacterExSetStorage()

# # initing creator
# #global {0}_ItemCreator
# {0}_ItemCreator = CharacterExItemCreator( {0}_IS, {0}_SS, '{0}' )

# # fill variables
# {0}_OS.read( '{1}/zorders.hxml' )
# {0}_FS.read( '{3}/folders.hxml' )
# {0}_IS.read( '{3}/items/', {0}_FS, {0}_OS )
# {0}_SS.read( '{3}/sets/', {0}_IS )

# # adds objects to linker dictionary
# WTXmlLinker._mLinkerDictionary[ '{0}' ] = [ {0}_FS, {0}_OS, {0}_IS, {0}_SS, {0}_ItemCreator ]

# # create static function with name: getLinkerKey_aKey()
# @staticmethod
# def _return_key_{0}():
#     return '{0}'

# # and add it to the linker class
# WTXmlLinker.getLinkerKey_{0} = _return_key_{0}
# """.format( aKey, aZOrderPath, aFolderPath, aItemsRootPath )
#        exec( execString )

        @staticmethod
        def prepareCharacterResources( aKey, aZOrderPath, aFolderPath, aItemsRootPath ):
            # create variables
            var_OS = CharacterExOrderStorage()
            var_FS = CharacterExFolderStorage()
            var_IS = CharacterExItemStorage()
            var_SS = CharacterExSetStorage()
            var_PS = CharacterExPresetStorage()
            var_creator = CharacterExItemCreator( var_IS, var_SS, aKey )

            # fill variables
            var_OS.read( aZOrderPath + '/zorders.hxml' )
            var_FS.read( aItemsRootPath + '/folders.hxml' )
            var_IS.read( aItemsRootPath + '/items/', var_FS, var_OS )
            var_SS.read( aItemsRootPath + '/sets/', var_IS )
            var_PS.read( aItemsRootPath + '/presets/' )

            # adds objects to linker dictionary
            WTXmlLinker._mLinkerDictionary[ aKey ] = [ var_FS, var_OS, var_IS, var_SS, var_creator, var_PS ]

            # create static function with name: getLinkerKey_aKey()
            execString = (
                    "@staticmethod\n"
                    "def _return_key_{0}():\n"
                    "   return '{0}'\n"
                    "# and add it to the linker class\n"
                    "WTXmlLinker.getLinkerKey_{0} = _return_key_{0}"
                    ).format( aKey )
            exec( execString )

        @staticmethod
        def f( aKey ):
            if aKey in WTXmlLinker._mLinkerDictionary:
                return WTXmlLinker._mLinkerDictionary[ aKey ][ WTXmlLinker._indF ]
            return None

        @staticmethod
        def o( aKey ):
            if aKey in WTXmlLinker._mLinkerDictionary:
                return WTXmlLinker._mLinkerDictionary[ aKey ][ WTXmlLinker._indO ]
            return None

        @staticmethod
        def i( aKey ):
            if aKey in WTXmlLinker._mLinkerDictionary:
                return WTXmlLinker._mLinkerDictionary[ aKey ][ WTXmlLinker._indI ]
            return None

        @staticmethod
        def s( aKey ):
            if aKey in WTXmlLinker._mLinkerDictionary:
                return WTXmlLinker._mLinkerDictionary[ aKey ][ WTXmlLinker._indS ]            
            return None

        @staticmethod
        def c( aKey ):
            if aKey in WTXmlLinker._mLinkerDictionary:
                return WTXmlLinker._mLinkerDictionary[ aKey ][ WTXmlLinker._indC ]            
            return None

        @staticmethod
        def p( aKey ):
            if aKey in WTXmlLinker._mLinkerDictionary:
                return WTXmlLinker._mLinkerDictionary[ aKey ][ WTXmlLinker._indP ]            
            return None