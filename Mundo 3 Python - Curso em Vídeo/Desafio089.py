ficha = []
while True:
    nome = str(input('Digite o nome: '))
    nota1 = float(input('Digite a 1ª nota: '))
    nota2 = float(input('Digite a 2ª nota: '))
    media = (nota1 + nota2) / 2
    ficha.append([nome, [nota1, nota2], media])
    resp = str(input('Quer continuar? [S/N] ')).upper().strip()
    if resp in 'N':
        break
print(30*'-=')
print(f'{"Nº":<4}{"NOME":<10}{"MÉDIA":>8}')
for i, a in enumerate(ficha):
    print(f'{i:<4}{a[0]:<10}{a[2]:>8.1f}')
while True:
    opc = int(input('Mostrar as notas de qual aluno? (999 para parar) '))
    if opc == 999:
        break
    if opc <= len(ficha) - 1:
        print(25*'-=')
        print(f'As notas de {ficha[opc][0]} são {ficha[opc][1]}.')
        print(25 * '-=')
print('FINALIZANDO...')