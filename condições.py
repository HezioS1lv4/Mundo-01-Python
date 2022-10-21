#tempo = int(input('Quantos anos tem o seu carro? '))

#if tempo <= 3:  # se
#    print('Seu carro está novo!')
#else:  # senão
#    print('Seu carro está velho!')

#print('--FIM--')

#////////////////////////////////////////////////////

#nome = str(input('Qual o seu nome? '))
#if nome == 'Gustavo':  # o == serve para comparação, dando resultados booleanos na função inserida
#    print('Que nome lindo você tem!')
#else:
#    print('Seu nome é normal!')

n1 = float(input('1a nota: '))
n2 = float(input('2a nota: '))
m = (n1 + n2) / 2

print('A sua média foi {}'.format(m))
if m >= 6:
    print('Parabens!')
else:
    print('Estude mais!')