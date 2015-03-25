init -997 python:
  
# Класс - обертка для словаря ивентов
    class Person(Entry):
        # constructor - Event initializing
        def __init__( self, Name, caption, defVals=None):
            SetArrayValue(Name, "caption", caption) 

            if defVals==None:
                defVals={"liking":0, "whoring":0}

            super(Person, self).__init__(Name=Name, Type="Person", defVals=defVals )

            self.Items=RegEntry(ItemCollection("items"+self.Name))        # Это словарь сохраняемых аргументов
#            if defVals
#            self.defVals = {"Items": ItemCollection("items"+self.Name)}        # Это словарь сохраняемых аргументов
#            if defVals!=None:
#                self.defVals.update(defVals)

            return

        @property
        def liking(self):
            return self.GetValue("liking")
        @liking.setter
        def liking(self, value):
            self.SetValue("liking", value, minim=-100, maxim=0)

        @property
        def whoring(self):
            return self.GetValue("whoring")
        @whoring.setter
        def whoring(self, value):
            self.SetValue("whoring", value, minim=0)




# При таком описании проперти объект корретно сохранялся/читался
#        @property
#        def liking(self):
#            return self.GetValue("test")
#        @liking.setter
#        def liking(self, value):
#            if renpy.store.whoring>0:
#                renpy.store.whoring+=1
#            self.SetValue("test", value)

