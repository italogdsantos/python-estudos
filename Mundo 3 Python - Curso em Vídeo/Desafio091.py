from random import randint
from time import sleep
from operator import itemgetter
jogo = {'Jogaodor 1': randint(1,6),
        'Jogaodor 2': randint(1,6),
        'Jogaodor 3': randint(1,6),
        'Jogaodor 4': randint(1,6)}
ranking = {}
print('Valores sorteados: ')
for k, v in jogo.items():
        print(f'O {k} jogou {v}.')
        sleep(0.5)
ranking = sorted(jogo.items(), key=itemgetter(1), reverse=True)
for j, v in enumerate(ranking):
        print(f'{j+1}º lugar: {v[0]} com {v[1]}')
        sleep(0.5)