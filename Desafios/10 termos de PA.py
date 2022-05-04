print('=' * 25)
print('10 Termos de uma PA')
print('=' * 25)

termo = int(input('Primeiro termo: '))
razão = int(input('Razão:'))
decimo = termo + (10 - 1) * razão

print('')
for numero in range(termo, decimo+razão, razão):
    print(numero, end=' -> ')
print('Acabou!')