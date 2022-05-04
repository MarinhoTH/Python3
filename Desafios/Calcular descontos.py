preço = float(input('Qual o preço do produto? R$'))
desconto = int(input('De quanto será o desconto em %?'))
descontoporcento = (preço/100) * desconto
valor = preço - descontoporcento

print(f'O produto que custava R${preço:.2f}, com {desconto}% de desconto vai custar R${valor:.2f}.')