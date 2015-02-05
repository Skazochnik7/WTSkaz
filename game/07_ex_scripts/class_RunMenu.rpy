init python:
    
   
    class MenuItem(store.object):
        def __init__(self, caption, label, isActive, evn):            
            self.caption = caption
            self.label = label
            self.isActive = isActive
            self.event=evn
    
    class RunMenu(store.object):
#        chose = None
        current = None
        screen = "display"
#        event = None
        
        def __init__(self,
            text=None,
            who=None,
            items=None):
    
            self.Clear()
            if items!=None:
                for i in items:
                    self.AddItem(i)
            self.SetPrompt(text, who)
            
        def AddItem(self, caption=None, label=None, isActive=True, evn=None):
            self.items.append(MenuItem(caption, label, isActive, evn))
            
        def Clear(self):
            self.items = [ ]
            self.text = None
            self.who = None
            
        def Show(self):
            RunMenu.current = self                        
            if self.text:
                renpy.say(self.who, self.text, interact=False)
            renpy.call_screen(RunMenu.screen)
            
        def SetPrompt(self, text=None, who=None):
            if text:
                self.text = text
                if who:
                    self.who = who                                
            return self.text




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
                        action [Function(this, sName=i.event.Name), Jump(i.label) ]
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

                        
