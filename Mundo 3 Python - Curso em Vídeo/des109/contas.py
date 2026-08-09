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

