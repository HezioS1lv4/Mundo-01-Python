print('===Desafio 022===')

nome = str(input('Digite seu nome completo: ')).strip()  # strip deleta espaços em branco no começo e final

print(nome.upper())
print(nome.lower())
print(len(nome) - nome.count(' '))
print(nome.find(' '))  # vai imprimir o índice que se encontra
# OU
separa = nome.split()
print(len(separa[0]))
