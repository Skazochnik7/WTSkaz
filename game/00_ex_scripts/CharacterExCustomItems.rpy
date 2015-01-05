init -998 python:
    ########################################################################################
    # we need additional class for dress ( to hide tits )
    class CharacterExItemDress( CharacterExItem ):
        def _fillHideList( self ):
            self.mHideList.append( 'tits' )

    ########################################################################################
    # we need additional class for robe ( to hide skirt )
    class CharacterExItemRobe( CharacterExItem ):
        def _fillHideList( self ):
            self.mHideList.append( 'skirt' )

    ########################################################################################
    # we need additional class for pose with a book ( to hide universal hands )
    class CharacterExItemPoseBook( CharacterExItem ):
        def _fillHideList( self ):
            self.mHideList.append( 'hands' )
           
    ########################################################################################
    # we need additional class for pose with skirt up ( need to hide basic hands, add shadow on panties/skin, also change skirt image )
    class CharacterExItemSkirtLifted( CharacterExItem ):
        def _fillHideList( self ):
            self.mHideList.append( 'skirt' )
            self.mHideList.append( 'hands' )
            self.mOldDressTex = None

        def innerOnSelfAdded( self, aItems, aCharacterEx ):
            # do not forget to call parent method!
            CharacterExItem.innerOnSelfAdded( self, aItems, aCharacterEx )
            pantiesFound = False
            if 'panties' in aItems.keys():
                pantiesFound = True
            if 'dress' in aItems.keys():
                dressItem = aItems[ 'dress' ]
                if dressItem.mName == 'dress_normal.png':
                    self.mOldDressTex = dressItem.getImage()
                    dressItem.updateImage( aCharacterEx.mClothesFolder + "dress_lifted_skirt.png" )
            # add shadow on panties
            if pantiesFound:
                aCharacterEx.addItem( 'panties_shadow', CharacterExItem( aCharacterEx.mPoseFolder, 'shadow_with_pants.png', G_Z_PANTIES + 1, 'panties' ) )
            else:
                aCharacterEx.addItem( 'panties_shadow', CharacterExItem( aCharacterEx.mPoseFolder, 'shadow_no_pants.png', G_Z_PANTIES + 1, 'legs' ) )
            
            
        def innerOnSelfRemoved( self, aItems, aCharacterEx ):
            # do not forget to call parent method!
            CharacterExItem.innerOnSelfRemoved( self, aItems, aCharacterEx )
            aCharacterEx.delItem( 'panties_shadow' )
            if self.mOldDressTex != None:
                if 'dress' in aItems.keys():
                    dressItem = aItems[ 'dress' ]
                    if dressItem.mName == 'dress_normal.png':
                        dressItem.updateImage( self.mOldDressTex )
                        self.mOldDressTex = None
            
            
        def innerOnItemAdded( self, aItemKey, aItem, aCharacterEx ):
            # do not forget to call parent method!
            CharacterExItem.innerOnItemAdded( self, aItemKey, aItem, aCharacterEx )
            if aItemKey == 'panties':
                dataShadow = aCharacterEx.getItem( 'panties_shadow' )
                if dataShadow != None and dataShadow.mName == 'shadow_no_pants.png':
                    aCharacterEx.addItem( 'panties_shadow', CharacterExItem( aCharacterEx.mPoseFolder, 'shadow_with_pants.png', G_Z_PANTIES + 1, 'panties' ) )
            
            
        def innerOnItemRemoved( self, aItemKey, aItem, aCharacterEx ):
            # do not forget to call parent method!
            CharacterExItem.innerOnItemRemoved( self, aItemKey, aItem, aCharacterEx )
            if aItemKey == 'panties':
                dataShadow = aCharacterEx.getItem( 'panties_shadow' )
                if dataShadow != None and dataShadow.mName == 'shadow_with_pants.png':
                    aCharacterEx.addItem( 'panties_shadow', CharacterExItem( aCharacterEx.mPoseFolder, 'shadow_no_pants.png', G_Z_PANTIES + 1, 'legs' ) )
                    
    ########################################################################################
    # we need additional class for pose with showing tits ( need to hide basic hands, add naked body and hide normal body )
