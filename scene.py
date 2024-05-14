import win32com.client
import win32gui

def listWindows():
    def winEnumHandler( hwnd, ctx ):
        if win32gui.IsWindowVisible( hwnd ):
            print ( hex( hwnd ), win32gui.GetWindowText( hwnd ) )
    win32gui.EnumWindows( winEnumHandler, None )

#listWindows()

import time

class Scene(object):
    def __init__(self):
        self.state=0
        self.shell = win32com.client.Dispatch("WScript.Shell")
        self.t0=0

    def doSendKeys(self,cmd):
        self.shell.AppActivate('OBS 30.1.2')
        #shell.AppActivate("Notepad")
        #shell.SendKeys("^a")  # Press CTRL+A (select all)
        #shell.SendKeys("{DELETE}")  # Delete selected text (depends on context)
        #shell.SendKeys("{TAB}")  # Press tab to change focus or perform other actions
        #shell.SendKeys('aaaa')
        import time
        time.sleep(0.2)

        self.shell.SendKeys(cmd,200)      #ctrl shift H

    def switchScene(self):
        t=time.time()
        if((t-self.t0)>3):       #make sure not to do this twice for some reason.
            if(self.state==0):
                print(str(t))
                print('state 0: sending H')
                self.doSendKeys('^(H)')      #ctrl shift H
            else:
                print(str(t))
                print('state 1: sending J')
                self.doSendKeys('^(J)')
            self.state+=1
            self.state=self.state%2
        self.t0=t
