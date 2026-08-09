print(40*'=')
print(f'{"LISTAGEM DE PREÇOS":^40}')
print(40*'=')
lista = ('Notebook', 4399,
         'Mouse', 299,
         'Teclado', 499,
         'Monitor', 1299,
         'Mem. RAM', 599,
         'SSD 1TB', 399)
for pos in range(0, len(lista)):
    if pos % 2 == 0:
        print(f'{lista[pos]:.<30}', end='')
    else:
        print(f'R${lista[pos]:>7.2f}')
print(40*'=')