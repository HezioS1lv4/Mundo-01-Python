# fatiamento de strings

frase = '        fodaseeeeeeeeeeeeee  Coi soi       '

# .count vai contar quantas vezes o elemento aparece na frase inserida
frase.count('o')
# .find ele procura dentro da frase se existe o elento citado e indica sua posição no indice, caso ñ exista ele imprime o valor -1
print(frase.find('claro'))
# .replace substitui o termo existente, pelo novo termo
frase.replace('fodas', 'tonenai')
# .upper transforma todos os valores em maiúsculos
frase.upper()
# .lower transforma todos os valroes em minúsculos
frase.lower()
# .capitalize transforma a primeira letra em maiúscula e o resto da str em minúscula
print(frase.capitalize())
# .title transforma todas as primeiras letras em maiúsculas
print(frase.title())
# .strip retorna todo o texto inserido deletando espaços em branco no início e no final
print(frase.strip())
# .rstrip deleta somente o lado direito(right)
frase.rstrip()
# .lstrip deleta somente o lado esquerdo(left)
frase.lstrip()
# .split separa todas as frases e as transforma em indíces. alimentados por ''
print(frase.split())
# .join a informação dentro dos '' será atribuido para todos os campos da str, preenchendo lado a lado cada elemento
print('-'.join(frase))

