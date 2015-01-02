init -998 python:
     
    # we need additional class for pose with book ( to hide universal hands and body )
    class HermioneItemPoseBook( HermioneItem ):
        def onSelfAdded( self, aItems, aHermioneView ):
            # this called when THIS item is added to Hermione
            for element in aItems.keys():
                if element == 'body':
                    itemBody = aItems[ 'body' ]
                    itemBody._hide( 'HermioneItemPoseBook' )
                if element == 'hands':
                    itemHands = aItems[ 'hands' ]
                    itemHands._hide( 'HermioneItemPoseBook' )
            
            
        def onSelfRemoved( self, aItems, aHermioneView ):
            # this called just before deleting SELF from Hermione
            for element in aItems.keys():
                if element == 'body':
                    itemBody = aItems[ 'body' ]
                    itemBody._show( 'HermioneItemPoseBook' )
                if element == 'hands':
                    itemHands = aItems[ 'hands' ]
                    itemHands._show( 'HermioneItemPoseBook' )
        
    # we need additional class for robe ( to hide skirt )
    class HermioneItemRobe( HermioneItem ):
        def onSelfAdded( self, aItems, aHermioneView ):
            # this called when THIS item is added to Hermione
            for element in aItems.keys():
                if element == 'skirt':
                    item = aItems[ 'skirt' ]
                    item._hide( 'HermioneItemRobe' )
            
            
        def onSelfRemoved( self, aItems, aHermioneView ):
            # this called just before deleting SELF from Hermione
            for element in aItems.keys():
                if element == 'skirt':
                    item = aItems[ 'skirt' ]
                    item._show( 'HermioneItemRobe' )
        
    
    # we need additional class for pose with skirt up ( need to hide basic hands, add shadow on panties/skin )
    
    
    # we need additional class for pose with showing tits ( need to hide basic hands, add naked body and hide normal body )