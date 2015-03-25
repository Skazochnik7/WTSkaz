init -997 python:
  
# Класс - обертка для словаря ивентов
    class Item(Entry):
        # constructor - Event initializing
        def __init__( self, Name, status, defVals=None):
            if defVals==None:
                defVals={"status": status, "count":0}
            else:
                defVals.update({"status": status, "count":0})
            super(Item, self).__init__(Name=Name, Type="Item", defVals=defVals )







