import pywinauto
import win32com.client
import win32gui
import pyautogui

import time

from pynput import keyboard

def listWindows():
    def winEnumHandler( hwnd, ctx ):
        if win32gui.IsWindowVisible( hwnd ):
            print ( hex( hwnd ), win32gui.GetWindowText( hwnd ) )
    win32gui.EnumWindows( winEnumHandler, None )

listWindows()
#exit()

app = pywinauto.Application(backend='uia')
#app.connect(title_re=".*Microsoft Edge.*")
app.connect(title_re=".*Edge.*")
#app.connect(title_re=".*Microsoft Edge.*", found_index=0)
dlg = app.top_window()
wrapper = dlg.child_window(title="App bar", control_type="ToolBar")
url = wrapper.descendants(control_type='Edit')

print(url[0].get_value())

def visit(page):
    url[0].iface_value.SetValue(page)
    pyautogui.keyDown('\n')
    time.sleep(0.2)
    pyautogui.keyUp('\n')

#visit('biztoc.com')

def enumDesc(wind):
    asdf=wind.descendants()
    results=[]
    for x in asdf:
        data=x.window_text()
        if(len(data) > 80):
#        if(x.window_text()!=''):
#            if(x.class_name()!=''):
#                if(x.class_name() not in ['tag','lmr']):
                    #print('ClassName: '+x.class_name())
                    print(data)
                    results += [x]
    return results

asdf=enumDesc(dlg)

