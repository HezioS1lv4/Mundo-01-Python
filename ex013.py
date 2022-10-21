print('===Desafio 013===')

salario = float(input('Qual o salário do Funcionário? R$'))
novo = salario + (salario*15/100)

print('Um funcionário que ganhava R${}, com 15% de aumento, passa a receber R${:.2f}'.format(salario, novo))


# pagando a vista com 5% de desconto, parcelado com 5% de aumento
valor = float(input('Qual o valor: '))
vista = valor - (valor*5/100)
parcelado = valor + (valor*5/100)
print('A vista você ira pagar R${}, Parcelado R${}'.format(vista, parcelado))
