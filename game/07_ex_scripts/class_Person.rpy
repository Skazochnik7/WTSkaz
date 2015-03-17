init -997 python:
  
# Класс - обертка для словаря ивентов
    class Person(Entry):
        # constructor - Event initializing
        def __init__( self, Name, caption, defVals=None):
            SetArrayValue(Name, "caption", caption) 

            if defVals==None:
                defVals={"test":0}

            super(Person, self).__init__(Name=Name, Type="Person", defVals=defVals )

            self._Items=RegEntry(ItemCollection("items"+self.Name))        # Это словарь сохраняемых аргументов
#            if defVals
#            self.defVals = {"Items": ItemCollection("items"+self.Name)}        # Это словарь сохраняемых аргументов
#            if defVals!=None:
#                self.defVals.update(defVals)

