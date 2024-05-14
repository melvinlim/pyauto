import time
import random
delay = 0.1
delay = 0.02
delay = 0.001
duration = 10
duration = 6000

from pywinauto import findwindows
import pywinauto

handle = findwindows.find_window(best_match='Montaro')
print(handle)
#app = pywinauto.Application().connect(path='your_process_name.exe')
app = pywinauto.Application().connect(handle=handle)

x=250
y=250

while(True):
  #app.MainDialog.click_input(coords=(x, y))
  app.Montaro.click_input(coords=(x, y))
  duration=random.randint(1000,3000)/1000
  time.sleep(duration)

print('done')
exit()
