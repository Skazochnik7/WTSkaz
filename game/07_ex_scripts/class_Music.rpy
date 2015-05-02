init -999 python:

# Работа с музыкой
    class Music(store.object):
        # constructor - Entry initializing
        def __init__( self): # 
            self.List=[]
            self.Name=None
            self.volume=1.0
            return

        def __call__( self, name=None, volume=1.0):
            if (name!=None):
                if name=="<": # Вернуться к предыдущей
                    self.List.pop() # Убрать из списка текущую/последнюю проигранную
                    name=self.List.pop() # Убрать из списка предыдущщую и запомнить ее.
                self.Start(name, volume) # Зfпустить проигрывание
            else:
                self.Stop()
            return e


        def Start(self,name, volume=1.0):
            self.Name=name
            self.List.append(self.Name)
            music_volume=1.0
            if name=="Supergirl":
                name="music/Reamonn-Supergirl.mp3"
                music_volume=0.2
            elif name=="Daphne Theme":
                name="music/Bittersweet Symphony (Instrumental).mp3"
                music_volume=0.2
            elif name=="Daphne Privacy":
                name="music/Cure-Lullaby.mp3"
                music_volume=0.2

#            renpy.music.stop(fadeout=1.0)
#            renpy.pause(1.0)
            self.Stop()
            renpy.music.play(name, fadein=1, fadeout=1)
            renpy.music.set_volume(music_volume*volume) 
            return

        def Stop(self):
            if self.volume==1.0:
                renpy.music.stop(fadeout=2.0)
            else:
                renpy.music.stop(fadeout=2.0)
#                renpy.pause(1.0) # Если играющая композиция громче других, то после начала затухания выдерживается пауза, затем восстанавливается уровень по умолчанию
            renpy.music.set_volume(1.0,3.0) 
            return

#        def MusicVolumeReset(self):
#            renpy.music.set_volume(1.0) 
#            return
