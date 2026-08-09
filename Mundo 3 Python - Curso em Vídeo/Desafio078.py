lista = []
maior = 0
menor = 0
for n in range(0,5):
    lista.append(int(input(f'Digite um valor para a posição {n}: ')))
print(f'Você digitou os valores: {lista}')

print(f'O maior valor digitado foi: {max(lista)} na posição ', end='')
for x, y in enumerate(lista):
    if y == max(lista):
        print(f'{x}... ', end='')
print()
print(f'O menor valor digitado foi: {min(lista)} na posição ', end='')
for a, b in enumerate(lista):
    if b == min(lista):
        print(f'{a}... ', end='')
print()