import pyautogui
import requests
import time

time.sleep(2)
x = 0
y = 0


while(x <= 30):
    x= x + 1
    time.sleep(2)
    response = requests.get('https://api.api-ninjas.com/v1/randomword', headers={'X-Api-Key':'7AGWVzVCrnWVPFK7cZEAxQ==yD9utGtt0zTHIlmE'})
    data = response.json()
    pyautogui.hotkey('ctrl', 'e')
    pyautogui.typewrite(data['word'])
    pyautogui.press('enter')
    print(f"{y}: {data['word']}")


pyautogui.hotkey('ctrl', 'shift','i')

while(y <= 20):
    y += 1
    time.sleep(2)
    response = requests.get('https://api.api-ninjas.com/v1/randomword', headers={'X-Api-Key':'7AGWVzVCrnWVPFK7cZEAxQ==yD9utGtt0zTHIlmE'})
    data = response.json()
    pyautogui.hotkey('ctrl', 'e')
    pyautogui.typewrite(data['word'])
    pyautogui.press('enter')
    print(f"{y}: {data['word']}")


