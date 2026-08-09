boletim = {}
boletim['nome'] = str(input('Nome: '))
boletim['média'] = float(input(f'Média de {boletim["nome"]}: '))
if boletim['média'] >= 6:
    boletim['situação'] = 'Aprovado'
elif 4 <= boletim['média'] < 6:
    boletim['situação'] = 'Recuperação'
elif boletim['média'] < 4:
    boletim['situação'] = 'Reprovado'
for k,v in boletim.items():
    print(f'  -{k} é igual a {v}')