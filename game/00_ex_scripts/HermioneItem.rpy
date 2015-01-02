label main_ex_HermioneItem_constants:
    # main zOrders
    define G_Z_UNDERLEGS = 0
    define G_Z_LEGS = 20
    define G_Z_PANTIES = 40
    define G_Z_SKIRT = 60
    define G_Z_HANDS = 80
    define G_Z_BODY = 100
    define G_Z_FACE = 200
    
    # additional zOrders
    define G_Z_POSE = 110
    define G_Z_HEADWEAR = 120

    # here is the keys for additional items
    define G_N_SKIRT = "skirt"
    define G_N_BADGE = "badge"
    define G_N_NETS = "nets"
    
    return

init -999 python:
    
    class HermioneItem:
        # create hermione item's description, if aPos == None, created item counts as NOT ADDITIONAL
        def __init__( self, aFolder, aName, aOrder, aPos = None ):
            self.mName = aName
            self.mFileFolder = aFolder
            self.mPath = aFolder + aName
            self.mZOrder = aOrder
            self.mItemPos = Transform( pos = ( 0, 0 ) )
            self.mIsVisible = True
            self.mIsAdditional = False
            if aPos is not None:
                self.mIsAdditional = True
                self.mItemPos = aPos
            # here we'll store all items, which affects visibility of this item
            # items, stored here change the visibility to FALSE
            self.mDirectors = set()

        def onSelfAdded( self, aItems, aHermioneView ):
            # this called when THIS item is added to Hermione
            # we can add additional items, needed for this item, to HermioneView
            # do nothing in base class
            None
            
        def onSelfRemoved( self, aItems, aHermioneView ):
            # this called just before deleting SELF from Hermione
            # do nothing in base class
            None
        
        def onItemAdded( self, aItem, aHermioneView ):
            # this called when other new item added to Hermione, and THIS item is existed before it
            # we can add additional items, needed for this item, to HermioneView
            # do nothing in base class
            None
            
        def onItemRemoved( self, aItem, aHermioneView ):
            # this called when other new item added to Hermione, and THIS item is existed before it
            # we can add additional items, needed for this item, to HermioneView
            # do nothing in base class
            None

        # do not call this anywhere from this class
        def _hide( self, aSource ):
            self.mIsVisible = False
            self.mDirectors.add( aSource )
                
        def _show( self, aSource ):
            self.mDirectors.discard( aSource )
            if not self.mDirectors:
                self.mIsVisible = True
