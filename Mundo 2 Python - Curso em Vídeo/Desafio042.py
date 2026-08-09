x = float(input('Digite um segmento: '))
y = float(input('Digite outro segmento: '))
z = float(input('Digite um outro segmento: '))
if x < y + z and y < x+ z and z < x + y:
    print('As retas podem formar um triângulo!')
    if x == y == z:
        print('Os segmentos {}, {} e {} formam um triângulo equilátero.'.format(x, y, z))
    elif x == y and x != z:
        print('Os segmentos {}, {} e {} formam um triângulo isósceles.'.format(x, y, z))
    elif x == z and x != y:
        print('Os segmentos {}, {} e {} formam um triângulo isósceles.'.format(x, y, z))
    elif x != y != z != x:
        print('Os segmentos {}, {} e {} formam um triângulo escaleno.'.format(x, y, z))
else:
    print('As retas não podem formar um triâmgulo.')

