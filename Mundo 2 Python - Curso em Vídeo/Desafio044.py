print(16*'=','Lojas Santos',16*'=')
x = float(input('Digite o valor da compra: R$ '))
y = int(input('Qual a forma de pagamento?\n[ 1 ] Dinheiro à vista\n[ 2 ] Cartão à vista\n[ 3 ] 2x no cartão\n[ 4 ] 3x ou mais no cartão\nQual é a sua opção? '))
if y == 1:
    print('Sua compra de R${:.2f} terá um valor final de R${:.f2}.'.format(x,x*0.90))
elif y == 2:
    print('Sua compra de R${:.2f} terá valor final de R${:.f2}.'.format(x,x))
elif y == 3:
    print('Sua compra de R${:.2f} terá 2 parcelas de R${:.2f} cada.'.format(x,(x*1.03)/2))
elif y == 4:
    z = int(input('Quantas parcelas? '))
    a = 1.04**z
    print('Sua compra de R${:.2f} terá {} parcelas de R${:.2f} cada.'.format(x,z,(a*x)/z))
