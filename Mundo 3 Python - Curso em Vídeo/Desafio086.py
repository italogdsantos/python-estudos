matriz = [[],[],[]]
for n in range(0,3):
    matriz[0].append(int(input(f'Digite um número para (0,{n}): ')))
for n in range(0,3):
    matriz[1].append(int(input(f'Digite um número para (1,{n}): ')))
for n in range(0,3):
    matriz[2].append(int(input(f'Digite um número para (2,{n}): ')))
print(f'{matriz[0]}')
print(f'{matriz[1]}')
print(f'{matriz[2]}')
