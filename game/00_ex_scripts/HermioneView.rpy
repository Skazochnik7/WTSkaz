init -999:
    screen HermioneViewScreen( aData, aPos ):
        python:
            dataToSort = aData.values()
            sorted_data = sorted( dataToSort, key = lambda item: item.mZOrder )
        for element in sorted_data:
            if element.mIsVisible == True:
                if element.mIsAdditional == False:
                    add element.mPath at aPos
                else:
                    add element.mPath at gSumPos( aPos, element.mItemPos )
                
        zorder hermione_main_zorder

init -998 python:
  
    class HermioneView:
        # constructor - memorizing Character object
        def __init__( self, aCharacter1, aCharacter2 ):
            self.mCh = aCharacter1
            self.mCh2 = aCharacter2
            self.mChActive = 0
            # currenlty dressed things
            self.mStuff = {}
            # here we'll save all items on Hermione
            self.mSavedItems = {}
            
            # memorize default pathes
            self.mBodyFolder = "00_ex/00_hermione/body/"
            self.mClothesFolder = "00_ex/00_hermione/clothes/"
            self.mFaceFolder = "00_ex/00_hermione/face/"
            self.mPoseFolder = "00_ex/00_hermione/pose/"
            
        # need for using as simple character dialogue
        def __call__( self, what, interact = True ):
            if self.mChActive == 0:
                return self.mCh( what, interact = interact )
            else:
                return self.mCh2( what, interact = interact )
                
        # need for using as simple character dialogue
        def predict( self, what ):
            if self.mChActive == 0:
                return self.mCh.predict( what )
            else:
                return self.mCh2.predict( what )
        
        #-----------------------------#
        
        # call this to switch from first character to second and reverse
        def change( self, aCharNum ):
            self.mChActive = aCharNum
        
        #-----------------------------#
        
        # show hermione screen with data parameters
        def showSelf( self, aData, aPos, aTransition = None ):
            renpy.show_screen( "HermioneViewScreen", aData, aPos )
            if aTransition is not None:
                renpy.with_statement( aTransition )            
        
        # hide hermione screen
        def hideSelf( self, aTransition = None ):
            renpy.hide_screen( "HermioneViewScreen" )
            if aTransition is not None:
                renpy.with_statement( aTransition )            
            
        #-----------------------------#
        
        # show hermione screen with saved parameters
        def showQ( self, aFace, aPos, aTransition = None ):
            if aFace is not None:
                self.addFace( HermioneItem( self.mFaceFolder, aFace, G_Z_FACE ) )
            renpy.show_screen( "HermioneViewScreen", self.mStuff, aPos )
            if aTransition is not None:
                renpy.with_statement( aTransition, None, True )
        
        # hide hermione screen
        def hideQ( self, aTransition = None ):
            self.hideSelf( aTransition )

        # below is two methods to simplifying typing
        def showQQ( self, aFace, aPos ):
            self.showQ( aFace, aPos, d3 )
        def hideQQ( self ):
            self.hideQ( d3 )

        #------------------------------#
        
        # call this to remove all items from hermione mStuff
        def clear():
            self.mStuff = {}
        
        #------------------------------#
            
        # add additional stuff on hermione ( permanent )
        def addAdditional( self, aKey, aHermioneItem ):
            self._addItem( aKey, aHermioneItem )
        
        # del additional stuff on hermione ( permanent )
        def delAdditional( self, aKey ):
            self._delItem( aKey )
            
        #------------------------------#
        
        # save/load/clear current items set
        def saveState( self ):
            self.mSavedItems = self.mStuff
    
        def loadState( self ):
            self.mStuff = self.mSavedItems
            
        def clearState( self ):
            self.mSavedItems = {}
            
        #------------------------------#

        # methods to add/del important parts of clothes, but you still can use addAdditional/delAdditional methods
        
        def addLegs( self, aData ):
            self._addItem( 'legs', aData )
        def delLegs( self ):
            self._delItem( 'legs' )
            
        def addHands( self, aData ):
            self._addItem( 'hands', aData )
        def delHands( self ):
            self._delItem( 'hands' )
            
        def addPanties( self, aData ):
            self._addItem( 'panties', aData )
        def delPanties( self ):
            self._delItem( 'panties' )

        def addSkirt( self, aData ):
            self._addItem( 'skirt', aData )
        def delSkirt( self ):
            self._delItem( 'skirt' )
            
        def addBody( self, aData ):
            self._addItem( 'body', aData )
        def delBody( self ):
            self._delItem( 'body' )
        
        #additional function for face to pass only file name
        def addFaceName( self, aFace ):
            self._addItem( 'face', HermioneItem( self.mFaceFolder, aFace, G_Z_FACE ) )
        
        def addFace( self, aData ):
            self._addItem( 'face', aData )
        def delFace( self ):
            self._delItem( 'face' )
            
        def addPose( self, aData ):
            self._addItem( 'pose', aData )
        def delPose( self ):
            self._delItem( 'pose' )

        #------------------------------#
        
        #DO NOT CALL CALL THESE METHODS DIRECTLY, THEY'RE INNER!
        def _addItem( self, aName, aData ):
            aData.onSelfAdded( self.mStuff, self )
            for item in self.mStuff.values():
                item.onItemAdded( aData, self )
            self.mStuff[ aName ] = aData

        def _delItem( self, aName ):
            data = self.mStuff[ aName ]
            data.onSelfRemoved( self.mStuff, self )
            del self.mStuff[ aName ]
            for item in self.mStuff.values():
                item.onItemRemoved( data, self )          
                
        ##
        # MAYBE OBSOLETE, USE WITH CARE
        ##
        # methods below used for simplifying your life :) they creates data for showing Hermione in some common states
        # return value is a dictionary, so you can change there whatever you want
        # define more methods if you want
        
        def getDataDressed( self, aFace ): #aSkirtType = "normal"
            dicRes = {}
            dicRes[ 'legs' ] = HermioneItem( self.mBodyFolder + "legs_universal.png", G_Z_LEGS )
            dicRes[ 'panties' ] = HermioneItem( self.mClothesFolder + "panties_normal.png", G_Z_PANTIES )          
            dicRes[ 'hands' ] = HermioneItem( self.mBodyFolder + "hands_universal.png", G_Z_HANDS )
            dicRes[ 'body' ] = HermioneItem( self.mBodyFolder + "body_dressed.png", G_Z_BODY )
            dicRes[ 'face' ] = HermioneItem( self.mFaceFolder + aFace, G_Z_FACE )
            
            dicRes.update( self.mStuff )
            return dicRes

        def getDataNaked( self, aFace ):
            dicRes = {}
            dicRes[ 'legs' ] = HermioneItem( self.mBodyFolder + "legs_universal.png", G_Z_LEGS )
            dicRes[ 'hands' ] = HermioneItem( self.mBodyFolder + "hands_universal.png", G_Z_HANDS )
            dicRes[ 'body' ] = HermioneItem( self.mBodyFolder + "body_naked.png", G_Z_BODY )
            dicRes[ 'face' ] = HermioneItem( self.mFaceFolder + aFace, G_Z_FACE )

            if G_N_NETS in self.mStuff:
                dicRes[ G_N_NETS ] = self.mStuff[ G_N_NETS ]
            return dicRes
            
        def getDataDressedSkirtUp( self, aWithPants = "with" ):
            dicRes = {}
            dicRes[ 'legs' ] = HermioneItem( self.mBodyFolder + "legs_universal.png", G_Z_LEGS )
            if aWithPants == "with":
                dicRes[ 'panties' ] = HermioneItem( self.mClothesFolder + "panties_normal.png", G_Z_PANTIES )
                dicRes[ 'panties_shadow' ] = HermioneItem( self.mPoseFolder + "shadow_" + aWithPants + "_pants.png", G_Z_PANTIES + 1 )
            elif aWithPants == "no":
                dicRes[ 'panties_shadow' ] = HermioneItem( self.mPoseFolder + "shadow_" + aWithPants + "_pants.png", G_Z_PANTIES + 1 )
            dicRes[ 'body' ] = HermioneItem( self.mBodyFolder + "body_dressed.png", G_Z_BODY )
            dicRes[ 'pose' ] = HermioneItem( self.mPoseFolder + "pose_skirt_up.png", G_Z_POSE )
            dicRes[ 'face' ] = HermioneItem( self.mFaceFolder + "body_01.png", G_Z_FACE )
            
            dicRes.update( self.mStuff )
            del dicRes[ G_N_SKIRT ]
            return dicRes
            
        def getDataDressedDressUp( self ):
            dicRes = {}
            dicRes[ 'legs' ] = HermioneItem( self.mBodyFolder + "legs_universal.png", G_Z_LEGS )
            dicRes[ 'body' ] = HermioneItem( self.mBodyFolder + "body_naked.png", G_Z_BODY )
            dicRes[ 'pose' ] = HermioneItem( self.mPoseFolder + "pose_dress_up.png", G_Z_POSE )
            dicRes[ 'face' ] = HermioneItem( self.mFaceFolder + "body_01.png", G_Z_FACE )

            dicRes.update( self.mStuff )
            del dicRes[ G_N_BADGE ]
            return dicRes
