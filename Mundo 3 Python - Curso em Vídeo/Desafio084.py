dado = []
lista = []
peso_maior = peso_menor = 0
pesado = []
leve = []
while True:
    dado.append(str(input('Digite um nome: ')))
    dado.append(float(input('Digite o peso: ')))
    lista.append(dado[:])
    dado.clear()
    continuar = str(input(('Você deseja continuar:[S/N] '))).upper()
    if continuar in 'N':
        break
for p in lista:
    if p[1] == peso_maior:
        pesado.append(p[0])
    if p[1] > peso_maior:
        peso_maior = p[1]
        pesado.clear()
        pesado.append(p[0])

peso_menor = float('inf')
for l in lista:
    if l[1] == peso_menor:
        leve.append(l[0])
    if l[1] < peso_menor:
        peso_menor = l[1]
        leve.clear()
        leve.append(l[0])

print(f'Foram cadastradas {len(lista)} pessoas.')
if len(pesado) > 1:
    print(f'As pessoas mais pesadas foram {pesado} com {peso_maior}Kg.')
else:
    print(f'A pessoa mais pesada foi {pesado} com {peso_maior}Kg.')
if len(leve) > 1:
    print(f'As pessoas mais leves foram {leve} com {peso_menor}Kg.')
else:
    print(f'A pessoa mais leve foi {leve} com {peso_menor}Kg.')