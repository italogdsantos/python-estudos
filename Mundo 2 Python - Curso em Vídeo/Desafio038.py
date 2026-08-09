x = int(input('Digite um valor inteiro '))
y = int(input('Digite outro valor inteiro '))
if x > y:
    print('{} é maior que {}.'.format(x,y))
elif y > x:
    print('{} é maior que {}.'.format(y,x))
elif x == y:
     print('{} e {} são iguais.'.format(x, y))
