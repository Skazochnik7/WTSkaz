


init -990 python:


  
# Класс - обертка для словаря логов ивентов
    class Debug(store.object):
        # constructor - Event initializing
        def __init__( self):
            self.FileName="debug.txt"
            self.On=True


        def SaveHeader( self):
            if self.On:
                f1 = open(self.FileName, 'a')
                f1.write("\n-----------------------------------------\n")
                f1.close()
             

# Когда будет несколько пересекающихся сценариев, условие нужно переписать
        def SaveFullEventInfo(self, evn, step, readyDef=None, ready=None, done=None):
            if self.On:
                f1 = open(self.FileName, 'a')
                sPrev="None"
                if evn.prev!=None:
                    sPrev=evn.prev.Name

                s=evn.Name+" : StartCount="+str(evn.StartCount)+" : FinishCount="+str(evn.FinishCount)+" : prev="+sPrev+" : block="+step["block"]
                if readyDef!=None and ready!=None:
                    s+=" : ready(Def&User)="+str(readyDef(evn))+"&"+str(ready(evn))
                if done!=None:
                    s+=" : done="+str(done(evn))

                f1.write(s+"\n")
        #                f1.write(time.time())
                f1.close()

        def SaveString( self, s):
            if self.On:
                f1 = open(self.FileName, 'a')
                s=s+"\n"
                f1.write(s)
                f1.close()

        def SaveClass( self, s):
            self.e=this.GetCall(s)
            self.SaveString(str(self.e.__dict__)+", IsReady()="+str(self.e.IsReady())+", IsDone()="+str(self.e.IsDone())+", IsActive()="+str(self.e.IsActive()) )


        def Dump( self):
#            self.SaveString("labelHistory\n"+str(labelHistory))
#            self.SaveClass("new_request_15")
#            self.SaveClass("new_request_15_complete")
#            self.SaveClass("new_request_20")
#            self.SaveClass("new_request_20_complete")
#            self.SaveClass("new_request_23")
#            self.SaveClass("new_request_23_complete")
#            self.SaveClass("new_request_24")
#            self.SaveClass("new_request_24_complete")
#            self.SaveClass("new_request_30")
#            self.SaveClass("new_request_30_complete")
            self.SaveClass("new_request_01")
            self.SaveClass("new_request_02")
            return

        def LoadExecute(self):
# Так можно делать просто            
#exec(open(filename).read())
            f1 = open("code.txt", 'r')
            self.SaveString("test")
            s=f1.read()
            self.SaveString(s)
            f1.close()
            self.SaveString(str(Execute(None,s)))
            return s



