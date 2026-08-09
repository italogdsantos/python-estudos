def voto(nasc):
    from datetime import date
    ano_atual = date.today().year
    if ano_atual - nasc < 16:
        print(f'Com {ano_atual - nasc} anos você não pode votar.')
    if ano_atual - nasc >= 16 and ano_atual - nasc < 70 :
        print(f'Com {ano_atual - nasc} anos você é obrigado a votar.')
    if ano_atual - nasc >= 70:
        print(f'Com {ano_atual - nasc} anos você não é obrigado a votar.')


print(30*'-')
ano = int(input('Que ano você nasceu? '))
voto(ano)