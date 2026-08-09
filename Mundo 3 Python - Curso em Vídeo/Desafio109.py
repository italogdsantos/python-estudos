from des109 import contas

num = float(input('Digite um valor: R$'))
print(f'A metade de {contas.moeda(num)} é: {contas.metade(num, True)}')
print(f'O dobro de {contas.moeda(num)} é: {contas.dobro(num, True)}')
print(f'Aumentando {contas.moeda(num)} em 10%, temos {contas.aumentar(num, 10, True)}')
print(f'Diminuindo {contas.moeda(num)} em 15%, temos {contas.diminuir(num, 15, True)}')