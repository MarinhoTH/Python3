def menu():
    print('-' *50 )
    print(f'|{"Main Menu":^48}|')
    print('-' *50 )
    print(f'|{"     1. New Game":<48}|')
    print(f'|{"     2. Game Rules":<48}|')
    print(f'|{"     3. Ranking":<48}|')
    print(f'|{"     0. Quit":<48}|')
    
    
    
    print('-' *50 )

def newgame():
    jogador= str(input('Player: '))

    print(f'Greetings, {jogador}. Pick beetween one of the classes bellow to define your fight status')
    classpicked = int(input(''' 
    [1] Fighter
    [2] Mage
    [3] Gunslinger
    [4] Beast
    >> '''))

    if classpicked == 0:
        print('')

    elif classpicked == 1:
        print('')


    elif classpicked== 2:
        print('')


    elif classpicked == 3:
        print('')
    elif classpicked == 3:
        print('')
    elif classpicked == 3:
        print('shh')

def rules():
    print('''
*Instructions*

You will fight a boss selected randomly.

You can choose your character class and each type of class have different attributes and can be better to fight some bosses.

Every round you will select a action to fight the boss.

Whoever gets to 0 health, lose''')

def ranking():
    print('''
RANK

1º: TH''')


def playagain():
    while True:
        pick= str(input('>> Do you want to play another game? [y/n] ')).strip() .lower()
        answer = pick[0]
        if answer == 'y':
            menu()
        elif answer== 'n':
            print('Game Completed!')
            break
        else:
            print("Choose a valid option")



