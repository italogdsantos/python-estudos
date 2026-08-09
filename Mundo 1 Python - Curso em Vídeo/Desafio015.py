x = int(input('Por quantos dias o carro foi alugado? '))
y = float(input('Quantos quilometros rodados? '))
d = x*60
km = y*0.15
print('Você deve R${} pelos dias e R${} pelos kms, gerando um total de R${}'.format(d,km,d+km))