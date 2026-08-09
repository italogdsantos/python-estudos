import random
y = random.randrange(1,11,1)
print(y)
x = int(input('Tente acertar um número que pensei de 1 a 10: '))
cont = 0
while x != y:
    if x < y:
        print('É maior que isso!')  
    elif x > y:
        print('É menor que isso!')
    x = int(input('Você errou! Tente outra vez: '))
    cont += 1

print(f'Parabéns! Você precisou de {cont} tentativas para acertar.')
