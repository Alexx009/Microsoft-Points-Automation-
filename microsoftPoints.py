import pyautogui
import requests
import time

time.sleep(2)
x = 0
y = 0


while(x <= 30):
    x= x + 1
    time.sleep(2)
    response = requests.get('https://random-word-api.herokuapp.com/word')
    data = response.json()
    pyautogui.hotkey('ctrl', 'e')
    pyautogui.typewrite(data[0])
    pyautogui.press('enter')
    print(x)


pyautogui.hotkey('ctrl', 'shift','i')

while(y <= 20):
    y= y + 1
    time.sleep(2)
    response = requests.get('https://random-word-api.herokuapp.com/word')
    data = response.json()
    
    pyautogui.hotkey('ctrl', 'e')
    pyautogui.typewrite(data[0])
    pyautogui.press('enter')
    print(y)