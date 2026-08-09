x = int(input('Qual a distância da sua viagem (em km) ? '))
if x > 200:
    y = x * 0.45
    print('O valor da sua passagem será R${:.2f}.'.format(y))
else:
    y = x * 0.5
    print('O valor da sua passagem será R${:.2f}.'.format(y))
print('Obrigadp pela preferência!')