print('===Desafio 015===')
dias = int(input('Quantos dias alugados? '))
km = float(input('Quantos Km rodados? '))

total = (60 * dias) + (0.15 * km)

print('O total a pagar é de R${}'.format(total))