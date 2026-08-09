x = 0
y = 0
for n in range(1,7):
    z = int(input(f'Digite um {n} valor: '))
    if z % 2 == 0:
        x = x + z
        y = y + 1
print(f'Você digitou {y} números pares, a soma entre eles é {x}.')