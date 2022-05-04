
mais18 = homens = mulheres = 0

while True:
    print('-' * 40)
    print('CADASTRE UMA PESSOA')
    print('-' * 40)
    idade = int(input('Idade: '))
    if idade >= 18:
            mais18 += 1
    sexo = str(input('Sexo: [M/F]'))
    if sexo in 'Mm':
        homens += 1
    if sexo in 'Ff' and idade < 20:
        mulheres += 1
    resposta = str(input('Quer continuar? [S/N]')).strip().upper()
    
    if resposta in 'Nn':
        break



print(f''' Total de pessoas com mais de 18 anos: {mais18}
Ao todo temos {homens} homem cadastrados
E temos {mulheres} mulheres com menos de 20 anos.''')