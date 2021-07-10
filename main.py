import pyautogui
import time
import random
input('Please open Mullvad undocked at the bottom right corner. If you need to stop the program, slam your mouse to any of the four corners. Press enter to continue.')
time.sleep(5)

def login():
    current_account = str(random.randint(1000000000000000, 9999999999999999))
    pyautogui.click(1643, 800)
    pyautogui.write(current_account)
    pyautogui.click(1875, 800)
    time.sleep(1)
while True:
    login()