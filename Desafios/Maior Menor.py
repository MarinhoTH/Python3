valor1 = int(input('Primeiro valor: '))
valor2 = int(input('Segundo valor: '))
valor3 = int(input('Terceiro valor: '))
menor = valor1
maior = valor1

if valor2 < valor1 and valor2 < valor3:
    menor = valor2
if valor3 <valor2 and valor3 < valor1:
    menor = valor3    


print(f'O menor valor digitado foi {menor}') 

if valor2 > valor1 and valor2 > valor3:
    maior = valor2
if valor3 > valor1 and valor3 > valor2:
    maior = valor3


print(f'O maior valor foi {maior}')