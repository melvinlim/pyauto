#works only from windows.  won't work from wsl2/linux vm.
import time
import pyautogui
delay = 0.1
delay = 0.02
delay = 0.01
delay = 0.002
delay = 0.001
duration = 10
duration = 6000
t0 = time.time()
while(True):
  pyautogui.mouseDown()
  time.sleep(delay)
  pyautogui.mouseUp()
  time.sleep(delay)
  td = time.time() - t0
  if(td > duration):
   break
print('done')
exit()
