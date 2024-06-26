from screenwrite import ScreenWriter
from pyhook import hook

from spotifyinfo import spotifySong
from animategif import MyLabel

from datetime import datetime

import win32api, win32con

import tkinter as Tkinter

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
        gif_path="valeriya-kim-edel-valentines-ver2.gif"
        label = MyLabel(root,gif_path,callback)
    if args.current_key == 'K' and args.event_type == 'key down' and 'Lcontrol' in args.pressed_key:
        print("Ctrl + K was pressed")
        print('fontSize = '+str(self.fontSize))
        self.fontSize -= 2
        print('fontSize = '+str(self.fontSize))
        gif_path="valeriya-kim-miku.gif"
        label = MyLabel(root,gif_path,callback)

h=hook(hCallback,mouse=False)

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
    msg+='\n'
    msg+=spotifySong()
    self.text.set(msg)
    return getState()

root=Tkinter.Tk()

sw=ScreenWriter(root,swCallback)

def callback(self):
    pass
    #return 'q'

def main():
        #root=Tkinter.Tk()
        #gif_path="C:\\Users\\winuser\\Downloads\\R.gif"
        gif_path="R.gif"
        gif_path="valeriya-kim-miku.gif"
        gif_path="valeriya-kim-edel-valentines-ver2.gif"
        label = MyLabel(root,gif_path,callback)

main()
