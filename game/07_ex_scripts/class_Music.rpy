init -999 python:

# Работа с музыкой
    class Music(store.object):
        # constructor - Entry initializing
        def __init__( self): # 
            self.List=[]
            self.Name=None
#            self.volume=1.0
            return

        def __call__( self, name=None):
            if (name!=None):
                if name=="<": # Вернуться к предыдущей
                    self.List.pop() # Убрать из списка текущую/последнюю проигранную
                    name=self.List.pop() # Убрать из списка предыдущщую и запомнить ее.
                self.Start(name) # Зfпустить проигрывание
            else:
                self.Stop()
            return e


        def Start(self,name):
            self.Name=name
            self.List.append(self.Name)

            self.__music_start_set={
                "Supergirl":"music/Reamonn-Supergirl.mp3",
                "Daphne Theme":"music/Bittersweet Symphony (Instrumental).mp3",
                 "Daphne Privacy": "music/Cure-Lullaby.mp3"  
            }

            self.Name = name if self.__music_start_set.get(name)==None else self.__music_start_set.get(name)
#            self.Stop()
            renpy.music.play(self.Name, fadein=1, fadeout=1)
            return

        def Stop(self):
            renpy.music.stop(fadeout=2.0)
            renpy.pause(2.1)
            return

#        def MusicVolumeReset(self):
#            renpy.music.set_volume(1.0) 
#            return
