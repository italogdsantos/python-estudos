def metade(m=0):

    m /= 2
    return m


def dobro(d=0):
    d *= 2
    return d


def aumentar(a=0, p: float = 0):
    a *= (1 + (p / 100))
    return a


def diminuir(d=0, p: float = 0):
    d *= (1 - (p / 100))
    return d


def moeda(p=0, m='R$'):
    return f'{m}{p:.2f}'.replace('.', ',')

