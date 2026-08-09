x = float(input('Qual a velocidade do carro (em km/h)? '))
if x > 80.0:
    y = (x-80.0)*7.00
    print('A velocidade permitda é 80km/h, você estava a {}km/h, sua multa custará R${:.2f}.'.format(x,y))
else:
    print('Você está na velocidade permitida.')
print('DIRIJA COM PRUDÊNCIA!')