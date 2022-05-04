import pyautogui
from time import sleep


pyautogui.alert('Calmo, o código vai começar. Tira as mãos do teclado e mouse!')
pyautogui.pause = 2


#Fazendo o checkin diario
pyautogui.press('winleft')
sleep(0.5)
pyautogui.write('opera', interval=0.1)
sleep(5)
pyautogui.press('enter')
sleep(10)
pyautogui.write('mihoyo')
pyautogui.press('down')
sleep(0.5)
pyautogui.press('enter')


'''#Evento Especial 
pyautogui.hotkey('ctrl', 't')
sleep(0.5)
pyautogui.write('hoyoverse', interval=0.1)
sleep(0.5)
pyautogui.press('down')
sleep(0.5)
pyautogui.press('enter')
sleep(5)
pyautogui.moveTo(-714, 654)
sleep(1)
pyautogui.click()
sleep(1)'''

#Abrindo o txt
pyautogui.press('winleft')
sleep(0.5)
pyautogui.write('teyvat.txt', interval=0.3)
sleep(1)
pyautogui.press('enter')
sleep(0.5) 

#Abrindo o Genshin
pyautogui.press('winleft')
sleep(1)
pyautogui.write('Genshin Impact')
sleep(0.5)
pyautogui.press('enter')





