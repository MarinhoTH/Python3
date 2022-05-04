from math import sin, cos, tan, radians, trunc, sqrt, hypot

angulo = float(input('Digite um ângulo: '))
seno = sin(radians(angulo))
cosseno = cos(radians(angulo))
tangente = tan(radians(angulo))

print(f'O seno desse ângulo é {seno:.2f}, o cosseno é {cosseno:.2f} e a tangente é {tangente:.2f}')

num = int(input('Digite um Número: '))
raiz = sqrt(num)

print(f'A raiz de {num} é {trunc(raiz)}')

oposto = float(input('Comprimento do cateto oposto: '))
adjacente = float(input('Comprimento do cateto adjacente: '))
hipotenusa = hypot(oposto, adjacente)

print(f'O comprimento da hipotenusa é {hipotenusa:.2f}.')