from random import randint
quant = int(input('Quantos jogos você quer fazer? '))
num = cont = 0
jogo = []
for j in range(0,quant):
    while True:
        num = randint(1,60)
        if num not in jogo:
            jogo.append(num)
            cont += 1
        if cont == 6:
            cont = 0
            break
    jogo.sort()
    print(jogo)
    jogo.clear()