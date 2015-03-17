init -997 python:
  
# Класс - обертка для словаря ивентов
    class Item(Entry):
        # constructor - Event initializing
        def __init__( self, Name, status, defVals=None):
            if defVals==None:
                defVals={"status": status}
            else:
                defVals.update({"status": status})
            super(Item, self).__init__(Name=Name, Type="Item", defVals=defVals )







