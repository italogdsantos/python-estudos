matriz = [[],[],[]]
num = pares = terceira = 0
for n in range(0,3):
    num = int(input(f'Digite um número para (0,{n}): '))
    matriz[0].append(num)
    if num % 2 == 0:
        pares += num
    if n == 2:
        terceira += num
for n in range(0,3):
    num = int(input(f'Digite um número para (1,{n}): '))
    matriz[1].append(num)   
    if num % 2 == 0:
        pares += num
    if n == 2:
            terceira += num
for n in range(0,3):
    num = int(input(f'Digite um número para (2,{n}): '))
    matriz[2].append(num)
    if num % 2 == 0:
        pares += num
    if n == 2:
        terceira += num
print(30*'-=')
print(f'{matriz[0]}')
print(f'{matriz[1]}')
print(f'{matriz[2]}')
print(30*'-=')
print(f'A soma de todos os valores pares é: {pares}')
print(f'A soma de dos valores da terceira coluna é: {terceira}')
print(f'O maior valor da segunda linha é: {max(matriz[1])}')
