init -997 python:
  
# Базовый класс, содержит методы работы с хранилищами arr и elog
    class Entry(store.object):
        # constructor - Entry initializing
        def __init__( self, Name, Type, defVals=None, constVals=None): # 
            self.Name=Name
            self.Type=Type

            self.defVals = defVals        # Это словарь доп. аргументов со значениями по умолчанию

            if constVals!=None:
                for s in constVals:
                    SetArrayValue(self.Name, s, constVals[s]) 
            return



# Альтернатива лямбдам- 
# exec("s_reading_lvl+=1") или 
#    gs = "(lambda x: x * 2 )(%d)"
#    renpy.say( her, "%d" % eval( gs % 2 ) )


        def GetValue(self, subkey):
            if subkey in self.defVals:
                return GetStoreValue(self.Name, subkey)
            else:
                return GetArrayValue(self.Name, subkey) 

        def SetValue(self, subkey, value, minim=None, maxim=None):
            if minim!=None:
                if value<minim:
                    value=minim
            if maxim!=None:
                if value>maxim:
                    value=maxim
            if subkey in self.defVals:
                if IsStoreSubKey(self.Name, subkey):
                    oldVal=GetStoreValue(self.Name, subkey)
                else:
                    oldVal=None
                SetStoreValue(self.Name, subkey, value)
            else:
                if IsArraySubKey(self.Name, subkey):
                    oldVal=GetArrayValue(self.Name, subkey)
                else:
                    oldVal=None
                SetArrayValue(self.Name, subkey, value)

            InitEntryField(self, subkey)

            if IsArrayKey("onChange"): # Если подключена обработка на изменение
                fn=GetArrayValue(self.Name,"onChange")
                if fn!=None:
                    fn(self, subkey, oldVal, value)
            return value

        def IncValue(self, subkey, incVal, minim=None, maxim=None):
            return self.SetValue(subkey, self.GetValue(subkey)+incVal, minim, maxim)






