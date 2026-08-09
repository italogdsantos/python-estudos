maior = 0
menor = 0
for n in range(1,8):
    idade = int(input(f'Digite o ano em que a {n}ª nasceu: '))
    if idade <= 2005:
        maior += 1
    else:
        menor += 1
if maior == 1:
    print('Somente uma pessoa é maior de idade.')
    print('Também tivemos seis menores de idade')
elif maior == 0:
    print('Todas as pessoas são menores de idade')
elif maior == 7:
    print('Todas as pessoas são maiores de idade.')
else:
    print(f'{maior} pessoas são maiores de idade e {menor} pessoas são menores de idade.')
