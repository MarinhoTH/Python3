#Funções

def linha(tamanho=80, tipo='-=-'):
    print(tipo * tamanho)


def leiaInt(msg):
    ok = False
    valor = 0
    while True:
        n = str(input(msg))
        if n.isnumeric():
            valor = int(n)
            ok = True
        else:
            print('\033[0;31mErro! Digite um número inteiro válido. \033[m')

        if ok:
            break
    return valor


def jogarNovamente(modo):
    while True:
            NovoJogo = str(input('Jogar Novamente? [S/N] ')).strip().upper()
            NovoJogo = NovoJogo[0]
            if NovoJogo == 'S':
                modo() 
            elif NovoJogo == 'N':
                print(f'Obrigado por jogar!')
                break
            else:
                print('Opção Inválida')


def menu(msg,tipo='-=-'):
    print(tipo * 40)
    print(f'{msg:^40}')
    print(tipo * 40)

