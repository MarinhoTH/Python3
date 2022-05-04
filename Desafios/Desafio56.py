somaidade = 0
médiaidade = 0

maioridadehomem = 0
nomevelho = ''

menormulher = 0

for p in range(1,5):
    print(f'-----{p}ª Pessoa -----')
    nome = str(input('Nome: ')).strip()
    idade = int(input('Idade: '))
    sexo = str(input('Sexo [M/F]: ')) .strip()
    print('')
    somaidade += idade
    if p == 1 and sexo in 'Mm':
        maioridadehomem = idade
        nomevelho = nome
    if sexo in 'Mm' and idade > maioridadehomem:    
        maioridadehomem = idade
        nomevelho = nome
    if sexo in 'Ff' and idade < 20:
        menormulher += 1

médiaidade = somaidade / 4

print('')
print(f'''A média de idade do grupo é de {médiaidade} anos
O homem mais velho tem {maioridadehomem} anos e se chama {nomevelho}.
Ao todo são {menormulher} mulher(s) com menos de 20 anos.''')