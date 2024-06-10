from random import choice, randrange
from datetime import datetime
from ctypes import windll

def getTime():
    now = datetime.now()
    current_time = now.strftime('%H:%M:%S')
    return current_time

import tkinter as Tkinter
import tkinter.font as tkFont
import win32api
import win32con
import win32gui
import pywintypes

def nop(self):
    pass

class ScreenWriter(Tkinter.Label):
    def __init__(self,root,callback=None):
        #root=Tkinter.Tk()
        self.text=Tkinter.StringVar()
        self.font=tkFont.Font(family='Times New Roman',size=40)
        #text.set('Text variable\nasdf')

        #modified from https://stackoverflow.com/questions/21840133/how-to-display-text-on-the-screen-without-a-window-using-python
        Tkinter.Label.__init__(self,
            root,
            textvariable=self.text,
            #text='Text on the screen',
            #font=('Times New Roman','80'),
            font=self.font,
            anchor='w',         #align text to left boundary of window
            justify='left',     #align text to left boundary of window
            fg='gray',
            bg='white')
        self.master.overrideredirect(True)
        #self.master.geometry("+250+250")
        #self.master.geometry("+0+0")
        self.master.geometry("+0+100")     #x and y locations
        self.master.lift()
        self.master.wm_attributes("-topmost", True)
        self.master.wm_attributes("-disabled", True)
        self.master.wm_attributes("-transparentcolor", "white")

        hWindow = pywintypes.HANDLE(int(self.master.frame(), 16))
        # http://msdn.microsoft.com/en-us/library/windows/desktop/ff700543(v=vs.85).aspx
        # The WS_EX_TRANSPARENT flag makes events (like mouse clicks) fall through the window.
        exStyle = win32con.WS_EX_COMPOSITED | win32con.WS_EX_LAYERED | win32con.WS_EX_NOACTIVATE | win32con.WS_EX_TOPMOST | win32con.WS_EX_TRANSPARENT
        win32api.SetWindowLong(hWindow, win32con.GWL_EXSTYLE, exStyle)

        self.pack()
        #self.mainloop()
        
        if(not callback):
            self.callback=nop
        else:
            self.callback=callback

        self.delay = 100
        self.after(self.delay, self.play)

        while False:
            cb=callback(self)
            if(cb):
                state=cb.state
                if(state=='q'):
                    break
                self.font['size']=cb.fontSize
            root.update_idletasks()
            root.update()

    def play(self):
        cb=self.callback(self)
        if(cb):
            state=cb.state
            if(state=='q'):
                return
            self.font['size']=cb.fontSize
        self.after(self.delay, self.play)
            
#def callback(self):
#    self.text.set(getTime())

#sw=ScreenWriter(callback)
#sw=ScreenWriter()
