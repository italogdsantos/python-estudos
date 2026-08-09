from random import randrange
print(20*'-=')
print('VAMOS JOGAR PAR OU ÍMPAR?')
print(20*'=-')
cont = 0
while True:
    num_máq = randrange(0,11)
    num_hum =  int(input('Digite um valor: '))
    jogada = str(input('Par ou Ímpar?[P/I] ')).upper().strip()[0]
    soma = (num_hum + num_máq) % 2
    print(f'Você jogou {num_hum} e o computador jogou {num_máq}.', end='')
    print(' Deu PAR' if soma == 0 else ' Deu ÍMPAR')
    print(20 * '=-')
    if jogada in 'In':
        if soma == 1:
            cont += 1
            print('Você ganhou!')
            print(20 * '=-')
        else:
            break
    if jogada in 'Pp':
        if soma == 0:
            cont += 1
            print('Você ganhou!')
            print(20 * '=-')
        else:
            break
print('GAME OVER.')
print(f'Você venceu {cont} ', end='')
print('rodadas consecutivas.' if cont > 1 else 'rodada.')