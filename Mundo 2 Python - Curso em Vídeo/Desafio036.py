print('=-'*15)
print('\033[1;33m Banco Santos Empréstimos \033[m')
print('=-'*15)
x = float(input('Qual o valor do imóvel que você quer comprar? R$'))
y = float(input('Qual o seu salário? R$'))
z = float(input('Em quantos anos você quer pagar? '))
a = z * 12
b = x / a
print('Para comprar uma casa de R${:.2f} em {:.0f} anos, a prestação será de R${:.2f}.'.format(x,z,b))
if b > y * 0.3:
    print('Empréstimo NEGADO!')
elif b <= y *0.3:
    print('Empréstimo APROVADO!')
print('Obrigado pela confiança.')

