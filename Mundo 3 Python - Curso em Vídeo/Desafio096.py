def area(larg, comp):
    a = larg * comp
    print(f'A área  de um terreno dimessionado {larg:.2f}m X {comp:.2f}m é {a:.2f}m².')


print('  Controle de terrenos  ')
print(25*'-')
x = float(input('Digite a largura do terreno (m): '))
y = float(input('Digite o comprimento do terreno (m): '))
area(x,y)
