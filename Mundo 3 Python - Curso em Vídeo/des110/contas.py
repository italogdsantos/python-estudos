def moeda(p=0, m='R$'):
    return f'{m}{p:.2f}'.replace('.', ',')


def metade(m=0, f=False):

    m /= 2
    if f:
        return moeda(m)
    else:
        return m


def dobro(d=0, f=False):
    d *= 2
    if f:
        return moeda(d)
    else:
        return d


def aumentar(a=0, p: float = 0, f=False):
    a *= (1 + (p / 100))
    if f:
        return moeda(a)
    else:
        return a


def diminuir(d=0, p: float = 0, f=False):
    d *= (1 - (p / 100))
    if f:
        return moeda(d)
    else:
        return d

def resumo(v, a, d):
    print(20*"-=")
    print('RESUMO DO VALOR'.center(40))
    print(20 * "-=")
    print('Preço analisado:', end='')
    print(f'{moeda(v):^38}')
    print('Metade do preço:', end='')
    print(f'{metade(v, True):^38}')
    print('Dobro do preço: ', end='')
    print(f'{dobro(v, True):^38}')
    print(f'{a}% de aumento: ', end='')
    print(f'{aumentar(v, a, True):^38}')
    print(f'{d}% de redução: ', end='')
    print(f'{diminuir(v, d, True):^38}')
    print(20 * "-=")
