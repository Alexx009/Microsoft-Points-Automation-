
import pyautogui
import requests
import time

time.sleep(5)
x = 0
y = 0



while x <= 30:
    x += 1
    time.sleep(10)
    response = requests.get('https://api.api-ninjas.com/v1/randomword', headers={'X-Api-Key': '7AGWVzVCrnWVPFK7cZEAxQ==yD9utGtt0zTHIlmE'})
    data = response.json()
    pyautogui.hotkey('ctrl', 'e')
    
    # Introduce delays between key presses to slow down the typing speed
    for char in data['word']:
        pyautogui.typewrite(char)
        time.sleep(10                              )
        
          # Adjust the sleep duration as needed

    pyautogui.press('enter')
    print(f"{y}: {data['word']}")

    
