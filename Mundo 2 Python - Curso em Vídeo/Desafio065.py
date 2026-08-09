x = y = a = b = c = 0
z = 'S'
while z != 'N':
    x = float(input('Digite um número: '))
    y += 1
    z = str(input('Você deseja continuar?[S/N] ')).upper().strip()[0]
    c += x
    if y == 1:
        b = c = x
    else:
        if x > a:
            a = x
        if x < b:
            b = x
print(f'Você digitou {y} números, sua soma é {c} e sua média é {x/y}.')
print(f'O maior número foi {a} e o menor número foi {b}.')