from random import randint
from time import sleep
from os import system

while True:
    input('''
~Blackjack~

>>> Start ''')

    numeroPlayer = randint(2,20)
    numeroMaquina = randint(15,25)
    

    print(f'Your number is {numeroPlayer}')
   

    while True:
        escolha = str(input('''
You want to raise or stop? 
>>> '''))
        if escolha in 'RaiseRAISEraise':
            numeroPlayer += randint(1,10)
            print(f'Your number is {numeroPlayer}') 
        else:
            break
      
   
    if escolha in 'Sstop':
        pass

    print(f'\nThe number of your opponent is {numeroMaquina}\n')
    sleep(3)

    if numeroPlayer == 21 and numeroMaquina != 21:
        print('You Won !')
        
    if numeroMaquina == numeroPlayer:
        print('Draw')
    elif numeroPlayer < 21 and numeroPlayer>numeroMaquina:
        print('You Won !')
    elif numeroPlayer < 21 and numeroMaquina>21:
        print('You Won !')
    elif numeroPlayer > 21 and numeroPlayer<numeroMaquina:
        print('You Won !')    
    else:
        print('\nYou Lost.')
        sleep(1)
        print('\nLoser.')
        sleep(2)
        print('\nTake the L.')
        sleep(1)

    str(input('''
EndGame
>>> '''))
    system('cls')
    


