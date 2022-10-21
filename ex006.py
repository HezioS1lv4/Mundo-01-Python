#import math
from math import sqrt

print('===Exercício 06===')
num = int(input('Digite um numero: '))
dob = num * 2
trip = num * 3
raiz = sqrt(num)
# OU
raiz = num ** (1/2)

print('O dobro de do valor inserido ({}) é de {}, o triplo: {} e sua raiz quadrada: {:.3f}'.format(num, dob, trip, raiz))

# caso o valor esteja muito grande, fazer controle(:.2f) na mascara sobre!
