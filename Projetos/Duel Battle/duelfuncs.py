def menu():
    print('-' *50 )
    print(f'|{"Main Menu":^48}|')
    print('-' *50 )
    print(f'|{"     1. New Game":<48}|')
    print(f'|{"     2. Game Rules":<48}|')
    print(f'|{"     3. Classes":<48}|')
    print(f'|{"     0. Quit":<48}|')
    print('-' *50 )


def rules():
    print('''
*Instructions*

You will fight a boss selected randomly.

You can choose your character class and each type of class have different attributes and can be better to fight some bosses.

Every round you will select a action to fight the boss.

Whoever gets to 0 health, lose''')


def stats():
    print('''
*Stats*

Attack: Damage per hit
Health: Life
Stamina: Hits per Round


Fighter:

health: 150
attack: 10
stamina: 1

Mage:

health: 100
attack: 5
stamina: 3

Gunslinger:

health: 100
attack: 6
stamina: 2

Beast:

health: 200
attack: 5
stamina: 1


Thunder King(secret):

health: 200
attack: 10
stamina:3


''')


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


def classtats(type):
    if type=='fighter':
        print('''
You selected Fighter!

health: 150
attack: 10
stamina: 1
''')
    
    if type=='mage':
        print('''
You selected Mage!

health: 100
attack: 5
stamina: 3
''')
    
    if type=='gunslinger':
        print('''
You selected Gunslinger!

health: 100
attack: 6
stamina: 2
''')
    if type=='beast':
        print('''
You selected Beast!

health: 200
attack: 5
stamina: 1
''')
    if type=='thunder':
        print('''
You selected the secret class!

Thunder King

health: 200
attack: 10
stamina: 3
''')

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
        classtats('thunder')






