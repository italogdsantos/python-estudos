from time import sleep

def contagem(inicio, fim, passo):
    print(45*'-')
    print(f'Contando de {inicio} de até {fim} de {passo} em {passo}.')
    print(45*'-')

    if passo < 0:
        passo *= -1
    if passo == 0:
        passo = 1
    if inicio < fim:
        if passo == 0:
            passo = 1
        cont = inicio
        while cont <= fim:
            sleep(0.3)
            print(f'{cont} ', end='')
            cont += passo
        print('FIM!')

    else:
        cont = inicio

        while cont >= fim:
            sleep(0.3)
            print(f'{cont} ', end='')
            cont -= passo
        print('FIM!')

contagem(0, 10, 1)
contagem(20, 10, 2)
print(45*'-')
ini = int(input('Início: '))
f = int(input('Fim:    '))
pas = int(input('Passo:  '))
contagem(ini, f, pas)