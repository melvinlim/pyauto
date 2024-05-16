from screenwrite import ScreenWriter
from pyhook import hook

from datetime import datetime

import win32api, win32con

state='running'

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

h.state=state

def getState():
    print(h.state)
    return h.state

def getTime():
    now = datetime.now()
    current_time = now.strftime('%H:%M:%S')
    return current_time

def swCallback(self):
    self.text.set(getTime())
    return getState()

sw=ScreenWriter(swCallback)
