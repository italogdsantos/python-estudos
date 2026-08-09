jogador_stats = {}
jogador_stats['gols'] = []
jogador_stats['jogador'] =  str(input('Nome do jogador: '))
jogador_stats['jogos'] = int(input(f'Quantos jogos {jogador_stats["jogador"]} jogou? '))

for i in range(1, jogador_stats['jogos']+1):
    jogador_stats['gols'].append(int(input(f'   - Quantos gols {jogador_stats["jogador"]} marcou na {i}ª partida? ')))
print(30*'=-')
print(jogador_stats)
print(30*'=-')
for j, k in jogador_stats.items():
    print(f'O campo {j} tem valor {k}.')
print(30*'=-')
print(f'O jogador {jogador_stats["jogador"]} jogou {jogador_stats["jogos"]} jogos.')
for p, q in enumerate(jogador_stats['gols']):
    print(f'=> Na partida {p+1}, fez {q} gols.')
print(30*'=-')
print(f'Totalizando {sum(jogador_stats["gols"])} gols.')