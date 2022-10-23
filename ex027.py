print('===Desafio 027===')

frase = str(input('Digite seu nome completo: ')).strip()
nome = frase.split()
print('Prazer conhecer-lo(a)!')

print('Seu primeiro nome é {}'.format(nome[0]))
print('Seu último nome é {}'.format(nome[len(nome)-1]))
