init -998 python:
     
    # we need additional class for robe ( to hide skirt )
    class CharacterExItemRobe( CharacterExItem ):
        def onSelfAdded( self, aItems, aCharacterEx ):
            # this called when THIS item is added to Hermione
            for element in aItems.keys():
                if element == 'skirt':
                    item = aItems[ 'skirt' ]
                    item._hide( 'CharacterExItemRobe' )
            
            
        def onSelfRemoved( self, aItems, aCharacterEx ):
            # this called just before deleting SELF from Hermione
            for element in aItems.keys():
                if element == 'skirt':
                    item = aItems[ 'skirt' ]
                    item._show( 'CharacterExItemRobe' )

    # we need additional class for pose with book ( to hide universal hands and body )
    class CharacterExItemPoseBook( CharacterExItem ):
        def onSelfAdded( self, aItems, aCharacterEx ):
            # this called when THIS item is added to Hermione
            for element in aItems.keys():
                if element == 'body':
                    itemBody = aItems[ 'body' ]
                    itemBody._hide( 'CharacterExItemPoseBook' )
                if element == 'hands':
                    itemHands = aItems[ 'hands' ]
                    itemHands._hide( 'CharacterExItemPoseBook' )
            
            
        def onSelfRemoved( self, aItems, aCharacterEx ):
            # this called just before deleting SELF from Hermione
            for element in aItems.keys():
                if element == 'body':
                    itemBody = aItems[ 'body' ]
                    itemBody._show( 'CharacterExItemPoseBook' )
                if element == 'hands':
                    itemHands = aItems[ 'hands' ]
                    itemHands._show( 'CharacterExItemPoseBook' )
        
    # we need additional class for robe ( to hide skirt )
    class CharacterExItemRobe( CharacterExItem ):
        def onSelfAdded( self, aItems, aCharacterEx ):
            # this called when THIS item is added to Hermione
            for element in aItems.keys():
                if element == 'skirt':
                    item = aItems[ 'skirt' ]
                    item._hide( 'CharacterExItemRobe' )
            
            
        def onSelfRemoved( self, aItems, aCharacterEx ):
            # this called just before deleting SELF from Hermione
            for element in aItems.keys():
                if element == 'skirt':
                    item = aItems[ 'skirt' ]
                    item._show( 'CharacterExItemRobe' )
        
    
    # we need additional class for pose with skirt up ( need to hide basic hands, add shadow on panties/skin )
    
    
    # we need additional class for pose with showing tits ( need to hide basic hands, add naked body and hide normal body )
    

    # we need additional class for naked body ( to hide badge, if present )
    class CharacterExItemBodyNaked( CharacterExItem ):
        def onSelfAdded( self, aItems, aCharacterEx ):
            # this called when THIS item is added to Hermione
            for element in aItems.keys():
                if element == G_N_BADGE:
                    item = aItems[ G_N_BADGE ]
                    item._hide( 'CharacterExItemBodyNaked' )
            
            
        def onSelfRemoved( self, aItems, aCharacterEx ):
            # this called just before deleting SELF from Hermione
            for element in aItems.keys():
                if element == G_N_BADGE:
                    item = aItems[ G_N_BADGE ]
                    item._show( 'CharacterExItemBodyNaked' )
        
