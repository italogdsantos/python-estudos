def fatorial(n, show=False):
    """"
    -> Caclula o fatorial de um número.
    :param n: O número a ser calculado.
    :param show: (opcional) Mostrar ou não o cálculo.
    :return: Mostra o valor do fatorial n.
    """
    y = n
    z = 1
    print(f'Calculando {n}! = ', end='')
    while y > 0:
        if show:
            print(f'{y}', end='')
            print(f' x ' if y > 1 else ' = ', end='')
        z *= y
        y -= 1
    return z

while True:
    x = int(input('Digite um valor para calcular o fatorial: '))
    conta = str(input('Você quer mostrar a conta? [S/N] ')).strip().upper()
    while conta not in 'SN':
        print('Resposta inválida, digite novamente!')
        conta = str(input('Você quer mostrar a conta? [S/N] ')).strip().upper()
    if conta in 'S':
        print(fatorial(x, show=True))
    if conta in 'N':
        print(fatorial(x, show=False))
    resp = str(input('Quer calcular outro fatorial? [S/N] ')).strip().upper()
    while resp not in 'SN':
        print('Resposta inválida, digite novamente!')
        resp = str(input('Quer calcular outro fatorial? [S/N] ')).strip().upper()
    if resp in 'N':
        break
print('Até a próxima!')