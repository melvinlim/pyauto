import time
import pyautogui
import random
delay = 0.1
delay = 0.02
delay = 0.01
delay = 0.002
delay = 0.001
duration = 10
duration = 6000
t0 = time.time()

time.sleep(5)
while(True):
  pyautogui.mouseDown()
  time.sleep(delay)
  pyautogui.mouseUp()
  duration=random.randint(1000,3000)/1000
  time.sleep(duration)
print('done')
exit()
