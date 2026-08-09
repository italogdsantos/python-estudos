import random
y = (random.randrange(0,5,1))
x = int(input('Advinhe um número entre 0 e 5 '))
if x == y:
    print('Parábens, você acertou o número aleatório!')
else:
    print('ERROU! O número escolhido pelo computador foi {}.'.format(y))
print('===FIM===')

