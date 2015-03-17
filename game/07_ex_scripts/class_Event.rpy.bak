init -997 python:
  
# Класс - обертка для словаря ивентов
    class Event(store.object):
        # constructor - Event initializing
        def __init__( self, sFullName, scenario, points, ready, done, OnChange, defVals, constVals):

            alter=None
            caption=None
            self.Name=sFullName
            if ":" in sFullName:
                sp =sFullName.split(":") 
                self.Name=sp[0]
                alter=sp[1]
                if len(sp)>2: caption=sp[2] 

            self.defVals = {"startCount": 0, "finishCount": 0, "start1": -1, "start2": -1, "finish1": -1, "finish2": -1, "bakfinish1": -1, "bakfinish2": -1,
                            "whored": -1, "bakwhored": -1}        # Это словарь доп. аргументов по умолчанию
            if defVals!=None:
                self.defVals.update(defVals)

            SetArrayValue(self.Name, "ready", ready) 
            SetArrayValue(self.Name, "done", done) 
            SetArrayValue(self.Name, "onChange", OnChange) # Если функция задана, она запустится при изменении какого-нибудь параметра
            SetArrayValue(self.Name, "alter", alter) 
            SetArrayValue(self.Name, "caption", caption) 
            SetArrayValue(self.Name, "points", points) 
            SetArrayValue(self.Name, "scenario", scenario) 

            if constVals!=None:
                for s in constVals:
                    SetArrayValue(self.Name, s, constVals[s]) 




# Альтернатива лямбдам- 
# exec("s_reading_lvl+=1") или 
#    gs = "(lambda x: x * 2 )(%d)"
#    renpy.say( her, "%d" % eval( gs % 2 ) )

        def InitTempVar(self, subkey, value):
#            SetArrayValue(self.Name, "temp", value) 
#            exec "this.GetCall('"+self.Name+"')._"+subkey+"=GetArrayValue('"+self.Name+"','temp')"

            self._temp=value
            exec "this.GetCall('"+self.Name+"')._"+subkey+"=this.GetCall('"+self.Name+"')._temp"
            return            

        def InitTempVars(self):
            __list=GetStoreAllSubKeys(self.Name)
            for subkey in __list:
                self.InitTempVar(subkey, self.GetValue(subkey))
            __list=GetArrayAllSubKeys(self.Name)
            for subkey in __list:
# Нельзя создавать переменные для лямбда- RenPy их пытается записать при сохранении и возвращает ошибку               
                if not subkey in ["ready", "done", "onChange"]:
                    self.InitTempVar(subkey, self.GetValue(subkey))
            return            




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

            self.InitTempVar(subkey, value)

#            debug.SaveString("Class="+self.Name+" subkey("+subkey+")="+str(value))
            fn=GetArrayValue(self.Name,"onChange")
            if fn!=None:
                fn(self, subkey, oldVal, value)
            return value

        def IncValue(self, subkey, incVal):
#            self.res=self.GetValue(subkey)+incVal
            return self.SetValue(subkey, self.GetValue(subkey)+incVal)



        def InitStart(self):
# Не инициализированы еще глобальные переменные и не заполнены значения. Работать напрямую с хранилищем
            for s in self.defVals:
                if not IsStoreSubKey(self.Name, s):
                    SetStoreValue(self.Name, s,  self.defVals[s])
# Создать для каждого параметра в хранилище поле типа self._var
            self.InitTempVars()


        # Произошло ли событие iStartFinishMode iDaysAgo дней назад или раньше?
        def IsExec( self, iDaysAgo, sStartFinishMode ):
            if self.GetValue(sStartFinishMode)==-1:
                return False
            else:
                return self.GetValue(sStartFinishMode) <= day-iDaysAgo

# Было ли завершено?
        def IsFinished( self ):
            return self.IsExec(0, "finish2")

# Логгировать запуск ивента
        def IncStarted( self ):
            if self.GetValue("start1")==-1:
                self.SetValue("start1", day)
            self.SetValue("start2", day)
            self.SetValue("startCount", self.GetValue("startCount")+1)
            return

# Логгировать завершение ивента
        def IncFinished( self ):
# Запомнить значения дат finish для отката на случай, если ивент будет начат и прерван.             
            self.SetValue("bakfinish1", self.GetValue("finish1"))
            self.SetValue("bakfinish2", self.GetValue("finish2"))
            self.SetValue("bakwhored", self.GetValue("whored"))
            if self.GetValue("finish1")==-1:
                self.SetValue("finish1", day)
            self.SetValue("finish2", day)
            self.SetValue("whored", whoring)
            self.IncValue("finishCount", 1)
            return

# Логгировать запуск ивента
        def IncPassed( self ):
            debug.SaveString("before IncStarted")
            self.IncStarted()
            debug.SaveString("after IncStarted")
            self.IncFinished()
            debug.SaveString("after IncFinished")
            return


# Завершено iDays назад или ранее?
        def IsAgo( self, iDays ):
            return self.IsExec(iDays, "finish2")

# Истина, если выполняется одно из условий:
#   Условие __done не задано, но при этом ивент завершен хотя бы раз (IsFinished)
#   Условие __done выполняется
        def IsDone(self):
            fn=GetArrayValue(self.Name,"done")
            val=None if fn==None else fn(self)
            bRes=self.IsFinished() if fn==None else val #or self.GetValue("IsOnDone")
            return bRes

        def IsReady(self):
# Условие старта обязательное, без его выполнения не запустится, как шаг сценария: либо это первый шаг сценария, либо предыдущий уже выполнен
            bReadyDef=True if self.prev==None else self.prev.IsDone()
# Условие старта дополнительное (написанное пользователем), соединяются с дефолтным через И
            fn=GetArrayValue(self.Name,"ready")
            val=None if fn==None else fn(self)
            bReady=True if fn==None else val
            return bReadyDef and bReady

        def IsActive(self):
            return self.IsReady() and not self.IsDone()

        def NotFinished(self):
            self.SetValue("finish1", self.GetValue("bakfinish1"))
            self.SetValue("finish2", self.GetValue("bakfinish2"))
            self.SetValue("whored", self.GetValue("bakwhored"))
            self.IncValue("finishCount", -1)
#            if self.GetValue("finishCount")<0: 
#                self.SetValue("finishCount", 0) # В некоторых случаях finishCount оказывается <0, видимо, из-за неправильной обработки отката. Пока не удается поймать где это, просто блокируем такие ситуации  

# Исполнить ивент
        def Run(self):
            renpy.call(self.Name)




