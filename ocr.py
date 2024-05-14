import screen_ocr
import win32gui

ocr_reader = screen_ocr.Reader.create_quality_reader()

#results = ocr_reader.read_screen()
#print(results.as_string())

#windowTitle='Spotify Free'

from win32gui import FindWindow, GetWindowRect, GetClientRect, ClientToScreen

def callback(hwnd, extra):
    windowTitle=win32gui.GetWindowText(hwnd)
    if(windowTitle!='' and windowTitle not in ['Default IME','MSCTFIME UI']):
        rect = win32gui.GetWindowRect(hwnd)
        x = rect[0]
        y = rect[1]
        w = rect[2] - x
        h = rect[3] - y
        print("WindowTitle: %s" % windowTitle)
        print("\tLocation: (%d, %d)" % (x, y))
        print("\t    Size: (%d, %d)" % (w, h))

win32gui.EnumWindows(callback, None)

def getRect(windowTitle):
    window_handle = FindWindow(None, windowTitle)
    if(window_handle):
        coords=(0,0)
        coords=ClientToScreen(window_handle,coords)
        print(coords)
        #window_rect   = GetWindowRect(window_handle)   #includes title and menu
        window_rect   = GetClientRect(window_handle)    #excludes title and menu
        print(window_rect)
        (x,y)=coords
        result=()
        result+=coords
        result+=(window_rect[2]+x,window_rect[3]+y)
        print(result)
        return result
    return None

def readWin(windowTitle):
    rect=getRect(windowTitle)
    #print(rect)

    results = ocr_reader.read_screen(rect)
    return results.as_string()

x=readWin('VirtuaNES - Vegas Dream (USA)')
print(x)
