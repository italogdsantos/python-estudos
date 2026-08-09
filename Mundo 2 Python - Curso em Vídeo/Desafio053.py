frase = str(input("Digite uma frase: ")).strip().upper()
junto = frase.replace(' ','')
inverso = ''
for n in range(len(junto) -1, -1, -1):
    inverso += junto[n]
print(f'O inverso de {junto} é {inverso}')
if inverso == junto:
    print('O que você digitou é um palíndromo.')
else:
    print('O que você digitou não é um palíndromo.')