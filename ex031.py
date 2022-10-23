print('==Desafio031===')

km = float(input('Qual da viagem distância em km? '))

if km <= 200:
    price = 0.50 * km
    print('O valor a se pagar pela distancia {} é de R${:.2f}'.format(km, price))
else:
    price = 0.45 * km
    print('O valor a se pagar pela distancia {} é de R${:.2f}'.format(km, price))

# Maneira simplificada de resolver o problema vvv
#   price = km * 0.50 if km <= 200 else km * 0.45