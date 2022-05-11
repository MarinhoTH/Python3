import funções as f
import pyautogui
from time import sleep
from keyboard import is_pressed

f.menu('Mensagem Automática',tipo='=')

def IrNaConversa():
    pyautogui.moveTo(-1331, 14)
    pyautogui.click()

    sleep(0.5)


    pyautogui.moveTo(-1150, 228)
    pyautogui.click()

    pyautogui.moveTo(-757, 821)
    pyautogui.click()


def MandarMensagem(msg, vezes=10,infinito=False):

    if infinito==True:
    
        while True:
            pyautogui.write(msg)
            pyautogui.press('enter')
            if is_pressed('capslock') == True:
                break
    else:
        for c in range(0,vezes ):
            pyautogui.write(msg)
            pyautogui.press('enter')
            sleep(0.1)


while True:
    opção = int(input(''' 
[1] = Método 1 - Indo na 1 conversa fixada
[2] = Método 2 - Indo nos contatos escolhidos

[999] = Parar o programa

Sua opção: '''))
    
#Método 1 - Escolhendo quantas mensagens(60 msg em 25segundos) 

    if opção == 1:

        msg = str(input('Mensagem pra mandar: '))
        numero = int(input('Vezes: '))

        pyautogui.alert('Coloca na aba do WebAPP e fixa a conversa')
       

        IrNaConversa()

        pyautogui.write('Vc foi avisado.')
        pyautogui.press('enter')
        sleep(0.5)
        MandarMensagem(msg,numero)

        pyautogui.alert('Acabou, pode voltar!')


#Método 2 - Selenium    

    elif opção == 2:
        msg = str(input('Mensagem pra mandar: '))
        

#Método 3 (secreto) - infinito       
    elif opção ==3:
        sure=str(input('Opção 3 escolhida. Tem certeza? '))
        if sure == 'boom':
            msg = str(input('Mensagem pra mandar: '))
            
            IrNaConversa()
            MandarMensagem(msg , infinito=True)
            
    elif opção==999:
        break
    else:
        print('Opção Inválida')
 
