print('===Desafio 011===')

l = float(input('Qual a largura da parede: '))
a = float(input('Qual a altura: '))

area = l * a

print('Sua parede tem a dimensão de {}x{} e sua área é de {}m².'.format(l, a, area))

# para voce pintar uma area, você precisa calcular a quantidade de litro por area
tinta = area / 2
print('Para pintar essa parede, você precisará de {}L de tinta.'.format(tinta))