label after_load:
# Метка - зерезервированная RenPy. На нее программа переходит после загрузки.
# Код ниже инициализирует переменные хранилища, если они не были инициализированы (например, написан новый шаг сценария)
# Этот же код вызываем из блока start для начальной инициализации переменных
    python:
        InitEntriesFields()
    return

label start_elog:    
    # Elog class initialization
    # Инициализация словаря параметров, которые необходимо записывать при сохранении и списка, содержащего историю перехода по меткам
    python:
        global elog
        global labelHistory
        global jumpHistory
        
    $elog=dict()
    $labelHistory=[]
    $jumpHistory=[]
#    $entries=[]
    return

init -999 python:

    import sys
    reload(sys)
    sys.setdefaultencoding('utf8')


# Функции для работы со словарем elog - сохранятеся
    def IsStoreKey(key):
        return key in elog

    def IsStoreSubKey(key, subkey):
        if IsStoreKey(key):
            return subkey in elog[key]
        return False

    def SetStoreValue(key, subkey, value):
#        debug.SaveString("SetStoreValue("+str(key)+", "+str(subkey)+", "+str(value), 3)
        if not IsStoreKey(key):
            elog.update({key: dict()})

        __SetStoreValue_oldvalue=GetStoreValue(key, subkey)

        if not IsStoreSubKey(key, subkey):
            elog[key].update({subkey: value})
        else:
            elog[key][subkey]=value
        OnChangeStoreValue(key, subkey, __SetStoreValue_oldvalue, value) # Перехватываем все изменения

# Намеренно не ставлю здесь проверок на наличие соответствующего поля. Разработчик должен проверять перед вызовом с помощью функций  IsStoreKey IsStoreSubKey
    def GetStoreValue(key, subkey):
        if IsStoreKey(key):
#            debug.SaveString("GetStoreValue("+str(key)+", "+str(subkey)+")="+str(elog[key].get(subkey)), 3)
            pass
        else:
            debug.SaveString("GetStoreValue("+str(key)+", "+str(subkey)+")=НЕТ КЛЮЧА!", 3)

        return elog[key].get(subkey)

    def GetStoreAllSubKeys(key):
        res=[]
        for s in elog:
            if s==key:
                for subkey in elog[s]:
                    res.append(subkey)
                return res
        return res



# Полная копия по функционалу верхнего блока процедур, но работает с объектом arr, который объявляется в блоке Init и не сохранятется и каждый раз инициализируется

    def IsArrayKey(key):
        return key in arr

    def IsArraySubKey(key, subkey):
        if IsArrayKey(key):
            return subkey in arr[key]
        return False

    def SetArrayValue(key, subkey, value):
#        debug.SaveString("SetArrayValue("+str(key)+", "+str(subkey)+", "+str(value), 3)
        if not IsArrayKey(key):
            arr.update({key: dict()})
        if not IsArraySubKey(key, subkey):
            arr[key].update({subkey: value})
        else:
            arr[key][subkey]=value

# Намеренно не ставлю здесь проверок на наличие соответствующего поля. Разработчик должен проверять перед вызовом с помощью функций  IsStoreKey IsStoreSubKey
    def GetArrayValue(key, subkey):
#        debug.SaveString("GetArrayValue("+str(key)+", "+str(subkey)+")="+str(arr[key].get(subkey)), 3)
        return arr[key].get(subkey)

    def GetArrayAllSubKeys(key):
        res=[]
        for s in arr:
            if s==key:
                for subkey in arr[s]:
#                    renpy.say(her,str(key)+" "+str(s)+" "+subkey)
                    res.append(subkey)
                return res
        return res

#    def GetLabelCount(s):
#        return labelHistory.count(s)

#    def IsLabelCountEq(s1, s2):
#        return labelHistory.count(s1)==labelHistory.count(s2)



    def RegEntry(entry):
        entry.handle=len(entries)
        entries.append(entry)
        return entry

    def GetEntry(Name):
        for o in entries:
            if o.Name==Name:
                return o
        return None


    def GetEntriesByType(typeName):
        __set=set()
        for o in entries:
            if o.Type==typeName:
                __set.update({o})
        return __set

    def InitEntryField(entry, subkey):
        exec "entries["+str(entry.handle)+"]._"+subkey+"=entries["+str(entry.handle)+"].GetValue('"+subkey+"')"
        return            

    def InitEntriesFields():
        if hasattr(renpy.store,"elog"): # Если уже инициализирован elog
#            this.InitStart()
            if hasattr(renpy.store,"event"):
                if renpy.store.event!=None: # Состояние переменной объекта event после чтения сохранения может отличаться от полей объекта this.GetCall(event.Name). 
                    for e in this.List: # Нужно сопоставить их, иначе присвоение полей одного из объектов непредсказуемо влияет на поля другого
                        if e.Name==renpy.store.event.Name:
                            renpy.store.event=this.GetCall(renpy.store.event.Name)
                            break

            for o in entries:   # Если значение не заполнено (т.е. разрабдотчик ввел новое или новый объект появился) - заполнить значениями по умолчанию
                for subkey in o.defVals:
                    if not IsStoreSubKey(o.Name, subkey):
                        SetStoreValue(o.Name, subkey,  o.defVals[subkey])
#        else:
        for o in entries: # для всех объектов типа наследников Entry создать поля типа  объект._имяпеременной
            __list=GetStoreAllSubKeys(o.Name)
            for subkey in __list:
                InitEntryField(o, subkey)
            __list=GetArrayAllSubKeys(o.Name)
            for subkey in __list:
# Нельзя создавать переменные для лямбда- RenPy их пытается записать при сохранении и возвращает ошибку               
                if not subkey in ["ready", "done"]:
                    InitEntryField(o, subkey)
        storeInitialized=True


    def OnChangeStoreValue(key, subkey, oldvalue, newvalue):
        __entry=GetEntry(key)        
        if __entry.Type=="Event":
# Если заключено соглашение с Гермионой, то после каждой встречи с Дафной Гриффиндор получает 10 очков
            if (__entry.GetValue("members")!=None):
                if ("daphne" in __entry.GetValue("members")) and (subkey=="finishCount") and (newvalue>(0 if oldvalue==None else oldvalue)):
                    if hermi._pointsPerDaphneVisit>0:
                        Say("По вашему соглашению с Гермионой Гриффиндор получает 10 очков")
                        renpy.store.gryffindor+=10

