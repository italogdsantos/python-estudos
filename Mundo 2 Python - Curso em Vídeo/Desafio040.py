x = float(input('Digite sua primeira nota: '))
y = float(input('Digite sua segunda nota: '))
z = (x+y)/2
if z >= 7.0:
    print('Sua média foi {}. Parabéns, você está APROVADO!'.format(z))
elif z < 7.0 and z > 5.0:
    print('Sua média foi {}. Estude mais, você está de RECUPERAÇÃO!'.format(z))
else:
    print('Sua média foi {}. Você está REPROVADO!'.format(z))