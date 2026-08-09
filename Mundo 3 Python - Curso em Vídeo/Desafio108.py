from des108 import contas

num = float(input('Digite um valor: R$'))
print(f'A metade de {contas.moeda(num)} é: {contas.moeda(contas.metade(num))}')
print(f'O dobro de {contas.moeda(num)} é: {contas.moeda(contas.dobro(num))}')
print(f'Aumentando {contas.moeda(num)} em 10%, temos {contas.moeda(contas.aumentar(num, 10))}')
print(f'Diminuindo {contas.moeda(num)} em 15%, temos {contas.moeda(contas.diminuir(num, 15))}')