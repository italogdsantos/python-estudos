print(20*'=')
print('20 TERMOS DE PA')
print(20*'=')
primeiro = int(input('Digite o primeiro termo de sua PA: '))
razao = int(input('Digite a razão da sua PA: '))
termo = primeiro
cont = 1
mais = 10
total = 0
while mais != 0:
    total = total + mais
    while cont <= total:
        print(f'{termo} -> ', end='')
        termo += razao
        cont += 1
    print('PAUSA')
    mais = int(input('Quantos termos você deseja ver a mais? '))
print(f'Progressão finalizada com {total} termos. ')