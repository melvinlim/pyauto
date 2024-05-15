import win32com.client
import win32gui
import pyautogui

from pynput import keyboard
from grabscreen import grabScreen
from ocr import readWin

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
    x=shell.AppActivate(window)
    #x=shell.AppActivate('Notepad')
    if(not x):
        print('failed to activate window: '+window)
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
import re
money=0

def checkMoney():
    start=x.find('$')
    match=re.search(r'[0-9]+',x[start:])
    if(match):
        sp=match.span()
        result=x[start+sp[0]:start+sp[1]]
        try:
            money=int(result)
            return money
        except e:
            print(e)
    return -1
    #print(result)

def skipStory():
    activate('VirtuaNES')
    time.sleep(1)
    sendKeys('j')

def upArrow():
    activate('VirtuaNES')
    time.sleep(1)
    sendKeys('up')

while running:
    waitForDiff()
    x=readWin('VirtuaNES - Vegas Dream (USA)')
    if(x.find('BET')):
        upArrow()
    print(x)
    tmp=checkMoney()
    if(tmp>=0):
        money=tmp
    else:
        skipStory()
        time.sleep(1)
        upArrow()
    print(money)
    make3Bet()

#class scene(object):
#    __init__(self):
#        self.state=0
listener.join()
