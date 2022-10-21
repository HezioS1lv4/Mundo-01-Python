import math
# from math import trunc
print('===Desafio 016===')
num = float(input('Digite um numero: '))

# a funcionalidade trunc da biblioteca math serve para termos o valor inteiro de alto com pontos flutuantes
print('A porção inteira de {} é {}'.format(num, math.trunc(num)))

# Apenas o int() pode resolver nesse caso, sem precisar importar

