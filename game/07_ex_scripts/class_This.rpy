init -992 python:
  
# Класс - тот же EventCollection , только со специфическим объявлениями
    class This(EventCollection): # Код специфический для игры, все в этом классе
        def __init__(self):
            super(This, self).__init__()
            self.Name=None

# this("event_01") пытается вернуть Event c именем event_01 (None, если не нашел в списке)
# Запоминает парметр - последнее обращение
        def __call__( self, sName=None):
            if (sName!=None): 
                this.Name=sName
# Если уже активирована глобальная переменная event, ей присваивается новое значение, если, конечно, это ивент 
            e=self.GetCall(self.Name)
            if hasattr(renpy.store,"event") and (e!=None): 
                renpy.store.event=e
            return e



# НЕ ПРИНАДЛЕЖИТ КЛАССУ
    def OnLabelExecute(s):
        try:
            if s[0]!="_":
                labelHistory.append(s)
                if len(labelHistory)>120:
                    del labelHistory[0:len(labelHistory)-121]

    # Каждый раз при переходе по метке происходит проверка - не имя ли ивента метка? Если да, переменной event присваивается значение, согласно текущей метке
                if this(s)!=None:
    # Если перешли на метку, которая есть ивент, автоматически запускается увеличение счетчика стартов-финишей. 
    # Случаи, когда ивент завершается на середине (и требуют уменьшания счетчика финишей) обрабатываются в коде самого ивента                
                    this().IncPassed()

        except Exception:
            pass


# Если текущий ивент - единственный после метки actualLabel, то пометить его, как не финишировавший.
# Пример: на метку too_much переход происходит только если Гермиона отказывается выполнять задания
# Часть из этих заданий оформлены как ивенты, часть - нет. Все задания начинаються после метки захода в меню выбора заданий
# Значит надо отследить запускался ли текущий ивент (хранящийся в event) после метки захода в меню выбора заданий, и если да, то откатить финиширование
# Альтернатива: 1. Все задания оформить как ивенты и ставить в too_much $event.NotFinished() без этого условия  2. В кажом ивенте перед каждой директивой jump too_much ставить $event.NotFinished()
    def IsEventOnlyAfter(actualLabel):
        for s in reversed(labelHistory[0:len(labelHistory)-2]): 
            if s==actualLabel:
                break
            if not this.GetCall(s) in [None, renpy.store.event.Name]: # Если результат - ивент, отличный от заданного
                return False
        return True

    def Execute(e, s, condition=True):
        if not condition: return False
        s=s.replace("_e.", "this.GetCall('"+e.Name+"').")
        exec s
        return True


    def Rand(iMax): #от 1 до iMax
        import random 
        return int(random.random()*iMax+1)

    def RandFromSet(availSet, onetimeSet={}):
        o=list(availSet)[Rand(len(availSet))-1]
        if o in onetimeSet:
            availSet-={o}                
        return o


#    def OnJumpExecute(loc, target, expression):
#        try:
#            if s[0]!="_":
#            jumpHistory.append({loc, target, expression})


#        except Exception:
#            pass



