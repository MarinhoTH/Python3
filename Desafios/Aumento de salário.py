salario = float(input('Qual o salário do funcionário? R$'))
aumento10 = salario + salario * (10 / 100)
aumento15 = salario + salario * (15 / 100)
aumento = salario

if salario > 1250.00:  
    aumento = aumento10
if salario <= 1250.00:
    aumento = aumento15


print(f'Quem ganhava R${salario :.2f} passa a ganhar R${aumento :.2f} agora.')

