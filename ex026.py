print('===Desafio 026===')

frase = str(input('Digite uma frase: ')).upper()

# count conta a quantidade da letra ou frase na variável
print('A letra A aparece {} na frase.'.format(frase.count('A')))

# find procura a letra na variável escolhida
print('A primeira letra A apareceu na posição {}'.format(frase.find('A')))

# rfind procura a letra específica de trás pra frente
print('A última letra A apareceu na posição {}'.format(frase.rfind('A')))
