init -999 python:

# Класс - работа со временем
    class Time(store.object):
        def __init__( self): # ELog:
            return

        def __call__( self):
            return self.stamp


        def Day(self, stamp=None):
            if (stamp==None):
                stamp=self.stamp
            return stamp//10000

        def Hour(self, stamp=None):
            if (stamp==None):
                stamp=self.stamp
            return (stamp-self.Day(stamp)*10000)//100

        def Minute(self, stamp=None):
            if (stamp==None):
                stamp=self.stamp
            return stamp-self.Day(stamp)*10000-self.Hour(stamp)*100

        def IsPassed(self, oldstamp, interval, intervalType="h"):
            self.__min=(self.Day(self.stamp)-self.Day(oldstamp))*24*60+(self.Hour(self.stamp)-self.Hour(oldstamp))*60+(self.Minute(self.stamp)-self.Minute(oldstamp))
            if intervalType=="m":
                return self.__min>=interval
            elif intervalType=="h":
                return self.__min/60>=interval
            elif intervalType=="d":
                return self.__min/(24*60)>=interval
            return None

        def IsAllFinishedAgo(self, interval, intervalType="h", scenario=None, points=None ):
            return self.IsPassed(this.GetTime("finish2",scenario, points), interval, intervalType)

        def IsAllStartedAgo(self, interval, intervalType="h", scenario=None, points=None ):
            return self.IsPassed(this.GetTime("start2",scenario, points), interval, intervalType)

        
        @property
        def stamp(self): # Можно было бы в минуты переводить, но тогда читается хуже при отладке
            return day*10000+900+1200*(1-daytime)


