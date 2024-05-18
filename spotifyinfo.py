import win32gui
import win32process
import win32api
import win32con

def enum_windows_proc(hwnd, lParam):
    title=win32gui.GetWindowText(hwnd)
    thread_id, pid = win32process.GetWindowThreadProcessId(hwnd)
    if(title not in ['','MSCTFIME UI','Default IME']):

        try:
            pid = win32process.GetWindowThreadProcessId(hwnd)
            handle = win32api.OpenProcess(win32con.PROCESS_QUERY_INFORMATION | win32con.PROCESS_VM_READ, False, pid[1])
            proc_name = win32process.GetModuleFileNameEx(handle, 0)
            if(proc_name.find('Spotify.exe')>=0):
                #print(proc_name)
                if(title.find('GDI+ Window (Spotify.exe)')<0):
                    #print(title)
                    lParam[0]=title
        except:
            pass

def spotifySong():
    param=[0]
    win32gui.EnumWindows(enum_windows_proc, param)
    result=param[0]
    return result

#r=spotifySong()
#print(r)
