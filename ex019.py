import random
# from random import choice

print('===Desafio 019===')

al1 = input('Primeiro aluno: ')
al2 = input('Segundo aluno: ')
al3 = input('Terceiro aluno: ')
al4 = input('Quarto aluno: ')
lista = [al1, al2, al3, al4]

# a função choice dentro de random serve para escolher um valor aleatório
print('O aluno escolhido foi {}'.format(random.choice(lista)))
