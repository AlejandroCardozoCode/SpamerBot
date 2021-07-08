#este bot spamea mensajes por medio de la pantalla, se necesita tener instalsdo los modulos de pyautogui
import pyautogui,time, keyboard
time.sleep(10)

while True:
    pyautogui.typewrite("para que aprenda loka")
    pyautogui.press("enter")
    if keyboard.is_pressed("alt"):
        print ("tecla a presionada")
        break
"""
while True:
    pyautogui.hotkey('ctrl','v')
    time.sleep(0.5)
    pyautogui.press("enter")
    if keyboard.is_pressed("alt"):
        print ("tecla a presionada")
        break
 """