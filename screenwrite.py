from random import choice, randrange
from datetime import datetime
from ctypes import windll

def getTime():
    now = datetime.now()
    current_time = now.strftime('%H:%M:%S')
    return current_time

import pygame
import win32api
import win32con
import win32gui
pg=pygame
# Initialize Pygame
pygame.init()

# Set the size of the window
window_size = (800, 600)

# Set the transparency color
fuchsia = (255, 0, 128)  # This color will be transparent

# Create a window without a frame
screen = pygame.display.set_mode(window_size, pygame.NOFRAME)

# Get the window handle (HWND)
hwnd = pygame.display.get_wm_info()["window"]

# Set window styles to include layered and transparent
styles = win32gui.GetWindowLong(hwnd, win32con.GWL_EXSTYLE)
styles |= win32con.WS_EX_LAYERED | win32con.WS_EX_TRANSPARENT
win32gui.SetWindowLong(hwnd, win32con.GWL_EXSTYLE, styles)

# Set the window's transparency color
win32gui.SetLayeredWindowAttributes(hwnd, win32api.RGB(*fuchsia), 0, win32con.LWA_COLORKEY)

font = pg.font.Font(None, 45)
timer = 60
screen_rect = screen.get_rect()
color = (randrange(256), randrange(256), randrange(256))
txt = font.render(getTime(), True, color)

# Define constants for the SetWindowPos function
HWND_TOPMOST = -1
SWP_NOMOVE = 0x0002
SWP_NOSIZE = 0x0001

# Set the window to always be on top
#windll.user32.SetWindowPos(hwnd, HWND_TOPMOST, 0, 0, 0, 0, SWP_NOMOVE | SWP_NOSIZE)
windll.user32.SetWindowPos(pygame.display.get_wm_info()['window'], -1, 0, 0, 0, 0, 0x0001)
# Main loop
done = False
while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

    # Fill the screen with the transparency color
    screen.fill(fuchsia)

    timer -= 1
    # Update the text surface and color every 10 frames.
    if timer <= 0:
        timer = 120
        color = (randrange(256), randrange(256), randrange(256))
        txt = font.render(getTime(), True, color)

    #screen.fill((30, 30, 30))
    screen.blit(txt, txt.get_rect(center=screen_rect.center))

    # Update the display
    pygame.display.update()
