lista = []
num = 0
for n in range(0,5):
    num = int(input('Digite um valor: '))
    lista.append(num)
    lista.sort()
    if lista.index(num) == n:
        print(f'{num} foi adicionado ao final da lista.')
    else:
        print(f'{num} foi adicionado na posição {lista.index(num)}.')
print(f'Os valores digitados foram: {lista}')
