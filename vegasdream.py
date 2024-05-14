import win32com.client
import win32gui
import pyautogui

from pynput import keyboard
from grabscreen import grabScreen

import numpy as np

def listWindows():
    def winEnumHandler( hwnd, ctx ):
        if win32gui.IsWindowVisible( hwnd ):
            print ( hex( hwnd ), win32gui.GetWindowText( hwnd ) )
    win32gui.EnumWindows( winEnumHandler, None )

listWindows()
#exit()

shell = win32com.client.Dispatch("WScript.Shell")

running=True

def on_press(key):
    try:
        key_press=key.char
    except:
        key_press=key.name
    #print(key_press)
    if(key_press=='q'):
        exit()
#        running=False
#        print('quitting.')


listener = keyboard.Listener(on_press=on_press)
listener.start()

def activate(window):
    print('activating: '+window)
    x=shell.AppActivate('VirtuaNES')
    #x=shell.AppActivate('Notepad')
    print(x)
    active_window = win32gui.GetWindowText(win32gui.GetForegroundWindow())
    print(active_window)

#def sendKeys(keys):
#    print('sending: '+keys)
#    x=shell.SendKeys(keys,True)

def sendKeys(keys):
    print('sending: '+keys)
    activate('VirtuaNES')
    pyautogui.keyDown(keys)
    time.sleep(0.2)
    pyautogui.keyUp(keys)
    
def make3Bet():
    activate('VirtuaNES')
    time.sleep(1)
    sendKeys('k')
    activate('VirtuaNES')
    time.sleep(1)
    sendKeys('k')
    activate('VirtuaNES')
    time.sleep(1)
    sendKeys('k')
    activate('VirtuaNES')
    time.sleep(1)
    sendKeys('j')

def waitForDiff():
    diff=100
    while(diff>10):
        s0=grabScreen('VirtuaNES')
        time.sleep(0.5)
        s1=grabScreen('VirtuaNES')
        diff=np.sum(np.abs(np.array(s1)-np.array(s0)))
        print(diff)

import time
while running:
    waitForDiff()
    make3Bet()

#class scene(object):
#    __init__(self):
#        self.state=0
listener.join()
