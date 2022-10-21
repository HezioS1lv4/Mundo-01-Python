import math
print('===Desafio 018===')

angulo = float(input('Digite o ângulo que você deseja: '))

# math.sin é para calcular seno
# math.cos para calcular cosseno
# math.tan para calcular tangente
# math.radians serve para transformar o angulo de X graus° para radianos

print('O ângulo de {} tem o SENO de {:.2f}'.format(angulo, math.sin(math.radians(angulo))))
print('O ângulo de {} tem o COSSENO de {:.2f}'.format(angulo, math.cos(math.radians(angulo))))
print('O ângulo de {} tem o TANGENTE de {:.2f}'.format(angulo, math.tan(math.radians(angulo))))
