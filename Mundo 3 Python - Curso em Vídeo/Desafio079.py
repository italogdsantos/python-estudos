lista = []
while True:
    num = int(input('Digite um número: '))
    if num not in lista:
        lista.append(num)
        print('Valor adicionado com Sucesso!')
        continuar = str(input(('Quer continuar? [S/N] '))).upper()
    else:
        print('Valor duplicado, não adicionarei.')
    if continuar in 'N':
        break
lista.sort()
print(f'Você digitou os valores (em ordem numérica): {lista}')
