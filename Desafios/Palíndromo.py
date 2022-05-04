frase = str(input('Digite uma frase: ')).strip() .upper()

separado = frase.split()
junto = ''.join(separado)

inverso = ''

for letra in range(len(junto) -1, -1, -1):
    inverso += junto[letra]

print('')
if inverso == junto:
    print('Bingo')
else: 
    print('Not')