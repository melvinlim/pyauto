import win32api
import win32con
from pywinauto.win32_hooks import Hook
from pywinauto.win32_hooks import KeyboardEvent
from pywinauto.win32_hooks import MouseEvent

class hook(object):
    def __init__(self,callback=None):
        self.main_thread_id = win32api.GetCurrentThreadId()
        def on_event(args):
            """Callback for keyboard and mouse events"""
            if isinstance(args, KeyboardEvent):
                if(callback):
                    callback(args.current_key)
                if args.current_key == 'A' and args.event_type == 'key down' and 'Lcontrol' in args.pressed_key:
                    print("Ctrl + A was pressed");
                    
                if args.current_key == 'L' and args.event_type == 'key down' and 'Lcontrol' in args.pressed_key:
                    print("Ctrl + L was pressed");
                    print('quitting')
                    print('press CTRL-D to close Idle window.')
                    win32api.PostThreadMessage(self.main_thread_id, win32con.WM_QUIT, 0, 0);

                if args.current_key == 'K' and args.event_type == 'key down':
                    print("K was pressed");

                if args.current_key == 'M' and args.event_type == 'key down' and 'Lcontrol' in args.pressed_key:
                    print("Ctrl + M was pressed");
                    hk.unhook_mouse()
                    print("Unhook mouse")

                if args.current_key == 'K' and args.event_type == 'key down' and 'Lcontrol' in args.pressed_key:
                    print("Ctrl + K was pressed");
                    hk.unhook_keyboard()
                    print("Unhook keyboard")

            if isinstance(args, MouseEvent):
                if args.current_key == 'RButton' and args.event_type == 'key down':
                    #import pdb
                    #pdb.set_trace()
                    xcoord=args.mouse_x
                    ycoord=args.mouse_y
                    print ("Right button pressed @ "+str(xcoord)+" "+str(ycoord))

                if args.current_key == 'WheelButton' and args.event_type == 'key down':
                    print("Wheel button pressed")
        hk = Hook()
        hk.handler = on_event
        hk.hook(keyboard=True, mouse=True)

def callback(key):
    print('key '+key+' was pressed.')

h = hook(callback)
