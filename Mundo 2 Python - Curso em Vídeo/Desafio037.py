x = int(input('Digite um número inteiro: '))
print('''Escolha uma das bases para conversão: '
[1] Converter para BINÁRIO'
[2] Converter para OCTAL'
[3] Converter para HEXADECIMAL''')
z = int(input('Escolha sua opção: '))
if z == 1:
      print('{} convertido em BINÁRIO é igual a {}'.format(x,bin(x)[2:]))
elif z == 2:
      print('{} convertido em OCTAL é igual a {}'.format(x,oct(x)[2:]))
elif z == 3:
      print('{} convertido em HEXADECIMAL é igual a {}'.format(x, hex(x)[2:]))
else:
      print('\033[1;30;43mValor inválido! Tente novamente.\033[m')
