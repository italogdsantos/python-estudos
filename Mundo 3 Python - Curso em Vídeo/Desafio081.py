lista = []
while True:
    lista.append(int(input('Digite um valor: ')))
    continuar = str(input('Você deseja continuar? [S/N] ')).upper()
    if continuar in 'N':
        break
print(30*'=-')
lista.sort(reverse=True)
print(f'Você digitou {len(lista)} valores na lista.')
print(f'Os valores que você digitou em ordem decrescente: {lista}')
if 5 in lista:
    print('O valor 5 foi encontrado na lista.')
else:
    print(f'O valor 5 não foi encontrado na lista.')