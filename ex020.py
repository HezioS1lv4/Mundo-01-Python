print('===Desafio 020===')

# import random
from random import shuffle  # (embaralhar)

n1 = input('Primeiro aluno: ')
n2 = input('Segundo aluno: ')
n3 = input('Terceiro aluno: ')
n4 = input('Quarto aluno: ')
lista = [n1, n2, n3, n4]

# a função shuffle dentro de random serve para embaralhar a ordem nos itens na lista
shuffle(lista)

print('A ordem de apresentação será {}'.format(lista))
