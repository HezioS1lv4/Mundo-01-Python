print('===Desafio 028!===')
import random
# from random import randint

pc = random.randint(1, 5)
# randint serve para escolher um numero aleatorio

num = int(input('De 1 a 5, qual numero o computador escolheu?! '))

if num == pc:
    print('Vencedor(a)!')
else:
    print('Perderdor(a)')
print('O número escolhido foi {}'.format(pc))
