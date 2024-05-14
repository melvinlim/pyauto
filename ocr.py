import screen_ocr
import win32gui

ocr_reader = screen_ocr.Reader.create_quality_reader()

#results = ocr_reader.read_screen()
#print(results.as_string())

windowTitle='Spotify Free'

from win32gui import FindWindow, GetWindowRect

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
        window_rect   = GetWindowRect(window_handle)
        return window_rect
    return None

#print(window_rect)

rect=getRect(windowTitle)

results = ocr_reader.read_screen(rect)
print(results.as_string())
