from pyautogui import * 
import pyautogui 
import time 
import keyboard
import cv2
import random
import win32api, win32con
import pyperclip



pyautogui.size()
#txt file opening part
pyautogui.doubleClick(1842,50,duration=10)
pyautogui.click(675,489,duration=4)
pyautogui.hotkey('ctrl', 'a',duration=4)
pyautogui.hotkey('ctrl', 'c',duration=4)


#sharex opening part
pyautogui.doubleClick(1853,929,duration=4)
pyautogui.click(x=1353, y=152,duration=4)
pyautogui.hotkey('shift','prtscr',duration=4)
pyautogui.moveTo(0,0,duration=4)
pyautogui.FAILSAFE = False
pyautogui.dragTo(1928,1084, 8)
pyautogui.moveTo(0,0,duration=4)

#chrome opening part
pyautogui.doubleClick(1848,347,duration=4)
pyautogui.hotkey('alt', 'space','x')
pyautogui.click(473,75,duration=4)
pyautogui.hotkey('ctrl', 'v')
pyautogui.hotkey('enter')
pyautogui.click(668,863,duration=4)
pyautogui.click(1421,663,duration=4)
pyautogui.hotkey('f11')

#minimising and opening comment section
time.sleep(3)
pyautogui.click(x=1756, y=830)
pyautogui.click(x=1787, y=1014,duration=3)


#attendance part
X=0
while X==0:
    if pyautogui.locateOnScreen('m.png', region=(1358,225,539,644), grayscale=True, confidence=0.6) != None:
        pyautogui.click(x=1513, y=907,duration=2)
        time.sleep(2)
        pyperclip.copy("2K18/EP/014 Anubhav Rai")
        pyautogui.hotkey("ctrl", "v")   
        X=1 
    
    elif pyautogui.locateOnScreen('n.png', region=(1358,225,539,644), grayscale=True, confidence=0.6) != None:

        pyautogui.click(x=1513, y=907,duration=2)
        time.sleep(2)
        pyperclip.copy("2K18/EP/014 Anubhav Rai")
        pyautogui.hotkey("ctrl", "v")
        X=1
    elif pyautogui.locateOnScreen('o.png', region=(1358,225,539,644), grayscale=True, confidence=0.6) != None:

        pyautogui.click(x=1513, y=907,duration=2)
        time.sleep(2)
        pyperclip.copy("2K18/EP/014 Anubhav Rai")
        pyautogui.hotkey("ctrl", "v")
        X=1
    elif pyautogui.locateOnScreen('p.png', region=(1358,225,539,644), grayscale=True, confidence=0.6) != None:

        pyautogui.click(x=1513, y=907,duration=2)
        time.sleep(2)
        pyperclip.copy("2K18/EP/014 Anubhav Rai")
        pyautogui.hotkey("ctrl", "v")
        X=1
    else:
        print("not seeing")
        X=0

pyautogui.hotkey('','enter')

#closing class
time.sleep(3)
pyautogui.click(x=1150, y=1015,duration=2)

#stopping the screen recorder
pyautogui.hotkey('shift','prtscr',duration=4)



