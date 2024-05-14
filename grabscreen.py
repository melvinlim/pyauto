import pyscreenshot as ImageGrab
import pygetwindow as gw

from PIL import Image
import io

import numpy as np

def grabScreen(windowTitle):

    # Resize smoothly down to 16x16 pixels
    newSize=(16,16)
    newSize=(32,32)
    newSize=(64,64)
    
    # Get the window with the title "Your Window Title"
    window = gw.getWindowsWithTitle(windowTitle)[0]

    # Get the window coordinates
    x1, y1, x2, y2 = window.left, window.top, window.left + window.width, window.top + window.height

    # Capture the specified window
    img = ImageGrab.grab(bbox=(x1, y1, x2, y2))
    #img.show()

    img_data = img.tobytes()
    recons_img = Image.frombytes(img.mode, img.size, img_data)

    imgSmall = img.resize(newSize, resample=Image.Resampling.BILINEAR)

    # Scale back up using NEAREST to original size
    #result = imgSmall.resize(img.size, Image.Resampling.NEAREST)
    result=imgSmall
    
    #result.show()
    return result

if __name__ == "__main__":
    #grabScreen('Montaro')
    result=grabScreen('VirtuaNES')
    result.show()
