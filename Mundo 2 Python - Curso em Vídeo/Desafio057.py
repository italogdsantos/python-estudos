n = str(input('Digite seu sexo:[F/M] ')).strip().upper()[0]
while not n in 'MmFm':
    n = str(input('Dado inválido, digite seu sexo: [F/M] ')).strip().upper()[0]
print('Fim!')