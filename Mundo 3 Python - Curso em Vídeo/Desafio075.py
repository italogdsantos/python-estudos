num = (int(input('Digite um número: ')),
       int(input('Digite um número: ')),
       int(input('Digite um número: ')),
       int(input('Digite um número: ')),
       int(input('Digite um número: ')),)
cont = 0
for n in num:
       if n % 2 == 0:
              cont += 1
print(f'Você digitou: {num}')
print(f'O valor 9 apareceu {num.count(9)} vezes.')
if 3 in num:
       print(f'O valor 3 apareceu na posição {num.index(3)+1}.')
else:
       print('O valor 3 não foi digitado.')
print(f'Foram digitados {cont} números pares.')