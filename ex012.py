print('===Desafio 012===')

price = float(input('Qual o preço do produto? R$'))
desconto = (price*5/100)
valor = price - desconto

print('O produto que custava R${}, na promoção com desconto de 5% vai custar R${:.2f}'.format(price, valor))

# OU
# valor = price - (price*5/100)
