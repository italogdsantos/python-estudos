print(20*'=')
print('20 TERMOS DE PA')
print(20*'=')
primeiro = int(input('Digite o primeiro termo de sua PA: '))
razao = int(input('Digite a razão da sua PA: '))
termo = primeiro
cont = 1
while cont <= 10:
    print(f'{termo}', end=' ')
    if cont <= 9:
        print('->', end=' ')
    else:
        print(end='')
    termo += razao
    cont += 1
print('FIM!!!')