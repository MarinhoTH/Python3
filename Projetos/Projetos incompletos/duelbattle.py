from random import choice
from os import system


def rules():
    print('''
*Instructions*

Each class has different attributes.
You will choose a class and fight a boss.

You have to pick an stat higher than the boss's to win and you lose if you stat is lower. If its a draw you lose aswell''')


def stats():
    print('''
*STATS*

Fighter                           Mage

power = 10                        power = 5

vitality = 150                    vitality = 150

stamina = 5                       stamina = 10


Gunslinger                      Beast
        
power = 6                       power = 8
vitality = 120                  vitality = 200
stamina = 7                     stamina = 6

Thunder King

power = 10
vitality = 200
stamina = 10



*Boss*


Caranthir

power = 10
vitality = 200
stamina = 10

Eredin

power = 10
vitality = 200
stamina = 10



Geralt

power = 10
vitality = 200
stamina = 10

Vesemir

power = 10
vitality = 200
stamina = 10
''')


def playagain():
    while True:
        pick= str(input('>> Do you want to play again? [y/n] ')).strip() .lower()
        answer = pick[0]
        if answer == 'y':
            menu()
            break
        elif answer == 'n':
            print('Game Completed!')
            break
        else:
            print("Choose a valid option")



def menu():
    while True:
        print('-' *50 )
        print(f'|{"Main Menu":^48}|')
        print('-' *50 )
        print(f'|{"     1. New Game":<48}|')
        print(f'|{"     2. Game Rules":<48}|')
        print(f'|{"     3. Class stats":<48}|')
        print(f'|{"     0. Quit":<48}|')
        print('-' *50 )
        
        opção= int(input('>> Digite uma opção: '))

        if opção == 0:
            print('Finished')
            break


        elif opção == 1:
            newgame()
            playagain()
            break


        elif opção == 2:
            rules()
            input('>> Pressione ENTER para voltar')
            system('cls')


        elif opção == 3:
            stats()
            input('>> Pressione ENTER para voltar')  
            system('cls') 


        else:
            print('Selecione uma opção válida')


def newgame():
    jogador= str(input('\n>> Player: '))

    print(f'\nGreetings, {jogador}. Pick beetween one of the classes bellow to define your fight stats')
    classpicked = int(input(''' 
[1] Fighter
[2] Mage
[3] Gunslinger
[4] Beast
    
>> '''))

    if classpicked == 1:
       battle('fighter')
    elif classpicked == 2:
       battle('mage')
    elif classpicked == 3:
       battle('gunslinger')
    elif classpicked == 4:
       battle('beast')
    elif classpicked == 0:
       print('You chose the hidden class Thunder King')
       battle('thunder')
    else:
        print('''
Invalid Option!

Game not started        
''')


def battle(type):
   
    if type == 'fighter':
        power = 10
        vitality = 150
        stamina = 5
    elif type == 'mage':
        power = 5
        vitality = 100
        stamina = 10
    elif type == 'gunslinger':
        power = 6
        vitality = 120
        stamina = 7
    elif type == 'beast':
        power = 8
        vitality = 200
        stamina = 6
    elif type == 'thunder':
        power = 10
        vitality = 200
        stamina = 10

    BossList = ['Caranthir', 'Eredin','Geralt','Vesemir']
    Boss = choice(BossList)
    if Boss =='Caranthir':
        bosspower= 6
        bossvitality = 5
        bossstamina = 8
    elif Boss=='Eredin':
        bosspower= 8
        bossvitality = 9
        bossstamina = 9
    elif Boss=='Geralt':
        bosspower= 6
        bossvitality = 5
        bossstamina = 10
    elif Boss=='Vesemir':
        bosspower= 6
        bossvitality = 4
        bossstamina = 3
    
    print(f'\nYou will face {Boss} in your battle.')


    statpicked=int(input(''' 
[1] - Power
[2] - Vitality
[3] - Stamina

>>Choose your best stat: '''))
    
    if statpicked == 1 :
        print(f'''
Your Power: {power}

Boss Power: {bosspower}        
''')
        print('You WON!') if power>bosspower else print('You LOST!')
    elif statpicked == 2 :
        print(f'''
Your Vitality: {power}

Boss Vitality: {bosspower}        
''')
        print('You WON!') if vitality>bossvitality else print('You LOST!')
    elif statpicked == 3 :
        print(f'''
Your Vitality: {vitality}

Boss Vitality: {bossvitality}
''')
        print('You WON!') if stamina>bossstamina else print('You LOST!')
    else:
        print('Invalid option')



system('cls')      

input(''' 
Warning!

For a otimized experience, maximize your terminal window

>>Press ENTER to continue  ''')

menu()
