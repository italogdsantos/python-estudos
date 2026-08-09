print(30*'=')
print('{:^30}'.format('BANCO SANTOS'))
print(30*'=')
valor = float(input('Quanto você deseja sacar? R$'))
total = valor
ced = 100.00
totced = 0
while True:
    if total >= ced:
        total -= ced
        totced += 1
    else:
        if totced > 0:
            print(f'Total de {totced} cédulas de R${ced:.2f}')
        if ced == 100:
            ced = 50
            totced = 0
        if ced == 50:
            ced = 20
            totced = 0
        elif ced == 20:
            ced = 10
            totced = 0
        elif ced == 10:
            ced = 5
            totced = 0
        elif ced == 5:
            ced = 1
            totced = 0
        elif ced == 0.5:
            ced = 0.25
            totced = 0
        elif ced == 0.25:
            ced = 0.1
            totced = 0
        elif ced == 0.1:
            ced = 0.05
            totced = 0
        elif ced == 0.05:
            ced = 0.01
            totced = 0
        elif ced == 0.01:
            totced = 0
        if total == 0:
            break
print(30*'=')
