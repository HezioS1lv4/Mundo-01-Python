import math
# from math import hypot

print('===Desafio 017===')
co = float(input('Comprimento do cateto oposto: '))
ca = float(input('Comprimento do cateto adjacente: '))
h = (co ** 2 + ca ** 2) ** (1/2)

print('A hipotenusa vai medir {:.2f}'.format(h))

# hypot serve para calcularmos a hipotenusa sem "trabalho braçal"
hi = math.hypot(co, ca)
print(hi)
