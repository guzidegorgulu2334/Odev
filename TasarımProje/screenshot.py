import pyautogui
import os
def screenshot():
    screenshoot = pyautogui.screenshot()
    file_name = "screenshot.jpg"
    file_path = os.path.join('C:\Users\Güzide\OneDrive\Masaüstü\Odev\screenshots', file_name)
    screenshoot.save(file_path)