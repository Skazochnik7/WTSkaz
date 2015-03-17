init -997 python:
  
# Класс - обертка для словаря ивентов
    class ItemCollection(Entry):
        # constructor - Event initializing
        def __init__( self, Name, allItemCount=0):
            self.Name=Name

            super(ItemCollection, self).__init__(Name=Name, Type="ItemCollection" )
            self.defVals=dict()
            for o in itemList:
                self.defVals.update({o.Name+"_count":allItemCount})    



        def __call__( self, sName=None):
            if sName==None:  # ItemCollection() - список всех, которых количество больше 0
                return self.GetList(0)
            for o in itemList: # Item по имени
                if o.Name==sName:
                    return o
            return None

#        def AddItems(self, itemSet): # на вход сет {"имя вещи":кол-во} кол-во может быть отрицательным  
        #   AddItems({"candy":{"status":0, "defVals":None, "count":5}})  
        #   AddItems({"candy":{}})  - дефлтное
        #   Пока вещи добавляются по отдельности, а не просто количество, т.е. предполагается, что у двух предметов одного типа могут быть разные характеристики
        #   Если не пригодится, можно упростить структуру
#            for s in itemSet:
#                self.AddItem(s, itemSet[s])    
#            return

        def AddItem(self, Name, count=1): # на вход сет {"имя вещи":кол-во} кол-во может быть отрицательным  
            return self.IncValue(self.Count(Name),count, minimum=0)


        def Count(self, Name):
            return self.GetValue(Name+"_count")

        def Clear(self):
            for o in self.defVals:
                self.SetValue(o.Name, 0)

        def Any(self):
            for o in self.defVals:
                if self.GetValue(o.Name)>0:
                    return True
            return False


        def GetList(self, level=0):
            self.__list=[]
            for i in range(len(itemList) - 1):
                if self.Count(itemList[i].Name)>level:
                    self.__list.append(itemList[i])
            return self.__list

        
        def First(self):
            return self.GetList()[0]






