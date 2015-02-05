
init -993 python:
  
# Обертка точки исполнения ивентов
    class RunPoint(store.object):
        # constructor - Event initializing
        def __init__( self, Name, ECO, defLabel=None):
            self.Name=Name
            self.ECO=ECO


# Добавить вызов процедуры/перехода в сценарий для этой точки
        def AddCall( self, sFullName, scenario="", ready=None, done=None, OnChange=None, defVals=None):
            self.ECO.AddEvent(sFullName, scenario, self.Name, ready, done, OnChange, defVals, None)


# Поскольку список ивентов создается в блоке инит, порядок следования ивентов жестко зафиксирован
# Если несколько ивентов могут запускаться в одной и той же точке, запустится тот, который был добавлен раньше (по движении по списку запускается первый ивент, который удовлетворяет условиям)
# Смысл сценария - связать события в одну нить. Если события в одном сенарии, последующее не может запуститься, пока не выполнено (IsDone) предыдущее.
        def GetStep(self):
            for e in self.ECO.List:
                 if e._block==self.Name and e.IsActive() :
                        return e

            return None

        def IsStep(self):
            return self.GetStep() != None

# Исполнить шаг (если есть готовый для исполнения)
        def RunStep(self):
            e = self.GetStep()
            if e!=None:
                e.Run()


            
                




