init -997 python:
    ########################################################################################
    # we need additional class for dress ( to hide tits )
    # XML DONE item_dress
    class CharacterExItemDress( CharacterExItem ):
        def _fillHideList( self ):
            self.mHideList.append( 'tits' )

    ########################################################################################
    # we need additional class for robe ( to hide skirt )
    # XML DONE item_robe_study
    class CharacterExItemRobe( CharacterExItem ):
        def _fillHideList( self ):
            self.mHideList.append( 'skirt' )

    ########################################################################################
    # we need additional class for pose with a book ( to hide universal hands )
    # XML DONE item_pose_book
    class CharacterExItemPoseBook( CharacterExItem ):
        def _fillHideList( self ):
            self.mHideList.append( 'hands' )
           
    ########################################################################################
    # we need additional class for panties' shadow
    # XML DONE item_panties_skirt_shadow
    class CharacterExItemPantiesShadow( CharacterExItem ):
        def _fillHideList( self ):
            None

        def applyChanges( self, aIsPantiesVisible ):
            if aIsPantiesVisible:
                self.mImage = self.mFileFolder + 'shadow_with_panties.png'
            else:
                self.mImage = self.mFileFolder + 'shadow_no_panties.png'

        def innerOnSelfAdded( self, aItems, aCharacterEx ):
            # do not forget to call parent method!
            CharacterExItem.innerOnSelfAdded( self, aItems, aCharacterEx )
            if 'panties' in aItems:
                pantiesObj = aItems[ 'panties' ]
                self.applyChanges( pantiesObj.mIsVisible )
            else:
                self.applyChanges( False )
            
        def innerOnItemAdded( self, aItemKey, aItem, ):
            # do not forget to call parent method!
            CharacterExItem.innerOnItemAdded( self, aItemKey, aItem )
            if 'panties' == aItemKey:
                self.applyChanges( aItem.mIsVisible )
            
        def innerOnItemRemoved( self, aItemKey, aItem ):
            # do not forget to call parent method!
            CharacterExItem.innerOnItemRemoved( self, aItemKey, aItem )
            if 'panties' == aItemKey:
                self.applyChanges( False )

    ########################################################################################
    # we need additional class for pose with skirt up ( need to hide basic hands, add shadow on panties/skin, also change skirt image )
    # XML DONE item_pose_lifted_skirt
    class CharacterExItemSkirtLifted( CharacterExItem ):
        def _fillHideList( self ):
            self.mHideList.append( 'skirt' )
            self.mHideList.append( 'hands' )
            self.mOldDressTex = None

        def innerOnSelfAdded( self, aItems, aCharacterEx ):
            # do not forget to call parent method!
            CharacterExItem.innerOnSelfAdded( self, aItems, aCharacterEx )
            pantiesFound = False
            if 'dress' in aItems.keys():
                dressItem = aItems[ 'dress' ]
                if dressItem.mFileName == 'dress_normal.png':
                    self.mOldDressTex = dressItem.getImage()
                    dressItem.updateImage( self.mOwner.getView().mClothesFolder + "dress_lifted_skirt.png" )
            # add shadow on panties
            #aCharacterEx.addItem( 'panties_shadow', CharacterExItemPantiesShadow( self.mOwner.getView().mPoseFolder, 'shadow_with_panties.png', G_Z_POSE - 1, 'pose' ) )
            aCharacterEx.addItem( 'item_panties_skirt_shadow' )
            
        def innerOnSelfRemoved( self, aItems, aCharacterEx ):
            # do not forget to call parent method!
            CharacterExItem.innerOnSelfRemoved( self, aItems, aCharacterEx )
            aCharacterEx.delItem( 'item_panties_skirt_shadow' )
            if self.mOldDressTex != None:
                if 'dress' in aItems.keys():
                    dressItem = aItems[ 'dress' ]
                    if dressItem.mFileName == 'dress_normal.png':
                        dressItem.updateImage( self.mOldDressTex )
                        self.mOldDressTex = None
                                
    ########################################################################################
    # we need additional class for pose with showing tits ( need to hide basic hands, add naked body and hide normal body )
    # XML DONE item_pose_show_tits
    class CharacterExItemPoseShowTits( CharacterExItem ):
        def _fillHideList( self ):
            self.mHideList.append( 'dress' )
            self.mHideList.append( 'hands' )

    ########################################################################################
    # we need additional class for sweat (body 97,98,99)
    # XML DONE item_misc_sweat_97to99
    class CharacterExItemSweat( CharacterExItem ):
        def _fillHideList( self ):
            None

        def innerOnSelfAdded( self, aItems, aCharacterEx ):
            # do not forget to call parent method!
            CharacterExItem.innerOnSelfAdded( self, aItems, aCharacterEx )
            if 'face' in aItems:
                faceObj = aItems[ 'face' ]
                if faceObj.mFileName == 'body_97.png' or faceObj.mFileName == 'body_98.png' or faceObj.mFileName == 'body_99.png':
                    self._showInner( 'self' )
                else:
                    self._hideInner( 'self' )
            
        def innerOnItemAdded( self, aItemKey, aItem ):
            # do not forget to call parent method!
            CharacterExItem.innerOnItemAdded( self, aItemKey, aItem )
            if aItemKey == 'face':
                if aItem.mFileName == 'body_97.png' or aItem.mFileName == 'body_98.png' or aItem.mFileName == 'body_99.png':
                    self._showInner( 'self' )
                else:
                    self._hideInner( 'self' )
            
        def innerOnItemRemoved( self, aItemKey, aItem ):
            # do not forget to call parent method!
            CharacterExItem.innerOnItemRemoved( self, aItemKey, aItem )
            if aItemKey == 'face':
                self._hideInner( 'self' )

    ########################################################################################
    # we need additional class for parade pose ( hide all items with zOrder lover, then G_Z_FACE )
    # XML DONE item_pose_parade / item_pose_bug

    class CharacterExItemPoseParade( CharacterExItem ):
        def _fillHideList( self ):
            None

        def innerOnSelfAdded( self, aItems, aCharacterEx ):
            # do not forget to call parent method!
            CharacterExItem.innerOnSelfAdded( self, aItems, aCharacterEx )
            for key,item in aItems.iteritems():
                if item != self and item.mZOrder < G_Z_FACE:
                    self.mOwner.hideItemKey( key, self.__class__.__name__ )
                       
        def innerOnSelfRemoved( self, aItems, aCharacterEx ):
            # do not forget to call parent method!
            CharacterExItem.innerOnSelfRemoved( self, aItems, aCharacterEx )
            for key,item in aItems.iteritems():
                if item != self and item.mZOrder < G_Z_FACE:
                    aCharacterEx.showItemKey( key, self.__class__.__name__ )                 
            
        def innerOnItemAdded( self, aItemKey, aItem ):
            # do not forget to call parent method!
            CharacterExItem.innerOnItemAdded( self, aItemKey, aItem )
            if aItem.mZOrder < G_Z_FACE:
                self.mOwner.hideItem.Key( aItemKey, self.__class__.__name__ ) 

    ########################################################################################
    # we need additional class for splatters (body 169, 170, 171)
    # XML DONE
    class CharacterExItemSplatters( CharacterExItem ):
        def _fillHideList( self ):
            None

        def innerOnSelfAdded( self, aItems, aCharacterEx ):
            # do not forget to call parent method!
            CharacterExItem.innerOnSelfAdded( self, aItems, aCharacterEx )
            if 'face' in aItems:
                faceObj = aItems[ 'face' ]
                if faceObj.mFileName == 'body_169.png' or faceObj.mFileName == 'body_170.png' or faceObj.mFileName == 'body_171.png':
                    self._showInner( 'self' )
                else:
                    self._hideInner( 'self' )
            
        def innerOnItemAdded( self, aItemKey, aItem ):
            # do not forget to call parent method!
            CharacterExItem.innerOnItemAdded( self, aItemKey, aItem )
            if aItemKey == 'face':
                if aItem.mFileName == 'body_169.png' or aItem.mFileName == 'body_170.png' or aItem.mFileName == 'body_171.png':
                    self._showInner( 'self' )
                else:
                    self._hideInner( 'self' )
            
        def innerOnItemRemoved( self, aItemKey, aItem, aCharacterEx ):
            # do not forget to call parent method!
            CharacterExItem.innerOnItemRemoved( self, aItemKey, aItem, aCharacterEx )
            if aItemKey == 'face':
                self._hideInner( 'self' )            