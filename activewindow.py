#https://stackoverflow.com/questions/10266281/obtain-active-window-using-python
from win32gui import GetWindowText, GetForegroundWindow

def activeWin():
    return GetWindowText(GetForegroundWindow())
