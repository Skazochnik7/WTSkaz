init python:
    
   
    class MenuItem(store.object):
        def __init__(self, caption, label, isActive, objName):            
            self.caption = caption
            self.label = label
            self.isActive = isActive
            self.objName=objName
    
    class RunMenu(store.object):
        current = None
        screen = "display"
        
        def __init__(self,
            text=None,
            who=None,
            items=None):
#            ,runCall=False 
    
#            self.runCall=runCall
            self.choice=None
            self.Clear()
            if items!=None:
                for i in items:
                    self.AddItem(i)
            if text:
                self.text = text
                if who:
                    self.who = who                                
            
        def AddItem(self, caption=None, label=None, isActive=True, evn=None):
            self.items.append(MenuItem(caption, label, isActive, evn))
            
        def Clear(self):
            self.items = [ ]
            self.text = None
            self.who = None
            
        def Show(self,
            escLabel=None,
            escText=None):
            RunMenu.current = self                        
            if self.text:
                renpy.say(self.who, self.text, interact=False)
#            renpy.say("","in1")
            if escLabel!=None:
                if escText==None:
                    escText="- Ничего -"
#                renpy.say("","in2")
                self.AddItem(escText, escLabel, True, "")
 #           renpy.say("","in3")
            renpy.call_screen(RunMenu.screen)
          

        def SetCurrentMenuItem(self, sName):
            self.choice=sName



screen display:
    add "03_hp/11_misc/bld.png"
    window:
        style "menu_window"
        xalign menu_x
        yalign 0.5

        vbox:
            style "menu"
            spacing 2

            for i in RunMenu.current.items:

                if i.isActive:

                    button:
# Если пытаться по нажатию кнопки сделать не jump, а call, чтобы вернуться по окончанию выполнения блока, то все срабатывает корректно, но затем, если сохранить, то сохранение не читается сохранение, оставил только механизм Jump                   
                        action [Function(this, sName=i.objName), Function(RunMenu.current.SetCurrentMenuItem, sName=i.objName), Jump(i.label)] # if not RunMenu.current.runCall else Function(renpy.call, i.label)] 
                        style "menu_choice_button"

                        text i.caption style "menu_choice"
                
                #if you want items to be hidden instead of grayed out,
                #then delete or modify the else statement
                else:
                    button: 
# Комментированный код показывает текст без кнопки в стиле menu_caption. Но по логике игре эти кнопки можно нажать, при этом выдается заглушка-сообщение. Поэтому кнопки остаются как есть, только подкрашеные
#                       text i.text style "menu_caption" 
                        action [Jump(i.label) ]
                        style "menu_choice_button"                    
                        text "{color=#ffff00}"+i.caption +"{/color}" style "menu_choice"


#                    button:
#                        style "menu_choice_button"               

#                        if i.tt != '':
#                            text "{0} {1}".format(i.text, i.tt) style "menu_choice"
#                        else:
#                            text i.text style "menu_choice"

    zorder 7

                        
