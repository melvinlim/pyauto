from random import choice, randrange
from datetime import datetime
from ctypes import windll

import tkinter as Tkinter
import tkinter.font as tkFont
import win32api
import win32con
import win32gui
import pywintypes

from PIL import Image, ImageTk

def nop(self):
    pass

#modified from https://www.blog.pythonlibrary.org/2023/12/05/viewing-an-animated-gif-with-python/
class MyLabel(Tkinter.Label):
    def __init__(self, master, filename):
        im = Image.open(filename)
        seq =  []
        try:
            while 1:
                seq.append(im.copy())
                im.seek(len(seq)) # skip to next frame
        except EOFError:
            pass # we're done
        try:
            self.delay = im.info['duration']
        except KeyError:
            self.delay = 100
        print(self.delay)
        first = seq[0].convert('RGBA')
        self.frames = [ImageTk.PhotoImage(first)]
        Tkinter.Label.__init__(self, master, image=self.frames[0])
        for image in seq[1:]:
            frame=image.convert('RGBA')
            self.frames.append(ImageTk.PhotoImage(frame))
        self.idx = 0
        self.cancel = self.after(self.delay, self.play)
    def play(self):
        self.config(image=self.frames[self.idx])
        self.idx += 1
        if self.idx == len(self.frames):
            self.idx = 0
            return
        print(self.idx)
        self.cancel = self.after(self.delay, self.play)

class ScreenWriter(object):
    def __init__(self,callback=None):
        root=Tkinter.Tk()
        #gif_path="C:\\Users\\winuser\\Downloads\\R.gif"
        gif_path="R.gif"

        #modified from https://stackoverflow.com/questions/21840133/how-to-display-text-on-the-screen-without-a-window-using-python
        label = MyLabel(root,
                        gif_path
            )
        label.anchor='w'
        label.justify='left'
        label.fg='gray'
        label.bg='white'
        label.master.overrideredirect(True)
        #label.master.geometry("+250+250")
        #label.master.geometry("+0+0")
        label.master.geometry("+0+100")     #x and y locations
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
            #label.play()
            cb=callback(self)
            if(cb):
                state=cb.state
                if(state=='q'):
                    break
                self.font['size']=cb.fontSize
            root.update_idletasks()
            root.update()

def callback(self):
    pass

sw=ScreenWriter(callback)
