from random import choice
BossList = ['Calanthir', 'Eredin','Geralt','Vesemir']


def rules():
    print('''
*Instructions*

Super trunfo''')


def stats():
    print('')


def playagain():
    while True:
        pick= str(input('>> Do you want to play another game? [y/n] ')).strip() .lower()
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


        elif opção == 3:
            stats()
            input('>> Pressione ENTER para voltar')   


        else:
            print('Selecione uma opção válida')


def newgame():
    jogador= str(input('Player: '))

    print(f'Greetings, {jogador}. Pick beetween one of the classes bellow to define your fight stats')
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
       battle('thunder')


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


    Boss = choice(BossList)
    bosspower= 2
    print(f'\nYou will face {Boss} in your battle.')


    statpicked=int(input(''' 
[1] - Power
[2] - Vitality
[3] - Stamina
>>Choose your best stat: '''))
    
    if statpicked == 1 :
        print('victory') if power>bosspower else print('defeat')
        
   
    else:
        print('Invalid option')



       






