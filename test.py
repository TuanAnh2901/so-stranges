import time
import pyautogui as g

# List of messages to be sent
m1 = [
    "Hello = dmm",
    "You are cute as fuck,dawg"
]
num = int(input("Enter times:"))
time.sleep(5)

# Loop through the messages and send them
for i in range(num):
    for m in m1:
        g.write(m)
        g.press("enter")
    