import math
x = float(input('Escreva o comprimento do cateto oposto em cm '))
y = float(input('Escreva o comprimento do cateto adjascente em cm '))
z = (math.pow(x,2))+(math.pow(y,2))
print('A hipotenusa mede {}cm'.format(math.sqrt(z)))