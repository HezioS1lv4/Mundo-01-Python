print('===Desafio033===')

num1 = int(input('Primeiro valor: '))
num2 = int(input('Segundo valor: '))
num3 = int(input('Terceiro valor: '))

menor = num1
if num2 < num1 and num2 < num3:
    menor = num2
if num3 < num1 and num3 < num2:
    menor = num3
# verificando a menor ^, o maior v
maior = num1
if num2 > num1 and num2 > num3:
    maior = num2
if num3 > num1 and num3 > num2:
    maior= num3

print('O menor valor diditado é {}'.format(menor))
print('O maior valor digitado é {}'.format(maior))
