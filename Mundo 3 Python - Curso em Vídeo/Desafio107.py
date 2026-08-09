from des107 import contas

num = float(input('Digite um valor: R$'))
print(f'A metade de {num} é: R${contas.metade(num)}')
print(f'O dobro de {num} é: R${contas.dobro(num)}')
print(f'Aumentando {num} em 10%, temos R${contas.aumentar(num, 10)}')
print(f'Diminuindo {num} em 15%, temos R${contas.diminuir(num, 15)}')