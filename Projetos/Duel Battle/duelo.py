from duelfuncs import *


input(''' 
Atenção!

Para uma melhor visualização, MAXIMIZE a janela do seu terminal!
>>Pressione ENTER para continuar  ''')


menu()

opção= int(input('>> Digite uma opção: '))


if opção == 0:
    print('Finished')


elif opção == 1:
    newgame()
    playagain()


elif opção == 2:
    rules()
    input('>> Pressione ENTER para voltar')


elif opção == 3:
    ranking()
    input('>> Pressione ENTER para voltar')   


else:
    print('Selecione uma opção válida')
    
