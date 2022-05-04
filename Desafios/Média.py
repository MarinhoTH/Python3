n1 = int(input('Digite um número: '))
contador = 1
resposta = str(input('Quer continuar? [S/N] ')).strip().capitalize()
n2 = 0
soma = n1 + n2

while resposta in 'Ss':
    n2 = int(input('Digite um número: '))
    resposta = str(input('Quer continuar? [S/N] ')).strip().capitalize()
    contador += 1
    n1 = n2
    soma = n1 + n2
    n2 = n1

    
soma += soma 
media = soma / contador


print(f'Você digitou {contador} números e a média foi {media:.1f}')

