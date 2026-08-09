x = float(input('Qual o salário do funcionário? '))
if x > 1380.00:
    print('O novo valor do salário é: R${:.2f}'.format(x*1.1))
else:
    print('O novo valor do salário é: R${:.2f}'.format(x*1.15))