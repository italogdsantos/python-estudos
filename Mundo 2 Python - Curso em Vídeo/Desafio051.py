print(20*'=')
print('20 TERMOS DE PA')
print(20*'=')
primeiro = int(input('Digite o primeiro termo de sua PA: '))
razao = int(input('Digite a razão da sua PA: '))
for n in range(0,20):
    pa = primeiro + razao * n
    print(pa, end=' -> ')
print('Acabou!')
