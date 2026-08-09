x = float(input('Digite o primeiro valor: '))
y = float(input('Digite o  segundo valor: '))
z = int(input('''\r[1] Somar
              \r[2] Mutiplicar
              \r[3] Maior
              \r[4] Novos números
              
              \rQUAL A SUA OPÇÃO? '''))

while z != 5:
    if z == 1:
        print(f'A soma entre {x} e {y} é igual a: {x+y}')
    elif z == 2:
        print(f'A multiplicação entre {x} e {y} é igual a: {x*y}')
    elif z == 3:
        if x > y:
            print(f'{x} é maior que {y}.')
        elif x == y:
            print(f'{x} é igual a {y}.')
        elif x < y:
            print(f'{x} é menor que {y}.')
    if z == 4:
        x = float(input('Digite o primeiro valor: '))
        y = float(input('Digite o  segundo valor: '))
    else:
        print('Opção inválida, tente novamente.')
    z = int(input('''\r[1] Somar
                  \r[2] Mutiplicar
                  \r[3] Maior
                  \r[4] Novos números
                  \r[5] Fim do programa 
                  
                  \rQUAL A SUA OPÇÃO? '''))

print('FIM!!')