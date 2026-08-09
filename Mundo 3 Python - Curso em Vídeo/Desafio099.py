def maior(*x):
    print('Definindo valores: ')
    print(f'{x}, foram {len(x)} valores informados.')
    print(f'O maior valor foi {max(x)} e o menor foi {min(x)}.')

maior(1, 5, 8, 15, -4)