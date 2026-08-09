def ficha(nome, gol):
    if nome == '':
        nome = '<desconhecido>'
    if gol not in '0123456789' or gol == '':
        gol = '0'
    print(f'O jogador {nome} marcou {gol} gols.')

n = str(input('Nome do jogador: ')).strip()
g = str(input('Número de gols: ')).strip()
ficha(n,g)