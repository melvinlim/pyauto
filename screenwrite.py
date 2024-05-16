from random import choice, randrange
from datetime import datetime
from ctypes import windll

def getTime():
    now = datetime.now()
    current_time = now.strftime('%H:%M:%S')
    return current_time

import tkinter as Tkinter
import win32api
import win32con
import win32gui
import pywintypes

def nop(self):
    pass

class ScreenWriter(object):
    def __init__(self,callback=None):
        root=Tkinter.Tk()
        self.text=Tkinter.StringVar()
        #text.set('Text variable\nasdf')

        #modified from https://stackoverflow.com/questions/21840133/how-to-display-text-on-the-screen-without-a-window-using-python
        label = Tkinter.Label(root,
            textvariable=self.text,
            #text='Text on the screen',
            font=('Times New Roman','80'),
            fg='gray',
            bg='white')
        label.master.overrideredirect(True)
        label.master.geometry("+250+250")
        label.master.lift()
        label.master.wm_attributes("-topmost", True)
        label.master.wm_attributes("-disabled", True)
        label.master.wm_attributes("-transparentcolor", "white")

        hWindow = pywintypes.HANDLE(int(label.master.frame(), 16))
        # http://msdn.microsoft.com/en-us/library/windows/desktop/ff700543(v=vs.85).aspx
        # The WS_EX_TRANSPARENT flag makes events (like mouse clicks) fall through the window.
        exStyle = win32con.WS_EX_COMPOSITED | win32con.WS_EX_LAYERED | win32con.WS_EX_NOACTIVATE | win32con.WS_EX_TOPMOST | win32con.WS_EX_TRANSPARENT
        win32api.SetWindowLong(hWindow, win32con.GWL_EXSTYLE, exStyle)

        label.pack()
        #label.mainloop()

        if(not callback):
            callback=nop

        while True:
            if(callback(self)=='q'):
                break
            root.update_idletasks()
            root.update()

#def callback(self):
#    self.text.set(getTime())

#sw=ScreenWriter(callback)
