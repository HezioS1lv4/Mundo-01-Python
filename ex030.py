print('===Desafio 030===')

num = int(input('Me diga um numero qualquer: '))
resultado = num % 2
# modulo(%) 2  vai indo de 2 em até conseguir chegar no valor almejado
# se sobrar o número 1 vai ser impar, se sobrar 0 vai ser par

if resultado == 0:
    print('O seu número é PAR'.format(resultado))
else:
    print('O número é ÍMPAR'.format(resultado))