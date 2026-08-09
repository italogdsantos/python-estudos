x = int(input('Digite um ano qualquer: '))
if x == 0 and x % 100 != 0 or x % 400 == 0:
    print('O ano {} é um ano bissexto.'.format(x))
else:
    print('O ano {} não é um ano bissexto.'.format(x))
