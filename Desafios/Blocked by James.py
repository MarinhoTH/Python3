lista = []


while True:
    num = int(input('Digite um valor: '))
    if num not in lista:
        lista.append(num)
    else:
        print('Blocked By James')
    resposta = str(input('Quer continuar? [S/N]'))
    if resposta in 'Nn':
        break


lista.sort()
print(*lista)


