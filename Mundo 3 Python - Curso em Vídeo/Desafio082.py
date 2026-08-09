lista = []
lista_p = []
lista_i = []
num = 0
while True:
    num = (int(input('Digite um valor: ')))
    lista.append(num)
    continuar = str(input('Você deseja continuar?[S/N] ')).upper()
    if num % 2 == 0:
        lista_p.append(num)
    else:
        lista_i.append(num)
    if continuar in 'N':
        break
print(f'A lista completa é: {lista}')
print(f'A lista de pares é: {lista_p}')
print(f'A lista de ímpares é : {lista_i}')