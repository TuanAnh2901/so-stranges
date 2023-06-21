import pyautogui as gui
import time
import random
import string

print("Nhớ chỉnh qua Vietnam unikey")
number = int(input("Enter the number: "))
time.sleep(5)

for i in range(number):
    s = string.ascii_letters
    m = "".join(random.sample(s, 3))
    gui.typewrite(m)
    gui.press("Enter")
