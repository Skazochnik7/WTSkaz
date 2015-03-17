init -997 python:
  
# Класс - обертка для словаря ивентов
    class Entry(store.object):
        # constructor - Event initializing
        def __init__( self, Name, Type, defVals=None, constVals=None): # 
            self.Name=Name
            self.Type=Type

            self.defVals = defVals        # Это словарь доп. аргументов по умолчанию

#            SetArrayValue(self.Name, "Type", Type) 

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

        def SetValue(self, subkey, value):
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


            fn=GetArrayValue(self.Name,"onChange")
            if fn!=None:
                fn(self, subkey, oldVal, value)
            return value

        def IncValue(self, subkey, incVal, minimum=None, maximum=None):
            __temp=self.GetValue(subkey)+incVal
            if minimum!=None:
                if __temp<minimum:
                    __temp=minimum
            if maximum!=None:
                if __temp>maximum:
                    __temp=maximum
            return self.SetValue(subkey, __temp)






