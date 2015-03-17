init -999 python:
    class WTXmlLinker:
        _lkHermione = 'hermione'

        @staticmethod
        def gerHermioneLinkerKey():
            return WTXmlLinker._lkHermione

        @staticmethod
        def f( aKey ):
            if aKey == WTXmlLinker._lkHermione:
                return Hermione_FB
            return None

        @staticmethod
        def o( aKey ):
            if aKey == WTXmlLinker._lkHermione:
                return Hermione_OB
            return None

        @staticmethod
        def i( aKey ):
            if aKey == WTXmlLinker._lkHermione:
                return Hermione_IB
            return None

        @staticmethod
        def s( aKey ):
            if aKey == WTXmlLinker._lkHermione:
                return Hermione_SB
            return None

        @staticmethod
        def c( aKey ):
            if aKey == WTXmlLinker._lkHermione:
                return Hermione_ItemCreator
            return None