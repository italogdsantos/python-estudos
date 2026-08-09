sexo = ''
continuar = ''
cont_20f = cont_m = cont_i = idade = 0
while True:
    print(38*'-')
    print(8*' ','CADASTRE UMA PESSOA')
    print(38*'-')
    idade = int(input('IDADE: '))
    sexo = str(input('Sexo[M/F] ')).upper().strip()[0]
    if idade > 18:
        cont_i += 1
    if sexo in 'Ff':
        if idade < 20:
            cont_20f += 1
    if sexo in 'Mm':
        cont_m += 1
    continuar = str(input('Deseja continuar?[S/N] ')).upper().strip()[0]
    if continuar in 'Nn':
        break
print(f'Ao total temos {cont_i} pessoas com mais de 18 anos.')
print(f'Ao todo temos {cont_m} homens cadastrados.')
print(f'E temos {cont_20f} mulheres com menos de 20 anos de idade.')
