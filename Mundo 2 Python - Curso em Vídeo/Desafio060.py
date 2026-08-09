x = int(input('Digite um valor para calcular o fatorial: '))
y = x
z = 1
print(f'Calculando {x}! = ', end='')
while y > 0:
    print(f'{y}', end='')
    print(f' x ' if y > 1 else ' = ', end='')
    z *= y
    y -= 1
print(f'{z}')