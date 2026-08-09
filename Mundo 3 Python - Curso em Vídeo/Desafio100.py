from random import randint


def sorteio(lista):
    print('Sorteando 5 valores: ', end='')
    for cont in range(0,5):
        n = randint(1,10)
        lista.append(n)
        print(f'{n} ', end='')
    print()
    print('Pronto!')

def somaPar(lista):
    soma = 0
    for i in lista:
        if i % 2 == 0:
            soma += i
    print(f'A soma de todos os números de {lista} pares é: {soma}')


num = []
sorteio(num)
somaPar(num)
