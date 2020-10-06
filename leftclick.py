import time
import pyautogui
import keyboard

pause = False

while True:
    while pause == False:
        if keyboard.is_pressed("p"):
            pause = True
            print("Paused")
            time.sleep(1)

        pyautogui.click()

        if keyboard.is_pressed("p"):
            pause = True
            print("Paused")
            time.sleep(1)
        time.sleep(0.25)

        if keyboard.is_pressed("p"):
            pause = True
            print("Paused")
            time.sleep(1)
        time.sleep(0.25)

        if keyboard.is_pressed("p"):
            pause = True
            print("Paused")
            time.sleep(1)
        time.sleep(0.25)

        if keyboard.is_pressed("p"):
            pause = True
            print("Paused")
            time.sleep(1)
        time.sleep(0.25)

    while pause == True:
        if keyboard.is_pressed("p"):
            pause = False
            print("Resuming")
            time.sleep(1)