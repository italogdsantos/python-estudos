x = y = z = 0
while True:
    x = int(input('Você deseja ver a tabuada de que valor? '))
    if x < 0:
        break
    print(20*'-=')
    print(f'{x} x 1 = {x} \n{x} x 2 = {x*2} \n{x} x 3 = {x*3} \n{x} x 4 = {x*4} \n{x} x 5 = {x*5} \n{x} x 6 = {x*6} \n{x} x 7 = {x*7} \n{x} x 8 = {x*8} \n{x} x 9 = {x*9} \n{x} x 10 = {x*10}')
    print(20*'-=')
print('Programa Tabuada encerrado. Volte sempre!')