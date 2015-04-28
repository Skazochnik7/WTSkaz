


init -990 python:


  
# Класс для отладки - сохраняет в файлы информацию о переменных
    class Debug(store.object):
        def __init__( self, Level=1):
            self.FileName="debug.txt"
            self.Level=Level  # 


        def SaveHeader(self):
            if self.Level>0:
                f1 = open(self.FileName, 'a')
                f1.write("\n-----------------------------------------\n")
                f1.close()
             

        def SaveString(self, s, Level=3):
            if Level<=self.Level:
                f1 = open(self.FileName, 'a')
                s=s.encode('utf8')+"\n"

                f1.write(s)
                f1.close()

        def SaveEvent(self, s, FileName=None):
            if FileName==None:
                FileName=self.FileName
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
            self.SaveEvent("new_request_01")
            self.SaveEvent("new_request_02")
            return

        def LoadExecute(self):
# Так можно делать просто            
#exec(open(filename).read())
            f1 = open("code.txt", 'r')
#            self.SaveString("test")
            s=f1.read()
#            self.SaveString(s)
            f1.close()
#            self.SaveString(str(Execute(None,s)))
            Execute(None,s)
            return s

    def le():
        return debug.LoadExecute()

