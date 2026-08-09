print('-='*15)
print('ANALISADOR DE TRIÂNGULOS')
print('-='*15)
x = float(input('Digite o valor de uma reta '))
y = float(input('Digite o valor de outra reta '))
z = float(input('Digite o valor de mais uma reta '))
if x < y + z and y < x+ z and z < x + y:
    print('As retas podem formar um triângulo!')
else:
    print('As retas não podem formar um triâmgulo.')