init -998 python:
  
# Класс - обертка для словаря ивентов
    class EventCollection(store.object):
        def __init__( self): # ELog:
            scenario=None
            points={}
            self.List=[] # Упорядоченный список ивентов.
            
# Можно вызвать eco("Name") и получить ивент "Name",
# Если вызвать с параметром None - получим саму коллекцию (полезно, если обращаться через лямбду)
        def __call__( self, sName=None):
            return self.GetCall(sName)

        def GetCall( self, sName=None):
            if sName==None:
                return self
           
            for e in self.List:
                if e.Name==sName:
                    return e

            return None


        def InitStart( self ):
            for e in self.List:
                e.InitStart()

        def InitTempVars(self):                
            for e in self.List:
                e.InitTempVars()

        def Where(self,points, scenario=""):
            self.scenario=scenario
# Необходимо делать копию, иначе скопируется просто ссылка на объект            
            self.points=points.copy()
            return self

# Внимание! Не проверяется на наличие в списке одноименных! Необходимо внимательно описывать секцию Init
        def AddStep( self, sFullName, ready=None, done=None, OnChange=None, defVals=None, constVals=None):
# Необходимо делать копию, иначе скопируется просто ссылка на объект            
            self.AddEvent(sFullName, self.scenario, self.points.copy(), ready, done, OnChange, defVals, constVals)


# Внимание! Не проверяется на наличие в списке одноименных! Необходимо внимательно описывать секцию Init
        def AddEvent( self, sFullName, scenario=None, points={}, ready=None, done=None, OnChange=None, defVals=None, constVals=None):
            prev=None
            prevInList=None

            if len(self.List)>0:
                prevInList=self.List[len(self.List)-1]

            for e in self.List:
                if e.GetValue("scenario")==scenario:
                    prev=e

            self.List.append(Event(sFullName, scenario, points, ready, done, OnChange, defVals, constVals))
# Нужно ставить не max(self.List), а self.List[len(self.List)-1] , max почему-то выдает предыдущее значение    ?!
            if prev!=None: prev.next=self.List[len(self.List)-1]
            self.List[len(self.List)-1].prev=prev
            self.List[len(self.List)-1].prevInList=prevInList
            
            return self.List[len(self.List)-1]



# Был ли завершен ивент (установлен флаг завершения)? Как параметр можно подать имя или альтернативное имя
        def Has( self, sNameOrAlter):
            for e in self.List:
                if e.Name==sNameOrAlter or e._alter==sNameOrAlter:
                    return e.IsDone()
            return False


# Поскольку список ивентов создается в блоке инит, порядок следования ивентов жестко зафиксирован
# Если несколько ивентов могут запускаться в одной и той же точке, запустится тот, который был добавлен раньше (по движении по списку запускается первый ивент, который удовлетворяет условиям)
# Смысл сценария - связать события в одну нить. Если события в одном сенарии, последующее не может запуститься, пока не выполнено (IsDone) предыдущее.
        def GetStep(self, point):
            for e in self.List:
                 if (point in e._points) and e.IsActive() and e._scenario!=None:
                        return e

            return None

        def IsStep(self, point):
            return self.GetStep(point) != None

# Исполнить шаг (если есть готовый для исполнения)
        def RunStep(self, point):
            e = self.GetStep(point)
            if e!=None:
                e.Run()










