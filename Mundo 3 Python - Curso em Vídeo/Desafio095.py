partidas = []
time = []
jogador_stats = {}
resp = 'S'
while True:
    jogador_stats.clear()
    jogador_stats['nome'] = str(input('Nome do jogador: '))
    jogador_stats['jogos'] = int(input(f'Quantos jogos {jogador_stats["nome"]} jogou? '))
    partidas.clear()
    for c in range(1, jogador_stats['jogos'] + 1):
        partidas.append(int(input(f'   -Quantos gols na partida {c}? ')))
    jogador_stats['gols'] = partidas[:]
    jogador_stats['total'] = sum(partidas)
    time.append(jogador_stats.copy())
    while True:
        resp = str(input('Quer continuar? [S/N] ')).upper()[0]
        if resp in 'SN':
            break
        print('Resposta inválida.')
    if resp == 'N':
        break
print(60*'-')
print('cod ', end=' ')
for i in jogador_stats.keys():
    print(f'{i:<15}', end='')
print()
print(60*'-')
for k, v in enumerate(time):
    print(f'{k+1}    ', end='')
    for d in v.values():
        print(f'{str(d):<15}', end='')
    print()
print(60*'-')
while True:
    busca = int(input('Mostrar os dados de qual jogador? (999 para parar) '))
    if busca == 999:
        break
    if busca > len(time) or busca <= 0:
        print(f'Erro! não existe jogador com código {busca}.')
    else:
        print(60 * '-')
        print(f'  LEVANTAMENTO DO JOGADOR {time[busca - 1]["nome"]}: ')
        for x, y in enumerate(time[busca - 1]['gols']):
            print(f'  No jogo {x+1}, fez {y} gols.')
        print(60 * '-')
print('VOLTE SEMPRE, OBRIGADO POR TESTAR.')