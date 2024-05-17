from screenwrite import ScreenWriter
from pyhook import hook

from datetime import datetime

import win32api, win32con

def hCallback(self,args):
    key=args.current_key
    print('key '+key+' was pressed.')
    if args.current_key == 'L' and args.event_type == 'key down' and 'Lcontrol' in args.pressed_key:
        self.state='q'
        print("Ctrl + L was pressed");
        print('quitting')
        print('press CTRL-D to close Idle window.')
        win32api.PostThreadMessage(self.main_thread_id, win32con.WM_QUIT, 0, 0);

h=hook(hCallback)

h.state='running'

def getState():
    #print(h.state)
    return h.state

def getTime():
    now = datetime.now()
    current_time = now.strftime('%H:%M:%S')
    return current_time

from activewindow import activeWin

def swCallback(self):
    msg=str(getTime())+'\n'+str(activeWin())
    self.text.set(msg)
    return getState()

sw=ScreenWriter(swCallback)
