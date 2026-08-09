x = y = z = 0
while True:
    x = int(input('Digite um número (999 para parar): '))
    if x == 999:
        break
    z += x
    y += 1
print(f'Você digitou {y} números, sua soma é {z}.')