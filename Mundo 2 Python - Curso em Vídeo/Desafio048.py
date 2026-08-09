y = 0
z = 0

for x in range(1,500, 2):
    if x % 3 == 0:
        z = z + 1
        y = y + x
print('A soma dos {} números ímpares que são múltiplos de 3 entre de 1 até 500  é:{}'.format(z,y))
