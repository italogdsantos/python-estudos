x = int(input('Digite um número: '))
y = int(input('Digite outro número: '))
z = int(input('Digite mais um número: '))
maior = x
if y>z and y>x:
    maior = y
if z>y and z>x:
    maior = z
menor = x
if y<z and y<x:
    menor = y
if z<y and z<x:
    menor = z
print('O maior número é: {}'.format(maior))
print('O menor número é: {}'.format(menor))