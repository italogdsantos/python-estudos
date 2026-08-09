from random import randint
x = ('Pedra','Papel','Tesoura')
y = randint(0,2)
print('''Suas opções:
[ 0 ] Pedra
[ 1 ] Papel
[ 2 ] Tesoura''')
z = int(input('Qual a sua jogada? '))
print('O computador jogou {}.'.format(x[y]))
print('O jogador jogou {}.'.format(x[z]))
if y == 0:
    if z == 0: #PEDRA
        print('EMPATE!')
    elif z == 1:
        print('Parabéns, você venceu!')
    elif z == 2:
        print('O computador venceu, jogue novamente.')
    else:
        print('Jogada inválida!')
elif y == 1: #PAPEL
    if z == 0:
        print('O computador venceu, jogue novamente.')
    elif z == 1:
        print('EMPATE!')
    elif z == 2:
        print('Parabéns, você venceu!')
    else:
        print('Jogada inválida!')
elif y == 2: #TESOURA
    if z == 0:
        print('Parabéns, você venceu!')
    elif z == 1:
        print('O computador venceu, jogue novamente.')
    elif z == 2:
        print('EMPATE!')
    else:
        print('Jogada inválida!')