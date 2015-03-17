init -997 python:
  
# Класс - обертка для словаря ивентов
    class ItemCollection(Entry):
        # constructor - Event initializing
        def __init__( self, Name, allItemCount=0):
            self.Name=Name

            super(ItemCollection, self).__init__(Name=Name, Type="ItemCollection", defVals={"Counts": []} )

            for o in itemList:
                self.defVals["Counts"].append(allItemCount)






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

        def AddItem(self, itemName, count=1): # на вход сет {"имя вещи":кол-во} кол-во может быть отрицательным  
            for i in range(len(itemList) - 1):
                if itemList[i].Name==itemName:
                    self.GetValue("Counts")[i]+=count
                    if self.GetValue("Counts")[i]<0:
                        self.GetValue("Counts")[i]=0
            return self.GetValue("Counts")[i]

#            _count=1 if itemPars.get("count")==None else itemPars["count"]
#            _status=0 if itemPars.get("status")==None else itemPars["status"]
#            defVals=itemPars.get("defVals")


#            while _count>0:
#                self.items.append(Item(s, _status, defVals))
#                _count-=1
#            if _count<0:
#                i=0
#                while i <= len(self.items) - 1: # идем по индексам, итерировать нельзя - меняется структура массива
#                    if self.items[i].Name==s:
#                        del(self.items[i])
#                    else:
#                        i+=1

        def Count(self, Name):
            for i in range(len(itemList) - 1):
                if itemList[i].Name==Name:
                    return self.GetValue("Counts")[i]
            return 0

        def Clear(self):
            for i in range(len(itemList) - 1):
                self.GetValue("Counts")[i]=0

        def Any(self):
            renpy.say("", "test")
            for i in range(len(itemList) - 1):
                if self.GetValue("Counts")[i]>0:
                    return True
            return False


        def GetList(self, level=0):
            self.list=[]
            for i in range(len(itemList) - 1):
                if self.GetValue("Counts")[i]>level:
                    self.list.append(itemList[i])
            return self.list

        
        def First(self):
            return self.GetList()[0]






