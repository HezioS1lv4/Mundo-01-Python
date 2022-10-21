print('===Exercício 04===')
info = input('Digite algo para o exercício: ')

print('O tipo primitivo desse valor é', type(info))
# isspace serve para verificarmos se no obj escrito possui somente espaço em branco
print('Só tem espaços?', info.isspace())
# isnumeric serve para verificarmos se o valor escrito é numérico (int)
print('É um número? ', info.isnumeric())
# isalpha serve para verificarmos se o valor escrito é alfabético
print('É alfabético? ', info.isalpha())
print('É alfanumérico? ', info.isalnum())
# isupper verifica se o texto digitado está tudo maiúsculo
print('Ésta em maiúsculas? ', info.isupper())
# islower verifica se o texto digitado está tudo minuscúlo
print('Ésta em miniscúlas? ', info.islower())
# istitle verifica se o texto digitado está com as iníciais maíusculas
print('Ésta capitalizada? ', info.istitle())
