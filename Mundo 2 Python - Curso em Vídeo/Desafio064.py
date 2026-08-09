x = int(input('Digite um valor (Digite 999 para parar): '))
cont = 0
y = x
while x != 999:
    cont += 1
    x = int(input('Digite um valor (Digite 999 para parar): '))
    y += x
print(f'Você digitou {cont} números, a soma entre eles é {y - 999}.')
