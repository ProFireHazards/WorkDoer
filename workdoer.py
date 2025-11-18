import pyautogui
import pyperclip
import time
import random

# Wait time to click into the app
time.sleep(5)

# Get clipboard content
text = pyperclip.paste()

# Type it out like a flawed little human
for char in text:
    pyautogui.write(char)
    time.sleep(random.uniform(0.03, 0.13))  # Variable delay to simulate human typing
