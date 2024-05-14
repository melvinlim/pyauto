import win32com.client
import win32gui

def listWindows():
    def winEnumHandler( hwnd, ctx ):
        if win32gui.IsWindowVisible( hwnd ):
            print ( hex( hwnd ), win32gui.GetWindowText( hwnd ) )
    win32gui.EnumWindows( winEnumHandler, None )

#listWindows()

def doSendKeys(cmd):
    shell = win32com.client.Dispatch("WScript.Shell")
    shell.AppActivate('OBS 30.1.2')
    #shell.AppActivate("Notepad")
    #shell.SendKeys("^a")  # Press CTRL+A (select all)
    #shell.SendKeys("{DELETE}")  # Delete selected text (depends on context)
    #shell.SendKeys("{TAB}")  # Press tab to change focus or perform other actions
    #shell.SendKeys('aaaa')
    import time
    time.sleep(0.2)

    shell.SendKeys(cmd)      #ctrl shift H

def switchScene():
    if(state==0):
        doSendKeys('^(H)')      #ctrl shift H
    else:
        doSendKeys('^(J)')
    state+=1
    state=state%2

#class scene(object):
#    __init__(self):
#        self.state=0
