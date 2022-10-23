print('===Desafio 029===')

v = int(input('Em qual velocidade estava o seu veículo? '))

if v > 80:
    m = 7 * (v - 80)
    print('Você foi multado! E o valor da multa a se pagar é R${}'.format(m))
else:
    print('Você não foi multado!')