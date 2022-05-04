from random import shuffle, choice

lista = list()

while True:
    lista.append(str(input('Nome da pessoa: ')))
    print('')
    r = str(input('Quer continuar? ')).strip()
    if r in 'Nn':
        break


print(f'A pessoa escolhida foi {choice(lista)}')
print('-=-' * 40)

shuffle(lista)
print(f"A Ordem escolhida é {lista}")