núm = int(input('Digite um número: '))
div = 0
for n in range(1,núm+1):
    if núm % n == 0:
        print('\033[34m', end='')
        div += 1
    else:
        print('\033[m', end='')
    print(f'{n}', end= ' ')
print(f'\n\033[mO número {núm} foi divisível {div} vezes.')
if div == 2:
    print('Por isso ele é primo.')
else:
    print('Por isso ele não é primo.')