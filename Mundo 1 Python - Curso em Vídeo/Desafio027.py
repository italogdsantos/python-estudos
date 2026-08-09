x = str(input('Digite o seu nome completo: ')).strip()
y = x.split()
print('Seu primeiro nome é: {}.'.format(y[0]))
print('Seu último nome é: {}.'.format(y[-1]))
