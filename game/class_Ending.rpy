label Ending_constants:
    # 
    define const_ENDING_PUBLIC_WHORE = 2
    define const_ENDING_YOUR_WHORE = 1
    define const_ENDING_STRONG_GIRL = 3

    return

init -999 python:
  
# Класс для удобного управления концовками. При инициализации в игре создается объект $ end = Ending()
    class Ending(store.object):
        # constructor - Ending initializing
        def __init__( self ):
            self.Index = const_ENDING_YOUR_WHORE # Номер концовки по умолчанию
            self.Values = {const_ENDING_YOUR_WHORE : 1, const_ENDING_PUBLIC_WHORE : 0, const_ENDING_STRONG_GIRL : 0} # Рейтинги концовки. В финале показывается концовка с наибольшим рейтингом. Если рейтинги одинаковы, то концовка, которая получила его последней 
                
# Установить рейтинг концовке под номером  iIndex, например : $ end.SetEndingValue(const_ENDING_STRONG_GIRL, 1)               
        def SetEndingValue( self, iIndex, iValue ):
            self.Values[iIndex]=iValue
            self.Index = iIndex
            for key in self.Values:
                if self.Values[key] > self.Values[iIndex]:
                    self.Index = key

# Добавить рейтинг концовке под номером  iIndex, например : $ end.IncEndingValue(const_ENDING_STRONG_GIRL, 1)               
        def IncEndingValue( self, iIndex, iIncValue ):
            self.SetEndingValue( iIndex, self.Values[iIndex]+iIncValue )

# Финальная концовка - iIndex? , например : if end.IsEnding(const_ENDING_STRONG_GIRL): # дальше код, который выполняется если условие - истинно               
        def IsEnding( self, iIndex ):
            if self.Index==iIndex:
                return True
            else:
                return False

# Получить номер финальной концовки, например : $ CurrentEnding= end.GetEnding()               
        def GetEnding( self ):
            return self.Index

# Получить текущий рейтинг для концовки iIndex, например : $ CurrentValue= end.GetEndingValue(const_ENDING_STRONG_GIRL)               
        def GetEndingValue( self, iIndex ):
            return self.Values[iIndex]


# Получить строку поздравления с окончанием игры для финальной концовки, например : centered "[end.Congratulation()]"" 
        def Congratulation ( self ):
            return "{size=+7}{color=#cbcbcb}Поздравляем с прохождением игры!{/color}{/size}\n\n{size=+5}{color=#cbcbcb}Это концовка \"0"+str(self.Index)+"\" из \"0"+str(len(self.Values))+"\".{/color}{/size}"

# Запомнить в объекте persistent финальную концовку, например : $ end.UpdatePersistent() 
        def UpdatePersistent ( self ):
            if persistent.endings is None:
                persistent.endings = set()
            persistent.endings.update({self.Index});

# Является ли концовка iIndex запомненной (т.е.) проходили ли ее раньше, например : if not end.IsPersistent(1): # дальше код, который выполняется, если условие истинно
        def IsPersistent ( self, iIndex ):
            return iIndex in persistent.endings

