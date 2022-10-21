# ANSI
# style: 0 none ; 1 bold ; 4 underline ; 7 negative
# text : 30 white ; 31 red ; 32 green ; 33 yellow ; 34 blue ; 35 purple; 36 light blue ; 37 grey
# back : 40 ao 47 (As ordens das cores se mantem)

#print('\033[0;30;41m teste')
#print('\033[4;33;44m teste')
#print('\033[1;35;43m teste')
#print('\033[30;42m teste')
#print('\033[m teste')
#print('\033[7;30m teste')

print('\033[7;29m Olá mundo!\033[m')

# chamando esse 7 na função pode ser trocado as cores para o inverso

a = 1
b = 3

print('Os valores são {}{}\033[m e \033[;35m{}\033[m!'.format('\033[;36m', a, b))
# se atentar ao uso das cores diretas ou com a utilização do {}