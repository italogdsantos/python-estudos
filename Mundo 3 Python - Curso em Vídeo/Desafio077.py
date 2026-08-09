coisas = ('Casa','Carro','Moto','Televisao','Sofa')
for p in coisas:
    print(f'\nNa palavra {p.upper()} temos ', end='')
    for letra in p:
        if letra.lower() in 'aeiou':
            print(letra, end=' ')