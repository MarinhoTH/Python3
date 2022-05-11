from time import sleep
import os


print(f'{" Bar do Juan ":#^80}')
    
while True:    
    conta = float(input('A conta deu quanto? R$' ))
    contacomjuros = conta + conta * (20 / 100)
    descontode5 = conta - (5 /100)
    descontode10 = conta - (10 / 100)

   
    print('''\n
    Formas de Pagamento

[ 1 ] à vista dinheiro
[ 2 ] à vista cartão
[ 3 ] 2x no Cartão 
[ 4 ] 3x ou mais no cartão
[ 5 ] Pix''')

    print('')
    escolha = int(input('Qual forma vc prefere? '))
    print('')
    if escolha == 1:
        print(f'Sua conta de R${conta:.2f} vai ter um desconto de 10%, e vai ficar por R${descontode10 :.2f}')

    elif escolha == 2:
        print(f'Sua conta de R${conta:.2f} vai ter um desconto de 5%, e vai ficar por R${descontode5 :.2f}')

    elif escolha == 3:
        print(f'Sua conta deu R${conta:.2f}')

    elif escolha == 4:
        parcelas = int(input('Quantas parcelas? '))
        valorparcelado = contacomjuros / parcelas
        print('')
        print(f'Sua conta será parcelada em {parcelas}x de {valorparcelado:.2f} COM JUROS')
        print(f'No final, sua conta de R${conta:.2f} vai ficar por R${contacomjuros:.2f}')

    elif escolha == 5:
        print(f'Sua conta deu R${conta:.2f}')
        print('')
        print('Pague por aqui: thiagomarinho561@gmail.com')

    else:
        print('A gente ainda não aceita cryptocoin chef, tente outra opção :)')
        
    print(f'{" Volte sempre ":#^80}\n') 
    sleep(8)
    os.system("cls")
