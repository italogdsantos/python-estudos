x = float(input('Digite seu peso em Kg:  '))
y = float(input('Digite sua altura em M: '))
z = x/(y**2)
if z < 18.5:
    print('Seu IMC é {:.2f}, você está abaixo do peso ideal.'.format(z))
elif z >= 18.5 and z < 25:
    print('Seu IMC é {:.2f}, você está no peso ideal.'.format(z))
elif z >= 25 and z < 30:
    print('Seu IMC é {:.2f}, você está com excesso de peso.'.format(z))
elif z >= 30 and z < 35:
    print('Seu IMC é {:.2f}, você está em obesidade classe I.'.format(z))
elif z >= 35 and z < 40:
    print('Seu IMC é {:.2f}, você está em obesidade classe II.'.format(z))
elif z >= 40:
    print('Seu IMC é {:.2f}, você está em obesidade classe III.'.format(z))
