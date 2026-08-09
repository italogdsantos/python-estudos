todos = []
pessoa = {}
soma =  cont = 0
while True:
    pessoa.clear()
    cont += 1
    pessoa['nome'] = str(input('Digite o nome: ')).capitalize()
    while True:
        pessoa['sexo'] = str(input('Digite o sexo [F/M]: ')).upper()
        if pessoa['sexo'] in 'FM':
            break
        print('Inválido, tente novamente.')
    pessoa['idade'] = int(input('Digite a idade: '))
    soma += pessoa['idade']
    todos.append(pessoa.copy())
    while True:
        resp = str(input('Quer continuar? [S/N] ')).upper()
        if resp in 'SN':
            break
        print('Iválido, tente novamente.')
    if resp in 'N':
        break
media = soma / cont
print(30*'=-')
print(f'Ao todo temos {cont} pessoas cadastradas.')
print(f'A média de idade é {media:.2f}.')
print('As mulheres registradas foram: ', end='')
for i in todos:
    if i['sexo'] == 'F':
        print(f'{i["nome"]} ', end='')
print()
print('As pessoas com idade maior que a média foram: ', end='')
for p in todos:
    if p['idade'] > media:
        print(f'{p["nome"]} ', end='')
print()
print(30*'=-')