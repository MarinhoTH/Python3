import pyautogui
from time import sleep


pyautogui.alert('Calmo, o código vai começar.')
pyautogui.pause = 2


#Fazendo o checkin diario
pyautogui.press('winleft')
sleep(0.5)
pyautogui.write('op.gg', interval=0.1)
sleep(5)
pyautogui.press('enter')
sleep(5)
pyautogui.press('winleft')
sleep(0.5)
pyautogui.write('League of Legends')
sleep(0.5)
pyautogui.press('enter')
sleep(5)

pyautogui.press('winleft')
sleep(0.5)
pyautogui.write('discord', interval=0.1)
sleep(1)
pyautogui.press('enter')
pyautogui.alert('acabo') 

