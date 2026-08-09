from math import radians,sin,cos,tan
x = float(input('Digite o valor de um ângulo em graus '))
cosseno  = cos(radians(x))
seno     = sin(radians(x))
tangente = tan(radians(x))
print('O cosseno desse ângulo é {:.3f}, o seno é {:.3f} e a tangente é {:.3f}' .format(cosseno,seno,tangente))