import pyautogui as gui
import time
import random
import string

print("Nhớ chỉnh qua Vietnam unikey khi nhập số")
number = int(input("Enter the number: "))
time.sleep(5)
e = "I Love You"
n = 1

for i in range(number):
        s = string.ascii_lowercase
        gui.typewrite(str(n) + ". " + e)
        gui.press("Enter")
        n = n + 1
