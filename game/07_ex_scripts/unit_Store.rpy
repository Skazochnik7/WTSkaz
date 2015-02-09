label after_load:
# Метка - зерезервированная RenPy. На нее программа переходит после загрузки.
# Код ниже инициализирует переменные хранилища, если они не были инициализированы (например, написан новый шаг сценария)
# Этот же код вызываем из блока start для начальной инициализации переменных
    python:
        if hasattr(renpy.store,"elog"):
            this.InitStart()
            if event!=None: # Состояние переменной объекта event после чтения сохранения может отличаться от полей объекта this.GetCall(event.Name). 
                for e in this.List: # Нужно сопоставить их, иначе присвоение полей одного из объектов непредсказуемо влмияет на поля другого
                    if e.Name==event.Name:
                        event=this.GetCall(event.Name)
                        break
        else:
            this.InitTempVars()
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
    return

init -999 python:


# Функции для работы со словарем elog - сохранятеся
    def IsStoreKey(key):
        return key in elog

    def IsStoreSubKey(key, subkey):
        if IsStoreKey(key):
            return subkey in elog[key]
        return False

    def SetStoreValue(key, subkey, value):
        if not IsStoreKey(key):
            elog.update({key: dict()})
        if not IsStoreSubKey(key, subkey):
            elog[key].update({subkey: value})
        else:
            elog[key][subkey]=value

# Намеренно не ставлю здесь проверок на наличие соответствующего поля. Разработчик должен проверять перед вызовом с помощью функций  IsStoreKey IsStoreSubKey
    def GetStoreValue(key, subkey):
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
        if not IsArrayKey(key):
            arr.update({key: dict()})
        if not IsArraySubKey(key, subkey):
            arr[key].update({subkey: value})
        else:
            arr[key][subkey]=value

# Намеренно не ставлю здесь проверок на наличие соответствующего поля. Разработчик должен проверять перед вызовом с помощью функций  IsStoreKey IsStoreSubKey
    def GetArrayValue(key, subkey):
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

