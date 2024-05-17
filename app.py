from screenwrite import ScreenWriter
from pyhook import hook

from datetime import datetime

import win32api, win32con

def hCallback(self,args):
    key=args.current_key
    print('key '+key+' was pressed.')
    if args.current_key == 'L' and args.event_type == 'key down' and 'Lcontrol' in args.pressed_key:
        self.state='q'
        print("Ctrl + L was pressed")
        print('quitting')
        print('press CTRL-D to close Idle window.')
        win32api.PostThreadMessage(self.main_thread_id, win32con.WM_QUIT, 0, 0);
    if args.current_key == 'J' and args.event_type == 'key down' and 'Lcontrol' in args.pressed_key:
        print("Ctrl + J was pressed")
        print('fontSize = '+str(self.fontSize))
        self.fontSize += 2
        print('fontSize = '+str(self.fontSize))
    if args.current_key == 'K' and args.event_type == 'key down' and 'Lcontrol' in args.pressed_key:
        print("Ctrl + K was pressed")
        print('fontSize = '+str(self.fontSize))
        self.fontSize -= 2
        print('fontSize = '+str(self.fontSize))

h=hook(hCallback)

h.state='running'
h.fontSize=20

def getState():
    #print(h.state)
    return h

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
