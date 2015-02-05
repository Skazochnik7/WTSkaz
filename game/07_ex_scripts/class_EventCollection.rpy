init -998 python:
  
# Класс - обертка для словаря ивентов
    class EventCollection(store.object):
        def __init__( self): # ELog:
            self.List=[] # Упорядоченный список ивентов.
#            self.ELog=ELog
            
# Можно вызвать eco("Name") и получить ивент "Name",
# Если вызвать с параметром None - получим саму коллекцию (полезно, если обращаться через лямбду)
        def __call__( self, sName=None):
            return self.GetCall(sName)

        def InitStart( self ):
            for e in self.List:
                e.InitStart()

        def InitTempVars(self):                
            for e in self.List:
                e.InitTempVars()


# Внимание! Не проверяется на наличие в списке одноименных! Необходимо внимательно описывать секцию Init
        def AddEvent( self, sFullName, scenario, block, ready, done, OnChange=None, defVals=None, constVals=None):
            prev=None
            prevInList=None

            if len(self.List)>0:
                prevInList=self.List[len(self.List)-1]

            for e in self.List:
                if e.scenario==scenario:
                    prev=e

            self.List.append(Event(sFullName, scenario, block, ready, done, OnChange, defVals, constVals))
# Нужно ставить не max(self.List), а self.List[len(self.List)-1] , max почему-то выдает предыдущее значение    ?!
            if prev!=None: prev.next=self.List[len(self.List)-1]
            self.List[len(self.List)-1].prev=prev
            self.List[len(self.List)-1].prevInList=prevInList
            
            return self.List[len(self.List)-1]



        def GetCall( self, sName=None):
            if sName==None:
                return self
           
            for e in self.List:
                if e.Name==sName:
                    return e

            return None



# Для функционала Flag, параметр вызов или Name или AlterName
# Был ли завершен ивент? Как параметр можно подать имя или альтернативное имя
        def IsDone(self, sNameOrAlter):
            for e in self.List:
                if e.Name==sNameOrAlter or e._alter==sNameOrAlter:
                    return e.IsDone()
            return False










