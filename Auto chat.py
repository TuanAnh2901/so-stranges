import pyautogui as gui
import time
import random
import string

print("Nhớ chỉnh qua Vietnam unikey khi nhập số")
number = int(input("Enter the number: "))
time.sleep(5)
test2 = ["I", "Don't", "Know"]
e = "I Love You"
n = 1
test = "Cust"

for i in range(number):
        s = string.ascii_lowercase
        gui.typewrite(random.choice(test2))
        ##gui.typewrite(str(n) + ". " + e)
        gui.press("Enter")
        ##n = n + 1
