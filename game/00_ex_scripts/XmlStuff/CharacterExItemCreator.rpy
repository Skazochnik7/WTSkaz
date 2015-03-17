init -998 python:
    class CharacterExItemCreator:
        def __init__( self, aItemBase, aSetBase, aXmlLinkerKey ):
            self.mItemBase = aItemBase
            self.mSetBase = aSetBase
            self.mXmlLinkerKey = aXmlLinkerKey    # key from linker

        # create single item by name
        # return one item
        def createItem( self, aItemName, aStyle = 'default' ):
            itemDesc = self.mItemBase.get( aItemName )
            if itemDesc != None:
                newItem = CharacterExItem.create( itemDesc, self.mXmlLinkerKey )
                if newItem.mActiveStyle != None and newItem.mActiveStyle != aStyle:
                        newItem.setStyle( aStyle )
                return newItem
            else:
                return None

        # here you pass the set name ( !!! SET NAME MUST BE WITHOUT * !!! )
        # return list of items from set
        def createSet( self, aSetName, aStyle = 'default' ):
            setItems = self.mSetBase.get( aSetName )
            if setItems != None:
                resList = []
                for item in setItems:
                    newItem = self.createItem( item )
                    if newItem.mActiveStyle != None and newItem.mActiveStyle != aStyle:
                        newItem.setStyle( aStyle )
                    resList.append( newItem )
                return resList
            else:
                return [None]

        # here you can pass item name or set name ( !!! SET NAME MUST START WITH * !!! )
        # for better using, always return a list of items ( list with one item or with set items )
        def create( self, aItemOrSetName, aStyle = 'default' ):
            if aItemOrSetName[0] == '*':
                setName = aItemOrSetName[1:]
                return self.createSet( setName, aStyle )
            else:
                return [self.createItem( aItemOrSetName, aStyle )]