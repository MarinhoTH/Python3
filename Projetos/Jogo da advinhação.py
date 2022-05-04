#Lembrete: No modo dificil fazer um sistema que armazena a quantidade de tentativas e cria um ranking, salvando o usuario e a data.

from random import randint
from time import sleep
from os import system


def linha(msg='', numero=40):
    print(msg * numero)
def JogarNovamente(modo):
    while True:
            NovoJogo = str(input('Jogar Novamente? [S/N] ')).strip().upper()
            NovoJogo = NovoJogo[0]
            if NovoJogo == 'S':
                system('cls')
                modo() 
            elif NovoJogo == 'N':
                linha()
                print(f'Obrigado por jogar, {jogador}!')
                linha('-=-')
                break
            else:
                print('Opção Inválida')


jogador = str(input('Digite o seu nome: ')).strip()
sleep(0.5)
while True:
    linha('=', 120)
    EscolhaDeModo = str(input(f'''{'Jogo da advinhação':^100}

Olá {jogador}. Nesse jogo você tem que advinhar um número escolhido aleatoriamente pela máquina.

Modos de jogo:  


Fácil  ( 1 - 10 ): A cada tentativa, você recebe uma dica até acertar o número. 

Difícil ( 1 - 5 ): A cada tentativa errada, um novo número é escolhido e você não recebe nenhuma ajuda.


Você quer jogar o modo fácil ou o modo difícil? [F/D]: ''')).strip().upper()
    ModoEscolhido = EscolhaDeModo[0]
    


#Primeiro Método (Fácil). Usando aproximação.
    if ModoEscolhido == 'F':                
    
        def Fácil():
            numero = randint(1,10)
            contador = 0
            linha('-=-')
            
            linha()
            print('Vou pensar em um número inteiro entre 1 e 10. Tente advinhar...')
            linha()
            
            
            while True:
                try:
                    resposta = int(input('Em que numero eu pensei? '))
                except ValueError:
                    print('\nDigite um número válido!\n')
                    resposta = int(input('Em que numero eu pensei? '))
                
                print('Processando...' )
                sleep(2)
                linha()


                if resposta == numero and contador == 0:
                    print('Boa jogador. Acertou de primeira')
                    sleep(3)
                    break

                elif resposta > numero:
                    contador += 1
                    print('Errou jogador. Tenta um número menor...')
                    sleep(2)
                    linha()
                elif resposta < numero:
                    print('Errou jogador! Tenta um número maior...')
                    contador += 1
                    sleep(2)
                    linha()
                elif resposta == numero:
                    contador += 1
                    print(f'Boa jogador! Precisou de {contador} tentativas')
                    sleep(3)
                    break
                elif ValueError:
                    print('Digite um número válido')        
        
        
        Fácil()
        JogarNovamente(Fácil)
        break        

#Segundo Método (Difícil). Até acertar.
    elif ModoEscolhido== 'D':    
        
        def Difícil():
            numero = randint(1,5)
            contador = 0
            linha('-=-')
            linha()
            print('Vou pensar em um número entre 1 e 5. Tente advinhar...')
            sleep(2)
            linha()
            

            while True:

                
                resposta = int(input('Em que numero eu pensei? '))
                linha()
                print('Processando...' )
                sleep(2)
                linha()
                
                if resposta == numero and contador == 0:
                    print('Boa jogador. Acertou de primeira')
                
                elif resposta == numero: 
                    contador += 1
                    print(f'Parabéns! Depois de {contador} tentativa(s), você venceu!') 
                    break    
                
                else: 
                    print(f'Errou! Eu pensei no número {numero} e não no {resposta}')
                    contador +=1
                    sleep(2)
                    numero = randint(1,5)
   

        Difícil()
        JogarNovamente(Difícil)
        break

    else:
        print('Opção inválida')



#Ranking